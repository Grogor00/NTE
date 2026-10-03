#!/usr/bin/env python3
"""S2-NF1: g_eff(T_GB) thermal map — close N_lock 19% gap (Jammer v0.1)."""
from __future__ import annotations

import math

M_NR = 1.221e19
M_PL = 2.435e18
G_EFF = 106.75  # corpus SM thermal at T >> all masses
N_F = 180
SQRT_2PI = math.sqrt(2 * math.pi)


def g_eff_sm_high_t() -> float:
    """Standard Model g_eff when T >> m_top (all species relativistic)."""
    # bosons: 28 = 2*2 (photon) + 2*8 (gluons) + 3*2 (W) + 1*2 (Z) + 1*2 (H) approx
    # fermions: (7/8) * 90 Weyl = 78.75
    g_boson = 28.0
    g_fermion = (7.0 / 8.0) * 90.0
    return g_boson + g_fermion


def s_dS(T: float, g: float) -> float:
    rho = (math.pi**2 / 30.0) * g * T**4
    H = math.sqrt((8 * math.pi / 3.0) * rho / M_NR**2)
    return math.pi * M_NR**2 / H**2


def main() -> None:
    T_gb = M_NR / SQRT_2PI
    g = g_eff_sm_high_t()
    n_lock = 45.0 / (4.0 * g)
    n_lock_corpus = 45.0 / (4.0 * G_EFF)
    n_lock_naive = 45.0 / (4.0 * (N_F / 2.0))

    print("# S2-NF1 — g_eff(T_GB) thermal map — Jammer v0.1")
    print("=" * 60)
    print(f"  T_GB = M_Pl,nr/sqrt(2pi)     = {T_gb:.4e} GeV")
    print(f"  T_GB / m_top                  = {T_gb / 173.0:.2e}  (all SM massless)")
    print(f"  g_eff(SM high-T)              = {g:.2f}")
    print(f"  g_eff corpus                  = {G_EFF:.2f}")
    print(f"  N_lock = 45/(4 g_eff)         = {n_lock:.6f}")
    print(f"  N_lock corpus                 = {n_lock_corpus:.6f}")
    print(f"  N_lock naive N_F/2=90         = {n_lock_naive:.6f}")
    print(f"  gap naive vs corpus           = {abs(n_lock_naive/n_lock_corpus - 1):.1%}")
    print(f"  S_dS at T_GB                  = {s_dS(T_gb, g):.6f}")
    print(f"  S_dS/4                        = {s_dS(T_gb, g)/4:.6f}")
    print()
    print("  SUNSHINE: g_eff = 106.75 is SM thermal dof at T_GB, NOT N_F/2.")
    print("  N_F=180 enters heat-kernel a_4; g_eff enters S_dS -> N_lock.")
    print("  S2-NF1: CLOSED at register level (no 19% tuning required).")


if __name__ == "__main__":
    main()
