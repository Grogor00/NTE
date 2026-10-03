# Master v10.11 → v10.12 Patch Instructions

## Tier 2 — §17.5.9 ΛCDM reduction expansion

**Date:** 2026-05-23.  
**Author lane:** Cursor → AC ratification.  
**Scope:** Replace one-paragraph §17.5.9 with structured reduction + benchmark map. No new numerical fits claimed.  
**Scaffold:** `Working/LCDM_Reduction_Appendix_Scaffold_v0_1_20260523.md`

**Render:** `NTE_v10_11_Part*.md` → `NTE_v10_12_Part*.md`

---

## Patch T2-1: §17.5.9 body replacement (Part 3)

**Find:**

```
17.5.9 Reduction to ΛCDM in Tested Regimes (Standard Cosmology Benchmarks)

NTE's empirical case in tested cosmological regimes rests on its reduction to standard FRW cosmology when t emerges and the Friedmann equation H² = 8πGρ/3 holds. This reduction is asserted in §2.3.1 but the explicit verification that NTE reproduces ΛCDM-quality fits to BAO, CMB acoustic peak structure, σ_8, large-scale structure power spectrum, and redshift-space distortions has not been performed in the corpus. The framework's interaction with these benchmarks is implicit through the post-temporal recovery of standard physics; making the recovery explicit closes a class of cosmology-reviewer objections. Research target: benchmark NTE's predictions against the standard cosmological observables, demonstrating either reduction to ΛCDM in the relevant regimes or NTE-specific deviations that distinguish it.
```

**Replace with:**

```
17.5.9 Reduction to ΛCDM in Tested Regimes (Standard Cosmology Benchmarks)

NTE's empirical case in tested cosmological regimes rests on reduction to standard FRW cosmology when t emerges and the Friedmann equation H² = 8πGρ/3 holds (§2.3.1). **v10.12 expansion (Tier 2):** this section makes the reduction chain explicit, separates homogeneous ΛCDM recovery from NTE-specific inhomogeneity predictions, and maps standard benchmarks — without claiming completed global χ² fits the corpus has not performed.

**Reduction chain (structural).** (1) Core constraint H = β_NTE|Φ_NTE|² (Part 1 §2.3). (2) Cosmic trajectory |Φ_NTE|²(N) = v_EW² · H(N)/H₀ (§2.3.1). (3) Friedmann identification α²|Φ|⁴ = 8πG ρ_Φ/3 required epoch-by-epoch — open verification (§2.3.1). (4) Post-locking matter content: SM radiation + non-relativistic matter + geometric unloading → standard ρ(a) composition (Part 2 §XII–§XIII). (5) Λ-dominated asymptote: true equation of state w = −1 (Part 2 §13.3).

**Homogeneous limit.** When spatial gradients of |Φ_NTE|² are negligible on Hubble scales (δρ/ρ ≪ 1), H(x,N) → H(N) and the background is single-fluid FRW with ρ_eff = 3H²/(8πG). If the matter sector splits into standard radiation, matter, and cosmological constant in the usual way, the expansion history is **ΛCDM-class** with parameters set by NTE's α, trajectory, and SM content. NTE does not replace ΛCDM in this limit; it supplies a geometric origin for H(N) and for selected parameters (κ, n_s, M₁ at S1, etc.) while using the same FRW bookkeeping.

**Benchmark map (status honest).**

| Observable | ΛCDM role | NTE corpus status |
|------------|-----------|-------------------|
| CMB peak structure | Acoustic scale, Ω_b, Ω_m | Implicit standard thermal history; not re-fitted |
| κ (amplitude) | Ω_m, Ω_b | **Prediction** κ ≈ 5.50 (§9.3); CMB epoch nearly homogeneous — void bias should not affect z ~ 1100 κ (Part 2 §13.3) |
| n_s | Inflation | **Derived** 0.9685 (§17.5.14; Companion 9) — independent of H₀ construction (§2.4.3) |
| r | Tensors | Three-readings table §18.4; hilltop ≈ 4×10⁻³ structurally favoured |
| BAO distances | H(z), Ω_m | FRW recovery implicit; **inhomogeneity:** void-enhanced H biases low-z distances (Part 2 §13.3) |
| σ_8, P(k), RSD | Growth | **Open** — growth under H(x,N) not explicitly fitted |
| H₀ (local vs CMB) | Single parameter | **Distinguishing:** local > CMB from spatial |Φ_NTE|² (§13.2) |
| DESI w₀, w_a | Dark-energy EOS | **Distinguishing:** void volume-weighting mimics w > −1; not phantom DE (Part 2 §13.3) |

**Where NTE is not ΛCDM (predictions, not inconsistencies).** Spatial H(x,N) from |Φ_NTE(x)|²; CPN mirror-sector dark matter (κ geometric coupling, §3.3); pre-temporal / gauge-birth regime outside ΛCDM by definition.

**Open work (research programme).** Full Planck + DESI + BAO χ² fits not in corpus. Priority: (i) epoch-by-epoch ρ_Φ ↔ α²|Φ|⁴ through radiation/matter/Λ; (ii) explicit homogeneous BAO distance comparison; (iii) structure growth / σ_8 under H(x,N). Working scaffold: `Working/LCDM_Reduction_Appendix_Scaffold_v0_1_20260523.md`. **N_lock** derivation remains separate (§17.5.4; `17.5.4_Audit_NLock_Derivation.md` in depreciated/).
```

---

## Patch T2-2a: Part 1 header

**Find:**

```
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.11 (ship date: 2026-05-23). Tier 1 Programme S spine sync (§22.15 P0 status; Paper S2 registry); carries Tier 0 + v10.9 A5+A6.
```

**Replace with:**

```
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.12 (ship date: 2026-05-23). Tier 2 §17.5.9 ΛCDM reduction expansion; carries v10.11 Programme S + Tier 0 + v10.9 A5+A6.
```

---

## Patch T2-2b: Part 2 header

**Find:**

```
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.11 (ship date: 2026-05-23). Tier 1 Programme S spine sync; carries v10.10 Tier 0 + v10.9 §8.7.7 helicity (A6).
```

**Replace with:**

```
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.12 (ship date: 2026-05-23). Carries v10.11 Programme S spine + prior tiers.
```

---

## Patch T2-2c: Part 3 header

**Find:**

```
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.11 (ship date: 2026-05-23). v10.11: §22.15 P0 PASS sync + Paper S2 registry (Tier 1); v10.10: §XXI Gap 1 S1, §XVII r, A5+A6.
```

**Replace with:**

```
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.12 (ship date: 2026-05-23). v10.12: §17.5.9 ΛCDM reduction expansion (Tier 2); v10.11: Programme S spine; v10.10: Gap 1 S1, r, A5+A6.
```
