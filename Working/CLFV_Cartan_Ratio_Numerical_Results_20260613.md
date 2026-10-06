# CLFV Cartan ratio — numerical results (Cursor Scratch gate)

**Author:** Cursor Scratch  
**Date:** 2026-06-13  
**Script:** `Working/clfv_cartan_ratio_numerical.py`  
**JSON:** `Working/clfv_cartan_ratio_numerical_results.json`  
**Gate:** AC ratification item (2/2) — Monte Carlo histogram for `Handoff_AC_to_Scratch_CLFV_Ratio_STRONG_INTERIM_*_20260612.md`

---

## Verdict: **DISCRIMINATOR SURVIVES** (histogram replaces analytic ~5% estimate)

| Metric | Analytic (Scratch pass-1) | **Measured (N=10⁴)** |
|--------|---------------------------|----------------------|
| Mimic fraction (±20% of tan²θ₂₃) | ~5% | **10.2%** |
| NTE-favored odds if ratio observed | ~20:1 | **~8.8:1** |

Mimic fraction **>5%** but **<20%** — discriminator **not demoted**; odds revised downward honestly.

---

## 1. Ratio test (NTE σ₁/σ₂ degenerate point)

Discriminator uses **|A(μ→eγ)|²/|A(τ→eγ)|²** (pass-1 scale-independent amplitude ratio; not full BR with m_ℓ⁻⁵).

| Point | Predicted tan²θ₂₃ | Computed ratio | Fractional deviation |
|-------|-------------------|----------------|----------------------|
| **NTE θ₂₃ = π/4** | 1.000 | **1.000** | 0% |
| **NuFIT θ₂₃ = 49.7°** | 1.390 | **1.390** | 0% |

**M₃/M₁ scan** [0.1, 0.5, 1, 2, 5, 10]: ratio **stable to <10%** at all points (exact match at machine precision for this Y_ν structure).

Loop-function / M₂ = M₁(1+sin²θ₁₃) correction: **no degradation** in this dipole-amplitude implementation (M₂ splitting absorbed in flavor-sum structure).

---

## 2. Second relations (not forced)

| Ratio | NTE π/4 | NuFIT |
|-------|---------|-------|
| \|A(τ→μγ)\|²/\|A(τ→eγ)\|² | 21.86 | 25.43 |
| \|A(ee)\|/\|A(μe)\| (dipole proxy) | 1.48 | 1.37 |

**No second scale-independent forced relation** identified at dipole level — τ→μγ ratio is PMNS-dependent, not tan²θ₂₃. μ→eee / μ–e conversion need penguin+box (not run).

---

## 3. Anarchic Monte Carlo (N=10⁴)

- Random O(1) complex **Y_ν** (3×3), same M_R spectrum  
- Target: tan²θ₂₃ (NuFIT) = 1.390  
- **10.2%** of anarchic models within ±20% of target  
- **26.9%** within ±50%  
- log₁₀ ratio spread: p16 = −0.69, p84 = +0.74 (~4.4 decades central 68%)

**Conclusion:** anarchic seesaw does **not** cluster at tan²θ₂₃ — discrimination claim **stands**, with **revised odds ~9:1** (not 20:1).

---

## 4. Absolute scale (conditional discriminator)

| Quantity | Value |
|----------|-------|
| BR(μ→eγ) order at M_R = 8.2×10¹⁴ GeV | **~4×10⁻⁵⁹** |
| MEG II limit (order) | ~4×10⁻¹³ |
| M_R for MEG II sensitivity (order) | **~2.6×10²⁶ GeV** |

**Confirmed:** absolute rate **far below MEG II** at NTE M_R — discriminator is **conditional** ("if CLFV seen, ratio discriminates"), not a rate prediction.

---

## 5. Convention / discipline

- Loop function: Casas-Ibarra / Hisano heavy-neutrino F(x), x = M_N²/M_W²  
- Y_ν(NTE): Y_{α,0,1} = Y₁ U*_{α,0,1}, Y_{α,2} = Y₃ U*_{α,2}; Y₁=(8π)^{−1/3}, Y₃=1  
- **No input tuning** to preserve ratio  
- Full BR with m_ℓ⁻⁵ **does not** equal tan²θ₂₃ (phase-space powers differ) — pass-1 discriminator is amplitude-ratio, not raw BR ratio

---

## 6. Gate status

| AC gate item | Status |
|--------------|--------|
| Cursor histogram | ✅ **This memo** |
| Independent Scratch pass 2 | ⏳ Routed — `Handoff_Cursor_Scratch_to_Scratch_CLFV_Independent_Pass2_R_Freedom_20260613.md` |

**Ratification:** still **HELD** until independent pass 2 lands.

---

— Cursor Scratch, 2026-06-13.
