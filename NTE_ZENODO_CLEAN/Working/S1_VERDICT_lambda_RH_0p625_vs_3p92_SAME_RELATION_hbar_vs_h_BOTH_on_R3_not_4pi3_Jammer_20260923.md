# S1 VERDICT — λ/R_H = 0.625 vs 3.92

**From:** Jammer · **To:** AC · **Cc:** Greg, Scratch, PC, Cursor · **Date:** 2026-09-23
**Answers:** `Handoff_AC_to_Scratch_Jammer_C21_Blockers_And_GATE4C_20260923.md` §S1.
**Source checked:** `C:\Users\gregw\Desktop\NTE_historical_archive\NTE v10_5\01_Master\NTE_v10_5_9.md` — §5.1 (lines 430–446), §5.3 (line 465), §5.4 (line 471), §6.5 (line 523). Canonical cross-check: `G:\My Drive\NTE_ZENODO_CLEAN\Core_Papers\NTE_v10_19_0_Part1_Foundations.md` §V.
**Register:** arithmetic verdict. Closed.

---

## Verdict

**The two figures don't contradict each other. They are one relation, reduced one way and unreduced the other.** Take the trigger condition in the form the corpus's own formula actually uses, n_γ · R_H³ = 1, together with Planck statistics. This gives

  x ≡ kT_reset · R_H / (ħc) = (π²/2ζ(3))^(1/3) = **1.60121**

and from that:

| Quantity | Value | Corpus figure |
|---|---|---|
| ħc/(kT·R_H) — the **reduced** thermal wavelength over R_H | **0.62453** | 0.625 (§5.3) |
| hc/(kT·R_H) = 2π × the above — the **unreduced** thermal wavelength over R_H | **3.92402** | 3.92 (§6.5) |

They are the same thing with and without the 2π: 0.62453 × 2π = 3.92402. The 1.60 and 0.625 in the NTFN-v7.1 rescaling ("λ′ = 0.625 l_P, E′ = 1.60 E_Planck, ρ′ = 1.60 ρ_Planck") are x and 1/x. Neither figure is a mistake. What's missing is a label saying which wavelength each one means.

**Neither figure is the wavelength of a typical photon.** For a blackbody at T_reset (same convention):
- Wien-peak wavelength / R_H = 0.790
- wavelength of a mean-energy photon (E = 2.701 kT) / R_H = 1.453

So "the seed photon's wavelength is 0.625 R_H" (§5.3, §5.4) and "the trigger photon has wavelength 3.92 R_H" (§6.5) are both overstatements of precision. The defensible statement is **order R_H**. That is what canonical Part 1 §V already says ("wavelength ∼ R_H"), and it holds under any convention.

## Second finding — a convention defect in the trigger condition itself (reaches the deposit set)

v10.5.9 §5.1 defines **V_H = (4π/3)R_H³** and states "setting n_γ × (4π/3)(c/H_dS)³ = 1 … kT_reset = ħH_dS(π²/2ζ(3))^(1/3)". **That derivation step is wrong.** The formula shown, and T_reset = 2.213 × 10⁻²⁹ K, both follow from **n_γ · R_H³ = 1** with no 4π/3:

| Convention | kT·R_H/ħc | T_reset (H_dS = H₀√Ω_Λ, H₀ = 67.6, Ω_Λ = 0.685) | photons per (4π/3)R_H³ |
|---|---|---|---|
| n_γ R_H³ = 1 (formula actually used) | 1.6012 | **2.218 × 10⁻²⁹ K** ≈ corpus 2.213 | **4.19** |
| n_γ (4π/3)R_H³ = 1 (as stated) | 0.9933 | 1.376 × 10⁻²⁹ K | 1 |

The small 2.218 vs 2.213 gap comes from input rounding (H₀ and Ω_Λ) and is immaterial. The ratio between the two conventions, (4π/3)^(1/3) = 1.612, is not immaterial.

- §5.1's line "Substituting back verifies N_γ = 1.00000000 photons per Hubble volume" is **false as written**. With the stated V_H, the count comes out at 4π/3 ≈ 4.19 photons.
- The archive's earliest form, `ntfn_v25_progress.docx` §2.3, writes the trigger as "n_gamma * R_H^3 = 1". That is the original convention. The (4π/3) definition was added later without updating the formula. **This, rather than a λ/R_H inconsistency, is the real 5-month propagated defect.**
- **Canonical Part 1 §V (v10.19.0)** carries "n_γ V_H = 1" and the same T_reset formula, but never defines V_H. Read with the conventional V_H = (4π/3)R_H³, the formula is off by 1.612. This is **deposit-set text** and needs a one-line fix before Zenodo. Deposited PDFs aren't touched otherwise: Part 1 carries no λ/R_H figure.

### Remedies (AC to choose; Greg ratifies)

- **(a) Recommended, minimal.** Define the trigger as one photon per **R_H³** (a Hubble cube), which is what the formula has always used, and say so explicitly. Keep T_reset as is. Part 1 §V change: "one photon per Hubble volume ($n_\gamma R_H^3 = 1$, with $V_H \equiv R_H^3$)".
- **(b)** Keep V_H = (4π/3)R_H³ and correct the formula to kT_reset = ħH_dS(3π/8ζ(3))^(1/3) and T_reset ≈ 1.38 × 10⁻²⁹ K, then check whether anything downstream (N_total ≈ 140.2, which moves by ln 1.612 ≈ 0.48 e-folds) needs re-stating.

Neither choice has a physics preference. "One photon per Hubble volume" is an order-of-magnitude trigger, and the factor 4π/3 is a convention, not a derivation. **The point is to state one convention and match the formula to it.** Choosing (a) keeps every downstream number. Choosing (b) moves T_reset and N_total. This is a register call, so it's Greg's.

## For C21 §5

- Replace both figures with **λ ∼ R_H**. If a number is wanted, state it with its label: "the reduced thermal wavelength ħc/kT_reset is 0.62 R_H under the n_γR_H³ = 1 convention". Do not call either number "the seed photon's wavelength".
- The §5.3 claim that the ratio is "universal … the same for all parent universes regardless of their α" **survives**. x = (π²/2ζ(3))^(1/3) is a pure number, whichever convention is used.

## Downstream sweep

- **Deposit set:** one line, Part 1 §V (per remedy a or b). Cursor's G2 grep found 0 hits for λ/R_H in Core_Papers, Popular_Editions, Pedagogical_Notes and Book, so there is nothing else to fix there.
- **The 60 archive files:** no correction sweep. They are archive, and the figures in them are internally consistent once labelled. Record this verdict as the reading key rather than editing history.
- **C21:** PC applies the §5 wording above.

S1 is closed. Nothing in this changes κ, δ_J, θ₂₃ or any other register entry.

— Jammer, 2026-09-23
