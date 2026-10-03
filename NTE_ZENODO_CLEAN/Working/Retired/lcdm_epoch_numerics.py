#!/usr/bin/env python3
"""Fill LCDM P1 epoch table (homogeneous Friedmann, Planck 2018 Omegas)."""
import math

Om_r, Om_m, Om_L = 9e-5, 0.315, 0.685


def H_ratio(N: float) -> float:
    return math.sqrt(
        Om_r * math.exp(-4 * N) + Om_m * math.exp(-3 * N) + Om_L
    )


def find_N_for_H(target: float) -> float:
    lo, hi = -30.0, 0.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if H_ratio(mid) < target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def z_from_N(N: float) -> float:
    """Approximate: at matter domination H ~ (1+z)^{3/2} => N ~ -2/3 ln(1+z)."""
    if N >= -1e-12:
        return 0.0
    return math.exp(-1.5 * N) - 1


rows = []
rows.append(("Today", 0.0, 1.0))

H_z05 = math.sqrt(Om_m * 1.5**3 + Om_L + Om_r * 1.5**4)
N_z05 = find_N_for_H(H_z05)
rows.append(("z ~ 0.5 (DESI BAO era)", N_z05, H_z05))

N_eq = math.log(Om_m / Om_L) / 3
rows.append(("Matter-Lambda equality", N_eq, H_ratio(N_eq)))

z_bbn = 1e9
H_bbn = math.sqrt(Om_r * (1 + z_bbn) ** 4 + Om_m * (1 + z_bbn) ** 3 + Om_L)
rows.append(("BBN (radiation dom.; z ~ 1e9)", find_N_for_H(H_bbn), H_bbn))

print("| Epoch | N (from today) | H/H0 | |Phi|^2/v_EW^2 | rel alpha^2|Phi|^4 | rho_Phi=rho_crit? |")
print("|-------|----------------|------|---------------|---------------------|-------------------|")
for name, N, hr in rows:
    phi2 = hr**2
    rel = phi2
    match = "YES (trajectory+ident.)" if rel > 0 else "-"
    print(
        f"| {name} | {N:.4f} | {hr:.6g} | {phi2:.6g} | {rel:.6g} | {match} |"
    )
