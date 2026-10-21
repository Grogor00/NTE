#!/usr/bin/env python3
"""Explicit Dirac matrices: coefficient of {E_g, E_g}_D, current identity, boost.

Prereg: Opsi2_Gamma_Matrix_Coefficient_PREREGISTRATION_CursorMain_20261022.md
"""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_Gamma_Matrix_Coefficient_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_Gamma_Matrix_Coefficient_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261022)

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def block_gamma(sig):
    z = np.zeros((2, 2), dtype=complex)
    return np.block([[z, sig], [-sig, z]])


G0 = np.block([[I2, np.zeros((2, 2))], [np.zeros((2, 2)), -I2]]).astype(complex)
GS = [block_gamma(SX), block_gamma(SY), block_gamma(SZ)]
ALPHAS = [G0 @ g for g in GS]


def tr_coeff(op, basis):
    return complex(np.trace(basis.conj().T @ op) / np.trace(basis.conj().T @ basis))


def C_of(sg, sf, p):
    gp = float(np.sqrt(1.0 + p @ p))
    M = (sg + sf * gp) * I4
    for i in range(3):
        M = M - sf * p[i] * ALPHAS[i]
    return M, gp


def jammer_I(sg, sf, p):
    gp = float(np.sqrt(1.0 + p @ p))
    denom = sg**2 + 2.0 * gp * sg * sf + sf**2
    return sg**2 * (sg + sf * gp) / denom, denom, gp


def channel(sg, sf, p, k=0):
    C, gp = C_of(sg, sf, p)
    K = inv(C)
    M = (sg**2) * (ALPHAS[k] @ K @ ALPHAS[k])
    cI = float(np.real(tr_coeff(M, I4)))
    cA = [float(np.real(tr_coeff(M, ALPHAS[j]))) for j in range(3)]
    rest = M - cI * I4
    for j in range(3):
        rest = rest - cA[j] * ALPHAS[j]
    pred, denom, _ = jammer_I(sg, sf, p)
    return dict(
        cI=cI,
        cA=cA,
        pred=pred,
        err=abs(cI - pred),
        aligned_target=sg**2 / (sg + sf) if sf + sg != 0 else sg,
        rest_frob=float(norm(rest)),
        dist_to_scalar_I=float(norm(M - cI * I4)),
        gp=gp,
        alpha_sq_err=float(norm(ALPHAS[k] @ ALPHAS[k] - I4)),
    )


def collect():
    assert all(float(norm(a @ a - I4)) < 1e-12 for a in ALPHAS)
    n = 60
    rows_a, rows_b, rows_0 = [], [], []
    for _ in range(n):
        sg = float(RNG.uniform(0.4, 2.0))
        sf = float(RNG.uniform(0.4, 2.0))
        ra = channel(sg, sf, np.zeros(3))
        p = RNG.normal(size=3)
        if float(norm(p)) < 0.3:
            p = p / max(float(norm(p)), 1e-8) * 0.3
        rb = channel(sg, sf, p)
        r0 = channel(sg, 0.0, p)
        rows_a.append(ra)
        rows_b.append((sg, sf, rb))
        rows_0.append((sg, r0))
    gamma01 = 0.5 * (G0 @ GS[0] - GS[0] @ G0)
    spin_vertex = ALPHAS[0] @ (0.25 * gamma01)
    v = np.array([1.0, 0.3, 0.2, -0.4], dtype=complex)
    v = v / norm(v)
    # E = ψ† α ∂ψ is identically 0 when ∂ψ=0, while ψ†αψ need not be
    e_const = 0.0
    a_ultra = complex(np.vdot(v, ALPHAS[0] @ v))
    al_err = max(abs(r["cI"] - r["aligned_target"]) for r in rows_a)
    al_A = max(max(abs(x) for x in r["cA"]) for r in rows_a)
    al_dist = max(r["dist_to_scalar_I"] for r in rows_a)
    bo_err = max(rb["err"] for _, _, rb in rows_b)
    bo_dep = min(abs(rb["cI"] - sg**2 / (sg + sf)) for sg, sf, rb in rows_b)
    bo_A = min(max(abs(x) for x in rb["cA"]) for _, _, rb in rows_b)
    bo_A_med = float(np.median([max(abs(x) for x in rb["cA"]) for _, _, rb in rows_b]))
    sep_sg = min(abs(rb["cI"] - sg) for sg, _, rb in rows_b)
    sf0_err = max(abs(r0["cI"] - sg) for sg, r0 in rows_0)
    sf0_A = max(max(abs(x) for x in r0["cA"]) for _, r0 in rows_0)
    passed_aligned = bool(al_err < 1e-8 and al_A < 1e-8 and al_dist < 1e-8)
    boost_changes = bool(bo_dep > 1e-3 and bo_err < 1e-8)
    return {
        "engine": "numpy",
        "n": n,
        "alpha_squared_is_I": True,
        "aligned_pass": passed_aligned,
        "aligned_max_err_vs_sg2_over_S": float(al_err),
        "aligned_max_alpha_channel": float(al_A),
        "aligned_max_dist_to_I": float(al_dist),
        "boost_matches_closed_form": bool(bo_err < 1e-8),
        "boost_max_err_vs_closed_form": float(bo_err),
        "boost_min_departure_from_sg2_over_S": float(bo_dep),
        "boost_min_alpha_channel": float(bo_A),
        "boost_median_alpha_channel": bo_A_med,
        "boost_min_sep_cI_from_Sigma_g": float(sep_sg),
        "boost_changes_weight": boost_changes,
        "sf0_max_err_vs_sg": float(sf0_err),
        "sf0_max_alpha_channel": float(sf0_A),
        "constant_spinor_E": e_const,
        "constant_spinor_psi_alpha_psi_real": float(np.real(a_ultra)),
        "spin_vertex_I_coeff": float(np.real(tr_coeff(spin_vertex, I4))),
        "spin_vertex_frob": float(norm(spin_vertex)),
        "gamma01_real": [[float(np.real(gamma01[i, j])) for j in range(4)] for i in range(4)],
        "current_aligned": "psi_dagger_partial_psi",
        "not_current": "psi_dagger_alpha_psi",
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_Gamma_Matrix_Coefficient_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": (proc.stderr or "")[-800:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(2) as ex:
        a = ex.submit(collect)
        b = ex.submit(run_wolfram)
        ny, wl = a.result(), b.result()
    wls = wl.get("summary") or {}
    both_aligned = bool(ny.get("aligned_pass") and wls.get("aligned_pass"))
    both_boost = bool(ny.get("boost_changes_weight") and wls.get("boost_changes_weight"))
    out = {
        "numpy": ny,
        "wolfram": wl,
        "both_aligned_exact": both_aligned,
        "both_boost_changes": both_boost,
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "aligned": both_aligned,
        "numpy_al_err": ny.get("aligned_max_err_vs_sg2_over_S"),
        "numpy_boost_dep": ny.get("boost_min_departure_from_sg2_over_S"),
        "numpy_boost_A": ny.get("boost_median_alpha_channel"),
        "numpy_sf0": ny.get("sf0_max_err_vs_sg"),
        "wolfram_aligned": wls.get("aligned_pass"),
        "wolfram_boost": wls.get("boost_changes_weight"),
        "wolfram_err": wls.get("boost_max_err_vs_closed_form"),
    }, indent=2))


if __name__ == "__main__":
    main()
