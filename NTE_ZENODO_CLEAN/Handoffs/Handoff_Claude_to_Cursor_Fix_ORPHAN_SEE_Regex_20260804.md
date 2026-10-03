# Handoff — Claude (chat) → Cursor Main: FIX render-pipeline bug deleting every "see" (HARD pre-ship blocker)

**From:** Claude (chat)
**To:** Cursor Main
**Date:** 2026-08-04
**Priority:** TOP — corpus-wide; blocks any deposit/share of PDFs. Higher priority than the masthead/overclaim/proofread items.
**Authorization:** Greg (diagnosing this bug live).

## Root cause (confirmed by reading the pipeline)
`Working/strip_corpus_metadata.py` defines:
```python
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b\s*\.?", re.I)
```
and `strip_corpus_metadata()` applies it globally: `text = ORPHAN_SEE.sub("", text)`.

This matches the **bare English word "see"/"See" anywhere in body prose** and deletes it. The `CLEANUP` pass right after collapses the resulting double space (`re.compile(r" +") -> " "`), so the omission is seamless and invisible.

**Evidence:** markdown source reads "...at gauge birth **(see below)**" and "We cannot **see** the conjugate orientation's matter"; the PDF rendered today reads "(below)" and "We cannot the conjugate orientation's matter." Same deletion everywhere the word "see" appears.

## Scope
`strip_corpus_metadata` runs on **every paper**: standalone Companions + Popular editions via `prepare_paper_pdf.py` (step 7), and the Parts (masters) via the render script's `isMaster` branch. **Every PDF in the corpus, as currently rendered, is missing every "see"/"See."** Hard blocker for deposit.

## Fix (one line, in `Working/strip_corpus_metadata.py`)
OLD:
```python
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b\s*\.?", re.I)
```
NEW:
```python
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b(?=\s*[);])", re.I)
```
Rationale: the internal-reference cases are already removed whole by `INTERNAL_PAREN` (`(see Working/…)`) and `BACKTICK_PATH` (`` `Working/…` ``). The only legitimate job left for `ORPHAN_SEE` is to clear a "see" that dangles **immediately before a `)` or `;`** — the residue left when a backtick path inside `(see `…`)` is stripped, leaving `(see )`. The lookahead `(?=\s*[);])` restricts the match to exactly that: it removes "see" only when the next non-space character is `)` or `;`, and never touches "see below", "see it", "cannot see the", or a sentence-ending "see." (Trade-off: a rare trailing "…; see ." orphan may survive as cosmetic residue — acceptable, since the rule must never delete real prose. Do NOT add `.` or end-of-line to the lookahead: a real sentence can end in "see.")

## Cache
Python recompiles `.pyc` from the `.py` mtime, so editing the `.py` is enough. If a stale `strip_corpus_metadata.cpython-313.pyc` exists in `Working/__pycache__`, deleting it is belt-and-braces.

## Secondary review (not blocking — verify, don't assume)
`WORKSHOP_TAIL` removes `Cross-ref…|Derivation|numerics|Parents|Working corpus|Canonical paper|attack route:` followed by text to the next period. In a technical paper a legitimately labelled line ("Derivation: …", "Parents: …") would be clipped. Check it isn't eating real content in the Companions/Parts; narrow if it is. Also the global `Greg-endorsed` removals are intended but global — confirm they don't clip legitimate prose.

## After the fix
Re-render **all** papers (Companions, Parts 1–3, Popular Full + Reader, Pedagogical notes). Spot-check the rendered Popular Full: "(see below)" present, and "We cannot see the conjugate orientation's matter electromagnetically" present. Return the render report.

## Guard for the future (recommended)
Add a post-render sanity check: for each paper, compare a whitespace-normalised word count (or a diff on lowercased prose) between the stripped scratch copy and the source body; flag any net word deletions that aren't inside a removed metadata/reference span. A silent-omission class like this should fail the build, not ship.

— Claude (chat), 2026-08-04
