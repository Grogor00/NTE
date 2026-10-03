# Jammer: §22.1c $m_{\nu_1}$ zero-parameter derive v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **ZERO-PARAMETER** (solar splitting register) — upgrades §22.1b bracket  
**Script:** `Working/paper_s22_1c_y_nu1_zero_param_numerics.py`  
**Parents:** `Jammer_S22_1b_Y_Nu1_Bracket_Derive_v0_1`; `Jammer_S22_1_Y_Nu2_Derive_v0_1`; Companion 13

---

## §0. Executive

| Quantity | v0.1b (bracket) | v0.1c (this memo) |
|----------|-----------------|-------------------|
| $Y_{\nu_1}$ | Structural bracket | **Derived** from $Y_{\nu_2}$, $\theta_{13}$, $M_1/M_R$ |
| $m_{\nu_1}$ | $m_{\nu_2}\sin^2\theta_{13}$ | **Same** — now **zero-parameter** (no new Yukawa constant) |

$$\boxed{m_{\nu_1}=\frac{(8\pi)^{-2/3}\sin^2\theta_{13}\,v_{\rm EW}^2}{M_R}=m_{\nu_2}\,\sin^2\theta_{13}}$$

Uses **only** inputs already committed for $m_{\nu_2}$: $(8\pi)^{-2/3}$, $v_{\rm EW}$, $M_R$, PMNS $\theta_{13}$, M₂ Z₂ sector.

---

## §1. Mechanism

1. **$m_{\nu_2}$** closed: $m_{\nu_2}=(8\pi)^{-2/3}v^2/M_R$ (Companion 13).  
2. **M₂ Z₂:** $\theta_{13}$ enters Majorana split and PMNS subleading line.  
3. **Normal hierarchy:** lightest mass set by **solar-scale splitting** — $\Delta m^2_{21}\approx m_2^2\sin^2\theta_{13}$ at leading PMNS geometry when $m_1\ll m_2$.

**Equivalent Yukawa (if needed):**

$$Y_{\nu_1}=(8\pi)^{-1/3}\sin\theta_{13}\sqrt{M_1/M_R},\qquad m_{\nu_1}=\frac{Y_{\nu_1}^2 v^2}{M_1}=m_{\nu_2}\sin^2\theta_{13}.$$

---

## §2. Numerics

| Quantity | Value |
|----------|-------|
| $m_{\nu_2}$ | 0.00860 eV |
| $m_{\nu_1}$ pred | **$\sim1.9\times10^{-4}$ eV** |
| $\sqrt{\Delta m^2_{21}}$ obs | $\sim8.6\times10^{-3}$ eV |
| Ratio $m_1/m_2$ | $\sin^2\theta_{13}\approx0.022$ |

**Honest tier:** $m_{\nu_1}$ is **zero-parameter** given $m_{\nu_2}$ + $\theta_{13}$ — **not** a separate genuine test of $\Delta m^2_{21}$ (would need full $D_F$ + PMNS derivation). Register as **characterisation / structural** in §17.5.20 unless Greg promotes.

**Not claimed:** precision fit to future $m_{\nu_1}$ mass measurements.

---

## §3. Corpus patch (§22.1)

Add after $Y_{\nu_1}$ bracket sentence:

> **$m_{\nu_1}$ zero-parameter (Jammer v0.1c, 2026-05-24):** $m_{\nu_1}=m_{\nu_2}\sin^2\theta_{13}=(8\pi)^{-2/3}\sin^2\theta_{13}\,v^2/M_R\sim1.9\times10^{-4}$ eV — no additional Yukawa constant beyond $\nu_2$ sector.

---

— Jammer §22.1c v0.1, 2026-05-24.
