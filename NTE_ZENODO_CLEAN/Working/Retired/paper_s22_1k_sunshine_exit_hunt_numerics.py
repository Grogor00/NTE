#!/usr/bin/env python3
"""Sunshine exit hunt — all rabbit holes (spinors, zeta, HK, chaos, off-diag, ...)."""
from __future__ import annotations

import cmath
import math
from itertools import product

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
INV_16PI2 = 1.0 / (16.0 * math.pi**2)
N_E = 63.4
N_LOCK = 45.0 / (4.0 * 106.75)
G_EFF = 106.75
V_EW = 246.0
SQRT2 = math.sqrt(2.0)
M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777
OBS_TM = M_TAU / M_MU
OBS_ME = M_MU / M_E
GEN = ("tau", "mu", "e")

# Riemann zeta specials
ZETA2 = math.pi**2 / 6.0
ZETA3 = 1.2020569031595942
ZETA4 = math.pi**4 / 90.0
FEIGENBAUM_D = 4.669201609102990
FEIGENBAUM_A = 2.5029078750958928
LOGISTIC_CHAOS = 3.569945671870944


def L_sun() -> float:
    return math.log(N_E / N_LOCK) / LN_8PI


def delta_sun(n: int) -> float:
    L = L_sun()
    return 2.0 / 3.0 + L / 3.0 + (n * L) / 2.0 + (n * n * L) / 12.0


def y_sun(n: int) -> float:
    return EIGHT_PI ** (-delta_sun(n))


def d_s3(k: int) -> float:
    return float((k + 1) * (k + 2))


def overlap(n: int, m: int = 0) -> float:
    return (3.0 / 2.0) / (n + m + 1.5)


def s_geom(g: int, r: int) -> float:
    return (d_s3(0) / d_s3(g)) * (overlap(g, 0) ** (2 * r))


def err_score(r_tm: float, r_me: float) -> float:
    if r_tm <= 0 or r_me <= 0:
        return 1e9
    return (math.log(r_tm / OBS_TM)) ** 2 + (math.log(r_me / OBS_ME)) ** 2


def ratios_y(y: tuple[float, float, float]) -> tuple[float, float]:
    return y[0] / y[1], y[1] / y[2]


def norm_e(f: tuple[float, float, float]) -> tuple[float, float, float]:
    s = f[2] if f[2] != 0 else 1.0
    return (f[0] / s, f[1] / s, 1.0)


def apply_factors(base: tuple[float, float, float], fac: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(b * ff for b, ff in zip(base, fac))


# --- building blocks (per generation g=0,1,2) ---


def block_lock_casimir(nu: int = 3) -> tuple[float, float, float]:
    return tuple(1.0 - (1.0 - (2 * g + 1) / 12.0) ** (nu + 1) for g in range(3))


def block_casimir_chart_pow(k: float) -> tuple[float, float, float]:
    return tuple((1.0 - (2 * g + 1) / 12.0) ** (-k) for g in range(3))


def block_s7_spinor() -> tuple[float, float, float]:
    """S^7 unit spinor 8 -> S^3 fibre 7 projection."""
    return tuple((8.0 / 7.0) ** g for g in range(3))


def block_s7_inverse() -> tuple[float, float, float]:
    return tuple((7.0 / 8.0) ** (2 - g) for g in range(3))


def block_hk_s(r: int) -> tuple[float, float, float]:
    return tuple(s_geom(g, r) ** (-1.0 / 6.0) for g in range(3))


def block_hk_delta(r: int) -> tuple[float, float, float]:
    """Y ~ (8pi)^{-delta_sun - hk_correction}."""
    out = []
    for g in range(3):
        s = s_geom(g, r)
        d_add = -math.log(s) / (3.0 * LN_8PI)
        out.append(EIGHT_PI ** (-(delta_sun(g) + d_add)) / y_sun(g))
    return tuple(out)


def block_cumulative_s(r: int) -> tuple[float, float, float]:
    prod = 1.0
    out = []
    for g in range(3):
        prod *= s_geom(g, r)
        out.append(prod ** (-1.0 / (3.0 * LN_8PI * LN_8PI)))  # test power
    return tuple(out)


def block_cumulative_y(r: int) -> tuple[float, float, float]:
    """delta from cumulative S product (S5b)."""
    prod = 1.0
    ys = []
    for g in range(3):
        prod *= s_geom(g, r)
        d = 2.0 / 3.0 - math.log(prod) / (3.0 * LN_8PI)
        ys.append(EIGHT_PI ** (-d))
    # return as factor relative to sunshine
    base = tuple(y_sun(g) for g in range(3))
    return tuple(y / b for y, b in zip(ys, base))


def block_zeta2_power(p: float) -> tuple[float, float, float]:
    return tuple(ZETA2 ** (p * g) for g in range(3))


def block_zeta3_zeta2() -> tuple[float, float, float]:
    r = ZETA3 / ZETA2
    return tuple(r**g for g in range(3))


def block_ne_nl(exp: float) -> tuple[float, float, float]:
    r = N_E / N_LOCK
    return tuple(r ** (exp * g * L_sun() / 3.0) for g in range(3))


def block_ne_nl_inv(exp: float) -> tuple[float, float, float]:
    r = N_LOCK / N_E
    return tuple(r ** (exp * (2 - g) * L_sun() / 3.0) for g in range(3))


def block_chaos_period3() -> tuple[float, float, float]:
    """Logistic period-3 window ~3.84 and chaos onset ~3.57 for 3 gen."""
    p3 = (1.0 + math.sqrt(6.0)) / 2.0  # ~1.449 - wrong
    # Feigenbaum scaling between generations
    return tuple((FEIGENBAUM_A ** g) / (FEIGENBAUM_D ** g) for g in range(3))


def block_feigenbaum() -> tuple[float, float, float]:
    return tuple(FEIGENBAUM_D ** (-g / 3.0) for g in range(3))


def block_spectral_zeta_s(s: float) -> tuple[float, float, float]:
    """Per-generation mode sum weight ~ d_g * lambda_g^{-s}."""
    out = []
    for g in range(3):
        lam = 1.5 + g
        w = d_s3(g) * (lam ** (-s))
        out.append(w)
    m = max(out)
    return tuple(x / m for x in out)


def block_entropy_weight() -> tuple[float, float, float]:
    """s_g ~ (2g+1)/12 integrated on chart."""
    return tuple(math.sqrt((2 * g + 1) / 12.0) for g in range(3))


def block_2g1_power(p: float) -> tuple[float, float, float]:
    return tuple((2 * g + 1) ** (p * g / 3.0) for g in range(3))


def block_2g1_inv_power(p: float) -> tuple[float, float, float]:
    return tuple((2 * g + 1) ** (-p * (2 - g) / 3.0) for g in range(3))


def block_zeta_spectral_dirac() -> tuple[float, float, float]:
    """Dirac zeta residue style: sum_{k<=g} d_k / lambda_k."""
    acc = 0.0
    out = []
    for g in range(3):
        lam = 1.5 + g
        acc += d_s3(g) / lam
        out.append(acc)
    tot = out[2]
    return tuple(t / tot for t in out)


def block_pi_zeta_combo() -> tuple[float, float, float]:
    """Boost mu/e by zeta(2) at electron only."""
    return (1.0, 1.0, ZETA2)


def block_exact_207_17_target() -> tuple[float, float, float]:
    """Minimal fix factors from sunshine to PDG ratios."""
    f_tm = OBS_TM / (EIGHT_PI ** (delta_sun(1) - delta_sun(0)))
    f_me = OBS_ME / (EIGHT_PI ** (delta_sun(2) - delta_sun(1)))
    return (f_tm, f_me, 1.0)  # wrong order - tau/mu needs F_tau/F_mu


def delta_unified(n: int, r: int, lock_nu: int, zeta_w: float) -> float:
    """Combined delta ansatz."""
    s = s_geom(n, r)
    hk = -math.log(s) / (3.0 * LN_8PI)
    a = 1.0 - (2 * n + 1) / 12.0
    lock = -math.log(max(1.0 - a ** (lock_nu + 1), 1e-30)) / LN_8PI
    zeta_term = zeta_w * math.log(ZETA2) / LN_8PI * n
    return delta_sun(n) + hk + lock + zeta_term


# --- off-diagonal 3x3 with sunshine diagonal ---


def eigh_symmetric_3x3(a: list[list[float]]) -> list[float]:
    m = [row[:] for row in a]
    for _ in range(60):
        p, q = 0, 1
        max_off = abs(m[0][1])
        for i, j in ((0, 2), (1, 2)):
            if abs(m[i][j]) > max_off:
                max_off, p, q = abs(m[i][j]), i, j
        if max_off < 1e-15:
            break
        phi = 0.5 * math.atan2(2 * m[p][q], m[q][q] - m[p][p])
        c, s = math.cos(phi), math.sin(phi)
        for i in range(3):
            mii, mqi = m[i][p], m[i][q]
            m[i][p] = c * mii - s * mqi
            m[i][q] = s * mii + c * mqi
        for j in range(3):
            mpj, mqj = m[p][j], m[q][j]
            m[p][j] = c * mpj - s * mqj
            m[q][j] = s * mpj + c * mqj
    return sorted(m[i][i] for i in range(3))


def y_offdiag_sunshine(eta: float, r: int = 2) -> tuple[float, float]:
    yd = [y_sun(g) for g in range(3)]
    y = [[0.0] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            if a == b:
                y[a][b] = yd[a]
            else:
                oab = overlap(a, b)
                sg = s_geom(a, r) * s_geom(b, r)
                y[a][b] = eta * INV_16PI2 * math.sqrt(sg) * oab * yd[a]
    ev = eigh_symmetric_3x3(y)
    # m ~ Y^2 v^2 for eigenvalues of Y (symmetric)
    r_me = (ev[1] / ev[0]) ** 2
    r_tm = (ev[2] / ev[1]) ** 2
    return r_tm, r_me


def grid_search_blocks() -> None:
    base = tuple(y_sun(g) for g in range(3))
    blocks: list[tuple[str, callable]] = [
        ("lock3", lambda: block_lock_casimir(3)),
        ("lock2", lambda: block_lock_casimir(2)),
        ("chart2", lambda: block_casimir_chart_pow(2.0)),
        ("chart1", lambda: block_casimir_chart_pow(1.0)),
        ("s7", block_s7_spinor),
        ("s7inv", block_s7_inverse),
        ("hk_s2", lambda: block_hk_s(2)),
        ("hk_s3", lambda: block_hk_s(3)),
        ("hk_s4", lambda: block_hk_s(4)),
        ("cum_r3", lambda: block_cumulative_y(3)),
        ("cum_r4", lambda: block_cumulative_y(4)),
        ("cum_r5", lambda: block_cumulative_y(5)),
        ("z2g", lambda: block_zeta2_power(1.0 / 3.0)),
        ("z32", block_zeta3_zeta2),
        ("neL", lambda: block_ne_nl(1.0)),
        ("neLinv", lambda: block_ne_nl_inv(1.0)),
        ("feig", block_feigenbaum),
        ("sz1", lambda: block_spectral_zeta_s(1.0)),
        ("sz2", lambda: block_spectral_zeta_s(2.0)),
        ("ent", block_entropy_weight),
        ("2g1_2", lambda: block_2g1_power(2.0)),
        ("2g1i2", lambda: block_2g1_inv_power(2.0)),
        ("dz", block_zeta_spectral_dirac),
        ("pz", block_pi_zeta_combo),
    ]
    best: list[tuple[float, str, float, float]] = []
    # singles
    for name, fn in blocks:
        f = norm_e(fn())
        y = apply_factors(base, f)
        r_tm, r_me = ratios_y(y)
        best.append((err_score(r_tm, r_me), name, r_tm, r_me))
    # pairs
    for (n1, f1), (n2, f2) in product(blocks, blocks):
        if n1 >= n2:
            continue
        fac = norm_e(tuple(a * b for a, b in zip(f1(), f2())))
        y = apply_factors(base, fac)
        r_tm, r_me = ratios_y(y)
        best.append((err_score(r_tm, r_me), f"{n1}+{n2}", r_tm, r_me))
    best.sort()
    print("\n## Top 25 block combinations (sunshine × factors)")
    for sc, tag, r_tm, r_me in best[:25]:
        pct_tm = 100 * abs(r_tm - OBS_TM) / OBS_TM
        pct_me = 100 * abs(r_me - OBS_ME) / OBS_ME
        print(f"  {sc:7.4f}  {tag:28s}  tau/mu={r_tm:7.2f} ({pct_tm:4.1f}%)  mu/e={r_me:7.1f} ({pct_me:4.1f}%)")


def grid_delta_unified() -> None:
    print("\n## Unified delta grid (sun + HK + lock + zeta*n)")
    best = []
    for r in range(2, 8):
        for lock_nu in range(0, 5):
            for zw in (0.0, 0.1, 0.2, 0.33, 0.5, 1.0):
                d = [delta_unified(n, r, lock_nu, zw) for n in range(3)]
                r_me = EIGHT_PI ** (d[2] - d[1])
                r_tm = EIGHT_PI ** (d[1] - d[0])
                sc = err_score(r_tm, r_me)
                best.append((sc, r, lock_nu, zw, r_tm, r_me))
    best.sort()
    for t in best[:12]:
        print(f"  sc={t[0]:.4f} r={t[1]} lock_nu={t[2]} zeta_w={t[3]:.3f}  tau/mu={t[4]:.2f}  mu/e={t[5]:.1f}")


def scan_offdiag() -> None:
    print("\n## Off-diagonal on sunshine diagonal")
    best = []
    for r in range(2, 7):
        for eta in (0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0):
            for eta_scale in (1.0, L_sun(), L_sun() * 12.0, FEIGENBAUM_A):
                e = eta * eta_scale
                r_tm, r_me = y_offdiag_sunshine(e, r)
                best.append((err_score(r_tm, r_me), r, e, r_tm, r_me))
    best.sort()
    for t in best[:10]:
        print(f"  sc={t[0]:.4f} r={t[1]} eta={t[2]:.2f}  tau/mu={t[3]:.2f}  mu/e={t[4]:.1f}")


def analytic_zeta_closure() -> None:
    print("\n## Analytic zeta / spectral candidates")
    base = tuple(y_sun(g) for g in range(3))
    candidates = [
        ("zeta2 on e only", (1.0, 1.0, ZETA2)),
        ("zeta2^(L/3) on e", (1.0, 1.0, ZETA2 ** (L_sun() / 3.0))),
        ("zeta2^(2/3) on e", (1.0, 1.0, ZETA2 ** (2.0 / 3.0))),
        ("zeta2^(1/2) on e", (1.0, 1.0, math.sqrt(ZETA2))),
        ("lock3 * zeta2 e", tuple(a * b for a, b in zip(block_lock_casimir(3), (1, 1, ZETA2)))),
        ("lock3 * zeta2^(L/3) e", tuple(a * b for a, b in zip(block_lock_casimir(3), (1, 1, ZETA2 ** (L_sun() / 3.0))))),
        ("lock3 * (Ne/Nl)^(L/12) e", tuple(a * b for a, b in zip(block_lock_casimir(3), (1, 1, (N_E / N_LOCK) ** (L_sun() / 12.0))))),
        ("lock3 * (5/3)^(2/3) mu/e", tuple(a * b for a, b in zip(block_lock_casimir(3), (1, (5.0 / 3.0) ** (2.0 / 3.0), 1.0)))),
        ("lock3 * (9/7)^(L/3)", tuple(a * b for a, b in zip(block_lock_casimir(3), block_casimir_chart_pow(L_sun() / 3.0)))),
    ]
    for name, fac in candidates:
        f = norm_e(fac)
        y = apply_factors(base, f)
        r_tm, r_me = ratios_y(y)
        print(f"  {name:32s}  tau/mu={r_tm:6.2f}  mu/e={r_me:6.1f}  err={err_score(r_tm, r_me):.4f}")


def solve_exact_factors() -> None:
    """What per-gen factors F_g (relative to e) hit BOTH ratios exactly with sunshine?"""
    print("\n## Exact factor targets (sunshine baseline)")
    y = [y_sun(g) for g in range(3)]
    f_mu = OBS_ME / (y[1] / y[2])  # multiply mu
    f_tau = OBS_TM / ((y[0] / y[1]) * f_mu)  # multiply tau? 
    # m_tm = (y0/y1)*(F0/F1) = OBS_TM => F0/F1 = OBS_TM * y1/y0
    f01 = OBS_TM * y[1] / y[0]
    f12 = OBS_ME * y[2] / y[1]
    print(f"  Need F_tau/F_mu = {f01:.4f}  F_mu/F_e = {f12:.4f}")
    print(f"  Product check F_tau/F_e = {f01*f12:.4f}  vs obs {OBS_TM*OBS_ME:.1f}")
    # structural decomposition
    a = [1.0 - (2 * g + 1) / 12.0 for g in range(3)]
    print(f"  Chart complements a_g = {a}")
    print(f"  (a_mu/a_e)^{-2} = {(a[1]/a[2])**(-2):.4f}  (a_tau/a_mu)^{-2} = {(a[0]/a[1])**(-2):.4f}")
    print(f"  zeta2 = {ZETA2:.4f}  zeta2^(1/6) = {ZETA2**(1/6):.4f}  pi^2/(6*e^(1/3)) etc.")


def main() -> None:
    print("# Sunshine exit hunt — all rabbit holes")
    print("=" * 70)
    print(f"  sunshine: tau/mu={ratios_y(tuple(y_sun(g) for g in range(3)))[0]:.1f}  mu/e={ratios_y(tuple(y_sun(g) for g in range(3)))[1]:.1f}")
    print(f"  PDG:      tau/mu={OBS_TM:.1f}  mu/e={OBS_ME:.1f}")
    print(f"  L={L_sun():.3f}  N_e/N_lock={N_E/N_LOCK:.1f}  zeta(2)={ZETA2:.4f}")

    solve_exact_factors()
    analytic_zeta_closure()
    grid_search_blocks()
    grid_delta_unified()
    scan_offdiag()

    print("\n## Best near-miss synthesis")
    base = tuple(y_sun(g) for g in range(3))
    fac = norm_e(tuple(a * b for a, b in zip(block_lock_casimir(3), (1.0, 1.0, ZETA2 ** (L_sun() / 3.0)))))
    y = apply_factors(base, fac)
    r_tm, r_me = ratios_y(y)
    print(f"  lock3 + zeta2^(L/3) on electron: tau/mu={r_tm:.2f} mu/e={r_me:.1f} err={err_score(r_tm, r_me):.4f}")


if __name__ == "__main__":
    main()
