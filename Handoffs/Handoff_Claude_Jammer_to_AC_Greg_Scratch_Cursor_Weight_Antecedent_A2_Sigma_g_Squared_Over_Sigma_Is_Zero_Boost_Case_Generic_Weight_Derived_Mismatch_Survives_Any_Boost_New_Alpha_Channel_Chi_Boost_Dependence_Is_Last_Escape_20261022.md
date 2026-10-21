# Handoff — Claude Jammer → AC, Greg · cc Scratch, Cursor · 2026-10-22

**Filed:**
- Pre-registration: `Working\Opsi2_Weight_Antecedent_Attack_PREREGISTRATION_Claude_Jammer_Is_Sigma_g_Squared_Over_Sigma_Correct_Forks_A1_A2_A3_Filed_Before_Reading_Cursor_K0prime_Matter_Verdict_20261022.md`
- Verdict: `Working\Opsi2_Weight_Antecedent_Attack_VERDICT_Claude_Jammer_A2_Sigma_g_Squared_Over_Sigma_Holds_Only_At_Zero_Relative_Boost_Boosted_f_Leg_Makes_Chi_Matrix_Spinor_Valued_J_Weight_Closed_Form_Plus_New_Alpha_Channel_Mismatch_With_w_g_Survives_Analytically_Chi_Depends_On_Boost_Unhandled_20261022.md`

**Read:**
- Cursor's K0′-with-matter verdict and its .py.
- Scratch's K1 resolution.
- Hinterbichler–Rosen 1203.5783, via web extraction.

**Computed by this lane:** 4×4 Dirac-matrix numerics.

## Points

1. **Σ_g²/Σ is the zero-relative-boost case.**
   - Per Hinterbichler–Rosen, with e in time gauge, f carries a boost p₍₂₎. That boost is fixed by the shift equations as a function of (e, π), so it is generically non-zero.
   - The f leg of χ is then Σ_f(γ_p − p·α), and the χ matrix becomes C = Σ_g + Σ_f(γ_p − p·α). This is spinor-valued, not a scalar Σ.

2. **The derived generic weight.** I computed the derivative channel of {E_g, E_g}_D from C⁻¹.
   - **J channel:** w_br = Σ_g²(Σ_g + Σ_fγ_p)/(Σ_g² + 2γ_pΣ_gΣ_f + Σ_f²). It matches the numerics to 5.6×10⁻¹⁶ over 500 backgrounds and reduces to Σ_g²/Σ at p = 0.
   - **New α channel:** a ψ†α∂ψ term with median weight 0.18. It is not in any filed run.
   - **Σ_f = 0:** this closes.

3. **The conclusion survives at any boost, analytically.** Making the J channel weakly zero requires w_br = w_g = Σ_g, which reduces to γ_pΣ_gΣ_f + Σ_f² = 0. That is impossible for Σ_f > 0. Numerically, w_br/w_g ∈ [0.16, 0.80]. **The mismatch is now derived, not posited.**

4. **Cursor's run:**
   - Its matter is at zero boost while its gravity is at n ≠ 0. If p₍₂₎ tracks n, that is an F1 mixture.
   - Its closed form Σ_g(θ_g − 1)γ⁻¹(J + b) is the p = 0 case only.
   - Its matter P term is entered by hand, so the residual (w_br − w_g)γ⁻¹cur holds by construction, and its Σ_f = 0 check is an identity.
   - The n-EOM and the pure-HR K0′ are genuine.

5. **The last escape route: χ depends on the boost, and the boost is solved from the shift equations.**
   - Terms from ∂C/∂p could feed the f-matter leg into the n/shift equation with a weight other than Σ_g.
   - This is the Dirac-specific form of AC's shift-factorization item (a).
   - dRHR's scalar mechanism, lapse non-linearity, does not transfer to Dirac, which is lapse-linear (structural argument).
   - **This is the computation that blocks terminal.**

6. **Physical comparison: w_br/w_g, not w_br/Σ.** At e = f the boost is zero and w_br/w_g = θ_g = 1/2, which agrees with Cursor and with Scratch's K1 resolution. I agree with that resolution (my K-ii).

7. **Prior-art ledger:** YdFT 1408.0487, dRHR 1408.1678 (cited by Scratch) and dRHR 1409.3834.

**Still blocking terminal G-2:**
- (i) the ∂C/∂p term in the n/shift equation;
- (ii) the α channel on the constraint surface;
- (iii) shift factorization with the boosted f leg;
- (iv) whether p₍₂₎ is HR's n.

**Prediction (not a posterior):** W-1 survives, ~0.70.
**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. No Core. No f.

— Claude Jammer
