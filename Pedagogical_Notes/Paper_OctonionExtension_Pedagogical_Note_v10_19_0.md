---
title: "How Time Forces a Gauge Group"
subtitle: "A tier-3 explanatory note on the octonionic origin of the Standard Model gauge group and the associativity transition"
author: "G. White"
date: "2026-06 (v10.19.0)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## The result in one paragraph

The Standard Model's gauge group SU(3) × SU(2) × U(1) is usually taken as an empirical input. Within NTE it is **adopted from the established division-algebra programme** (Günaydin–Gürsey; Furey; Todorov–Dubois-Violette), with the non-associativity↔time reading also prior art (Gogberashvili; Köplinger). Before time exists, there is no mechanism to enforce that operations compose associatively — and by Hurwitz (1898) there is exactly one non-associative normed division algebra, the octonions 𝕆, with automorphism group G₂. When time emerges, causal ordering forces associativity; the algebra reduces 𝕆 → ℍ, and a selected imaginary direction (read as the electroweak vacuum at gauge birth) has G₂-stabiliser SU(3). The quaternionic subalgebra carries SU(2); CPN parity assigns SU(2)_R to the mirror sector; the selected direction gives U(1)_Y. Beyond the gauge group, three generations come from J₃(𝕆), and the Majorana condition (required independently by the dark-matter mechanism) gives exactly 90 Weyl species — a framework-specific cross-consistency. Technical development: Companion 16; Part 2 §§8.5–8.6.

## Why this matters in one paragraph

The Standard Model has roughly twenty free parameters and one large structural choice: the gauge group. NTE's claim is **conditional uniqueness given its premises**, not novelty of the group theory: Hurwitz + G₂ stabiliser + CPN parity select SU(3)_C × SU(2)_L × U(1)_Y once the pre-temporal algebra is octonionic. Whether those premises are correct is tested by the framework's other predictions; what this note explains is how the adoption fits together.

---

## The four normed division algebras

There are exactly four normed division algebras over the real numbers. This is a classical theorem of Adolf Hurwitz from 1898:

| Algebra | Dimension | Properties |
|---|---|---|
| ℝ (reals) | 1 | ordered, commutative, associative |
| ℂ (complex) | 2 | non-ordered, commutative, associative |
| ℍ (quaternions) | 4 | non-ordered, non-commutative, associative |
| 𝕆 (octonions) | 8 | non-ordered, non-commutative, **non-associative** |

Hurwitz proved that the four listed are *all* such algebras over the reals. There are no other choices.

The sequence has a clean structure called the *Cayley-Dickson construction*: each algebra is built from the previous one by a specific doubling procedure, losing one algebraic property at each step. ℝ becomes ℂ by losing ordering; ℂ becomes ℍ by losing commutativity; ℍ becomes 𝕆 by losing associativity. The next step (𝕆 → "sedenions") would lose the division-algebra property altogether — Hurwitz's theorem says you have to stop at the octonions.

The four algebras correspond to the four parallelisable spheres: S⁰ (real), S¹ (complex), S³ (quaternionic), S⁷ (octonionic). This is the Adams theorem.

## Why time forces associativity

In post-temporal physics, sequential operations compose associatively — enforced by the time-ordering operator, which assigns a definite sequence to any product of operations by their time coordinates.

What if there is no time coordinate? Then there's no time-ordering operator. There's no mechanism to enforce that (A·B)·C = A·(B·C). In a setting without time, the algebra of operations is *generically non-associative*.

The framework's pre-temporal epoch is precisely this kind of setting. Before the gauge-birth transition where causal ordering is established, there is no temporal direction, and no enforcement of associativity. By Hurwitz's theorem, the only normed division algebra that is non-associative is the octonions. The pre-temporal algebra must be 𝕆.

When the gauge-birth transition happens, associativity is suddenly enforced. The algebra must reduce to a smaller, associative subalgebra. The only candidates within 𝕆 are the four-dimensional quaternionic subalgebras ℍ.

This is the *associativity transition*: 𝕆 → ℍ at the moment time emerges.

## How the gauge group emerges

The symmetry group of the octonions — the automorphisms preserving the algebraic structure — is the exceptional Lie group G₂, of dimension 14. At the transition, the symmetry group must reduce to something smaller, compatible with the quaternionic subalgebra that survives.

When the Higgs vacuum acquires a value, it selects a specific direction in the imaginary octonions Im(𝕆), a 7-dimensional space. The Higgs vacuum picks one direction e₁ ∈ Im(𝕆), and the stabiliser of that direction within G₂ is exactly SU(3). This is a clean mathematical fact: G₂ acts transitively on the 6-sphere of unit imaginary octonions, and the stabiliser at any point has dimension 14 − 6 = 8, which is the dimension of SU(3). The stabiliser group *is* SU(3), acting on a complex 3-dimensional space (the colour triplet) plus its conjugate (the antitriplet).

This is SU(3)_C — the colour gauge group of the strong interaction.

Meanwhile, the framework's spatial geometry is the 3-sphere S³, which is the same as the unit quaternions, which is the same as the Lie group SU(2). With the further structural commitment that the framework's bilateral cosmology selects left-handed gauge structure for the observable sector, SU(2) becomes SU(2)_L — the weak isospin gauge group.

And the selected direction e₁ defines a one-dimensional complex line in the algebra — a U(1) symmetry. This is U(1)_Y, the hypercharge gauge group.

Combining: SU(3)_C × SU(2)_L × U(1)_Y. This is the Standard Model gauge group. It emerges from 𝕆 plus the gauge-birth transition plus the Higgs vacuum direction.

## The Cayley-Dickson sequence as cosmic epochs

| Epoch | Active algebra | What gets added |
|---|---|---|
| Pre-temporal | 𝕆 (non-associative) | (initial state — no temporal ordering yet) |
| Gauge birth | ℍ (associative) | associativity, via causal ordering |
| Electroweak symmetry breaking | ℂ (commutative) | commutativity, via U(1)_EM = phase symmetry |
| Classical limit | ℝ (ordered) | ordering, via decoherence to definite outcomes |

Each transition corresponds to a known physical event. The four epochs reverse the Cayley-Dickson sequence. The universe runs *up* the algebraic tower from 𝕆 to ℝ as time, gauge structure, and classical determinism are progressively added.

## Three generations from J₃(𝕆)

The exceptional Jordan algebra J₃(𝕆) — 3×3 Hermitian matrices over the octonions with the Jordan product — is 27-dimensional. The "3" in J₃ corresponds to the three rows/columns of these Hermitian matrices, providing three independent copies of the single-generation structure. (Note: this three-generation count is structurally distinct from the dim(adj SU(2)) = 3 in the bare-coupling derivation. The Jordan-algebra "three" is a generation count; the gauge-content "three" is the dimension of the SU(2) adjoint representation. They are independent structural facts.)

Three generations × 16 Weyl states per generation = 48 states (in the Dirac case). The framework's commitment to Majorana neutrinos removes 3 right-handed neutrinos, giving 45 independent Weyl species per cosmological sector. Doubled across the bilateral mirror cosmology, the total is exactly 90 — which is the framework's species count.

There's a non-trivial cross-consistency here: the Majorana condition was committed to for the dark-matter mechanism, not chosen to fit the 90-species count. The two structural commitments agree at exactly 90. The agreement is what makes the structural reading worth taking seriously.

## What is adopted, what is NTE-specific, and what is open

*Adopted prior art (conditional uniqueness given NTE premises):* the gauge group SU(3)_C × SU(2)_L × U(1)_Y and the three-generation / species structure from the octonionic / J₃(𝕆) programme (credited; Companion 16; Part 3 ledger).

*NTE's claimed increments:* reading the symmetry-breaking direction as the electroweak vacuum at gauge birth; the Cayley–Dickson ↔ cosmic-epoch correspondence (structural, not dynamical); CPN parity assignment of SU(2)_R to the mirror sector; the Majorana → 90 cross-consistency with the dark-sector mechanism.

*Open / not claimed:* Yukawa values and the mass hierarchy; three-generation hypercharge completion; technical naturalness (programme only).

## What would break it

If experiments discover a fourth generation of Standard Model fermions, the J₃(𝕆) construction's three-generation prediction fails. If experiments discover that neutrinos are Dirac rather than Majorana, the framework's Majorana commitment fails, the dark-matter mechanism breaks, *and* the 90-species count is wrong. If the explicit hypercharge verification across three generations fails, the species count is correct but the assignments are arbitrary, weakening the structural case.

## Provenance

This is a tier-3 explanatory note. Technical companion: **Companion 16** (`Companion_16_Octonion_Gauge_Species_v10_19_0.md`), which supersedes Desktop `Paper_OctonionExtension_v10_9.md`. The companion note *The Shape Where the Anomaly Vanishes* covers the F₁ trace-anomaly uniqueness of the framework's spatial geometry on the same setting; the companion note *A Coupling Forced by Geometry* derives the bare Hopf-bundle coupling κ₀ = 3/√(4π) that enters the framework's downstream predictions. The full pedagogical note set is organised around the joint statement that the framework's predictions cohere from one structural substrate — Companion 12 develops the heat-kernel evidence for that coherence.

---

*Corpus version: NTE v10.19.0 draft (aligned 2026-08-03).*

— G. White, 2026-08 (tier-3 explanatory note; prior-art honesty pass).
