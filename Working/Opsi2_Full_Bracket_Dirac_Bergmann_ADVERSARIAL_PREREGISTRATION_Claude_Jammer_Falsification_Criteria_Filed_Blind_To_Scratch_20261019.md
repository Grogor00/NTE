# O(ψ²) full bracket set and Dirac–Bergmann chain: ADVERSARIAL PRE-REGISTRATION (Jammer)

Directive: Handoffs\Directive_AC_Compute_Full_Opsi2_Bracket_Set_And_Run_Dirac_Bergmann_Chain_To_End_20261019.md (read in full).
Filed **blind to Scratch**. At filing time, Scratch has no pre-registration or verdict in Handoffs\ or Working\ created after the directive.
Not read: RULING_AC_Claim3_..._20261019.md. Its content is summarised in the directive §0 (D2→D2′, W-3 reopened). I will read it before my Phase-2 review.

**Stake.** I raised the inference gap. A G-4 or G-1 landing vindicates that finding more than G-2 does. I counter that by fixing the criteria now, before seeing Scratch's work.

## The test I will apply (directive §3)
Does the computation **reach** the fork it claims? Each fork has a minimum evidentiary content. A filing that claims a fork without that content is graded as **not reaching it**, and I will regrade it to G-4 with the gap named.

## Control requirement (applies to every fork)
**K0. Pure-HR control.** At ψ = 0 the method must reproduce the known ghost-free result: the vierbein form of Hassan–Rosen / Hinterbichler–Rosen, in which the derivative-of-δ parts close and the secondary is preserved by fixing the lapse ratio.
- This is the decisive check, for a structural reason. In pure bigravity, {C_g(x), C_g(y)} already produces ∂δ terms whose coefficients are the g-momentum density alone, which is not a constraint by itself. The HR cancellation handles them.
- A method that flags "non-constraint coefficient on ∂δ" as ghost return would also flag pure HR. It would therefore be wrong.
- So the filing must show its ψ-dependent obstruction **survives the same mechanism that rescues pure HR**, not merely that a non-constraint coefficient appears.

## Minimum content per fork
- **G-2 (ghost via the derivative sector).** The filing must:
  1. compute the derivative-of-δ parts of {C_g, C_f}, {C_g, C_g} and {C_f, C_f} at O(ψ²), tracking C_i^(g), C_i^(f) and C_i^(ψ) against the total C_i;
  2. pass K0;
  3. show that the O(ψ²) residual cannot be absorbed by the shift multipliers (shifts multiply only the total C_i) or by the lapse freedom of the first-class combination;
  4. show that preserving the second-class primary therefore becomes a condition on a lapse, or its derivatives, rather than a new constraint;
  5. exhibit one explicit generic configuration (not φ₀ = 0, not isotropic) where the residual is nonzero.
- **G-3 (ghost via failure of S^(ψ²) preservation).** The filing must:
  1. have the derivative sector closed, so that S^(ψ²) genuinely arises;
  2. compute {S^(ψ²), C_g} and {S^(ψ²), C_f};
  3. show both vanish weakly, or that preservation generates a further constraint that changes the count. That count must still end with the BD mode alive.
- **G-1 (ghost-free at O(ψ²)).** The filing must:
  1. have the derivative sector closed, including at O(ψ²), with the closing mechanism named;
  2. show {S^(ψ²), H} ≈ 0 fixes the lapse ratio with a coefficient that is nonzero on generic data;
  3. give the final dof count: 7 + 4 dof (22 phase-space dimensions), with the Dirac second-class pairs counted.
  - G-1 must also be scoped as perturbative (O(ψ²) about ψ = 0). It must not be stated as non-perturbative ghost freedom.
- **G-4.** It must name the exact uncomputed bracket(s) and the reason each is blocked.

## Falsification criteria (each one is a fail if violated)
- **F1.** Any use of φ₀ = 0, isotropy or mini-superspace as the decisive setting.
- **F2.** Dismissing any ∂δ term as "weakly zero" on the strength of a partial momentum density (C_i^(D), C_i^(g) or C_i^(f) alone).
- **F3.** Landing a fork on "the HR identities do not extend" (absence of a proof). That was the original error.
- **F4.** Skipping K0.
- **F5.** Treating the relative Lorentz as fixed at Λ₀ beyond the order justified. S3a's O(ψ⁴) corollary must be re-checked wherever derivative terms are involved, because S3a was ultralocal.
- **F6.** Grassmann ordering or parity errors in the Dirac brackets, where O(ψ²) bilinears are treated as c-numbers without stating it.
- **F7.** The residual stated as ≥ 6 dimensions (it is 3), or a dof count without its convention.
- **F8.** Import of S2 or S3 conclusions as premises for the new fork. Their algebra may be reused; their labels may not.
- **F9.** Over-reading a partial chain as a terminal fork. This is the directive's named failure.

## Priors
- G-1 0.20
- G-2 0.35
- G-3 0.10
- **G-4 0.35**

G-4 is high because K0 plus the full derivative sector in 3+1d with spinors is a long computation, and the honest outcome of one round may be partial. AC's G-2 prior is declared; I discount it.

## My own lean on mechanism (to be tested, not asserted)
- In single-metric Einstein–Dirac, {H⊥(x), H⊥(y)} closes on the *full* single-metric momentum constraint, which includes the Dirac piece.
- In the doubly-coupled case, the Dirac momentum density is shared between both metrics' hypersurface algebras. Only one total C_i exists. So it is plausible that {C_g, C_g} at O(ψ²) carries C_i^(ψ)∂δ with weight from the g-term only, while {C_f, C_f} carries it with weight from the f-term only. Whether the HR combination absorbs that mismatch is the crux.
- I hold this at the level of a hypothesis. It is the place I will look first.
