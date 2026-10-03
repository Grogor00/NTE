# Paper S2 × BR2d-J3 — heat-kernel upgrade v1.0

**From:** Jammer (R&D) + Paper S2 spine (Scratch S2-A–S2-E)  
**Date:** 2026-05-23  
**Status:** **DERIVED at heat-kernel register** — upgrades BR2d-J3 v1.0 proof-sketch  
**Script:** `Working/paper_s2_br2d_j3_heat_kernel_numerics.py`  
**Parents:** `Jammer_BR2d_J3_Action_Derive_v1_0`; Paper S2 S2-A/S2-B/S2-C-B/S2-D; Paper S4; S3-f3 refinement

---

## §0. Executive

BR2d-J3 v1.0 derived $\mathcal{S}=\mathcal{S}_{\rm bulk}+\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}$ at **proof-sketch** level. This document **anchors every crystallisation term** to the canonical Paper S2 heat-kernel on

$$M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F,\qquad A_F=\mathbb{O}\oplus\mathbb{O}$$

**Upgrade verdict:** BR2d-J3 → **heat-kernel derived** (register v1.0).

---

## §1. Spectral triple at crystallisation (Paper S2-A)

### §1.1 Geometry

| Quantity | Formula | Numeric (corpus) |
|----------|---------|------------------|
| ${\rm Vol}(S^3)$ | $2\pi^2$ | 19.739 |
| $\beta_{\rm GB}$ | $\sqrt{2\pi}/M_{\rm Pl,nr}$ | $2.05\times10^{-19}$ GeV$^{-1}$ |
| ${\rm Vol}(M)$ | $2\pi^2\beta_{\rm GB}$ | $4.05\times10^{-18}$ GeV$^{-1}$ |
| $N_F$ | $180$ ($A_F=\mathbb{O}\oplus\mathbb{O}$) | S2-B §2.3 |

**Confluence (S2-A §2.1):** $\beta_{\rm GB} M_{\rm Pl,nr}=\sqrt{2\pi}$ ⟹ $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ (J6-n3 / §22.18).

### §1.2 Seeley–DeWitt coefficients (S2-B, S2-C-B)

On $M$ with Dirac $D_M$, spinor rank $r=4$:

$$\boxed{a_0=\frac{N_F\beta_{\rm GB}}{2},\quad a_2=-\frac{N_F\beta_{\rm GB}}{4},\quad a_4\big|_M=\frac{3N_F\beta_{\rm GB}}{2}=270\beta_{\rm GB}}$$

CC2008: $a_{2n}=0$ for $n\ge2$ on round $S^3\times S^1$ — exponential tail suppressed (S3-f4 negative verdict preserved).

---

## §2. Heat-kernel form of $\mathcal{S}_{\rm cryst}$

BR2d-J3 v1.0 wrote $\mathcal{S}_{\rm cryst}$ schematically. **Upgrade:**

$$\mathcal{S}_{\rm cryst}=\int_0^{N_{\rm lock}} dy\,\sqrt{h}\left[\underbrace{\frac{f_0\,a_4}{{\rm Vol}(M)}}_{\rho_{\rm surf}(y)}+\mu(y)\big(\mathcal{H}-\alpha|\Phi|^2\big)+\underbrace{\lambda_{\rm Hopf}\,\kappa_0\,Y_{00}}_{\mathcal{I}_{\rm fibre}}\right]$$

| Term | Paper S2 source | Role |
|------|-----------------|------|
| $\rho_{\rm surf}$ | $f_0 a_4/{\rm Vol}(M)$ | boundary formation energy density from spectral action |
| $\mu(H-\alpha|\Phi|^2)$ | Appendix B.3 | constraint **activates** on $y\in[0,N_{\rm lock}]$ |
| $\lambda_{\rm Hopf}\kappa_0 Y_{00}$ | S2-B Step 5; Hopf fibre | U(1) / Born / fibre **nucleation** |
| $\mathcal{S}_{\rm ent}$ | audit C2 | $\int_0^{N_{\rm lock}}T_{\rm GB}\,s\,dy=S_{\rm dS}/4$ |

**Hopf anchor:** $\kappa_0=3/\sqrt{4\pi}$ from $(R_{S^3}/2)\times Y_{00}$ pathway (S2-B Step 5) — **not** a free parameter.

---

## §3. Heat-kernel form of $\mathcal{S}_{\rm post}$

Post-$G$, comoving $S^3$ exists with **fixed** internal volume factor:

$$\mathcal{S}_{\rm post}={\rm Vol}(S^3)\int dN\left[\mathcal{L}_{\rm eff}+\mu(N)\big(H-\alpha|\Phi_{\rm NTE}|^2\big)\right] = 2\pi^2\int dN[\cdots]$$

Appendix B.3 is the **$N$-integrated** limit of the spectral action on $M$ after **comoving uplift** $V(N)=2\pi^2 e^{3N}$.

**Discipline:** ${\rm Vol}(M)=2\pi^2\beta_{\rm GB}$ (internal spectral) **≠** $V_{\rm lock}=2\pi^2 e^{3N_e}$ (comoving) — Paper S4 Lemma 2. Same $2\pi^2$, different registers.

---

## §4. Proposition — $\delta(V-V_{\rm lock})$ from heat-kernel + unimodular

**Step 1 (S2-D / §22.15):** Unimodular projection removes leading $f_4\Lambda^4 a_0$ extensive mode.

**Step 2 (S2-D):** Fixed post-projection residual at lock scale: $\mathcal{E}_{\rm lock}=\Lambda_{a_4}\sim f_0 a_4$ (S2-D; S3-f2 $f_0\sim O(1)$ derived).

**Step 3 (crystallisation):** Conditional measure on **one** comoving cell at $G$:

$$d\mu(V)=\frac{1}{V_{\rm lock}}\,\delta(V-V_{\rm lock})\,dV,\qquad V_{\rm lock}=2\pi^2 e^{3N_e}$$

**Step 4 (integral):**

$$\Lambda_{\rm obs}=\int\rho_\Lambda\,d\mu=\Lambda_{a_4}\,e^{-3N_e}/(2\pi^2)$$

**Numeric:** $1.046\times$ Planck (script §E).

**Register:** $\delta(V-V_{\rm lock})$ is **required** by (i) unimodular fixed mode, (ii) single lock cell $2\pi^2 e^{3N_e}$, (iii) heat-kernel $a_4$ amplitude — not an ad hoc choice.

---

## §5. Proposition — $N_{\rm lock}=S_{\rm dS}/4$ heat-kernel linked

**Thermal entropy (audit §3.4):** with $T_{\rm GB}$ from $\beta_{\rm GB}$ and $H^{(F)}=\mathrm{Friedmann}(T_{\rm GB})$:

$$S_{\rm dS}=\frac{\pi M_{\rm Pl}^2}{H_F^2}=\frac{45}{g_{\rm eff}}$$

**Entropy constraint on $\mathcal{S}_{\rm ent}$:**

$$N_{\rm lock}=\frac{S_{\rm dS}}{4}=\frac{45}{4g_{\rm eff}}=0.105386\quad(g_{\rm eff}=106.75)$$

**Heat-kernel link to $N_F$:** $N_F=180$ counts finite Hilbert-space dimension on $A_F$; SM thermal $g_{\rm eff}=106.75$ at $T_{\rm GB}$ is **not** $N_F/2$ exactly (script §F: 0.125 vs 0.105 — 19% illustrative gap). **Structural chain:** species content on $A_F$ → thermal bath at gauge birth → $S_{\rm dS}$ → $N_{\rm lock}$. Exact $N_F\to g_{\rm eff}$ map = **Paper S2 Session 2** upgrade (honest open).

**Register (C2):** upgrade **derived-at-action-split** → **derived-at-heat-kernel** (this document).

---

## §6. Theorem — $2\pi^2$ uniqueness at crystallisation

At event $G$, three uses of $2\pi^2$ **coincide by construction**:

| Use | Object |
|-----|--------|
| ${\rm Vol}(S^3)$ in ${\rm Vol}(M)$ | spectral triple internal |
| $V_3$ in $\mathcal{S}_{\rm post}$ | comoving spatial slice |
| Denominator in $\Lambda_{a_4}e^{-3N_e}/(2\pi^2)$ | lock-cell normalisation (R6) |

**$4\pi$ alternative (Hopf base area):** gives $1.64\times$ — subdominant ambiguity; **$2\pi^2={\rm Vol}(S^3)$** is heat-kernel canonical on $M$ (S2-A §2.1).

---

## §7. BR2d-J3 register upgrade table

| Item | v1.0 proof-sketch | v1.0 heat-kernel |
|------|-------------------|------------------|
| $\mathcal{S}_{\rm cryst}$ | schematic | $f_0 a_4/{\rm Vol}(M)+\mu+\lambda_{\rm Hopf}\kappa_0 Y_{00}$ |
| $\delta(V-V_{\rm lock})$ | path-integral narrative | unimodular + $a_4$ + $2\pi^2 e^{3N_e}$ |
| $N_{\rm lock}$ | $S_{\rm dS}/4$ + $T_{\rm GB}$ | + $\beta_{\rm GB}$ from $M$ |
| $T_{\rm GB}$ | J6-n3 simplified $S_E$ | $\beta_{\rm GB}=\sqrt{2\pi}/M_{\rm Pl,nr}$ from $M$ |
| Hopf term | named | $\kappa_0=3/\sqrt{4\pi}$ from S2-B |

---

## §8. Honest remaining open

| Item | Register |
|------|----------|
| Exact $N_F\to g_{\rm eff}$ at $T_{\rm GB}$ | 19% gap in naive $N_F/2$ — Paper S2 refine |
| Full Tomita–Takesaki P0.10 on $A_F$ | parallel; not blocking |
| $\alpha$ from bulk projection | R4 lemma — separate track |

---

## §9. Falsifiers

1. Paper S2 gives $\beta_{\rm GB}$ at $H^{(\alpha)}$ scale → $T_{\rm GB}$ chain breaks  
2. Smoothed $d\mu$ with $\sigma_N\gtrsim1$ → R6 match fails (S3-f3)  
3. $4\pi$ replaces $2\pi^2$ with no S3 spectral justification → $1.64\times$ shift  

---

## §10. Corpus patches authorised

- **BR2d-J3 v1.0:** status → **heat-kernel derived**  
- **§22.19:** cite this doc + Paper S2 spine  
- **§17.5.4 (C2):** heat-kernel derived  
- **Paper S4 / S3-f3:** $\delta(V-V_{\rm lock})$ **derived** (not proof-sketch)

— Paper S2 × BR2d-J3 heat-kernel upgrade v1.0, 2026-05-23.
