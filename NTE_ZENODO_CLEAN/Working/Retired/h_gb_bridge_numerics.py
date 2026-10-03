#!/usr/bin/env python3
"""H_GB bridge numerics — three-epoch timeline (Impact #1)."""
from __future__ import annotations

import math

ALPHA = 2.38e-47  # GeV^-1
M_PL = 1.221e19  # GeV non-reduced (corpus §18.2)
G_EFF = 106.75
SQRT_2PI = math.sqrt(2 * math.pi)


def h_friedmann(T: float, g: float, M: float) -> float:
    rho = (math.pi**2 / 30.0) * g * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M**2)


def main() -> None:
    h_alpha = ALPHA * M_PL**2
    t_gb = M_PL / SQRT_2PI
    h_f = h_friedmann(t_gb, G_EFF, M_PL)
    h_hh = M_PL  # natural HH upper bound (§18.2)

    n_e = math.log(M_PL / h_alpha)
    s_ds = math.pi * M_PL**2 / h_f**2
    n_lock = s_ds / 4.0

    log_ratio_ff = math.log(h_f / h_alpha)
    log_ratio_hh = math.log(h_hh / h_alpha)

    print("H_GB bridge — three-epoch timeline (v0.1)")
    print("=" * 58)
    print("\n## Epoch labels (NOT equal)")
    print(f"H_GB^(alpha)  constraint at locking     = {h_alpha:.4e} GeV")
    print(f"H_GB^(F)      Friedmann at T_GB         = {h_f:.4e} GeV")
    print(f"H_HH          HH upper bound (§18.2)    = {h_hh:.4e} GeV")
    print(f"Ratio H^(F) / H^(alpha)               = {h_f/h_alpha:.4e}")
    print(f"Ratio H_HH / H^(alpha)                = {h_hh/h_alpha:.4e}")
    print(f"\n## Epoch B — inflation e-folds (§18.2)")
    print(f"N_e = ln(M_Pl / H^(alpha))            = {n_e:.2f}")
    print(f"N_e = ln(H_HH / H^(alpha))            = {log_ratio_hh:.2f}")
    print(f"\n## Epoch A — thermal horizon (audit C1+C2)")
    print(f"T_GB = M_Pl/sqrt(2pi)                 = {t_gb:.4e} GeV ({t_gb/M_PL:.4f} M_Pl)")
    print(f"S_dS = pi M_Pl^2 / H^(F)^2            = {s_ds:.6f}")
    print(f"N_lock = S_dS/4                       = {n_lock:.6f}")
    print(f"45/(4 g_eff)                          = {45/(4*G_EFF):.6f}")
    print(f"\n## Bridge gaps (open)")
    print(f"ln(H^(F)/H^(alpha))                   = {log_ratio_ff:.2f}  (thermal->locking)")
    print(f"N_e - ln(H^(F)/H^(alpha))            = {n_e - log_ratio_ff:.2f}  (HH->thermal?)")
    print(f"N_lock vs N_e                         = {n_lock:.4f} vs {n_e:.2f}  (different roles)")
    print("\n## Falsifier check")
    print("Forced H^(alpha)=H^(F) breaks N_e OR N_lock — excluded.")
    print("alpha_req for H^(alpha)=H^(F):",
          f"{math.sqrt(math.pi * G_EFF / (45 * M_PL**2)):.4e} GeV^-1",
          f"(corpus alpha {ALPHA:.4e})")


if __name__ == "__main__":
    main()
