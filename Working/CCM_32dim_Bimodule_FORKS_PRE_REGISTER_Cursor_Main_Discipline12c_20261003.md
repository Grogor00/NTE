# CCM 32-dim bimodule — Discipline 12(c) fork pre-register

**From:** Cursor Main  
**To:** AC, Greg  
**Cc:** Jammer  
**Date:** 2026-10-03  
**Authority:** Greg directive “pursue this” on Jammer’s CCM×octonion verdict (two-sided relation on 32-dim).  
**Status:** Forks filed **before** computation. No numerical run yet at file time.

**Upstream:** `Working\CCM_Octonion_VERDICT_Jammer_…_20261003.md` §3.1 / landing row “Two-sided relation on a 32-dim enlargement = U”.

---

## Question

Can one build commuting actions of C₊ ≅ M₂(ℍ) and C₋ ≅ M₄(ℂ) (the algebras Jammer extracted from left multiplication on a single 𝕆), related by a real structure J in the CCM two-sided sense, on the 32-real-dimensional space ℂ ⊗_ℝ (𝕆 ⊕ 𝕆) — or prove it cannot be done?

(Abstract existence of some M₂(ℍ)–M₄(ℂ) bimodule of this dimension is not the question; the question is whether the **octonion-sourced** Clifford algebras admit such a pair on that space.)

---

## Forks (register before run)

| ID | Outcome | Meaning |
|----|---------|---------|
| **W** | Works as deposited | Commuting C₊ / J C₋ J⁻¹ pair from octonion left-multiplication generators exists on ℂ ⊗ (𝕆 ⊕ 𝕆) with no further named structure beyond the complex structure ω already required for the trace (Jammer §2). |
| **Wc** | Works with named additions | Pair exists only after naming extra structure (e.g. identifying the space with V_ω ⊗_ℂ V_ω rather than the summand-split ℂ⊗(𝕆⊕𝕆); a second independent complex structure; a non-native J; discarding summand grading). Additions must be listed in the landing. |
| **F** | Fails | No such commuting faithful pair exists on ℂ ⊗ (𝕆 ⊕ 𝕆) under the octonion-native generator constraints (proven numerically and/or by commutant / representation argument). |
| **U** | Undetermined | Computation or proof inconclusive (numerical instability, incomplete case scan, unread CCM [3] detail blocking a clause). |

**Landing rule.** Exactly one of W / Wc / F / U for the two-sided 32-dim question. Companion 11 grade is out of scope for this run (stays adopted unless W lands cleanly on the deposited finite algebra without enlargements AC has not ratified).

**Secondary checks (report, not forked):**
- Abstract tensor-product sanity: C₋ ⊗ I and I ⊗ C₊ on ℂ⁴ ⊗ ℂ⁴ commute (expected pass; controls the code).
- Whether ℂ ⊗ (𝕆 ⊕ 𝕆) ≅ V_ω ⊗_ℂ V_ω can be made **canonical** from deposit data, or is a Wc addition.
- SU(3)→U(2) cost from ω: inherited from Jammer; not re-opened.

**Computation plan (post-register):** `Working/ccm_32dim_bimodule.py` using `farnsworth_stage1_octonion.py` left-mult matrices; Fano convention as deposited.

**Non-goals this run:** patching Companion 11; mimetic-DM spine edit; one-sided S⁴ saddle / Companion 8 scale match (needs its own pre-register).

— Cursor Main, 2026-10-03 (pre-computation).
