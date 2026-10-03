# Scratch Adversarial Review — Cursor's Branch I v0.3 Numerical Pass (Scratch v0.1)

**Author:** Scratch (Connes Programme lead)
**Date:** 2026-05-27
**Trigger:** Greg directive 2026-05-27 ("continue with next… choose one yourself if you have some"). Cursor v0.3 pass landed at 13:14Z; review provides Scratch perspective on top of Jammer's designated structural review.
**Scope:** Adversarial review of `Working/Cursor_LCDM_Void_Bias_BranchI_v0_3_Pass_20260528.md` from the perspective of `Working/Cosmic_Dipole_Anomaly_Axiom_Filter_Pass_Scratch_v0_1_20260527.md` §5 candidate-reading framework. Complements (does not duplicate) Jammer's structural review per the validated Scratch ↔ Cursor + Jammer ↔ Cursor patterns.
**Status:** v0.1 reviewer findings; routed to Jammer for incorporation into the consolidated v0.3 adjudication; Greg recognition gates flagged separately.

---

## §1 — Scope of this review (what it is and isn't)

**What this review IS**: a check of Cursor v0.3 numerical pass against the filter-pass-level structural commitments documented in Scratch's cosmic-dipole filter pass. Specifically: does v0.3's output fire the candidate-reading thresholds I committed to in filter pass §5? Are the implicit framings consistent with the filter-pass-level honest-scope discipline (Lesson #34)?

**What this review IS NOT**:
- A duplicate of Jammer's designated structural review (8 r-gates + numerical methodology) per `Handoff_Jammer_to_Cursor_Branch_I_8_RGates_plus_v0_3_Numerical_Pass_Routed_20260527.md`. Jammer covers the math substrate.
- A correctness check on Cursor's Python code. I haven't read `lcdm_bao_void_bias.py` for this review.
- A re-derivation of Cursor's numerical results. I'm taking v0.3's reported numbers at face value and reviewing their interpretation against filter-pass-level structural commitments.

Reviewer-perspective overlap with Jammer's review is intentional where it strengthens the consolidated v0.4 input; reviewer-perspective divergence from Jammer is flagged explicitly.

## §2 — v0.3 reported state (as given)

Cursor's v0.3 reports:

| Survey | Directional δ-σ | Status |
|--------|-----------------|--------|
| CatWISE | **−0.13σ** | Within 1σ; effectively consistent |
| Wagenveld | **+3.28σ** | Overshoot persists across g(z) models |
| Singal | **+0.63σ** | Within 1σ |
| Quaia | **+0.52σ** | Within 1σ |

Sensitivity (Wagenveld only): pow2 +3.28σ, pow3 +2.40σ, exp +4.23σ. Minimum is **+2.40σ** (pow3), still **outside 2σ envelope**.

Defaults used in-script: b = 0.055, α = 0.24, g(z) = (1+z)^-2 (pow2). **Worksheet-level placeholders; not parameter-optimised.**

## §3 — Adversarial review against cosmic dipole filter pass §5

### §3.1 Branch I closure criterion check

Cosmic dipole filter pass §5 candidate Branch I closure criterion (per §5.1, ratified): "*If Branch I yields a quantitative directional prediction matching CatWISE/Wagenveld/Singal data within 2σ envelopes after parameter optimisation, the cosmic dipole anomaly is promoted from* §17.5.12 *watch-list to Charter-14 prediction surface.*"

v0.3 status against this criterion:

- **Three of four surveys** (CatWISE, Singal, Quaia) within 1σ → would satisfy the criterion individually
- **One survey (Wagenveld)** outside 2σ (minimum 2.40σ across g(z) variants)
- **Critical caveat**: v0.3 is NOT parameter-optimised. Defaults are worksheet placeholders, not joint-fit best-fit values.

**Adversarial verdict on closure assessment**: v0.3 does NOT meet the closure criterion as-is, but the criterion explicitly required *after parameter optimisation*. v0.3 is pre-optimisation. The Wagenveld 3.28σ residual is a **partial-trigger signal** but does not yet fire the spawn condition for downgrade to "candidate falsifier of void-axis hypothesis" per filter pass §5.

### §3.2 Branch II spawn-trigger check

Cosmic dipole filter pass §8 item 5 Branch II spawn trigger: "*If Branch I (Jammer's directional void-bias extension) closes with a quantitative misalignment between predicted and observed dipole direction beyond 2σ, the residual unexplained dipole becomes Branch II/III territory and Scratch picks up the Hopf-fibration global-rigidity work then.*"

Key phrase: "**direction** misalignment beyond 2σ" — not magnitude misalignment.

v0.3 reports **magnitude** δ-σ values (CatWISE −0.13, Wagenveld +3.28, etc.). These are *not* directly the direction-misalignment-angle metric the Branch II trigger keys on. Cursor's v0.3 §3.4 explicitly notes: "*No direction-angle fit against explicit local-void axis catalogues*" is among the open scope items.

**Adversarial verdict on Branch II trigger**: trigger is **NOT met** — neither magnitude nor direction has been adjudicated against the 2σ criterion at parameter-optimised level, and direction-alignment angle has not even been computed in v0.3. Branch II stays HELD. Trigger condition refines to: "Branch I v0.4 closes with direction-alignment angle >2σ misalignment with KBC void axis (or equivalent local-void direction catalogue) at parameter-optimised best fit AND magnitude δ-σ >2σ across multiple surveys."

This sharper trigger formulation is **a substantive Scratch contribution** to Branch II spawn gating that the filter pass v0.1 left underspecified. Recommend including in v0.4 closure adjudication.

### §3.3 Wagenveld residual structural reading

The Wagenveld 3.28σ overshoot is robust to g(z) form variation (min 2.40σ pow3, max 4.23σ exp). This robustness is **structurally significant** — it suggests the issue is NOT g(z) model selection.

Three candidate readings (Jammer's gate 4 already flags these; my framing differs slightly):

**(A) Parameter degeneracy / b-α joint optimisation will absorb it.** v0.3 used b=0.055, α=0.24. The joint (b, α, g) optimisation in v0.4 may find a configuration that respects Wagenveld within 2σ while keeping the other three surveys within 2σ. Plausible; needs v0.4 to settle.

**(B) Wagenveld systematic.** Wagenveld 2024/2025 NVSS+RACS-low radio surveys may have a calibration or sky-coverage issue that the literature hasn't fully characterised. Citing literature systematic doesn't earn the "Branch I closes" claim, but it does soften the residual interpretation.

**(C) Structural residual.** The Wagenveld measurement is correctly characterising a *real component* of the matter dipole that local-void-axis (Branch I) alone cannot account for. If (C) holds even after v0.4 optimisation, Branch II / Branch III becomes empirically motivated, not merely held.

**Adversarial verdict on reading priority**: (A) is the parsimonious null; v0.4 should test it explicitly. (B) is unverifiable without going to primary survey systematics. (C) requires v0.4 to fail (A) before being seriously entertained. **v0.4's primary job is to discriminate (A) from (C); (B) sits outside what NTE can adjudicate.**

This is a **sharper framing than Cursor's v0.3** §3 *Sensitivity (fixed b/alpha)* paragraph offers. Cursor reports g(z) sensitivity as if g(z) is the parameter degree of freedom that matters; the actual operative degeneracy is (b, α) joint variation, which v0.3 did NOT explore.

### §3.4 Cross-survey D(z) decline check

Cosmic dipole filter pass §5 noted Branch I should predict a *redshift-decline* of D(z) — high at low z (CatWISE), declining at higher z (Quaia z~1).

v0.3 reported survey-by-survey δ-σ but did not extract D(z) slope. From v0.3 numbers:
- CatWISE (z_eff ~ 0.3): −0.13σ (prediction matches data closely)
- Singal (z_eff ~ 0.5): +0.63σ (prediction slightly high)
- Quaia (z_eff ~ 1.2): +0.52σ (prediction slightly high)
- Wagenveld (radio, z_eff ~ 1.0): +3.28σ (prediction much too high)

Reading: the *direction-consistent decline* is partially supported (CatWISE prediction is good; higher-z surveys have positive residuals suggesting prediction over-shoots at higher z). But Wagenveld (similar effective z to Quaia) being 6× more discrepant than Quaia is a *structural anomaly* — it suggests either Wagenveld is genuinely different (radio vs. infrared/optical), or the model is missing structure.

**Adversarial flag**: v0.4 should include a **separate radio-vs-photometric channel analysis**. If radio surveys (Wagenveld, Singal) jointly overshoot while photometric surveys (CatWISE infrared, Quaia photometric QSOs) match, this is a *systematic radio-vs-photometric residual* that is structurally important.

Singal δ-σ is small (+0.63σ); Wagenveld is huge (+3.28σ). Both are radio surveys. So it's not "radio surveys overshoot uniformly" — it's "Wagenveld specifically overshoots." This further isolates the issue to Wagenveld's specific methodology (NVSS+RACS-low joint analysis vs. Singal's different radio combination).

**Recommendation for v0.4**: include explicit Wagenveld-specific systematic discussion, perhaps cross-checking against the Wagenveld paper's own internal consistency tests.

### §3.5 Lesson #34 vocabulary-inheritance check

Cosmic dipole filter pass §6 explicit honest-scope discipline: "*Branch I makes the alignment claim but the direction value is empirical*" — direction comes from KBC void survey, not from NTE derivation. Branch I is structurally about "the matter dipole aligns with the local-void axis," not "NTE predicts the direction value."

v0.3 §3 *Defaults used in-script* uses α=0.24 — but Jammer's gate 6 (per `Handoff_Jammer_to_Cursor_Branch_I_8_RGates_plus_v0_3_Numerical_Pass_Routed_20260527.md` §2 gate 6) explicitly flags: "Is this the right honest framing, or should NTE be making a theoretical prediction of $\hat{n}_{void}$ from first principles?"

**Adversarial verdict on vocabulary**: v0.3 framing is *consistent* with honest scope — it treats α as a fittable parameter, not as a derived NTE prediction. No Lesson #34 violation. But the v0.3 narrative doesn't *explicitly* re-state the "direction is empirical, alignment is the structural prediction" framing. **Recommend v0.4 narrative include explicit re-statement of this honest-scope framing** so the empirical-vs-derived split is preserved in the consolidated deliverable.

## §4 — Where Scratch review aligns with Jammer's expected review

Per `Handoff_Jammer_to_Cursor_Branch_I_8_RGates_plus_v0_3_Numerical_Pass_Routed_20260527.md` §5, Jammer's expected review focuses on:

- Whether joint optimisation finds a genuine minimum or a degenerate fit
- D(z) decline significance against actual covariance structure
- Direction-alignment angle cross-check against independent KBC void axis estimates
- r-gate adjudication independence

Scratch review aligns with Jammer on all of these but adds the filter-pass-level perspective:

- **§3.1 closure criterion** — Scratch contributes the explicit ratified-criterion check
- **§3.2 Branch II trigger** — Scratch contributes the sharpened trigger formulation (direction-misalignment > 2σ + magnitude > 2σ jointly, post-optimisation)
- **§3.3 reading priority** — Scratch contributes the (A)/(B)/(C) reading framework with v0.4 discrimination criterion
- **§3.4 cross-survey channel** — Scratch contributes the radio-vs-photometric flag
- **§3.5 vocabulary check** — Scratch contributes the Lesson #34 honest-scope verification

## §5 — Where Scratch review may diverge from Jammer's

One potential divergence flag:

- v0.3's §3 *Sensitivity (fixed b/alpha)* table treats g(z) model as the operative degree of freedom. If Jammer reads this as appropriate (g(z) is genuinely model-uncertain), Jammer would not flag it as a methodology issue. Scratch flags it (§3.3 above) as a *narrative* issue — the genuine operative degeneracy is (b, α) joint variation, and v0.3's framing under-emphasises this. If Jammer concurs, this is a v0.4 narrative-tightening item.

Recommend Jammer cross-read this point. No technical correction; framing tightening only.

## §6 — Recommendations for Cursor v0.4

Consolidated from §3 + §4 above:

1. **Parameter optimisation as primary v0.4 task** — joint (b, α, g-form) optimisation against all four surveys + DESI BAO. This is the operative test for Branch I closure per the ratified §5 criterion.
2. **Direction-alignment angle computation** — currently noted as "open scope" in v0.3 §3. v0.4 should fold this in; it's load-bearing for Branch II spawn trigger assessment.
3. **Wagenveld-specific systematic analysis** — radio-vs-photometric channel separation if (A) optimisation does NOT resolve Wagenveld. If Wagenveld remains the only outlier at 2σ+ after optimisation, Wagenveld systematic adjudication is required before reading the residual as Branch II evidence.
4. **Narrative tightening** on honest scope — explicit re-statement that direction comes from KBC, alignment is the structural NTE prediction. Lesson #34 maintenance.
5. **Reading-priority discrimination** — v0.4 should structurally test (A) vs (C) (parameter-degeneracy null vs structural residual) and explicitly call which is supported by the data + optimisation.

## §7 — Cross-stream signals

### §7.1 To Jammer (R&D)

This review is **input to Jammer's consolidated v0.3 adjudication**. Jammer remains the designated adversarial reviewer; Scratch contributes filter-pass-level perspective without claiming primary review role. Specifically: recommend Jammer incorporate §3.1 (closure criterion), §3.2 (Branch II trigger sharpening), §3.3 (reading priority) into the v0.3 adjudication output. §3.4 (radio-vs-photometric) and §3.5 (Lesson #34 maintenance) are framing additions Jammer may or may not accept.

### §7.2 To Cursor (render lane)

v0.4 recommendations consolidated in §6. Pickup at Cursor's convenience after Jammer's v0.3 adjudication ratifies (or refines) Scratch's filter-pass-level framings.

### §7.3 To AC (corpus integration)

§17.5.12 cosmic-dipole watch-list row (Greg-ratified add-now this morning) remains correct as-is. Branch I status is still "watch-list" pending v0.4 outcome. No corpus integration action triggered by this review.

### §7.4 To Greg (recognition gates)

Two recognition gates flagged:

1. **Branch II trigger sharpening** (§3.2) — ratify Scratch's refined trigger formulation: "Branch I v0.4 closes with direction-alignment angle > 2σ misalignment AND magnitude δ-σ > 2σ across multiple surveys at parameter-optimised best fit"?
2. **Reading-priority discrimination criterion** (§3.3) — ratify Scratch's framing that v0.4's *primary job* is to discriminate reading (A) from reading (C), with (B) sitting outside NTE adjudication?

Scratch recommendation: ratify both as part of v0.3 → v0.4 transition discipline.

## §8 — File ops

- This review: `Working/Scratch_Adversarial_Review_Cursor_BranchI_v0_3_Pass_20260527.md`
- Direct create with parentId expected; no root duplicate.

## §9 — Files referenced

- `Working/Cursor_LCDM_Void_Bias_BranchI_v0_3_Pass_20260528.md` (reviewed)
- `Working/Cosmic_Dipole_Anomaly_Axiom_Filter_Pass_Scratch_v0_1_20260527.md` (filter pass framework)
- `Working/LCDM_Void_Bias_BAO_Worksheet_Branch_I_Directional_Jammer_v0_2_20260527.md` (v0.2 substrate; Jammer's analytical setup)
- `Handoffs/Handoff_Jammer_to_Cursor_Branch_I_8_RGates_plus_v0_3_Numerical_Pass_Routed_20260527.md` (Jammer routing handoff)
- `Handoffs/Handoff_Greg_Ratification_Cosmic_Dipole_Filter_Pass_v0_1_20260527.md` (ratification anchor)

---

— Scratch (Connes Programme lead), 2026-05-27. Adversarial review v0.1 of Cursor's Branch I v0.3; complements Jammer's structural review; sharpens Branch II spawn trigger formulation; recommends v0.4 directives for Cursor.
