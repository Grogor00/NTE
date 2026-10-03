# C21 T1 VERDICT — the seed-as-boundary-data does NOT pin N_e. N_e is a horizon-matching quantity insensitive to the total budget; honest matching gives N_* ≈ 55–56, not 63.4.

**From:** Scratch · **To:** AC · **Cc:** Greg, Jammer, PC · **Date:** 2026-09-24
**Directive:** `Handoffs\Handoff_AC_to_Scratch_Jammer_C21_Seed_Boundary_Data_Research_Directive_20260924.md` — thread T1.
**Register:** speculation being tested; a negative is a result. Primary sources read: `Core_Papers\Companion_17_KPhi_Frame_Closure_v10_19_0.md`, `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` (§3 snapshot), `Handoffs\Handoff_PC_to_Greg_Companion21_ConformalReset_Outline_PROPOSED_20260922.md`.

---

## Pre-registered fork (stated BEFORE the result, per directive)

- **N_e lands near 63.4** → the existing (n_s, r) is reinforced and *derived*. Best case.
- **N_e lands elsewhere** → C21's budget falsifies the current (n_s, r), or is itself falsified. Report as such.
- **The budget does not close without new commitments** → the thread is no better than the others.

## Verdict

**Third fork: the budget does not close to pin N_e** — and for a structural reason, not a missing number: **N_e is insensitive to N_total.** Fixing the seed's total expansion budget cannot pin the observable e-fold count. Separately, when the horizon-matching is done honestly with NTE's own r-value, it yields **N_* ≈ 55.5 (±~2 from reheating)**, i.e. C17's *alternate* pairing (0.9646, 0.0070), not the corpus default N_e = 63.4 → (0.9692, 0.0053). The seed reading neither derives 63.4 nor rescues it; if anything it mildly disfavours it.

## 1. N_total is ≈ 140 (verified, not assumed)

ln(R_H,now / ℓ_P) = ln(1.37×10²⁶ m / 1.62×10⁻³⁵ m) = **140.3**. AC's naive estimate confirmed. (This is a horizon-ratio heuristic, not a scale-factor count; the distinction is the crux below.)

## 2. Why fixing N_total cannot pin N_e (the decisive point)

N_e ≡ N_* is the number of e-folds between pivot-scale horizon exit (k* = 0.05 Mpc⁻¹) and the end of inflation. It is fixed by the **horizon-matching condition** k* = a_* H_*, which depends on:
- the inflationary energy scale H_* — **locked observationally** by (A_s, r), not free;
- the post-inflation thermal history (T_reh, expansion eras).

Decompose the total budget: **N_total = N_pre + N_e + N_post**, where N_pre = inflationary e-folds *before* the pivot exited (unobservable), N_post = e-folds from end of inflation to now (fixed by the thermal history). Matching fixes N_e; the thermal history fixes N_post; **N_pre absorbs whatever N_total is.** Changing the total budget slides only the unobservable pre-pivot portion — it does not move N_e. Therefore a seed datum that fixes N_total supplies **no constraint on the observable N_e.** This is independent of any NTE-specific dynamics; it is the structure of the matching problem.

## 3. Honest matching value (with NTE's own inputs)

From A_t = r A_s: H_* = 1.8×10¹³ GeV (7.4×10⁻⁶ M_Pl); V_*^(1/4) = 8.7×10¹⁵ GeV. Entropy-conservation matching, instantaneous reheating (ρ_reh ≈ V_*, T_reh = 3.6×10¹⁵ GeV), pivot k* = 0.05 Mpc⁻¹:

    N_* = ln(H_*/H0) − ln(k*/a0H0) − ln(T_reh/T0) − ⅓ln(g_s ratio)
        = 126.87 − 5.40 − 64.90 − 1.10 = **55.5**.

Reheating uncertainty spans roughly N_* ∈ [53, 57] for standard (w ≤ 1/3) histories at this fixed V_*. Reaching 63.4 needs **+7.9 e-folds**, available only from a non-standard kination-dominated (w > 1/3) reheating epoch that NTE does not have. So the corpus default N_e = 63.4 is ~8 e-folds above honest matching and remains an unpinned, high input.

## 4. A genuine scale tension surfaced (bonus, adversarial)

NTE's gauge birth = hot Big Bang at **T_GB ~ 0.4 M_Pl ≈ 9.7×10¹⁷ GeV** (Part 2) is **~270×** the reheat energy the measured r permits (T_reh from V_* ≈ 3.6×10¹⁵ GeV). Gauge birth and the α=2 inflationary scale therefore **cannot be the same reheating event** — you cannot thermalise to a higher energy density than the inflaton carried. Either they are distinct epochs (the α=2 plateau sits below the gauge-birth scale, with the seed far above both), or the corpus is carrying two incompatible primordial scales. This is exactly the Euclidean-section caveat C17 flag #1 warns of: the Lorentzian slow-roll map is being read on a section whose physical expansion history is not the Lorentzian one, so N_e here is a **bookkeeping parameter of an imported formula**, not a physical Lorentzian e-fold count — which is *why* a Lorentzian total-budget argument gets no grip on it.

## 5. What this means for the corpus (inputs only; AC decides)

- C21's seed-as-boundary-data does **not** upgrade Companion 17's conditional (n_s, r) to a derived prediction. N_e stays an input; C21 §10/§12 should say so in one line.
- The honest matching value (~55.5) coincides with C17's alternate pairing (0.9646, 0.0070), which sits closer to Planck 2018 (0.9649 ± 0.0042, ~0σ) than the default 0.9692 (+1.0σ) — but this is *not* a derivation either; it is what standard matching gives at fixed (A_s, r). Report, do not promote.
- The T_GB / V_* scale tension (§4) is a separate, real item worth its own flag regardless of C21. Recommend routing to a dedicated check.

— Scratch, 2026-09-24. T1: budget does not close to pin N_e (N_e insensitive to N_total); honest matching ≈ 55.5, not 63.4; T_GB/V_* scale tension surfaced.
