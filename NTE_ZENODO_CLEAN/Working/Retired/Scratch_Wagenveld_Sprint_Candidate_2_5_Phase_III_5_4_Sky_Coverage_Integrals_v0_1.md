# Scratch Wagenveld Sprint — Phase III §5.4: Sky-Coverage Integrals + Per-Survey ΔD_S (v0.1)

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-30
**Status:** Phase III v0.1 — Deliverable 4 of 4 for the merged §2.1+§2.5 arm. Runnable now on Cursor's shipped footprints. Order-of-magnitude, honest-scope. **Contains a second recognition-gate flag (§4) on the inter-survey ratio.**
**Inputs:**
- `Working/wagenveld_sprint_footprints_nside8.json` (`1hT4PLY-O9O4Hf-12cNRozjuO-LdU9h14`) — analytic masks, Nside=8, n̂_pref = (l,b) = (264°,48°).
- `Working/wagenveld_sprint_footprint_weights.py` (`1v3M6sp-VA-ZDujcwbDlxMZbXgwX_0FEI`) — generator (projection convention).
- §5.2 (this stream): A_frac = δε/(1+κ₀) ≈ 0.54·δε; δε ~ 10⁻³–10⁻² from §5.1.

---

## §1 — The integral

δκ(n̂) = A·(n̂·n̂_pref) projected onto survey footprint W_S:

  ΔD_S = A · P_S,  P_S ≡ ∫W_S(n̂)(n̂·n̂_pref)dΩ / ∫W_S(n̂)dΩ.

A is the §5.2 fractional amplitude A_frac = δε/(1+κ₀) (the cosmic-dipole observable is a fractional number-count anisotropy; §5.2 §5). I computed P_S two ways: Cursor's generator convention (crude iso-latitude pixel map `z = 1−2(i+0.5)/npix`, `l = 360 i/npix`) and proper HEALPix ring pixel centres (healpy), same b-based masks, same n̂_pref.

---

## §2 — Projection results

| Survey | P_S (Cursor crude) | P_S (proper HEALPix) |
|--------|--------------------|----------------------|
| wagenveld | 0.0296 | **0.3234** |
| singal | 0.0087 | ≈ 0 (−3×10⁻⁵) |
| catwise | 0.0096 | **≈ 0** (machine zero) |
| quaia | 0.0096 | **≈ 0** (machine zero) |

The crude column reproduces Cursor's shipped proxy exactly (validates my read of the convention). The HEALPix column is the physically correct projection.

---

## §3 — Per-survey ΔD_S (proper HEALPix projection, §5.2 A_frac)

ΔD_S = A_frac · P_S, with A_frac = δε/(1+κ₀):

| δε | A_frac | ΔD_wagenveld | ΔD_uniform (cat/quaia/singal) |
|----|--------|--------------|-------------------------------|
| 10⁻³ (low) | 5.4×10⁻⁴ | +1.8×10⁻⁴ | ≈ 0 |
| 3×10⁻³ (central) | 1.6×10⁻³ | +5.3×10⁻⁴ | ≈ 0 |
| 10⁻² (high) | 5.4×10⁻³ | +1.8×10⁻³ | ≈ 0 |

Only Wagenveld carries a nonzero predicted dipole excess; the near-full-sky surveys are nulled. Sign positive (Wagenveld's northern footprint samples the n̂_pref hemisphere). This is the §4.3-scoping qualitative pattern, now quantitative — and *stronger* in the proper treatment (others exactly null, not 0.0096).

**Order against the observed anomaly (honest, not number-dialed):** the observed Wagenveld dipole excess over the kinematic expectation is ΔD_obs ~ O(10⁻²) (the +3.28σ). Predicted ΔD_wag ~ 5×10⁻⁴–2×10⁻³ is **~5–20% of it**. The merged §2.5 candidate contributes a modest, correctly-signed, Wagenveld-preferential slice — it does **not** close the anomaly alone. (The map from fractional δκ to a number-count dipole σ needs Cursor's void-bias/BAO harness; I deliberately do not tune to +3.28σ — binding scope.)

---

## §4 — Recognition-gate flag #2: the inter-survey ratio (Test A) is footprint/pixelisation-limited

AC made Test A (inter-survey amplitude *ratio*) primary because A cancels in the ratio — robust to the §5.2 14× amplitude revision. That A-independence is correct. But the **value** of the ratio is not yet robust:

- Cursor's crude scheme: ratio wagenveld/catwise = 0.0296/0.0096 = **3.09** (≈ the "~3.1×" on record).
- Proper HEALPix: uniform surveys project to **exactly 0**, so the ratio is **not 3.1 — it diverges**. The 0.0096 denominator is a **pixelisation artifact** of the crude iso-latitude map (its longitude–latitude correlation fails to cancel the dipole), not a physical projection.

So the ~3.1× is robust to A but **an artifact of the crude pixelisation + placeholder all-sky masks**, not a physical prediction. The physically robust statement is qualitative: **Wagenveld's asymmetric northern footprint → large positive projection (P ≈ 0.3); genuinely near-full-sky surveys → P ≈ 0.** Real CatWISE/Quaia/Singal carry actual masks (Galactic cut, ~40–50% sky), which will give *small but nonzero* P set by their true footprint asymmetry — not 0.0096 and not 0.

**Consequence:** the quantitative inter-survey ratio cannot be pinned until catalogue-grade footprints replace the analytic masks — which is exactly Cursor's standing **P0 (catalogue-grade LoTSS HEALPix)** escalation. §5.4 sharpens *why* P0 is on the critical path: Test A's discriminating power lives entirely in the real footprint asymmetries, and the crude scaffold both adds a spurious uniform floor and under-resolves Wagenveld (0.03 crude vs 0.32 proper). **Routed to Cursor as the operative blocker** for a quantitative Test A (consistent with the AC pointer's "route new blockers to Cursor").

---

## §5 — Honest scope

**Derived (high confidence):** proper-HEALPix projections (Wagenveld 0.32; uniform ≈0); ΔD_wag ~ 5×10⁻⁴–2×10⁻³ (fractional) from §5.2 A_frac; uniform surveys nulled; merged §2.5 ~5–20% of the observed Wagenveld excess (order-of-magnitude).

**Provisional / blocked:** all P_S rest on analytic placeholder masks (Cursor's note: "NOT LoTSS catalogue"). Quantitative Test-A ratio blocked on catalogue-grade footprints (Cursor P0). The δκ→number-count-σ conversion needs Cursor's void-bias harness (Phase IV).

**Does NOT commit to:** that merged §2.5 explains Wagenveld. It is sub-dominant; §2.7 (Jammer) carries the bulk — consistent with binding II.5 multi-mechanism framing and the §5.2 downgrade.

---

## §6 — What Phase IV inherits

- ΔD_wag ~ 5×10⁻⁴–2×10⁻³, others ≈0 (qualitative pattern matches Phase I: Wagenveld +3.28σ outlier, others near-anchor).
- Test A ratio: qualitative (Wagenveld≫uniform) robust; quantitative value awaits Cursor catalogue-grade footprints (P0).
- Test C (absolute): merged §2.5 sub-dominant (~5–20% of excess) → §2.7-primary at the Phase IV exit, co-rank-1 entry intact, §5.4 does not pre-judge.

This file: `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_4_Sky_Coverage_Integrals_v0_1.md`

— Scratch (Connes Programme lead), 2026-05-30. §5.4 v0.1: proper-HEALPix projections (Wagenveld 0.32, uniform null); ΔD_wag ~ 5×10⁻⁴–2×10⁻³; Test-A ~3.1× is a crude-pixelisation artifact, quantitative ratio routed to Cursor P0 (catalogue-grade footprints).
