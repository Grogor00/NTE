# P09 Gate-0 — Secondary Constraint PREREGISTRATION (Scratch, construction)

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-09
**Authority:** Greg GO 2026-10-09; Directive `Directive_Cursor_Main_to_Scratch_Jammer_Gate0_Secondary_Constraint_Algebra_GO_Original_Work_D1_vs_D2_20261009.md`
**Status:** PRE-REGISTERED BEFORE COMPUTING — forks and method declared; results follow in separate VERDICT file
**Blind to:** Jammer's attack preregistration (filed separately; I do not read it until my verdict is filed)
**Label:** ORIGINAL WORK — no prior art for the two-tetrad single first-order-fermion constraint algebra (Cursor Main literature confirmation 2026-10-09)

---

## 0. Banked (do not re-derive)

- **D3 excluded:** primary lapse-linearity holds for a first-order Dirac on two tetrads (Scratch 2026-10-08)
- **N_eff ≈ 1.52:** symmetric Z₂-even ν excluded at ~10σ, independent of this round. Even D1 does not restore it.
- **Broad:** amplifier/5.50 withdrawn; κ₀ retained. No f. Not a route to κ.

---

## 1. Object to be computed

After the Hassan–Rosen shift redefinition, compute the Poisson bracket (or Dirac bracket, after second-class reduction):

$$\big\{ C_g(x),\; C_f(y) \big\}$$

where $C_g = H_\perp^{(g,\text{grav})} + H_\perp^{(g,\text{Dirac})}$ and $C_f = H_\perp^{(f,\text{grav})} + H_\perp^{(f,\text{Dirac})}$ are the full Hamiltonian constraint densities for the two metrics, including the contribution of a single Dirac spinor kinetically coupled to both tetrads under only the diagonal local Lorentz group.

**Decide:** does this bracket generate a secondary constraint (→ D1, BD ghost removed) or not (→ D2, ghost returns)?

---

## 2. Pre-registered forks (fixed before computing)

| ID | Meaning | Consequence |
|---|---|---|
| **D1** | Bracket yields a secondary constraint; BD ghost removed | Gate-0 gravity-sector W-1 (foundation only; N_eff still kills symmetric ν) |
| **D2** | Secondary constraint lost / spoiled by relative-boost dof or Dirac symplectic current | Ghost returns → W-3 |
| **D4** | Cannot close the bracket in this round; named blockers only | Gate-0 stays undetermined, sharpened |

**D3 is closed** (lapse-linearity banked). Failure licensed: D2 is fully available.

---

## 3. Method — five steps

**Step 1: Relative Lorentz elimination.** With only the diagonal Lorentz preserved (the spinor couples to both tetrads under a single spinor representation), the relative Lorentz parameters (6 components: 3 boosts, 3 rotations) are no longer gauge. Determine whether they are AUXILIARY (algebraically determined by the modified symmetric vierbein condition, i.e., the equation of motion for the antisymmetric vierbein part) or DYNAMICAL (acquire kinetic terms from the Dirac coupling). If auxiliary → eliminate via modified SVC and proceed. If dynamical → count propagating dof and check for ghost.

**Step 2: Dirac second-class constraints.** The Dirac field's momentum is $\pi_\psi \propto (\sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f)\,\psi^\dagger$, where $A_{(I)}$ are the normal projectors from each tetrad. This is a primary second-class constraint. Determine the second-class constraint matrix $C_{\alpha\beta} = \{\chi_\alpha, \chi_\beta\}$ and pass to the Dirac bracket. Note: $C_{\alpha\beta}$ depends on both spatial metrics and on the relative boost (through $A_g, A_f$).

**Step 3: Effective Hamiltonian.** After eliminating relative Lorentz (Step 1) and Dirac second-class constraints (Step 2), write the effective Hamiltonian:

$$H = N_g\,C_g(\gamma_g, \pi_g, \gamma_f, \pi_f, \psi) + N_f\,C_f(\gamma_g, \pi_g, \gamma_f, \pi_f, \psi) + n^i\,C_i + \ldots$$

Verify that $C_g, C_f$ do not depend on the lapses (lapse-linearity, already banked) and identify the cross-metric dependencies introduced by the spinor.

**Step 4: Bracket computation.** Compute $\{C_g(x), C_f(y)\}$ (using the Dirac bracket from Step 2). Decompose into:
1. $\{C_g^{(\text{grav})}, C_f^{(\text{grav})}\}$ — the pure HR bracket (known → secondary constraint)
2. $\{C_g^{(\text{D})}, C_f^{(\text{grav})}\} + \{C_g^{(\text{grav})}, C_f^{(\text{D})}\}$ — the cross terms (the key unknown)
3. $\{C_g^{(\text{D})}, C_f^{(\text{D})}\}$ — the pure Dirac bracket
4. Dirac-bracket corrections from Step 2

Determine whether the total is a new constraint (D1), zero/degenerate (undetermined), or structure-function-valued (D2).

**Step 5: Controlled truncation (if Step 4 is intractable).** If the full bracket cannot be evaluated, perform a controlled truncation:
- **(5a)** Semiclassical expansion to $O(\psi^2)$: expand around the vacuum ($\psi = 0$) where the pure HR secondary constraint holds, and compute the leading fermionic correction.
- **(5b)** 1+1 dimensional truncation: the constraint algebra in 1+1d is simpler (2×2 tetrads, 2-component spinor, single relative-boost parameter). Compute the bracket there and check whether the secondary constraint survives.
- **(5c)** Mini-superspace: restrict to homogeneous/isotropic metrics. The constraint algebra reduces to finite-dimensional mechanics.

Any truncation that decides D1 vs D2 conclusively is sufficient; but I will not claim a non-perturbative D1 from a perturbative argument (K4 from the directive).

---

## 4. Threats I am attacking myself (construction's own adversarial)

1. **Opening 1 (shift-sector):** The Dirac symplectic current $\pi_\psi \propto (\sqrt{\gamma_g} A_g + \sqrt{\gamma_f} A_f)\psi^\dagger$ depends on the relative boost, which lives in the HR shift-redefinition sector. If the identity $\partial C/\partial n^k \propto C_i$ (HR eq. 21/29) fails with the spinor, the bracket cannot be evaluated at fixed $n^i$, and the HR cancellation mechanism breaks.

2. **Opening 2 (relative Lorentz):** The diagonal-only Lorentz promotes the relative boost from gauge to physical. If the relative boost acquires kinetic terms from the Dirac coupling or if the modified SVC fails to determine it algebraically, new propagating dof appear — and one may be the ghost.

3. **Opening 4 (Dirac bracket modification):** The spinor's second-class constraint matrix $C_{\alpha\beta}$ depends on both metrics and the relative boost. The Dirac-bracket correction $-\{C_g, \chi_\alpha\}\,C^{\alpha\beta}_{-1}\,\{\chi_\beta, C_f\}$ contributes to the gravitational constraint bracket and is absent in both the pure-gravity and single-tetrad-fermion cases.

4. **Algebraic structure mismatch:** The HR potential's dependence on the square-root matrix $S = \sqrt{\gamma_g^{-1}\gamma_f}$ is through the elementary symmetric polynomials $e_n(S)$, which satisfy specific Cayley–Hamilton identities. The Dirac contribution depends on the MATRIX ELEMENTS of $S$ (through the triad $\varepsilon_\alpha^i = e_\alpha^j S_j^i$ from the SVC). Different algebraic structure → the HR cancellation may not extend.

---

## 5. Expected landing (stated before computing)

**D4** — I expect to establish that the relative Lorentz parameters remain auxiliary (Step 1), write the effective Hamiltonian (Step 3), and identify the structural form of the correction to the bracket, but NOT to close the full bracket computation. The structural argument will lean D1 or D2; I will state the lean honestly and name the next lemma.

**Failure I license:** if the structural argument clearly gives D2 (ghost returns), I will land D2 with evidence, not hide it behind D4. The honest D4 is only for "the argument is genuinely inconclusive."

---

— Scratch, 2026-10-09. Pre-registered before computing.
