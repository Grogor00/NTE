---
title: "A Coupling Forced by Geometry"
subtitle: "A tier-3 explanatory note on the bare dimensionless coupling 3/√(4π) from monopole projection on the unit Hopf bundle"
author: "G. White"
date: "2026-06 (v10.19.0)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## The result in one paragraph

When you ask "how strongly do two specific physical sectors couple to each other, just from the shape of the space they live on, before any correction?" — there is sometimes a clean geometric answer with no adjustable parameter. The companion paper derives one such answer: on the unit 3-sphere with its natural Hopf-fibration structure, the bare coupling between three SU(2) gauge-field components on the 2-sphere Hopf base (each sourcing an s-wave monopole projection of a Killing spinor on the unit 3-sphere) and a monopole-projected gauge sector comes out to exactly 3/√(4π), or about 0.846. The number doesn't have to be fitted to anything. The 3 counts dim(adj SU(2)) — three independent gauge-field components (a = 1, 2, 3), not three separate Killing-spinor polarisations: for each fixed chirality sign, the Killing-spinor solution space on S³ is only 2-dimensional (the fundamental of SU(2); Bär 1993), and the "three channels" is the action of those three gauge components on one Killing-spinor amplitude. The 1/√(4π) is the value of the simplest constant function on a unit 2-sphere when properly normalised. Their product is the structural coupling, and the construction is so direct that an independent anchor from a separate physics context — a Yang–Mills instanton calculation (Sonner–Tong 2009) — confirms the structural reading that the factor 3 counts the dim(adj SU(2)) gauge-component count, with a related spectral-action heat-kernel computation reproducing the same number through analytic machinery as an internal consistency check.

## Why this matters in one paragraph

Dimensionless coupling constants in physics are mostly inputs — measured numbers that you have to put into your theory rather than derive from it. The fine-structure constant α_em ≈ 1/137 is the most famous; the strong-interaction coupling at a particular energy scale is another. When a theoretical framework can produce a specific dimensionless coupling from pure structural arithmetic — with no fitted parameter — it deserves special attention, because it puts one of physics's traditionally free inputs onto a structural footing. The 3/√(4π) identity is one such. It's a single clean number that emerges from the geometry of the unit Hopf bundle, with an independent anchor from a separate physics context (Sonner–Tong 2009 in Yang–Mills instanton physics) confirming the gauge-content structural reading, and a state-independent normalisation (stable against perturbative correction by the Gaunt-coefficient triviality of the s-wave channel, as developed below). Beyond this standalone math-physics result, the same coupling enters the framework's broader dark-matter ratio prediction κ = κ₀ / (1 − κ₀) ≈ 5.50, but that downstream identification is *not* part of this paper — the present result is purely the bare structural value.

---

## What's a coupling, in geometric terms

When physicists talk about a coupling between two physical sectors, they usually mean: how strongly does an interaction between them respond to a given strength of one of the underlying fields? The electromagnetic coupling tells us how strongly photons respond to charged particles. The weak coupling tells us how strongly the W and Z bosons mediate weak interactions. These are dimensionless numbers (when you set them up properly in fundamental units), and at the level of a Lagrangian or an action functional, they appear as coefficients in front of specific products of fields.

For most physical sectors, the bare coupling — the value before any corrections from interactions with other fields — has to be measured. There's no "first-principles" reason for the electromagnetic coupling to be 1/137 rather than 1/200 or 1/100; the value just is what it is, and the theory tells you how that bare value evolves with energy scale once you include corrections.

But there are special situations where a coupling is *structurally determined* by the geometry of the space the physics lives on. The simplest examples involve sectors that interact through the topology or curvature of a fixed background, in such a way that the coupling has no "knobs" — the geometry gives it a unique value, with no room for it to be anything else.

The present result is one such situation: the bare coupling between three SU(2) gauge-field components on the 2-sphere Hopf base (each tied to a Killing-spinor projection on the unit 3-sphere) and a monopole-projected gauge sector. The geometry forces the number; there is no fitted parameter.

## The geometry

A 3-sphere (S³) is the surface of a 4-dimensional ball. With a particular natural metric — the *round metric of unit radius* — it has constant positive curvature in every direction. There's a famous fact about the unit 3-sphere: it's also the underlying space of the Lie group SU(2). Every point on the 3-sphere corresponds to one element of SU(2), and vice versa.

The 3-sphere has a beautiful fibration structure called the *Hopf fibration*, discovered by Heinz Hopf in 1931. It says: the 3-sphere can be sliced into a family of circles, one circle for every point of a 2-sphere. Stack all those circles together (with the right twisting), and you get the 3-sphere back. In symbols: S³ → S², with the fibre over each point of S² being a circle S¹.

This fibration carries a natural magnetic structure: there's a canonical U(1) connection whose curvature corresponds to one quantum of *magnetic flux* through the 2-sphere base. From a physics perspective, the Hopf bundle is the geometric setting for the Dirac monopole — the simplest example of a magnetic monopole.

Two more ingredients before we can state the result:

*Killing spinors.* On the round unit 3-sphere, there are certain "parallel" spinor fields called *Killing spinors* — solutions of a specific differential equation that says the covariant derivative of the spinor is proportional to the gamma-matrix product. These are the natural fermion solutions on the curved background. For each fixed chirality sign, the Killing-spinor solution space is **2-dimensional** — the **fundamental (spin-1/2)** representation of SU(2) (Bär 1993). That 2-dimensional space is **acted on** by the three left-invariant Killing vector fields that generate su(2) ≅ Lie(SU(2)); those three vectors transform under the **adjoint** representation of SU(2). The number 3 that enters the bare coupling is *dim(adj SU(2))* — three SU(2) gauge-field components (or, geometrically, three adjoint Killing **vectors**), not three independent Killing **spinors**.

*Spherical harmonics on the 2-sphere.* Any function on a sphere can be decomposed into a sum of spherical harmonics Y_{ℓm}, which are analogues on the sphere of the sines and cosines on a circle. The simplest harmonic — the one with ℓ = 0 — is just a constant function. The properly normalised version (the one whose square integrates to 1 over the sphere) is Y_{00} = 1/√(4π). This is the *monopole harmonic* — the s-wave channel in the language of monopole physics, the most symmetric possible function on the 2-sphere.

## The cancellation, and where the number comes from

The geometric setup combines these ingredients. A constant Killing spinor on the unit 3-sphere has a specific behaviour when you integrate it around the Hopf fibre (the circle) above any point on the 2-sphere. The Hopf fibre is geometrically the same at every point, so the integration produces a constant function on the 2-sphere base. Normalising that constant function to have unit L²-norm — which is the convention for any quantum field theory matrix element — fixes it to exactly Y_{00} = 1/√(4π).

So one gauge component's Killing-spinor projection, when carried through the Hopf structure to the 2-sphere base, becomes the monopole harmonic Y_{00}. Three SU(2) gauge-field components (a = 1, 2, 3) — each with the same s-wave amplitude from that projection — contribute independently. Summing over the three components gives the total bare coupling

κ₀ = 3 × Y_{00} = 3/√(4π) = 3/(2√π) ≈ 0.846

The factor 3 is dim(adj SU(2)) = the gauge-component count (convention-independent; Sonner–Tong 2009). The factor 1/√(4π) is the L²-normalisation of the constant function on the unit 2-sphere. The product is the bare structural coupling, with no adjustable parameter anywhere along the way.

## The primary derivation and an independent anchor

What makes this identity convincing is the primary derivation's robustness plus an independent anchor confirming its structural content.

The primary derivation is the Hopf-projection construction described above: take the three SU(2) gauge-field components on the 2-sphere base, each sourcing an s-wave amplitude from Killing-spinor projection on the 3-sphere; sum them. The answer is 3/√(4π). This is the source of the identity.

The independent anchor comes from a completely different physics context — instanton calculations in SU(2) Yang–Mills theory. Jeremy Sonner and David Tong, in a 2009 paper on Berry phase in supersymmetric quantum mechanics, identify the factor 3 = dim(adj SU(2)) in the coupling structure of Yang–Mills connections to Killing-spinor matter. The Sonner–Tong setup has nothing to do with the Hopf bundle directly; it's a separate calculation in a related but distinct corner of mathematical physics. The match does not constitute a separate derivation of κ₀ — both readings ultimately count the same gauge content. What the agreement supports is the structural identification that the factor of three is the gauge-content count from dim(adj SU(2)) = 3, not a phenomenological factor that happens to land at three.

A related computation in the Connes–Chamseddine spectral-action programme produces κ₀ = 3/√(4π) at the second-order heat-kernel coefficient (a₂) on a Hopf-product spectral triple. This is the same content as the Hopf-projection derivation through different mathematical machinery (analytic rather than geometric); it serves as an internal consistency check across the spectral-action and Hopf-projection routes rather than as a separate independent anchor for the structural number.

## State-independent normalisation

A worry, when you compute a number this cleanly, is that perturbative corrections might shift it. The s-wave coupling 3/√(4π) is the *bare* structural value; could higher-mode corrections from other Dirac modes on the 2-sphere change it?

The answer is no, by a clean selection-rule argument. The matrix element of the constant function Y_{00} between any normalised state ψ on the 2-sphere reduces to:

⟨ψ|Y_{00}|ψ⟩ = (1/√(4π)) × ∫|ψ|² dΩ = 1/√(4π) = Y_{00}

— independently of the mode content of ψ. The integral on the right is just the L²-norm of ψ, which is 1 by normalisation. So the s-wave matrix element is the s-wave amplitude itself, with no perturbative correction from higher modes.

This is the *Gaunt-coefficient triviality* of the s-wave channel. The Gaunt integral (the integral of three spherical harmonics) vanishes unless the angular momenta of the three add up appropriately; when one of them is Y_{00}, the integral becomes diagonal in the other two and proportional to the s-wave amplitude. Higher Dirac modes on the 2-sphere can occupy higher angular momentum channels, but they don't couple back to the s-wave through Y_{00}.

The consequence: 3/√(4π) is a **state-independent normalisation** at the s-wave level — a mathematical identity that no physical parameter can modify. Any observed deviation from this value, in a context where the construction applies, must come from non-perturbative physics (self-consistency closures, non-s-wave channels, different multiplet counts) — not from perturbative corrections within the s-wave sector.

## What would break it

This is a finite math-physics identity, falsifiable by direct calculation.

If anyone reproduces the same Hopf-bundle construction and gets a different number, the present derivation contains an error. The arithmetic is reproducible in a few lines of spin-geometry and spherical-harmonic algebra.

If the SU(2)-adjoint gauge-component count is wrong — if the sector has a different multiplicity than three independent adjoint components — the factor 3 changes accordingly. The convention-independence of dim(adj SU(2)) = 3 is anchored by the Sonner–Tong identification, but a structural rethinking of the gauge-sector multiplicity could in principle replace the 3 with a different integer.

If a heat-kernel calculation on the same Hopf-product background yields a coefficient different from 3 at the leading SU(2)-adjoint order, the internal consistency between the Hopf-projection and spectral-action routes breaks, and at least one of the two routes would contain a formulation error that produces the discrepancy.

The result stands as a structural fact about the unit Hopf bundle. It does not depend on cosmological commitments or on any specific physical identification of the coupling with an observed quantity. The companion result κ = κ₀/(1 − κ₀) ≈ 5.50 — which the framework uses to predict the dark-matter ratio — is a separate downstream identification that takes 3/√(4π) as input. The present result is purely the bare value.

## Provenance

This is a tier-3 explanatory note. It is a companion to the standalone technical paper *A structural derivation of the bare dimensionless coupling 3/√(4π) from monopole projection on the unit Hopf bundle* (Paper Hopf Kappa₀ Clean Standalone v0.2). The companion note *The Shape Where the Anomaly Vanishes* establishes the manifold S³ × S¹ as the unique closed product 4-manifold where the relevant trace anomaly vanishes; the present coupling lives naturally on that same canonical background. The downstream note *From 0.846 to 5.50* develops the CPN-symmetric resummation κ₀ → κ = κ₀/(1 − κ₀) ≈ 5.50.

---

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

— G. White, 2026-06 (tier-3 explanatory note, v10.19.0 rebuild).
