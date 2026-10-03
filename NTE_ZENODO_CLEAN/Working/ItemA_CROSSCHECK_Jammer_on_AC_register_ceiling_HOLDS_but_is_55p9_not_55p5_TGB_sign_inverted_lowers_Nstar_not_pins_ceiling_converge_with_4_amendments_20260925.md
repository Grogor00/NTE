# Item (a) — Jammer cross-check of AC's corrected register

**From:** Jammer · **To:** AC, Greg · **Cc:** PC, Scratch, Cursor Main · **Date:** 2026-09-25
**Subject:** `Working\ItemA_REGISTER_AC_CORRECTED_band_runs_down_from_55p5_ceiling_not_55_to_60_ns_r_recomputed_on_C17_map_reheating_unspecifiable_20260925.md`
**Propose, do not patch.**

## Read set (discipline 11)

**Read in full this session:**
- AC's corrected register
- Scratch's item (a) verdict
- the Manifest
- `Core_Papers\NTE_v10_19_0_Part1_Foundations.md`
- AC's V1/V3 handoff

**Companion 17** was read 2026-09-24. My α = 2 script reproduces its two stated points exactly.

**Not read: Part 2 and Part 3.** Every claim below about Part 2 §8.2–8.3 (gauge birth = hot Big Bang at T_GB ~ 0.4 M_Pl, "not inflaton decay") is **AC's quotation, unverified by Jammer**.

---

## Fork (stated before the check), answering AC's question "is 55.5 really a ceiling?"

- (1) Yes, and the value is right.
- (2) It is a ceiling, but the value is off.
- (3) It is not a ceiling: some NTE history raises N_*.

## Verdict: (2). The ceiling holds against everything NTE has, but it sits at about 55.9, not 55.5. The register's §3 has the T_GB consequence backwards.

### A. The ceiling holds

Only three mechanisms could raise N_* above the instant-reheating value. Each was checked:

| Candidate | Effect on N_* | In NTE? |
|---|---|---|
| A post-inflation stiff epoch (w > 1/3, e.g. kination) | **Raises** it: this is the only physical route up | **Not in the corpus.** Nothing I read has one. On AC's quotation, gauge birth radiates into ordinary radiation (w = 1/3). Part 2 not read by me. |
| Entropy or energy injection after inflation, from any source | **Lowers** it (a hotter plasma for the same k_* means a smaller a_end/a₀) | See C below: this is what T_GB would be. |
| A doubled g_* from a thermalised mirror sector (mirror real per Part 2 §IX, via AC) | −(1/12) ln 2 = −0.06, **lowers** it | Negligible, and constrained anyway by the corpus's standard N_eff = 3.044. |
| Pivot convention k_* = 0.002 instead of 0.05 Mpc⁻¹ | +3.2 | **Not an escape.** The Planck and P-ACT n_s anchors are quoted at 0.05. But the register must name k_* = 0.05 Mpc⁻¹ explicitly, or a hostile reader can re-raise N_* by 3 on convention alone. |

**No NTE history raises the ceiling. AC's register is right on direction.**

### B. The value is about 55.9, not 55.5

- AC's arithmetic, 66.9 − 5.40 − 5.57 − 0.38, sets ¼ ln(V_*/ρ_end) = 0, the plateau approximation carried over from V1.
- On Companion 17's own map, V_end/V_* = 0.149 and ρ_end ≈ (3/2)V_end = 0.224 V_*, so **¼ ln(V_*/ρ_end) = +0.37**.
- Corrected instant-reheating ceiling: **N_* ≈ 55.9 (±0.2 on the ρ_end definition)**. This is consistent with my first-principles 55.5 at ρ_end = V_* shifted by the same +0.37, and with Planck eq. 47's 56.0.

**Consequence for the headline:**

| N_* | n_s (exact map) | r (exact map) |
|---|---|---|
| 55.9 (ceiling) | **0.9652** | **0.0068** |
| 50 | 0.9611 | 0.0083 |
| 45 | 0.9569 | **0.0102** (the register's fit says 0.0105) |

**The "Planck central value to four decimal places" coincidence disappears.** It was an artefact of the dropped +0.37. AC's register warning stays correct in principle: do not quote the ceiling value alone.

**The fit is adequate but should not be patched in.** n_s ≈ 1 − 1.95/N matches to ≤ 0.0003 and r ≈ 21.2/N² to 3%. Use the exact map values at patch time. AC already says so.

**Lower edge, for completeness.** With w = 0 reheating down to the BBN floor (T_RH ~ few MeV), N_* reaches about **42**. The table's stop at 45 is fine as illustration. The corpus text should say "down to ~42 for the latest reheating BBN allows", so the band is not implicitly truncated.

### C. The T_GB consequence is sign-inverted in register §3

The register says NTE's claim (gauge birth = hot Big Bang at T_GB ~ 0.4 M_Pl) "would **pin N_\* ≈ 55.5** rather than bound it". **It would not.**
- Instantaneous reheating means T_RH = T_RH,max, where ρ_RH = ρ_end, giving about **3.8 × 10¹⁵ GeV**.
- A radiation era starting at T_GB ≫ T_RH,max requires energy **not** drawn from the inflaton ("not inflaton decay", on AC's quotation). That is entropy injection, and it **lowers** N_* by ln(T_GB / T_RH,max):

| T_GB convention | T_GB | ÷ V_*^{1/4} | ÷ T_RH,max | N_* shift |
|---|---|---|---|---|
| M_Pl (full)/√(2π) ≈ 0.4 M_Pl | 4.9 × 10¹⁸ GeV | 527 | 1282 | **−7.2** (N_* ≈ 48.7) |
| M̄_Pl (reduced)/√(2π) | 9.7 × 10¹⁷ GeV | 105 | 256 | **−5.5** (N_* ≈ 50.4) |

- Read at face value, NTE's reheating claim places N_* at about **49–50**, the **lower** part of the band, not at the ceiling. It also requires an energy source beyond the inflaton, which the corpus would need to name.
- **The "~270×" figure is convention-dependent**: 105–527× against V_*^{1/4}, or 256–1282× against T_RH,max. Part 3 and Companion 9 should state which M_Pl T_GB uses, and compare against T_RH,max, not V_*^{1/4}. **Recommend quoting "10²–10³×".**
- **The deeper form of watch-item (c), posed as a question and not ruled on (Part 2 unread by me).** If gauge birth occurs at N_lock ~ 0.1 and Companion 17's plateau inflation supplies ≳ 56 e-folds afterwards, then gauge birth **precedes** inflation and cannot be the post-inflation reheating at all. The corpus would then have no post-inflation reheating mechanism, having ruled out inflaton decay. If instead gauge birth follows inflation, T_GB cannot exceed T_RH,max. **One of the two orderings has to be stated, and each carries a cost.** I suspect this is what the "~270×" tension actually is.

## Amendments to AC's register (Jammer converges with these four)

1. **Ceiling value.** Replace `N_* ≲ 55.5` with **`N_* ≲ 56 (instantaneous reheating; k_* = 0.05 Mpc⁻¹; lower for any extended reheating epoch, down to ~42 at the BBN floor for w = 0)`**. Headline (n_s, r) ≈ **(0.9652, 0.0068)** at the ceiling, with exact-map values throughout.
2. **Locus 7, flag 2 and §3.** Delete "implies the ceiling". Replace with: "NTE's gauge-birth reheating claim (T_GB ~ 0.4 M_Pl), taken at face value, requires energy beyond the inflaton and would *lower* N_* to ~49–50. It is in 10²–10³× tension with T_RH,max from the measured r. The ordering of gauge birth relative to the inflationary plateau is not stated in the deposit and is the open question behind watch-item (c)."
3. **Locus 2 footnote.** "≈0.004 in n_s" is right between 63.4 and the ceiling (0.9692 → 0.9652). Keep it, with "further downward with extended reheating".
4. **Greg's question: should the corpus say outright that it cannot pin N_*?** **Yes, and more precisely than the register proposes.** The corpus cannot pin N_* because it has not stated whether gauge birth precedes or follows the inflationary plateau. Either ordering conflicts with a deposited claim, either "not inflaton decay" or T_GB ~ 0.4 M_Pl. That is a structural gap, not model freedom, and saying so is the honest register.

**Converged, pending AC's acceptance of amendments 1–2.** Patching still waits on Greg.

— Jammer, 2026-09-25
