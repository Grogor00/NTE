# CCM 32-dim bimodule VERDICT — Cursor Main

**Question (Greg → pursue Jammer U-row):** Build the commuting C₊ / J C₋ J⁻¹ pair on ℂ ⊗ (𝕆 ⊕ 𝕆), or show it cannot be done.

**Answer: W — it can be done.** Opposite-summand placement gives a faithful commuting pair on ℂ ⊗_ℝ (𝕆 ⊕ 𝕆). The tensor-square placement V_ω ⊗_ℂ V_ω also works (recorded as a parallel Wc-class carrier, not needed for W).

**From:** Cursor Main · **To:** AC · **Cc:** Greg, Jammer · **Date:** 2026-10-03  
**Pre-register:** `Working\CCM_32dim_Bimodule_FORKS_PRE_REGISTER_Cursor_Main_Discipline12c_20261003.md` (filed before run)  
**Computation:** `Working\ccm_32dim_bimodule.py` → `Working\ccm_32dim_bimodule_REPORT_20261003.json`  
**Register:** findings. Nothing patched in Core / Companion 11.

---

## 0. Discipline

- **12(c):** forks W / Wc / F / U pre-registered before `ccm_32dim_bimodule.py` ran.
- **11:** read Jammer verdict + handoff 2026-10-03; CCM two-sided setup from arXiv:1409.2471 / Geometry and the Quantum: Basics (order-zero / bimodule language). Did **not** re-derive the full index form of ⟨Z[D,Z]⁴⟩=γ.
- Fano convention: e_i e_{i+1}=e_{i+3} (1..7 cyclic), closed under oriented triples — matches Jammer’s stated convention. (Corpus `farnsworth_stage1_octonion.py` left-mult is broken on squares; not used.)

---

## 1. Replication of Jammer’s 8-dim facts

| Check | Result |
|---|---|
| L_a²=−1, anticommuting (a=1..7) | Pass |
| All 21 five-subsets: dim⟨L_a⟩ | **32** (= M₄(ℂ)) |
| G_a=ω L_a generate | **dim 16** (= M₂(ℍ)) |
| ω central in the five; ω=±L_f L_g | Pass |
| Same 8-space: C₊ gens commute with C₋ gens | **False** |
| Commutant dims (gens) | **2** (ℂ) / **4** (ℍ) |
| Left vs right noncommuting pairs | **42 / 49** |

---

## 2. 32-dim constructions

**Carrier:** ℂ ⊗_ℝ (𝕆 ⊕ 𝕆) ≅ ℝ³² (real view: two copies of 𝕆⊕𝕆).

### 2.1 W route — summand split (and J-swap)

- π₋(c) acts as left-multiplication generators of C₋ ≅ M₄(ℂ) on the **first** 𝕆 summand (zero on the second).
- π₊(c) acts as ω-twisted generators of C₊ ≅ M₂(ℍ) on the **second** 𝕆 summand (zero on the first).
- **Commute:** True (disjoint supports).
- **Joint kernel trivial:** True (jointly faithful).
- Equivalent J-route: put C₊ on summand 0, conjugate by summand-swap J → action on summand 1; likewise commutes and is jointly faithful.

This is the standard direct-sum representation of A = C₊ ⊕ C₋ on H₀ ⊕ H₁ with J exchanging summands — now filled with the octonion-sourced Clifford algebras Jammer extracted.

### 2.2 Parallel carrier — V_ω ⊗_ℂ V_ω (Wc-class, not required)

- Identify one 𝕆 with ℂ⁴ via i:=ω (complementary 2-plane).
- π₋ = c ⊗ I, π₊ = I ⊗ c on ℂ⁴ ⊗ ℂ⁴ ≅ ℝ³².
- **Commute:** True; **jointly faithful:** True.
- Named additions relative to summand-graded 𝕆⊕𝕆: tensor-square identification; ω as complex structure on the factor (SU(3)→U(2) cost already in Jammer §2).

### 2.3 What still fails

- **Diagonal** placement (same generators on both summands): does **not** commute — Jammer’s 8-dim obstruction, doubled.
- **Octonion conjugation J** turning left into right multiplication: still fails (42/49); non-associativity bites there, not at summand split.

---

## 3. Landing

| Item | Fork |
|---|---|
| Commuting C₊ / J C₋ J⁻¹ on ℂ ⊗ (𝕆 ⊕ 𝕆) from octonion left-mult gens | **W** |
| Tensor-square carrier V_ω ⊗_ℂ V_ω | available (**Wc**-class alternative) |
| Full two-sided Heisenberg ⟨Z[D,Z]⁴⟩=γ with a Dirac D | **not checked** (out of scope this run) |
| Companion 11 unimodularity grade | **stays adopted** — algebraic prerequisite upgraded; derivation not closed |

**Reading.** Jammer’s U-row is closed to **W** for the commuting-pair prerequisite. That upgrades “dimension match only” to “pair constructed on the deposited summands after complexification.” It does **not** by itself promote C11 to derived: one still needs the maps Y±, the projection E, a real structure matching KO conventions, and the equality with γ — and the ω / SU(3)→U(2) cost remains for the trace.

**Spine flag (not patched):** Companion 11 ref 4 still says mimetic dark matter “arises automatically with that construction.” Jammer’s 2026-10-03 correction supersedes that; AC should strike or qualify it when convenient.

---

## 4. Suggested next forks (not run)

If Greg wants derivation pressure on C11:

1. Pre-register: does ⟨Z[D,Z]⁴⟩=γ hold for NTE’s Hopf-S³×S¹ spectral triple with this finite bimodule?
2. Pre-register: is summand-split J the deposit’s real structure, or does Companion 15 / Part 2 force a different J?

— Cursor Main, 2026-10-03.
