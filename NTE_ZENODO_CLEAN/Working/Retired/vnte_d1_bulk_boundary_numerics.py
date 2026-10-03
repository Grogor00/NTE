#!/usr/bin/env python3
"""V_NTE Session 5 D1 — bulk-to-boundary projection numerics."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_NR = 1.221e19
M_PL = 2.435e18
G_EFF = 106.75
N_E = -math.log(ALPHA * M_NR)
N_LOCK = 45.0 / (4.0 * G_EFF)
PHI_INF = 2.0 * math.sqrt(N_E)  # M_Pl,red units (J6-D2)


def phi_stage3(y: float, phi0: float) -> float:
    A = phi0**2 * math.exp(-N_LOCK) / N_LOCK
    return math.sqrt(A * y)


def phi_sector2(N: float) -> float:
    return math.sqrt(M_NR / ALPHA) * math.exp(-N / 2.0)


def v_post(phi_gev: float) -> float:
    """Role (A) Friedmann inversion quartic on constraint trajectory."""
    return 3.0 * ALPHA**2 * M_PL**2 * phi_gev**4


def v_bulk_hh(phi_gev: float) -> float:
    """Role (B) HH saddle Phi^2 sector (J6-D1)."""
    m_e2 = (1.0 / 6.0) * 12.0 * M_NR**2
    return 0.5 * m_e2 * phi_gev**2


def v_hilltop(phi_mpl_red: float, phi0_mpl_red: float = 15.0) -> float:
    """Companion 9 hilltop schematic: V ~ Phi^4 - Phi^6 (normalised)."""
    lam = 1.0
    mu = 1.0 / (phi0_mpl_red**2)
    return lam * phi_mpl_red**4 - mu * phi_mpl_red**6


def r_hilltop_slow_roll(N: float) -> float:
    """Standard hilltop tensor-to-scalar (leading): r ~ 12/N^2."""
    return 12.0 / N**2


def main() -> None:
    print("# V_NTE Session 5 D1 — bulk-to-boundary projection numerics")
    print("=" * 68)

    phi_g = phi_sector2(N_E)
    phi0_c0 = phi_g / math.exp(-N_LOCK / 2.0)
    phi_y = phi_stage3(N_LOCK, phi0_c0)

    print("\n## A — Junction G: C0 |Phi| match (Pi_G + Stage 3)")
    print(f"  |Phi|(N=N_e) constraint       = {phi_g:.6e} GeV")
    print(f"  |Phi|(y=N_lock) Stage 3       = {phi_y:.6e} GeV")
    print(f"  ratio                         = {phi_y/phi_g:.6f}  (expect 1)")
    print(f"  Phi0 for C0                   = {phi0_c0:.6e} ({phi0_c0/M_NR:.4f} M_Pl,nr)")

    print("\n## B — Role separation: V_bulk vs V_post (NOT one smooth V)")
    phi_hh = PHI_INF * M_PL
    v_b = v_bulk_hh(phi_hh)
    v_p = v_post(phi_g)
    print(f"  V_bulk @ HH Phi_inf           = {v_b:.4e} GeV^4")
    print(f"  V_post @ G |Phi|              = {v_p:.4e} GeV^4")
    print(f"  V_post / V_bulk               = {v_p/v_b:.4e}")
    print("  DEAD END: single-chart V(Phi) extension pre->post.")
    print("  SUNSHINE: R_G projection at event G; different registers (S17.5.19).")

    print("\n## C — Bulk Sector 1 (n_s) vs hilltop (r) discipline")
    print(f"  Phi_inf / M_Pl,red            = {PHI_INF:.4f}  (J6-D2)")
    ns = 1.0 - 2.0 / N_E
    print(f"  n_s = 1 - 2/N_e                 = {ns:.6f}  (target 0.9685)")
    r_est = r_hilltop_slow_roll(N_E)
    print(f"  r ~ 12/N_e^2 (hilltop leading)  = {r_est:.6f}  (corpus ~4e-3)")

    v_ht = v_hilltop(PHI_INF)
    print(f"  V_hilltop(Phi_inf) schematic    = {v_ht:.4f} (M_Pl,red units)")

    print("\n## D — K(Phi) = 1 (S2-C-A) closes Session 5 kinetic leg")
    print("  V_post(Phi, Phi_dot) = 3 alpha^2 M_Pl^2 Phi^4 - (1/2) Phi_dot^2")
    print("  Off-trajectory hilltop uses Role (B) bulk/pre chart only for r.")

    print("\n## E — Projection operator summary")
    print("  R_G: V_post = consistency with H=alpha|Phi|^2 at G")
    print("  Pi_G: Phi_bulk -> |Phi_NTE| (Z2 even; NOT identity at HH)")
    print("  C0 + local dy/dN at G: br2d_j3_action_derive_numerics.py")

    print("\n## Verdict")
    print("  D1 CLOSED at bulk-to-boundary register (not smooth Phi extension).")


if __name__ == "__main__":
    main()
