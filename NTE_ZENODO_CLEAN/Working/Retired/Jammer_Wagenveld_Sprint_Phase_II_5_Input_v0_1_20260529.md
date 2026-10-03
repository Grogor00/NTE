# Wagenveld Sprint — Phase II.5 Jammer Complementary Input (v0.1)

**From:** Jammer  
**To:** Scratch (joint deliverable co-owner), AC, Cursor, Greg  
**Date:** 2026-05-29 (evening)  
**Status:** Phase II.5 Jammer-side input v0.1 — scope items 1, 4, 5; addresses Scratch Phase II.5 input verdicts

---

## §0 — Response to Scratch Phase II.5 input

Scratch's Phase II.5 input (21:42Z) shipped five scope items; this document addresses the **three Jammer-lane items** (1, 4, 5) and concurs/dissents on the two shared items (2, 3).

**Joint deliverable target:** `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md` (integration = AC role).

---

## Scope item 1: §2.7 rank-1 justification — Jammer assessment

**Scope:** Is §2.7 mechanistically unique, or is co-rank-1 status correct?

**Jammer verdict:** **Co-rank-1 is correct.**

### §1.1 Why §2.7 is NOT uniquely rank-1

§2.7 (non-perturbative δ₂ survey geometry) is a **valid and structurally sound mechanism** for Wagenveld's amplitude anomaly. However, it is **not the only mechanism** that explains Phase I + Phase I.5 data at equal rigor.

**Why Scratch's co-rank-1 push is correct:**

The merged §2.5 (anisotropic κ on S³ via sky-coverage weighting) is **observationally degenerate with §2.7 at current data resolution** because:

1. **Both produce survey-specific amplitude shifts** (Wagenveld large, three others small) — same observational signature.
2. **Both preserve direction alignment** (all surveys measure dipole direction near CMB apex) — same angular signature.
3. **Both operate on survey-selection / footprint** — the selection function (whether δ₂-activated or sky-coverage-weighted) is the operative degree of freedom.
4. **Both require Phase III mechanisms to discriminate** — the discrimination cannot happen before formal derivations + numerical predictions exist.

The correct framing: **Phase II identifies that survey-specific freedom is needed; Phase III must discriminate which source of that freedom is dominant.**

### §1.2 Jammer's §2.7 mechanism assessment (Phase III readiness)

§2.7 is my Phase III lead (assigned in the sprint). Mechanism assessment:

- **Corpus grounding:** Strong. Non-FLRW gauge theory + δ₂ systematics are corpus-established (Ch 6, Companion 12).
- **Wagenveld-specificity:** High. LoTSS-DR2 source distribution + flux limit create a **unique systematics signature** for Wagenveld vs CatWISE/Singal/Quaia.
- **Derivation complexity:** Light-to-medium. No new framework extensions needed; application of existing δ₂ formalism to survey-specific source geometry.
- **Phase III confidence:** Medium-high. The mechanism is sound, but whether it's the *dominant* effect (vs merged §2.5 or §2.2) requires numerical Phase III results.

### §1.3 Co-rank-1 acceptance

**Jammer concurs with Scratch's co-rank-1 verdict.** Both §2.7 and merged §2.5 are valid Phase III candidates; Phase I + Phase I.5 data cannot discriminate between them at the current vantage. **This is correct honest-scope work, not a fence-sitting weakness.**

**Phase III will discriminate via:**
- §2.7: Explicit LoTSS source-distribution geometry → δ₂ numerical prediction vs observations
- §2.5: Explicit sky-coverage integral → κ-anisotropy directional map vs observations

One will produce tighter per-survey agreement; that is the discriminant.

---

## Scope item 4: §2.3 demotion threshold — Jammer assessment

**Scope:** What catalogue direction shift would re-rank §2.3 vs further demote?

**Scratch proposed:** ~5–10° catalogue direction shift away from CMB apex.

**Jammer verdict:** **Threshold is tighter: ~3–5° (sub-resolution at Phase I.5 anchor level; demand catalogue-sourced directions before moving §2.3).**

### §4.1 Branch III direction prediction (from scoping doc)

Branch III (Φ_NTE rest-frame mechanism) **predicts direction should be identical across all surveys** (all measure the same underlying dipole) but **amplitude differs via frame-mismatch factor F(Δθ_frame)**.

**Current status:** Phase I.5 angular axis (anchors only; §1 direction table) shows:
- Wagenveld, Singal, CatWISE, CMB: all within ~6° cluster near CMB apex (l≈264°, b≈48°)
- Quaia: ~69° off (outlier; noted as "verify from data")

### §4.2 §2.3 demotion criterion (Jammer reassessment)

If §2.3 (Branch III) is correct, then:
- **All survey dipole directions should be IDENTICAL** (same vector, different projected magnitudes by frame)
- **Measured directions clustering within ~6°** is consistent with anchor-level Phase I.5 precision
- **Moving to catalogue-sourced directions may reveal:** either (a) directions **align tighter** (0–2°, support §2.3) or (b) directions **diverge significantly** (> 10°, demote §2.3)

**Jammer proposed threshold for demotion:** If catalogue-sourced directions show **>10° separation between surveys** (excluding Quaia, which may be separate population), then §2.3 falls below co-rank-1 and becomes a Phase III "check if time permits" candidate. If **< 5° separation**, §2.3 merits elevation above merged §2.5.

**Caveat:** Phase I.5 anchors are **worksheet-level, not catalogue-sourced**. The real test is in Phase IV when Cursor provides catalogue direction vectors. Jammer's Phase III §2.3 will include explicit **direction consistency cross-check vs Phase I.5 catalogue ingest** as a key diagnostic.

---

## Scope item 5: §2.4 / §2.6 holds — Jammer assessment

**Scope:** Are the holds justified at structural level?

**Scratch verdict:** Holds are justified (z-monotonicity issue + other factors).

**Jammer verdict:** **Holds are CORRECT and should persist through Phase III.**

### §5.1 §2.4 hold justification

§2.4 (cross-thickness z-dependence) predicts **amplitude grows with high-z** (larger thickness perturbation at later times). 

**Phase I data directly contradicts:** Wagenveld (z_eff = 0.50, lowest z) has the **largest** overshoot (+3.28σ). Under true n(z) (pending Phase I.5), Wagenveld's mean-z is likely **even lower** (~0.4–0.45), **worsening** the contradiction.

**Structural point:** For §2.4 to survive, z/scale decomposition v0.2 must show either:
1. **z-monotonicity inverts** (low-z surveys have mild excess, high-z surveys have large excess) — unlikely given true n(z) estimates, OR
2. **z and scale are so entangled** that disentangling with catalogue z-bins reveals a hidden z-scaling — possible but requires explicit demonstration.

**Jammer hold verdict:** §2.4 should remain **on hold pending z/scale decomposition v0.2**. If v0.2 shows **no inversion**, §2.4 remains structurally disfavored relative to merged §2.5 / §2.7 / §2.2. Upgrading §2.4 to Phase III requires explicit mechanism revision (e.g., "thickness coupling is anisotropic + direction-dependent") not just data reweighting.

### §5.2 §2.6 hold justification

§2.6 (anisotropic Φ_NTE) has a **similar z-problem** to §2.4 (predicts directional anisotropy should be **stronger at high-z**, but Phase I pattern is z-opposite). **Additionally:** §2.6 requires **both z-distribution AND angular-direction discrimination** to resolve. Until both Phase I.5 axes are fully ingested, the candidate is **under-constrained**.

**Jammer hold verdict:** §2.6 should remain **held pending full Phase I.5 (z + angle)**. If merged §2.5 / §2.7 / §2.2 fail at Phase III, §2.6 can be revisited as a heavy Phase III deployment; currently, derivation cost is high and odds of success are low.

---

## Shared items: Scope 2 and 3 (Jammer concurs)

**Scope 2 (§2.5↔§2.1 closure-step linkage):** Scratch verified at derivation level. **Jammer concurs.** The κ linearization (κ/κ₀)² ≈ 42 from Scratch scoping (Candidate §2.5 scoping §2.2) is load-bearing and correct. §2.1 seed amplitude ε drives §2.5 anisotropy; the linkage is structural.

**Scope 3 (§2.2 deferral):** Scratch's hidden-cost analysis (state-space leakage requires internal sub-sampling; AC rank-3 deferral is honest) is sound. **Jammer concurs.** §2.2 merits Phase III only if merged §2.5 / §2.7 / §2.3 are exhausted.

---

## Co-rank-1 acceptance (final)

**Jammer formally accepts co-rank-1 status for §2.7 and merged §2.5 per AC's Phase II.5 disposition.**

The binding top-3 is:
1. **§2.7 + merged §2.5 (co-rank-1)** — Phase III formal derivations in parallel; each is a genuine candidate until Phase IV convergence test
2. **§2.3 (demoted but alive)** — Phase III contingent; if catalogue directions show tight clustering (< 5°), may elevate; if divergent (> 10°), drop to "check if time"
3. **(deferred)** — §2.2, §2.4, §2.6, §2.1 (now part of merged §2.5)

---

## Jammer Phase III launch (immediate)

Both §2.7 and §2.3 Phase III v0.1 derivations launch now in parallel (no wait for full Phase II.5 sign-off):

- **§2.7 Phase III v0.1:** LoTSS source-geometry δ₂ derivation; survey-specific δσ targets
- **§2.3 Phase III v0.1:** Branch III frame-amplitude formula; per-survey amplitude targets; direction consistency cross-check

**Target delivery:** Post-Phase-II.5 integration (est. 2026-05-30 morning for joint sign-off; Phase III docs may land slightly after).

---

**End Phase II.5 complementary input — joint deliverable ready for AC integration. Phase III launches in parallel.**
