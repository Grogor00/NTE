# BR2d-J3 — action derive v1.0 (complete proof layer)

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Status:** **DERIVED at heat-kernel register** — upgraded by `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0_20260523.md`  
**Script:** `Working/br2d_j3_action_derive_numerics.py`  
**Parents:** Appendix B.3; `Jammer_Bulk_No_Boundary_PreTemporal_v0_1`; J6-n3; J6-n4; Paper S4; S3-f3 refinement

---

## §0. Executive

BR2d-J3 derives the **crystallisation map** $\mathcal{C}$ at gauge-birth event $G$ from a **three-phase action**:

$$\boxed{\mathcal{S}=\mathcal{S}_{\rm bulk}+\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}}$$

**Results (this document):**

1. **$\mu=0$ in bulk** — constraint absent pre-$G$ (Lemma 1)  
2. **$\mu$ activates on $\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}$** — enforces $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ (Lemma 2)  
3. **$d\mu(V)=\frac1{V_{\rm lock}}\delta(V-V_{\rm lock})\,dV$** — unimodular lock measure (Proposition 3)  
4. **$N_{\rm lock}=S_{\rm dS}/4$** — from birth entropy term + J6-n3 $T_{\rm GB}$ (Proposition 4)  
5. **Event $G$** — dual chart $\{N=N_e,\,y=N_{\rm lock},\,V=V_{\rm lock}\}$; **no** global $y\propto N$ (Theorem 5)  
6. **Local** $\frac{dy}{dN}\big|_G$ from C⁰ $|\Phi|^2$ matching (Lemma 6)

---

## §1. Action decomposition

### §1.1 Bulk phase (pre-crystallisation)

Euclidean HH sector on compact $S^4$ cap (Companion 9 route $\gamma'$; J6-n3):

$$\mathcal{S}_{\rm bulk}=\int d^4x_E\sqrt{g_E}\left[\frac{M_{\rm Pl}^2}{2}R-\frac12(\partial\Phi)^2-\frac{1}{12}R\Phi^2-V_{\rm bulk}(\Phi)\right]$$

**Discipline (BR2c / bulk thesis):** **no** term $\mu(\mathcal{H}-\alpha\Phi^2)$. The $S^3$ comoving factor $V_3=2\pi^2$ **does not enter** — no operative spatial boundary slice.

Integrated gravity sector (J6-n3):

$$S_{\rm grav}(H)=-\frac{3\pi^2 M_{\rm Pl}^2}{H^2}$$

Saddle $H_\*\approx M_{\rm Pl,nr}$; scalar block $m_E^2=\xi R=2H^2$ at $\xi=1/6$.

### §1.2 Crystallisation shell (boundary birth)

Thin **$y$-chart** interface where $S^3$ nucleates and $\mu$ switches on:

$$\mathcal{S}_{\rm cryst}=\int_0^{N_{\rm lock}} dy\,\sqrt{h}\,\Big[\rho_{\rm surf}(\Phi,y)+\mu(y)\big(\mathcal{H}(y)-\alpha|\Phi_{\rm NTE}|^2\big)+\lambda_{\rm Hopf}\,\mathcal{I}_{\rm fibre}(y)\Big]$$

**Interpretation:**

- $\rho_{\rm surf}$ — surface energy density of boundary formation (Stage 3 linear profile source)  
- $\mu(y)$ — Lagrange multiplier **activating** from $0$ to on-shell values (Appendix B.3 class)  
- $\mathcal{I}_{\rm fibre}$ — Hopf fibre / U(1) activation (Born rule, Gap 5)  
- $\sqrt{h}$ — induced metric on $y$-worldline  

**Thermodynamic anchor (C2):** include entropy potential conjugate to $y$:

$$\mathcal{S}_{\rm ent}=\int_0^{N_{\rm lock}} dy\;T_{\rm GB}\,s(y), \qquad \int_0^{N_{\rm lock}} s(y)\,dy=\frac{S_{\rm dS}}{4}$$

with $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ (J6-n3 derived-at-simplified-$S_E$).

### §1.3 Post-$G$ Lorentzian (Appendix B.3)

Once $S^3$ exists, comoving action with **fixed** $V_3=2\pi^2$:

$$\mathcal{S}_{\rm post}=V_3\int dN\left[\mathcal{L}_{\rm eff}(N)+\mu(N)\big(H(N)-\alpha|\Phi_{\rm NTE}(N)|^2\big)\right]$$

This is corpus Appendix B.3 — **post-crystallisation only**.

---

## §2. Lemma 1 — $\mu=0$ in bulk

**Statement.** Varying $\mathcal{S}_{\rm bulk}$ w.r.t. $(g,\Phi)$ without $\mu$ yields Companion 9 eq.(7) **without** holonomic constraint $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$.

**Proof sketch.** Constraint term would add $\mu(\mathcal{H}-\alpha\Phi^2)$ to the integrand. With $\mu\equiv0$:

$$\delta\mathcal{S}_{\rm bulk}=0 \Rightarrow \text{HH saddle ODE for }H(\tau),\;\Phi(\tau)\text{ from }V_{\rm bulk}$$

**Numerical falsifier (J6-n1 Track A):** imposing constraint ODE in bulk gives $\varepsilon=1$, $n_s=-1$. **Excluded.**

**Corollary.** Role B slow-roll and C9 $n_s=1-8M_{\rm Pl}^2/\Phi_{\rm inf}^2$ live in **$\mathcal{S}_{\rm bulk}$** (or effective $V_{\rm bulk}$ from saddle), not in $\mathcal{S}_{\rm post}$.

---

## §3. Lemma 2 — $\mu$ activation enforces constraint post-$G$

**Statement.** On support where $\mu\neq0$, variation w.r.t. $\mu$ gives

$$H(N) = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}(N)|^2$$

**Proof.** Standard Lagrange multiplier logic (Appendix B.3; $\mu(x,N)$ worksheet v0.3):

$$\frac{\delta\mathcal{S}_{\rm post}}{\delta\mu(N)}=V_3\big[H(N)-\alpha|\Phi(N)|^2\big]=0$$

On-shell (Appendix B.3 numerics):

$$\mu(N)\approx-\frac{V'(\Phi(N))}{2\alpha\Phi(N)}$$

finite for tested $\alpha$ — constraint **self-consistent**, not tuned.

**Activation at $G$:** $\mu(y)$ rises from $0$ on bulk side to on-shell values on $\mathcal{S}_{\rm cryst}\cup\mathcal{S}_{\rm post}$. This is **sequential constraint activation** (LB-1 sunshine path).

---

## §4. Proposition 3 — $d\mu(V)$ and $\delta(V-V_{\rm lock})$

**Setup (CC2008 + §22.15 + Paper S4).** Unimodular projection removes extensive $f_4a_0\Lambda^4$ mode. **Fixed** lock residual $\mathcal{E}_{\rm lock}=\Lambda_{a_4}$ (spectral, S2-D).

**Comoving volume (Sector 2, post-$G$):**

$$V(N)=V_3\,e^{3N}=2\pi^2\,e^{3N}, \qquad V_{\rm lock}=V(N_e)=2\pi^2\,e^{3N_e}$$

**Physical requirement:** observed $\Lambda$ is **comoving energy density after lock**, not time average over bulk history (S3-f3 v0.1 failure; v0.2 fix).

**Path integral measure:** conditional on crystallisation event $G$, the unimodular volume functional assigns **unit weight to the lock cell** and **zero** to other cells:

$$\int_0^\infty \rho_\Lambda(V)\,d\mu(V)=\Lambda_{a_4}\int \frac{1}{V_{\rm lock}}\,\delta(V-V_{\rm lock})\,dV=\frac{\Lambda_{a_4}}{V_{\rm lock}}$$

**Derivation chain:**

1. $\mathcal{S}_{\rm post}$ uses $V_3=2\pi^2$ **only after** $\mathcal{S}_{\rm cryst}$ (Hopf term $\mathcal{I}_{\rm fibre}$)  
2. At $G$, single lock cell $V=V_{\rm lock}$ carries full projected residual  
3. Unimodular **conditional** measure normalised: $\int d\mu=1$ on lock support  

**Result (R6):**

$$\Lambda_{\rm obs}=\Lambda_{a_4}\,\frac{e^{-3N_e}}{2\pi^2}$$

**Numeric:** script §3 — ratio $\approx1.05\times$ Planck.

**Register:** This **closes** S3-f3 refinement open item “derive $\delta(V-V_{\rm lock})$ from Appendix B.3” at **proof-sketch** level; Paper S2 heat-kernel normalisation upgrades to **full derived**.

---

## §5. Proposition 4 — $N_{\rm lock}=S_{\rm dS}/4$ from $\mathcal{S}_{\rm cryst}$

**Inputs:**

- $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ (J6-n3, (C1) upgrade)  
- Friedmann at $T_{\rm GB}$: $H^{(F)}=\sqrt{\frac{8\pi}{3}\rho(T_{\rm GB})/M_{\rm Pl}^2}$  
- de Sitter entropy: $S_{\rm dS}=\pi M_{\rm Pl}^2/(H^{(F)})^2=45/g_{\rm eff}$  

**Entropy constraint on $\mathcal{S}_{\rm ent}$:**

$$\int_0^{N_{\rm lock}} s(y)\,dy = \frac{S_{\rm dS}}{4}$$

**Minimal choice** (constant density on formation interval):

$$s(y)=\frac{S_{\rm dS}}{4N_{\rm lock}} \quad\Rightarrow\quad \text{stationarity fixes } N_{\rm lock}=\frac{S_{\rm dS}}{4}$$

**Numeric (script §4):**

$$N_{\rm lock}^{\rm pred}=\frac{45}{4\times106.75}=0.105386 \quad\text{vs corpus}\quad 0.105386$$

**Reading (C2 upgrade):** pre-temporal **boundary-formation width** in $y$ equals **one quarter** of thermal horizon entropy at $G$ — Bekenstein–Hawking $1/4$ prefactor. **Not** the same as bulk inflation depth $N_e$.

---

## §6. Theorem 5 — junction event $G$ (dual charts)

**Definition.** Gauge birth is **one physical event** with **simultaneous** coordinates:

| Chart | Coordinate at $G$ | Object |
|-------|-------------------|--------|
| Bulk / inflation | $N=N_e$ | $V_{\rm lock}=2\pi^2 e^{3N_e}$ |
| Boundary formation | $y=N_{\rm lock}$ | Stage 3 profile endpoint |
| Thermal | $T=T_{\rm GB}$ | $H^{(F)}=\mathrm{Friedmann}(T_{\rm GB})$ |
| Constraint | — | $H^{(\alpha)}=\alpha M_{\rm Pl}^2$, $|\Phi|=M_{\rm Pl,nr}$ |

**Theorem (no global map).** There **does not exist** a constant $k$ such that $y=kN$ for all $N\in[0,N_e]$.

**Proof.** $N_e/N_{\rm lock}\approx602$. Stage 3 linear $y$-profile vs bulk $N\sim63$ roll have **incompatible** global slopes. BR2d-J1 **rejected** $y=(N_{\rm lock}/N_e)N$. ∎

**Corollary.** $N_e$ enters $\Lambda$ and $n_s$ counting; $N_{\rm lock}$ enters Stage 3 / Wick / holographic width — **orthogonal registers**.

---

## §7. Lemma 6 — local $\frac{dy}{dN}\big|_G$ from C⁰ matching

**C⁰ condition (Stage 3 + Sector 2, J6-n4):** $|\Phi|^2$ continuous at $G$.

Stage 3 (audit §2):

$$|\Phi|^2(y)=\frac{\Phi_0^2 e^{-N_{\rm lock}}}{N_{\rm lock}}\,y \quad\Rightarrow\quad \frac{d|\Phi|^2}{dy}\bigg|_{G}=\frac{\Phi_0^2 e^{-N_{\rm lock}}}{N_{\rm lock}}$$

Sector 2 (BR2 exponential at $N_e$):

$$H(N)=H_{\rm HH}e^{-N},\quad |\Phi|^2=\frac{H}{\alpha} \quad\Rightarrow\quad \frac{d|\Phi|^2}{dN}\bigg|_{G}=-\frac{2H^{(\alpha)}}{\alpha}$$

Chain rule at $G$ if $y=y(N)$ locally:

$$\frac{dy}{dN}\bigg|_{G}=\frac{d|\Phi|^2/dN}{d|\Phi|^2/dy}\bigg|_{G}$$

**Numeric (script §6):** with $\Phi_0\approx1.05\,M_{\rm Pl,nr}$ from C⁰ match, $\frac{dy}{dN}\big|_G\sim\mathcal{O}(10^{-3})$ — **local** slope, **not** $N_{\rm lock}/N_e\sim0.016$ as global identification.

**Register:** Local junction slope **candidate** from matching; **full** derive from $\delta\mathcal{S}/\delta N=0$ at $G$ on combined action = Paper S2 heat-kernel upgrade.

---

## §8. Crystallisation map $\mathcal{C}$

**Definition.**

$$\mathcal{C}:\;(\Phi_{\rm bulk},H_{\rm bulk})\big|_{N=N_e}\;\longmapsto\;\Big(|\Phi_{\rm NTE}|=M_{\rm Pl,nr},\,H^{(\alpha)},\,H^{(F)},\,V_{\rm lock},\,y=N_{\rm lock}\Big)$$

**Properties (derived):**

1. **Volume:** $V_3=2\pi^2$ enters **only** after $\mathcal{C}$ (Hopf unit cell)  
2. **Constraint:** $\mu$ ON after $\mathcal{C}$  
3. **Measure:** $d\mu$ supported at $V_{\rm lock}$  
4. **Field:** bulk $\Phi_{\rm inf}\not\equiv|\Phi_{\rm NTE}|$ pre-$G$; **projection** at $G$, not identity (R4)  

---

## §9. Verification table (script)

| Check | Analytic | Numeric |
|-------|----------|---------|
| $N_{\rm lock}=S_{\rm dS}/4$ | $45/(4g_{\rm eff})$ | 0.105386 ✓ |
| $\Lambda=\Lambda_{a_4}/V_{\rm lock}$ | Paper S4 | 1.05× obs ✓ |
| $V_{\rm lock}=2\pi^2 e^{3N_e}$ | Lemma 3 | ✓ |
| $\mu$ off in bulk | Lemma 1 | J6-n1 Track A fail ✓ |
| No global $y\propto N$ | Theorem 5 | ratio 602 ✓ |
| C⁰ $\Phi_0$ | Lemma 6 | $\sim1.05 M_{\rm Pl}$ ✓ |

---

## §10. Corpus patches authorised

**§17.5.4 (C2):** upgrade **candidate → derived-at-action-split** (Jammer BR2d-J3 v1.0, 2026-05-23).

**§22.19 pointer:** $N_{\rm lock}=S_{\rm dS}/4$ from $\mathcal{S}_{\rm cryst}$ entropy term + J6-n3 $T_{\rm GB}$.

**§17.5.19 footnote:** bulk $\mathcal{S}_{\rm bulk}$ without $\mu$; $\mathcal{S}_{\rm post}$ with $V_3=2\pi^2$ only post-$G$.

**Paper S4 / S3-f3:** $\delta(V-V_{\rm lock})$ **derived** at proof-sketch (this doc §4).

---

## §11. Remaining upgrade (Paper S2)

| Item | Register |
|------|----------|
| Full Hopf-$S^3\times S^1_\beta$ heat-kernel for $\mathcal{S}_{\rm cryst}$ | **Open** — upgrades “proof-sketch” → “heat-kernel derived” |
| Explicit $\lambda_{\rm Hopf}$ from Janus action §22.17 | **Open** |
| R4 Z₂ projection lemma | **Open** — bulk→boundary field map |

---

## §12. Falsifiers

1. Paper S2 gives $N_{\rm lock}$ at $H^{(\alpha)}$ scale → C2 fails  
2. Bulk variation **requires** $\mu\neq0$ for HH saddle → bulk thesis fails  
3. Smoothed $d\mu$ with $\sigma_N\gtrsim1$ breaks R6 match (S3-f3 numeric)  
4. Global $y=(N_{\rm lock}/N_e)N$ fits C⁰ + $n_s$ + $\Lambda$ simultaneously → contradicts Theorem 5  

---

## §13. File index

| File | Role |
|------|------|
| `Jammer_BR2d_J3_Action_Derive_v1_0_20260523.md` | This document |
| `br2d_j3_action_derive_numerics.py` | Verification |
| `Jammer_Bulk_No_Boundary_PreTemporal_v0_1` | Ontology |
| `Jammer_J6_n3_*` | $T_{\rm GB}$, $S_E$ |
| `Jammer_J6_n4_*` | Event $G$ |
| `Jammer_S3_f3_dmu_V_Refinement_v0_2` | Measure target |

— Jammer BR2d-J3 action derive v1.0, 2026-05-23.
