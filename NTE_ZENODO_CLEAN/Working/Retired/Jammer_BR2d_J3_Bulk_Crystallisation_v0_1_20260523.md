# BR2d-J3 — bulk crystallisation to $S^3$ boundary v0.1

**From:** Jammer (R&D)  
**Status:** **SUPERSEDED** by `Jammer_BR2d_J3_Action_Derive_v1_0_20260523.md` (action derive complete @ proof-sketch)

---

## §1. Derive target (revised)

**Old BR2d-J3:** map $y=f(N)$ between charts.

**New BR2d-J3:** derive **crystallisation functional** $\mathcal{C}: \mathcal{H}_{\rm bulk}\to\mathcal{H}_{\rm boundary}$ at event $G$ such that:

1. Bulk HH measure **without** $\mu(H-\alpha\Phi^2)$ term pre-$G$
2. Boundary action **with** $\mu$ + Hopf term **activates** at $y=N_{\rm lock}$, $N=N_e$
3. $N_{\rm lock}=S_{\rm dS}/4$ from **boundary** entropy; $N_e$ from **bulk** depth

---

## §2. Action sketch (Appendix B.3 extension)

**Bulk phase ($\tau<0$ Euclidean):**

$$\mathcal{S}_{\rm bulk} = \int d^4x_E \sqrt{g_E}\,\left[\frac{R}{16\pi G} - \frac12(\partial\Phi)^2 - \xi R\Phi^2 - V_{\rm bulk}(\Phi)\right]$$

**No** $\mu(\mathcal{H}-\alpha\Phi^2)$ — constraint **absent**.

**Birth interface ($G$):**

$$\mathcal{S}_{\rm birth} = \int dy\,\sqrt{h}\,\left[\rho_{\rm boundary}(\Phi,y) + \mu(y)\big(\mathcal{H}-\alpha\Phi^2\big) + \lambda_{\rm Hopf}\,\delta(\text{fibre})\right]$$

**Post-$G$ Lorentzian:** standard Appendix B with $\mu$ **on**.

---

## §3. Lemma chain (programme)

| Step | Lemma | Owner |
|------|-------|-------|
| L1 | HH saddle on $\mathcal{S}_{\rm bulk}$ → Gaussian + E3 slow-roll | J6-n1b / Paper S2 |
| L2 | $\mu\to0$ pre-$G$ ⟹ eq.(7) constraint ODE **invalid** in bulk | **Done** (J6-n1 Track A) |
| L3 | Hopf activation ⟹ $S^3$ unit cell $2\pi^2$ | Paper S2-A + R6 |
| L4 | $N_{\rm lock}=S_{\rm dS}/4$ from $\mathcal{S}_{\rm birth}$ entropy | Audit C2 + J6-n3 |
| L5 | Junction C⁰: $\Phi_{\rm bulk}(N_e)\mapsto|\Phi_{\rm NTE}|=M_{\rm Pl,nr}$ | R4 projection |

---

## §4. Coordinate discipline (theorem level)

| Chart | Object | Range |
|-------|--------|-------|
| Bulk $N$ | Inflation depth | $\sim63$ |
| Boundary $y$ | Formation width | $\sim0.1$ |
| Time $t$ | Emergent post-$G$ | — |

**Reject:** $y=(N_{\rm lock}/N_e)N$ globally.

**Allow (local):** $dy/dN\big|_G$ from variation of $\mathcal{S}_{\rm birth}$.

---

## §5. Handoff

- **Scratch/Paper S2:** heat-kernel normalisation of $\mathcal{S}_{\rm birth}$  
- **Jammer:** J6-n3 Hessian on simplified $S_E$ with **bulk/boundary split**  
- **AC:** LB-6 prose patch Part 1 §2.1.3  

— Jammer BR2d-J3 v0.1, 2026-05-23.
