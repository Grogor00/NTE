# Wagenveld Sprint — z/scale Decomposition (Jammer v0.1)

**From:** Jammer  
**To:** AC (Phase II ranking), Cursor (Phase I.5 data ingest coordination), Scratch, Greg  
**Date:** 2026-05-29  
**Status:** Working document — z_eff non-monotonicity investigation; phase II input  
**Parent:** `Working/Wagenveld_Sprint_Phase_I_Pattern_Characterisation_v0_1.md` (Cursor)

---

## §0 — Problem statement

Phase I reveals a **z-redshift non-monotonicity:** Wagenveld, with the **lowest worksheet z_eff = 0.50**, shows the **largest overshoot δσ = +3.28σ**. By contrast, Quaia (highest z_eff = 1.80) shows mild overshoot (+0.52σ). This pattern:

1. **Contradicts naive high-z candidates** (§2.1 gauge-birth seed, §2.4 cross-thickness z-dep, §2.6 anisotropic Φ_NTE), which predict larger anomaly at higher z.
2. **Suggests scale/depth rather than z-scaling** — or worksheet z_eff is not representative of the true mean redshift of contributing sources.
3. **Has major Phase II consequence:** If pattern persists under true catalogue n(z), deprioritize z-driven candidates; elevate scale/frame/survey-selection mechanisms (§2.2, §2.3, §2.5, §2.7).

**This document formalizes the decomposition to test the z_eff proxy.**

---

## §1 — Survey redshift distributions (from literature)

| Survey | Reference | Tracer / method | True z range | Approx. median z | Approx. mean z | Notes |
|--------|-----------|-----------------|--------------|------------------|-----------------|-------|
| **CatWISE** | Marocco+ 2021; WISE-selected AGN | WISE W1 mag-limited AGN | 0.2–3.0 | ~1.0 | ~1.2 (worksheet z_eff) | Fairly broad tail to high-z; worksheet z_eff ~representative |
| **Wagenveld** | Wagenveld+ 2024; LoTSS-DR2 + NVSS heritage | Radio flux-limited (∼2–5 mJy LoTSS; ∼20 mJy NVSS) | 0.01–1.5 | ~0.3 | **0.4–0.5** (worksheet 0.50 plausible) | **LoTSS bias to low-z**; NVSS even lower; combined sample may cluster at z < 0.5 |
| **Singal** | Singal 2011+; multi-radio composite | Radio flux-limited (mixed) | 0.01–2.0 | ~0.8 | **~1.0** (worksheet 1.00 matches) | More uniform; includes NVSS but also deeper samples |
| **Quaia** | Gaia DR3 + unWISE (Lie+ 2024) | Gaia + WISE QSO selection | 0.4–5.5 | ~1.5 | **~1.8** (worksheet 1.80 matches) | Deep optical QSO sample; steep tail past z~3 |

**Honest-scope caveat:** z distributions are from papers' summary statistics or histogram reads, not re-derived. LoTSS z-distribution is the least-well-characterized (Wagenveld paper cites "z from radio/optical cross-matching, not photometric"; bias to measurable-redshift sources typical).

---

## §2 — z_eff vs true n(z): what Phase I might have missed

### §2.1 Wagenveld z-distribution bias

Phase I uses worksheet z_eff = 0.50 as a scalar proxy. But **LoTSS-DR2 is flux-limited at ~2 mJy**, which is **biased toward low-z**, high-luminosity radio sources. A source at z=0.3, L=10^{26} W/Hz is much brighter than the same source at z=0.8.

**Implication:** True *mean* z of Wagenveld's redshift-measured subsample may be **lower** than z_eff = 0.50 (which includes many z < 0.3 sources with no redshift). This would **worsen the z-monotonicity puzzle** — the anomaly would be **even lower z** than Phase I assumed.

### §2.2 Singal blend

Singal's composite (NVSS + deeper radio samples) is **more uniform in luminosity-distance**, so z_eff = 1.00 is **more robust** than Wagenveld's.

### §2.3 CatWISE and Quaia

Both have **well-measured redshifts** (AGN/QSO optical spectroscopy or photometric anchors). Their worksheet z_eff values are likely **close to true means**.

**Table summary:**

| Survey | Worksheet z_eff | Approx. true mean z (literature) | Implication |
|--------|-----------------|----------------------------------|-------------|
| Wagenveld | 0.50 | **0.4–0.5** (LoTSS bias to low-z) | May be **even lower**; non-monotonicity **worsens** |
| Singal | 1.00 | ~1.0 | **Consistent** |
| CatWISE | 1.20 | ~1.2 | **Consistent** |
| Quaia | 1.80 | ~1.8 | **Consistent** |

---

## §3 — Scale / BAO-redshift axis (independent of z-monotonicity)

The worksheet also tracks **scale** via the BAO clustering redshift. Phase I notes z and scale are **entangled** (different surveys have different effective depths / sky volumes).

| Survey | BAO scale proxy | Entanglement with z_eff |
|--------|-----------------|------------------------|
| Wagenveld | LoTSS large sky area (41K sq deg), flux-limited | **High:** Low flux limit → biased to low z AND small physical scale |
| Singal | Composite, mixed area coverage | Medium |
| CatWISE | Smaller sky area (lower surface density), higher flux limit | **Medium-high:** Better depth, but poorer area |
| Quaia | Deep optical, limited sky area (inherit Gaia+unWISE footprint) | **Medium:** Depth vs area trade-off |

**Key question for Phase III (if §2.2 leakage or §2.3 frame selected):** Is the Wagenveld anomaly **scale-dominated** (BAO/void clustering depth) rather than z-dominated? This requires **internal sub-sample test** — compare low-z vs high-z Wagenveld subsample dipoles separately.

**Phase II input:** If scale is dominant, Jammer Phase III should prioritize **§2.2 state-space leakage** (Scratch's candidate) or **§2.3 Φ_NTE frame/depth** (Jammer's candidate), not pure z-drivers.

---

## §4 — Formal decomposition plan (Phase I.5 + Cursor partnership)

### Step 1: Catalogue n(z) ingest (Cursor Phase I.5)
- Extract per-survey redshift distribution from primary papers / survey releases
- Provide Jammer: per-survey **histogram n(z)** or **mean ± σ** for low-z, mid-z, high-z bins
- Supply: **survey effective volume V_eff(z)** if available (BAO-relevant)

### Step 2: Re-weight Branch I predictions (Jammer)
- Replace scalar z_eff with **integral over n(z)**:
  $$\langle g \rangle_{\text{true}} = \frac{1}{N} \int g(z) \, n(z) \, dz$$
- Recompute **D_pred per survey** using true ⟨g⟩
- Examine whether **δσ pattern inverts** (i.e., does Wagenveld remain outlier under true n(z)?

### Step 3: Internal sub-sample discrimination (Jammer → Phase III if needed)
- If Wagenveld z-distribution is **genuinely biased to low-z** (LoTSS flux limit), flag for Phase III:
  - Does low-z Wagenveld subsample spike more than high-z subsample?
  - If yes → **scale/BAO-depth signal** (supports §2.2 or §2.3)
  - If no → **survey-methodology signal** (supports §2.7)

### Step 4: AC Phase II implication flag
- Deliver to AC: "Which z-driven candidates (§2.1, §2.4, §2.6) survive or are ruled out under true n(z)?"

---

## §5 — Preliminary honest-scope decomposition (v0.1)

**Given Phase I.5 data not yet fully ingested**, I present a **qualitative skeleton** based on literature n(z) estimates:

### Wagenveld under low-z bias correction

If true mean z ≈ **0.4** (vs worksheet 0.50), and g(z) ∝ (1+z)^{-2}:
- ⟨g⟩_low-z=0.4 ≈ 0.58
- ⟨g⟩_worksheet(0.50) ≈ 0.53

The **difference is small** (~10%), so **z_eff non-monotonicity likely persists**. The anomaly is **not explained by z_eff mis-estimation alone**.

**Implication:** The anomaly **points to non-z axes** — scale, survey-selection, frame/depth, or anisotropy.

### Scale entanglement flag

Wagenveld's large sky area (41K sq deg) and low-z bias together imply **deep clustering depth in comoving distance**:
- Low z + large area = **high V_eff at small comoving scale**
- This could **amplify void-clustering dipole** if the void axis is aligned with Wagenveld's sky coverage (Phase III test: §2.2 leakage + sky geometry).

---

## §6 — What Jammer needs from Cursor Phase I.5

1. **Per-survey n(z):** histogram or binned table for Wagenveld, Singal, CatWISE, Quaia
2. **V_eff(z) estimates** if available (BAO-relevant for Phase III scale tests)
3. **Sky area / footprint masks** per survey (needed for Phase III §2.2 / §2.3 depth entanglement)
4. **Direction vectors** + misalignment angle per survey (needed for Phase III §2.5 anisotropic κ)

---

## §7 — Phase II implications (for AC ranking)

| Candidate | Phase I z-test | v0.1 z-decomposition | Recommended tier |
|-----------|---|---|---|
| §2.1 Gauge-birth seed | ✗ (poor if z_eff trusted) | **✗ (persists under true n(z) estimate)** | Deprioritize unless Phase III rules out scale/survey |
| §2.2 Leakage | ? (not ruled out by z) | **? (scale entanglement flagged)** | **Keep — prioritize if Phase I.5 V_eff shows high void-clustering scale** |
| §2.3 Φ_NTE frame | ? (needs Branch III) | **Keep (not ruled out by z)** | **Keep — Jammer formalisation in progress** |
| §2.4 Cross-thickness z | ✗ (poor if z_eff trusted) | **✗ (persists under true n(z) estimate)** | Deprioritize on z |
| §2.5 Anisotropic κ | ? (angle data missing) | **? (z-independent; wait for angular data)** | **Keep — highest-leverage Phase I.5 ingest** |
| §2.6 Anisotropic Φ_NTE | ✗ | **✗ (persists)** | Deprioritize on z |
| §2.7 Non-pert δ₂ | ✗ (but survey-selection consistent) | **✓ (survey-specific + selection-driven)** | **Fallback; elevate if top-3 < 3** |

---

## §8 — Honest scope (v0.1)

- **LoTSS z-distribution:** Estimated from literature (Wagenveld 2024 + LoTSS papers); **not re-derived from catalogues** (out of scope).
- **Re-weighting via true n(z):** Will be **numerical exercise** once Cursor Phase I.5 lands; v0.1 is qualitative skeleton.
- **Internal sub-sample tests:** Deferred to Phase III if §2.2 or §2.3 in top-3 (requires catalogue-level access).
- **Scale/BAO entanglement:** Flagged as a **concern for Phase III**, not resolved in Phase I.5.

---

## §9 — Jammer next step

**Await Cursor Phase I.5 delivery** (per-survey n(z), V_eff, footprint, direction vectors).  
**Then deliver:** Formal recomputation of Branch I δσ under true n(z); output: revised Phase II ranking guidance for AC.

**Parallel:** Continue **Branch III (Φ_NTE rest-frame)** scoping for §2.3 formal derivation (independent of z/scale outcome).

---

**End z/scale decomposition v0.1. Awaiting Phase I.5 data ingest → formal v0.2 calculation.**
