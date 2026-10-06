# CURSOR → AC / Greg: Deposit register v5 DRAFT read. Blockers 2 & 4 corrected from disk. Version/header pass awaits GO.

**From:** Cursor Main · **To:** AC, Greg · **Cc:** PC · **Date:** 2026-10-06
**Reads:** `Handoffs\NTE_Corpus_Deposit_Register_v5_DRAFT_AC_20261006.md`
**Also reads:** `Handoffs\AC_Version_String_And_Status_Header_Pass_Specification_Deposit_Blocker_1_20261006.md` (DRAFT — not executed)

---

## 1. v5 design — recorded

Cursor adopts AC’s framing: **v5 is the index, not the status signal**; headers inside files are primary; v4.1’s four-month staleness is why. **NOT READY** with four named blockers — accepted as the deposit gate state until cleared.

§4 (two channels, four open sectors) and §7 (honest summary) noted. No Cursor edit to the DRAFT.

## 2. Blocker corrections — Cursor’s disk truth

| # | v5 DRAFT says | Cursor correction |
|---|---|---|
| **1** | Version strings stale | **Agreed.** Spec filed; **not executed** until Greg ratifies the pass. Mojibake already checked: **report-side only** (r2 table; 0 Core `â€` hits). Spec §6 can stop flagging. |
| **2** | Loci 1–4 unapplied — “AC blocks pending Cursor’s verbatim reports” | **Verbatim reports already filed** (`Handoff_Cursor_Main_to_AC_Kappa_As_CDM_Register_Eight_Loci_Verbatim_Current_State_20261006.md`). Locus **5** inserted; loci **6–8** applied under 22:27 GO. **Waiting: AC-authored NEW blocks for loci 1–4** (and C11 / N-3 per GO). Spec 4(b): version pass must not run while bodies still assert κ = Ω_DM/Ω_b. |
| **3** | C21 / Dark Sector unintegrated, NO_PDF | **Agreed** — Greg/PC gate; Cursor does not self-promote into `Core_Papers\`. |
| **4** | Five Cursor mechanicals outstanding | **CLOSED this session** — see `Handoff_Cursor_Main_to_AC_Greg_Five_Mechanicals_Plus_Void_Magnitude_CLOSED_20261006.md` (C21 §8.4.1→§8.4 verified already closed in v0.7; citation sweep; Δm²₂₁ NuFIT 6.0 on Ch12/Ch15; DS1-A; whole-set render currency; void V2). **v5 blocker 4 should drop or restate as closed.** |

## 3. Version-string + status-header pass — Cursor stance

**Ready to execute on Greg GO** of `AC_Version_String_And_Status_Header_Pass_Specification_Deposit_Blocker_1_20261006.md`, under AC’s sequencing:

1. **Loci 1–4 applied first or together** (AC drafts; Cursor applies).
2. Then the 23-artefact version/`date:` + status-header pass.
3. Before/after version-line report to AC **before** whole-set PDF re-render (spec §4a).

**Will not invent dates** for Companions 1–4, 7, 10, 13, 18–20 — status line will use AC’s “pre-campaign; read and found clean” form with **AC’s read date** once supplied (spec §3: do not invent).

**Open-items field** will follow v5 §4 / spec §3 lists; report rather than guess if a paper’s list is wrong.

## 4. Small v5 §5 nits (for AC’s fill pass)

- Part 2 row says “locus 5 pending” — locus 5 is **Part 3**; Part 2 took **loci 7–8** (and still awaits loci 2 / 4 / N-3).
- Part 3 ratification should also note loci **6** (BBN line) applied same evening.

## 5. Cursor queue (ordered)

1. AC blocks → apply **loci 1–4** (and C11 / N-3 when cleared).
2. Greg GO → execute version + status-header pass → before/after report → render.
3. Blocker 3: no Cursor action until Greg/PC.

---

— Cursor Main, 2026-10-06.
