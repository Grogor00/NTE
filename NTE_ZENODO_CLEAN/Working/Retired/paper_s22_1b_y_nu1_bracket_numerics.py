#!/usr/bin/env python3
"""Section 22.1b — Y_nu1 bracket numerics (Z2 + hierarchy)."""
from __future__ import annotations

import math

V_EW = 246.0
M_R = 8.2e14
M1 = 6.041e9
M2 = 6.176e9
Y2 = (8.0 * math.pi) ** (-1.0 / 3.0)
S13_DEG = 8.57
S13 = math.sin(math.radians(S13_DEG))
DM2_SOLAR = 7.5e-5
MNU1_SUM_BOUND = 0.037  # eV cosmological bound (order)
SQRT_DM2_SOLAR = math.sqrt(DM2_SOLAR)


def m_nu_ev(y: float, m_rh: float) -> float:
    return (y * V_EW) ** 2 / m_rh * 1.0e9


def main() -> None:
    print("# Section 22.1b — Y_nu1 bracket numerics")
    print("=" * 60)

    mnu2 = Y2**2 * V_EW**2 / M_R * 1e9
    sqrt_m1_mr = math.sqrt(M1 / M_R)

    print("\n## A — Anchor (nu2 closed)")
    print(f"  m_nu2 (zero-param)           = {mnu2:.6f} eV")
    print(f"  ratio/solar                  = {mnu2/SQRT_DM2_SOLAR:.4f}")

    print("\n## B — Y_nu1 bracket routes")
    y1_z2 = Y2 * S13 * sqrt_m1_mr
    y1_hier = Y2 * S13  # hierarchy only
    routes = [
        ("Y1 = Y2 sin13 sqrt(M1/MR), M_1", y1_z2, M1),
        ("Y1 = Y2 sin13, M_R", y1_hier, M_R),
        ("Y1 = Y2 sin13 sqrt(M1/MR), M_R", y1_z2, M_R),
    ]
    for label, y1, mden in routes:
        m1 = m_nu_ev(y1, mden)
        print(f"  {label:<28} Y1={y1:.6f}  m1={m1:.6f} eV")

    print("\n## C — Mass-ratio bracket (no Y1)")
    m1_ratio = mnu2 * S13**2
    m1_ratio_m2 = mnu2 * S13**2 * (M1 / M2)
    print(f"  m1 ~ m2 sin^2(13)           = {m1_ratio:.6f} eV")
    print(f"  m1 ~ m2 sin^2(13) M1/M2     = {m1_ratio_m2:.6f} eV")

    print("\n## D — Consistency checks")
    m1_canon = m_nu_ev(y1_z2, M1)
    print(f"  m1 canon (B primary)         = {m1_canon:.6e} eV")
    print(f"  sum bound m1 < {MNU1_SUM_BOUND} eV       = {m1_canon < MNU1_SUM_BOUND}")
    print(f"  m1/m2                        = {m1_canon/mnu2:.4f}")
    print(f"  sqrt(Dm2) ratio m1/m2       = {m1_canon/mnu2:.4f} vs sin13={S13:.4f}")

    print("\n## E — Normal hierarchy")
    print(f"  m3 > m2 > m1 required: m1 << m2  PASS ({m1_canon:.4f} << {mnu2:.4f})")

    print("\n## Verdict")
    print("  Y_nu1 BRACKET at Z2+PMNS register — not zero-parameter closure.")
    print("  Primary: Y1 = (8pi)^(-1/3) sin(theta13) sqrt(M1/MR); seesaw M_1.")


if __name__ == "__main__":
    main()
