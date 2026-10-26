#!/usr/bin/env python3
"""Boost-sector K0' with the full Dirac matrix in the n-equation.

Carries c_I and the alpha channel. Routes psi†(dC/dp)psi as an ultralocal
source. Reports medians. Sigma_f = 0 is an exact draw, not a projection.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_Boost_FullMatrix_nEOM_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_Boost_FullMatrix_nEOM_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261027)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


g = load("gammamat", "Opsi2_Gamma_Matrix_Coefficient_PARALLEL_CursorMain.py")
k0 = load("k0matter", "Opsi2_K0prime_Matter_nEOM_PARALLEL_CursorMain.py")


def tr_coeff(op, basis):
    return complex(np.trace(basis.conj().T @ op) / np.trace(basis.conj().T @ basis))


def decompose(sg, sf, p):
    C, gp = g.C_of(sg, sf, p)
    K = inv(C)
    cI = np.zeros(3)
    cA = np.zeros((3, 3))
    rest = np.zeros(3)
    for k in range(3):
        M = (sg ** 2) * (g.ALPHAS[k] @ K @ g.ALPHAS[k])
        cI[k] = float(np.real(tr_coeff(M, g.I4)))
        for j in range(3):
            cA[k, j] = float(np.real(tr_coeff(M, g.ALPHAS[j])))
        R = M - cI[k] * g.I4
        for j in range(3):
            R = R - cA[k, j] * g.ALPHAS[j]
        rest[k] = float(norm(R))
    pred, _, _ = g.jammer_I(sg, sf, p)
    dCs = []
    for i in range(3):
        dCs.append(sf * (p[i] / gp) * g.I4 - sf * g.ALPHAS[i])
    return C, gp, cI, cA, rest, float(pred), dCs


def fd_err(sg, sf, p, dCs):
    eps = 1e-6
    dp = p.copy()
    dp[0] += eps
    C2, _ = g.C_of(sg, sf, dp)
    C, _ = g.C_of(sg, sf, p)
    return float(norm((C2 - C) / eps - dCs[0]))


def draw_p():
    p = RNG.normal(size=3)
    if float(norm(p)) < 0.3:
        p = p / max(float(norm(p)), 1e-8) * 0.3
    return p


def draw_currents():
    cur_I = RNG.normal(size=3)
    cur_A = RNG.normal(size=(3, 3))
    psi = RNG.normal(size=4) + 1j * RNG.normal(size=4)
    psi = psi / norm(psi)
    return cur_I, cur_A, psi


def one_full(bg, sg, sf, p, swap=False):
    if swap:
        sg, sf = sf, sg
    gamma = bg["gamma"]
    Dn = bg["Dn"]
    U = bg["U"]
    pot = bg["pot"]
    ginv = inv(gamma)
    cur_I, cur_A, psi = draw_currents()
    _, gp, cI, cA, rest, pred, dCs = decompose(sg, sf, p)
    u = np.array([float(np.real(np.vdot(psi, dC @ psi))) for dC in dCs])
    bracket = cI * cur_I + np.einsum("kj,jk->k", cA, cur_A)
    alpha_vec = np.einsum("kj,jk->k", cA, cur_A)
    i_mis = (cI - sg) * cur_I
    w_g = sg
    E_g = float(RNG.uniform(-1.0, 1.0))

    def assemble(source_extra):
        R = U - w_g * cur_I - source_extra
        R0 = -float(R @ Dn) - pot - E_g - w_g * float(Dn @ cur_I) - float(Dn @ source_extra)
        C_grav = R0 + float(R @ Dn) + pot
        C_N = C_grav + E_g + w_g * float(Dn @ cur_I) + float(Dn @ source_extra)
        P_grav = C_grav * Dn + ginv @ (R - U)
        P = P_grav + (E_g + w_g * float(Dn @ cur_I) + float(Dn @ source_extra)) * Dn
        P = P + ginv @ bracket
        return P - C_N * Dn, float(abs(C_N)), float(norm(P))

    resid, c_on, p_on = assemble(np.zeros(3))
    resid_u, _, _ = assemble(u)
    analytic = ginv @ (bracket - w_g * cur_I)
    v = bracket - w_g * cur_I
    uu = float(u @ u)
    if uu > 1e-18:
        v_orth = v - u * float(v @ u) / uu
    else:
        v_orth = v
    return dict(
        resid=float(norm(resid)),
        analytic_err=float(norm(resid - analytic)),
        u_routed_delta=float(norm(resid_u - resid)),
        orth_frac=(float(norm(v_orth)) / float(norm(v))) if float(norm(v)) > 1e-12 else 0.0,
        alpha_piece=float(norm(ginv @ alpha_vec)),
        i_piece=float(norm(ginv @ i_mis)),
        cI_err=float(np.max(np.abs(cI - pred))),
        cI_vs_half=float(np.max(np.abs(cI - 0.5 * sg))) if abs(sg - sf) < 1e-12 else float("nan"),
        alpha_coeff=float(np.max(np.abs(cA))),
        rest=float(np.max(rest)),
        fd=fd_err(sg, sf, p, dCs),
        c_on=c_on,
        p_on=p_on,
        gp=gp,
    )


def pack(rows, key):
    return np.array([r[key] for r in rows], dtype=float)


def summarise(rows, label):
    resid = pack(rows, "resid")
    return {
        "label": label,
        "n": len(rows),
        "median_resid": float(np.median(resid)),
        "median_alpha_piece": float(np.median(pack(rows, "alpha_piece"))),
        "median_I_piece": float(np.median(pack(rows, "i_piece"))),
        "median_orth_frac": float(np.median(pack(rows, "orth_frac"))),
        "max_analytic_err": float(np.max(pack(rows, "analytic_err"))),
        "max_u_routed_delta": float(np.max(pack(rows, "u_routed_delta"))),
        "max_cI_err": float(np.max(pack(rows, "cI_err"))),
        "median_alpha_coeff": float(np.median(pack(rows, "alpha_coeff"))),
        "max_rest": float(np.max(pack(rows, "rest"))),
        "max_fd": float(np.max(pack(rows, "fd"))),
        "max_C_on": float(np.max(pack(rows, "c_on"))),
        "fraction_resid_gt_1e-3": float(np.mean(resid > 1e-3)),
    }


def collect(n_keep, mode):
    rows = []
    tries = 0
    while len(rows) < n_keep and tries < n_keep * 30:
        tries += 1
        bg = k0.try_background(k0.RNG)
        if bg is None:
            continue
        if mode == "matter":
            sg = float(RNG.uniform(0.4, 2.0))
            sf = float(RNG.uniform(0.4, 2.0))
            rows.append(one_full(bg, sg, sf, draw_p(), swap=False))
        elif mode == "sf0":
            sg = float(RNG.uniform(0.4, 2.0))
            rows.append(one_full(bg, sg, 0.0, draw_p(), swap=False))
        elif mode == "k5":
            sg = float(RNG.uniform(0.4, 2.0))
            sf = float(RNG.uniform(0.4, 2.0))
            rows.append(one_full(bg, sg, sf, draw_p(), swap=True))
        elif mode == "equal":
            s = float(RNG.uniform(0.4, 2.0))
            rows.append(one_full(bg, s, s, draw_p(), swap=False))
        elif mode == "p0":
            sg = float(RNG.uniform(0.4, 2.0))
            sf = float(RNG.uniform(0.4, 2.0))
            rows.append(one_full(bg, sg, sf, np.zeros(3), swap=False))
        else:
            raise ValueError(mode)
    return rows


def run_numpy():
    pure = k0.pure_hr()
    matter = summarise(collect(80, "matter"), "boost")
    sf0 = summarise(collect(40, "sf0"), "sf0")
    k5 = summarise(collect(80, "k5"), "k5")
    equal_rows = collect(40, "equal")
    equal = summarise(equal_rows, "equal")
    equal["median_abs_cI_minus_sg_over_2"] = float(np.nanmedian(pack(equal_rows, "cI_vs_half")))
    p0 = summarise(collect(40, "p0"), "p0")
    controls = bool(
        pure["pass"]
        and matter["max_analytic_err"] < 1e-6
        and matter["max_u_routed_delta"] < 1e-6
        and matter["max_fd"] < 1e-5
        and sf0["median_resid"] < 1e-8
        and sf0["median_alpha_coeff"] < 1e-8
        and p0["median_alpha_coeff"] < 1e-8
    )
    residual_survives = bool(
        controls
        and matter["median_resid"] > 1e-3
        and matter["median_alpha_piece"] > 1e-3
        and matter["fraction_resid_gt_1e-3"] >= 0.95
        and k5["median_resid"] > 1e-3
    )
    return {
        "engine": "numpy",
        "pure_hr": pure,
        "boost": matter,
        "sigma_f_0": {k: sf0[k] for k in ("n", "median_resid", "median_alpha_coeff", "max_cI_err")},
        "k5_swap": {k: k5[k] for k in ("n", "median_resid", "median_alpha_piece", "max_cI_err", "fraction_resid_gt_1e-3")},
        "equal_weights": {
            "median_resid": equal["median_resid"],
            "median_abs_cI_minus_sg_over_2": equal["median_abs_cI_minus_sg_over_2"],
            "median_alpha_coeff": equal["median_alpha_coeff"],
        },
        "aligned_p0": {
            "median_resid": p0["median_resid"],
            "median_alpha_coeff": p0["median_alpha_coeff"],
            "max_cI_err": p0["max_cI_err"],
        },
        "formula_holds_all_three_directions": bool(matter["max_cI_err"] < 1e-8 and k5["max_cI_err"] < 1e-8),
        "matrix_remainder_below_1e-8": bool(matter["max_rest"] < 1e-8),
        "controls_pass": controls,
        "residual_survives_boost_nEOM": residual_survives,
        "statistic": "median over draws; no minimum-departure flag",
    }


def run_wolfram():
    if not WL.is_file():
        return {"returncode": None, "summary": {}, "stderr_tail": "no wl"}
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_Boost_FullMatrix_nEOM_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": (proc.stderr or "")[-600:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        a = ex.submit(run_numpy)
        b = ex.submit(run_wolfram)
        numpy_s = a.result()
        wolfram_b = b.result()
    out = {"numpy": numpy_s, "wolfram": wolfram_b}
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "controls": numpy_s["controls_pass"],
        "survives": numpy_s["residual_survives_boost_nEOM"],
        "median_resid": numpy_s["boost"]["median_resid"],
        "median_alpha": numpy_s["boost"]["median_alpha_piece"],
        "median_I": numpy_s["boost"]["median_I_piece"],
        "median_orth_frac": numpy_s["boost"]["median_orth_frac"],
        "sf0": numpy_s["sigma_f_0"]["median_resid"],
        "k5": numpy_s["k5_swap"]["median_resid"],
        "pure": numpy_s["pure_hr"]["pass"],
        "wolfram_rc": wolfram_b.get("returncode"),
        "wolfram_median": (wolfram_b.get("summary") or {}).get("median_resid"),
    }, indent=2))


if __name__ == "__main__":
    main()
