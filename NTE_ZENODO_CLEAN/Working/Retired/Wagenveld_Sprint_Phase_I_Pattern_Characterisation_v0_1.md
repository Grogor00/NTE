# Wagenveld Sprint — Phase I Pattern Characterisation (Cursor v0.1)

**From:** Cursor  
**To:** AC (Phase II ranking), Jammer (analytical formalisation), Greg  
**Date:** 2026-05-29  
**Authority:** Greg sprint activation 2026-05-29; foundation `Working/AC_Wagenveld_Sprint_Architectural_Scoping_v0_1_20260528.md`  
**Status:** Phase I deliverable — **data pattern only**; no candidate mechanism developed here.

---

## §0 — Scope and inputs

**Question.** Along AC §3’s four discrimination axes (z, scale, angle, survey-selection), what pattern does the current Branch I worksheet produce for CatWISE / Singal / Quaia / Wagenveld?

**Sources (this pass).**

| Source | Role |
|--------|------|
| `Working/lcdm_bao_void_bias.py` | Canonical numerical worksheet (defaults + sensitivity + v0.4 Wagenveld-focused grid) |
| `Working/Cursor_LCDM_Void_Bias_BranchI_v0_3_Pass_20260528.md` | Prior pass snapshot |
| `Working/Scratch_Adversarial_Review_Cursor_BranchI_v0_3_Pass_20260527.md` | Adversarial read (radio isolation, z-decline tension) |
| `Working/LCDM_Void_Bias_BAO_Worksheet_Branch_I_Directional_Jammer_v0_2_20260527.md` | Survey metadata / literature anchors |

**Explicit gaps (Phase I cannot close yet).**

- No ingested primary dipole tables or covariances  
- No direction-angle fits (`n̂_void` vs survey dipole vectors)  
- `z_eff`, `p`, `D_obs`, `σ` are worksheet placeholders — not re-derived from catalogues this pass  

---

## §1 — Survey inventory (worksheet row)

| Survey | Channel | Tracer / band | `z_eff` (worksheet) | `p` | `D_obs` | `D_kin` (baseline) | δσ @ defaults* |
|--------|---------|---------------|---------------------|-----|---------|-------------------|----------------|
| **CatWISE** | IR / WISE | WISE-selected AGN | 1.20 | 1.5 | 0.014 | 0.0046 | **−0.13** |
| **Wagenveld** | Radio | LoTSS-DR2 / NVSS lineage | 0.50 | 1.8 | 0.011 | 0.0050 | **+3.28** |
| **Singal** | Radio | Multi radio combination | 1.00 | 1.5 | 0.013 | 0.0050 | **+0.63** |
| **Quaia** | Optical | Gaia + unWISE QSO | 1.80 | 1.50 | 0.010 | 0.0050 | **+0.52** |

\*Defaults: `b = 0.055`, `α = 0.24`, `g(z) = (1+z)^{-2}` (`pow2`). δσ = `(D_pred − D_obs) / σ_obs`.

**Branch I prediction:** `D_pred = D_kin + p · b · ⟨g⟩_int(z_eff) · α`.

---

## §2 — Magnitude pattern (axis: survey-selection / channel)

### 2.1 Central fact

- **One outlier:** Wagenveld (+3.28σ at defaults).  
- **Three near-anchor:** CatWISE (−0.13σ), Singal (+0.63σ), Quaia (+0.52σ) — all within ~1σ.

### 2.2 Channel read (Scratch v0.3 flag, confirmed)

| Hypothesis | Phase I verdict |
|------------|-----------------|
| “Radio overshoots uniformly” | **Rejected** — Singal (radio) +0.63σ vs Wagenveld (radio) +3.28σ |
| “IR/photometric matches, radio fails” | **Too coarse** — CatWISE (IR) matches; Quaia (optical QSO) mild overshoot; Singal (radio) mild overshoot |
| “Wagenveld-specific” | **Supported** at worksheet level — isolation is survey/methodology, not band alone |

**Survey-selection axis:** Strong Wagenveld specificity; not reducible to radio-vs-photometric binary.

---

## §3 — z-dependence axis

### 3.1 Naive z_eff vs |δσ|

| Rank by `z_eff` | Survey | δσ (defaults) |
|-----------------|--------|---------------|
| Lowest z | Wagenveld (0.50) | **Largest overshoot** |
| Mid | Singal (1.00) | +0.63 |
| Mid-high | CatWISE (1.20) | −0.13 |
| Highest z | Quaia (1.80) | +0.52 |

**Pattern:** Residual magnitude is **not monotone in worksheet `z_eff`**. The largest overshoot sits at the **lowest** `z_eff`, while the highest-`z` survey (Quaia) is mild.

### 3.2 Implication for AC candidates (pattern-only)

| Candidate class | z-scaling expectation | Phase I fit |
|-----------------|----------------------|-------------|
| §2.1 Gauge-birth seed, §2.4 cross-thickness z-dep, §2.6 anisotropic Φ_NTE | High-z → larger excess | **Poor** if `z_eff` proxy is trusted |
| §2.3 Φ_NTE frame mismatch | Depth / frame mix | **Ambiguous** — needs Branch III numbers |
| §2.2 Leakage (scale) | Scale not z | **Not ruled out** — z and scale correlated |
| §2.5 Anisotropic κ | Mild z, strong angle | **Open** — angle data missing |
| §2.7 Survey geometry / δ₂ | Selection-specific | **Consistent** with Wagenveld isolation |

**Caveat.** Worksheet `z_eff` may mis-rank true mean redshift of contributing sources; Phase I.5 should ingest catalogue `z` distributions before AC commits to eliminating z-driven candidates.

---

## §4 — g(z) model axis (structural robustness)

Wagenveld δσ across `g(z)` (fixed `b`, `α`):

| Model | Wagenveld δσ | CatWISE δσ |
|-------|--------------|------------|
| `pow2` | +3.28 | −0.13 |
| `pow3` | +2.40 | −0.95 |
| `exp` | +4.23 | +0.71 |
| `struct_iv` | +6.82 | +8.35 |

**Pattern.**

- Wagenveld overshoot **persists** for all phenomenological `g(z)` forms; minimum **+2.40σ** (`pow3`).  
- Not removed by `g(z)` choice alone (Scratch adversarial point confirmed).  
- `struct_iv` breaks all surveys — treat as non-viable pending derivation, not sprint candidate.

---

## §5 — Parameter degeneracy axis (v0.4 grid, exploratory)

Script includes bounded grid: vary `α`, Wagenveld-only `(p, z_eff)`, and `g(z)`; minimize **max |δσ|** across four surveys.

| Scan | Best max \|δσ\| | Notes |
|------|------------------|-------|
| Wagenveld-focused (free `p_wag`, `z_wag` only for Wagenveld) | **0.57** | `α=0.16`, `p_wag=1.0`, `z_wag=0.40`, `exp` |
| Joint (`α`, `b`, `g(z)` shared; all surveys use table `z`, `p`) | **1.21** | `α=0.12`, `b=0.055`, `exp` — Wagenveld still +1.12σ |

**Pattern.**

- **Hypothesis (A)** from Scratch — joint `(b, α, g)` optimisation may absorb Wagenveld — **partially supported** only if Wagenveld is allowed **distinct effective `(p, z_eff)`** relative to other surveys.  
- Shared-parameter joint grid **does not** bring Wagenveld inside 1σ without worsening CatWISE.  
- Before invoking Branch II/III, sprint should run **honest joint fit** with explicit penalty for survey-specific nuisance parameters (AC honest-scope: don’t overfit one catalogue).

---

## §6 — Angular axis

**Status:** **No data in worksheet.** Direction vectors for `n̂_void`, CMB kinematic dipole, and per-survey measured dipole directions not ingested.

**Phase I.5 ask (Cursor):** Add dipole direction table + misalignment angle diagnostic (degrees) per survey.

**AC table pre-read (which candidates need angle first):** §2.1, §2.2, §2.3, §2.5, §2.6 — not §2.4 or §2.7.

---

## §7 — Scale axis (proxy only)

| Survey | Characteristic scale proxy | Comment |
|--------|---------------------------|---------|
| CatWISE | WISE flux-limited IR AGN | Large sky density, moderate depth |
| Wagenveld | LoTSS-DR2 radio | Different selection function, highest `p` in table (1.8) |
| Singal | Multi-radio composite | Similar band to Wagenveld, different combination |
| Quaia | QSO, `z` to ~3 | Deepest `z_eff` in table |

**Pattern.** Wagenveld and Singal share **radio** channel but differ in **combination / sky / systematics**; scale and `z_eff` are entangled. Disentangling requires **internal sub-samples** per catalogue (AC §2.2 recommendation) — out of scope for v0.1 characterisation.

---

## §8 — Mapping to AC §3 discrimination table (tentative)

Legend: ✓ = pattern consistent; ✗ = inconsistent at worksheet level; ? = insufficient data

| Candidate | z-dep | scale-dep | angular | survey-selection | Phase I tent. |
|-----------|-------|-----------|---------|------------------|---------------|
| §2.1 Gauge-birth seed | ✗ | ? | ? | ✓ (Wagenveld-specific) | Deprioritise until `z` bins fixed |
| §2.2 Leakage | ? | ? | ? | ✓ | Keep — scale/z entangled |
| §2.3 Φ_NTE frame | ? | ? | ? | ✓ (radio depth) | Keep — Jammer Branch III |
| §2.4 Cross-thickness z | ✗ | ? | ✓ (inherits BI dir) | ✓ | Deprioritise on z |
| §2.5 Anisotropic κ | ? | ? | **needs data** | ✓ (sky coverage) | **Priority for angle ingest** |
| §2.6 Anisotropic Φ_NTE | ✗ | ? | ? | ✓ | Deprioritise on z |
| §2.7 Non-pert. δ₂ | ✗ | ✗ | ✗ | **✓✓** | Fallback if III fails |

**AC action (Phase II):** Adversarially review this mapping; do not treat as Cursor-vetted elimination.

---

## §9 — Sprint Phase I.5 / II queue (Cursor)

1. Ingest structured survey table (provenance + citation keys) — separate JSON/CSV.  
2. Dipole **direction** table + misalignment utility.  
3. Joint fit with explicit DOF accounting (shared vs per-survey nuisance).  
4. Re-run when Branch I v0.5 lands — compare pattern stability.  
5. Hand to Jammer: formal z/scale decomposition using catalogue `n(z)` not single `z_eff`.

---

## §10 — One-paragraph honest-scope summary

At current Branch I defaults, the cosmic-dipole worksheet shows a **stable Wagenveld-only overshoot** (+2.4σ to +4.2σ across viable `g(z)` forms) while three other surveys sit near anchor. The residual is **not** explained by “all radio surveys high” (Singal is fine) and is **not** monotone in worksheet effective redshift (Wagenveld has the lowest `z_eff` but the largest error). Angular and true scale discrimination are **not yet measured**. Parameter scans show Wagenveld can be folded into a sub-1σ joint envelope only with **survey-specific** `(p, z_eff)` freedom — shared-parameter fits still leave Wagenveld at ~+1.1σ best case. Phase II should rank candidates accordingly, with **§2.5 (angular)** and **§2.2/§2.3 (scale/frame)** leading pending data ingest, and **§2.1/§2.4/§2.6** held until `z` proxy is validated.

---

*End Phase I v0.1 — Cursor 2026-05-29.*
