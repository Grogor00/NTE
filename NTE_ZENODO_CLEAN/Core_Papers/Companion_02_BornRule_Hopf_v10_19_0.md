---
title: "The Born rule is the Hopf fibration"
author: "Gregory Lyndon White"
date: "2026-06 (v10.19.0)"
---

*Part of NTE Corpus v10.19.0 (deposited 2026-06). Companion 2.*

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

---

## Abstract

The Born rule — the postulate that measurement probabilities are given by P = |⟨φ|ψ⟩|² — has been an axiom without derivation since 1926. This paper shows that, given the complex Hilbert-space structure of quantum states and the unobservability of global U(1) phase, the Born rule including its specific quadratic exponent is the geometrically natural probability map on the state space — a reformulation rather than a derivation from less. The normalised state space of a spin-½ system is the 3-sphere S³. The unobservability of global phase is the U(1) fibre symmetry of S³. The quotient of S³ by this symmetry is the Hopf fibration S³ → S², the unique non-trivial U(1) bundle over the 2-sphere. The Hopf projection is inherently quadratic: the only smooth function from S³ to [0,1] that is simultaneously U(1)-invariant, SU(2)-equivariant, and correctly normalised — with normalisation, additivity across basis partitions, continuity, and consistency under SU(2)-rotated bases jointly forcing linearity in |z|² — is |z|². The Born exponent of 2 is therefore the topological signature of the Hopf map under the assumed inputs, not a free parameter; the inputs themselves — bilinearity in amplitude and the complex Hilbert space — are this paper's premises rather than its outputs (§7.2). The derivation extends to arbitrary spin via generalised Hopf fibrations and to continuous variables via the infinite-dimensional limit. The result is consistent with Gleason's theorem, reaching the same conclusion from geometric rather than measure-theoretic premises — both proceeding from premises rather than from less.

---

## 1. The question

Quantum mechanics rests on a few postulates, most with clear motivation: the state space is a Hilbert space (superposition), time evolution is unitary (conservation), observables are Hermitian (real outcomes). The Born rule stands apart. It states that if a system is in state |ψ⟩ and is measured in the orthonormal basis {|φ_k⟩}, the probability of outcome k is P_k = |⟨φ_k|ψ⟩|². The rule works — confirmed in every quantum experiment — but has never been derived from anything more fundamental; it is bolted on as a separate axiom.

The question is not whether the probability should depend on the overlap ⟨φ|ψ⟩ — some dependence is natural. The question is **why the square**: why |⟨φ|ψ⟩|² and not |⟨φ|ψ⟩|, |⟨φ|ψ⟩|⁴, or some other function? The exponent of 2 is the entire content that demands explanation. This paper gives the geometric explanation, given quantum mechanics's standard inputs, using no physics beyond the standard formalism and no mathematics beyond what is already in it. Why those inputs are the right ones — why quantum mechanics is built on complex amplitudes rather than real or quaternionic ones — is a question the paper sharpens rather than closes (§7.2).

## 2. Three facts

The derivation rests on three established, uncontroversial facts, present in every textbook.

**Fact 1: the state space of a spin-½ system is S³.** A general state |ψ⟩ = z₁|↑⟩ + z₂|↓⟩ with |z₁|² + |z₂|² = 1 is a unit vector in ℂ²; the constraint defines the unit 3-sphere S³ ⊂ ℂ² ≅ ℝ⁴. Every normalised spin-½ state is a point on S³, and conversely. This is a definition, not an analogy.

**Fact 2: global phase is unobservable.** The states |ψ⟩ and e^{iξ}|ψ⟩ are physically identical for any ξ, since all predictions depend on inner products and |⟨φ|e^{iξ}ψ⟩| = |⟨φ|ψ⟩|. Geometrically, the physical state space is not S³ but the quotient of S³ by the U(1) action (z₁, z₂) → (e^{iξ}z₁, e^{iξ}z₂).

**Fact 3: the Hopf fibration.** The quotient S³/U(1) is the 2-sphere S², and the projection π: S³ → S², π(z₁, z₂) = [z₁ : z₂] ∈ ℂP¹ ≅ S², is the Hopf fibration — the unique non-trivial principal U(1) bundle over S² (Hopf, 1931). It is the map from the full state space (S³) to the physical state space (S²), obtained by quotienting out the unobservable global phase. In standard quantum mechanics the physical state space S² is the Bloch sphere: every physicist who has drawn a Bloch sphere has used the Hopf fibration, named or not.

## 3. The derivation

### 3.1 Setup

A spin-½ state is a point (z₁, z₂) on S³. A measurement in the |↑⟩/|↓⟩ basis asks for the probability of "↑": a function P: S³ → [0,1] satisfying three requirements imposed by the three facts.

### 3.2 Requirements

**Requirement 1 (Fact 2): U(1) invariance.** P(e^{iξ}z₁, e^{iξ}z₂) = P(z₁, z₂) for all ξ; otherwise physically identical states would get different probabilities.

**Requirement 2: SU(2) equivariance.** Rotating both state and measurement axis by the same SU(2) element leaves probabilities unchanged: P(U|ψ⟩, U|↑⟩) = P(|ψ⟩, |↑⟩) — rotational invariance of the physics.

**Requirement 3: normalisation.** P(↑) + P(↓) = 1: for two outcomes, their probabilities exhaust the total.

### 3.3 The unique solution

Only one function satisfies all three: P(↑) = |z₁|².

**Step 1 — U(1) invariance restricts the form.** A smooth function on S³ invariant under the global phase action can depend only on U(1)-invariant combinations of (z₁, z₂): |z₁|², |z₂|² (= 1 − |z₁|² on S³), z₁z̄₂, and z̄₁z₂. So P(↑) = F(|z₁|², z₁z̄₂, z̄₁z₂); the cross-terms are still permitted by Requirement 1 alone.

**Step 2 — normalisation fixes complementary structure.** Once Step 3 eliminates the cross-terms, the residual f(|z₁|²) must satisfy f(r) + f(1 − r) = 1 for all r ∈ [0,1]. This complementarity is satisfied by f(r) = r but also by others (e.g. sin²(πr/2)); the residue from Step 3 singles out the linear solution.

**Step 3 — SU(2) equivariance selects f(r) = r, via two layers of gauge symmetry.** *Layer 1* (already used): the global U(1) action restricts F to the four invariants above. *Layer 2*: the stabiliser U(1) of the measurement axis within SU(2). The |↑⟩ axis is fixed by rotations about itself, generated by U_θ = diag(e^{iθ}, e^{−iθ}), acting as (z₁, z₂) → (e^{iθ}z₁, e^{−iθ}z₂). Under this, |z₁|² and |z₂|² are unchanged but the cross-terms transform as z₁z̄₂ → e^{2iθ}(z₁z̄₂), z̄₁z₂ → e^{−2iθ}(z̄₁z₂). Equivariance under the stabiliser of its own measurement axis therefore eliminates the cross-terms, leaving P(↑) = f(|z₁|²). The two layers are physically distinct — Layer 1 is the global phase symmetry making |ψ⟩ and e^{iξ}|ψ⟩ identical; Layer 2 is the rotational symmetry of measurement-axis selection within SU(2) — and both are required.

*Selecting f(r) = r.* Combine the residual f(|z₁|²) with complementarity (f(r) + f(1−r) = 1), additivity over basis partitions (probability of an outcome in any subset of basis vectors decomposes additively), continuity, and consistency across SU(2)-rotated bases (f the same function in every basis). These force f linear, f(r) = r. Any nonlinear f compatible with complementarity (e.g. sin²(πr/2)) fails additivity over higher-dimensional partitions, or fails consistency when SU(2) rotates the basis. Therefore **P(↑) = |z₁|² = |⟨↑|ψ⟩|²** — the Born rule.

### 3.4 Why the exponent is 2

The exponent arises at a precise step. The probability is a function of the overlap ⟨↑|ψ⟩ = z₁, a complex number; the probability is a real non-negative number, so we need a map ℂ → ℝ≥0. U(1) invariance makes it a function of |z₁|. But the probability is linear in |z₁|², not in |z₁|, and the distinction matters: P = |z₁| is not smooth at z₁ = 0 and fails normalisation (|z₁| + |z₂| ≠ 1 on S³ in general), whereas P = |z₁|² is smooth and satisfies |z₁|² + |z₂|² = 1 exactly. The exponent is 2 because the S³ constraint is *quadratic*, and the probability must respect it to satisfy normalisation. A linear constraint would define a simplex, not a sphere, with different probability rules. The state space of quantum mechanics is a sphere in *complex* space, and complex spheres have quadratic defining equations. The Born exponent of 2 is the exponent of the defining equation of the state space — selected by that geometry given the complex Hilbert space and U(1) phase invariance taken as inputs here (§7.2).

## 4. Extension to higher spin

A spin-j state is a unit vector in ℂ^{2j+1}, |ψ⟩ = Σ_m c_m |j, m⟩ with Σ|c_m|² = 1; the state space is S^{4j+1} ⊂ ℂ^{2j+1}, the global phase action is the same scalar U(1), and the quotient is S^{4j+1}/U(1) = ℂP^{2j} (the generalised Hopf fibration). The probability P(m) = |c_m|² follows by the same two-layer argument: Layer 1 restricts to U(1)-invariants of {c_m, c̄_m}; Layer 2 (the stabiliser U(1) of |m⟩ within SU(2j+1)) eliminates cross-terms c_m c̄_{m'} (m ≠ m'), which transform non-trivially under the diagonal action fixing |m⟩'s phase; normalisation, additivity, and continuity then force linearity. The U(1) fibre structure is identical in all dimensions because global phase acts by scalar multiplication in every representation. The angular dependence for a specific geometry is P(m | j, θ) = |d^j_{m'm}(θ)|², inheriting the quadratic exponent from the Hopf projection.

## 5. Extension to continuous variables

For a particle in L²(ℝ³), a separable Hilbert space with countable basis {|n⟩}, |ψ⟩ = Σ_n c_n |n⟩ with Σ|c_n|² = 1, the coefficients lie on S^∞ ⊂ ℓ²(ℂ); global phase acts as (c_n) → (e^{iξ}c_n), the quotient is S^∞/U(1) = ℂP^∞, and P_n = |c_n|² follows by the same argument extended to infinite dimensions (scalar phase multiplication commutes with everything). In the position representation ψ(x) = ⟨x|ψ⟩, the probability density P(x) = |ψ(x)|² is the continuous limit: at each x the amplitude is complex, and the U(1)-invariant map to a density is |ψ(x)|². The momentum representation is the unitary Fourier transform, preserving the inner product, the S^∞ constraint, and the U(1) fibre, so P(p) = |ψ̃(p)|² follows identically.

## 6. Consistency with existing results

**Gleason's theorem (1957)** proves that in dimension ≥ 3 the unique non-contextual probability measure on projections is the Born rule, assuming the Hilbert-space structure and non-contextuality. The present derivation assumes less in one respect: only the geometric structure of the state space (S³), the unobservability of global phase (U(1)), and rotational covariance (SU(2)). Non-contextuality emerges as a *consequence* of the Hopf projection rather than being assumed: P(↑) = |z₁|² depends only on the overlap with |↑⟩, not on the choice of orthogonal complement. Gleason supplies the measure-theoretic proof that no alternative exists; this paper supplies the geometric reason this measure is the natural one.

**Other derivation programmes.** Deutsch–Wallace derive the rule from rational betting in an Everettian framework (assuming many-worlds and a rationality axiom); Zurek from environment-assisted invariance (assuming decoherence and an environment); Carroll–Sebens from self-locating uncertainty in branching worlds (assuming Everettian branching). The present derivation uses only the geometry of S³, the unobservability of global phase, and SU(2) symmetry — inputs already in the standard formalism and accepted across interpretations. This makes it narrower in interpretation-specific dependencies, but it does not make it more fundamental in the axiom-from-less sense: the complex Hilbert space and the bilinearity in amplitude those inputs encode remain premises rather than outputs (§7.2).

## 7. What the derivation does and does not accomplish

### 7.1 What it does

It demonstrates that the Born rule, including its quadratic exponent, is the geometrically natural probability map on the standard state space, given three premises already part of the formalism — no new physics, no interpretation-specific assumptions, no additional axioms. The exponent of 2 is identified as a topological property of the Hopf fibration. It explains *why* the exponent is 2 rather than another number, given the inputs: because the state space is a complex sphere (quadratic defining equation), not a simplex or a real sphere — and that quadratic constraint is itself the bilinearity-in-complex-amplitude commitment encoded in the inputs. The framework therefore does not strictly reduce the axiom count of quantum mechanics; it reformulates the Born-rule axiom as a geometric consequence of axioms the formalism already carries (complex Hilbert space, unitarity, Hermitian observables, global U(1) phase invariance). The geometric reading makes visible *why* the structure is forced once those axioms are accepted; it does not derive the rule from less.

### 7.2 What it does not

It does not, by itself, explain why the state space is a complex Hilbert space rather than a real or quaternionic one; it takes the ℂ² structure of spin-½ states as given. The wider framework addresses this through the Cayley–Dickson sequence 𝕆 → ℍ → ℂ → ℝ as a sequence of cosmic phases: the pre-temporal boundary algebra is the unique non-associative normed division algebra 𝕆 (Hurwitz), whose automorphism group G₂ breaks under the gauge-birth selection mechanism to deliver SU(3)_C × SU(2)_L × U(1)_Y, with the complex structure inherited from the descent through ℂ; S³ ≅ SU(2) appears as the quaternionic submanifold of S⁷ ≅ unit 𝕆, providing both the SU(2)_L gauge factor and the spin-½ state-space topology used here. The state space being S³ is therefore not an arbitrary postulate within the broader framework, though the "why complex amplitudes" question is sharpened rather than fully closed by this picture.

It does not explain the measurement problem — why outcomes are definite rather than superposed; it produces the correct probabilities but does not address the transition from "all outcomes possible" to "one outcome actual." It does not derive quantum mechanics itself; it derives one axiom (the Born rule) from the others.

Companion 6 supplies the physical mechanism by which the U(1) fibre structure assumed here arises: gauge symmetry switches on at temporal locking, and global phase becomes unobservable as a *consequence* of gauge symmetry rather than as a free postulate (the two-layer argument of §3.3 is mirrored there). The framework's scope-honest position is that the geometric reading demonstrates the Born rule's *geometric naturalness* given complex Hilbert space and global U(1) phase invariance, rather than deriving the rule from less. This is a real and useful result — it makes visible why the structure is forced once the inputs are accepted — but the question "why exponent 2?" is sharpened rather than closed: it is pushed back to "why complex Hilbert space?" and "why bilinearity in amplitude?" The framework offers a partial physical-mechanism answer to the complex-rather-than-quaternionic question via the Cayley–Dickson descent at gauge birth, and Companion 6 supplies the activation story for the U(1) fibre; the bilinearity-in-amplitude question remains an open research target.

## 8. Conclusion

The Born rule has been an unexplained postulate for nearly a century. Once the geometric inputs the formalism already carries are made explicit — the complex Hilbert space, the S³ structure of normalised states, the unobservability of global phase — the rule's specific quadratic form follows from those inputs. Quantum states are points on S³; global phase is unobservable; the quotient S³/U(1) is the Hopf fibration; the Hopf projection is quadratic; therefore the probability is the squared modulus of the amplitude. The derivation uses nothing beyond standard quantum mechanics and the topology of the 3-sphere, and the exponent of 2 is a feature of the map from complex coordinates to real probabilities, forced by the geometry of the state space we have used since 1926.

The deeper question it opens is *why the state space is S³* — why quantum mechanics is built on complex numbers rather than reals or quaternions. This paper does not answer that, but it sharpens it: if the Born rule is geometry, the foundational question is not "why are probabilities quadratic?" but "why is the geometry complex?" A framework in which the S³ structure arises from the topology of a higher-dimensional manifold — as the boundary geometry of a 4D spacetime with the pre-temporal algebra 𝕆 descending through Cayley–Dickson to ℂ — provides one such answer, developed in the corpus and in Companion 6.

---

*Correspondence: the geometric interpretation of the Born rule presented here arises naturally within a broader framework treating S³ as the boundary topology of spacetime, from which temporal emergence, entanglement, and the discrete energy spectrum follow as geometric consequences. See Companion 1 (entanglement as single-object geometry) and Companion 6 (the Born rule's activation at gauge birth).*
