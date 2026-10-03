#!/usr/bin/env python3
"""P-dS3: modular/dS scale consistency at H_GB^(F) (§22.8 / P0.10).

Checks F1 thickness ell=1/H against KMS beta_dS=2*pi/H and P-dS1/2
GH entropy / N_lock chain. Identification-layer numerics only — not TT proof.
"""

from __future__ import annotations

import math

M_PL_GEV = 1.221e19  # reduced Planck mass
G_EFF = 106.75


def h_gb_friedmann() -> float:
    """H_GB^(F) from audit (C1): H^2 = (pi * g_eff / 45) * M_Pl^2."""
    return math.sqrt(math.pi * G_EFF / 45.0) * M_PL_GEV


def main() -> None:
    h = h_gb_friedmann()
    ell = 1.0 / h
    beta_ds = 2.0 * math.pi / h  # KMS parameter candidate 1/T_dS, natural units
    s_gh = math.pi * M_PL_GEV**2 / h**2
    n_lock = s_gh / 4.0

    print("P-dS3 modular / dS scale check (H_GB^(F) route)")
    print("-" * 52)
    print(f"H_GB^(F)     = {h:.6e} GeV")
    print(f"ell = 1/H    = {ell:.6e} GeV^-1  (F1)")
    print(f"beta_dS      = {beta_ds:.6e} GeV^-1  (2*pi/H)")
    print(f"S_GH         = {s_gh:.6f}")
    print(f"N_lock = S/4 = {n_lock:.6f}")
    print(f"beta_dS/(2*pi*ell) = {beta_ds / (2.0 * math.pi * ell):.6f}  (expect 1)")
    print(f"N_lock/S_GH      = {n_lock / s_gh:.6f}  (expect 0.25)")

    # Corpus alpha route contrast (P-dS1 Route B FAIL)
    alpha_corpus = 2.38e-47
    h_alpha = alpha_corpus * M_PL_GEV**2
    print("-" * 52)
    print("Contrast H_GB^(alpha) = alpha * M_Pl^2 (incompatible with N_lock ~ 0.1):")
    print(f"H_GB^(alpha) = {h_alpha:.6e} GeV")
    print(f"S_GH         = {math.pi * M_PL_GEV**2 / h_alpha**2:.6e}")


if __name__ == "__main__":
    main()
