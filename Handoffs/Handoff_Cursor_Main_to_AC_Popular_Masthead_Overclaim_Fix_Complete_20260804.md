# Handoff — Cursor Main → AC: Popular masthead meta-leak + opening overclaim — COMPLETE

**From:** Cursor Main  
**To:** AC / PC (voice-consistency review welcome)  
**Cc:** Greg, Claude (chat)  
**Date:** 2026-08-04  
**Fulfils:** `Handoffs/Handoff_Claude_to_Cursor_Popular_Masthead_Overclaim_Fix_20260804.md`  
**MO:** byte-exact OLD/NEW; match-or-report

---

## Fix 1 — clean date masthead
Applied in all three live reader-facing copies (exact OLD found):

| File | Result |
|---|---|
| `Popular_Editions/Popular_Full_Edition_v10_19_0.md` | `date: "2026-08-04 (v10.19.0)"` |
| `Popular_Editions/Popular_Reader_Edition_v10_19_0.md` | same |
| `Book/Appendix_A_Popular_Reader_Edition_v10_19_0.md` | same (Book masthead sync) |

**Sweep:** no other live Popular/Appendix A date lines carried the θ₁₂/DESI changelog parenthetical. Core technical date lines (e.g. Companion 9 “draft — eq.(1)…”, Part 3 Session manifest) left untouched — deposit ledger, not reader Popular masthead. Ignored `Book/depreciated/`, `Book_with_TP/`, Book scratch.

## Fix 2 — opening overclaim
Exact OLD present in Full, Reader, and Appendix A — all three replaced with:

> There is a fact buried in your physics textbook that almost every physicist notices, and almost every physicist sets aside.

**Report:** Reader was not differently worded; same sentence as Full — no PC rewrite needed.

## Re-render
- `Popular_Full_Edition_v10_19_0.pdf` — PASS  
- `Popular_Reader_Edition_v10_19_0.pdf` — PASS  
- Staging via `%TEMP%\nte-build-scratch` (Drive scratch retired)  
- PDF text check: no “withdrawal / naked-w / nobody has fully followed”; opening “almost every physicist notices” present

— Cursor Main, 2026-08-04
