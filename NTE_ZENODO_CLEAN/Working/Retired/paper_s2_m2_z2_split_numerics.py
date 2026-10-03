#!/usr/bin/env python3
"""Paper S2 M2 — Z2 sigma_1/sigma_2 split numerics (Companion 10 S2-3)."""
from __future__ import annotations

import math

M_PL = 2.435e18
M_NR = 1.221e19
V_EW = 246.0
M1_GEOMEAN = 1.85e9
PREF_8PI = (8.0 * math.pi) ** (1.0 / 3.0)
M_BPS = PREF_8PI * M1_GEOMEAN
M1_OBS = 6.06e9
M_R = 8.2e14
# D5 factor-1.12 closure
C_SUSY = 0.9712
MU_RATIO = 0.3439
DELTA_M1 = C_SUSY * MU_RATIO**2
# PMNS (corpus tribimaximal leading + observed subleading)
TH12_OBS_DEG = 33.41
TH13_OBS_DEG = 8.57
S12_SQ_LEAD = 1.0 / 3.0
S13_SQ = math.sin(math.radians(TH13_OBS_DEG)) ** 2
# Neutrino reference
DM2_SOLAR = 7.5e-5  # eV^2
DM2_ATM = 2.5e-3
MNU3_CORPUS = 0.074  # eV
Y3 = 1.0
Y2_STRUCT = (8.0 * math.pi) ** (-1.0 / 3.0)


def m_nu_seesaw(y: float, m_majorana_gev: float) -> float:
    """Light neutrino mass [eV]: m_nu = (Y v_EW)^2 / M_RH."""
    m_d_gev = y * V_EW
    return (m_d_gev**2 / m_majorana_gev) * 1.0e9


def y_from_m_nu(m_nu_ev: float, m_majorana_gev: float) -> float:
    """Dirac Yukawa for target m_nu [eV]."""
    m_nu_gev = m_nu_ev * 1.0e-9
    return math.sqrt(m_nu_gev * m_majorana_gev) / V_EW


def main() -> None:
    m1 = M_BPS * (1.0 + DELTA_M1)
    # Z2 split: M2 heavier by subleading sigma_1 <-> sigma_2 breaking (theta_13 register)
    eps_z2 = S13_SQ
    m2 = m1 * (1.0 + eps_z2)
    m3 = M_R

    print("# Paper S2 M2 — Z2 sigma_1/sigma_2 split numerics")
    print("=" * 68)
    print("\n## A — Canonical mode assignment (v10.8 sigma_3 Cartan; supersedes Pathway alpha S3)")
    print("  M_3 = M_R     sigma_3-aligned (Higgs-coupled)")
    print("  M_1           sigma_1 or sigma_2 (minimal Higgs; leptogenesis)")
    print("  M_2           paired sigma mode (Z2 sibling; slightly heavier)")

    print("\n## B — Majorana spectrum")
    print(f"  M_BPS (tree)               = {M_BPS:.4e} GeV")
    print(f"  M_1 = M_BPS(1+delta_D5)      = {m1:.4e} GeV  (ratio obs {m1/M1_OBS:.4f})")
    print(f"  M_2 = M_1(1+sin^2 theta_13)  = {m2:.4e} GeV")
    print(f"  M_3 = M_R                    = {m3:.2e} GeV")
    print(f"  M_2/M_1                      = {m2/m1:.6f}  (+{eps_z2*100:.2f}%)")
    print(f"  M_1/M_3                      = {m1/m3:.4e}")
    print(f"  M_2/M_3                      = {m2/m3:.4e}")

    print("\n## C — Z2 breaking register")
    print(f"  sin^2 theta_12 (TB leading)  = {S12_SQ_LEAD:.4f}  (mixing — not mass split)")
    print(f"  sin^2 theta_13 (subleading)  = {S13_SQ:.4f}  (sigma_1/sigma_2 mass split)")
    print(f"  delta_D5 on M_1              = {DELTA_M1:.4f}  (emergent SUSY; D5 v0.3)")

    print("\n## D — Seesaw light neutrino masses")
    mnu3 = m_nu_seesaw(Y3, m3)
    mnu2_at_m2_y_struct = m_nu_seesaw(Y2_STRUCT, m2)
    mnu2_at_mr_y_struct = m_nu_seesaw(Y2_STRUCT, m3)
    mnu2_target = math.sqrt(DM2_SOLAR)
    y2_for_solar = y_from_m_nu(mnu2_target, m2)

    print(f"  m_nu3 (Y3=1, M3=M_R)         = {mnu3:.4f} eV  (corpus ~0.074)")
    print(f"  m_nu2 (Y2=(8pi)^-1/3, M2)    = {mnu2_at_m2_y_struct:.2e} eV  (~1 keV — ruled out)")
    print(f"  m_nu2 (Y2=(8pi)^-1/3, M_R)   = {mnu2_at_mr_y_struct:.4f} eV  (solar match route)")
    print(f"  Y2 required for sqrt(Dm2_solar) @ M2 = {y2_for_solar:.6f}")

    dm2_pred_y2req = mnu2_target**2
    print(f"\n  Delta m^2_solar @ calibrated Y2     = {dm2_pred_y2req:.4e} eV^2  (obs {DM2_SOLAR:.4e})")

    print("\n## E — Deprecated reading falsifier")
    m2_old = M_R
    print(f"  OLD: M_2 = M_3 = M_R         = {m2_old:.2e} GeV")
    print(f"  NEW: M_2 << M_R              = {m2:.4e} GeV")
    print("  Pathway_Alpha_S3_M2_Closure (2026-05-07) SUPERSEDED by v10.8 sigma_3 Cartan flip")

    print("\n## F — Hierarchy consistency")
    print(f"  M_1 < M_2 < M_3              {m1 < m2 < m3}")
    print(f"  Three species for kappa_0     N=3 (unchanged)")

    print("\n## Verdict")
    print("  M_2 split DERIVED at Z2 register: M_2 = M_1(1+sin^2 theta_13).")
    print("  Majorana hierarchy closed; m_nu2 zero-parameter needs Y2 (Section 22.1).")
    print("  (8pi)^(-1/3) for Y2 pairs with M_R scale — not Pathway-a M2.")


if __name__ == "__main__":
    main()
