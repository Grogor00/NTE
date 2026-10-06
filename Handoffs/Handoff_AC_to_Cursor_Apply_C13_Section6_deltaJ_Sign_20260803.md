# Handoff — AC → Cursor Main: apply Companion 13 §6 (δ_J-sign / within-sector CP-parity). Check-first; ratified.

**From:** AC · **To:** Cursor Main (apply) · **Cc:** Greg (ratifier), CR · **Date:** 2026-08-03
**Authorization:** Greg-ratified (the §6 draft + three repairs were ratified 2026-07-09; Greg re-authorised progressing via Cursor this session).
**Source draft (already in Drive):** `Working/Companion13_deltaJ_Sign_Section_DRAFT_plus_Apply_Instructions_20260709.md` (ID `1PBXwyoAybhV5UlXvZYOAgGXqCCPyE4W0`). Its **Part 1** is the canonical content; its **Part 2** is the byte-exact apply spec. Execute that spec.
**Canonical target:** `Core_Papers/Companion_13_..._v10_18_0.md` (ID `1fMxwVY0cArYGNQSbgP2DkLy82v666Bz_`); keep `paper-build/scratch-src/` mirror hash-identical.

---

## STEP 0 — Check-first (do not skip; work postdates the draft)

Grep Companion 13 for the string `within-sector CP-parity` and for a `## 6. The sign of` heading.
- **If §6 already present** (a prior pass applied it): STOP, verify it matches the draft's Part 1 text, and file a one-line "already applied — verified" report. Do nothing else.
- **If absent:** proceed to Step 1.

Also re-verify the citation is still live: confirm Part 2 §X and Part 3 §XVII still cite Companion 13 for the δ_J-sign / within-sector CP-parity claim (they did as of the 2026-07-09 edit pass). If those citations were removed or retargeted in the interim, STOP and report — the insertion's purpose (back a dangling citation) may have changed.

## STEP 1 — Apply per the draft's Part 2

1. **Insert §6** ("## 6. The sign of δ_J: a within-sector CP-parity, and free spectral data") after §5, before the current §6 "Scope".
2. **Renumber:** old `## 6. Scope...` → `## 7.`; old `## 7. Falsifiability` → `## 8.` (grep for stray `§6`/`§7` cross-refs after; the draft notes none exist, confirm).
3. **Abstract sentence** appended (draft Part 1).
4. **Reference** appended (Part 2 §X, §IX–X bilateral CPN; Part 3 §XVII).

Byte-exact from the draft's Part 1. Do not paraphrase.

## STEP 2 — Consistency note (Companion 15 exists now)

Companion 15 (E(Φ)/Farnsworth, 2026-08-02) also treats free spectral data in the neutrino sector. §6's line "the finite-Dirac computation that would ground any Yukawa magnitude (item 22.4)" is consistent with Companion 15's open-E(Φ)/K(Φ) framing — no change needed, but if a natural one-clause cross-ref to Companion 15 fits without altering meaning, note it as a *proposal* in your report (do not apply unratified).

## STEP 3 — Render + report

Re-run `paper-build/render-all-clean.ps1` (expect PASS incl. C13). File `Handoff_Cursor_to_AC_C13_Section6_Applied_20260803.md`: every string changed, the renumber confirmation, render result, and the Step-0 check outcome.

**Discipline:** byte-exact; canonical file verified; no new claims beyond the ratified §6; flag anything ambiguous rather than inventing.

— AC, 2026-08-03. Apply C13 §6 from the Working/ draft (check-first: it may already be applied); backs the Parts 2/3 δ_J-sign citation; render + report.
