# Handoff — AC → Cursor: Working-candidates triage, PASS 2 (disposition rules)

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-22
**In response to:** `Handoffs\Handoff_Cursor_to_AC_Working_Candidates_Triage_Complete_20260922.md` and `Working\Working_Candidates_Triage_Report_20260922.md`
**Status:** Greg-directed. Pass 1 was correct against AC's rules; AC's rules were too cautious (758 held). Pass 2 replaces them with decisive disposition rules. **Target: ≤ 25 held.**
**Addressing:** name/path only (discipline 9).

---

## 0. Correction — the "render-blocking" finding is withdrawn (AC error)

AC's Pass 1 handoff wrongly stated that the live `strip_corpus_metadata.py` lives in `paper-build\`. **It lives in `Working\`** — the 2026-08-04 ORPHAN_SEE fix was applied there, and your own report confirms `Working\strip_corpus_metadata.py` carries the corrected pattern. `Working\__pycache__\` holds compiled `strip_corpus_metadata`, `prepare_paper_pdf`, and `strip_publication_tail` — proof they are imported from `Working\` at render time.

**Nothing is missing. Do not restore anything to `paper-build\`.** Leave `Working\__pycache__\` alone (it is the pipeline's own cache; it regenerates).

---

## 1. PROTECT — never move (overrides every rule below)

- **P1** Every script invoked or imported by the render pipeline. Derive the list from `render-all-clean.ps1` and the imports of `prepare_paper_pdf.py`; include at minimum `Working\strip_corpus_metadata.py`, `Working\prepare_paper_pdf.py`, `Working\strip_publication_tail.py`. Report the derived list.
- **P2** `Working\Farnsworth_Archive_Pull_20260802\` and all contents.
- **P3** Anything in `Working\` modified **on or after 2026-08-01** (post-rebuild working era), unless it is a byte-identical duplicate.
- **P4** `Working\Working_Candidates_Triage_Report_20260922.md` and this pass's outputs.

---

## 2. KEEP rules — destination `Working\` (from candidates) or stays (in `Working\`)

**K1 — cited.** The filename or its stem is cited in any file under `Core_Papers\`, `Pedagogical_Notes\`, `Book\`, or `Popular_Editions\`. Report the citing file.

**K2 — input to an open item.** Only these:
- *σ↔generation dictionary (Item 1) and TM1 idempotent (Item 8):* `CHARTER_GATE1_*`, `GATE2_*`, `GATE3_*`, `GATE4*_*`, `GATE5_*`, `GATE6*_*`, `CHARTER_P4D_*`, `Investigation_P4D_*`, `FS_Geometry_Finding_Theta23_*`, `M1_Sigma3_Cartan_Mode_Derivation_v1.md`, `CR2_Programme_S_Sigma3_*`.
- *Route-B E(Φ_NTE) / Paper S2 build:* `farnsworth_stage*.py`.
- *M_R figure trace (PC's Appendix C blocker):* **any** file, of any name, containing `8.2` adjacent to `10^{14}`, `10¹⁴`, `×10^14`, or `e14`. Keep it **and report the matching line verbatim with filename** — this is the answer PC needs. Also keep `Cursor_Heat_Kernel_M_R_Critical_Review_*` and `CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_*`.
- *T_GB fibre-modulus identification (open, Companion 12):* files containing `fibre modulus` or `fiber modulus`, or `β_GB` together with `√(2π)` / `sqrt(2*pi)`.

**K3 — reproducibility for live canonical results.** `clfv_cartan_ratio_numerical.py` with `clfv_cartan_ratio_numerical_results.json` and `CLFV_Cartan_Ratio_Numerical_Results_20260613.md` (Companion 18); `kappa_closure_g1_adversarial_jammer.py`, `kappa_closure_p2eqp_check.py`, and the three `KAPPA_CLOSURE_*` result notes (κ closure).

**K4 — standing guidance and unique reader assets, if no successor exists in `Pedagogical_Notes\`, `Book\` or `Popular_Editions\`:** `NTE_Book_Title_and_Pratchett_Discipline_*`, `NTE_Book_DeAI_Voice_Pass_*`, `NTE_Book_Popular_Voice_Register.md`, `NTE_Book_Appendix_and_Corpus_Links_Discipline_*`, `NTE_Acronym_Naming_Discipline_*`, `Publication_Title_Block_Standard_*`, `Standalone_Papers_Accessibility_Tiering_Framework_*`, `NTE_Reader_Glossary_Companion_v1_0.md`, `NTE_FAQ_Supplement_DRAFT_v0_2_*`. The last two predate the August withdrawals — keep, and register each in manifest §10 as *"kept, stale vs v10.19, needs PC currency pass before any use."*

**K5 — octonionic neutrino-mixing standalone** (`NTE_Octonionic_Spine_Neutrino_Mixing_Sector_v0_2_DRAFT_White*.pdf/.tex`): compare against `New folder\` (manifest home of the octonionic standalones). Same or later version there → R1/Retired. Otherwise keep in `Working\` and report.

**K6 — `cursor_task_ledger.json`:** keep only if your current monitoring lane reads it. Say which.

---

## 3. RETIRE rules — destination `Working\Retired\`

Anything not caught by P or K, in **either** folder, retires. For clarity, this explicitly includes:

- **D1 — closed May–June process material.** `CR2_*`, `CR4_*`, `CR_Question_*`, `Jammer_*`, `AC_Patch_*`, `AC_Tier2g_*`, `AC_Bulk_Boundary_*`, `AC_Lambda_Pathways_*`, `AC_Full_Corpus_Reading_Register_*`, `AC_Wagenveld_*`, `Master_v10_*`, `Master_Part_3_*`, `MASTER_REBUILD_*`, `Companion_v10_8_*`, `Companion_1[123]_v10_17_2_Scratch_CR_Verification_*`, `LB5_*`, `LB6_*`, `BR5_*`, `LCDM_*`, `Load_Bearing_Blocks_*`, `Mu_xN_*`, `H_GB_*` (unless K2), `J6_*`, `NTE_PP_Audit_*`, `NTE_Pedagogical_Pivot_*`, `PC_*`, `Chapter_NEW_*`, `NTE_Session_Writeup_*`, `NTE_Corpus_Sitrep_*`, `Comprehensive_Status_Update_*`, `CRITICAL_UPDATE_*`, `DRAFT_CatchUp_*`, `NTE_Recording_Gap_Audit_*`, `Drive_Sync_Manifest_*`, `Corpus_Gap_*`, `Corpus_Sunshine_*`, `NTE_CR2_Sunshine_*`, `Paper_Scope_Alignment_*`, `Cursor_*` audits/reviews, `NTE_Corpus_Critical_Review_*`, `NTE_Extension_Scorecard_*`, `NTE_Unified_Corpus_Network_Map_*`, `NTE_Ontological_Bridge_*`, `NTE_Book_Open_Future_*`, `Greg_Tier1_Standalone_Upload_*`, `NTE_Standalone_Claims_Inventory_*`, `Compatibility_Catalogue_*`, `II_0_Graded_Criteria_*`.
- **D2 — concluded or dormant research threads whose results are integrated or recorded** (verdicts exist; nothing in Part 3's open list or manifest §10 depends on them): `Connes_Programme_*`, `NTE_Connes_Programme_*`, `BF2020_*`, `Filter_Report_*`, `Cross_Fertilization_*`, `Wagenveld_*`, `Jammer_Wagenveld_*`, `C3_Anisotropic_*`, `CPN_Universe_Pair_*`, `CRUNCH_*`, `Gate0_Worksheet_*`, `Investigation_FS_*`, `CHARTER_FS_*`, `AC_Assessment_Scratch_FS_*`, `NTE_Note_CPN_*`, `Assessment_*`, `BMV_*`, `Cosmic_Dipole_*`, `Connes_Rovelli_*`, `External_*`, `KSIP_*`, `Kletetschka_2025_extracted.txt`, `Draft_Outreach_*`, `NTE_Time_Dimension_Count_*`, `NTE_vs_Singh_*`, `NTE_x_Singh_*`, `NTE_Provenance_Audit_*`, `NTE_External_Positioning_*`, `NTE_Governance_Note_*`, `NTE_Investigation_Note_*`, `NTE_Visualisation_*`, `Exploration_*`, `compass_artifact_*`, `CLFV_2A_Extension_*`, `BH_Nthickness_*`, `AC_Foundations_Probe_*`, `EXTERNAL_ColdReferee_*`, `Programme_S_*`, `Paper_PhiNTE_*`, `Paper_A1_*`, `Paper_A2_*`, `P1_*`, `P5_v0_3_*`, `Cursor_BranchI_*`.
  **Guard:** before retiring any D2 file, grep Part 3's open list and manifest §10 for the file's distinctive topic words. A hit → HOLD and report the hit.
- **D3 — carriers of withdrawn or retired content.** `Candidate_Pathway_Neutrino_*ChiralitySuperposition*`, `Companion_Paper_7a_Neutrino_as_Chirality_Superposition_*` (retired strobe/chirality-superposition ontology); `n_s_Wick_Rotation_*` (superseded by Companion 17); `Eta_*`, `eta_*` (η demoted to structural consistency); `Derivation_Y3_*`; `lcdm_bao_void_bias.py` and `*Void_Bias*` (superseded by the 2026-08 forward model, which reversed the DESI claim).
- **D4 — spent calculations and numerics for superseded work.** `j1_*`, `j4_*`, `j6_*`, `lcdm_*`, `lambda_*`, `lb1_*`, `m1_*`, `br2d_*`, `bh_*`, `mu_xN_*`, `gap1_*`, `h_gb_*`, `cr2_*`, `alpha_*`, `pc03_*`, `paper_s22_*`, `p5_*`, `healpix_ring.py`, `*_Calculation.txt`.
- **D5 — spent tooling.** Every script in `Working candidates\` not protected by P1. If a candidate script **is** invoked by the pipeline and **no** live copy exists → HOLD (pipeline gap). Otherwise retire.
- **D6 — ID caches.** `INDEX_NTE_Canonical_Drive_IDs_*` → Retired. It is the exact failure mode discipline 9 forbids.
- **D7 — registries, queues, ledgers.** `NTE_CR2_Execution_Queue.json`, `NTE_CR2_Open_Work_Registry.json`, `NTE_CR2_Registry_Waves.json`, `alpha_to_beta_*.json`, `consolidated_*`, and `cursor_task_ledger.json` unless K6. **`cursor_task_ledger.json.corrupt.bak` (1.93 GB) → Retired, and flag it to Greg for deletion** — it is consuming Drive space for nothing.

**Tilde and short names** (`CO…~1.MD`, `AC_HON~1.MD`, `ADVERS~1.MD`, `ATTACK~1.MD`, `EMERGE~1.MD`, `MA…~1.MD`, `NTE_HA~1.MD`, `NTE_IN~n.MD`, `NTE_FA~1 - Copy.MD`, and every other `~` file): read the header, identify the document, then apply P/K/D to the identified document. Report the identification for each (short name → document title → rule). Do not rename.

**Files with ` (1)` or ` - Copy` in the name:** compare against the unsuffixed twin; identical → Retired; different → keep the later-modified one under K/D and retire the other.

---

## 4. HOLD only for

- a K/D conflict (a file matches both),
- a D2 guard hit,
- a pipeline gap (D5),
- an unreadable or unidentifiable file.

Each held item gets **three lines**: what it is, which rules conflict, what decision AC or Greg needs to make.

---

## 5. Deliverables — keep them readable

The Pass 1 report is 1.27 MB, too large to verify through Drive. For Pass 2:

1. **`Working\Working_Candidates_Triage_Pass2_Summary_20260922.md`** — **under 40 KB**:
   - counts per rule;
   - the full KEEP list (filename → rule);
   - the M_R trace result (K2) — matching lines verbatim, or a plain "no occurrence of 8.2 × 10¹⁴ found in either folder";
   - the tilde/short-name identification table;
   - the derived P1 pipeline list;
   - the HOLD list, three lines each.
2. **`Working\Working_Candidates_Triage_Pass2_Moves_20260922.csv`** — one row per moved file: filename, rule, destination.
3. Retire the Pass 1 report to `Working\Retired\` once the Pass 2 summary exists.
4. Completion handoff to `Handoffs\`, addressed to AC.
5. Update the manifest §10 in-progress line with the new held count.

Same guards as Pass 1: move never copy, no deletes, no renames, SHA-256 on collisions, nothing outside `Working\` and `Working candidates\`.

---

— AC, 2026-09-22.
