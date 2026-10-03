---
title: "F₁ = −18 C² + 11 E₄ and uniqueness of vanishing on S³ × S¹ in the product-of-spheres family"
author: "G. White"
date: "2026-08-03 (v10.19.0 companion)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (draft). Companion 20. Rewritten from `New folder/Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_…_v0_3_20260622.md`. Supersedes the thinner `Paper_S3xS1_TraceAnomaly_Vanishing_…_v0_1` in New folder. Pedagogical twin: `Pedagogical_Notes/Paper_F1_Trace_Anomaly_S3xS1_Pedagogical_Note_v10_19_0.md`.*

---

## Scope

$a_4=0$ on $S^3\times S^1$ is **established prior art** (Chamseddine–Connes 2008; Mistry–Pinzul–Rachwał 2020). Companions 11–12 *use* that fact. This companion deposits the algebraic/geometric lemma the corpus cites: the $d$-parametric combination $F_1$ decomposes as $-18\,C^2+11\,E_4$, and among product manifolds $S^p\times F^q$ ($p+q=4$, $F^q$ flat, $p\in\{2,3,4\}$) both $C^2$ and $E_4$ vanish simultaneously and pointwise **only at $p=3$**.

Uniqueness is **not** claimed among all closed 4-manifolds (e.g. flat $T^4$; closed-hyperbolic $N^3\times S^1$).

---

## 1. The combination $F_1$

$$
F_1 \;=\; 5\,R^2 \;-\; 8\,R_{\mu\nu}^2 \;-\; 7\,R_{\mu\nu\rho\sigma}^2.
$$
Matching to $\alpha C^2+\beta E_4+\gamma R^2$ with the standard Weyl/Euler definitions yields $\alpha=-18$, $\beta=11$, $\gamma=0$:
$$
\boxed{F_1 \;=\; -18\,C^2 \;+\; 11\,E_4.}
$$

The $R^2$ coefficient cancels exactly — $F_1$ is built entirely from genuine anomaly content. Cross-check by expanding $-18C^2+11E_4$ recovers $(5,-8,-7)$ on $(R^2,R_{\mu\nu}^2,R_{\mu\nu\rho\sigma}^2)$.

Per-Dirac anomaly coefficients $c_W=-1/20$, $a_E=+11/360$ identify the same integer pair $(-18,+11)$ with the standard trace-anomaly combination (Birrell–Davies; Duff; Christensen–Duff).

---

## 2. Curvature on $S^p\times F^q$

On unit-radius $S^p$: $R=p(p-1)$, $R_{\mu\nu}^2=p(p-1)^2$, $R_{\mu\nu\rho\sigma}^2=2p(p-1)$; flat factor contributes zero. For $p\in\{2,3,4\}$:

| $p$ | $C^2$ | $E_4$ | $F_1$ |
|---|---|---|---|
| 2 | $\neq0$ | $\neq0$ | $\neq0$ |
| **3** | **0** | **0** | **0** |
| 4 | $\neq0$ | $\neq0$ | $\neq0$ |

(Explicit monomial evaluation as in the source standalone §4–§5; $S^3\times S^1$ is simultaneously Weyl-flat and Euler-zero.)

**Restricted uniqueness.** Among $S^p\times F^{4-p}$ with $p\in\{2,3,4\}$, only $p=3$ gives $F_1\equiv0$ pointwise. This is the geometric content behind $a_4(D^2)|_{S^3\times S^1}=0$ used in Companions 11–12.

---

## 3. What this does and does not fix

**Does:** pin why the NTE substrate's fourth Seeley–DeWitt coefficient vanishes; supply the $-18C^2+11E_4$ identity cited by Companions 11–12; distinguish $S^3\times S^1$ within the product-of-spheres family.

**Does not:** derive $\Lambda$'s numerical value (Companion 11: structural quietness is unimodular / surface-only, logically upstream of $a_4$); claim uniqueness among all 4-manifolds; close $K(\Phi)$ or $T_{\mathrm{GB}}$.

---

## 4. Relation to other companions

| Companion | Relation |
|---|---|
| **11** | $\Lambda$ structural mechanism; cites $a_4=0$ via this identity |
| **12** | Chord; $a_4=0$ clean spine fact |
| **14** | RW coefficients — different geometry; sphere $a_8/a_{10}$ cross-checks |
| New-folder HeatKernel standalone | Computational extract overlapping Comp 12; **not** separately filed (redundant) |

---

## References

1. A. H. Chamseddine and A. Connes, arXiv:0812.0165 (2008) — $a_4=0$ on $S^3\times S^1$.
2. D. V. Vassilevich, Phys. Rept. **388**, 279 (2003).
3. N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (1982) §6.
4. M. J. Duff; S. M. Christensen and M. J. Duff — 4D trace anomaly coefficients.

---

*Companion 20 · NTE v10.19.0 · G. White · 2026-08-03*
