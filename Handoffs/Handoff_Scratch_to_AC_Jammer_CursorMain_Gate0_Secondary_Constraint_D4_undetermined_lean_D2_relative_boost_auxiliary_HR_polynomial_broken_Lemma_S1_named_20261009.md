# HANDOFF — Scratch → AC / Jammer / Cursor Main: Gate-0 Secondary Constraint filed — D4, lean D2

**Date:** 2026-10-09 · **From:** Scratch (construction lead) · **To:** AC, Jammer (attack), Cursor Main (literature) · **Cc:** Greg, PC
**Commissioned by:** `Directive_Cursor_Main_to_Scratch_Jammer_Gate0_Secondary_Constraint_Algebra_GO_Original_Work_D1_vs_D2_20261009.md` (Greg GO)
**Label:** ORIGINAL WORK

**Pre-registration:** `Working/P09_Gate0_Secondary_Constraint_PREREGISTRATION_Scratch_forks_D1_D2_D4_method_ADM_canonical_SVC_bracket_original_work_20261009.md`
**Verdict:** `Working/P09_Gate0_Secondary_Constraint_VERDICT_Scratch_D4_undetermined_structural_lean_D2_relative_boost_auxiliary_but_Dirac_breaks_HR_polynomial_structure_next_lemma_S1_named_20261009.md`

---

## Landing: D4 — undetermined, structural lean D2 (~60–65%)

Not D1 (I cannot close the secondary constraint). Not D2 (I cannot prove the correction is fatal). Honestly D4 with a named lean, a named next lemma, and one positive intermediate result.

---

## Three results

### Result 1 (positive): Relative boost is AUXILIARY — Opening 2 partially resolved

The 6 relative Lorentz parameters (3 boosts, 3 rotations) that become physical under the diagonal-only Lorentz do NOT propagate. The conjugate momentum $p_{\Lambda_{\text{rel}}} \approx 0$ is a primary constraint; its preservation gives the **modified symmetric vierbein condition** (standard SVC + Dirac source), which is algebraic (no time derivatives). The $(p_\Lambda, \text{SVC})$ pair is second-class and non-degenerate, eliminating all 6 parameters from the phase space.

**This means:** no new propagating degrees of freedom from the relative Lorentz sector. The relative boost is determined by the metrics and the spinor, not by initial conditions. A genuine positive finding.

**But:** after elimination, the relative boost MODIFIES the effective Hamiltonian constraints (through the SVC solution $\Lambda^*(\gamma_g, \gamma_f, \psi)$), feeding the structural threat into Opening 1.

### Result 2 (structural obstruction): The Dirac field breaks the HR polynomial structure

The HR secondary constraint relies on the interaction potential's dependence on $S = \sqrt{\gamma_g^{-1}\gamma_f}$ being through the elementary symmetric polynomials $e_n(S)$, which satisfy Cayley–Hamilton identities. The Dirac spatial-derivative (kinetic) term, after SVC elimination, depends on the **matrix elements** $S^i_j$ directly (through $\varepsilon_\alpha^i = e_\alpha^j S_j^i$). This is a structurally different class of dependence.

The bracket $\{C_g, C_f\}$ receives non-zero corrections from the Dirac field's cross-metric dependence:
$$\{C_g^{(\text{D})}(x),\,C_f^{(\text{grav})}(y)\} = \int d^3z\;\frac{\delta C_g^{(\text{D})}}{\delta\gamma_{ij}^{(f)}(z)}\;\frac{\delta C_f^{(\text{grav})}}{\delta\pi^{ij}_{(f)}(z)} \;\neq\; 0$$

This correction is activated by the doubly-coupled spinor's dependence on $\gamma_f$ through the SVC-eliminated triad. It is absent for single-metric matter. It falls outside the HR polynomial class. **This is the structural lean toward D2.**

### Result 3 (blocker named): Lemma S1

**Cannot close D1 vs D2 without computing the correction explicitly.** The correction might cancel due to:
- Clifford-algebra / Fierz identities constraining the Dirac bilinear
- Dirac-bracket effects (the fermionic second-class structure modifies ALL brackets, including gravitational ones)
- Unexpected structure in the modified SVC solution

**Lemma S1:** Compute $\Delta\mathcal{S} = \{C_g^{(\text{D})}, C_f^{(\text{grav})}\} + \{C_g^{(\text{grav})}, C_f^{(\text{D})}\} + \{C_g^{(\text{D})}, C_f^{(\text{D})}\} + \text{(Dirac-bracket corrections)}$ on the constraint surface, to $O(\psi^2)$, in a tractable setting.

**Recommended tractable setting:** 1+1 dimensional bigravity + Dirac (2×2 tetrads, 2-component spinor, 1 relative-boost parameter). D2 in 1+1d → D2 generically. D1 in 1+1d → suggestive but requires 3+1d confirmation.

**Pre-requisite (sub-lemma S1a):** explicit modified SVC solution $\Lambda^*(\gamma_g, \gamma_f, \psi)$ to $O(\psi^2)$.

---

## Status of the three pre-registered openings + Jammer's fourth

| Opening | Status | Summary |
|---|---|---|
| 1 (shift sector) | **OPEN — primary blocker** | Dirac cross-metric dependence activates a non-zero correction to $\{C_g, C_f\}$; the HR identity $\partial C/\partial n^k \propto C_i$ is unverified for the spinor case |
| 2 (relative Lorentz) | **PARTIALLY RESOLVED** | Relative boost is auxiliary (non-propagating) — positive. But feeds into Opening 1 through the SVC modification |
| 3 (cross-metric lapse) | **RESOLVED (non-fatal)** | Confirmed non-fatal; lapse-linearity holds, cross-metric dependence enters secondary, not primary |
| 4 (Dirac bracket) | **OPEN** | Dirac-bracket correction is non-zero and structurally novel; not computed explicitly; part of Lemma S1 |

---

## Standing — unchanged

- **Gate 0: UNDETERMINED** (D4). Not W-1, not W-3. Sharpened from the prior D4 by Result 1 (positive) and the structural lean (D2).
- **N_eff ≈ 1.52:** excluded at ~10σ, independent, banked. Even D1 does not restore the symmetric ν.
- **No f. Not a route to κ.** Broad: amplifier/5.50 withdrawn; κ₀ retained.
- **Deposit: P04 / adopted ΛCDM / cosmological sector open.** Unchanged.

---

## For Jammer

My verdict is filed. The positive finding (Result 1, relative boost auxiliary) and the structural obstruction (Result 2, polynomial structure broken) are both available for attack. I expect Jammer to:
- Attack whether the relative-boost auxiliarity argument is watertight (the non-degeneracy of the SVC Hessian depends on "generic" metrics — what about cosmological special points?)
- Attack whether my lean toward D2 understates the obstruction (he might argue the structural argument is SUFFICIENT for D2, not merely suggestive)
- Press Opening 4 (Dirac bracket), which I flagged but did not resolve

I welcome the attack. Convergence on D4 with a D2 lean would be the strongest result this round can produce.

---

## For AC

Please register: **Scratch Gate-0 secondary constraint filed — D4 (undetermined), structural lean D2 (~60–65%). Positive intermediate: relative boost is auxiliary (non-propagating, modified SVC still determines it algebraically). Structural obstruction: Dirac spatial-derivative term depends on matrix elements of $S$, not elementary symmetric polynomials — breaks HR polynomial structure. Bracket correction non-zero. Cannot close without Lemma S1 (explicit computation in 1+1d or $O(\psi^2)$ in 3+1d). Gate 0 stays undetermined. No number restored. Deposit unchanged.**

---

— Scratch, 2026-10-09. Original work. Filed after pre-registration, before seeing Jammer's attack.
