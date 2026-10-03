# ΛCDM Tier 2c — Structure growth / σ₈ worksheet scaffold (P3)

**Stream:** Cursor scaffold → **Jammer** execution; AC §17.5.9  
**Date:** 2026-05-23 (v0.1)  
**Status:** Structural scaffold — **no growth ODE integration performed**

---

## §1. Question

Under NTE's post-locking FRW reduction (§17.5.9), does **linear growth** D(z) / **σ₈(z)** match ΛCDM in the homogeneous limit, and how does **spatial H(x,N) = β_NTE|Φ(x,N)|²** modify growth + RSD relative to standard GR?

**Corpus default (homogeneous):** when δρ/ρ ≪ 1 on BAO/RSD scales, background H(N) is ΛCDM-class → **standard growth ODE** should apply to the mean.

**NTE-specific (inhomogeneous):** void/supercluster Φ(x) gradients modify local H and potentially growth — ties to §13.2 Hubble tension and §12.4 DESI w₀ narrative.

---

## §2. Homogeneous growth (Jammer baseline)

Linear growth factor D(a) satisfies (ΛCDM):

$$\ddot{D} + 2H\dot{D} - \frac{3}{2}\Omega_m(a) H^2 D = 0$$

with initial conditions D(a→0) ∝ a in matter domination.

**Derived quantities:**

| Symbol | Definition | Planck 2018 fiducial |
|--------|------------|----------------------|
| σ₈ | σ(R=8 h⁻¹ Mpc) at z=0 | 0.811 ± 0.006 |
| f(z) | d ln D / d ln a | ~ Ω_m(z)^0.55 (approx) |
| fσ₈(z) | f(z) × σ₈(z) | DESI RSD target |

**NTE homogeneous prediction:** Same H(z) as P1/P2 worksheets → **same D(z), σ₈(z), fσ₈(z) as ΛCDM** at matched {Ω_m, Ω_Λ, H₀}. No extra growth parameter in corpus.

**Script stub:** extend `lcdm_epoch_numerics.py` or new `lcdm_growth_numerics.py` (Jammer).

---

## §3. NTE inhomogeneous layer (open)

| Effect | Mechanism | Worksheet task |
|--------|-----------|----------------|
| Local H boost in voids | \|Φ(x)\|² lower in voids → **faster** local expansion | Perturbative δH/H on growth? |
| κ mirror DM | Geometric DM not adiabatic CDM | Does P(k) match ΛCDM+CDM on large scales? |
| Volume-weighted RSD | Tracer bias × void sampling | Tie to §12.4 diagnostics |

**Honest status:** Part 2 does **not** ship a closed growth equation with spatial Φ(x). P3 is **Jammer-derivation**, not Cursor closure.

---

## §4. Benchmark anchors (Jammer to fill)

| z_eff | fσ₈ (DESI/Planck class) | σ₈(z) hom ΛCDM | NTE hom (=ΛCDM) | Notes |
|-------|-------------------------|----------------|-----------------|-------|
| 0.51 | [Jammer] | [compute] | same | LRG1 era; BAO P2 link |
| 0.71 | [Jammer] | [compute] | same | LRG2 — BAO void-bias anchor |
| 0.93 | [Jammer] | [compute] | same | High-z hom recovery |
| 1.32 | [Jammer] | [compute] | same | ELG2 |

**Cross-check:** If homogeneous growth matches ΛCDM but **RSD+BAO joint** prefers w₀wₐ, void-bias inference (P2 reconciliation) is **consistent**; if growth fails at hom level, reduction chain breaks (F1 in P4 catalogue).

---

## §5. DESI / BAO reconciliation link

P2 shows **homogeneous** D_M can overshoot DESI at z≈0.71 (+2.6σ). Illustrative void volume-weighting (Part 2 §12.4) **shortens** inferred D_M at that bin — see `LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`.

P3 asks: does **fσ₈** show parallel low-z bias, or stay ΛCDM? NTE falsifier §17.5.12: w_obs diagnostic (b) ties w departure to σ₈²(z)/Ω_Λ(z).

---

## §6. Jammer deliverables

1. Integrate growth ODE; table σ₈(z), f(z), fσ₈(z) for Planck + NTE H₀.  
2. Compare to DESI RSD published fσ₈(z) (exploratory Δ/σ, not χ²).  
3. Decide if inhomogeneous layer is perturbative (~percent) or requires N-body.  
4. Update P4 catalogue F1/F5 with growth evidence.

---

## §7. Cross-references

- `Working/LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_2_20260523.md` (P2)  
- `Working/LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md`  
- Part 2 §12.4, §13.2; §17.5.9 benchmark row σ₈/P(k)/RSD  
- `Working/LCDM_Chi2_Falsifier_Catalogue_v0_1_20260523.md` (P4)

— Cursor P3 scaffold v0.1, 2026-05-23.
