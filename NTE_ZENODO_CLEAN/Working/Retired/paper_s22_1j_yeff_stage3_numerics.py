#!/usr/bin/env python3
"""§22.5 — y_eff(N) on Stage-3 y-chart × sunshine Yukawas; ratio scan."""
from __future__ import annotations

import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
N_E = 63.4
N_LOCK = 45.0 / (4.0 * 106.75)
M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777
GEN = ("tau", "mu", "e")
OBS_R_TM = M_TAU / M_MU
OBS_R_ME = M_MU / M_E


def L_bulk_surface() -> float:
    return math.log(N_E / N_LOCK) / LN_8PI


def delta_sunshine(n: int) -> float:
    L = L_bulk_surface()
    return 2.0 / 3.0 + L / 3.0 + (n * L) / 2.0 + (n * n * L) / 12.0


def y_sun(n: int) -> float:
    return EIGHT_PI ** (-delta_sunshine(n))


def ratios_from_y(y: tuple[float, float, float]) -> tuple[float, float]:
    yt, ym, ye = y
    return yt / ym, ym / ye


def err_score(r_tm: float, r_me: float) -> float:
    """log-space symmetric error vs PDG."""
    if r_tm <= 0 or r_me <= 0:
        return 1e9
    return (math.log(r_tm / OBS_R_TM)) ** 2 + (math.log(r_me / OBS_R_ME)) ** 2


def y_from_lock_factors(f: tuple[float, float, float]) -> tuple[float, float, float]:
    base = tuple(y_sun(i) for i in range(3))
    return tuple(b * ff for b, ff in zip(base, f))


# --- Stage-3 linear |Phi|^2 ~ y; y_eff(y) = (y/N)^nu ---


def lock_exposure_cube(nu: float, y_on_frac: tuple[float, float, float]) -> tuple[float, float, float]:
    """F_g = 1 - (y_on/N)^(nu+1); tau,mu,e onset fractions on chart."""
    return tuple(1.0 - a ** (nu + 1.0) for a in y_on_frac)


def model_lock_integral(nu: float, scheme: str) -> tuple[float, float, float]:
    """Structural onset assignments on [0, N_lock]."""
    if scheme == "z_thirds":
        # z_g = n*pi/6  =>  y_g = n*N/3
        y_on = (0.0, 1.0 / 3.0, 2.0 / 3.0)
    elif scheme == "z_thirds_rev":
        y_on = (2.0 / 3.0, 1.0 / 3.0, 0.0)
    elif scheme == "casimir_12":
        # y_g/N = (2g+1)/12  with g=0,1,2
        y_on = tuple((2 * g + 1) / 12.0 for g in range(3))
    elif scheme == "casimir_inv":
        y_on = tuple(1.0 - (2 * g + 1) / 12.0 for g in range(3))
    elif scheme == "lock_node":
        # y_g = N/(2g+1)^2  (sunshine denominator family)
        y_on = tuple(1.0 / ((2 * g + 1) ** 2) for g in range(3))
    else:
        raise ValueError(scheme)
    return lock_exposure_cube(nu, y_on)


# --- Multiplicative Stage-3 node factors (2g+1)^p ---


def model_node_power(p: float, use_g: bool = True) -> tuple[float, float, float]:
    if use_g:
        return tuple((2 * g + 1) ** (p * g / 3.0) for g in range(3))
    return tuple((2 * g + 1) ** p for g in range(3))


# --- y_eff at freeze: evaluate (y_g/N)^nu at structural y_g ---


def model_freeze_eval(nu: float) -> tuple[float, float, float]:
    y_frac = tuple((2 * g + 1) / 12.0 for g in range(3))
    return tuple(a**nu for a in y_frac)


# --- Entropy-weight sunshine companion: (N_e/N_lock)^{g(g+1)/6} ---


def model_entropy_weight() -> tuple[float, float, float]:
    r = N_E / N_LOCK
    return tuple(r ** (g * (g + 1) / 6.0) for g in range(3))


def model_casimir_chart_power(pow: float) -> tuple[float, float, float]:
    """y_g/N = 1 - (2g+1)/12 from inverse-Casimir chart position."""
    y_frac = tuple(1.0 - (2 * g + 1) / 12.0 for g in range(3))
    return tuple(a ** (-pow) for a in y_frac)


def model_delta_chart_shift(k: float) -> tuple[float, float, float]:
    """Y_g *= (y_g/N)^{-k} with y_g/N = 1-(2g+1)/12."""
    return model_casimir_chart_power(k)


# --- Combined structural candidates ---


def combine(
    f_lock: tuple[float, float, float],
    f_node: tuple[float, float, float] | None = None,
    normalize_e: bool = True,
) -> tuple[float, float, float]:
    if f_node is None:
        out = f_lock
    else:
        out = tuple(a * b for a, b in zip(f_lock, f_node))
    if normalize_e and out[2] != 0:
        scale = 1.0 / out[2]
        out = tuple(x * scale for x in out)
    return out


def scan() -> None:
    print("# §22.5 Stage-3 y_eff × sunshine — ratio scan")
    print("=" * 64)
    print(f"  N_e/N_lock = {N_E/N_LOCK:.1f}   L = {L_bulk_surface():.3f}")
    print(f"  sunshine only: m_tau/m_mu = {ratios_from_y(y_from_lock_factors((1,1,1)))[0]:.1f}")
    print(f"                 m_mu/m_e   = {ratios_from_y(y_from_lock_factors((1,1,1)))[1]:.1f}")
    print(f"  PDG targets:   m_tau/m_mu = {OBS_R_TM:.1f}   m_mu/m_e = {OBS_R_ME:.1f}")
    print()

    best: list[tuple[float, str, float, float]] = []

    # lock integral scans
    for scheme in ("z_thirds", "z_thirds_rev", "casimir_12", "casimir_inv", "lock_node"):
        for nu in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
            f = model_lock_integral(nu, scheme)
            y = y_from_lock_factors(f)
            r_tm, r_me = ratios_from_y(y)
            sc = err_score(r_tm, r_me)
            best.append((sc, f"lock[{scheme}] nu={nu}", r_tm, r_me))

    # node power scans
    for p in (0.25, 0.33, 0.5, 0.67, 1.0, 1.33, 1.5, 2.0, 2.67, 3.0, 4.0, 5.0):
        for use_g in (True, False):
            f = model_node_power(p, use_g=use_g)
            y = y_from_lock_factors(f)
            r_tm, r_me = ratios_from_y(y)
            tag = f"node p={p} g={'2g/3' if use_g else 'const'}"
            best.append((err_score(r_tm, r_me), tag, r_tm, r_me))

    # freeze eval
    for nu in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
        f = model_freeze_eval(nu)
        y = y_from_lock_factors(f)
        r_tm, r_me = ratios_from_y(y)
        best.append((err_score(r_tm, r_me), f"freeze (y_g/N)^nu nu={nu}", r_tm, r_me))

    # entropy weight alone
    f = model_entropy_weight()
    y = y_from_lock_factors(f)
    r_tm, r_me = ratios_from_y(y)
    best.append((err_score(r_tm, r_me), "entropy (Ne/Nl)^(g(g+1)/6)", r_tm, r_me))

    # bulk-step scans on mu/e only (sunshine L/3 family)
    L = L_bulk_surface()
    for coeff in (1.0 / 6.0, 1.0 / 3.0, 1.0 / 2.0, 2.0 / 3.0, 1.0):
        step = (N_E / N_LOCK) ** (coeff * L)
        for which in ("mu_only", "mu_e"):
            if which == "mu_only":
                f = (1.0, step, 1.0)
            else:
                f = (1.0, step, 1.0 / step)
            y = y_from_lock_factors(f)
            r_tm, r_me = ratios_from_y(y)
            best.append(
                (err_score(r_tm, r_me), f"bulk (Ne/Nl)^({coeff}L) on {which}", r_tm, r_me)
            )

    # combined: lock + node (structural rationals)
    combos = [
        ("lock_node", 2.0, 2.0 / 3.0, True),
        ("casimir_inv", 2.0, 2.0 / 3.0, True),
        ("z_thirds_rev", 3.0, 2.0 / 3.0, True),
        ("lock_node", 3.0, 2.0 / 3.0, True),
        ("casimir_12", 4.0, 2.0 / 3.0, True),
        ("z_thirds", 5.0, 4.0 / 3.0, True),
        ("lock_node", 2.0, 4.0 / 3.0, True),
        ("z_thirds_rev", 2.0, 2.0 / 3.0, True),
        ("lock_node", 2.0, 1.0 / 3.0, True),
        ("casimir_inv", 3.0, 4.0 / 3.0, True),
    ]
    for scheme, nu, p, use_g in combos:
        f = combine(model_lock_integral(nu, scheme), model_node_power(p, use_g=use_g))
        y = y_from_lock_factors(f)
        r_tm, r_me = ratios_from_y(y)
        tag = f"combo {scheme} nu={nu} + (2g+1)^({p}g/3)"
        best.append((err_score(r_tm, r_me), tag, r_tm, r_me))

    best.sort(key=lambda t: t[0])
    print("## Top 12 structural models (log-error score)")
    for sc, tag, r_tm, r_me in best[:12]:
        print(f"  score={sc:6.3f}  {tag:42s}  tau/mu={r_tm:7.2f}  mu/e={r_me:7.2f}")

    print("\n## Primary derived candidate (Jammer v0.1j)")
    f_lock = model_lock_integral(3.0, "casimir_inv")
    y = y_from_lock_factors(f_lock)
    r_tm, r_me = ratios_from_y(y)
    print("  y_eff(y) = y_0 * sqrt(y/N_lock)  (Stage-3 |Phi_pre|^2 ~ y)")
    print("  y_g/N = 1 - (2g+1)/12  (inverse-Casimir chart)")
    print("  F_lock = 1 - (1 - (2g+1)/12)^4 ;  normalize F_e=1")
    fn = combine(f_lock)
    print(f"  F_norm = ({fn[0]:.3f}, {fn[1]:.3f}, {fn[2]:.3f})")
    print(f"  m_tau/m_mu = {r_tm:.2f}  (obs {OBS_R_TM:.2f})")
    print(f"  m_mu/m_e   = {r_me:.2f}  (obs {OBS_R_ME:.2f})")

    print("\n## Zero-parameter closure attempt (bulk step on mu-e only)")
    # extra mu-e step: (N_e/N_lock)^(L/3) from sunshine L/3 coefficient
    L = L_bulk_surface()
    step = (N_E / N_LOCK) ** (L / 3.0)
    f2 = (1.0, step, 1.0)
    y2 = y_from_lock_factors(f2)
    r_tm2, r_me2 = ratios_from_y(y2)
    print(f"  Y_mu *= (N_e/N_lock)^(L/3) = {step:.2f}")
    print(f"  m_tau/m_mu = {r_tm2:.1f}   m_mu/m_e = {r_me2:.1f}")

    print("\n## Split closure: casimir_inv nu=3 (tau/mu) + node (mu/e)")
    f_lock = model_lock_integral(3.0, "casimir_inv")
    for p in (0.5, 2.0 / 3.0, 1.0, 4.0 / 3.0, 2.0):
        for use_g in (True, False):
            f = combine(f_lock, model_node_power(p, use_g=use_g))
            y = y_from_lock_factors(f)
            r_tm, r_me = ratios_from_y(y)
            print(
                f"  lock+casimir_inv nu=3 + node p={p} g={'2g/3' if use_g else 'const'}"
                f"  -> tau/mu={r_tm:.2f}  mu/e={r_me:.1f}"
            )

    for k in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
        f = model_delta_chart_shift(k)
        y = y_from_lock_factors(f)
        r_tm, r_me = ratios_from_y(y)
        print(f"  chart (y_g/N)^(-{k})  tau/mu={r_tm:.2f}  mu/e={r_me:.1f}")

    f = combine(model_lock_integral(3.0, "casimir_inv"), model_casimir_chart_power(2.0))
    y = y_from_lock_factors(f)
    r_tm, r_me = ratios_from_y(y)
    print(f"\n  COMBO lock casimir_inv^4 + chart^(-2): tau/mu={r_tm:.2f}  mu/e={r_me:.1f}")

    print("\n## Derived two-factor (v0.1j proposal)")
    # F_lock from inverse Casimir chart; F_node = (2g+1)^{-2(2-g)/3}
    f_lock = model_lock_integral(3.0, "casimir_inv")
    f_node = tuple((2 * g + 1) ** (-2.0 * (2 - g) / 3.0) for g in range(3))
    f = combine(f_lock, f_node)
    y = y_from_lock_factors(f)
    r_tm, r_me = ratios_from_y(y)
    print(f"  F_lock = 1-(1-(2g+1)/12)^4")
    print(f"  F_node = (2g+1)^(-2(2-g)/3)")
    print(f"  m_tau/m_mu = {r_tm:.2f}  m_mu/m_e = {r_me:.1f}")

    print("\n## Verdict")
    print("  casimir_inv nu=3 alone: tau/mu ~ 18 (obs 17); mu/e ~ 94 (obs 207).")
    print("  Combined node exponent can land mu/e ~ 200 at cost of tau/mu.")


if __name__ == "__main__":
    scan()
