# Handoff: Claude Jammer → AC, Greg (cc Scratch, Cursor Main, PC). Round 3 Phase-2: fix the target before round 4

Review: Working\Opsi2_Round3_PHASE2_REVIEW_Claude_Jammer_G4_Correct_But_Rj_Closed_Form_Drops_Volume_Weights_Correct_Form_hg_thetag_minus_thetaf_X_squared_On_Canonical_P_And_w_Equals_1_Not_Forced_By_K1_20261019.md

## Findings
- **G-4 is correctly reached by both lanes.** F14 is cured in Cursor.
- **The ratified R_j = h_g(I−X)²p_j drops the volume weights.**
  - Using densitized spinors (K4), each lapse constraint carries θ_{g,f} = √γ_{g,f}/(√γ_g+√γ_f). The residual then acts on the canonical momentum density P_j.
  - Corrected form: **R_j = h_g(w_gθ_g I − w_fθ_f X)² P_j.** It is still a positive-semidefinite perfect square.
  - θ_f/θ_g = 1/det X, so the residual depends on det X as well as X.
  - The single-metric limit (θ=1 → h^{ij}P_j) shows the weights cannot be dropped.
  - K1 passes for both forms (θ_g = θ_f at X=I). That is why the omission went unnoticed.
  - The two forms differ off X=I. For X = cI, the corrected form goes as (1−c⁻²)², not (1−c)².
  - My own round-2 formula had the same omission; corrected.
  - The derivation is analytic and checked against the single-metric limit. Both lanes should reproduce or refute it.
- **"w = 1 forced by K1" is circular.** K1 checks residuals; it does not select the constraint combination. Even as a constraint it only fixes w at X=I. The HR second-class weights are field-dependent and come from the first-class/second-class split (K0′). AC's "forced, not chosen" should be withdrawn.
- **Cursor R3-A (B1/B2 is not a W·P counter-term) is plausible but schematic.** The on-shell trade through C_j ≈ 0, which contains ∇π_f, is asserted, not checked. I record it as "plausible", not "established".

## Proposed additions
- **F16:** a residual stated in undensitized ψ†∂ψ, or without θ weights.
- **F17:** K1 used as a selection principle.

## Posteriors
Unchanged: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

## Asks
- **AC:** amend the ratified closed form and withdraw "w=1 forced", before Greg's round-4 GO.
- **Lanes:** the round-4 D-matrix test must target h_g(w_gθ_g − w_fθ_f X)²P_j, with the w's derived from K0′.
