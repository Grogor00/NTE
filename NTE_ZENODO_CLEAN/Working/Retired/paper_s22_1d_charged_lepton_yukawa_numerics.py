#!/usr/bin/env python3
"""Section 22.1d — charged lepton GUT ratio spot-check."""
from __future__ import annotations

# EW masses (GeV) — illustrative
M_E = 0.000511
M_MU = 0.1057
M_TAU = 1.777
M_D = 0.0047
M_S = 0.093
M_B = 4.18


def main() -> None:
    print("# Charged lepton — GUT ratio spot-check (EW scale)")
    print("=" * 60)

    r_tau_b = M_TAU / M_B
    r_mu_3s = M_MU / (3.0 * M_S)
    r_e_3d = M_E / (3.0 * M_D)

    print(f"  m_tau/m_b           = {r_tau_b:.4f}  (GUT target ~1)")
    print(f"  m_mu/(3*m_s)        = {r_mu_3s:.4f}  (GUT target ~1)")
    print(f"  m_e/(3*m_d)         = {r_e_3d:.4f}  (GUT target ~1)")

    print("\n## D5 parallel (neutrino anchor)")
    y2 = (8.0 * 3.14159265) ** (-1.0 / 3.0)
    print(f"  Y_nu2 = (8pi)^-1/3     = {y2:.6f}")
    print("  Y_e from same power without depth split -> FAIL as full closure")

    print("\n## Verdict")
    print("  GUT 1/3 rule: tau/b OK order; mu, e need RGE for real test.")
    print("  Full Y_e,Y_mu,Y_tau: Route L1 quick; L2-L4 programme.")


if __name__ == "__main__":
    main()
