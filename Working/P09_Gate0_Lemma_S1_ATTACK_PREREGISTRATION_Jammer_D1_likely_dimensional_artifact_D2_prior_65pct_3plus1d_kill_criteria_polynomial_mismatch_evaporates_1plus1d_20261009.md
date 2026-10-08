# P09 Gate-0 — Lemma S1 ATTACK PRE-REGISTRATION (Jammer, adversarial)

## Landing pre-registered: D1 in 1+1d LIKELY — but D1 ≠ evidence for D1 in 3+1d

**From:** Claude Jammer (adversarial lane)
**To:** AC, Scratch (construction), Cursor Main (literature)
**Cc:** Greg, PC
**Date:** 2026-10-09
**Status:** Pre-registration filed BLIND to Scratch's Lemma S1 construction
**Conflict declared.** No rescue.

**Prior:** `Arbitration_AC_Gate0_Secondary_Constraint_D4_Ratified_Lean_D2_Chair_67pct_S1_Authorized_Awaits_Greg_GO_20261009.md` (AC R4 authorized; Greg GO received)
**Directive:** `Directive_Cursor_Main_to_Scratch_Jammer_Lemma_S1_1plus1d_Bigravity_Dirac_GO_Original_Work_20261009.md`

---

## 0. Prior on D1 vs D2 in 1+1d — the critical dimensional issue

### 0a. The polynomial-class mismatch EVAPORATES in 1+1d

This is the single most important structural observation for Lemma S1 and it changes everything about how to read the result.

In 3+1d, the spatial dimension is 3. The square-root matrix $S = \sqrt{\gamma_g^{-1}\gamma_f}$ is a $3\times3$ matrix with 9 independent matrix elements $S^i_j$ and only 3 independent elementary symmetric polynomials $e_1(S), e_2(S), e_3(S)$. The HR potential depends on $e_n(S)$; the Dirac kinetic term depends on the matrix elements $S^i_j$. This is Result 2 / B4 — the core structural lean toward D2, chair credence ~67%.

**In 1+1d, the spatial dimension is 1.** The square-root "matrix" $S$ is a **scalar:**

$$S = \sqrt{\gamma_g^{-1}\gamma_f} = \sqrt{\gamma_f / \gamma_g}$$

It has **one** matrix element ($S$ itself) and **one** elementary symmetric polynomial ($e_1(S) = \mathrm{tr}(S) = S$). These are **identical:**

$$S^1_1 = S = e_1(S)$$

**The distinction between "depends on matrix elements of $S$" and "depends on elementary symmetric polynomials of $S$" does not exist in 1+1d.** Any function of $S$ is automatically in the polynomial class, because there is only one polynomial and it IS $S$.

The Dirac kinetic term in 1+1d:

$$\bar\psi\,\gamma^\alpha\,\varepsilon_\alpha^1\,D_1\psi = \bar\psi\,\gamma^\alpha\,e_\alpha^1\,S\,D_1\psi$$

depends on $S = e_1(S)$ — which is IN the HR polynomial class. The structural mismatch that is the core D2 mechanism in 3+1d simply does not arise.

### 0b. Prior credences

| Outcome in 1+1d | Jammer prior | Reasoning |
|---|---|---|
| **D1** | **~55–65%** | The core D2 mechanism (polynomial-class mismatch) is dimensionally absent. The HR cancellation machinery should work in 1+1d because the Dirac term's S-dependence IS polynomial. The Clifford algebra in 1+1d is $2\times2$ (Pauli matrices), allowing additional simplifying identities not available in 3+1d. |
| **D2** | **~25–35%** | Possible through the Dirac-bracket correction (Opening 4), which introduces cross-metric dependence through $\Sigma = \sqrt{\gamma_g} A_g + \sqrt{\gamma_f} A_f$. Also possible through a mechanism not captured by the polynomial-class argument — e.g., the S-dependence might be polynomial-class but still non-zero on the constraint surface. |
| **D4** | **~5–10%** | If the 1+1d computation is too degenerate to decide (e.g., if 2d gravity's topological character makes the constraint algebra trivially satisfied). |

### 0c. Prior on what 1+1d tells us about 3+1d

| 1+1d result | Implication for 3+1d | Strength |
|---|---|---|
| D1 in 1+1d | **NEAR-ZERO.** The polynomial-class mismatch is absent in 1+1d. A D1 result confirms that the HR machinery works when the obstruction is removed. It says nothing about whether the obstruction (which exists only in $d_{\text{spatial}} \geq 2$) is fatal in 3+1d. | **Not evidence for 3+1d D1** |
| D2 in 1+1d | **VERY STRONG for 3+1d D2.** If the ghost returns even WITHOUT the polynomial-class mismatch, a deeper mechanism is at work — one that persists in higher dimensions. D2 in 1+1d → D2 in 3+1d with high confidence. | **Strong evidence for 3+1d D2** |
| D4 in 1+1d | The setting is too simple to decide. 3+1d question remains at the prior (~67% D2 from AC). | **No update** |

**Asymmetry is extreme:** D1 in 1+1d is nearly uninformative for 3+1d. D2 in 1+1d is devastating for 3+1d D1. The Directive's pre-registered rules (D1 → "suggestive only, maintain W-2") are correct but UNDERSTATE this: 1+1d D1 is not just "suggestive" of 3+1d D1 — it is EXPECTED and VACUOUS because the D2 mechanism is dimensionally absent.

---

## 1. Kill criteria for any Scratch D1 claim in 1+1d

Any D1 claim in the 1+1d computation must survive ALL of the following. Failure of any one → the D1 result is a dimensional artifact, not physics.

### K1-S1: Polynomial-class control

**If Scratch claims D1, they must explicitly identify WHERE the polynomial-class mismatch would have appeared in $d_{\text{spatial}} \geq 2$ and show that its ABSENCE in 1+1d is what allows the cancellation.**

- If the D1 cancellation relies on $S$ being a scalar (i.e., on the fact that $S^i_j = S\,\delta^i_j$ in 1+1d with $d_{\text{spatial}} = 1$), the result is a dimensional artifact.
- If the D1 cancellation relies on Cayley–Hamilton being trivially satisfied for a $1\times1$ "matrix" ($S^1 = e_1(S)\,I$ is automatic when $I$ is $1\times1$), same conclusion.
- If the D1 cancellation uses a mechanism that WOULD work for a $3\times3$ matrix $S$ (i.e., doesn't use the scalar nature of $S$), THAT would be evidence for D1 in 3+1d. But I expect no such mechanism to be identified.

**Kill line:** D1 cancellation in 1+1d is a dimensional artifact UNLESS Scratch can exhibit the cancellation mechanism in a way that generalizes to $d_{\text{spatial}} = 3$.

### K2-S1: Clifford-algebra triviality

In 1+1d, the Clifford algebra is $\mathrm{Cl}(1,1)$, generated by $2\times2$ gamma matrices ($\gamma^0, \gamma^1$). The spinor is 2-component. The algebra is:

$$\gamma^0\gamma^1 + \gamma^1\gamma^0 = 0, \qquad (\gamma^0)^2 = I, \qquad (\gamma^1)^2 = -I$$

There are exactly **4** linearly independent elements: $\{I, \gamma^0, \gamma^1, \gamma^0\gamma^1\}$. Every $2\times2$ matrix is a linear combination of these. This means:

- Every Dirac bilinear $\bar\psi\,\Gamma\,\psi$ (for any gamma-matrix structure $\Gamma$) is a LINEAR COMBINATION of the four bilinears: $\bar\psi\psi$, $\bar\psi\gamma^0\psi$, $\bar\psi\gamma^1\psi$, $\bar\psi\gamma^0\gamma^1\psi$.
- In 1+1d, Fierz identities are MAXIMALLY constraining — there are only 4 independent bilinears and 4 independent gamma structures. In 3+1d, there are 16 gamma structures and the bilinear space is much richer.
- Any D1 cancellation that works because the Dirac bilinear has "only 4 components" in 1+1d will fail in 3+1d where it has 16.

**Kill line:** If the D1 cancellation uses Fierz rearrangements or gamma-matrix completeness specific to $2\times2$ matrices (e.g., the Pauli-matrix trace identity $\mathrm{tr}(\sigma_a\sigma_b) = 2\delta_{ab}$), it is dimension-specific.

### K3-S1: Topological triviality / too few dof

In 1+1d, pure gravity (Einstein-Hilbert) is topological — there are no local propagating gravitational degrees of freedom. The massive bigravity in 1+1d has:

- Phase space: $\gamma_g, \pi_g, \gamma_f, \pi_f$ = 4 gravitational variables
- Plus Dirac (after second-class): 2 real spinor components
- Total: 6

After spatial diffeomorphism ($C_1 \approx 0$, 1 first-class → removes 2) and assuming D1:
- $C_g, C_f$ + secondary constraint + its preservation = 4 second-class → remove 4
- Remaining: 6 - 2 - 4 = 0 bosonic propagating dof + Dirac on-shell

With D2:
- $C_g, C_f$ = 2 second-class → remove 2
- Remaining: 6 - 2 - 2 = 2 → 1 propagating bosonic mode = the ghost

**The 1+1d test has a degenerate feature:** D1 corresponds to ZERO propagating bosonic modes. The massive graviton doesn't propagate in 1+1d even in the ghost-free case. In 3+1d, D1 → 7 propagating modes (5 massive graviton + 2 massless). The constraint algebra in 1+1d is more constrained (smaller phase space, fewer variables, fewer indices), and cancellations that close the constraint counting to zero may be more likely than those that close it to the specific nonzero value required in 3+1d.

**Kill line:** If D1 holds in 1+1d and the mechanism relies on the phase space being so small that the constraints "over-determine" the system (as happens when D1 → 0 propagating graviton), this is an artifact of the toy dimensionality.

### K4-S1: Dirac-bracket structure

The Dirac-bracket correction to $\{C_g, C_f\}$ depends on:

$$-\{C_g,\,\chi_A\}\,C^{AB}_{-1}\,\{\chi_B,\,C_f\}$$

where $\chi = \pi_\psi - \Sigma\,\psi^\dagger$ and $C_{AB} = \{\chi_A, \chi_B^\dagger\}$ depends on $\Sigma = \sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f$.

In 1+1d, $A_g$ and $A_f$ are $2\times2$ matrices. The constraint matrix $C_{AB}$ is $2\times2$ (since the spinor is 2-component). Its inverse is trivial: for a $2\times2$ matrix, $C^{-1} = (\mathrm{tr}(C)\,I - C)/\det(C)$ by Cayley–Hamilton for $2\times2$. This introduces a SPECIFIC algebraic simplification: the Dirac-bracket correction has a closed form involving $1/\det(C)$, which in 3+1d ($4\times4$ constraint matrix) would involve a much more complex structure.

**Kill line:** If D1 relies on a specific simplification of $C^{-1}_{AB}$ that uses $2\times2$ matrix identities (Cayley–Hamilton for $2\times2$, or explicit $\sigma$-matrix inversion), it does not generalize.

### K5-S1: Non-perturbative closure

Same as the prior round's K4. The bracket closure must hold non-perturbatively in the spinor field $\psi$ (not just at $O(\psi^2)$). In 1+1d, the $O(\psi^2)$ approximation may be exact for certain topological reasons (2d fermion condensates), which would be another 1+1d-specific feature.

**Kill line:** Same standard — non-perturbative closure required.

---

## 2. Attack openings specific to 1+1d truncation

### Opening A: Polynomial-class mismatch is dimensionally absent (PRIMARY)

As detailed in §0a. In 1+1d, $S$ is a scalar, so "matrix elements of $S$" and "elementary symmetric polynomials of $S$" are the same object. The structural obstruction identified in the prior round (B4, chair credence ~67% D2) does not exist in 1+1d.

**If Scratch finds D1:** Expected. The test is vacuous — the obstruction was never there.
**If Scratch finds D2:** Devastating. A deeper mechanism is at work.

### Opening B: Too few dof — toy cancellation

In 1+1d, the gravitational phase space has 4 variables (2 per metric). After the spatial diffeomorphism, there are 2 gravitational phase-space variables. The constraint analysis involves finitely many terms. Cancellations that "just work out" in such a small system may have no analog in the 54-component space of $\delta S^i_j / \delta\gamma^{(f)}_{kl}$ in 3+1d.

I anticipate Scratch's computation will show a D1 cancellation involving a small number of terms (perhaps 2–4), each of which can be written in terms of $S$ and $\delta S/\delta\gamma_f = 1/(2S\gamma_g)$. In 3+1d, the analogous computation involves the full matrix $\delta S^i_j/\delta\gamma^{(f)}_{kl}$, which has 54 independent components and is NOT expressible in terms of the 6 derivatives $\delta e_n(S)/\delta\gamma^{(f)}_{kl}$. The "toy cancellation" in 1+1d does not scale.

### Opening C: Clifford simplification is dimension-specific

In 1+1d ($\mathrm{Cl}(1,1)$, 2-component spinor):
- Gamma-matrix space is 4-dimensional: $\{I, \gamma^0, \gamma^1, \gamma^{01}\}$
- Every bilinear $\bar\psi\Gamma\psi$ decomposes into these 4 channels
- Fierz identities are maximally constraining

In 3+1d ($\mathrm{Cl}(1,3)$, 4-component spinor):
- Gamma-matrix space is 16-dimensional: $\{I, \gamma^\mu, \gamma^{\mu\nu}, \gamma^{\mu\nu\rho}, \gamma^5\}$
- Bilinears have 16 independent channels: scalar, vector (4), tensor (6), axial-vector (4), pseudoscalar
- Fierz identities are much weaker (many more independent structures)

Any cancellation in 1+1d that relies on the COMPLETENESS of $\{I, \gamma^0, \gamma^1, \gamma^{01}\}$ as a basis for ALL $2\times2$ matrices (which is trivially true and not true for $4\times4$ matrices with 16-dimensional gamma space) is specific to 1+1d.

### Opening D: Dirac-bracket inversion triviality

$C_{AB}$ is $2\times2$ in 1+1d, $4\times4$ in 3+1d. The $2\times2$ inverse is algebraically trivial; the $4\times4$ inverse is not. Any cancellation involving $C^{-1}_{AB}$ must be checked for dimensional dependence.

---

## 3. Explicit fences — even D1 does not rescue anything

These hold for any S1 outcome, restated for the Lemma S1 context:

1. **Even D1 in 1+1d ≠ restore ν.** N_eff ≈ 1.52 excludes the symmetric doubly-coupled Z₂-even neutrino at ~10σ. Ghost-freedom in 1+1d would mean nothing for this. Independent, parameter-free, banked.

2. **No κ.** The broad amplifier (κ₅.₅₀) was withdrawn. κ₀ is retained. Nothing in S1 provides a route to restoring κ.

3. **No f.** The HR five coefficients and mass scale remain free. S1 does not constrain them.

4. **D1 in 1+1d ≠ D1 in 3+1d.** The Directive pre-registers this (D1 → "suggestive only, maintain W-2"). I argue it is WEAKER than "suggestive" — it is EXPECTED and VACUOUS because the D2 mechanism is absent. Maintain W-2 regardless.

5. **Deposit: P04 / adopted ΛCDM / cosmological sector open.** Unchanged by any S1 outcome.

---

## 4. What I will attack in Scratch's S1 verdict

When Scratch files their Lemma S1 construction, I will:

1. **Check whether D1 or D2.** If D1: apply kill criteria K1-S1 through K5-S1 above. If D2: assess whether the mechanism is dimension-independent (strong) or dimension-specific (weaker than expected).

2. **Press the polynomial-class evaporation.** If Scratch claims D1, they must confront that the core D2 mechanism (B4) is absent in 1+1d. If they don't address this, the D1 result is uninterpretable.

3. **Check the sub-lemma S1a (modified SVC).** The SVC solution $\Lambda^*(\gamma_g, \gamma_f, \psi)$ must be correctly computed. In 1+1d, $\Lambda$ is a single boost parameter — the SVC is a single algebraic equation. Any error here propagates into the bracket.

4. **Check term-by-term structure.** For each term in $\Delta\mathcal{S}$:
   - Term II (cross: Dirac-grav): Should involve $\delta/\delta\gamma_f$ acting on the Dirac Hamiltonian. In 1+1d, this is $\partial/\partial\gamma_f$ (one variable).
   - Term III (pure Dirac): $\{C_g^{(D)}, C_f^{(D)}\}$. In 1+1d with 2-component spinor, check if this is identically zero (it might be, by anticommuting Grassmann structure at $O(\psi^2)$).
   - Term IV (Dirac-bracket correction): Check the $C^{-1}_{AB}$ structure for dimensional simplification.

5. **If D1 by explicit cancellation:** Identify which step of the cancellation fails in 3+1d. The polynomial-class evaporation (Opening A) and Clifford simplification (Opening C) are the most likely dimension-specific steps.

6. **If D2 by explicit obstruction:** Assess whether the mechanism is dimension-independent. If it is, D2 is confirmed generically. If it relies on some 1+1d-specific feature (unlikely for D2, but check), the result needs 3+1d confirmation.

---

## 5. Summary of adversarial position

**I EXPECT D1 in 1+1d.** This is not a concession — it is the structural prediction from the dimensional analysis. The polynomial-class mismatch, which is the core D2 mechanism in 3+1d, does not exist when $S$ is a scalar. The HR cancellation machinery should work in 1+1d because the Dirac term's $S$-dependence IS trivially in the polynomial class.

**D1 in 1+1d would be a NULL RESULT for the 3+1d question.** It confirms that the HR cancellation works when the obstruction is absent. It says nothing about what happens when the obstruction is present ($d_{\text{spatial}} \geq 2$).

**D2 in 1+1d would be DEVASTATING for D1 in 3+1d.** If the ghost returns even without the polynomial-class mismatch, a mechanism deeper than Result 2 is at work — one that persists in all dimensions.

**My 3+1d credence remains ~67–70% D2** regardless of the 1+1d outcome (unless D2 appears in 1+1d, which would push it to ~85–90%).

**The 1+1d computation is worth doing** (it's cheap, it COULD produce the devastating D2, and even a null result sharpens the locus), but its D1 outcome should not be celebrated or interpreted as evidence for ghost-freedom in 3+1d.

---

## 6. Pre-registration integrity

This document was written BLIND to Scratch's S1 construction. I do not know:
- Whether Scratch finds D1, D2, or D4 in 1+1d
- What specific form the bracket takes in 1+1d
- Whether the sub-lemma S1a (modified SVC) introduces unexpected structure
- Whether the Dirac-bracket correction (term IV) has surprising behaviour in 1+1d

My kill criteria, openings, and prior are fixed as of this filing. I will attack Scratch's verdict against them, not adjust them ex post.

---

— Claude Jammer, 2026-10-09. Attack pre-registration filed for Lemma S1 (1+1d bigravity + Dirac). Blind to Scratch. Armed and waiting.
