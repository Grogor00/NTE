# Handoff — AC → Cursor: Working triage PASS 3 (retire the over-kept set)

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-22
**In response to:** `Handoffs\Handoff_Cursor_to_AC_Working_Candidates_Triage_Pass2_Complete_20260922.md`
**Status:** Greg-directed. Pass 2 applied AC's rules correctly. **One AC rule was over-broad** and is the cause of this pass.
**Addressing:** name/path only (discipline 9).

---

## Why

K2's M_R trace said "keep **any** file containing 8.2 × 10¹⁴" — intended to *find* the figure's source, not to keep every carrier. It pulled ~49 files into `Working\`, overriding D-rules that name several of them explicitly (chirality-superposition drafts, η notes, v10.x patch instructions, a spent `apply_*` script). The trace has now done its job: the figure is canonical in `Core_Papers\Companion_13_Yukawa_Nu2_v10_19_0.md` §4. **The K2-M_R keep rule is withdrawn**, and the K2 fibre-modulus content rule with it (same over-breadth). Files kept only by those rules retire.

---

## A. Move to `Working\Retired\` — explicit list

Move each of these from `Working\` (move, never copy; SHA-256 on collision as before). If a name is absent, report it; do not guess.

```
_p5_prepare_test.md
apply_companion_v10_17_2.py
Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601 (1).md
Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601.md
CO00A2~1.MD
COD347~1.MD
COE381~1.MD
COEFB4~1.MD
Companion_12_v10_17_2_Scratch_CR_Verification_v0_1.md
Companion_13_v10_17_2_Scratch_CR_Verification_v0_1.md
Connes_Programme_Charter_v1.md
Connes_Programme_Launch_Plan_v1.md
Corpus_Sunshine_Path_Audit_Results_Scratch_P0_20260525.md
CPN_Universe_Pair_S1_Gibbons_Hartle_Conserved_Charge_Audit_Concession_Path_Likely_Hopf_Charge_Open_Claude_Jammer_20260617.md
CPN_Universe_Pair_T1_Jammer_Side_Parity_Computation_PASS_DERIVED_Claude_Jammer_20260617.md
CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md
CR2_Programme_S_F6_Collateral_Scan_Cursor_Jammer_20260601.md
Eta_Asymmetry_Magnitude_Reframing_Audit_v2.md
eta_Calculation.txt
eta_precondition_check_worksheet.py
gap1_pathwayA_session2_worksheet.py
Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1_20260524.md
Jammer_M2_Z2_Split_Derive_v0_1_20260524.md
M1_From_Geometry_E_search.md
Master_v10_10_Tier1_Patch_Instructions_Programme_S_Spine_20260523.md
Master_v10_14_Tier2d_Patch_Instructions_PaperS2_S2C_20260523.md
Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523 (1).md
Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523.md
Master_v10_8_to_v10_9_Patch_Instructions_A6_FalsifiabilityCatalogue_Consolidation_20260523.md
NTE_Pedagogical_Pivot_Companions_Register.md
NTE_Provenance_Audit_New_vs_ReDerived_vs_Imported_First_Pass_AC_20260622.md
NTE_Standalone_Claims_Inventory_v0_1_20260524.md
NTE_Standalone_Claims_Inventory_v0_2_20260524.md
NTE_vs_Singh_Octonionic_Theory_Precise_Overlap_Differentiation_Map_Stronger_Simpler_Verdict_Parsimony_Edge_Singh_Derives_QM_Alpha_AC_20260622.md
Package_E8b_P4_Pivot_CLFV_Sister_Prediction_Replacement_Prose_Draft_PC_20260618.md
paper_s22_1_y_nu2_numerics.py
paper_s22_1b_y_nu1_bracket_numerics.py
paper_s22_1c_y_nu1_zero_param_numerics.py
paper_s2_chord_closure_numerics.py
Paper_S2_Chord_Closure_Synthesis_v1_0_20260524.md
paper_s2_d5_factor_112_numerics.py
paper_s2_m2_z2_split_numerics.py
Paper_S2_HeatKernel_Phase_I_Item_2_D_F_Yukawa_Structure_Jammer_v0_2_20260529.md
Paper_S2_S2A_Operator_Setup_v0_1.md
Paper_S2_S2B_Coefficients_Plus_Kappa0_v0_1.md
Paper_S2_S2CB_a4_Weyl_Euler_v0_1.md
Paper_S2_S2CC_DF_Subleading_v0_1.md
Paper_S2_S2E_AC_Integration_Package_v0_1.md
Paper_S2_Scope_and_Attack_Route_v0_1_20260523.md
Paper_S2_v1_0_Scratch_CR_Verification_v0_1.md
PC_Scoping_Memo_Corpus_State_and_Pedagogical_Opportunities_20260613.md
Popular_Paper_Spectral_Action_v1.md
Programme_S_Paper_S6_v1_0_Canonical_Synthesis_Post_Cursor_20260526.md
Scratch_Adversarial_Review_AC_Wagenveld_Sprint_v0_1_20260528.md
Scratch_Kappa0_to_XiV_Rename_Routing_Report_v0_1_20260528.md
Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_1_Seed_Amplitude_v0_1.md
Sigma_t_Phi_NTE_Investigation_Direction_2_BottomUp_Jammer_v1.md
Twistor_Theory_Axiom_Filter_Pass_Jammer_v1.md
Working_FalsifierSearch_Unitary_CPN_TwoLayer_Opening_Scoping_Claude_Jammer_20260610.md
```

Reasons, by family: pre-rebuild process material (D1); concluded research threads (D2); retired chirality-superposition ontology, η demotion, and the retired chord (`Paper_S2_Chord_*`, `paper_s2_chord_*`) (D3); spent numerics and tooling (D4, D5); May Paper-S2 drafts superseded by Companions 14/15 and the verified-coefficient work of 2026-08.

---

## B. Confirmed KEEP — stays in `Working\`

- **P1 pipeline:** `prepare_paper_pdf.py`, `prepare_master_pdf.py`, `strip_publication_tail.py`, `strip_corpus_metadata.py`.
- **P3 post-August:** every file you tagged P3, unchanged.
- **σ↔generation dictionary / TM1 (Items 1, 8):** all `GATE*_VERDICT_*`, `CHARTER_GATE1_*`, `CHARTER_P4D_*`, `Investigation_P4D_*`, `FS_Geometry_Finding_Theta23_*`, `M1_Sigma3_Cartan_Mode_Derivation_v1.md`, `CR2_Programme_S_Sigma3_Adversarial_*`, `CR2_Programme_S_Sigma3_Y3_Derivation_Memo_*`.
- **Route-B / Paper-S2 build:** the six `farnsworth_stage*.py`.
- **Open M_R derivation (Part 3 open list):** `CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_*`, `Cursor_Heat_Kernel_M_R_Critical_Review_v0_2_*`, `Scratch_Heat_Kernel_Cross_Check_M_R_Scoping_v0_1.md`, `Scratch_M_R_BPS_Anchored_Cross_Check_v0_1.md`, `Scratch_M_R_BPS_Anchored_Cross_Check_v0_2_Full_Lagrangian_Closure.md`, `Scratch_M_R_Cross_Check_v0_4_Reconciliation_with_Cursor_Review.md`, `Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md`.
- **Open atmospheric-ratio overshoot:** `Sunshine_P5_Solar_Sunshine_Verdict_REFRAME_*`.
- **Reproducibility of live canonical results:** `clfv_cartan_ratio_numerical.py` + results `.json` + results `.md` (Companion 18); the five κ-closure files; `Unimodular_Gravity_Verification_CC2008_v1.md` (Companion 11).
- **Standing guidance / reader assets (K4):** `NTE_Acronym_Naming_Discipline_*`, `NTE_Book_Appendix_and_Corpus_Links_Discipline_*`, `NTE_Book_DeAI_Voice_Pass_*`, `NTE_Book_Popular_Voice_Register.md`, `NTE_Book_Title_and_Pratchett_Discipline_*`, `Publication_Title_Block_Standard_*`, `Standalone_Papers_Accessibility_Tiering_Framework_*`, `NTE_Reader_Glossary_Companion_v1_0.md`, `NTE_FAQ_Supplement_DRAFT_v0_2_*`.
- **K5:** `NTE_Octonionic_Spine_Neutrino_Mixing_Sector_v0_2_DRAFT_White_20260626.tex`.

Anything in `Working\` top level that is in **neither** list A nor list B: **report it, do not move it.**

---

## C. Owed from Pass 2 — tilde identification

The Pass 2 summary gave each `~` file's rule but not its identity. For all **24** tilde files (now in `Working\Retired\`, or moving there under A), report: short name → first heading → date/version line → probable original long filename. No moves needed; this is so the record shows what was retired.

---

## D. Register — manifest §10 (two lines)

Under the existing in-progress item for this triage, update the held count to the Pass 3 result, and add this watch-item:

```
- **Companion 13 ref 4 citation defect** (found 2026-09-22 during Working triage) — `Companion_13_Yukawa_Nu2_v10_19_0.md` reference 4 attributes "the heavy scale M_R = M_Pl^{3/4} v_EW^{1/4}" to Part 3, but Part 3 carries no M_R formula or number (only "M_R (pathway identified, not derived)" and "the derivation of M_R" as open). Either Part 3 gains the pathway line at that register, or ref 4 is re-pointed. Greg to rule. Not blocking.
```

---

## E. Deliverables

1. Append a **Pass 3** section to `Working\Working_Candidates_Triage_Pass2_Summary_20260922.md`: files moved, anything reported under B's catch-all, and the tilde table from C.
2. Append the Pass 3 moves to `Working\Working_Candidates_Triage_Pass2_Moves_20260922.csv`.
3. Completion handoff to `Handoffs\`, addressed to AC.

---

— AC, 2026-09-22.
