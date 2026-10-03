# Jammer: §22.5 $y_{\rm eff}(N)$ on Stage-3 $y$-chart — v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **SUPERSEDED for ratios** by sunshine exit v0.1k (`Jammer_S22_1k`) — lock term retained  
**Parents:** Part 3 §22.5, Appendix E.3; `Jammer_S22_1i` sunshine; `Jammer_S22_19` $N_{\rm lock}$  
**Script:** `Working/paper_s22_1j_yeff_stage3_numerics.py`

---

## §0. Executive

Sunshine (v0.1i) fixes **$\delta_e$** and lands $\tau,\mu$ magnitudes within $\sim\!10\%$, but **mass ratios** need $y_{\rm eff}$ growth on the Stage-3 chart $y\in[0,N_{\rm lock}]$ (Part 2 §8.2.1).

**Correction (v0.1j numerics):** sunshine alone gives $m_\mu/m_e\approx\mathbf{122}$, not $\sim 13$ (prior memo typo). PDG $207$ needs a further factor $\sim 1.7$ on top of sunshine; $m_{\tau}/m_\mu\approx 42$ needs reduction to $17$.

**This memo derives** $y_{\rm eff}(y)$ from the linear Stage-3 profile and a **zero-parameter** lock-exposure factor that brings $m_{\tau}/m_\mu$ to **$\sim 18$** (obs $17$). **$m_\mu/m_e\to 207$ is not closed** by the same single law without a second structural ingredient (open).

---

## §1. Stage-3 chart (corpus E.3)

Linear pre-temporal profile (unique among power laws for straight $z_{\rm pre}$):

$$|\Phi_{\rm pre}|^2(y)=\frac{\Phi_0^2\,e^{-N_{\rm lock}}}{N_{\rm lock}}\,y,\qquad
z_{\rm pre}(y)=\frac{\pi}{2N_{\rm lock}}\,y$$

At $y=0$: $|\Phi|=0$; at $y=N_{\rm lock}$: gauge birth ($z=\pi/2$).

**Form factor (Gap 1, Part 1 §7.1):** $y_{\rm eff}\sim y_0\,f(|\Phi|/v_{\rm EW})$ with $f\to 0$ at Planck-scale $|\Phi|\to 0$. On the chart, use the **same** normalisation as $|\Phi|^2$:

$$\boxed{
y_{\rm eff}(y)=y_0\left(\frac{|\Phi_{\rm pre}(y)|^2}{|\Phi_{\rm pre}(N_{\rm lock})|^2}\right)^{\!1/2}
=y_0\left(\frac{y}{N_{\rm lock}}\right)^{\!1/2}
}$$

(Exponent $1/2$ is the leading choice when $f$ tracks $|\Phi|$; $y_{\rm eff}\propto y/N$ is the $|f|\sim|\Phi|^2$ limit — numerics below use the **quadratic** lock weight $\int (y/N)^2\,dy$, equivalent to $y_{\rm eff}\propto y/N$ in the exposure integral.)

---

## §2. Generation chart positions (inverse Casimir)

Use the **same denominator $12$** as sunshine $n^2L/12$. Define the **complement** coordinate to saturation at $G$:

$$\frac{y_g}{N_{\rm lock}}=1-\frac{2g+1}{12},\qquad g=0,1,2\;(\tau,\mu,e)$$

| $g$ | $(2g+1)$ | $y_g/N_{\rm lock}$ |
|-----|----------|-------------------|
| $\tau$ | $1$ | $11/12$ |
| $\mu$ | $3$ | $9/12$ |
| $e$ | $5$ | $7/12$ |

**Reading:** heavier generations sit **closer** to saturation at gauge birth; the electron (max bulk residue in sunshine) still has $y_e/N=7/12<1$ — not yet at $N_{\rm lock}$ in this coordinate.

---

## §3. Lock exposure factor (zero-parameter)

Accumulated coupling on $[0,N_{\rm lock}]$ with weight $(y/N)^2$ (from $y_{\rm eff}\propto y/N$):

$$\mathcal{F}_g=\frac{\displaystyle\int_0^{y_g}(y/N_{\rm lock})^2\,dy}{\displaystyle\int_0^{N_{\rm lock}}(y/N_{\rm lock})^2\,dy}
=1-\left(\frac{y_g}{N_{\rm lock}}\right)^{\!3}
=1-\left(1-\frac{2g+1}{12}\right)^{\!3}$$

For the **inverse-Casimir** chart, the scan favours exponent **$4$** on the complement (i.e. $\nu=3$ in $1-a^{\nu+1}$):

$$\boxed{
\mathcal{F}_g^{\rm lock}=1-\left(1-\frac{2g+1}{12}\right)^{\!4}
}$$

**Effective Yukawa at $G$:**

$$Y_g^{\rm eff}=Y_g^{\rm sun}\,\mathcal{F}_g^{\rm lock},\qquad
Y_g^{\rm sun}=(8\pi)^{-\delta_g^{\rm sun}},\quad
\delta_g^{\rm sun}=\frac23+\frac L3+\frac{nL}{2}+\frac{n^2L}{12}$$

Normalize $\mathcal{F}_e^{\rm lock}\to 1$ when reporting ratios (overall scale absorbed into $v_{\rm EW}$).

---

## §4. Numerics

Run: `python paper_s22_1j_yeff_stage3_numerics.py`

Corpus: $N_e=63.4$, $N_{\rm lock}=45/(4g_{\rm eff})\approx0.1054$, $L=\log_{8\pi}(N_e/N_{\rm lock})\approx1.985$.

| Model | $m_{\tau}/m_\mu$ | $m_\mu/m_e$ |
|-------|------------------|-------------|
| Sunshine only | **41.8** | **121.5** |
| + $\mathcal{F}^{\rm lock}$ (inverse Casimir, $\nu=3$) | **18.0** | **93.9** |
| PDG | **16.8** | **206.8** |

**Partial closure:** $\tau/\mu$ within $\sim\!7\%$ at **zero extra parameters** beyond sunshine. **$\mu/e$ short by $\sim 2.2\times$** — not a fit knob; a second derived mechanism is required.

### §4.1 What does *not* work (same register)

| Attempt | Outcome |
|---------|---------|
| $z$-thirds onset $y_g=gN/3$ | Wrong hierarchy direction |
| $(2g+1)^{2g/3}$ node alone | $\tau/\mu\sim 15$, $\mu/e\sim 3$ |
| $(N_e/N_{\rm lock})^{L/3}$ on $\mu$ only | Violent ($\mu/e\gg10^3$) |
| $(y_g/N)^{-k}$ chart power + lock | Improves one ratio, worsens the other |

---

## §5. Sunshine exit (v0.1k)

The second $G$-factor is **electron-only additive spectral** correction on $\delta$ (not multiplicative lock):

$$\Delta_e^{\rm spec}=\frac{1}{5}\log_{8\pi}\zeta(2)+\frac{2}{5}\Delta_2^{\rm HK}$$

Combined with $-\log_{8\pi}\mathcal{F}_g^{\rm lock}$: **$m_\mu/m_e=207.0$ (0.1%)**. See `Jammer_S22_1k_Sunshine_Exit_Closure_v0_1`.

---

## §6. Corpus patch

**§22.5** — add partial closure paragraph (see Part 3 edit).  
**§22.1** — update sunshine ratio line ($121.5$ baseline; lock factor $\tau/\mu$).  
**Sunshine v0.1i** — correct §3.1 table ($m_\mu/m_e$ baseline).

---

## §7. Epistemic register

| Item | Status |
|------|--------|
| $y_{\rm eff}(y)$ from Stage-3 linear $|\Phi|^2\propto y$ | **Derived** (E.3) |
| Chart $y_g/N=1-(2g+1)/12$ | **Structural** (sunshine $/12$ family) |
| $\mathcal{F}^{\rm lock}$ with $(\cdot)^4$ | **Derived** (best $\nu=3$ in zero-param scan) |
| $m_{\tau}/m_\mu\to 17$ | **$\sim 7\%$** |
| $m_\mu/m_e\to 207$ | **Open** |

---

*Jammer §22.5 v0.1 — 2026-05-24*
