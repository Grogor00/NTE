# J1-G2 — $\mathcal{O}(\Phi_N^2)$ metric / Shapiro / perihelion v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **S2 closed at 2PN solar-system compatibility** — G3/G4 **open**  
**Script:** `Working/j1_g2_2pn_metric_numerics.py`  
**Parents:** J1 S1 sign-off; `Mu_xN_Local_Lagrange_Action_Worksheet_v0_3`; P-BH4 programme; §22.16

---

## §0. Executive

| Gap | Claim | Verdict |
|-----|-------|---------|
| **G2** | $\mathcal{O}(\Phi_N^2)$ in $g_{\mu\nu}$; Shapiro; Mercury perihelion | **Closed at 2PN compatibility** |
| **G3** | Strong-field / horizon ($|Φ_N|\sim 1$) | **Open** (P-BH4) |
| **G4** | Single action unifying μ + $\xi=1/6$ bare sector | **Open** (Paper S2) |

**Mechanism.** The $(\mu,\Phi_{\rm NTE})$ sector is **holonomic**: on-shell slaving removes independent scalar propagation at 1PN (J1) and **cannot source new $\mathcal{O}(\Phi_N^2)$ tensor structure** in vacuum exterior. Exterior $R=0$ → metric is Schwarzschild class → PPN $(\gamma,\beta)=(1,1)$ at 2PN observables.

**Do not claim:** full non-perturbative strong-field (G3); Hawking; G4 unification.

---

## §1. Scope

**In scope (G2).**

- Extend $\mathcal{H}[g]=H_0\sqrt{1+2\Phi_N}$ to $\mathcal{O}(\Phi_N^2)$  
- Constraint cancellation in $G_{\mu\nu}$ at $\mathcal{O}(\Phi_N^2)$ (static isotropic)  
- Shapiro delay factor $(1+\gamma)=2$  
- Mercury perihelion advance $\approx 43''/{\rm century}$

**Out of scope.**

- $|Φ_N|\gtrsim 0.1$ (G3 / P-BH4)  
- J4 horizon shell (uses G3-trusted register separately)  
- Off-shell ghost scan beyond holonomic class

---

## §2. Lemma 1 — Exact vs linear slaving at $\mathcal{O}(\Phi_N^2)$

**1PN linear (v0.3):** $\sqrt{1+2\Phi_N}=1+\Phi_N+\mathcal{O}(\Phi_N^2)$.

**Exact on-shell (G2 register):**

$$\mathcal{H}=H_0\sqrt{1+2\Phi_N}, \qquad |\Phi_{\rm NTE}|^2=\frac{H_0}{\alpha}\sqrt{1+2\Phi_N}=v_{\rm EW}^2\sqrt{1+2\Phi_N}$$

**Expansion:**

$$|\Phi_{\rm NTE}|^2=v_{\rm EW}^2\left(1+\Phi_N-\frac{\Phi_N^2}{2}+\frac{\Phi_N^3}{2}+\mathcal{O}(\Phi_N^4)\right)$$

**Discipline.** Structural identity prose “$|\Phi|^2=v_{\rm EW}^2(1+\Phi_N)$” is **1PN accurate**; G2 uses **exact** $\sqrt{}$ slaving for second-order variation. Difference at $\mathcal{O}(\Phi_N^2)$ is $-\frac12 v_{\rm EW}^2\Phi_N^2$ — **absorbed by algebraic $\mu$**, not a free dynamical mode.

---

## §3. Lemma 2 — Constraint stress at $\mathcal{O}(\Phi_N^2)$

**Action (unchanged):**

$$S=\frac{M_{\rm Pl}^2}{2}\int\sqrt{-g}\,R+S_{\rm matter}+S_\Phi+\int\sqrt{-g}\,\mu(\mathcal{H}-\alpha|\Phi|^2)$$

**Static isotropic:** $g_{00}=-(1+2\Phi_N+\eta\Phi_N^2+\cdots)$, $g_{ij}=(1-2\gamma_{\rm eff}\Phi_N+\cdots)\delta_{ij}$.

**Variation w.r.t. $g^{00}$ at $\mathcal{O}(\Phi_N^2)$:**

$$\frac{\delta\mathcal{H}}{\delta g^{00}}=-\frac{H_0}{2\sqrt{1+2\Phi_N}}=-\frac{H_0}{2}\left(1-\Phi_N+\frac{3\Phi_N^2}{2}+\cdots\right)$$

With **exact** slaving $|\Phi|^2=(H_0/\alpha)\sqrt{1+2\Phi_N}$:

$$\frac{\delta|\Phi|^2}{\delta g^{00}}=\frac{H_0}{2\alpha\sqrt{1+2\Phi_N}}\left(1+\cdots\right)$$

**Key point (holonomic).** $\Phi_{\rm NTE}$ has **no kinetic term on-shell** — constraint eliminates independent propagation (J1 §3). The $\mu$-weighted combination

$$\Delta T_{\mu\nu}^{\rm constr}=\mu\left[\frac{\delta\mathcal{H}}{\delta g^{\mu\nu}}-2\alpha\Phi\,\frac{\delta|\Phi|^2}{\delta g^{\mu\nu}}\right]_{\rm on-shell}$$

is **algebraically fixed** by $\mathcal{H}=\alpha|\Phi|^2$; at $\mathcal{O}(\Phi_N^2)$ it adjusts **only** to enforce the constraint on the **already-Einstein** geometry — it does **not** introduce an independent $\Phi_N^2$ source in vacuum exterior.

**Vacuum exterior ($T_{\mu\nu}^{\rm matter}=0$, $R=0$):** $G_{\mu\nu}=0$ → **Schwarzschild class**. Constraint compatible iff $\mathcal{H}[g]=\alpha|\Phi[g]|^2$ — satisfied by Lemma 1 slaving on Schwarzschild $\Phi_N(r)$.

---

## §4. Proposition 3 — PPN at $\mathcal{O}(\Phi_N^2)$

**Statement.** In vacuum static exterior, NTE metric is **Schwarzschild isotropic/harmonic** through $\mathcal{O}(\Phi_N^2)$ with

$$\gamma_{\rm PPN}=1, \qquad \beta_{\rm PPN}=1.$$

**Proof sketch.**

1. J1: $\gamma=\beta=1$ at $\mathcal{O}(\Phi_N)$; no scalar fifth force.  
2. G2: constraint sector cannot add independent $\mathcal{O}(\Phi_N^2)$ stress in vacuum (Lemma 2).  
3. Pure EH sector → standard GR exterior → unique PPN coefficients at tested orders.

**Corollary (Shapiro).** Excess delay proportional to $(1+\gamma)$; $\gamma=1$ → **GR/Cassini** value.

**Corollary (perihelion).** Advance per orbit with $(\gamma,\beta)=(1,1)$ → **$\approx 43''/{\rm century}$** for Mercury (script §3).

---

## §5. Numeric verification

**Script:** `Working/j1_g2_2pn_metric_numerics.py`

| Check | Result |
|-------|--------|
| $(1+\gamma)$ Shapiro factor | **2.000** (GR) |
| Linear vs exact slaving @ 1 AU | $\Delta|\Phi|^2/H_0 \sim 10^{-16}$ |
| Mercury $\Delta\omega$ per century | **~43.0''** (GR) |
| $\mathcal{O}(\Phi_N^2)$ g_00 coeff vs harmonic Schw. | **match** at solar $|Φ_N|$ |

---

## §6. Falsifiers

| ID | Test | Status |
|----|------|--------|
| F1 | Shapiro requires $\gamma\neq 1$ at Cassini precision | **Pass** ($\gamma=1$) |
| F2 | Perihelion requires $\beta\neq 1$ | **Pass** ($\beta=1$) |
| F3 | Independent scalar $\mathcal{O}(\Phi^2)$ force | **Pass** (holonomic) |
| G3 | $|Φ_N|\sim 1/2$ at $r_s$ | **Open** — J4 uses separate shell register |

---

## §7. Corpus patches authorised

**Recommended §22.16 status upgrade (AC):**

> **S1 closed at 1PN; S2 closed at 2PN solar-system compatibility (Jammer J1-G2, 2026-05-24).** Shapiro/perihelion inherit GR via holonomic constraint + Schwarzschild exterior. **G3** (P-BH4 strong-field) and **G4** (Paper S2 unification) **open**.

**Corpus patch authorised:** **Y** (status register only)

---

## §8. Cross-references

- `Jammer_Mu_xN_S1_Signoff_v0_1_20260523.md`  
- `Mu_xN_Local_Lagrange_Action_Worksheet_v0_3_20260523.md`  
- `Jammer_J4_BH_g_ell_Derive_v0_1_20260524.md` (G3 separate)  
- `mu_xN_ppn_check.py`; `j1_g2_2pn_metric_numerics.py`

---

— Jammer J1-G2 v0.1, 2026-05-24.
