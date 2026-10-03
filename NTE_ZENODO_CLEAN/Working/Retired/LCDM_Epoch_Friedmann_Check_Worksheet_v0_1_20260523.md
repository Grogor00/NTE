# ΛCDM Tier 2c — Epoch Friedmann identification worksheet (P1)

**Stream:** Cursor draft → **Jammer** execution / numerics; AC master cross-ref  
**Date:** 2026-05-23  
**Master hook:** §17.5.9 open work (i); Part 1 §2.3.1  
**Status:** Structural worksheet — **not** a completed multi-epoch proof

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
| Ω_m, Ω_Λ, Ω_r | 0.315, 0.685, ~9×10⁻⁵ | Planck 2018 (NTE loop uses Ω_Λ in N_total) |

Homogeneous Friedmann ratio (e-fold N from today):

$$\frac{H(N)}{H_0} = \sqrt{\Omega_r e^{-4N} + \Omega_m e^{-3N} + \Omega_\Lambda}$$

---

## §2. Structural check at H = H₀ (today)

Left-hand side (trajectory-imposed):

$$\alpha^2 |\Phi|^4 = \alpha^2 v_{\mathrm{EW}}^4 \left(\frac{H}{H_0}\right)^2 \Big|_{H=H_0} = \alpha^2 v_{\mathrm{EW}}^4$$

Right-hand side if ρ_Φ = ρ_crit = 3H₀²/(8πG):

$$\frac{8\pi G}{3}\rho_{\mathrm{crit}} = H_0^2$$

**Consistency condition:** α² v_EW⁴ = H₀² ⟺ H₀ = β_NTE v_EW² — **satisfied by construction** (§2.4.3: H₀ is not an independent prediction).

**Verdict at today:** Friedmann identification holds **by calibration**, not as an extra empirical constraint.

---

## §3. Epoch table (homogeneous trajectory; Jammer to fill numerics)

| Epoch | N (from today) | H/H₀ | \|Φ\|²/v_EW² | α²\|Φ\|⁴ (arb.) | ρ_crit ∝ H² | Match if ρ_Φ=ρ_crit? |
|-------|----------------|------|--------------|----------------|-------------|----------------------|
| Today | 0 | 1 | 1 | α² v_EW⁴ | H₀² | ✓ by construction |
| z ~ 0.5 (DESI BAO) | ~0.45 | [compute] | [compute] | [compute] | [compute] | **Jammer** |
| Matter–Λ equality | ~0.55 | [compute] | [compute] | [compute] | [compute] | **Jammer** |
| BBN (T ~ 1 MeV) | [large negative] | [compute] | ~10^17 (corpus order) | [compute] | [compute] | **Open** — needs V_NTE / ρ_Φ split |
| Gauge birth | N_lock | [H_GB/H₀] | ~M_Pl² scale | [compute] | [compute] | **Outside ΛCDM** |

**Jammer task:** For each row, compute whether an independent ρ_Φ from V_NTE (when specified) equals 3H²/(8πG) with H from the trajectory, or document the residual. Flag epochs where SM radiation/matter ρ dominates and ρ_Φ is only a fraction of ρ_total.

---

## §4. What would falsify homogeneous reduction

1. Trajectory |Φ(N)|² inconsistent with observed H(z) when α is held fixed at characterisation value.  
2. BBN or CMB constraints require \|Φ\| evolution incompatible with §2.3.1 while keeping H = α\|Φ\|².  
3. Independent ρ_Φ from derived V_NTE disagrees with 3H²/(8πG) at > few-percent level in radiation/matter eras (once V_NTE is specified).

---

## §5. Cross-references

- `Working/LCDM_Reduction_Appendix_Scaffold_v0_2_20260523.md`  
- `Working/LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_1_20260523.md` (P2)  
- Part 1 §2.3.0–§2.3.1, §2.4.3

— Cursor, 2026-05-23.
