---
title: "A Polynomial That Vanishes on the 3-Sphere"
subtitle: "A tier-3 explanatory note on the heat-kernel a₄ cancellation for S³"
author: "G. White"
date: "2026-06 (cleaned tier-3 representation; v10.19.0 corpus)"
---

*Independent Researcher, Auckland, New Zealand · gregwhite00@gmail.com*

## The result in one paragraph

When you compute a particular curvature combination that appears in quantum-field calculations on curved spaces — specifically the combination 5R² − 8R_μν² − 7R_μνρσ² that is the standard "a₄" coefficient from heat-kernel calculations — and evaluate it pointwise on a sphere of dimension *d*, the result factorises cleanly as *d*(*d*−1)(*d*−3)(5*d*+2). The factorisation makes immediately visible that *d* = 3 is the unique integer dimension *d* ≥ 2 at which this combination vanishes non-trivially. This is the algebraic content of an established fact in spectral geometry: Alain Chamseddine and Alain Connes demonstrated in 2008 that the spectral action's heat-kernel coefficients vanish on S³ × S¹, and Mistry, Pinzul, and Rachwał in 2020 noted that "the spectral action somehow prefers this background." The present note's contribution is small: a clean polynomial factorisation that makes the *d*-specificity transparent at the algebraic level, and a structural framing of *d* = 3 as a spectral-dynamical selection criterion alongside the other structural arguments for the 3-sphere. The substantive cancellation was established before; this is a refinement of the algebraic statement.

## Why this matters in one paragraph

The 3-sphere is already a strong structural candidate for a closed three-dimensional spatial geometry — parallelisability, Lie-group uniqueness, parity, and related arguments say so before this note speaks. The present result adds one more **structural** filter: a spectral-dynamical argument from heat-kernel mathematics. The polynomial picks out *d* = 3 algebraically. Combined with the further fact that S³ × S¹ is — within the small product-of-spheres family {S^p × F^q : p ∈ {2,3,4}} — the unique member where the spectral action's a₄ combination vanishes (not unique among all closed 4-manifolds: flat T⁴ and closed-hyperbolic N³ × S¹ also have Weyl-flat / Euler-zero structure outside that family, and the present note states the restriction explicitly), the case for S³ is reinforced. That reinforcement is mild and **does not by itself pick the universe from data** — the next section separates structural filtering from observational testing.

*Scope.* The substantive cancellation reported here is established prior work; this note's role is to make the *d*-specificity transparent algebraically and to situate the result within the framework's broader architecture. No novelty is claimed for the cancellation itself.

---

## What the heat-kernel coefficient is

*Standalone glossary entry:* (heat-kernel expansion + a₀/a₂/a₄.)

When physicists do quantum-field calculations on a curved background spacetime, they encounter a standard mathematical tool called the *heat-kernel expansion*. The heat kernel is a function that solves a particular differential equation associated with the Laplace or Dirac operator on the background; expanding it in powers of a small parameter gives a series of coefficients, each of which is a specific combination of curvature invariants of the background.

The first non-trivial coefficient is called *a₂* and is proportional to the scalar curvature R. The next is *a₄*, which for the squared Dirac operator on a 4-dimensional Riemannian manifold has the standard Seeley-DeWitt form

a₄ ∝ 5R² − 8R_μν² − 7R_μνρσ²

where R is the Ricci scalar, R_μν is the Ricci tensor, R_μνρσ is the full Riemann tensor, and the squares are pointwise scalar contractions. The specific coefficients (5, −8, −7) are standard heat-kernel mathematics (Gilkey 1984), and the combination appears in the bosonic spectral action of Connes and Chamseddine — a programme that derives physical laws from the spectrum of a Dirac operator on a curved geometry.

This combination doesn't just *exist*; it has a specific value at every point on any given Riemannian manifold. The question the present note addresses is: what value does this combination take when the manifold is the round unit sphere S^d?

## The polynomial

For the unit sphere S^d with the standard round metric, the curvature invariants take simple values:

- R = d(d − 1)
- R_μν² = d(d − 1)²
- R_μνρσ² = 2d(d − 1)

Substituting these into the a₄ combination gives a polynomial in d. After algebraic simplification, the polynomial factorises:

5R² − 8R_μν² − 7R_μνρσ² = **d(d − 1)(d − 3)(5d + 2)**

The roots of the quartic are *d* ∈ {−2/5, 0, 1, 3}. The negative and fractional roots are not physically meaningful sphere dimensions; the integer roots are *d* = 0 (trivial), *d* = 1 (trivial — the circle has zero curvature, so all invariants vanish identically), and *d* = 3.

Here is the table evaluated at small integer dimensions:

| d | R | R_μν² | R_μνρσ² | a₄ combination |
|---|---|-------|---------|---------------|
| 1 | 0 | 0 | 0 | 0 (trivial: circle is flat) |
| 2 | 2 | 2 | 4 | −24 |
| **3** | **6** | **12** | **12** | **0** (non-trivial cancellation) |
| 4 | 12 | 36 | 24 | 264 |
| 5 | 20 | 80 | 40 | 1080 |
| 6 | 30 | 150 | 60 | 2880 |
| 7 | 42 | 252 | 84 | 6216 |

The cancellation at d = 3 is the substantive content. Among integer sphere dimensions d ≥ 2, only the 3-sphere produces a vanishing a₄ combination, and the factorisation makes this transparent at the algebraic level.

## What's established and what's new

A scrupulously honest framing matters here. The substantive content is established in the literature; the present note's contribution is a small refinement.

*Established (prior art):*

- **Chamseddine–Connes 1996** introduced the spectral action principle and computed the a₄ coefficient with the standard (5, −8, −7) relative weights for the Dirac Laplacian.
- **Gilkey 1984** is the standard heat-kernel reference; the (5, −8, −7) combination follows from Gilkey's general formulas applied to the squared Dirac operator.
- **Chamseddine–Connes 2008** ("The Uncanny Precision of the Spectral Action") demonstrated by direct calculation that the spectral action's a₄ coefficient vanishes on S³ × S¹, and explicitly verified that it is *non-zero* on S⁴, with the remark that "this vanishing of the Seeley coefficients does not hold for the 4 sphere." The d = 3 specificity is recognised at the spectral-action level in this paper.
- **Mistry–Pinzul–Rachwał 2020** generalised the analysis to general conformally flat 4-manifolds and found the cancellation does *not* extend. They concluded explicitly: "the cancellation of the 6-order terms for this background should be considered as accidental: it is not automatic but happens due to the non-trivial cancellation between terms depending on the curvature. Because this happens exactly for the coefficients fixed by the spectral action, one might speculate that the spectral action somehow prefers this background."

*New here (small refinement):*

- The explicit polynomial factorisation **d(d − 1)(d − 3)(5d + 2)** as a function of the sphere dimension d. The algebra is elementary — direct substitution into the standard sphere curvature invariants — but the explicit factorised form doesn't appear in the surveyed literature (Chamseddine–Connes 1996; Chamseddine–Connes 2008; Mistry–Pinzul–Rachwał 2020; the Marcolli / van den Dungen–van Suijlekom spectral-action surveys).
- A structural framing of the result as a *spectral-dynamical selection criterion* for d = 3: alongside the well-known arguments for the 3-sphere from parallelisability, Lie-group structure, and parity properties, there is now also a spectral-dynamical argument from the algebraic form of the heat-kernel coefficient.

*What's not claimed:*

A specialist in spectral geometry, reading the present result, would correctly identify the substantive content as Chamseddine–Connes 2008's. The d-parametric factorisation is a small refinement that makes the d-specificity transparent in the perturbative regime; it doesn't change the underlying mathematics. The result is suitable as a structural argument within the framework's broader programme, and as a clean algebraic statement to cite when discussing the framework's d = 3 selection. It is *not* a standalone discovery in spectral geometry.

## The combination with Hopf fibrations

A separate observation tightens the structural reading. Hopf fibrations of the form S^d → S^(d−1) exist precisely for *d* = 1, 3, 7 (by Adams' theorem). Of these:

- *d = 1*: trivial. The circle has zero curvature; the cancellation is degenerate.
- *d = 3*: the Hopf fibration S³ → S² is non-trivial. The spectral cancellation holds.
- *d = 7*: the Hopf fibration S⁷ → S⁴ exists. The spectral cancellation does *not* hold (evaluating the polynomial at d = 7 gives 6216, not zero).

So d = 3 is the unique sphere dimension where the Hopf fibration structure and the spectral cancellation coexist non-trivially. This is a structural correlation worth noting: among the three sphere dimensions that admit Hopf fibrations, only one (S³) also satisfies the algebraic spectral cancellation. The combination of the two structural facts — Hopf fibration plus spectral cancellation — uniquely picks out S³ at this level of the structural argument.

This is what the framework leverages at the **structural** level. The 3-sphere is distinguished from multiple independent directions: parallelisability, Lie group, parity, Hopf fibration, and the present spectral-dynamical argument. None of that is yet a telescope measurement.

## From structural filters to observation (honest scope)

The cancellation result is about **which geometries the spectral action can use cleanly**, not about proving from the CMB that nature chose S³. The path from here to "leading candidate for what we observe" is a **chain**; the present section names each link so nothing is oversold.

**Three structural filters:**

1. **Sphere dimension.** The a₄ polynomial vanishes non-trivially only at *d* = 3 among integer sphere dimensions *d* ≥ 2. That rules out S², S⁴, S⁵, … for this cancellation — not flat ℝ³, but also not higher spheres.

2. **Hopf plus cancellation.** Hopf fibrations exist for *d* = 1, 3, 7 only. Only *d* = 3 has both a non-trivial Hopf map **and** the spectral cancellation. S⁷ has Hopf structure but fails the polynomial (6216 at *d* = 7).

3. **Four-dimensional background.** Within the small product-of-spheres family {S^p × F^q : p ∈ {2,3,4}}, only S³ × S¹ has both Weyl-squared and Euler density vanishing pointwise, so the trace-anomaly combination vanishes there. The uniqueness is **within that family**, not across all closed 4-manifolds: flat T⁴ and closed-hyperbolic N³ × S¹ also have Weyl-flat / Euler-zero structure outside the family, and the Mistry–Pinzul–Rachwał (2020) result is that the cancellation does **not** extend to arbitrary conformally flat 4-manifolds. Generic "nice" backgrounds are disfavoured relative to S³ × S¹ **for these fixed spectral-action coefficients**.

Together, these are **compatibility filters**: they narrow the class of backgrounds on which the Chamseddine–Connes expansion is structurally clean and aligned with Hopf-based machinery elsewhere in the framework.

**What this note does *not* claim:**

- **Not** that the observable universe is spatially flat (*k* = 0). S³ is **positively curved and closed**. Observed near-flatness is handled elsewhere (large-radius S³ after long expansion looks Euclidean locally — see *The Shape of Time*, Ch 3).

- **Not** that geometry sits in a **least-action equilibrium**. The spectral **action** is the organising principle, but the present result evaluates an expansion on a **fixed** background. Vanishing a₄ means a curvature term drops out of that expansion on S³ × S¹ — not that nature minimised *S*.

- **Not** a Bayesian win over every cosmological model from data. The present result does not fit parameters to Planck or NuFIT.

**Where observation enters (downstream — not in the present note):**

Once the spectral triple is **fixed** on S³ × S¹ (plus internal algebra), separate work in the framework's master corpus produces a small set of structural results, each carried at its stated register. Clean structural results include the dark-matter-to-baryon ratio κ ≈ 5.5 (one structural derivation through the Hopf-bundle bare coupling κ₀ = 3/√(4π) plus one algebraic closure κ = κ₀/(1−κ₀)), the maximal CP phase δ_J = π/2 from the bilateral CPN-conjugate structure, the gauge-birth thermal scale T_GB, and the maximal atmospheric mixing θ₂₃ = π/4 inherited from the established μ–τ symmetry programme. Other results sit at honestly-scoped registers and the framework states them as such:

- The solar neutrino mass m_ν₂ at ≈ 0.993× the measured splitting is a confluence-tier match used as the M_R-normalisation point in the framework's spectral-action arithmetic — not an independent zero-parameter hit. The atmospheric leg with the same M_R overshoots by ≈ 1.5×, which is stated and held open.
- The primordial spectral index n_s ≈ 0.97 is consistent-with but **not derived-from** the framework. The Hartle–Hawking under-determination of the slow-roll tilt is an open structural question; the framework does not claim n_s as derived.
- The baryon asymmetry η_B is at structural-consistency-with-a-geometric-heavy-neutrino-scale register, not zero-parameter.

**That** combined picture — clean structural predictions at their stated registers plus the honestly-scoped consistency checks — is the empirical filter. If precision data moves outside the structural predictions with the substrate held fixed, the substrate fails. Not because a₄ stopped vanishing, but because the broader confluence breaks.

**"Leading candidate" in plain language:** within this architecture, S³ × S¹ is the geometry that (i) passes the structural filters above, (ii) keeps the spectral expansion clean, (iii) supports the Hopf and neutrino machinery, and (iv) — tested elsewhere — yields the structural results listed above at their stated registers. The present note establishes (i) and part of (ii); it **reinforces** a spatial S³ the framework already uses for other reasons; it does **not** close the observational case by itself.

## What would break it

The polynomial factorisation is a finite algebraic identity verifiable in a few lines. Any error would be caught by direct calculation: substitute the standard sphere curvature invariants into the a₄ combination, factorise the resulting polynomial. The roots {−2/5, 0, 1, 3} are reproducible.

If the curvature invariants on the unit sphere S^d turn out to be different from the standard (R = d(d−1), R_μν² = d(d−1)², R_μνρσ² = 2d(d−1)), the polynomial would change. These are textbook formulas; any error would propagate from there.

If the a₄ coefficient's (5, −8, −7) weights are wrong (Gilkey 1984, Chamseddine–Connes 1996), the polynomial would be different. The combination's coefficients are well-established.

What the result is *not* doing is proving anything new about the deeper spectral-action structure. The cancellation on S³ × S¹ (Chamseddine–Connes 2008) and the "spectral action prefers this background" framing (Mistry–Pinzul–Rachwał 2020) stand on their own. The present polynomial factorisation is a refinement to those established results.

## Positioning

This note sits within a family of programmes that take the Standard Model to arise from division-algebra and noncommutative-geometric structure, with time and spacetime emergent rather than fundamental. The relevant neighbours include the spectral action / noncommutative-geometry programme (Chamseddine–Connes 1996, 1997, 2008, 2010), the division-algebra Standard Model line (Günaydin–Gürsey 1973; Furey 2014, 2018; Dubois-Violette 2016; Todorov–Dubois-Violette 2018), the relational and emergent-time programmes (Page–Wootters 1983; Rovelli 1991; Connes–Rovelli 1994; Wheeler–DeWitt; Barbour; experimental test Moreva et al. 2013), and the non-associativity-as-time line (Gogberashvili 2004; Köplinger–Dzhunushaliev–Gogberashvili). The closest architectural relative is T. P. Singh's octonionic / pre-quantum pre-spacetime theory (2019–2025), which assembles emergent time + octonionic-NCG + exceptional-Jordan Standard Model + Connes time + Majorana neutrinos + left–right symmetry into one framework.

The framework here — Non-Temporal Emergence — is a distinct implementation within that class, not a new class. Its own choices differentiate it within the family: an e-fold count coordinate N as fundamental and proper time as emergent via t = iΔN (a specific Wick-rotation proposal for what time emerges from, distinct from modular or Connes time), the S³ × S¹ Hopf substrate as the load-bearing geometric commitment, the bilateral CPN-conjugate two-orientation cosmology, and specific identifications including κ₀ = 3/√(4π) from the Hopf-bundle bare coupling, the dark-matter / baryon ratio as a cross-sector fixed point, and a CLFV amplitude ratio tan²θ₂₃ at the seesaw level. NTE assumes quantum mechanics rather than deriving it, carries no trace dynamics, no Grassmann-matrix aikyons, no spontaneous-localisation collapse, no E₈×E₈, and no sedenions; its distinctiveness sits in the specific assembly and its specific predictions, not in the existence of the assembly.

The framework does not fit numbers. Every quantity is either **structural** (fixed by geometry / algebra) or **honestly scoped** as conditional, a cross-check, or open. Results are tiered explicitly — derived, re-derived (credited), imported (credited), or open. This is a deliberate methodological discipline and a deliberate contrast with coupling-constant "derivations" elsewhere in the class that rely on assembled closed forms plus corrections.

**The present note's cancellation result is one of the established prior results NTE adopts; the d-parametric polynomial is the small algebraic refinement the note offers.** No novelty is claimed for the cancellation itself.

## Provenance

This is a tier-3 explanatory note for the curious reader. It is not a standalone novelty claim and is not the source of any framework prediction. The substantive content — the heat-kernel a₄ cancellation on S³ × S¹ and the d = 3 spectral-dynamical selection — sits in the prior literature, with Chamseddine–Connes (1996, 2008) and Mistry–Pinzul–Rachwał (2020) carrying the original demonstrations and the spectral-action framing, and Gilkey (1984) as the standard heat-kernel reference. The present note's algebraic refinement (the explicit polynomial factorisation that makes the d = 3 specificity transparent as a root rather than a numerical coincidence) is a small didactic increment.

The framework's full development of the architectural role of S³ × S¹ — including the chord of structural results that this substrate carries (developed in Companion 12, "the chord") and the bilateral cosmology and parameter ledger (developed in Part 2 Structure and Part 3 Accounting of the framework's master corpus) — is documented separately and is not duplicated here. Readers interested in why the framework reaches for S³ × S¹ at the broader level should follow those threads. *The Shape of Time*, Chapter 3, gives the lay-register account of how large-radius S³ after long expansion looks Euclidean locally.

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

— G. White, 2026-06 (cleaned tier-3 representation).
