# Handoff — Cursor Main → AC / Scratch / Greg: pipeline repair — sticky heuristic-pending cleared

**From:** Cursor Main  
**To:** AC, Scratch, Greg  
**Cc:** Jammer, PC  
**Date:** 2026-09-27  
**Sign:** **Cursor Main**

Scratch’s ten-hour diagnosis is **accepted in full.** The supervisor was reporting a stuck promote/drain pipeline as hourly “health.” That is worse than silence. Repair was prioritized above content.

---

## What was wrong (three layers)

| Layer | Fault |
|---|---|
| **1. Save abort (earlier today)** | Bloated `SEQ-GB` title → `ledger_save_abort` (fixed ~04:50) |
| **2. `promote_skip no_specs` on REISSUE** | Catch-all matched `Directive_(AC_|Cursor_)` only — **`Directive_REISSUE_*` never promoted** |
| **3. Heuristic ≠ promote** | `Get-UnfulfilledMandatoryInbounds` requires ledger **VERIFIED**. Delivered work left as QUEUED/CLAIMED → **re-listed forever** while ticks looked green |

Scratch’s pattern holds: hand-carry works; chain stalls. Root causes were (2)+(3), not specialist failure.

---

## Repairs applied this turn

1. **Inbound map:** catch-all now `Directive_(REISSUE_|AC_|Cursor_)`.  
2. **Ledger catch-up:** N-thickness, sequencing CRUX, BoundaryCondition, ItemA set, AR1/II0, 71.21 → **VERIFIED** (completions already on disk).  
3. **REISSUE:** ledger row **VERIFIED**; promote now `fulfilled`.  
4. **Supervisor:** sticky pending (≥5 items or ≥2h same list) writes **PIPELINE STUCK** — not a green-looking tick.  
5. **Verify:** `Get-UnfulfilledMandatoryInbounds` → **count = 0**.

---

## On Scratch’s three outstanding (none need a lane — agreed)

| Item | Owner | Cursor Main note |
|---|---|---|
| **Existence-gate / Part 2 §8.1 vs exit (a)** | **Greg** | Not a promote bug; architectural ruling |
| **κ closure under Door B (C5/C6/source)** | **Scratch hold** | Lanes must not call κ closure settled until Scratch clears |
| **Pipeline repair** | **Cursor Main** | This handoff — done for the stuck-list failure mode |

---

## Still true / still owed

- Workers “running” ≠ draining new work; green PID is not throughput. Escalation text now says so.  
- Phase-2 DESI directive still AC’s to issue (Scratch prestage ready).  
- Book surfaces still lag Door B (PC).  
- Existence-gate and κ-closure holds stand.

**Next supervisor tick should show heuristic-pending: none** (or PIPELINE STUCK if something new sticks). If the identical ten-name list reappears, the repair failed — escalate to Greg immediately.

— Cursor Main, 2026-09-27.
