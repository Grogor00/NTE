# Handoff — Cursor → AC: Working-candidates triage complete

**From:** Cursor Main · **To:** AC · **Cc:** Greg · **Date:** 2026-09-22
**Status:** Complete for Cursor phase (R1–R5 + known strip item). Held items await AC verification.
**In response to:** `Handoffs\Handoff_AC_to_Cursor_Working_Candidates_Triage_20260922.md`

---

## Done

1. Triaged every file under `Working candidates\` and every top-level file under `Working\`.
2. Applied only unambiguous R1–R5 moves (+ AC-directed pre-fix `strip_corpus_metadata.py`) → `Working\Retired\`. Move-never-copy; no deletes; no renames; no `paper-build\` writes.
3. Left `Working\Farnsworth_Archive_Pull_20260802\` untouched (inventory only).
4. Report: `Working\Working_Candidates_Triage_Report_20260922.md`

## Totals

**files seen:** 807 · **moved to Working:** 0 · **moved to Retired:** 49 · **held:** 758

## Top finding (also at report head)

`paper-build\strip_corpus_metadata.py` is **MISSING**. The corrected ORPHAN_SEE pattern lives in `Working\strip_corpus_metadata.py`:

```
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b(?=\s*[);])", re.I)
```

Pre-fix copy from `Working candidates\` retired. AC/Greg: restore the corrected script into `paper-build\` if the render pipeline still calls it by that path.

## Held for AC

758 files held (FLAG packets in the report): 8.3 short-names, physics numerics, prose working docs, scripts without completion evidence, and all Working top-level items not caught by R1–R5.

`Working candidates\` folder itself was not removed.

## Amendment

Report appendix: 8.3/tilde-short names re-listed (22 files) — initial regex missed AC_*~1.MD forms; all still HELD.

## Manifest

§10 In-progress line registered.

— Cursor Main, 2026-09-22.
