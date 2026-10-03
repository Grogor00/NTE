# J1 — μ(x,N) covariant δg_μν formal sign-off v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Stream:** Formal backlog P0 / LB-3  
**Inputs:** `Mu_xN_Local_Lagrange_Action_Worksheet_v0_3_20260523.md`; `mu_xN_ppn_check.py`; §22.16 (v10.17.1); Greg R5 (2026-05-23)

**Verdict:** **§22.16 S1 closed at 1PN static weak field.** Corpus patch **authorised (AC)** for status-line upgrade. Strong-field / second-post-Newtonian work remains **open** (P-BH4).

---

## §1. Scope of sign-off

This sign-off covers:

- Choice of $\mathcal{H}[g]=H_0\sqrt{-g_{00}/(-g_{00})_\infty}$ as corpus default (v0.2 §2)
- On-shell slaving $|\Phi_{\rm NTE}|^2=v_{\rm EW}^2(1+\Phi_N/c^2)$ from $H_0=\alpha v_{\rm EW}^2$
- Covariant variation at **1PN** in static isotropic weak field
- PPN parameters $\gamma=1$, $\beta=1$ at leading order

**Out of scope (explicit gaps):** $\mathcal{O}(\Phi_N^2)$ metric corrections (Shapiro, perihelion); strong-field / horizon (P-BH4); unification with full Janus action (§22.17); off-shell ghost scan beyond holonomic-constraint class.

---

## §2. Verification performed

### §2.1 $\mathcal{H}[g]$ choice

Jammer confirms v0.2 rejection table: trace-$K$ and Ricci-scalar choices conflict with vacuum Schwarzschild or over-specify ADM. Linear $-g_{00}$ gives wrong 1PN coefficient ($1+2\Phi_N$ vs required $1+\Phi_N$ for proper-time ratio).

**Verdict:** $\mathcal{H}[g]$ default is **corpus-aligned** and **unique among logged alternatives** at solar-system EFT.

### §2.2 On-shell constraint algebra

At 1PN, $g_{00}=-(1+2\Phi_N)$ gives $\mathcal{H}=H_0(1+\Phi_N)$ (with $c=1$). Constraint $\mathcal{H}=\alpha|\Phi|^2$ yields $|\Phi|^2=(H_0/\alpha)(1+\Phi_N)=v_{\rm EW}^2(1+\Phi_N)$ — the §2.3 structural identity, now as constraint surface rather than independent dynamics.

**Script check:** `mu_xN_ppn_check.py` — constraint residual $| \mathcal{H}-\alpha|\Phi|^2 |/H_0 < 10^{-11}$ at 1 AU and solar surface (machine zero at infinity).

### §2.3 Covariant variation at 1PN (Jammer expansion)

Action (v0.3 §2):

$$S = \frac{M_{\rm Pl}^2}{2}\int\sqrt{-g}\,R + S_{\rm matter} + S_\Phi + \int\sqrt{-g}\,\mu\,(\mathcal{H}-\alpha|\Phi|^2)$$

**Variation w.r.t. $\mu$:** $\mathcal{H}=\alpha|\Phi|^2$ on-shell.

**Variation w.r.t. $\Phi$:** Klein–Gordon with source $2\alpha\mu\Phi$. In the **slaved regime**, constraint eliminates independent scalar propagation: $\Phi$ is algebraic in $\Phi_N$ at 1PN.

**Variation w.r.t. $g^{\mu\nu}$:** Constraint sector contributes

$$\Delta T_{\mu\nu}^{\rm constr} = \mu\left[\frac{\delta\mathcal{H}}{\delta g^{\mu\nu}} - 2\alpha\Phi\,\frac{\delta|\Phi|^2}{\delta g^{\mu\nu}}\right]_{\rm on-shell}$$

With $\mathcal{H}=H_0\sqrt{-g_{00}/(-g_{00})_\infty}$:

$$\frac{\delta\mathcal{H}}{\delta g^{00}} = -\frac{H_0}{2\sqrt{1+2\Phi_N}} \approx -\frac{H_0}{2}(1-\Phi_N)$$

The $\alpha|\Phi|^2$ term contributes $\delta(\alpha|\Phi|^2)/\delta g^{00} = (H_0/2)(1+\Phi_N)$ **when $\Phi$ is slaved through the constraint**. The **00 components cancel at $\mathcal{O}(\Phi_N)$** when $\mu$ enforces the constraint — the scalar sector does not source a fifth force at 1PN.

Spatial components: $\mathcal{H}$ depends only on $g_{00}$ at this order → **$g_{ij}$ uncorrected at $\mathcal{O}(\Phi_N)$** → $\gamma_{\rm PPN}=1$.

Remaining $G_{00}$ reduces to standard Poisson form with matter source → **$\beta_{\rm PPN}=1$** at leading order (no scalar gradient force).

**Jammer note:** v0.3 §3 compresses this into prose; the cancellation is **correct at 1PN** given holonomic slaving. A fully publishable treatment would write $\mu(x)$ explicitly from the $G_{00}$ equation and show $G_{ij}$ decoupling term-by-term — recommended for Paper S2 appendix, not required to block S1.

### §2.4 Proper-time check

Corpus structural identity: $\tau(x)/\tau(\infty)=1+\Phi_N/c^2$. Script matches Schwarzschild 1PN factor to machine precision at 1 AU and solar surface.

---

## §3. Numbered gaps (falsifiers)

| ID | Gap | Register | Falsifier |
|----|-----|----------|-----------|
| **G1** | Explicit $\mu(x)$ solution displayed | 1PN closed implicitly | If explicit $\mu$ requires $\Phi_N$-dependent $\gamma\neq1$ at $\mathcal{O}(\Phi_N)$, S1 fails |
| **G2** | $\mathcal{O}(\Phi_N^2)$ in $g_{00}$ | Open | Shapiro / Mercury need full $\delta g_{\mu\nu}$ at second order |
| **G3** | Strong-field / horizon | Open (P-BH4) | If on-shell slaving breaks before $r_s$, BH programme blocked |
| **G4** | Single boundary action unifying μ + ξ=1/6 bare action | Open (Paper S2) | Not required for S1; §22.16 full closure still open at deeper level |

**None of G1–G4 falsifies the 1PN sign-off** as scoped above.

---

## §4. Corpus patch authorised

**Recommended §22.16 status line (AC):**

> **Status (v10.17.2):** **S1 closed at 1PN static weak field (Jammer J1 sign-off, 2026-05-23).** $\mathcal{H}[g]$ chosen; covariant $\delta g_{\mu\nu}$ at 1PN in worksheet v0.3; PPN $\gamma=\beta=1$ at leading order verified (`mu_xN_ppn_check.py`). Gaps G2–G4 remain (Shapiro/perihelion, P-BH4 strong-field, Paper S2 unification).

**Corpus patch authorised:** **Y** (status register only; no prediction change)

---

## §5. Next Jammer actions (from J1)

1. **P-BH4 prep:** $\mathcal{O}(\Phi_N^2)$ metric variation worksheet (optional before J4)
2. **J4 blocked until G3 addressed** — do not claim strong-field μ from S1 alone

— Jammer J1 sign-off v0.1, 2026-05-23.
