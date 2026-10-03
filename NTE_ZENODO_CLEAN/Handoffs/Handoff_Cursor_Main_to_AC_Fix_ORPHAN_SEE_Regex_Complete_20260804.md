# Handoff — Cursor Main → AC: ORPHAN_SEE regex fix + full re-render — COMPLETE

**From:** Cursor Main  
**To:** AC  
**Cc:** Greg, Claude (chat)  
**Date:** 2026-08-04  
**Fulfils:** `Handoffs/Handoff_Claude_to_Cursor_Fix_ORPHAN_SEE_Regex_20260804.md`  
**Priority:** HARD pre-ship blocker — closed

---

## Fix (exact)
`Working/strip_corpus_metadata.py`:

```python
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b(?=\s*[);])", re.I)
```

Cleared `Working/__pycache__`. Bare prose "see" / "See" no longer deleted; only orphan `see` immediately before `)` or `;` remains in scope.

## Secondary review (narrowed where needed)
- **WORKSHOP_TAIL** was eating real prose (`not a derivation:…`, Companion 12 `dedicated derivation:…`, ped-note headings). Narrowed to require line-start or `;` / newline before the label. Live hits after narrow: **0**.
- **Greg-endorsed** global removals: only Comp 9 sign-note and Comp 17 "With the Greg-endorsed plus sign" → "With the plus sign". Intended deposit hygiene; no other prose clipped.

## Guard (recommended — shipped)
`render-all-clean.ps1` now fails the build if:
- source has ≥2 bare `see` words and stripped scratch retains &lt;50%, or
- canaries `cannot see` / `(see below)` present in source but missing from scratch.

## Re-render
- **36/36 all_pass** (`paper-build/render_all_clean_report.json`)
- Popular Full PDF spot-check: `(see below)` present; `cannot see the conjugate…` present; no `We cannot the conjugate`

— Cursor Main, 2026-08-04
