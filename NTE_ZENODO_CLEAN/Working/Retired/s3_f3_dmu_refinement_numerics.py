#!/usr/bin/env python3
"""S3-f3 refinement: dmu(V) integral reproduces Paper S4 closure."""
from __future__ import annotations

import math

M_PL = 2.435e18
M_NR = 1.221e19
ALPHA = 2.38e-47
N_E = -math.log(ALPHA * M_NR)
VOL_S3 = 2 * math.pi**2
V_LOCK = VOL_S3 * math.exp(3 * N_E)
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
BETA_GB = math.sqrt(2 * math.pi) / M_PL
H0 = ALPHA * 246.0**2


def V_of_N(N: float) -> float:
    return VOL_S3 * math.exp(3 * N)


def h_sector2(N: float) -> float:
    return M_NR * math.exp(-N)


def h_post(N: float) -> float:
    om_r, om_m, om_l = 9e-5, 0.315, 0.685
    h = math.sqrt(om_r * math.exp(-4 * N) + om_m * math.exp(-3 * N) + om_l)
    return H0 * h


def integrate_weighted(
    n0: float,
    n1: float,
    weight: str,
    h_fn,
    rho_fn,
    step: float = 0.05,
) -> tuple[float, float]:
    """Return (int rho w dN, int w dN)."""
    n = n0
    num = den = 0.0
    while n <= n1 + 1e-12:
        V = V_of_N(n)
        H = max(h_fn(n), 1e-300)
        rho = rho_fn(n, V)
        if weight == "uniform":
            w = 1.0
        elif weight == "dt_H":
            w = 1.0 / H
        elif weight == "dlnV":
            w = 1.0 / (3 * V)
        else:
            raise ValueError(weight)
        num += rho * w * step
        den += w * step
        n += step
    return num, den


def mu_lock_integral() -> float:
    """Refined NTE measure: int rho(V) dmu with dmu = (1/V_lock) delta(V-V_lock) dV."""
    return LAMBDA_A4 / V_LOCK


def mu_lock_from_N_delta() -> float:
    """Equivalent: int rho(N) delta(N-N_e) dN with rho(N)=Lambda_a4/V(N)."""
    return LAMBDA_A4 / V_of_N(N_E)


def main() -> None:
    print("# S3-f3 dmu(V) refinement — measure integral vs Paper S4 closure")
    print(f"N_e     = {N_E:.6f}")
    print(f"V_lock  = {V_LOCK:.4e}")
    print(f"Lambda_a4 = {LAMBDA_A4:.4e} GeV^4")
    print(f"Lambda_obs = {LAMBDA_OBS:.4e} GeV^4")
    closure = LAMBDA_A4 * math.exp(-3 * N_E) / VOL_S3
    print(f"Paper S4 closure = {closure:.4e} GeV^4  ratio/obs = {closure/LAMBDA_OBS:.4f}")
    print()

    print("## A. Refined lock-cell measure (Paper S4 / S3-f3 v0.2)")
    for name, val in [
        ("int rho dmu_lock (delta V)", mu_lock_integral()),
        ("int rho delta(N-N_e) dN", mu_lock_from_N_delta()),
    ]:
        print(f"  {name:32s} = {val:.4e}  ratio/obs = {val/LAMBDA_OBS:.4f}")
    print("  => Refined dmu REPRODUCES Paper S4 closure exactly.")
    print()

    rho_const = lambda n, v: LAMBDA_A4
    rho_vol = lambda n, v: LAMBDA_A4 / v

    print("## B. S3-f3 v0.1 weight schemes (rho = Lambda_a4 constant)")
    segments = [
        ("pre-lock S2", 0.0, N_E, h_sector2),
        ("post-lock", -30.0, 0.0, h_post),
    ]
    for wname in ("uniform", "dt_H", "dlnV"):
        print(f"  Weight {wname}:")
        for seg_name, n0, n1, hfn in segments:
            num, den = integrate_weighted(n0, n1, wname, hfn, rho_const, step=0.1)
            avg = num / den if den else float("nan")
            print(f"    {seg_name:14s}  <rho>_w = {avg:.4e}  log10/obs = {math.log10(avg/LAMBDA_OBS):.1f}")
    print("  => Trajectory-averaged constant rho does NOT close gap (confirms S3-f3).")
    print()

    print("## C. Volume-normalised density rho(N)=Lambda_a4/V(N)")
    print("  Weight uniform on [0, N_e]:")
    num, den = integrate_weighted(0, N_E, "uniform", h_sector2, rho_vol, step=0.05)
    avg = num / den
    print(f"    <rho/V>_uniform = {avg:.4e}  ratio/obs = {avg/LAMBDA_OBS:.4f}")
    print(f"    value at N=N_e only = {LAMBDA_A4 / V_of_N(N_E):.4e}  (closure)")
    print("  => Only N=N_e (lock) evaluation matches — not the pre-lock average.")
    print()

    print("## D. Discrete lock measure vs smeared Gaussian in N")
    for sigma in [0.0, 0.1, 1.0, 5.0]:
        if sigma == 0:
            lam = mu_lock_from_N_delta()
        else:
            # int Lambda_a4 * 2pi^2/V(N) * exp(-(N-Ne)^2/2sigma^2) dN / int exp ...
            step = 0.02
            n = 0.0
            num = den = 0.0
            while n <= N_E + 5 * sigma + 1:
                ker = math.exp(-0.5 * ((n - N_E) / sigma) ** 2) if sigma else 0.0
                if sigma == 0:
                    break
                num += LAMBDA_A4 / V_of_N(n) * ker * step
                den += ker * step
                n += step
            lam = num / den if den else float("nan")
        print(f"  sigma_N = {sigma:4.1f}  Lambda_eff = {lam:.4e}  ratio/obs = {lam/LAMBDA_OBS:.4f}")
    print("  => Measure must be lock-localised (sigma->0) — event G, not smeared history.")
    print()

    print("## E. Formal refined definition")
    print("  dmu_ref(V) = (1 / V_lock) delta(V - V_lock) dV")
    print("  rho_Lambda(V) = Lambda_a4  (spectral lock amplitude)")
    print("  Lambda_obs = int rho dmu_ref = Lambda_a4 / V_lock")
    print("  Equivalent: rho(N)=Lambda_a4/V(N), dmu= delta(N-N_e) dN")
    print()
    print("## S3-f3 refinement verdict")
    print("  v0.1 gap: averaged trajectory weights without lock-cell normalisation.")
    print("  v0.2: unimodular + event G fixes dmu at V_lock with 1/V_lock normalisation.")
    print("  Integral matches Paper S4 Proposition 4 @ 1.05x obs.")


if __name__ == "__main__":
    main()
