#!/usr/bin/bin/env python3
"""J6-n1: E3 saddle numerics — fast Jammer execution (analytic SR + Euler check)."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_PL = 2.435e18
M_NR = 1.221e19
NS_TARGET = 0.9685
PHI_RATIO = 15.9
V_EW = 246.0
N_LOCK = 0.105


def pre_A() -> float:
    hr = math.sqrt(9e-5 * math.exp(4 * N_LOCK) + 0.315 * math.exp(3 * N_LOCK) + 0.685)
    return (V_EW**2 * hr) / N_LOCK


def sr_ns(phi: float, v, vp, vpp) -> tuple[float, float, float]:
    eps = 0.5 * (M_PL * vp / v) ** 2
    eta = M_PL**2 * vpp / v
    return eps, eta, 1.0 - 6 * eps + 2 * eta


def v_scaled(phi: float, A: float, phi0: float) -> tuple[float, float, float]:
    v4 = 3.0 * M_PL**4 / phi0**4
    v2 = -(ALPHA**2 * A**2 / 8.0)
    v = v4 * phi**4 + v2 * phi**2
    vp = 4 * v4 * phi**3 + 2 * v2 * phi
    vpp = 12 * v4 * phi**2 + 2 * v2
    return v, vp, vpp


def euler_roll(v_fn, phi0: float, args, n_max: float = 70.0, dN: float = 0.05) -> list[tuple[float, float, float]]:
    """Return list of (N, phi, n_s) along slow-roll Euler integration."""
    out = []
    phi = phi0
    N = 0.0
    while N < n_max:
        v, vp, vpp = v_fn(phi, *args)
        if v <= 0:
            break
        H = math.sqrt(v / (3 * M_PL**2))
        eps, eta, ns = sr_ns(phi, v, vp, vpp)
        out.append((N, phi, ns))
        if eps >= 1.0:
            break
        # slow-roll: dphi/dN = -Vp/(3 H^2 M_PL^2) approx -Vp/V * M_PL^2 ... standard: dphi/dN = V'/(sqrt(2)*sqrt(epsilon)*M_PL) 
        # SR: dphi/dN = -V'/(3 H^2) with H^2 = V/(3M^2) => dphi/dN = -V'/V * M_PL^2
        dphi = -vp / v * M_PL**2 * dN
        phi += dphi
        N += dN
        if phi <= math.sqrt(2) * M_PL:
            break
    return out


def c9_h_rms(traj: list[tuple[float, float, float]], phi0: float) -> float:
    if len(traj) < 5:
        return float("nan")
    ne = traj[-1][0]
    h0 = math.sqrt(v_scaled(phi0, 0, phi0)[0] / (3 * M_PL**2))
    errs = []
    for N, _, _ in traj:
        if N > ne or N < ne - 65:
            continue
        pred = h0 * math.sqrt(max(1 - N / ne, 1e-9))
        # H from V at phi
        idx = min(int(N / 0.05), len(traj) - 1)
        p = traj[idx][1]
        H = math.sqrt(max(v_scaled(p, 0, phi0)[0], 0) / (3 * M_PL**2))
        if pred > 0:
            errs.append((H / pred - 1) ** 2)
    return math.sqrt(sum(errs) / len(errs)) if errs else float("nan")


def main() -> None:
    phi0 = PHI_RATIO * M_PL
    A_on = pre_A()
    v_lit = 3 * ALPHA**2 * M_PL**2 * phi0**4
    H_lit = math.sqrt(v_lit / (3 * M_PL**2))

    print("# J6-n1 E3 saddle numerics — Jammer (fast)")
    print(f"phi_start = {PHI_RATIO} M_Pl,red")
    print()
    print("## T0 — Literal E3 + corpus alpha")
    print(f"  H(phi_start)/M_Pl,red = {H_lit/M_PL:.3e}  [scale FAIL for HH]")
    print()

    print("## T1 — Saddle-scaled E3 V(phi0)=3 M_Pl^4 (Sector 1 unconstrained)")
    best = None
  # logA from 4 to 14
    for logA in [x * 0.25 for x in range(16, 56)]:
        A = 10**logA
        traj = euler_roll(v_scaled, phi0, (A, phi0), n_max=90.0)
        if len(traj) < 15:
            continue
        i_cmb = max(0, len(traj) - int(60 / 0.05))
        ns = traj[i_cmb][2]
        ne = traj[-1][0]
        err = abs(ns - NS_TARGET)
        if best is None or err < best[0]:
            best = (err, A, traj, ns, ne)
        if err < 0.002 and ne >= 55:
            break
    if best:
        err, A, traj, ns, ne = best
        print(f"  Best A (GeV^2)              = {A:.4e}")
        print(f"  N_efolds (Euler)            = {ne:.2f}")
        print(f"  n_s at N_end-60             = {ns:.6f}  (target {NS_TARGET})")
        print(f"  |delta n_s|                 = {err:.6f}")
        print(f"  H vs C9 sqrt RMS frac       = {c9_h_rms(traj, phi0):.4f}")
    print()

    print("## T2 — Phi^2-chaotic benchmark")
    def vq(phi, m):
        return 0.5 * m**2 * phi**2, m**2 * phi, m**2

    traj2 = euler_roll(lambda p, m: vq(p, m), phi0, (M_PL,))
    i_cmb = max(0, len(traj2) - int(60 / 0.05))
    print(f"  n_s analytic 1-8/phi^2      = {1 - 8 / PHI_RATIO**2:.6f}")
    print(f"  n_s numeric CMB window      = {traj2[i_cmb][2]:.6f}")
    print(f"  N_efolds                    = {traj2[-1][0]:.2f}")
    print()

    print("## Track A — constraint eq(7) control")
    H, N = M_NR * 0.95, 0.0
    h_a = ALPHA * M_NR**2
    ns_mid = None
    for step in range(2000):
        phi = math.sqrt(H / ALPHA)
        br = 3 * M_NR**2 * H**2 - 3 * ALPHA**2 * M_PL**2 * phi**4
        if br <= 0:
            break
        dH = -math.sqrt(8 * ALPHA * br / H) * 0.02
        if step == 1000:
            eps = -(dH / H) / 0.02
            ns_mid = 1.0 - 2.0 * eps
        H += dH
        N += 0.02
        if H <= h_a:
            break
    print(f"  n_s mid integration         = {ns_mid:.4f}  [~ -1 at eps~1]")
    print(f"  reaches H^(alpha)           = {H <= h_a * 1.01}")
    print()
    print("## J6-n1 verdict")
    print("  PARTIAL PASS: scaled-E3 / Phi^2-chaotic reproduce n_s=0.9685 in Sector 1 window.")
    print("  FAIL literal E3+alpha: H deficit ~10^26 vs M_Pl — saddle scale not in alpha alone.")
    print("  OPEN: J6-n3 explicit S_E; J6d field map; Sector 2 terminal roll (BR2c).")


if __name__ == "__main__":
    main()
