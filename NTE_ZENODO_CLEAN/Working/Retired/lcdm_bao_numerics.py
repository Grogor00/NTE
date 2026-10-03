#!/usr/bin/env python3
"""Homogeneous LCDM/NTE BAO distances: D_C, D_M, D_V vs DESI DR1 anchors."""
import math

C_KM_S = 299792.458  # km/s; with H0 in km/s/Mpc gives D in Mpc
OM_R, OM_M, OM_L = 9e-5, 0.315, 0.685
R_D = 147.09  # Mpc, Planck 2018 fiducial (fixed, not refit)

PARAM_SETS = [
    ("Planck 2018", 67.4),
    ("NTE construction", 67.6),
]

# DESI 2024 DR1 (arXiv:2404.03002 Table 1); BGS uses D_V, others D_M
DESI_ROWS = [
    ("BGS", 0.295, "D_V", 7.93, 0.15),
    ("LRG1", 0.510, "D_M", 13.62, 0.25),
    ("LRG2", 0.706, "D_M", 16.85, 0.32),
    ("LRG3+ELG1", 0.930, "D_M", 21.71, 0.28),
    ("ELG2", 1.317, "D_M", 27.79, 0.69),
]


def E(z: float) -> float:
    return math.sqrt(OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3 + OM_L)


def comoving_distance(z: float, H0: float, steps: int = 4000) -> float:
    if z <= 0:
        return 0.0
    dz = z / steps
    s = sum(dz / E((i + 0.5) * dz) for i in range(steps))
    return (C_KM_S / H0) * s


def D_H(z: float, H0: float) -> float:
    """Hubble distance c/H(z) in Mpc."""
    return C_KM_S / (H0 * E(z))


def D_V(z: float, D_M: float, H0: float) -> float:
    """DESI-style volume distance: (z * D_M^2 * D_H)^(1/3)."""
    return (z * D_M**2 * D_H(z, H0)) ** (1 / 3)


def main():
    print("Homogeneous LambdaCDM distances (NTE H(z) identical at matched Omegas)")
    print(f"r_d = {R_D} Mpc (fixed)\n")
    print(
        "| tracer | z_eff | obs | LCDM Planck | LCDM NTE | "
        "DESI | Delta/sigma |"
    )
    print("|--------|-------|-----|-------------|----------|------|-------------|")

    H0_p, H0_n = 67.4, 67.6
    for _tr, z_eff, obs_type, desi_val, desi_sig in DESI_ROWS:
        D_C_p = comoving_distance(z_eff, H0_p)
        D_C_n = comoving_distance(z_eff, H0_n)
        dm_p, dm_n = D_C_p / R_D, D_C_n / R_D
        dv_p = D_V(z_eff, D_C_p, H0_p) / R_D
        dv_n = D_V(z_eff, D_C_n, H0_n) / R_D
        pred_p = dv_p if obs_type == "D_V" else dm_p
        pred_n = dv_n if obs_type == "D_V" else dm_n
        delta = pred_p - desi_val
        nsig = delta / desi_sig if desi_sig else float("nan")
        print(
            f"| {_tr} | {z_eff:.3f} | {obs_type} | {pred_p:.3f} | {pred_n:.3f} | "
            f"{desi_val:.2f}+/-{desi_sig:.2f} | {delta:+.3f} ({nsig:+.2f} sig) |"
        )

    print("\nNTE vs Planck H0 column shift (homogeneous):")
    z = 0.51
    dm_p = comoving_distance(z, H0_p) / R_D
    dm_n = comoving_distance(z, H0_n) / R_D
    print(f"  z={z}: Delta(D_M/r_d) = {dm_n - dm_p:.4f} ({100*(dm_n/dm_p-1):.3f}%)")

    print("\nStep A identity check: H(z)/H0 at z=0.51 =", E(0.51))


if __name__ == "__main__":
    main()
