# Handoff — Cursor → AC: Manifest §4 path-first rebuild + §6.9 / §7 / rev 10.6 applied

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC · **Date:** 2026-09-18  
**Status:** **DONE** (MF-1..MF-4). No render (manifest only).  
**Source:** `Handoff_AC_to_Cursor_Manifest_PathFirst_Rebuild_MANDATORY_20260918.md`  
**Target:** `NTE_Workflow_Manifest_v10_18.md` (canonical root)

---

## Patch results

| Patch | Result |
|---|---|
| MF-1 §4 range replace (path-first; IDs removed) | **OK** |
| MF-2 §6 discipline 9 (path/name only; NEVER Drive ID) | **OK** (byte-exact) |
| MF-3 §7 resolve-by-path tooling line | **OK** (byte-exact) |
| MF-4 Last updated → rev 10.6 | **OK** (prefix replaced; retained text after prior `rev 10.5.` — see below) |

**Retraction noted.** Ch12 handoff §C / Notes "use the live tree" framing superseded by discipline 9; no further Cursor action.

**Greg Drive-UI still open (not Cursor):** (1) move `Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` from archive Book → canonical `Book\`; (2) rename superseded root to `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`.

---

## MF-4 retained after `rev 10.5.`

Retained verbatim after the new rev-10.6 lead-in:

> Part 1 clarification set (lapse / velocity dilation; four-velocity and the two uses of c; null-time as reparameterisation freedom; θ₁₂ currency; trailer and header date) and matching Part 2 currency fixes (header date; trailer). §3 μ–τ reflection θ₁₃ correction (Greg-ratified). κ-appendix watch-item closed — verified applied. Companion 15 cross-reference declined. Standing convention: a clean-rebuild trailer is a **currency** statement ("physics current to …"), except Part 3's "condensed from", which is provenance. Prior: rev 10.4 (2026-08-09) deposit set unify to **v10.19.0**.

---

## MF-1 — replaced block (verbatim, what was removed)

```
## 4. Folder structure (lean tree — verified 2026-07-06)

Top-level: **`NTE_ZENODO_CLEAN`** — `1Rn6Jun6MvCUyW5xdiZSitMFNWEUPdtqX` *(canonical, Greg 2026-08-03)*  
Superseded root (archive pending rename to `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`): `1zvYfkcbE21PMsLV_3ci-z86TrwsqvDTk`

Deposit-facing (`.md` sources):
- Core_Papers/ — `1-ImB7b6PWgD4Lc_wsacjHJKkb0Tr4O7X` (Companions 01–17 + Parts 1–3; verify live IDs after tree rebuild)
- Popular_Editions/ — `1qYyTy8v6BOHjLItQRKYCXF4_0E5J6ng4` (2: Full + Reader)
- Pedagogical_Notes/ — `1IOI06atIEGbaUZbmMSuFQb_w2dOOBP6W` (11 tier-3 notes)

Build area:
- paper-build/ — `1TacJgwJcC57S2HNzWarPETXpDlEE9rzi` (`render_all_clean_report.json` only; logs are build-local)
- paper-build/pdf-out/ — `1_n-dvfgBTRqtIQZjFFgWNhMHvupchbEv` (rendered PDFs — deliverables stay in Drive)
- **scratch staging is NOT in Drive.** `render-all-clean.ps1` uses `%TEMP%\nte-build-scratch` (stripped/mutated copies for pandoc only). Do not recreate `paper-build/scratch-src/` or mirror Core_Papers into the synced tree.

Coordination (reinstated 2026-07-05):
- Working/ — `1PlYUZSnhmzYAunxo6RUF-T1d8kdgadP7` (durable stream reasoning / working notes)
- Handoffs/ — `1c4FXZcZvfKcFcH6OD7l_z4iCKs7yvzCJ` (stream → AC/Greg handoffs; propose → ratify → integrate)

Book:
- Book/ — `13FjM9mgXm9pUQONNv7Zo3Xo-lJn-U43T` (chapters + subfolders)

Octonionic standalones (source folder, not deposit) — `1O0LVu4GMFgHMsgqcX48sEa0abbfpyutQ` ("New folder"): the Octonionic-Origin standalone (v0.1/v0.2), the Neutrino-Mixing-Sector paper, and the two-sector-necessity deep-dive. These ground the ℍ⊂𝕆 / J₃(𝕆) claims in Parts 2–3.

This manifest lives at the tree root. Folder IDs go stale on a tree rebuild — verify live access before writing (§7).
```

— Cursor Main, 2026-09-18.
