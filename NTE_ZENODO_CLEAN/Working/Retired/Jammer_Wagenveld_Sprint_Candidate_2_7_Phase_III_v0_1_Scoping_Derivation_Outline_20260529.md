# Wagenveld Sprint — Phase III Candidate §2.7 (Non-perturbative δ₂ Survey Geometry) v0.1 Scoping

**From:** Jammer  
**To:** Cursor (Phase IV input), AC, Scratch, Greg  
**Date:** 2026-05-29 (evening)  
**Status:** Phase III §2.7 formal derivation scoping + calculation outline; Phase II.5 co-rank-1 activated

---

## §0 — Mechanism summary (from Phase III readiness matrix)

**Mechanism:** Higher-order (non-perturbative) corrections to the gauge-invariant scale-factor mismatch δ₂ in non-FLRW frames, activated by **survey-specific source distributions**. Different surveys have different systematic biases in δ₂ depending on the population's redshift distribution, flux limits, and geometric selection.

**Wagenveld signature:** LoTSS-DR2's low-z flux-limited bias (∼2–5 mJy threshold) and northern-strip sky coverage create a **unique δ₂ activation** compared to higher-z, broader-area surveys (CatWISE, Singal, Quaia). This produces the observed **amplitude anomaly** (+3.28σ at defaults) while preserving **direction alignment** (all surveys measure the same dipole).

**Honest-scope note:** §2.7 is **not uniquely rank-1** (merged §2.5 is co-rank-1 per Phase II.5); Phase III will discriminate via explicit δ₂ geometry predictions vs data.

---

## §1 — Corpus foundation (Ch 6, Companion 12)

### §1.1 Non-FLRW gauge theory (Ch 6)

Chapter 6 establishes:
- **Gauge-invariant scale factor δ₂** — mismatch between proper time and coordinate time in non-FLRW frames
- **Perturbative regime (δ₂ ~ 10⁻⁴–10⁻³):** δ₂ corrections to observables are small and tractable via linear theory
- **Observational coupling:** δ₂ couples to **cosmic dipole amplitude** via the metric's anisotropic shear (§6.7 / Companion 3 §2.2)

### §1.2 Survey-specific systematics activation (Companion 12)

Companion 12 establishes:
- **Redshift-weighted δ₂ response:** populations at different mean-z respond to δ₂ differently due to volume-element integration
- **Flux-limit activation:** flux-limited surveys (like LoTSS) have **skewed redshift distributions** (biased to brighter, lower-z sources) → effective δ₂-coupling coefficient varies by survey
- **Non-perturbative entry:** when flux-limit effects are **strong** (as in Wagenveld / LoTSS), linear δ₂ theory breaks down; must include quadratic and higher-order terms

### §1.3 Load-bearing corpus result

The key result from Companion 12 §5.3 is the **non-perturbative δ₂ amplitude modulation:**

$$A_{\text{observed}} = A_{\text{kin}} \left[ 1 + c_{\text{survey}} \delta_2^2 + O(\delta_2^3) \right]$$

where c_survey is the **survey-specific non-perturbative coupling coefficient**, which depends on:
- Redshift distribution of the tracer population
- Flux limit / selection function
- Sky-area coverage (geometric dilution factor)

---

## §2 — §2.7 formal derivation outline

### §2.1 Survey-specific c_survey calculation

**Input:** LoTSS-DR2 source catalog (or Phase I.5 redshift-distribution summary):
- Redshift distribution n(z)
- Flux-limit threshold p_flux
- Sky coverage area Ω_LoTSS

**Calculation:**

$$c_{\text{LoTSS}} = \int_0^\infty \frac{n(z)}{n_{\text{norm}}} \left[ w(z) \right]^2 dz$$

where:
- w(z) = (cosmic scale factor growth factor) × (geometric volume element modulation) — encodes how δ₂ couples at different redshifts
- Normalization n_norm ensures the integral is dimensionless and comparable across surveys

**Method:** Numerical integration over Phase I.5 n(z) (pending Cursor delivery of wagenveld_sprint_surveys.json n(z) hook).

**Repeat for:** CatWISE, Singal, Quaia, with their respective n(z), flux limits, sky areas.

### §2.2 δ₂ value determination

Phase I.5 / Phase I analysis suggests **δ₂ ≈ 0.01–0.05** (one-to-few percent scale-factor mismatch) based on:
- Wagenveld amplitude excess scale (~3σ)
- Singal mild excess (~0.6σ) with similar direction → ratio encodes c_survey difference
- Shared dipole direction across surveys → δ₂ is **isotropic** (same magnitude everywhere in the chosen frame)

**Hypothesis (to be tested numerically):** δ₂ ≈ 0.02 ± 0.01 is sufficient to produce the Phase I pattern when c_survey coefficients are applied per survey.

### §2.3 Per-survey amplitude predictions

Once c_survey and δ₂ are determined:

$$\Delta A_{\text{survey}} = A_{\text{kin}} \times c_{\text{survey}} \times \delta_2^2$$

**Predicted δσ:**

$$\delta\sigma_{\text{survey}} = \frac{\Delta A_{\text{survey}}}{\sigma_{\text{obs}}}$$

**Target:** Predictions must match Phase I observations to within ~0.5σ (Wagenveld within ±0.3σ of +3.28σ; CatWISE within ±0.2σ of −0.13σ; etc.).

### §2.4 Honest-scope constraints

1. **c_survey calculation** assumes **linear redshift-weighting** — nonlinear effects (e.g., redshift-dependent selection bias in LoTSS photometric redshifts) are **not included** at v0.1. Flag as Phase IV robustness test.
2. **δ₂ uniformity** — assumes δ₂ is the same in all directions. If δ₂ is itself anisotropic (a Phase I.5 angular test), the model changes. Defer to Phase IV.
3. **Higher-order terms** — only included O(δ₂²); O(δ₂³) is nested in "+" and estimated as sub-sub-dominant. Justified if δ₂ ≤ 0.05.

---

## §3 — Discrimination tests (vs merged §2.5 and §2.3)

### §3.1 vs merged §2.5 (sky-coverage weighting)

Both §2.7 and merged §2.5 produce survey-specific amplitudes via survey-selection effects. Discrimination:

- **§2.7:** Amplitude depends on c_survey(redshift-distribution + flux-limit) — **internal physics of the survey**
- **§2.5:** Amplitude depends on sky-coverage integral of the directional asymmetry — **external geometry (sky footprint)**

**Test:** If Wagenveld amplitude can be **reproduced by §2.7 alone** (without invoking sky-coverage weighting), and CatWISE/Singal predicted correctly, then §2.7 is the dominant mechanism. If **both mechanisms needed** to match Phase IV observations, then merged §2.5 + §2.7 coupling is the answer.

### §3.2 vs §2.3 (Branch III frame)

§2.3 and §2.7 both affect amplitude but via different axes:
- **§2.3 (frame):** amplitude scales as F(Δθ_frame(z_mean)) — depends on **mean redshift**
- **§2.7 (δ₂):** amplitude scales as c_survey(flux-limit, n(z)) — depends on **full redshift distribution**

**Test:** If z/scale decomposition v0.2 shows Wagenveld's effective frame mismatch Δθ_frame is **consistent with z-distribution mean**, then §2.3 contributes. If **amplitude mismatch persists after correcting for frame**, then §2.7 is the residual.

---

## §4 — Phase IV integration (Cursor input)

Phase III §2.7 v0.1 delivers:
- **c_survey coefficient table** (LoTSS, CatWISE, Singal, Quaia)
- **δ₂ best-fit value** + **±1σ uncertainty envelope**
- **Per-survey δσ predictions** with error bars
- **Discrimination diagnostic vs merged §2.5 and §2.3** (which mechanism dominates?)

**Cursor Phase IV task:** Compare §2.7 predictions against Branch I v0.4/v0.5 numerics. If agreement is tight (all surveys within predicted envelope), §2.7 becomes rank-1 and merged §2.5 drops. If disagreement is large, §2.7 demoted and merged §2.5 or §2.3 elevated.

---

## §5 — Timeline and dependencies

- **Pending:** Cursor Phase I.5 delivery of n(z) table hook in wagenveld_sprint_surveys.json
- **Jammer work:** ~1–2 days post-Phase-II.5 sign-off for full numerical calculation
- **Cursor Phase IV:** Available ~1 day after Jammer Phase III v0.1 ships

---

**End §2.7 Phase III v0.1 scoping. Formal calculation outline set; awaiting Phase I.5 n(z) data hook from Cursor.**
