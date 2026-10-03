# Void / δw(z) attack route v0.1 (Impact #3)

**Stream:** Cursor scaffold → **Jammer primary** (DESI covariances)  
**Date:** 2026-05-23  
**Status:** **Template + diagnostic numerics** — tracer-weighted model **open**  
**Scripts:** `void_dw_z_diagnostics.py`, `lcdm_bao_void_bias.py`  
**Parent:** `Top_5_Impact_Attack_Index_v0_1_20260523.md` #3; `P_dS4_Observational_Anchor_v0_1`

---

## §1. Problem

NTE predicts $w_{\rm true}=-1$; low-$z$ $w_{\rm obs}>-1$ from **void-enhancement** of $H(x,N)=\alpha|\Phi|^2$ (§12.4). Homogeneous layer $\equiv\Lambda$CDM (Gate #2). **Discrimination** requires §17.5.12 diagnostics (a)–(d), not global $\chi^2$.

---

## §2. Phenomenological template (Cursor v0.1)

Volume-weighting bias on inferred Hubble parameter:

$$\delta H(z)/H_{\rm hom}(z) = b\,\frac{\sigma_8^2(z)}{\sigma_8^2(0)}\,\frac{\Omega_\Lambda(z)}{\Omega_\Lambda(0)} \quad (z < z_{\rm cut})$$

with $z_{\rm cut}\approx0.85$ (structure-formation crossover; **not fitted** — Jammer to derive).

**Effective $w$ proxy** (exploratory):

$$w_{\rm eff}(z) - 1 \approx -\frac{2}{3}\,\frac{\delta H}{H}\,\frac{\Omega_m(z)}{\Omega_m(z)+\Omega_\Lambda(z)}$$

**Register:** template for **diagnostic (b)** only — not a derived $w(z)$ from action.

---

## §3. Diagnostic programme

| ID | Test | Cursor v0.1 | Jammer |
|----|------|-------------|--------|
| **(a)** | $w$ bias $\propto$ void fraction LOS | — | Tracer map + DESI |
| **(b)** | Bias $\downarrow$ with $z$; tracks $\sigma_8^2/\Omega_\Lambda$ | **Script** | Refine $b$, $z_{\rm cut}$ |
| **(c)** | Vanishes under CV / volume-weighting fix | — | LSST-era |
| **(d)** | CMB $\kappa$ unchanged | P-dS4 / Planck 0.83$\sigma$ | Gate #6 extraction |

**Falsifier:** constant $w\neq-1$ across $z$ **without** (a)–(d) pattern.

---

## §4. BAO reconciliation (illustrative)

From `lcdm_bao_void_bias.py` ($b=0.055$, **not fitted**):

| Tracer | $z$ | Hom $\Delta/\sigma$ | Void $\Delta/\sigma$ |
|--------|-----|---------------------|----------------------|
| LRG2 | 0.71 | **+2.6** | **+0.2** |

**Reading:** void template **directionally** reconciles worst homogeneous BAO overshoot — **illustrative only**; Jammer must joint-fit with covariances.

**Growth (P3):** homogeneous $f\sigma_8$ at $z=0.71$ is **+0.2$\sigma$** — BAO bias does **not** require parallel growth crisis.

---

## §5. DESI / high-$z$ anchor

- §20.7(c): DESI hints $w>-1$ **low-$z$ only** — directional match  
- Template: $\delta H\to0$ as $z\to z_{\rm cut}$ → $w_{\rm eff}\to-1$  
- **Do not claim** NTE fits DESI BAO or $w_0w_a$

---

## §6. Attack routes

| Route | Content | Owner |
|-------|---------|-------|
| **V1** | Tracer-weighted void fraction → $\delta H(z)$ | Jammer |
| **V2** | Joint BAO ($D_M,D_H$) with DESI $r\approx-0.44$ | Jammer |
| **V3** | $w_0w_a$ exploratory (Greg gate) | Jammer |
| **V4** | CMB $\kappa$ extraction (diagnostic d) | Jammer Gate #6 |

---

## §7. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| V-d1 | This route + `void_dw_z_diagnostics.py` | **Done v0.1** |
| V-d2 | Replace $b=0.055$ with derived amplitude | Jammer |
| V-d3 | Diagnostics (a)–(c) evidence table | Jammer |
| V-d4 | CMB $\kappa$ numerics | Jammer |

---

## §8. Discipline

- No global $\chi^2$ beat of $\Lambda$CDM  
- No "NTE fits DESI"  
- $w_{\rm true}=-1$ always

---

## §9. Cross-references

- `LCDM_Void_Bias_BAO_Worksheet_v0_1`, `LCDM_Growth_Sigma8_Worksheet_v0_2`  
- §17.5.12 Category G; Part 2 §12.4, §13.3

— Cursor void/δw v0.1, 2026-05-23.
