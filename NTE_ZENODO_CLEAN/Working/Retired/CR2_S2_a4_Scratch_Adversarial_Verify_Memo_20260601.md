# CR2 — Scratch adversarial verify: S2 §5.5 a₄ (CR-H1)

**Date:** 2026-06-01  
**Lane:** PC/Scratch (autonomous PS-01)  
**Baseline:** `Working/cr2_s2_a4_gilkey_check.py`  
**Cross-ref:** `Working/CR2_S2_a4_Gilkey_Recompute_Memo_Cursor_20260601.md`; `Handoff_CR_to_Cursor_AC_Critical_Review_Findings_and_Response_20260601.md`

---

## Verdict: **FAIL (as written)** — do not sign PASS

Independent rerun of Cursor baseline script (2026-06-01):

| Check | Result |
|-------|--------|
| C² on S³ (R=6) | 0 |
| E₄ on S³ (R=6) | 0 |
| F₁ = −18C² + 11E₄ | 0 |
| F₁ R² coefficient | 0 |
| S2 §5.5 boxed a₄ | 270 β_GB ≠ 0 |

**Conclusion:** Under the Vassilevich §5.1 formula quoted in S2, **∫ F₁ = 0 ⇒ a₄ = 0**. The boxed a₄ = 270β_GB contradicts §5.2–§5.4 without an displayed Lichnerowicz **E = R/4** (or other non-F₁) contribution.

---

## Adversarial notes (Scratch lane)

1. **Not a numeric typo** — structural: Weyl-flat + Euler-zero kills the F₁ integrand; "R² dominates" in §5.5 misreads the cancellation proved two sections earlier.
2. **Λ closure load-bearing** — if Route A (a₄ = 0), Λ_{a₄} / Note 3 / six-note chord require reroute or tier downgrade (align CR-H2 concern).
3. **Derivation chain absent** — no Gilkey expansion with explicit E-dependent terms shown; **270β_GB is unsupported** until Jammer Route B/D recompute lands.
4. **Cursor memo accepted** — contradiction documentation is accurate; no independent PASS possible without new mathematics.

---

## Routing

| Owner | Action |
|-------|--------|
| **Jammer** | Route B/D: explicit a₄ integrand with E terms, or prove a₄ = 0 |
| **Cursor** | Hold S2 §5.5 / outreach a₄ claims; MAIN-03 CR-H1 advance |
| **AC** | CR-H2 Λ tier + Companion 11 caveat restore (awaiting AC ratification) |

**Scratch sign-off:** **VERIFY FAIL** — consistent with CR-H1; blocked on derivation chain.

---

*Scratch adversarial lane — CR2 PS-01*
