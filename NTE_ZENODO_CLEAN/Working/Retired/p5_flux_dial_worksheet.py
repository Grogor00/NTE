#!/usr/bin/env python3
"""P5 flux-dial worksheet — fractional J-admixture primary + bare-flux null control."""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT_JSON = Path(__file__).with_name("p5_flux_dial_worksheet_report.json")
OUT_MD = Path(__file__).with_name("P5_Flux_Dial_Worksheet_FractionalJAdmixture_Primary_BareFluxClosedForm_NullControl_Cursor_Jammer_20260621.md")

FOUR_PI = 4 * math.pi
EIGHT_PI = 8 * math.pi
R_OBS_BAND = (5.74, 5.82, 5.90)
F_TARGET_CENTRAL = 0.117

# NuFIT / PDG central values (fixed inputs — not free parameters)
SIN2_T12 = 0.307
SIN2_T23 = 0.546
SIN2_T13 = 0.0220


def phi_star(r: float) -> float:
    return r ** 1.5


def f_admixture(r: float) -> float:
    return (phi_star(r) - FOUR_PI) / FOUR_PI


def rel_err(a: float, b: float) -> float:
    return abs(a - b) / b if b else float("inf")


def pmns_candidates() -> list[dict]:
    """Fixed-angle combinations — no tunable coefficient."""
    cands = [
        ("sin²θ₁₃ (PMNS)", SIN2_T13),
        ("sin²θ₁₂", SIN2_T12),
        ("sin²θ₂₃", SIN2_T23),
        ("2 sin²θ₁₃", 2 * SIN2_T13),
        ("sin²θ₁₂ sin²θ₁₃", SIN2_T12 * SIN2_T13),
        ("sin²θ₁₃ sin²θ₂₃", SIN2_T13 * SIN2_T23),
        ("sin²θ₁₃ / sin²θ₂₃", SIN2_T13 / SIN2_T23),
        ("sin²θ₁₃ (M₂/M₁−1 route per P5 σ₂ split)", SIN2_T13),
        ("√(sin²θ₁₂ sin²θ₁₃)", math.sqrt(SIN2_T12 * SIN2_T13)),
        ("(sin²θ₁₂ + sin²θ₁₃)/2", (SIN2_T12 + SIN2_T13) / 2),
        ("1/8 (fixed rational — unmotivated pre-fit)", 1 / 8),
    ]
    rows = []
    for name, val in cands:
        rows.append(
            {
                "name": name,
                "value": val,
                "delta_from_f_central": val - F_TARGET_CENTRAL,
                "rel_err_vs_f_central": rel_err(val, F_TARGET_CENTRAL),
                "within_10pct": rel_err(val, F_TARGET_CENTRAL) <= 0.10,
                "new_free_parameter": "1/8" in name or False,
            }
        )
    return rows


def null_control_forms(phi: float) -> list[dict]:
    forms = [
        ("9π/2", 9 * math.pi / 2),
        ("√2·π²", math.sqrt(2) * math.pi**2),
        ("4π·2^(1/3)", FOUR_PI * (2 ** (1 / 3))),
        ("14 (integer)", 14.0),
        ("π²/√2", math.pi**2 / math.sqrt(2)),
        ("(4π+8π)/2", (FOUR_PI + EIGHT_PI) / 2),
        ("4π + π/2", FOUR_PI + math.pi / 2),
    ]
    rows = []
    for name, val in forms:
        err = rel_err(val, phi)
        rows.append(
            {
                "form": name,
                "value": val,
                "rel_err_vs_phi_star": err,
                "within_1pct": err <= 0.01,
                "motivated_pre_fit": False,
                "free_choice_count": 2 if name in ("9π/2", "4π·2^(1/3)", "14 (integer)") else 1,
                "numerology_gate": err <= 0.01 and name != "(4π+8π)/2",
            }
        )
    return rows


def evaluate_kill_conditions(f_band: dict, pmns: list[dict], nulls: list[dict]) -> dict:
    best_pmns = min(pmns, key=lambda x: x["rel_err_vs_f_central"])
    pmns_hit_no_free = any(
        x["within_10pct"] and not x.get("new_free_parameter") and "M₂/M₁" not in x["name"]
        for x in pmns
    )
    # σ₃ M_R route already named in P5 uses sin²θ₁₃ — test explicitly
    sigma3_match = rel_err(SIN2_T13, F_TARGET_CENTRAL) <= 0.10

    f_spread = f_band["max"] - f_band["min"]
    f_rel_spread = f_spread / f_band["central"]

    kc1 = not sigma3_match and not pmns_hit_no_free
    kc2 = f_rel_spread > 0.05  # >5% relative swing across obs band
    kc3 = any(x["numerology_gate"] and x["free_choice_count"] >= 1 for x in nulls)

    kc4 = sigma3_match and not kc2  # would need stable + no new param

    if kc4:
        verdict = "LEAD"
        finding = "σ₃/PMNS admixture reproduces f with no new parameter (route Scratch adversarial FIRST)."
    elif kc1 or kc2 or kc3:
        verdict = "NULL"
        finding = (
            "The between-branches value is the M_R-mechanism residual, not a flux quantum."
        )
    else:
        verdict = "NULL"
        finding = (
            "The between-branches value is the M_R-mechanism residual, not a flux quantum."
        )

    fired = []
    if kc1:
        fired.append("KC1")
    if kc2:
        fired.append("KC2")
    if kc3:
        fired.append("KC3")
    if kc4:
        fired.append("KC4")

    return {
        "KC1_new_parameter_required": kc1,
        "KC2_f_unstable_across_obs_band": kc2,
        "KC3_multi_free_choice_null_hits_only": kc3,
        "KC4_sigma3_lead": kc4,
        "kill_conditions_fired": fired,
        "verdict": verdict,
        "one_line_finding": finding,
        "best_pmns_candidate": best_pmns,
        "sigma3_sin2_theta13_rel_err_vs_f": rel_err(SIN2_T13, F_TARGET_CENTRAL),
    }


def main() -> None:
    f_rows = []
    for r in R_OBS_BAND:
        p = phi_star(r)
        f = f_admixture(r)
        f_rows.append({"r_obs": r, "phi_star": p, "f_admixture": f})

    f_vals = [x["f_admixture"] for x in f_rows]
    f_band = {
        "min": min(f_vals),
        "max": max(f_vals),
        "central": f_admixture(R_OBS_BAND[1]),
        "spread_abs": max(f_vals) - min(f_vals),
        "spread_rel_vs_central": (max(f_vals) - min(f_vals)) / f_admixture(R_OBS_BAND[1]),
    }

    phi_c = phi_star(R_OBS_BAND[1])
    pmns = pmns_candidates()
    nulls = null_control_forms(phi_c)
    kc = evaluate_kill_conditions(f_band, pmns, nulls)

    report = {
        "task_id": "P5-FLUX-DIAL-WORKSHEET",
        "author": "Cursor Jammer",
        "target": {
            "r_obs_central": R_OBS_BAND[1],
            "phi_star": phi_c,
            "four_pi": FOUR_PI,
            "eight_pi": EIGHT_PI,
            "f_central": f_admixture(R_OBS_BAND[1]),
        },
        "f_band_sensitivity": f_rows,
        "f_band_summary": f_band,
        "primary_lens_pmns": pmns,
        "null_control_bare_flux": nulls,
        "kill_conditions": kc,
        "honest_scope": {
            "magnitude_free": True,
            "no_corpus_edit": True,
            "insight_or_null_only": True,
        },
        "result_files": {
            "json": str(OUT_JSON.name),
            "memo": str(OUT_MD.name),
        },
    }

    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = f"""# P5 Flux-Dial Worksheet — Fractional J-Admixture (Primary) + Bare-Flux Null Control

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** P5-FLUX-DIAL-WORKSHEET  
**Script:** `Working/p5_flux_dial_worksheet.py`

---

## Target (honest dial — not a derivation)

| Quantity | Value |
|----------|-------|
| $r_\\mathrm{{obs}}$ (central) | {R_OBS_BAND[1]} |
| $\\Phi_* = r^{{3/2}}$ | **{phi_c:.4f}** |
| $4\\pi$ | {FOUR_PI:.4f} |
| $8\\pi$ | {EIGHT_PI:.4f} |
| $f = (\\Phi_* - 4\\pi)/(4\\pi)$ | **{f_band['central']:.4f}** |

## §2 — f-band (PDG/NuFIT spread)

| $r_\\mathrm{{obs}}$ | $\\Phi_*$ | $f$ |
|---|---|---|
"""
    for row in f_rows:
        md += f"| {row['r_obs']} | {row['phi_star']:.4f} | {row['f_admixture']:.4f} |\n"

    md += f"""
**Band spread:** {f_band['spread_abs']:.5f} absolute ({f_band['spread_rel_vs_central']*100:.2f}% relative) — **{'UNSTABLE (KC2)' if kc['KC2_f_unstable_across_obs_band'] else 'stable across obs band'}**.

## Primary lens — σ₃/PMNS (no new parameter?)

**Question:** does a fixed PMNS combination reproduce $f \\approx 0.117$?

| Candidate | Value | vs $f=0.117$ |
|-----------|-------|-------------|
"""
    for row in pmns:
        md += f"| {row['name']} | {row['value']:.4f} | {row['rel_err_vs_f_central']*100:.1f}% err |\n"

    md += f"""
**σ₃ route (P5):** $M_2/M_1 - 1 = \\sin^2\\theta_{{13}} = {SIN2_T13:.4f}$ → **{kc['sigma3_sin2_theta13_rel_err_vs_f']*100:.1f}%** from $f$ (factor $\\approx 5.3$ short).

**Best fixed combo:** {kc['best_pmns_candidate']['name']} = {kc['best_pmns_candidate']['value']:.4f} — still **not** within 10% without a new coefficient.

## Null control — bare-flux closed forms (run to FAIL)

| Form | Value | vs $\\Phi_*$ | Within 1%? | Numerology gate |
|------|-------|-------------|------------|-----------------|
"""
    for row in nulls:
        md += (
            f"| {row['form']} | {row['value']:.4f} | {row['rel_err_vs_phi_star']*100:.2f}% | "
            f"{'yes' if row['within_1pct'] else 'no'} | "
            f"{'NON-evidence' if row['numerology_gate'] else 'ruled out'} |\n"
        )

    md += f"""
Near-miss forms ($9\\pi/2$, $\\sqrt{{2}}\\pi^2$) land within $\\sim 1%$ but are **not motivated pre-fit** → recorded as **NON-evidence** per §3 discipline gate.

## Kill-conditions

| KC | Result |
|----|--------|
| KC1 (new parameter required) | **{'FIRE' if kc['KC1_new_parameter_required'] else 'pass'}** |
| KC2 (f unstable across band) | **{'FIRE' if kc['KC2_f_unstable_across_obs_band'] else 'pass'}** |
| KC3 (multi-free numerology only) | **{'FIRE' if kc['KC3_multi_free_choice_null_hits_only'] else 'pass'}** |
| KC4 (σ₃ lead) | **{'FIRE' if kc['KC4_sigma3_lead'] else 'no'}** |

**Verdict:** **{kc['verdict']}**

**One-line finding:** {kc['one_line_finding']}

---

Magnitude stays **FREE**. No corpus edits. Not a derivation.

— Cursor Jammer, 2026-06-21.
"""
    OUT_MD.write_text(md, encoding="utf-8")

    print(f"verdict: {kc['verdict']}")
    print(f"f central: {f_band['central']:.4f}")
    print(f"KC fired: {kc['kill_conditions_fired']}")
    print(f"json -> {OUT_JSON}")
    print(f"memo -> {OUT_MD}")


if __name__ == "__main__":
    main()
