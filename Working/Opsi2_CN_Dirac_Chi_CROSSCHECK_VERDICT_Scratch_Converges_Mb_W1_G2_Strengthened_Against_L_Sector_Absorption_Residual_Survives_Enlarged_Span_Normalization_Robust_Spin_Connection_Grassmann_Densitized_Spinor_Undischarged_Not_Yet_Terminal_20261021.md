# Opsi2 — {C_N,C_N}_D cross-check VERDICT (Scratch): converges with Cursor on M-b / W-1 (G-2, 5.5-mode); strengthened against the L-sector-absorption escape; two shared assumptions remain undischarged, so NOT yet a ratifiable terminal G-2.

**Lane:** Scratch (construction lead / cross-check). **Date:** 2026-10-21. **Per:** Greg's instruction (2026-10-21 ~23:19 NZDT) — Scratch checks independently, Cursor runs the parallel heavy pass. **Read at body this session:** Cursor's verdict `Working\Opsi2_CN_Dirac_Chi_VERDICT_CursorMain_Mb_W1_Weight_Sigma_g_Squared_Over_Sigma_Not_Constraint_Weight_20261021.md`; AC's ruling `Handoffs\RULING_AC_Scratch_Self_Correction_Accepted_K0prime_Passed_Three_Lanes_G4_Blocker_Is_Dirac_Chi_Channel_20261021.md`; Cursor R3 `Working\Opsi2_Round3_Dirac_Bracket_Coefficient_VERDICT_CursorMain_..._20261019.md`. No Core. No f. P04 unchanged.

## The object and Cursor's claim
Diagonal χ-correction of the gate self-bracket: −{E_g,χ}C⁻¹{χ,E_g}|_∂δ ∝ **(Σ_g²/Σ) p_j** (two g-legs, no π_f, so R3's bilinear×π distinctness does NOT apply — same monomial p_j). The total momentum constraint matter piece is π_ψ∂_iψ ∝ **Σ p_j**. Weights differ by (Σ_g/Σ)² ≠ 1 for Σ_f≠0 → does not vanish weakly → M-b / W-1 (G-2, HR case 1: lapse fixed, odd phase space / 5.5 modes).

## My independent check (Wolfram, 400 random backgrounds)
1. **Reproduce (single-constraint projection onto C_i^tot).** v = R_g + (Σ_g²/Σ)p, u = R_g + Σp: **median residual 0.46** (all 400 > 10⁻³). Matches Cursor's 0.40–0.42 (difference = my simplified gravitational modeling). Cursor's arithmetic confirmed.
2. **Adversarial enlargement (my addition — the F21 "L-sector absorbs it" escape Cursor did not test).** Enlarge the span to include the L-shift momentum constraint (modeled R_f + Σ_f p, carrying matter p_i). Least-squares residual: **median 0.093, min 0.0016, 100% of 400 > 10⁻³.** The L-sector reduces the mismatch (~0.46→~0.09) but **cannot eliminate it.** Analytic reason: matching the R_g and R_f gravitational coefficients forces the p-weight to Σ_g, never Σ_g²/Σ unless Σ_f=0; the deficit ∝ Σ_g Σ_f/Σ.
3. **Control.** At Σ_f=0 (single-frame limit): residual = O(10⁻¹⁶) in both spans. Clean — the ghost indication is entirely a doubly-coupled (Σ_f≠0) effect.
4. **Normalization-robustness.** The p-weight ratio (Σ_g/Σ)² is invariant under common spinor rescaling (Σ_g,Σ_f)→s(Σ_g,Σ_f). Rules out the naive π-normalization attack (for a frame-common rescaling).

## Landing — converge, strengthen, but hold short of terminal
**M-b / W-1 (G-2, 5.5-mode) is now a strong, two-lane, adversarially stress-tested INDICATION:** the gate's own χ-corrected Dirac self-bracket does not vanish weakly; the Boulware–Deser secondary fails to exist (HR case 1), so doubly-coupled Dirac matter revives the ghost at O(ψ²). My enlarged-span test closes the most obvious M-a escape (L-sector absorption), which Cursor's single-constraint projection had left open.

**Not yet a ratifiable terminal G-2 — two assumptions remain undischarged, shared by BOTH numerical models (honest negatives):**
- **(A) Spin connection + full term-by-term Grassmann expansion are omitted from both scripts** (Cursor's own load-bearing caveat). Those are additional ∂δ-covectors; they could shift the bracket weight away from Σ_g²/Σ. Until included, the weight is a two-leg-contraction estimate.
- **(B) The densitized-spinor normalization.** I confirmed robustness under *common* rescaling, but the physical canonical variable φ = Σ^{1/2}ψ redistributes Σ_g vs Σ_f *frame-differentially* — a non-common rescaling not tested here. This is the deeper form of the attack point Cursor flagged ("π ~ Σψ"). If φ makes the bracket and constraint weights co-transform, the ratio could move.
- Both projection spans (Cursor's and mine) are **structural models** of the HR constraint algebra, not the explicit algebra.

## Recommendation
Discharge (A) and (B) — spin-connection/Grassmann ∂δ terms, and the φ=Σ^{1/2}ψ densitized recomputation — as the next (and likely final) object before AC rules the terminal fork. Suitable for Cursor's parallel engines with my cross-check; I will run the φ-redefinition invariance test independently. **For AC/Greg:** the evidence favors G-2, but ratification should wait on (A)+(B); I do not move posteriors unilaterally.

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Scratch