# S3-f2 — structural $f_k$ from S2-A spectrum v0.1

**From:** Jammer (R&D) — executing Scratch queue item  
**Date:** 2026-05-23  
**Script:** `Working/s3_f2_fk_moments_numerics.py`  
**Parents:** Paper S3 §R1; S2-A/B/C-B; CC2008; S3-f3

---

## §1. Mission

Compute **derived** spectral-cutoff moments $f_0,f_2,f_4$ for NTE Dirac operator on $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$ — **not** fit to $\Lambda_{\rm obs}$.

**Question:** Does structural $f$ from CC2008 exponential + S2 heat-kernel coefficients close the post-unimodular **~83 OOM** gap?

---

## §2. Inputs (S2 arc)

| Quantity | Value | Source |
|----------|-------|--------|
| $N_F$ | 180 | S2-B (A_F = 𝕆⊕𝕆) |
| $\beta_{\rm GB}$ | $\sqrt{2\pi}/M_{\rm Pl}$ | J6-n3 / Companion 9 |
| $a_0$ | $N_F\beta_{\rm GB}/2$ | S2-B |
| $a_2$ | $-N_F\beta_{\rm GB}/4$ | S2-B |
| $a_4|_M$ | $(3/2)N_F\beta_{\rm GB}$ | S2-C-B (R²-only) |
| F1 anchor | $270\beta_{\rm GB}$ | S2-C-B |

**Spectrum (S2-A):** $\mu_{k,m}^2=(k+\tfrac32)^2+(2\pi(m+\tfrac12)/\beta_{\rm GB})^2$, mult $=4(k+1)(k+2)\times N_F$, $\theta=\tfrac12$ on $S^1$.

---

## §3. Cutoff moments (derived)

### §3.1 CC2008 exponential $h(\rho^2)=e^{-\rho^2}$

On round $S^3\times S^1$ (Theorem 3):

$$\int_0^\infty e^{-\rho^2}\rho^3\,d\rho = \tfrac12, \qquad \int_0^\infty e^{-\rho^2}\rho\,d\rho = \tfrac12$$

**Register:** $\Lambda^4$ and $\Lambda^2$ weights **equal** at O(1) — no built-in $10^{-83}$.

### §3.2 Connes moments $f_k=\int_0^\infty f(u)\,u^{k/2-1}\,du$

| Cutoff $f(u)$ | $f_4$ | $f_2$ | $f_0$ | $f_4/f_2$ |
|---------------|-------|-------|-------|-----------|
| $e^{-u}$ (CC default) | 1 | 1 | $\infty$* | 1.00 |
| $e^{-u^2}$ (Gaussian) | 0.50 | 0.89 | $\infty$* | 0.56 |

*$f_0$ log-divergent in Connes convention; CC2008 Theorem 3 regulates finite part at **O(1)** — same register as corpus §22.15.

---

## §4. Spectral action assembly ($\Lambda_{\rm cut}=M_{\rm Pl}$)

$$S = f_4\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_0 a_4 + \cdots$$

| Term | $e^{-u}$ cutoff | Role |
|------|-----------------|------|
| $f_4\Lambda^4 a_0/{\rm Vol}(M)$ | $1.6\times10^{74}\,{\rm GeV}^4$ | **Unimodular removed** |
| $f_0 a_4$ residual | $2.4\times10^{37}\,{\rm GeV}^4$ | **Gravitating CC piece** |
| $f_2\Lambda^2 a_2$ | $\sim10^{20}$ | EH sector (not $\Lambda$ density) |

Gaussian cutoff changes $f_4/f_2$ by O(1) only — **does not** move residual by 83 dex.

---

## §5. Tuning falsifier

| Route | Required moment | $\log_{10}$ | Verdict |
|-------|-----------------|-------------|---------|
| $f_4$ (no unimodular) | $1.7\times10^{-121}$ | $-120.8$ | **Forbidden** |
| $f_0$ (post-unimodular) | $1.2\times10^{-84}$ | $-83.9$ | **Forbidden** |
| Derived $f_0$ | O(1) | 0 | **Honest** |

**S3-f2 verdict:** Structural $f_k$ **derived**; ratios O(1). **Does NOT close ~83 OOM.**

---

## §6. Combined stack (with S3-f3)

$$\Lambda_{\rm obs} \stackrel{?}{=} \underbrace{\mathcal{P}_{\rm uni}[f_4 a_0]}_{\rm removed} \times \underbrace{f_0 a_4}_{\sim10^{83}\ \text{(derived }f_0)} \times \underbrace{\mathcal{W}_{d\mu}}_{\rm S3\text{-}f3} \times \underbrace{\mathcal{S}_{R3}}_{\rm a_6+\ \text{exponential}}$$

| Factor | S3-f2 / S3-f3 status |
|--------|----------------------|
| R1 $f_k$ | **Done v0.1** — O(1); fixes ratios only |
| R2 $d\mu(V)$ | **Done v0.1** — no 83 OOM alone |
| R3 $a_6+$ | **Open** — primary bulk suppression candidate |

---

## §7. Numeric discipline notes

1. **Naive spectrum sum** at physical $\beta_{\rm GB}\sim1/M_{\rm Pl}$: $S^1$ modes decouple from $\mathrm{Tr}(e^{-D^2/\Lambda^2})$ at $\Lambda\sim M_{\rm Pl}$; full coefficients = S2-B Hurwitz closed form (not truncated sum).
2. **$f_0$ regulation** must match CC2008 Theorem 3 tail — not imported from $\Lambda_{\rm obs}$.
3. **F1 anchor** $270\beta_{\rm GB}$ unchanged — no $f_k$ choice breaks κ₀ or $n_s$.

---

## §8. AC pointer

> **S3-f2 (Jammer, 2026-05-23):** $f_0,f_2,f_4$ derived from CC2008 exponential + Connes moments on S2-A/B/C coefficients. Moments O(1); $f_0^{\rm req}\sim10^{-84}$ to match obs is **forbidden tuning**. Residual $\Lambda\sim f_0 a_4\sim10^{37}\,{\rm GeV}^4$ with derived $f_0$. R3 ($a_6+$) remains primary closure route.

---

## §9. Cross-references

- `Paper_S3_Structural_f_Attack_Route_v0_1_20260523.md` §R1  
- `Jammer_S3_f3_dmu_V_from_PhiN_v0_1_20260523.md`  
- `Paper_S2_S2A_Operator_Setup_v0_1.md`; S2-B; S2-C-B  
- `Unimodular_Gravity_Verification_CC2008_v1.md`

— Jammer S3-f2 v0.1, 2026-05-23.
