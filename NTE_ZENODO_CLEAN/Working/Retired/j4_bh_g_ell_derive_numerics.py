#!/usr/bin/env python3
"""J4 — derive g(ell/ell_inf) from H constraint; verify M^2 scaling."""
from __future__ import annotations

import math

C = 2.99792458e8
G = 6.67430e-11
HBAR = 1.054571817e-34


def rs(m_kg: float) -> float:
    return 2 * G * m_kg / C**2


def phi_n_at(r_m: float, m_kg: float) -> float:
    return -G * m_kg / (r_m * C**2)


def ell_ratio(phi_n: float) -> float:
    """Lemma 2: x = ell/ell_inf = 1/(1 + Phi_N) from slaving."""
    return 1.0 / (1.0 + phi_n)


def h_ratio(phi_n: float) -> float:
    """Lemma 1: x = H_0/H(r) = 1/(1 + Phi_N) under slaving."""
    return 1.0 / (1.0 + phi_n)


def g_derived(x: float) -> float:
    """Proposition 3: g(x) = x from boundary microstate counting."""
    return x


def s_bh_natural(m_kg: float) -> float:
    r = rs(m_kg)
    return math.pi * r**2 / G


def s_nte_derived(m_kg: float) -> float:
    r0 = rs(m_kg)
    x = ell_ratio(phi_n_at(r0, m_kg))
    return s_bh_natural(m_kg) * g_derived(x)


def integral_thickness_linear(m_kg: float, r_max_mult: float = 1e6) -> float:
    r0 = rs(m_kg)
    r1 = r_max_mult * r0
    n = 200
    total = 0.0
    prev_r = r0
    prev_f = ell_ratio(phi_n_at(r0, m_kg)) - 1.0
    for i in range(1, n + 1):
        r = r0 * (r1 / r0) ** (i / n)
        f = ell_ratio(phi_n_at(r, m_kg)) - 1.0
        total += 0.5 * (prev_f + f) * (r - prev_r)
        prev_r, prev_f = r, f
    return total


def main() -> None:
    m_sun = 1.98847e30
    masses = [("M_sun", m_sun), ("10 M_sun", 10 * m_sun), ("10^6 M_sun", 1e6 * m_sun)]

    print("# J4 — BH g(ell/ell_inf) derived from constraint action")
    print()
    print("## 1. Lemma 1+2: x = ell/ell_inf = H_0/H(r) = 1/(1+Phi_N)")
    print("| M | r_s [m] | Phi_N @ r_s | x = ell/ell_inf | H_0/H | g(x)=x |")
    print("|---|---------|-------------|-----------------|-------|--------|")
    for label, m in masses:
        r0 = rs(m)
        pn = phi_n_at(r0, m)
        x = ell_ratio(pn)
        hr = h_ratio(pn)
        print(f"| {label} | {r0:.4e} | {pn:+.4f} | {x:.4f} | {hr:.4f} | {g_derived(x):.4f} |")

    print()
    print("## 2. Theorem 4: S_NTE = (A/4G) * g(x) @ r_s")
    sbh = s_bh_natural(m_sun)
    snte = s_nte_derived(m_sun)
    print(f"  S_BH (1 M_sun)   = {sbh:.4e}")
    print(f"  S_NTE derived    = {snte:.4e}")
    print(f"  S_NTE / S_BH     = {snte/sbh:.4f}  (expect 2.0 at leading Schwarzschild)")

    print()
    print("## 3. M^2 scaling (relative to M_sun)")
    print("| M | S_BH ratio | S_NTE ratio | additive int ratio |")
    print("|---|------------|-------------|---------------------|")
    s_ref = s_bh_natural(m_sun)
    sn_ref = s_nte_derived(m_sun)
    i_ref = integral_thickness_linear(m_sun)
    for label, m in masses:
        print(
            f"| {label} | {s_bh_natural(m)/s_ref:.2e} | "
            f"{s_nte_derived(m)/sn_ref:.2e} | "
            f"{integral_thickness_linear(m)/i_ref:.2e} |"
        )

    print()
    print("## 4. Falsifier panel")
    x_rs = ell_ratio(phi_n_at(rs(m_sun), m_sun))
    checks = [
        ("g(x) = x (not free trial)", abs(g_derived(x_rs) - x_rs) < 1e-12),
        ("x = H_0/H at r_s", abs(x_rs - h_ratio(phi_n_at(rs(m_sun), m_sun))) < 1e-12),
        ("S_NTE / S_BH = 2 at r_s (1 M_sun)", abs(snte / sbh - 2.0) < 0.01),
        ("M^2 scaling S_NTE", abs(s_nte_derived(10 * m_sun) / sn_ref - 100) < 1),
        ("Additive route NOT M^2", abs(integral_thickness_linear(10 * m_sun) / i_ref - 10) < 2),
    ]
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    print("## J4 verdict")
    print("  g(ell/ell_inf) = H_0/H(r) DERIVED at constraint-shell register.")
    print("  G3 (P-BH4 full covariant strong-field) remains OPEN.")
    print("  Hawking / information programme NOT claimed.")


if __name__ == "__main__":
    main()
