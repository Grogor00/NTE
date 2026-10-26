#!/usr/bin/env python3
"""Project the bracket mismatch onto dC/dp. Boosted shift degree. NumPy || Wolfram."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.linalg import lstsq, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_dCdp_Alpha_Factorization_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_dCdp_Alpha_Factorization_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261026)

spec = importlib.util.spec_from_file_location(
    "gammamat", HERE / "Opsi2_Gamma_Matrix_Coefficient_PARALLEL_CursorMain.py"
)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def flat(m):
    return np.asarray(m, dtype=complex).reshape(-1)


def project(target, cols):
    if not cols:
        return float(norm(flat(target))), flat(target)
    A = np.column_stack([flat(c) for c in cols])
    coef, *_ = lstsq(A, flat(target), rcond=None)
    resid = flat(target) - A @ coef
    return float(norm(resid)), resid


def dC_list(sf, p, gp):
    out = []
    for i in range(3):
        out.append(sf * (p[i] / gp) * g.I4 - sf * g.ALPHAS[i])
    return out


def one(sg, sf, p):
    C, gp = g.C_of(sg, sf, p)
    K = np.linalg.inv(C)
    k = 0
    M = (sg**2) * (g.ALPHAS[k] @ K @ g.ALPHAS[k])
    Delta = M - sg * g.I4
    dCs = dC_list(sf, p, gp)
    # finite-difference check of dC at a shifted p
    eps = 1e-6
    dp = p.copy()
    dp[0] += eps
    C2, _ = g.C_of(sg, sf, dp)
    dC_num = (C2 - C) / eps
    fd_err = float(norm(dC_num - dCs[0]))
    r_dC, _ = project(Delta, dCs)
    r_C, _ = project(M, [C])
    nD = float(norm(flat(Delta)))
    nM = float(norm(flat(M)))
    return dict(
        rel_dC=r_dC / max(nD, 1e-30),
        abs_dC=r_dC,
        rel_C=r_C / max(nM, 1e-30),
        abs_Delta=nD,
        fd_err=fd_err,
    )


def run_numpy(n=60):
    gen, zero, sf0 = [], [], []
    for _ in range(n):
        sg = float(RNG.uniform(0.4, 2.0))
        sf = float(RNG.uniform(0.4, 2.0))
        p = RNG.normal(size=3)
        if float(norm(p)) < 0.3:
            p = p / max(float(norm(p)), 1e-8) * 0.3
        gen.append(one(sg, sf, p))
        zero.append(one(sg, sf, np.zeros(3)))
        sf0.append(one(sg, 0.0, p))
    def col(rows, key):
        return np.array([r[key] for r in rows], dtype=float)
    return {
        "engine": "numpy",
        "n": n,
        "median_rel_resid_dCdp": float(np.median(col(gen, "rel_dC"))),
        "min_rel_resid_dCdp": float(np.min(col(gen, "rel_dC"))),
        "median_rel_resid_onto_C": float(np.median(col(gen, "rel_C"))),
        "min_rel_resid_onto_C": float(np.min(col(gen, "rel_C"))),
        "p0_median_rel_dCdp": float(np.median(col(zero, "rel_dC"))),
        "p0_min_rel_dCdp": float(np.min(col(zero, "rel_dC"))),
        "sf0_max_abs_Delta": float(np.max(col(sf0, "abs_Delta"))),
        "max_fd_err": float(np.max(col(gen, "fd_err"))),
        "escape_fails": bool(
            np.median(col(gen, "rel_dC")) > 1e-2
            and np.min(col(zero, "rel_dC")) > 1e-2
            and np.max(col(sf0, "abs_Delta")) < 1e-8
            and np.max(col(gen, "fd_err")) < 1e-6
        ),
    }


def run_factorization():
    Nmul, L, sg, sf = sp.symbols("N L sg sf", positive=True)
    px, py, pz = sp.symbols("px py pz", real=True)
    L1, L2, L3 = sp.symbols("L1 L2 L3")
    n1, n2, n3 = sp.symbols("n1 n2 n3")
    d1, d2, d3 = sp.symbols("Dn1 Dn2 Dn3")
    J1, J2, J3 = sp.symbols("J1 J2 J3")
    Li = sp.Matrix([L1, L2, L3])
    n = sp.Matrix([n1, n2, n3])
    Dn = sp.Matrix([d1, d2, d3])
    J = sp.Matrix([J1, J2, J3])
    p = sp.Matrix([px, py, pz])
    gp = sp.sqrt(1 + (p.dot(p)))
    # boosted f leg depends on p, not on the multipliers
    Ng = Li + L * n + Nmul * Dn
    Nf = Li + L * n
    H = sp.expand(sg * Ng.dot(J) + sf * gp * Nf.dot(J))
    mult = [Nmul, L, L1, L2, L3]
    num, den = sp.fraction(sp.together(H))
    nd = int(sp.total_degree(sp.Poly(sp.expand(num), *mult)))
    dd = int(sp.total_degree(sp.Poly(sp.expand(den), *mult)))
    Hs = (Ng.dot(J)) ** 2 / Nmul
    n2s, d2s = sp.fraction(sp.together(sp.expand(Hs)))
    nds = int(sp.total_degree(sp.Poly(sp.expand(n2s), *mult)))
    dds = int(sp.total_degree(sp.Poly(sp.expand(d2s), *mult)))
    return {
        "dirac_num_degree": nd,
        "dirac_den_degree": dd,
        "dirac_linear": bool(nd <= 1 and dd == 0),
        "scalar_num_degree": nds,
        "scalar_den_degree": dds,
        "scalar_linear": bool(nds <= 1 and dds == 0),
        "p_not_a_multiplier": True,
        "factorization_holds": bool(nd <= 1 and dd == 0 and not (nds <= 1 and dds == 0)),
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_dCdp_Alpha_Factorization_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": (proc.stderr or "")[-800:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(3) as ex:
        a = ex.submit(run_numpy)
        b = ex.submit(run_factorization)
        c = ex.submit(run_wolfram)
        ny, fac, wl = a.result(), b.result(), c.result()
    wls = wl.get("summary") or {}
    both = bool(ny.get("escape_fails") and wls.get("escape_fails"))
    out = {"numpy": ny, "sympy_factorization": fac, "wolfram": wl, "both_escape_fails": both}
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "numpy_escape_fails": ny.get("escape_fails"),
        "numpy_median_rel": ny.get("median_rel_resid_dCdp"),
        "numpy_p0": ny.get("p0_min_rel_dCdp"),
        "numpy_onto_C": ny.get("median_rel_resid_onto_C"),
        "factorization": fac.get("factorization_holds"),
        "wolfram_escape": wls.get("escape_fails"),
        "wolfram_median": wls.get("median_rel_resid_dCdp"),
        "both": both,
    }, indent=2))


if __name__ == "__main__":
    main()
