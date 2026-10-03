# Handoff — Cursor Main → AC: build scratch local + Comp 17 reconcile + full re-render — COMPLETE

**From:** Cursor Main  
**To:** AC  
**Cc:** Greg, Claude (chat)  
**Date:** 2026-08-04  
**Fulfils:** `Handoffs/Handoff_Claude_to_Cursor_BuildFix_ScratchLocal_Comp17_20260804.md`

---

## Change 1 — scratch out of Drive
`paper-build/render-all-clean.ps1`:
- `$scratchDir = Join-Path $env:TEMP "nte-build-scratch"` (exact NEW)
- `$logFile` also under `$scratchDir` (optional from handoff — done)
- `$outDir` remains `paper-build/pdf-out`

Also aligned legacy `paper-build/build-pdfs.ps1` to the same TEMP scratch (same hazard).

## Change 2 — purge synced scratch artifacts
- Deleted **37** files from `paper-build/scratch-src/`
- Confirmed **0** `.md` remain under `paper-build/scratch-src/`
- Removed Drive-synced `paper-build/renderlog_*.txt` (logs now TEMP-only)

## Change 3 — stop Core↔scratch sync
- No active bidirectional sync script found under `Working/`
- Retired the workflow in `NTE_Workflow_Manifest_v10_18.md` (§4 build area, §5 Cursor lane, §7 duplicate-copy hazard): Cursor edits canonical folders only; scratch is build-local and never a sync target

## Change 4 — Companion 17
- Exactly **one** `Companion_17*.md` in the tree (outside purged scratch):  
  `Core_Papers/Companion_17_KPhi_Frame_Closure_v10_19_0.md`
- Provenance header present (Read §5.1 / sign-corrected Companion 9 eq.(1); Greg-endorsed plus sign in §1)
- Prior stripped scratch copy purged with Change 2

## Change 5 — full re-render
- Ran `render-all-clean.ps1` after Changes 1–4
- Report: **expected = 36, produced = 36, all_pass = true**
- Report path: `paper-build/render_all_clean_report.json`
- Staging confirmed under `%TEMP%\nte-build-scratch` (not Drive)
- Renamed v10.19 papers re-rendered from current sources (Companions 8, 9, 15; Parts 2, 3; Comp 17; Popular Full/Reader; Octonion note) — PDF `LastWriteTime` ≥ source

## Out of scope (per handoff note for Greg)
Pre-existing duplicate Core_Papers-type folders elsewhere in Drive are **not** resolved by this build fix.

— Cursor Main, 2026-08-04
