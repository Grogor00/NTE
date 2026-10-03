---
title: "Paper Scope-Alignment Sweep Results"
author: "Cursor Main"
date: "2026-06-13 (Δ1–Δ8 grep pass — AC ratification pending)"
---

**Re:** `Handoff_AC_to_Cursor_PC_Scope_Alignment_Delta_List_AND_Sweep_All_Candidate_Papers_Publish_Safety_Gate_20260613.md` + amendment `Handoff_AC_to_Cursor_PC_AMENDMENT_Sweep_Includes_Public_Zenodo_v2_Papers_For_v3_Refresh_20260613.md`

**Method:** Cursor Main grep pass against Δ1–Δ8 triggers. **Flag-and-propose only** — AC ratifies fixes before corpus patch. Wording proposals draw from AC CURRENT forms in scope-alignment handoff.

**Legend:** PUBLIC-NOW = in Zenodo v2 deposit (2026-06-01). Verdict: **CLEAN** | **FIXES-REQUIRED** | **VERIFY-ONLY** (likely clean post-v2; confirm).

---

## Summary table

| Paper | PUBLIC-NOW | Δ fires | Verdict |
|-------|------------|---------|---------|
| `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` | y | Δ1, Δ6, Δ8 | **FIXES-REQUIRED** |
| `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` | y (legacy filename) | Δ1, Δ6, Δ8 | **FIXES-REQUIRED** |
| `Paper_S2_v1_0_Consolidation_20260525.md` | n (held) | Δ1 (retired OK), Δ6, Δ8 | **FIXES-REQUIRED** (internal language) |
| `Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md` | y | — | **VERIFY-ONLY** → likely **CLEAN** |
| `Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md` | y | — | **VERIFY-ONLY** → likely **CLEAN** |
| `Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md` | y | — | **VERIFY-ONLY** → likely **CLEAN** (B3 language patched) |
| `Paper_OctonionExtension_v10_9.md` | n | Δ8 | **VERIFY-ONLY** |
| `Paper_S1_v0_4.md` | n | Δ8 | **VERIFY-ONLY** |
| `Paper_Kappa_AB_v10_17_2.md` | n | Δ8 | **VERIFY-ONLY** |
| `Paper_Popular_v10_8_Full_Edition.md` | y | Δ8 | **FIXES-REQUIRED** (internal CR2 tags) |
| `Paper_Popular_v10_8_Reader_Edition.md` | n | Δ8 | **FIXES-REQUIRED** (internal CR2 tags) |
| `NTE_v10_17_Part1_Foundations.md` | y | Δ4, Δ8 | **VERIFY-ONLY** |
| `NTE_v10_17_Part2_Structure.md` | y | Δ8 | **VERIFY-ONLY** |
| `NTE_v10_17_Part3_Accounting.md` | y | Δ1, Δ3, Δ8 | **FIXES-REQUIRED** (v3 must rebuild from current) |
| Pedagogical pivots (10) | n | Δ8 (some) | **VERIFY-ONLY** |
| Book deposit (separate DOI) | y | Δ1 | **FIXES-REQUIRED** — Package C applied 2026-06-13 to Ch 10/12/15/Prelude/Appendix A |

---

## Per-paper detail

### P5 Solar — `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` (PUBLIC-NOW)

| Δ | Location | Offending text (summary) | Proposed fix (AC CURRENT form) |
|---|----------|--------------------------|--------------------------------|
| **Δ1** | Abstract parity contrast; §6 tier register (~L47, L153) | Still states Λ prediction at **$1.05\times$ observed** and $\Lambda_{\mathrm{NTE}}^{\mathrm{pred}} \approx 1.05 \times \Lambda_{\mathrm{obs}}$ as live Tier B+ contrast | Replace with: **structural unimodular quietness stands**; **numeric 1.05× chain RETIRED** (a₄=0); Λ is open work pending β_NTE geometric derivation — parity contrast only, not a live Λ number |
| **Δ5** | — | Solar 0.993× + atmospheric 1.49× gap already correct (CR2 B1) | **CLEAN** on Δ5 |
| **Δ6** | §6 (~L155) | `genuine **with caveats** per CR2 tiering — **AC disposition pending**` for n_s | Replace with settled outward wording: **n_s = 0.9685, genuine with stated caveats (β_NTE-chain + slow-roll import)** — remove "AC disposition pending" |
| **Δ8** | Multiple | `CR2 / B1`, `CR2 B1`, `Tier 2g` in references | Translate to neutral scientific language for publication; remove internal programme tags from body |

**Verdict:** **FIXES-REQUIRED** — blocks v3 Zenodo until Δ1 + Δ6 patched and AC-ratified.

---

### Paper S2 — `Paper_S2_v1_0_Consolidation_20260525.md` (held; S2 publish-blocked per AC break-repair handoff)

| Δ | Notes |
|---|-------|
| **Δ1** | Numeric 1.05× consistently **reroute-or-retire** with strikethrough — **CLEAN** on live-claim test |
| **Δ6** | Header `pending Cursor Drive sync`; references `AC disposition` patterns absent for n_s |
| **Δ8** | Extensive `CR-H1`, `CR-H2`, `CR2` internal labels throughout — acceptable for framework-internal paper but **must strip for outward Zenodo extract** |

**Verdict:** **FIXES-REQUIRED** for publication extract; plus **AC S2 break-repair gate** (BREAK-1 K(Φ) re-derivation, BREAK-2 §12.3 strike, BREAK-3 scope statement) — separate from Δ sweep.

---

### Master Part 3 — `NTE_v10_17_Part3_Accounting.md` (PUBLIC-NOW — **v3 must rebuild from current**)

| Δ | Location | Issue | Proposed fix |
|---|----------|-------|--------------|
| **Δ1** | §17.5.18 (~L316) | Still shows `≈ 1.05× observed Λ` in formula line before reroute note | Lead with structural mechanism; move 1.05× to historical/reroute-only clause per CR-H2 CURRENT form |
| **Δ3** | §17.5.12 | CLFV Category H with six qualifiers — **CURRENT** (ratified 2026-06-13) | **CLEAN** — ensure v3 PDF uses this section |
| **Δ8** | Throughout §17.5 | CR2, CR-H2, Tier 2g register language | Internal corpus OK; v3 PDF for external readers may need neutral register summary per AC |

**Verdict:** **FIXES-REQUIRED** for v3 Part 3 PDF (rebuild from current master, not June-1 snapshot).

---

### Popular Full + Reader — (Full = PUBLIC-NOW)

| Δ | Issue | Proposed fix |
|---|-------|--------------|
| **Δ1** | Λ ~~1.05×~~ strikethrough + reroute-or-retire — **CURRENT** | **VERIFY-ONLY** — confirm no unstrikethrough live 1.05× claims remain |
| **Δ8** | Header `CR-H1/H2 sync (Cursor Main…)`; body `CR2`, `AJ-06`, patch footers | Remove internal sync headers and patch footers from v3 publication PDF; translate to neutral reader-facing tier language |

**Verdict:** **FIXES-REQUIRED** on Δ8 hygiene for v3; Δ1 likely **CLEAN** on verify.

---

### F1, P4, Hopf κ₀ — (PUBLIC-NOW v2 set)

Spot-check: no Δ1/Δ5 stale neutrino or Λ live claims found in grep pass.

**Verdict:** **VERIFY-ONLY** → likely **CLEAN** for v3 (confirm per-file read).

---

### Octonion, S1, Kappa A+B — (held candidates)

No Δ1/Δ2/Δ4/Δ5 fires in quick pass. Δ8 internal references may exist in headers.

**Verdict:** **VERIFY-ONLY**

---

### Book deposit (separate Zenodo DOI)

Package C cascade applied 2026-06-13 to canonical `Book/` Ch 10, 12, 15, Prelude, Appendix A. Ch 13 already reroute lead.

**Verdict:** **FIXES-REQUIRED** → **applied** (await PC verification). `Book_with_TP/` still stale — not in deposit refresh until separate sprint.

---

## Δ2 / Δ4 quick corpus scan (publication-bound)

| Δ | Papers grep | Result |
|---|-------------|--------|
| **Δ2** C3 birefringence sky-test | No "observable GW chirality" or "0.3° birefringence prediction" in candidate Papers/ set | **CLEAN** on quick pass |
| **Δ4** CCC sole-survivor | No `sole surviving` / `only viable` in Papers/ | **CLEAN** on quick pass |

---

## Routing (per AC handoff)

| Stream | Action |
|--------|--------|
| **AC** | Ratify proposed fixes; prioritise P5 v0.3 Δ1+Δ6 for v3 Zenodo |
| **Cursor Main** | Apply AC-ratified patches; stage v3 bundle after fixes |
| **Greg** | Zenodo v3 publish click after AC pre-check |
| **Cursor Jammer** | BREAK-1 K(Φ) re-derivation (S2 gate) |
| **Scratch** | BREAK-5 κ₀ independence investigation |

---

## Related AC inbound (2026-06-13) — status

| Handoff | Status |
|---------|--------|
| CR-V1 + splits + MB stamp | ✅ Done |
| Link-reference index TASK | 🔄 In progress — `Working/build_ac_file_reference_index.py` + `Workflow/INDEX_NTE_FileReference_AC.md` v0.1 |
| Scope-alignment sweep | ✅ This file — AC ratification pending |
| S2 break-repair routes | ⏳ BREAK-2 render eligible; BREAK-1 Jammer; BREAK-3 AC scope para |
| Zenodo v3 amendment | ⏳ Blocked on sweep fixes + Part 3 rebuild |

---

— Cursor Main, 2026-06-13.
