# ΛCDM Tier 2c — Structure growth / σ₈ worksheet (P3)

**Stream:** Cursor numerics → **Jammer** inhomogeneous layer; AC §17.5.9  
**Date:** 2026-05-23 (v0.2)  
**Status:** **Homogeneous numerics done** (`lcdm_growth_numerics.py`); inhomogeneous layer open

---

## §1. Question

Under NTE's post-locking FRW reduction (§17.5.9), does **linear growth** D(z) / **σ₈(z)** match ΛCDM in the homogeneous limit, and how does **spatial H(x,N) = β_NTE|Φ(x,N)|²** modify growth + RSD relative to standard GR?

**Corpus default (homogeneous):** when δρ/ρ ≪ 1 on BAO/RSD scales, background H(N) is ΛCDM-class → **standard growth ODE** applies to the mean.

**NTE-specific (inhomogeneous):** void/supercluster Φ(x) gradients modify local H and potentially growth — ties to §13.2 Hubble tension and §12.4 DESI w₀ narrative.

---

## §2. Homogeneous growth (filled)

Linear growth factor D(a) satisfies (ΛCDM):

$$\ddot{D} + 2H\dot{D} - \frac{3}{2}\Omega_m(a) H^2 D = 0$$

**Fiducials:** Planck 2018 — Ω_m = 0.315, Ω_Λ = 0.685, Ω_r = 9×10⁻⁵, σ₈(0) = 0.811.

**NTE homogeneous prediction:** Same H(z) as P1/P2 → **same D(z), σ₈(z), fσ₈(z) as ΛCDM**. No extra growth parameter in corpus.

**Script:** `Working/lcdm_growth_numerics.py` (ODE in ln a, D(1)=1).

---

## §3. Homogeneous benchmark table (2026-05-23)

| z_eff | D(z) | f(z) | σ₈(z) | fσ₈ hom | DESI fσ₈ (ref.) | Δ/σ |
|-------|------|------|-------|---------|-----------------|-----|
| 0.00 | 1.000 | 0.529 | 0.811 | 0.429 | — | — |
| 0.51 | 0.765 | 0.764 | 0.621 | 0.474 | 0.457 ± 0.033 | +0.5σ |
| 0.71 | 0.693 | 0.820 | 0.562 | 0.461 | 0.454 ± 0.030 | +0.2σ |
| 0.93 | 0.626 | 0.865 | 0.508 | 0.439 | 0.448 ± 0.028 | −0.3σ |
| 1.32 | 0.531 | 0.916 | 0.431 | 0.394 | 0.434 ± 0.032 | −1.2σ |

**DESI column:** illustrative central ±1σ from DESI BAO+RSD literature (not corpus fit). **No global χ².**

**Reading:**

1. **Homogeneous NTE ≡ ΛCDM** at matched calibration (same tautology class as P1/P2).  
2. Exploratory DESI offsets are **sub-1.5σ per bin** — **milder** than P2 BAO LRG2 (+2.6σ hom D_M overshoot at z≈0.71).  
3. **No parallel low-z growth “crisis”** at homogeneous level; BAO void-bias reconciliation (P2) is **not** mirrored by a +2σ fσ₈ spike at z≈0.71 (+0.2σ only).  
4. High-z bin (z≈1.32) shows largest hom undershoot (−1.2σ) — Jammer to check against DESI ELG systematics before inferring w₀wₐ.

**NTE hom column:** identical to ΛCDM row (by construction).

---

## §4. NTE inhomogeneous layer (open — Jammer)

| Effect | Mechanism | Worksheet task |
|--------|-----------|----------------|
| Local H boost in voids | \|Φ(x)\|² lower in voids → faster local expansion | Perturbative δH/H on growth? |
| κ mirror DM | Geometric DM not adiabatic CDM | Does P(k) match ΛCDM+CDM on large scales? |
| Volume-weighted RSD | Tracer bias × void sampling | Tie to §12.4 diagnostics |

**Honest status:** Part 2 does **not** ship a closed growth equation with spatial Φ(x). Inhomogeneous P3 remains **Jammer-derivation**.

---

## §5. DESI / BAO reconciliation link

P2: homogeneous D_M overshoot at LRG2 z≈0.71 (+2.6σ); illustrative void weighting → ~+0.2σ (`LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`).

P3: at same z≈0.71, **fσ₈ hom vs DESI is +0.2σ** — consistent with ΛCDM, **not** with a void-bias correction of BAO magnitude. Joint BAO+RSD narrative requires **inhomogeneous** or **systematics** layer; do **not** claim “NTE fits DESI RSD.”

§17.5.12 falsifier (b): w_obs diagnostic ties w departure to σ₈²(z)/Ω_Λ(z) — still open.

---

## §6. Jammer deliverables (remaining)

1. ~~Integrate growth ODE; hom table~~ — **done (Cursor v0.2)**.  
2. H₀ sensitivity / NTE H₀=69.47 variant (if distinct from Planck).  
3. Inhomogeneous layer: perturbative vs N-body decision.  
4. Update P4 catalogue F1/F5 with growth evidence.

---

## §7. Cross-references

- `Working/lcdm_growth_numerics.py`  
- `Working/LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_2_20260523.md` (P2)  
- `Working/LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`  
- Part 2 §12.4, §13.2; §17.5.9 benchmark row σ₈/P(k)/RSD  
- `Working/LCDM_Chi2_Falsifier_Catalogue_v0_1_20260523.md` (P4)

— Cursor P3 v0.2, 2026-05-23.
