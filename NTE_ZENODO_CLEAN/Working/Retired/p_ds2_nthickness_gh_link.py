#!/usr/bin/env python3
"""P-dS2 — link F1 ell=1/H to Gibbons-Hawking entropy (gauge-birth horizon)."""
from __future__ import annotations

import math

M_PL = 1.221e19  # GeV corpus
G_EFF = 106.75
ALPHA = 2.38e-47
BETA_GB = math.sqrt(2 * math.pi) / (2.435e18)


def s_gh(H_gev: float, M_pl: float) -> float:
    return math.pi * M_pl**2 / H_gev**2


def h_friedmann(M_pl: float, g_eff: float) -> float:
    T = M_pl / math.sqrt(2 * math.pi)
    rho = (math.pi**2 / 30.0) * g_eff * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M_pl**2)


def main() -> None:
    H_F = h_friedmann(M_PL, G_EFF)
    H_alpha = ALPHA * M_PL**2

    ell_F = 1.0 / H_F
    ell_alpha = 1.0 / H_alpha

    S_F = s_gh(H_F, M_PL)
    S_alpha = s_gh(H_alpha, M_PL)
    N_lock = 45.0 / (4.0 * G_EFF)

    print("# P-dS2 — N-thickness (F1) vs Gibbons-Hawking entropy")
    print()
    print("## F1 identity: ell = 1/H  (same as Hubble radius in natural units)")
    print()
    print("| scale | H [GeV] | ell=1/H [GeV^-1] | S_GH=pi M^2/H^2 |")
    print("|-------|---------|------------------|-----------------|")
    print(f"| H_GB^(F) Friedmann | {H_F:.4e} | {ell_F:.4e} | {S_F:.6f} |")
    print(f"| H_GB^(alpha) lock  | {H_alpha:.4e} | {ell_alpha:.4e} | {S_alpha:.4e} |")
    print(f"| H0 ~ alpha v_EW^2  | {ALPHA * 246**2:.4e} | — | — |")
    print()
    print("## N_lock / thickness programme (audit C2)")
    print(f"S_dS (Friedmann)     = {S_F:.6f}")
    print(f"N_lock = S_dS/4      = {N_lock:.6f}")
    print(f"N_lock = 45/(4 g)    = {45/(4*G_EFF):.6f}")
    print()
    print("## Structural link (programme — not derived)")
    print(f"ell(H_GB^(F)) * H_GB^(F) = 1  (F1)")
    print(f"S_GH * H^2 / M_Pl^2 = pi     (GH definition)")
    print(f"N_lock / S_GH = {N_lock/S_F:.6f} = 1/4  (C2 candidate)")
    print()
    print("Reading: GH entropy at Friedmann gauge-birth horizon pairs with")
    print("N-thickness depth N_lock = quarter of S_dS; alpha-route H gives wrong S_GH.")
    print("P-dS2 does NOT close dS/CFT — only F1+GH+audit consistency at H_GB^(F).")


if __name__ == "__main__":
    main()
