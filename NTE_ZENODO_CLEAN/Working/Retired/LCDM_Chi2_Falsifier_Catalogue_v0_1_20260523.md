# ΛCDM Tier 2c — Global χ² programme scope + falsifier catalogue (P4)

**Stream:** Cursor draft → AC (scope gate) + Jammer (execution)  
**Date:** 2026-05-23  
**Status:** **Scope document only** — no fits performed in corpus

---

## §1. What the corpus does **not** claim (2026-05-23)

| Item | Status |
|------|--------|
| Planck TT/TE/EE + lensing global fit | **Not performed** |
| DESI DR2 BAO χ² | **Not performed** |

**Cursor worksheets (2026-05-23):** P1 epoch table + P2 homogeneous BAO table **computed** (`*_v0_2_*.md`); exploratory Δ/σ vs DESI only — **not** a likelihood fit (see P2 §4).
| Pantheon+/SH0ES joint H₀ fit | **Not performed** |
| Growth σ_8, fσ_8, P(k) likelihood | **Not performed** |
| MCMC chains / corner plots in Papers/ | **None** |

§17.5.9 expansion (v10.12+) states this explicitly. This file is the **programme definition** for a future run.

---

## §2. Proposed χ² stack (when authorised)

**Tier A — Background only (minimal credible step):**

- Data: DESI BAO D_V/r_d + optional SN Ia H(z) (not full SNe systematics).  
- Model: Homogeneous ΛCDM-class H(z) from NTE trajectory (same as ΛCDM with H₀ = β_NTE v_EW²).  
- Test: NTE parameters within 1σ of ΛCDM best-fit **or** document where NTE forbids a region ΛCDM allows.

**Tier B — CMB distance priors:**

- Add θ_MC, r_s priors from Planck (not full likelihood) — fast consistency check.

**Tier C — Full (deferred):**

- Planck high-ℓ + low-ℓ + lensing; RSD; κ amplitude; requires growth sector (P3 open).

**Owner:** Jammer numerics; AC signs off before any "χ² = X" language enters master.

---

## §3. Falsifier catalogue (homogeneous reduction fails)

| ID | Falsifier | If observed |
|----|-----------|-------------|
| F1 | Homogeneous H(z) from §2.3.1 disagrees with BAO+SN at >3σ with fixed α | Trajectory or β_NTE characterisation wrong |
| F2 | Epoch Friedmann check (P1) fails at BBN/CMB for ρ_Φ = ρ_crit | §2.3.1 identification broken |
| F3 | CMB κ converges to value ≠ 5.50 at z~1100 (homogeneous epoch) | κ prediction falsified (void bias ruled out per §13.3) |
| F4 | n_s derivation + H₀ construction accidentally double-use same datum | Epistemic hygiene failure (§2.4.3 already separates) |
| F5 | Void-bias explanation fails DESI diagnostic (d): w bias correlates with void fraction | Alternative DE required |

**Non-falsifiers (distinguishing predictions, not ΛCDM failure):**

- Local H₀ > CMB H₀ (§13.2).  
- DESI w₀ > −1 at low z with w → −1 at high z (§13.3).  
- κ = 5.50 vs Ω_m from CMB (different microphysics — mirror sector).

---

## §4. Deliverables checklist (Jammer / AC)

- [ ] P1 epoch table numerically filled (`LCDM_Epoch_Friedmann_Check_Worksheet_v0_1`)  
- [ ] P2 D_V/r_d table at z = 0.51, 0.71, 1.01 (`LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_1`)  
- [ ] P3 growth equation note (σ_8) — separate future file  
- [ ] Tier A exploratory χ² — **only after Greg authorises "claim fit" language**  
- [ ] AC: one paragraph in §17.5.9 when Tier A complete — no silent upgrade

---

## §5. Cross-references

- `Working/LCDM_Reduction_Appendix_Scaffold_v0_2_20260523.md`  
- Master §17.5.9 (v10.14 Tier 2c pointer)  
- CR adversarial priorities 2026-05-21 cluster B (cosmology credibility)

— Cursor, 2026-05-23.
