# Handoff — PC → Cursor: Chapter 1 v9 ratified, apply instruction

**From:** Claude_PC · **To:** Cursor · **Cc:** Greg, AC · **Date:** 2026-09-18
**Status:** **RATIFIED by Greg, 2026-09-18, in session.** This supersedes the "do not apply until Greg confirms" line in the patch-set file. Cleared to apply.

**Patch source:** `Handoff_PC_to_Greg_Cursor_Chapter01_v9_A9_Patch_Set_20260918.md` (Handoffs, this folder). Fourteen patches, P1–P14.
**Target:** `G:\My Drive\NTE_ZENODO_CLEAN\Book\Chapter_01_The_Photons_Journey_v8.md`
**Output:** `G:\My Drive\NTE_ZENODO_CLEAN\Book\Chapter_01_The_Photons_Journey_v9.md`

---

## Apply rules

1. **All-or-nothing.** Work on a copy. Apply all fourteen patches to the copy; write out as v9 **only if all fourteen match**. If any OLD block fails to match, write nothing, leave v8 untouched, and report. A partially patched chapter is worse than an unpatched one.
2. **Byte-exact, match-or-report.** Do not normalise whitespace, do not fuzzy-match, do not repair near-misses, do not force. Report the failing patch ID with twenty lines of surrounding file context so PC can re-author against what is actually there.
3. **Escaping.** The OLD blocks were authored in raw markdown. If a block fails on escaped characters alone — backslash-asterisk for asterisk, backslash-hash for hash — **report it rather than unescaping and proceeding.** That failure mode is worth knowing about for every future patch set, not silently absorbed in this one.
4. **Three patches are insertions, not replacements.** P8, P11 (first block) and P13 (first block) are keyed to anchor text stated in the patch set. Insert as whole paragraphs with a blank line either side; do not consume the anchor.
5. **P11 and P13 each carry a second, separate replacement block** after the insertion. Both are required. P12 likewise carries two blocks, in different sections.
6. **Do not touch the copy under the superseded root.** Canonical tree only: `G:\My Drive\NTE_ZENODO_CLEAN\Book\`. The duplicate Book folder under the old root is a known issue, flagged separately, and is not in scope here.
7. **Do not delete v8.** Leave it in place until Greg says otherwise.

## On success

- Register `Chapter_01_The_Photons_Journey_v9.md` on the **Manifest §10 watch-list**, with its ratification date. This is the standing fix for the failure that left Appendix C v1.3 invisible from 2026-08-04 until today and Ch 12 v4.1 unratified from 2026-07-04 until today.
- Report back as `Handoff_Cursor_to_PC_Chapter01_v9_Applied_20260918.md`: which patches matched first time, any that needed a second look, and the resulting file size.

## On failure

Report as `Handoff_Cursor_to_PC_Chapter01_v9_Match_Failures_20260918.md` with the context blocks. PC re-authors; no attempt at repair at the Cursor end.

---

— Claude (PC lane), 2026-09-18.
