#!/usr/bin/env python3
"""P-BH1a — N-thickness shell numerics (Schwarzschild exterior, §2.3 identity)."""
from __future__ import annotations

import math

C = 2.99792458e8  # m/s
G = 6.67430e-11  # m^3 kg^-1 s^-2
V_EW_GEV = 246.0
ALPHA = 2.38e-47  # GeV^-1
M_SUN_KG = 1.98847e30


def schwarzschild_rs(m_kg: float) -> float:
    return 2 * G * m_kg / C**2


def phi_newton(r_m: float, m_kg: float) -> float:
    return -G * m_kg / (r_m * C**2)


def phi_nte_sq_over_vew2(phi_n: float) -> float:
    return 1.0 + phi_n


def ell_ratio(phi_n: float) -> float:
    """ell(r) / ell(inf) = 1 / (1 + Phi_N) for structural identity."""
    return 1.0 / (1.0 + phi_n)


def h_over_h0(phi_n: float) -> float:
    return 1.0 + phi_n


def main() -> None:
    m = M_SUN_KG
    rs = schwarzschild_rs(m)
    ell_inf_si = 1.0 / (ALPHA * V_EW_GEV**2)  # natural; display order of magnitude only

    print("# P-BH1a — N-thickness shell numerics (solar-mass BH exterior)")
    print(f"M = M_sun, r_s = {rs:.4e} m")
    print(f"ell(inf) ~ 1/(alpha v_EW^2) [natural units]")
    print()
    print("| r/r_s | Phi_N | |Phi|^2/v_EW^2 | ell/ell_inf | H/H0 | regime |")
    print("|-------|-------|-------------|-------------|------|--------|")

    for mult in [1000, 100, 10, 5, 2.5, 2.0, 1.5, 1.1, 1.01]:
        r = mult * rs
        pn = phi_newton(r, m)
        ratio = phi_nte_sq_over_vew2(pn)
        er = ell_ratio(pn)
        hh = h_over_h0(pn)
        if abs(pn) < 0.01:
            regime = "1PN OK"
        elif abs(pn) < 0.1:
            regime = "1PN marginal"
        elif abs(pn) < 0.5:
            regime = "strong field"
        else:
            regime = "identity breakdown"
        print(f"| {mult:5.2f} | {pn:+.4e} | {ratio:.6f} | {er:.6f} | {hh:.6f} | {regime} |")

    pn_rs = phi_newton(rs, m)
    print()
    print("## Summary")
    print(f"At r = r_s: Phi_N = {pn_rs:.4f} (|Phi_N| ~ 0.5 — strong field)")
    print(f"  |Phi|^2/v_EW^2 = {phi_nte_sq_over_vew2(pn_rs):.4f}")
    print(f"  ell/ell_inf = {ell_ratio(pn_rs):.4f}  (~2x thinning at leading order)")
    print()
    print("At r = 2 r_s: Phi_N = {:.4f}".format(phi_newton(2 * rs, m)))
    print(f"  ell/ell_inf = {ell_ratio(phi_newton(2 * rs, m)):.4f}")
    print()
    print("Discipline: structural identity trusted for |Phi_N| << 1 only; P-BH4 needed at horizon.")
    print("Area law S_BH = pi rs^2/G not computed — P-BH1b open.")


if __name__ == "__main__":
    main()
