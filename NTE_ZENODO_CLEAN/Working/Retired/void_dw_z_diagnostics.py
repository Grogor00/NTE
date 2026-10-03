#!/usr/bin/env python3
"""Void / delta-w diagnostics — Impact #3 (§17.5.12 b)."""
from __future__ import annotations

import math

OM_R, OM_M, OM_L = 9e-5, 0.315, 0.685
SIGMA8_0 = 0.811
B_ILLUST = 0.055  # NOT fitted — Jammer to derive
Z_CUT = 0.85


def E(z: float) -> float:
    return math.sqrt(OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3 + OM_L)


def omega_lambda(z: float) -> float:
    num = OM_L
    den = OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3 + OM_L
    return num / den


def sigma8_ratio_sq(z: float) -> float:
    g = E(z) / E(0)
    s8_z = SIGMA8_0 * g / (1 + z)
    return (s8_z / SIGMA8_0) ** 2


def delta_h_over_h(z: float) -> float:
    if z > Z_CUT:
        return 0.0
    return B_ILLUST * sigma8_ratio_sq(z) * omega_lambda(z) / omega_lambda(0)


def w_eff_proxy(z: float) -> float:
    """Exploratory: w_eff from delta H bias (not derived from action)."""
    dh = delta_h_over_h(z)
    if dh <= 0:
        return -1.0
    om_m = OM_M * (1 + z) ** 3
    om_l = OM_L
    frac = om_m / (om_m + om_l + OM_R * (1 + z) ** 4)
    return -1.0 + (2.0 / 3.0) * dh * frac


def main() -> None:
    print("Void / delta-w diagnostics (Impact #3 v0.1)")
    print(f"b={B_ILLUST} illustrative, z_cut={Z_CUT}")
    print("-" * 62)
    print(f"{'z':>6} {'dH/H':>10} {'w_eff':>10} {'s8^2/s8_0^2':>12} {'OmL/OmL0':>10}")
    for z in [0.0, 0.3, 0.51, 0.71, 0.85, 0.93, 1.1, 1.32]:
        dh = delta_h_over_h(z)
        w = w_eff_proxy(z)
        print(
            f"{z:6.2f} {dh:10.5f} {w:10.5f} "
            f"{sigma8_ratio_sq(z):12.4f} {omega_lambda(z)/omega_lambda(0):10.4f}"
        )
    print("-" * 62)
    print("Diagnostic (b): dH/H -> 0 by z~z_cut; w_eff -> -1 at high z.")
    print("Jammer: replace b with tracer-weighted void model; joint DESI covariances.")


if __name__ == "__main__":
    main()
