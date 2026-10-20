# Opsi2 — STEP 1 (the mapping) VERDICT (Scratch): HR's BD gate is the coefficient of the single g-lapse N, not C_g − C_f; the frame-mixing cross piece relocates to the secondary

**Lane:** Scratch (construction lead). **Date:** 2026-10-21. **Under:** `Handoffs\CORRECTION_AC_F12_Premise_False_HR_Requires_Weak_Vanishing_S_Block_Not_Last_Object_20261021.md` §4 step 1; Greg's GO 2026-10-21 12:53 NZDT.
**Register:** original work (source-structural). No Core. No f. P04 unchanged.
**Sources read at canonical state this session:** `arxiv.org/pdf/1111.2070` §4 (bimetric), eqs (4.4)–(4.8), cross-read with §2–3 (recorded in `Working\HR_1111_2070_CANONICAL_PDF_Confirmed_By_Scratch_Statement_ii_Equation_For_N_5p5_Modes_Closed_All_Four_Confirmed_L_Sector_Four_Constraints_Refines_Mapping_20261021.md`). Corpus setup re-read: `Working\Opsi2_Constraint_Chain_REFERENCE_action_N_naive_double_kinetic_Dirac_two_vierbeins_full_Dirac_Bergmann_chain_staged_once_...20261020.md`; `Handoffs\Directive_AC_Compute_Full_Opsi2_Bracket_Set_And_Run_Dirac_Bergmann_Chain_To_End_20261019.md`.

## The question (step 1)
Does the shared-π_ψ frame-mixing cross piece (corpus weight G = h_g X, from {C_g^(ψ), C_f^(ψ)} via the Dirac bracket through χ) sit in the self-bracket {C, C} of the BD gate, or in the secondary channel {C, H₀}? This turns on WHICH constraint is HR's BD gate.

## Finding — from HR 1111.2070 §4 (canonical PDF)
HR's bimetric constraint **C is a single scalar, the coefficient of the single g-lapse N** — eq (4.4): L = M_g²π^ij∂_tγ_ij + M_f²p^ij∂_t f_ij − H₀ + N C.
- Eq (4.6): C = M_g² R⁰(g) + M_g² R(g)_i D^i_j n^j + 2m²M_eff²√det γ V. **"The bimetric constraint C is identical to that defined above for massive gravity (2.13)."**
- **The f-sector Hamiltonian R⁰(f) does NOT appear in C — it appears in H₀, multiplied by the f-lapse L.** C depends on f_ij only through n^i and the potential V (gravitational), and is independent of p^ij.
- The f-lapse L and f-shift L^i are **non-dynamical** (Lagrange multipliers); varying them produces the four additional constraints. n^i = n^i(γ, f, π) (eq 4.8), independent of N, L, L^i, p^ij.

**So HR's BD gate is C = coeff of N_g, and C ≠ C_g − C_f** — a difference would carry R⁰(f) with a sign; HR's C does not (R⁰(f) is in H₀). This is cross-consistent with the massive-gravity §2 structure (single constraint) and with Soloviev 2006.16230 (one lapse N̄ multiplies the tetrad primary ð®).

*Strength (register-discipline): the prose statements above extracted cleanly from the canonical PDF; the detailed index structure of (4.6) is as-rendered by the PDF→markdown pass, not independently re-derived. The structural conclusion — C is g-sector gravitational + potential, with R⁰(f) and the f-frame content in H₀ — does not depend on those indices and is triple-sourced (1111.2070 §2 and §4, Soloviev).*

## Consequence — the cross piece relocates, using the corpus's OWN computed brackets
The matter content of the gate C is the g-frame Dirac energy C_g^(ψ) only (coefficient of N_g). Therefore:
- **{C, C} matter self-bracket = {C_g^(ψ), C_g^(ψ)} → weight h_g (frame-matched, healthy).** The dangerous cross weight G = h_g X does NOT appear in {C, C}, because C_f^(ψ) is not in C.
- **The cross weight G = h_g X enters {C, H₀}** — because C_f^(ψ) is the matter piece of H₀'s f-lapse coefficient. {C, H₀} is exactly the secondary C^(2) (the corpus's ð®). So the frame-mixing cross piece lives in the SECONDARY, not the self-bracket.

The corpus's individual bracket computations survive — h_g, h_f, and G = h_g X are correct brackets; what changes is which of them assemble into the BD gate. The gate's self-bracket sees only h_g; the secondary sees G = h_g X.

## What this overturns (recognition-gate, class level)
The corpus's identification **C_SC ≈ C_g − C_f ("K1-forced equal weight") as HR's second-class BD gate is not HR's constraint.** HR's gate is the asymmetric coeff-of-N_g object C with R⁰(f) removed to H₀; the symmetric difference C_g − C_f is a different object. Consequently:
- **Q-Stage3** (`Working\Opsi2_Q_Stage3_VERDICT_Scratch_lands_G4_sharpened_cross_weight_not_in_span_hg_hf_20261020.md`) computed the self-bracket {C_SC, C_SC} of that mis-identified object, so its R_j = h_g(I−X)² p_j = h_g + h_f − 2G is **not the matter contribution to HR's BD gate {C, C}** (which is h_g alone). The G-4 *verdict that the fork is open* survives — the fork IS still open — but its *reasoning* (the cross piece makes the gate's self-bracket fail to close) is mis-targeted: the cross piece is not in the gate's self-bracket.
- This is a deeper correction than the F12 premise (weak-vanishing vs absorption). The error class is "identifying the symmetric difference C_g − C_f as HR's gate without checking HR's actual constraint," tracing through R3 (C_SC weight), the R_j closed form, and Q-Stage3. **The R_j computation and its brackets are NOT void** — they are correct brackets of a non-gate combination, reusable where that combination legitimately appears (notably in assembling the secondary, where G = h_g X now belongs).

I flag this for AC/Greg ratification; I do not unilaterally declare the C_SC thread void — the brackets stand, their assembly into the gate is what is corrected.

## Sharpened targets for steps 2–3 (pre-registered alongside)
- **Step 2 (K0′, control):** {C, C} with g-frame Dirac matter → expected weakly zero via the Dn channel (single-dynamical-metric Dirac; frame-matched weight h_g).
- **Step 3 (decisive):** the secondary C^(2) = {C, H₀} carries G = h_g X; its preservation {C^(2), H} decides G-1/G-2/G-3/G-4, gated on surviving the matter-modified multiplier n^i(γ,f,π).

**Posteriors held** (a source-structural reframe is not a fork landing): G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Scratch