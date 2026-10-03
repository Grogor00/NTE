# ΛCDM Tier 2c — NTE vs DESI BAO reconciliation note

**Stream:** Cursor analysis → **Jammer** refine / **AC** §17.5.9 language  
**Date:** 2026-05-23  
**Basis:** P2 numerics (`lcdm_bao_numerics.py`); void-bias illustration (`lcdm_bao_void_bias.py`); Part 2 §12.4, §13.2–§13.3; §17.5.9

---

## §1. Problem statement (precise)

There is **no separate “NTE homogeneous H(z)”** that disagrees with DESI. At matched {Ω_m, Ω_Λ, Ω_r, H₀}, NTE's post-locking trajectory gives **H_NTE(z) = H_ΛCDM(z)** (P1–P2 PASS).

What P2 measured is **Planck-ΛCDM homogeneous distances vs DESI DR1** — a tension that exists in **standard cosmology** (DESI 2024 VI reports displacement vs Planck-ΛCDM at z ≲ 0.8).

**Reconciliation task:** Show this is **not** a failure of NTE's homogeneous reduction, and that NTE's **pre-existing** inhomogeneity programme (void-enhanced H) provides the **correct interpretive layer** for low-z BAO/DESI w₀wₐ — without claiming a completed global fit.

---

## §2. Three-layer reconciliation

### Layer A — Homogeneous identity (closed)

| Claim | Status |
|-------|--------|
| NTE H(z) = ΛCDM H(z) at matched Ω's | ✓ Algebraic (P1, P2) |
| NTE H₀ = β_NTE v_EW² ≈ 67.6 vs Planck 67.4 | <0.3% distance shift — negligible vs DESI bin errors |
| “NTE predicts different BAO than ΛCDM” in hom limit | **False** |

### Layer B — DESI vs Planck-ΛCDM (external benchmark)

P2 homogeneous table (Planck H₀=67.4, r_d fixed):

| Bin | z_eff | Δ (Planck_hom − DESI) on D_M or D_V |
|-----|-------|-----------------------------------|
| LRG1 | 0.51 | −0.13 (−0.5σ) — DESI **longer** |
| LRG2 | 0.71 | **+0.84 (+2.6σ)** — DESI **shorter** |
| LRG3+ELG1 | 0.93 | +0.20 (+0.7σ) |
| ELG2 | 1.32 | +0.22 (+0.3σ) |

**Pattern:** Mixed sign, ~1–2.6σ per bin — **not** a uniform “NTE wrong” shift. Worst case is **LRG2**: homogeneous Planck **overpredicts** comoving distance (DESI sees **shorter** scale).

### Layer C — NTE void-bias mechanism (corpus, Part 2 §12.4)

NTE predicts:

1. **True** w = −1 (geometric unloading).  
2. **Observed** w₀ > −1 at low z from **volume-weighted void-enhanced H** — BAO distances **shorter** than homogeneous ΛCDM.  
3. Bias **grows** toward z → 0, **vanishes** at high z (diagnostics §17.5.12).

**Directional match:** LRG2 (+2.6σ hom overshoot) is exactly the bin where **shorter inferred D_M** moves Planck prediction **toward** DESI.

Illustrative void model (`lcdm_bao_void_bias.py`, **not fitted**, b≈0.055):

| Bin | Hom σ | Void σ (illustrative) |
|-----|-------|------------------------|
| LRG2 z=0.71 | **+2.63** | **+0.20** |
| LRG1 z=0.51 | −0.51 | −2.93 (overshoots — see §3) |
| LRG3+ELG1 | +0.73 | −2.45 |

**Takeaway:** A single phenomenological void bias **cannot** close all bins simultaneously without a full tracer + covariance analysis. It **can** show the **mechanism direction** resolves the **largest homogeneous overshoot** (LRG2).

---

## §3. Honest limits (do not overclaim)

| Limit | Detail |
|-------|--------|
| Not a χ² fit | Illustrative b only; Jammer must use DESI covariances + tracer weights |
| LRG1 | Hom already −0.5σ; naive void bias worsens — DESI z=0.51 D_M/D_H split is ~2σ anomaly **orthogonal** to D_V (DESI 2024 VI §discussion) |
| High-z bins | Integral still samples low-z biased segment; full reconciliation needs **line-of-sight void fraction** (diagnostic (a)) |
| r_d | Fixed Planck r_d; DESI+BBN r_d shift would move all columns coherently |
| Phantom wₐ | NTE reads w₀wₐ as **parameterisation artifact** of non-linear void bias (§12.4) — test is **joint** DESI+CMB+SN, not single D_M bin |

---

## §4. Recommended corpus language (AC / §17.5.9)

**Say:**

> Homogeneous NTE reduction matches ΛCDM distances. DESI–Planck per-bin offsets are external to NTE's homogeneous class. NTE interprets low-z DESI w₀ > −1 and **select** BAO distance deficits (e.g. z≈0.7) as **void volume-weighting** of H(x,N) = β_NTE|Φ|² — one mechanism with Hubble tension (§13.2), not dynamical dark energy.

**Do not say:**

> NTE fits DESI BAO.  
> NTE resolves DESI w₀wₐ at Nσ (not computed).

---

## §5. Tests that would confirm / falsify this reconciliation

| Test | Confirm void narrative | Falsify |
|------|------------------------|---------|
| (a) w₀ departure vs void fraction along LOS | Correlation | No correlation at predicted amplitude |
| (b) w bias ∝ σ₈²(z)/Ω_Λ(z) | Trend with z | Flat or wrong z-scaling |
| (c) Variance-corrected BAO | Bias vanishes | Persists |
| (d) CMB κ at z~1100 | κ → 5.50, no void bias | Same low-z bias in κ |
| P3 fσ₈(z) | Consistent with σ₈(z) scaling in (b) | Hom growth breaks |

(From §17.5.12 + Part 2 §12.4 diagnostics.)

---

## §6. Jammer next steps

1. Replace illustrative b with **tracer-weighted** void model or ISW-corrected H_eff.  
2. Joint D_M + D_H at LRG1/LRG2 with DESI correlation r ≈ −0.44.  
3. P3 growth: verify homogeneous fσ₈ track before inhomogeneous layer.  
4. P4 Tier A: exploratory w₀w_a from biased vs unbiased distance columns only if Greg authorises.

---

## §7. Cross-references

- `Working/LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_2_20260523.md`  
- `Working/lcdm_bao_numerics.py`, `Working/lcdm_bao_void_bias.py`  
- `Working/LCDM_Growth_Sigma8_Worksheet_v0_1_20260523.md` (P3)

— Cursor, 2026-05-23.
