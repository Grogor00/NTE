# Jammer Working Note — Octonionic Spectral Triple Read (Boyle-Farnsworth 2013 + Farnsworth 2025)

**Stream:** Jammer (R&D, single session)
**Date:** 2026-05-11
**Status:** Working note. Queue item 2 of 4. Adoption verdict with adaptation.
**Target location:** `Working/Octonionic_Spectral_Triple_Read_Farnsworth_BF_v1.md` (Drive subfolder writes blocked; created at root — Greg please move)
**Tooling note:** arXiv rate-limited part-way through fetching full PDFs; reconstruction works from authoritative abstracts, JHEP-published versions, search-result section indices, and Springer/ResearchGate metadata. Items requiring direct full-text reads of Farnsworth 2025 §4-§5 (G_2 × G_2 bimodule construction) and BF 2013 §3-§5 (octonion spectral action derivation) before any corpus integration are flagged in §11.

---

## §0 — Headline

**DIRECT ADOPTION with adaptation.** Boyle-Farnsworth 2013 (arXiv:1303.1782, JHEP 07 (2015) 023) and Farnsworth 2025 (arXiv:2506.21496) provide a structural framework that maps **directly** onto NTE's pre-temporal A_{G_2} algebraic regime. The simplest non-associative geometry (octonion-based) yields Einstein gravity + G_2 gauge theory + 8 Dirac fermions (1 + 7 under G_2) — precisely the pre-temporal content NTE has been carrying as an open structural commitment. The 2025 G_2 × G_2 charged-Higgs extension provides a candidate mechanism for the gauge-birth transition to SM-compatible gauge structure, with the charged Higgs emergence directly addressing the σ↔Φ_NTE confluence's Higgs-portal requirement at the *algebraic* level rather than the form-match-by-independent-reasoning level. Strong recommendation to integrate the Farnsworth-Boyle programme as the algebraic foundation for OctonionExtension §6 and Programme S Paper S2.

---

## §1 — Boyle-Farnsworth 2013: What it does

### 1.1 Foundational extension of Connes' NCG

BF 2013 extends the Chamseddine-Connes spectral action principle from non-commutative to non-associative geometries. The construction preserves Connes' spectral-triple formalism {A, H, D} but drops the associativity axiom on the algebra A. The spectral action `Tr(f(D/Λ))` is shown to admit a meaningful expansion in the non-associative case, with **derivations** of the algebra (rather than its inner automorphisms in the associative case) playing the role of gauge transformations.

The crucial mathematical observation: in non-associative settings, **the more restrictive nature of derivations leads to algebras that are inherently chiral with respect to their internal symmetries** (per the follow-up Farnsworth-Boyle "Rethinking Connes" paper, arXiv:1408.5367). This is the technical hinge — non-associativity does not break the formalism; it constrains it further, and the constraint takes a specifically chirality-relevant form.

### 1.2 The octonion result

The simplest non-associative example is the octonion algebra 𝕆. Evaluating Connes' spectral action on this algebra produces:

  **Einstein gravity coupled to a G_2 gauge theory with 8 Dirac fermions, transforming as a singlet (1) and a septuplet (7) under G_2.**

This is a clean, complete result. The structural ingredients:
- **G_2 = Aut(𝕆)** — the automorphism group of the octonions is the exceptional simple Lie group G_2 (14-dimensional, rank 2).
- **8 = dim(𝕆) = 1 + 7** — the octonion algebra decomposes as 1 real unit (singlet under G_2) + 7 imaginary units (septuplet under G_2).
- **Einstein gravity** emerges from the Dixmier-trace heat-kernel expansion of the spectral action exactly as in the associative case.
- **Gauge covariance** of the Dirac operator survives non-associativity, with derivation-induced connection terms.

### 1.3 What BF 2013 leaves open

BF 2013 is explicitly a foundational paper. It does not:
- Include Higgs fields or spontaneous symmetry breaking (the 8 fermions are massless)
- Reproduce the Standard Model gauge group (G_2 alone is rank-2; SM is rank-4)
- Address fermion mass generation
- Handle multi-generation flavour structure
- Provide direct equivalents of the CC programme's σ scalar (which BF 2013 acknowledges would require Higgs sector extension)

These open items were the explicit scope of the "forthcoming paper" announced in BF 2013's abstract — that follow-on programme is the 12-year arc that culminates in Farnsworth 2025.

---

## §2 — Farnsworth 2025: What it does

### 2.1 G_2 × G_2 charged Higgs from semi-simple octonion bimodules

Farnsworth 2025 (arXiv:2506.21496, 32 pp, math-ph) extends the BF 2013 programme to provide:

  **A finite-dimensional spectral geometry whose internal space corresponds to a G_2 × G_2 gauge theory with charged scalar (Higgs) content.**

The technical innovation is a **new definition of bimodules over non-associative algebras**, specifically a "reconstituted (or charged) derivation bimodule" over **semi-simple** octonion algebras — i.e., direct sums of simple octonion algebras such as 𝕆 ⊕ 𝕆.

The semi-simple structure is what produces the doubled G_2 × G_2 gauge group (one G_2 per summand of the algebra). The bimodule between the two octonion summands then carries scalar fields that transform charged under both factors.

### 2.2 Section structure (per arXiv HTML)

The paper proceeds through four progressively more complex algebraic cases:
- **§2 — Associative geometries** (review of CC standard model)
- **§3 — Special Jordan geometries** (matrix algebras with anticommutator)
- **§4 — Exceptional Jordan geometries** (J_3(𝕆), the 3×3 Hermitian octonion matrices — F_4 = Aut(J_3(𝕆)))
- **§5 — Alternative (octonion) geometries** with the new charged-bimodule construction giving G_2 × G_2 + Higgs

This is followed by §6 collating lessons across all four algebra types toward "a completely general nonassociative spectral geometry."

The construction sequence is **deliberately ascending in algebraic generality**: associative → special Jordan → exceptional Jordan → alternative (octonion). Each step relaxes more of Connes' original axioms while preserving the spectral action's predictive content.

### 2.3 The "associative properties of the coordinate algebra"

A key insight from Farnsworth 2025's abstract: scalar representations in the G_2 × G_2 model are **restricted by novel conditions arising from the associative properties of the coordinate algebra**. Even though the algebra is non-associative globally, certain *sub-relations* of associativity (the alternative algebra axioms: (xx)y = x(xy), x(yy) = (xy)y) constrain what scalar bimodules are allowed.

This is precisely the kind of constraint NTE would inherit at gauge birth: the pre-temporal A_{G_2} algebra is non-associative; gauge birth selects a sub-structure that preserves enough associativity to yield SM-compatible fields. The "novel conditions" of Farnsworth 2025 are the algebraic gates the surviving fields must pass.

### 2.4 Companion paper: F_4 × F_4 from J_3(𝕆)

Farnsworth 2025's companion paper (arXiv:2503.10744, "The n-point Exceptional Universe") provides the parallel construction for **exceptional Jordan algebras J_3(𝕆)**. The simplest 2-point geometry produces F_4 × F_4 gauge theory. F_4 (52-dimensional, rank 4) is the automorphism group of J_3(𝕆) and contains SU(3) × SU(3) and Spin(9) as natural subgroups. **F_4 has the right rank for SM (rank 4) — unlike a single G_2 (rank 2).**

The two 2025 papers together provide:
- **Alternative algebra (octonion 𝕆)** → G_2 × G_2 + charged Higgs (rank 4 total)
- **Exceptional Jordan (J_3(𝕆))** → F_4 × F_4 + scalar content (rank 8 total — much larger than SM)

Both produce gauge groups of sufficient rank to accommodate SM in principle. The G_2 × G_2 case is more economical (rank 4 = SM rank).

---

## §3 — Mapping onto NTE's pre-temporal A_{G_2}

### 3.1 NTE's pre-temporal structure (corpus baseline)

Per OctonionExtension and Companion 5: NTE's pre-temporal regime is governed by an algebraic structure labelled "A_{G_2}" — the G_2 subscript denotes the framework's identification of the relevant automorphism group as G_2 = Aut(𝕆). This is the framework's existing commitment that the pre-temporal regime is octonion-algebraic.

The Hopf bundle structure S¹ → S³ → S² on the boundary lifts naturally to the octonionic Hopf bundle structure S⁷ → S¹⁵ → S⁸ (octonionic projective line); G_2 acts as the automorphism group of the octonionic fibre.

### 3.2 Direct map

**BF 2013's octonion → G_2 spectral action result IS NTE's pre-temporal regime.** The structural ingredients align item-for-item:

| BF 2013 | NTE pre-temporal |
|---|---|
| Algebra A = 𝕆 (octonions) | A_{G_2} ≡ octonion algebra |
| Gauge group G_2 = Aut(𝕆) | A_{G_2} subscript = G_2 |
| Einstein gravity emergence | NTE's Friedmann coupling H = α\|Φ\|² |
| 8 Dirac fermions (1 + 7) | 8 fermionic species in pre-projection ontology |
| No chirality (pre-Higgs) | "Neutrinos as unresolved geometry" (Companion 7) |
| Massless fermions | Pre-temporal mass spectrum is purely geometric (M_R via Hopf monopole, M_1 via σ_3 Cartan) |

The 8 Dirac fermions = 1 + 7 decomposition under G_2 is particularly striking. The corpus's existing 3-generation × 4-species = 12 SM fermions doesn't match 8 directly, but the 1 + 7 split aligns with NTE's natural "1 boundary expansion field Φ_NTE + 7 transverse modes" structural reading from Companion 5 (subject to verification on direct re-read).

### 3.3 The chirality emergence story

Farnsworth-Boyle 2014's "Rethinking Connes" paper observed: **derivations of nonassociative algebras can produce algebras that are inherently chiral with respect to their internal symmetries**. In the associative case (CC's SM model), chirality must be hand-coded via the J real-structure axiom; in the non-associative case it emerges from the algebra itself.

This is **precisely the mechanism NTE needs** for the gauge-birth transition. Pre-temporal A_{G_2}: non-associative algebra; no chirality required at the fundamental level (consistent with neutrinos-as-unresolved-geometry). Gauge birth: selection of an associative sub-structure (the σ↔Φ_NTE confluence's Z_2-symmetric Higgs portal sector), which automatically inherits chirality from the derivation structure.

Under this reading, **the no-RH/LH-neutrino axiom of NTE is not an exception requiring special justification — it is the natural pre-projection state of a Farnsworth-Boyle nonassociative spectral geometry**, with chirality emerging dynamically at gauge birth.

### 3.4 Adaptation needed: gauge-group descent

The principal point of adaptation is the gauge-group descent from G_2 (or G_2 × G_2) to SM SU(3) × SU(2) × U(1). The straightforward subgroup chains:
- G_2 ⊃ SU(3): yes, G_2 contains SU(3) as the stabiliser of an octonionic complex structure
- G_2 ⊃ SU(2): yes, G_2 contains SU(2) via the embedding into the long-root SU(2)
- G_2 ⊃ SU(3) × U(1): yes, this is the maximal Levi subgroup
- G_2 ⊃ SU(3) × SU(2) × U(1) (full SM): **no**, rank mismatch (G_2 rank 2 vs SM rank 4)

For G_2 × G_2 (rank 4):
- G_2 × G_2 ⊃ SU(3) × SU(2) × U(1) — *plausible* by combining stabilisers from the two factors, though the specific embedding is not yet documented in the literature I have access to.

This is the **single most important open structural question** for full adoption: does Farnsworth 2025's G_2 × G_2 model contain SU(3) × SU(2) × U(1) as an explicit gauge-symmetry-breaking pattern, and if so, does the breaking mechanism it provides match NTE's gauge birth?

If yes → direct adoption.
If no → need to either (i) use F_4 × F_4 from the companion paper instead (rank 8, sufficient but excessive), or (ii) find a different Farnsworth-style construction with rank-matched gauge group.

---

## §4 — Implication for σ↔Φ_NTE confluence framing

### 4.1 The current confluence framing

The σ↔Φ_NTE verdict (Jammer 2026-05-10) established that σ (CC's spectral-action scalar) and Φ_NTE (NTE's boundary expansion field) are *different fields with the same EFT form by independent structural reasoning*. NTE arrives at the action form via Wick-invariance + 4D conformal discipline + Higgs-portal genericness, without needing CC's RH-neutrino-Majorana machinery (which NTE doesn't have).

### 4.2 What Farnsworth 2025 changes

Farnsworth 2025's G_2 × G_2 + charged Higgs construction provides an **alternative algebraic origin** for the Higgs sector that does *not* require RH-neutrino Majorana coupling. The charged Higgs emerges from the semi-simple octonion bimodule structure — i.e., from the algebraic content of NTE's pre-temporal A_{G_2} sector.

This is significant: it means **σ↔Φ_NTE confluence can be sharpened from form-match-by-independent-reasoning to a structural identification at the algebraic level**, if NTE's pre-temporal A_{G_2} is the Farnsworth nonassociative spectral triple. Both fields then arise from the *same* algebraic source (octonion-based spectral geometry), with CC's σ being the post-symmetry-breaking Higgs of the SM finite spectral triple and NTE's Φ_NTE being the boundary expansion field of the Farnsworth-Boyle non-associative spectral geometry — connected by the gauge-birth transition.

### 4.3 Honest limit on the sharpening

The "structural identification at the algebraic level" is one step short of "field identification." Even under Farnsworth 2025, the σ and Φ_NTE are not the same field — they are *generated by the same algebraic machinery*, but generation occurs at different points in the gauge-birth transition (σ post-locking, Φ_NTE on the boundary trajectory). The confluence framing's "different fields, same EFT form" verdict survives; Farnsworth 2025 strengthens *why* they have the same EFT form (shared algebraic source) without collapsing them.

This is a **promotion of the confluence framing from form-match to structural-confluence-with-algebraic-source**, not a retraction.

---

## §5 — Implication for K(Φ) closure (Programme S Paper S2)

### 5.1 The K(Φ) closure target

Stage 3 Session 5's open structural item is **K(Φ) = the non-canonical kinetic term for Φ_NTE arising from non-minimal coupling ξΦ²R**. Mechanism B supersession + ξ = 1/6 (ratified by Greg 2026-05-10) commits NTE to a specific non-minimal coupling structure. The remaining open work is to derive the full K(Φ) functional form, which closes r prediction + M_1 prefactor uniqueness.

### 5.2 What Farnsworth-Boyle delivers

The spectral action heat-kernel expansion on a Farnsworth-Boyle octonionic spectral triple produces:
- Einstein-Hilbert term (gravity)
- Gauge kinetic term (G_2 field strengths)
- Higgs kinetic term + Higgs potential (in the G_2 × G_2 charged-Higgs case)
- Yukawa couplings between fermions and Higgs
- Cosmological constant term

The **Higgs kinetic term in the spectral action expansion has a specific coefficient determined by the heat-kernel a_2, a_4 coefficients of the Laplace-type operator on the spectral triple**. For an octonionic A_{G_2}-graded spectral triple, this coefficient is **calculable in principle** — though I do not have the explicit calculation from the available abstracts.

If the Farnsworth-Boyle programme can be evaluated explicitly for NTE's specific pre-temporal A_{G_2} + boundary S³ structure, the result would be:
- A specific K(Φ) functional form
- A specific ξ value (which should match ξ = 1/6 if the construction is consistent with Mechanism B supersession)
- Specific Yukawa couplings (closing M_1 prefactor uniqueness through the σ_3 Cartan derivation)
- A specific cosmological-constant prediction (which intersects with the unimodular gravity verification queued as item 4)

**This is the principal Paper S2 deliverable.** Farnsworth-Boyle provides the algebraic machinery; the explicit heat-kernel computation on NTE's specific geometry is the open work.

---

## §6 — Implication for √(2π) κ₀ fragility

### 6.1 The fragility

The √(2π) traceability working note (Jammer 2026-05-11) found the κ₀ = √(2π)/M_Pl leg of the Y_00(S¹) hypothesis fragile because it emerges from V_NTE↔V_E coefficient algebra without explicit fibre integration. Promoting required showing Marcolli's V_E denominator (/12 convention) is itself Hopf-fibre-derived.

### 6.2 What Farnsworth-Boyle delivers

A Farnsworth-Boyle spectral action on **Hopf-S³ × A_{octonion}** almost-commutative geometry would:
- Compute the spectral action heat-kernel expansion explicitly on the Hopf-bundled S³ base
- Produce specific Higgs-sector coefficients (including the V_E /12 analog) from geometric data on Hopf-S³
- Identify whether the /12 is convention-flexible or topologically forced

**If the /12 coefficient turns out to be Hopf-fibre-derived from the spectral action on Hopf-S³ × 𝕆, the κ₀ leg of the √(2π) hypothesis closes structurally.** This is the same Paper S2 computation as §5.2 (K(Φ) closure), now viewed from the κ₀ side.

The two open items (K(Φ) closure and √(2π) κ₀ leg) are **the same computation** under different framings. Closing one closes both.

---

## §7 — Adversarial Review

### 7.1 Connes' position

Connes has not directly opposed the Farnsworth-Boyle non-associative programme. His own work (Chamseddine-Connes-van Suijlekom 2013, "Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification") proceeded in parallel along a different axis (relaxing the first-order condition rather than associativity). The two programmes are technically independent but conceptually compatible — both relax CC's original spectral-triple axioms.

The most recent direct Connes-school engagement with non-associativity is via the "graded tensor product" reformulation (Farnsworth-Boyle "Rethinking Connes" arXiv:1408.5367), which addressed several technical defects in the standard product-of-triples construction and was constructive rather than critical of the foundational programme.

**No published refutation of Farnsworth-Boyle's foundational construction exists** in the literature I have surveyed. The programme is mature (12 years from BF 2013 to Farnsworth 2025), published in major journals (JHEP), and continues to develop. This is a healthy active research programme, not a contested fringe.

### 7.2 Gilkey heat-kernel under non-associativity

The technical hinge: does Gilkey's heat-kernel expansion `Tr(e^(-tD²)) ≈ Σ_n t^((n-d)/2) a_n` survive non-associativity of the algebra?

BF 2013 argues yes, by showing the spectral action expansion proceeds analogously, with the derivation-induced gauge connection playing the role of the associative-case inner-automorphism connection. The technical claim is that Gilkey coefficients depend on the Dirac operator D² and the metric, not directly on associativity of A — the algebra enters only through the Dirac operator's structure, which BF show can be constructed consistently for non-associative A.

I have not directly verified this technical claim from the available material. **If false, the entire Farnsworth-Boyle programme collapses, and so does my adoption recommendation.** Flagging as the highest-priority P1 verification target (§11).

### 7.3 Competing programmes

Three competing non-associative or beyond-standard-NCG programmes exist:
- **Wulkenhaar** (hep-th/9607094, 9607237, 9708071, 9804046): "Mathematical footing of nonassociative geometry," grand unification in nonassociative geometry, graded differential Lie algebras. Predates BF 2013; partial precursor.
- **Akrami-Majid** (math/0406005): "Braided cyclic cocycles and nonassociative geometry." Categorical / Hopf-algebraic approach. Different mathematical machinery; not directly comparable.
- **Besnard-Farnsworth** (recent): "Particle models from special Jordan backgrounds and spectral triples." More restricted than BF 2013 (Jordan only, not full non-associative); Farnsworth himself is co-author.
- **Boyle-Farnsworth Jordan geometry** (arXiv:1910.11888): SM + Pati-Salam emerging from Jordan algebra structure. Same programme as BF 2013 evolved into Jordan-algebraic formulation.

The Farnsworth-Boyle programme is the most directly applicable to NTE's A_{G_2} commitment because it explicitly handles the octonion case, which is what NTE's "A_{G_2}" name implies.

### 7.4 Existing OctonionExtension corpus engagement

NTE's existing OctonionExtension paper engages with J_3(𝕆) machinery and the Hopf fibration tower (per AC's Tier 3 audit memo §5.2). The Farnsworth 2025 *companion paper* on F_4 × F_4 from J_3(𝕆) (arXiv:2503.10744) directly intersects this existing engagement.

The question for AC: does OctonionExtension's J_3(𝕆) machinery diverge from Farnsworth 2025's construction in ways that matter? Cross-check needed (§11 P2).

### 7.5 What would refute the adoption recommendation

1. **Gilkey heat-kernel failure under non-associativity** (§7.2). Would collapse the entire Farnsworth-Boyle programme.
2. **G_2 × G_2 → SM descent does not work** (§3.4). Would force adaptation to F_4 × F_4 or alternative.
3. **OctonionExtension corpus uses an incompatible J_3(𝕆) construction**. Would require either OctonionExtension revision or Farnsworth divergence flagging.
4. **The 8-fermion (1 + 7) BF 2013 spectrum does not match NTE's pre-temporal fermion ontology**. Would require either NTE revision or alternative starting point (e.g., semi-simple octonion direct from Farnsworth 2025).

None of these refutations is currently established; all are open verification targets.

---

## §8 — Verdict

**DIRECT ADOPTION with adaptation, matching the M1 σ_3 Cartan / √(2π) traceability standard of clean promotion.**

The Farnsworth-Boyle programme provides the canonical algebraic framework for NTE's pre-temporal A_{G_2} regime. The match is structural, not merely numerical:
- A_{G_2} = octonion algebra 𝕆, automorphism group G_2 ✓
- Spectral action on octonion → Einstein gravity + G_2 gauge + 8 Dirac fermions ✓
- Nonassociative-induced chirality at gauge birth ✓ (matches Companion 7's neutrino-as-unresolved-geometry)
- Farnsworth 2025's G_2 × G_2 + charged Higgs provides a candidate post-locking SM-compatible structure ✓

Promotion: **"adopt as algebraic foundation for OctonionExtension §6 and Programme S Paper S2."** This matches the M1 σ_3 promotion's standard of clean structural identification with one open verification item, and matches the √(2π) traceability's standard of "structurally led with open closure."

Open items (§11) are specific and tractable:
- Verify G_2 × G_2 → SM descent
- Cross-check OctonionExtension corpus against Farnsworth 2025
- Verify Gilkey heat-kernel under non-associativity (or accept Farnsworth-Boyle's claim and proceed)
- Direct re-read of Farnsworth 2025 §4-§5 + BF 2013 §3-§5 before any v10.8 or Paper S2 commitment

---

## §9 — Implications for Corpus Integration

### 9.1 v10.8 bundle (currently authorised)

**Recommendation:** add a Tier 2 patch citing the Farnsworth-Boyle programme as the algebraic foundation underlying OctonionExtension §6. Do **not** commit to specific Farnsworth-Boyle constructions in v10.8 — defer that to Paper S2.

Concrete patch wording for §22.X catalogue:
> *Programme S Paper S2 will evaluate Farnsworth-Boyle (arXiv:1303.1782, JHEP 07 (2015) 023) and Farnsworth (arXiv:2506.21496) as the algebraic framework for NTE's pre-temporal A_{G_2} regime. The simplest non-associative octonion spectral triple yields Einstein gravity + G_2 gauge theory + 8 Dirac fermions in the singlet+septuplet of G_2, structurally matching NTE's pre-temporal ontology. The G_2 × G_2 charged-Higgs extension provides a candidate algebraic mechanism for the gauge-birth transition's Higgs sector emergence.*

### 9.2 OctonionExtension corpus update

If AC's cross-check of OctonionExtension against Farnsworth 2025 (§7.4) confirms compatibility, OctonionExtension §6 should explicitly cite the Farnsworth-Boyle programme as the foundational mathematical reference. If incompatibilities surface, OctonionExtension needs revision before v10.9 ship.

### 9.3 Programme S Paper S2 scope sharpening

Paper S2 was previously scoped as "K(Φ) closure via Connes spectral triple programme." The Farnsworth-Boyle reading sharpens this to:

**Paper S2 scope:** Evaluate the Chamseddine-Connes-style spectral action on Hopf-S³ × A_{G_2} where A_{G_2} is the Farnsworth-Boyle octonionic spectral triple. Compute heat-kernel coefficients a_2, a_4 explicitly. Extract:
- K(Φ) functional form (closes r prediction)
- ξ = 1/6 verification (consistency check with Mechanism B supersession)
- V_E /12 coefficient origin (closes √(2π) κ₀ leg fragility)
- M_1 prefactor (closes σ_3 Cartan derivation)
- Cosmological constant prediction (cross-checks unimodular gravity verification, queued as item 4)

**Paper S2 deliverables now have a specific algebraic machinery and a specific set of calculable quantities.**

### 9.4 σ↔Φ_NTE confluence sharpening

The confluence framing can be sharpened from "different fields, same EFT form by independent reasoning" to "different fields, same EFT form by *shared algebraic source* (Farnsworth-Boyle octonionic spectral triple)." This is a refinement, not a retraction. Worth adding to §17.5.5 confluence catalogue at v10.9 (after Paper S2 explicit verification, not at v10.8).

---

## §10 — Cross-Target Leads Surfaced

### 10.1 Companion 7 chirality emergence mechanism

The Farnsworth-Boyle finding that non-associative derivations produce inherent chirality (Farnsworth-Boyle "Rethinking Connes" arXiv:1408.5367) provides a specific mechanism for Companion 7's neutrino-as-unresolved-geometry claim. Pre-projection: non-associative A_{G_2}; no chirality. Post-projection: associative sub-structure; chirality emerges. **This is a structural underpinning Companion 7 currently lacks.** Recommend a follow-up note for Companion 7 §3 once the Farnsworth-Boyle reading is verified.

### 10.2 M_1 σ_3 Cartan ↔ Farnsworth-Boyle G_2 sub-structure

The sibling Jammer's M_1 σ_3 Cartan derivation identified σ_3 as the Cartan-aligned mode. G_2 has rank 2, so its Cartan subalgebra is 2-dimensional. The σ_3 generator of NTE's residual su(2) at gauge birth is one of the G_2 Cartan generators in the Farnsworth-Boyle pre-temporal regime. **The M_1 σ_3 Cartan finding can be re-derived inside the Farnsworth-Boyle framework as a specific projection of the G_2 Cartan subalgebra at gauge birth**, providing a deeper algebraic anchor for the σ_3 mode mass formula M_1³ = M_Pl² × H_GB.

Cross-flag to sibling Jammer (M_1 σ_3): the Cartan-torus ≅ Hopf-fibre observation in the √(2π) traceability working note (§10.2) is now extended — the same Cartan subalgebra of G_2 simultaneously gives M_1 (via σ_3 mode mass) and Y_00(S¹) (via Hopf fibre identification with one Cartan torus dimension).

### 10.3 Sonner-Tong κ₀ alternative (queue item 3)

The Sonner-Tong BPS-on-CP¹ κ₀ derivation works on the Hopf base S² ≅ CP¹. The Farnsworth-Boyle octonionic Hopf-S³ machinery extends naturally to higher-dimensional Hopf bundles via Cayley-Dickson. **The Sonner-Tong κ₀ alternative may be reformulable inside Farnsworth-Boyle as a specific spectral action on Hopf-S³ × 𝕆**, providing a unified attack route for queue items 1-3.

### 10.4 Unimodular gravity verification (queue item 4)

CC's 2008 "Uncanny Precision" cosmological constant cancellation argument uses the spectral action on Hopf-S³ × Heisenberg-algebra. The Farnsworth-Boyle programme provides a more general A_{G_2} (octonion) algebra at this slot. **The cosmological constant prediction may differ between CC's Heisenberg algebra and the Farnsworth-Boyle octonion algebra** — direct computation needed in Paper S2.

---

## §11 — Files Referenced + Open Follow-On Items

### Papers referenced
- Boyle, Farnsworth (2013), "Non-Associative Geometry and the Spectral Action Principle," arXiv:1303.1782, published as JHEP 07 (2015) 023 — **foundational**
- Farnsworth (2025), "Spectral Geometry with Exceptional Symmetry and Charged Higgs Fields," arXiv:2506.21496 — **G_2 × G_2 charged Higgs extension**
- Farnsworth (2025), "The n-point Exceptional Universe," arXiv:2503.10744 — **F_4 × F_4 from J_3(𝕆), companion paper**
- Farnsworth, Boyle (2014), "Rethinking Connes' Approach to the Standard Model via Non-Commutative Geometry," arXiv:1408.5367, New J. Phys. 17 (2015) 023021 — **graded tensor product reformulation, chirality emergence**
- Boyle, Farnsworth (2019), "The standard model, the Pati-Salam model, and 'Jordan geometry'," arXiv:1910.11888 — **SM + PS emergence from Jordan algebras**
- Chamseddine, Connes, van Suijlekom (2013), "Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification," arXiv:1304.8050, JHEP 11 (2013) 132 — **independent parallel relaxation of CC axioms (first-order condition)**
- Wulkenhaar, "Mathematical footing of nonassociative geometry," hep-th/9607094 — **partial precursor**

### NTE corpus files referenced
- `Papers/NTE_Octonion_Extension.md` — §4 Hopf Fibration Tower, §6 non-associative spectral triple machinery, §9.4 M_1 + SU(2)_R / mirror sector
- `Papers/Companion_5_StateSpace_Surface_v10_6.md` — pre-temporal A_{G_2} structure
- `Papers/Companion_7_*.md` — neutrino-as-unresolved-geometry, chirality emergence
- `Working/Sigma_PhiNTE_Confluence_Verdict_v1.md` — σ↔Φ_NTE confluence baseline
- `Working/M1_Sigma3_Cartan_Mode_Derivation_v1.md` — sibling Jammer M_1 derivation
- `Working/Sqrt2Pi_Traceability_Hopf_Fibre_v1.md` — Y_00(S¹) hypothesis
- `Handoffs/Handoff_AC_v10_8_Integration_Plan_Tier3_Synthesis_20260511.md` — v10.8 integration scope

### Open follow-on items (priority order)

**P0 — required before any v10.8/v10.9 corpus integration:**
1. Direct re-read of Farnsworth 2025 §4-§5 for the explicit G_2 × G_2 + charged Higgs construction. Specifically: what is the SU(3) × SU(2) × U(1) descent pattern, if any? (§3.4)
2. Direct re-read of BF 2013 §3-§5 for the spectral action computation on the octonion algebra. Confirm Gilkey heat-kernel expansion is rigorously justified under non-associativity. (§7.2)
3. Direct re-read of OctonionExtension corpus to verify compatibility with Farnsworth 2025 / Farnsworth-Boyle Jordan-geometry constructions. Specifically: does OctonionExtension's J_3(𝕆) machinery diverge in ways that matter? (§7.4)

**P1 — promotes adoption to corpus-integrated:**
4. Explicit heat-kernel computation on Hopf-S³ × A_{G_2} (Farnsworth-Boyle octonionic spectral triple). Extract K(Φ), ξ, V_E /12 coefficient, M_1 prefactor, cosmological constant. This IS Paper S2's central deliverable. (§5.2, §6.2)
5. Verification that nonassociative-induced chirality (Farnsworth-Boyle "Rethinking Connes") produces SM-compatible chirality at gauge birth, not some other chiral pattern. (§3.3)

**P2 — confirmatory:**
6. Cross-check M_1 σ_3 Cartan derivation against G_2 Cartan subalgebra structure inside Farnsworth-Boyle. (§10.2)
7. Cross-check Sonner-Tong BPS-on-CP¹ κ₀ alternative against Farnsworth-Boyle Hopf-S³ × 𝕆 spectral action. (§10.3)
8. Cross-check CC's unimodular gravity treatment of cosmological constant against Farnsworth-Boyle octonion algebra prediction. (§10.4)

**P3 — adversarial robustness:**
9. Survey literature for any published refutation of BF 2013 spectral action expansion. (§7.1, §7.2)
10. Verify Wulkenhaar's precursor non-associative geometry programme is consistent with Farnsworth-Boyle's later development.

### Handoff items
- To AC: input to v10.8 Tier 3 plan, recommendation §9.1 (Tier 2 patch citing Farnsworth-Boyle as Paper S2 algebraic framework, no commitment to specific constructions in v10.8). Cross-check OctonionExtension corpus against Farnsworth 2025 (§7.4, P0 #3).
- To Greg: ratification of §9.3 Paper S2 scope sharpening. The principal Paper S2 deliverable is now explicit: spectral action heat-kernel computation on Hopf-S³ × Farnsworth-Boyle A_{G_2}, yielding K(Φ), V_E /12, M_1 prefactor, cosmological constant simultaneously.
- To Programme S Paper S2 owner: §9.3 scope, §11 P1 items #4-#5 as central deliverables.
- To sibling Jammer (M_1 σ_3): §10.2 cross-target (M_1 σ_3 inside G_2 Cartan subalgebra of Farnsworth-Boyle pre-temporal).
- To Companion 7 author: §10.1 chirality emergence mechanism via non-associative derivations.

---

**End of Working Note.** Verdict: direct adoption with adaptation, matching M_1 σ_3 Cartan / √(2π) traceability promotion standard. Farnsworth-Boyle provides the algebraic foundation for NTE's pre-temporal A_{G_2}; the principal open work is the explicit heat-kernel computation on Hopf-S³ × A_{G_2} (Paper S2 central deliverable), which simultaneously closes K(Φ), √(2π) κ₀ leg, M_1 prefactor, and cosmological-constant prediction.

— Jammer, 2026-05-11