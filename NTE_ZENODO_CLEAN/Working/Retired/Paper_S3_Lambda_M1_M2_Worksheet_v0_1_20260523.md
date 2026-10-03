# Paper S3 — Λ_NTE mechanisms M1 + M2 worksheet v0.1

**Stream:** Cursor → Scratch Paper S3  
**Date:** 2026-05-23  
**Status:** Structural attack on **remaining ~10⁸³ gap** after unimodular + a₄  
**Prior:** `Paper_S3_Lambda_NTE_Numerical_Scaffold_v0_1_20260523.md`, S2-D §2.3–§2.4

---

## §1. Baseline (closed numerics)

| Stage | $\Lambda$ [GeV⁴] | vs obs |
|-------|------------------|--------|
| Observed | $\sim 2.8\times 10^{-47}$ | 1 |
| Naive $f_4\Lambda^4 a_0$/Vol($M$) | $\sim 1.6\times 10^{74}$ | $\sim 10^{121}$ |
| Post-unimodular $a_4$ residual | $\sim 2.4\times 10^{37}$ | **$\sim 10^{83}$** |

**Scripts:** `paper_s3_lambda_nte_numerics.py`, `paper_s3_m1_m2_numerics.py`

Paper S3 must close the **$10^{83}$** gap, not the naive $10^{121}$ (unimodular already handles leading mode per §22.15).

---

## §2. M1 — CC2008 spectral cutoff / $f_4$ moment

### §2.1 Mechanism

Spectral action: $S = f_4\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_0 a_4 + \cdots$

- **Unimodular (§22.15):** $f_4\Lambda^4 a_0$ **does not gravitate** at classical level for volume-preserving variations — projected out.
- **Residual $\Lambda$** enters through $f_0 a_4$, sub-leading $f_2 a_2 Vol($M$) cross-terms, and **choice of $f$** fixing relative weights.

CC2008 §3: on round $S^3\times S^1$, **all $a_{2n}$ for $n\ge 2$ vanish** for the canonical exponential cutoff — leaving only cosmological + EH terms with exponentially small remainder. NTE **inherits** this on $M = {\rm Hopf}\text{-}S^3 \times S^1_{\beta_{\rm GB}}\times A_F$.

### §2.2 Numerics (M1)

If (counterfactual) the naive term were **not** projected:

$$f_4^{\rm req} \sim \Lambda_{\rm obs}/\Lambda_{\rm naive} \sim 10^{-121}$$

**This is not a solution** — it is the fine-tuning Paper S3 must **avoid by construction**.

**Structural route (Scratch):**

1. Derive $f$ from NTE spectral triple (not fit $f_4$ to $\Lambda_{\rm obs}$)
2. Use CC2008 exponential moment structure so $a_4$ coefficient 270$\beta_{\rm GB}$ is **the first gravitating CC piece**
3. Combine with M2/M3/M5 for remaining $10^{83}$

### §2.3 M1 status

| Claim | Register |
|-------|----------|
| Unimodular removes $f_4 a_0$ from observables | **Closed** (§22.15) |
| $f_4^{\rm req}\sim 10^{-121}$ if naive term gravitates | **Numerics** — falsifies tuning route |
| Structural $f$ from spectral triple | **Open** — Scratch Paper S3 §2 |

---

## §2.4 NTE-specific anchor (§22.15)

CC2008 leaves $d\mu(V)$ free; NTE fixes residual via **$H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ trajectory** + Friedmann history. Paper S3 must compute **$d\mu(V)\to \Lambda_{\rm NTE}^{\rm residual}$** on Hopf-$S^3\times S^1_{\beta_{\rm GB}}\times A_F$, not import $\Lambda_{\rm obs}$.

---

## §3. M2 — Hopf holographic projection ($S^3\to S^2$)

### §3.1 Mechanism sketch

NTE's internal space has **Hopf fibration** $S^3\to S^2$ with fibre $S^1$. Dark-matter κ derivation already uses **2D Hopf base** (Y₀₀ on $S^2$); Λ density may inherit **area-law** scaling distinct from 3D volume counting.

**Heuristic:** if cosmological constant density tracks **effective horizon area** of the Hopf base rather than $S^3$ volume:

$$\Lambda_{\rm eff} \sim \Lambda_{a_4}\times\left(\frac{A_{S^2}}{A_{\rm eff}}\right)^p$$

with $A_{\rm eff}\sim {\rm Vol}(M)^{2/3}$ from compact internal radius $\sim\beta_{\rm GB}$.

### §3.2 Numerics (M2 — Cursor heuristic v0.1)

From `paper_s3_m1_m2_numerics.py`:

| Quantity | Value |
|----------|-------|
| Vol($M$) | $\sim 2.0\times 10^{-17}$ GeV$^{-1}$ |
| $r_{\rm eff}\sim {\rm Vol}^{1/3}$ | $\sim 2.7\times 10^{-6}$ GeV$^{-1}$ |
| $A_{\rm eff}\sim \pi r_{\rm eff}^2$ | $\sim 2.3\times 10^{-11}$ GeV$^{-2}$ |
| $\Lambda_{\rm M2}$ (naive area$^2$ scaling) | **Wrong direction** — increases $\Lambda$; heuristic **falsified** |

**Reading:** naive area heuristic supplies **at most $\mathcal{O}(10^2$–$10^4)$** extra suppression — **insufficient alone** for $10^{83}$. M2 must be a **derived** area law from spectral triple (Ryu-Takayanagi / dS horizon on $S^3$), not this OOM guess.

### §3.3 Connection to κ (cross-check discipline)

κ₀ = 3/√(4π) uses **same Hopf base** — M2 must **not** alter κ₀ topological protection (S2-D §2.5). Λ suppression acts on **volume-mode / unimodular residual**, not on Y₀₀ monopole normalisation.

### §3.4 M2 status

| Claim | Register |
|-------|----------|
| Hopf base relevant to Λ | **Plausible** — same geometry as κ |
| Cursor area heuristic closes gap | **Falsified** — ~$10^{79}$ short |
| Formal dS/$S^3$ entropy area law | **Open** — tie §22.8 P-dS1 |

---

## §4. Combined stack (M1 + M2 + downstream)

$$\Lambda_{\rm obs} \stackrel{?}{=} \underbrace{\mathcal{P}_{\rm uni}[f_4 a_0]}_{\text{removed}} + \underbrace{f_0 a_4}_{\sim 10^{83}\times} \times \underbrace{\mathcal{S}_{\rm Hopf}}_{\text{M2}} \times \underbrace{\mathcal{B}_{\beta_{\rm GB}}}_{\text{M3}} \times \underbrace{e^{-a_6+\ldots}}_{\text{M5}}$$

| Mechanism | Target | Status |
|-----------|--------|--------|
| Unimodular | $10^{121}$ | **Closed** §22.15 |
| M1 structural $f$ | Relative $a_4/a_0$ weights | Open |
| M2 Hopf area | $\lesssim 10^{80}$ needed | Heuristic insufficient |
| M3 $\beta_{\rm GB}$ boundary | Sign + magnitude | Jammer |
| M5 $a_6+$ CC2008 | Exponential | Programme S |

**Paper S3 deliverable:** single derived chain with **no continuous tune**; must land within $\lesssim 10\times\Lambda_{\rm obs}$.

---

## §5. Falsifiers (unchanged)

1. Derived $\Lambda_{\rm NTE}$ wrong sign vs $\Lambda$CDM acceleration  
2. Mechanism breaks κ, $n_s$, or F1 $a_4$ anchor  
3. Requires hidden parameter not in §XVII register  

---

## §6. Cross-references

- §17.5.18, §22.15, §22.20  
- `Working/Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md`  
- `Working/Priority_IV_Pathway_Programmes_v0_1_20260523.md` (P-dS1 link)

— Cursor Paper S3 M1+M2 v0.1, 2026-05-23.
