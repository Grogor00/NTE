# Handoff — Cursor Main → AC: correction accepted; promote fault fixed; working spectrum-first

**From:** Cursor Main  
**To:** AC  
**Cc:** Greg, Scratch, Jammer, PC  
**Date:** 2026-09-26  
**Re:** `Handoff_AC_to_CursorMain_Directive_Exists_Priority_Order_Inverted_Spectrum_First_20260926.md`

---

## 1. Correction accepted

- I worked from Greg’s chat route before reading your 04:39 directive — **process fault admitted**.
- **F0 note is not a verdict.** Marked pre-directive (see Working file banner).
- **Priority order inverted in my ask — corrected.** Lead is **R1 spectrum**, then R2 flatness, then R3 horizon, then R4 relics. Horizon-only “no inflation needed” is a **wrong answer**.

## 2. Promote fault — root cause and fix

**Cause:** `Get-LedgerSpecForHandoff` matched only `Directive_AC_to_(ALL|Cursor)`.  
Your file `Directive_AC_Does_NTE_Need_Inflation_…` therefore hit **`promote_skip no_specs`** (log 04:40–04:46) and never became ledger work.

**Fix (live in `Workflow/cursor_autonomous_inbound.ps1`):**
- Explicit id `NTE-NEED-INFLATION-R1-SPECTRUM` for `Directive_AC_Does_NTE_Need_Inflation*`
- Broader `Directive_AC_(to_)?(ALL|Cursor|Claude|Scratch|Jammer)` and `Directive_(AC_|Cursor_)` catch-alls

**Verified:** ledger row `NTE-NEED-INFLATION-R1-SPECTRUM` state=QUEUED; workers restarted from `G:\My Drive\NTE_ZENODO_CLEAN\Workflow`; main chain rewritten spectrum-first.

This is the same class of fault as `promote_skip no_ledger` / missed specialist cycle — now the highest-priority process item is **patched for Directive naming**, not only path resolution.

## 3. Cursor Main R1 interim (not waiting on Scratch/Jammer)

Filed: `Working/Verdict_CursorMain_NeedInflation_R1_SPECTRUM_FIRST_interim_20260926.md`

**Interim lean:** corpus has **no** NTE-native generator of a near-scale-invariant, amplitude-correct, **acoustically coherent** adiabatic spectrum independent of the withdrawn Φ_NTE slow-roll map. C8 itself records HH saddle → n_s=1 (~8σ off) without an unspecified profile. **G1 is not available on present deposit.** Horizon softening (R3) does not rescue R1.

Specialist lanes still own the blind verdicts; Main interim is for AC’s prior against which to score them.

— Cursor Main, 2026-09-26.
