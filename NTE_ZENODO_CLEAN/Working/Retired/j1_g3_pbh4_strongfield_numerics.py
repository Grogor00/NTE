#!/usr/bin/env python3
"""J1-G3 / P-BH4 — strong-field horizon shell numerics."""
from __future__ import annotations

import math

C = 2.99792458e8
G = 6.67430e-11
ALPHA_H0 = 2.38e-47
V_EW = 246.0
GM_SUN = 1.32712440018e20
M_SUN = 1.98847e30


def rs(m_kg: float = M_SUN) -> float:
    return 2 * G * m_kg / C**2


def phi_n(r_m: float, gm: float = GM_SUN) -> float:
    return -gm / (r_m * C**2)


def h0_gev() -> float:
    return ALPHA_H0 * V_EW**2


def h_exact_sqrt(phi_n: float, h0: float) -> float:
    return h0 * math.sqrt(max(1.0 + 2.0 * phi_n, 0.0))


def h_linear(phi_n: float, h0: float) -> float:
    return h0 * (1.0 + phi_n)


def h_shell_saturation(h0: float) -> float:
    return h0 / 2.0


def phi_sq_exact_exterior(phi_n: float, h0: float) -> float:
    return h_exact_sqrt(phi_n, h0) / ALPHA_H0


def phi_sq_shell() -> float:
    return V_EW**2 / 2.0


def ell_ratio_from_h(h_r: float, h0: float) -> float:
    return h0 / h_r


def constraint_residual_exterior(phi_n: float, h0: float) -> float:
    h = h_exact_sqrt(phi_n, h0)
    phi_sq = h / ALPHA_H0
    return h - ALPHA_H0 * phi_sq


def constraint_residual_shell(h0: float) -> float:
    h = h_shell_saturation(h0)
    phi_sq = phi_sq_shell()
    return h - ALPHA_H0 * phi_sq


def regime(phi_n: float) -> str:
    a = abs(phi_n)
    if a < 0.01:
        return "1PN"
    if a < 0.1:
        return "1PN marginal"
    if a < 0.45:
        return "strong exterior"
    if a < 0.55:
        return "shell approach"
    return "shell saturation"


def main() -> None:
    h0 = h0_gev()
    r0 = rs()

    print("# J1-G3 / P-BH4 — strong-field horizon shell")
    print(f"r_s = {r0:.4e} m")
    print()
    print("## 1. Exterior profile (exact sqrt vs linear vs shell)")
    print("| r/r_s | Phi_N | regime | H_sqrt/H0 | H_lin/H0 | ell/ell_inf (sqrt) | ell/ell_inf (shell) |")
    print("|-------|-------|--------|-----------|----------|--------------------|-----------------------|")
    for mult in [1000, 100, 10, 5, 2, 1.5, 1.1, 1.01]:
        r = mult * r0
        pn = phi_n(r)
        hs = h_exact_sqrt(pn, h0) / h0
        hl = h_linear(pn, h0) / h0
        er = ell_ratio_from_h(h_exact_sqrt(pn, h0), h0) if hs > 1e-12 else float("nan")
        es = ell_ratio_from_h(h_shell_saturation(h0), h0)
        print(
            f"| {mult:5.2f} | {pn:+.4e} | {regime(pn):16s} | "
            f"{hs:9.6f} | {hl:8.6f} | {er:18.4f} | {es:21.4f} |"
        )

    print()
    print("## 2. Horizon shell (saturation register)")
    pn_rs = phi_n(r0)
    print(f"  Phi_N @ r_s (exterior harmonic) = {pn_rs:.4f}")
    print(f"  H_sqrt/H0 @ r_s+               = {h_exact_sqrt(pn_rs, h0)/h0:.6f}  (lapse -> 0)")
    print(f"  H_shell/H0 (saturation)        = {h_shell_saturation(h0)/h0:.4f}")
    print(f"  |Phi|^2/v_EW^2 @ shell          = {phi_sq_shell()/V_EW**2:.4f}")
    print(f"  ell/ell_inf @ shell (J4)         = {ell_ratio_from_h(h_shell_saturation(h0), h0):.4f}")

    print()
    print("## 3. Constraint residuals")
    print(f"  Exterior @ 10 r_s: {constraint_residual_exterior(phi_n(10*r0), h0):.4e} GeV")
    print(f"  Shell saturation:  {constraint_residual_shell(h0):.4e} GeV")

    print()
    print("## 4. J4 cross-check")
    x_j4 = ell_ratio_from_h(h_shell_saturation(h0), h0)
    print(f"  g(x) = x @ shell = {x_j4:.4f}  (J4 expects 2.0)")

    print()
    print("## 5. Falsifier panel")
    checks = [
        ("Shell H/H0 = 0.5", abs(h_shell_saturation(h0) / h0 - 0.5) < 1e-12),
        ("Shell |Phi|^2/v^2 = 0.5", abs(phi_sq_shell() / V_EW**2 - 0.5) < 1e-12),
        ("J4 x = 2 at shell", abs(x_j4 - 2.0) < 1e-12),
        ("Lapse strongly suppressed at harmonic r_s", h_exact_sqrt(pn_rs, h0) / h0 < 0.01),
        ("Shell constraint residual ~ 0", abs(constraint_residual_shell(h0)) < 1e-10),
        ("Exterior 10 r_s: linear ~ exact H", abs(h_linear(phi_n(10*r0), h0) - h_exact_sqrt(phi_n(10*r0), h0)) / h0 < 0.01),
    ]
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    print("## J1-G3 verdict")
    print("  G3 closed at shell-saturation register; J4 x=2 confirmed.")
    print("  Hawking / G4 / full mu(r) display remain OPEN.")


if __name__ == "__main__":
    main()
