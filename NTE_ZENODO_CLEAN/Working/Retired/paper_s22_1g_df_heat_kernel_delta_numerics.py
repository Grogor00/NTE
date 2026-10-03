#!/usr/bin/env python3
"""L4 — delta_n from D_F heat-kernel / S^3 spectral weights (non-circular geometry)."""
from __future__ import annotations

import math

EIGHT_PI = 8.0 * math.pi
LN_8PI = math.log(EIGHT_PI)
V_EW = 246.0
SQRT2 = math.sqrt(2.0)
INV_16PI2 = 1.0 / (16.0 * math.pi**2)

M_E = 0.000510999
M_MU = 0.105658
M_TAU = 1.777

# generation labels: 0=tau, 1=mu, 2=e (lightest = largest mode index)
GEN = ("tau", "mu", "e")
IDX = {"tau": 0, "mu": 1, "e": 2}


def d_s3(k: int) -> float:
    return float((k + 1) * (k + 2))


def overlap(n: int, m: int = 0) -> float:
    return (3.0 / 2.0) / (n + m + 1.5)


def y_from_mass(m: float) -> float:
    return SQRT2 * m / V_EW


def delta_from_y(y: float) -> float:
    return -math.log(y) / LN_8PI


def delta_from_supp(supp: float, delta_base: float = 2.0 / 3.0) -> float:
    """delta = delta_base - (1/3) log_{8pi}(supp); supp=1 at tau anchor."""
    if supp <= 0:
        return float("nan")
    return delta_base - math.log(supp) / (3.0 * LN_8PI)


def model_hk_a(r: int = 2) -> dict[str, float]:
    """HK-A: (D_F^2)_g ~ M_1^2 * (d_0/d_g) * O_{g,0}^{2r}  (S2-C-C block + S3 spectrum)."""
    d0 = d_s3(0)
    out: dict[str, float] = {}
    for name, g in zip(GEN, range(3)):
        o = overlap(g, 0)
        supp = (d0 / d_s3(g)) * (o ** (2 * r))
        out[name] = delta_from_supp(supp)
    return out


def model_hk_b() -> dict[str, float]:
    """HK-B: radiative tower sum_{k=0}^{g} O_{k,0}^2 / (16 pi^2)."""
    delta_base = 2.0 / 3.0
    out: dict[str, float] = {}
    for name, g in zip(GEN, range(3)):
        stack = sum(overlap(k, 0) ** 2 for k in range(g + 1))
        out[name] = delta_base + stack * INV_16PI2
    return out


def model_hk_c() -> dict[str, float]:
    """HK-C: delta = 2/3 + ln(d_g/d_0) / ln(8pi)  (multiplicity depth)."""
    d0 = d_s3(0)
    out: dict[str, float] = {}
    for name, g in zip(GEN, range(3)):
        out[name] = 2.0 / 3.0 + math.log(d_s3(g) / d0) / LN_8PI
    return out


def model_hk_d() -> dict[str, float]:
    """HK-D: CC2008 single-gen weight w_g = d_g / lambda_g^2; delta from ln(w_tau/w_g)."""
    out: dict[str, float] = {}
    w = []
    for g in range(3):
        lam = 1.5 + g
        w.append(d_s3(g) / (lam**2))
    w_tau = w[0]
    for name, g in zip(GEN, range(3)):
        out[name] = 2.0 / 3.0 + math.log(w_tau / w[g]) / LN_8PI
    return out


def mass_ratio_from_delta(de: float, dm: float, dt: float) -> tuple[float, float]:
    r_me = EIGHT_PI ** (de - dm)
    r_tm = EIGHT_PI ** (dm - dt)
    return r_me, r_tm


def main() -> None:
    print("# L4 D_F heat-kernel — delta_n numerics (Jammer v0.1g)")
    print("=" * 60)

    obs = {n: delta_from_y(y_from_mass(m)) for n, m in zip(GEN, (M_TAU, M_MU, M_E))}
    print("\n## Observed (phenomenological guide)")
    for n in GEN:
        print(f"  delta_{n:3s} (from m)     = {obs[n]:.3f}")

    models = [
        ("HK-A associator r=2", model_hk_a(2)),
        ("HK-A associator r=3", model_hk_a(3)),
        ("HK-B radiative stack", model_hk_b()),
        ("HK-C multiplicity log", model_hk_c()),
        ("HK-D eigenvalue weight", model_hk_d()),
    ]

    print("\n## Geometric models (non-circular)")
    for title, d in models:
        print(f"\n  [{title}]")
        for n in GEN:
            print(f"    delta_{n:3s} = {d[n]:.3f}")
        r_me, r_tm = mass_ratio_from_delta(d["e"], d["mu"], d["tau"])
        print(f"    pred m_mu/m_e = {r_me:.1f}  (obs {M_MU/M_E:.1f})")
        print(f"    pred m_tau/m_mu = {r_tm:.1f}  (obs {M_TAU/M_MU:.1f})")

    print("\n## Tr_F(D_F^2) sector split (S2-C-C)")
    tr_nu = 2.0 / 3.0  # leading Y_nu2 register
    print(f"  delta_nu2 (Dirac transverse)  = {tr_nu:.3f}")
    print(f"  delta_singlet base (L2)       = {2.0/3.0:.3f}")
    print(f"  delta_e (HK-A r=2)            = {model_hk_a(2)['e']:.3f}")

    print("\n## Verdict")
    print("  HK-A r=2: order correct for hierarchy; magnitudes bracket not closure.")
    print("  Full closure needs PMNS-embedded D_F + mixing (Paper S5).")


if __name__ == "__main__":
    main()
