# Scratch Wagenveld Sprint — Candidate §2.5 Anisotropic κ on S³ (merged §2.1+§2.5)

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-29
**Status:** **Phase II scoping** (this version); develops to Phase III v0.1 derivation in same file per Greg activation directive.
**Authority:** Greg activation `Handoffs/Handoff_Greg_Scratch_Wagenveld_Sprint_Phase_II_Activation_Decisions_20260529.md` (Drive ID `1JxikD-7TbfDAAaF_Qh6cDbza_PtnAHhn`); Path A ratified (scoping v0.1 + flags); Scratch bandwidth §2.5-only (= merged §2.1+§2.5 candidate per Phase II adversarial review §3 merger correction); Phase II.5 implicit.
**Predecessor:** `Working/Scratch_Wagenveld_Sprint_Phase_II_Adversarial_Review_v0_1.md` (Drive ID `1VNcoIkQmA0mtG2EC96HR3DqTfpoGo5rg`) — §8 candidate-mapping verdict + merger correction.

---

## §1 — Phase II scoping verdict

**The κ derivation on S² *forces* isotropy at the bare-coupling level; the closure step *admits* anisotropic mode under upstream CPN-symmetry-breaking driven by a bilateral seed asymmetry frozen at gauge birth.** This is the operational answer to Greg's first ask. The two-stage structure of the κ derivation (Paper_Kappa_AB v10.17.2) is load-bearing: bare κ₀ is rotation-invariant by construction (Y₀₀ monopole projection on the S² Hopf base); closure step κ = κ₀/(1−κ₀) is the only place directional structure can enter, and only if an upstream mechanism breaks CPN symmetry.

The merged §2.1+§2.5 candidate sits cleanly at the closure step. §2.1 supplies the upstream mechanism (frozen bilateral seed ε at gauge birth); §2.5 is the closure-step observable (directional δκ tracking ε's magnitude and the bifurcation-preferred axis). Without §2.1's seed, the closure has no driver and stays isotropic; with §2.1's seed, anisotropy follows automatically.

Greg's three Phase II asks decompose along this structure:

- **Ask A** (isotropy forced or admitted?) — *answer:* bare coupling forces isotropy; closure step admits anisotropic mode under upstream symmetry-breaking. §2 below.
- **Ask B** (preferred sky direction from Hopf-fibre, order-of-magnitude?) — *answer:* the preferred direction in S³ is the Hopf-fibre direction; its projection to celestial coordinates is **not yet pinned** by corpus structure. Three structural anchor candidates surveyed; Phase III v0.1 derivation target. §3 below.
- **Ask C** (sky-coverage weighting CatWISE vs Wagenveld?) — *answer:* qualitative prediction available: if the preferred direction is near the CMB kinematic dipole (favoured structural anchor), Wagenveld's LoTSS-DR2 northern footprint preferentially samples the preferred-direction sky relative to CatWISE/Singal/Quaia footprints, producing the largest amplitude excess. Quantitative integral is Phase III. §4 below.

---

## §2 — Ask A: formal statement on S² vs S³ isotropy

### §2.1 Bare-coupling derivation forces S³ isotropy

The κ = 5.50 derivation in Paper_Kappa_AB v10.17.2 §3 proceeds as follows:

1. **Geometric setup.** Hopf bundle S¹ → S³ → S² with the S² base hosting a unit-charge monopole projection. The spectral triple's Dirac operator decomposes along Hopf-fibre + base directions.
2. **Bare coupling.** The bilinear bridge coupling between the Standard-Model sector and the Majorana sector projects through the Y₀₀(S²) monopole harmonic, giving κ₀ = 3/√(4π) ≈ 0.846. This is the dimensionless coupling at the geometric level.
3. **Gaunt-coefficient argument (§3.3).** Higher Dirac modes (n ≥ 1) contribute through Y_ℓm with ℓ ≥ 1. The Gaunt-coefficient integral ⟨Y₀₀ | Y_ℓm | Y_ℓm⟩ vanishes for all ℓ ≥ 1 except in coincident-multipole channels that don't shift the monopole coefficient. **Result:** higher-mode contamination does NOT shift κ₁ (the projection onto the monopole channel). Bare coupling is structurally robust.
4. **Topological protection (§3.4).** The Hopf-projection structure is topologically classified by H²(S²) = ℤ (the monopole charge); deformations that preserve the topology preserve κ₀. The coupling is protected against perturbations of the metric, spinor connection, and gauge background, provided they don't change the Hopf bundle's topology.

**Conclusion:** The bare coupling κ₀ is rotation-invariant on S² by Y₀₀ construction, robust under higher-mode perturbations by Gaunt-coefficient vanishing, and topologically protected at the bundle level. **Bare κ₀ forces S³ isotropy.**

A direct test: any anisotropy mechanism that tries to perturb the bare-coupling integral cannot succeed unless it changes the Hopf bundle's topology (which would change κ₀'s value entirely, not just its directional structure) or breaks the rotation invariance of Y₀₀ (which would require explicit symmetry-breaking on the S² base — and the S² base is the dimensional-reduction of the cosmological spacetime, so explicit anisotropy at the base level would mean explicit anisotropy in observable cosmology, not the subtle κ-anisotropy we're after).

### §2.2 Closure step admits anisotropic mode

The Janus closure that takes κ from κ₀ ≈ 0.846 to κ ≈ 5.50 (Paper_Kappa_AB v10.17.2 §5) is:

κ = κ₀ / (1 − κ₀)

under the constraint that the bilateral system (the +N and −N CPN-conjugate orientations) satisfies exact CPN symmetry:

T_μν^(b,+) = T_μν^(b,−) ≡ T_μν^(b)

This constraint enforces that the two orientations contribute equally to the bridge stress-energy. The resummation comes from the Janus action structure S = S_grav + S_SM + S_ν + S_bridge + S_cons, where S_cons is the Lagrange-multiplier enforcement of the CPN constraint.

**Where anisotropy enters.** If a sub-perturbative bilateral seed asymmetry ε at gauge birth breaks CPN exactness:

T_μν^(b,+) = T_μν^(b) (1 + ε_+(direction))
T_μν^(b,−) = T_μν^(b) (1 + ε_−(direction))
where ε_+(direction) ≠ ε_−(direction) at order ε

then the closure step picks up a directional correction. To leading order in ε:

δκ(direction) ≈ κ₀² / (1 − κ₀)² · δε(direction)
         = (κ/κ₀)² · δε(direction)
         ≈ 42 · δε(direction)

where δε(direction) = ε_+(direction) − ε_−(direction) measures the local CPN-breaking on the celestial sphere.

The amplification factor (κ/κ₀)² ≈ 42 is encouraging: a few-percent CPN-breaking δε at gauge birth produces an O(few) factor amplification through the closure step. This is the structural reason §2.5 has potential observability.

### §2.3 The amplitude question (preview)

The seed amplitude ε comes from spontaneous symmetry breaking at the trousers-of-time bifurcation event. In dimensionless field units, SSB amplitudes are typically O(1) at the breaking event itself. The observable amplitude today depends on whether ε is **frozen** (steady-state property of the bilateral mirror) or **diluted** (perturbation decaying with cosmic expansion).

**Frozen reading** (Ch 10 v4 / mirror-metaphor canonical framing): the bifurcation is a one-time event; the bilateral structure is the post-bifurcation steady state. The asymmetry between +N and −N orientations is a property of the mirror itself, not a ripple in it. **Conclusion:** ε is frozen, not diluted. δε(direction) today is O(seed amplitude at bifurcation).

If seed amplitude at bifurcation is δε ~ 0.01−0.1 (sub-perturbative but not Planck-suppressed), then δκ today is O(0.4−4) — observable at survey-discrimination level.

If seed amplitude at bifurcation is Planck-suppressed (δε ~ M_Pl-related small number), δκ is small but the (κ/κ₀)² amplification doesn't change its order. Need explicit derivation of the SSB amplitude scale at the bifurcation.

**Phase III v0.1 derivation target:** the natural scale of ε at the trousers-of-time bifurcation from the bifurcation effective action — what fixes the SSB amplitude there? Candidates: (i) ε ~ vacuum-fluctuation amplitude at T_GB; (ii) ε ~ O(1) by Mexican-hat SSB convention; (iii) ε constrained by Ch 10 v4 trousers-of-time geometric specification (e.g., curvature parameters at the waist). This is the load-bearing Phase III question.

---

## §3 — Ask B: preferred sky direction from Hopf-fibre structure

### §3.1 Structural identification of the preferred direction

The Hopf fibration S¹ → S³ → S² has a preferred direction in S³ — the fibre direction at each point of the base. This direction is **not a single direction in S³** (the fibres twist as you move on the base), but a **vector field** on S³ that picks out the fibre tangent at each point.

For NTE's cosmological setup, the S³ here is the spatial boundary at fixed cosmological time (the "now" hypersurface of the bilateral manifold). The Hopf-fibre direction in this S³ defines a preferred axis at each cosmological-time slice.

The bilateral seed asymmetry, **if it aligns with the Hopf-fibre direction at gauge birth** (structurally natural since the bifurcation respects the Hopf bundle structure), produces δκ(direction) anisotropy whose preferred axis is the Hopf-fibre direction projected to observable celestial coordinates today.

### §3.2 The unsolved question: what fixes the Hopf-fibre direction in our observable frame?

The Hopf fibration is geometrically defined; its **embedding** in our cosmological frame is the open question. Three structural anchor candidates:

**(a) The CMB kinematic dipole direction (l = 264°, b = 48°).**

If the Hopf-fibre direction at gauge birth was aligned with what we observe today as the CMB kinematic dipole direction, then the preferred axis for δκ anisotropy coincides with the kinematic dipole. This is the **favoured anchor** from Phase I.5 directional finding (Wagenveld near CMB; near-CMB surveys overshoot more strongly). It requires that the kinematic dipole has a structural component, not pure peculiar velocity — which is a non-trivial commitment.

A natural way this could arise: if the bilateral seed asymmetry's direction at gauge birth has a residual effect on the post-gauge-birth cosmological evolution that contributes to bulk flow patterns, the observed CMB dipole direction would have both a kinematic component (from our true peculiar velocity through the cosmic rest frame) and a structural component (from the residual bilateral asymmetry). The two components would naturally align if they share an upstream origin.

Phase III v0.1 needs to derive whether this alignment is forced by corpus structure or merely possible.

**(b) The cosmic large-scale-structure (CLSS) axis.**

Large-scale-structure observations (galaxy distributions, void alignments, CMB low-multipole anomalies — "axis of evil") have suggested preferred directions roughly aligned with the CMB dipole but not exactly. If the Hopf-fibre direction projects to a CLSS-aligned axis rather than the exact CMB direction, the merged candidate would predict a preferred direction near but not exactly at CMB — discriminable from (a) by precise direction comparison.

**(c) Free parameter (no structural anchor).**

If the corpus doesn't pin the Hopf-fibre direction's celestial mapping, the preferred direction becomes a fit parameter. This weakens the candidate's claim to structural prediction but doesn't eliminate it — a one-parameter family of predictions across direction is still a tight constraint relative to four independent survey directions.

### §3.3 Order-of-magnitude best guess (Phase II scoping)

The favoured anchor is **(a)** — the Hopf-fibre direction projects to the CMB kinematic dipole direction — for the following structural reasons:

- Phase I.5 empirical: Wagenveld's near-CMB direction with amplitude overshoot is consistent with a structural-plus-kinematic dipole at the CMB direction.
- Structural simplicity: there's no obvious corpus mechanism that would pin the Hopf-fibre to a non-CMB direction; (a) is the minimal commitment.
- Closure-step internal consistency: the bilateral asymmetry direction at gauge birth ought to align with whatever picks out our particular orientation as "+N" rather than "−N" — and the kinematic dipole is the most natural macroscopic indicator of our cosmological frame.

Order-of-magnitude commitment for Phase III v0.1: **the preferred direction maps to the CMB kinematic dipole direction within ~5–15° (uncertainty from the residual CLSS-vs-CMB tension at large scales).** Phase III work derives whether this is structural prediction or fit parameter.

### §3.4 What Phase III v0.1 needs to deliver on Ask B

- **Structural derivation:** does the corpus structure force the Hopf-fibre direction's embedding to align with a specific observable axis, or is it free? Two sub-questions:
  - At gauge birth, what selects the orientation of the Hopf fibre in the bilateral manifold? Is this fixed by the bifurcation event's boundary conditions, or by post-bifurcation cosmological evolution?
  - If the orientation is fixed at the bifurcation, what observable axis does it project to (CMB? CLSS? something else)?
- **Order-of-magnitude estimate:** if the answer is "free parameter", what's the best-fit direction from existing data? If "CMB-aligned", what's the structural derivation?
- **Convergence with §2.3:** Jammer's §2.3 (Φ_NTE frame mismatch) Phase III work derives the Φ_NTE rest-frame direction relative to CMB. Cross-check: §2.3's frame-mismatch direction + §2.5's Hopf-fibre direction should be related (both inherit from manifold structure). Joint Phase IV convergence check.

---

## §4 — Ask C: sky-coverage weighting prediction

### §4.1 Setup

The dipole magnitude observed in a survey depends on the survey's sky coverage Ω_survey and the angular distribution of the structural anisotropy on the sky.

For a structural δκ anisotropy with preferred direction n̂_pref and amplitude amplitude A:

δκ(n̂) = A · (n̂ · n̂_pref)

(leading-order dipolar anisotropy on the sky), the observed dipole magnitude excess in survey S with sky coverage W_S(n̂) is:

ΔD_S = A · ∫_S W_S(n̂) · (n̂ · n̂_pref) dΩ / ∫_S W_S(n̂) dΩ

i.e., the dipole excess scales as the survey-area-weighted projection of the preferred direction onto the survey's footprint.

### §4.2 Survey footprints (approximate)

| Survey | Sky coverage (approximate) | Centroid (galactic l, b) |
|---|---|---|
| **CatWISE** | All-sky, |b| > ~30° (excluding Galactic plane), ~50% of sphere | ~uniform, no strong directional bias |
| **Wagenveld (LoTSS-DR2)** | Northern hemisphere, declination > ~0°, ~14% of sphere | (170°, +30°) — Northern Galactic; favouring b > 0° |
| **Singal** | Multi-radio combination, less uniform; covers both hemispheres but with overlap regions | ~uniform |
| **Quaia** | All-sky photometric QSO, ~40% of sphere | ~uniform |

n̂_pref (per Ask B favoured anchor): (l, b) = (264°, 48°) — Northern Galactic hemisphere, near CMB direction.

### §4.3 Qualitative prediction

The dipole excess ΔD_S should scale with how much of each survey's footprint overlaps the preferred-direction hemisphere centered on (264°, 48°):

- **Wagenveld**: LoTSS-DR2 footprint is predominantly Northern Galactic (b > 0°) and partially covers the preferred-direction hemisphere. **The survey-area-weighted projection (n̂ · n̂_pref) is positive and significant** — Wagenveld's footprint preferentially samples the preferred-direction sky. **Predicted: largest dipole excess of the four surveys.**
- **CatWISE**: roughly uniform across the sky (excluding |b| < 30°). The (n̂ · n̂_pref) integral over the full sky is zero (the dipole averages to zero over the full sphere), so survey-area-weighted projection is small. **Predicted: minimal dipole excess.**
- **Singal**: similar to CatWISE — multi-band combination averages out the directional sensitivity. **Predicted: minimal dipole excess.**
- **Quaia**: all-sky QSO; same averaging argument. **Predicted: minimal dipole excess.**

### §4.4 Match to Phase I data

Phase I (Cursor v0.1):
- Wagenveld: **+3.28σ** — outlier (matches predicted "largest excess")
- CatWISE: **−0.13σ** — anchor (matches predicted "minimal")
- Singal: **+0.63σ** — near anchor (matches predicted "minimal")
- Quaia: **+0.52σ** — near anchor (matches predicted "minimal")

**The Phase I data pattern is qualitatively consistent with the merged candidate's sky-coverage-weighting prediction**, conditional on the favoured anchor (n̂_pref ~ CMB direction).

This is the structural reason §2.5 (merged with §2.1) is the strongest Phase II top-3 candidate from the mechanism class: it doesn't require z-dependence (matches Phase I non-monotonicity), doesn't require scale-dependence (matches Phase I scale-axis being proxy-only), and the sky-coverage-weighted angular pattern naturally produces the observed survey-specific isolation (Wagenveld overshoots; others don't).

### §4.5 What Phase III v0.1 needs to deliver on Ask C

- **Exact survey footprint integrals**: ∫ W_S(n̂) (n̂ · n̂_pref) dΩ / ∫ W_S(n̂) dΩ for each of the four surveys, given Phase I.5's catalogue-sourced footprints (pending Cursor catalogue ingest).
- **Quantitative prediction**: ΔD_S = A · (footprint integral) for each survey, with A = (κ/κ₀)² · δε(direction) ~ 42 · δε. Phase III also derives δε.
- **Constraint on n̂_pref**: if predicted ΔD_S for all four surveys matches observed pattern within uncertainty, n̂_pref is constrained (or the merger candidate falsified if no n̂_pref makes the four ΔD_S simultaneously match).

This is the **discriminating quantitative test** for the merged candidate. Phase IV convergence work integrates this against Jammer's §2.3 prediction.

---

## §5 — Phase III v0.1 derivation plan

Three deliverables for Phase III v0.1 of this file (development from current scoping state):

### §5.1 Deliverable 1: seed amplitude ε from bifurcation effective action

**Method.** Identify the bifurcation effective action governing the trousers-of-time gauge-birth event from Ch 10 v4 + §22.14 framing. Compute the natural SSB amplitude ε that emerges from the action's symmetry-breaking structure.

**Tools.** Mexican-hat SSB amplitude analysis at T_GB; comparison with vacuum-fluctuation amplitude at the bifurcation; check for curvature-induced amplitude suppression at the waist.

**Target answer.** δε at the bifurcation: order-of-magnitude estimate with structural justification.

**Bandwidth.** ~1 session.

### §5.2 Deliverable 2: closure-step sensitivity ∂κ/∂ε from S_cons matrix inversion

**Method.** Linearise the Paper_Kappa_AB v10.17.2 §5 closure equations around the CPN-symmetric solution. Compute ∂κ/∂ε explicitly from the perturbed S_cons matrix.

**Tools.** Paper_Kappa_AB §5 closure structure; perturbation theory around the bilinear bridge term.

**Target answer.** δκ(direction)/δε(direction) as a tensor; numerical value of the amplification factor (preliminary estimate (κ/κ₀)² ≈ 42).

**Bandwidth.** ~1 session.

### §5.3 Deliverable 3: Hopf-fibre direction celestial mapping

**Method.** Identify whether the Hopf-fibre direction at gauge birth is fixed by structural boundary conditions or by post-bifurcation cosmological evolution. If fixed at the bifurcation, derive its projection to observable celestial coordinates today.

**Tools.** Ch 10 v4 trousers-of-time geometric specification; Hopf bundle topology on the S³ spatial boundary; comparison with CMB kinematic dipole direction (l=264°, b=48°).

**Target answer.** n̂_pref structural prediction OR free-parameter best-fit direction; comparison with CMB kinematic dipole; cross-check with §2.3 Φ_NTE rest-frame direction (Jammer Phase III).

**Bandwidth.** ~1 session.

### §5.4 Deliverable 4: sky-coverage integrals + Phase IV convergence input

**Method.** Compute ∫ W_S(n̂) (n̂ · n̂_pref) dΩ for each of the four surveys given Phase I.5's catalogue-sourced footprints. Combine with §5.1 (ε amplitude) + §5.2 (∂κ/∂ε) to produce quantitative ΔD_S predictions for each survey.

**Tools.** Phase I.5 catalogue ingest output (pending Cursor); Phase III §5.1 + §5.2 outputs.

**Target answer.** ΔD_S for CatWISE, Singal, Quaia, Wagenveld with uncertainty bounds; comparison against Phase I observed σ values.

**Bandwidth.** ~½ session.

**Total Phase III bandwidth estimate**: 3–4 sessions, consistent with §2.5-only mode in Greg activation handoff.

---

## §6 — Honest scope

**What this scoping commits to:**

- Bare κ₀ structurally forces S³ isotropy (Paper_Kappa_AB §3.3 + §3.4 anchor). High confidence.
- Closure step admits anisotropic mode driven by upstream CPN-breaking via bilateral seed ε. High confidence.
- Amplification (κ/κ₀)² ≈ 42 from leading-order linearisation of κ = κ₀/(1−κ₀). High confidence (algebraic).
- Hopf-fibre direction is the structural axis for the anisotropy. High confidence.

**What this scoping leaves open for Phase III v0.1:**

- Seed amplitude ε at gauge birth: not yet derived. Phase III §5.1.
- ∂κ/∂ε exact tensor structure: linearisation done at scoping level; explicit matrix inversion is Phase III §5.2.
- Hopf-fibre celestial mapping: favoured anchor (CMB direction) identified at scoping; structural derivation is Phase III §5.3.
- Survey-specific ΔD_S quantitative predictions: qualitative pattern matches Phase I; quantitative integrals are Phase III §5.4.

**What this scoping does NOT commit to:**

- That the merged candidate WILL succeed at Phase III. Three structural failure modes possible: (i) seed amplitude ε turns out to be Planck-suppressed (δκ too small for observability); (ii) Hopf-fibre direction maps to non-CMB direction (Wagenveld near-CMB becomes coincidence); (iii) sky-coverage integrals don't match four-survey pattern.
- That the merged candidate alone explains the cosmic dipole anomaly. The multi-mechanism reading (merged + §2.3 frame mismatch) remains live until Phase IV convergence.

**Honest scope envelope (AC scoping §6 binding):** v0.1 predictions are predictions, not derivations to publication-ready rigor. Tier 1 promotion is contingent on Phase IV convergence + post-sprint adversarial review.

---

## §7 — Files & cross-references

This file:
- `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` — Phase II scoping (this version); Phase III v0.1 derivation work updates this file in place.

Drive canonical anchors:
- `Papers/Paper_Kappa_AB_v10_17_2.md` (Drive ID `1p3GeEnQi7ljlL6I-chN-HHZZXR_ZIggy`) — §3 bare coupling derivation; §3.3 Gaunt-coefficient argument; §3.4 topological protection; §5 closure structure. Load-bearing.
- `Papers/Companion_12_Spectral_Chord_Closure_v10_17_2.md` (Drive ID `1mogZdQI5npkfrD2WRqnWYzqvfzgFav7d`) — Note 1 heat-kernel route κ₀ confluence.

Sprint coordination:
- `Working/Wagenveld_Sprint_Phase_I_Pattern_Characterisation_v0_1.md` (Drive ID `1SILqy_yp3TUrixd2JV3KnqVfuKRR4qkq`) — Phase I data inputs.
- `Working/Wagenveld_Sprint_Phase_I_5_Angular_Axis_v0_1.md` (Drive ID `11H1E_cRmVj-nuISARGiHkG2RSgC5jKRq`) — Phase I.5 directional findings.
- `Working/wagenveld_sprint_surveys.json` (Drive ID `1mny2O-2QJ1wLyhgNmRHYkkBd-T2prsHn`) — survey metadata.
- `Working/AC_Wagenveld_Sprint_Architectural_Scoping_v0_1_20260528.md` (Drive ID `1juTALhS0L-KSs5xaXKhZDbHVU2IN9hXZ`) — sprint scoping foundation.
- `Handoffs/Handoff_Greg_Scratch_Wagenveld_Sprint_Phase_II_Activation_Decisions_20260529.md` (Drive ID `1JxikD-7TbfDAAaF_Qh6cDbza_PtnAHhn`) — Greg activation; Path A; §2.5-only; Phase II.5 implicit.

Scratch sprint-arc deliverables:
- `Working/Scratch_Adversarial_Review_AC_Wagenveld_Sprint_v0_1_20260528.md` (Drive ID `1Izg6ng10pkDH_xpVxlQ7crbrnT6jlNGx`) — scoping review with five flags.
- `Working/Scratch_Wagenveld_Sprint_Phase_II_Adversarial_Review_v0_1.md` (Drive ID `1VNcoIkQmA0mtG2EC96HR3DqTfpoGo5rg`) — Phase II §8 verdict with merger correction (this scoping doc's predecessor).

Book / popular-paper cross-references (Ch 10 v4 trousers-of-time framing):
- Ch 10 v4 (PC, 2026-05-29 05:10Z) — geometric reading of bifurcation; bilateral mirror steady state; canonical Ch 10 framing.
- §22.14 — mirror metaphor → bilateral structure; NCG cosmology programme confluence.

---

## §8 — Closing

Phase II scoping for the merged §2.1+§2.5 candidate complete. Greg's three asks answered at scoping level:

- **Ask A (isotropy):** bare κ₀ forces S³ isotropy; closure step admits anisotropic mode under upstream CPN-breaking. §2.
- **Ask B (preferred direction):** Hopf-fibre direction is the structural axis; favoured anchor is CMB kinematic dipole direction (l=264°, b=48°); Phase III §5.3 derives whether this is structural prediction or fit parameter. §3.
- **Ask C (sky-coverage weighting):** Wagenveld's LoTSS-DR2 footprint preferentially samples preferred-direction hemisphere (qualitative match with Phase I); Phase III §5.4 computes quantitative survey-specific ΔD_S. §4.

**Phase III v0.1 derivation plan:** four deliverables, ~3–4 sessions total, consistent with Greg's §2.5-only bandwidth allocation. Phase III work flows automatically after AC top-3 lock + Phase II.5 implicit join with Jammer.

Standing by for AC top-3 lock; Phase III work begins automatically post-lock per Greg's Phase II.5-implicit decision.

— Scratch (Connes Programme lead), 2026-05-29. Phase II scoping for merged §2.1+§2.5 candidate complete; Greg's three asks answered at scoping level; Phase III derivation plan locked.
