---
title: "The Shape Where the Anomaly Vanishes"
subtitle: "A tier-3 explanatory note on F₁ = −18 C² + 11 E₄ and the vanishing of the trace-anomaly combination on S³ × S¹ among product-of-spheres 4-manifolds"
author: "G. White"
date: "2026-06 (v10.19.0)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## The result in one paragraph

When physicists do quantum-field calculations on a curved 4-dimensional space, certain extra terms appear that wouldn't appear in flat space. They are called *anomalies*, not because anything has gone wrong but because they reflect the curvature of the background. One specific anomaly term — call it F₁ for the rest of this note — shows up when you compute the trace of a fundamental matrix that physicists use to characterise such backgrounds. The companion paper makes two claims about F₁. First, that F₁ is built out of just two structural ingredients — the curvature's *shape-distorting* part and the curvature's *topological* part — with the curvature's overall *size* dropping out exactly. Second, that among a small natural family of candidate 4-dimensional shapes (products of round spheres with flat factors), one specific shape is the unique member of that family where both structural ingredients vanish at every point, making F₁ vanish identically. The shape is a 3-dimensional sphere combined with a circle, written S³ × S¹.

## Why this matters in one paragraph

S³ × S¹ has been showing up across mathematical physics as a candidate spacetime for various quantum-gravity programmes — particularly the *spectral action principle*, a programme that derives physical laws from operator spectra on curved geometries. The uniqueness result establishes one structural reason why: on S³ × S¹, the anomaly term that would otherwise complicate certain heat-kernel computations identically vanishes. The 4-dimensional shape we live on (whichever one that turns out to be) does not have to be S³ × S¹; the result is not making that claim. What the result *is* doing is identifying one specific reason why, when you list the candidate 4-dimensional shapes that quantum-gravity programmes might want to build physics on, S³ × S¹ stands out from the others in a structurally clean way.

---

## What the curvature pieces actually mean

Curvature in 4 dimensions can be decomposed into three pieces, each capturing a different aspect of how the space bends.

**Shape-distorting curvature** (the Weyl part): if a small cluster of test particles is stretched in one direction while being squeezed perpendicular to that direction without changing the total volume, that is shape-distorting curvature at work. Mathematicians write it as C, and the quantity C² (Weyl-squared) measures the magnitude of this distortion at each point.

**Topological curvature** (the Euler density): this encodes a shape's global topological signature. In 4 dimensions there is a pointwise Euler density (call it E₄) built from the Riemann curvature at each location. When you integrate E₄ over a closed 4-dimensional space, you recover the 4-dimensional Euler characteristic — a whole-number topological label of the shape.

**Size-only curvature**: a single number, R, that measures the overall scalar curvature at a point.

These three pieces — Weyl-squared C², Euler density E₄, and scalar-squared R² — form a *basis* for the curvature-squared content of any 4-dimensional space. The paper's first algebraic result is that F₁, when written in this basis, has *exactly zero* size-only piece. F₁ is composed entirely of shape-distorting and topological parts: specifically, F₁ = −18 C² + 11 E₄. The size-only piece cancels by exact integer arithmetic.

---

## The family of candidate shapes

To find where F₁ vanishes, the paper considers a natural small family of 4-dimensional shapes:

- **p = 2:** S² × T² — a 2-sphere combined with a flat torus
- **p = 3:** S³ × S¹ — a 3-sphere combined with a flat circle (the one we care about)
- **p = 4:** S⁴ — a 4-sphere by itself, with no flat factor

A note on honest scope: the uniqueness result is *within this family*, not across all 4-dimensional shapes. The flat 4-torus T⁴ and closed-hyperbolic N³ × S¹ lie outside this product-of-spheres family and also achieve simultaneous vanishing. The result establishes that within the natural small product-of-spheres family, S³ × S¹ is the unique candidate.

---

## Where the cancellation happens

On the 4-sphere (p = 4): Weyl-squared C² vanishes (the 4-sphere is conformally flat) but the 4-sphere has nonzero topology so E₄ ≠ 0. Result: C² = 0 but E₄ ≠ 0.

On S² × T² (p = 2): the Euler density vanishes (the product with a flat factor kills it) but the Weyl-squared part is nonzero. Result: E₄ = 0 but C² ≠ 0.

On S³ × S¹ (p = 3): *both* pieces vanish. The 3-sphere has equal curvature in all three of its directions, which makes the product's Weyl tensor vanish pointwise. At the same time, the product with a flat circle kills the pointwise Euler density. Result: C² = 0 *and* E₄ = 0 simultaneously.

The cancellation at p = 3 is not a coincidence. It is the structural fact that S³ has *isotropic* curvature (the same in all three directions) while still being curved enough to combine non-trivially with the circle. Only S³ × S¹ has the combination of isotropic curvature and zero topological density that makes both anomaly pieces vanish at every point.

Therefore: F₁ = −18 C² + 11 E₄ vanishes identically (pointwise) on S³ × S¹, and S³ × S¹ is the unique value of p in the small product family at which this happens.

---

## Why this matters for quantum-gravity programmes

When you do spectral-action heat-kernel computations on a generic 4-manifold, the trace anomaly is some non-trivial function of position, and you have to carry it through every step of the calculation. When you do those computations on S³ × S¹, the anomaly identically vanishes — both pieces are zero at every point — and your calculation simplifies dramatically. That simplification is one of several reasons why S³ × S¹ has emerged as a canonical background for spectral-action-based quantum-gravity programmes.

---

## What would falsify the result

The algebraic identity F₁ = −18 C² + 11 E₄ is a finite linear-algebra fact. Any error in the calculation would be caught by direct verification: substitute back into the original definition of F₁ and check that the coefficients of R², R_μν², and R_μνρσ² come out to (5, −8, −7). The paper does this cross-check explicitly; the arithmetic is exact.

The uniqueness statement is a finite calculation on three candidate manifolds. Any error would be caught by re-computing C² and E₄ on S², S³, S⁴ products with their respective flat complements, using the standard expressions for the curvature tensors on round spheres.

---

## Provenance

This is a tier-3 explanatory note. It is a companion to the standalone technical paper *F₁ = −18 C² + 11 E₄ and the vanishing of the trace-anomaly combination on S³ × S¹ among product-of-spheres 4-manifolds* (Paper F1 Trace Anomaly S3xS1 Uniqueness Clean Standalone). The companion note *A Coupling Forced by Geometry* takes up a related geometric result on the same Hopf-bundle background. The result is framework-independent: no specific cosmological commitments are required for the algebraic identity or the uniqueness verification; the result is a math-physics theorem about closed product 4-manifolds.

---

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

— G. White, 2026-06 (tier-3 explanatory note, v10.19.0 rebuild).
