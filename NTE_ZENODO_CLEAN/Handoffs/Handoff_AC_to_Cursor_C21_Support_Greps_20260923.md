# Handoff — AC → Cursor: C21 support greps + campaign mechanicals

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC · **Date:** 2026-09-23
**Nature:** read-only greps and render checks. **No content edits.** Complements `Handoff_PC_to_Cursor_Housekeeping_Batch_ReadOnly_20260923.md` — if any task below duplicates one already done there, say so and skip it.
**Addressing:** name/path only.

---

## G1 — Cramer / Wheeler–Feynman crediting scope

AC has ruled the incomplete-transaction framing must be credited (see `Handoff_AC_to_PC_C21_FirstPass_AC_Response_20260923.md` §3). PC established zero credit anywhere in the historical archive. **AC needs the scope in the deposit set**, to author the patches.

Grep `Core_Papers\`, `Popular_Editions\`, `Pedagogical_Notes\`, `Book\` for: `transaction`, `transactional`, `absorber`, `no possible absorber`, `cannot complete`, `unclosed`, `Cramer`, `Wheeler-Feynman`, `Wheeler–Feynman`.

Report: filename, section heading, and the sentence verbatim. Separate hits that **use the idea** from incidental uses of the words. AC needs to know which paper used it first.

---

## G2 — λ/R_H occurrence map in the deposit set

Scratch is adjudicating 0.625 vs 3.92 (`Handoff_AC_to_Scratch_Jammer_C21_Blockers_And_GATE4C_20260923.md`, S1). PC's sweep covered the historical archive; **this is the live deposit set**, so AC knows the correction radius before the verdict lands.

Grep the same four folders for: `0.625`, `3.92`, `lambda/R_H`, `λ/R_H`, `λ = 3.92`, `0.625 R_H`.

Report filename, section, sentence verbatim, and which of the two figures each carries. A file carrying **both** gets flagged at the top.

---

## G3 — Render currency sweep

Confirm PDF newer than `.md` in `paper-build\pdf-out\` for: Chapter 1 v10, the Prelude v7, and — once `Handoff_AC_to_Cursor_GO_MR_Register_And_Item224_Repair_20260923.md` completes — Part 3, Companion 10, Companion 13. Report any file where the `.md` is newer.

---

## G4 — A9 violations in the popular editions

PC reports (`Register_PC_Outstanding_Work_All_Streams_20260923.md`, C6) that `Popular_Full_Edition_v10_19_0.md`, `Popular_Reader_Edition_v10_19_0.md` and `Book\Appendix_A_Popular_Reader_Edition_v10_19_0.md` still carry A9 violations, and that these are **not on the campaign list**. Confirm and scope.

Grep those three for: `from the photon's perspective`, `photon's frame`, `photon's own frame`, `experiences no time`, `emission and absorption`, `same instant`, `same event`, `limit case`.

Report filename, section, sentence verbatim, count per file.

**Sequencing note for the record:** Appendix A is synced *from* the Reader edition, so the popular editions must be corrected first or the next sync reintroduces the violations. Do not patch anything — PC drafts, AC integrates.

---

## G5 — Duplicate-name resolution (PC's D1)

Three files share the name `Handoff_AC_to_PC_AppendixC_v13_Retarget_And_Query_Resolutions_20260918.md` — reported at 8,658 / 8,092 / 7,971 bytes, two in `Handoffs\` and one at the Drive root. Since we resolve by name, this is a live hazard.

SHA-256 each, report the first heading and date line of each, and say which is AC's original (AC wrote the 8,658-byte one on 2026-09-18). **Do not delete or rename** — report only; Greg rules on disposition.

---

## Deliverable

One report, `Working\C21_Support_Greps_20260923.md`, **under 40 KB**, with a section per task. Completion handoff to `Handoffs\` addressed to AC.

---

— AC, 2026-09-23.
