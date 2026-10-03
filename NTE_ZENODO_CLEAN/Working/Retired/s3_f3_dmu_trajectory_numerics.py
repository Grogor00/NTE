#!/usr/bin/env python3
"""S3-f3: dmu(V) from Phi(N) / H(N) trajectory (Jammer)."""
from __future__ import annotations

import math
from dataclasses import dataclass

ALPHA = 2.38e-47
M_PL = 2.435e18
M_NR = 1.221e19
V_EW = 246.0
N_E = 63.4056
N_LOCK = 45.0 / (4.0 * 106.75)
OM_R, OM_M, OM_L = 9e-5, 0.315, 0.685
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
H0 = ALPHA * V_EW**2


def h_ratio(N: float) -> float:
    return math.sqrt(OM_R * math.exp(-4 * N) + OM_M * math.exp(-3 * N) + OM_L)


@dataclass
class Segment:
    name: str
    n0: float
    n1: float
    h_fn: callable


def V_of_N(N: float, v0: float = 1.0) -> float:
    return v0 * math.exp(3.0 * N)


def phi_post(N: float) -> float:
    return V_EW * math.sqrt(h_ratio(N))


def h_post(N: float) -> float:
    return H0 * h_ratio(N)


def h_sector2(N: float) -> float:
    return M_NR * math.exp(-N)


def h_sector1(N: float, ne: float = 63.4) -> float:
    """Sector 1 Role B: C9 H = H_HH sqrt(1 - N/Ne)."""
    x = max(1.0 - N / ne, 1e-12)
    return M_PL * math.sqrt(x)


def phi_sector1(N: float, ne: float = 63.4) -> float:
    """Role B inflaton scale (not constraint Phi_NTE)."""
    phi_inf = 15.9 * M_PL
    # slow-roll Phi^2 chaotic: Phi(N) ~ Phi_inf * sqrt(1 - N/Ne) schematic
    x = max(1.0 - N / ne, 1e-12)
    return phi_inf * math.sqrt(x)


def integrate_segment(seg: Segment, weight: str, n_step: float = 0.05) -> dict:
    """Integrate over N in [n0, n1] with weight scheme."""
    n = seg.n0
    sum_w = 0.0
    sum_v = 0.0
    sum_v13 = 0.0
    sum_hinv = 0.0
    sum_phi4 = 0.0
    while n <= seg.n1 + 1e-12:
        if seg.name == "post-lock":
            H = h_post(n)
            phi = phi_post(n)
        elif seg.name.startswith("pre-lock S1"):
            H = h_sector1(n)
            phi = phi_sector1(n)
        else:
            H = h_sector2(n)
            phi = math.sqrt(max(H / ALPHA, 0.0))
        V = V_of_N(n)
        if weight == "uniform_N":
            w = 1.0
        elif weight == "dt_H":
            w = 1.0 / max(H, 1e-300)
        elif weight == "dlnV":
            w = 1.0 / (3.0 * max(V, 1e-300))
        else:
            raise ValueError(weight)
        dn = n_step
        sum_w += w * dn
        sum_v += w * V * dn
        sum_v13 += w * (V ** (1 / 3)) * dn
        sum_hinv += w * (1.0 / max(H, 1e-300)) * dn
        sum_phi4 += w * (ALPHA**2 * phi**4) * dn
        n += n_step
    return {
        "sum_w": sum_w,
        "mean_V": sum_v / sum_w if sum_w else float("nan"),
        "mean_V13": sum_v13 / sum_w if sum_w else float("nan"),
        "mean_Hinv": sum_hinv / sum_w if sum_w else float("nan"),
        "mean_alpha_phi4": sum_phi4 / sum_w if sum_w else float("nan"),
    }


def pushforward_dmu_v(V: float, v_min: float, v_max: float, n_pts: int = 5000) -> float:
    """Approximate mu(V in [v_min,v_max]) for piecewise trajectory (uniform N)."""
    # Pre-lock sector 2
    mu = 0.0
    dn = N_E / n_pts
    for i in range(n_pts):
        N = i * dn
        Vn = V_of_N(N, v0=1.0)
        if v_min <= Vn <= v_max:
            mu += dn / (3.0 * max(Vn, 1e-300))
    # Post-lock N in [-30, 0]
    dn2 = 30.0 / n_pts
    for i in range(n_pts + 1):
        N = -30.0 + i * dn2
        Vn = V_of_N(N - N_E, v0=math.exp(3 * N_E))  # anchor continuity at lock
        if v_min <= Vn <= v_max:
            mu += dn2 / (3.0 * max(Vn, 1e-300))
    return mu


def main() -> None:
    segments = [
        Segment("pre-lock S1 (Role B C9)", 0.0, N_E, h_sector1),
        Segment("pre-lock S2 (Role A roll)", 0.0, N_E, h_sector2),
        Segment("post-lock (lcdm)", -30.0, 0.0, h_post),
    ]
    print("# S3-f3 dmu(V) from Phi(N) trajectory — Jammer")
    print(f"Lambda_a4 residual = {LAMBDA_A4:.4e} GeV^4")
    print(f"Lambda_obs         = {LAMBDA_OBS:.4e} GeV^4")
    print(f"log10 gap          = {math.log10(LAMBDA_A4/LAMBDA_OBS):.2f}")
    print()

    for wname in ("uniform_N", "dt_H", "dlnV"):
        print(f"## Weight scheme: {wname}")
        total_w = 0.0
        for seg in segments:
            r = integrate_segment(seg, wname, n_step=0.1 if seg.name.startswith("pre") else 0.05)
            total_w += r["sum_w"]
            print(f"  {seg.name:28s}  sum_w={r['sum_w']:.4e}  <V>={r['mean_V']:.4e}  <V^1/3>={r['mean_V13']:.4e}")
            print(f"    <H^-1>={r['mean_Hinv']:.4e}  <alpha^2 Phi^4>={r['mean_alpha_phi4']:.4e} GeV^4")
        print(f"  Total measure (unnorm) = {total_w:.4e}")
        print()

    print("## Sector 1 vs Sector 2 — dt_H weight share (pre-lock only)")
    s1 = integrate_segment(segments[0], "dt_H", n_step=0.2)
    s2 = integrate_segment(segments[1], "dt_H", n_step=0.2)
    share1 = s1["sum_w"] / (s1["sum_w"] + s2["sum_w"])
    print(f"  Sector 1 fraction of pre-lock dt-weight = {share1:.4f}")
    print(f"  Sector 1 <H^-1> = {s1['mean_Hinv']:.4e}  vs S2 = {s2['mean_Hinv']:.4e}")
    print()

    v_lock = math.exp(3 * N_E)
    bins = [
        (1.0, 1e10, "pre-lock bulk"),
        (1e10, 1e50, "mid"),
        (1e50, 1e200, "near lock V"),
    ]
    for lo, hi, lab in bins:
        mu = pushforward_dmu_v(0, lo, hi)
        print(f"  mu(V in [{lo:.0e},{hi:.0e}]) ~ {mu:.4e}  ({lab})")
    print(f"  V at lock ~ exp(3 N_e) = {v_lock:.4e}")
    print()

    print("## Lambda_eff bracket (honest)")
    # If residual density ~ Lambda_a4 uniform in configurations, trajectory weight doesn't change scale
    lambda_eff_uniform = LAMBDA_A4
    # Volume-weighted naive: Lambda ~ Lambda_a4 / <V>^(1/3) scale — still insufficient
    r_pre = integrate_segment(segments[0], "dlnV", n_step=0.2)
    vol_supp = r_pre["mean_V"] ** (-1)  # illustrative 1/V weight
    lambda_vol = LAMBDA_A4 * vol_supp
    print(f"  Lambda_a4 (constant residual)     = {LAMBDA_A4:.4e} GeV^4")
    print(f"  x 1/<V>_pre (illustrative)         = {lambda_vol:.4e} GeV^4")
    print(f"  log10 to obs still                = {math.log10(lambda_vol/LAMBDA_OBS):.1f}")
    print()
    print("## S3-f3 verdict")
    print("  dmu(V) CONSTRUCTED from BR2c S1 (C9) + S2 (Role A) + lcdm post-lock.")
    print("  dt_H weight: Sector 2 terminal roll dominates (~100%); S1 negligible (H~M_Pl).")
    print("  Trajectory-derived dmu does NOT alone supply ~10^83 suppression.")
    print("  R3 (a6+ exponential) + R1 (f moments) still required per Paper S3 route.")


if __name__ == "__main__":
    main()
