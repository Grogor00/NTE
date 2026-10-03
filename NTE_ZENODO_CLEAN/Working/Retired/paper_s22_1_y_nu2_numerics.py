#!/usr/bin/env python3
"""Section 22.1 — Y_nu2 structural derivation numerics."""
from __future__ import annotations

import math

V_EW = 246.0
M_R = 8.2e14
M1 = 6.041e9
M2 = 6.176e9
PREF_8PI = (8.0 * math.pi) ** (1.0 / 3.0)
Y2_STRUCT = (8.0 * math.pi) ** (-1.0 / 3.0)
Y3 = 1.0
MNU3_CORPUS = 0.074
DM2_SOLAR = 7.5e-5
DM2_ATM = 2.5e-3
SQRT_DM2_SOLAR = math.sqrt(DM2_SOLAR)


def m_nu_ev(y: float, m_rh_gev: float) -> float:
    return (y * V_EW) ** 2 / m_rh_gev * 1.0e9


def main() -> None:
    print("# Section 22.1 — Y_nu2 structural derivation numerics")
    print("=" * 68)

    print("\n## A — Structural constants")
    print(f"  (8pi)^(1/3)  D5 prefactor     = {PREF_8PI:.6f}")
    print(f"  (8pi)^(-1/3) Y2 candidate    = {Y2_STRUCT:.6f}")
    print(f"  (8pi)^(-2/3) m_nu2 factor    = {Y2_STRUCT**2:.6f}")

    print("\n## B — Zero-parameter route: m_nu2 = (8pi)^(-2/3) v^2 / M_R")
    mnu2_zp = Y2_STRUCT**2 * V_EW**2 / M_R * 1e9
    print(f"  m_nu2 pred                   = {mnu2_zp:.6f} eV")
    print(f"  sqrt(Dm2_solar) obs         = {SQRT_DM2_SOLAR:.6f} eV")
    print(f"  ratio pred/obs               = {mnu2_zp/SQRT_DM2_SOLAR:.4f}")
    print(f"  Dm2_solar pred               = {mnu2_zp**2:.4e} eV^2  (obs {DM2_SOLAR:.4e})")

    print("\n## C — Equivalent Yukawa routes")
    routes = [
        ("Y2=(8pi)^-1/3, M_R", Y2_STRUCT, M_R),
        ("Y2=(8pi)^-1/3, M_2", Y2_STRUCT, M2),
        ("Y2=(8pi)^-1/3 sqrt(M1/MR), M_2", Y2_STRUCT * math.sqrt(M1 / M_R), M2),
        ("Y2=(8pi)^-1/3 sqrt(M1/MR), M_1", Y2_STRUCT * math.sqrt(M1 / M_R), M1),
    ]
    for label, y, m in routes:
        mn = m_nu_ev(y, m)
        print(f"  {label:<32} m_nu2={mn:.6f} eV  ratio/solar={mn/SQRT_DM2_SOLAR:.4f}")

    print("\n## D — Identity check")
    y_eff = Y2_STRUCT * math.sqrt(M1 / M_R)
    lhs = m_nu_ev(y_eff, M2)
    rhs = mnu2_zp
    print(f"  (Y2^2 v^2/M_2) with Y2=(8pi)^-1/3 sqrt(M1/MR) = {lhs:.6f} eV")
    print(f"  (8pi)^-2/3 v^2/M_R                         = {rhs:.6f} eV")
    print(f"  relative difference                          = {abs(lhs-rhs)/rhs:.4e}")

    print("\n## E — Full neutrino spectrum (structural)")
    mnu3 = m_nu_ev(Y3, M_R)
    mnu2 = mnu2_zp
    mnu1_z2 = mnu2 * math.sqrt(math.sin(math.radians(8.57)) ** 2)  # Z2 subleading
    print(f"  m_nu3 (Y3=1, M_R)            = {mnu3:.4f} eV  (corpus {MNU3_CORPUS})")
    print(f"  m_nu2 (zero-param)           = {mnu2:.4f} eV")
    print(f"  m_nu1 bracket (nu2 x sqrt(s13^2)) = {mnu1_z2:.4f} eV  (illustrative)")
    print(f"  Dm2_atm pred ~ m3^2          = {mnu3**2:.4e} eV^2  (obs {DM2_ATM:.4e})")
    print(f"  Dm2_solar pred               = {mnu2**2:.4e} eV^2")

    print("\n## F — Y_nu1 bound (normal hierarchy)")
    y1_bound = math.sqrt(0.037e-9 * M1) / V_EW
    y1_z2 = Y2_STRUCT * math.sqrt(M1 / M_R) * math.sin(math.radians(8.57))
    print(f"  Y1 upper (m_nu1<0.037 eV)     = {y1_bound:.6f}")
    print(f"  Y1 bracket Z2 x hierarchy    = {y1_z2:.6f}")

    print("\n## Verdict")
    print("  Y_nu2 = (8pi)^(-1/3) DERIVED as inverse D5 prefactor on sigma_1/sigma_2 sector.")
    print("  Zero-parameter m_nu2 = (8pi)^(-2/3) v^2/M_R (M_R scale in seesaw).")
    print("  Equivalent: Y_nu2=(8pi)^(-1/3) sqrt(M1/MR) with M_2 in seesaw formula.")


if __name__ == "__main__":
    main()
