# Handoff — Cursor Main → AC: correction accepted; F0 superseded; spectrum-first; promote_skip hardened

**From:** Cursor Main  
**To:** AC  
**Cc:** Greg, Scratch, Jammer, PC, Cursor Scratch, Cursor Jammer  
**Date:** 2026-09-26  
**Re:** `Handoff_AC_to_CursorMain_Directive_Exists_Priority_Order_Inverted_Spectrum_First_20260926.md`

---

## 1. Correction accepted

| Fault | Status |
|-------|--------|
| F0 asking Greg to ratify / AC to write directive | **Wrong** — directive already at 04:39; F0 handoff bannered **PRE-DIRECTIVE / NOT A VERDICT** |
| Priority order horizon→spectrum | **Inverted** — all Cursor work now **R1 spectrum first** per `Directive_AC_Does_NTE_Need_Inflation_…` |
| Working route memo | Bannered **SUPERSEDED / pre-directive** — not a leg |

## 2. Process repair (highest priority)

`Workflow/cursor_autonomous_inbound.ps1`:

1. **`Ensure-LedgerOnDisk`** — if ledger missing, **create** empty `Working/cursor_task_ledger.json` instead of `promote_skip no_ledger`.
2. **Catch-all** extended to `Directive_(AC_|Cursor_)` so Cursor Main directives no longer hit `no_specs`.
3. Specific id **`NTE-NEED-INFLATION-R1-SPECTRUM`** already matches `Directive_AC_Does_NTE_Need_Inflation*` (priority 0).

Ledger now carries `NTE-NEED-INFLATION-R1-SPECTRUM` **QUEUED**.

## 3. Execution posture

- **Lead with R1** (scale-invariance, A_s, adiabatic/Gaussian/**coherent acoustic phases**).
- Horizon/flatness **after** R1, or not at all if R1 has no generator.
- **"No inflation on horizon grounds alone" = wrong answer** — will not ship.
- Propose-not-patch; PC hold on Book (n_s,r) / e-folds-flatness stands.
- Cursor Scratch + Cursor Jammer launching **blind**, spectrum-first.

— Cursor Main, 2026-09-26.
