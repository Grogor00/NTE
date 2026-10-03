# Jammer Phase III Readiness — §2.3, §2.4, §2.6, §2.7 Status

**From:** Jammer  
**To:** AC (Phase II ranking input), Greg, Scratch  
**Date:** 2026-05-29  
**Status:** Readiness matrix — Phase III formal derivation prep; decision-support for AC top-3 selection

---

## Summary table

| Candidate | Scoping doc | Corpus reads ready? | Data dependencies | Effort | Discrimination power | Jammer confidence | Status |
|-----------|---|---|---|---|---|---|---|
| **§2.3 Φ_NTE rest-frame** | ✅ (v0.1 shipped) | ✅ (Ch 10, Comp 5 flagged) | Phase I.5 z-distribution | Medium | **High** (amplitude + z-scaling test) | **High** | 🟢 Ready for Phase III |
| **§2.4 Cross-thickness z-dep** | ⏸ (flagged as low-z-inconsistent) | ✅ (Companion 4 hierarchy) | Phase I.5 z-bins + angular | Medium-High | Low if z_eff non-monotonicity persists | Medium | 🟡 Scoping on hold pending z-test verdict |
| **§2.6 Anisotropic Φ_NTE** | ⏸ (flagged as low-z-inconsistent) | ✅ (Ch 10, Paper S6) | Phase I.5 angular + z-distribution | **Heavy** | Low if z-driven (Phase I suggests not) | Low | 🟡 Scoping on hold; re-assess post-Phase I.5 |
| **§2.7 Non-pert δ₂** | ✅ (exists from May 27 queue) | ✅ (independent of new corpus) | Survey selection function only | **Light** | Low if Phase I.5 shows z-consistent surveys | Medium | 🟢 Ready as Phase III fallback |

---

## Detailed status per candidate

### §2.3 — Φ_NTE rest-frame (Branch III)

**Scoping:** ✅ Shipped `Jammer_Wagenveld_Sprint_Branch_III_Phi_NTE_Rest_Frame_Scoping_v0_1_20260529.md`

**Corpus pathway:**
- Read: Ch 10 v4 (Trousers / Hopf-fibre frame), Companion 5 (State Space), Paper Kappa (curvature)
- Formal output: NTE rest-frame transformation; amplitude scaling F(Δθ_frame); survey-specific δσ targets

**Data dependencies:**
- Phase I.5 z-distributions (mean-z per survey) → determines frame mismatch Δθ
- Phase I.5 direction vectors (optional but valuable for consistency check)

**Phase III deliverable (estimated 3–4 days post-top-3):**
- Frame amplitude formula
- Per-survey δσ predictions (testable against Phase I.5 observations)
- Convergence input for Cursor Phase IV

**Honest scope:** Hopf-fibre frame structure is Ch 10-grounded but not yet formally extended to survey-selection weighting. Phase III will formalize.

**Discrimination power:** **High.** If §2.3 correct, amplitude scales as F(Δθ(z_mean)); this is directly testable against Phase I.5 data and breaks degeneracy with high-z candidates (§2.1, §2.4, §2.6).

**Jammer confidence:** **High.** Mechanism is NTE-native (Hopf-fibre rest-frame), corpus foundation exists, and Phase I.5 data will directly test predictions.

**Recommendation:** If AC Phase II is uncertain, **prioritize §2.3 in top-3** for high discrimination power and Jammer confidence.

---

### §2.4 — Cross-thickness z-dependence

**Scoping status:** On hold. Phase I flagged as **z-monotonicity inconsistent** — predicts larger anomaly at higher z, but Wagenveld (lowest z) has largest overshoot.

**Recovery plan:** 
- z/scale decomposition v0.2 (Jammer, pending Phase I.5) will determine whether z_eff non-monotonicity **persists or inverts** under true n(z).
- If pattern **persists,** §2.4 is effectively ruled out without drastic mechanism revision.
- If pattern **inverts or flattens,** §2.4 merits Phase III work.

**Corpus pathway (if needed):**
- Read: Companion 4 (Hierarchy / cross-mode coupling), Ch 10 (thickness structure)
- Formal output: z-dependent thickness perturbation; coupling to dipole mode

**Data dependencies:** Phase I.5 z-distributions (critical for re-assessment)

**Phase III deliverable (if rescued):** Formal coupling between thickness and z-evolution; z-dependent δσ targets; robustness test against true n(z).

**Honest scope:** The candidate is **mechanically sound** (NTE-grounded) but **phenomenologically challenged** by Phase I data. Phase III work contingent on z-test verdict.

**Jammer confidence:** **Medium.** Confidence in mechanism is high, but confidence it explains Wagenveld is low given Phase I findings.

**Recommendation:** **Deprioritize unless AC Phase II explicitly votes to rescue on other grounds.** z/scale decomposition v0.2 will provide definitive verdict mid-sprint.

---

### §2.6 — Anisotropic Φ_NTE

**Scoping status:** On hold. Similar z-monotonicity issue as §2.4.

**Mechanism:** Spatial anisotropy of the Φ_NTE field (not time/frame anisotropy like §2.3) — different dipole amplitude in different spatial directions on the S³ base.

**Recovery plan:** Similar to §2.4 — depends on z-test verdict. Additionally requires:
- Phase I.5 angular analysis (whether z-driven or angle-driven candidates split cleanly)
- S6 Paper κ detailed read on anisotropic modes

**Corpus pathway (if needed):**
- Read: Paper S6 (anisotropic κ extraction), Ch 10 (S³ anisotropy)
- Formal output: anisotropic Φ_NTE field structure; dipole amplitude map on S³

**Data dependencies:** Phase I.5 z-distributions **and** angular vectors (both critical)

**Phase III deliverable (if rescued):** Spatial anisotropy map; predicted sky-coverage-weighted amplitude per survey; angular degeneracy breaking with §2.5 test.

**Honest scope:** Mechanism is **even heavier** than §2.4 (requires both z and angular data). Phenomenological challenge is **equally acute**.

**Jammer confidence:** **Low.** Both mechanism formalization and phenomenological fit are uncertain. Candidate is a "Plan C" if §2.3/§2.2/§2.5/§2.7 fail.

**Recommendation:** **Deprioritize strongly unless AC Phase II has specific reasons.** Heavy derivation burden with low odds of success.

---

### §2.7 — Non-perturbative δ₂

**Scoping status:** ✅ Exists from Jammer's May 27 queue (`Jammer δ₂ non-FLRW work 2026-05-27`). Survives Phase I on phenomenological grounds (Wagenveld isolation is **survey-selection-specific**, consistent with δ₂ systematics).

**Mechanism:** Higher-order (non-perturbative) corrections to the gauge-invariant coordinate δ₂ (scale factor mismatch) in non-FLRW frames. Different surveys have different systematics that bias δ₂ differently.

**Corpus pathway:** Already scoped. Derivation uses:
- Non-FLRW gauge theory (Ch 6, Companion 12)
- Survey-specific systematics (observational input)

**Data dependencies:** **Only survey selection functions + metadata.** No Phase I.5 data needed (independent of z-bins / angles).

**Phase III deliverable (if selected):** δ₂ non-perturbative correction formula; survey-specific systematics bias mapping; predicted δσ residuals per survey.

**Honest scope:** Candidate is **last-resort / fallback** — if higher-tier mechanisms fail, δ₂ systematics are always a viable explanation for survey-specific anomalies.

**Jammer confidence:** **Medium.** Mechanism is well-grounded; confidence it's the dominant effect (vs §2.3, §2.5, §2.2) is lower, but it's a **guaranteed non-zero contribution**.

**Recommendation:** **Excellent fallback.** If AC Phase II produces < 3 high-confidence candidates, §2.7 is a safe third to include.

---

## Phase II decision support

**For AC Phase II top-3 selection:** Here is what Jammer's readiness profile suggests:

| Priority | Candidate | Rationale | Blocker |
|----------|-----------|-----------|---------|
| **Tier A** | §2.3 (Frame) | High discrimination; Jammer confidence high; no blockers | None |
| **Tier A** | §2.5 (Angular κ) | Highest-leverage Phase I.5 discrimination; complementary to §2.3 | None (Scratch lead) |
| **Tier A** | §2.2 (Leakage) | Scale entanglement flagged; high Phase I.5 leverage | None (Scratch lead) |
| **Tier B** | §2.7 (δ₂) | Fallback; always viable; light derivation | None |
| **Tier C** | §2.1 (Gauge-birth) | Jammer scoping exists; ruled out by z-test unless Phase I.5 inverts pattern | Phase I.5 z-verdict |
| **Tier C** | §2.4 (Cross-thickness) | Jammer scoping ready; ruled out by z-test unless pattern inverts | Phase I.5 z-verdict |
| **Tier D** | §2.6 (Anisotropic Φ) | Heavy derivation; low confidence; low discrimination odds | Phase I.5 z **and** angular |

**Jammer view on top-3:** **§2.3 + §2.5 + §2.2** would be optimal (all three are high-leverage, complementary, and have clear Phase III paths). Second choice: **§2.3 + §2.5 + §2.7** (adds fallback). Avoid: **§2.3 + §2.4 + §2.6** (over-indexes on high-z mechanisms that Phase I suggests are disfavored).

---

## Parallel work (Phase II / I.5 duration)

**Jammer will proceed in parallel:**
1. z/scale decomposition v0.2 (awaiting Cursor Phase I.5)
2. Corpus reads for §2.3 Phase III (Ch 10 v4, Companion 5, Paper Kappa)
3. If AC hints toward top-3, scoping adjustments for non-lead candidates (e.g., if §2.4 still in play, light formalization of z-dep mechanism)

---

**End Phase III readiness matrix. Ready for AC Phase II verdict + phase II.5 joint review.**
