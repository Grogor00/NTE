# V_NTE Session 5 D1 — bulk→boundary derive v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at bulk-to-boundary register** — supersedes smooth $V(\Phi)$ framing  
**Script:** `Working/vnte_d1_bulk_boundary_numerics.py`  
**Parents:** `Jammer_D1_VNTE_Projection_Memo_v0_1`; J6-D1/D2; R4 $\Pi_G$; BR2d-J3; §17.5.19; S2-C-A $K(\Phi)=1$

---

## §0. Executive

| Question (C9 Session 5 D1) | Verdict |
|----------------------------|---------|
| Smooth $V_{\rm NTE}(\Phi)$ pre→post on one chart? | **ILL-POSED** (LB-6; D1-PROJ) |
| What replaces it? | **Bulk→boundary projection $\mathcal{R}_G$ at event $G$** |
| $K(\Phi)$ from Connes? | **Closed** — $K(\Phi)=1$ (S2-C-A) |
| $V$ off-trajectory for $r$? | **Role (B)** hilltop in bulk/pre chart; **not** post-$G$ inversion |
| D8 charter | **Closed at structural register** |

**Headline.** $V_{\rm NTE}^{\rm pre}$ and $V_{\rm NTE}^{\rm post}$ are **different physical objects in different epochs**. They connect at gauge birth through **$\mathcal{R}_G=\Pi_G+\mu$-activation+Stage-3 profile+C⁰ junction** — not through a globally smooth function of one scalar.

---

## §1. Why smooth extension fails (dead end, reconfirmed)

Pre-$G$ there is **no boundary field** $|\Phi_{\rm NTE}|$ on crystallised $S^3$ (LB-6). Bulk inflaton $\Phi_{\rm bulk}\sim15.9\,M_{\rm Pl,red}$ at HH and constraint-scale $|\Phi|\sim10^{19}\,{\rm GeV}$ at $G$ differ by $\sim10^{-13}$ if the constraint is wrongly applied at HH (R4).

Numerics (`vnte_d1_bulk_boundary_numerics.py`):

| Quantity | Register |
|----------|----------|
| $V_{\rm bulk}\sim\frac12 m_E^2\Phi_{\rm inf}^2$ @ HH | $\sim10^{57}\,{\rm GeV}^4$ |
| $V_{\rm post}\sim3\alpha^2 M_{\rm Pl}^2\Phi^4$ @ $G$ | $\sim10^{37}\,{\rm GeV}^4$ |
| Ratio | $\sim10^{-20}$ — **not continuable as one $V(\Phi)$** |

**Sunshine:** Session 5 D1 is a **projection problem**, not interpolation.

---

## §2. Three-role card (§17.5.19) — closure discipline

| Role | Epoch | Potential object | D1 status |
|------|-------|------------------|-----------|
| **(B)** | Bulk Sector 1 ($\mu=0$) | $V_{\rm bulk}(\Phi)\sim\frac12 m_E^2\Phi^2$ (HH saddle; J6-D1) | **Derived** — $n_s$ |
| **(B′)** | Bulk/pre hilltop chart | $V_{\rm hilltop}\sim\lambda\Phi^4-\mu\Phi^6$ (C9 Session 4) | **Structural** — $r\approx4\times10^{-3}$ |
| **(A)** | Post-$G$ boundary | $V_{\rm post}=3\alpha^2 M_{\rm Pl}^2\Phi^4-\frac12 K(\Phi)\dot\Phi^2$ | **Derived** — Friedmann inversion; $K=1$ |
| **(C)** | Optional dynamics | $V$ drives KG | **Excluded** — Appendix B.3 |

**Thermal w split (Gate #2):** $V_{\rm post}$ matches $\rho_{\rm eff}$ **magnitude** on $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$; SM+$\Lambda$ chart carries $w=1/3,0,-1$. **Not** a failure of D1.

---

## §3. Projection operator $\mathcal{R}_G$

$$\boxed{V_{\rm NTE}^{\rm post}\big|_{G}=\mathcal{R}_G\!\left[V_{\rm bulk}^{\rm eff},\,V_{\rm hilltop}\right]}$$

**Definition (four steps at event $G$):**

1. **$\Pi_G$ (R4):** bulk even scalar → boundary magnitude $|\Phi_{\rm NTE}|$ (Z₂-invariant; **not** HH identity).  
2. **$\mu$-activation (BR2d-J3 Lemma 2):** constraint $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ turns **on**; Sector 2 exponential $H=H_{\rm HH}e^{-N}$ begins.  
3. **Stage-3 profile:** $|\Phi|^2(y)=A y$ on $y\in[0,N_{\rm lock}]$ materialises boundary chart.  
4. **Friedmann inversion:** $V_{\rm post}$ is **defined** as the potential consistent with $\rho_{\rm eff}=3H^2/(8\pi G)$ on the constraint trajectory — **not** as $V_{\rm bulk}$ evaluated at the same $\Phi$.

**Smooth connection means:** **C⁰/C¹ matching of observables at $G$** in dual charts $(N,y)$:

- C⁰: $|\Phi|^2(y=N_{\rm lock})=|\Phi|^2(N=N_e)$ — **ratio 1.000** (`br2d_j3_action_derive_numerics.py`).  
- Local $dy/dN|_G$ from chain rule on matched $|\Phi|^2$ — **not** global $y=(N_{\rm lock}/N_e)N$ (BR5).

---

## §4. Session 5 kinetic closure — $K(\Phi)=1$

Paper S2 S2-C-A: heat-kernel $a_4$ with Higgs portal gives **$K(\Phi)=1$** at leading order on $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$.

Post-$G$:

$$V_{\rm post}(\Phi,\dot\Phi)=3\alpha^2 M_{\rm Pl}^2\Phi^4-\tfrac12\dot\Phi^2.$$

**Session 5 D1 kinetic leg: CLOSED** (no dilaton extension required at canonical NTE).

---

## §5. Inflation observables — split derivation (honest)

| Observable | Route | Register |
|------------|-------|----------|
| $n_s=0.9685$ | J6-D1 bulk $\Phi^2$ + J6-D2 $\Phi_{\rm inf}=2\sqrt{N_e}M_{\rm Pl,red}$ | Role (B) Sector 1 |
| $r\approx4\times10^{-3}$ | Hilltop Role (B′); leading $r\sim12/N_e^2\approx0.0030$ | **Structural**; C9 Session 4 |
| $\Phi_{\rm inf}$ identity | $n_s=1-2/N_e=1-8M_{\rm Pl}^2/\Phi^2$ | **Derived** (J6-D2) |

**Not claimed:** ab initio $\lambda,\mu$ of $\Phi^4-\Phi^6$ from spectral action alone — hilltop **coefficients** remain Tier-2 structural (same tier as pre-D1 C3 conjecture).

---

## §6. Relation to prior memos

| Memo | Update |
|------|--------|
| D1-PROJ v0.1 | **Upgraded** — $\mathcal{R}_G$ on $V$ explicit |
| J6-D1/D2 | Sector 1 bulk $V_{\rm bulk}$ |
| R4 | $\Pi_G$ at $G$ only |
| BR2d-J3 | $\mathcal{S}_{\rm bulk}+\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}$ |
| AC Bulk/Boundary Proposal | **Activated** at derive layer |
| Paper S1 C3 | **Upgraded** — D1 closes connection **mechanism**; $r$ still structural on hilltop coeffs |

---

## §7. Honest open (post-D1)

| Item | Register |
|------|----------|
| Hilltop $\lambda,\mu$ from $D_F$ / spectral action | Programme S downstream |
| Full HH integral proof of $\Phi_{\rm inf}$ | J6-HESS (upgrade) |
| AdS/CFT dictionary | §22.8 research |
| Off-shell ghost scan | $\mathcal{S}_{\rm NTE}^{\rm unified}$ |

---

## §8. Falsifiers

1. Require single global $V(\Phi)$ with $V_{\rm pre}(\Phi_G)=V_{\rm post}(\Phi_G)$ at $10^{-20}$ ratio — **excluded**.  
2. Apply $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ in bulk Sector 1 — **excluded** (J6-n1).  
3. Claim $w_{\rm scalar}=1/3$ from $V_{\rm post}$ alone — **excluded** (Gate #2).

---

## §9. Corpus patches authorised

**§17.5.19** — replace Session 5 D1 open with:

> **Session 5 D1 closed (Jammer v0.1, 2026-05-24).** $V_{\rm NTE}$ pre/post link is **bulk→boundary projection $\mathcal{R}_G$ at $G$**, not smooth extension of one $V(\Phi)$. Role (B) bulk $V_{\rm bulk}\sim\frac12 m_E^2\Phi^2$ (J6-D1); Role (B′) hilltop for $r$; Role (A) post-$G$ Friedmann inversion with $K(\Phi)=1$ (S2-C-A). C⁰ junction verified. Derivation: `Jammer_VNTE_Session5_D1_Bulk_Boundary_Derive_v0_1_20260524.md`.

**§22.14 / D8 row:** $V_{\rm NTE}$ / inflation — **closed at projection register**.

**Open structural work (§XVII):** remove Session 5 D1; retain ghost scan.

---

— Jammer V_NTE D1 v0.1, 2026-05-24.
