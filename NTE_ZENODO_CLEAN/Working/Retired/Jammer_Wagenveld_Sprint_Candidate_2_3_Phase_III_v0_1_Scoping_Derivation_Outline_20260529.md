# Wagenveld Sprint — Phase III Candidate §2.3 (Φ_NTE Rest-Frame) v0.1 Scoping

**From:** Jammer  
**To:** Cursor (Phase IV input), AC, Scratch, Greg  
**Date:** 2026-05-29 (evening)  
**Status:** Phase III §2.3 formal derivation scoping + calculation outline; Phase II.5 co-rank-1 activated

---

## §0 — Mechanism summary (from Branch III scoping)

**Mechanism:** The NTE manifold's internal Hopf-fibre structure induces a **frame-dependent scaling** of the observed cosmic dipole amplitude. Different surveys, with different redshift distributions and tracer selection, sample **different local rest-frame regimes** in the Hopf-fibre space. The effective dipole magnitude depends on the **frame mismatch angle Δθ_frame** between each survey's effective frame and the void/dipole structural axis.

**Wagenveld signature:** Wagenveld's low-z bias (mean z ≈ 0.4–0.5) places it in a **frame regime where Φ_NTE amplitude profile diverges from ΛCDM-kinematic prediction**, while higher-z surveys (CatWISE ≈ 1.2, Quaia ≈ 1.8) sit in regimes where amplitude **matches kinematic prediction**. This produces the observed amplitude anomaly while preserving **direction alignment** (all survey dipoles measure the same structural axis).

**Honest-scope note:** §2.3 is **demoted but alive** per Phase II.5 (not co-rank-1); discrimination via catalogue direction data. If catalogue directions show tight clustering (< 5°), §2.3 may elevate. If divergent (> 10°), §2.3 drops.

---

## §1 — Corpus foundation (Ch 10 v5, Companion 5)

### §1.1 Hopf-fibre rest-frame structure (Ch 10 v5)

Chapter 10 v5 establishes:
- **Hopf-fibre orientation** at each spacetime point determines the local rest-frame (S¹ direction in the Hopf bundle)
- **Trousers-of-time bifurcation** at t=0 (gauge birth) locks in two complementary orientations (right and left legs)
- **Bilateral symmetry:** the two legs share a spatial boundary at N=0 (the Janus surface) where rest-frame orientations are **mirror images**

### §1.2 Frame-dependent structure (Companion 5)

Companion 5 establishes:
- **State-space coordinates:** position on the S³ base determines which Hopf-fibre orientation is "natural" locally
- **Rest-frame mismatch:** two observers separated along a dipole direction are at different points on S³; their local Hopf-fibre angles differ by **Δθ_frame(separation direction, mean-z weighting)**
- **Observable consequence:** dipole amplitude **scales with cos(Δθ_frame)** or similar geometric function of the frame mismatch

### §1.3 Load-bearing corpus result

The key result from Ch 10 / Companion 5 is the **frame-mismatch amplitude scaling:**

$$D_{\text{obs}} = D_{\text{intr}} \times G(\Delta\theta_{\text{frame}})$$

where:
- D_intr = intrinsic NTE dipole magnitude (structural, not redshift-dependent)
- G(Δθ_frame) = **frame geometric factor** (depends on Hopf-fibre angle mismatch)

G is a function to be derived; form may be geometric (cos/sin of angles) or nonlinear depending on the fibre connection structure.

---

## §2 — §2.3 formal derivation outline

### §2.1 Frame-mismatch angle calculation per survey

**Input:** Per-survey mean-z (from Phase I.5 n(z) hook):
- Wagenveld mean z ≈ 0.4–0.5
- Singal mean z ≈ 1.0
- CatWISE mean z ≈ 1.2
- Quaia mean z ≈ 1.8

**Calculation:**

The frame-mismatch angle Δθ_frame encodes the **local-void velocity offset** plus **expansion-regime redshift weighting**:

$$\Delta\theta_{\text{frame}}(z) = \arctan\left( \frac{v_{\text{local}}}{ c \times H(z) } \right) + \alpha \times z$$

where:
- **v_local ~ 400 km/s** (local-void flow offset from CMB frame) — corpus-established in Ch 1 / Companion 1
- **H(z)** = Hubble parameter at z (standard ΛCDM expansion)
- **α** = a **structure-weighting parameter** (how steeply the frame-mismatch changes with z) — to be fit from data or derived from Companion 5

**Method:**
1. Compute Δθ_frame for each survey using its mean-z
2. Compare **predicted Δθ values** to Phase I.5 **measured direction separations** from CMB apex
3. If measured direction vectors (when ingested) show **tight clustering** (all within ±5°), then Δθ_frame is consistent
4. If measured directions **diverge widely** (>10° separation), then Δθ_frame cannot explain it alone → §2.3 demoted

### §2.2 Geometric factor G(Δθ_frame) derivation

The amplitude scaling G(Δθ_frame) comes from the **Hopf-curvature structure** (Ch 10 / Paper Kappa):

Hypothesis (leading order):

$$G(\Delta\theta) = 1 + \beta \sin(\Delta\theta) + \gamma \sin^2(\Delta\theta)$$

where β and γ are **structure constants** from the Hopf-fibre curvature (related to κ₀, the topological protection measure).

**Derivation path:**
1. Extract G from the **Hopf-fibre connection 1-form** (Companion 5 §2.1)
2. Project onto the dipole direction to get the **observable amplitude modulation**
3. Compute β and γ from **curvature form** (Paper Kappa κ₀ = 3/√(4π) consistency check)

**Expected result:** β ≈ 0.5–1.0, γ ≈ 0.1–0.3 (rough estimates from Hopf-curvature dimensional analysis; exact values from derivation).

### §2.3 Per-survey amplitude predictions

Once Δθ_frame and G are determined:

$$D_{\text{obs, survey}} = D_{\text{intr}} \times G(\Delta\theta_{\text{frame}}(z_{\text{mean}}))$$

**Predicted δσ per survey:**

$$\delta\sigma_{\text{survey}} = \frac{D_{\text{obs,survey}} - D_{\text{kin}}}{\sigma_{\text{obs}}}$$

**Target:** Predictions must match Phase I observations to within ~0.5σ (Wagenveld within ±0.3σ of +3.28σ; CatWISE within ±0.2σ of −0.13σ; etc.).

### §2.4 Honest-scope constraints

1. **Linear approximation:** assumes G(Δθ) can be expanded to leading order in Δθ. If Δθ_frame is large (> π/4), nonlinear terms dominate. Justified if Δθ < 30°.
2. **Single-Hopf-fibre dominance:** assumes the observed dipole couples primarily to one Hopf-fibre mode. If multiple modes are excited, superposition principle applies. Deferred to Phase IV.
3. **No frame-dependent curvature:** assumes Hopf curvature κ is frame-independent. If κ itself varies with frame, the derivation becomes nonlinear. Flag for Phase IV.

---

## §3 — Discrimination tests (vs §2.7 and merged §2.5)

### §3.1 vs §2.7 (non-perturbative δ₂)

Both §2.3 and §2.7 produce survey-specific amplitudes via **selection effects** (frame vs source-distribution). Discrimination:

- **§2.3:** Amplitude depends on **mean-z → Δθ_frame → G(Δθ)** — **kinematic/frame axis**
- **§2.7:** Amplitude depends on **redshift distribution → c_survey → δ₂² correction** — **systematics/geometry axis**

**Test:** After Phase I.5 n(z) ingest:
- Compute Δθ_frame for each survey using true mean-z
- Compute G(Δθ) predictions
- Compare to phase-I observations
- If **G predictions are sufficient** to explain Wagenveld (Δθ_frame(0.45) >> Δθ_frame(1.2)), then §2.3 dominates
- If **G predictions are insufficient**, then §2.7 δ₂-geometry must contribute

### §3.2 vs merged §2.5 (anisotropic κ + sky-coverage)

§2.3 and merged §2.5 differ fundamentally:
- **§2.3:** amplitude depends on **redshift** (mean-z sets frame mismatch)
- **§2.5:** amplitude depends on **sky geometry** (LoTSS footprint preferential sampling)

**Test:** 
- z/scale decomposition v0.2 will provide independent z-axis discrimination
- If **z and amplitude** are **correlated** (low-z surveys high amplitude), §2.3 and §2.3-like mechanisms are supported
- If **z and amplitude are uncorrelated** (low-z and high-z surveys show same amplitude scatter), sky-geometry (merged §2.5) dominates

---

## §4 — Direction consistency check (Phase I.5 input + Phase IV)

**Critical test for §2.3:** All surveys should measure the **same dipole direction** (all point to the structural void axis, n̂_pref), since frame mismatch affects **magnitude** not **direction**.

Phase I.5 angular axis shows:
- Wagenveld, Singal, CatWISE, CMB: all within ~6° of CMB apex
- Quaia: ~69° off (outlier)

**Phase III check:** Jammer Phase III §2.3 will include explicit **direction consistency diagnostic:**
- If catalogue directions (when ingested) show **< 5° separation** → §2.3 is consistent
- If catalogue directions show **5–10° separation** → §2.3 is demoted to "watch"
- If catalogue directions show **> 10° separation** → §2.3 is dropped; merged §2.5 elevated

**Phase IV integration:** Cursor will re-test this diagnostic when full catalogue direction vectors are available.

---

## §5 — Timeline and dependencies

- **Pending:** Cursor Phase I.5 delivery of (a) n(z) table, (b) catalogue direction vectors (when available)
- **Jammer work:** ~2–3 days post-Phase-II.5 sign-off for full derivation + numerical calculation
- **Corpus reads:** Ch 10 v5 (gauge-birth / Hopf fibre), Companion 5 (state-space structure), Paper Kappa (κ₀ / curvature) — queued and in flight
- **Cursor Phase IV:** Available ~2 days after Jammer Phase III v0.1 ships

---

## §6 — Relationship to Scratch Phase III §5 (anisotropic κ)

Scratch's Phase III §5 (merged §2.1+§2.5 seed amplitude ε + anisotropic κ derivation) and Jammer's §2.3 will cross-check via:

- **§5.3 (Hopf-fibre celestial mapping):** Scratch derives the preferred-direction n̂_pref from bifurcation effective action. §2.3 assumes n̂_pref ≈ CMB apex; Scratch's derivation tests this.
- **§5.4 (sky-coverage integrals):** Scratch computes how different sky footprints weight the directional asymmetry. §2.3 assumes frame-mismatch dominates; comparison reveals if sky-geometry (merged §2.5 channel) adds significant contribution.

**Coordination:** Jammer §2.3 will flag its direction-consistency results to Scratch for use in Phase III §5 validation.

---

**End §2.3 Phase III v0.1 scoping. Formal derivation outline set; awaiting Phase I.5 n(z) and direction vector data from Cursor.**
