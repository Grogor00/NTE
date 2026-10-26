# ∂C/∂p "does not cancel": ADVERSARIAL REVIEW (Claude Jammer)

**Target:** `Working\Opsi2_dCdp_Alpha_Factorization_VERDICT_CursorMain_dCdp_Does_Not_Cancel_20261026.md`. I read it in full.

**Also read in full this session:**
- `Handoffs\RULING_AC_Chi_Weight_Derived_Aligned_Breaks_Under_Boost_Engine_Run_Scope_Fixed_Not_Terminal_20261022.md`. This contains AC's instruction to Jammer to "attack the boost formula and the α-channel claim".
- `Handoffs\Directive_AC_to_Cursor_Bimetric_Deep_Dive_Boost_Sector_Below_Stage1_Priority_20261026.md`.
- `Working\Opsi2_Gamma_Matrix_Coefficient_VERDICT_CursorMain_Aligned_Exact_Boost_Changes_Current_20261022.md`.

**Not read:** Cursor's dCdp .py, .wl and .json; Cursor's χ-weight derivation verdict; Scratch's aligned derivation.

**Pre-registration:** this is a short review against the criteria already filed in my 10-22 verdict (§3 item 4, which named ∂C/∂p as the last escape). No new pre-registration file was written. I disclose that as a process gap.

**Stake:** I named ∂C/∂p as the residual escape route.

## 1. The boost formula and the α channel (AC's 10-22 instruction)

Cursor built C from the Dirac matrices independently and did not import my numbers. It reproduces the current-channel coefficient c_I = Σ_g²(Σ_g + Σ_fγ_p)/(Σ_g² + 2γ_pΣ_gΣ_f + Σ_f²) to 4×10⁻¹⁶ in both engines, and the α channel with median 0.23 / 0.19.

**Two independent constructions now agree. I have no attack on the formula itself.**

Cursor also found that c_I = Σ_g/2 for every p when Σ_g = Σ_f. The algebra confirms it: numerator Σ_g²·Σ_g(1+γ), denominator 2Σ_g²(1+γ), giving Σ_g/2. That is correct, and it is a good catch of a misleading summary statistic.

## 2. The dCdp verdict: the conclusion holds, but for a better reason than the one filed

**(a) The free-coefficient model is not the real structure.**
- The script asks whether a·∂C/∂p (a free coefficient times the matrix) can cancel Δ = M − Σ_g I.
- If p is a phase-space function, as in Hinterbichler–Rosen where p₍₂₎ is fixed as a function of (e, π) by the shift equations, then ∂C/∂p does not enter as an additive matrix in the n-equation.
- It enters the **Dirac brackets** through χ's dependence on (e, π) via p. The new terms are of the form ψ†(∂C/∂p)ψ · {p, E_g}.
- So the right question is not "can a multiple of ∂C/∂p cancel Δ?" but "what ∂δ monomials do these bracket terms produce?"

**(b) Answering that question directly gives the same conclusion, more robustly.**
- ψ†(∂C/∂p)ψ carries **no derivative on ψ**. The new terms are ultralocal spinor bilinears multiplying {p, E_g}.
- They therefore produce ∂δ coefficients on density or spin-density monomials, **never on the current ψ†∂_kψ**, which is where Δ lives.
- An independent monomial cannot cancel Δ.

This is structural reasoning, not a computation. It confirms Cursor's landing and does not depend on the free-coefficient model.

**(c) The "on-shell p drops out" reading (§1, second paragraph) is too quick.**
- An envelope argument removes ∂/∂p from the *value* of a Hamiltonian at a stationary point.
- It does not remove p-dependence from *brackets*, because χ depends on p explicitly.
- §2(b) makes this moot for the current channel, but the sentence should not stand as written.

**(d) Shift factorization (§3).** Agreed. The boosted f leg is degree 1 in the multipliers, so the scalar dRHR non-linearity is not recreated.

**(e) Is p HR's n? (§4).** Still unidentified. Cursor covers both readings, so this is not blocking.

## 3. Not terminal

The dCdp run is a **component** check. AC's 10-26 directive sets the bar for a terminal result:
- K0′ passed in the **same run**;
- a genuine Σ_f = 0;
- K5;
- the **full matrix**, carrying both c_I(p) and the α channel through the matter-modified n-EOM.

Item (a) of the directive, the full-matrix engine run, has not landed. Until it does, G-2 remains a direction (now with all named escapes closed at the monomial level), not a landing.

**Prediction (not a posterior):** W-1 survives, ~0.75. This is up from 0.70 because ∂C/∂p is now closed by monomial independence.

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

**Context.** My conjugate-universe verdict of today recommends dropping the populated twin. If Greg adopts that, Opsi2 becomes a stand-alone technical note and none of this is load-bearing.

— Claude Jammer, 2026-10-26.
