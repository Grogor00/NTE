# T1 VERDICT — does the C21 seed pin N_e?

**From:** Jammer · **To:** AC · **Cc:** Greg, Scratch, PC · **Date:** 2026-09-24
**Answers:** `Handoffs\Handoff_AC_to_Scratch_Jammer_C21_Seed_Boundary_Data_Research_Directive_20260924.md` §T1.
**Register:** computation on Companion 17's own potential and kinetic term; standard slow-roll and e-fold budget. Speculation-tier directive, but the result bears on a **deposited** conditional.

## Pre-registered fork (AC's, registered in the directive before computation)
- N_e near 63.4 → the existing prediction is reinforced and derived.
- N_e elsewhere → C21 falsifies the current (n_s, r), or is itself falsified. Report it; do not smooth it.
- The budget does not close without new commitments → say so.

## Result: third branch for C21, second branch for the corpus

**1. C21 does not pin N_e.** The pivot horizon-exit count N_* depends only on the history *after* the pivot left the horizon (V_*, ρ_end, reheating, k_*/a₀H₀). It does not depend on how inflation began. The seed is an initial or boundary condition, so it cannot enter N_*. The most it can set is the *total* inflation, and even that it does not fix:
- Companion 17's potential is a plateau: V_E → 36λM⁴ ≈ (9.3 × 10¹⁵ GeV)⁴.
- An initial energy of about 1.6 ρ_Pl (the NTFN rescaling) cannot sit in V_E. So nothing ties the initial Φ to the seed, and the total e-fold count is free.
- C21's only budget consequence is a **lower bound**: N_total ≥ 64.2 (|Ω_k| < 0.004) or ≥ 64.9 (|Ω_k| < 0.001). Any Φ_initial ≳ 16.5 M satisfies it.

**2. The budget closes without C21, and it does not land on 63.4.** Companion 17 reproduces exactly: 63.4 → (0.9692, 0.0053) with φ* = 16.35, and 55 → (0.9646, 0.0070). Feeding its own V_*, derived from A_s = 2.1 × 10⁻⁹ and its own r, into the standard relation (Planck 2018 inflation paper, eq. 47; k_* = 0.05 Mpc⁻¹, H₀ = 67.6, g = 106.75) gives:

| Post-inflation history | N_* | n_s | r | vs P-ACT-LB 0.9743 ± 0.0034 | vs Planck 0.9649 ± 0.0042 |
|---|---|---|---|---|---|
| Instant reheating (**upper bound** for w ≤ 1/3) | **56.0** | **0.9652** | **0.0067** | **−2.7σ** | +0.1σ |
| w = 0 reheating, T_rh = 10¹² GeV | 53.4 | 0.9636 | 0.0074 | −3.2σ | −0.3σ |
| w = 0 reheating, T_rh = 10⁹ GeV | 51.1 | 0.9620 | 0.0080 | −3.6σ | −0.7σ |

**Reaching 63.4 requires about 7.4 extra e-folds.** That means a long stiff (w > 1/3, kination-like) epoch after inflation, and the corpus has none: it has standard radiation and standard BBN.

**3. Where 63.4 comes from.** N_e = 63.4 is exactly **−ln(β_NTE · M_Pl)**, using the non-reduced M_Pl (value 63.406). Part 1 §2.4 already classes that reading ("n_s = 1 − 2/N_e with N_e = −ln(β_NTE M_Pl)") as conditional and not a passed test. Companion 17's "corpus default N_e = 63.4" therefore carries over a number whose basis the corpus has already withdrawn. It is not the pivot exit count.

## Verdict
- **C21 contributes no N_e pin.** C21 §12 should say so in one sentence.
- **Standing finding for AC and Greg; not caused by C21, found in the course of T1.** The budget-consistent value for Companion 17's own model is N_* ≤ 56, giving **(n_s, r) ≈ (0.965, 0.007)**. Consequences:
  - It fits Planck 2018.
  - It sits **2.7σ or more below P-ACT-LB**, getting worse with realistic reheating.
  - r ≈ 0.007–0.008 remains in the CMB-S4/LiteBIRD window.
- The registered (0.9692, 0.0053) holds only with an unmotivated extra 7 e-folds.

This is the "lands elsewhere" branch of the fork, applied to the deposited conditional. It is reported, not smoothed.

## Recommended (Greg ratifies; AC authors)
- **Companion 17 §3:** replace "corpus default N_e = 63.4" with the budget-derived N_* ≤ 56.0 (instant-reheating bound). Quote **(0.9652, 0.0067)** as the headline conditional, with the reheating band beside it.
- Keep 63.4 only with its source stated (−ln β_NTE M_Pl), labelled as requiring a non-standard post-inflationary history.
- Update the Part 3 prediction register and Manifest §3 to match.
- State the P-ACT-LB tension on its face, as was done for w = −1.

## Caveats
- Assumes Companion 17's frame closure and Lorentzian slow-roll, which are its own flags 1 and 3. The σ values assume Gaussian errors on quoted anchors.
- Unit convention: M in F = M² + Φ²/6 is taken as the reduced Planck mass, consistent with φ* = 16.35 reproducing exactly.
- Scratch should re-derive N_* independently before AC acts, including the ρ_end definition and g_th.

## Script
`scratchpad t1.py` (numpy/scipy): slow-roll on K(Φ) = (1+Φ²/3)/(1+Φ²/6)², V = Φ⁴/(1+Φ²/6)²; ε = 1 end; Planck-2018 eq. 47 self-consistent solve. Available on request; core lines:
`N* = 67 − ln(k*/a0H0) + ¼ ln(V*²/ρ_end) − (1/12) ln g_th + (1−3w)/(12(1+w)) ln(ρ_th/ρ_end)`, with `V* = (3π²/2) A_s r`.

— Jammer
