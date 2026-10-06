---
title: "The Symmetry That Locks the Mix"
subtitle: "A tier-3 explanatory note on maximal atmospheric neutrino mixing from an antilinear μ-τ reflection on the Majorana sector"
author: "G. White"
date: "2026-06 (cleaned tier-3 representation; v10.19.0 corpus)"
---

*Independent Researcher, Auckland, New Zealand · gregwhite00@gmail.com*

## The result in one paragraph

Neutrinos oscillate between three flavours — electron-neutrino, muon-neutrino, tau-neutrino — as they travel. The rate of oscillation depends on three "mixing angles" that describe how much each flavour overlaps with each mass eigenstate, plus one CP-violating phase δ. One of the mixing angles, called θ₂₃ or the *atmospheric mixing angle* (because it was first pinned down by neutrinos produced when cosmic rays hit the atmosphere), is observed close to 45° — meaning the muon-neutrino and tau-neutrino flavours are essentially a balanced mixture of two underlying mass states. The framework derives this exact 45° value from a single structural assumption: that the Majorana neutrino sector carries an *antilinear μ-τ reflection* symmetry. This symmetry — a combined swap of muon and tau labels with a complex-conjugation operation on the quantum amplitudes — forces two predictions at once: θ₂₃ = π/4 (maximal atmospheric mixing) and |δ| = π/2 (maximal CP violation). The reactor angle θ₁₃ is compatible with the symmetry at any non-zero value — the symmetry does not force it to zero. Both forced predictions become sharply falsifiable at DUNE and Hyper-Kamiokande in the late 2020s.

## Why this matters in one paragraph

The Standard Model with three neutrino flavours has three mixing angles and one CP phase that, in the absence of any further principle, you have to measure rather than predict. The solar angle θ₁₂ is about 33°; the reactor angle θ₁₃ is about 8.6°; the atmospheric angle θ₂₃ is near 45°. The CP phase δ is currently constrained to a broad band around 3π/2, with substantial uncertainty. Symmetry-based explanations across the past 25 years have proposed reasons why θ₂₃ should be exactly 45°. The framework here goes further: it places both θ₂₃ = 45° and |δ| = π/2 on the structural side of the ledger, from the same antilinear discrete symmetry. Two predictions from one structural commitment, testable jointly at DUNE and Hyper-K. The distinctive feature of the framework's realisation is the location of the symmetry (on the chirality-superposition pattern of the Majorana sector, not on the flavour-sector mass matrix as in earlier symmetry-based proposals) and the fact that θ₁₃ ≠ 0 is compatible with the symmetry rather than being generated as a perturbation from a symmetry-breaking source.

---

## What a mixing angle is

Start with what the neutrino oscillation data tells us. There are three neutrinos labelled by *flavour* (the kind of charged lepton they're paired with in weak interactions): ν_e, ν_μ, ν_τ. There are also three neutrinos labelled by *mass* (the eigenstates of the mass operator): ν₁, ν₂, ν₃, with three distinct mass values.

These two labellings are not the same. A muon-neutrino produced in a weak interaction is *not* a mass eigenstate; it's a quantum mechanical superposition of the three mass eigenstates with specific coefficients. As the neutrino travels, the three mass components evolve at slightly different rates (because they have different masses), and the superposition rotates. By the time the neutrino reaches a detector, the overlap with each flavour has changed — sometimes it shows up as ν_μ, sometimes as ν_τ, sometimes as ν_e. The neutrino has *oscillated*.

The coefficients in the superposition are organised into a 3×3 unitary matrix called the *PMNS matrix*, after Pontecorvo, Maki, Nakagawa, and Sakata, who first proposed neutrino oscillations in various combinations through the 1950s–60s. The PMNS matrix is parametrised by three angles (θ₁₂, θ₁₃, θ₂₃) and a phase (δ, sometimes written δ_CP) that captures CP-violating effects. The three angles govern how strongly the three flavours mix with each other; the phase governs the difference in oscillation behaviour between neutrinos and antineutrinos.

The atmospheric mixing angle θ₂₃ governs the (μ, τ) ↔ (2, 3) sub-mixing — how much the muon and tau flavours overlap with the second and third mass eigenstates. The observed value is approximately 49.7°, with current uncertainty allowing for the range 44°–50°. The "maximal" value 45° sits inside that range.

What does 45° mean physically? It means the muon-flavour and tau-flavour are equal superpositions of the second and third mass eigenstates — half-and-half. The mixture is as balanced as it can possibly be. A small deviation from 45° (a few degrees) would mean one flavour leans slightly toward one mass eigenstate; *no* deviation (exactly 45°) means perfect balance.

## Why 45° is structurally special

If θ₂₃ were 30° or 60°, no one would ask "why that value?" — they would just be measured numbers. But 45° is the symmetry point. It's the value forced by an exchange-plus-reflection symmetry between the muon and tau labels of the PMNS matrix.

To see the shape of the argument at its simplest, consider a linear exchange symmetry first. Imagine two visible states X and Y that are mixed from two underlying objects A and B by a 2×2 unitary rotation. The rotation has one parameter, an angle θ. If there is a linear exchange symmetry that says "swap A and B, and X and Y respond the same way," then the rotation must be invariant under that swap. The only rotation that satisfies this is the 45° rotation — every other angle privileges one object over the other and breaks the symmetry.

That's the *linear* version of the argument. The framework's realisation goes further. Instead of a plain linear exchange, the framework's structural symmetry is an *antilinear* μ-τ reflection: a combined operation that (i) swaps the muon and tau labels *and* (ii) takes the complex conjugate of the quantum-mechanical amplitudes involved. The complex conjugation matters because quantum amplitudes are complex numbers, and reflecting their imaginary parts adds an additional constraint on the phases.

An antilinear symmetry constrains more than a linear exchange does. A linear exchange μ ↔ τ constrains the *magnitudes* of the μ-row and τ-row entries in the PMNS matrix to be equal. An antilinear reflection R constrains both the magnitudes *and* the phases: for each mass eigenstate i, R requires U*_{μi} = U_{τi}. That extra phase constraint is what forces the CP phase to a specific magnitude in addition to forcing the mixing angle to 45°.

Both predictions come out from the same structural commitment. That's what makes the antilinear framing more powerful than the plain linear one.

## The chirality-superposed Majorana sector

The framework's antilinear reflection acts on the *chirality-superposition pattern* of the Majorana sector. To unpack that phrase:

*Majorana fermions* are particles that are their own antiparticles. Neutrinos may or may not be Majorana — that's an open experimental question, tested by searches for *neutrinoless double-beta decay*. The framework treats neutrinos as Majorana, and the present derivation uses one structural property of Majorana fermions: their left- and right-handed chirality components are not independent particle species, but coupled polarisations of the same fundamental field.

The standard treatment of Standard Model weak interactions privileges one direction in the SU(2)_L gauge symmetry — the direction aligned with the Higgs vacuum value. By convention, that direction is called σ₃, where σ₁, σ₂, σ₃ are the three Pauli matrices that generate SU(2). The σ₃ direction is the *Cartan direction*; the other two directions, σ₁ and σ₂, span the *Cartan-orthogonal subspace*.

The framework's assignment is that the three Majorana neutrino mass eigenstates have specific structural polarisations:

- *ν₃* is aligned with the Higgs VEV direction (the Cartan direction). Its chirality structure is cleanly separable — left and right chirality components can be distinguished.
- *ν₁* and *ν₂* lie in the Cartan-orthogonal subspace. Their chirality structure is *superposed* — left and right components are coupled together in a way that doesn't separate cleanly into independent particles.

The antilinear μ-τ reflection is a structural discrete symmetry acting on this chirality-superposition pattern. The reflection's action maps the μ-flavour labelling to the τ-flavour labelling with a compensating complex conjugation on the amplitudes involved. The chirality-superposed structure of ν₁ and ν₂ is what makes the antilinear character natural: complex conjugation is intrinsic to how left and right chirality components are related when they are superposed rather than independent.

Once the reflection acts on the chirality-superposition pattern at the mass-matrix level, it induces the antilinear μ ↔ τ constraint on the PMNS matrix at the flavour level. The magnitude constraint forces θ₂₃ = π/4. The phase constraint forces |δ| = π/2. The reactor angle θ₁₃ is compatible with the symmetry at any value — the reflection does not force it to zero, and the observed θ₁₃ ≈ 8.6° is a natural value under the symmetry rather than a perturbation from a symmetry-breaking source.

## The three predictions

The antilinear reflection produces three structural results for the neutrino mixing sector.

*θ₂₃ = π/4 = 45° (forced).* The magnitude constraint from the antilinear reflection: |U_{μi}|² = |U_{τi}|² for each mass eigenstate i. Combined with unitarity of the PMNS matrix, this forces the atmospheric angle to exactly 45°. The observed value, from the NuFIT 5.3 global oscillation fit, is θ₂₃ ≈ 49.7° in normal mass ordering, with the current 1σ band consistent with the range 44°–50°. The deviation from exactly 45° is a few degrees — within experimental uncertainty and within the size expected from the sub-leading Z₂-breaking effect that also drives θ₁₃ to its measured value.

*|δ| = π/2 (forced).* The phase constraint from the antilinear reflection: arg(U_{μi}) + arg(U_{τi}) = 0 (equivalently: U_{μi} × U_{τi} is real for each mass eigenstate i). With θ₂₃ = π/4 from the magnitude constraint, the phase constraint reduces to sin(δ) = ±1, forcing |δ| = π/2 — maximal CP violation. The observed value is currently constrained to a broad band around 3π/2 (with substantial uncertainty and mass-ordering-dependent tensions between different experimental analyses). Sub-leading corrections to δ from the same source that drives θ₁₃ are structurally correlated with the θ₁₃ magnitude.

*θ₁₃ ≠ 0 (natural).* The antilinear reflection does not constrain θ₁₃. Unlike the linear μ-τ exchange framing (Lam-2001 and related realisations), which forces θ₁₃ = 0 at leading order and requires a separate symmetry-breaking source to give the observed θ₁₃ ≈ 8.6°, the antilinear reflection is compatible with θ₁₃ ≠ 0 at any value. The observed reactor angle is a *natural* consequence of the symmetry-preserving sector, not a perturbation from a breaking source.

The three predictions carry different weights. The θ₂₃ prediction is falsifiable at DUNE and Hyper-K to about ±0.5° precision by the early 2030s. The |δ| prediction is falsifiable jointly with θ₂₃ at the same experiments — precision δ measurement will resolve whether |δ| = π/2 is confirmed or excluded. The θ₁₃ compatibility is not a precision test in the same sense; it's a structural feature that the observed non-zero value is *consistent* with the framework's symmetry rather than a challenge to it.

A note on the two forced predictions: their operator-level connection is not yet established. The framework's structural commitment is that both θ₂₃ = π/4 and |δ| = π/2 follow from the *same character* — the antilinear μ-τ reflection — but the operator-level derivation showing they emerge from the same underlying operator (rather than two related operators that both carry the antilinear character) is open work. "Same character" is where the framework currently sits; "same operator" is the further identification that the technical companion aims for.

## What distinguishes this from earlier proposals

Several earlier frameworks have proposed symmetry-based reasons why θ₂₃ should be 45°. The earliest — Lam's linear μ-τ exchange Z₂ from 2001 — places a linear swap symmetry on the flavour-sector charged-lepton mass matrix. Under linear exchange, θ₂₃ = 45° is forced but θ₁₃ = 0 at leading order, with a separate symmetry-breaking source needed to give the observed θ₁₃ ≈ 8.6°. The CP phase δ is unconstrained by the linear symmetry. Related proposals in the tri-bimaximal literature (Harrison-Perkins-Scott 2002; Farzan-Smirnov 2007) place the symmetry on different sub-matrices with variations on the same theme.

The present framework's antilinear realisation differs in three ways:

*Location.* The symmetry acts on the chirality-superposition pattern of the Majorana sector, not on the flavour-sector charged-lepton mass matrix. The distinction is between where the structural fact lives — deep in the chirality structure of the neutrino sector versus in the observable mass-matrix sector.

*Character.* The symmetry is antilinear (swap plus complex conjugation), not linear. The antilinear character produces the additional |δ| = π/2 prediction that the linear frameworks do not.

*Sub-leading pattern.* The linear frameworks predict θ₁₃ = 0 at leading order; the antilinear framing has θ₁₃ ≠ 0 as compatible with the symmetry. The observed reactor angle is a natural value, not a perturbation.

Distinguishing the two routes empirically requires joint precision measurement of θ₂₃ and δ at next-generation long-baseline neutrino experiments (DUNE, Hyper-Kamiokande). The linear framing predicts θ₂₃ = 45° with δ free; the antilinear framing predicts both θ₂₃ = 45° and |δ| = π/2. If precision δ measurements resolve away from |δ| = π/2, the antilinear framing is falsified while a linear framing may still survive.

## The sister prediction — a related lab-physics test

The antilinear μ-τ reflection has a sister implication for charged-lepton physics that the framework's broader corpus develops in full elsewhere. The structural commitment underlying the antilinear reflection at the neutrino mixing level (developed in the present note) shares character with the structural commitment underlying a predicted amplitude ratio for charged-lepton flavour violation (developed in the *Clean Gates* companion note).

Charged-lepton flavour violation (CLFV) is the phenomenon where a charged lepton decays into another charged lepton plus a photon — μ → eγ or τ → eγ. These processes are vanishingly small in the Standard Model but can be larger in extensions with right-handed Majorana neutrinos. The framework's structural prediction is for the *ratio* between two CLFV amplitudes squared:

|A(μ → eγ)|² / |A(τ → eγ)|² = tan²θ₂₃

For θ₂₃ = 45° this ratio is exactly 1.

The connection between the antilinear reflection on the neutrino sector (developed here) and the CLFV amplitude ratio (developed in Clean Gates) is at the *character* level: both emerge from structural commitments carrying antilinear character on the Majorana sector. The full operator-level derivation of the CLFV ratio, and its precise relationship to the antilinear reflection that forces θ₂₃ = π/4 and |δ| = π/2 here, is developed in the technical companion. What matters for the present note is that a second, structurally related lab-physics prediction travels with the framework's Majorana-sector commitments, and future CLFV detection would test that character through an independent channel.

Six qualifiers travel with the CLFV amplitude ratio prediction, and naming them honestly is what makes it a gate rather than an advertisement: it is *conditional* (fires only if CLFV is observed at all — the framework's absolute rate at its preferred right-handed neutrino mass scale is far below current experimental sensitivity), at the *amplitude level* rather than the branching ratio (mass-power dressings distort the ratio), carries a width of about ±2–3% from subleading corrections, has odds of about 9 to 1 versus anarchic seesaw, and its structural connection to the θ₂₃ = π/4 prediction sits at the character level rather than the operator level.

## What would break it

The antilinear μ-τ reflection is a strong structural claim that can be tested in multiple ways.

*θ₂₃ measurement.* If next-generation neutrino experiments (DUNE, Hyper-Kamiokande) measure θ₂₃ substantially outside the range consistent with 45° at the projected precision, the antilinear reflection is falsified. The projected precision of about ±0.5° by the early 2030s puts this test squarely in reach.

*δ measurement.* If precision δ measurement resolves outside the range consistent with |δ| = π/2, the antilinear character is falsified. The current experimental band is broad and consistent with |δ| = π/2, but tightening measurements will discriminate. If |δ| resolves substantially away from π/2, the framework's antilinear framing fails while a linear framing (with δ unconstrained) may still survive.

*θ₂₃ + δ joint pattern.* Because both are predicted by the same antilinear commitment, a joint pattern outside the framework's expectations is a doubled falsifier: both predictions can be tested at the same experiments, and both must hold together under the antilinear character.

*CLFV detection.* If charged-lepton flavour violation is detected at a future experiment (next-generation MEG-class search, Belle II τ-decay precision, an FCC-era CLFV program) and the measured |A(μ→eγ)|²/|A(τ→eγ)|² amplitude ratio differs significantly from tan²θ₂₃ at the framework's predicted θ₂₃ value, the structural character underlying both the neutrino-sector antilinear reflection and the CLFV ratio is broken through a second, structurally related channel. The framework's Majorana-sector antilinear commitment does not survive that miss.

*Majorana nature of neutrinos.* If neutrinoless double-beta decay searches continue to find nothing at the sensitivity reached by KamLAND-Zen, LEGEND, and nEXO over the next decade, the chirality-superposed-Majorana framing on which the derivation rests no longer applies. The framework's broader commitments would force a retreat to a different structural reading of neutrino mixing.

*Mass ordering.* If the neutrino mass ordering turns out to be inverted (third-generation lightest, not heaviest), the assignment of ν₃ to the Cartan direction fails, and the structural argument needs reconstruction.

The collective signal is what the framework is committed to: maximal atmospheric mixing *and* maximal CP violation as two structural facts (not coincidences), chirality-superposition as the location of the symmetry, and a related lab-physics test through the CLFV amplitude ratio.

## Positioning

This note sits within a family of programmes that take the Standard Model to arise from division-algebra and noncommutative-geometric structure, with time and spacetime emergent rather than fundamental. The relevant neighbours include the spectral action / noncommutative-geometry programme (Chamseddine–Connes 1996, 1997, 2008, 2010), the division-algebra Standard Model line (Günaydin–Gürsey 1973; Furey 2014, 2018; Dubois-Violette 2016; Todorov–Dubois-Violette 2018), the relational and emergent-time programmes (Page–Wootters 1983; Rovelli 1991; Connes–Rovelli 1994; Wheeler–DeWitt; Barbour; experimental test Moreva et al. 2013), and the non-associativity-as-time line (Gogberashvili 2004; Köplinger–Dzhunushaliev–Gogberashvili). The closest architectural relative is T. P. Singh's octonionic / pre-quantum pre-spacetime theory (2019–2025), which assembles emergent time + octonionic-NCG + exceptional-Jordan Standard Model + Connes time + Majorana neutrinos + left–right symmetry into one framework.

The neutrino-mixing-sector antilinear μ-τ reflection framing sits within a mature literature on μ-τ symmetries. The linear μ-τ exchange approach traces to Lam (2001) with related work by Harrison-Perkins-Scott (2002; tri-bimaximal), Xing (2002), Kitabayashi-Yasuè (2004), and reviews by King (2015). The antilinear variant — sometimes called "μ-τ reflection" or "GL-symmetry" — was proposed by Harrison-Perkins-Scott (2002) and developed by Grimus-Lavoura (2003, 2004), Farzan-Smirnov (2007), Grimus-Lavoura-Ludl (2008), and Xing-Zhao (2015). The present note's structural contribution is placing the antilinear reflection on the chirality-superposition pattern of the Majorana sector as a corollary of the framework's broader commitments (rather than as a discrete assumption applied to the mass matrix by hand), and identifying it as the shared structural character underlying both the mixing-angle prediction and the sister CLFV amplitude ratio developed in the framework's Clean Gates companion.

The framework — Non-Temporal Emergence — is a distinct implementation within the broader emergent-spacetime class, not a new class. Its own choices differentiate it within the family: an e-fold count coordinate N as fundamental and proper time as emergent via t = iΔN (a specific Wick-rotation proposal for what time emerges from, distinct from modular or Connes time), the S³ × S¹ Hopf substrate as the load-bearing geometric commitment, the bilateral CPN-conjugate two-orientation cosmology, and specific identifications including κ₀ = 3/√(4π) from the Hopf-bundle bare coupling, the dark-matter / baryon ratio as a cross-sector fixed point, the two-branch neutrino mass ratio, and the CLFV amplitude ratio at the seesaw level. NTE assumes quantum mechanics rather than deriving it, carries no trace dynamics, no Grassmann-matrix aikyons, no spontaneous-localisation collapse, no E₈×E₈, and no sedenions; its distinctiveness sits in the specific assembly and its specific predictions, not in the existence of the assembly.

The framework does not fit numbers. Every quantity is either **structural** (fixed by geometry / algebra) or **honestly scoped** as conditional, a cross-check, or open. Results are tiered explicitly — derived, re-derived (credited), imported (credited), or open. The three predictions of the present note — θ₂₃ = π/4 forced, |δ| = π/2 forced, θ₁₃ ≠ 0 natural — sit on the structural side; the connection to the CLFV amplitude ratio sits at the character level with the operator-level unification open.

**The antilinear μ-τ reflection is established prior work with a substantial literature. The framework's structural contribution here is the specific assembly of that antilinear reflection on the chirality-superposition pattern of the Majorana sector — as a corollary of broader framework commitments rather than a discrete assumption imported by hand — and the identification of the shared structural character with the sister CLFV amplitude ratio developed elsewhere.**

## Provenance

This is a tier-3 explanatory note for the curious reader. It is not a standalone novelty claim and is not the source of any framework prediction in itself. The mathematical content — the antilinear μ-τ reflection framework for neutrino mixing, the derivation that R forces θ₂₃ = π/4 and |δ| = π/2, and the compatibility of θ₁₃ ≠ 0 with R — sits in the prior literature, with Harrison-Perkins-Scott (2002), Grimus-Lavoura (2003, 2004), Farzan-Smirnov (2007), and Xing-Zhao (2015) carrying the original technical developments.

The framework's structural placement of the antilinear reflection on the chirality-superposition pattern of the Majorana sector — as a consequence of its broader commitments to the S³ × S¹ substrate, the bilateral CPN-conjugate cosmology, and the chirality-superposed Majorana assignment — is developed in the framework's master corpus. Part 2 (Structure) of the master corpus carries the gauge sector, the neutrino results, and the σ-mode assignment on which the antilinear reflection sits; Part 3 (Accounting) carries the parameter ledger with honest-scope tiers and the falsifiability register. The framework's Companion 10 develops the Majorana mass scales M_R and M₁ that anchor the seesaw architecture; Companion 12 ("the chord") sets out the joint pattern of structural results the framework's S³ × S¹ substrate carries. The Clean Gates companion note develops the sister CLFV amplitude ratio prediction — the framework's first conditional lab-physics discriminator — that shares the antilinear character with the mixing-sector predictions here.

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

— G. White, 2026-06 (cleaned tier-3 representation).
