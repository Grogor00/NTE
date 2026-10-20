# DIRECTIVE — Scratch → Cursor Main · cc AC, Greg, Jammer · 2026-10-21

**Authority:** Greg's pass-to-Cursor instruction (2026-10-21). **This is the likely FINAL object before the terminal fork.** Both lanes converge on M-b/W-1 (G-2) at the two-leg-contraction level; two shared assumptions remain, and they are what AC will want discharged before ratifying.

## Object — recompute the gate self-bracket matter weight {C_N,C_N}_D|_∂δ, discharging:
**(A) Spin connection + full Grassmann expansion.** The current scripts (yours and my cross-check) use the two-leg contraction E_g ⊃ Σ_g ψ†α^k∇_kψ with the ∇ reduced to ∂. Include the spin-connection pieces of ∇_k and do the term-by-term Grassmann expansion of −{E_g,χ}C⁻¹{χ,E_g}. **Question:** do the added ∂δ-covectors change the matter weight away from Σ_g²/Σ, or is Σ_g²/Σ stable?

**(B) Densitized canonical spinor φ = Σ^{1/2}ψ.** Redo the computation in the variable that makes {φ, π_φ} canonical with unit weight (Σ = Σ_g+Σ_f). Recompute BOTH the gate self-bracket matter weight AND the momentum-constraint matter weight in φ. **Question:** does the ratio (bracket weight)/(constraint weight) = (Σ_g/Σ)² persist, or does the frame-differential rescaling Σ_g vs Σ_f make them co-transform so the ratio → 1? This is the deeper form of the π~Σψ attack point; a *common* rescaling leaves the ratio invariant (I verified), but φ is NOT a common rescaling.

## Decision (pre-commit before compute)
- Ratio ≠ 1 survives (A) AND (B), and residual survives the projection onto the full constraint span incl. L-shift → **terminal G-2 (5.5-mode)**.
- Ratio → 1 under (A) or (B) → **M-a**: step 2 truly passes, decision moves to the secondary {C, H₀}.
- Uncomputable at O(ψ²) → **G-4**, name the blocker.
Guards: F19–F23, K5 lapse-swap. Engines NumPy ∥ Wolfram, both run; file prereg before compute.

## Scratch cross-check baseline (compare against)
Two-leg level (400 backgrounds): single-constraint residual median 0.46; **enlarged span incl. L-shift residual median 0.093, 100%>10⁻³, min 0.0016**; Σ_f=0 control → 10⁻¹⁶; (Σ_g/Σ)² invariant under common rescale. I will run the φ-invariance test (B) independently in parallel.

**Standing:** No Core. No f. P04 unchanged. Forks/license: `Working\PREREGISTRATION_Scratch_Opsi2_Steps2to3_..._20261021.md`. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Scratch