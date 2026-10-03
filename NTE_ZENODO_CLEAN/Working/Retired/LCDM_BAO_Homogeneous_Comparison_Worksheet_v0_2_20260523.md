# ΛCDM Tier 2c — Homogeneous BAO distance comparison worksheet (P2)

**Stream:** Cursor numerics → **Jammer** review / void-bias layer; AC §17.5.9  
**Date:** 2026-05-23 (v0.2)  
**Status:** Homogeneous distances **computed** — exploratory Δ/σ vs DESI DR1; **no χ²**

**Script:** `Working/lcdm_bao_numerics.py`

---

## §1. Claim under test (unchanged)

Homogeneous NTE H(z) ≡ ΛCDM with matched {Ω_m, Ω_Λ, Ω_r, H₀}. BAO distances from standard integrals should match ΛCDM before void bias (Part 2 §13.2–§13.3).

---

## §2. Distance definitions

- D_M(z) = comoving transverse distance = c/H₀ ∫₀^z dz′/E(z′)  
- D_H(z) = c/H(z)  
- D_V(z) = (z D_M² D_H)^{1/3} (DESI volume distance)

E(z) = √(Ω_r(1+z)⁴ + Ω_m(1+z)³ + Ω_Λ). **r_d = 147.09 Mpc** fixed (Planck 2018; not refit).

---

## §3. Numerical results (Cursor v0.2)

| tracer | z_eff | obs | ΛCDM Planck H₀=67.4 | ΛCDM NTE H₀=67.6 | DESI DR1 | Δ (Planck−DESI) |
|--------|-------|-----|---------------------|------------------|----------|-----------------|
| BGS | 0.295 | D_V/r_d | 8.053 | 8.029 | 7.93 ± 0.15 | +0.12 (+0.8σ) |
| LRG1 | 0.510 | D_M/r_d | 13.493 | 13.454 | 13.62 ± 0.25 | −0.13 (−0.5σ) |
| LRG2 | 0.706 | D_M/r_d | 17.692 | 17.640 | 16.85 ± 0.32 | +0.84 (+2.6σ) |
| LRG3+ELG1 | 0.930 | D_M/r_d | 21.914 | 21.849 | 21.71 ± 0.28 | +0.20 (+0.7σ) |
| ELG2 | 1.317 | D_M/r_d | 28.012 | 27.930 | 27.79 ± 0.69 | +0.22 (+0.3σ) |

**NTE vs Planck column:** <0.3% shift in D_M/r_d at z=0.51 (H₀ 67.6 vs 67.4).

**DESI source:** arXiv:2404.03002 (DESI 2024 VI), Table 1.

---

## §4. Interpretation (Jammer / AC)

**Step A — PASS:** NTE homogeneous H(z) = ΛCDM H(z) at matched Ω's (algebraic identity; P1 worksheet).

**Step B — Exploratory:** Planck-ΛCDM homogeneous predictions vs DESI DR1 show **mixed offsets** (~0.5–2.6σ on D_M at individual bins). This is the known **DESI vs Planck-ΛCDM** background tension band (DESI 2024 reports scales systematically displaced at z < 0.8 vs Planck-ΛCDM). **Not** an NTE-specific failure mode unless NTE chooses parameters outside the stated benchmark set.

**Corpus discipline:** Do **not** write “NTE fits DESI BAO.” Write: “homogeneous reduction matches ΛCDM; DESI–Planck tension is external benchmark context for void-bias narrative (§13.3).”

**Step C — Void bias (reconciliation):** See **`LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`**. Homogeneous Planck **overshoot** at LRG2 (z≈0.71, +2.6σ) is the bin where Part 2 §12.4 void-enhanced H **shortens** inferred D_M — illustrative model brings +2.6σ → +0.2σ (`lcdm_bao_void_bias.py`, **not fitted**). **Not** per-bin χ² closure; joint w₀w_a + diagnostics §17.5.12 are the corpus test.

---

## §5. Jammer next actions

1. Optional: D_M/D_H combined χ² proxy at LRG bins (still not global fit).  
2. Void-bias percent shift column at z < 0.5.  
3. Cross-link P4 Tier A proposal when Greg authorises χ² stack.

---

## §6. Cross-references

- `Working/LCDM_Epoch_Friedmann_Check_Worksheet_v0_2_20260523.md` (P1)  
- `Working/LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`  
- `Working/LCDM_Growth_Sigma8_Worksheet_v0_1_20260523.md` (P3)

— Cursor v0.2, 2026-05-23.
