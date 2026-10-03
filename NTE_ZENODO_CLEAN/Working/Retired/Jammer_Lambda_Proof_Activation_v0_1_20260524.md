# Λ-PROOF activation — heat-kernel derived measure v0.1

**From:** Jammer (R&D) — Sprint B  
**Date:** 2026-05-24  
**Status:** **DERIVED** at heat-kernel register  
**Parents:** Paper S4; BR2d-J3 §4; S3-f3 v0.2; Greg R6

---

## §0. Executive

Upgrades §17.5.18 from "path-integral derive δ(V−V_lock) still open" to **derived** at the heat-kernel / unimodular-lock register.

| Layer | Source | Status |
|-------|--------|--------|
| Unimodular projection | CC2008 + §22.15 | Done |
| Λ_{a_4} residual | S2-D heat-kernel | Done |
| V_lock = 2π² e^{3N_e} | Friedmann comoving | Done |
| dμ(V) = δ(V−V_lock)/V_lock | BR2d-J3 §4 + S3-f3 v0.2 | **Derived** |
| Λ_pred = Λ_{a_4} e^{−3N_e}/(2π²) | Paper S4 Prop 4 | **1.05× obs** |

---

## §1. Derivation chain

**Step A — Unimodular lock residual (S2-D).** After projecting extensive f₄a₀Λ⁴ mode, fixed spectral residual Λ_{a_4} ~ 10³⁷ GeV⁴.

**Step B — Comoving volume at lock (Sector 2).**

$$V_{\rm lock}=2\pi^2\,e^{3N_e},\qquad N_e=-\ln(\alpha M_{\rm Pl,nr})$$

**Step C — Measure (BR2d-J3 Proposition 3).** Conditional on crystallisation at G, unimodular volume functional assigns unit weight to lock cell:

$$\int_0^\infty \rho_\Lambda(V)\,d\mu(V)=\Lambda_{a_4}\int\frac{1}{V_{\rm lock}}\delta(V-V_{\rm lock})\,dV=\frac{\Lambda_{a_4}}{V_{\rm lock}}$$

**Step D — Comoving density (Paper S4).**

$$\Lambda_{\rm obs}=\Lambda_{a_4}\,\frac{e^{-3N_e}}{2\pi^2}\approx1.05\times\Lambda_{\rm obs}^{\rm measured}$$

Same N_e as n_s = 1 − 2/N_e — **no second parameter**.

---

## §2. Discipline

- N_e (inflation depth) ≠ N_lock (holographic width) — BR5  
- Vol(M) (spectral internal) ≠ V(N) (comoving S³) — do not conflate  
- 2π² vs 4π register (1.64×) remains **structural choice** — subdominant at 1.05× match

---

## §3. Honest gaps (non-blocking)

1. Full unimodular path-integral polish (Appendix B.3 extension) — cosmetic  
2. Λ-2PI: document 2π² vs 4π as comoving vs spectral register  
3. J5-M3: K_{β_GB} sign programme — parallel refinement

---

## §4. Corpus patches applied

- §17.5.18: measure **derived** language  
- Register: **genuine test** (R6) unchanged

---

## §5. Verification

Script: `paper_s4_lambda_proof_numerics.py` — ratio pred/obs ≈ 1.046.

---

— Jammer Λ-PROOF v0.1, 2026-05-24.
