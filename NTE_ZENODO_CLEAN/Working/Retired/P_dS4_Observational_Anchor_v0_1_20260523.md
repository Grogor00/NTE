# P-dS4 — observational anchor: CMB κ + high-z $w\to -1$ v0.1 (§22.8 / §17.5.12)

**Stream:** Cursor scaffold → Jammer numerics / DESI–Euclid era  
**Date:** 2026-05-23  
**Status:** **Partial** — falsifier catalogue wired; homogeneous checks done; **inhomogeneous void diagnostics open**  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-dS4  
**Related:** `LCDM_CMB_Kappa_Test_Worksheet_v0_1`, `LCDM_Void_Bias_BAO_Worksheet_v0_1`, `LCDM_Growth_Sigma8_Worksheet_v0_2`

---

## §1. Mission

Supply an **empirical boundary** on the dS / dark-energy sector (§22.8) **without** full de Sitter QG proof (P-dS1–3):

> NTE predicts **$w_{\rm true}=-1$ exactly**; apparent $w>-1$ at low $z$ is **void-enhancement bias** that must **vanish at high $z$** and **not** contaminate CMB-era $\kappa$.

P-dS4 packages §17.5.12 Category G diagnostics as the **observational programme** parallel to operator-algebra work (P-dS3).

**Honest register:** this is **falsifiability wiring**, not a claim that NTE beats $\Lambda$CDM on a global $\chi^2$ (homogeneous layer $\equiv \Lambda$CDM per Gate #2 / P3 v0.2).

---

## §2. Two anchors

| Anchor | Prediction | Current data | Status |
|--------|------------|--------------|--------|
| **A — CMB $\kappa$** | $\kappa=5.50\pm0$ at $z\sim1100$ (no void bias) | Planck: $\kappa_{\rm obs}=5.38\pm0.15$ (**0.83$\sigma$**) | **Within 1$\sigma$**; Jammer extraction TBD |
| **B — high-$z$ $w$** | $w_{\rm obs}(z)\to -1$ as $z$ increases | DESI hints $w>-1$ low-$z$ only (§20.7(c)) | **Directional match**; amplitude/diagnostics open |

**Discriminant (diagnostic d):** if low-$z$ BAO/$w$ bias appears but CMB $\kappa$ shifts the same way → **falsifies** void-enhancement reading.

---

## §3. Four $w$ diagnostics (§17.5.12 / Part 2 §12.4)

| ID | Test | Data programme | Cursor/Jammer |
|----|------|----------------|---------------|
| **(a)** | $w$ departure $\propto$ void fraction along LOS | DESI DR3+, Euclid | Jammer — `LCDM_Void_Bias_BAO_Worksheet_v0_1` |
| **(b)** | Departure $\downarrow$ with $z$, tracks $\sigma_8^2(z)/\Omega_\Lambda(z)$ | Same + growth | Partial — P3 hom $\equiv \Lambda$CDM |
| **(c)** | Departure vanishes under cosmic-variance / volume-weighting fix | LSST era | **Open** |
| **(d)** | CMB $\kappa$ at $z\sim1100$ **unchanged** by void bias | Planck → CMB-S4 | Scaffold — Gate #6 Jammer primary |

**Falsifier:** persistent $w\neq -1$ **without** (a)–(d) pattern → NTE dark-energy reading fails.

---

## §4. CMB $\kappa$ programme (Anchor A)

**Why homogeneous epoch matters:** $\delta\rho/\rho\sim10^{-5}$ at recombination → void structure absent → $\kappa$ is **clean zero-parameter test** of mirror-gravity amplitude.

| Step | Owner | Status |
|------|-------|--------|
| Define $\kappa$ extraction (peak ratios / $\Omega$'s) | Jammer | Open |
| Compare to $5.50$; CMB-S4 band $[5.27,5.73]$ | Jammer | Milestone mid-2030s |
| Document $\Omega_m$ degeneracy | Jammer | Partial |
| Void bias negligible at $z\sim1100$ | Corpus prose | **Closed** (Part 2 §13.3) |

**Current tension:** $0.83\sigma$ — **not a corpus tension** at present precision; tightens at CMB-S4.

---

## §5. High-$z$ $w$ programme (Anchor B)

**NTE stack:** $w_{\rm true}=-1$ from $\Omega_\Lambda$ as geometric unloading (§12.4); inhomogeneous $| \Phi(x)|$ mimics dynamical DE in biased estimators.

| Layer | Work | Status |
|-------|------|--------|
| Homogeneous | `lcdm_growth_numerics.py` P3 v0.2 | **Done** — matches $\Lambda$CDM |
| $\rho_{\rm eff}$ vs $\rho_{\rm total}$ | `lcdm_vnte_rho_eff_numerics.py` D1 | **Done** — confirms Gate #2 (bookkeeping chart) |
| Inhomogeneous void + BAO | Jammer primary | **Open** |
| $\delta w(z)$ profile vs DESI | §17.5.12 research target (iv) | **Open** |

**DESI (2026):** low-$z$ $w>-1$ hint — **consistent with sign** of void reading; **not** closure.

---

## §6. Relation to P-dS1–3

| Programme | Role |
|-----------|------|
| P-dS1/2 | $N_{\rm lock}=S_{\rm dS}/4$, $H_{\rm GB}^{(F)}$ — **internal** |
| P-dS3 | Modular $\beta_{\rm dS}=2\pi/H$ — **algebraic** |
| **P-dS4** | **Observational** boundary: universe looks like $\Lambda$CDM + fixed $\kappa$ at CMB; $w\to-1$ at high $z$ |

No claim that P-dS4 **derives** GH entropy — only that **late-time / CMB data** must stay compatible with $w=-1$ + $\kappa=5.50$ story.

---

## §7. What P-dS4 does NOT claim

- Global $\chi^2$ superiority over $\Lambda$CDM (explicitly deferred — inhom layer)  
- CMB-S4 / DESI **numerical closure** (Jammer)  
- Full dS/CFT or TT (P-dS3 / P0.10)  
- $H_{\rm GB}^{(\alpha)}\leftrightarrow H_{\rm GB}^{(F)}$ bridge

---

## §8. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| P-dS4a | This anchor card | **Done v0.1** |
| P-dS4b | CMB $\kappa$ Jammer numerics | Open (scaffold exists) |
| P-dS4c | Void / $\delta w(z)$ vs DESI | Open |
| P-dS4d | Diagnostic (a)–(c) evidence table | Open |

---

## §9. Cross-references

- §17.5.12 Category A ($\kappa$, $n_s$, $w$) + Category G  
- §17.5.9 ΛCDM reduction; Greg Gate #2 ratification  
- `LCDM_Reduction_Appendix_Scaffold_v0_6` P5 routing  
- P-dS1–3 worksheets; §22.8 pathway

— Cursor P-dS4 v0.1, 2026-05-23.
