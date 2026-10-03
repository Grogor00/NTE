#!/usr/bin/env python3
"""P3: homogeneous LambdaCDM linear growth (Planck 2018 Omegas).

NTE homogeneous limit: same H(z) as P1/P2 -> same D(z), sigma8(z), f sigma8(z).
No global chi2; exploratory offset vs published DESI RSD bins.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp

OM_R = 9.0e-5
OM_M = 0.315
OM_L = 0.685
SIGMA8_0 = 0.811  # Planck 2018 TT,TE,EE+lowE+lensing

# DESI 2024 BAO+RSD (approx. central values for worksheet offset; not fitted)
DESI_FSIG8 = {
    0.51: (0.457, 0.033),
    0.71: (0.454, 0.030),
    0.93: (0.448, 0.028),
    1.32: (0.434, 0.032),
}


def h_ratio(a: float) -> float:
    return math.sqrt(OM_R * a ** -4 + OM_M * a ** -3 + OM_L)


def omega_m(a: float) -> float:
    h2 = OM_R * a ** -4 + OM_M * a ** -3 + OM_L
    return OM_M * a ** -3 / h2


def growth_rhs(lna: float, y: np.ndarray) -> np.ndarray:
    """ODE in x = ln(a): y = [D, dD/dx]."""
    a = math.exp(lna)
    h = h_ratio(a)
    om = omega_m(a)
    # d ln h / d ln a = (a/h) dh/da
    dh_da = 0.5 / h * (-4 * OM_R * a ** -5 - 3 * OM_M * a ** -4)
    dlna_h = a * dh_da / h
    d, dp = y
    d2 = -(2.0 + dlna_h) * dp + 1.5 * om * d
    return np.array([dp, d2])


def integrate_growth(a_ini: float = 1e-3) -> tuple[np.ndarray, np.ndarray]:
    lna_ini = math.log(a_ini)
    lna_end = 0.0  # a = 1
    y0 = np.array([a_ini, a_ini])  # D ~ a in matter domination
    sol = solve_ivp(
        growth_rhs,
        (lna_ini, lna_end),
        y0,
        method="DOP853",
        rtol=1e-10,
        atol=1e-12,
        dense_output=True,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    lna_grid = np.linspace(lna_ini, lna_end, 4000)
    y = sol.sol(lna_grid)
    d = y[0]
    d_norm = d / d[-1]
    return np.exp(lna_grid), d_norm


@dataclass
class GrowthRow:
    z: float
    d: float
    f: float
    sigma8: float
    fsig8: float


def interp_at_z(a_grid: np.ndarray, d_grid: np.ndarray, z: float) -> GrowthRow:
    a = 1.0 / (1.0 + z)
    d = float(np.interp(a, a_grid, d_grid))
    # f = d ln D / d ln a via finite diff on grid
    idx = int(np.searchsorted(a_grid, a))
    idx = max(1, min(idx, len(a_grid) - 2))
    da = a_grid[idx + 1] - a_grid[idx - 1]
    dd = d_grid[idx + 1] - d_grid[idx - 1]
    dlnD_dlnA = (a / d) * (dd / da) if d > 0 else 0.0
    f = dlnD_dlnA
    sigma8 = SIGMA8_0 * d
    return GrowthRow(z=z, d=d, f=f, sigma8=sigma8, fsig8=f * sigma8)


def main() -> None:
    a_grid, d_grid = integrate_growth()
    z_bins = [0.0, 0.51, 0.71, 0.93, 1.32]
    rows = [interp_at_z(a_grid, d_grid, z) for z in z_bins]

    print("# P3 homogeneous growth (Planck 2018 Omegas; NTE hom = LambdaCDM)")
    print()
    print("| z_eff | D(z) | f(z) | sigma8(z) | f*sigma8 hom | DESI f*sigma8 | Delta/sigma |")
    print("|-------|------|------|-----------|--------------|---------------|-------------|")
    for r in rows:
        desi = DESI_FSIG8.get(r.z)
        if desi:
            mu, sig = desi
            delta = r.fsig8 - mu
            ds = delta / sig
            desi_str = f"{mu:.3f} +/- {sig:.3f}"
            ds_str = f"{delta:+.3f} ({ds:+.1f} sigma)"
        else:
            desi_str = "-"
            ds_str = "-"
        print(
            f"| {r.z:.2f} | {r.d:.4f} | {r.f:.4f} | {r.sigma8:.4f} | "
            f"{r.fsig8:.4f} | {desi_str} | {ds_str} |"
        )

    print()
    print(f"sigma8_0 = {SIGMA8_0}; Om_m = {OM_M}; Om_L = {OM_L}; Om_r = {OM_R}")
    print("Homogeneous NTE: identical row (same H(z) as P1/P2).")
    print("DESI values: illustrative central +/- 1sigma (not corpus fit).")


if __name__ == "__main__":
    main()
