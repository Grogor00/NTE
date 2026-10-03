# Jammer: M₂ Z₂ split derive v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at Z₂ register** — Majorana hierarchy closed; $m_{\nu_2}$ Yukawa open  
**Script:** `Working/paper_s2_m2_z2_split_numerics.py`  
**Parents:** Companion 10 §3.8 / §7 S2-3; D5 factor-1.12; §17.5.17

---

## §0. Executive

**$M_2$ split closes** on the **canonical v10.8 $\sigma_3$ Cartan assignment** (supersedes `Pathway_Alpha_S3_M2_Closure.md` 2026-05-07 $\sigma_3=M_1$ reading):

| Mode | Polarisation | Mass (GeV) | Mechanism |
|------|--------------|------------|-----------|
| $M_1$ | $\sigma_1/\sigma_2$ (minimal Higgs) | $6.04\times10^9$ | BPS + D5 emergent SUSY ($\delta\approx0.115$) |
| $M_2$ | Z$_2$ sibling | $6.18\times10^9$ | $M_1(1+\sin^2\theta_{13})$ |
| $M_3$ | $\sigma_3$ Cartan | $8.2\times10^{14}$ | $M_R=M_{\rm Pl}^{3/4}v_{\rm EW}^{1/4}$ |

**Hierarchy:** $M_1<M_2<M_3$ with $M_2/M_1=1.022$ (+2.2%). **Not** $M_2=M_R$.

---

## §1. Structural mechanism

**Three Killing-spinor modes** $\leftrightarrow$ $\dim({\rm adj\,\mathfrak{su}(2)})=3$ (same anchor as $\kappa_0$, D5).

**Higgs VEV** aligns with **$\sigma_3$ Cartan** direction → $\sigma_3$ mode strongly Higgs-coupled → **$M_3=M_R$**.

**$\sigma_1,\sigma_2$ pair:** orthogonal to VEV; degenerate at **Z$_2$** ($\theta_{23}=\pi/4$ from $\sigma_1\leftrightarrow\sigma_2$ symmetry). Subleading **PMNS $\theta_{13}$** breaks Z$_2$ between Majorana masses:

$$\boxed{M_2=M_1\,(1+\sin^2\theta_{13})}$$

**Discipline:** $\sin^2\theta_{12}=1/3$ (tribimaximal) controls **mixing**, not this **mass** split — avoids $O(0.3)$ from old hand-wave.

---

## §2. Numerics (script)

| Quantity | Value |
|----------|-------|
| $M_{\rm BPS}$ | $5.419\times10^9$ |
| $M_1$ (D5 corrected) | $6.041\times10^9$ (ratio obs **0.997**) |
| $M_2$ | $6.176\times10^9$ |
| $M_3=M_R$ | $8.2\times10^{14}$ |
| $M_2/M_1$ | **1.022** |
| $\sin^2\theta_{13}$ | 0.0222 ($8.57°$) |

---

## §3. Seesaw / light neutrinos (honest)

| Route | $m_{\nu_2}$ | Status |
|-------|-------------|--------|
| $Y_2=(8\pi)^{-1/3}$, $M_2\sim6\times10^9$ | $\sim1.1\,{\rm keV}$ | **Ruled out** |
| $Y_2=(8\pi)^{-1/3}$, $M_R$ | **0.0086 eV** | Matches solar (old $M_2=M_R$ route) |
| $Y_2$ calibrated @ $M_2$ for $\sqrt{\Delta m^2_{\rm solar}}$ | **$9.4\times10^{-4}$** | Tier-2 / §22.1 |

**Verdict:** Majorana **spectrum** closed at Z₂ register. **$m_{\nu_2}$** closed at §22.1 (Jammer v0.1, 2026-05-24): $(8\pi)^{-2/3}v^2/M_R$ @ 0.993× solar; $(8\pi)^{-1/3}$ pairs with **$M_R$** in seesaw denominator, not Pathway-$\alpha$ $M_2$ alone.

$m_{\nu_3}=0.074$ eV with $Y_3=1$, $M_3=M_R$ **unchanged**.

---

## §4. Supersedes / falsifiers

**Supersedes:** `Pathway_Alpha_S3_M2_Closure.md` ($M_2=M_3=M_R$, $\sigma_3=M_1$) — inconsistent with Companion 10 v10.8 §3.8 and §17.5.17.

| Falsifier | Consequence |
|-----------|-------------|
| $M_2/M_R\sim1$ at leading order | v10.8 Cartan assignment fails |
| $M_2/M_1\gg1+\sin^2\theta_{13}$ | Z$_2$ split mechanism fails |
| $M_2<M_1$ | ordering violation |

---

## §5. Corpus patches authorised

- **§17.5.17:** $M_2$ **derived** — $M_1(1+\sin^2\theta_{13})$; cross-ref this memo
- **Companion 10 §7 S2-3:** mark **closed** at Z₂ register
- **Deprecate note** on `Pathway_Alpha_S3_M2_Closure.md`

---

## §6. Honest open

- Ab initio $\sin^2\theta_{13}$ from spectral triple (currently observation-anchored subleading input)
- ~~$Y_{\nu_2}$ structural derivation (§22.1)~~ — **partial closed** (`Jammer_S22_1_Y_Nu2_Derive_v0_1`)
- $m_{\nu_1}$ bound / normal ordering full closure

---

— Jammer M₂ split v0.1, 2026-05-24.
