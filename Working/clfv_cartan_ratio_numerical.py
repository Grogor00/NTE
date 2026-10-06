#!/usr/bin/env python3
"""CLFV Cartan ratio numerical verification — Cursor Scratch gate item.
Convention: Casas-Ibarra type-I seesaw dipole (Casas & Ibarra 2001; Hisano et al.).
Loop function F(x), x = M_N^2 / M_W^2.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

# PDG / NuFIT 5.3 (2024) NO central values (radians)
THETA12 = math.radians(33.7)
THETA13 = math.radians(8.6)
THETA23_NUFIT = math.radians(49.7)
THETA23_NTE = math.pi / 4
DELTA_CP = math.radians(197.0)

Y1 = (8 * math.pi) ** (-1 / 3)
Y3 = 1.0
M_W = 80.379  # GeV
M_R_NOM = 8.2e14  # GeV
V_EW = 246.0
G_F = 1.1663787e-5  # GeV^-2
ALPHA = 1 / 137.035999084
M_MU = 0.1056583745
M_TAU = 1.77686
M_E = 0.5109989461e-3

# Light neutrino masses (eV) — NO ordering, handoff/C13 bracket
M_NU1 = 0.0023
DM21_SQ = 7.5e-5  # eV^2
DM31_SQ = 2.5e-3
M_NU2 = math.sqrt(M_NU1**2 + DM21_SQ)
M_NU3 = math.sqrt(M_NU1**2 + DM31_SQ)

MEG2_LIMIT_BR = 4.2e-13  # MEG II 90% CL (order of magnitude)


def pmns_matrix(theta12, theta13, theta23, delta=DELTA_CP):
    c12, s12 = math.cos(theta12), math.sin(theta12)
    c13, s13 = math.cos(theta13), math.sin(theta13)
    c23, s23 = math.cos(theta23), math.sin(theta23)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * np.exp(-1j * delta)],
            [
                -s12 * c23 - c12 * s23 * s13 * np.exp(1j * delta),
                c12 * c23 - s12 * s23 * s13 * np.exp(1j * delta),
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * np.exp(1j * delta),
                -c12 * s23 - s12 * c23 * s13 * np.exp(1j * delta),
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


def loop_f(x: float) -> float:
    """Casas-Ibarra / Hisano heavy-neutrino loop function for dipole LFV."""
    if x <= 0:
        return 0.0
    if abs(x - 1.0) < 1e-10:
        return -1.5
    om = 1.0 - x
    return x / (2 * om) + math.log(x) / om**2 - 1.0 / om**2


def y_nu_nte(U: np.ndarray) -> np.ndarray:
    """3x3 Dirac neutrino Yukawa: Y1 on gen 1-2, Y3 on gen 3 (pass-1 structure)."""
    Y = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        Y[a, 0] = Y1 * np.conj(U[a, 0])
        Y[a, 1] = Y1 * np.conj(U[a, 1])
        Y[a, 2] = Y3 * np.conj(U[a, 2])
    return Y


def y_nu_anarchic(rng: np.random.Generator) -> np.ndarray:
    """Random 3x3 complex Yukawa, O(1) entries (anarchic baseline)."""
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    return z / np.linalg.norm(z) * 2.0


def y_nu_casas_ibarra(
    U: np.ndarray, masses_gev: np.ndarray, m_nu_ev: np.ndarray, R: np.ndarray
) -> np.ndarray:
    m = np.array([m_nu_ev[0], m_nu_ev[1], m_nu_ev[2]]) * 1e-9  # eV -> GeV
    pref = math.sqrt(2) / V_EW
    return pref * np.diag(np.sqrt(masses_gev)) @ R @ np.diag(np.sqrt(m)) @ U.conj().T


def dipole_amp(i: int, j: int, Y: np.ndarray, M_heavy: np.ndarray) -> complex:
    s = 0.0 + 0.0j
    for k in range(3):
        x = (M_heavy[k] / M_W) ** 2
        s += Y[i, k] * np.conj(Y[j, k]) * loop_f(x)
    return s


def br_dipole(i: int, j: int, Y: np.ndarray, M_heavy: np.ndarray, m_lepton: float) -> float:
    """BR(ℓ_i → ℓ_j γ) ∝ |A|² / m_i^5 (relative scale)."""
    A = dipole_amp(i, j, Y, M_heavy)
    return abs(A) ** 2 / m_lepton**5


def heavy_masses(theta13: float, M_R: float, m3_over_m1: float = 1.0) -> np.ndarray:
    M1 = M_R
    M2 = M_R * (1.0 + math.sin(theta13) ** 2)
    M3 = M_R * m3_over_m1
    return np.array([M1, M2, M3])


def amp_ratio_mu_e_tau_e(Y: np.ndarray, M_heavy: np.ndarray) -> float:
    """|A(μ→eγ)|² / |A(τ→eγ)|² — pass-1 scale-independent discriminator."""
    A_me = dipole_amp(1, 0, Y, M_heavy)
    A_te = dipole_amp(2, 0, Y, M_heavy)
    if abs(A_te) <= 0:
        return float("nan")
    return abs(A_me) ** 2 / abs(A_te) ** 2


def br_ratio_mu_e_tau_e(Y: np.ndarray, M_heavy: np.ndarray) -> float:
    """Full BR ratio including m_ℓ⁻⁵ phase space (not the pass-1 discriminator)."""
    br_me = br_dipole(1, 0, Y, M_heavy, M_MU)
    br_te = br_dipole(2, 0, Y, M_heavy, M_TAU)
    if br_te <= 0:
        return float("nan")
    return br_me / br_te


def tan2_theta23(U: np.ndarray) -> float:
    u_mu3, u_tau3 = U[1, 2], U[2, 2]
    return abs(u_mu3) ** 2 / abs(u_tau3) ** 2


def absolute_br_mu_e_gamma(Y: np.ndarray, M_heavy: np.ndarray) -> float:
    """Order-of-magnitude BR(μ→eγ): (3α/32π)(M_W/M_R_eff)^4 |A_flavor|² (seesaw scaling)."""
    A = dipole_amp(1, 0, Y, M_heavy)
    M_eff = float(np.mean(M_heavy))
    scale = (M_W / M_eff) ** 4
    pref = (3 * ALPHA) / (32 * math.pi)
    return pref * scale * abs(A) ** 2


def run_nte_scan():
    rows = []
    for label, th23 in [("NuFIT", THETA23_NUFIT), ("NTE_pi4", THETA23_NTE)]:
        U = pmns_matrix(THETA12, THETA13, th23)
        Y = y_nu_nte(U)
        target = tan2_theta23(U)
        for m3m1 in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            M = heavy_masses(THETA13, M_R_NOM, m3m1)
            r = amp_ratio_mu_e_tau_e(Y, M)
            dev = abs(r - target) / target if target > 0 else float("nan")
            rows.append(
                {
                    "case": label,
                    "theta23_deg": math.degrees(th23),
                    "M3_over_M1": m3m1,
                    "ratio": r,
                    "tan2_theta23": target,
                    "frac_dev": dev,
                    "within_10pct": bool(dev < 0.10),
                }
            )
    return rows


def run_anarchic_mc(n: int = 10_000, seed: int = 42):
    rng = np.random.default_rng(seed)
    U_nufit = pmns_matrix(THETA12, THETA13, THETA23_NUFIT)
    target = tan2_theta23(U_nufit)
    M = heavy_masses(THETA13, M_R_NOM, 1.0)
    ratios = []
    for _ in range(n):
        Y = y_nu_anarchic(rng)
        r = amp_ratio_mu_e_tau_e(Y, M)
        if math.isfinite(r) and r > 0:
            ratios.append(r)
    ratios = np.array(ratios)
    log_r = np.log10(ratios)
    log_t = math.log10(target)
    within_20 = np.sum(np.abs(ratios - target) / target <= 0.20) / len(ratios)
    within_50 = np.sum(np.abs(ratios - target) / target <= 0.50) / len(ratios)
    # mimic fraction: within factor 2 in log space (~ same as 20% for order unity
    mimic_20 = within_20
    return {
        "n_samples": len(ratios),
        "target_tan2_theta23": target,
        "median_ratio": float(np.median(ratios)),
        "log10_p16": float(np.percentile(log_r, 16)),
        "log10_p84": float(np.percentile(log_r, 84)),
        "frac_within_20pct": float(within_20),
        "frac_within_50pct": float(within_50),
        "mimic_fraction_20pct": float(mimic_20),
        "odds_nte_favored": float((1 - mimic_20) / mimic_20) if mimic_20 > 0 else float("inf"),
    }


def second_relations(U: np.ndarray, M_heavy: np.ndarray):
    Y = y_nu_nte(U)
    A_me = dipole_amp(1, 0, Y, M_heavy)
    A_te = dipole_amp(2, 0, Y, M_heavy)
    A_tm = dipole_amp(2, 1, Y, M_heavy)
    A_ee = dipole_amp(0, 0, Y, M_heavy)
    return {
        "amp_ratio_mu_e_tau_e": abs(A_me) ** 2 / abs(A_te) ** 2 if A_te else None,
        "amp_ratio_tau_mu_tau_e": abs(A_tm) ** 2 / abs(A_te) ** 2 if A_te else None,
        "dipole_A_ee_over_A_me": abs(A_ee / A_me) if A_me else None,
        "note": "μ→eee and μ–e conversion need penguin+box; dipole proxies only",
    }


def meg2_scale_estimate(Y_template, M_heavy, br_at_MR):
    """Rough M_R to reach MEG II: BR ∝ 1/M_R^4 for seesaw."""
    if br_at_MR <= 0:
        return None
    scale = (br_at_MR / MEG2_LIMIT_BR) ** 0.25
    return M_R_NOM / scale


def main():
    U_nte = pmns_matrix(THETA12, THETA13, THETA23_NTE)
    U_nufit = pmns_matrix(THETA12, THETA13, THETA23_NUFIT)
    M_nom = heavy_masses(THETA13, M_R_NOM, 1.0)
    Y_nte = y_nu_nte(U_nte)
    Y_nufit = y_nu_nte(U_nufit)

    scan = run_nte_scan()
    anarchic = run_anarchic_mc(10_000)
    sec_nte = second_relations(U_nte, M_nom)
    sec_nufit = second_relations(U_nufit, M_nom)
    br_abs = absolute_br_mu_e_gamma(Y_nte, M_nom)

    out = {
        "convention": "Casas-Ibarra 2001 / Hisano dipole; F(x) heavy-neutrino loop",
        "nte_scan": scan,
        "anarchic_mc": anarchic,
        "second_relations_nte_pi4": sec_nte,
        "second_relations_nufit": sec_nufit,
        "absolute_BR_mu_e_gamma_at_MR": br_abs,
        "MEG2_limit_order": MEG2_LIMIT_BR,
        "MR_for_MEG2_sensitivity_order": meg2_scale_estimate(Y_nte, M_nom, br_abs),
        "nte_point": {
            "amp_ratio_pi4": amp_ratio_mu_e_tau_e(Y_nte, M_nom),
            "tan2_pi4": tan2_theta23(U_nte),
            "amp_ratio_nufit": amp_ratio_mu_e_tau_e(Y_nufit, M_nom),
            "tan2_nufit": tan2_theta23(U_nufit),
            "br_ratio_pi4_with_m5": br_ratio_mu_e_tau_e(Y_nte, M_nom),
        },
    }
    path = Path(__file__).with_name("clfv_cartan_ratio_numerical_results.json")
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    return out


if __name__ == "__main__":
    main()
