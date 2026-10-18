# Round 3: PHASE-2 REVIEW (Jammer)

**Landing:** G-4 is correctly reached by both lanes. But the ratified closed form R_j = h_g(I−X)²p_j omits the volume (density) weights. Using K1 to "force w = 1" is a misuse of a control. Both points must be fixed before round 4 targets the D-matrix against the wrong object.

**Read in full this session:**
- Handoffs\RULING_AC_Round3_Ratified_Rj_Equals_hg_I_minus_X_Squared_pj_AC_Misstatement_Corrected_Round4_Scoped_20261019.md
- Working\Opsi2_Round3_VERDICT_Scratch_lands_G4_sharpened_..._20261019.md
- Working\Opsi2_Round3_Dirac_Bracket_Coefficient_VERDICT_CursorMain_G4_..._20261019.md

**Not read:** the round-3 pre-registrations and Cursor's F14 acceptance body.

My own round-2 note A4 shares the first defect. I correct it here as well.

## 1. Fork check
Both lanes claim G-4, name a blocker, and decline G-1 and G-2 under F12, F13 and K3. **G-4 is reached.** F9 and F13 pass. F14 is cured in Cursor (χ is now included).

## 2. Defect 1: the closed form drops the volume weights (K4 fires)

**Derivation.** Use the densitized canonical spinor φ = Σ^{1/2}ψ (K4, which I pre-registered), with {φ, φ†} = δ.
- At the aligned boost, Σ = s_g + s_f, where s_g = √det γ_g and s_f = √det γ_f.
- The two Dirac Hamiltonian densities are C_g^(ψ) = s_g ψ†α_g∂ψ + h.c. and C_f^(ψ) = s_f ψ†α_f∂ψ + h.c.
- In φ these become (θ_g) φ†α_g∂φ and (θ_f) φ†α_f∂φ, with **θ_g = s_g/Σ, θ_f = s_f/Σ, θ_g + θ_f = 1**.
- The ∂δ coefficients therefore carry the weights:
  - θ_g² h_g in {C_g, C_g};
  - θ_f² h_f in {C_f, C_f};
  - θ_gθ_f G in {C_g, C_f}.
- These act on the **canonical** momentum density P_j = φ†∂_jφ, i.e. π_ψ∂_jψ. That is the quantity that enters the total momentum constraint C_j with unit weight.

**Control (the single-metric limit).** At θ = 1 the weight reduces to h^{ij}P_j, the standard Einstein–Dirac closure. So the weights cannot be dropped.

**Corrected residual, same algebra as before (G = h_g X, h_f = h_g X²):**

> **R_j = h_g (θ_g I − θ_f X)² P_j**, and with HR combination weights w: **h_g (w_g θ_g I − w_f θ_f X)² P_j**

It is still a positive-semidefinite perfect square. But it is a **different matrix** from h_g(I−X)²:
- θ_f/θ_g = s_f/s_g = 1/det X, so the residual carries **det X** in addition to X.
- K1 still passes. At X = I, s_f = s_g, so θ_g = θ_f = ½, and with w_g = w_f the residual vanishes. **K1 cannot distinguish the two forms.** That is exactly why the omission went unnoticed.
- The forms differ off X = I. On proportional backgrounds X = cI (c ≠ 1), h_g(I−X)² ∝ (1−c)², whereas the corrected form gives ∝ (1 − c·c⁻³)², i.e. (1 − c⁻²)², up to the w-weights.

**Index hygiene.** The lanes write p_j = ψ†∂_jψ and call it "the matter part of total C_j with unit weight". The matter part of C_j is the canonical P_j = Σψ†∂_jψ (hermitianized), not ψ†∂_jψ. The "not ∝ total C_j" argument should be restated in P_j. Its conclusion does not change.

**Consequence for round 4.** The D-matrix test must target h_g(w_gθ_g − w_fθ_f X)² P_j, including the det X-dependent θ's. Testing absorption of h_g(I−X)² p_j would test the wrong object and could produce a false G-1 or a false G-2.

**Self-correction.** My round-2 A4 formula h_g(w_g − w_f X)² made the same omission: the w's there silently absorbed nothing. The corrected statement has the w's multiplying θ's.

**Status of this derivation.** It is analytic and short, and checked against the single-metric limit. It is not numerically verified beyond that limit. Both lanes should reproduce or refute it explicitly. It is the K4 cross-check doing its job.

## 3. Defect 2: "w = 1 is forced by K1" is circular, and false as stated
Scratch §2 says C_g − wC_f gives h_g(I − wX)², which vanishes at X = I only for w = 1, so w = 1 is "forced". AC §1 adopted this ("forced, not chosen").

- **K1 is a control on a claimed residual. It is not a principle that selects the constraint combination.** Choosing the combination so that the residual vanishes at X = I presupposes health at X = I.
- **Even taken as a constraint, it fixes w only at X = I.** A field-dependent weight w(X) with w(I) = 1 satisfies K1 equally well. In HR the second-class combination is fixed by the constraint algebra itself: the first-class combination is the diagonal time-diffeomorphism generator. Its weights are field-dependent: lapse-ratio and, through n^i, D-dependent.
- **So the operative combination's weights must be derived from the HR structure** (K0′). They cannot be read off from K1.

## 4. Cursor R3-A (B1/B2 are not a W·P counter-term): accepted as plausible, register "established" too strong
- The field-content argument is sound at the ∂δ level. B1's ∂δ coefficient is (spinor bilinear) × π_f, not (metric weight) × P_j.
- But it is computed schematically: C⁻¹ ~ Σ⁻¹; Grassmann ordering, the boost factors A_g, A_f and the spin/ω sector are not tracked (F6).
- The on-shell step ("weak equality via C_f ≈ 0 still does not manufacture W·P") is asserted, not shown. The momentum constraint C_j ≈ 0 does contain π_f (as ∇π_f), so trading π-structures for P_j should be checked explicitly, not dismissed.
- **Record as "plausible, schematic"**, pending round 4's full preservation bracket, which must include B1/B2 anyway.

## 5. Posteriors
None earned. I hold G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. My corrections do not move them: the residual is still a nonzero perfect square, and the D-matrix question is unchanged in kind.

## 6. For AC (before Greg's round-4 GO)
1. Ratification stands as to G-4.
2. **Amend the ratified closed form** to R_j = h_g(w_gθ_g I − w_fθ_f X)² P_j, θ = √γ/Σ, P_j canonical. Alternatively, have the lanes show the θ's cancel. I do not expect them to; the single-metric limit requires them.
3. **Withdraw "w = 1 is forced by K1".** The weights come from the HR first-class/second-class split (K0′), and are field-dependent.
4. Round 4 is unchanged in scope (the D-matrix preservation bracket with K0′), but **targets the corrected object**.
5. Add **F16**: residuals stated in undensitized ψ†∂ψ, or without the volume weights θ, in a bimetric bracket.
6. Add **F17**: K1 used as a selection principle rather than a check.
