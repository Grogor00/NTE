# Jammer: §22.1b $Y_{\nu_1}$ bracket derive v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **BRACKET** (Tier-2 structural) — not zero-parameter closure  
**Script:** `Working/paper_s22_1b_y_nu1_bracket_numerics.py`  
**Parents:** `Jammer_S22_1_Y_Nu2_Derive_v0_1`; Companion 13; M₂ Z₂ split; Companion 7 σ-modes

---

## §0. Executive

| Quantity | Bracket prediction | vs observation |
|----------|-------------------|----------------|
| $Y_{\nu_1}$ | $(8\pi)^{-1/3}\sin\theta_{13}\sqrt{M_1/M_R}$ | **structural** |
| $m_{\nu_1}$ | $Y_1^2 v^2/M_R$ | **$\sim10^{-3}$ eV** — consistent with $m_1\lesssim0.037$ eV bound |

**Verdict:** §22.1 **advances** from “$Y_{\nu_1}$ open” to **bracketed** normal hierarchy. Charged-lepton Yukawas remain open.

---

## §1. Mechanism (Z₂ + PMNS subleading)

Companion 7 / §17.5.17:

- $\nu_1$ ↔ $\sigma_1$ mode; $\nu_2$ ↔ $\sigma_2$; $\nu_3$ ↔ $\sigma_3$ (Cartan).  
- M₂ Z₂ split: $M_2=M_1(1+\sin^2\theta_{13})$ — $\theta_{13}$ enters **Majorana** spectrum.  
- **Bracket:** PMNS $\theta_{13}$ also suppresses $\nu_1$ **Dirac** line relative to $\nu_2$ on the same D5-inverse flux class.

$$\boxed{Y_{\nu_1}=(8\pi)^{-1/3}\,\sin\theta_{13}\,\sqrt{\frac{M_1}{M_R}}}$$

**Seesaw** ($M_1$ from Z₂ split; cancels $\sqrt{M_1/M_R}$ in $Y_1$):

$$\boxed{m_{\nu_1}=\frac{(8\pi)^{-2/3}\,\sin^2\theta_{13}\,v_{\rm EW}^2}{M_R}=m_{\nu_2}\,\sin^2\theta_{13}}$$

Equivalent: $m_{\nu_1}=Y_1^2 v^2/M_1$ with $Y_1$ as above.

---

## §2. Numerics

| Route | $m_{\nu_1}$ (eV) |
|-------|------------------|
| $Y_1^2 v^2/M_1$ (canonical bracket) | **$\sim1.9\times10^{-4}$** |
| $m_{\nu_2}\sin^2\theta_{13}$ (mass-ratio) | **$\sim1.9\times10^{-4}$** |
| Cosmological bound | $m_1\lesssim0.037$ eV — **PASS** |

$m_{\nu_2}=0.0086$ eV (0.993× solar) — anchor unchanged.

**Not claimed:** match to future precision $m_{\nu_1}$ or $\Delta m^2_{21}$ without full $D_F$ derivation.

---

## §3. Honest tier

| Item | Register |
|------|----------|
| $Y_{\nu_2}$, $m_{\nu_2}$ | **Derived** (Companion 13) |
| $Y_{\nu_1}$, $m_{\nu_1}$ | **Bracket** (θ₁₃ + Z₂ structure) |
| $Y_e,Y_\mu,Y_\tau$ | **Open** |

Inventory Claim 13 analogue for $\nu_1$: **Tier B bracket**, not B+ genuine test.

---

## §4. Corpus patch (§22.1 addendum)

> **$Y_{\nu_1}$ bracket (Jammer v0.1, 2026-05-24).** $Y_{\nu_1}=(8\pi)^{-1/3}\sin\theta_{13}\sqrt{M_1/M_R}$; $m_{\nu_1}=m_{\nu_2}\sin^2\theta_{13}\sim2\times10^{-4}$ eV (seesaw $M_1$). Normal hierarchy; $m_1\ll0.037$ eV. Bracket only — not zero-parameter closure.

---

— Jammer §22.1b v0.1, 2026-05-24.
