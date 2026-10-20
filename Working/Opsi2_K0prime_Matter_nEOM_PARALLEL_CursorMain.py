#!/usr/bin/env python3
"""K0' engine + matter. Solve the n-equation. Test P - C_N (Dn), not a projection.

Prereg: Opsi2_K0prime_Matter_nEOM_PREREGISTRATION_CursorMain_20261021.md
"""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import det, inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_K0prime_Matter_nEOM_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_K0prime_Matter_nEOM_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261021)


def matrix_sqrt_spd(A):
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    w = np.clip(np.real(w), 0, None)
    return (V * np.sqrt(w)) @ V.T


def D_of_n(gamma, f3, n):
    x = 1.0 - float(n @ f3 @ n)
    if x <= 1e-12:
        raise ValueError("x")
    Q = x * np.eye(3) + np.outer(n, f3 @ n)
    inside = inv(gamma) @ f3 @ Q
    inside = 0.5 * (inside + inside.T)
    return matrix_sqrt_spd(inside) @ inv(Q)


def random_spd(rng):
    A = rng.normal(size=(3, 3))
    return A @ A.T + 0.4 * np.eye(3)


def try_background(rng):
    gamma = random_spd(rng)
    f3 = random_spd(rng)
    n = rng.normal(size=3)
    n = 0.25 * n / max(1.0, norm(n))
    x = 1.0 - float(n @ f3 @ n)
    if x <= 0.2:
        return None
    try:
        D = D_of_n(gamma, f3, n)
    except (ValueError, np.linalg.LinAlgError):
        return None
    if abs(np.linalg.det(D)) < 1e-8 or np.linalg.cond(D) > 1e6:
        return None
    Dn = D @ n
    if norm(n) < 1e-3 or norm(Dn) < 1e-3:
        return None
    sqrt_g = np.sqrt(det(gamma))
    beta1, m2 = 1.0, 1.0
    U = 2.0 * m2 * sqrt_g * beta1 * (f3 @ n) / np.sqrt(x)
    try:
        VbarM = (beta1 / np.sqrt(x)) * (f3 @ inv(D))
    except np.linalg.LinAlgError:
        return None
    Vbar = inv(gamma) @ VbarM @ inv(gamma)
    pot_vec = 2.0 * m2 * sqrt_g * (Vbar @ gamma @ Dn)
    # vacuum identity: gamma^{-1} U = pot_vec
    if norm(inv(gamma) @ U - pot_vec) > 1e-6:
        return None
    V = beta1 * np.sqrt(x) * np.trace(D)
    pot = 2.0 * m2 * sqrt_g * V
    return dict(gamma=gamma, n=n, Dn=Dn, U=U, pot=pot, sqrt_g=sqrt_g)


def pack(rows, key):
    a = np.array([r[key] for r in rows], dtype=float)
    return a


def pure_hr(n_try=200):
    rows = []
    for _ in range(n_try):
        bg = try_background(RNG)
        if bg is None:
            continue
        gamma, Dn, U, pot = bg["gamma"], bg["Dn"], bg["U"], bg["pot"]
        R = U.copy()  # vacuum n-equation
        R0 = -float(R @ Dn) - pot  # C = 0
        C = R0 + float(R @ Dn) + pot
        P = C * Dn + inv(gamma) @ (R - U)
        R0_off = R0 + 1.7
        C_off = R0_off + float(R @ Dn) + pot
        P_off = C_off * Dn + inv(gamma) @ (R - U)
        rows.append(
            dict(
                resid=float(norm(P - C * Dn)),
                P_on=float(norm(P)),
                P_off=float(norm(P_off)),
                C_on=float(abs(C)),
            )
        )
    resid = pack(rows, "resid")
    P_on = pack(rows, "P_on")
    P_off = pack(rows, "P_off")
    return {
        "n_kept": len(rows),
        "max_resid": float(np.max(resid)),
        "max_P_on_C0": float(np.max(P_on)),
        "min_P_when_C_nonzero": float(np.min(P_off)),
        "pass": bool(
            len(rows) >= 20
            and np.max(resid) < 1e-8
            and np.max(P_on) < 1e-8
            and np.min(P_off) > 1e-3
        ),
    }


def one_matter(bg, Sigma_g, Sigma_f, swap=False):
    """Return residual norm on C_N=0, residual off C_N, analytic error, theta."""
    gamma, Dn, U, pot = bg["gamma"], bg["Dn"], bg["U"], bg["pot"]
    if swap:
        Sigma_g, Sigma_f = Sigma_f, Sigma_g
    Sigma = Sigma_g + Sigma_f
    w_g = Sigma_g
    w_br = (Sigma_g ** 2 / Sigma) if Sigma > 0 else Sigma_g
    w_tot = Sigma
    J = RNG.normal(size=3)
    b = RNG.normal(size=3)
    E_g = float(RNG.uniform(-1.0, 1.0))
    cur = J + b
    # n-equation: R + w_g cur = U
    R = U - w_g * cur
    # C_grav = R0 + R·Dn + pot; C_N = C_grav + E_g + w_g Dn·cur
    # Choose R0 so C_N = 0.
    R0 = -float(R @ Dn) - pot - E_g - w_g * float(Dn @ cur)
    C_grav = R0 + float(R @ Dn) + pot
    C_N = C_grav + E_g + w_g * float(Dn @ cur)
    ginv_cur = inv(gamma) @ cur
    # Vacuum piece + ordinary completion with the bracket weight on the current.
    P_grav = C_grav * Dn + inv(gamma) @ (R - U)
    P = P_grav + (E_g + w_g * float(Dn @ cur)) * Dn + w_br * ginv_cur
    resid_vec = P - C_N * Dn
    analytic = (w_br - w_g) * ginv_cur
    # C_N != 0 probe: shift R0. Residual must be unchanged.
    R0_off = R0 + 1.7
    C_grav_off = R0_off + float(R @ Dn) + pot
    C_off = C_grav_off + E_g + w_g * float(Dn @ cur)
    P_grav_off = C_grav_off * Dn + inv(gamma) @ (R - U)
    P_off = P_grav_off + (E_g + w_g * float(Dn @ cur)) * Dn + w_br * ginv_cur
    resid_off = P_off - C_off * Dn
    # b = 0 on the same J, same background
    cur_J = J
    R_J = U - w_g * cur_J
    R0_J = -float(R_J @ Dn) - pot - E_g - w_g * float(Dn @ cur_J)
    C_grav_J = R0_J + float(R_J @ Dn) + pot
    C_J = C_grav_J + E_g + w_g * float(Dn @ cur_J)
    P_J = (
        C_grav_J * Dn
        + inv(gamma) @ (R_J - U)
        + (E_g + w_g * float(Dn @ cur_J)) * Dn
        + w_br * (inv(gamma) @ cur_J)
    )
    # R_f solves total momentum and must not move the residual
    R_f = -R - w_tot * cur
    total = R + R_f + w_tot * cur
    theta = (Sigma_g / Sigma) if Sigma > 0 else 1.0
    return dict(
        resid=float(norm(resid_vec)),
        resid_off=float(norm(resid_off)),
        resid_J=float(norm(P_J - C_J * Dn)),
        analytic_err=float(norm(resid_vec - analytic)),
        off_minus_on=float(norm(resid_off - resid_vec)),
        total_mom=float(norm(total)),
        P_on=float(norm(P)),
        theta=float(theta),
        factor=float(abs(w_br - w_g)),
    )


def summarise_matter(rows, label):
    resid = pack(rows, "resid")
    return {
        "label": label,
        "n": len(rows),
        "median_abs_resid": float(np.median(resid)),
        "max_abs_resid": float(np.max(resid)),
        "fraction_gt_1e-3": float(np.mean(resid > 1e-3)),
        "max_analytic_err": float(np.max(pack(rows, "analytic_err"))),
        "max_off_minus_on": float(np.max(np.abs(pack(rows, "off_minus_on")))),
        "max_total_mom": float(np.max(pack(rows, "total_mom"))),
        "median_resid_J_only": float(np.median(pack(rows, "resid_J"))),
        "median_theta_g": float(np.median(pack(rows, "theta"))),
        "median_abs_factor": float(np.median(pack(rows, "factor"))),
        "min_P_on_surface": float(np.min(pack(rows, "P_on"))),
    }


def _draw_sigmas():
    return float(RNG.uniform(0.3, 2.0)), float(RNG.uniform(0.3, 2.0))


def collect_generic(n_keep, mode):
    rows = []
    tries = 0
    while len(rows) < n_keep and tries < n_keep * 25:
        tries += 1
        bg = try_background(RNG)
        if bg is None:
            continue
        if mode == "matter":
            sg, sf = _draw_sigmas()
            rows.append(one_matter(bg, sg, sf, swap=False))
        elif mode == "sf0":
            sg = float(RNG.uniform(0.3, 2.0))
            rows.append(one_matter(bg, sg, 0.0, swap=False))
        elif mode == "k5":
            sg, sf = _draw_sigmas()
            rows.append(one_matter(bg, sg, sf, swap=True))
        elif mode == "ef":
            s = float(RNG.uniform(0.3, 2.0))
            rows.append(one_matter(bg, s, s, swap=False))
        else:
            raise ValueError(mode)
    return rows


def run_numpy_main():
    pure = pure_hr()
    matter = summarise_matter(collect_generic(200, "matter"), "matter")
    sf0 = summarise_matter(collect_generic(80, "sf0"), "sf0")
    k5 = summarise_matter(collect_generic(200, "k5"), "k5")
    ef = summarise_matter(collect_generic(80, "ef"), "ef")
    analytic_ok = (
        matter["max_analytic_err"] < 1e-6
        and sf0["max_analytic_err"] < 1e-6
        and k5["max_analytic_err"] < 1e-6
        and matter["max_off_minus_on"] < 1e-6
        and matter["max_total_mom"] < 1e-6
    )
    pass_G2 = bool(
        pure["pass"]
        and analytic_ok
        and sf0["max_abs_resid"] < 1e-8
        and matter["median_abs_resid"] > 1e-3
        and matter["fraction_gt_1e-3"] >= 0.95
        and k5["median_abs_resid"] > 1e-3
        and k5["fraction_gt_1e-3"] >= 0.95
    )
    pass_Ma = bool(pure["pass"] and matter["median_abs_resid"] < 1e-8)
    if pass_G2:
        lane = "G-2"
    elif pass_Ma:
        lane = "M-a"
    else:
        lane = "G-4"
    return {
        "engine": "numpy",
        "pure_hr": pure,
        "matter": matter,
        "sigma_f_0": sf0,
        "k5_swap": k5,
        "e_equals_f_report_only": ef,
        "pass_G2": pass_G2,
        "pass_Ma": pass_Ma,
        "lane": lane,
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_K0prime_Matter_nEOM_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": (proc.stderr or "")[-500:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        a = ex.submit(run_numpy_main)
        b = ex.submit(run_wolfram)
        numpy_s = a.result()
        wolfram_b = b.result()
    wl = wolfram_b.get("summary") or {}
    lanes = {numpy_s.get("lane"), wl.get("lane")}
    if lanes == {"G-2"}:
        both = "G-2"
    elif lanes == {"M-a"}:
        both = "M-a"
    else:
        both = "G-4"
    out = {"numpy": numpy_s, "wolfram": wolfram_b, "both_lane": both}
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "numpy_lane": numpy_s.get("lane"),
        "numpy_median": numpy_s["matter"]["median_abs_resid"],
        "numpy_sf0": numpy_s["sigma_f_0"]["max_abs_resid"],
        "numpy_pure": numpy_s["pure_hr"]["max_resid"],
        "wolfram_lane": wl.get("lane"),
        "wolfram_median": wl.get("median_abs_resid"),
        "both": both,
    }, indent=2))


if __name__ == "__main__":
    main()
