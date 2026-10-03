# ΛCDM Tier 2c — Homogeneous BAO distance comparison worksheet (P2)

**Stream:** Cursor draft → **Jammer** numerics; AC §17.5.9 integration  
**Date:** 2026-05-23  
**Status:** Setup + comparison protocol — **no χ²**, no claimed DESI/Planck fit

---

## §1. Claim under test (homogeneous limit)

When δρ/ρ ≪ 1 on BAO scales, NTE predicts **the same H(z)** as ΛCDM with the same {Ω_m, Ω_Λ, Ω_r, H₀} carried by the §2.3.1 trajectory. BAO **comoving distances** D_C(z) and volume-averaged D_V(z) should then match ΛCDM at the percent level **before** void-selection bias (Part 2 §13.2–§13.3).

**Distinguishing layer (separate worksheet):** void-enhanced H(x,N) biases **inferred** low-z distances and DESI w₀wₐ — not a failure of homogeneous H(z).

---

## §2. Distance definitions (standard)

Comoving distance:

$$D_C(z) = c \int_0^z \frac{dz'}{H(z')}$$

Angular diameter distance: D_A = D_C/(1+z). Volume distance: D_V = [z D_C² D_A]^{1/3} (approximation used in surveys).

**ΛCDM H(z):**

$$H(z) = H_0 \sqrt{\Omega_r (1+z)^4 + \Omega_m (1+z)^3 + \Omega_\Lambda}$$

---

## §3. Parameter sets (Jammer: pick one primary column)

| Set | H₀ [km/s/Mpc] | Ω_m | Ω_Λ | Notes |
|-----|---------------|-----|-----|-------|
| Planck 2018 | 67.4 | 0.315 | 0.685 | External ΛCDM benchmark |
| NTE construction | 67.6 | 0.315 | 0.685 | β_NTE v_EW²; Ω_Λ in N_total loop (§2.4.2) |
| SH0ES-tension split | 73.0 / 67.4 | same | same | NTE void narrative uses **local** > **CMB** — compare columns |

Sound horizon r_d: use published fitting formula (Planck 2018: r_d ≈ 147.09 Mpc) — **do not refit** in this worksheet; hold fixed for distance comparison.

---

## §4. Redshift anchors (DESI-era)

| Survey use | z | Observable | Homogeneous prediction |
|------------|---|------------|------------------------|
| BAO (example) | 0.51 | D_V/r_d | D_V^ΛCDM(z)/r_d — **compute** |
| BAO (example) | 0.71 | D_V/r_d | same |
| BAO (example) | 1.01 | D_V/r_d | same |
| CMB (acoustic) | ~1100 | θ_* | standard thermal history (implicit) |

**Jammer deliverable:** Python/Camb-class script or table: D_V(z_i)/r_d for ΛCDM rows above; second column NTE homogeneous H(z) — should be **identical** if same Ω's and H₀. Third column: optional void-bias model from §13.3 (percent shift at low z only).

---

## §5. Comparison protocol (honest)

1. **Step A — Homogeneous:** Show NTE H(N) trajectory → H(z) equals ΛCDM with matched Ω's (algebraic or numeric).  
2. **Step B — BAO:** Compare D_V/r_d to DESI published central values; report Δ/σ **as exploratory**, not corpus closure.  
3. **Step C — Inhomogeneity:** Only if Step A matches: attribute low-z DESI w₀ > −1 to void bias per Part 2 §13.3, not to homogeneous H(z) failure.

**Do not claim:** "NTE fits DESI BAO χ² = …" until global pipeline (P4 catalogue) is run and Greg/AC authorise.

---

## §6. Expected qualitative outcome (corpus)

| Regime | Expected |
|--------|----------|
| z ≳ 1 homogeneous | NTE ≡ ΛCDM distances (same H(z)) |
| z ≲ 0.3 inferred | Void bias may shorten distances → mimics w > −1 |
| CMB z ~ 1100 | Nearly homogeneous; κ prediction testable without void bias (§13.3 diagnostic (d)) |

---

## §7. Cross-references

- Part 2 §13.2–§13.3, §17.5.9 benchmark row "BAO distances"  
- `Working/LCDM_Epoch_Friedmann_Check_Worksheet_v0_1_20260523.md` (P1)  
- `Working/LCDM_Chi2_Falsifier_Catalogue_v0_1_20260523.md` (P4)

— Cursor, 2026-05-23.
