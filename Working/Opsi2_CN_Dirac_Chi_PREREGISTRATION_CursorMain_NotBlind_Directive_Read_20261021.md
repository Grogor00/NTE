# PRE-REGISTRATION — Cursor Main: χ-corrected {C_N, C_N}_D

**Filed before the run.** Not blind: `Handoffs\Directive_Scratch_to_CursorMain_…_Chi_Corrected_…_20261021.md` was the assignment and was read. The tests below are fixed anyway.

**Gate:** C_N = C_HR + E_g + (Dn)·p only (F20). Not C_g−C_f.  
**Bracket:** Dirac, {A,B}_D = {A,B} − {A,χ}C⁻¹{χ,B}, χ = π_ψ − i Σ ψ, Σ = Σ_g+Σ_f (F22).  
**Engines:** NumPy ∥ Wolfram. No Core.

## What will be computed
The ∂δ monomial of the diagonal correction −{E_g,χ}C⁻¹{χ,E_g}, using the R3 factorisation (E_g ⊃ Σ_g ψ†α^k ∇_k ψ; C⁻¹ ∼ Σ⁻¹).

## Decision (pre-committed)
- If that coefficient is ∝ p_j with a scalar that equals the coefficient in C_i^tot for every Σ_f, including Σ_f=0 as a control → **M-a / W-0**.
- If a projection of the ∂δ covector onto span{C_i^tot = R_i + (matter momentum)} leaves a residual that stays nonzero when Σ_f≠0, including after n is varied (F19), and the fit is a projection not a scalar α (F23) → **M-b / W-1 (5.5-mode G-2)**.
- If the monomial or the projection cannot be evaluated → **W-2 / G-4**.

**K5:** repeat with Σ_g ↔ Σ_f. The obstruction, if any, must be the same kind on both gates.  
**K1 control:** Σ_f=0 ⇒ residual consistent with 0.

— Cursor Main, 2026-10-21.
