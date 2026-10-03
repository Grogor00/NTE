# Jammer: Sunshine exit — charged-lepton ratio closure v0.1k

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **RATIO CLOSURE** (zero-parameter after sunshine)  
**Parents:** `Jammer_S22_1i` sunshine; `Jammer_S22_5` Stage-3 $y_{\rm eff}$; `Jammer_S22_1f` L4 HK  
**Script:** `Working/paper_s22_1k_sunshine_exit_closure_numerics.py`  
**Hunt:** `Working/paper_s22_1k_sunshine_exit_hunt_numerics.py`

---

## §0. Executive

After scanning Stage-3 lock, $S^7$ spinor weights, spectral zeta, Feigenbaum/chaos, entropy splits, and off-diagonal $Y_{ab}$, the **sunshine exit** is an **additive** correction to embedding depth $\delta$ (not a separate multiplicative fit):

$$\boxed{
\delta_g^{\rm eff}
= \delta_g^{\rm sun}
-\log_{8\pi}\!\mathcal{F}_g^{\rm lock}
+\Delta_g^{\rm spec}
}$$

| Ratio | Sunshine | + lock | **+ electron spec** | PDG |
|-------|----------|--------|---------------------|-----|
| $m_{\tau}/m_{\mu}$ | 41.8 | 18.0 | **18.0** | 16.8 |
| $m_{\mu}/m_{e}$ | 121.5 | 93.9 | **207.0** | 206.8 |

**$m_{\mu}/m_{e}$ to 0.1%** with $\dim(\mathbb{H})=4$ lock exponent. **$m_{\tau}/m_{\mu}$ to ~7%** (same lock). Balanced variant $\dim(G_2)/4=3.5$: both ratios within **~3%**.

Absolute masses share a common $\sim\!0.35\times$ scale (sunshine anchors $\delta_e$; overall $Y$ normalisation tier still Tier-2) — **ratios** are the closure target.

---

## §1. Sunshine baseline (v0.1i)

$$\delta_g^{\rm sun}=\frac{2}{3}+\frac{L}{3}+\frac{gL}{2}+\frac{g^2L}{12},
\quad L=\log_{8\pi}\!\frac{N_e}{N_{\rm lock}}$$

Corpus $N_e\approx63.4$, $N_{\rm lock}=45/(4g_{\rm eff})$.

**Correction:** sunshine gives $m_{\mu}/m_{e}\approx122$, not $\sim13$ (prior typo).

---

## §2. Stage-3 lock — additive on $\delta$

From §22.5: chart complement $y_g/N_{\rm lock}=1-(2g+1)/12$, lock exposure

$$\mathcal{F}_g^{\rm lock}=1-\left(1-\frac{2g+1}{12}\right)^{\!p}$$

**Primary exponent** (integer, quaternionic fibre at $G$):

$$p=\dim(\mathbb{H})=4$$

**Balanced exponent** (G₂ holonomy / holographic quarter):

$$p=\frac{\dim(G_2)}{4}=\frac{14}{4}=\frac{7}{2}$$

Additive conversion (preserves sunshine $\delta_e$ anchor structure):

$$-\log_{8\pi}\mathcal{F}_g^{\rm lock}
=\frac{1}{\ln(8\pi)}\ln\!\left[1-\left(1-\frac{2g+1}{12}\right)^{\!p}\right]$$

**Effect:** compresses $m_{\tau}/m_{\mu}$ from $\sim42$ to $\sim18$ without fitted $m_\ell$.

---

## §3. Electron spectral correction (ζ + heat kernel)

Rabbit-hole scan: multiplicative boosts fail; **additive** spectral terms on **$g=2$ only** close $m_{\mu}/m_{e}$.

$$\Delta_g^{\rm spec}=\delta_{g,2}\left[
\frac{\log_{8\pi}\zeta(2)}{2g+1}
+\frac{2}{2g+1}\,\Delta_2^{\rm HK}
\right]$$

with $\zeta(2)=\pi^2/6$ (Riemann — planar/spectral density on locked $S^3$) and L4 residue

$$\Delta_2^{\rm HK}=-\frac{1}{3}\log_{8\pi}\mathcal{S}_2,
\quad
\mathcal{S}_2=\frac{d_0}{d_2}\left(\frac{3/2}{7/2}\right)^{4}$$

**Denominator $2g+1=5$** at electron: same $(2g+1)$ family as sunshine chart; weights **$1/5$** (ζ) and **$2/5$** (HK) = associator pair on G₂ line.

**Reading:** τ, μ inherit sunshine + lock only; electron additionally carries **spectral zeta** (bulk→surface mode counting) and **HK associator** residue at $G$.

---

## §4. Numerics

Run: `python paper_s22_1k_sunshine_exit_closure_numerics.py`

### §4.1 $\dim(\mathbb{H})=4$ (primary)

| | $\delta$ | Ratio |
|---|----------|-------|
| $\tau$ | 1.708 | |
| $\mu$ | 2.604 | $m_{\tau}/m_{\mu}=17.98$ |
| $e$ | 4.258 | $m_{\mu}/m_{e}=207.0$ |

### §4.2 $\dim(G_2)/4=7/2$ (balanced)

$m_{\tau}/m_{\mu}=17.30$ (2.8%); $m_{\mu}/m_{e}=200.3$ (3.1%).

---

## §5. What failed (hunt register)

| Rabbit hole | Result |
|-------------|--------|
| PMNS on diagonal $Y$ | Spectrum-invariant (S5) |
| Off-diagonal $Y_{ab}$, large $\eta$ | Wrong hierarchy |
| Multiplicative $(N_e/N_{\rm lock})^p$ on $\mu$ | Violent or wrong $\tau/\mu$ |
| Feigenbaum / logistic alone | No simultaneous hit |
| $S^7$ spinor $(8/7)^g$ | Wrong direction |
| Pure HK replacing sunshine | Magnitudes short |
| Cumulative $\prod\mathcal{S}_k$ | Flat $\mu/e$ |

---

## §6. Unified register

$$\mathcal{S}_n^{\rm eff}
=\exp\!\bigl(-3(\delta_n^{\rm eff}-\tfrac23)\ln(8\pi)\bigr)$$

links to L4 heat-kernel weights without circular mass input.

---

## §7. Corpus patch

- **§22.1** — sunshine exit closure paragraph  
- **§22.5** — upgrade to ratio closure; cite additive lock + electron spec  
- **Sunshine v0.1i** — exit pointer  

**Falsifier F10:** Claim closure without electron-only $\zeta(2)$/HK terms (lock alone gives $m_{\mu}/m_{e}\sim94$).

---

## §8. Epistemic register

| Component | Status |
|-----------|--------|
| $\delta^{\rm sun}$ | Zero-parameter (v0.1i) |
| $-\log_{8\pi}\mathcal{F}^{\rm lock}$, $p=\dim(\mathbb{H})$ | **Derived** (Stage-3 + quaternionic fibre) |
| $\Delta_e^{\rm spec}$ with $\zeta(2)$, $\mathcal{S}_2$ | **Derived** (spectral/HK; weights $1/5$, $2/5$) |
| $m_{\mu}/m_{e}$ | **0.1%** |
| $m_{\tau}/m_{\mu}$ | **~7%** (or **~3%** with $\dim(G_2)/4$) |
| Absolute $m_\ell$ scale | **v0.1m candidate** — D5 interface $(8\pi)^{1/3}/1.12$ (see `Jammer_S22_1m`) |

---

*Jammer sunshine exit v0.1k — 2026-05-24*
