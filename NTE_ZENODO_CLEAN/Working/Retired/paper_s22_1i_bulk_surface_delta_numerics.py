#!/usr/bin/env python3
"""Sunshine: bulk-to-surface embedding depth at gauge birth G."""
from __future__ import annotations

import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
V_EW = 246.0
SQRT2 = math.sqrt(2.0)

# Corpus registers (Part 3 / BR5 / audit)
N_E = 63.4
N_LOCK = 45.0 / (4.0 * 106.75)  # ~0.1054
G_EFF = 106.75

M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777

GEN = ("tau", "mu", "e")


def L_bulk_surface() -> float:
    """log_{8pi}(N_e / N_lock)."""
    return math.log(N_E / N_LOCK) / LN_8PI


def delta_sunshine(n: int) -> float:
    """Bulk-surface sunshine formula (Jammer derive v0.1i)."""
    L = L_bulk_surface()
    return 2.0 / 3.0 + L / 3.0 + (n * L) / 2.0 + (n * n * L) / 12.0


def y_from_delta(d: float) -> float:
    return EIGHT_PI ** (-d)


def main() -> None:
    print("# Sunshine — bulk pre-temporal / surface temporal delta_n")
    print("=" * 60)
    print(f"  N_e = {N_E}   N_lock = {N_LOCK:.4f}   N_e/N_lock = {N_E/N_LOCK:.1f}")
    print(f"  L = log_8pi(N_e/N_lock) = {L_bulk_surface():.3f}")

    obs_d = {n: -math.log(SQRT2 * m / V_EW) / LN_8PI for n, m in zip(GEN, (M_TAU, M_MU, M_E))}

    print("\n## Observed vs sunshine delta")
    for i, nm in enumerate(GEN):
        d = delta_sunshine(i)
        print(f"  {nm:3s}  pred delta={d:.3f}  obs={obs_d[nm]:.3f}  ratio={d/obs_d[nm]:.3f}")

    print("\n## Mass ratios (m ~ Y v/sqrt2, Y ~ (8pi)^-delta)")
    dt, dm, de = [delta_sunshine(i) for i in range(3)]
    r_mt = EIGHT_PI ** (dm - dt)  # m_tau/m_mu
    r_me = EIGHT_PI ** (de - dm)  # m_mu/m_e
    r_et = EIGHT_PI ** (de - dt)  # m_e/m_tau
    print(f"  pred m_tau/m_mu = {r_mt:.1f}  (obs {M_TAU/M_MU:.1f})")
    print(f"  pred m_mu/m_e   = {r_me:.1f}  (obs {M_MU/M_E:.1f})")
    print(f"  pred m_e/m_tau  = {r_et:.1f}  (obs {M_E/M_TAU:.4f})")

    print("\n## Composite: sunshine delta + GUT colour (L1) at M_GUT=2e16")
  # tau anchor: m ~ Y^2 v^2; only check order
    y_tau = y_from_delta(dt)
    y_mu = y_from_delta(dm)
    y_e = y_from_delta(de)
    print(f"  Y_tau:Y_mu:Y_e = {y_tau:.3e}:{y_mu:.3e}:{y_e:.3e}")

    print("\n## Coefficient rationale (structural)")
    print("  2/3     G2 singlet (L2)")
    print("  L/3     bulk->surface at G (same N_e,N_lock as n_s, Lambda)")
    print("  nL/2    half lock-step per generation (dim su(2)=3)")
    print("  n^2L/12 4 spinor * 3 gen on S^3 Casimir weight")

    print("\n## Verdict")
    print("  SUNSHINE: delta magnitudes ~10-20% at zero extra params.")
    print("  Ratios: sunshine m_mu/m_e ~ 122 (not 13); see paper_s22_1j_yeff_stage3_numerics.py")


if __name__ == "__main__":
    main()
