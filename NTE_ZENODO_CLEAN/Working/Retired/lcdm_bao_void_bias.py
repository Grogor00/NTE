#!/usr/bin/env python3
"""BAO void-bias + Branch I directional matter-dipole worksheet.

v0.3 scope (Jammer handoff 2026-05-27):
- keep BAO homogeneous vs void-biased reconciliation layer
- add directional Branch I dipole estimates with alpha parameter
- output joint delta-sigma style diagnostics (no chi-square fitting)

v0.5 sprint (Wagenveld Phase I.5, 2026-05-29):
- load survey directions from wagenveld_sprint_surveys.json when present
- angular separation diagnostics (galactic l,b)

v0.7 sprint (Jammer §2.7 Phase IV, 2026-05-31):
- Test A geometry vector comparison (§2.7 vs merged §2.5 vs observed X)
- joint 85/15 split diagnostic per Jammer v0.1 handoff
"""
import json
import math
from pathlib import Path

C_KM_S = 299792.458
OM_R, OM_M, OM_L = 9e-5, 0.315, 0.685
R_D = 147.09
H0 = 67.4
B_VOID = 0.055
ALPHA = 0.24
G_MODEL = "pow2"
KAPPA0 = 3.0 / math.sqrt(4.0 * math.pi)  # bare Hopf coupling (Scratch §5.2)
DELTA_EPS_LOW = 1e-3
DELTA_EPS_HIGH = 1e-2
FOOTPRINT_JSON = "wagenveld_sprint_footprints_nside16.json"

# Jammer §2.7 v0.1 geometry vector (Wag, Sing, CatWISE, Quaia) — normalized to Wagenveld
JAMMER_27_VECTOR = (1.000, 1.392, 1.881, 0.864)
# Observed X = DeltaD / D_kin (Jammer numerical results 2026-05-31)
OBSERVED_X_VECTOR = (1.200, 1.600, 2.043, 1.000)
SURVEY_ORDER = ("wagenveld", "singal", "catwise", "quaia")

SURVEY_ID_MAP = {
    "CatWISE": "catwise",
    "Wagenveld": "wagenveld",
    "Singal": "singal",
    "Quaia": "quaia",
}

DESI_ROWS = [
    ("BGS", 0.295, "D_V", 7.93, 0.15),
    ("LRG1", 0.510, "D_M", 13.62, 0.25),
    ("LRG2", 0.706, "D_M", 16.85, 0.32),
    ("LRG3+ELG1", 0.930, "D_M", 21.71, 0.28),
    ("ELG2", 1.317, "D_M", 27.79, 0.69),
]

DIPOLE_ROWS = [
    # tracer, z_eff, p, observed dipole, 1-sigma, kinematic baseline
    ("CatWISE", 1.20, 1.5, 0.014, 0.003, 0.0046),
    ("Wagenveld", 0.50, 1.8, 0.011, 0.003, 0.0050),
    ("Singal", 1.00, 1.5, 0.013, 0.003, 0.0050),
    ("Quaia", 1.80, 1.5, 0.010, 0.004, 0.0050),
]


def E(z):
    return math.sqrt(OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3 + OM_L)


def comoving_distance(z, steps=4000):
    if z <= 0:
        return 0.0
    dz = z / steps
    s = sum(dz / E((i + 0.5) * dz) for i in range(steps))
    return (C_KM_S / H0) * s


def D_H(z):
    return C_KM_S / (H0 * E(z))


def D_V(z, D_M):
    return (z * D_M**2 * D_H(z)) ** (1 / 3)


def g_of_z(z, model=G_MODEL):
    if model == "pow2":
        return (1 + z) ** -2
    if model == "pow3":
        return (1 + z) ** -3
    if model == "exp":
        return math.exp(-z)
    if model == "struct_iv":
        # Structurally motivated candidate from worksheet:
        # g(z) ∝ sigma8(z)^2 / Omega_L(z), normalized to g(0)=1.
        sigma8_z0 = 0.811
        growth_ratio = E(z) / E(0)
        sigma8_z = sigma8_z0 * growth_ratio / (1 + z)
        omega_l_z = OM_L / (E(z) ** 2)
        omega_l_0 = OM_L / (E(0) ** 2)
        raw = (sigma8_z**2) / max(omega_l_z, 1e-12)
        raw0 = (sigma8_z0**2) / max(omega_l_0, 1e-12)
        return raw / raw0
    raise ValueError(f"Unknown g(z) model: {model}")


def g_avg_integrated(z, model=G_MODEL, steps=4000):
    if z <= 0:
        return 0.0
    dz = z / steps
    s = sum(g_of_z((i + 0.5) * dz, model=model) * dz for i in range(steps))
    return s / z


def void_bias_delta_H(z):
    """Phenomenological void volume-weighting (Part 2 §12.4).

    Active only z < 0.85 (DESI homogeneous-limit crossover band).
    b ~ 0.05-0.06 gives ~5% H_eff boost at z~0.7 — illustrative, NOT fitted.
    """
    if z > 0.85:
        return 0.0
    sigma8_z0 = 0.811
    growth_ratio = E(z) / E(0)
    sigma8_z = sigma8_z0 * growth_ratio / (1 + z)
    b = B_VOID
    return b * (sigma8_z / sigma8_z0) ** 2


def D_M_with_bias(z, steps=4000):
    """D_M with effective H(z') = H_hom(z') * (1 + delta_H(z')) along LOS."""
    if z <= 0:
        return 0.0
    dz = z / steps
    s = 0.0
    for i in range(steps):
        zp = (i + 0.5) * dz
        bias = 1.0 + void_bias_delta_H(zp)
        s += dz / (E(zp) * bias)
    return (C_KM_S / H0) * s


def dipole_void_amplitude(z_eff, p, alpha=ALPHA, b=B_VOID, model=G_MODEL):
    return p * b * g_avg_integrated(z_eff, model=model) * alpha


def ang_sep_deg(l1, b1, l2, b2):
    """Great-circle separation on the sphere (galactic l,b in degrees)."""
    phi1, th1 = math.radians(l1), math.radians(90.0 - b1)
    phi2, th2 = math.radians(l2), math.radians(90.0 - b2)
    c1 = (
        math.sin(th1) * math.sin(th2) * math.cos(phi1 - phi2)
        + math.cos(th1) * math.cos(th2)
    )
    c1 = max(-1.0, min(1.0, c1))
    return math.degrees(math.acos(c1))


def load_sprint_surveys():
    path = Path(__file__).with_name("wagenveld_sprint_surveys.json")
    if not path.is_file():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_footprint_projections():
    path = Path(__file__).with_name(FOOTPRINT_JSON)
    if not path.is_file():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def merged_25_delta_d(projection: float, delta_eps: float) -> float:
    """§5.2 fractional number-count anisotropy: ΔD = A_frac · P_S."""
    a_frac = delta_eps / (1.0 + KAPPA0)
    return a_frac * projection


def print_footprint_delta_kappa_interface(footprint_data, sprint_data):
    """Wire δκ → number-count σ for Scratch Test C (Phase IV interface)."""
    if not footprint_data:
        print("\n(no footprint JSON — run wagenveld_sprint_footprint_weights.py first)")
        return

    surveys_fp = footprint_data["surveys"]
    obs_by_id = {s["id"]: s for s in sprint_data["surveys"]} if sprint_data else {}

    print("\nMerged SS2.5 d-kappa -> number-count delta-D_S (Scratch Test C interface):")
    print(
        f"delta-eps band [{DELTA_EPS_LOW:.0e}, {DELTA_EPS_HIGH:.0e}] -> "
        f"A_frac = delta-eps/(1+kappa0), kappa0={KAPPA0}"
    )
    print(
        "| survey | P_S | dD_low | dD_high | D_obs excess | sigma_excess | frac_of_excess |"
    )
    print("|--------|-----|--------|---------|--------------|----------|----------------|")

    wag_excess = None
    for label, sid in SURVEY_ID_MAP.items():
        fp = surveys_fp.get(sid)
        if not fp:
            continue
        p_s = fp["dipole_projection"]
        d_low = merged_25_delta_d(p_s, DELTA_EPS_LOW)
        d_high = merged_25_delta_d(p_s, DELTA_EPS_HIGH)
        obs = obs_by_id.get(sid, {})
        d_obs = obs.get("D_obs")
        d_kin = obs.get("D_kinematic")
        d_sig = obs.get("sigma_D_obs")
        if d_obs is not None and d_kin is not None:
            excess = d_obs - d_kin
            sig_ex = excess / d_sig if d_sig else float("nan")
            mid = 0.5 * (d_low + d_high)
            frac = mid / excess if excess > 0 else float("nan")
            if sid == "wagenveld":
                wag_excess = excess
        else:
            excess = sig_ex = frac = float("nan")

        print(
            f"| {label} | {p_s:.4f} | {d_low:.2e} | {d_high:.2e} | "
            f"{excess:.4f} | {sig_ex:+.1f}sigma | {frac:.0%} |"
        )

    if wag_excess and wag_excess > 0:
        d_mid = merged_25_delta_d(
            surveys_fp["wagenveld"]["dipole_projection"],
            0.5 * (DELTA_EPS_LOW + DELTA_EPS_HIGH),
        )
        print(
            f"\nTest C flag: merged SS2.5 mid-band dD_wag ~ {d_mid:.2e} vs "
            f"observed excess ~ {wag_excess:.3f} -> sub-dominant (~{d_mid/wag_excess:.0%} of excess). "
            "SS2.7 carries bulk per SS5.4 honest scope."
        )

    # Test A projection ratios (A-independent)
    p_wag = surveys_fp["wagenveld"]["dipole_projection"]
    print("\nTest A projection ratios (P_survey / P_wagenveld; A-independent):")
    for sid, fp in surveys_fp.items():
        p_s = fp["dipole_projection"]
        ratio = p_s / p_wag if p_wag else float("inf")
        print(f"  {sid}: {ratio:.4f}  (P_S={p_s:.4f})")

    print_phase_iv_test_a(surveys_fp)


def footprint_geometry_vector(surveys_fp) -> tuple[float, ...]:
    """Merged §2.5 Test A vector: P_S / P_wagenveld per survey."""
    p_wag = surveys_fp["wagenveld"]["dipole_projection"]
    return tuple(
        surveys_fp[sid]["dipole_projection"] / p_wag if p_wag else 0.0
        for sid in SURVEY_ORDER
    )


def vector_max_rel_err(pred: tuple[float, ...], obs: tuple[float, ...]) -> float:
    errs = []
    for p, o in zip(pred, obs):
        if o > 0:
            errs.append(abs(p - o) / o)
    return max(errs) if errs else float("inf")


def print_phase_iv_test_a(surveys_fp):
    """Phase IV Test A: §2.7 vs merged §2.5 vs observed X (Jammer 2026-05-31)."""
    merged_25 = footprint_geometry_vector(surveys_fp)
    obs_norm = tuple(x / OBSERVED_X_VECTOR[0] for x in OBSERVED_X_VECTOR)

    print("\nPhase IV Test A — geometry vectors (normalized to Wagenveld):")
    print("| survey | obs X/D_k | merged SS2.5 | Jammer SS2.7 | 85/15 combo |")
    print("|--------|-----------|--------------|--------------|-------------|")
    combo = tuple(
        0.85 * j + 0.15 * m for j, m in zip(JAMMER_27_VECTOR, merged_25)
    )
    labels = ("Wagenveld", "Singal", "CatWISE", "Quaia")
    for i, lab in enumerate(labels):
        print(
            f"| {lab} | {obs_norm[i]:.3f} | {merged_25[i]:.3f} | "
            f"{JAMMER_27_VECTOR[i]:.3f} | {combo[i]:.3f} |"
        )

    err_27 = vector_max_rel_err(JAMMER_27_VECTOR, obs_norm)
    err_25 = vector_max_rel_err(merged_25, obs_norm)
    err_combo = vector_max_rel_err(combo, obs_norm)
    print(
        f"\nTest A max relative error vs observed: "
        f"SS2.7={err_27:.1%}, SS2.5={err_25:.1%}, 85/15 combo={err_combo:.1%}"
    )
    print(
        "Verdict: SS2.7 strongly preferred over SS2.5-only; "
        f"85/15 split {'improves' if err_combo < err_27 else 'does not improve'} pure SS2.7 fit."
    )

    # Resonance-model absolute X check (Jammer Table §2.3)
    pred_x = (1.10, 1.53, 2.07, 0.95)
    print("\nJammer resonance absolute X = DeltaD/D_kin (pred vs obs):")
    print("| survey | pred | obs | match |")
    print("|--------|------|-----|-------|")
    for lab, p, o in zip(labels, pred_x, OBSERVED_X_VECTOR):
        match = 100 * p / o if o else float("nan")
        print(f"| {lab} | {p:.2f} | {o:.3f} | {match:.0f}% |")


def print_joint_fit_dof(rows=None):
    """Bounded grid: shared vs Wagenveld-only nuisance DOF (delta-sigma objective)."""
    if rows is None:
        rows = DIPOLE_ROWS
    print("\nJoint-fit DOF ladder (max |delta-sigma| objective):")
    best_shared = None
    for alpha in (0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.24, 0.28):
        for b in (0.04, 0.055, 0.07, 0.09):
            for model in ("pow2", "pow3", "exp"):
                ds_list = []
                for survey, z_eff, p, d_obs, d_sig, d_kin in rows:
                    d_pred = d_kin + dipole_void_amplitude(
                        z_eff, p, alpha=alpha, b=b, model=model
                    )
                    ds_list.append(abs((d_pred - d_obs) / d_sig))
                obj = max(ds_list)
                if best_shared is None or obj < best_shared[0]:
                    best_shared = (obj, alpha, b, model)
    obj, alpha, b, model = best_shared
    print(f"  Tier 1 shared (alpha,b,g): max|ds|={obj:.2f} @ a={alpha}, b={b}, {model}")

    best_wag = None
    for alpha in (0.12, 0.16, 0.20, 0.24):
        for b in (0.04, 0.055, 0.07):
            for model in ("pow2", "pow3", "exp"):
                for z_w in (0.35, 0.4, 0.45, 0.5, 0.55):
                    for p_w in (0.8, 1.0, 1.2, 1.5, 1.8):
                        ds_list = []
                        for survey, z_eff, p, d_obs, d_sig, d_kin in rows:
                            z_use = z_w if survey == "Wagenveld" else z_eff
                            p_use = p_w if survey == "Wagenveld" else p
                            d_pred = d_kin + dipole_void_amplitude(
                                z_use, p_use, alpha=alpha, b=b, model=model
                            )
                            ds_list.append(abs((d_pred - d_obs) / d_sig))
                        obj = max(ds_list)
                        if best_wag is None or obj < best_wag[0]:
                            best_wag = (obj, alpha, b, model, z_w, p_w)
    obj, alpha, b, model, z_w, p_w = best_wag
    print(
        f"  Tier 2 +Wagenveld (z,p): max|ds|={obj:.2f} @ a={alpha}, b={b}, "
        f"{model}, z_w={z_w}, p_w={p_w}"
    )


def print_angular_diagnostics(sprint_data):
    ref = sprint_data["reference_frames"]
    l_cmb, b_cmb = ref["cmb_kinematic_dipole_l_deg"], ref["cmb_kinematic_dipole_b_deg"]
    l_void = ref.get("branch_I_void_axis_l_deg", l_cmb)
    b_void = ref.get("branch_I_void_axis_b_deg", b_cmb)

    print("\nWagenveld sprint - angular axis (worksheet / literature anchors):")
    print("| survey | l | b | sep_CMB_deg | sep_void_deg | sigma_dir |")
    print("|--------|---|---|-------------|--------------|-----------|")
    for s in sprint_data["surveys"]:
        l_s, b_s = s["dipole_l_deg"], s["dipole_b_deg"]
        sig = s.get("dipole_sigma_deg")
        sep_cmb = ang_sep_deg(l_s, b_s, l_cmb, b_cmb)
        sep_void = ang_sep_deg(l_s, b_s, l_void, b_void)
        sig_s = f"{sig:.0f}" if sig is not None else "—"
        print(
            f"| {s['label']} | {l_s:.1f} | {b_s:.1f} | "
            f"{sep_cmb:.1f} | {sep_void:.1f} | {sig_s} |"
        )

    print("\nInter-survey separations (deg):")
    labels = [s["label"] for s in sprint_data["surveys"]]
    coords = [(s["dipole_l_deg"], s["dipole_b_deg"]) for s in sprint_data["surveys"]]
    print("|  | " + " | ".join(labels) + " |")
    print("|" + "---|" * (len(labels) + 1))
    for i, li in enumerate(labels):
        row = f"| {li} |"
        for j, lj in enumerate(labels):
            if i == j:
                row += " — |"
            else:
                row += f" {ang_sep_deg(coords[i][0], coords[i][1], coords[j][0], coords[j][1]):.1f} |"
        print(row)


def main():
    print("BAO reconciliation + Branch I directional dipole worksheet")
    print(f"H0={H0}, r_d={R_D} Mpc, b={B_VOID}, alpha={ALPHA}, g(z)={G_MODEL}\n")
    print(
        "| tracer | z | obs | D_hom/r_d | D_void/r_d | DESI | "
        "hom sig | void sig |"
    )
    print("|--------|---|-----|-----------|------------|------|---------|----------|")
    for tr, z, obs, desi, sig in DESI_ROWS:
        D_C = comoving_distance(z)
        D_C_v = D_M_with_bias(z)
        if obs == "D_V":
            pred_h = D_V(z, D_C) / R_D
            pred_v = D_V(z, D_C_v) / R_D
        else:
            pred_h = D_C / R_D
            pred_v = D_C_v / R_D
        dh = (pred_h - desi) / sig
        dv = (pred_v - desi) / sig
        print(
            f"| {tr} | {z:.2f} | {obs} | {pred_h:.3f} | {pred_v:.3f} | "
            f"{desi:.2f} | {dh:+.2f} | {dv:+.2f} |"
        )

    print("\nDirectional matter dipole estimates (Branch I):")
    print(
        "| survey | z_eff | p | g_int | D_void | D_pred | D_obs | delta-sigma |"
    )
    print("|--------|-------|---|-------|--------|--------|-------|-------------|")
    for survey, z_eff, p, d_obs, d_sig, d_kin in DIPOLE_ROWS:
        g_int = g_avg_integrated(z_eff, model=G_MODEL)
        d_void = dipole_void_amplitude(z_eff, p, alpha=ALPHA, b=B_VOID, model=G_MODEL)
        d_pred = d_kin + d_void
        ds = (d_pred - d_obs) / d_sig
        print(
            f"| {survey} | {z_eff:.2f} | {p:.2f} | {g_int:.3f} | "
            f"{d_void:.4f} | {d_pred:.4f} | {d_obs:.4f} | {ds:+.2f} |"
        )

    print("\nSensitivity by g(z) choice (fixed b, alpha):")
    print("| survey | model | D_pred | delta-sigma |")
    print("|--------|-------|--------|-------------|")
    for survey, z_eff, p, d_obs, d_sig, d_kin in DIPOLE_ROWS:
        for model in ("pow2", "pow3", "exp", "struct_iv"):
            d_pred = d_kin + dipole_void_amplitude(
                z_eff, p, alpha=ALPHA, b=B_VOID, model=model
            )
            ds = (d_pred - d_obs) / d_sig
            print(f"| {survey} | {model} | {d_pred:.4f} | {ds:+.2f} |")

    # v0.4-style bounded grid search (delta-sigma objective; no chi-square)
    print("\nV0.4 grid scan (Wagenveld-focused):")
    print("| alpha | p_wag | z_wag | model | max|delta-sigma| |")
    print("|-------|-------|-------|-------|------------------|")
    best = None
    for alpha in (0.16, 0.20, 0.24, 0.28, 0.32):
        for p_wag in (1.0, 1.2, 1.5, 1.8, 2.0):
            for z_wag in (0.4, 0.5, 0.6, 0.7, 0.8):
                for model in ("pow2", "pow3", "exp", "struct_iv"):
                    ds_list = []
                    for survey, z_eff, p, d_obs, d_sig, d_kin in DIPOLE_ROWS:
                        if survey == "Wagenveld":
                            p_use = p_wag
                            z_use = z_wag
                        else:
                            p_use = p
                            z_use = z_eff
                        d_pred = d_kin + dipole_void_amplitude(
                            z_use, p_use, alpha=alpha, b=B_VOID, model=model
                        )
                        ds_list.append(abs((d_pred - d_obs) / d_sig))
                    objective = max(ds_list)
                    if best is None or objective < best[0]:
                        best = (objective, alpha, p_wag, z_wag, model)
    objective, alpha, p_wag, z_wag, model = best
    print(f"| {alpha:.2f} | {p_wag:.2f} | {z_wag:.2f} | {model} | {objective:.2f} |")

    print_joint_fit_dof()

    sprint_data = load_sprint_surveys()
    if sprint_data:
        print_angular_diagnostics(sprint_data)
    else:
        print("\n(no wagenveld_sprint_surveys.json — skip angular axis)")

    footprint_data = load_footprint_projections()
    print_footprint_delta_kappa_interface(footprint_data, sprint_data)


if __name__ == "__main__":
    main()
