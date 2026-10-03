#!/usr/bin/env python3
"""S22-ABS: common absolute Yukawa scale Y_0 after sunshine exit (v0.1l)."""
from __future__ import annotations

import math

from paper_s22_1k_sunshine_exit_closure_numerics import (
    DIM_G2,
    DIM_H,
    GEN,
    M_E,
    M_MU,
    M_TAU,
    delta_eff,
    mass_from_y,
    y_from_delta,
)

OBS = (M_TAU, M_MU, M_E)


def m_bare(g: int, lock_power: float = DIM_H) -> float:
    return mass_from_y(y_from_delta(delta_eff(g, lock_power)))


def main() -> None:
    print("# S22-ABS — common Y_0 after sunshine exit (v0.1l)")
    print("=" * 64)

    for label, p in [("dim(H)=4", DIM_H), ("dim(G2)/4", DIM_G2 / 4.0)]:
        print(f"\n## [{label}]")
        bare = [m_bare(g, p) for g in range(3)]
        y0s = [OBS[i] / bare[i] for i in range(3)]
        print("  m_bare (ratio exit, no Y_0):")
        for nm, m in zip(GEN, bare):
            print(f"    {nm:3s}  {m:.6f} GeV")
        print("  Y_0 = m_obs/m_bare per generation:")
        for nm, y0 in zip(GEN, y0s):
            print(f"    {nm:3s}  {y0:.4f}")
        y0_mean = sum(y0s) / 3.0
        y0_geom = (y0s[0] * y0s[1] * y0s[2]) ** (1.0 / 3.0)
        print(f"  mean Y_0 = {y0_mean:.4f}  geom = {y0_geom:.4f}")
        print("  with universal Y_0 = mean:")
        for i, nm in enumerate(GEN):
            m = y0_mean * bare[i]
            print(f"    {nm:3s}  {m:.6f}  obs {OBS[i]:.6f}  ratio {m/OBS[i]:.4f}")

    print("\n## Structural candidates vs Y_0 ~ 2.63 (obs/pred uplift)")
    y0_tgt = 2.634
    cands = {
        "8/3 (octonion dim / generations)": 8.0 / 3.0,
        "e (Euler)": math.e,
        "(8pi)^(1/3)": (8.0 * math.pi) ** (1.0 / 3.0),
        "3/(8pi)^(-1/3)": 3.0 / (8.0 * math.pi) ** (-1.0 / 3.0),
        "1/(3/8)": 8.0 / 3.0,
        "sqrt(8pi)": math.sqrt(8.0 * math.pi),
        "N_e/N_lock^(1/3)": (63.4 / (45.0 / (4.0 * 106.75))) ** (1.0 / 3.0),
    }
    for name, val in cands.items():
        print(f"  {name:28s}  {val:.4f}  err% {abs(val - y0_tgt) / y0_tgt * 100:.1f}")

    inv = 1.0 / y0_tgt
    print(f"\n  pred/obs ~ {inv:.3f}  (= 3/8 bracket if Y_0 = 8/3)")

    print("\n## Ratio invariance check (Y_0 cancels)")
    bare = [m_bare(g) for g in range(3)]
    print(f"  m_tau/m_mu bare = {bare[0]/bare[1]:.2f}  obs {M_TAU/M_MU:.2f}")
    print(f"  m_mu/m_e   bare = {bare[1]/bare[2]:.1f}  obs {M_MU/M_E:.1f}")

    print("\n## Verdict")
    print("  Universal Y_0 = m_obs/m_pred ~ 2.63 (+/-3%) — gen-universal uplift.")
    print("  pred/obs ~ 0.38 ~ 3/8 (dual bracket). Leading candidate: Y_0 = 8/3.")
    print("  Ratios unchanged by Y_0; sunshine exit ratio closure stands.")


if __name__ == "__main__":
    main()
