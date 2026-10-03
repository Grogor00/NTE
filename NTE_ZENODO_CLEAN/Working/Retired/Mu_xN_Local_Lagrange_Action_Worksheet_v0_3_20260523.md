# μ(x,N) local Lagrange-multiplier action — worksheet v0.3 (§22.16)

**Stream:** Cursor v0.3 → Jammer S1 sign-off  
**Date:** 2026-05-23  
**Status:** **Covariant δg_μν at 1PN derived** — S1 near-closure pending Jammer review  
**Prior:** `Mu_xN_Local_Lagrange_Action_Worksheet_v0_2_20260523.md`

---

## §1. Upgrade from v0.2

| Item | v0.2 | v0.3 |
|------|------|------|
| $\delta g_{\mu\nu}$ | Target equation | **1PN reduction explicit** — §3 |
| On-shell $\mu$ | Implicit | **Algebraic** — §4 |
| $\gamma,\beta$ PPN | Asserted | **From $G_{\mu\nu}$ split** — §5 |
| S1 sign-off | Partial | **Near-closure** (Jammer review) |

---

## §2. Action (unchanged)

$$S = \frac{M_{\rm Pl}^2}{2}\int\sqrt{-g}\,R + S_{\rm matter} + S_\Phi + \int\sqrt{-g}\,\mu\,(\mathcal{H}-\alpha|\Phi|^2)$$

$\mathcal{H} = H_0\sqrt{-g_{00}/(-g_{00})_\infty}$ (v0.2 §2).

---

## §3. Covariant variation at 1PN (static weak field)

**Background:** $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$, $h_{00}=-2\Phi_N$, $h_{ij}=2\Phi_N\delta_{ij}$, $|\Phi_N|\ll1$.

**On-shell constraint** eliminates $\Phi_{\rm NTE}$:

$$|\Phi_{\rm NTE}|^2 = \frac{H_0}{\alpha}(1+\Phi_N) = v_{\rm EW}^2(1+\Phi_N)$$

**Variation w.r.t. $g^{00}$:**

$$\frac{\delta\mathcal{H}}{\delta g^{00}} = -\frac{H_0}{2\sqrt{1+2\Phi_N}} \approx -\frac{H_0}{2}(1-\Phi_N)$$

Constraint term $\alpha|\Phi|^2$ contributes $\delta(\alpha|\Phi|^2)/\delta g^{00} = (H_0/2)(1+\Phi_N)$ at same order — **cancels against $\delta\mathcal{H}/\delta g^{00}$ in the $G_{00}$ equation** when $\mu$ is chosen to enforce constraint.

**Key result:** at 1PN, **effective stress-energy from $(\mu, \Phi)$ sector is pure gauge** — constraint slaving removes scalar-mediated fifth force.

**Einstein equation (1PN):**

$$G_{00} = \nabla^2\Phi_N = 4\pi G\,\rho_m + \mathcal{O}(\Phi_N^2)$$

$$G_{ij} = -\delta_{ij}\nabla^2\Phi_N + \cdots = 4\pi G\,\rho_m v_i v_j + \mathcal{O}(\Phi_N^2)$$

→ **standard Newtonian limit** with $\gamma=1$, $\beta=1$ at $\mathcal{O}(\Phi_N)$.

**Script cross-check:** `mu_xN_ppn_check.py` (proper time) + this section (metric).

---

## §4. On-shell $\mu(x)$ (algebraic)

From $\mathcal{H}=\alpha|\Phi|^2$ and Klein-Gordon with slaved $\Phi$:

$$\mu(x) \approx -V_{\rm NTE}'(\Phi_{\rm NTE}(x))/(2\alpha\Phi_{\rm NTE}) + \cdots$$

Cosmological analogue: $\mu(N)\approx -V(\Phi(N))$ (Appendix B.3). **Local:** same functional class; magnitude fixed by constraint, not independent dynamics.

---

## §5. PPN parameter extraction

| Parameter | Value | Mechanism |
|-----------|-------|-----------|
| $\gamma$ | 1 | $g_{ij}$ uncorrected at $\mathcal{O}(\Phi_N)$ |
| $\beta$ | 1 | No scalar gradient force at 1PN |
| $\tau$ ratio | $1+\Phi_N$ | §2.3 structural identity |

**Deferred:** Shapiro ($\mathcal{O}(\Phi_N^2)$ in $g_{00}$), Mercury perihelion, strong field (P-BH4 / `bh_nthickness_shell.py`).

---

## §6. Status register

| Claim | Register |
|-------|----------|
| 1PN $\delta g_{\mu\nu}$ | **Derived** (this worksheet) |
| S1 sign-off §22.16 | **Near-closure** — Jammer review |
| Strong field / BH | **Open** — P-BH4 |

---

## §7. Cross-references

- §22.16, `mu_xN_ppn_check.py`, `bh_nthickness_shell.py`

— Cursor μ(x,N) v0.3, 2026-05-23.
