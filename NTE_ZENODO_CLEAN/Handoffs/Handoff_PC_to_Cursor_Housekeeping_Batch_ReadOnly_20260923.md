# Handoff — PC → Cursor: read-only housekeeping batch

**From:** Claude_PC · **To:** Cursor Main · **Cc:** Greg, AC · **Date:** 2026-09-23
**Status:** **Read-only. Report only. No moves, no renames, no deletes, no edits.** Every item below ends in a decision that is Greg's or AC's.
**Context:** `Register_PC_Outstanding_Work_All_Streams_20260923.md`, section D.
**Priority:** H1 first — it affects name resolution, which everything else depends on. The rest in any order.

---

## H1 — Three different files share one name

`Handoff_AC_to_PC_AppendixC_v13_Retarget_And_Query_Resolutions_20260918.md` exists three times, at **8,658**, **8,092** and **7,971 bytes** — two in `Handoffs\`, one at the Drive root. Three different documents under one name.

Two of them were created at 06:33 and 06:37 on 2026-09-18, *before* PC wrote the third at 06:41. PC authored one; the other two came from elsewhere.

This matters because the whole workflow resolves by name (Manifest §6 discipline 9). A name lookup returns whichever copy Drive picks, and the other two go on existing invisibly.

**Report, per copy:** full path, byte size, created and modified times, and a 10-line head plus the `From:`/`To:`/`Status:` block — enough for AC to tell which is which and whether any content is unique to one. **Do not nominate a winner and do not touch any of them.**

---

## H2 — Popular editions carry A9 violations, and Appendix A inherits them

Not on the campaign's A9 list, which named Prelude, Ch 2, Ch 4, Ch 5 only. PC is adding it.

Grep these three, report hits with one line of context each:

- `Popular_Editions\Popular_Full_Edition_v10_19_0.md`
- `Popular_Editions\Popular_Reader_Edition_v10_19_0.md`
- `Book\Appendix_A_Popular_Reader_Edition_v10_19_0.md`

Terms: `photon's perspective`, `from the photon`, `same instant`, `same event`, `same point`, `limit case`, `no clock` (context only), `experiences zero time`, `proper time` near |Φ_NTE|, `Higgs coupling` in any embedding or dial context.

**Sequencing note for the report:** Appendix A is synced *from* the Popular Reader edition. So the popular editions must be repaired first, or the next sync re-introduces the error into the Book. PC will author the patches.

---

## H3 — Render currency

Confirm PDF newer than `.md` for each, and report any where it is not:

- `Book\Chapter_01_The_Photons_Journey_v10.md`
- `Book\Prelude_The_Forty_Million_Year_Instant_v7.md`
- `Core_Papers\NTE_v10_19_0_Part3_Accounting.md`
- `Core_Papers\Companion_10_*.md`
- `Core_Papers\Companion_13_Yukawa_Nu2_v10_19_0.md`

The last three only once the M_R / item 22.4 GO has landed — that report is already owed under `Handoff_AC_to_Cursor_GO_MR_Register_And_Item224_Repair_20260923.md` and this does not duplicate it.

---

## H4 — Filename date-stamp drift

Several handoffs from this campaign carry a date stamp that does not match when the work was ratified: `20260918` on work Greg ratified 2026-09-21, and `20260922` on work done 2026-09-21.

**Report a list only** — filename, stamp in the name, actual created/modified date, and what the file records. Greg's call whether to restamp; flagged twice already without a ruling, so this is to give him the list to rule on, not to act.

---

## H5 — Archive-tree hygiene

Read-only status check on three known items:

1. Has the superseded root been renamed to `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802` (Manifest §4)? If not, confirm it still answers reads — that is the condition under which a stale pointer silently returns the wrong file.
2. Is `Copy of Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` still present in the superseded Book folder?
3. Does the superseded Book folder still contain `Appendix_C_The_Open_Ledger_v1_2_DRAFT_PC_20260705.md`? The canonical Book folder carries only v1.3, and AC's original targeting table named v1.2 — worth confirming where that pointer led.

---

## Deliverable

One report: `Handoff_Cursor_to_PC_Housekeeping_Batch_20260923.md`, filed to `Handoffs\`, with a section per item. Where an item needs a decision, say whose and state the options — do not choose.

---

— Claude (PC lane), 2026-09-23.
