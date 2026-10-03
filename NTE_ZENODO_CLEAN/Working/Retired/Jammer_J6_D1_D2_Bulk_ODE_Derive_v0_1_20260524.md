# J6-D1 / J6-D2 — bulk Sector-1 ODE + $\Phi_{\rm inf}$ lemma v0.1

**From:** Jammer (R&D) — Sprint A  
**Date:** 2026-05-24  
**Status:** **J6-D1 PASS** (Route P1); **J6-D2 DERIVED** (algebraic lemma)  
**Script:** `Working/j6_d1_bulk_ode_numerics.py`  
**Parents:** `J6_HH_Saddle_Scope_Memo_v0_1`; `Jammer_LB1_Exhaustive_Resolution`; `Open_Gaps_Derivation_Pathways_Sunshine_Map_v0_1_20260524`

---

## §0. Executive

| ID | Deliverable | Verdict |
|----|-------------|---------|
| **J6-D1** | Integrate bulk Sector-1 slow-roll; extract $H_{\rm inf}(N)$ | **PASS** — $\Phi^2$ chaotic, RK45 + exact analytic |
| **J6-D2** | Derive $\Phi_{\rm inf}=2\sqrt{N_e}\,M_{\rm Pl,red}$ | **DERIVED** — three definitions agree at O(1%) |

**Corpus discipline:** $\mu=0$ in bulk; constraint $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ **not** applied during Sector 1.

---

## §1. J6-D2 — Lemma ($\Phi_{\rm inf}$ identity)

**Lemma (J6-D2).** For $\Phi^2$-chaotic slow-roll with $V=\tfrac12 m^2\Phi^2$, $m=M_{\rm Pl,red}$, and e-fold counting $N_e=-\ln(\alpha M_{\rm Pl,nr})$:

$$\boxed{\frac{\Phi_{\rm inf}}{M_{\rm Pl,red}} = 2\sqrt{N_e}}$$

**Proof (algebraic).**

1. Slow-roll: $n_s = 1 - 8M_{\rm Pl,red}^2/\Phi^2$ (C9; Jammer J6-n1 T2).  
2. E-fold counting: $n_s = 1 - 2/N_e$ (§18.3 e-fold identity).  
3. Equate: $2/N_e = 8/\Phi^2 \Rightarrow \Phi = 2\sqrt{N_e}\,M_{\rm Pl,red}$.

**Independent route (SR integration):** $\Phi_{\rm end}=\sqrt{2}\,M_{\rm Pl,red}$, $\Phi_{\rm inf}^2-\Phi_{\rm end}^2=4M_{\rm Pl,red}^2 N_e \Rightarrow \Phi_{\rm inf}=\sqrt{4N_e+2}\,M_{\rm Pl,red}$ — numerically $\sqrt{4N_e+2}\approx 2\sqrt{N_e}$ at $N_e=63.4$.

**Numeric (script):** $2\sqrt{N_e}=15.9255$; C9 $15.9$; $\sqrt{4N_e+2}=15.9882$ — spread **0.4%**.

---

## §2. J6-D1 — Sector-1 ODE (Route P1 primary)

### §2.1 Model

Bulk effective potential at HH saddle (J6-n3): $m_E^2=\xi R=2H^2$ at $H\sim M_{\rm Pl}$ gives **$\Phi^2$-chaotic** with $m=M_{\rm Pl,red}$:

$$V=\tfrac12 M_{\rm Pl,red}^2 \Phi^2,\quad H^2=\frac{V}{3M_{\rm Pl,red}^2}$$

**Not** literal $\alpha^2\Phi^4$ (J6-n1 Track A **fails**).

### §2.2 Exact solution

$$\Phi^2(N)=\Phi_{\rm inf}^2-4M_{\rm Pl,red}^2 N,\quad N_{\rm end}=\frac{\Phi_{\rm inf}^2-\Phi_{\rm end}^2}{4M_{\rm Pl,red}^2}$$

$$H(N)=\frac{M_{\rm Pl,red}\,\Phi(N)}{\sqrt{6}\,M_{\rm Pl,red}},\quad n_s(N)=1-\frac{8M_{\rm Pl,red}^2}{\Phi^2(N)}$$

### §2.3 Numeric acceptance (corpus inputs)

| Check | Target | Result |
|-------|--------|--------|
| $\Phi_{\rm inf}/M_{\rm Pl,red}$ | $2\sqrt{N_e}=15.9255$ | **15.9255** |
| $N_{\rm end}$ | $N_e=63.4056$ | **62.906** (0.5 e-fold) |
| $n_s$ @ $N_{\rm end}-60$ | $0.9685\pm0.0042$ | **0.96694** (**0.37$\sigma$**) |
| RK45 vs analytic $n_s$ @ CMB | — | **match** |

**Verdict:** Sector-1 $H_{\rm inf}(N)$ **closed** at $\Phi^2$-chaotic / saddle-$m_E$ register.

---

## §3. Dead ends (reconfirmed)

| Route | Verdict |
|-------|---------|
| Literal $\alpha^2\Phi^4$ bulk slow-roll | **FAIL** $H\sim10^{-26}M_{\rm Pl}$ |
| Constraint eq.(7) in bulk | **FAIL** $n_s\to-1$ |
| Scaled E3 alone for full window | **FAIL** $n_s@N=0\approx0.905$ |
| Coupled adiabatic $m_E(H)$ without full Hessian | **unstable** — defer to J6-HESS |

---

## §4. Corpus patches authorised

- **§18.3:** cross-ref $n_s=1-2/N_e$ **identical** to C9 $1-8M_{\rm Pl}^2/\Phi_{\rm inf}^2$ when $\Phi_{\rm inf}=2\sqrt{N_e}M_{\rm Pl,red}$.
- **§17.5.14 / Companion 9:** Sector-1 uses saddle $m_E$, not $\alpha$ quartic.
- **G-NS row:** **closed** at identity level; formal HH integral proof = J6-HESS upgrade.

---

## §5. Open (not blocking J6-D1)

| ID | Item |
|----|------|
| J6-HESS | Full $(g,\Phi)$ coupled saddle from $\mathcal{S}_{\rm bulk}$ |
| Sector 2 | BR2 exponential terminal roll (separate chart) |
| Scaled E3 | Alternative $V_{\rm bulk}$ — not primary closure path |

---

— Jammer J6-D1/D2 v0.1, 2026-05-24.
