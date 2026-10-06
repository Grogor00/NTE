---
title: "Vanishing of the conformal trace-anomaly density on S³ × S¹ and the heat-kernel coefficients of the product Dirac operator"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-20 (v0.1 pre-submission draft)"
---

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

---

## Abstract

We compute the Seeley–DeWitt heat-kernel coefficients $a_0$, $a_2$, $a_4$ of the spinor Laplacian on the closed Riemannian product $M = S^3 \times S^1$, with $S^3$ the round unit 3-sphere and $S^1$ a flat circle. We show that the fourth coefficient vanishes identically, $a_4 = 0$, as a consequence of two pointwise curvature identities on this manifold: the Weyl tensor vanishes ($C^2 = 0$) and the Gauss–Bonnet Euler density vanishes ($E_4 = 0$). We give the elementary reason — the standard four-dimensional conformal trace-anomaly combination $5R^2 - 8R_{\mu\nu}^2 - 7R_{\mu\nu\rho\sigma}^2$ for a Dirac field decomposes as $-18\,C^2 + 11\,E_4$ in the Weyl–Euler basis, so simultaneous Weyl-flatness and Euler-flatness force it to zero. We then observe that among closed product manifolds $S^p \times F^q$ with $F^q$ flat and total dimension four ($p \in \{2,3,4\}$), $p = 3$ is the only value for which $C^2$ and $E_4$ vanish *simultaneously and pointwise*; we state precisely what this does and does not establish, noting that uniqueness does not extend to all closed 4-manifolds (flat $T^4$ and closed hyperbolic $N^3 \times S^1$ are Weyl-flat or Euler-flat outside this product-of-spheres family; cf. Lafontaine 1988; Chang–Gursky–Yang 2003). The vanishing of $a_4$ has a direct physical consequence in spectral-action models built on this manifold: the higher-derivative ($R^2$, Weyl-squared) sector of the induced gravitational action is absent at this order, and any quantity previously extracted from a non-zero $a_4$ density on this substrate must be sourced elsewhere. The results are self-contained and use only standard heat-kernel technology (Gilkey 1995; Vassilevich 2003).

---

## 1. Introduction

The Seeley–DeWitt (heat-kernel) coefficients of a Laplace-type operator on a closed Riemannian manifold encode, term by term, the local curvature content of the induced effective action. For a second-order operator of Laplace type on a four-manifold, the small-$t$ expansion of the heat trace is

$$\mathrm{Tr}\,e^{-tD^2} \;\sim\; \sum_{k=0}^{\infty} a_{2k}(D^2)\, t^{k-2}, \qquad t \to 0^+,$$

with $a_0$ the volume term, $a_2$ the Einstein–Hilbert term, and $a_4$ the four-derivative (curvature-squared) term. In spectral-action approaches to gravity and unified models, these coefficients *are* the bosonic action: $a_0$ contributes a cosmological term, $a_2$ Newton's constant, and $a_4$ the higher-derivative ($R^2$, Weyl-squared, Gauss–Bonnet) sector (Chamseddine–Connes 1997; Vassilevich 2003).

The manifold $M = S^3 \times S^1$ — the round unit 3-sphere times a flat circle — is of independent interest as a Euclidean background: it is the conformal compactification underlying finite-temperature field theory on $S^3$, and it appears as a substrate in noncommutative-geometry model-building. This note establishes a clean structural fact about it: the four-derivative heat-kernel coefficient of the Dirac operator vanishes identically on $M$, and it does so for a transparent reason rooted in the conformal trace anomaly.

The argument is elementary and self-contained. In Section 2 we record the curvature of $M$. In Section 3 we give the heat-kernel coefficients $a_0$ and $a_2$. In Section 4 we prove $a_4 = 0$ via the Weyl–Euler decomposition of the Dirac trace-anomaly combination. In Section 5 we examine the product-of-spheres family and state the precise (restricted) sense in which $p = 3$ is distinguished. Section 6 states the consequence for spectral-action models and the scope of the result.

---

## 2. Geometry of $M = S^3 \times S^1$

Let $S^3$ carry the round metric of unit radius and $S^1$ a flat circle of circumference $\beta$. The product metric is $g_M = g_{S^3} \oplus g_{S^1}$.

The round unit $S^3$ has constant sectional curvature $+1$, hence

$$\mathrm{Ric}_{S^3} = 2\,g_{S^3}, \qquad R_{S^3} = 6.$$

The circle is flat. The product therefore has

$$R_M = 6, \qquad \mathrm{Ric}_M = \mathrm{diag}(2,2,2,0), \qquad \mathrm{Vol}(M) = 2\pi^2 \beta,$$

using $\mathrm{Vol}(S^3) = 2\pi^2$ for the unit 3-sphere.

The quadratic curvature invariants on $M$ are inherited from $S^3$ (the flat $S^1$ direction contributes nothing). For the round unit $S^3$ embedded as the curved factor:

$$R_{\mu\nu\rho\sigma}^2\big|_M = 12, \qquad R_{\mu\nu}^2\big|_M = 12, \qquad R^2\big|_M = 36. \tag{2.1}$$

These follow from the maximal symmetry of $S^3$: with $R_{ijkl} = (g_{ik}g_{jl} - g_{il}g_{jk})$ on the unit 3-sphere, $R_{ijkl}^2 = 2\cdot 3 = 6$ within $S^3$, and $R_{ij}^2 = 4\cdot 3 = 12$, $R^2 = 36$; promoting to the 4-manifold $M$ (with the flat circle adding no curvature) gives (2.1). We use (2.1) throughout.

---

## 3. Heat-kernel coefficients $a_0$ and $a_2$

For a Dirac operator $D$ on a closed spin 4-manifold, $D^2$ is of Laplace type with $D^2 = -\nabla^2 + E$, where by the Lichnerowicz formula $E = R/4$ (acting on the rank-4 spinor bundle). The standard Gilkey coefficients (Gilkey 1995; Vassilevich 2003), with spinor-bundle rank $r = 4$, give:

**Volume term.**

$$a_0 = \frac{r}{(4\pi)^2}\int_M \sqrt{g}\, d^4x = \frac{4}{16\pi^2}\,\mathrm{Vol}(M) = \frac{\mathrm{Vol}(M)}{4\pi^2} = \frac{2\pi^2\beta}{4\pi^2} = \frac{\beta}{2}.$$

**Einstein–Hilbert term.** For the Dirac operator the $a_2$ density is $\dfrac{1}{(4\pi)^2}\,\mathrm{tr}\!\left(\tfrac{1}{6}R - E\right) = \dfrac{1}{(4\pi)^2}\,\mathrm{tr}\!\left(\tfrac{1}{6}R - \tfrac{1}{4}R\right) = -\dfrac{r}{(4\pi)^2}\cdot\dfrac{R}{12}.$ Integrating over $M$ with $R = 6$, $r = 4$:

$$a_2 = -\frac{r}{(4\pi)^2}\cdot\frac{1}{12}\int_M R\,\sqrt{g}\, d^4x = -\frac{4}{16\pi^2}\cdot\frac{6\cdot 2\pi^2\beta}{12} = -\frac{\beta}{4}.$$

These are the volume (cosmological) and Einstein–Hilbert contributions respectively; their signs and normalisations follow the Gilkey–Vassilevich convention.

---

## 4. The fourth coefficient vanishes: $a_4 = 0$

### 4.1 The Dirac $a_4$ density

For the Dirac operator with $E = R/4$ on a four-manifold, the integrated fourth Seeley–DeWitt coefficient reduces (after using the Gauss–Bonnet term and discarding total derivatives) to a multiple of the conformal trace-anomaly combination (Gilkey 1995 §4.8; Vassilevich 2003 §4.3; Birrell–Davies 1982):

$$a_4 = \frac{1}{(4\pi)^2}\,\frac{1}{360}\int_M \Big[\,5R^2 - 8R_{\mu\nu}^2 - 7R_{\mu\nu\rho\sigma}^2\,\Big]\sqrt{g}\, d^4x. \tag{4.1}$$

The bracket is the standard four-dimensional Dirac-field trace-anomaly polynomial.

### 4.2 Weyl–Euler decomposition

In four dimensions the curvature-squared invariants can be re-expressed in the basis $\{C^2, E_4, R^2\}$, where

$$C^2 = R_{\mu\nu\rho\sigma}^2 - 2R_{\mu\nu}^2 + \tfrac{1}{3}R^2$$

is the Weyl tensor squared, and

$$E_4 = R_{\mu\nu\rho\sigma}^2 - 4R_{\mu\nu}^2 + R^2$$

is the Gauss–Bonnet (Euler) density. A direct substitution gives the identity

$$5R^2 - 8R_{\mu\nu}^2 - 7R_{\mu\nu\rho\sigma}^2 \;=\; -18\,C^2 + 11\,E_4. \tag{4.2}$$

*Check of (4.2).* Expand the right-hand side:
$-18C^2 = -18R_{\mu\nu\rho\sigma}^2 + 36R_{\mu\nu}^2 - 6R^2$, and $11E_4 = 11R_{\mu\nu\rho\sigma}^2 - 44R_{\mu\nu}^2 + 11R^2$. Summing: $(-18+11)R_{\mu\nu\rho\sigma}^2 + (36-44)R_{\mu\nu}^2 + (-6+11)R^2 = -7R_{\mu\nu\rho\sigma}^2 - 8R_{\mu\nu}^2 + 5R^2$, which is the left-hand side. ∎

The $R^2$ coefficient cancels because $-18\cdot\tfrac{1}{3} + 11 = -6 + 11 = 5$ matches and the cross-terms close; equivalently the trace-anomaly polynomial has no independent $R^2$ piece in this basis, as required for a conformal anomaly.

### 4.3 Pointwise vanishing on $M$

Evaluate $C^2$ and $E_4$ on $M = S^3 \times S^1$ using (2.1):

$$C^2\big|_M = 12 - 2(12) + \tfrac{1}{3}(36) = 12 - 24 + 12 = 0,$$
$$E_4\big|_M = 12 - 4(12) + 36 = 12 - 48 + 36 = 0.$$

Both vanish **pointwise**. ($C^2 = 0$ reflects that $S^3 \times S^1$ is locally conformally flat — a round 3-sphere times a line is conformally flat; $E_4 = 0$ reflects that the four-dimensional Euler density of a product with a flat factor vanishes.)

By (4.2), the integrand of (4.1) is $-18C^2 + 11E_4 = 0$ pointwise. Therefore

$$\boxed{a_4(D^2)\big|_{S^3\times S^1} = 0.}$$

Equivalently, substituting (2.1) directly into the original polynomial: $5(36) - 8(12) - 7(12) = 180 - 96 - 84 = 0$, confirming the same result without the basis change.

### 4.4 A caution on the integrand

The vanishing is specific to the **Dirac** trace-anomaly polynomial $5R^2 - 8R_{\mu\nu}^2 - 7R_{\mu\nu\rho\sigma}^2$. A different field content (scalar, vector) has different coefficients and a generally non-zero $a_4$ on the same manifold; and a naive curvature polynomial with the wrong coefficients (e.g. $5R^2 - 2R_{\mu\nu}^2 + 2R_{\mu\nu\rho\sigma}^2$) does **not** vanish on $M$ — it gives $180 - 24 + 24 = 180 \neq 0$. The result $a_4 = 0$ holds for the spinor Laplacian with $E = R/4$, and only because both $C^2$ and $E_4$ vanish; it is not a generic feature of the manifold across all operators.

---

## 5. The product-of-spheres family

It is natural to ask how distinguished $M = S^3 \times S^1$ is. Consider closed product manifolds $S^p \times F^q$ of total dimension four, with $S^p$ a round sphere and $F^q$ flat (so $q = 4-p$ and $F^q$ is a flat torus or circle factor); the curved factor is the sphere. The relevant cases are $p \in \{2,3,4\}$.

- **$p = 2$** ($S^2 \times T^2$): $C^2 \neq 0$ and $E_4 \neq 0$. (A round $S^2$ times a flat 2-torus is not conformally flat in 4D, and its Euler density does not vanish pointwise.)
- **$p = 3$** ($S^3 \times S^1$): $C^2 = 0$ **and** $E_4 = 0$, as shown in §4.3.
- **$p = 4$** ($S^4$, with no room for a flat factor): $C^2 = 0$ (the round $S^4$ is conformally flat / Einstein) but $E_4 \neq 0$ (the Euler characteristic of $S^4$ is 2, so $\int E_4 \neq 0$).

Within this family, $p = 3$ is therefore the unique value for which the conformal trace-anomaly combination vanishes pointwise.

**Scope of the claim (stated precisely).** This is a finite check within the round-sphere-times-flat product family at $p \in \{2,3,4\}$. It is *not* a uniqueness theorem among all closed 4-manifolds. Other closed 4-manifolds outside this family also have one or both invariants vanishing: a flat 4-torus $T^4$ has $C^2 = E_4 = 0$ trivially (it is flat), and closed hyperbolic products $N^3 \times S^1$ can be locally conformally flat (Lafontaine 1988; Chang–Gursky–Yang 2003 classify conformally flat and related product structures). The statement here is the modest and correct one: *among $S^p\times F^q$ products of dimension four with a flat factor, only $p=3$ achieves simultaneous pointwise $C^2 = E_4 = 0$.* No broader uniqueness is claimed.

---

## 6. Consequence for spectral-action models, and scope

### 6.1 Consequence

In a spectral-action construction, the bosonic action induced by a Dirac operator on a four-manifold is, to leading orders, a sum of the heat-kernel coefficients weighted by moments of the cutoff function: schematically $S \sim f_4\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_0 a_4 + \cdots$. The result $a_4 = 0$ on $M = S^3\times S^1$ has a direct structural consequence:

**The four-derivative (curvature-squared) sector of the induced gravitational action is absent at this order on this background.** In particular there is no induced Weyl-squared or $R^2$ (Starobinsky-type) term from the $a_4$ coefficient on $S^3 \times S^1$, and any physical quantity that one might attempt to extract from a non-zero $a_4$ *density* on this substrate is not available — it must be sourced from a different coefficient, a different operator (e.g. a gauge-twisted Dirac operator carrying an external field strength, whose $a_4$ need not vanish), or a different background.

This is a constraint, not a prediction: it tells model-builders what the canonical untwisted product Dirac operator on this manifold can and cannot supply.

### 6.2 Scope and falsifiability

The results of this note are self-contained and rest only on:
1. the curvature of $S^3 \times S^1$, equation (2.1);
2. the standard Gilkey–Vassilevich heat-kernel coefficients for the Dirac operator;
3. the algebraic identity (4.2), checked explicitly.

They are falsifiable by direct computation: an independent evaluation of the curvature invariants (2.1), of the algebraic identity (4.2), or of the coefficients $a_0, a_2, a_4$ is a finite calculation that either confirms or refutes the stated values. In particular, any independent finding that $C^2 \neq 0$ or $E_4 \neq 0$ pointwise on $S^3 \times S^1$ would refute §4.3; and any error in (4.2) would be exposed by the expansion given beneath it.

What this note does **not** address: the spectral action's full content beyond these coefficients; gauge-twisted (inner-fluctuated) Dirac operators, whose $a_4$ involves the gauge field strength and is generally non-zero; the finite-part / zeta-function determinant; and any model-specific identification of $\beta$ or of the spinor content. These are deliberately outside the scope of a result that is meant to be checkable on its own terms.

---

## References

1. P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, 2nd ed. (CRC Press, 1995).
2. D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279–360 (2003) [arXiv:hep-th/0306138].
3. A. H. Chamseddine and A. Connes, "The spectral action principle," Commun. Math. Phys. **186**, 731–750 (1997) [arXiv:hep-th/9606001].
4. N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge University Press, 1982).
5. T. Friedrich, "Der erste Eigenwert des Dirac-Operators einer kompakten Riemannschen Mannigfaltigkeit," Math. Nachr. **97**, 117–146 (1980). (Dirac spectrum on $S^3$.)
6. J. Lafontaine, "Conformal geometry from the Riemannian viewpoint," in *Conformal Geometry* (Vieweg, 1988). (Conformally flat product structures.)
7. S.-Y. A. Chang, M. J. Gursky, and P. C. Yang, "A conformally invariant sphere theorem in four dimensions," Publ. Math. IHÉS **98**, 105–143 (2003).

---

*v0.1 pre-submission draft, 2026-06-20. Self-contained: all curvature values, the heat-kernel coefficients, and the algebraic identity (4.2) are derived or checked in the text; no external working notes are required to verify the result.*
