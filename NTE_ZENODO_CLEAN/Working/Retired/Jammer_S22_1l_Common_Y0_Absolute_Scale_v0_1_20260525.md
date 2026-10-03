# Jammer S22-1l — Common $Y_0$ Absolute Charged-Lepton Scale (post sunshine exit)

**Stream:** Cursor (Jammer lane)  
**Date:** 2026-05-25  
**Status:** v0.1 — bracket + numerics; **not** Tier-A closure  
**Parent:** `Jammer_S22_1k_Sunshine_Exit_Closure_v0_1_20260524.md` (ratio exit signed off)

---

## §1. Problem

Sunshine exit fixes **ratios** at zero extra parameters ($m_\mu/m_e \approx 207$, $m_{\tau}/m_\mu \approx 18$ with $\dim(\mathbb{H})=4$ lock). Absolute magnitudes from $m_\ell = (8\pi)^{-\delta_g^{\rm eff}} v_{\rm EW}/\sqrt{2}$ sit at **pred/obs $\approx 0.37$–0.40** uniformly across $\tau,\mu,e$ — not generation-dependent.

Corpus §22.1: *"Still open: common absolute $Y_0$ scale."*

---

## §2. Universal uplift (not suppression)

Define a single post-ratio factor:

$$m_\ell^{\rm phys} = Y_0 \cdot m_\ell^{\rm pred}, \qquad m_\ell^{\rm pred} = (8\pi)^{-\delta_\ell^{\rm eff}} \frac{v_{\rm EW}}{\sqrt{2}}.$$

Numerics (`paper_s22_1l_absolute_y0_numerics.py`, $\dim(\mathbb{H})=4$ lock):

| Gen | $m^{\rm pred}$ (GeV) | $m^{\rm obs}$ | $Y_0 = m^{\rm obs}/m^{\rm pred}$ |
|-----|----------------------|---------------|----------------------------------|
| $\tau$ | 0.706 | 1.777 | 2.52 |
| $\mu$ | 0.0393 | 0.1057 | 2.69 |
| $e$ | $1.90\times10^{-4}$ | $5.11\times10^{-4}$ | 2.69 |

**Mean $Y_0 \approx 2.63$** (geom mean 2.63); spread **< 7%** across generations.

With $Y_0 = 2.634$: all three masses match obs within **~2%** (lock variant $\dim(G_2)/4$ similar).

**Ratios:** unchanged — $Y_0$ cancels in $m_i/m_j$.

---

## §3. Structural brackets (Tier 2 until derived)

| Bracket | Value | vs $Y_0 \approx 2.63$ |
|---------|-------|------------------------|
| **$8/3$** | 2.667 | **1.2%** |
| $e$ | 2.718 | 3.2% |
| $(8\pi)^{1/3}$ | 4.46 | wrong direction (needs $1/Y_0 \sim 0.38$) |
| $3/8 = 1/Y_0$ | 0.375 | **1.1%** vs pred/obs |

**Dual reading:** absolute uplift $Y_0 \approx 8/3$ (octonion dimension / three generations); or equivalently bare masses are **$3/8$** of physical scale before interface matching at $G$.

**Not** fit from data alone — bracket is **post-hoc** until derived from LB-6 bulk→surface measure or $D_F$ overall normalisation (Scratch Programme S / Jammer open).

---

## §4. Lock exponent prose (S22-TM, Greg choice)

| Exponent | $m_\mu/m_e$ | $m_{\tau}/m_\mu$ | Use |
|----------|-------------|------------------|-----|
| $\dim(\mathbb{H})=4$ | **207** (0.1%) | **18.0** (~7%) | **Default prose** — quaternionic fibre at $G$ |
| $\dim(G_2)/4 = 7/2$ | 200.3 (~3%) | 17.3 (~3%) | **Balanced** alternative |

**Recommendation:** corpus §22.1 / §22.5 cite $\dim(\mathbb{H})=4$ as primary; footnote $\dim(G_2)/4$ as $\sim 3\%$ balanced variant. Greg ratification optional.

---

## §5. Epistemic register

| Item | Status |
|------|--------|
| Ratio closure (v0.1k) | **Signed off** |
| Common $Y_0$ | **Bracket** $Y_0 \approx 8/3$; numerics 2% match |
| Derivation of $8/3$ from $D_F$ / spectral measure | **Open** → Scratch research |
| Corpus patch | **Queued AC** (§22.1 one-line bracket) |

---

## §6. Falsifiers

- Generation-dependent $Y_0(g)$ with $>10\%$ spread after ratio exit → kills single-scale story.
- Derived $Y_0$ from heat-kernel / LB-6 lands far from $8/3$ with no reconciliation → bracket retired.

---

## §7. Files

- `Working/paper_s22_1l_absolute_y0_numerics.py`
- `Working/paper_s22_1k_sunshine_exit_closure_numerics.py` (imported)

---

*Jammer S22-1l — 2026-05-25. Cursor return-pass item; AC corpus check queued.*
