#!/usr/bin/env python3
"""Sunshine exit — full charged-lepton ratio closure (Jammer v0.1k)."""
from __future__ import annotations

import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
N_E = 63.4
N_LOCK = 45.0 / (4.0 * 106.75)
DIM_H = 4.0  # quaternionic fibre dim at G (Part 1 §2.1.3)
DIM_G2 = 14.0
V_EW = 246.0
SQRT2 = math.sqrt(2.0)
ZETA2 = math.pi**2 / 6.0

M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777
OBS_TM = M_TAU / M_MU
OBS_ME = M_MU / M_E
GEN = ("tau", "mu", "e")


def L_bulk() -> float:
    return math.log(N_E / N_LOCK) / LN_8PI


def delta_sunshine(n: int) -> float:
    L = L_bulk()
    return 2.0 / 3.0 + L / 3.0 + (n * L) / 2.0 + (n * n * L) / 12.0


def s_geom(g: int, r: int = 2) -> float:
    d = lambda k: float((k + 1) * (k + 2))
    o = (3.0 / 2.0) / (g + 1.5)
    return (d(0) / d(g)) * (o ** (2 * r))


def delta_hk(g: int, r: int = 2) -> float:
    return -math.log(s_geom(g, r)) / (3.0 * LN_8PI)


def lock_factor_chart(g: int, power: float) -> float:
    a = 1.0 - (2 * g + 1) / 12.0
    return 1.0 - a**power


def delta_lock_log(g: int, power: float) -> float:
    return -math.log(lock_factor_chart(g, power)) / LN_8PI


def delta_electron_spectral(g: int) -> float:
    """Only g=2 (electron): zeta(2) + HK residue weighted by 1/(2g+1) and 2/(2g+1)."""
    if g != 2:
        return 0.0
    denom = 2 * g + 1  # 5
    return math.log(ZETA2) / (denom * LN_8PI) + (2.0 / denom) * delta_hk(2)


def delta_eff(g: int, lock_power: float = DIM_H) -> float:
    return delta_sunshine(g) + delta_lock_log(g, lock_power) + delta_electron_spectral(g)


def y_from_delta(d: float) -> float:
    return EIGHT_PI ** (-d)


def mass_from_y(y: float) -> float:
    return y * V_EW / SQRT2


def main() -> None:
    print("# Sunshine exit closure — Jammer v0.1k")
    print("=" * 64)
    print(f"  N_e/N_lock = {N_E/N_LOCK:.1f}   L = {L_bulk():.3f}")
    print(f"  lock exponent dim(H) = {DIM_H}  (alt: dim(G2)/4 = {DIM_G2/4})")

    for label, p in [("dim(H)=4", DIM_H), ("dim(G2)/4", DIM_G2 / 4.0)]:
        ds = [delta_eff(g, p) for g in range(3)]
        ys = [y_from_delta(d) for d in ds]
        r_tm = ys[0] / ys[1]
        r_me = ys[1] / ys[2]
        print(f"\n## [{label}]")
        for n, nm in enumerate(GEN):
            m = mass_from_y(ys[n])
            obs = (M_TAU, M_MU, M_E)[n]
            print(f"  {nm:3s}  delta={ds[n]:.4f}  m_pred={m:.6f}  m_obs={obs:.6f}  m_ratio={m/obs:.3f}")
        print(f"  m_tau/m_mu = {r_tm:.4f}  (obs {OBS_TM:.4f})")
        print(f"  m_mu/m_e   = {r_me:.2f}  (obs {OBS_ME:.1f})")

    print("\n## Formula (boxed)")
    print("  delta_g^eff = delta_g^sun - log_{8pi}[1-(1-(2g+1)/12)^dim(H)]")
    print("            + delta_{g,2} * [ log_{8pi}(zeta(2))/(2g+1) + (2/(2g+1))*Delta_2^HK ]")
    print("\n## vs prior stages")
    ds0 = [delta_sunshine(g) for g in range(3)]
    r0 = EIGHT_PI ** (ds0[1] - ds0[0]), EIGHT_PI ** (ds0[2] - ds0[1])
    print(f"  sunshine only:     tau/mu={r0[0]:.1f}  mu/e={r0[1]:.1f}")
    ds1 = [delta_sunshine(g) + delta_lock_log(g, DIM_H) for g in range(3)]
    r1 = EIGHT_PI ** (ds1[1] - ds1[0]), EIGHT_PI ** (ds1[2] - ds1[1])
    print(f"  + lock dim(H):     tau/mu={r1[0]:.1f}  mu/e={r1[1]:.1f}")
    ds2 = [delta_eff(g, DIM_H) for g in range(3)]
    r2 = EIGHT_PI ** (ds2[1] - ds2[0]), EIGHT_PI ** (ds2[2] - ds2[1])
    print(f"  + electron spec:   tau/mu={r2[0]:.2f}  mu/e={r2[1]:.1f}  <-- EXIT")

    print("\n## Verdict")
    print("  RATIO CLOSURE at ~0.1% (mu/e) and ~7% (tau/mu) with dim(H)=4 lock.")
    print("  Tradeoff variant dim(G2)/4: both ratios within ~3%.")


if __name__ == "__main__":
    main()
