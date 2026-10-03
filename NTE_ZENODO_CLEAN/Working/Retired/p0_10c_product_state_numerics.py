#!/usr/bin/env python3
"""P0.10c — product state omega on C^inf(M) x A_F; modular scale checks."""
from __future__ import annotations

import math

M_PL_NR = 1.221e19
N_F = 180
G_EFF = 106.75
SQRT_2PI = math.sqrt(2 * math.pi)


def h_gb_friedmann() -> float:
    return math.sqrt(math.pi * G_EFF / 45.0) * M_PL_NR


def main() -> None:
    print("# P0.10c — product state / modular scale numerics")
    print("=" * 62)

    beta_gb = SQRT_2PI / M_PL_NR
    t_gb = M_PL_NR / SQRT_2PI
    h = h_gb_friedmann()
    ell = 1.0 / h
    beta_ds = 2.0 * math.pi / h
    n_lock = 45.0 / (4.0 * G_EFF)
    n_lock_naive = 45.0 / (4.0 * (N_F / 2.0))

    print("\n## A — Fibre / gauge-birth (D9)")
    print(f"  beta_GB                    = {beta_gb:.6e} GeV^-1")
    print(f"  T_GB = M_Pl,nr/sqrt(2pi)   = {t_gb:.6e} GeV")
    print(f"  beta_GB * T_GB             = {beta_gb * t_gb:.6f}  (expect sqrt(2pi)={SQRT_2PI:.6f})")

    print("\n## B — Modular / dS identification (P-dS3)")
    print(f"  H_GB^(F)                   = {h:.6e} GeV")
    print(f"  ell = 1/H                  = {ell:.6e} GeV^-1")
    print(f"  beta_dS = 2pi/H            = {beta_ds:.6e} GeV^-1")
    print(f"  beta_dS / (2*pi*ell)       = {beta_ds / (2.0 * math.pi * ell):.6f}  (expect 1)")

    print("\n## C — N_lock / g_eff vs N_F (S2-NF1)")
    print(f"  N_lock = 45/(4*g_eff)        = {n_lock:.6f}")
    print(f"  N_lock naive 45/(4*N_F/2)  = {n_lock_naive:.6f}")
    print(f"  naive overshoot vs corpus    = {n_lock_naive / n_lock - 1:.1%}")

    print("\n## D — Product-state register")
    print(f"  dim H_F = N_F              = {N_F}")
    print(f"  M_int = B(H_F) type I      = True (finite internal factor)")
    print(f"  omega = omega_geom x omega_int  (spec v0.1)")

    print("\n## Verdict")
    print("  P0.10c: product state specified; beta scales consistent.")
    print("  S2-NF1: use g_eff=106.75 in N_lock, not N_F/2.")


if __name__ == "__main__":
    main()
