# CCM × Octonion RESULT — Jammer: **O2 lands.** 64 real dimensions is the minimum; it is realised on 𝕆 ⊗ 𝕆; 32 is excluded.

**From:** Jammer · **To:** AC · **Cc:** Greg · **Date:** 2026-10-03
**Pre-registration:** `Working\CCM_Octonion_PREREGISTRATION_Jammer_Two_Sided_Bimodule_Minimum_Dimension_Outcomes_O1_32_suffices_O2_64_minimum_O_tensor_O_O3_fails_Consequences_Fixed_Before_Computation_20261003.md` (filed 07:45Z, before the run; prediction disclosed there as not blind).
**Register:** findings, not rulings. Nothing patched.

## Read set

- Chamseddine–Connes–Mukhanov, *Geometry and the Quantum: Basics*, arXiv:1411.0977: fetched this session through a summarising tool. Requirements R1–R4 are as that tool quoted them. **Not read line by line.** If R1 or R3 is mis-stated, the 32-dimension exclusion needs re-checking.
- Nothing in `Core_Papers\` was re-read for this result.
- Computation: `scratchpad/bimod.py` (numerical, 64×64 real matrices). Not on Drive.

## What was computed

Notation: L_a is left multiplication by e_a on 𝕆; ω = L₁L₂L₃L₄L₅; G_a = ωL_a.

| Check | Expected | Got |
|---|---|---|
| dim C₊ (from G_a), dim C₋ (from L_a) | 16, 32 | 16, 32 |
| G_a⊗1 and 1⊗L_b commute on 𝕆⊗𝕆 | yes | yes |
| Generated algebra on ℝ⁶⁴ | 512 (= M₁₆(ℂ)) | 512 |
| Its commutant | 8 (= M₂(ℂ)) | 8 |
| P± = ½(1 ± ω⊗ω) | two invariant 32-dim halves | rank 32, 32; invariant |
| Commutant on one half | 2 (irreducible) | 2 |
| J = τ(L₆⊗1) on P₊, its inverse on P₋ (τ swaps the factors) | orthogonal, J² = 1, swaps halves | all true |
| Order zero [a, J b J⁻¹] = 0, all generator pairs of C₊ ⊕ C₋ | holds | holds |
| Left C₋ on the second half | ±L_b⊗1 | true for all five |

## Why 32 is excluded

- R3 needs a sector carrying C₊ on the left and J C₋ J⁻¹ on the right.
- That sector is a module of M₂(ℍ) ⊗ M₄(ℂ) ≅ M₁₆(ℂ). Its smallest module is 32 real dimensions and is irreducible (commutant ℂ, computed).
- A 32-dimensional space is therefore entirely that one sector. C₋ then has no left action, so R1 fails and J has nowhere to send it.
- So ℂ ⊗ (𝕆 ⊕ 𝕆) cannot host the structure. Neither can 𝕆 ⊕ 𝕆 (shown earlier today).

## What 64 means

- 𝕆 ⊗ 𝕆 is 64 real = 32 complex dimensions.
- That is the size of Chamseddine–Connes's own finite space for M₂(ℍ) ⊕ M₄(ℂ) (2·4² = 32 complex; stated from background knowledge, not fetched).
- So the octonionic route does not find a smaller or different home for CCM. It re-coordinatises theirs. Every real-linear operator on 𝕆 is a polynomial in left multiplications, so "built from octonions" does not discriminate anything here.
- The deposit's algebra is a direct **sum** of two octonion algebras; this needs the **tensor product** of two octonion spaces. Those are different structures.

## Not done

- **The relation itself.** No Dirac operator on S³×S¹ was coupled; ⟨Z[D,Z]⁴⟩ = γ was not solved. Only the finite-space prerequisites were shown.
- J's commutation signs with D and γ (the mod-8 conditions) and antilinearity with respect to a fixed complex structure were not checked. J is a real orthogonal involution satisfying order zero.
- The 2-plane / SU(3) → U(2) cost from the earlier verdict is unchanged.

## Consequences (as pre-registered for O2)

- Companion 11 is not regraded.
- CCM unimodularity is available to NTE **only by adopting a 64-dimensional finite space equal to Chamseddine–Connes's**. That is a structural change, to be decided on structural grounds and not to recover unimodularity (discipline 12(c)).
- **Spine hazard:** that finite space comes with its own fermion content and gauge structure (Pati–Salam type; background knowledge). Adopting it would put the deposit's particle derivation in dependence on, or in competition with, theirs.

**Question for Greg:** does any deposit paper already use 𝕆 ⊗ 𝕆, or a 64-dimensional (32 complex) fermion space? If it does, this result becomes a structural match worth examining. If not, CCM stays a foreign candidate. I have not searched for this.

— Jammer, 2026-10-03.
