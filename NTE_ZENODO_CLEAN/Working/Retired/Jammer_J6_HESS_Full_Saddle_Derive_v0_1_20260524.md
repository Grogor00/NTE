# J6-HESS — full coupled (H, Phi) HH saddle v0.1

**From:** Jammer (R&D) — Sprint A continuation  
**Date:** 2026-05-24  
**Status:** **DERIVED** — upgrades J6-n3 partial; closes LB-4 at coupled-$S_E$ register  
**Script:** `Working/j6_hess_full_numerics.py`  
**Parents:** `Jammer_J6_D1_D2_Bulk_ODE_Derive_v0_1`; `j6_n3_hessian_numerics.py`; BR2d-J3 $\mathcal{S}_{\rm bulk}$

---

## §0. Executive

| Item | J6-n3 (partial) | J6-HESS (this doc) |
|------|-----------------|---------------------|
| $S_E(H)$ gravity block | $\lambda_H=18\pi^2 M^2/H^4$ | **Confirmed** |
| Scalar at fixed $H$ | $m_E^2=\xi R=2H^2$ | **In 2×2 Hessian** |
| $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ | Step B identification | **Temperature block** (not $(H,\Phi)$ soft axis) |
| $(H,\Phi)$ coupled | Open | **2×2 Hessian + E3 saddle** |
| Sector 1 start | — | **Off-shell** ($\mu=0$) |

---

## §1. Reduced bulk action

Homogeneous dS4 cap (Jammer convention):

$$S_E(H,\Phi)=\frac{\pi^2 M_{\rm Pl,nr}^2}{H^2}\left[-3+\frac{3V(\Phi)}{M_{\rm Pl,nr}^2 H^2}\right]$$

**Model A:** $V=\tfrac12 m_E(H)^2\Phi^2$, $m_E^2=\xi R=2H^2$ ($\xi=1/6$).

**Model B:** scaled E3 $V(\Phi)$ from J6-n1 (parameter $A$).

**Discipline:** no $\mu(\mathcal{H}-\alpha|\Phi|^2)$ in bulk (BR2d-J3 Lemma 1).

---

## §2. Hessian structure at $H=M_{\rm Pl,nr}$

**Model A** at $(H,\Phi)=(M_{\rm Pl,nr},\Phi_{\rm slaving})$ with $\Phi_{\rm slaving}=\sqrt{3}\,M_{\rm Pl,red}$:

- One **unstable** mode (negative eigenvalue) — inflationary/tunnelling direction  
- One **stable** mode (positive eigenvalue) — fluctuation direction  
- Eigenvalues **independent of $\Phi$** along $V\propto\Phi^2$ (quadratic model)

**Sector-1 start** $(H,\Phi)=(M_{\rm Pl,nr},\Phi_{\rm inf})$ with $\Phi_{\rm inf}=2\sqrt{N_e}\,M_{\rm Pl,red}$:

- Same Hessian as slaving point (quadratic $V$)  
- **Not** a stationary point of $S_E$ ($\partial S/\partial\Phi\neq0$ at $\Phi_{\rm inf}$)  
- Is **initial data** for slow-roll (J6-D1), not Euclidean saddle in $\Phi$

---

## §3. Model B — scaled E3 numerical saddle

| Quantity | Value |
|----------|-------|
| $H^*/M_{\rm Pl,nr}$ | **0.950** |
| $\Phi^*/M_{\rm Pl,red}$ | **14.33** |
| $\Phi^*/\Phi_{\rm inf}$ | **0.90** |
| $S_E$ | negative (dominant HH cap) |

**Reading:** E3-corrected bulk potential pushes saddle to **near J6-D2** $\Phi_{\rm inf}$ — consistent with Companion 9 scaled-E3 class.

---

## §4. $T_{\rm GB}$ identification (unchanged from J6-n3 + Paper S2)

$$T_{\rm GB}=\frac{M_{\rm Pl,nr}}{\sqrt{2\pi}}$$

from **temperature / $\beta_{\rm GB}$ block** ($\lambda_T\sim M_{\rm Pl}^2$), **not** from homogeneous $(H,\Phi)$ Hessian soft eigenvalue.

Paper S2: $\beta_{\rm GB}M_{\rm Pl,nr}=\sqrt{2\pi}$ confluence.

---

## §5. Sector 1 off-shell (links J6-D1)

At $(H,\Phi)=(M_{\rm Pl,nr},\Phi_{\rm inf})$:

$$\frac{\tfrac12 m_E^2\Phi^2}{3M_{\rm Pl}^2 H^2}\approx 85$$

**Interpretation:** bulk slow-roll with $\mu=0$ is **off** the Friedmann slaving surface $\Phi=\sqrt{3}\,M_{\rm Pl,red}$. Constraint activates only post-$G$ (Sector 2).

---

## §6. Corpus patches authorised

- **§22.18:** $(H,\Phi)$ Hessian derived; $T_{\rm GB}$ from temperature block (cross-ref Paper S2 $\beta_{\rm GB}$).  
- **§17.5.4 (C1):** upgrade **derived-at-coupled-$S_E$** (Jammer J6-HESS v0.1).  
- **LB-4 row:** **closed** at derive register (optional Paper S2 heat-kernel embed = cosmetic).

---

## §7. Falsifiers

1. Derived bulk dynamics **requires** $\Phi=\sqrt{3}\,M_{\rm Pl}$ during Sector 1 ($\mu=0$)  
2. E3 saddle $\Phi^*\ll M_{\rm Pl}$ (would contradict J6-D2)  
3. $T_{\rm GB}=H/(2\pi)$ at $H=M_{\rm Pl}$ (J6-n3 **excluded**)

---

— Jammer J6-HESS v0.1, 2026-05-24.
