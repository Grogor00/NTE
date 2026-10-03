# Paper S3 — Λ_NTE numerical closure scaffold v0.1 (Priority IV-3)

**Stream:** Cursor scaffold → **Scratch** Paper S3 execution  
**Date:** 2026-05-23  
**Status:** OOM numerics + mechanism stack map — **not** observational closure  
**Lineage:** `Working/Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md` §2; §17.5.18; §22.15

---

## §1. Problem statement

Observed: $\Lambda_{\rm obs} \sim (10^{-3}\,{\rm eV})^4 \sim 10^{-122} M_{\rm Pl}^4$.

Naive spectral $f_4\Lambda^4 a_0$ on $M = {\rm Hopf}\text{-}S^3 \times S^1_{\beta_{\rm GB}} \times A_F$: **$\sim 10^{0}$–$10^{1}\,M_{\rm Pl}^4$** (S2-D §2.1).

Unimodular projection (§22.15): removes leading volume mode; **residual at $a_4$ level still $\sim 10^{83}\times\Lambda_{\rm obs}$** (S2-D §2.3–§2.4).

**Paper S3 mission:** identify **quantitative** suppression chain closing gap to $10^{-122} M_{\rm Pl}^4$ without breaking κ₀, F1, or $a_4$ structural anchors.

---

## §2. Numerics (Cursor v0.1)

**Script:** `Working/paper_s3_lambda_nte_numerics.py`

| Channel | $\Lambda$ [GeV⁴] | vs $\Lambda_{\rm obs}$ |
|---------|-------------------|------------------------|
| Observed ($\sim 10^{-3}$ eV)$^4$ | $\sim 10^{-47}$ | 1 |
| Naive $f_4\Lambda^4 a_0$/Vol($M$) | $\sim 10^{74}$ | $\sim 10^{121}$ |
| $a_4$ residual (S2-D §2.3) | $\sim 10^{36}$ | **$\sim 10^{83}$** |

**Reading:** unimodular + $a_4$ **insufficient alone** — confirms §17.5.18 "framework only / ~10⁸³ off; Paper S3".

---

## §3. Mechanism stack candidates (Paper S3 attack route)

| ID | Mechanism | Target suppression | Owner |
|----|-----------|-------------------|-------|
| M1 | CC2008 $f_4$ moment choice / dμ(V) on compact $M$ | $\gtrsim 10^{120}$ | Scratch |
| M2 | Hopf $S^3\to S^2$ holographic projection of $\Lambda$ density | TBD | Scratch |
| M3 | Gauge-birth $S^1_{\beta_{\rm GB}}$ boundary counter-term | `Paper_S3_Lambda_M3_Beta_GB_Boundary_v0_1` | **Scaffold v0.1** |
| M4 | D_F $\sim 10^{-18}$ leakage into $\Lambda$ (S2-C-C) | Subdominant | Scratch |
| M5 | Non-perturbative $a_6+$ on round $M$ (CC2008 vanishing) | Exponential? | Programme S |

**Discipline:** no claim "NTE predicts Λ" until single chain closes to within $\lesssim 10\times\Lambda_{\rm obs}$ without tuned parameters.

---

## §4. Falsifiers

1. Residual $\Lambda_{\rm NTE}$ sign wrong vs acceleration history  
2. Mechanism stack breaks κ = 5.50 or $n_s$ route  
3. Requires hidden continuous parameter not in §XVII accounting  

---

## §5. Cross-references

- §17.5.18, §22.15, §22.20  
- `Working/Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md`  
- Scratch queue: Paper S3 after D5

— Cursor Paper S3 scaffold v0.1, 2026-05-23.
