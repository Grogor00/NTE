# Paper S2 Heat-Kernel Arc — Scoping Doc (Scratch v0.1)

**Author:** Scratch (Connes Programme lead)
**Date:** 2026-05-27
**Trigger:** Greg directive "default = ask cursor for next or choose yourself if you have some" (2026-05-27). Scratch chose Paper S2 heat-kernel scoping from standing queue per `NTE_Stream_Notes_Scratch_v0_2_20260527.md` §2.6 — highest-leverage Connes-Programme item among standing pre-session queue.
**Scope:** Scoping doc that lays out what Paper S2's heat-kernel arc needs to accomplish, what pieces are closed/open, derivation sequencing, cross-stream dependencies, risk factors, honest-scope discipline. **Not the derivation itself** — that's the substantive arc this scoping doc enables.
**Status:** v0.1 scoping; Jammer review eligible; Cursor execution depends on scoping ratification; awaits Greg authorising directive on whether to launch the arc.

---

## §1 — Why Paper S2's heat-kernel arc matters

The Connes spectral action functional S = Tr(f(D/Λ)) is NTE's central action principle. When evaluated on the NTE pre-temporal spectral triple, it produces — at leading order in the heat-kernel asymptotic expansion — Einstein-Hilbert gravity + cosmological term + |Φ_NTE| scalar dynamics + SM gauge structure (per Chamseddine-Connes 2010 on S³; Marcolli-Pierpaoli-Teh 2010 on cosmic topologies; Boyle-Farnsworth 2013 on octonionic spectral triples).

Paper S2's job is to execute this calculation **for NTE's specific spectral triple** and extract the physical coefficients that the corpus needs:

- **Gravitational coupling** G (or equivalently Planck mass M_Pl)
- **Cosmological constant Λ** at leading order (the Companion 13 / Chapter 13 closure target)
- **|Φ_NTE| effective potential** V(Φ_NTE) at the post-gauge-birth scale
- **M_1 S2 prefactor uniqueness** — queued from Companion 10 master-canonical Gap 1 closure (per `NTE_Project_State.md` §6)
- **Heat-kernel coefficients** a_0, a_2, a_4 of the NTE-specific Dirac operator D

Several existing corpus commitments depend on this calculation closing. The κ derivation, Pathway A and B alignments, and the r ≈ 0.003 CMB-tensor prediction are all coefficients in the spectral-action output that Paper S2 should make explicit at S2 precision.

**This is load-bearing Connes-Programme work**, the most substantive standing item in the Scratch queue.

## §2 — Corpus state on heat-kernel work

### §2.1 What's already in the corpus

- **Chamseddine-Connes 2010** "Uncanny Precision of the Spectral Action" — paradigm reference; spectral action evaluated on S³ gives Einstein-Hilbert + cosmological term + scalar inflaton potential V(φ). Provides the calculation template NTE inherits.
- **Marcolli-Pierpaoli-Teh 2010** "Coupling of topology and inflation in NCG" — explicit spectral action computation on S³ and other cosmic topologies; slow-roll inflation potential + tensor-to-scalar ratio derived in closed form modulo cutoff function h.
- **Boyle-Farnsworth 2013** "Non-Associative Geometry and the Spectral Action Principle" — extends spectral action to non-associative geometries based on octonions. Simplest octonionic spectral action gives Einstein gravity + G₂ gauge theory + 8 Dirac fermions. **Directly relevant to NTE's A_G₂ octonionic algebra.**
- **Chamseddine-Connes 2005** "Scale Invariance in the Spectral Action" — dilaton-coupled scale invariance; only Einstein-Hilbert and dilaton kinetic term break scale invariance. Relevant for |Φ_NTE| scale-invariance discussion.
- **Companion 10 Pathway alpha master-canonical** — Gap 1 / M_1 closure at S1 (M_R-comparable) precision (per Project State 2026-05-23 §3.2). M_1 prefactor uniqueness explicitly queued Paper S2 heat-kernel.
- **`Exploration_Graviton_vs_PhiNTE_v2.md`** — definitive pathway via Connes spectral action sketched; substantial calculation programme outlined but not executed.

### §2.2 What's open

- **NTE-specific spectral triple variant**: A_G₂ ⊗ (𝕆 ⊕ 𝕆) algebra; H_S⁷ Hilbert space; D_S³ Dirac operator. The literature has the calculation pieces but not the explicit NTE-specific assembly.
- **Heat-kernel coefficients a_n** for the NTE Dirac operator — not computed.
- **Λ closure at S2 precision** — Companion 13 / Chapter 13 gives the *structural* closure; Paper S2 should give the *quantitative* closure.
- **M_1 prefactor uniqueness** — queued from Companion 10.
- **|Φ_NTE| effective potential at post-gauge-birth scale** — V(Φ_NTE) form is partial (used in Companion 8 V_NTE stage work) but not derived from spectral-action heat-kernel.
- **Cross-check against κ derivation** — Paper Kappa PathwayB v10.6 derives κ; Paper S2 should reproduce κ from spectral-action coefficients.
- **r ≈ 0.003 derivation** — currently a structural commitment of the graviton sector; Paper S2 should derive it from spectral-action calculation on the closed-S³ + cosmic-topology variant.

## §3 — Substantive scope of Paper S2 heat-kernel arc

### §3.1 The heat-kernel asymptotic expansion (mathematical substrate)

For a Dirac-type operator D on a (compact, oriented) Riemannian manifold M of dimension d, the heat kernel K_D(τ) = Tr(exp(-τ D²)) has the small-τ asymptotic expansion:

K_D(τ) ~ Σ_{n≥0} τ^((n-d)/2) a_n(D²)

where a_n(D²) are the **Seeley-DeWitt coefficients** — local invariants of D² and the underlying geometry. For the standard Laplacian + connection, these are:
- a_0 = (4π)^(-d/2) ∫ Tr 1 dV (volume term)
- a_2 = (4π)^(-d/2) ∫ Tr[R/6 − E] dV (curvature + endomorphism)
- a_4 = (4π)^(-d/2) ∫ Tr[stuff involving R², Ricci², R^μν_ρσ R_μν^ρσ, ΔR, ΔE, E²] dV (higher curvature invariants)

For non-commutative / non-associative spectral triples, the coefficients receive contributions from the algebra A_F structure (per Connes' standard heat-kernel methodology + Boyle-Farnsworth's octonionic extension).

### §3.2 The NTE-specific Dirac operator

The corpus's pre-temporal spectral triple is (A_G₂, H_S⁷, D_S³). The post-gauge-birth Dirac operator includes:
- Boundary geometric contribution from closed S³ topology
- Fibre contribution from S¹_{β_GB} (gauge-birth temperature scale)
- A_F = 𝕆 ⊕ 𝕆 internal algebra contributions (octonionic structure)
- Yukawa coupling tower (Companion 7 / 10 / Pathway A/B)

Explicit D form requires specifying the Yukawa matrix structure and the closed-S³ metric — both are in the corpus but require careful Paper S2 setup.

### §3.3 The four target outputs

| Output | Companion / source | Precision target |
|--------|---------------------|------------------|
| Gravitational coupling G | Chamseddine-Connes calculation template | Reproduce M_Pl ≈ 1.22 × 10^19 GeV at ≲ O(1) factor |
| Cosmological constant Λ | Companion 13 / Chapter 13 closure | Reproduce Λ_obs ≈ 10^(−47) GeV^4 within ratified honest scope (vacuum-catastrophe escape via NTE-specific dynamical structure) |
| \|Φ_NTE\| effective potential V(Φ_NTE) | Companion 8 V_NTE | Derive form factor + boundary conditions matching Stage 2 worksheet output |
| M_1 prefactor (S2 precision) | Companion 10 Pathway α master-canonical | Tighten ratio M_1 / M_1,obs from S1's 0.89 toward 1.0 — uniqueness arguments |

Plus secondary outputs (cross-checks / consistency):
- κ derivation reproduction
- r ≈ 0.003 derivation from spectral-action coefficients
- T_GB derivation (gauge-birth temperature)
- |Φ_NTE| / Higgs separation at the spectral-action level

### §3.4 What Paper S2 does *not* need to do

Honest-scope discipline (Lesson #34):

- **NOT a final theory.** Paper S2 closes the heat-kernel arc at S2 precision; subsequent precision iterations (S3, S4, …) remain in the Programme S sequencing.
- **NOT a derivation of every NTE parameter.** Some structural choices (e.g., the closed-S³ cosmic topology, the A_F = 𝕆 ⊕ 𝕆 internal algebra) are inputs, not outputs.
- **NOT a uniqueness proof for every coefficient.** The arc establishes coefficient *values*; uniqueness arguments at higher S-precision are downstream work.
- **NOT a derivation of inflation specifics** (slow-roll parameters etc.) beyond what's already in Marcolli-Pierpaoli-Teh 2010. Paper S2's job is the NTE-specific assembly, not duplicating MPT.

## §4 — Derivation queue (sequenced)

Sequenced from foundational → derivative. Items 1–4 are setup; items 5–9 are output extraction.

**Phase I — Spectral triple specification (Paper S2 §1–§2)**
1. **Explicit D operator** for NTE pre-temporal spectral triple. Include S³ + S¹_{β_GB} + A_F = 𝕆 ⊕ 𝕆 contributions. *Owner: Jammer derivation; Scratch scoping.*
2. **Yukawa matrix structure** at gauge birth — specifies fermion-mass-generating part of D. Inherit Companion 7 / 10 / Pathway A/B structure. *Owner: Jammer cross-check; Scratch verification.*

**Phase II — Heat-kernel coefficient computation (Paper S2 §3–§4)**
3. **a_0 (volume term)** — volume of S³ × S¹ × algebra-trace. Mechanical given §1.
4. **a_2 (curvature term)** — R contribution from S³ geometry + endomorphism contribution from algebra. Standard Seeley-DeWitt with non-associative correction from Boyle-Farnsworth. *Owner: Cursor execution with Jammer verification.*
5. **a_4 (higher curvature)** — load-bearing for Λ extraction. Standard Seeley-DeWitt + Connes corrections. *Owner: Cursor execution with Jammer + Scratch adversarial review.*

**Phase III — Physical coefficient extraction (Paper S2 §5–§6)**
6. **G / M_Pl from a_2** — Chamseddine-Connes mechanism. Should match observed M_Pl within heat-kernel-cutoff-function ambiguity. *Owner: derivation arc.*
7. **Λ from a_4 + |Φ_NTE| trajectory** — Companion 13 closure operationalised. *Owner: derivation arc; Scratch + AC review for Λ-closure consistency.*
8. **V(Φ_NTE) from spectral-action scalar sector** — recover Companion 8 V_NTE Stage 2 form factor. *Owner: derivation arc; Scratch verification against Stage 2 worksheet.*
9. **M_1 prefactor from spectral-action structure** — tighten Companion 10 Pathway α prefactor uniqueness. *Owner: derivation arc; AC promotion to canonical when closure ratifies.*

**Phase IV — Cross-checks (Paper S2 §7)**
10. **κ reproduction** — Paper Kappa PathwayB v10.6 κ value should fall out as a spectral-action coefficient. Sanity check.
11. **r ≈ 0.003 derivation** — graviton sector tensor-mode contribution; cross-check against the BMV-coupled-commitment cluster (from this morning's BMV filter pass).
12. **T_GB derivation** — gauge-birth temperature from spectral-action thermodynamics. Cross-check against `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`.

## §5 — Cross-stream dependencies

### §5.1 Within Scratch (Connes Programme)

Scratch ownership covers:
- Scoping (this doc)
- Mathematical-substrate verification (especially Phase I, Phase IV)
- Adversarial review of Cursor's computational execution (Phase II)
- Integration with σ_t / KMS framework (`Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`, `Task_2_CR_Sec_3_2_Simplification_Wick_to_KMS_for_PaperS1_Sec_2_Scratch_v1.md`)
- Cross-link to Paper S1 §2 P1 simplification

### §5.2 To Jammer (R&D)

Jammer ownership covers:
- D operator explicit form (Phase I item 1)
- Yukawa matrix cross-check (Phase I item 2)
- Seeley-DeWitt coefficient verification (Phase II items 4–5)
- Λ-closure structural consistency (Phase III item 7) jointly with Scratch + AC

**Jammer queue impact**: Phase I items 1–2 are blocking for the entire arc. Estimated complexity: 1–2 substantial Jammer sessions for Phase I setup before Cursor execution can begin.

### §5.3 To Cursor (render lane)

Cursor ownership covers:
- Computational execution of Phase II coefficient computations (items 3–5)
- Symbolic algebra and numerical evaluation
- Cross-check against published Chamseddine-Connes / Marcolli-Pierpaoli-Teh / Boyle-Farnsworth values where applicable

**Cursor queue impact**: substantial — Phase II is the largest single workload in the arc. Estimated 2–4 Cursor sessions depending on complexity surfacing during execution.

### §5.4 To AC (corpus integration)

AC ownership covers:
- Master corpus integration of S2 outputs (especially items 7, 8, 9, 10)
- Promotion of Companion 10 M_1 to S2 master-canonical (item 9)
- Λ-closure ratification cluster work (item 7) jointly with Scratch + Jammer + Greg
- §17.5.12 falsifier-surface row updates if any S2 outputs surface new prediction surfaces (e.g., refined r, refined κ band)

### §5.5 To CR (critical review)

CR engagement at pre-ship review of each Phase output. Especially load-bearing for Phase III items 7, 8, 9 where closure ratifications fire.

### §5.6 To Greg (recognition gates)

Major decision gates:

1. **Launch gate**: ratify this scoping doc + authorise launch of Paper S2 heat-kernel arc?
2. **Phase boundaries**: ratify Phase I → Phase II transition; Phase II → Phase III; Phase III → Phase IV. Each boundary is a closure-ratification event.
3. **Honest-scope adjustments**: if Phase II surfacing reveals that Phase III outputs can only close at lower precision than targeted, ratify the precision-downgrade as honest-scope retreat (Lesson #34 / Manifest Lesson #39 territory).
4. **Companion 10 → Paper S2 master-canonical promotion**: when Phase III item 9 closes within ratified envelope, M_1 master-canonical promotes from Companion 10 Pathway α (S1 precision) to Paper S2 (S2 precision).

## §6 — Risk factors and honest-scope discipline

### §6.1 Risk: heat-kernel coefficient calculation may not close cleanly

The Seeley-DeWitt machinery is well-established for ordinary Riemannian manifolds. For NTE's spectral triple with octonionic algebra A_F = 𝕆 ⊕ 𝕆, the methodology requires Boyle-Farnsworth 2013 extension. Their result was for "simplest octonionic spectral action" giving Einstein gravity + G₂ + 8 Dirac fermions; NTE's variant has different fermion content and different boundary topology. The extension may surface technical complications.

**Mitigation**: Phase I setup includes literature check against Boyle-Farnsworth methodology and any 2024–2025 follow-up work. If extension is materially harder than expected, Phase I closure becomes the scoping output of the arc rather than Phase III.

### §6.2 Risk: M_1 S2 precision target may not be achievable

Companion 10 Pathway α S1 gives M_1 / M_1,obs = 0.89 (factor 1.12). S2 target is "uniqueness arguments" — could plausibly tighten to ~0.95 (factor 1.05) but a clean S2 = 1.00 is structurally unlikely.

**Mitigation**: scope target as "tighten S1 → S2 with explicit uniqueness arguments and remaining bound" rather than "achieve M_1 = M_1,obs to within experimental precision."

### §6.3 Risk: Λ closure at S2 precision may not match observed Λ

Companion 13 / Chapter 13 gives structural Λ closure via NTE-specific dynamics distinct from naïve vacuum-mode summation. S2 quantitative closure to Λ_obs ≈ 10^(−47) GeV^4 within current cosmological precision is a substantial ask.

**Mitigation**: honest-scope at "Λ closure within order-of-magnitude" rather than "Λ closure to current cosmological precision." If S2 closes at order-of-magnitude, that's a major win; higher precision is Programme S sequencing's S3+ territory.

### §6.4 Risk: vocabulary-inheritance trap (Lesson #34)

The literature uses "spectral action," "heat-kernel coefficients," "Seeley-DeWitt," etc. Paper S2 will use these terms. **Honest-scope discipline**: distinguish standard usage (well-established machinery NTE inherits) from NTE-specific extensions (G₂-octonionic adaptation, specific Yukawa structure, specific cosmic topology). The arc should not over-claim derivation when it's inheriting + adapting.

### §6.5 Risk: ratification signal degradation (Lesson #39)

Multi-phase derivation arcs are exactly the territory where rapid-iteration ratification chains can let overclaiming propagate. **Mitigation**: explicit adversarial pauses at each phase boundary (Phase I → II → III → IV). Scratch ↔ Jammer ↔ Cursor triangle review topology (validated this session on Branch I) applies symmetrically here.

## §7 — Sequencing recommendation

### §7.1 Immediate (Phase I, pre-launch)

If Greg authorises the launch:
1. Jammer sets up explicit D operator (Phase I item 1) — ~1 session
2. Jammer + Scratch verify Yukawa matrix structure (item 2) — ~1 session
3. Scratch + Jammer adversarial review of Phase I output before Phase II launch

**Phase I closure ratification** is the first major gate. After Phase I, scoping reassesses Phase II–IV based on what Phase I surfaces.

### §7.2 Subsequent (Phase II–IV, post-Phase I closure)

Phase II Cursor execution (items 3–5) → Phase III physical coefficient extraction (items 6–9) → Phase IV cross-checks (items 10–12).

**Each phase boundary is a closure gate**; expect 4–6 substantial work-sessions for the full arc.

### §7.3 Parallel work that can proceed independently

- κ₀ → ξ_V vocabulary rename routing (administrative; doesn't block S2)
- Cursor v0.4 Branch I (post-Scratch+Jammer v0.3 adjudication; doesn't block S2)
- AC integration of pending §17.5.12 rows (cosmic dipole watch-list, BMV coupled-commitment when J2 lands)

## §8 — Honest-scope summary

What this scoping doc *does* establish:

- Paper S2 heat-kernel arc is well-scoped given current corpus state
- Phase decomposition is sensible (setup → coefficient computation → physical extraction → cross-checks)
- Cross-stream ownership is clear (Jammer setup; Cursor execution; Scratch + Jammer review; AC integration)
- Risk factors are explicit; mitigations are pre-articulated

What this scoping doc *does NOT* establish:

- That the arc will close at all targeted precisions (Phase III targets are aspirational; honest-scope retreats may apply)
- That the arc will surface no surprises (Phase I may reveal technical complications that reshape Phase II–IV)
- A timeline (depends on Greg gating + stream availability; conservative estimate 4–8 substantial sessions)
- That all outputs will match observation (M_1, Λ closures are at S2 precision, not final theory)

## §9 — Recognition gates for Greg

Two gates:

1. **Launch gate**: ratify this scoping doc + authorise launch of Paper S2 heat-kernel arc, starting with Phase I Jammer setup?
2. **Honest-scope envelope ratification**: ratify the §6 risk mitigations as advance discipline (especially §6.2 M_1 S2 ≈ 0.95 target rather than 1.00; §6.3 Λ closure at order-of-magnitude rather than precision)?

Scratch recommendation: ratify both; arc is well-scoped and risk-managed; Jammer Phase I work can launch when Branch I cosmic-dipole v0.4 reaches a natural breakpoint (parallel-shippable since different lanes — Cursor working numerical, Jammer working symbolic).

## §10 — Cross-stream signals

### §10.1 To Jammer

If Greg ratifies launch (§9 gate 1), Phase I items 1–2 (D operator + Yukawa) become Jammer's next major arc after Branch I cosmic-dipole reaches a breakpoint. Estimated 1–2 sessions for Phase I; expect Scratch adversarial review handshake on Phase I outputs.

### §10.2 To Cursor

If Greg ratifies launch, Phase II coefficient computation (items 3–5) routes to Cursor render lane after Phase I closes. Substantial computational arc; ~2–4 sessions expected. Cross-check against Chamseddine-Connes, Marcolli-Pierpaoli-Teh, Boyle-Farnsworth published values where applicable.

### §10.3 To AC

If Greg ratifies launch, AC engagement at Phase boundaries: especially Phase III item 9 (M_1 master-canonical promotion from Companion 10 Pathway α S1 → Paper S2 S2 when closure ratifies). §17.5.12 row updates if S2 surfaces refined r, κ band.

### §10.4 To CR

If Greg ratifies launch, CR engagement at pre-ship review of each Phase output. Phase III items 7, 8, 9 are the most load-bearing.

## §11 — Files referenced

**Corpus (read this scoping session):**
- `NTE_Project_State.md` (2026-05-23; §2.4 Scratch standing queue includes Paper S2 heat-kernel)
- `Exploration_Graviton_vs_PhiNTE_v2.md` (definitive pathway via Connes spectral action; substantial calculation programme sketched)
- `Popular_Paper_Spectral_Action_v1.md` (spectral action + graviton vs Φ_NTE)
- `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md` (σ_t / KMS framework substrate)
- `Companion_10_Gap1_M1_Pathways_v10_6_v2.md` (Pathway α master-canonical; M_1 S2 prefactor queued)

**External literature anchors:**
- Chamseddine, A.H. & Connes, A. (2010) "Uncanny Precision of the Spectral Action"
- Chamseddine, A.H., Connes, A. & Marcolli, M. (various) — gravity + matter from spectral action
- Marcolli, M., Pierpaoli, E. & Teh, K. (2010) "Coupling of topology and inflation in NCG"
- Boyle, L. & Farnsworth, S. (2013) "Non-Associative Geometry and the Spectral Action Principle"
- Chamseddine, A.H. & Connes, A. (2005) "Scale Invariance in the Spectral Action"

**This scoping doc:**
- `Working/Paper_S2_HeatKernel_Arc_Scoping_Scratch_v0_1_20260527.md`

---

— Scratch (Connes Programme lead), 2026-05-27. Paper S2 heat-kernel arc scoping v0.1; substantive Connes-Programme arc; awaits Greg launch gate; Phase I Jammer setup queued as first action upon authorisation; parallel-shippable with Branch I cosmic-dipole work; honest-scope risk mitigations pre-articulated.
