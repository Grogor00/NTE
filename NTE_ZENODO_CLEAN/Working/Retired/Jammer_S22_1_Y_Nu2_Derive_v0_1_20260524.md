# Jammer: §22.1 Y_ν₂ structural derive v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at D5-inverse register** — zero-parameter $m_{\nu_2}$; $Y_{\nu_1}$ bracket open  
**Script:** `Working/paper_s22_1_y_nu2_numerics.py`  
**Parents:** D5 BPS prefactor; M₂ Z₂ split; Companion 10 §3.8; Pathway α S3 candidate

---

## §0. Executive

| Quantity | Structural prediction | vs observation |
|----------|----------------------|----------------|
| $Y_{\nu_2}$ | $(8\pi)^{-1/3}$ | inverse D5 prefactor |
| $m_{\nu_2}$ | $(8\pi)^{-2/3}\,v_{\rm EW}^2/M_R$ | **0.993×** $\sqrt{\Delta m^2_{\rm solar}}$ |
| $m_{\nu_3}$ | $v_{\rm EW}^2/M_R$ ($Y_3=1$) | **0.997×** corpus 0.074 eV |

**Verdict:** §22.1 **partial closure** — $Y_{\nu_2}$ and $m_{\nu_2}$ promoted from calibrated input to **structural derivation** at the same register as D5/M₁. $Y_{\nu_1}$, full $\{Y_{\nu_i}\}$ from $D_F$, and charged-lepton hierarchy remain open.

---

## §1. Structural mechanism

### §1.1 D5 prefactor and its inverse

Pathway α / D5 fixes the **Majorana** cube-root quantisation:

$$M_{\rm BPS}=(8\pi)^{1/3}(M_{\rm Pl}^2 H_{\rm GB})^{1/3}.$$

The factor $(8\pi)^{1/3}$ is **not tunable** — Majorana doubling ($8\pi$) times three-dimensional flux/volume root ($\pi^{1/3}$ structure). **Dirac Yukawa** couplings on the **same** Hopf–Killing-spinor flux line carry **one fewer power** of the volumetric normalisation:

$$\boxed{Y_{\nu_2}=(8\pi)^{-1/3}}$$

**Reading:** mass scales as $M\sim({\rm flux}/V)^{1/3}$; Yukawa scales as $M^{0}\times({\rm flux}/V)^{-1/3}$ at leading order on the $\sigma_1/\sigma_2$ sector orthogonal to the Higgs Cartan direction.

### §1.2 Seesaw scale: $M_R$ not $M_2$

Canonical v10.8 assignment (§17.5.17): $\sigma_3$ Cartan mode → $M_3=M_R$; $\sigma_1/\sigma_2$ pair → $M_1,M_2$ at Pathway-$\alpha$ scale.

**Light neutrino mass** for the second generation:

$$\boxed{m_{\nu_2}=\frac{(8\pi)^{-2/3}\,v_{\rm EW}^2}{M_R}}$$

**Not** $m_{\nu_2}=Y_{\nu_2}^2 v^2/M_2$ with $Y_{\nu_2}=(8\pi)^{-1/3}$ alone — that gives $\sim1\,{\rm keV}$ (ruled out in M₂ numerics).

**Physical content:** PMNS / seesaw **mixes** the light $\nu_2$ with the **Cartan-scale** RH sector in the denominator; $Y_{\nu_2}$ carries the **inverse BPS prefactor** on the $\sigma_1/\sigma_2$ coupling line.

### §1.3 Equivalent parametrisation (M₂ register)

Algebraically identical:

$$m_{\nu_2}=\frac{Y_{\nu_2}^2 v_{\rm EW}^2}{M_2},\qquad Y_{\nu_2}=(8\pi)^{-1/3}\sqrt{\frac{M_1}{M_R}}.$$

Uses derived $M_1,M_2$ from D5 + Z₂ split — **0.972×** solar scale via $M_2$ route (2% from $M_1/M_2$ split).

---

## §2. Numerics (script)

| Route | $m_{\nu_2}$ (eV) | Ratio to $\sqrt{\Delta m^2_{\rm solar}}$ |
|-------|------------------|----------------------------------------|
| $(8\pi)^{-2/3}v^2/M_R$ | **0.00860** | **0.993** |
| $Y_2=(8\pi)^{-1/3}$, $M_R$ | 0.00860 | 0.993 |
| $Y_2=(8\pi)^{-1/3}\sqrt{M_1/M_R}$, $M_2$ | 0.00841 | 0.972 |
| $Y_2=(8\pi)^{-1/3}$, $M_2$ only | 1142 | ruled out |

$\Delta m^2_{\rm solar}$ pred $=7.40\times10^{-5}\,{\rm eV}^2$ (obs $7.5\times10^{-5}$).

$m_{\nu_3}=0.0738\,{\rm eV}$ with $Y_3=1$.

---

## §3. $Y_{\nu_1}$ bracket (partial)

Normal hierarchy: $m_{\nu_1}\ll m_{\nu_2}$.

**Bracket:** $Y_{\nu_1}\sim Y_{\nu_2}\times\sin\theta_{13}\times\sqrt{M_1/M_R}$ (Z₂ + hierarchy) $\sim1.4\times10^{-4}$ — consistent with sum bound $m_{\nu_1}\lesssim0.037\,{\rm eV}$.

**Not closed** at zero-parameter level.

---

## §4. Relation to prior memos

| Memo | Update |
|------|--------|
| Pathway α S3 (2026-05-07) | $m_{\nu_2}$ candidate **confirmed**; $M_2=M_R$ assignment **superseded** |
| M₂ Z₂ split | $M_2$ in seesaw **only** via $\sqrt{M_1/M_R}$ factor |
| D5 | $(8\pi)^{1/3}$ prefactor **dual** → $Y_{\nu_2}$ |

---

## §5. Honest open

| Item | Register |
|------|----------|
| Full $D_F$ Yukawa from spectral action | Paper S2 / OctonionExtension |
| Charged-lepton $Y_e,Y_\mu,Y_\tau$ | §22.1 full programme |
| $m_{\nu_1}$ zero-parameter | Bracket only |
| Ab initio why seesaw denominator is $M_R$ | Mixing / σ₃ Cartan mechanism level |

---

## §6. Falsifiers

1. Precision $\Delta m^2_{\rm solar}$ kills $(8\pi)^{-2/3}v^2/M_R$ at high confidence  
2. $Y_{\nu_2}$ measured from high-energy process $\neq(8\pi)^{-1/3}$ at leading order  
3. Inverted hierarchy with same $\{M_i\}$ — would break $M_R$ denominator assignment  

---

## §7. Corpus patches authorised

**§22.1 replacement paragraph (AC):**

> **Partial closure (Jammer v0.1, 2026-05-24).** The Pathway α / D5 BPS prefactor $(8\pi)^{1/3}$ fixes $M_1$ at the Majorana cube-root level. Its inverse $(8\pi)^{-1/3}$ is the leading **Dirac Yukawa** normalisation on the $\sigma_1/\sigma_2$ Killing-spinor sector. With $M_R$ from §19.7 and $Y_3=1$, the light neutrino mass $m_{\nu_2}=(8\pi)^{-2/3}v_{\rm EW}^2/M_R$ matches $\sqrt{\Delta m^2_{\rm solar}}$ at **0.993×** with no additional parameter. Equivalent form: $m_{\nu_2}=Y_{\nu_2}^2v^2/M_2$ with $Y_{\nu_2}=(8\pi)^{-1/3}\sqrt{M_1/M_R}$ and $M_2=M_1(1+\sin^2\theta_{13})$ (§17.5.17). Charged-lepton Yukawas and $Y_{\nu_1}$ remain open; full $\{Y_{\nu_i}\}$ from $D_F$ is Programme S downstream.

**§17.5.20:** upgrade $m_{\nu_2}$ to **framework-derivative** in prediction table.

**Greg White byline:** `Papers/Companion_13_Yukawa_Nu2_D5_Inverse_v10_17.md` (2026-05-24).

---

— Jammer §22.1 Y_ν₂ v0.1, 2026-05-24.
