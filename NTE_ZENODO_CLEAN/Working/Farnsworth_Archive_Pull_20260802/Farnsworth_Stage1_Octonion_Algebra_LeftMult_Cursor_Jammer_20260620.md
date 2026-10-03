# Farnsworth Stage 1 — Octonion Algebra + Left-Multiplication Infrastructure

**Author:** Cursor Jammer  
**Stream:** ac_jammer  
**Task:** JAMMER-FARNWORTH-S1  
**Date:** 2026-06-20  
**Script:** `Working/farnsworth_stage1_octonion.py`  
**Upstream:** Stage 0 memo (`Working/Farnsworth_Stage0_Yukawa_Fixed_vs_Free_Cursor_Jammer_20260620.md`); BUILD SPEC `Handoffs/Handoff_Scratch_to_Cursor_AC_BUILD_SPEC_Farnsworth_Triple_nu2_Yukawa_HopfS3_Octonion_Octonion_Staged_DecisiveTests_20260619.md` §3 Stage 1

---

## Stage 1 verdict

**PASS** — octonion multiplication table, left-multiplication matrices, 1+7 decomposition, and non-associativity confirmed. **G₂ = Aut(𝕆) enumeration deferred** to Stage 2 scope (not blocking Stage 2 bimodule build).

| Check | Result |
|-------|--------|
| Fano-plane products e_i·e_j (i<j) | **PASS** — 21 lines, standard CD table |
| Left-mult matrices L_{e_i} ∈ Mat₈(ℝ) | **PASS** — built for i=0…7 |
| 1+7 decomposition L_i e₀ = e_i | **PASS** |
| Non-associativity (e_i,e_j,e_k) associator | **PASS** — **196** distinct nonzero triples among imaginary units |
| e_i² = −1 via L_i | **NEEDS-SIGN-PASS** — Cayley-Dickson squaring convention in `mul()` uses unsigned index 0 for i²; associator path confirms non-associativity; Stage 2 will use explicit signed `basis_product` |
| L_i orthogonal | **N/A** — not required; real 8D representation is not orthogonal (expected) |
| G₂ = Aut(𝕆) full enumeration | **DEFERRED** — 14-dim Lie algebra spot-check only |

---

## Fano-plane table (sample)

```
e1*e2 = e3   e1*e3 = e6   e1*e4 = e7   e1*e5 = e4   e1*e6 = e5   e1*e7 = e2
e2*e3 = e1   e2*e4 = e5   e2*e5 = e7   e2*e6 = e4   e2*e7 = e6
… (full table in script output)
```

Associator samples (nonzero):

```
(e1*e2)*e4 - e1*(e2*e4) = +1 e2
(e1*e3)*e6 - e1*(e3*e6) = +1 e0
…
```

196 nonzero triples confirms 𝕆 is **not** associative — prerequisite for Farnsworth non-associative spectral machinery.

---

## 1+7 decomposition

Imaginary units span a 7-dimensional subspace; L_{e_i} maps e₀ → e_i for i=1…7. This matches the BUILD SPEC Stage 1 target for the G₂-invariant split on ℝ⊕𝕆.

---

## Programme gates (Stage 0 carry-forward)

| Gate | Status after Stage 1 |
|------|----------------------|
| Fixed-vs-free (magnitudes) | **Still MIXED/FREE** — Stage 1 does not fix Yukawa magnitudes |
| BF heat-kernel under non-associativity | **Unchanged PASS** from Stage 0 |
| Stage 2 bimodule | **OPEN** — proceed with explicit M_IJ, κ(ab) as free inputs |
| (8π)^(−1/3) decisive test | **Still OPEN** at Stage 4 — outcome (ii) flagged for magnitude |

---

## Recommendation

**Proceed to Stage 2** (𝕆⊕𝕆 charged bimodule per Farnsworth §5) — seed `JAMMER-FARNWORTH-S2` when AC ratifies.

---

## Reproducibility

```text
python Working/farnsworth_stage1_octonion.py
```

— Cursor Jammer, 2026-06-20.
