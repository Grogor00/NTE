# ΛCDM Tier 2c — Epoch Friedmann identification worksheet (P1)

**Stream:** Cursor draft → **Jammer** review / V_NTE split; AC master cross-ref  
**Date:** 2026-05-23 (v0.2 numerics filled by Cursor)  
**Master hook:** §17.5.9 open work (i); Part 1 §2.3.1  
**Status:** Homogeneous epoch table **computed** — not a multi-component ρ_Φ vs ρ_m,r,Λ decomposition

---

## §1. Identification to verify

At each post-locking epoch, NTE requires:

$$\alpha^2 |\Phi_{\mathrm{NTE}}|^4 = \frac{8\pi G}{3}\,\rho_\Phi$$

with trajectory (§2.3.1):

$$|\Phi_{\mathrm{NTE}}|^2 = v_{\mathrm{EW}}^2 \cdot \frac{H(N)}{H_0}$$

**Corpus constants (natural units unless noted):**

| Symbol | Value | Source |
|--------|-------|--------|
| α | 2.38 × 10⁻⁴⁷ GeV⁻¹ | §2.4.2 characterisation |
| v_EW | 246 GeV | SM |
| H₀ (NTE construction) | β_NTE v_EW² ≈ 67.6 km/s/Mpc | §2.4.2–§2.4.3 |
| H₀ (Planck 2018) | 67.4 ± 0.5 km/s/Mpc | external benchmark |
| Ω_m, Ω_Λ, Ω_r | 0.315, 0.685, ~9×10⁻⁵ | Planck 2018 |

Homogeneous Friedmann ratio (e-fold N from today):

$$\frac{H(N)}{H_0} = \sqrt{\Omega_r e^{-4N} + \Omega_m e^{-3N} + \Omega_\Lambda}$$

**Script:** `Working/lcdm_epoch_numerics.py` (re-runnable).

---

## §2. Structural check at H = H₀ (today)

Left-hand side (trajectory-imposed): α² v_EW⁴ (since H/H₀ = 1).

Right-hand side if ρ_Φ = ρ_crit: 8πG ρ_crit/3 = H₀².

**Consistency:** α² v_EW⁴ = H₀² ⟺ H₀ = β_NTE v_EW² — **by construction** (§2.4.3).

---

## §3. Epoch table (homogeneous trajectory — Cursor v0.2 numerics)

| Epoch | N (from today) | H/H₀ | \|Φ\|²/v_EW² | (H/H₀)² rel. today | ρ_Φ = ρ_crit if trajectory + full identification? |
|-------|----------------|------|--------------|---------------------|---------------------------------------------------|
| Today | 0.000 | 1.000 | 1.000 | 1.000 | ✓ by construction |
| z ~ 0.5 (DESI BAO era) | −0.406 | 1.322 | 1.749 | 1.749 | ✓ **if** ρ_Φ carries full ρ_crit |
| Matter–Λ equality | −0.259 | 1.171 | 1.370 | 1.370 | ✓ same caveat |
| BBN (radiation dom.; z ~ 10⁹) | −20.72 | 9.49×10¹⁵ | 9.00×10³¹ | 9.00×10³¹ | ✓ same caveat |

**Interpretation (Jammer):** Under \|Φ\|² = v_EW² (H/H₀) and H₀ = β_NTE v_EW², the identity α²\|Φ\|⁴ = H² holds at **every** homogeneous epoch **if** ρ_Φ is identified with **all** of ρ_crit. That is not an extra empirical constraint — it is the trajectory + calibration stack.

**Open physics (not closed by this table):**

1. Decompose ρ_total = ρ_Φ + ρ_m + ρ_r + ρ_Λ — does V_NTE assign ρ_Φ equal to ρ_crit or a sub-fraction while SM+Λ carry the rest?
2. BBN/CMB: \|Φ\|² ~ 10³¹ v_EW² is enormous; compare to independent V_NTE energy density when Session 5 D1 lands.
3. Gauge birth (N_lock): outside homogeneous ΛCDM reduction.

---

## §4. What would falsify homogeneous reduction

(Unchanged from v0.1 — now with epoch anchors for item 1.)

1. Trajectory \|Φ(N)\|² inconsistent with observed H(z) at fixed α.  
2. BBN/CMB require \|Φ\| evolution incompatible with §2.3.1.  
3. Independent ρ_Φ from V_NTE ≠ 3H²/(8πG) at > few-percent in radiation/matter eras.

---

## §5. Cross-references

- `Working/LCDM_Reduction_Appendix_Scaffold_v0_2_20260523.md`  
- `Working/LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_1_20260523.md` (P2)  
- `Handoff_Cursor_to_Jammer_AC_Tier2c_LCDM_Worksheets_20260523.md`

— Cursor v0.2 numerics, 2026-05-23.
