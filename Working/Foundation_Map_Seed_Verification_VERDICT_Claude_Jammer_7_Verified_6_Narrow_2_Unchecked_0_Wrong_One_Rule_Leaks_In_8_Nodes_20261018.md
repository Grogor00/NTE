# Foundation Map seed verification: VERDICT (Jammer)

Directive: Handoffs\Directive_AC_to_Jammer_Verify_The_Foundation_Map_Fifteen_Seed_Nodes_20261018.md
Pre-registration: Working\Foundation_Map_Seed_Verification_PREREGISTRATION_Claude_Jammer_20261018.md (filed before any node file was opened)
Read in full this session, all at current state: the 15 node files in Working\foundation_map\, the README, and PROGRESS_CursorMain_20261018.md.

**Primaries fetched today by me, to check Cursor's PARTIAL nodes:**
- arXiv:1803.08930v2 (abstract): "The Big Bang, CPT, and neutrino dark matter", Boyle–Finn–Turok.
- arXiv:1803.08928 (PRL text): "CPT-Symmetric Universe", Boyle–Finn–Turok.
- arXiv:quant-ph/9909073 (Busch, full text).
- ar5iv 1004.1483 (Masanes–Müller): §I and the abstract. §IV was truncated in the fetch.

**What each grade rests on.**
- (n) node-internal coherence and register only.
- (p) checked against a primary fetched by me today.
- (c) relies on Cursor's stated fetch; I asked what was read, and the node states it.
- [k] my own background knowledge, not read this session. It is used only to flag, never to verify.

## Per-node grades

| # | Node | Grade | Basis |
|---|---|---|---|
| 1 | gleason_born_d_ge_3 | **NARROW** (edge + assumes); claim line OK | n; primary 1957 UNCHECKED |
| 2 | d2_underdetermined | **NARROW** | p (Busch) + n |
| 3 | complex_qm_operational | **NARROW** | p (MM §I) + c |
| 4 | qubit_bloch_ball_3d | **VERIFIED** (strip one-rule leaks) | p (MM abstract) |
| 5 | g2_su3_branching | **VERIFIED** | own computation + c |
| 6 | g2_cannot_contain_sm | **VERIFIED** | own computation |
| 7 | sm_inside_f4 | **VERIFIED** | c |
| 8 | sm_from_cl6_furey | **VERIFIED** | c |
| 9 | doubly_coupled_bd_ghost | **VERIFIED** (strip leaks) | c |
| 10 | hassan_rosen_bimetric | **VERIFIED** (AC's β prior already met) | c |
| 11 | unimodular_trace_free | **NARROW** | n + [k] |
| 12 | neff_act_dr6 | **NARROW** (dataset label) | c + [k] |
| 13 | mirror_baryons_x_le_0p3 | **UNCHECKED** (no identifiable source) | n |
| 14 | spectral_action_cosmo_term | **UNCHECKED** (no specific source; possible inversion flagged) | n + [k] |
| 15 | bft_cpt_universe | **NARROW** | p |

**WRONG: none.** Seven nodes are VERIFIED, six NARROW and two UNCHECKED. The pre-registered prior (at least 5 NARROW, P=0.7) held. The prior of at least one WRONG (0.25) did not.

## Corrections, node by node

**1. gleason_born_d_ge_3.**
- The claim line is fine at textbook strength.
- The edge "`excludes` → underdetermination in d=2" is mistyped. Gleason's hypothesis *does not cover* d=2; it excludes nothing there. Retype it as "d=2 lies outside hypothesis (see d2_underdetermined)".
- `assumes` says "Complex Hilbert space". Gleason holds over real and quaternionic spaces too, and in separable infinite dimension with σ-additivity [k]. That is understatement, not overstatement; fix it at the next primary read.
- The node stays not usable as a premise until the 1957 text is read.

**2. d2_underdetermined.**
- (i) **Attribution.** The counterexample family originated in my readiness verdict of 2026-10-15. Scratch computed it independently the same day. Credit both lanes.
- (ii) **The one rule.** The external established result should lead. Busch (fetched today) states: "The statement of the present theorem also extends to the case of 2-dimensional Hilbert spaces where Gleason's theorem fails." Our computation is a check, not the source. Bell 1966 is the classic qubit non-contextual model [k]; Cursor to fetch.
- (iii) **Strip** "That C2's specific Hopf uniqueness claim is false…" and the `gap-between` "vs Hopf-geometric uniqueness programmes". Both refer to our deposit.
- (iv) **Standing rule.** The node's "assumes-context → gleason_born_d_ge_3" points at a PARTIAL node. Repoint it to Busch, whose fetched text states the d≥3 hypothesis and its failure at d=2.
- **Corrected claim line:**
  > "Gleason's theorem fails at d=2 (Busch 2003, stated explicitly). Frame-function additivity on projectors does not single out the Born rule for a qubit: explicit families such as f(r)=sin²(πr/2) and r+ε sin 2πr satisfy normalisation, phase invariance and joint SU(2) invariance (computed, Jammer and Scratch, 2026-10-15). Uniqueness is restored on effects/POVMs (Busch 2003), which also holds at d=2."

**3. complex_qm_operational.**
- The claim line is fine ("from operational axioms" is the right strength).
- **Error in `assumes`:** Masanes–Müller's axioms are listed as "local tomography, continuous reversibility, etc.". MM §I (fetched) gives five requirements:
  1. a bit's state fixed by finitely many probabilities;
  2. local tomography;
  3. equivalence of subsystems;
  4. symmetry (any pure state reversibly transformable to any other);
  5. all measurements allowed.
- "Continuous reversibility" belongs to Hardy, not MM. Fix the list.
- **Strip** "octonion descent, physical S³ cosmology" and "Any NTE-specific claim" from `does not establish` (the one rule). Replace them with the source-internal limits:
  - finite dimension;
  - the GPT framework itself is assumed;
  - each package rules out real and quaternionic theories only within its axioms. For MM, local tomography is the axiom that does this [k].

**4. qubit_bloch_ball_3d.** VERIFIED. The MM abstract (fetched) promises "a group-theoretic explanation of the Bloch ball and its three-dimensionality". The §IV proof was truncated in my fetch, so my check is at abstract strength.
- Strip "physical universe is a 3-sphere" and "spin-j on S³". Those are corrections to our papers, not limits of MM.
- Replace with: "does not establish the dimension outside the MM axiom set; does not address composite-system geometry beyond the stated requirements."

**5. g2_su3_branching.** VERIFIED. Authorship is stated correctly: Günaydin–Gürsey for the result, Jammer for the computation. No claim of external authorship for our work.

**6. g2_cannot_contain_sm.** VERIFIED and correctly scoped.
- The rank fact is elementary Lie theory. The centraliser-0 computation is ours, and the node says so.
- `does not establish` correctly protects F₄ and Cl(6).
- Optional addition, which follows from centraliser 0: "no SU(2) or U(1) inside g₂ commutes with Stab(e₁)."

**7, 8. sm_inside_f4, sm_from_cl6_furey.** VERIFIED on Cursor's fetches. Both are scoped as constructions, not derivations of physics, and both name the missing three-generation mechanism.

**9. doubly_coupled_bd_ghost.** VERIFIED. Strip "Any NTE-specific action" and "geometric bridges without second kinetic metric". The second is framed toward our use. Keep it out until step 4.

**10. hassan_rosen_bimetric.** VERIFIED. AC's prior is already met: the β coefficients and the mass scale sit in `does not establish` as free parameters.
- Suggested addition, to be fetched before entry: "does not establish stable cosmological solutions (gradient/Higuchi-type instabilities are discussed in follow-up literature)" [k].

**11. unimodular_trace_free.** NARROW.
- (i) The source field fails the schema. "Jiroušek et al. / related 2023 literature (campaign cite)" names no paper and was not fetched. Buchmüller–Dragon has no title or venue. That leg must be marked `verified: NO`, not PARTIAL.
- (ii) The claim "offering a structural approach to the cosmological-constant problem" over-reads the source. Whether unimodular gravity helps at all is the main dispute. One argument says Λ simply returns as an integration constant, with no gain on radiative stability; Padilla–Saltas 2015 is the reference I recall [k], and Cursor should fetch it. That dispute, not only a global four-volume condition, is what "contested" should name.
- **Corrected claim line:**
  > "In unimodular / trace-free formulations, a constant vacuum energy drops out of the field equations and Λ re-enters as an integration constant (Henneaux–Teitelboim 1989; Buchmüller–Dragon 1988, to be fully cited). Whether this addresses the cosmological-constant problem is disputed."

**12. neff_act_dr6.** NARROW (minor).
- The quoted figure 2.86 ± 0.13 is the P-ACT-LB combination. LB adds CMB lensing and BAO to Planck+ACT [k; confirm from the abstract]. The claim line says "combining ACT DR6 with Planck"; label it "P-ACT-LB (Planck + ACT DR6 + lensing + BAO)".
- Strip "campaign figure used in Core/Working".
- The rest is correct. The difference from 3.044 is about 1.4σ, consistent with "within uncertainties".

**13. mirror_baryons_x_le_0p3.** UNCHECKED.
- "Mirror-matter reviews and papers (Foot; Berezhiani and collaborators)" identifies no source, so the node cannot be verified and must be `verified: NO`.
- Flag for whoever fetches [k]: the x ≲ 0.3 figure is, as I recall, mainly a BBN/ΔN_eff bound. The all-dark-matter requirement from structure formation is usually quoted tighter (x ≲ 0.2).
- "The epoch that fixes the DM ratio" is our phrasing, not the literature's.
- Strip "Campaign uses this bound in Part 3".

**14. spectral_action_cosmo_term.** UNCHECKED.
- The sources are non-specific: "multiple; e.g. 2008"; "CCM 2014 (campaign cite)".
- Two flags for the fetch:
  - (i) In Chamseddine–Connes–Mukhanov's volume quantisation, as I recall [k], M₂(ℍ) ⊕ M₄(ℂ) *emerges* from the Clifford algebras of the higher Heisenberg relation. The node lists it under `assumes`. If my recollection holds, the node inverts output and input.
  - (ii) `does not establish` should state that the cosmological term arrives with natural size ~f₄Λ⁴. The spectral action reproduces the cosmological-constant problem; it does not resolve it [k].
- "Geometric origin of gravitational and gauge terms" is interpretive. Use "the heat-kernel expansion of Tr f(D/Λ) yields …".

**15. bft_cpt_universe.** NARROW. Checked against both primaries today.
- (i) **Missing from `does not establish`:** the mass. Both abstracts say matching the observed dark-matter density "requires its mass to be 4.8×10⁸ GeV". The mass is set by abundance matching, not predicted.
- (ii) "inflation-free with r = 0 in their framing" → 1803.08930: "in the absence of an epoch of cosmic inflation, there should be no primordial, long-wavelength gravitational waves". The prediction is conditional, and neither abstract states r.
- (iii) "Antimatter sorting" in `establishes` is not in either abstract as fetched. Mark it unverified or cut it.
- (iv) **Strip** the NTE M₁ overproduction sentence and AC's "replaces a failed origin sector" caveat. Both are ours. The caveat belongs at step 4.
- Arxiv numbers: 1803.08928 is the PRL ("CPT-Symmetric Universe"). 1803.08930 is "The Big Bang, CPT, and neutrino dark matter". Cite both.
- Upgrade `verified` to YES at abstract strength (Jammer, 2026-10-18).
- **Corrected claim line:**
  > "Boyle–Finn–Turok propose that the universe before the bang is the CPT image of the universe after it. This selects a vacuum, and a Z₂-stabilised right-handed neutrino becomes the dark matter; matching the observed density requires mass 4.8×10⁸ GeV. Absent inflation, they predict no primordial long-wavelength gravitational waves."

## Structural tests
- **S1 (`does not establish` non-empty):** passes for all 15, with no empty fields. Its weakness is different: in eight nodes, part of the field is spent on **our** items instead of the source's own limits, and that displaces the source-internal limits that belong there (BFT's fitted mass; spectral action's Λ⁴). This is the over-read signature AC asked me to look for, in a subtler form.
- **S2 (no PARTIAL premise):** one violation, d2 → gleason. Fix by repointing to Busch.
  - The `gap-between` edges Cursor pre-seeded are Scratch's step. Two of them point at our programmes ("Hopf-geometric uniqueness programmes", "physical-S³ identification programmes"), and those must go.
- **S3 (the one rule: nothing of ours):** leaks in **8 of 15** nodes:
  - d2;
  - complex_qm;
  - qubit;
  - doubly_coupled;
  - neff;
  - mirror;
  - bft;
  - unimodular ("campaign cite").
  - Each leak is a mention of our corpus in a cautionary or contextual role. The GO forbids exactly that ("not a withdrawn item as a cautionary node"). This is a class finding: one sweep fixes it.
- **S4 (fetched, not recollection):** three nodes carry sources nobody has identified: unimodular (Jiroušek), mirror and spectral. "PARTIAL" understates this; they should read `verified: NO`.

## Rule check on AC's three priors
- Reconstruction: the claim strength is correct ("operational axioms"). The defect is a mis-listed MM axiom, not overstatement.
- Hassan–Rosen: already correct.
- Unimodular: contested status is visible, but the dispute it names is not the main one, and that leg is unsourced.

AC's priors were right on one node out of three. Overstatement in this map comes from leakage and from missing source-internal limits, not from inflated claim lines.
