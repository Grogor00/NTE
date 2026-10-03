# Working Candidates Triage — Pass 2 Summary (2026-09-22)

**Agent:** Cursor Main · **Generated:** 2026-09-22 22:15 UTC+12:00
**Handoff:** `Handoffs\Handoff_AC_to_Cursor_Working_Candidates_Triage_Pass2_20260922.md`

## Correction acknowledged

Pass-1 "render-blocking / restore to paper-build" finding is **withdrawn** (AC error). Live strip/prepare scripts live in `Working\`. `__pycache__` left alone. No restore to `paper-build\`.

## P1 — derived render-pipeline protect list

From `paper-build\render-all-clean.ps1` + imports of `prepare_paper_pdf.py` / `prepare_master_pdf.py`:
- `Working\prepare_paper_pdf.py`
- `Working\prepare_master_pdf.py`
- `Working\strip_publication_tail.py`
- `Working\strip_corpus_metadata.py`

## Counts

**moved to Working (from candidates):** 107 · **moved to Retired:** 639 · **held:** 0
`Working candidates\` files remaining: **0** (folder left in place).
`Working\` top-level files now: **123**.

### Counts per rule (moves)

- D1 closed May–June process: 215
- D default: 166
- D5 spent tooling: 88
- D2: 53
- K2 M_R numeric trace content: 49
- D4 spent numerics: 44
- D2 concluded/dormant research: 29
- D tilde-identified default retire: 20
- K2 fibre-modulus / β_GB content: 16
- K2 open-item: 15
- K4 standing guidance: 8
- D7 registries/queues/ledgers: 7
- D3 withdrawn/retired content carriers: 7
- K3 reproducibility: 6
- K2 Route-B farnsworth_stage*.py: 6
- K1 cited: 4
- D1 Cursor_* audits/reviews: 3
- D5 candidate twin of live P1 Working script: 3
- K2 M_R figure / seesaw convention: 2
- D7: 1
- K5 octonionic standalone keep: 1
- D6 ID caches: 1
- K5/R1 New folder has same/later: 1
- Pass2: retire Pass1 report: 1

## KEEP — `Working\` top-level after Pass 2

- `.cursor_handoff_watch_state.json` [P3/post-Aug]
- `_archive_search_conformal_20260922.py` [P3/post-Aug]
- `_emergence_grep_20260921.py` [P3/post-Aug]
- `_p5_prepare_test.md`
- `_pass2_finalize_summary.py` [P3/post-Aug]
- `_triage_pass2_20260922.py` [P3/post-Aug]
- `apply_companion_v10_17_2.py`
- `Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601 (1).md`
- `Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601.md`
- `CHARTER_GATE1_Sigma_Triple_vs_J3O_Generation_Identification_VERDICT_Inequivalent_Reps_Gauge_Adjoint_vs_Jordan_Slots_Real_Tension_Operative_Content_Regroundable_Scratch_20260625.md`
- `CHARTER_P4D_Sequel_Rec1_Generation_Swap_vs_Bilateral_CPN_Literal_Operator_Identity_Scratch_Lead_Gated_20260624.md`
- `clfv_cartan_ratio_numerical.py`
- `clfv_cartan_ratio_numerical_results.json`
- `CLFV_Cartan_Ratio_Numerical_Results_20260613.md`
- `CO00A2~1.MD`
- `COD347~1.MD`
- `COE381~1.MD`
- `COEFB4~1.MD`
- `Companion_12_v10_17_2_Scratch_CR_Verification_v0_1.md`
- `Companion_13_v10_17_2_Scratch_CR_Verification_v0_1.md`
- `Connes_Programme_Charter_v1.md`
- `Connes_Programme_Launch_Plan_v1.md`
- `Corpus_Sunshine_Path_Audit_Results_Scratch_P0_20260525.md`
- `CPN_Universe_Pair_S1_Gibbons_Hartle_Conserved_Charge_Audit_Concession_Path_Likely_Hopf_Charge_Open_Claude_Jammer_20260617.md`
- `CPN_Universe_Pair_T1_Jammer_Side_Parity_Computation_PASS_DERIVED_Claude_Jammer_20260617.md`
- `CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md`
- `CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_Claude_Jammer_20260601.md`
- `CR2_Programme_S_F6_Collateral_Scan_Cursor_Jammer_20260601.md`
- `CR2_Programme_S_Sigma3_Adversarial_Cursor_Scratch_20260601.md`
- `CR2_Programme_S_Sigma3_Y3_Derivation_Memo_Cursor_Jammer_20260601.md`
- `Cursor_Heat_Kernel_M_R_Critical_Review_v0_2_20260525.md`
- `Eta_Asymmetry_Magnitude_Reframing_Audit_v2.md`
- `eta_Calculation.txt`
- `eta_precondition_check_worksheet.py`
- `EvolvingDM.md` [P3/post-Aug]
- `farnsworth_stage1_octonion.py`
- `farnsworth_stage2_bimodule.py`
- `farnsworth_stage3_neutrino_block.py`
- `farnsworth_stage4_hopf_overlap.py`
- `farnsworth_stage4full_associator_envelope.py`
- `farnsworth_stage5_assemble.py`
- `FS_Geometry_Finding_Theta23_Z2_Should_Be_MuTau_REFLECTION_Not_Exchange_Predicts_deltaCP_PlusMinus_HalfPi_Fixes_Theta13_Antilinear_Is_CPN_Scratch_20260624.md`
- `gap1_pathwayA_session2_worksheet.py`
- `GATE2_VERDICT_PASS_Regroundable_J3O_SlotSwap_Carries_Generation_Z2_And_Connector_Conjugation_Is_P4D_Antilinear_Reflection_Sigma2_Odd_Automatic_From_Hermiticity_Scratch_20260626.md`
- `GATE3_VERDICT_PASS_ParameterFree_Colour_Singlet_ImO_1Dim_e1_Forces_Connector_Direction_DeepDive_CLOSED_Regroundable_P4_P4D_onto_J3O_Spine_Scratch_20260626.md`
- `GATE4_VERDICT_PARTIAL_PMNS_from_J3O_th23_delta_forced_th12_sumrule_TM1_favoured_th13_input_Scratch_20260626.md`
- `GATE4B_VERDICT_TM2_is_J3O_natural_branch_solar_residual_structural_NOT_TM1_charged_lepton_subcheck_Scratch_20260626.md`
- `GATE4C_VERDICT_EMPTY_no_generation1_mechanism_in_J3O_TM1_not_delivered_solar_prediction_TM2_0p341_2p8sigma_Scratch_20260626.md`
- `GATE5_VERDICT_NEGATIVE_RG_running_CANNOT_explain_solar_2p8sigma_SM_regime_short_by_100x_th12_0p341_scale_stable_JUNO_decisive_Scratch_20260626.md`
- `GATE6_VERDICT_GLIMPSE_TM1_is_timelike_branch_of_Lorentzian_generation_metric_HartleHawking_selector_open_NOT_closed_Scratch_20260626.md`
- `GATE6b_VERDICT_FirstApprox_NEGATIVE_corpus_CPN_is_NOT_T_arrow_preserving_cannot_select_arrow_flipping_TM1_HartleHawking_route_largely_closed_Scratch_20260626.md`
- `Investigation_P4D_Sequel_VERDICT_PARALLEL_NOT_DESCENDED_Wolfram_Independent_GenSwap_IntraSector_CPN_InterSector_Associator_Intracopy_No_4pi_to_8pi_Promotion_TripleConvergent_Scratch_20260624.md`
- `Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1_20260524.md`
- `Jammer_M2_Z2_Split_Derive_v0_1_20260524.md`
- `kappa_closure_g1_adversarial_jammer.py`
- `KAPPA_CLOSURE_G1_Adversarial_Result_Cursor_Jammer_20260620.md`
- `KAPPA_CLOSURE_G1_Jammer_Physics_Sight_Cursor_Jammer_20260620.md`
- `kappa_closure_p2eqp_check.py`
- `KAPPA_CLOSURE_P2eqP_Check_Result_Cursor_Main_20260620.md`
- `M1_From_Geometry_E_search.md`
- `M1_Sigma3_Cartan_Mode_Derivation_v1.md`
- `Master_v10_10_Tier1_Patch_Instructions_Programme_S_Spine_20260523.md`
- `Master_v10_14_Tier2d_Patch_Instructions_PaperS2_S2C_20260523.md`
- `Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523 (1).md`
- `Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523.md`
- `Master_v10_8_to_v10_9_Patch_Instructions_A6_FalsifiabilityCatalogue_Consolidation_20260523.md`
- `NTE_Acronym_Naming_Discipline_v0_1_20260526.md`
- `NTE_Book_Appendix_and_Corpus_Links_Discipline_v0_1_20260526.md`
- `NTE_Book_DeAI_Voice_Pass_20260526.md`
- `NTE_Book_Popular_Voice_Register.md`
- `NTE_Book_Title_and_Pratchett_Discipline_v0_1_20260526.md`
- `NTE_FAQ_Supplement_DRAFT_v0_2_Grown_From_Companions_And_Recent_Work_Clusters_Neutrino_Time_QuantumFoundations_CP_DarkMatter_Lambda_GaugeOctonions_Methodology_Three_PaperWorthy_Flagged_GregGated_AC_20260625.md`
- `NTE_Investigation_Note_Neutrino_Condensate_Bridge_Route_CLOSED_DvaliFuncke_AC_20260922.md` [P3/post-Aug]
- `NTE_Octonionic_Spine_Neutrino_Mixing_Sector_v0_2_DRAFT_White_20260626.tex`
- `NTE_Pedagogical_Pivot_Companions_Register.md`
- `NTE_Provenance_Audit_New_vs_ReDerived_vs_Imported_First_Pass_AC_20260622.md`
- `NTE_Reader_Glossary_Companion_v1_0.md`
- `NTE_Standalone_Claims_Inventory_v0_1_20260524.md`
- `NTE_Standalone_Claims_Inventory_v0_2_20260524.md`
- `NTE_vs_Singh_Octonionic_Theory_Precise_Overlap_Differentiation_Map_Stronger_Simpler_Verdict_Parsimony_Edge_Singh_Derives_QM_Alpha_AC_20260622.md`
- `Package_E8b_P4_Pivot_CLFV_Sister_Prediction_Replacement_Prose_Draft_PC_20260618.md`
- `Paper_Alpha_Cosmological_FixedPoint_CCC_Exploratory_v0_1_Scratch_20260603.md` [P3/post-Aug]
- `Paper_C21_ConformalReset_SeedPhoton_FirstPass_PC_20260922.md` [P3/post-Aug]
- `paper_s22_1_y_nu2_numerics.py`
- `paper_s22_1b_y_nu1_bracket_numerics.py`
- `paper_s22_1c_y_nu1_zero_param_numerics.py`
- `paper_s2_chord_closure_numerics.py`
- `Paper_S2_Chord_Closure_Synthesis_v1_0_20260524.md`
- `paper_s2_d5_factor_112_numerics.py`
- `Paper_S2_HeatKernel_Phase_I_Item_2_D_F_Yukawa_Structure_Jammer_v0_2_20260529.md`
- `paper_s2_m2_z2_split_numerics.py`
- `Paper_S2_S2A_Operator_Setup_v0_1.md`
- `Paper_S2_S2B_Coefficients_Plus_Kappa0_v0_1.md`
- `Paper_S2_S2CB_a4_Weyl_Euler_v0_1.md`
- `Paper_S2_S2CC_DF_Subleading_v0_1.md`
- `Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md`
- `Paper_S2_S2E_AC_Integration_Package_v0_1.md`
- `Paper_S2_Scope_and_Attack_Route_v0_1_20260523.md`
- `Paper_S2_v1_0_Scratch_CR_Verification_v0_1.md`
- `PC_Scoping_Memo_Corpus_State_and_Pedagogical_Opportunities_20260613.md`
- `Popular_Paper_Spectral_Action_v1.md`
- `prepare_master_pdf.py` [P1]
- `prepare_paper_pdf.py` [P1]
- `Programme_S_Paper_S6_v1_0_Canonical_Synthesis_Post_Cursor_20260526.md`
- `Publication_Title_Block_Standard_20260528.md`
- `Scratch_Adversarial_Review_AC_Wagenveld_Sprint_v0_1_20260528.md`
- `Scratch_Heat_Kernel_Cross_Check_M_R_Scoping_v0_1.md`
- `Scratch_Kappa0_to_XiV_Rename_Routing_Report_v0_1_20260528.md`
- `Scratch_M_R_BPS_Anchored_Cross_Check_v0_1.md`
- `Scratch_M_R_BPS_Anchored_Cross_Check_v0_2_Full_Lagrangian_Closure.md`
- `Scratch_M_R_Cross_Check_v0_4_Reconciliation_with_Cursor_Review.md`
- `Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_1_Seed_Amplitude_v0_1.md`
- `Sigma_t_Phi_NTE_Investigation_Direction_2_BottomUp_Jammer_v1.md`
- `Standalone_Papers_Accessibility_Tiering_Framework_v0_1_20260526.md`
- `strip_corpus_metadata.py` [P1]
- `strip_publication_tail.py` [P1]
- `Sunshine_P5_Solar_Sunshine_Verdict_REFRAME_Structural_Locked_C2_Pending_Lagrangian_8pi_negativethird_Open_Claude_Jammer_20260618.md`
- `Twistor_Theory_Axiom_Filter_Pass_Jammer_v1.md`
- `Unimodular_Gravity_Verification_CC2008_v1.md`
- `Working_Candidates_Triage_Pass2_Moves_20260922.csv` [P3/post-Aug]
- `Working_Candidates_Triage_Pass2_Summary_20260922.md` [P3/post-Aug]
- `Working_FalsifierSearch_Unitary_CPN_TwoLayer_Opening_Scoping_Claude_Jammer_20260610.md`
- `Working_Note_sqrt2pi_kappa_cfm_leg_withdrawn_20260803.md` [P3/post-Aug]

## K2 — M_R trace (8.2 × 10¹⁴)

Found **56** file(s) with an 8.2↔10¹⁴ adjacency (first matching line each):
- `_p5_prepare_test.md`:17: `With the right-handed Cartan mass scale $M_R = 8.2 \times 10^{14}$ GeV (set independently by the heaviest light-neutrino mass), the two branches give:`
- `_pass2_finalize_summary.py`:52: `if "8.2" in ln and re.search(r"10\^|10¹|e14|×10", ln):`
- `_triage_pass2_20260922.py`:394: `"8.2" in ln and re.search(r"10\^|10¹|e14|×10", ln, re.I)`
- `apply_companion_v10_17_2.py`:46: `C7_NEW_73 = """NTE v10.17.2 corpus §19.7 + Companion 12 v10.17.2 Note 4 + Companion 13 v10.17.2 §4.4 supplies m_{ν_3} = v_EW²/M_R = 0.0738 eV from M_R = M_Pl^{3/4} · v_EW^{1/4} ≈ 8.2 × 10¹⁴ GeV via th`
- `Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601 (1).md`:22: `The prediction is **≈ 1.47–1.50× too large** — the same factor whichever leg you anchor. Anchoring solar (clean): v²/M_R = m_ν₂·(8π)^(2/3) = 0.00862 × 8.574 = 0.0739 eV ⇒ M_R = 8.2×10¹⁴ GeV (corpus va`
- `Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601.md`:23: `The prediction is **≈ 1.47–1.50× too large** — the same factor whichever leg you anchor. Anchoring solar (clean): v²/M_R = m_ν₂·(8π)^(2/3) = 0.00862 × 8.574 = 0.0739 eV ⇒ M_R = 8.2×10¹⁴ GeV (corpus va`
- `clfv_cartan_ratio_numerical.py`:24: `M_R_NOM = 8.2e14  # GeV`
- `CLFV_Cartan_Ratio_Numerical_Results_20260613.md`:64: `| BR(μ→eγ) order at M_R = 8.2×10¹⁴ GeV | **~4×10⁻⁵⁹** |`
- `CO00A2~1.MD`:22: `within a factor 1.12 of the value leptogenesis requires (≈ 6.1 × 10⁹ GeV), the residual being an O(1) gauge-birth correction rather than a free parameter. The cube root is the 3-dimensionality of the `
- `COD347~1.MD`:54: `**The Majorana and Dirac mass scales.** The same spine carries the right-handed Majorana scales, cross-checked against the dedicated derivation: the lightest, M₁ = (8π)^{1/3}(M_Pl² H_GB)^{1/3} ≈ 5.4 ×`
- `COE381~1.MD`:54: `**The Majorana and Dirac mass scales.** The same spine carries the right-handed Majorana scales, cross-checked against the dedicated derivation: the lightest, M₁ = (8π)^{1/3}(M_Pl² H_GB)^{1/3} ≈ 5.4 ×`
- `COEFB4~1.MD`:54: `**m_{ν₂} = (8π)^{-2/3} v_EW² / M_R**,  with M_R = 8.2 × 10¹⁴ GeV, v_EW = 246 GeV,`
- `Companion_12_v10_17_2_Scratch_CR_Verification_v0_1.md`:64: `| 4: M_1 = 5.40 × 10⁹ GeV; M_R = 8.2 × 10¹⁴ GeV (S2-D) | ✓ Cross-checked (Pathway α) |`
- `Companion_13_v10_17_2_Scratch_CR_Verification_v0_1.md`:69: `- m_{ν_2} = 0.117 × 60,516 / (8.2 × 10¹⁴) GeV = 7,080 / 8.2 × 10¹⁴ GeV = 8.63 × 10⁻¹² GeV = 8.63 × 10⁻³ eV = **0.00863 eV** ✓ (matches stated 0.00860 within rounding)`
- `Corpus_Sunshine_Path_Audit_Results_Scratch_P0_20260525.md`:89: `| M_R = M_Pl^(3/4) × v_EW^(1/4) numerical | ✓ 0.997× corpus 8.2 × 10¹⁴ GeV |`
- `CPN_Universe_Pair_S1_Gibbons_Hartle_Conserved_Charge_Audit_Concession_Path_Likely_Hopf_Charge_Open_Claude_Jammer_20260617.md`:77: `- The pair-separation question is at **gauge birth** (T ~ M_R = 8.2×10¹⁴ GeV; ~12 orders above EWSB)`
- `CPN_Universe_Pair_T1_Jammer_Side_Parity_Computation_PASS_DERIVED_Claude_Jammer_20260617.md`:49: `The inflaton dynamics relevant for T1 are at the **gauge-birth scale** (T ~ M_R = 8.2×10¹⁴ GeV; pre-EWSB by many orders of magnitude). At this regime CPN is the real-orthogonal involution at fundament`
- `CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md`:23: `The prediction is **≈ 1.47–1.50× too large** — the same factor whichever leg you anchor. Anchoring solar (clean): v²/M_R = m_ν₂·(8π)^(2/3) = 0.00862 × 8.574 = 0.0739 eV ⇒ M_R = 8.2×10¹⁴ GeV (corpus va`
- `CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_Claude_Jammer_20260601.md`:65: `The framework's single-M_R assumption: **M_{R_1} = M_{R_2} = M_{R_3} = M_R ≈ 8.2 × 10¹⁴ GeV** (one right-handed mass for all three generations).`
- `CR2_Programme_S_F6_Collateral_Scan_Cursor_Jammer_20260601.md`:13: `Counterfactual scan: if locked corpus adopted $Y_3 = \sqrt{2/3}$ ($m_{\nu_3} = 0.0492$ eV, not $0.0738$ eV) while holding $M_R = 8.2 \times 10^{14}$ GeV and $Y_{\nu_2} = (8\pi)^{-1/3}$ fixed, **atmosp`
- `Cursor_Heat_Kernel_M_R_Critical_Review_v0_2_20260525.md`:60: `- If M_R^4 = **c** × M_Pl³ × v_EW with **c = Vol(S³) = 2π²**, then M_R is **~2.1×** too large vs corpus (8.18×10¹⁴ GeV vs 8.2×10¹⁴).`
- `Eta_Asymmetry_Magnitude_Reframing_Audit_v2.md`:67: `**Δm_eff:** the corpus has a geometric derivation of the Majorana mass scale M_R at line 1274 (§19.7, in the orbifold + J₃(𝕆) section): *"The J₃(𝕆) structure provides a natural Majorana mass scale M_R`
- `eta_Calculation.txt`:8: `Corpus quoted: 8.2 × 10¹⁴ GeV`
- `eta_precondition_check_worksheet.py`:38: `print(f"  Corpus quoted: 8.2 × 10¹⁴ GeV")`
- `gap1_pathwayA_session2_worksheet.py`:31: `M_R_corpus = 8.2e14   # GeV (corpus M_R from Hopf bundle)`
- … +31 more

## K6 — cursor_task_ledger.json

Monitoring lane reads `Working\.cursor_handoff_watch_state.json`, **not** `cursor_task_ledger.json`. Ledger retired (D7).

**Greg flag — corrupt.bak:** At Pass-1 inventory, `Working candidates\cursor_task_ledger.json.corrupt.bak` was ~1.93 GB. At Pass-2 apply time the file was **already gone** from the tree (not in candidates, Working, or Retired). Not moved by Cursor. Please check Drive trash / version history and delete if it reappears.

## Tilde / short-name identification (all retired)

Tilde/`~` files moved: **24**. Sample:

| short name | rule |
|---|---|
| `AC_HON~1.MD` | D tilde-identified default retire |
| `AC_HON~2.MD` | D tilde-identified default retire |
| `AC_RAT~1.MD` | D tilde-identified default retire |
| `ADVERS~1.MD` | D tilde-identified default retire |
| `ATTACK~1.MD` | D tilde-identified default retire |
| `CO00A2~1.MD` | K2 M_R numeric trace content |
| `CO6C86~1.MD` | D tilde-identified default retire |
| `CO21D3~1.MD` | D tilde-identified default retire |
| `CO36DE~1.MD` | D tilde-identified default retire |
| `CO82EA~1.MD` | D tilde-identified default retire |
| `CO516C~1.MD` | D tilde-identified default retire |
| `CO4419~1.MD` | D tilde-identified default retire |
| `CO6356~1.MD` | D tilde-identified default retire |
| `COD347~1.MD` | K2 M_R numeric trace content |
| `COE381~1.MD` | K2 M_R numeric trace content |
| `COEFB4~1.MD` | K2 M_R numeric trace content |
| `EMERGE~1.MD` | D tilde-identified default retire |
| `MA8073~1.MD` | D tilde-identified default retire |
| `MA9462~1.MD` | D tilde-identified default retire |
| `MAA27E~1.MD` | D tilde-identified default retire |
| `NTE_FA~1 - Copy.MD` | D tilde-identified default retire |
| `NTE_HA~1.MD` | D tilde-identified default retire |
| `NTE_IN~1 - Copy.MD` | D tilde-identified default retire |
| `NTE_IN~3.MD` | D tilde-identified default retire |

## HOLD list

**(none)** — Pass-2 cleanup retracted the over-broad D2 Part-3 full-text guard. Re-checked against Part 3 §Open work + manifest §10 In-progress/Open only; no K/D conflicts remained. Candidate twins of live P1 scripts (different SHA) retired — Working copies win.

## K4 stale register

Kept in Working (currency pass needed before use): `NTE_Reader_Glossary_Companion_v1_0.md`; `NTE_FAQ_Supplement_DRAFT_v0_2_*` (see manifest §10).

## Pass 1 report

Retired to `Working\Retired\Working_Candidates_Triage_Report_20260922.md`.

---

# Pass 3 — retire over-kept set (2026-09-22 22:24 UTC+12:00)

**Handoff:** Handoffs\Handoff_AC_to_Cursor_Working_Triage_Pass3_Retire_OverKept_20260922.md

K2 M_R-content and fibre-modulus content keep rules **withdrawn**. List A retired.

## Pass 3 moves: **59** → Working\Retired\

- _p5_prepare_test.md
- apply_companion_v10_17_2.py
- Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601 (1).md
- Candidate_Pathway_Neutrino_Atmospheric_ChiralitySuperposition_KillingSpinor_Scratch_Claude_20260601.md
- CO00A2~1.MD
- COD347~1.MD
- COE381~1.MD
- COEFB4~1.MD
- Companion_12_v10_17_2_Scratch_CR_Verification_v0_1.md
- Companion_13_v10_17_2_Scratch_CR_Verification_v0_1.md
- Connes_Programme_Charter_v1.md
- Connes_Programme_Launch_Plan_v1.md
- Corpus_Sunshine_Path_Audit_Results_Scratch_P0_20260525.md
- CPN_Universe_Pair_S1_Gibbons_Hartle_Conserved_Charge_Audit_Concession_Path_Likely_Hopf_Charge_Open_Claude_Jammer_20260617.md
- CPN_Universe_Pair_T1_Jammer_Side_Parity_Computation_PASS_DERIVED_Claude_Jammer_20260617.md
- CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md
- CR2_Programme_S_F6_Collateral_Scan_Cursor_Jammer_20260601.md
- Eta_Asymmetry_Magnitude_Reframing_Audit_v2.md
- eta_Calculation.txt
- eta_precondition_check_worksheet.py
- gap1_pathwayA_session2_worksheet.py
- Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1_20260524.md
- Jammer_M2_Z2_Split_Derive_v0_1_20260524.md
- M1_From_Geometry_E_search.md
- Master_v10_10_Tier1_Patch_Instructions_Programme_S_Spine_20260523.md
- Master_v10_14_Tier2d_Patch_Instructions_PaperS2_S2C_20260523.md
- Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523 (1).md
- Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523.md
- Master_v10_8_to_v10_9_Patch_Instructions_A6_FalsifiabilityCatalogue_Consolidation_20260523.md
- NTE_Pedagogical_Pivot_Companions_Register.md
- NTE_Provenance_Audit_New_vs_ReDerived_vs_Imported_First_Pass_AC_20260622.md
- NTE_Standalone_Claims_Inventory_v0_1_20260524.md
- NTE_Standalone_Claims_Inventory_v0_2_20260524.md
- NTE_vs_Singh_Octonionic_Theory_Precise_Overlap_Differentiation_Map_Stronger_Simpler_Verdict_Parsimony_Edge_Singh_Derives_QM_Alpha_AC_20260622.md
- Package_E8b_P4_Pivot_CLFV_Sister_Prediction_Replacement_Prose_Draft_PC_20260618.md
- paper_s22_1_y_nu2_numerics.py
- paper_s22_1b_y_nu1_bracket_numerics.py
- paper_s22_1c_y_nu1_zero_param_numerics.py
- paper_s2_chord_closure_numerics.py
- Paper_S2_Chord_Closure_Synthesis_v1_0_20260524.md
- paper_s2_d5_factor_112_numerics.py
- paper_s2_m2_z2_split_numerics.py
- Paper_S2_HeatKernel_Phase_I_Item_2_D_F_Yukawa_Structure_Jammer_v0_2_20260529.md
- Paper_S2_S2A_Operator_Setup_v0_1.md
- Paper_S2_S2B_Coefficients_Plus_Kappa0_v0_1.md
- Paper_S2_S2CB_a4_Weyl_Euler_v0_1.md
- Paper_S2_S2CC_DF_Subleading_v0_1.md
- Paper_S2_S2E_AC_Integration_Package_v0_1.md
- Paper_S2_Scope_and_Attack_Route_v0_1_20260523.md
- Paper_S2_v1_0_Scratch_CR_Verification_v0_1.md
- PC_Scoping_Memo_Corpus_State_and_Pedagogical_Opportunities_20260613.md
- Popular_Paper_Spectral_Action_v1.md
- Programme_S_Paper_S6_v1_0_Canonical_Synthesis_Post_Cursor_20260526.md
- Scratch_Adversarial_Review_AC_Wagenveld_Sprint_v0_1_20260528.md
- Scratch_Kappa0_to_XiV_Rename_Routing_Report_v0_1_20260528.md
- Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_1_Seed_Amplitude_v0_1.md
- Sigma_t_Phi_NTE_Investigation_Direction_2_BottomUp_Jammer_v1.md
- Twistor_Theory_Axiom_Filter_Pass_Jammer_v1.md
- Working_FalsifierSearch_Unitary_CPN_TwoLayer_Opening_Scoping_Claude_Jammer_20260610.md

## Neither list A nor list B (report only, not moved)

(none — every remaining Working\ top-level file matches list B: P1 / P3 / open-item / K3–K5.)

## C — Tilde identification (24 files in Retired)

| short name | first heading | date/version/status line | probable original long filename |
|---|---|---|---|
| AC_HON~1.MD | # AC honest-scope revision → Paper P4D v0.2 (drop-in replacements) | **Date:** 2026-06-24 | (from heading) AC honest-scope revision → Paper P4D v0.2 (drop-in replacements) |
| AC_HON~2.MD | # AC honest-scope revision → Paper P4D v0.3 (propagating the descent verdict) | **Date:** 2026-06-24 | (from heading) AC honest-scope revision → Paper P4D v0.3 (propagating the descent verdict) |
| AC_RAT~1.MD | # AC ratification-sight — Paper P4D (antilinear θ₂₃ / μτ-reflection / CPN unification) v0.1 | **Date:** 2026-06-24 | (from heading) AC ratification-sight — Paper P4D (antilinear θ₂₃ / μτ-reflection / CPN unification) v0.1 |
| ADVERS~1.MD | # Adversarial Pass on Paper P4D v0.1 (Scratch) — Independent Jammer-Side Triple-Check — Three Load-Bearing Claims HOLD; Three Minor Recommendations; Open Litera | **From:** Claude Jammer (specialist session — independent triple-check per paper status block; morning sync complete; manifest rev10 binding) | (from heading) Adversarial Pass on Paper P4D v0.1 (Scratch) — Independent Jammer-Side Triple-Check — Three Load-Bea |
| ATTACK~1.MD | # Attack on Literal-Operator-Identity Derivation (P4D Rec 1) — Bilateral CPN J ≢ Generation σ_1↔σ_2 Z_2 at Operator Level — TYPE IDENTITY HOLDS, LITERAL IDENTIT | **Date:** 2026-06-24 | (from heading) Attack on Literal-Operator-Identity Derivation (P4D Rec 1) — Bilateral CPN J ≢ Generation σ_1↔σ_2 Z_ |
| CO00A2~1.MD | ## Abstract | title: "The lightest right-handed Majorana mass from S³ flux quantisation" | (from heading) Abstract |
| CO21D3~1.MD | ## Abstract | title: "The neutrino as unresolved geometry: neither particle nor antiparticle" | (from heading) Abstract |
| CO36DE~1.MD | ## Abstract | title: "There is no pair: entanglement as single-object geometry" | (from heading) Abstract |
| CO4419~1.MD | ## Abstract | title: "The hierarchy problem is a resonance" | (from heading) Abstract |
| CO516C~1.MD | ## Abstract | title: "The Born rule is the Hopf fibration" | (from heading) Abstract |
| CO6356~1.MD | ## Abstract | title: "Quantisation is compactness" | (from heading) Abstract |
| CO6C86~1.MD | ## Abstract | title: "The cosmological constant in NTE: unimodular suppression on a boundary-only geometry" | (from heading) Abstract |
| CO82EA~1.MD | # Companion papers — triage and clean-up plan (three-tier taxonomy + audit) | **Author:** AC · **Date:** 2026-06-23 · **Status:** internal plan. Assigns each Companion to a tier (2 distinctive / 3 pedagogical) with the audit and prior-art | (from heading) Companion papers — triage and clean-up plan (three-tier taxonomy + audit) |
| COD347~1.MD | ## Abstract | title: "Notes from one chord: structural results from a single heat-kernel computation" | (from heading) Abstract |
| COE381~1.MD | ## Abstract | title: "Notes from one chord: structural results from a single heat-kernel computation" | (from heading) Abstract |
| COEFB4~1.MD | ## Abstract | title: "The second neutrino Yukawa from the D5 inverse" | (from heading) Abstract |
| EMERGE~1.MD | # EMERGENCE MAP — Jammer Blind Derivation of f_3/f_2 from N-Clock Geometry — KILL #2 FIRES under Canonical Metric (S³×S¹ block-diagonal; σ_2, σ_3 both spatial m | **Date:** 2026-06-23 | (from heading) EMERGENCE MAP — Jammer Blind Derivation of f_3/f_2 from N-Clock Geometry — KILL #2 FIRES under Canon |
| MA8073~1.MD | ## XVII. Parameter accounting | title: "Non-Temporal Emergence — Part 3 of 3: Accounting, Falsifiability, and Open Work" | (from heading) XVII. Parameter accounting |
| MA9462~1.MD | ## VIII. The gauge birth | title: "Non-Temporal Emergence — Part 2 of 3: Structure and Dynamics" | (from heading) VIII. The gauge birth |
| MAA27E~1.MD | ## Abstract | title: "Non-Temporal Emergence — Part 1 of 3: Foundations and Method" | (from heading) Abstract |
| NTE_FA~1 - Copy.MD | # NTE FAQ Supplement — anticipated reader questions, brief answers + pointers (DRAFT v0.1) | **Author:** AC  **Date:** 2026-06-25 | (from heading) NTE FAQ Supplement — anticipated reader questions, brief answers + pointers (DRAFT v0.1) |
| NTE_HA~1.MD | # NTE Handoffs/ full-window triage (05-27 → 06-23) + KSIP excision list | **Date:** 2026-06-23 | (from heading) NTE Handoffs/ full-window triage (05-27 → 06-23) + KSIP excision list |
| NTE_IN~1 - Copy.MD | # Investigation note — offset-pattern CHASE RESULT (the ≈1.5 cluster dissolves; one real tension survives) | **Date:** 2026-06-24 | (from heading) Investigation note — offset-pattern CHASE RESULT (the ≈1.5 cluster dissolves; one real tension survi |
| NTE_IN~3.MD | # Investigation note — does the neutrino's LH/RH chirality superposition extend to a 4π/8π superposition? | **Date:** 2026-06-25 | (from heading) Investigation note — does the neutrino's LH/RH chirality superposition extend to a 4π/8π superpositi |

## Held

**0**

