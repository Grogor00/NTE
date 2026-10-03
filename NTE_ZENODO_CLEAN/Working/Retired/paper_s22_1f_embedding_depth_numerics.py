#!/usr/bin/env python3
"""L2 — charged-lepton embedding depth delta_l from (8pi)^(-delta) ansatz."""
from __future__ import annotations

import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
V_EW = 246.0
SQRT2 = math.sqrt(2.0)

M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777

SIN2_T13 = 0.0222
SIN2_T12 = 1.0 / 3.0  # tribimaximal register in corpus


def y_from_mass(m: float) -> float:
    return SQRT2 * m / V_EW


def delta_from_y(y: float) -> float:
    return -math.log(y) / LN_8PI


def overlap(n: int) -> float:
    """S^3 mode overlap psi_n with psi_0 anchor (sec 19.4)."""
    return (3.0 / 2.0) / (n + 1.5)


def mass_ratio_from_delta(d_heavy: float, d_light: float) -> float:
    """m_heavy/m_light = (8pi)^(d_light - d_heavy) for Y ~ (8pi)^(-delta)."""
    return EIGHT_PI ** (d_light - d_heavy)


def main() -> None:
    print("# L2 embedding depth — (8pi)^(-delta_l) numerics")
    print("=" * 60)

    y_e, y_mu, y_tau = y_from_mass(M_E), y_from_mass(M_MU), y_from_mass(M_TAU)
    d_e, d_mu, d_tau = delta_from_y(y_e), delta_from_y(y_mu), delta_from_y(y_tau)

    print("\n## A — Phenomenological delta from observed masses")
    print(f"  Y_e, Y_mu, Y_tau (EW)     = {y_e:.3e}, {y_mu:.3e}, {y_tau:.3e}")
    print(f"  delta_e, delta_mu, delta_tau = {d_e:.3f}, {d_mu:.3f}, {d_tau:.3f}")
    print(f"  delta_e - delta_mu        = {d_e - d_mu:.3f}  (need ~1.65 for m_mu/m_e)")
    print(f"  delta_mu - delta_tau      = {d_mu - d_tau:.3f}  (need ~0.87 for m_tau/m_mu)")
    print(f"  delta_nu2 (corpus)        = {1.0/3.0:.3f}  -> Y = {(EIGHT_PI)**(-1/3):.4f}")

    print("\n## B — Structural baseline (sector split)")
    d_nu = 1.0 / 3.0
    d_singlet_base = 2.0 / 3.0  # G2 singlet: one extra inverse volumetric power
    print(f"  delta_nu (Dirac, sigma_1/2)   = {d_nu:.3f}")
    print(f"  delta_singlet base (L2)       = {d_singlet_base:.3f}")
    print(f"  Y at base singlet             = {(EIGHT_PI)**(-d_singlet_base):.4f}")
    print(f"  F2: Y_e != Y_nu2 without split -> PASS if delta_e > delta_nu")

    print("\n## C — Bracket ansatze (generation index n=0,1,2 for e,mu,tau)")
    ansatze: list[tuple[str, float, float, float]] = []

    # C1: base + overlap^2 stack (lightest gets largest stack)
    def c1() -> tuple[float, float, float]:
        def d(n: int) -> float:
            stack = sum(overlap(k) ** 2 for k in range(n + 1))
            return d_singlet_base + stack / 3.0

        return d(2), d(1), d(0)  # e, mu, tau

    # C2: base + (1/3)*overlap(n) per generation
    def c2() -> tuple[float, float, float]:
        return (
            d_singlet_base + overlap(2) / 3.0,
            d_singlet_base + overlap(1) / 3.0,
            d_singlet_base + overlap(0) / 3.0,
        )

    # C3: linear J3 steps: delta = (3-g)/3 for g=1,2,3
    def c3() -> tuple[float, float, float]:
        return 1.0, 2.0 / 3.0, 1.0 / 3.0

    # C4: Z2 + PMNS increments on singlet base (e heaviest depth)
    def c4() -> tuple[float, float, float]:
        d_t = d_nu
        d_m = d_singlet_base + SIN2_T13
        d_el = d_singlet_base + SIN2_T13 + SIN2_T12
        return d_el, d_m, d_t

    # C5: fit one overlap amplitude alpha on C2 form
    def c5_alpha() -> float:
        target = math.log(M_MU / M_E) / LN_8PI  # delta_e - delta_mu
        o_e, o_mu = overlap(2), overlap(1)
        return target * 3.0 / (o_e - o_mu)

    alpha = c5_alpha()
    def c5() -> tuple[float, float, float]:
        return (
            d_singlet_base + alpha * overlap(2) / 3.0,
            d_singlet_base + alpha * overlap(1) / 3.0,
            d_singlet_base + alpha * overlap(0) / 3.0,
        )

    for name, fn in [
        ("C1 overlap^2 stack", c1),
        ("C2 overlap/3 per gen", c2),
        ("C3 (3-g)/3 linear", c3),
        ("C4 base+PMNS angles", c4),
        (f"C5 C2 scaled alpha={alpha:.2f}", c5),
    ]:
        de, dm, dt = fn()
        ansatze.append((name, de, dm, dt))
        r_me = mass_ratio_from_delta(dm, de)
        r_tm = mass_ratio_from_delta(dt, dm)
        print(f"\n  [{name}]")
        print(f"    delta_e, mu, tau = {de:.3f}, {dm:.3f}, {dt:.3f}")
        print(f"    pred m_mu/m_e     = {r_me:.2f}  (obs {M_MU/M_E:.1f})")
        print(f"    pred m_tau/m_mu   = {r_tm:.2f}  (obs {M_TAU/M_MU:.1f})")

    print("\n## D — L1 x L2 hybrid (GUT tau anchor)")
    # tau Yukawa from GUT m_tau ~ m_b at M_GUT; apply (8pi)^(-delta_tau) at EW
    d_tau_struct = d_nu  # parallel third gen
    y_tau_pred = EIGHT_PI ** (-d_tau_struct)
    print(f"  Y_tau ~ (8pi)^(-1/3) only     = {y_tau_pred:.4f}  (obs Y_tau ~ {y_tau:.4f})")
    print("  Hierarchy requires delta_e >> delta_tau (not one universal 1/3).")

    print("\n## Verdict")
    best = min(ansatze, key=lambda x: abs(math.log(mass_ratio_from_delta(x[2], x[1]) / (M_TAU / M_MU))))
    print(f"  Best tau/mu among brackets: {best[0]}")
    print("  Structural delta_singlet=2/3 resolves F2; generation spacing = BRACKET (Paper S5).")
    print("  Phenomenological deltas ~ {d_e:.1f}, {d_mu:.1f}, {d_tau:.1f} guide L4 D_F.".format(
        d_e=d_e, d_mu=d_mu, d_tau=d_tau
    ))


if __name__ == "__main__":
    main()
