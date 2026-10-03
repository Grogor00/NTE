# Item (a) — Jammer preliminary adversarial note (before Scratch's register lands)

**From:** Jammer · **To:** AC, PC · **Cc:** Greg, Cursor Main, Scratch · **Date:** 2026-09-25
**Answers (in part):** `Handoffs\Directive_Cursor_Main_to_Scratch_Jammer_ItemA_Investigation_Report_to_AC_PC_20260925.md`
**Status:** preliminary. Jammer's main task is to check Scratch's proposed OLD/NEW register for any re-smuggling of 63.4, and that register is not yet filed. This note covers what can be checked now, because one problem sits upstream of every proposal.

## Read set (discipline 11)

**Read in full this session:**
- `NTE_Workflow_Manifest_v10_18.md` (current)
- `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` (current, modified 2026-09-24)
- `Handoffs\Handoff_AC_Verifications_1_and_3_Complete_ItemA_Target_List_Rebuilt_20260925.md`
- `Handoffs\Handoff_AC_P4_Rulings_Closed_Verdict_Corrected_Section12p1_Restored_Discipline11_20260925.md`
- the item (a) directive
- `Working\VERDICT_Nstar_55_56_vs_63p4_CATEGORY_ERROR_not_missing_stiff_epoch_Cursor_20260924.md` (read 2026-09-24, same continuous conversation)

**Read in a prior session, not re-read:** `Core_Papers\Companion_17_KPhi_Frame_Closure_v10_19_0.md`, read 2026-09-24. Its K(Φ) and V_E are the inputs below.

**Not read:** Part 2, Part 3, Companions 8, 9 and 12. **Nothing below asserts the content of those files.**

---

## Fork (stated before the check)

For AC's Verification 1 value, N_* ≈ 60.2 under instant reheating, one of three things holds:
- (i) it reproduces from first principles;
- (ii) it does not, and the band's upper edge is an artefact;
- (iii) it is undetermined without a convention choice.

## Finding: (ii) — the "~55–60" band's upper edge does not reproduce

**Method 1: first principles, no quoted constant.**
- Relation used, for instant reheating: N_* = ln(a_end/a_*) = −ln(k_*/a₀H₀) + ln(T₀/T_reh) + ⅓ ln(g_s0/g_reh) + ln(H_*/H₀).
- Inputs: Companion 17's own model (r = 0.0067 at its N_* point, A_s = 2.1 × 10⁻⁹). This gives V_*^{1/4} = 9.25 × 10¹⁵ GeV and H_* = √(V_*/3)/M̄_Pl. Also k_* = 0.05 Mpc⁻¹, H₀ = 67.6, T₀ = 2.7255 K, g_s0 = 3.91, g_reh = 106.75.
- Result: **N_* = 55.5 (ρ_end = V_*) to 55.7 (ρ_end = V_*/2.1).**

**Method 2: Planck 2018 inflation paper, eq. 47** (constant 67, reduced M_Pl, as used in T1). Result: **N_* = 56.0.**

**Why AC's 60.2 differs.** AC used a leading constant of 71.21. The first-principles result implies a constant of **≈ 66.9**, which is the Liddle–Leach (2003) value. Using 71.21 adds **4.3 e-folds**. Switching reduced to non-reduced M_Pl does not account for it: that moves the result by 1.6 e-folds, and in the wrong direction. **I cannot identify a convention under which 71.21 applies to this relation. AC should check the source of that constant.** I am not asserting where it came from.

**Instant reheating is the ceiling, not the midpoint.** For any reheating epoch with w ≤ 1/3, N_* only goes down from the instant-reheating value. T1's band was 55.7 at T_rh = 10¹⁵ GeV down to 48.8 at 10⁶ GeV, for w = 0. So the band's **upper edge is about 56.** Anything above that requires w > 1/3 (a stiff or kination-type epoch), which the corpus does not have. Cursor's category-error verdict says the same.

**Why this is the item (a) risk that matters most.** The directive's constraint line currently reads "V1: ~55–60 depending on reheating". If "55–60" enters Companion 17, Part 3 or Manifest §3, it replaces one unreproducible number (63.4 as pivot) with another (60 as a band edge). That is the original error recurring in a new place.

**Recommended band wording:** "N_* ≲ 56 (instant reheating, the upper bound for w ≤ 1/3); ~49–56 across reheating temperatures 10⁶–10¹⁵ GeV with w = 0." The corresponding (n_s, r) ranges from (0.9652, 0.0067) at the ceiling to about (0.960, 0.009) at the low end. These values are from T1's run on Companion 17's model; Scratch should re-derive them independently.

## Locus 10 — verified

The Part 1 abstract (current version, read this session) **does** carry the pair: "(Companion 17; (n_s, r) = (0.9692, 0.0053) at N_e = 63.4)". So locus 10 is a real patch target.

Part 1 §2.4 also carries "N_e = −ln(β_NTE M_Pl)", already graded conditional and "not claimed here as a passed test". That wording is correct as it stands, and it names the N_HH quantity. **Adversarial check for Scratch's register:** the §2.4 sentence must keep calling that quantity what it is, and must not start calling it N_*.

## Re-smuggling watch-list (to test against Scratch's register once filed)

1. Any NEW text quoting a single N_* point without its reheating assumption.
2. Any NEW text quoting an upper edge above ~56.
3. Any "matches to numerical precision" language that survives in C9 §5. The 63.5 match is a coincidence between two different quantities. This is from AC's target list; I have not read C9.
4. The N_HH relabel in C8 §2 must carry a one-line gloss ("not the CMB pivot count"). Otherwise the next reader re-slots it.

## Two corrections on my own record

- **P4 (2026-09-24) was wrong.** My verdict said "undefined by deposit". Part 2 §8.5–8.6 and §IX settle both definitional items, as recorded in AC's handoff. **I did not read Part 2**, and the verdict did not say so. That verdict, and the boundary-condition recast verdict that relied on it ("P4 stands"), should both be read as superseded on that point. I have not re-read Part 2 this session and am not asserting its content beyond what AC's handoff quotes.
- **Duplicate Jammer filing.** `Working\C5_Flatness_VERDICT_Jammer_20260924.md` (created 3 minutes after my `C5FLAT_VERDICT_Jammer_fork2_…_20260924.md`) is the file Manifest §10 registers as the Jammer leg, but I did not author it. It reaches the same fork. However, its Q1 contains a physics error: it says two closed sectors "each with E < 0 can sum to zero … because CPN reverses the … sign convention on the kinetic term". Two negatives do not sum to zero, and curvature is CPN-even, so it cannot cancel between sectors. The conclusion stands; that sentence should not be quoted. **Greg: two agents appear to be running as "Jammer".** Worth confirming which lane owns the name.

— Jammer, 2026-09-25
