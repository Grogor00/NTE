# μ(x,N) local Lagrange-multiplier action — worksheet v0.2 (§22.16)

**Stream:** Cursor v0.2 → Jammer S1 sign-off  
**Date:** 2026-05-23  
**Status:** **S1 partial closure** — $\mathcal{H}[g]$ chosen; PPN 1PN verified numerically; full $\delta g_{\mu\nu}$ variation **Open — Jammer**  
**Prior:** `Mu_xN_Local_Lagrange_Action_Worksheet_v0_1_20260523.md`

---

## §1. Upgrade from v0.1

| Item | v0.1 | v0.2 |
|------|------|------|
| $\mathcal{H}[g]$ | Open | **Closed (corpus default)** — §2 |
| PPN 1PN | Sketch | **Verified** — `mu_xN_ppn_check.py` |
| $\delta g_{\mu\nu}$ | Open | Explicit target eq — §3 |
| S1 sign-off | No | **Partial** — pending covariant variation |

---

## §2. Choice of $\mathcal{H}[g]$ (corpus default)

**Post-locking static weak field.** ADM line element (isotropic, $c=1$):

$$ds^2 = -(1+2\Phi_N)\,dt^2 + (1-2\Phi_N)\,d\mathbf{x}^2, \qquad \Phi_N = -\frac{GM}{rc^2}$$

**Definition (ties to §2.3.1 cosmological $H_0 = \alpha v_{\rm EW}^2$):**

$$\boxed{\mathcal{H}(x) = H_0\,\sqrt{\frac{-g_{00}(x)}{-g_{00}|_{\infty}}} = H_0\,(1+\Phi_N/c^2) + \mathcal{O}(\Phi_N^2)}$$

**Homogeneous FRW limit:** $g_{00} = -1$, $\Phi_N=0$ → $\mathcal{H}=H_0=H(t)$ when $H_0\leftrightarrow H(t)$ on cosmological slices.

**On-shell constraint:**

$$\mathcal{H} = \alpha|\Phi_{\rm NTE}|^2 \quad\Rightarrow\quad |\Phi_{\rm NTE}|^2 = v_{\rm EW}^2(1+\Phi_N/c^2)$$

using $H_0 = \alpha v_{\rm EW}^2$ at the present epoch (§2.4.2 calibration). This is the **structural identity** of §2.3 — now enforced as the constraint surface of $S_{\rm constr}$, not an independent dynamical ansatz.

**Rejected alternatives (logged):**

| $\mathcal{H}[g]$ | Issue |
|------------------|-------|
| Trace of extrinsic curvature $K$ | Requires full ADM foliation; over-specifies for solar-system EFT |
| $R$ (Ricci scalar) | Nonzero in vacuum Schwarzschild; conflicts with $R=0$ exterior |
| $-g_{00}$ linear | Gives $H/H_0 = 1+2\Phi_N$ — **wrong** 1PN coefficient |

---

## §3. Variation equations (v0.2 explicit)

Action (unchanged from v0.1):

$$S = S_{\rm EH} + S_{\rm matter} + S_{\rm \Phi} + \int d^4x\,\sqrt{-g}\,\mu(x)\,[\mathcal{H}(x) - \alpha|\Phi_{\rm NTE}|^2]$$

**$\delta\mu$:** $\mathcal{H} = \alpha|\Phi_{\rm NTE}|^2$ on-shell.

**$\delta\Phi_{\rm NTE}$:**

$$\Box\Phi_{\rm NTE} - V'_{\rm NTE}(\Phi_{\rm NTE}) = 2\alpha\mu(x)\,\Phi_{\rm NTE}$$

In the **slaved regime** (solar-system EFT): constraint eliminates independent scalar dynamics; $\Phi_{\rm NTE}$ is algebraic in $\Phi_N$ at 1PN.

**$\delta g_{\mu\nu}$ (target — Jammer):**

$$G_{\mu\nu} = 8\pi G\,T_{\mu\nu}^{\rm matter} + \mu(x)\left[\frac{\delta\mathcal{H}}{\delta g^{\mu\nu}} - 2\alpha\Phi_{\rm NTE}\frac{\delta|\Phi_{\rm NTE}|^2}{\delta g^{\mu\nu}}\right]$$

With $\mathcal{H} = H_0\sqrt{-g_{00}/(-g_{00})_\infty}$:

$$\frac{\delta\mathcal{H}}{\delta g^{00}} = -\frac{H_0}{2\sqrt{-g_{00}(-g_{00})_\infty}} + \cdots$$

At 1PN, this contributes only to $g_{00}$ — **spatial sector unchanged** → $\gamma_{\rm PPN}=1$.

**EFT note:** $\mu(x)$ is not a propagating degree of freedom; it enforces holonomic constraint (same class as Appendix B.3 cosmological $\mu(N)$).

---

## §4. PPN 1PN verification

**Script:** `Working/mu_xN_ppn_check.py`

**Results (Solar system):**

| Quantity | NTE (§2.3) | Schwarzschild 1PN | Match |
|----------|------------|-------------------|-------|
| $\tau(x)/\tau(\infty)$ | $1+\Phi_N/c^2$ | $1+\Phi_N/c^2$ | ✓ (script) |
| $\gamma_{\rm PPN}$ | 1 | 1 | ✓ (spatial metric untouched) |
| $\beta_{\rm PPN}$ | 1 | 1 | ✓ at leading order (no scalar force) |

**Constraint residual** $|\mathcal{H} - \alpha|\Phi|^2|/H_0 < 10^{-15}$ at 1 AU and solar surface with $\mathcal{H}[g]$ choice §2.

**Not verified in v0.2:** Shapiro delay, Mercury perihelion (need full $\delta g_{\mu\nu}$ at $\mathcal{O}(\Phi_N^2)$); strong-field P-BH4.

---

## §5. Janus / Connes layering (unchanged)

- Single-orientation $g_{\mu\nu}$ at solar-system scales (§22.17 EFT decoupling)
- $\xi=1/6$ bare coupling orthogonal in vacuum ($R=0$)
- Unification with $S_{\rm Janus}$ still open

---

## §6. Status register

| Claim | Register |
|-------|----------|
| $\mathcal{H}[g]$ default | **S1 closed** (corpus-aligned) |
| PPN 1PN proper-time | **Verified** (script) |
| Full covariant variation | **Open** — Jammer session |
| S1 sign-off §22.16 | **Partial** — upgrade from scaffold to partial closure |
| P-BH4 strong-field | **Still blocked** until $\mathcal{O}(\Phi^2)$ metric |

---

## §7. Cross-references

- §22.16, §17.5.3, Appendix B.3  
- `Working/mu_xN_ppn_check.py`  
- `Working/Priority_IV_Pathway_Programmes_v0_1_20260523.md` (P-BH4)

— Cursor μ(x,N) v0.2, 2026-05-23.
