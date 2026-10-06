# Handoff — Jammer → AC: Companion 5 Flatness Audit Complete

**From:** Jammer (Claude, adversarial lane)
**To:** AC (Claude)
**Cc:** Greg, PC, Cursor
**Date:** 2026-09-24

---

## Status

Adversarial audit of Companion 5's flatness derivation is **complete**.

Verdict filed: `Working\C5_Flatness_VERDICT_Jammer_20260924.md`

Blind protocol confirmed: no Scratch / Cursor / other-lane output was read before filing.

---

## Fork chosen

**Fork 2 — Two-quantity conflation confirmed; flatness derivation fails.**

Both claimed routes to flatness (Euler closure and dynamical H = β|Φ|²) fail on independent grounds. The core error is conflating the bilateral CPN zero-energy condition (constraining the pair of conjugate sectors) with the single-sector Friedmann energy (which determines spatial curvature). These are logically independent quantities, and the closed S³ topology requires them to differ.

---

## Summary of findings

| Question | Finding |
|---|---|
| Q1 (bilateral → curvature?) | **No.** Bilateral zero-energy constrains the pair, not individual-sector curvature. Conflation error. |
| Q2 (Euler identity doing work?) | **No.** Notation for the antipodal map plus decoration. Zero curvature content. |
| Q3 (dynamical route?) | **No.** H = β\|Φ\|² constrains expansion rate, not curvature term. Fails independently. |
| Q4 (reconciliation) | Part 3's treatment is correct (Ω_k < 0 strictly, driven toward zero). Companion 5 is the outlier. |
| Q5 (§9 replacement) | Draft replacement aligns §9 with ratified item 11. |

---

## Action items for AC / §10 patch

1. **Withdraw** the flatness derivation claim from Companion 5 (five instances identified: abstract, §4 paragraph, §8 table, §8 enumeration, §9 falsifier).
2. **Replace §9 falsifier** with text consistent with Part 3 item 11: "Spatial curvature sign: the boundary ontology requires a closed S³, hence Ω_k < 0 strictly; confirmed Ω_k > 0 at significance falsifies the framework at the ontological level (falsifiability item 11)."
3. **Replace §4 "Flatness" paragraph** with text consistent with Part 3: the closed S³ has Ω_k < 0 strictly, with |Ω_k| driven toward zero by the e-fold run.
4. **Correct abstract and §8** to remove "Flatness (Ω_k = 0)" and "flatness (Euler closure)" respectively.
5. Do NOT edit Core_Papers or Manifest directly — AC/Cursor to handle via §10 patch after both lanes report.

---

## Standing note

The finding "the flatness derivation does not hold and should be withdrawn" is consistent with the directive's standing instruction that this is a permitted and possibly correct outcome. The Part 3 treatment (ratified) already handles observed near-flatness correctly; no structural content is lost by the withdrawal.

---

— Jammer, 2026-09-24.
