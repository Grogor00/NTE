#!/usr/bin/env python3
"""P-BH1b — S_BH vs N-thickness shell entropy candidates; M^2 scaling test."""
from __future__ import annotations

import math

C = 2.99792458e8
G = 6.67430e-11
HBAR = 1.054571817e-34
ALPHA = 2.38e-47
V_EW_GEV = 246.0


def rs(m_kg: float) -> float:
    return 2 * G * m_kg / C**2


def phi_n_at(r_m: float, m_kg: float) -> float:
    return -G * m_kg / (r_m * C**2)


def ell_ratio(phi_n: float) -> float:
    return 1.0 / (1.0 + phi_n)


def s_bh_si(m_kg: float) -> float:
    """Bekenstein-Hawking S = A/(4G) = 4 pi G M^2 / (hbar c) [SI, k_B=1 units]."""
    return 4 * math.pi * G * m_kg**2 / (HBAR * C)


def s_bh_natural(m_kg: float) -> float:
    """S = pi rs^2 / G in c=1 units (length^2 / G ~ M_Pl^2)."""
    r = rs(m_kg)
    return math.pi * r**2 / G


def integral_thickness_linear(m_kg: float, r_max_mult: float = 1e6) -> float:
    """FAIL candidate: int_{rs}^{rmax} (ell/ell_inf - 1) dr ~ M ln(r) [not M^2]."""
    r0 = rs(m_kg)
    r1 = r_max_mult * r0
    # trapezoid on log grid
    n = 200
    total = 0.0
    prev_r = r0
    prev_f = ell_ratio(phi_n_at(r0, m_kg)) - 1.0
    for i in range(1, n + 1):
        r = r0 * (r1 / r0) ** (i / n)
        f = ell_ratio(phi_n_at(r, m_kg)) - 1.0
        total += 0.5 * (prev_f + f) * (r - prev_r)
        prev_r, prev_f = r, f
    return total


def s_nte_multiplicative(m_kg: float) -> float:
    """Programme candidate: S_NTE = (A/4G) * g(ell/ell_inf at horizon); g = ell/ell_inf."""
    r0 = rs(m_kg)
    g_horizon = ell_ratio(phi_n_at(r0, m_kg))
    return s_bh_natural(m_kg) * g_horizon


def main() -> None:
    masses = [
        ("M_sun", 1.98847e30),
        ("10 M_sun", 1.98847e31),
        ("10^6 M_sun", 1.98847e36),
    ]

    print("# P-BH1b — area law vs N-thickness entropy candidates")
    print()
    print("## Bekenstein-Hawking baseline S_BH = A/(4G) ~ M^2")
    print("| M | r_s [m] | S_BH [natural] | ell/ell_inf @ r_s |")
    print("|---|---------|----------------|-------------------|")
    s_ref = None
    m_ref = None
    for label, m in masses:
        r0 = rs(m)
        sbh = s_bh_natural(m)
        g0 = ell_ratio(phi_n_at(r0, m))
        print(f"| {label} | {r0:.4e} | {sbh:.4e} | {g0:.4f} |")
        if s_ref is None:
            s_ref, m_ref = sbh, m

    print()
    print("## Scaling tests (relative to M_sun)")
    print("| M | S_BH / S_BH,sun | (int thickness dr) / same | S_NTE mult / same |")
    print("|---|-----------------|---------------------------|-------------------|")
    i_ref = integral_thickness_linear(m_ref)
    sm_ref = s_nte_multiplicative(m_ref)
    for label, m in masses:
        ratio_bh = s_bh_natural(m) / s_ref
        ratio_i = integral_thickness_linear(m) / i_ref
        ratio_sm = s_nte_multiplicative(m) / sm_ref
        print(f"| {label} | {ratio_bh:.2e} | {ratio_i:.2e} | {ratio_sm:.2e} |")

    print()
    print("## Verdict")
    print("- S_BH scales as M^2 (ratio 10^2 for 10 M_sun, 10^12 for 10^6 M_sun)")
    print("- Linear thickness integral int (ell/ell_inf-1) dr scales ~ M (FAIL for area law)")
    print("- Multiplicative S_NTE = (A/4G)*(ell/ell_inf)|_rs preserves M^2 (O(1) factor ~2 at r_s)")
    print("- P-BH1b: additive e-fold density integral NOT viable; horizon-area x thickness factor IS")
    print("  Jammer must derive g(ell) from Janus + mu(x,N) — not ship as derived yet.")


if __name__ == "__main__":
    main()
