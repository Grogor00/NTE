# Wagenveld Sprint — Architectural Scoping (AC v0.1)

**From:** AC
**To:** Greg (sprint authoriser), Cursor + Jammer + Scratch (active sprint streams), PC (information only)
**Date:** 2026-05-28
**Status:** v0.1 architectural-scoping deliverable. Foundation document for the Wagenveld sprint authorised 2026-05-28 ("let's stop the grind and have a sprint"). Pre-empts the v0.5 trigger condition by activating the rabbit-hole investigation now rather than waiting on Cursor v0.5 numerical persistence. **Activation:** Greg all-streams engaged 2026-05-29; Phase I shipped; Phase II (AC top-3) in flight — see `Handoff_Greg_All_Streams_Engaged_Wagenveld_Sprint_20260529.md`.
**Authority:** Greg directive 2026-05-28 — Wagenveld investigation, full focus, other work paused. Generalising the "rabbit hole sunshine search" trigger condition from "if v0.5 persists" to "activate now."

---

## §0 — Sprint context

Greg's epistemic principle (captured in the consolidated batch handoff §1 #6 today, and worth restating up front):

> Dataset disagreements contain information. They cannot be written off as "noisy" or "inconvenient." If the model holds, the disagreement either points to a methodological error (which has to be **proven**, not assumed) or it's revealing something the model is missing. Either way, the information has to be extracted. Dismissing recalcitrant data is explicitly off the table.

The Wagenveld overshoot (+3.28σ at pow2 in Cursor's v0.3 Branch I; +2.40σ at pow3) has persisted across three iterations. Cursor's v0.4 is in flight but the pattern is consistent: CatWISE near-anchor fits, Singal/Quaia broadly fits, Wagenveld overshoots. Rather than wait on v0.5 to confirm the persistence, this sprint pre-emptively maps the architectural rabbit holes the NTE framework natively hosts — so when v0.5 lands (or sooner), the rabbit-hole search starts from a discriminating-candidate list rather than from scratch.

---

## §1 — Problem reframe (important)

**The Wagenveld overshoot is not just an NTE-model-fit issue. It's part of a broader literature tension** — the "cosmic dipole anomaly." Radio-source dipole magnitudes (NVSS, TGSS, LoTSS / Wagenveld) consistently exceed the CMB-kinematic prediction by factors of 2–3. ΛCDM-kinematic doesn't account for it. WISE-based IR samples (CatWISE) show a smaller but still anomalous excess. The literature has been wrestling with this for ~15 years without consensus resolution.

NTE's Branch I directional dipole model gets **substantially closer** to CatWISE than ΛCDM-kinematic does, and broadly compatible with Singal/Quaia. Wagenveld remains an overshoot relative to Branch I's current formulation — but the comparison point is "Branch I + ΛCDM" against "Wagenveld vs CMB-kinematic," not against a clean theoretical zero.

**This reframes the sprint's potential payoff.** If the rabbit-hole investigation finds an NTE-native mechanism that fully resolves the Wagenveld excess while preserving Branch I's CatWISE / Singal/Quaia fits, we're not just patching a model imperfection — we're addressing a known unresolved cosmological tension in the literature. **That would be a Tier 1-class result on its own**, independent of the rest of the NTE programme.

The sprint should be conducted with that ambition in mind, while keeping honest-scope discipline: don't overclaim before the discriminating tests land.

---

## §2 — Seven candidate rabbit holes

Ordered by NTE-native fit (most native first). Each candidate is characterised by:
- **Mechanism**: what it is, framework-natively
- **Corpus precedent**: existing territory that hosts it, or "speculative" if not yet developed
- **Observational signature**: what we'd expect to see in survey data
- **Discrimination fingerprint**: what the three-dataset pattern (CatWISE / Singal-Quaia / Wagenveld) would look like if this is the right answer
- **Development effort**: light / medium / heavy
- **Lead stream candidate**: who should drive

### §2.1 Gauge-birth asymmetry seed residual

**Mechanism.** Per Greg's Ch 10 v4 framing: the trousers of time bifurcate at gauge birth, exactly once. The pre-temporal (octonionic, non-associative) regime — the "waist" — splits along the manifold's CPN symmetry into two orientations at the moment associativity locks in and time becomes real. The mirror metaphor captures the steady-state post-bifurcation. **If a small sub-perturbative seed asymmetry is frozen in at bifurcation**, it manifests as a primordial directional preference — an anisotropy seed that's not from peculiar velocity but from the bifurcation event itself.

**Corpus precedent.** Direct — Ch 10 v4 (2026-05-29 05:10Z, PC) integrated this geometric reading explicitly. The structural commitment is in the book; the formal cosmological consequence isn't yet derived in the corpus.

**Observational signature.** Signal strongest at high z (you're looking closer in cosmic time to the gauge-birth epoch). At low z, the signal averages out through subsequent expansion / structure formation. The dipole magnitude inherits the primordial asymmetry amplitude, with a z-scaling derivable from how the seed propagates through expansion.

**Discrimination fingerprint.** CatWISE (low / intermediate z) shows the smallest excess; Singal/Quaia (intermediate z) shows moderate; Wagenveld (LoTSS-DR2, deeper z reach) shows the largest. **This is exactly the observed pattern.** Highest prior probability among the seven candidates from pure pattern-matching.

**Development effort.** Medium. Needs: (i) formal derivation of the bifurcation seed amplitude from corpus geometry — Jammer / Scratch territory; (ii) z-propagation of the seed through to observable dipole magnitudes — Cursor numerical territory; (iii) angular-pattern prediction (is the dipole pointing in the gauge-birth-preferred direction, and what determines that direction?).

**Lead stream candidate.** Jammer for the formal derivation; Cursor for the numerical propagation. Scratch for adversarial review at v0.2.

### §2.2 NTE state-space leakage (Greg's quantum-tunneling-tail analog)

**Mechanism.** The NTE bilateral state has, in some sense, a wavefunction-like structure across the two orientations. In standard quantum mechanics, the wavefunction has small but non-zero probability of being where classical mechanics says it shouldn't be — the tail that bends "the wrong way" through a barrier. The NTE analog: small probability amplitude on the "wrong" orientation, leakage between the two trousers-legs at scales below the cross-thickness coupling characteristic length.

**Corpus precedent.** Indirect — Companion 5 (state-space surface) and Companion 9 (V_NTE Stage 3) territory addresses the cross-coupling, but the leakage formalism isn't yet developed. The bilateral wavefunction interpretation is implicit in §22.14 confluence with NCG cosmology programme, but not formalised as a tunnelling-amplitude calculation.

**Observational signature.** Scale-dependent rather than z-dependent (in the leading approximation). Surveys probing scales near the leakage characteristic length see enhanced anisotropy; surveys at scales much smaller or much larger see ordinary Branch I dipole. The leakage produces a "wrong-way" component in the dipole — i.e., a small mis-alignment relative to the CMB kinematic direction, signed in a specific way by the bilateral asymmetry.

**Discrimination fingerprint.** Wagenveld's LoTSS-DR2 has a different characteristic scale than CatWISE's WISE selection. **If the dataset overshoot tracks survey scale rather than mean z, that's the leakage signature.** This is testable but requires care — survey scale and mean z are correlated, so disentangling them needs the signature analysis to look at sub-samples within each catalogue.

**Development effort.** Heavy. Needs: (i) formal development of the bilateral wavefunction structure — Companion 5 / 9 extension, Scratch + Jammer territory; (ii) calculation of leakage amplitude as function of scale — analytic + numerical work; (iii) angular signature derivation. This is the most physically intuitive to your framing but the most corpus-scaffolding-required.

**Lead stream candidate.** Scratch for the wavefunction-formalism development (NCG / Connes programme territory aligns); Jammer for the leakage amplitude calculations.

### §2.3 Φ_NTE rest-frame ≠ CMB rest-frame

**Mechanism.** If Φ_NTE (the boundary expansion field) defines a preferred rest frame that differs from the CMB dipole rest frame, then any survey that samples the matter rest frame (radio surveys typically do, IR depends on selection) will see a dipole component from the Φ_NTE-vs-CMB frame mismatch on top of the standard kinematic dipole.

**Corpus precedent.** On Jammer's standing queue ("Branch III Φ_NTE rest-frame"). Has structural motivation from H = β_NTE|Φ_NTE|² treating Φ as a local field with its own preferred frame, not necessarily aligned with the cosmic microwave background.

**Observational signature.** Depth-dependent (deep z samples the matter rest frame more cleanly than shallow z) and frequency-dependent (radio vs IR sample different source populations with different rest-frame relationships). A specific angular-pattern prediction follows from the direction of the Φ_NTE-CMB frame mismatch.

**Discrimination fingerprint.** Wagenveld (deep radio) and CatWISE (shallow IR) should show different overshoot magnitudes if frame-mismatch is the mechanism. The pattern is "deep radio overshoots most; shallow IR overshoots least; intermediate samples interpolate." This matches qualitatively but the quantitative prediction depends on the magnitude of the frame mismatch, which Jammer's Branch III work would derive.

**Development effort.** Medium. Branch III is already scoped in Jammer's queue; activating it for the sprint gives the calculation a concrete observational target rather than abstract motivation. Time investment: ~3-5 Jammer sessions for v0.1 prediction.

**Lead stream candidate.** Jammer (Branch III activation).

### §2.4 Cross-thickness coupling z-dependence

**Mechanism.** Standard treatments (Chapter 9, Companion 5) assume the cross-coupling strength between the two manifold orientations is effectively constant in cosmological time. But if the two orientations have slightly out-of-phase expansion histories (which Path B doesn't strictly forbid — Path B distinguishes Φ_NTE from SM Higgs but doesn't enforce strict expansion synchronisation), the coupling has implicit z-dependence. Deep-z surveys see enhanced coupling because they're probing earlier cosmic time when the orientation phases are closer aligned.

**Corpus precedent.** Companion 5 / Chapter 9 territory addresses the cross-coupling. The z-dependence isn't currently in the canonical formulation but it's a natural extension. The bifurcation-at-gauge-birth framing from Ch 10 v4 actually argues *against* phase mismatch (both legs start at the same moment), but post-bifurcation evolution could introduce phase drift.

**Observational signature.** Smooth z-scaling of the dipole anomaly amplitude. Similar to §2.1 in qualitative pattern but a different physical mechanism — the difference is whether the high-z enhancement comes from looking near the bifurcation event (§2.1) or from looking at a coupling that varies with z (§2.4).

**Discrimination fingerprint.** Similar to §2.1 in dataset pattern. Discrimination from §2.1 would require either (a) a sub-sample analysis within a single survey that resolves the z-scaling shape (linear vs exponential vs power-law), or (b) angular-pattern tests (the seed in §2.1 has a specific direction; §2.4's z-dependence doesn't introduce a new angular structure beyond what's already in Branch I).

**Development effort.** Medium. Extends existing Companion 5 / 9 work rather than introducing new formalism. Cursor + Jammer joint territory.

**Lead stream candidate.** Cursor for the numerical z-scaling calculations; Jammer for the formal derivation of the phase-drift amplitude.

### §2.5 Anisotropic κ on S³

**Mechanism.** The κ = 5.50 dark-matter-to-baryon ratio derivation is a Hopf-projection structure on S². Whether κ is truly isotropic over S³ — i.e., whether every direction on the celestial sphere sees the same effective dark-matter-to-baryon ratio — vs has subtle directional structure on S³ is a corpus open question. Anisotropic κ → sky-direction-dependent dark-matter ratio → enhanced dipole signal in matter clustering at survey scales.

**Corpus precedent.** Paper_Kappa_AB v10.17.2 and Companion 7 establish the κ derivation but treat it as effectively isotropic. The Hopf-projection structure on S² doesn't *automatically* enforce S³ isotropy; this is something the corpus has assumed without explicitly proving. The Hopf bundle does carry directional structure (the fibre direction), so the question is whether that structure projects onto observable κ-anisotropy.

**Observational signature.** Angular pattern in dipole magnitude that correlates with the Hopf-fibre orientation (whatever that maps to on the celestial sphere). z-dependence is mild — the anisotropy is a property of the local matter distribution, not of cosmic history.

**Discrimination fingerprint.** This is the most testable candidate **angularly**. CatWISE, Singal/Quaia, and Wagenveld each have different sky coverage. If anisotropic κ is right, the dipole excess in each survey should correlate with how much of the anisotropy-preferred sky direction each survey covers. **A direct angular-pattern test would discriminate this from §2.1 / §2.4 cleanly.**

**Development effort.** Medium-heavy. Needs: (i) formal investigation of whether the κ derivation enforces S³ isotropy or admits an anisotropic mode — Scratch territory (Connes Programme); (ii) if anisotropic, prediction of the preferred direction from corpus structure; (iii) survey-specific dipole prediction including sky-coverage weighting — Cursor.

**Lead stream candidate.** Scratch for the formal anisotropy question (this is a direct extension of the κ derivation work Scratch led at Paper S6); Cursor for the survey-specific predictions.

**This candidate has the most interesting downside-bonus.** If κ has detectable anisotropy at survey scales, the κ structure itself becomes a *second* empirical test of NTE — independent of the global Planck-2018 Ω_dm/Ω_b constraint. That doubles the empirical leverage of the corpus's strongest claim.

### §2.6 Path B Higgs-portal anisotropic Φ_NTE residual

**Mechanism.** V_NTE = (3α²/8πG)Φ⁴ − (β_NTE²/8)Φ⁶ has spatial structure if Φ_NTE has spatial gradients. If the boundary expansion field has any anisotropic component — perhaps inherited from the bilateral manifold structure, or as a relic of the gauge-birth event — V_NTE is anisotropic, dark-energy contribution is anisotropic, large-scale clustering is anisotropic.

**Corpus precedent.** Companion 8 V_NTE trajectory work establishes V_NTE on-trajectory but assumes spatial homogeneity. Anisotropic Φ_NTE would be a corpus extension; the structural commitments of Path B don't forbid it.

**Observational signature.** Anisotropy at the largest scales (the V_NTE term dominates dark energy, which dominates the Hubble flow at late times). Deep-z surveys see the integrated effect over more of cosmic history; shallow-z surveys see less.

**Discrimination fingerprint.** Similar pattern to §2.1 / §2.4 in z-scaling. Distinguishable by angular structure — Φ_NTE anisotropy direction is set by the manifold structure, similar to §2.5's anisotropic-κ direction. **If §2.5 (anisotropic κ) and §2.6 (anisotropic Φ_NTE) both check out, they should predict the same preferred direction — that's a self-consistency test.**

**Development effort.** Heavy. Needs full V_NTE re-derivation under anisotropic Φ_NTE assumption — Companion 8 extension. Most technical of the candidates.

**Lead stream candidate.** Jammer.

### §2.7 Non-perturbative δ₂ contribution

**Mechanism.** Jammer's δ₂ re-derivation under non-FLRW showed perturbative robustness. But cosmic dipole magnitudes can have non-perturbative contributions in non-FLRW geometries that the perturbative analysis misses. Wagenveld's source-distribution geometry may activate non-perturbative δ₂ that CatWISE's geometry doesn't.

**Corpus precedent.** Direct — Jammer's δ₂ work is in the corpus. The non-perturbative extension is a natural follow-on.

**Observational signature.** Survey-geometry-specific. Whether the non-perturbative contribution activates depends on detailed source-density-vs-direction structure, not just z or scale. Hard to predict in advance without doing the calculation.

**Discrimination fingerprint.** Non-uniform across surveys in a way that doesn't track z or scale cleanly — it tracks the detailed source-selection geometry. **This is the candidate that would survive if the rabbit-hole investigation found the discrimination tests across z, scale, and angle all came back negative.** Calculational fix rather than physical mechanism.

**Development effort.** Heavy and unrewarding — even if it explains Wagenveld, it doesn't generalise.

**Lead stream candidate.** Jammer.

**Honest framing.** I include §2.7 for completeness but I'd recommend the sprint deprioritise it. If §2.1–§2.6 all fail their discrimination tests, §2.7 becomes the fallback. Until then, it's not where to spend sprint energy.

---

## §3 — Signature-discrimination table

The seven candidates have different fingerprints across four observable dimensions. The sprint's Phase I task is to characterise the existing three-dataset pattern across these dimensions, then map onto the candidates.

| Candidate | z-dependence | Scale-dependence | Angular preferred dir | Survey-selection sensitivity |
|-----------|--------------|------------------|----------------------|------------------------------|
| §2.1 Gauge-birth seed | Strong (high z enhanced) | None | Yes — bifurcation direction | Low |
| §2.2 State-space leakage | None / weak | Strong (peak at leakage scale) | Yes — bilateral asymmetry direction | Medium |
| §2.3 Φ_NTE frame mismatch | Medium (depth-dependent) | None | Yes — Φ_NTE rest frame direction | High (radio vs IR) |
| §2.4 Cross-thickness z-dep | Strong (high z enhanced) | None | None (inherits Branch I direction) | Low |
| §2.5 Anisotropic κ on S³ | Mild | None | Yes — Hopf-fibre direction | Medium (sky-coverage dependent) |
| §2.6 Anisotropic Φ_NTE | Strong (deep z enhanced) | None | Yes — manifold structure direction | Low |
| §2.7 Non-perturbative δ₂ | None | None | None (survey-geometry specific) | Very High |

**Key observation.** §2.1 and §2.4 produce similar z-scaling but different angular signatures (§2.1 has a bifurcation-preferred direction; §2.4 doesn't). §2.5 and §2.6 produce similar angular signatures (both inherit from manifold structure) — they should predict the *same* preferred direction if both are real, which is a self-consistency test. §2.2 is uniquely scale-driven rather than z-driven. §2.3 is uniquely survey-selection-sensitive in the radio-vs-IR axis.

**Discrimination strategy.**

1. **Phase I.** Characterise the existing CatWISE / Singal-Quaia / Wagenveld overshoot pattern across z-bin, angular structure, and survey-selection axis. This is data work, not theory. Cursor + Jammer.
2. **Phase II.** Compare against the table. Identify which 2–3 candidates the pattern best fits.
3. **Phase III.** Develop the top candidates theoretically to v0.1 prediction. Lead streams per §2 subsections.
4. **Phase IV.** Test v0.1 predictions against v0.4 + v0.5 numerical data. Convergence or further iteration.

---

## §4 — Sprint phase plan

### Phase I — Pattern characterisation (Cursor + Jammer, 1–2 sessions each)

**Deliverables.** A signature-characterisation note for the existing three-dataset pattern, organised along the four discrimination axes (z, scale, angle, survey-selection). Doesn't develop any candidate; just maps the pattern.

**Owners.** Cursor (numerical extraction from existing data); Jammer (analytical formalisation of the pattern).

**Output target.** `Working/Wagenveld_Sprint_Phase_I_Pattern_Characterisation_v0_1.md`.

### Phase II — Candidate top-3 ranking (AC, 1 session, after Phase I)

**Deliverables.** AC review of Phase I against §3 table; ranked list of top 3 candidates to develop theoretically.

**Owners.** AC, light coordination.

**Output target.** Brief handoff identifying top 3 candidates and stream allocation.

### Phase III — Top candidate development (multi-stream, parallel, 3–5 sessions each)

**Deliverables.** v0.1 theoretical predictions for each top candidate, including z-scaling, angular pattern, scale dependence (whichever applies), and survey-specific dipole-magnitude predictions for CatWISE / Singal-Quaia / Wagenveld.

**Owners.** Per §2 subsection lead-stream assignments.

**Output target.** One Working/ note per candidate, suffix `Wagenveld_Sprint_Candidate_[N]_*`.

### Phase IV — Convergence test (Cursor + Jammer + AC, 1–2 sessions)

**Deliverables.** Quantitative comparison of each candidate's v0.1 predictions against the Cursor v0.4 (and v0.5 if shipped by sprint end) numerical Branch I results. Identify which candidate(s) best fit; what residuals remain; what the integrated NTE-resolved cosmic-dipole-anomaly picture looks like.

**Owners.** Cursor + Jammer numerical; AC integration.

**Output target.** `Working/Wagenveld_Sprint_Phase_IV_Convergence_Test_v0_1.md` and, if the sprint succeeds, a draft paper outline for a standalone "Cosmic Dipole Anomaly Resolved by NTE" Tier 1 candidate.

### Phase V (contingent) — Tier 1 standalone paper

**Deliverable contingent on sprint success.** If a candidate (or coherent combination of candidates) cleanly resolves the cosmic dipole anomaly, the sprint output becomes a fifth Tier 1 standalone paper for the joint preprint bundle.

**Owners.** TBD; Jammer or Scratch likely as lead.

**Decision point.** End of Phase IV.

---

## §5 — Stream allocation summary

| Stream | Phase I | Phase II | Phase III | Phase IV |
|--------|---------|----------|-----------|----------|
| **AC** | Coordination | **Lead** (top-3 selection) | Integration support | Integration |
| **Cursor** | **Lead** (numerical) | Support | Per-candidate numerical predictions | **Lead** (convergence) |
| **Jammer** | Support | Support | **Lead on §2.3, §2.4, §2.6, §2.7** | Numerical + analytical |
| **Scratch** | None | Adversarial review | **Lead on §2.2, §2.5** + adversarial review | Adversarial review |
| **PC** | None | None | None | None (unless Phase V activates) |

**Activation requirement.** Greg activates Jammer and Scratch for this sprint. Cursor is already active per autonomous mode but needs explicit signal that the Wagenveld sprint takes precedence over the consolidated-batch-handoff items (corpus patches, S6 promotion, External Empirical Surface companion, pedagogical pivots).

---

## §6 — Honest-scope envelope

**Bindings on the sprint (Greg-ratifiable at Phase I):**

- v0.1 predictions are predictions, not derivations to publication-ready rigor. The honest scope is "this candidate predicts ~X with uncertainty bounds Y; consistent with Wagenveld pattern at level Z" — not "this candidate is proven to explain the cosmic dipole anomaly."
- Multiple candidates may partially explain the pattern. The right outcome may be a coherent combination rather than a single winner; that's allowed and worth surfacing.
- If Phase III predictions don't survive Phase IV convergence test, the sprint outcome is "we've eliminated candidates X, Y, Z; remaining candidates require deeper investigation." That's a legitimate sprint result, not failure.
- The cosmic dipole anomaly is a hard, long-standing problem. We don't get to claim resolution easily. The sprint's outcome bar is "produced testable predictions across the candidate space"; "fully resolved the anomaly" is a higher bar that requires post-sprint adversarial review and external scrutiny.

**Bindings on this scoping document:**

- AC has not derived any of the candidate mechanisms in this scoping note. The mechanisms are sketched architecturally; their formal development belongs to the lead-stream owners in Phase III.
- §3's signature-discrimination table is AC's architectural read, not a Jammer/Scratch/Cursor-vetted prediction set. Phase II would adversarially review this table before committing to candidate development.

---

## §7 — Cross-references

**Existing corpus territory each candidate touches:**

- §2.1 Gauge-birth seed: Ch 10 v4 (PC, 2026-05-29), §22.14 (mirror metaphor → bilateral structure)
- §2.2 State-space leakage: Companion 5 (state-space surface), Companion 9 (V_NTE Stage 3 cross-coupling)
- §2.3 Φ_NTE rest-frame: Jammer standing queue (Branch III), Chapter 9, Companion 5
- §2.4 Cross-thickness z-dep: Companion 5, Chapter 9, V_NTE bulk-boundary work
- §2.5 Anisotropic κ on S³: Paper_Kappa_AB v10.17.2, Companion 7, Paper S6 v1.0 (M_R heat-kernel theorem-grade)
- §2.6 Anisotropic Φ_NTE: Companion 8 V_NTE Trajectory, §22.16 local Lagrange-multiplier action principle
- §2.7 Non-perturbative δ₂: Jammer δ₂ non-FLRW work (2026-05-27)

**Branch I work currently in flight:**

- Cursor v0.4 increment (`Handoff_Cursor_to_Jammer_BranchI_v0_4_Increment_20260528.md`)
- 8-R-gates initial assessment (Cursor 13:40Z 27th)
- Jammer CMB κ analytical v0.1 (ratified 2026-05-28, gates 1–5, 7)

**Sprint-related Greg directives in record:**

- Wagenveld trigger condition (consolidated batch handoff §1 #6 today)
- Epistemic principle on dataset disagreements (consolidated batch handoff §1 #6)
- Sprint authorisation 2026-05-28 ("stop the grind and have a sprint")

---

## §8 — Closing

This document is the foundation for the Wagenveld sprint. Phase I activation requires:

1. **Greg ratification of this scoping document** (or revisions if anything reads wrong).
2. **Greg activation of Jammer and Scratch** for sprint participation.
3. **Cursor priority shift** — pause non-sprint items (corpus patches, S6 promotion, External Empirical Surface, pedagogical pivots) in favour of Phase I numerical extraction.
4. **Optional: pre-emptive Phase I kickoff handoff** from AC to Cursor + Jammer with the §3 table and Phase I deliverable target.

AC remains in coordination role through Phase II; light involvement Phase III; integration role Phase IV.

— AC, 2026-05-28. Wagenveld sprint architectural scoping v0.1 ready for Greg ratification and stream activation.
