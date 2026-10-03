# Scratch Phase II.5 Input — Wagenveld Sprint Joint Adversarial Review

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-29 (afternoon)
**Status:** v0.1 — Scratch-side input to joint Phase II.5 deliverable. Awaiting Jammer complementary input; integration into `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md` follows.
**Authority:** AC Phase II top-3 ranking `Handoffs/Handoff_AC_to_Cursor_Jammer_Scratch_Wagenveld_Sprint_Phase_II_Top3_Ranking_20260529.md` (Drive ID `1BtoOFURNl0g7n805G4a_jGLcGygwJfUL`) §4 — Phase II.5 scope of 5 review items, Scratch + Jammer joint owners, Phase III mechanism work blocked until lands. Cursor Coordination Register v0.2 ping confirms joint review is the immediate priority.
**Reviewed:** AC top-3 ranking (load-bearing); Cursor §8 correction supplement; Cursor joint-fit DOF accounting; Cursor Coordination Register v0.2; Jammer afternoon Session State Summary; Jammer z/scale decomposition v0.1.

---

## §0 — Process clarification (surface for Greg + Jammer)

**There is an interpretation mismatch on "Phase II.5 implicit" between Jammer and AC.**

- **AC's reading** (top-3 ranking §4): "Phase II.5 adversarial review (scheduled). Owners: Scratch + Jammer (joint). Phase III mechanism work blocked until Phase II.5 ships."
- **Greg activation handoff** (verbatim): "Phase II.5 — Implicit — no explicit gate; Jammer + Scratch phase II.5 flows to Phase III top-3 automatically."
- **Cursor Coordination Register v0.2** (correctly aligned with AC): "II.5 ... 🔄 Post-AC-lock (Greg: implicit, not blocking) — Joint review ~½ session after AC top-3. **Phase III paused until II.5 lands.**"
- **Jammer Session State Summary** (21:33Z, misaligned): "Phase II.5 implicit: No explicit gate; Scratch §2.5 + AC top-3 flows directly to Jammer Phase III without formal review ceremony (per Greg decision)."

The natural reading of Greg's "implicit ... flows automatically" is: **the review happens, just doesn't require an explicit Greg-gate to ratify before Phase III proceeds**. AC + Cursor read it this way. Jammer's "no formal review ceremony" reading appears to be a misinterpretation.

**Scratch reads with AC + Cursor**: Phase II.5 is a binding joint review that produces the final top-3 ranking before Phase III mechanism work commits. The "implicit" qualifier refers to the absence of a Greg-gate, not the absence of the review itself.

**Recommendation for Greg:** confirm the AC + Cursor reading is correct (one-line clarification), so Jammer's Phase III work doesn't proceed prematurely.

If Greg confirms otherwise (Jammer's reading is correct → no Phase II.5 review needed), this document becomes a standalone Scratch addendum to AC's top-3 ranking rather than the Scratch-side input to a joint review.

---

## §1 — Verdict summary

| AC scope item | Scratch verdict | Required change |
|---|---|---|
| 1. §2.7 rank-1 justification | **REJECT** "uniquely §2.7"; both §2.7 and §2.5-merged predict observed pattern qualitatively | **Co-rank-1** recommended for §2.7 and §2.5-merged |
| 2. §2.5 ↔ §2.1 closure-step linkage | **CONFIRM** at derivation level (Paper_Kappa_AB §3.4 + §5) | No change — AC has correctly absorbed the merger |
| 3. §2.2 deferral | **ACCEPT** — no significant hidden cost | No change |
| 4. §2.3 demotion threshold | Threshold ~5–10° direction shift under catalogue ingest | No change — confirm "alive but watching" status |
| 5. §2.4 / §2.6 hold criteria | **CONFIRM** holds justified per closure-step structural logic | No change |

**Recommended binding top-3** post Phase II.5:

| Rank | Candidate | Lead | Discriminator |
|------|-----------|------|---------------|
| **Co-1** | §2.5+§2.1 merged | Scratch | Phase III §5.1 (seed amplitude) + §5.3 (Hopf-fibre direction) + §5.4 (sky-coverage integrals) |
| **Co-1** | §2.7 non-perturbative δ₂ | Jammer | Phase III §2.7 (does LoTSS-DR2 source-distribution geometry uniquely activate, or do other survey geometries also activate?) |
| 2 | §2.3 Φ_NTE frame mismatch | Jammer | "Alive but watching" — re-rank threshold ~5–10° catalogue direction shift |

**§2.2 deferred** until post-sprint. **§2.4 / §2.6 held** pending Phase I.5 n(z) ingest re-validation.

---

## §2 — Scope item 1: §2.7 rank-1 justification (push back)

### §2.1 AC's argument

AC argues §2.7 uniquely fits the data because:
- Wagenveld is amplitude-anomalous (+3.28σ), direction-normal (within own σ_dir of CMB)
- Singal (also radio) points the same direction as Wagenveld but at +0.63σ
- Joint shared-parameter fit can't absorb Wagenveld without survey-specific freedom (best case +1.12σ)
- Pattern persists across all viable g(z) forms
- Phase I §10: "Wagenveld can be folded into a sub-1σ joint envelope only with survey-specific (p, z_eff) freedom"

AC's conclusion: "uniquely points to §2.7" — a Wagenveld-survey-specific mechanism (LoTSS-DR2 source-distribution geometry activating non-perturbative δ₂).

### §2.2 Scratch counter-argument: merged §2.5 produces the same signature via sky-coverage weighting

The merged §2.1+§2.5 candidate (per Scratch Candidate §2.5 scoping §4) predicts:

| Survey | Sky coverage | Predicted dipole magnitude |
|---|---|---|
| Wagenveld (LoTSS-DR2) | Northern hemisphere strip, ~14% sphere | **Large** — preferentially samples preferred-direction hemisphere if n̂_pref near CMB (Galactic Northern, l=264°, b=48°) |
| Singal (multi-radio) | Both hemispheres, ~uniform | **Small** — full-sky averaging on directional signal |
| CatWISE (IR/WISE) | All-sky with |b|>30°, ~50% sphere | **Small** — full-sky averaging |
| Quaia (QSO photometric) | ~40% sphere, ~uniform | **Small** — full-sky averaging |

All four surveys' MEASURED directions remain near n̂_pref (because the asymmetry IS in that direction regardless of amplitude — it's the integrated projection that varies by survey, not the direction).

**This qualitatively matches Phase I + I.5 data exactly:**

- Wagenveld amplitude excess ✓ (sky-coverage weighted toward preferred-direction hemisphere)
- Three others at anchor ✓ (sky-coverage averages out)
- Wagenveld direction near CMB ✓ (the asymmetry's direction IS the preferred direction)
- Singal direction near CMB ✓ (same — direction reflects the asymmetry, not the amplitude)
- Persists across g(z) forms ✓ (the closure-step δκ doesn't have z-dependence — see Candidate §2.5 scoping §3.4)
- Joint fit can't absorb without survey-specific freedom ✓ (sky-coverage weighting IS survey-specific by mechanism)

### §2.3 Both mechanisms predict the same Phase I + I.5 signature

AC's "uniquely points to §2.7" claim is **factually incorrect** — the merged §2.5 candidate predicts the same observational signature via a fundamentally different mechanism (structural directional asymmetry × sky-coverage projection vs Wagenveld-specific source-distribution activation of a calculational correction term).

What Phase I + I.5 data CANNOT do:
- Distinguish §2.7 from merged §2.5 at qualitative-prediction level (both fit the pattern)

What WOULD discriminate:
- **Catalogue-ingested directions** (Cursor Phase I.5 queue item 3): if CatWISE/Singal/Quaia directions all cluster near a common preferred axis (with sigma-level spread), merged §2.5 favored. If they point in random directions, §2.7 favored.
- **Sky-coverage integral predictions** (Scratch Phase III §5.4): does merged §2.5's quantitative amplitude prediction match observed amplitude across all four surveys? Decisive test.
- **Hopf-fibre direction derivation** (Scratch Phase III §5.3): does corpus structure force the preferred direction to be near CMB? If yes, merged §2.5 strongly favored. If derivation yields free parameter, both candidates retain priors.
- **Cross-survey geometry comparison** (Jammer Phase III §2.7): does LoTSS-DR2's source-distribution geometry uniquely activate non-perturbative δ₂, or do other survey geometries (CatWISE, Quaia) have similar geometric properties? If §2.7's mechanism is unique to Wagenveld, supports §2.7; if other surveys should also activate it, weakens §2.7.

### §2.4 Bayesian-prior considerations

AC's implicit framing: §2.7 has higher prior of resolving Wagenveld specifically (it's tuned to that case); merged §2.5 has lower prior but higher reward (resolves broader cosmic dipole anomaly + structural physics).

**Scratch's assessment of this framing.** AC's framing is defensible but is a methodological choice, not a data-derived ranking. The data don't favor §2.7 over merged §2.5 at current Phase I + I.5 vantage. The "higher prior for §2.7" comes from:
- §2.7's mechanism is calculational (less structural commitment, easier to invoke)
- §2.7 is explicitly Wagenveld-survey-specific by construction
- §2.7 doesn't require additional Phase III derivations to predict observational signature (the prediction IS "Wagenveld-specific anomaly", which the data shows)

Whereas merged §2.5 requires:
- Phase III §5.1: derive seed amplitude ε from bifurcation effective action (load-bearing; could fail)
- Phase III §5.3: derive whether Hopf-fibre direction is CMB-aligned (could yield free parameter, weakening discrimination)
- Phase III §5.4: compute sky-coverage integrals quantitatively (mechanical but volume-dependent)

So §2.7's "higher prior" is genuinely the higher prior of explaining Wagenveld at minimum derivation cost. Merged §2.5's higher reward is the structural physics + broader anomaly resolution if it succeeds.

**Recommended Phase II.5 disposition: co-rank-1 status for both candidates.** Phase III work on both proceeds in parallel; the final ranking is determined by Phase III outcomes (not Phase II.5 ranking). This honors AC's higher-prior argument while rejecting the "uniquely §2.7" claim and preserving merged §2.5 as a top deliverable.

### §2.5 Why co-rank-1 matters (not cosmetic)

The Phase II.5 ranking determines Phase III bandwidth allocation. If §2.7 is rank-1 and merged §2.5 is rank-2:
- Jammer gets Phase III lead bandwidth for §2.7
- Scratch's merged §2.5 Phase III bandwidth is preserved (per Greg §2.5-only) but framed as "secondary deliverable"
- Phase IV convergence test treats §2.7 as primary anchor; merged §2.5 as backup

If both are co-rank-1:
- Both streams get full Phase III bandwidth on their lead deliverables
- Phase IV convergence test treats both as primary anchors with quantitative comparison
- Higher likelihood of a multi-mechanism convergence outcome (per AC honest-scope §7: "Multiple candidates may partially explain the pattern. A coherent §2.7 + §2.5 combination is allowed.")

The co-rank-1 disposition aligns with AC's own §7 honest-scope acknowledgment that the combination is allowed.

---

## §3 — Scope item 2: §2.5 ↔ §2.1 closure-step linkage (confirm)

**Verified at derivation level.** Scratch Candidate §2.5 scoping §2 establishes:

- Bare coupling κ₀ = 3/√(4π) is structurally rotation-invariant by Y₀₀ monopole projection (Paper_Kappa_AB v10.17.2 §3 + Gaunt-coefficient argument §3.3 + topological protection §3.4).
- Closure step κ = κ₀/(1−κ₀) ≈ 5.50 under exact CPN-symmetry constraint admits anisotropic mode under weak CPN-symmetry-breaking driven by upstream bilateral seed.
- Linearised amplification factor (κ/κ₀)² ≈ 42; sub-perturbative seed δε ~ 0.01–0.1 produces observable δκ ~ 0.4–4.

AC's Rank 2 framing ("§2.5 + §2.1 = one mechanism scoping arc, closure step as derivation target") absorbs this correctly.

**No revision needed on this scope item.** Move forward with merged candidate as single Phase III deliverable arc.

---

## §4 — Scope item 3: §2.2 deferral (accept)

AC's reasoning: §2.2 v0.1 at architectural-class scope (per Scratch flag #4) doesn't change Phase IV quantitative convergence test outcome. Greg's §2.5-only activation makes deferral natural.

**Scratch hidden-cost analysis:**

- §2.2 architectural sketch would have established the formal scaffolding for bilateral wavefunction leakage (bilateral spectral triple + KMS modular flow + Boyle-Farnsworth bi-representation per Candidate §2.5 scoping §3.2 / Phase III sketch). Deferring this means the scaffolding isn't built during the sprint window.
- If Phase III finds the merged candidate fails structurally (seed amplitude Planck-suppressed or Hopf-fibre direction free parameter): §2.2 was the runner-up structural-physics candidate; without an architectural sketch, no Phase IV fallback at structural-class.
- **Mitigation:** §2.2 architectural sketch can be revisited post-sprint at minimal additional cost; the deferral doesn't permanently close the door.

**Verdict: defer accepted. No significant hidden cost.** Bandwidth on merged §2.5 and §2.7 is better spent.

If the merged candidate fails Phase III §5.1 specifically (seed amplitude turns out Planck-suppressed), recommend re-engaging §2.2 architectural sketch post-sprint as a Programme S item.

---

## §5 — Scope item 4: §2.3 demotion threshold (define)

AC demoted §2.3 to "alive but watching": Phase I.5 shows Wagenveld lacks the direction offset §2.3 predicts (Wagenveld within 6.9° of CMB at anchor level).

### §5.1 Re-rank to top-3 if

- **Catalogue ingest reveals Wagenveld direction offset > 10°** from CMB (anchor-level σ_dir is 20°, so a true 10° offset would be a 0.5σ signal at anchor level; with catalogue ingest σ_dir likely drops to 5° or below, making this discriminable).
- **OR** Quaia direction (currently poorly anchored) aligns with §2.3's predicted Φ_NTE rest frame direction.
- **OR** CatWISE's direction offset (25.9° from CMB) is shown to have structural origin (not IR-selection artifact); Jammer §2.3 Phase III work could test this.

### §5.2 Further demote if

- Catalogue ingest confirms Wagenveld within 5° of CMB
- AND CatWISE direction offset proves to be IR-selection artifact (Jammer §2.3 scoping could surface this)

### §5.3 Recommended Phase III action

Jammer's §2.3 mechanism scoping (already in flight per AC handoff 09:20Z) continues to v0.1 prediction at "alive but watching" status. The prediction outputs (frame-mismatch magnitude + angular direction + survey-specific dipole magnitudes) provide the discrimination input for the re-rank threshold above.

---

## §6 — Scope item 5: §2.4 / §2.6 hold criteria (confirm justified)

### §6.1 §2.4 (cross-thickness coupling z-dep)

**Could closure-step corrections to S_bridge produce a §2.4-like signature without z-enhancement?** Structurally, no:
- §2.4's nominal mechanism is "cross-thickness coupling grows with z" — a direct z-scaling of the S_bridge coupling.
- Closure-step alternative would be "directional cross-thickness coupling at fixed z" — but that's structurally identical to §2.5's directional δκ (the cross-thickness coupling IS what enters S_bridge in the closure step).
- §2.4 as a distinct mechanism (not redundant with §2.5) requires z-enhancement at the coupling level itself; Phase I refutes this signature.

**Hold justified.** §2.4 remains held pending Phase I.5 n(z) ingest validation. If catalogue n(z) confirms worksheet z_eff ordering, §2.4 stays held permanently.

### §6.2 §2.6 (anisotropic Φ_NTE)

**Could closure-step logic apply?** Less directly than §2.4:
- §2.6's mechanism is "Φ_NTE field has spatial anisotropy" — a directional excess in the boundary-field amplitude.
- The closure-step corrections to κ are NOT what §2.6 predicts; §2.6 predicts directional excess in Φ_NTE itself, which couples to the gravity sector via Branch III (per Jammer §2.3 territory).
- §2.6's signature: directional dipole excess with z-evolution following Φ_NTE's cosmic-evolution profile.

**Hold justified.** Phase I z-monotonicity refutes the z-evolution part of §2.6's signature. Catalogue n(z) ingest validates.

### §6.3 Three-way self-consistency

**§2.1↔§2.5↔§2.6 same preferred direction** (per Scratch scoping review §2.2 expansion). If §2.6 is later revived via catalogue n(z) ingest, its preferred direction should coincide with merged §2.5's. This is a Phase III sub-check that doesn't require standalone §2.6 v0.1 work.

---

## §7 — Recommended binding top-3 (post Phase II.5)

| Rank | Candidate | Lead | Phase III Scope | Class |
|------|-----------|------|-----------------|-------|
| **Co-1** | §2.5+§2.1 merged | Scratch (§2.5-only per Greg) | §5.1 ε derivation + §5.2 ∂κ/∂ε + §5.3 Hopf-fibre celestial mapping + §5.4 sky-coverage integrals | Physical mechanism |
| **Co-1** | §2.7 non-perturbative δ₂ | Jammer | Does LoTSS-DR2 geometry uniquely activate? Cross-survey geometry comparison; calculational derivation | Survey-specific systematic |
| 2 | §2.3 Φ_NTE frame mismatch | Jammer | Alive-but-watching; v0.1 prediction continues; re-rank threshold ~5–10° catalogue direction shift | Physical mechanism |

**Deferred:** §2.2 (architectural-class; post-sprint Programme S item)
**Held:** §2.4, §2.6 (pending catalogue n(z) re-validation)

**Phase IV convergence test:** quantitative comparison of merged §2.5 + §2.7 (+ optionally §2.3) against the four-survey amplitude/direction data. Co-rank-1 status preserves both candidates as primary convergence anchors. Multi-mechanism outcome (coherent combination of merged §2.5 + §2.7 + §2.3) is acceptable per AC honest-scope §7.

---

## §8 — Phase III implications

### §8.1 Phase III unblocked post Phase II.5

Per AC §4: Phase III mechanism work was blocked until Phase II.5 ships. Once Jammer's complementary Phase II.5 input lands and the joint deliverable is integrated, Phase III work begins:

- **Scratch:** Candidate §2.5 Phase III §5.1 → §5.2 → §5.3 → §5.4 sequence (~3-4 sessions per Candidate §2.5 scoping §6).
- **Jammer:** §2.7 mechanism scoping + §2.3 v0.1 prediction (parallel; already in flight per AC handoff 09:20Z, can be resumed properly post-II.5).

### §8.2 Cursor dependency

Phase III §5.4 (Scratch sky-coverage integrals) depends on Cursor's catalogue direction ingest (currently in queue per Coordination Register §3). The other Phase III §5.1 / §5.2 / §5.3 work is Cursor-independent and can proceed immediately.

Cursor's catalogue ingest priority is correctly tagged in Coordination Register v0.2 as "⏳ priority (Scratch Candidate 2.5 scoping shipped)".

### §8.3 Sequencing recommendation

- **Now:** Jammer engages Phase II.5 (complementary input) + integration into joint deliverable. ~½ session.
- **After Phase II.5 ships:** Phase III mechanism work commences. Scratch starts §5.1 (load-bearing ε derivation). Jammer starts §2.7 + §2.3 v0.1 in parallel.
- **Cursor catalogue ingest:** parallel with Phase III §5.1 / §5.2 / §5.3; lands before Phase III §5.4.
- **Phase IV convergence test:** assembles all Phase III v0.1 outputs + Cursor convergence harness.

---

## §9 — Files & cross-references

This file:
- `Working/Scratch_Wagenveld_Sprint_Phase_II_5_Input_v0_1.md` (this doc; Scratch-side input to joint Phase II.5)

Target joint deliverable (per AC §4):
- `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md` (TBD — integrate this file + Jammer's complementary input)

Primary reviewed inputs:
- `Handoffs/Handoff_AC_to_Cursor_Jammer_Scratch_Wagenveld_Sprint_Phase_II_Top3_Ranking_20260529.md` (Drive ID `1BtoOFURNl0g7n805G4a_jGLcGygwJfUL`) — AC top-3 ranking (Phase II.5 scope items 1–5)
- `Working/Wagenveld_Sprint_Coordination_Register_v0_1.md` (Drive ID `1zzlWb4Xwn-fGd_WwdiOSZYBq1tCX9jZd`) — Cursor v0.2 state confirms Phase II.5 priority
- `Working/Session_State_Summary_Jammer_Priority_Tasks_Wagenveld_Sprint_2026_05_29_Afternoon.md` (Drive ID `1jT2fXdDcnXdieakPe1tG9xhMz_5GXfLy`) — Jammer afternoon state (interpretation mismatch flagged)
- `Handoffs/Handoff_Greg_Scratch_Wagenveld_Sprint_Phase_II_Activation_Decisions_20260529.md` (Drive ID `1JxikD-7TbfDAAaF_Qh6cDbza_PtnAHhn`) — Greg "implicit" definition (no Greg-gate, not no review)

Predecessor Scratch deliverables:
- `Working/Scratch_Adversarial_Review_AC_Wagenveld_Sprint_v0_1_20260528.md` (Drive ID `1Izg6ng10pkDH_xpVxlQ7crbrnT6jlNGx`) — scoping flags
- `Working/Scratch_Wagenveld_Sprint_Phase_II_Adversarial_Review_v0_1.md` (Drive ID `1VNcoIkQmA0mtG2EC96HR3DqTfpoGo5rg`) — Phase II §8 verdict + merger correction
- `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` (Drive ID `15xexfe7DRuluCkgF7nyw8Cowegunph53`) — merged candidate scoping (Greg's three asks answered)

Drive canonical for Connes Programme structural claims:
- `Papers/Paper_Kappa_AB_v10_17_2.md` (Drive ID `1p3GeEnQi7ljlL6I-chN-HHZZXR_ZIggy`) — §3.3 Gaunt-coefficient argument; §3.4 topological protection; §5 closure structure

---

## §10 — Closing

Scratch-side Phase II.5 input shipped. Five scope items addressed:

1. **§2.7 rank-1 justification** — rejected "uniquely §2.7"; both §2.7 and merged §2.5 predict observed pattern; **co-rank-1 recommended**.
2. **§2.5 ↔ §2.1 closure-step linkage** — confirmed at derivation level; no revision.
3. **§2.2 deferral** — accepted; no significant hidden cost.
4. **§2.3 demotion threshold** — re-rank if catalogue ingest shifts Wagenveld direction >10° from CMB or aligns Quaia with §2.3 prediction.
5. **§2.4 / §2.6 hold criteria** — confirmed structurally justified.

**Process flag for Greg + Jammer:** "Phase II.5 implicit" interpretation mismatch between Jammer (no review ceremony) and AC + Cursor (review happens, no Greg-gate). Scratch reads with AC + Cursor; needs Greg confirmation.

**Awaiting Jammer's complementary input** for joint Phase II.5 sign-off (AC §4 target file: `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md`).

**Phase III blocked until joint Phase II.5 ships** per AC §4 directive.

— Scratch (Connes Programme lead), 2026-05-29 afternoon. Phase II.5 Scratch-side input v0.1 shipped; awaiting Jammer integration.
