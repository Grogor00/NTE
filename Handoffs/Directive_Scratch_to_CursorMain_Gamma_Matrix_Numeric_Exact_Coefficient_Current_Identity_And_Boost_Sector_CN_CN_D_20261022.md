# DIRECTIVE — Scratch → Cursor Main · cc AC, Greg, Jammer · 2026-10-22

**Authority:** Greg's pass-to-Cursor model. Scratch has derived the weight = Σ_g²/Σ in the aligned sector (`Working\Opsi2_CN_Dirac_Chi_Weight_DERIVATION_Scratch_..._NotBlind_20261022.md`). These are the referee-grade pieces that remain; run them on the γ-matrix engines, I cross-check.

## Object — explicit γ-matrix computation of {E_g,E_g}_D's ∂δ term
Use explicit Dirac γ-matrices (incl. the g-frame spin connection ω^{ab}γ_ab written out). Compute −{E_g,χ_a}(C⁻¹)^{ab}{χ_b,E_g} and extract the ∂δ coefficient. Three deliverables:

1. **Exact coefficient.** Confirm the weight is exactly Σ_g²/Σ (not Σ_g²/Σ × a γ-trace factor that differs from the constraint's). Report the numerical coefficient.
2. **Current identity.** Determine the bilinear the ∂δ term actually carries — the local vector current ψ†α^kψ, or the canonical momentum density ψ†∂_kψ — and whether it is the SAME bilinear that appears in the total momentum constraint C_i. (Your CN verdict said "same monomial p_j"; verify against the γ-matrix result, since the subtraction naively gives ψ†α^kψ.)
3. **Boost sector (the new one, from Deffayet 1208.4493).** Repeat with X carrying a relative-boost component (time-legs NOT parallel: γ^a f_a^0 = Λ γ⁰ Λ⁻¹, Λ a boost), instead of the purely-spatial 3×3 X. Does the weight stay Σ_g²/Σ, or does the relative boost change it? This decides whether G-2 is aligned-sector-only or general.

Decision: coefficient = Σ_g²/Σ and current = C_i's current → antecedent fully confirmed (aligned sector). Boost changes it → G-2 is aligned-sector-only; name the boost dependence. Engines NumPy ∥ Wolfram; prereg before compute.

## Scratch baseline
Aligned-sector derivation: C ∝ Σ (both legs ∝ γ⁰), {E_g,χ} ∝ Σ_g, product Σ_g²/Σ. Projection residual (constraint span incl. L-shift) survives ∝ Σ_gΣ_f/Σ, →0 at Σ_f=0. I run the boost-sector cross-check independently.

**Standing:** No Core. No f. P04 unchanged. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Scratch