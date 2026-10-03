# Pedagogical-pivot companions — canonical register

**Owner:** PC (authoring + CR) · Cursor (PDF build after PC ship) · Greg (ratify)  
**Discipline brief:** `Handoffs/Handoff_PC_to_Cursor_Pedagogical_Pivot_Versions_Tier1_Standalone_Papers_20260528.md` §4–§9  
**Voice register:** `Working/NTE_Book_Popular_Voice_Register.md` · `.cursor/rules/nte-book-popular-voice.mdc`

---

## Version rule

| Label | Meaning | Location |
|-------|---------|----------|
| **PC v1.0** | Canonical outreach companion; PDF + optional Zenodo | `Papers/` only |
| **PC v0.1** | PC first draft (F1 only; superseded) | `Papers/depreciated/` |
| **Cursor v0.1** | Cursor reference draft only — **not canonical** | `Papers/depreciated/` |

Target filename for every companion: `Paper_<Stem>_Pedagogical_Pivot_v1_0_<YYYYMMDD>.md`

---

## Companion ledger (10 papers)

| # | Parent technical | Canonical companion | Status | Superseded drafts |
|---|------------------|---------------------|--------|-------------------|
| 1 | `Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md` | `Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 (PC CR PASS — calibration anchor) | `depreciated/…_v0_1_20260528.md` |
| 2 | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 3 | `Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md` | `Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 4 | `Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md` | `Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 5 | `Paper_Kappa_AB_v10_17_2.md` | `Paper_Kappa_AB_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 6 | `Paper_S6_M_R_Heat_Kernel_v1_0.md` | `Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30; **outreach HOLD (AC pending)** — Scratch atmospheric-match flag 2026-05-31 (~1.48× not 0.997×) | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 7 | `Paper_S2_v1_0_Consolidation_20260525.md` | `Paper_S2_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 8 | `Paper_S1_v0_4.md` | `Paper_S1_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 + observational-scope § (Cursor 2026-05-31; **PC read PASS** 2026-05-31 — canonical as-shipped) | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 9 | `Paper_OctonionExtension_v10_9.md` | `Paper_OctonionExtension_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |
| 10 | `Paper_External_Empirical_Surface_Clean_Gates_v0_1_20260530.md` | `Paper_External_Empirical_Surface_Clean_Gates_Pedagogical_Pivot_v1_0_20260530.md` | **PC v1.0 shipped** 2026-05-30 | `depreciated/…_v0_1_20260530.md` (Cursor) |

**Batch handoff:** `Handoffs/Handoff_PC_to_Cursor_AC_Pedagogical_Pivot_Companions_v1_0_Batch_Completion_20260530.md`

**Not companions:** `Paper_Popular_v10_8_Full_Edition.md`, `Paper_Popular_v10_8_Reader_Edition.md` (separate lay editions).

**Reader glossary (non-pivot):** `Working/NTE_Reader_Glossary_Companion_v1_0.md` (v1.4). PDF: `paper-build/pdf-out/NTE_Reader_Glossary_Companion_v1_0.pdf`. **PC read PASS** 2026-05-31; **AC ratified for consistency/internal use** 2026-05-31 (pre-distribution: external-definition scan + Greg sign-off). Not a Zenodo tier.

---

## PC queue (Greg 2026-05-30) — **CLOSED**

**Handoff:** `Handoffs/Handoff_Greg_to_PC_Pedagogical_Pivot_Companions_v1_0_Queue_20260530.md`

All 10 PC v1.0 companions shipped 2026-05-30. Cursor PDF rebuild + register reconciliation complete 2026-05-31.

---

## PDF build (`paper-build/build-pdfs.ps1`)

**Current:** all **10** PC v1.0 pedagogical pivots in `$pedagogical` array + Reader Glossary in `$workingDocs`. PDFs in `paper-build/pdf-out/`.

Cursor v0.1 PDFs in `pdf-out/` are stale — do not use for outreach.

---

## Zenodo

Live corpus tier (8 files) unchanged. Pedagogical pivots are outreach-only until Greg expands deposit deliberately.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | **Hotfix sprint applied** (PC ratification, Cursor execution): S2 pivot Note 5 + Honest scope retreats (Λ 1.05× retired post CR2; atmospheric removed from Tier A list); κ pivot opening / two-stages / why-κ₀<1 / what-would-break-it / provenance (Killing-spinor channels → SU(2)-adjoint gauge components per Bär 1993, mirrors Hopf pivot PS-05); register row 2 parent v0_2 → v0_3; Clean Gates pivot adds CLFV Category H block (first ratified lab-physics discriminator, conditional six-qualifier per AC 2026-06-13). PDFs rebuilt: S2 pivot, κ pivot, Clean Gates pivot. |
| 2026-05-31 | **AC inventory reconciliation confirmed** — 10 pivot sources + 10 PDFs + glossary match shipped state; numerics on PC verification (AC spot-check on request); glossary AC ratified consistency/internal use |
| 2026-05-31 | Register reconciled: rows 2–7, 9–10 → PC v1.0 shipped 2026-05-30; S1 observational-scope § PC PASS; all 10 pivots in build-pdfs; glossary PC read noted |
| 2026-05-30 | 10 PC v1.0 pedagogical-pivot companions shipped (F1 CR-passed; P5, P4, Hopf, κ, S6, S1, S2, Octonion, Clean Gates drafted) — `Handoff_PC_to_Cursor_AC_…_Batch_Completion_20260530.md` |
| 2026-05-30 | Register created; 9 Cursor v0.1 drafts moved to `depreciated/`; PC v1.0 queue filed |
