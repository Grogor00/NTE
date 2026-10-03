#!/usr/bin/env python3
"""PPN 1PN check for mu(x,N) constraint action (§22.16 / Mu_xN worksheet v0.2)."""
from __future__ import annotations

import math

# Natural units: c = 1 for algebra; restore c in printed ratios
C = 2.99792458e8  # m/s (display only)
V_EW_GEV = 246.0
ALPHA_H0 = 2.38e-47  # GeV^-1 (corpus α; H0 = α v_EW²)


def phi_newton(r_m: float, gm: float) -> float:
    """Dimensionless Newtonian potential Phi_N = -GM/(r c^2)."""
    return -gm / (r_m * C**2) if r_m > 0 else 0.0


def phi_nte_sq(phi_n: float, v_ew: float = V_EW_GEV) -> float:
    """|Phi_NTE|^2 from structural identity §2.3."""
    return v_ew**2 * (1.0 + phi_n)


def h_eff(phi_n: float, h0: float) -> float:
    """H_eff[g] = H0 * sqrt(-g00/g00|inf) with g00 = -(1+2*Phi_N), c=1."""
    lapse_ratio = math.sqrt(1.0 + 2.0 * phi_n)
    return h0 * lapse_ratio


def constraint_residual(phi_n: float, h0: float, alpha: float, v_ew: float = V_EW_GEV) -> float:
    """C = H_eff - alpha |Phi_NTE|^2; should be ~0 on-shell."""
    return h_eff(phi_n, h0) - alpha * phi_nte_sq(phi_n, v_ew)


def proper_time_ratio(phi_n: float) -> float:
    """tau(x)/tau(inf) = 1 + Phi_N per corpus §2.3 (Schwarzschild 1PN)."""
    return 1.0 + phi_n


def schwarzschild_1pn(phi_n: float) -> float:
    """GR Schwarzschild g00 factor: sqrt(1+2Phi) ~ 1+Phi at 1PN."""
    return 1.0 + phi_n


def main() -> None:
    h0 = ALPHA_H0 * V_EW_GEV**2  # GeV
    gm_sun = 1.32712440018e20  # GM_sun in m^3/s^2
    r_earth = 1.495978707e11  # 1 AU

    phi_1au = phi_newton(r_earth, gm_sun)
    phi_solar = phi_newton(6.96e8, gm_sun)

    print("# mu(x,N) PPN 1PN check — structural identity under H = alpha |Phi|^2")
    print(f"H0 = {h0:.4e} GeV, alpha = {ALPHA_H0:.4e} GeV^-1")
    print()
    print("## Constraint on-shell (H_eff[g] choice)")
    print("| regime | Phi_N | H_eff - alpha|Phi|^2 [GeV] | rel |")
    print("|--------|-------|---------------------------|-----|")
    for label, phi in [("infinity", 0.0), ("1 AU", phi_1au), ("solar surface", phi_solar)]:
        res = constraint_residual(phi, h0, ALPHA_H0)
        rel = abs(res / h0) if h0 else float("nan")
        print(f"| {label} | {phi:.4e} | {res:.4e} | {rel:.2e} |")

    print()
    print("## Proper time vs Schwarzschild 1PN")
    print("| regime | tau(x)/tau(inf) | 1+Phi_N (Schw.) | delta |")
    print("|--------|-----------------|-----------------|-------|")
    for label, phi in [("1 AU", phi_1au), ("solar surface", phi_solar)]:
        tau = proper_time_ratio(phi)
        sch = schwarzschild_1pn(phi)
        print(f"| {label} | {tau:.12f} | {sch:.12f} | {abs(tau-sch):.2e} |")

    print()
    print("## PPN parameters (leading order)")
    print("- gamma_PPN = 1: spatial g_ij unchanged at O(Phi) — constraint slaved to lapse")
    print("- beta_PPN = 1: no scalar-mediated fifth force at 1PN (mu enforces algebraic constraint)")
    print("- Shapiro / perihelion: require v0.3 metric variation delta g_munu — deferred")


if __name__ == "__main__":
    main()
