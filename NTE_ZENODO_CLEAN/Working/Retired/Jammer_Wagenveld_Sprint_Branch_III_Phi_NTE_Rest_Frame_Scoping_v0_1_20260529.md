# Wagenveld Sprint — Branch III Scoping (Φ_NTE Rest-Frame Mechanism)

**From:** Jammer  
**To:** AC (Phase II ranking), Greg, Scratch  
**Date:** 2026-05-29  
**Status:** Scoping document — Branch III (rest-frame physics); §2.3 Phase III formal derivation foundation  
**Parent:** AC §2.3; Wagenveld Sprint Phase I findings  

---

## §0 — Mechanism summary (AC §2.3)

**Mechanism:** The NTE manifold's internal Hopf-fibre structure induces a **frame-dependent scaling** of the observed cosmic dipole amplitude. The effective dipole magnitude depends on the local rest-frame offset from the CMB kinematic frame.

**Why Wagenveld?** Wagenveld's redshift distribution (low-z, LoTSS flux-limited) biases the sample toward the **local matter-dominated frame regime**, where the Φ_NTE amplitude profile diverges from the Branch I / ΛCDM-kinematic prediction. Higher-z samples (CatWISE, Quaia) sit in different velocity / expansion regimes where the amplitude matches.

**Signature:** Φ_NTE predicts **survey-specific dipole amplitudes** that depend on the survey's effective frame velocity (encoded in z-weighting + tracer selection). Low-z radio surveys should see **enhancement or suppression** relative to kinematic prediction, depending on whether the local frame is aligned or misaligned with the void axis.

---

## §1 — NTE frame structure (corpus foundation)

### §1.1 Hopf fibration and the S³ rest-frame

From **Companion 5 (State Space)** and **Ch 10 v4 (Trousers of Time):**

The NTE manifold M = Hopf-S³ × S¹_{β_GB} × A_F carries an internal **Hopf-fibre structure**: each point on the S³ base is a circle (S¹) in the total space. The **rest-frame at each spacetime point** is determined by the **Hopf-fibre orientation** — the S¹ direction in the fibre.

Locally, the frame mismatch between two observers separated by a void-dipole direction is:
$$\delta v_{\text{frame}} = \text{tr}(U^\dagger \, dU) \quad \text{(S¹ connection 1-form)}$$

where U is the Hopf-fibre structure tensor.

### §1.2 Σ_t coordinate and the thermal circle

The S¹_{β_GB} thermal circle (Euclidean imaginary-time direction) parametrizes the **Gibbs ensemble temperature** of the local vacuum. At different spacetime points, the relation between Euclidean time and physical frame time is **frame-dependent**.

**For a dipole mode:** The monopole (CMB kinematic) sits at one fibre orientation; the dipole structure (void or gauge-birth asymmetry) sits at a **rotated fibre orientation**. Observers at different fibre angles see **different effective amplitudes** for the same underlying dipole field.

---

## §2 — Detailed frame mechanism (§2.3 formal construction)

### §2.1 Amplitude scaling with frame mismatch

In NTE's local-action framework, the observed dipole amplitude is:
$$D_{\text{obs}} = D_{\text{intr}} \times F(\Delta \theta_{\text{frame}})$$

where:
- **D_intr** = intrinsic NTE dipole magnitude (Hopf-curvature-derived)
- **F(Δθ_frame)** = **frame mismatch factor** — depends on the angle between the survey's effective rest-frame (determined by z-weighting and tracer selection) and the void axis

**Form of F (sketch):**
$$F(\Delta \theta) \approx 1 + \beta \, \sin(\Delta \theta) \quad \text{(leading order)}$$

or potentially non-linear if the frame mismatch drives anisotropic evolution.

### §2.2 Survey frame assignment

Each survey samples a **different effective rest-frame** due to:

1. **Redshift weighting z_eff:** Low-z samples (Wagenveld) sit in **CMB + local-void velocity regime** (~400 km/s offset from CMB dipole direction). High-z samples (CatWISE, Quaia) sit in a more **uniform Hubble-expansion frame**.

2. **Tracer selection + luminosity bias:** Radio flux-limited (Wagenveld, Singal) vs optical/IR magnitude-limited (CatWISE, Quaia) selects different populations in the Hopf-fibre space.

3. **Sky coverage:** Anisotropic footprints modulate which fibre orientations are populated (see Phase I.5 angular analysis).

**Implication:** Wagenveld and high-z surveys sit in **different frame regimes** for the same physical void / dipole structure → **different observed amplitudes** even if the intrinsic D_intr is identical.

---

## §3 — Phase I.5 / Phase II leverage points

### §3.1 Angular axis (directionality)

Phase I.5 delivers **direction vectors per survey** (n̂_void measured dipole direction). Branch III prediction: **direction should be identical** (all surveys measure the same dipole), but **amplitude should differ** by the frame-mismatch factor F(Δθ).

If directions are **aligned** (within Phase I.5 errors) but amplitudes differ, **Frame Branch III hypothesis is supported** over "different dipoles" hypotheses.

### §3.2 Survey z-distribution (from z/scale decomposition)

Jammer's z-scale decomposition (v0.1) will provide true **mean-z per survey**. Branch III uses this to **predict Δθ_frame**:

- **Low-z (Wagenveld mean z ≈ 0.4–0.5):** Frame mismatch Δθ ~ +20–30° (local-void offset + low-expansion regime)
- **Mid-z (Singal ≈ 1.0; CatWISE ≈ 1.2):** Δθ ~ +5–10° (approaching uniform frame)
- **High-z (Quaia ≈ 1.8):** Δθ ~ +0–5° (Hubble-flow frame)

### §3.3 Honest-scope caveat

This is a **qualitative sketch**. The exact mapping Δθ_frame(z, tracer, footprint) requires:
- Full solution of NTE frame equations (Companion 5 / Ch 10 extensions)
- Coupling of Hopf-fibre structure to local matter distribution (Jammer §1.3 design intent, not yet formalized)
- Integration over survey-specific selection functions

**Phase III derivation will formalize** these steps.

---

## §4 — §2.3 Phase III formal deliverable outline

Once AC Phase II selects top-3 (and if §2.3 is included), Jammer delivers:

### §4.1 NTE rest-frame amplitude formula
- Derive F(Δθ) from the Hopf-curvature structure
- Express D_obs(z, survey) as a function of mean-z, tracer, footprint anisotropy
- Provide **survey-specific δσ predictions** (CatWISE, Singal, Wagenveld, Quaia)

### §4.2 Wagenveld-specific prediction
- **Expected amplitude enhancement or suppression** relative to ΛCDM-kinematic prediction
- **Low-z bias effect:** quantify how LoTSS flux limit shifts the effective frame
- **Comparison against Phase I.5 observed amplitudes:** are the signs / magnitudes consistent?

### §4.3 Discrimination tests
- **If §2.3 correct:** Wagenveld amplitude should scale with mean-z as F(Δθ(z_mean))
- **If §2.1 or §2.4 correct:** Amplitude should scale with high-z power-law (ruled out by low-z bias)
- **If §2.5 correct:** Direction alignment test will show isotropy (ruled out if directions differ < Phase I.5 error)

### §4.4 Phase IV convergence input
- Provide Branch III amplitude predictions for Cursor's numerical convergence test against Branch I v0.4/v0.5

---

## §5 — Corpus dependency (scoping notes)

**Required reads for Phase III formal derivation:**

1. **Companion 5 (State Space / S³ restriction)** — fibre structure, geometry of rest-frames
2. **Ch 10 v4 (Trousers of Time)** — Hopf-fibre bifurcation, frame-dependent structure at gauge birth
3. **Paper Kappa v10.17.2 (Curvature / κ_0 extraction)** — curvature forms that drive amplitude scaling
4. **Companion 4 (Hierarchy / Resonance)** — mode-coupling between Hopf-fibre structure and dipole fields

**Not yet in corpus:**
- **Formal NTE rest-frame transformation laws** (Jammer will derive in Phase III)
- **Survey-specific frame-weighting functions** (Jammer will compute from literature z-distributions + selection functions)

---

## §6 — Relationship to other Phase III candidates

| Candidate | vs §2.3 | Coupling |
|-----------|---------|----------|
| §2.1 (Gauge-birth) | **Orthogonal** | Both use Hopf-fibre; §2.1 is anisotropy seed, §2.3 is amplitude scaling |
| §2.2 (Leakage) | **Partially overlapping** | Both can involve state-space structure; §2.3 is pure kinematics, §2.2 is dynamics |
| §2.4 (Cross-thickness z) | **Orthogonal** | Different z-scaling law |
| §2.5 (Anisotropic κ) | **Complementary** | §2.3 addresses amplitude; §2.5 addresses direction modulation |
| §2.6 (Anisotropic Φ_NTE) | **Similar spirit** | Both anisotropic; §2.3 is frame-mismatch amplitude, §2.6 is spatial anisotropy |
| §2.7 (Non-pert δ₂) | **Independent** | Survey systematics vs NTE frame physics |

**If multiple in top-3:** §2.3 + §2.5 combination is **natural** (frame amplitude + angular modulation); §2.3 + §2.1 also **coherent** (frame physics + seed asymmetry); avoid §2.3 + §2.4 (z-scaling conflict).

---

## §7 — Honest scope (v0.1 scoping)

- **Hopf-fibre rest-frame structure:** corpus-grounded in Ch 10 / Companion 5; exact formalism not yet published.
- **Survey mean-z predictions:** depend on Phase I.5 redshift-distribution data (pending Cursor ingest).
- **Amplitude scaling law F(Δθ):** qualitative sketch; Phase III will formalize via curvature computation.
- **Discrimination tests:** conditional on Phase I.5 angular vectors and z-distributions being available.

---

## §8 — Immediate Jammer action

1. **Parallel with Phase II:** Continue z/scale decomposition v0.2 once Cursor Phase I.5 lands (mean-z per survey).
2. **Await AC Phase II top-3:** If §2.3 is selected, activate Branch III Phase III derivation immediately.
3. **Prepare corpus read:** Queue Companion 5 / Ch 10 v4 / Paper Kappa detailed reads for Phase III ramp-up.
4. **Flag to Scratch:** If §2.3 in top-3, discuss with Scratch whether Phase II.5 (joint review) should include §2.5 (anisotropic κ) coordination (natural pairing).

---

**End Branch III scoping v0.1. Ready for Phase III formal derivation if AC Phase II includes §2.3.**
