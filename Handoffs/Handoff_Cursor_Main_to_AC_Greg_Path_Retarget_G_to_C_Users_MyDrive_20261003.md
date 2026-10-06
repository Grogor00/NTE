# Handoff: Path retarget G: → C:\Users\gregw\My Drive (2026-10-03)

**From:** Cursor Main  
**To:** AC / Greg  
**Corpus root (live):** `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN`

## Summary

Retargeted load-bearing Workflow / Manifest / Working scripts from Google Drive letter `G:\My Drive\NTE_ZENODO_CLEAN` to mirror `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN` (forward-slash variant likewise). Historical Handoffs left unchanged (36 files ≥ 20 threshold).

## Pre-check

- NEW root exists; `NTE_Workflow_Manifest_v10_18.md` present.
- Manifest Length **before** replace: **61498** (required).
- Manifest Length **after** replace: **61546** (expected: `C:\Users\gregw\...` is longer than `G:\...`).

## Strings

| Variant | OLD | NEW |
|---------|-----|-----|
| backslash | `G:\My Drive\NTE_ZENODO_CLEAN` | `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN` |
| forward slash | `G:/My Drive/NTE_ZENODO_CLEAN` | `C:/Users/gregw/My Drive/NTE_ZENODO_CLEAN` |

Replace method: UTF-8 read → string replace → write temp → `Move-Item` atomic (BOM preserved when present).

## Files changed (37)

### Workflow (8)
- `Workflow\auto.ps1`
- `Workflow\cursor_autonomous_toggle.ps1`
- `Workflow\cursor_autonomous_poll.ps1`
- `Workflow\cursor_autonomous_handoff_sweep.ps1`
- `Workflow\Resolve-NteRoots.ps1`
- `Workflow\_verify_apply_20260925.py`
- `Workflow\_apply_part1_part3_patch_registers_20260927.py`
- `Workflow\.cursor_autonomous_supervisor.log`

### Manifest / root (2)
- `NTE_Workflow_Manifest_v10_18.md`
- `_apply_review_response_20260925.py`

### Working scripts + flags (27)
- `Working\.cursor_handoff_greg_flags.md`
- `Working\_apply_book_opening_arc_20260924.py`
- `Working\_apply_omega_f11_20260924.py`
- `Working\_apply_c5_fork2_20260925.py`
- `Working\_apply_p1v_manifest_20260923.py`
- `Working\_apply_pc_av_aw_ax_af1_20260925.py`
- `Working\_apply_pc_av_aw_ax_af1_20260925b.py`
- `Working\_apply_ratified_20260925.py`
- `Working\_archive_search_conformal_20260922.py`
- `Working\_c21_pc_readonly_20260923.py`
- `Working\_g6_g7_grep_20260925.py`
- `Working\_emergence_grep_20260921.py`
- `Working\_patch_inbound_patterns_20260925.py`
- `Working\_pass2_finalize_summary.py`
- `Working\_greg_batch_apply_pass2.py`
- `Working\_greg_batch_apply_20260925.py`
- `Working\_inv_exact.py`
- `Working\_inv_check.py`
- `Working\_verify_book_opening_arc_20260924.py`
- `Working\_triage_pass2_20260922.py`
- `Working\_probe_apply_loci_20260925.py`
- `Working\_render_p3_c10_c13.ps1`
- `Working\_render_p1_p3.ps1`
- `Working\_render_c17_c20_stale.ps1`
- `Working\_render_c13_once.ps1`
- `Working\_render_part1_once.ps1`
- `Working\Retired\_triage_working_candidates_20260922.py`

## Verification

- `rg` on `Workflow` for `G:\My Drive\NTE_ZENODO_CLEAN` and `G:/My Drive/NTE_ZENODO_CLEAN`: **no hits**.
- Manifest current: **no G: hits**.
- `auto.ps1 status` (from Workflow; **not** `on all`):

```
NTE Cursor autonomous streams
  master enabled: False
  main : enabled=False tick=3m stopped
  ac_jammer : enabled=False tick=5m stopped
  pc_scratch : enabled=False tick=7m stopped
  supervisor : enabled=False tick=60m stopped
```

## Leftover historical G: mentions (not rewritten)

| Area | File count | Notes |
|------|------------|-------|
| Handoffs | **36** | Left historical (≥20 threshold) |
| Working (narrative/logs) | **8** | `.md` / `.txt` only; scripts already fixed |
| Book | **1** | `Book\paper-build\renderlog_Chapter_04_Time_and_Expansion_v9.txt` |
| Root historical | **1** | `NTE_Workflow_Manifest_v10_18_PRE_RESTORE_20260930.md` |

Working leftover narratives include e.g. `NTE_Corpus_Path_Lock_Drive_Only_20260926.md`, verdict/route notes, apply/report txt, Retired triage report.

## Policy note

Live lane scripts and Manifest now point at `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN`. Do not reintroduce `G:\My Drive\NTE_ZENODO_CLEAN` into Workflow or Manifest.