---
title: "The cosmological constant in NTE: unimodular suppression on a boundary-only geometry"
author: "Gregory Lyndon White"
date: "2026-06 (v10.19.0)"
---

*Part of NTE Corpus v10.19.0 (deposited 2026-06). Companion 11.*

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*This companion expands the cosmological-constant treatment stated in the master corpus (Part 2, structure; Part 3, accounting): it sets out in full why empty space does not gravitate at the catastrophic level, how NTE **adopts** the unimodular / trace-free formulation that achieves this (credited; not derived from the cited spectral-triple literature), and the precise boundary that separates what the framework derives from what it does not.*

---

## Abstract

The cosmological constant problem has two layers. The **old** problem asks why empty space is not deafeningly loud — why the quantum vacuum energy does not gravitate at the Planck-scale level a naive field-theory estimate predicts, an overestimate of order 10¹²⁰. The **new** problem asks why the residual, after any suppression, sits near 10⁻¹²² in Planck units rather than anywhere else.

NTE resolves the old problem (**adopted and credited**: unimodular / trace-free gravity) and is explicit that it does not, at present, resolve the new one. The resolution has a structural origin with two **related but not identical** readings. Geometrically, NTE adopts the unimodular / trace-free Einstein equations, in which a constant vacuum density does not source curvature (Λ at most an integration constant); the spectral action's leading extensive term is thereby prevented from gravitating under that adopted formulation. Ontologically, NTE's degrees of freedom live on the closed S³ boundary, not in a bulk interior; a vacuum energy that scales with four-volume is then the wrong object for a *constant* extensive mode, and the catastrophic 10¹²⁰ is the numerical signature of that category error. The ontology motivates the formal restriction, which is narrower: a time-varying vacuum still gravitates, so an accelerated epoch remains possible. **The formal reading governs.**

This suppression is **structural at leading order** and acts on the volume term, so it is independent of the subleading spectral data; in particular it does not rest on the fourth Seeley–DeWitt coefficient a₄, which in any case vanishes on the canonical S³×S¹ substrate. NTE **adopts** the suppression of the catastrophe; it does **not** derive the specific observed magnitude of Λ, and makes no such claim. Empty space is quiet because the adopted geometry forbids the loud *constant* term — not because large terms finely cancel, and not as a tuned coincidence.

---

## 1. The two cosmological constant problems

Every quantum field contributes zero-point energy to the vacuum. Summing modes to the Planck scale gives a vacuum energy density of order M_Pl⁴ — about 10¹²⁰ times the observed cosmological value. This is the largest failure of an order-of-magnitude estimate in physics, and it is robust: lowering the cutoff does not rescue it, since even an electroweak-scale cutoff leaves the estimate dozens of orders of magnitude too large, and the leading dependence is on the highest scale in the loop. The discrepancy is not a number that needs trimming; it is a sign that the calculation is asking the wrong question of the geometry.

The failure is structural in a precise sense. Quantum field theory assigns the vacuum an energy density that, fed into the ordinary Einstein equations, couples to the *total* four-volume and curves spacetime accordingly. General relativity, taken in that ordinary form, has no mechanism to refuse the coupling. The two theories are individually consistent and jointly catastrophic exactly because a constant vacuum energy is allowed to gravitate extensively. Any resolution of the **old** problem must intervene at that junction — it must arrange that the extensive, volume-scaling piece of the vacuum energy does not source curvature.

The **new** problem is logically downstream and sharper. Suppose some mechanism removes the catastrophe, leaving a residual that is *intrinsically* small rather than the difference of two huge numbers. One still must explain why that residual takes the particular value observed (near 10⁻¹²² in Planck units) rather than zero or any other small number. The two problems call for different things: the old one for a structural prohibition, the new one for a derivation of a specific magnitude. NTE supplies the first and is candid that it does not supply the second.

## 2. Where the cosmological constant sits in the spectral action

NTE's gravitational sector is read from the spectral action of the framework's noncommutative geometry: the bosonic action is the heat-kernel expansion of the Dirac operator D on the canonical spectral triple, whose base is M = S³ × S¹ (closed compact spatial 3-sphere, compactified temporal circle) with a finite internal part. For a Laplace-type operator D² on a closed 4-manifold the relevant expansion is

  Tr f(D²/Λ²) ∼ f₄ Λ⁴ a₀ + f₂ Λ² a₂ + f₀ a₄ + …,

where the aₖ are integrals of local curvature invariants — the Seeley–DeWitt coefficients — and the fₖ are moments of the cutoff function. The physics of the leading three terms is standard and important here:

- **a₀ — the volume coefficient.** a₀ is proportional to the total volume of M. The term f₄ Λ⁴ a₀ is the **cosmological constant term** of the spectral action: an energy density of order Λ⁴ multiplying the volume. This is precisely the extensive, volume-scaling object whose naive value is catastrophic.
- **a₂ — the Einstein–Hilbert coefficient.** a₂ carries the scalar curvature integral; f₂ Λ² a₂ reproduces the Einstein–Hilbert action and fixes the gravitational scale.
- **a₄ — the fourth-order coefficient.** a₄ collects the curvature-squared (Weyl² and Euler) invariants — the conformal-anomaly content. It is subleading in the curvature expansion and plays no role in the leading cosmological term.

The cosmological constant problem, in this language, is the statement that f₄ Λ⁴ a₀ is enormous: the extensive a₀ mode, multiplied by Λ⁴ at the natural cutoff, is the 10¹²⁰. The question NTE must answer is what, in the geometry, prevents this leading extensive term from gravitating.

## 3. The unimodular projection: removing the extensive mode

The answer is that the NTE spectral triple does not admit the extensive term as a dynamical contribution. Chamseddine and Connes established that spectral-triple gravity carries a built-in **unimodular** constraint: among metric variations, those that preserve the total kinematical volume form a constrained class, and the leading cosmological term of the spectral action is annihilated on that class. Writing P_uni for the projection onto volume-preserving variations,

  P_uni[ f₄ Λ⁴ a₀ ] = 0.

The mechanism is exactly that of unimodular gravity. If the metric determinant is held fixed (the volume element is non-dynamical), then a term proportional to ∫√g — which is what f₄ Λ⁴ a₀ is — contributes no variation and therefore no source: it cannot appear in the field equations. Equivalently, one obtains the **trace-free Einstein equations**, in which only the trace-free part of the stress tensor sources curvature. A spatially constant vacuum energy density is pure trace; its trace-free part is zero; it does not gravitate. The cosmological constant, in this formulation, is demoted from a term in the action to at most an integration constant of the equations of motion — it is removed as a gravitating energy density, not cancelled against another large term.

NTE adopts this structure, because its substrate *is* a spectral triple of the Chamseddine–Connes type: the Hopf-S³ × S¹ base with an octonionic finite part. The unimodular projection is an adopted formulation, credited below — and not, as earlier drafts stated, a property inherited automatically from the cited spectral-triple literature. Unimodularity is not generic to spectral-triple gravity: the cited Chamseddine–Connes action carries the catastrophic cosmological term, and the only Chamseddine–Connes source of unimodularity is the volume quantisation of Chamseddine–Connes–Mukhanov (2014), which requires the Clifford algebras M₂(ℍ) ⊕ M₄(ℂ). Whether NTE's non-associative 𝕆 ⊕ 𝕆 triple admits that relation is an open mathematical question this corpus has not posed. **CCM 2014 is recorded as a candidate grounding, not shown for NTE's triple.** The **old** problem is thereby addressed at the adopted-register level: under the unimodular / trace-free equations, the extensive mode that would have produced the catastrophe does not gravitate.

It is worth being precise about what this does and does not buy. The projection removes the *leading*, volume-scaling term — the one responsible for the 10¹²⁰. It does not by itself fix the value of whatever finite residual survives at subleading order; that is the new problem, taken up in §6. The achievement of §3 is the prohibition, which is complete and structural.

## 4. The boundary-only reading

The unimodular projection has a transparent counterpart in NTE's ontology, and the two illuminate each other. NTE is a boundary-only (surface) framework: the physical degrees of freedom are carried on the expanding closed S³ wavefront, and the interior four-volume is not an independent arena (Part 1, Foundations; Part 2, structure). The boundary *is* the physics.

In that setting, a vacuum energy that scales with four-volume is simply the wrong object. It assigns extensive energy to a bulk the framework does not treat as fundamental, integrating an energy density over a volume of degrees of freedom that are not there. The naive estimate's 10¹²⁰ is, on this reading, the quantitative signature of that mismatch: it is the size of the error one makes by computing a volume-scaling vacuum energy for a system whose degrees of freedom are surface ones. Correctly accounting only for boundary degrees of freedom, the extensive contribution has nothing to multiply.

The ontology motivates the formal restriction, which is narrower. The unimodular constraint is the formal statement that the volume mode is non-dynamical; the boundary-only ontology is the physical reason a *constant* extensive volume mode has nothing to multiply. The trace-free equations remove only the **constant, extensive** mode; a **time-varying** vacuum energy still gravitates through its variation, which is what permits an accelerated epoch. The ontological statement, read without that qualification, would forbid any extensive vacuum energy from gravitating — including an inflationary plateau — and the corpus's origin sector requires exactly such an epoch (Part 3, cosmological origin sector). **The two readings are therefore related but not identical, and the formal one governs.** A constant vacuum density does not gravitate in NTE under the adopted unimodular / trace-free equations.

## 5. Independence from the subleading spectral data

Because the suppression acts on the leading a₀ (volume) term, it is insensitive to the subleading coefficients. This matters for the framework's honesty about a₄. On the canonical NTE substrate M = S³ × S¹, the fourth Seeley–DeWitt coefficient **vanishes**:

  a₄(D²)|_M = 0,

because the Dirac trace-anomaly integrand on this geometry, −18 C² + 11 E₄ (the fixed integer combination of the Weyl-squared and Euler densities), is pointwise zero: the round S³ × flat S¹ product is simultaneously Weyl-flat and Euler-zero (this is the F₁/heat-kernel result established elsewhere in the corpus and in the prior literature). One might ask whether the Λ suppression depends on this. It does not. The unimodular projection of §3 operates entirely at the a₀ level; a₄ enters only the curvature-squared sector and never the leading cosmological term. The structural resolution of the old problem would stand for any value of the subleading coefficients, and stands in particular here, where a₄ happens to vanish. The vanishing of a₄ is a genuine fact about the substrate, but the Λ mechanism is logically upstream of it.

This separation is deliberate, and it forecloses a tempting overreach: one must not let the specific values of subleading coefficients smuggle a derived *magnitude* for Λ in through the back door. The framework's claim is confined to the leading-order prohibition, which is where the structure actually licenses a claim.

## 6. Scope: what is derived, and what is not

The honest boundary of the result is sharp.

**Adopted and credited (mechanism); structural consequence within NTE.** The old problem is resolved — **adopted and credited**: unimodular / trace-free gravity (Buchmüller–Dragon 1988; Henneaux–Teitelboim 1989, both in the references below). The structural *consequence* within NTE is derived; the *mechanism* is adopted. A boundary-only geometry under that adopted unimodular constraint forbids the **constant** extensive vacuum term from gravitating; empty space is structurally quiet at that order, independent of subleading spectral data and of any fine cancellation. This is a definite, non-trivial commitment — it places NTE within the unimodular family of resolutions and ties the adopted mechanism to the framework's surface ontology. **Conditional on the unimodular initial-data class.** The literature holds that unimodular gravity resolves the old problem only where the initial-data formulation yields a global constraint on the space-time four-volume (Jiroušek, arXiv:2301.01662, 2023); otherwise Λ is specified as data and the fine-tuning returns. A closed S³ with a no-boundary origin (Companion 9 §3; Part 1 §2.1.2) makes a global four-volume a natural quantity, which is a **candidate** reason NTE meets the condition — **not a demonstration**.

**Not derived (the magnitude).** NTE does not derive the specific observed value of Λ. The suppression of §§3–4 establishes that the surviving residual is *intrinsically* small — set by the geometry forbidding large terms rather than by tuning — but "intrinsically small" is not "this particular number." Bridging that gap would require deriving the residual's magnitude from the geometry alone, without observational input, and the framework does not at present do so. No quantity in this paper is adjusted to match the observed Λ, and the observed value is not used to fix any structural element of the mechanism. The new problem is left open, explicitly.

Keeping this line sharp is the point. The structural prohibition is what the geometry licenses, and it is claimed; the magnitude is what the geometry does not yet license, and it is not.

## 7. Status and falsifiability

The structural claim is testable in the way a structural claim can be. It commits NTE to a vacuum that does not gravitate through the extensive mode — a specific stance, not a tautology. It would be in tension with any demonstration that the NTE spectral triple fails to carry the unimodular projection, or that a boundary-only ontology nonetheless requires a gravitating extensive vacuum term. Within general relativity proper, the same commitment is the well-defined content of unimodular / trace-free gravity, whose phenomenology is studied independently.

What this paper does not offer — and does not pretend to offer — is a falsifiable numerical prediction for Λ. Such a prediction would require the geometry-only derivation of the residual magnitude described in §6, which remains open. Should that derivation be found, the new problem would come into scope and the value would become a forward test. Until then, the contribution is the structural one, stated at its true strength and no further: the universe's vacuum is quiet at rest because its geometry forbids the loud term — one boundary, a unimodular constraint, no fine cancellation, and no claim on the number.

---

## References

1. A. H. Chamseddine and A. Connes, "The Spectral Action Principle," Commun. Math. Phys. **186**, 731 (1997); "Why the Standard Model," J. Geom. Phys. **58**, 38 (2008) [arXiv:0706.3688]; "Noncommutative Geometry as a Framework for Unification of all Fundamental Interactions including Gravity," Fortsch. Phys. **58**, 553 (2010) [arXiv:0812.0165].
2. D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279 (2003) — Seeley–DeWitt coefficients a₀, a₂, a₄.
3. W. Buchmüller and N. Dragon, "Einstein gravity from restricted coordinate invariance," Phys. Lett. B **207**, 292 (1988); M. Henneaux and C. Teitelboim, "The cosmological constant and general covariance," Phys. Lett. B **222**, 195 (1989) — unimodular / trace-free gravity and the vacuum's non-gravitation (**adopted and credited** as C11's mechanism).
4. A. H. Chamseddine, A. Connes and V. Mukhanov, "Geometry and the quantum: basics," JHEP **12**, 098 (2014) [arXiv:1409.2471] — volume quantisation / higher-degree Heisenberg relation as the Chamseddine–Connes route to unimodularity; **candidate grounding for NTE, not shown** (requires M₂(ℍ) ⊕ M₄(ℂ); NTE's finite algebra is 𝕆 ⊕ 𝕆). Mimetic dark matter arises automatically with that construction — spine hazard if ever adopted.
5. V. Jiroušek, "Unimodular approaches to the cosmological constant problem," arXiv:2301.01662 (2023) — old-problem resolution conditional on a global four-volume constraint in the initial-data class.
6. NTE corpus, Part 1 (Foundations) §II (boundary-only surface ontology); Part 2 (structure) and Part 3 (accounting) — the cosmological-constant treatment this companion expands.
7. The heat-kernel spectral action on S³ × S¹ × (𝕆 ⊕ 𝕆) and the trace-anomaly result — a₄ = 0 on the canonical substrate via −18 C² + 11 E₄ = 0.
