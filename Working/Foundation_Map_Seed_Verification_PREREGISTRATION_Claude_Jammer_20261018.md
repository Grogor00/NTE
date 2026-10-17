# Foundation Map: verification of the 15 seed nodes. PRE-REGISTRATION (Jammer)

Directive: Handoffs\Directive_AC_to_Jammer_Verify_The_Foundation_Map_Fifteen_Seed_Nodes_20261018.md, read in full.
Scope: Handoffs\THE_FOUNDATION_MAP_Scope_And_Build_Order_Nothing_Of_Ours_Until_The_Landscape_Is_Built_20261016.md and Handoffs\GO_AC_Foundation_Map_Ratified_Build_The_Seed_Set_Cursor_Then_Jammer_Then_Scratch_20261016.md, both read in full.
Filed after listing the 15 node files in Working\foundation_map\ and before opening any of them.

**Stake.** I computed two of the nodes (g2_su3_branching and g2_cannot_contain_sm) and originated the d=2 counterexample that a third node records. Scratch also computed it. I am liable to under-scrutinise those three. I will hold them to the same "does not establish" test as the rest.

**Grades per node:** VERIFIED / NARROW AS STATED / WRONG / UNCHECKED. UNCHECKED means I cannot judge without the primary and have no reliable session read of it. Verifying a node from the node file alone checks internal coherence and register, not fidelity to the source. I will say which kind of check each grade rests on.

## Priors (to be discounted)
- **Reconstruction (complex_qm_operational):** NARROW, 0.6. Risk: a reading of "complex QM from nothing". The axioms are operational and include continuous reversibility and local tomography; real QM fails local tomography.
- **qubit_bloch_ball_3d:** NARROW, 0.4. Masanes–Müller derive d=3 from their axioms. The node must not read as unconditional.
- **gleason_born_d_ge_3:** VERIFIED or NARROW, 0.5. Risk: omitting that Gleason gives density operators and mixed states on all projections, or that it assumes non-contextual frame functions, or that it is stated for separable Hilbert spaces with dim ≥ 3.
- **d2_underdetermined:** VERIFIED, 0.6. Risk: overstating it as "the Born rule fails at d=2". The correct claim is that the qubit's Born rule is not fixed by frame-function additivity without POVMs (Busch).
- **g2_su3_branching:** VERIFIED, 0.7. Risk: claiming external authorship for our computation, or omitting the standard citation.
- **g2_cannot_contain_sm:** VERIFIED, 0.6. Risk: overreach, by stating that octonions cannot give the SM. They can, via F₄ / Cl(6). The no-go is about G₂ subgroups only.
- **sm_inside_f4 and sm_from_cl6_furey:** NARROW, 0.5. Risk: "derives the SM" where the source shows the group or one generation's representations; three generations and hypercharge for all three are open in Furey.
- **doubly_coupled_bd_ghost:** VERIFIED, 0.5. The exception must be named.
- **hassan_rosen_bimetric:** NARROW, 0.6, following AC's prior on β and the mass scale.
- **unimodular_trace_free:** NARROW, 0.6, following AC's prior on contested status.
- **neff_act_dr6:** VERIFIED, 0.6. Risk: wrong dataset combination, or the error read as a measurement of non-standard radiation.
- **mirror_baryons_x_le_0p3:** NARROW or UNCHECKED, 0.6. Risk: x ≲ 0.3 is a model-dependent bound, set by BBN and CMB at various strengths.
- **spectral_action_cosmo_term:** NARROW, 0.6. Risk: the cosmological term's coefficient is cutoff- and f-moment-dependent, and "volume quantisation" (CCM 2014) is a separate result with its own assumptions.
- **bft_cpt_universe:** NARROW, 0.6. Risk: BFT's own mass is fixed by matching the DM abundance, and the PRL abundance formula is all I hold from my session read.

## Structural tests
- S1: is every "does not establish" field non-empty and specific?
- S2: does any node `assumes` a node that is verified: NO / PARTIAL? This is the standing rule.
- S3: does any node carry our own claims beyond the three permitted computed verifications? This is the one rule.
- S4: does any node state a source as fetched without saying who read it, and when?

Global prior: at least 5 of 15 graded NARROW (0.7). At least one graded WRONG (0.25).
