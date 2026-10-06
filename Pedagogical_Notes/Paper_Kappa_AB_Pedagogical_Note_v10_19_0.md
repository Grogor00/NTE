---
title: "From 0.846 to 5.50"
subtitle: "A tier-3 explanatory note on the dark-matter coupling ratio κ = 5.50 from Hopf monopole projection + CPN-symmetric resummation"
author: "G. White"
date: "2026-06 (v10.19.0)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## The result in one paragraph

The dark-matter-to-baryon ratio — how much dark matter there is in the universe compared to ordinary baryonic matter — is measured by cosmologists at 5.38 ± 0.15 from the cosmic microwave background. The companion paper derives this number, 5.50, from geometry. The derivation has two stages. The first stage produces a *bare* coupling between two sectors of a structural model — three SU(2)-adjoint gauge-field components on a Hopf-bundle 3-sphere, where the 3 counts the dimension of the adjoint representation of SU(2) — and that bare coupling comes out to 3/√(4π) ≈ 0.846, the math-physics identity covered in a companion note. The second stage takes that bare 0.846 and *resums* it through a self-consistent feedback loop between two mirror-symmetric sides of the framework's geometry. The geometric series 0.846 + 0.846² + 0.846³ + … converges (because 0.846 is less than 1) to 0.846/(1 − 0.846) ≈ 5.50. The amplification factor 1/(1 − 0.846) ≈ 6.49 is what turns the bare coupling into the cosmic ratio. The framework identifies the resummed value with the dark-matter-to-baryon ratio. The agreement with Planck's measurement is 0.8σ (5.50 vs 5.38 ± 0.15).

## Why this matters in one paragraph

Dark matter is one of the largest unsolved problems in modern physics. Cosmological observations require something that gravitates without emitting light, in roughly five times the abundance of ordinary matter. The standard approach is to postulate a new particle (WIMP, axion, sterile neutrino, etc.) and ask why it would be five times more abundant than baryons — typically requiring a fine-tuned production mechanism in the early universe. The present framework takes a different route: dark matter is identified structurally as the gravitational echo of matter on the other side of a bilateral mirror-symmetric geometry, and the ratio 5.50 emerges from a geometric closure rather than a thermal-history calculation. The 0.8σ agreement with Planck is empirically striking; whether the structural identification is correct is a separate question that the broader framework's other predictions are meant to test collectively. The standalone math-physics content of the present paper is the derivation chain — bare coupling plus closure — giving 5.50; the dark-matter identification is the framework's downstream physical reading of that number.

---

## The two stages of the derivation

The derivation has a sharp internal structure. There are two distinct steps, and they correspond to two different kinds of mathematical work.

The first step is the *bare coupling*. This is a clean math-physics identity on the unit Hopf bundle, derived in detail in the companion note *A Coupling Forced by Geometry*. It says: when the three SU(2)-adjoint gauge-field components on a unit 3-sphere project to the 2-sphere base of the Hopf fibration via integration over the fibre, the bare dimensionless coupling between them and a monopole gauge sector comes out to exactly 3/√(4π). The 3 is the dimension of the adjoint representation of SU(2) — the gauge sector lives in this representation, not in the framework's Killing-spinor space, which is 2-dimensional fundamental per Bär 1993 — and the 1/√(4π) is the L²-normalisation of the simplest spherical harmonic on the unit 2-sphere. The number 3/√(4π) ≈ 0.846 is structurally fixed — one primary Hopf derivation plus Sonner–Tong independent anchor (heat-kernel route reaches same value, not independent third confirmation). We take that result as input here.

The second step is the *resummation* — the new content of the present paper. Given the bare coupling κ₀ = 0.846, what observable cosmic ratio does the framework predict?

## The mirror-symmetric closure

The framework's cosmology has a specific structural commitment: the universe is one closed manifold with two orientations, related by a CPN symmetry that conjugates the two sides. We occupy one orientation; the other is real, with its own matter content, evolving under the same physics in its own forward direction of time. The two orientations share a thin spatial boundary; they cannot communicate by signal, but they couple gravitationally through the boundary.

When you write down the cosmological field equations on this bilateral geometry, something distinctive happens. The gravitational source on our side (call it our orientation's stress-energy tensor T⁺) couples not only to our orientation's metric but also, through the boundary, to the stress-energy on the other side (T⁻). And the same is true on the other side. The cross-coupling has a specific strength: the bare coupling κ₀.

But here's the key: what we measure as the gravitational signal in our orientation is the *effective* stress-energy tensor T̃⁺, which includes both our own ordinary matter T_b⁺ and the gravitational contribution from the other side. The other side's effective stress-energy T̃⁻ similarly includes both its own ordinary matter and the gravitational contribution from us. Each side's effective tensor is coupled to the other side's effective tensor.

When the mirror symmetry (CPN) imposes that the two orientations contain equivalent ordinary matter (T_b⁺ = T_b⁻ = T_b) and have equivalent effective tensors (T̃⁺ = T̃⁻ = T̃), the equations simplify dramatically:

T̃ = T_b + κ₀ T̃

This is a self-consistency equation: T̃ appears on both sides, because the gravitational coupling between the orientations is mutual. The solution is

T̃ = T_b / (1 − κ₀)

The total observed gravitational signal is the original ordinary-matter signal, amplified by the factor 1/(1 − κ₀).

## The geometric series

The factor 1/(1 − κ₀) has a clean interpretation as a sum. If you expand it as a geometric series:

1/(1 − κ₀) = 1 + κ₀ + κ₀² + κ₀³ + …

each term represents a successive round of gravitational coupling between the two orientations. The first term (1) is the direct contribution from ordinary matter on our side. The second term (κ₀) is the coupling-strength contribution from ordinary matter on the other side. The third term (κ₀²) is the coupling-strength contribution from the *back-reaction* on our side of the other side's contribution. And so on, ad infinitum.

Each term is smaller than the previous one by a factor of κ₀ ≈ 0.846. The series converges because κ₀ < 1. The total is 1/(1 − 0.846) ≈ 6.49.

If the matter on each side is equal (CPN symmetry), and the total observed gravitational signal is amplified by 6.49 relative to ordinary matter alone, then the apparent dark sector — the gravitational excess we attribute to dark matter — is the difference between the observed signal and the ordinary-matter contribution:

ρ_DM / ρ_b = κ₀ / (1 − κ₀)

For κ₀ = 3/√(4π) ≈ 0.846:

κ = 0.846 / (1 − 0.846) = 0.846 / 0.154 ≈ 5.506

This is the dark-matter-to-baryon ratio the framework predicts.

## The number

The match with Planck's cosmological measurement:

| Quantity | Framework | Observation | Ratio |
|---|---|---|---|
| Bare coupling κ₀ | 0.846 | — | — |
| Resummed ratio κ | 5.506 | 5.38 ± 0.15 (Planck 2018) | 1.03× |

The 1.03× ratio sits at about 0.84σ from the measured value — within current cosmological precision. The deviation is small enough that whether the framework's prediction is exactly right depends on improvements to the cosmological measurement (CMB-S4 is expected to halve the uncertainty in the 2030s) rather than on the framework's specific arithmetic.

There's a structural commitment the prediction is making that's worth naming explicitly. The alternative — if the cross-orientation coupling were *linear* rather than self-consistent (no back-reaction loop) — would give κ = κ₀ ≈ 0.846, off the observed value by a factor of about 6.4, or roughly 30σ from Planck's measurement. The self-consistency loop is not optional; it's the structural commitment that the framework's cosmological field equations make.

Honest scope: this is a *framework-dependent identification* (Tier B in the framework's internal register), not a direct laboratory measurement of κ. The number 5.50 comes out of the geometry of the resummation; identifying that number with the cosmic dark-matter-to-baryon ratio requires accepting that dark matter is the gravitational echo of the other orientation. Other identifications are possible. The framework's case rests on the combination: a structurally derived number 5.50, a 0.8σ agreement with a precision cosmological observable, and the structural identification scheme that connects them. The match is striking; the identification scheme has to be tested by the framework's other predictions to be convincing.

## Why κ₀ has to be less than 1

The geometric series 1 + κ₀ + κ₀² + κ₀³ + … converges only if κ₀ < 1. Otherwise the resummation diverges and the effective stress-energy tensor blows up — physically impossible.

The bound κ₀ < 1 is therefore a *structural requirement* of the framework: the bare coupling between the bridge channels cannot exceed unity, or the cosmological closure breaks. Given that κ₀ = 3/√(4π) ≈ 0.846 in the framework's setup, this constraint is satisfied but with room to spare.

There's a structural reason for the specific factor 3 in 3/√(4π): it counts the number of independent bridge channels, equal to dim(adj SU(2)) = 3. If the gauge sector that mediates between orientations turned out to be larger than SU(2) — for instance, an SU(3) bridge sector with eight adjoint components — the bare coupling would exceed 1 and the closure would diverge. The framework's commitment to an SU(2)-adjoint bridge (three gauge-field components, *not* three generations of fermions — those are structurally distinct commitments) is therefore tied to the convergence of the cosmological closure. A larger bridge gauge group would break the structure before any quantitative prediction is tested.

## What would break it

If precision cosmology improves to push the observed κ outside the band κ = 5.50 ± a few × σ, the framework's number is wrong. If the gauge sector mediating between orientations is structurally larger than SU(2), the bare coupling κ₀ would exceed 1 and the closure would diverge. If direct dark-matter detection succeeds (a positive WIMP signal, an axion, or another candidate particle), the structural identification of dark matter with the gravitational echo of the other orientation fails. If the κ₀ derivation itself is wrong, the prediction breaks at the input level.

## Appendix: the cross-source coefficient survives the variation

The closure in the body assumes one thing about the field equations: that the two orientations' Einstein equations cross-source each other at strength *exactly* κ₀ = 3/√(4π) — the same number the bare Hopf projection produced — with no extra factor introduced when those equations are obtained by varying an action. Because the whole result (5.50 rather than 0.846, a factor of about 6.5) rides on that coefficient, this appendix shows it explicitly.

**The action.** The framework's bilateral gravity is a single action spanning both orientations,

S = (1/16πG) ∫ √(−g⁺) R⁺  +  (1/16πG) ∫ √(−g⁻) R⁻  +  S_m[g⁺,ψ⁺]  +  S_m[g⁻,ψ⁻]  +  S_bridge[g⁺,g⁻,ν] :

two Einstein–Hilbert terms, ordinary matter on each side, and one shared bridge term — the Z₂-even unresolved neutrino ν, delocalised over the Hopf fibre, the only field carrying stress-energy on both metrics at once.

**The variation.** Varying with respect to the + metric, δS/δg⁺_μν = 0, gives the + orientation's Einstein equation with two sources,

G⁺_μν = 8πG ( T_b⁺ + T_bridge⁺ )_μν ,   with   T_bridge⁺_μν = −(2/√(−g⁺)) · δS_bridge/δg⁺^μν ,

and symmetrically on the − side. T_b⁺ is ordinary matter; the entire question is the magnitude of T_bridge⁺ — the stress-energy the − side deposits on our metric through the shared neutrino.

**Where the coefficient comes from.** The bridge field couples to each metric through its angular profile on the internal S² base of the Hopf fibration. Having failed the projection S³ → S², the neutrino is smeared *isotropically* across that base, so its normalised angular profile is the constant s-wave Y₀₀ = 1/√(4π). The stress-energy it transmits from the − side onto the + metric is that side's source projected onto this shared s-wave channel — the monopole projection — which for any normalised isotropic density returns its Y₀₀ weight, 1/√(4π), per channel. The bridge runs in the three su(2)-adjoint components (dim adj SU(2) = 3), so the transmitted coefficient is 3 × 1/√(4π) = 3/√(4π) = κ₀. It is the *same* overlap that fixed the bare coupling, reappearing here as the strength linking the two Einstein equations rather than as a coupling inside one of them.

**Why the variation does not renormalise it.** Three facts keep the coefficient from acquiring a spurious factor when the metric is varied:

1. *The overlap sits on a fixed base.* The dynamical fields are the two 4-dimensional orientation metrics; the overlap that sets κ₀ is an integral over the *internal* unit S² of the Hopf base, whose measure is not among the varied quantities. Varying g⁺ cannot rescale a number fixed on the internal base.

2. *The Jacobian cancels.* The √(−g⁺) produced by the variation multiplies both the geometric side (via G⁺_μν) and the matter side (in the definition of T_bridge⁺ above); it divides out in forming G⁺_μν = 8πG T⁺_μν, so it cannot re-weight the cross term relative to the ordinary-matter term. The universal factor of 2 in the stress-tensor definition is likewise common to T_b⁺ and T_bridge⁺ and drops from their ratio — and it is that ratio, not either term alone, that the closure uses.

3. *Idempotency holds it order by order.* The s-wave projector P = |Y₀₀⟩⟨Y₀₀| satisfies P² = P with ∫ Y₀₀² dΩ = 1, so a second cross-insertion carries exactly κ₀², and the n-th carries κ₀ⁿ. No overlap factor accumulates down the series — the reason the geometric sum closes to a clean 1/(1 − κ₀) rather than 1/(1 − G κ₀) with G ≠ 1. (This "G = 1" property has been checked independently in the monopole sector.)

With the coefficient pinned at κ₀ on every insertion, the CPN-symmetric closure T̃ = T_b + κ₀ T̃ is exactly the relation solved in the body, and its fixed point is κ = κ₀/(1 − κ₀).

**Scope.** This is established in the averaged, s-wave (monopole) sector — the sector in which κ = 5.50 is compared against Planck. The full non-averaged bridge (retaining the higher-ℓ structure of Θ) and the complete ghost-free nonlinear bimetric completion (Hassan–Rosen-class) remain open refinements of the two-orientation gravity, exactly as Part 2 §IX records; nothing here claims them. The claim is the narrower one the headline number needs: in the sector where 5.50 is quoted, the cross-source coefficient is κ₀ by construction of the action, not by choice.

## Provenance

This is a tier-3 explanatory note. It is a companion to the standalone technical paper *The Dark Matter Coupling Ratio κ = 5.50 from Hopf Monopole Projection + CPN-Symmetric Resummation* (Paper DM Ratio Identification CrossSector FixedPoint TwoOrientation Cosmology Clean Standalone v0.1). The companion note *A Coupling Forced by Geometry* covers the bare coupling κ₀ = 3/√(4π) as a standalone math-physics result. The companion note *The Shape Where the Anomaly Vanishes* establishes the substrate manifold.

---

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

— G. White, 2026-06 (tier-3 explanatory note, v10.19.0 rebuild).
