# Jammer: §22.1e charged-lepton embedding depth L2 v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **STRUCTURAL BRACKET** — sector split derived; generation depths open  
**Parent:** `Jammer_S22_1d_Charged_Lepton_Yukawa_Attack_Route_v0_1`  
**Script:** `Working/paper_s22_1f_embedding_depth_numerics.py`  
**Corpus:** §19.3–§19.4; §17.5.17; Companion 13 D5 inverse

---

## §0. Executive

| Item | Register | v0.1e |
|------|----------|-------|
| Neutrino Dirac $Y_{\nu_2}$ | **Derived** | $\delta_\nu=\tfrac13$ → $(8\pi)^{-1/3}$ |
| Charged-lepton **sector** | **Structural bracket** | $\delta_{\rm singlet}=\tfrac23$ base |
| $\delta_e,\delta_\mu,\delta_\tau$ | **Bracket / fit** | see §3 |
| F2 ($Y_e=Y_{\nu_2}$) | Falsifier | **Not triggered** — $\delta_e\gg\delta_\nu$ |

**Headline.** L2 supplies the **missing volumetric power** between neutrino ($\sigma_1/\sigma_2$) and charged-lepton (**G₂ singlet**) lines. The **inter-generation hierarchy** is **not** closed by a single rational $\delta$; it needs the §19.4 overlap programme (or L4 $D_F$).

---

## §1. Ansatz

$$\boxed{Y_\ell \sim (8\pi)^{-\delta_\ell}}$$

Same Hopf–$S^3$ flux normalisation as D5 / Companion 13, with **embedding depth** $\delta_\ell$ set by representation + generation.

| Sector | $7_{G_2}$ piece | Coupling line | Leading $\delta$ |
|--------|-----------------|---------------|------------------|
| Majorana $M_1$ | BPS mass | flux$/V)^{1/3}$ | $(8\pi)^{+1/3}$ in $M$ |
| Dirac $\nu_2$ | $\sigma_1/\sigma_2$ | transverse to VEV | $\delta_\nu=\tfrac13$ |
| Charged $\ell$ | **singlet** | $\sigma_3$ / Higgs | $\delta_{\rm singlet}=\tfrac23$ |

**Why $\delta_{\rm singlet}=2/3$?** Dirac Yukawa carries one inverse cube-root volumetric factor ($\delta_\nu=1/3$). The G₂ **singlet** lacks the colour triplet fold ($N_c=3$) that enforces Georgi–Jarlskog $m_\ell/m_q=1/3$ at GUT; leading singlet counting adds **one more** inverse power on the same $(8\pi)$ line:

$$\delta_{\rm singlet}=\delta_\nu+\frac13=\frac23.$$

This is **structural counting**, not a fit. It sets $Y\sim(8\pi)^{-2/3}\approx0.12$ — still **too large** for $Y_e$; generation structure must suppress further.

---

## §2. Generation spacing (§19.4 programme)

Corpus overlap on $S^3$ Killing-spinor modes:

$$\mathcal{O}_{nm}=\frac{3/2}{n+m+3/2}.$$

**Bracket family** (lightest generation = largest depth):

$$\delta_\ell^{(g)}=\frac23+\frac{\alpha}{3}\,\mathcal{O}_{n(g),0}^{\,p},
\qquad n(e)=2,\;n(\mu)=1,\;n(\tau)=0,
\qquad p\in\{1,2\}.$$

- $p=1$, $\alpha=1$: **fails** $m_\mu/m_e$ (pred $\sim1.3$, obs $\sim207$).
- $p=2$, $\alpha=1$: **fails** (pred $\sim1.8$).
- **Single amplitude** $\alpha$ fit to $m_\mu/m_e$ alone needs $|\alpha|\sim30$ (wrong sign for $\tau/\mu$) — overlap **cannot** fit both ratios; radiative $1/(16\pi^2)$ tower (§19.4) or $D_F$ required.

**PMNS-bracket** ($\delta_\tau=\tfrac13$, step $\sin^2\theta_{13}$, $\sin^2\theta_{12}$): wrong hierarchy direction / magnitude.

---

## §3. Phenomenological depths (guide only)

From $Y_\ell=\sqrt{2}\,m_\ell/v_{\rm EW}$ and $Y_\ell=(8\pi)^{-\delta_\ell}$:

| $\delta$ | Value |
|----------|-------|
| $\delta_e$ | **~3.95** |
| $\delta_\mu$ | **~2.30** |
| $\delta_\tau$ | **~1.42** |
| $\delta_{\nu_2}$ | **0.333** |

Spacing: $\delta_e-\delta_\mu\approx1.65\leftrightarrow m_\mu/m_e$; $\delta_\mu-\delta_\tau\approx0.87\leftrightarrow m_\tau/m_\mu$.

**Discipline:** these are **targets for L4**, not postulates. Do not ship as zero-parameter predictions.

---

## §4. L1 × L2 hybrid

| Layer | Role |
|-------|------|
| **L2** | Sector normalisation $(8\pi)^{-\delta_\ell}$ |
| **L1** | G₂ colour $1/N_c$ at $M_{\rm GUT}$ |

Third generation: $\delta_\tau\approx\tfrac13$ is **compatible** with $\tau$–$b$ unification (L1 Test A $m_\tau/m_b\to1.53$ at 1-loop). First/second need **extra depth** beyond L1 — consistent with §3.

---

## §5. Falsifiers

| ID | Test | v0.1e |
|----|------|-------|
| F2 | $Y_e=(8\pi)^{-1/3}$ without split | **Not triggered** ($\delta_e\gg\tfrac13$) |
| F4 | $\delta_\tau=\delta_\nu$ **and** $m_e$ matched | **Fails** — hierarchy needs $\delta_e\gg\delta_\tau$ |
| F5 | Any bracket in §2 matches both ratios | **Not yet** |

---

## §6. Corpus patch

> **L2 (Jammer v0.1e, 2026-05-24):** charged leptons carry $(8\pi)^{-\delta_\ell}$ with structural $\delta_{\rm singlet}=2/3$ (G₂ singlet vs $\sigma_1/\sigma_2$ neutrino $\delta_\nu=1/3$); $\delta_e,\delta_\mu,\delta_\tau$ spacing **bracket** from §19.4 overlaps — open at Paper S5 / $D_F$.

---

## §7. Next

1. **Radiative tower:** $\delta_\ell\supset(1/16\pi^2)\sum\mathcal{O}^2$ (§19.4) — numeric v0.2  
2. ~~**L4 $D_F$**~~ — **DONE** (`Jammer_S22_1f_DF_Heat_Kernel_Delta_L4_v0_1`)  
3. Optional: 2-loop L1 + fixed $\delta_\ell$ bracket

---

— Jammer §22.1e L2 v0.1, 2026-05-24.
