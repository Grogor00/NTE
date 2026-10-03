# CR2 — Paper S2 §5.5 a₄ Gilkey recompute (Cursor memo)

**Date:** 2026-06-01  
**Trigger:** CR-H1 (`Handoff_CR_to_Cursor_AC_Critical_Review_Findings_and_Response_20260601.md`)  
**Artifact under test:** `Papers/Paper_S2_v1_0_Consolidation_20260525.md` §5.2–§5.5  
**Status:** **OPEN** — contradiction documented; numeric check filed; Scratch cross-check requested

---

## §1 — The contradiction (CR-H1)

Paper S2 proves on M = S³×S¹ (R = 6 on S³ factor):

1. **§5.2:** F₁ = 5R² − 8R_μν² − 7R_μνρσ² = −18C² + 11E₄ with R² coefficient cancelling in the combination.
2. **§5.4:** Pointwise **C² = 0** and **E₄ = 0** on M.
3. **Therefore:** F₁ ≡ 0 on M.

Standard Seeley–DeWitt a₄ for Dirac (Vassilevich 2003, S2 §5.1):

$$a_4(D^2) = \frac{1}{(4\pi)^2} \frac{1}{360} N_F \int_M F_1 \sqrt{g}\, d^4x$$

If F₁ = 0 pointwise, **∫ F₁ = 0** ⇒ **a₄ from this integrand = 0** (not 270β_GB).

Yet **§5.5** boxes:

$$a_4(D^2)|_M = \frac{3 N_F \beta_{\rm GB}}{2} = 270\,\beta_{\rm GB} \neq 0$$

justified by "the R² piece dominates" — directly contradicting §5.2's statement that the R² piece **cancels in F₁** and §5.4's vanishing of C² and E₄.

**Downstream load:** Λ closure §7 (Λ_{a₄}), Note 3 K(Φ), "chord" Note 5 — all depend on nonzero a₄.

---

## §2 — Cursor numeric check

Script: `Working/cr2_s2_a4_gilkey_check.py`

On unit-radius S³×S¹ with R(S³)=6, flat S¹:

| Quantity | Value |
|----------|-------|
| C² | 0 |
| E₄ | 0 |
| F₁ = 5R² − 8R_μν² − 7R_μνρσ² | 0 |
| ∫ F₁ dV (form factor) | **0** |
| S2 claimed a₄ coefficient | 270 β_GB (**nonzero**) |

**Verdict:** As written, **§5.4 and §5.5 cannot both hold** under the §5.1 Vassilevich formula.

---

## §3 — Possible resolutions (for Scratch/Jammer)

| Route | Mechanism | Consequence |
|-------|-----------|-------------|
| **A** | a₄ truly 0 on this substrate | Λ_{a₄} route collapses; reroute Λ or accept Tier downgrade |
| **B** | Lichnerowicz E = R/4 + F adds **non-F₁** a₄ terms Gilkey includes separately | Rewrite §5.5 with explicit E-dependent integrand; recompute numeric value |
| **C** | Different operator / spectral action normalization than §5.1 | Document mismatch; unify with Jammer BR2d-J3 |
| **D** | §5.4 evaluation error (C²,E₄ not both zero) | Recompute curvature invariants on S³×S¹ |

**CR recommendation:** Route **B or D** first — do not ship a₄ = 270β_GB without displayed derivation chain.

---

## §6 — Route B advance (MAIN-03, 2026-06-01)

Gilkey/Vassilevich Dirac heat-kernel a₄ on curved backgrounds includes **Lichnerowicz-type terms** beyond the F₁ = 5R² − 8R_μν² − 7R_μνρσ² combination:

- Standard expansion uses **E = R/4** (or equivalent endomorphism E in the Lichnerowicz formula) plus field-strength F_μν pieces in the Seeley–DeWitt integrand.
- S2 §5.2–§5.4 proves **F₁ ≡ 0** on M = S³×S¹ when C² = E₄ = 0 — this kills the **F₁ channel** in the quoted §5.1 formula.
- §5.5's "R² dominates" language is **misapplied** to F₁; any nonzero a₄ must come from **E-dependent or F-dependent terms not displayed** in the F₁-only argument.

**Cursor interim conclusion:** Under the **written** §5.1–§5.4 chain, a₄ = 0 (Route A). Restoring a₄ = 270β_GB requires Jammer to box the **full** Gilkey a₄ integrand with explicit E terms (Route B) or disprove §5.4 (Route D).

**Λ reroute impact (if Route A holds):** Λ_{a₄} / S2 §7 / Companion 12 Note 3 chord — **collapse or tier downgrade**; align CR-H2 AC disposition. Do **not** restore 270β_GB without derivation.

---

## §4 — Cursor lane status

- [x] Contradiction documented  
- [x] Numeric sanity script  
- [x] Scratch independent spectral recompute  
- [ ] Jammer BR2d-J3 alignment  
- [ ] S2 §5.5 patch (blocked on A–D resolution)  
- [ ] AC disposition on Λ tier if Route A

---

## §5 — Honest-scope interim label

Until resolved, downgrade S2/C12 claims:

> **a₄ on S³×S¹: UNDER REVIEW (CR-H1)** — Weyl-flat + Euler-zero implies F₁=0; boxed a₄=270β_GB inconsistent with §5.1 formula as written.

Do **not** cite a₄=270β_GB in new outreach until CR-H1 closes.

---

*Cursor render lane — CR2 WP-CR-H1*
