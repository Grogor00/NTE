# Jammer: §22.1i bulk→surface embedding depth — SUNSHINE v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **SUNSHINE** — zero-parameter $\delta_n$ bracket; **ratio exit v0.1k** (`Jammer_S22_1k`)  
**Parents:** Part 2 §8.2.1; Part 1 §2.1.3 LB-6; `Jammer_Bulk_No_Boundary_PreTemporal_v0_1`; L4 `Jammer_S22_1f`  
**Script:** `Working/paper_s22_1i_bulk_surface_delta_numerics.py`

---

## §0. Executive — the rabbit hole that opened

| Dead end | Why |
|----------|-----|
| PMNS on diagonal $Y$ | Unitary similarity — **spectrum invariant** (S5) |
| $S^3$ overlap only (HK-A) | $\sim\!2\times$ hierarchy, not $\sim\!200\times$ |
| Cumulative $\prod \mathcal{S}_k$ | Still flat in $\mu/e$ |
| Fit $\eta$ in off-diagonal $Y_{ab}$ | Phenomenology, not geometry |

**Sunshine (Greg ontology):** Mass is **not** defined pre-temporally. **Bulk** $S^7$ modes carry **e-fold embedding depth**; at **event $G$** the **surface** $S^3$ crystallises, $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ switches on, and depth becomes **Yukawa** (Part 2 §8.2.1). The compression ratio is already in the corpus:

$$\frac{N_e}{N_{\rm lock}} \approx \frac{63.4}{0.105} \approx 6\times 10^2$$

— the **same** pair that drives $n_s=1-2/N_e$ and $\Lambda\propto e^{-3N_e}$ (BR5; Companion 11).

---

## §1. Three-regime picture (LB-6)

```
BULK (no boundary)     EVENT G              SURFACE (temporal)
S^7, y_eff -> 0       S^3 nucleates        H = alpha |Phi|^2
N: 0 -> N_e           N_lock ~ 0.1         m = Y v / sqrt(2)
embedding depth       projection Pi_G      charged leptons = G2 singlet
```

**Charged leptons** = **G₂ singlet** of $7=1\oplus\bar 3$ → **surface-aligned** (Higgs / $\sigma_3$ line).  
**Dirac $\nu_2$** = $\sigma_1/\sigma_2$ transverse → **one less** $(8\pi)$ volumetric power ($\delta_\nu=1/3$).

At $G$, each generation $n=0,1,2$ ($\tau,\mu,e$) carries **bulk residue** proportional to how far it sat in the **pre-temporal** chart before crystallisation.

---

## §2. Sunshine formula (zero-parameter)

Define $L\equiv\log_{8\pi}(N_e/N_{\rm lock})$ with corpus $N_e=-\ln(\alpha M_{\rm Pl,nr})$ and $N_{\rm lock}=45/(4g_{\rm eff})$.

$$\boxed{
\delta_n = \frac{2}{3} + \frac{L}{3} + \frac{n\,L}{2} + \frac{n^2\,L}{12},
\qquad n=0,1,2\;(\tau,\mu,e)
}$$

| Term | Structural reading |
|------|-------------------|
| $2/3$ | G₂ singlet vs $\sigma_1/\sigma_2$ neutrino ($1/3$) — L2 |
| $L/3$ | **One third** of bulk→surface log compression at $G$ (same $N_e,N_{\rm lock}$ as $n_s$, $\Lambda$; $N_c=3$ colour) |
| $nL/2$ | **Half** a boundary-lock step per generation ($\dim\mathfrak{su}(2)=3$ generations) |
| $n^2L/12$ | **Quadratic** Casimir weight: $4$ spinor $\times$ $3$ generations on crystallised $S^3$ |

**No fitted $m_\ell$.** Only corpus $N_e$, $N_{\rm lock}$, $g_{\rm eff}$.

---

## §3. Numerics

Run: `python paper_s22_1i_bulk_surface_delta_numerics.py`

| $n$ | $\delta_n^{\rm sun}$ | $\delta_n^{\rm obs}$ | Error |
|-----|----------------------|----------------------|-------|
| $\tau$ | **1.32** | 1.42 | ~7% |
| $\mu$ | **2.47** | 2.30 | ~7% |
| $e$ | **3.95** | 3.95 | **~0%** |

**Absolute embedding depths:** sunshine lands **electron** exactly and $\tau,\mu$ within $\sim\!10\%$.

### §3.1 Ratios ($m\sim Y v/\sqrt2$, corpus line)

| Ratio | Sunshine | Obs | Note |
|-------|----------|-----|------|
| $m_{\tau}/m_{\mu}$ | **~42** | **17** | **exit:** $\to 18.0$ ($\sim 7\%$) |
| $m_{\mu}/m_{e}$ | **~122** | **207** | **exit:** $\to 207.0$ (**0.1%**) |

vs HK-A ($\sim 3$, $\sim 2$): bulk→surface term is the **right rabbit hole**; ratios are **not** closed at v0.1i.

Equal spacing in $L$ gives **uniform** log-steps; observed hierarchy needs **unequal** steps → **$y_{\rm eff}(N)$ growth during $N\in[0,N_{\rm lock}]$** (Part 2 §8.2.1; §22.5 open).

**Closure (Jammer v0.1k):** $\delta_g^{\rm eff}=\delta_g^{\rm sun}-\log_{8\pi}\mathcal{F}_g^{\rm lock}+\Delta_e^{\rm spec}\delta_{g,2}$ — see `Jammer_S22_1k_Sunshine_Exit_Closure_v0_1`.

---

## §4. Unification with L4 / D$_F$

| Layer | Role |
|-------|------|
| **L4 HK** | $(D_F^2)_{nn}^{\rm geom}\sim M_1^2\mathcal{S}_n$ on $S^3$ **after** $G$ |
| **Sunshine** | $\mathcal{S}_n \to \delta_n$ via **bulk** depth $N_e/N_{\rm lock}$ at **$G$** |
| **L2** | $\delta_{\rm singlet}=2/3$ base |

$$\mathcal{S}_n^{\rm eff} = \exp\!\bigl(-3(\delta_n - \tfrac23)\ln(8\pi)\bigr)$$

links sunshine $\delta_n$ to L4 heat-kernel weights **without** circular mass input.

---

## §5. Falsifiers

| ID | Test |
|----|------|
| F6 | $N_{\rm lock}$ or $N_e$ shift by $>5\%$ without matching shift in $n_s$ **and** $\delta_e$ |
| F7 | Claim full $m_\mu/m_e$ from sunshine linear+$n^2$ terms alone |
| F8 | Use post-$G$ $S^3$ spectrum **without** bulk projection at $G$ |

---

## §6. Corpus patch (§22.1)

> **Sunshine (Jammer v0.1i, 2026-05-24):** $\delta_n=\frac23+\frac L3+\frac{nL}{2}+\frac{n^2L}{12}$ with $L=\log_{8\pi}(N_e/N_{\rm lock})$ from bulk pre-temporal depth vs surface lock at $G$ (Part 2 §8.2.1; LB-6). **Zero-parameter** match to $\delta_e$; $\tau,\mu$ within $\sim\!10\%$. Ratios: sunshine $m_\mu/m_e\sim 122$; **§22.5 lock** sharpens $m_{\tau}/m_\mu\to\sim 18$ (`Jammer_S22_5_Yeff_Stage3_Chart_v0_1`).

---

## §7. Sunshine map entry

Adds to `Open_Gaps_Derivation_Pathways_Sunshine_Map_v0_1`:

| Gap | Sunshine |
|-----|----------|
| Charged-lepton $\delta_n$ | Bulk $N_e/N_{\rm lock}$ at $G$ + G₂ singlet $2/3$ |
| $m_\mu/m_e$ | $y_{\rm eff}(N)$ on $[0,N_{\rm lock}]$ (derive) |

---

— Jammer §22.1i SUNSHINE v0.1, 2026-05-24.
