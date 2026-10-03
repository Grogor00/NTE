# Paper S3 — Λ_NTE mechanism M3: S¹_{β_GB} boundary counter-term v0.1

**Stream:** Cursor scaffold → Jammer/Scratch Paper S3  
**Date:** 2026-05-23  
**Status:** Structural scaffold — **not** numerical closure  
**Prior:** `Paper_S3_Lambda_M1_M2_Worksheet_v0_1_20260523.md`; S2-D §2.4 item 3

---

## §1. Mission

Evaluate whether the **gauge-birth circle** $S^1_{\beta_{\rm GB}}$ in $M = {\rm Hopf}\text{-}S^3 \times S^1_{\beta_{\rm GB}} \times A_F$ supplies a **boundary counter-term** that further suppresses post-unimodular $\Lambda_{\rm NTE}$ residual ($\sim 10^{83}\times\Lambda_{\rm obs}$ after $a_4$).

**Owner split:** Jammer (boundary action / Appendix B.3); Scratch (spectral triple integral).

---

## §2. Corpus anchors

| Quantity | Value / source |
|----------|----------------|
| $\beta_{\rm GB}$ | $\sqrt{2\pi}/M_{\rm Pl}$ (§22.14, Paper S2) |
| Vol($M$) | $2\pi^2\beta_{\rm GB}$ |
| $a_0$ | $N_F\beta_{\rm GB}/2$, $N_F=180$ |
| $a_4$ R² piece | $270\beta_{\rm GB}$ (S2-C-B) |
| Gauge birth | Temporal locking at $N_{\rm lock}$; $S^1$ factor = compact **e-fold** direction |

---

## §3. Mechanism sketch (M3)

**Idea:** Spectral action on $M$ with **localized boundary conditions** on $S^1_{\beta_{\rm GB}}$ at gauge birth (Wick rotation / locking transition) adds **extrinsic curvature / conical defect** contribution to effective $\Lambda$:

$$\Delta\Lambda_{\rm M3} \stackrel{?}{=} \frac{1}{\text{Vol}(M)^2}\int_{\partial M} \mathcal{K}_{\beta_{\rm GB}}\,dS$$

where $\mathcal{K}_{\beta_{\rm GB}}$ is extrinsic or **seam** curvature from C¹ kink at locking (Appendix E §E.3).

**Sign programme:** boundary term could be **negative** (partial cancellation of positive $a_4$ residual).

---

## §4. Numerics (Cursor OOM v0.1)

**Script:** `Working/paper_s3_m3_beta_gb_numerics.py`

| Estimate | Order |
|----------|-------|
| $\beta_{\rm GB}$ | $\sim 10^{-18}$ GeV$^{-1}$ |
| Vol($M$) | $\sim 10^{-17}$ GeV$^{-1}$ |
| $a_4/\text{Vol}^2$ scaling | $\sim 10^{37}$ GeV$^4$ (same class as S2-D residual) |
| M3 seam factor (if $\mathcal{K}\sim 1/\beta_{\rm GB}$) | $\mathcal{O}(10^1$–$10^3)$ — **insufficient alone** for $10^{83}$ |

**Reading:** M3 is **plausible sign/magnitude contributor** but requires **derived** $\mathcal{K}_{\beta_{\rm GB}}$ from explicit $S_E$ at locking — not OOM fit.

---

## §5. Attack route (Paper S3)

1. **Appendix B.3 extension:** local $\mu(x,N)$ + **temporal boundary** at $N=N_{\rm lock}$ on $S^1_{\beta_{\rm GB}}$
2. **Gilkey–Weldon boundary heat-kernel** terms on $S^1$ with periodicity $\beta_{\rm GB}$
3. **Cross-check:** M3 must not alter $\kappa_0$, $K(\Phi)=1$, or $n_s$ route (S2-D §2.5)

---

## §6. Falsifiers

1. Derived M3 term **increases** $\Lambda_{\rm NTE}$ residual  
2. Requires continuous parameter not in §XVII register  
3. Breaks F1 Weyl-flat / Euler-zero on $M$

---

## §7. Status

| Claim | Register |
|-------|----------|
| M3 mechanism plausible | **Scaffold** |
| M3 closes $10^{83}$ gap alone | **Falsified** (OOM) |
| Full M3 derivation | **Jammer + Scratch** |

---

## §8. Cross-references

- §22.15, §17.5.18, Appendix B.3, Appendix E (C¹ kink)  
- `Paper_S3_Lambda_M1_M2_Worksheet_v0_1_20260523.md`

— Cursor Paper S3 M3 v0.1, 2026-05-23.
