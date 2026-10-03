# D1-PROJ — $V_{\rm NTE}$ bulk→boundary projection memo v0.1

**From:** Jammer (R&D) — Sprint A item 3  
**Date:** 2026-05-24  
**Status:** **DERIVED** — supersedes smooth-extension framing; see `Jammer_VNTE_Session5_D1_Bulk_Boundary_Derive_v0_1_20260524.md`  
**Parents:** `Jammer_R4_Z2_Projection_Lemma_v1_0`; §17.5.19; AC Proposal §2.4; LB-6

---

## §0. Problem

Companion 9 Session 5 D1 asked for a **smooth** $V_{\rm NTE}(\Phi)$ connecting $V_{\rm NTE}^{\rm pre}$ ($\Phi^4-\Phi^6$) to $V_{\rm NTE}^{\rm post}$ (Friedmann inversion).

**LB-6 verdict:** pre-$G$ there is **no boundary field** $\Phi_{\rm NTE}$ on $S^3$ — the question is **ill-posed** as single-chart function extension.

---

## §1. Sunshine reframe

| Role | Epoch | Object | Potential |
|------|-------|--------|-----------|
| **(B)** | Bulk HH / Sector 1 | $\Phi_{\rm bulk}$ on Euclidean saddle | $V_{\rm bulk}(\Phi)\sim\tfrac12 m_E^2\Phi^2$ (saddle) |
| **(A)** | Post-$G$ boundary | $|\Phi_{\rm NTE}|$ on $S^3$ | $V_{\rm post}$ = Friedmann inversion on $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ |

**Junction at $G$:** $\Pi_G$ (R4) + Stage-3 profile + C⁰ matching — **not** $V_{\rm pre}(\Phi)=V_{\rm post}(\Phi)$.

**Smooth means:** C⁰/C¹ consistency of **physical observables** at $G$ in dual charts $(N,y)$, not a global $V(\Phi)$ on one field.

---

## §2. Projection mechanism (register)

$$\boxed{V_{\rm NTE}^{\rm post} = \mathcal{R}_G\big[V_{\rm bulk}^{\rm eff}\big]}$$

where $\mathcal{R}_G$ comprises:

1. **Z₂ even projection** $\Pi_G: \Phi_{\rm bulk}\mapsto|\Phi_{\rm NTE}|$ (R4 lemma).  
2. **Constraint activation** $\mu\to$ on-shell enforcing $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ (BR2d-J3 Lemma 2).  
3. **Stage-3 linear profile** on $y\in[0,N_{\rm lock}]$ materialising boundary magnitude.  
4. **Friedmann inversion** defining $V_{\rm post}$ on the constraint trajectory post-$G$.

---

## §3. What is **not** claimed

- AdS/CFT dictionary (open research).  
- Identity $V_{\rm bulk}=V_{\rm post}$ at HH ($\sim10^{57}$ ratio in probe).  
- Single $\Phi$ variable for both epochs.

---

## §4. D1 acceptance criteria (revised)

| Criterion | Test |
|-----------|------|
| C⁰ $|\Phi|^2$ at $G$ | J6-n4 / `br2d_j3_action_derive_numerics.py` **PASS** |
| Role discipline | §17.5.19 card **ratified** |
| No smooth-extension requirement | This memo |

**Open derive:** explicit $\mathcal{R}_G$ on $V$ (not only $|\Phi|$) from heat-kernel $\mathcal{S}_{\rm cryst}$.

---

## §5. Corpus sentence (proposed footnote §17.5.19)

> *Session 5 D1 (Jammer v0.1, 2026-05-24): $V_{\rm NTE}$ pre/post connection is a **bulk-to-boundary projection at $G$**, not a smooth extension of one $V(\Phi)$. See `Jammer_D1_VNTE_Projection_Memo_v0_1_20260524.md`.*

---

— Jammer D1-PROJ v0.1, 2026-05-24.
