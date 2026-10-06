# Handoff — Cursor Main → AC: corpus edit complete (δ_J sign + emergence residuals + Part A)

**From:** Cursor Main · **To:** AC · **Cc:** Greg, CR · **Date:** 2026-07-09 (executed 2026-07-11)
**Re:** `Handoff_AC_to_Cursor_Apply_Ratified_Edits_plus_Corpus_Wide_deltaJ_Emergence_Grep_20260709.md` · manifest `Handoff_AC_Edit_Manifest_Retire_Strong_Emergence_Claim_plus_deltaJ_Part2_Sweep_Fix_20260709.md`
**Authorization:** Greg-ratified canonical corpus edit. No Zenodo / DOI / deposit action.

---

## Canonical path verification

- Corpus root: `C:\Users\gregw\Desktop\NTE_ZENODO_CLEAN`
- Canonical files live flat under `Core_Papers\` (no Google-Drive-style ID folder nesting in this clean tree). ID hints from AC were treated as Drive metadata only.
- Edited / verified: `NTE_v10_18_0_Part{1,2,3}_*.md` and grepped all `Companion_01`–`Companion_13` `*_v10_18_0.md`.
- `paper-build/scratch-src/` Part 1–3 mirrors are hash-identical to Core_Papers (established mirror pattern); kept consistent. Companions also mirrored under scratch-src; no Companion text changes this pass.

---

## Part A — four ratified edits: BYTE-EXACT CONFIRMED

All four EDIT strings are present in Core_Papers; pre-edit strings absent.

| Edit | File | Status |
|------|------|--------|
| **EDIT 2** (first / deposit-relevant) | `NTE_v10_18_0_Part2_Structure.md` §X | **Landed.** Honest-scope: existence zero-parameter via `$\|\delta_J\|=\pi/2\neq0$`; sign *not* fixed (Companion 13; §XVII). Derivation line: `$\|\delta_J\|=\pi/2$ — **maximal CP-violation magnitude…** (sign free — §XVII). |
| **EDIT 1** | `NTE_v10_18_0_Part1_Foundations.md` §2.1.2 | **Landed.** Final sentence = Wick-rotation / coherent-reformulation wording (not axiom-consequence / postulate reduction). |
| **EDIT 3** | `NTE_v10_18_0_Part2_Structure.md` §8.1 | **Landed.** “follows from the emergence picture once the frame is granted — not an independently added postulate.” |
| **EDIT 4** | `NTE_v10_18_0_Part3_Accounting.md` Open work | **Landed.** K(Φ) item includes ℓ=1/H circularity clause. |

Old strings confirmed absent: `existence and sign`; `consequence of the NTE axioms` (Parts); `This is a consequence of the NTE axioms, not a new postulate.`; bare `determine $K(\Phi)$ (unlocks $n_s$/$r$);` without circularity note.

---

## Part B — corpus-wide grep + propagation

### B1 — δ_J sign (Parts + Companions 01–13)

**Additional edit (propagation of ratified |δ_J| magnitude / sign-free position):**

| File | Before → After |
|------|----------------|
| `NTE_v10_18_0_Part2_Structure.md` §8.4 | `CP violation ($\delta_J = \pi/2$, §X)` → `CP violation ($\|\delta_J\| = \pi/2$, §X)` |

**B1 edit count:** 1 string (Part 2 §8.4), in addition to Part A EDIT 2 (2 strings in §X).

**Companion δ_J-sign staleness:** **none.** No Companion file contains `\delta_J` / `δ_J` / “existence and sign” / “sign of the asymmetry” claims. Companions with leptogenesis/η language (esp. **Companion 10**) already treat η as order-unity consistency with underived CP/washout factors — left untouched.

**No Companion named for δ_J-sign catch** — the under-propagation was Part 2 only (§X + §8.4), not Companions.

### B2 — emergence over-claim phrasing

**B2 edit count:** 0 beyond Part A EDIT 1 / EDIT 3 (already the ratified softenings).

Hits reviewed and **not** edited:

| Locus | Why not edited |
|-------|----------------|
| Part 1 abstract / §I — “without asserting that the field dynamically creates time” | Already correct (denies mechanistic claim). |
| Part 1 §II.0 — “not counted as postulate reductions” | Already correct (demoted register). |
| Companion 01 L45 — “This is not a new postulate; it is the intersection of four established facts.” | Entanglement ontology from SR/path-integral/Bell/delayed-choice — **not** an emergence/postulate-reduction claim. Flag only. |

### B3 — K(Φ)

EDIT 4 already applied in Part 3 Open work. No further Companion K(Φ) open-list edits (optional; low priority; none required for consistency with Parts).

---

## Flagged, not edited (AC/Greg)

1. **Part 2 §X formula line** still writes geometric phase `$\delta_J = (\pi/2)(1 - e^{-M/\hbar H_{\mathrm{dS}}})$` (signed positive branch) before the corrected “giving `$\|\delta_J\|=\pi/2$` …” clause. Ambiguous convention residual — not a clear “sign is fixed” claim; left for adjudication rather than inventing formula rewrite.
2. **Companion 13 citation gap:** Parts 2/3 cite Companion 13 for within-sector CP-parity / free spectral data ($M_\nu$ vs $M_\nu^*$), but Companion 13 text does not currently discuss δ_J sign. No invented Companion 13 paragraph this pass.
3. **Popular editions (out of scope for this handoff’s Parts+Companions sweep)** still carry “existence and sign” wording:
   - `Popular_Editions/Popular_Full_Edition_v10_18_0.md` L296, L358, L366, L390
   - `Popular_Editions/Popular_Reader_Edition_v10_18_0.md` L191
   - Same strings also in `paper-build/scratch-src/Popular_*.md`. Recommend a follow-on Popular-only pass if deposit packaging includes those editions.
4. Companion 01 “not a new postulate” (above) — leave unless AC wants entanglement-register alignment.

---

## Files touched (this cycle)

| Path | Change summary |
|------|----------------|
| `Core_Papers/NTE_v10_18_0_Part1_Foundations.md` | EDIT 1 |
| `Core_Papers/NTE_v10_18_0_Part2_Structure.md` | EDIT 2 (×2 strings) + EDIT 3 + B1 §8.4 |
| `Core_Papers/NTE_v10_18_0_Part3_Accounting.md` | EDIT 4 |
| `paper-build/scratch-src/NTE_v10_18_0_Part{1,2,3}_*.md` | Hash-matched mirrors of the above |
| Companions 01–13 | **None edited** |

---

## Render

Ran established `paper-build/render-all-clean.ps1`.

- Report: `paper-build/render_all_clean_report.json`
- Result: **29/29 PASS** (`at`: 2026-07-11T15:00:13+12:00)
- Includes Parts 1–3, Companions 01–13, Popular editions, pedagogical notes.

---

## Watch state

Updated `Working/.cursor_handoff_watch_state.json`: marked apply + completion handoffs processed; bumped `poll_tick` / `last_poll`.

---

## One-line for parent / AC

Part A all four edits byte-exact in Core_Papers; B1 +1 (§8.4 `|δ_J|`); B2 +0 beyond Part A; **no Companion δ_J-sign staleness**; render **29/29 PASS**; Popular “existence and sign” flagged out-of-scope.

— Cursor Main, 2026-07-09.
