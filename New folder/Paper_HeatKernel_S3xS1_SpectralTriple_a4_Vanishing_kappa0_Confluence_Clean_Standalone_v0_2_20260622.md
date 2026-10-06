---
title: "A Seeley–DeWitt heat-kernel computation on the S³ × S¹ spectral triple: the established vanishing of a₄ and the κ₀ confluence"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-22 (v0.2 pre-submission draft)"
---

*Part of NTE Corpus v10.18.0 (deposited 2026-06).*

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

## Scope of this paper

The central computational fact used here — that the fourth Seeley–DeWitt coefficient of the Dirac operator **vanishes on $S^3 \times S^1$** — is **established in the prior literature**: Chamseddine–Connes (2008, arXiv:0812.0165) compute $a_4 = 0$ on $S^3 \times S^1$ (and $a_4 \neq 0$ on $S^4$), and Mistry–Pinzul–Rachwał (2020) extend the analysis. **This paper claims no novelty for the vanishing of $a_4$.** Its purpose is to carry out the $a_0/a_2/a_4$ computation explicitly on the specific substrate used by the Non-Temporal Emergence (NTE) framework — $S^3 \times S^1$ with an octonionic finite part — and to record which framework quantities that single computation touches, honestly tiered. The framework-specific elements are the substrate choice and finite multiplicity, the $\kappa_0$ confluence reading, and the honest-status accounting (§6); none of these is a claim that $a_4 = 0$ is a new result.

---

## Abstract

We carry out the Seeley–DeWitt expansion of the Dirac operator on a product spectral triple with base $M = S^3 \times S^1$ (round unit 3-sphere times flat circle) and a finite part supplying $N_F$ internal species, and record the coefficients $a_0, a_2, a_4$ in closed form on this substrate. The fourth coefficient vanishes, $a_4(D^2)\big|_M = 0$ — an **established result** (Chamseddine–Connes 2008; Mistry–Pinzul–Rachwał 2020), reproduced here on the NTE substrate because the Dirac trace-anomaly integrand $-18\,C^2 + 11\,E_4$ is pointwise zero on $S^3 \times S^1$ (both the Weyl and Euler densities vanish). The bare dimensionless coupling read from $a_2$ via the Hopf-harmonic content of the $S^3$ curvature is $\kappa_0 = 3/\sqrt{4\pi} \approx 0.846$ — the same value reached by an independent monopole-projection route, a confluence. We then separate what this single computation derives ($\kappa_0$ confluence; operator-setup scales) from what is a consistency cross-check ($M_1$, $M_R$), open ($K(\Phi)$), or retired (a previously quoted $a_4$-dependent $\Lambda$ value; the structural unimodular mechanism is unaffected).

---

## 1. Introduction

The spectral action (Chamseddine–Connes 1997, 2010) computes the bosonic action of a noncommutative geometry as a heat-kernel expansion of its Dirac operator, with leading physics in the Seeley–DeWitt coefficients $a_0$ (cosmological-constant scale), $a_2$ (Einstein–Hilbert), $a_4$ (fourth-order curvature / trace anomaly).

We compute these on the substrate $M = S^3 \times S^1$ with a finite part $A_F$ supplying $N_F$ species — the substrate selected on independent structural grounds by NTE (closed compact spatial $S^3$, compactified temporal $S^1$). In NTE the finite algebra is $A_F = \mathbb{O} \oplus \mathbb{O}$, $N_F = 180$ [companion octonion note]; here $A_F$ enters only through the trace multiplicity $N_F$ and, sub-leading, $\mathrm{Tr}_F(D_F^2)$.

The purpose is computational and the load-bearing fact — $a_4 = 0$ on $S^3 \times S^1$ — is **not ours**: it is Chamseddine–Connes (2008). We reproduce it on the NTE substrate, exhibit the $\kappa_0$ confluence, and state precisely which framework quantities the computation does and does not fix.

---

## 2. The spectral triple

**Base.** $M = S^3 \times S^1$, product metric, $S^3$ round unit, $S^1$ flat. Curvature concentrated in $S^3$: $\mathrm{Ric}_{S^3} = 2 g_{S^3}$, $R = 6$, $\mathrm{Vol}(S^3) = 2\pi^2$, $\mathrm{Ric}_M = \mathrm{diag}(2,2,2,0)$, $\mathrm{Vol}(M) = 2\pi^2\beta$ ($\beta$ = circumference of $S^1$). In NTE $\beta = \sqrt{2\pi}/M_{\mathrm{Pl,nr}}$; this plays no role in the coefficient structure and is kept symbolic.

**Finite part and Dirac operator.** $A_F$ supplies $N_F$ via $\mathrm{Tr}_F(\mathbf{1}_F) = N_F$. Full Dirac $D = D_M \otimes 1 + \gamma_M \otimes D_F$. The $S^3$ Dirac spectrum is $\pm(\tfrac32 + k)$, multiplicity $(k+1)(k+2)$ (Friedrich 1980); flat-$S^1$ antiperiodic. We use $D^2 = -\nabla^2 + R/4$ (Lichnerowicz) and Gilkey–Vassilevich conventions.

---

## 3. Heat-kernel expansion

For a Laplace-type $D^2$ on a closed 4-manifold, $\mathrm{Tr}\,e^{-tD^2} \sim \sum_{k\ge0} a_{2k}(D^2)\,t^{k-2}$ as $t \to 0^+$, with $a_{2k}$ integrals of local curvature invariants.

---

## 4. The coefficients

**4.1 $a_0$ — volume.** $a_0 = r N_F \mathrm{Vol}(M)/(16\pi^2) = N_F\beta/2 = 90\beta$ ($N_F=180$, $r=4$).

**4.2 $a_2$ — Einstein–Hilbert, and the κ₀ confluence.** With $\xi=1/6$, $a_2 = -N_F\beta/4 = -45\beta$ (using $\int_M R = 12\pi^2\beta$). The $a_2$ integrand carries $R_{S^3}=6$, whose Hopf decomposition exposes $R_{S^3}/2 = 3 = \dim(\mathrm{adj}\,\mathfrak{su}(2))$; projecting onto the $S^2$ s-wave $Y_{00}=1/\sqrt{4\pi}$ gives

$$\kappa_0 = \dim(\mathrm{adj}\,\mathfrak{su}(2)) \times Y_{00}(S^2) = \frac{3}{\sqrt{4\pi}} \approx 0.846,$$

the same value as an independent monopole-projection route [companion κ₀ note] — a **confluence**, not an independent second derivation (both routes share the $3 \times Y_{00}$ structure). The closure $\kappa = \kappa_0/(1-\kappa_0) \approx 5.51$ is a separate result and is not reached here.

**4.3 Finite-part suppression.** Sub-leading $D_F$ contributions enter via $\mathrm{Tr}_F(D_F^2)$, suppressed by $\sim10^{-18}$ at the framework's scales; the results above and below are robust to them.

---

## 5. a₄ vanishes — an established result, reproduced on this substrate

The Seeley–DeWitt $a_4$ for the Dirac operator with $E = R/4$ is (Vassilevich 2003)

$$a_4(D^2) = \frac{N_F}{(4\pi)^2}\cdot\frac{1}{360}\int_M \big(5R^2 - 8R_{\mu\nu}^2 - 7R_{\mu\nu\rho\sigma}^2\big)\sqrt{g}\,d^4x,$$

the integrand being the 4D Dirac trace-anomaly combination $-18\,C^2 + 11\,E_4$ (the $R^2$ coefficient cancels). On $M = S^3\times S^1$, $R_{\mu\nu\rho\sigma}^2 = 12$, $R_{\mu\nu}^2 = 12$, $R^2 = 36$, giving

$$C^2\big|_M = 12 - 24 + 12 = 0, \qquad E_4\big|_M = 12 - 48 + 36 = 0,$$

so the integrand is $180 - 96 - 84 = 0$ and

$$a_4(D^2)\big|_M = 0.$$

**This is Chamseddine–Connes (2008)** — who established $a_4 = 0$ on $S^3 \times S^1$ (contrasting $a_4 \neq 0$ on $S^4$) — extended by Mistry–Pinzul–Rachwał (2020). We reproduce it on the NTE substrate and claim no novelty for it. (An explicit $d$-parametric factorisation that makes the $d=3$ vanishing transparent is given as a pedagogical note, "A polynomial that vanishes on the 3-sphere," in the explanatory set; it too is a refinement of the established result, not a new claim.)

**Two cautions.** (i) This is the **untwisted** product Dirac operator (no external gauge connection, so no $\Omega^2$ term); the twisted operator generating the SM bosonic sector is different and outside this computation. (ii) The Dirac integrand $-18C^2 + 11E_4$ is the correct one; the non-Dirac combination $5R^2 - 2R_{\mu\nu}^2 + 2R_{\mu\nu\rho\sigma}^2$ (which is $180$ on $M$) must not be substituted.

---

## 6. What this computation organises

Honest status tiers:
- **Derived here:** the operator-setup scale $T = M_{\mathrm{Pl,nr}}/\sqrt{2\pi}$ and the $2\pi^2 = \mathrm{Vol}(S^3)$ normalisation (substrate facts). *Not* $a_4=0$ — that is CC 2008, reproduced.
- **Confluence:** $\kappa_0 = 3/\sqrt{4\pi}$ (§4.2).
- **Cross-check (not derivation):** $M_1 \approx 5.4\times10^9$ GeV, $M_R \approx 8.2\times10^{14}$ GeV — consistent with the $N_F=180$ doubling, not derived here.
- **Open:** $K(\Phi)$. With $a_4 = 0$ on the untwisted substrate the prior $a_4$-based route to $K(\Phi)$ is closed; any $n_s$/$r$ statement is conditional on a separate determination and not claimed.
- **Retired:** a previously quoted $\Lambda \approx 1.05\,\Lambda_{\mathrm{obs}}$ rested on an $a_4$-dependent residual — withdrawn. The structural unimodular mechanism is independent of $a_4$ and unaffected.

The honest organising claim: these quantities are touched by **one** computation on **one** substrate — but only the $\kappa_0$ confluence and the operator-setup facts are results *of* the heat kernel here; $a_4 = 0$ is imported (CC 2008), and the rest are cross-checks or open/retired.

---

## 7. Discussion and falsifiers

The substrate $S^3 \times S^1$ is Weyl-flat and Euler-zero pointwise, which is why CC 2008's $a_4 = 0$ holds there and no fourth-order ($R^2$/Starobinsky) term is generated at this order on the untwisted operator. That NTE's independently-chosen substrate coincides with the one on which the spectral action is tractable in closed form at $a_4$ is the structural observation worth recording — not a new derivation.

Falsifiers: (1) an independent evaluation finding $a_4 \neq 0$ for the untwisted Dirac operator on $S^3\times S^1$ would contradict CC 2008 and §5; (2) a heat-kernel bare coupling differing from $3/\sqrt{4\pi}$ would break the §4.2 confluence; (3) $C^2 \neq 0$ or $E_4 \neq 0$ pointwise on $S^3\times S^1$ would falsify the geometric input.

---

## References

1. A. H. Chamseddine and A. Connes, "Noncommutative geometry as a framework for unification," Fortsch. Phys. **58**, 553 (2010) [arXiv:0812.0165] — $a_4 = 0$ on $S^3 \times S^1$.
2. S. Mistry, A. Pinzul, L. Rachwał (2020) — extension of the spectral-action curvature analysis.
3. A. H. Chamseddine and A. Connes, "The Spectral Action Principle," Commun. Math. Phys. **186**, 731 (1997).
4. P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (1984).
5. D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279 (2003).
6. T. Friedrich, Math. Nachr. **97**, 117 (1980).
7. N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (CUP, 1982), Ch. 6.

---

*v0.2 pre-submission draft. Changes from v0.1: added the up-front Scope statement crediting Chamseddine–Connes 2008 and Mistry–Pinzul–Rachwał 2020 for $a_4 = 0$; §5 retitled and rewritten to present the vanishing as established and reproduced, not freshly derived; §6 tier corrected ($a_4=0$ moved from "derived" to "imported"); the F1 factorisation demoted to a pedagogical "see also." The κ₀ confluence and honest-status accounting are the framework-specific content; no novelty is claimed for $a_4 = 0$.*
