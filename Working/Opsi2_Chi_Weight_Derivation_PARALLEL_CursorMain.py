#!/usr/bin/env python3
"""Derive {E,E}_D from the constraint matrix. Do not insert Sigma_g^2/Sigma.

Prereg: Opsi2_Chi_Weight_Derivation_PREREGISTRATION_CursorMain_20261022.md
"""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_Chi_Weight_Derivation_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_Chi_Weight_Derivation_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261022)
N = 6


def make_J(n):
    dim = 4 * n
    J = np.zeros((dim, dim))
    for i in range(n):
        J[i, 2 * n + i] = 1.0
        J[2 * n + i, i] = -1.0
        J[n + i, 3 * n + i] = 1.0
        J[3 * n + i, n + i] = -1.0
    return J


JMAT = make_J(N)


def constraint_grads(sigma):
    grads = []
    for i in range(N):
        g = np.zeros(4 * N)
        g[2 * N + i] = 1.0
        grads.append(g)
    for i in range(N):
        g = np.zeros(4 * N)
        g[3 * N + i] = 1.0
        g[i] = -sigma
        grads.append(g)
    return grads


def grad_E(i, u, v, sg, omega):
    g = np.zeros(4 * N)
    ip, im = (i + 1) % N, (i - 1) % N
    dv = 0.5 * (v[ip] - v[im]) + omega[i] * v[i]
    g[i] = sg * dv
    g[N + ip] += sg * u[i] * 0.5
    g[N + im] += sg * u[i] * (-0.5)
    g[N + i] += sg * u[i] * omega[i]
    return g


def dirac_block(u, v, omega, sg, sigma):
    gchi = constraint_grads(sigma)
    C = np.array([[ga @ JMAT @ gb for gb in gchi] for ga in gchi])
    Cinv = inv(C)
    gE = [grad_E(i, u, v, sg, omega) for i in range(N)]
    # {E_i, chi_a} and {chi_b, E_j}
    Ech = np.array([[ge @ JMAT @ gc for gc in gchi] for ge in gE])
    chE = np.array([[gc @ JMAT @ ge for gc in gchi] for ge in gE]).T
    poisson = np.array([[ga @ JMAT @ gb for gb in gE] for ga in gE])
    dirac = poisson - Ech @ Cinv @ chE
    return dirac, C


def alpha_of(meas, unit):
    m = meas.ravel()
    u = unit.ravel()
    den = float(u @ u)
    if den < 1e-18:
        return None
    return float(m @ u / den)


def run_numpy(n_trial=40):
    rows = []
    c_entry_err = []
    poisson_max = []
    omega_shift = []
    for _ in range(n_trial):
        u = RNG.normal(size=N)
        v = RNG.normal(size=N)
        omega = 0.5 * RNG.normal(size=N)
        sg = float(RNG.uniform(0.4, 2.0))
        sf = float(RNG.uniform(0.4, 2.0))
        sigma = sg + sf
        unit, _ = dirac_block(u, v, omega, 1.0, 1.0)
        meas, C = dirac_block(u, v, omega, sg, sigma)
        bare, _ = dirac_block(u, v, np.zeros(N), sg, sigma)
        a = alpha_of(meas, unit)
        a_bare = alpha_of(bare, dirac_block(u, v, np.zeros(N), 1.0, 1.0)[0])
        if a is None or a_bare is None:
            continue
        # C[0, N] should be {chi^u_0, chi^v_0} = Sigma
        c_entry_err.append(abs(C[0, N] - sigma))
        poisson_max.append(float(np.max(np.abs(dirac_block(u, v, omega, sg, sigma)[0] * 0))))
        # unreduced Poisson of two E's is measured inside dirac_block; recompute
        gE = [grad_E(i, u, v, sg, omega) for i in range(N)]
        P0 = np.array([[ga @ JMAT @ gb for gb in gE] for ga in gE])
        poisson_max[-1] = float(np.max(np.abs(P0)))
        omega_shift.append(abs(a - a_bare))
        k5, _ = dirac_block(u, v, omega, sf, sigma)
        a5 = alpha_of(k5, unit)
        sf0, _ = dirac_block(u, v, omega, sg, sg)
        a0 = alpha_of(sf0, unit)
        rows.append(
            dict(
                alpha=a,
                pred=sg**2 / sigma,
                sg=sg,
                sigma=sigma,
                theta=sg / sigma,
                theta2=(sg / sigma) ** 2,
                err=abs(a - sg**2 / sigma),
                sep_sg=abs(a - sg),
                sep_sigma=abs(a - sigma),
                sep_theta=abs(a - sg / sigma),
                k5_err=abs(a5 - sf**2 / sigma),
                sf0_err=abs(a0 - sg),
                omega_vs_bare=abs(a - a_bare),
            )
        )
    err = np.array([r["err"] for r in rows])
    return {
        "engine": "numpy",
        "n": len(rows),
        "max_abs_err_vs_sg2_over_S": float(np.max(err)),
        "max_C_entry_err": float(np.max(c_entry_err)),
        "max_unreduced_poisson": float(np.max(poisson_max)),
        "min_sep_from_Sigma_g": float(np.min([r["sep_sg"] for r in rows])),
        "min_sep_from_Sigma": float(np.min([r["sep_sigma"] for r in rows])),
        "min_sep_from_theta": float(np.min([r["sep_theta"] for r in rows])),
        "max_k5_err": float(np.max([r["k5_err"] for r in rows])),
        "max_sf0_err": float(np.max([r["sf0_err"] for r in rows])),
        "max_omega_changes_alpha": float(np.max([r["omega_vs_bare"] for r in rows])),
        "median_alpha": float(np.median([r["alpha"] for r in rows])),
        "median_pred": float(np.median([r["pred"] for r in rows])),
        "weight_is_sg2_over_S": bool(
            np.max(err) < 1e-8
            and np.min([r["sep_sg"] for r in rows]) > 1e-3
            and np.min([r["sep_sigma"] for r in rows]) > 1e-3
            and np.min([r["sep_theta"] for r in rows]) > 1e-3
            and np.max([r["k5_err"] for r in rows]) < 1e-8
            and np.max([r["sf0_err"] for r in rows]) < 1e-8
            and np.max(c_entry_err) < 1e-8
        ),
    }


def run_factorization():
    Nmul, L, sg, sf = sp.symbols("N L sg sf", positive=True)
    L1, L2, L3 = sp.symbols("L1 L2 L3")
    n1, n2, n3 = sp.symbols("n1 n2 n3")
    d1, d2, d3 = sp.symbols("Dn1 Dn2 Dn3")
    J1, J2, J3 = sp.symbols("J1 J2 J3")
    Li = sp.Matrix([L1, L2, L3])
    n = sp.Matrix([n1, n2, n3])
    Dn = sp.Matrix([d1, d2, d3])
    J = sp.Matrix([J1, J2, J3])
    Ng = Li + L * n + Nmul * Dn
    mult = [Nmul, L, L1, L2, L3]

    def degree_in_multipliers(expr):
        num, den = sp.fraction(sp.together(sp.expand(expr)))
        return int(sp.total_degree(sp.Poly(sp.expand(num), *mult))), int(
            sp.total_degree(sp.Poly(sp.expand(den), *mult))
        )

    out = {}
    for name, Nf in (("Nf_is_Lvec", Li), ("Nf_shares_n_piece", Li + L * n)):
        H = sp.expand(sg * (Ng.dot(J)) + sf * (Nf.dot(J)))
        nd, dd = degree_in_multipliers(H)
        coeff_N = sp.factor(sp.expand(H).coeff(Nmul))
        out[name] = {
            "num_degree": nd,
            "den_degree": dd,
            "linear": bool(nd <= 1 and dd == 0),
            "coeff_of_N": str(coeff_N),
            "coeff_is_sg_Dn_dot_J": bool(sp.expand(coeff_N - sg * (Dn.dot(J))) == 0),
        }
    # quadratic scalar kinetic term, same Ng substitution: (Ng·J)^2 / N
    Hs = (Ng.dot(J)) ** 2 / Nmul
    nd, dd = degree_in_multipliers(Hs)
    out["scalar_quadratic"] = {
        "num_degree": nd,
        "den_degree": dd,
        "linear": bool(nd <= 1 and dd == 0),
    }
    out["dirac_linear_scalar_not"] = bool(
        out["Nf_is_Lvec"]["linear"]
        and out["Nf_shares_n_piece"]["linear"]
        and out["Nf_is_Lvec"]["coeff_is_sg_Dn_dot_J"]
        and not out["scalar_quadratic"]["linear"]
    )
    return out


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_Chi_Weight_Derivation_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": (proc.stderr or "")[-600:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(3) as ex:
        a = ex.submit(run_numpy)
        b = ex.submit(run_factorization)
        c = ex.submit(run_wolfram)
        ny, fac, wl = a.result(), b.result(), c.result()
    wls = wl.get("summary") or {}
    both = bool(ny.get("weight_is_sg2_over_S") and wls.get("weight_is_sg2_over_S"))
    out = {
        "numpy": ny,
        "sympy_factorization": fac,
        "wolfram": wl,
        "both_weight_sg2_over_S": both,
        "shift_factorization_holds": bool(fac.get("dirac_linear_scalar_not")),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "numpy_weight": ny.get("weight_is_sg2_over_S"),
        "numpy_max_err": ny.get("max_abs_err_vs_sg2_over_S"),
        "numpy_min_sep_sg": ny.get("min_sep_from_Sigma_g"),
        "wolfram_weight": wls.get("weight_is_sg2_over_S"),
        "wolfram_max_err": wls.get("max_abs_err_vs_sg2_over_S"),
        "factorization": fac.get("dirac_linear_scalar_not"),
        "both": both,
    }, indent=2))


if __name__ == "__main__":
    main()
