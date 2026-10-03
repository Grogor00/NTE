# Wagenveld Sprint — Phase III Candidate §2.7 (Non-perturbative δ₂) v0.1 — Calculation Framework & Numerical Setup

**From:** Jammer  
**To:** Cursor (data delivery trigger), AC, Scratch, Greg  
**Date:** 2026-05-30  
**Status:** §2.7 Phase III v0.1 framework complete; ready for numerical execution upon n(z) data arrival

---

## §0 — Mechanism summary (from scoping doc)

Higher-order (non-perturbative) corrections to gauge-invariant scale-factor mismatch δ₂ in non-FLRW frames, activated by survey-specific source distributions. Different surveys have different systematic biases in δ₂ depending on redshift distribution and flux limits.

**Wagenveld signature:** LoTSS-DR2's low-z flux-limited bias creates a **unique δ₂ activation** (highest amplitude) compared to higher-z, broader-area surveys.

---

## §1 — Framework (from corpus)

### §1.1 Non-perturbative δ₂ amplitude modulation (Companion 12 §5.3)

$$A_{\text{observed}} = A_{\text{kin}} \left[ 1 + c_{\text{survey}} \delta_2^2 + O(\delta_2^3) \right]$$

where:
- A_kin = kinematic dipole amplitude (ΛCDM baseline) ≈ 3.6 mK
- c_survey = survey-specific non-perturbative coupling coefficient (dimensionless)
- δ₂ = gauge-invariant scale-factor mismatch (~0.01–0.05, to be fit)

### §1.2 Survey-specific coupling coefficient

$$c_{\text{survey}} = \int_0^\infty \frac{n(z)}{n_{\text{norm}}} \left[ w(z) \right]^2 dz$$

where:
- n(z) = redshift distribution (from Phase I.5 data)
- w(z) = volume-element modulation × growth-factor weighting (CH 6 / Companion 12 geometry)
- n_norm = normalization (ensures dimensionless output)

---

## §2 — Numerical calculation procedure

### §2.1 Data inputs (awaiting Cursor n(z) hook)

**Required from `wagenveld_sprint_surveys.json` v0.4+ or Phase I.5 addendum:**

1. **Redshift distributions** (per survey):
   - Wagenveld: n(z) or mean-z ≈ 0.42 ± 0.05 minimum
   - Singal: n(z) or mean-z ≈ 1.00 ± 0.1 minimum
   - CatWISE: n(z) or mean-z ≈ 1.20 ± 0.1 minimum
   - Quaia: n(z) or mean-z ≈ 1.80 ± 0.2 minimum

2. **Flux limits / selection functions** (already in working files):
   - Wagenveld: ~2–5 mJy LoTSS threshold
   - Others: magnitude/AGN-selection limits

3. **Sky coverage** (from Cursor HEALPix delivery):
   - f_sky per survey (already available from nside16 JSON)

### §2.2 Step 1: Compute c_survey coefficients

**Pseudocode:**

```
for survey in [wagenveld, singal, catwisewise, quaia]:
  z_mean = mean_redshift[survey]
  n_z = redshift_distribution[survey] or approximation_from_mean_z(z_mean)
  
  # Volume-element weighting (from Companion 12 §5.3)
  w_z = (1 + z_power_law_exponent) * growth_factor(z) * geometric_modulation(z)
  
  # Integral: ∫ (n(z) / N_norm) * w(z)² dz
  c_survey = numerical_integrate(n_z * (w_z**2), z_from=0, z_to=6) / N_norm
  
  print(f"c_survey[{survey}] = {c_survey:.4f}")
```

**Honest-scope simplification for v0.1:** 
- Use **linear redshift-weighting** (w(z) ∝ (1+z)) — nonlinear effects deferred to Phase IV
- Normalize by ∫ w(z)² dz over full redshift range
- Treat each survey independently; no covariance at v0.1

### §2.3 Step 2: Fit δ₂ value

**Input:** Phase I observations (δσ per survey)

**Target:** Find δ₂ such that predictions match Phase I within ~0.5σ:

$$\chi^2(\delta_2) = \sum_{\text{survey}} \left( \frac{\delta\sigma_{\text{pred}}(\delta_2) - \delta\sigma_{\text{obs}}}{\sigma_{\text{obs}}} \right)^2$$

**Method:** Least-squares fit or grid search over δ₂ ∈ [0.01, 0.05]

**Expected result:** δ₂ ≈ 0.02–0.03 (from scoping; refined by fit)

### §2.4 Step 3: Per-survey amplitude predictions

**Once δ₂ is fit:**

$$\Delta A_{\text{survey}} = A_{\text{kin}} \times c_{\text{survey}} \times \delta_2^2$$

$$\delta\sigma_{\text{survey}} = \frac{\Delta A_{\text{survey}}}{\sigma_{\text{obs}}}$$

**Output table:**

| Survey | c_survey | δσ_pred | δσ_obs (Phase I) | Agreement |
|--------|----------|---------|---|---|
| Wagenveld | ? | +3.2σ? | +3.28σ | — |
| Singal | ? | +0.6σ? | +0.63σ | — |
| CatWISE | ? | −0.1σ? | −0.13σ | — |
| Quaia | ? | +0.5σ? | +0.52σ | — |

**Target:** All predictions within ±0.3σ of observations.

---

## §3 — Discrimination tests (Phase IV input)

### §3.1 Test A: Inter-survey amplitude ratios

**§2.7 prediction:**

$$\frac{\delta\sigma_{\text{Wagenveld}}}{\delta\sigma_{\text{full-sky}}} \approx \frac{c_{\text{LoTSS}} \times \delta_2^2}{c_{\text{uniform}} \times \delta_2^2} = \frac{c_{\text{LoTSS}}}{c_{\text{uniform}}}$$

(δ₂ cancels; depends on c_survey only)

**Robustness:** A-independent; this ratio discriminates §2.7 from merged §2.5 (which includes sky-coverage weighting).

### §3.2 Test C: Absolute amplitude

**§2.7 prediction:** δ₂ ≈ 0.02–0.03 → A ≈ (c_survey × δ₂²) → must match all four surveys simultaneously.

**Robustness:** Tightest constraint; tests whether single δ₂ value explains all surveys or if multiple mechanisms are needed.

### §3.3 Discrimination vs merged §2.5 (§5.4 refresh)

Both §2.7 and merged §2.5 (post-14× revision) contribute sub-dominantly. Test A will show which routing (δ₂-systematics vs sky-coverage) is dominant via the amplitude-ratio pattern.

---

## §4 — Calculation timeline

**Phase 0 (ready now):**
- Framework set ✅
- Corpus references identified ✅
- Pseudocode drafted ✅
- Phase I observation targets extracted ✅

**Phase 1 (pending Cursor n(z) delivery):**
- Load n(z) data → compute c_survey coefficients
- Fit δ₂ to Phase I observations
- Generate per-survey predictions
- Compute discrimination tests (A, C)

**Estimated duration post-data:** ~1–2 days for numerical calculation + cross-check

---

## §5 — Data delivery trigger

**Blocking item:** n(z) table finalization from Cursor

**Trigger condition:** When Cursor delivers `wagenveld_sprint_surveys.json` v0.4+ with mean-z values per survey (minimum: Wagenveld ~0.42, Singal ~1.0, CatWISE ~1.2, Quaia ~1.8), Jammer §2.7 numerical work launches immediately.

**Full z-histogram ingest (optional):** Refines w(z) integral; Phase IV can request upgrade if v0.1 results warrant.

---

## §6 — Honest scope (v0.1)

- **Linear redshift-weighting:** w(z) ∝ (1+z) only; nonlinear effects deferred to Phase IV
- **No covariance structure:** treats each survey independently; correlated systematics deferred
- **δ₂ uniformity assumption:** assumes δ₂ is the same in all directions; anisotropic δ₂ is a Phase IV test
- **Higher-order terms:** O(δ₂³) nested in "+"; justified if δ₂ ≤ 0.05

---

## §7 — Ready state

✅ Framework complete  
✅ Corpus references verified  
✅ Calculation procedure outlined  
✅ Phase I targets extracted  
⏳ **Awaiting n(z) data** for execution launch

---

**End §2.7 Phase III v0.1 framework. Standing by for Cursor n(z) delivery to trigger numerical work.**
