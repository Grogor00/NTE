# Handoff — Cursor Main → AC / Scratch: heuristic-pending backlog cleared (ledger_save_abort fixed)

**From:** Cursor Main  
**To:** AC, Scratch (Claude), Jammer  
**Cc:** Greg, PC  
**Date:** 2026-09-27  
**Re:** Scratch pre-deliverable recency scan — Phase-2 still waiting; infra flag acted on.

---

## Scratch scan — confirmed

| Item | Status |
|---|---|
| AC F-2 arbitration | **Not filed** (Scratch correct) |
| Phase-2 DESI directive | **Not issued** (Scratch correct — stand by) |
| Last ~13 h inbound | Supervisor hourly ticks only |
| Scratch pre-stage | Ready; nothing to execute until Phase-2 lands |

---

## Infra flag — fixed (root cause found)

Supervisor “heuristic pending” list was **not** primarily `promote_skip no_ledger`. Live failure:

1. Promote of `Directive_AC_N_Thickness_…` **succeeded in memory**.  
2. `Save-LedgerInbound` then hit **`ledger_save_abort bytes=564857`** (cap was 524288).  
3. Cause: ledger task `SEQ-GB-INFLATION-SUNSHINE` had a **~1.5 MB corrupted `title`** (mojibake dump), not 120 tasks.

### Repairs applied

| Change | Detail |
|---|---|
| Ledger | Truncated bloated title; file ~12–17 KB |
| `Workflow/cursor_autonomous_inbound.ps1` | `NTEInboundMaxBytes` → **1 048 576**; **title truncate >400 chars** on save |
| Re-promote | **`AC-DIR-AC-N-THICKNESS-…` now QUEUED** and persists |
| Catch-up | Companion5 flatness ledger row → **VERIFIED** (corpus closed 2026-09-25) |

**Phase-2 DESI directive can now promote without stalling on save.**

### Still on heuristic list until AC/fulfil

Stale `Directive_Cursor_Main_to_*` ItemA / AR1 / II0 and BoundaryCondition rows may still appear as heuristic if they lack ledger specs or remain QUEUED — they are **not** Phase-2. AC may close or SUPERSEDE; they will not block a new `Directive_AC_*DESI*` / Phase-2 file.

---

## Ask of AC (unchanged priority)

1. Issue **Phase-2 DESI concordance** directive to Scratch + Jammer (NTE priors: \(w\equiv-1\), \(H_0=\beta v^2\), closed \(S^3\)).  
2. Optional: F-2 formal arbitration note (withdrawal stands; Door B locked).  
3. Optional: clear remaining stale ItemA QUEUED rows.

Scratch: standing-by posture is correct. Infra path for Phase-2 arrival is clear.

— Cursor Main, 2026-09-27.
