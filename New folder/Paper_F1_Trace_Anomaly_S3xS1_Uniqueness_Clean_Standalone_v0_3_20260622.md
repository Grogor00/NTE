---
title: "F₁ = −18 C² + 11 E₄ and the vanishing of the trace-anomaly combination on S³ × S¹ among product-of-spheres 4-manifolds"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-22 (v0.3 pre-submission draft)"
---

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

---

## Abstract

We identify the d-parametric curvature combination

$$F_1(d) \;=\; 5\, R^2 \;-\; 8\, R_{\mu\nu}^2 \;-\; 7\, R_{\mu\nu\rho\sigma}^2$$

with the standard 4D conformal anomaly combination expressed in the Weyl + Euler basis. The algebraic identity

$$F_1 \;=\; -18\, C^2 \;+\; 11\, E_4 \qquad (\text{with the } R^2 \text{ coefficient cancelling exactly})$$

reduces $F_1$ to a fixed integer linear combination of the Weyl-squared invariant $C^2$ and the Euler density $E_4$. Per-Dirac fermion coefficients $c_W = -1/20$ and $a_E = +11/360$ (standard 4D trace anomaly) give the multiplicative identification $F_1 \leftrightarrow -18\, c_W + 11\, a_E$ up to an overall $N_F$ (multi-fermion) factor.

$F_1$ emerges in heat-kernel computations on closed Riemannian 4-manifolds as the d-parametric form of the trace-anomaly contribution at fourth curvature order; its $d = 3$ root cancellation has been observed in spectral-action calculations (Chamseddine–Connes 2010 [arXiv:0812.0165]) and motivates the algebraic question taken up here.

We then evaluate $F_1$ on closed product 4-manifolds of the form $S^p \times F^q$ where $F^q$ is a flat factor of dimension $q = 4 - p$, and verify that $C^2 = 0$ and $E_4 = 0$ simultaneously and pointwise **only at $p = 3$**, among $p \in \{2, 3, 4\}$. The 3-sphere times a flat circle is therefore the unique value of $p \in \{2,3,4\}$ in the product-of-spheres family $S^p \times F^q$ on which the $F_1$ d-parametric combination identically vanishes; uniqueness is not claimed within the broader class of closed 4-manifolds (e.g. flat $T^4$ and closed-hyperbolic $N^3 \times S^1$ are Weyl-flat/Euler-zero outside this family). The result is purely algebraic / differential-geometric; verifiable in a few lines of curvature-invariant arithmetic.

The note is structured for direct reference: §2 derives the algebraic decomposition; §3 identifies it with the standard 4D trace anomaly per-Dirac coefficients; §4 computes the curvature invariants on $S^p \times F^q$ closed product manifolds; §5 establishes the uniqueness result at $p = 3$; §6 collects discussion and the connection to spectral-action programmes.

---

## 1. Introduction

The trace anomaly of a conformally coupled free field on a 4-dimensional Riemannian manifold $M$ decomposes, in the standard basis (Weyl-squared, Euler density, $R^2$), as

$$\langle T^\mu_{\;\mu} \rangle \;=\; \frac{1}{(4\pi)^2}\Big[\, c_W\, C^2 \;+\; a_E\, E_4 \;+\; c_R\, R^2 \,\Big],$$

with $c_W$, $a_E$, $c_R$ numerical coefficients that depend on the field content (per-Dirac fermion: $c_W = -1/20$, $a_E = +11/360$, $c_R = +1/3$; Birrell–Davies 1982 §6; Duff 1977; Christensen–Duff 1978/1979). Here $C^2$ and $E_4$ denote the Weyl-squared invariant and the Euler density:

$$C^2 \;=\; R_{\mu\nu\rho\sigma}^2 \;-\; 2 R_{\mu\nu}^2 \;+\; \tfrac{1}{3} R^2, \qquad E_4 \;=\; R_{\mu\nu\rho\sigma}^2 \;-\; 4 R_{\mu\nu}^2 \;+\; R^2.$$

Both $C^2$ and $E_4$ are pointwise-defined scalar invariants constructed from the Riemann tensor and its contractions. The $R^2$ coefficient $c_R$ can be absorbed into a local counterterm and is not present in some conventions; the $(C^2, E_4)$ part is the genuine anomaly content. The general structure of the heat-kernel expansion that produces such trace-anomaly contributions is detailed in Vassilevich (2003).

We consider a specific d-parametric combination of curvature invariants

$$F_1(d) \;=\; 5\, R^2 \;-\; 8\, R_{\mu\nu}^2 \;-\; 7\, R_{\mu\nu\rho\sigma}^2$$

motivated by its appearance in heat-kernel computations on closed Riemannian 4-manifolds — particularly in spectral-action contexts (Chamseddine–Connes 2010), where the d-parametric form factors through a root-finding condition at $d = 3$. The derivation of $F_1$ itself, in its original physical context, is outside the scope of this note. We ask two algebraic / geometric questions about $F_1$:

**Question A.** Does $F_1$ decompose cleanly in the standard 4D trace-anomaly basis $(C^2, E_4, R^2)$? If so, what are the coefficients?

**Question B.** On what closed product manifolds of the form $S^p \times F^q$ (with $F^q$ a flat factor) does $F_1$ vanish identically (pointwise)?

Both questions admit clean answers. We address them in §§2–4 below; §5 collects the uniqueness result.

---

## 2. The F_1 decomposition

Substituting $C^2$ and $E_4$ into a general linear combination

$$F_1 \;=\; \alpha\, C^2 \;+\; \beta\, E_4 \;+\; \gamma\, R^2$$

and matching to $F_1 = 5 R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2$ gives three linear equations in $(\alpha, \beta, \gamma)$. Reading coefficients off the $R_{\mu\nu\rho\sigma}^2$, $R_{\mu\nu}^2$, and $R^2$ monomials:

- $R_{\mu\nu\rho\sigma}^2$ coefficient: $\alpha + \beta = -7$
- $R_{\mu\nu}^2$ coefficient: $-2\alpha - 4\beta = -8$, i.e. $\alpha + 2\beta = 4$
- $R^2$ coefficient: $\alpha/3 + \beta + \gamma = 5$

The first two equations give $\alpha = -18$, $\beta = 11$. Substituting into the third:

$$\gamma \;=\; 5 \;-\; \frac{\alpha}{3} \;-\; \beta \;=\; 5 \;-\; \frac{-18}{3} \;-\; 11 \;=\; 5 \;+\; 6 \;-\; 11 \;=\; 0.$$

The $R^2$ coefficient **cancels exactly**. Therefore

$$\boxed{\; F_1 \;=\; -18\, C^2 \;+\; 11\, E_4. \;}$$

Equivalently: the original integer coefficients $(5, -8, -7)$ on $(R^2, R_{\mu\nu}^2, R_{\mu\nu\rho\sigma}^2)$ admit no $R^2$ piece in the $(C^2, E_4, R^2)$ basis; $F_1$ is built entirely from the genuine anomaly content. We have used standard linear algebra; the derivation is one short calculation.

**Cross-check.** Expanding $-18 C^2 + 11 E_4$:
- $R^2$ coefficient: $-18 \times (1/3) + 11 \times 1 + 0 = -6 + 11 = 5$ ✓
- $R_{\mu\nu}^2$ coefficient: $-18 \times (-2) + 11 \times (-4) = 36 - 44 = -8$ ✓
- $R_{\mu\nu\rho\sigma}^2$ coefficient: $-18 \times 1 + 11 \times 1 = -7$ ✓

All three monomial coefficients match $F_1$'s original form.

---

## 3. Identification with the standard 4D trace anomaly

The standard per-Dirac trace anomaly coefficients in the $(C^2, E_4, R^2)$ basis are (Birrell–Davies 1982 §6; Duff 1977; Christensen–Duff 1978/1979):

$$c_W^{\rm Dirac} \;=\; -\frac{1}{20}, \qquad a_E^{\rm Dirac} \;=\; +\frac{11}{360}, \qquad c_R^{\rm Dirac} \;=\; +\frac{1}{3}.$$

The combination $-18\, c_W + 11\, a_E$ evaluates to

$$-18 \times \left(-\frac{1}{20}\right) \;+\; 11 \times \frac{11}{360} \;=\; \frac{18}{20} \;+\; \frac{121}{360} \;=\; \frac{324 + 121}{360} \;=\; \frac{445}{360}.$$

The numerical value $445/360$ is a pure rational number from standard 4D trace-anomaly arithmetic. The identification

$$\boxed{\; F_1 \;\leftrightarrow\; -18\, c_W \;+\; 11\, a_E \;}\quad\text{(per Dirac fermion)}$$

is therefore an algebraic equivalence in the integer-coefficient basis $(-18, +11) \times (C^2, E_4)$ at the trace-anomaly level. For a field content with $N_F$ Dirac fermions, the multi-fermion overall coefficient multiplies through: $F_1 \leftrightarrow -18\, N_F\, c_W + 11\, N_F\, a_E$.

The crucial point: $F_1$'s $d = 3$ root cancellation (in its original physical context) is **structurally equivalent to** the simultaneous vanishing of the standard (Weyl-squared, Euler-density) anomaly combination, multiplied by the standard per-Dirac coefficients. The $d = 3$ selection criterion has a deep reading: it picks out the dimension at which both $C^2 = 0$ AND $E_4 = 0$ are simultaneously achievable on the manifold under consideration. We address this geometric question next.

---

## 4. Curvature invariants on closed product manifolds S^p × F^q

Consider a closed Riemannian product 4-manifold

$$M \;=\; S^p \times F^q, \qquad p + q = 4,$$

where $S^p$ carries the unit-radius round metric and $F^q$ is a flat factor of dimension $q$. The cases of interest are:

- $q = 0$: $M = S^4$ alone (no flat factor)
- $q = 1$: $M = S^p \times S^1$ where $S^1$ carries the flat product metric
- $q = 2$: $M = S^p \times T^2$ where $T^2$ is a flat 2-torus, or $M = S^p \times (\mathbb{R}^2 / \Lambda)$ for some flat lattice quotient

The curvature invariants on such a product reduce to those on the $S^p$ factor; the flat factor contributes zero.

**Riemann tensor on unit-radius $S^p$:** $R_{ijkl} = g_{ik} g_{jl} - g_{il} g_{jk}$.

**Ricci tensor:** $R_{ij} = (p - 1)\, g_{ij}$.

**Ricci scalar:** $R = p(p - 1)$.

**Curvature-squared invariants** (computed by explicit contraction with these expressions):

$$R^2 \;=\; [p(p-1)]^2, \qquad R_{\mu\nu}^2 \;=\; p(p-1)^2, \qquad R_{\mu\nu\rho\sigma}^2 \;=\; 2\, p(p-1).$$

The $R_{\mu\nu}^2$ formula follows from $R_{ij} R^{ij} = (p-1)^2\, g_{ij}\, g^{ij} = (p-1)^2 \times p$. The $R_{\mu\nu\rho\sigma}^2$ formula follows from $R_{ijkl} R^{ijkl} = (g_{ik} g_{jl} - g_{il} g_{jk})(g^{ik} g^{jl} - g^{il} g^{jk}) = 2 p^2 - 2 p = 2 p(p-1)$.

We tabulate for $p \in \{2, 3, 4\}$ (corresponding to $q \in \{2, 1, 0\}$ respectively):

| $p$ | $R$ | $R^2$ | $R_{\mu\nu}^2$ | $R_{\mu\nu\rho\sigma}^2$ |
|:---:|:---:|:-----:|:-------------:|:-----------------------:|
| 2 | 2 | 4 | 2 | 4 |
| 3 | 6 | 36 | 12 | 12 |
| 4 | 12 | 144 | 36 | 24 |

The Weyl-squared invariant $C^2$ and Euler density $E_4$ on $M$ evaluate to:

| $p$ | $C^2 = R_{\mu\nu\rho\sigma}^2 - 2 R_{\mu\nu}^2 + R^2/3$ | $E_4 = R_{\mu\nu\rho\sigma}^2 - 4 R_{\mu\nu}^2 + R^2$ |
|:---:|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2 | $4 - 4 + 4/3 = 4/3 \neq 0$ | $4 - 8 + 4 = 0$ |
| **3** | **$12 - 24 + 12 = 0$** | **$12 - 48 + 36 = 0$** |
| 4 | $24 - 72 + 48 = 0$ | $24 - 144 + 144 = 24 \neq 0$ |

The $p = 4$ case ($M = S^4$) is Weyl-flat — a well-known property of the round 4-sphere as a conformally-flat Einstein space — but is not Euler-zero (the integral of $E_4$ over $S^4$ gives the standard Euler characteristic $\chi(S^4) = 2$ up to normalisation). The $p = 2$ case ($M = S^2 \times F^2$) is Euler-zero (a known property of such products) but is not Weyl-flat. Only $p = 3$ achieves both simultaneously and pointwise.

---

## 5. The uniqueness result at p = 3

From the table in §4:

| $p$ | $C^2 = 0$? | $E_4 = 0$? | Both vanish? |
|:---:|:----------:|:----------:|:------------:|
| 2 | no | yes | no |
| **3** | **yes** | **yes** | **yes** |
| 4 | yes | no | no |

**Result.** Among 4-dimensional closed Riemannian product manifolds of the form $S^p \times F^q$ where $p + q = 4$, $S^p$ carries the unit-radius round metric, and $F^q$ is flat (with $p \in \{2, 3, 4\}$), the case $p = 3$ — that is, $M = S^3 \times S^1$ — is the unique value of $p$ at which the Weyl-squared invariant $C^2$ and the Euler density $E_4$ vanish identically (pointwise).

This is a finite-$p$ verification within the product-of-spheres family at small $p$; it does not claim uniqueness within the broader class of closed Riemannian 4-manifolds.

**Corollary.** $F_1 = -18\, C^2 + 11\, E_4$ (per §2) vanishes identically on $M = S^3 \times S^1$, and this is the unique value of $p$ in the family above at which $F_1$ vanishes pointwise (and hence integrates to zero with any positive integration measure).

**Geometric reading.** $S^3$ has equal Ricci-eigenvalue curvature in all three directions; on the product $S^3 \times S^1$, the Weyl tensor (traceless part of curvature) vanishes pointwise because the round 3-sphere is conformally flat at the level of its curvature decomposition, and the Euler density vanishes because the 4-dimensional product of a constant-curvature 3-sphere with a flat circle has zero pointwise Pfaffian. The $p = 4$ case loses Euler-zero because $S^4$ has nonzero Euler characteristic; the $p = 2$ case loses Weyl-zero because $S^2$ is not conformally flat in the product geometry. The simultaneous vanishing at $p = 3$ is the structural coincidence.

---

## 6. Discussion

The two facts established in §§2 and 5 are:

(A) $F_1 = -18\, C^2 + 11\, E_4$ — the d-parametric integer combination $(5, -8, -7)$ on $(R^2, R_{\mu\nu}^2, R_{\mu\nu\rho\sigma}^2)$ reduces, by standard linear algebra in the $(C^2, E_4, R^2)$ basis, to integer coefficients $(-18, +11)$ on the genuine anomaly content $(C^2, E_4)$, with $R^2$ absent.

(B) On closed product 4-manifolds $S^p \times F^q$ with $p + q = 4$, the unique value of $p \in \{2, 3, 4\}$ at which both $C^2 = 0$ and $E_4 = 0$ pointwise is $p = 3$, giving $M = S^3 \times S^1$.

These two facts combine: $F_1$ vanishes identically (pointwise) on $S^3 \times S^1$ within the small-$p$ closed product 4-manifold family. Equivalently, the $d = 3$ root cancellation in $F_1$'s original physical context is the algebraic statement of simultaneous Weyl-flatness and Euler-zero on $S^3 \times S^1$.

A consequence: the standard 4D Weyl + Euler trace anomaly (per Dirac, $c_W = -1/20$ and $a_E = +11/360$) evaluates to zero on $S^3 \times S^1$ — both anomaly pieces vanish identically because their pointwise integrands vanish. The $R^2$ piece of the trace anomaly ($c_R = +1/3$ per Dirac) is generically nonzero on $S^3 \times S^1$ since $R = 6$ (and $R^2 = 36$); the trace anomaly therefore reduces to $R^2$-only at leading order on this background.

**Connection to spectral-action programmes.** The spectral action principle of Chamseddine and Connes (Commun. Math. Phys. 293, 867 [2010; arXiv:0812.0165]) computes the bosonic action of a noncommutative geometry as a heat-kernel expansion of the Dirac operator on a spectral triple (Vassilevich 2003). The $a_4$ Seeley–DeWitt coefficient of this expansion contains the standard 4D trace-anomaly combination, which makes the $C^2 / E_4$ vanishing locus geometrically significant: on those manifolds where both anomaly pieces vanish identically, the spectral action reduces to an $R^2$-only contribution at fourth curvature order. The present note's uniqueness result identifies $S^3 \times S^1$ as the canonical product-of-spheres background on which this $R^2$-only reduction holds, independently of any specific cosmological framework using $S^3 \times S^1$ as substrate.

---

## References

1. N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge University Press, 1982), Chapter 6.
2. M. J. Duff, "Observations on conformal anomalies," Nucl. Phys. **B125**, 334–348 (1977).
3. S. M. Christensen and M. J. Duff, "Axial and conformal anomalies for arbitrary spin in gravity and supergravity," Phys. Lett. **B76**, 571–574 (1978); "New gravitational index theorems and supertheorems," Nucl. Phys. **B154**, 301–342 (1979).
4. D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279–360 (2003).
5. A. H. Chamseddine and A. Connes, "The Spectral Action Principle," Commun. Math. Phys. **186**, 731–750 (1997); "Why the Standard Model," J. Geom. Phys. **58**, 38–47 (2008) [arXiv:0706.3688]; "Noncommutative Geometry as a Framework for Unification of all Fundamental Interactions including Gravity," Fortsch. Phys. **58**, 553–600 (2010) [arXiv:0812.0165].
6. J. Lafontaine, "Remarques sur les variétés conformément plates," Math. Ann. **282**, 313–333 (1988).
7. Z. Chang, P. Gursky, and C. Yang, "An example of a complete conformally flat manifold of negative Ricci curvature," Int. Math. Res. Not. **2003**, 1–9 (2003).

---

*v0.3 pre-submission draft. Self-contained: the $F_1$ decomposition (§2) and the $S^3 \times S^1$ uniqueness within the product-of-spheres family (§5) are established here from curvature arithmetic alone; no external framework is required for either result.*
