# Handoff — Claude (chat) → Cursor Main: move build scratch out of Drive; reconcile Companion 17; full re-render

**From:** Claude (chat)
**To:** Cursor Main
**Date:** 2026-08-04
**Authorization:** Greg, 2026-08-04 ("go") — Core_Papers is the single canonical source; scratch copies must not live in the synced Drive tree.
**MO:** byte-exact OLD/NEW; match-or-report; return a completion handoff.

## Root cause (confirmed by reading render-all-clean.ps1)
The script reads `Core_Papers`, `Popular_Editions`, `Pedagogical_Notes` directly (correct single source), copies each file into `paper-build\scratch-src`, strips metadata / mutates for LaTeX, and renders that to `pdf-out`. The copy is one-way and force-overwritten each run — the script never writes back. **But `scratch-src` is inside the Drive-synced tree**, so the stripped staging copies sync up to Drive and appear as look-alike second copies of every paper (different content because metadata is stripped). This is the Companion 17 "divergence": a Core_Papers master next to a stripped render-artifact of itself.

## Change 1 — move scratch out of the synced tree (render-all-clean.ps1)
Apply this exact edit to the **current** `render-all-clean.ps1` (the 4598-byte one whose report writes to `paper-build\pdf-out`):

OLD:
```
$scratchDir = Join-Path $buildDir "scratch-src"
```
NEW:
```
$scratchDir = Join-Path $env:TEMP "nte-build-scratch"
```

Leave `$outDir = Join-Path $buildDir "pdf-out"` unchanged — PDFs are deliverables and should stay in Drive. `New-Item -Force $scratchDir` already handles creating the new location. The prepare/strip scripts resolve via `$workingRoot = repoRoot\Working` and are unaffected. Verify a render still succeeds after the change (all absolute paths via Join-Path, so no relative-path breakage expected).

Optional (same rationale, lower priority): the `renderlog_*.txt` files are also written to `paper-build` (synced). If you want them out of Drive too, point `$logFile` at `$scratchDir`.

## Change 2 — purge the existing synced scratch artifacts
Delete the contents of `paper-build\scratch-src` from the local tree (propagates the deletion to Drive). These are stale stripped artifacts and will regenerate locally on the next render. After deletion, confirm no `.md` under `paper-build\scratch-src` remains in Drive.

## Change 3 — stop any bidirectional Core_Papers↔scratch-src sync
If the Cursor workflow currently syncs `Core_Papers` ↔ `scratch-src` in both directions, remove that step. Cursor edits `Core_Papers` directly; scratch is build-local only and never a source or a sync target.

## Change 4 — Companion 17 reconciliation
Master = the `Core_Papers` copy of `Companion_17_KPhi_Frame_Closure_v10_19_0.md` that carries the provenance header ("executes the Read §5.1 definition of K(Φ)… on the sign-corrected Companion 9 eq. (1)", "Greg-endorsed plus sign"). Any stripped/headerless copy elsewhere is the render artifact — purge per Change 2. Confirm Core_Papers holds exactly one `.md` for Companion 17.

## Change 5 — clean full re-render (also closes the pre-ship render-currency gate)
After Changes 1–4, run a full `render-all-clean` so every `v10_19_0` PDF is built from current Core_Papers source — in particular the renamed **Companions 8, 9, 15** and **Parts 2, 3**, whose PDFs were renamed on 2026-08-04 but not necessarily re-rendered from v10.19 content (rename ≠ re-render). Return the report; confirm expected == produced and all_pass, and that the renamed papers' PDFs postdate their v10.19 source.

## Note for Greg (separate from this build fix)
This stops NEW scratch artifacts reaching Drive. The pre-existing **duplicate Core_Papers-type folders** in Drive (from the desktop-sync reorganization) are a distinct cleanup — the build fix does not resolve those; they still want a one-time reconcile so there is a single Core_Papers folder in Drive matching `G:\My Drive\NTE_ZENODO_CLEAN\Core_Papers`.

— Claude (chat), 2026-08-04
