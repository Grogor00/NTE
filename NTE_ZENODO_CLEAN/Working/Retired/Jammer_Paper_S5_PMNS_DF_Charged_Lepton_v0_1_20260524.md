# Jammer: Paper S5 — PMNS-embedded $D_F$ charged lepton v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **STRUCTURAL DERIVATION + NEGATIVE RESULT** on PMNS alone; **bracket** on off-diagonal $D_F$  
**Parents:** `Jammer_S22_1f_DF_Heat_Kernel_Delta_L4_v0_1`; §19.1; §19.4; S2-C-C  
**Script:** `Working/paper_s22_1h_pmns_df_delta_numerics.py`

---

## §0. Executive

| Item | v0.1 |
|------|------|
| $Y=U\,\mathrm{diag}(y_{\rm geom})\,U^\dagger$ | **Spectrum invariant** — PMNS alone does **not** split $\delta_n$ |
| Off-diagonal $D_F$ | $Y_{ab}=\eta\,\mathcal{O}_{ab}Y_a/(16\pi^2)$ ($a\neq b$) — **required** |
| HK-A $r=3$ | $m_{\tau}/m_{\mu}\approx16$ (**obs 17**) — **bracket match** |
| HK-A $r=3$ | $m_{\mu}/m_{e}\approx6$ (**obs 207**) — **still open** |
| **Verdict** | S5 closes **logic** of embedding; charged Yukawas **not** promoted to partial closure |

---

## §1. Canonical embedding

### §1.1 $D_F$ block (S2-C-C)

Charged sector: $M_e=v_{\rm EW}Y_e$ (3×3). PMNS $U$ from §19.1 ($\theta_{23}=\pi/4$, $\sin^2\theta_{12}=1/3$, $\sin^2\theta_{13}=0.022$).

### §1.2 Geometric Yukawa **before** EWSB

Diagonal in **generation** ($\sigma$/Killing index $g$):

$$Y_g^{\rm geom}=(8\pi)^{-\delta_g^{\rm HK}},\qquad
\mathcal{S}_g=\frac{d_0}{d_g}\left(\frac{3/2}{g+3/2}\right)^{2r}.$$

### §1.3 Off-diagonal heat-kernel couplings (new)

Cross-terms in $(D_F^2)_{ab}$ from §19.4 overlaps:

$$\boxed{Y_{ab}=\frac{\eta}{16\pi^2}\,\mathcal{O}_{ab}\,\sqrt{\mathcal{S}_a\mathcal{S}_b}\,Y_a^{\rm geom}},
\quad a\neq b,\qquad Y_{aa}=Y_a^{\rm geom}}.$$

Hermitian symmetrisation optional ($Y_{ab}=Y_{ba}$); v0.1 uses row insertion above.

**PMNS map:** $Y_e^{(\rm flav)}=U\,Y^{\rm geom}\,U^\dagger$ — only affects eigenvalues when $Y^{\rm geom}$ is **not** diagonal.

---

## §2. Key theorem (S5 v0.1)

If $Y^{\rm geom}=\mathrm{diag}(y_0,y_1,y_2)$ and $U$ is unitary, then eigenvalues of $U Y^{\rm geom} U^\dagger$ are $\{y_0,y_1,y_2\}$.

**Corollary:** L4 + PMNS **without** off-diagonal $D_F$ cannot improve $m_\mu/m_e$. Falsifies route “rotate only.”

---

## §3. Numerics

Run: `python paper_s22_1h_pmns_df_delta_numerics.py`

| Model | $m_{\tau}/m_{\mu}$ | $m_{\mu}/m_{e}$ |
|-------|-------------------|-----------------|
| HK-A $r=2$ | ~8 | ~4 |
| HK-A $r=3$ | **~16** | ~6 |
| + off-diag $\eta\in[1,40]$ | ~8–16 ($r=2$) | **unchanged** (~4) |

**Interpretation.**

- **$\tau/\mu$:** raising $r$ in $\mathcal{O}^{2r}$ (associator depth) lands at **obs order** for $r=3$.
- **$\mu/e$:** needs **cumulative** suppression (product of $\mathcal{S}_k$ along generation stack) or $\mathrm{Tr}_F(D_F^4)$ weighting — **bracket only** in v0.1:

$$\mathcal{S}_e^{\rm cum}=\prod_{k=0}^{2}\mathcal{S}_k
\Rightarrow \delta_e^{\rm cum}\approx1.5\;(r=2),\ \text{still below obs }\sim4.$$

---

## §4. Cumulative-depth bracket (Paper S5b programme)

$$\delta_n^{\rm cum}=\frac{2}{3}-\frac{1}{3\ln(8\pi)}\ln\prod_{k=0}^{n}\mathcal{S}_k$$

| $n$ | $r=2$ $\delta^{\rm cum}$ | obs guide |
|-----|--------------------------|-----------|
| $\tau$ | 0.67 | 1.42 |
| $\mu$ | ~0.9 | 2.30 |
| $e$ | ~1.5 | 3.95 |

**Not closed** — motivates **$\mathrm{Tr}_F(D_F^4)$** insertion (S2-C-C $\Delta a_4\propto\mathrm{Tr}(D_F^4)$) as next geometric amplifier.

---

## §5. Corpus patch

> **Paper S5 (Jammer v0.1, 2026-05-24):** PMNS embeds in $D_F$ but **does not** split $Y_e,Y_\mu,Y_\tau$ without off-diagonal heat-kernel couplings; $r=3$ HK bracket matches $m_{\tau}/m_{\mu}$; $m_{\mu}/m_{e}$ open (`Jammer_Paper_S5_PMNS_DF_Charged_Lepton_v0_1`).

---

## §6. Next

1. **S5b:** $\mathrm{Tr}_F(D_F^4)$ weight on per-generation $\mathcal{S}_n$ (link §22.23 $\Delta a_4^{D_F}$).
2. **Threshold / L1** composite after depths fixed.
3. Greg-byline **Companion 14** (optional) if promoted.

---

— Jammer Paper S5 v0.1, 2026-05-24.
