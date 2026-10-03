# Paper S3 — structural $f$ attack route v0.1 (Impact #2)

**Stream:** Cursor scaffold → Jammer / Scratch Paper S3  
**Date:** 2026-05-23  
**Status:** **R6 ratified @ genuine-test tier** (Greg 2026-05-23) — Λ_pred ≈ 1.05× obs; BR2d-J3 refine open  
**Script:** `Working/paper_s3_structural_f_numerics.py`  
**Parent:** `Top_5_Impact_Attack_Index_v0_1_20260523.md` #2

---

## §1. Problem

After unimodular projection (§22.15), residual $\Lambda_{\rm NTE}\sim10^{83}\times\Lambda_{\rm obs}$ at $a_4$ level (S2-D). Paper S3 must close **~83 orders** without:

- tuning $f_4\sim10^{-121}$ (M1 **falsified**),
- naive Hopf area heuristic (M2 **falsified**),
- O(1) $\beta_{\rm GB}$ seam alone (M3 **falsified**).

---

## §2. Suppression budget (script)

| Stage | $\Lambda$ [GeV$^4$] | $\log_{10}(\Lambda/\Lambda_{\rm obs})$ |
|-------|---------------------|----------------------------------------|
| Observed | $2.8\times10^{-47}$ | 0 |
| Naive $a_0$/Vol | $\sim10^{74}$ | **121** |
| Post-unimodular $a_4$ | $\sim10^{37}$ | **83** |
| **Gap to close** | — | **~83** |

**Target:** derived chain landing within $\lesssim10\times\Lambda_{\rm obs}$ with **no continuous tune**.

---

## §3. Attack routes

### R1 — Structural $f$ from spectral triple (M1, primary)

**Mechanism:** CC2008 exponential cutoff on $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$:

$$f_k = \int_0^\infty e^{-k\Lambda^2}\,d\Lambda$$

On round $S^3\times S^1$, **$a_{2n}=0$ for $n\ge2$** — higher heat-kernel coefficients vanish; gravitating CC enters through **$f_0 a_4$** with weight fixed by **derived** $f$, not fit.

**Deliverable (Jammer/Scratch):** compute $f_0,f_2,f_4$ moments from NTE Dirac spectrum (S2-A) + CC2008 prescription.

**Register:** relative weights **closed** once $f$ derived; absolute $\Lambda_{\rm NTE}$ still needs R2–R4.

### R2 — $d\mu(V)$ from Friedmann + $\Phi(N)$ trajectory (§22.15)

**Mechanism:** Unimodular leaves $d\mu(V)$ free; NTE fixes it via $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ history — **not** $\Lambda_{\rm obs}$ import.

**Coupling to Impact #1:** $H_{\rm GB}^{(\alpha)}$, $N_e$, $\Phi(N)$ trajectory set volume distribution over cosmic history.

**Deliverable:** map $\Phi(N)\to d\mu(V)\to \Lambda_{\rm NTE}^{\rm residual}$.

### R3 — CC2008 exponential tail $a_6+$ (M5)

**Mechanism:** Remaining modes beyond $a_4$ contribute **exponentially small** terms on $S^3\times S^1$ — potential $\sim10^{80}$–$10^{90}$ suppression if spectral gap large enough.

**Deliverable:** explicit $a_6,a_8$ on NTE $M$ (Paper S3/S4).

### R4 — Hopf holographic area law (M2, derived)

**Mechanism:** Replace falsified OOM heuristic with **Ryu–Takayanagi / dS horizon** on $S^3$ (P-dS1): $\Lambda_{\rm eff}\propto 1/S_{\rm GH}$ not Vol$^{-1}$.

**Anchor:** $S_{\rm GH}\sim O(1)$ vs Dirac dim $\sim10^{27}$ — **log(dim)** not dim.

**Deliverable:** tie M2 to P-dS1/P-dS3 modular entropy programme.

### R5 — M3 $\beta_{\rm GB}$ boundary + C¹ kink (sign)

**Mechanism:** Extrinsic curvature at gauge-birth seam on $S^1_{\beta_{\rm GB}}$ — **negative** counter-term candidate (M3 scaffold).

**Register:** sign programme only until Jammer derives $\mathcal{K}_{\beta_{\rm GB}}$.

---

## §4. Combined stack (honest)

$$\Lambda_{\rm obs} \stackrel{?}{=} \underbrace{\mathcal{P}_{\rm uni}[f_4a_0]}_{\rm removed} \times \underbrace{f_0 a_4}_{\sim10^{83}} \times \underbrace{\mathcal{S}_{\rm struct}}_{\rm R1–R5 product}$$

**Required $\mathcal{S}_{\rm struct}\sim10^{-83}$** from **derived** factors only.

| Route | Max plausible (v0.1) | Status |
|-------|----------------------|--------|
| R1 $f$ moments | Fixes **ratios** O(1); **does not** close 83 OOM | **Done v0.1** (S3-f2) |
| R2 $d\mu(V)$ | Trajectory **specifies** measure; **does not** close 83 OOM alone | **Done v0.1** (S3-f3) |
| R3 $a_6+$ | CC2008 tail **$\sim 0.2$** at canonical $\mu\Lambda$ — **does not** close 83 OOM | **Done v0.1** (S3-f4) |
| R4 RT / $S_{\rm GH}$ | Replaces failed M2 heuristic | Open |
| R5 M3 boundary | O(1)–$10^3$ — insufficient alone | Sign open |

**Discipline:** no ship claim until single chain with falsifiers passes.

---

## §5. Falsifiers

1. Derived $\Lambda_{\rm NTE}$ wrong sign vs acceleration  
2. Breaks $\kappa_0$, $n_s$, F1 $a_4=270\beta_{\rm GB}$  
3. Hidden tune parameter in §XVII register  
4. $f_4^{\rm req}\sim10^{-121}$ presented as solution (forbidden)

---

## §6. Deliverables checklist

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S3-f1 | This attack route + budget script | Cursor | **Done v0.1** |
| S3-f2 | Compute $f_k$ from S2-A spectrum | Scratch | **Done v0.1** |
| S3-f3 | $d\mu(V)$ from $\Phi(N)$ | Jammer | **Done v0.1** |
| S3-f4 | $a_6+$ on $M$ | Paper S4 | **Done v0.1** |

---

## §7. Cross-references

- `Paper_S3_Lambda_M1_M2_Worksheet_v0_1`, M3 scaffold, S2-D  
- §17.5.18, §22.15, §22.20; P-dS1 (M2 link)

— Cursor Paper S3 structural $f$ v0.1, 2026-05-23.
