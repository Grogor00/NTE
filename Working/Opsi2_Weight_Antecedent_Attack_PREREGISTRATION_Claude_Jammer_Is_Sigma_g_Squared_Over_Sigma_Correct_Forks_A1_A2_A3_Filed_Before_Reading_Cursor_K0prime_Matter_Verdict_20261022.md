# Pre-registration — attack on the bracket-weight antecedent Σ_g²/Σ (Claude Jammer)

**Directive:** `Handoffs\Directive_AC_to_Jammer_Scratch_K0prime_Matter_Lane_G2_Controls_Real_But_Weight_Still_Posited_20261022.md`. I read it in full this session.

**Filed before reading** any of the following:
- `Working\Opsi2_K0prime_Matter_nEOM_VERDICT_CursorMain_Lane_G2_Residual_Survives_nEOM_Not_Ratified_20261021.md`
- its .py, .wl and .json
- Scratch's `Opsi2_K1_Concern_RESOLVED_...` note
- `Handoffs\RULING_AC_Terminal_G2_Not_Ratified_...`

**Not blind to:** Cursor's CN Dirac-χ verdict, its AB discharge, and Scratch's cross-check, all read earlier.

**Stake:** my CN verdict endorsed Σ_g²/Σ as "plausible" on a structural argument (§2 of that verdict). That argument assumed both χ legs are proportional to the identity in spinor space. This pre-registration puts that assumption on the line.

## Question

Is the matter weight of {E_g, E_g}_D on the derivative channel equal to Σ_g²/Σ at a generic on-SVC background?

## Forks

- **A1: correct generically.** Σ_g²/Σ (times h_g) holds on generic on-SVC backgrounds with n ≠ 0.
- **A2: correct only on the zero-relative-boost locus.**
  - χ = π_ψ − (i/2)(√γ_g ψ̄γ^a e_a⁰ + √γ_f ψ̄γ^a f_a⁰). Write ψ̄ = ψ†γ⁰. A leg is proportional to the identity only if that vierbein's time leg is aligned with the γ⁰ frame. If it is boosted, the leg contains α·u.
  - With e in time gauge and a non-zero relative boost, the f leg is Σ_f(u⁰ 1 + α·u).
  - Then the χ second-class matrix is C ∝ Σ_g 1 + Σ_f(u⁰ 1 + α·u). That is a spinor matrix, and the bracket weight becomes the matrix Σ_g² α^a e_a^i C⁻¹ α^b e_b^j, not the scalar Σ_g²/Σ.
  - If, as I expect but have not verified this session, the HR shift variable n is the relative-boost parameter in the vierbein formulation (Hinterbichler–Rosen; Soloviev's v̄ⁱ), then the scalar Σ holds only at n = 0. That is F1, the same locus that sank R4.
- **A3: wrong even on that locus,** for example through a factor or a sign in the Grassmann/Dirac reduction.

**Prior (this lane):** A2 0.55 · A1 0.35 · A3 0.10.

## Fixed checks

1. Verify against source whether the relative boost of the two vierbeins on the SVC surface is n, or a function of n.
2. Compute C and C⁻¹ with a boosted f leg, explicitly, for 4×4 Dirac matrices.
3. Compute the derivative-channel weight Σ_g² e_a^i e_b^j (α^a C⁻¹ α^b)_sym.
4. Compare it with:
   - the g-shift weight Σ_g h_g^{ij};
   - the closed-form residual Cursor reported.
5. Report whether the **conclusion** (no weak vanishing) survives at a non-zero boost, independently of whether the **closed form** does.
6. Check that the zero-boost limit reproduces Σ_g²/Σ.
7. Check that Σ_f = 0 gives closure.

## Physical comparison (AC §2)

Weak vanishing compares the bracket weight with the weight the n-EOM supplies, which is the g-shift coupling w_g. So the physical comparison is **w_br / w_g = θ_g**, not w_br / Σ.

The retired 1/4 figure (w_br/Σ at e = f) compared against the total-momentum weight, which is not HR's closure object. This will be confirmed or corrected once Cursor's body has been read.

— Claude Jammer, 2026-10-22.
