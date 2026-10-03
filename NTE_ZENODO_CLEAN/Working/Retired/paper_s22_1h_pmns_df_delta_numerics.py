#!/usr/bin/env python3
"""Paper S5 v0.1 — PMNS + off-diagonal D_F Yukawa (no numpy)."""
from __future__ import annotations

import cmath
import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
INV_16PI2 = 1.0 / (16.0 * math.pi**2)
V_EW = 246.0
SQRT2 = math.sqrt(2.0)

M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777


def overlap(n: int, m: int) -> float:
    return (3.0 / 2.0) / (n + m + 1.5)


def d_s3(k: int) -> float:
    return float((k + 1) * (k + 2))


def s_geom(g: int, r: int) -> float:
    return (d_s3(0) / d_s3(g)) * (overlap(g, 0) ** (2 * r))


def delta_from_s(s: float, base: float = 2.0 / 3.0) -> float:
    return base - math.log(max(s, 1e-30)) / (3.0 * LN_8PI)


def y_from_delta(d: float) -> float:
    return EIGHT_PI ** (-d)


def pmns_u() -> list[list[complex]]:
    s13 = math.sqrt(0.0222)
    c13 = math.sqrt(1.0 - 0.0222)
    s12, c12 = math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)
    s23 = c23 = math.sqrt(0.5)
    return [
        [c12 * c13, s12 * c13, s13],
        [-s12 * c23 - c12 * s23 * s13, c12 * c23 - s12 * s23 * s13, s23 * c13],
        [s12 * s23 - c12 * c23 * s13, -c12 * s23 - s12 * c23 * s13, c23 * c13],
    ]


def mat_mul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def mat_dagger(m: list[list[complex]]) -> list[list[complex]]:
    return [[m[j][i].conjugate() for j in range(3)] for i in range(3)]


def y_geom_matrix(r: int, eta: float) -> list[list[float]]:
    s = [s_geom(g, r) for g in range(3)]
    yd = [y_from_delta(delta_from_s(sg)) for sg in s]
    y = [[0.0] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            if a == b:
                y[a][b] = yd[a]
            else:
                oab = overlap(a, b)
                y[a][b] = eta * INV_16PI2 * math.sqrt(s[a] * s[b]) * oab * yd[a]
    return y


def eigh_symmetric_3x3(a: list[list[float]]) -> list[float]:
    """Real symmetric 3x3 via Jacobi."""
    m = [row[:] for row in a]
    for _ in range(50):
        p, q = 0, 1
        max_off = abs(m[0][1])
        for (i, j) in ((0, 2), (1, 2)):
            if abs(m[i][j]) > max_off:
                max_off, p, q = abs(m[i][j]), i, j
        if max_off < 1e-14:
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


def complex_to_real_eigs(y: list[list[float]]) -> list[float]:
    return eigh_symmetric_3x3([[y[i][j] for j in range(3)] for i in range(3)])


def y_pmns(yg: list[list[float]]) -> list[list[float]]:
    u = pmns_u()
    yc = [[complex(yg[i][j], 0) for j in range(3)] for i in range(3)]
    p = mat_mul(mat_mul(u, yc), mat_dagger(u))
    return [[p[i][j].real for j in range(3)] for i in range(3)]


def delta_cumulative(n_gen: int, r: int) -> float:
    prod = 1.0
    for g in range(n_gen + 1):
        prod *= s_geom(g, r)
    return delta_from_s(prod)


def main() -> None:
    print("# Paper S5 — off-diagonal D_F + PMNS (Jammer v0.1h)")
    print("=" * 60)
    print(f"\n  obs m_mu/m_e = {M_MU/M_E:.1f}  m_tau/m_mu = {M_TAU/M_MU:.1f}")

    print("\n## Cumulative S_prod (S5b bracket)")
    for r in (2, 3):
        for n, nm in enumerate(("tau", "mu", "e")):
            d = delta_cumulative(n, r)
            print(f"  r={r}  delta_{nm} cum (n<={n}) = {d:.3f}")

    for r in (2, 3):
        print(f"\n## r={r}")
        for eta in (1.0, 4.0, 12.0, 40.0):
            yg = y_geom_matrix(r, eta)
            ev = complex_to_real_eigs(yg)
            r_me = (ev[1] / ev[0]) ** 2
            r_tm = (ev[2] / ev[1]) ** 2
            evp = complex_to_real_eigs(y_pmns(yg))
            r_mep = (evp[1] / evp[0]) ** 2
            r_tmp = (evp[2] / evp[1]) ** 2
            print(f"  eta={eta:4.0f}  gen: mu/e={r_me:6.1f} tau/mu={r_tm:5.1f}  |  +PMNS: mu/e={r_mep:6.1f} tau/mu={r_tmp:5.1f}")

    print("\n## Verdict")
    print("  Unitary PMNS alone: no change (spectrum invariant).")
    print("  Off-diagonal O_ab/(16pi^2): tau/mu can match; mu/e needs eta>>1 or higher tower.")


if __name__ == "__main__":
    main()
