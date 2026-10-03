#!/usr/bin/env python3
"""J6-n4 / BR2d: y <-> N locking junction numerics (Jammer)."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_PL = 2.435e18  # reduced
M_NR = 1.221e19
G_EFF = 106.75
N_LOCK = 45.0 / (4.0 * G_EFF)  # S_dS/4
N_E = -math.log(ALPHA * M_NR)
PHI_RATIO = 15.9


def h_alpha() -> float:
    return ALPHA * M_NR**2


def h_friedmann_tgb() -> float:
    T = M_NR / math.sqrt(2 * math.pi)
    rho = (math.pi**2 / 30.0) * G_EFF * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M_NR**2)


def phi_stage3_y(y: float, phi0: float, n_lock: float = N_LOCK) -> float:
    """|Phi|^2(y) = (Phi0^2 e^{-N_lock}/N_lock) y  (audit linear profile)."""
    A = phi0**2 * math.exp(-n_lock) / n_lock
    return math.sqrt(max(A * y, 0.0))


def phi_sector2_N(N: float, h_hh: float = M_NR) -> float:
    """Role A constraint exponential: |Phi| = sqrt(H_HH/alpha) exp(-N/2)."""
    return math.sqrt(h_hh / ALPHA) * math.exp(-N / 2.0)


def h_sector2_N(N: float, h_hh: float = M_NR) -> float:
    return h_hh * math.exp(-N)


def phi_sector1_profile(N: float, ne: float, h_hh: float = M_NR) -> float:
    """C9 sqrt slow-roll H; phi from H=alpha phi^2 only if constraint on — not used for Role B."""
    return PHI_RATIO * M_PL  # constant excursion scale (J6-n1 T2)


def main() -> None:
    h_a = h_alpha()
    h_f = h_friedmann_tgb()
    phi0 = M_NR  # anchor Phi0 at Planck scale

    phi_y_end = phi_stage3_y(N_LOCK, phi0)
    phi_n_end = phi_sector2_N(N_E)
    h_n_end = h_sector2_N(N_E)

    print("# J6-n4 BR2d y <-> N junction numerics — Jammer")
    print(f"N_lock (y-axis) = {N_LOCK:.6f}")
    print(f"N_e (N-axis)    = {N_E:.4f}")
    print(f"Ratio N_e/N_lock = {N_E/N_LOCK:.2f}  [NOT a global scale factor]")
    print()

    print("## A — Coordinate orthogonality (default register)")
    print("  y in [0, N_lock]: Stage 3 profile / holographic width")
    print("  N in [0, N_e]:    cosmological inflation depth (Sector 1+2)")
    print("  Same numeric label 'e-fold' — different charts (BR2c Sector 0 vs 1/2).")
    print()

    print("## B — Junction event G (gauge birth) — simultaneous readings")
    print("| quantity | chart y=N_lock | chart N=N_e |")
    print("|----------|----------------|-------------|")
    print(f"| coord    | y = {N_LOCK:.4f} | N = {N_E:.2f} |")
    print(f"| |Phi|    | {phi_y_end:.3e} GeV | {phi_n_end:.3e} GeV |")
    print(f"| |Phi|/M_Pl,nr | {phi_y_end/M_NR:.4f} | {phi_n_end/M_NR:.4f} |")
    print(f"| H (const) | — | {h_n_end:.3e} GeV (Role A) |")
    print(f"| H^(F)     | {h_f:.3e} GeV (thermal) | same event |")
    print(f"| H^(alpha) | {h_a:.3e} GeV (constraint) | same event |")
    print(f"| T_GB      | M_Pl/sqrt(2pi) | same event |")
    print()

    print("## C — Stage 3 vs Sector 2 endpoint (continuity target)")
    match_phi = abs(phi_y_end / phi_n_end - 1.0)
    print(f"  |Phi|(y=N_lock) with Phi0=M_Pl,nr     = {phi_y_end:.4e} GeV")
    print(f"  |Phi|(N=N_e) Role A constraint       = {phi_n_end:.4e} GeV (= M_Pl,nr)")
    print(f"  Relative mismatch if Phi0=M_Pl,nr    = {match_phi:.4f}")
    phi0_adj = phi_n_end / math.sqrt(math.exp(-N_LOCK))
    print(f"  Phi0 adjusting match at G            = {phi0_adj:.4e} GeV ({phi0_adj/M_NR:.4f} M_Pl,nr)")
    print()

    print("## D — Proposed junction map (BR2d-J1, local, not global)")
    print("  Event identification: gauge birth G is ONE transition, TWO charts:")
    print("    y -> N_lock  AND  N -> N_e  (and N -> 0 for Role B slow-roll exit — see memo)")
    print("  No global y = (N_lock/N_e) N  (ratio ~600 — charts not linearly identified).")
    print("  Local C0: |Phi|^2(y) matches post-lock exponential at G with Phi0 calibrated.")
    print()

    print("## E — Sector 1 exit vs Sector 2 entry (Role B -> Role A handoff)")
    phi_b = PHI_RATIO * M_PL
    phi_a_hh = math.sqrt(M_NR / ALPHA)
    print(f"  Role B Phi_inf ~ {PHI_RATIO} M_Pl,red     = {phi_b:.3e} GeV")
    print(f"  Role A |Phi|(HH peak) sqrt(M_Pl/alpha) = {phi_a_hh:.3e} GeV")
    print(f"  Ratio B/A at HH                        = {phi_b/phi_a_hh:.3e}")
    print("  => Field map at lock is NOT magnitude identity (R4 open; Z2 portal route).")
    print()

    print("## F — Bridge identity check")
    print(f"  ln(H^(F)/H^(alpha)) = {math.log(h_f/h_a):.2f}")
    print(f"  N_e + 1             = {N_E + 1:.2f}")
    print("  => Thermal epoch sits ~1 e-fold above constraint depth in log-H (bridge v0.1).")
    print()

    print("## J6-n4 verdict")
    print("  BR2d-J1 junction event G specified; charts orthogonal by default.")
    print("  C0 Phi matching at G achievable with Phi0 ~ 1.05 M_Pl,nr (calibration, not derived).")
    print("  R4 field map remains OPEN; Sector handoff is sequential activation (BR2d-J2).")
    print("  Full derived map: Appendix B.3 / Paper S2 (BR2d-J3 programme).")


if __name__ == "__main__":
    main()
