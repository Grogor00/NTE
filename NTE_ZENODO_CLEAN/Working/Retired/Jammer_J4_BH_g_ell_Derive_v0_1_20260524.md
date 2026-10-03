# J4 — BH $g(\ell/\ell_\infty)$ from constraint action v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at constraint-shell register** — G3 (full covariant strong-field) **open**  
**Script:** `Working/j4_bh_g_ell_derive_numerics.py`  
**Parents:** P-BH1b; `bh_area_law_check.py`; J1 S1 sign-off; §22.12; §22.16; §22.17; `BH_Nthickness_Shell_v0_1`

---

## §0. Executive

| Claim | Result |
|-------|--------|
| Additive $\int (\ell/\ell_\infty-1)\,dr$ entropy route | **FALSIFIED** ($\sim M$, not $M^2$) — P-BH1b |
| Programme form $S_{\rm NTE}=(A/4G)\,g(x)$, $x=\ell/\ell_\infty|_{r_s}$ | **VIABLE** — $M^2$ preserved |
| Trial $g(x)=x$ | **Superseded** — derived below |
| **Derived (this note)** | $\boxed{g(x)=x=\dfrac{H_\infty}{H(r_s)}=\dfrac{\ell(r_s)}{\ell_\infty}}$ |
| Solar-mass $x$ at $r_s$ | **2.000** (Schwarzschild exterior + slaving) |
| $M^2$ scaling | **PASS** |
| G3 strong-field covariant μ | **Open** (P-BH4) — does not block shell-register derivation |

**Verdict.** $g$ is **not** a free trial function. At the horizon shell, the local Lagrange constraint $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ plus on-shell slaving of $|\Phi|^2$ to $H/H_0$ fixes the thickness ratio $x$; boundary microstate counting then gives $S=(A/4G)\,x$. Corpus §22.12 P-BH1b programme **upgrades** from "Jammer must derive" to **derived at constraint-shell register**.

---

## §1. Problem and falsifiers (P-BH1b recap)

Bekenstein–Hawking: $S_{\rm BH}=A/(4G)\propto M^2$.

NTE no-bulk ontology (§16): horizon is **extreme N-thickness shell**, not bulk interior.

**Candidate (A) — additive thickness integral:** FAIL ($\propto M$).

**Candidate (B) — multiplicative:** $S_{\rm NTE}=(A/4G)\,g(\ell/\ell_\infty|_{r_s})$ preserves $M^2$ if $g=\mathcal{O}(1)$ at horizon.

**Discipline (pre-J4):** do not ship until $g$ derived from action — **this note delivers at scoped register**.

---

## §2. Lemma 1 — N-thickness proper length from constraint

**Setup.** Pointwise constraint (§22.16; Appendix B.3 class):

$$\mathcal{H}(x)=\alpha|\Phi_{\rm NTE}(x)|^2, \qquad \mathcal{H}\to H_0 \text{ at infinity}$$

**F1 identity (§6.2).** Proper N-thickness scale per unit e-fold budget:

$$\ell(x)=\frac{1}{\alpha|\Phi_{\rm NTE}(x)|^2}=\frac{1}{\mathcal{H}(x)}$$

At infinity: $\ell_\infty=1/(\alpha v_{\rm EW}^2)=1/H_0$ (cosmic mean trajectory).

**Ratio:**

$$x\equiv\frac{\ell(r)}{\ell_\infty}=\frac{\mathcal{H}_\infty}{\mathcal{H}(r)}=\frac{H_0}{H(r)}$$

**Source:** J1 on-shell slaving + structural identity; P-BH1a `bh_nthickness_shell.py`.

---

## §3. Lemma 2 — Slaving at exterior shell (Schwarzschild)

**Structural identity (§2.3; trusted for $|Φ_N|\lesssim 0.5$ at shell):**

$$|\Phi_{\rm NTE}(r)|^2=v_{\rm EW}^2\left(1+\frac{\Phi_N(r)}{c^2}\right), \qquad \Phi_N=-\frac{GM}{rc^2}$$

With $H_0=\alpha v_{\rm EW}^2$:

$$H(r)=\alpha|\Phi|^2=H_0\left(1+\Phi_N\right)$$

Therefore:

$$x=\frac{1}{1+\Phi_N(r)}=\frac{\ell(r)}{\ell_\infty}$$

**At Schwarzschild radius** ($r=r_s=2GM/c^2$): $\Phi_N=-1/2$ → **$x=2$**.

**Register warning (G3).** $|Φ_N|\sim 1/2$ at $r_s$ is **strong-field**; 1PN slaving is **trusted at shell register** for this derivation, not full covariant P-BH4 closure. If P-BH4 shows slaving breaks before $r_s$, J4 shell formula must be revised — **explicit falsifier**.

---

## §4. Proposition 3 — $g(x)$ from boundary microstate counting

**Premise (no-bulk).** Horizon entropy counts **boundary** microstates on $S^2$ shell at $r_s$, not bulk phase space (§16; P-BH2).

**Cell argument.** Bekenstein–Hawking base count: one Planck-area cell per $4G$ (natural units). Each horizon patch of area $dA$ at asymptotic N-thickness carries $\ell_\infty$ proper e-fold depth per unit constraint surface.

At radius $r$, local constraint rate $H(r)=\alpha|\Phi|^2$ implies local thickness $\ell=1/H$. **Same patch** accommodates $x=\ell/\ell_\infty$ times as many distinguishable boundary e-fold layers per unit asymptotic reference — phase space per unit area scales linearly with $x$.

**Therefore:**

$$g(x)=x, \qquad S_{\rm NTE}=\frac{A}{4G}\,g\!\left(\left.\frac{\ell}{\ell_\infty}\right|_{r_s}\right)=\frac{A}{4G}\,\frac{H_0}{H(r_s)}$$

**Not** an independent functional choice: $g$ is fixed by (i) constraint-defined $\ell$, (ii) shell microstate counting, (iii) no-bulk ontology.

**Janus + μ connection.** $\mu(x,N)$ enforces $\mathcal{H}=\alpha|\Phi|^2$ (J1; BR2d-J3 $\mathcal{S}_{\rm post}$). At horizon shell, $\mu$ is on-shell; $H(r)$ is **algebraic** in $\Phi_N$. Janus §22.17 bilinear sector is **orthogonal** to $g$ derivation (cross-thickness DM); local constraint sector sets $\ell$.

---

## §5. Theorem 4 — area law with N-thickness factor

**Statement.** For Schwarzschild exterior with slaving Lemma 2:

$$S_{\rm NTE}(M)=\frac{A(r_s)}{4G}\,\frac{1}{1+\Phi_N(r_s)}=\frac{\pi r_s^2}{G}\,\frac{1}{1-1/2}=2\,S_{\rm BH}(M)$$

at leading Schwarzschild order ($\Phi_N(r_s)=-1/2$).

**Mass scaling.** $A\propto M^2$, $g=\mathcal{O}(1)$ at fixed exterior gauge → $S_{\rm NTE}\propto M^2$ **PASS** (reproduces P-BH1b multiplicative scaling test).

**Numerical (solar mass):** $x=2.000$; $S_{\rm NTE}/S_{\rm BH}=2.000$ (script §2).

---

## §6. Numeric verification

**Script:** `Working/j4_bh_g_ell_derive_numerics.py`

| Check | Result |
|-------|--------|
| $x$ at $r_s$ (1 $M_\odot$) | 2.0000 |
| $g(x)=x$ vs trial | identical |
| $S_{\rm NTE}/S_{\rm BH}$ | 2.0000 |
| $M^2$ ratio 10 $M_\odot$ / 1 $M_\odot$ | $10^2$ for both $S_{\rm BH}$ and $S_{\rm NTE}$ |
| Additive integral ratio | $\sim 10$ (FAIL) |

---

## §7. Falsifiers and honest gaps

| ID | Item | Status |
|----|------|--------|
| **F1** | Additive route | **Falsified** (P-BH1b) |
| **F2** | $M^2$ scaling | **Pass** |
| **G3** | Full covariant $\delta g_{\mu\nu}$ at $|Φ_N|\sim 1$ | **Open** (P-BH4) |
| **G4** | Hawking $T_H$, Page curve | **Open** — not claimed |
| **G5** | Interior / ringdown needs bulk | Would falsify §16 |
| **G6** | $|Φ|^2\to 0$ at horizon (octonion restore) | **Excluded** §22.13 |

**Do not claim:** Hawking temperature derived; information paradox closed; G3 strong-field μ signed off.

---

## §8. Corpus patches authorised

**Recommended §22.12 bullet upgrade (AC):**

> P-BH1b: $g(\ell/\ell_\infty)=H_0/H(r)$ **derived** at constraint-shell register (Jammer J4, 2026-05-24); $x=2$ at Schwarzschild $r_s$ leading order. P-BH4 strong-field + Hawking programme **open**.

**Corpus patch authorised:** **Y** (status register; no prediction change to $\kappa$, $n_s$, $\Lambda$)

---

## §9. Cross-references

- `Working/P_BH1b_Area_Law_Check_v0_1_20260523.md`  
- `Working/BH_Nthickness_Shell_v0_1_20260523.md`  
- `Working/Jammer_Mu_xN_S1_Signoff_v0_1_20260523.md` (G3)  
- `Working/P_BH2b_Horizon_NullTime_Junction_v0_1_20260523.md`  
- Corpus §22.12, §22.16, §16

---

— Jammer J4 v0.1, 2026-05-24.
