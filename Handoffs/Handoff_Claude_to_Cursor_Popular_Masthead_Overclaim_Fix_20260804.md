# Handoff — Claude (chat) → Cursor Main (place exact) / cc PC: Popular-edition masthead meta-leak + opening overclaim

**From:** Claude (chat)
**To:** Cursor Main — place byte-exact (text supplied, no PC-voice rewrite required); cc PC for voice-consistency review
**Date:** 2026-08-04
**Authorization:** Greg flagged both; final wording is Greg's call. Do not apply until Greg fires.
**Targets:** `Popular_Full_Edition_v10_19_0.md`, `Popular_Reader_Edition_v10_19_0.md` (and check the Book front matter for the same two issues).
**MO:** byte-exact OLD/NEW; match-or-report per file (Reader may phrase the opening differently — report if OLD not found rather than force).

---

## Fix 1 — remove changelog meta from the reader-facing date line
Corpus changelog leaked into the public masthead. A reader has no referent for "θ₁₂ withdrawal + DESI naked-w alignment."

OLD:
```
date: "2026-08-04 (v10.19.0 — θ₁₂ withdrawal + DESI naked-w alignment)"
```
NEW:
```
date: "2026-08-04 (v10.19.0)"
```
Apply the same in both editions. **Sweep:** check every reader-facing edition's title/date block (Full, Reader, and any Book masthead) for the same pattern — a change-description in parentheses after the version — and strip the change-description, keeping `date "(version)"` clean.

## Fix 2 — opening overclaim (contradicts the paper's own §3)
The opening asserts an unverifiable "nobody has" while paragraph 3 says every physicist knows the fact and sets it aside. Align the opening to §3.

OLD:
```
There is a fact buried in your physics textbook that nobody has fully followed to its conclusion.
```
NEW:
```
There is a fact buried in your physics textbook that almost every physicist notices, and almost every physicist sets aside.
```
This foreshadows the existing §3 payoff ("This paper is what happens when you don't set it aside") instead of contradicting it. Reader edition: if its opening is compressed/differently worded, PC adjusts to the same sense (no "nobody has" superlative); report the exact current sentence so wording can be matched.

## Convention note (for the ledger / build, separate from these two edits)
Reader-facing editions should carry a **clean date only** in the masthead — corpus version-diff / changelog annotations belong in the corpus ledger, not the public title block. The strip scripts don't catch inline annotations in the visible date field, so this needs to be a PC/template discipline rather than an automated strip.

## After placement
Re-render the two Popular editions (and Book if touched) and return the report.

— Claude (chat), 2026-08-04
