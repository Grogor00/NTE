# DIRECTIVE — Scratch → Cursor Main · cc AC, Greg, Jammer · 2026-10-21

**Authority:** Greg (2026-10-21 ~23:19 NZDT): "you can pass computations on to cursor… you can check yourself, and get cursor to run parallel checks." This is the decisive Opsi2 object; Scratch specifies + checks, Cursor runs the heavy parallel pass. AC rules the terminal fork.

**This answers Cursor's own ask** (`Working\Opsi2_Steps123_VERDICT_CursorMain_G4_K0_Pass_Cross_Not_In_C_N_Self_Bracket_Chi_Uncomputed_20261021.md` §4): yes — the next object is exactly the χ-correction to {C_N, C_N}.

## The object
The χ-corrected Dirac self-bracket of the **correct** gate (ratified: `Handoffs\RULING_AC_BD_Gate_Is_HR_Coefficient_Of_Ng_Not_C_SC_Cross_Piece_Relocates_To_Secondary_20261021.md`):
  C_N = C_HR + E_g + (Dn)·p  (matter = g-frame Dirac energy E_g = C_g^(ψ) only).
Compute the ∂δ coefficient of {C_N(x), C_N(y)}_D at O(ψ²), with
  {A,B}_D = {A,B} − {A,χ} C⁻¹ {χ,B},  χ = π_ψ − i(Σ_g+Σ_f)ψ,  C⁻¹ ~ Σ⁻¹,  Σ = Σ_g+Σ_f.
Decompose:
  {C_N,C_N}_D|_∂δ = [Poisson diagonal: h_g·p_j]  +  [χ-correction: −{E_g,χ}C⁻¹{χ,E_g}].

## The decision — M-a vs M-b, then weak vanishing
- **M-a (clean):** the χ-correction's ∂δ coefficient is f-independent / frame-matched / reduces to constraints → the gate self-bracket closes weakly, step 2 passes, the decision moves to the secondary {C,H₀}.
- **M-b (χ-entangled; Jammer favours, and the Σ_g/Σ factor makes it live):** the χ-correction carries genuine X/f-dependence that does NOT reduce to the constraint set → the frame-mixing is in the gate's own self-bracket.

**Key discriminant, already partly computed (Cursor R3, `Working\Opsi2_Round3_Dirac_Bracket_Coefficient_VERDICT_CursorMain_..._20261019.md`):** the χ-correction's field content is **(spinor bilinear ψ†α^kψ) × (π-structure)** with a Σ_g/Σ prefactor — structurally distinct from **(metric weight) × (Dirac momentum p_j)**. If that distinctness holds for the DIAGONAL self-correction too, the χ-correction cannot be absorbed into C_i^tot ∝ p_j, and M-b lands with non-closure. Confirm or refute this for the diagonal {E_g,χ}C⁻¹{χ,E_g} (R3 established it for the gravity–matter cross; the diagonal is the new piece).

## Weak-vanishing test (the fork decider) — with Jammer's guards
Project {C_N,C_N}_D onto the FULL constraint span {C_N, C_i^tot (grav + matter p_i), χ} and compute the residual:
- **F23:** projection onto the constraint span, NOT a scalar fit.
- **F19:** substitute the MATTER-MODIFIED multiplier n^i(γ,f,π) (with matter), not the pure-HR n.
- **F22:** Dirac bracket throughout (the Poisson self-bracket already passed — that is not the test).
- **F20:** gate is C_N (coeff of N_g), never C_g−C_f.
- **F21:** L-sector active (four L-constraints), not inert.
- **K5 control:** the dof count must be invariant under redefining the OTHER metric's shift (lapse-role swap).

Outcome mapping (Jammer W-forks): residual weakly zero → **W-0** (G-1 path opens, not yet G-1); non-vanishing that SURVIVES the matter-modified multiplier → **W-1 = G-2 (5.5-mode)**; still uncomputed → **W-2 = G-4**.

## Engines / protocol
NumPy ∥ Wolfram Engine 15, both run (your established protocol). File your pre-registration before compute, blind to this directive's expectations. Report field content explicitly and all stats in JSON.

## Scratch independent check (baseline for your parallel run) — Wolfram, 200 random SVC backgrounds
- G = h_g X symmetric on SVC: max dev 2.7e-15.
- h_g + h_f − 2G = h_g(I−X)²: max dev 2.3e-14; weighted w_g²h_g−2w_gw_fG+w_f²h_f = h_g(w_g I − w_f X)²: max dev 7.7e-14.
- **Correct gate Poisson self-weight = h_g: X-free, min magnitude 3.3, still 3.9 at X=I (never vanishes).**
- **Mis-identified C_g−C_f self-weight = h_g(I−X)²: X-dependent, exactly 0 at X=I.**
⇒ the Poisson self-bracket of the correct gate carries no X-mixing (confirmed); the whole question is the Dirac χ-correction above.

**Standing:** No Core. No f. P04 unchanged. Forks and license: `Working\PREREGISTRATION_Scratch_Opsi2_Steps2to3_..._20261021.md`. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Scratch