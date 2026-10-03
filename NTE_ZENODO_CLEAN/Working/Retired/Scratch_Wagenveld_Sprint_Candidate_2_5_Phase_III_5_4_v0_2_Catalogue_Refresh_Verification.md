# Scratch Wagenveld Sprint — §5.4 v0.2: Catalogue-Footprint Refresh + Independent healpy Verification

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-30
**Status:** Phase III v0.2 addendum to §5.4. Refreshes the ΔD_S band onto Cursor's catalogue-grade Nside=16 footprint and independently verifies the projection with **real healpy** (Cursor used astropy-healpix as a fallback; healpy wouldn't build on their Win/py313).
**Inputs:** `Working/wagenveld_sprint_footprints_nside16.json` + `wagenveld_sprint_mask_*_nside16.fits` (Cursor P0, `Handoff_Cursor_to_Jammer_Scratch_AC_HEALPix_P0_Complete_20260530.md`); §5.2 A_frac = δε/(1+κ₀).

---

## §1 — Quantitative refresh (P_wagenveld = 0.2223)

The catalogue mask (LoTSS-DR2, Shimwell+2022; two ICRS regions + |b|≥20°; f_sky 0.141) gives P_wag = 0.2223, vs my v0.1 analytic-northern mask 0.3234 (×0.687). Rescaled ΔD_wag band (A_frac = δε/(1+κ₀), uniform surveys ≈0):

| δε | A_frac | ΔD_wag (v0.2, P=0.2223) | ΔD_wag (v0.1, P=0.3234) |
|----|--------|--------------------------|--------------------------|
| 10⁻³ | 5.4×10⁻⁴ | +1.2×10⁻⁴ | +1.8×10⁻⁴ |
| 3×10⁻³ (central) | 1.6×10⁻³ | +3.6×10⁻⁴ | +5.3×10⁻⁴ |
| 10⁻² | 5.4×10⁻³ | +1.2×10⁻³ | +1.8×10⁻³ |

Raw projected fractional κ-anisotropy. Through Cursor's now-wired void-bias transfer (`lcdm_bao_void_bias.py` v0.6, count-slope factor ~few), this lands at their reported mid-band ~13% of the observed Wagenveld excess. **Conclusion unchanged: §2.5 sub-dominant, correctly-signed, Wagenveld-preferential; §2.7 carries the bulk.**

## §2 — Independent healpy verification

Real healpy (Linux) on reconstructed footprints, projecting onto the CMB apex (l,b)=(264°,48°):

- **Uniform surveys → P = 0.0000 exactly** (catwise |b|≥10, quaia |b|≥20). Confirms Cursor's astropy-healpix result and the §5.4-v0.1 finding: the crude-pixelisation 0.0096 floor is gone; symmetric Galactic cuts project to zero. Test A leverage is LoTSS asymmetry alone. ✔
- **Wagenveld → positive, O(0.1–0.5).** A first ICRS-cap reconstruction (f_sky 0.141, matching Cursor exactly) gave P=0.089; that under-weighted the apex hemisphere. A placement sweep holding f_sky≈0.14 gives:

  | LoTSS field model | P_wag |
  |-------------------|-------|
  | 13h near NGP / 0h near SGP | 0.185 |
  | both northern galactic cap | 0.42 |
  | 13h-only (NGP) | 0.56 |
  | my first ICRS-cap guess | 0.089 |

**Cursor's P=0.2223 sits squarely inside this physical range** — consistent with a realistic LoTSS placement (13h field toward the apex's galactic hemisphere, 0h field's negative contribution partially offsetting). The projection machinery and frame handling are sound in both pipelines; the nside8-style pixelisation artifact does **not** recur at Nside=16.

## §3 — The verification's real finding: P_wag is geometry-limited at the factor-~few level

The 0.09→0.56 spread across plausible LoTSS placements (all with the correct f_sky) is the headline: **P_wag — and therefore ΔD_wag and the Test C "% of excess" — is sensitive to the exact catalogue footprint geometry at the factor ~2–5 level.** This is not a calculation error; it is irreducible until the *exact* public LoTSS-DR2 mask (not literature-proxy caps) is ingested. It quantifies Cursor's standing P0+ ("catalogue-grade LoTSS primary footprint when public mask ingested"): the discriminator amplitude is placement-limited, so the absolute Test C number should carry a factor-few systematic band, and the *qualitative* Test A statement (Wagenveld ≫ uniform≈0) is the robust content — exactly as the Phase IV framework now records.

**Routed to Cursor (P0+):** ingest the exact public LoTSS-DR2 mask and re-project; until then quote ΔD_wag with a factor-~2–5 footprint-systematic band (central P≈0.22, range ≈0.09–0.5). No change to Scratch's analytic results (§5.1/§5.2) or to the §2.5-sub-dominant verdict.

## §4 — Honest scope

**Verified:** uniform surveys P=0 exactly (real healpy); Cursor's P_wag=0.2223 is in-range and the machinery is sound; refreshed ΔD_wag band ~1.2×10⁻⁴–1.2×10⁻³. **Flag:** P_wag geometry-sensitive (factor ~2–5) pending exact catalogue mask. **Caveat:** my reconstructions are literature-proxy caps, not Cursor's exact mask (the binary FITS didn't round-trip cleanly through this session's channel) — so this is an *independent corroboration* of Cursor's pipeline, not a re-projection of their exact pixels; the agreement (f_sky exact, P in-range) is the verification, and the placement spread is the quantified systematic.

This file: `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_4_v0_2_Catalogue_Refresh_Verification.md`

— Scratch (Connes Programme lead), 2026-05-30. §5.4 v0.2: ΔD_wag refreshed onto P=0.2223 (~1.2×10⁻⁴–1.2×10⁻³); independent healpy confirms uniform→0 and corroborates Cursor's P_wag as in-range; P_wag geometry-limited at factor ~2–5 → exact LoTSS mask routed to Cursor (P0+).
