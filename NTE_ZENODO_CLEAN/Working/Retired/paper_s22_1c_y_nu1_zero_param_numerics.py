#!/usr/bin/env python3
"""Section 22.1c — m_nu1 zero-parameter numerics."""
from __future__ import annotations

import math

V_EW = 246.0
M_R = 8.2e14
S13_DEG = 8.57
Y2 = (8.0 * math.pi) ** (-1.0 / 3.0)
DM2_21 = 7.5e-5  # eV^2 solar-scale order


def main() -> None:
    s13 = math.sin(math.radians(S13_DEG))
    mnu2 = Y2**2 * V_EW**2 / M_R * 1e9
    mnu1 = mnu2 * s13**2
    mnu1_direct = Y2**2 * s13**2 * V_EW**2 / M_R * 1e9

    print("# Section 22.1c — m_nu1 zero-parameter numerics")
    print("=" * 60)
    print(f"  m_nu2                         = {mnu2:.6f} eV")
    print(f"  m_nu1 = m2 sin^2(13)          = {mnu1:.6f} eV")
    print(f"  m_nu1 direct (8pi)^-2/3 ...   = {mnu1_direct:.6f} eV")
    print(f"  sqrt(Dm2_21) obs ~            = {math.sqrt(DM2_21):.6f} eV")
    print(f"  m1/m2                         = {mnu1/mnu2:.4f}")
    print(f"  m1^2 / Dm2_21 (order)         = {mnu1**2/DM2_21:.4f}")
    print("\n## Verdict")
    print("  m_nu1 ZERO-PARAMETER from m_nu2 + sin^2(theta_13).")
    print("  Full Delta m^2_21 match NOT claimed (needs D_F+PMNS).")


if __name__ == "__main__":
    main()
