# Handoff — Cursor Main → AC: deposit corpus unify to v10.19.0 — COMPLETE

**From:** Cursor Main  
**To:** AC  
**Cc:** Greg  
**Date:** 2026-08-09  
**Fulfils:** plan *Unify deposit corpus to v10.19.0* (Greg-authorized; Book deferred)

---

## Policy held
- Deposit lanes only: `Core_Papers/`, `Popular_Editions/`, `Pedagogical_Notes/` + matching PDFs.
- **Book deferred** (separate bring-up-to-date pass).
- Version-label pass only — no new physics edits.

## Renames (24) — `v10_18_0` → `v10_19_0` (`.md` + `pdf-out`)

### Core_Papers (14)
- Companions 01–07, 10–14, 16
- `NTE_v10_18_0_Part1_Foundations` → `NTE_v10_19_0_Part1_Foundations`

### Pedagogical_Notes (10)
- BornRule, External_Empirical_Surface, F1, Hopf_Bundle, Kappa_AB, P4, Quantisation_Compactness, S1, S2, S6  
  (Octonion ped note was already `v10_19_0`)

## Already on v10_19 (12) — no rename
Companions 08, 09, 15, 17–20; Parts 2–3; Popular Full/Reader; Octonion ped note.

## Stamp pass
Mechanical `v10.18.0` → `v10.19.0` (and `v10_18_0` → `v10_19_0` if present) across deposit markdown.  
Deposit remaining `v10.18.0` / `v10_18_0` string contexts: **none**.

## Manifest
`NTE_Workflow_Manifest_v10_18.md` rev 10.4 — deposit described as unified v10.19.0; Book still pending; Part 3 path updated to `NTE_v10_19_0_Part3_Accounting`.

## Re-render
- `render-all-clean.ps1` → **expected 36, produced 36, all_pass true**
- PDF basenames: **0** × `v10_18_*`, **36** × `v10_19_*`
- Staging remains `%TEMP%\nte-build-scratch` (not Drive)

## Explicitly deferred
- Book chapters / Book build alignment to Session A + Popular θ₁₂/DESI + K(Φ) updates.

— Cursor Main, 2026-08-09
