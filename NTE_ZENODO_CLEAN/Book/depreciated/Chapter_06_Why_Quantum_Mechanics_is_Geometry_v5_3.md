# The Shape of Time

# Chapter 6 — Why Quantum Mechanics is Geometry

*Non-Temporal Emergence (NTE): the Null-Time Extension to the Standard Model*

G. White

---


## *The Shape of Probability*

> *A sphere of states, projected through phase, becomes a sphere of probabilities. The squaring is not a recipe — it is the geometry.*

---

The previous five chapters have built a picture. The universe is a closed three-dimensional surface — a three-sphere — expanding, with a geometric scalar field setting the rate at which time accumulates. That picture has done a great deal of work: the photon's null-time, the structure of entanglement, the flatness of the observed universe, the emergence of time itself, and the relationship between the boundary expansion field and the Standard Model Higgs.

The reader who has been following along may have noticed something. Quantum mechanics has a three-sphere at its heart too. It has been sitting in the formalism for nearly a century — the state space of the simplest quantum system, the spin-1/2 particle. Physics students learn the formalism without being told that this is what they are looking at. The framework's reading is that this is not a coincidence. The same kind of geometric object is doing the same kind of work in both places.

This chapter is about why.

There is a postulate at the heart of quantum mechanics that has never been derived. It's the rule that tells you how to extract probabilities from a wavefunction, and it has been confirmed in every experiment performed since 1926, to extraordinary precision, in every corner of physics where quantum mechanics applies. It's called the Born rule.

Max Born wrote it down in 1926, almost in passing, in a footnote added in proof to a paper on quantum scattering. The wavefunction ψ, he proposed, is not itself a probability — it's something more abstract, a complex-valued amplitude. To extract the probability of a measurement outcome, you take the absolute square: P = |⟨φ|ψ⟩|². The probability is the magnitude squared of the inner product between the system's state and the measurement basis.

Born received the Nobel Prize in 1954 specifically for this rule. It's one of the most experimentally validated statements in physics. And for nearly a century, it has been bolted onto the formalism as a separate axiom — a brute fact about how quantum measurements work, not derivable from anything more fundamental.

This chapter is about why it doesn't have to be that way. The Born rule is not an unmotivated postulate. Given the geometric structure that quantum mechanics already takes for granted — a complex state space with a U(1) phase whose absolute value is physically irrelevant — the rule emerges with a specific structural shape rather than being chosen by hand. The chapter does not claim the Born rule appears from nothing. It claims that, given what quantum mechanics already assumes about the geometry of states, the *form* of the probability rule is no longer a free choice — it's selected by what the geometry will support. That is a weaker claim than "the Born rule is forced by pure mathematics," and it's the claim the framework can defend.

## The Question Born Could Not Answer

Born's rule has a specific feature that demands explanation. The probability depends on the *square* of the inner product, not on the inner product itself, and not on its fourth power, or any other function of it. Why exactly the square?

This is not an idle question. If the probability rule were |⟨φ|ψ⟩| rather than |⟨φ|ψ⟩|², the formalism could have been built around it; the linearity of the wavefunction's evolution would still work; the expectation values would just look different. If the rule were |⟨φ|ψ⟩|⁴, similarly. There is no obvious mathematical reason from the wavefunction's properties alone that the exponent should be 2 rather than some other power.

Born's contemporaries asked. Heisenberg, Bohr, Pauli — none of them produced a derivation. Schrödinger never accepted that probability was the right reading of his wavefunction in the first place. Einstein famously did not believe the rule was the right account of nature. The exponent of 2 was treated as one of the brute facts about the quantum world: experiments confirm it, the formalism uses it, do not look too hard at why.

In 1957, Hugh Everett's many-worlds interpretation tried to derive the Born rule from the structure of branching. Decades of attempts followed, with various technical successes and philosophical disputes about whether any of them really worked. In the same year, 1957, Andrew Gleason published a theorem showing that, given certain assumptions about how probabilities should behave on Hilbert spaces of dimension three or higher, the Born rule is the *only* consistent probability rule. Gleason's theorem is rigorous and important, but it does not answer the question Born could not answer. It tells you that *if* you accept certain measure-theoretic premises, the Born rule must follow. It does not tell you why those premises are the right ones — and it does not give you a picture of *what the Born rule is* geometrically.

The framework's account contrasts with Gleason's not by avoiding premises altogether, but by working from premises of a different kind. Gleason's premises are measure-theoretic. The framework's are geometric: that the state space of a spin-1/2 particle is a three-sphere, and that the global phase is physically irrelevant. Given those geometric inputs, the Born rule is what the geometry will support — and the framework's account gives a picture, missing from Gleason, of *what the Born rule is*: the unique probability function on the quotient space the Hopf projection produces. The exponent of 2 is not a free parameter to be set by hand; it's what the Hopf projection selects, once the geometric inputs are accepted. The chapter's claim, then, is the one its opening has already named: not that the Born rule appears from nothing, but that — given what quantum mechanics already assumes about the geometry of states — the form of the probability rule is no longer a free choice.

## Three Facts You Already Know

The derivation rests on three facts. All three are standard quantum mechanics, already present in every quantum mechanics textbook, none of which is exotic or controversial. Combining them gives the Born rule.

**Fact one.** The state of a spin-1/2 particle — an electron, say, with its spin pointing in some direction — can be written as a complex two-component vector. Two complex numbers, one for "spin up" and one for "spin down." For the state to be normalised (so that the total probability of finding the spin in *some* direction is 1), the sum of the squared magnitudes of the two complex numbers must equal 1.

This constraint defines a specific geometric object. Two complex numbers correspond to four real numbers, and the constraint that their squared magnitudes sum to 1 — namely |z₁|² + |z₂|² = 1 — defines the unit sphere in four-dimensional real space. This is exactly the three-sphere S³, the same closed three-dimensional space we have been discussing as the universe itself.

The state space of a spin-1/2 particle is, geometrically, an S³ — a three-sphere. The physical universe, the framework claims, is also an S³. We will be careful about what this does and does not mean, structurally, later in the chapter. For now, the relevant fact is that S³ is the geometric object on which the rest of the chapter's argument rests.

**Fact two.** Two quantum states that differ only by an overall *global phase* — multiplied by some factor of the form e^(iθ) — are physically identical. No experiment can distinguish them. This has been part of quantum mechanics since the formalism was written down. It's not an additional postulate; it falls out of the fact that all physical predictions depend on inner products, and an overall phase factor does not affect the magnitude of any inner product.

In geometric language: states that differ by a global phase are *the same point* in the physical state space. The full S³ has more points than there are physically distinct states; we have to identify all the points that differ by a phase factor as one point.

**Fact three.** The mathematical operation of identifying all points on S³ that differ by a phase factor has a name. It's called the *Hopf fibration*, discovered by the Swiss mathematician Heinz Hopf in 1931. It's the mathematical map from S³ to a smaller object — the two-dimensional sphere S². Every point on S² corresponds to a circle of points on S³ that all differ from each other only by a global phase factor.

The two-sphere S² that results from this identification is, in the language of quantum mechanics, the *Bloch sphere*. Every physics student who has drawn a picture of a spin pointing in a direction has drawn a point on the Bloch sphere. They have used the Hopf fibration, whether they called it by that name or not.

These three facts, taken together, have a specific geometric content. The state space of a spin-1/2 particle is S³. The physically distinct states are points on S² (the Bloch sphere). The map between them is the Hopf fibration. None of this is new physics. All of it's standard.

## What the Derivation Says

Now the move that produces the Born rule.

A measurement of a spin-1/2 particle asks: given that the particle is in some state on S³, and given that we are measuring in some basis (say "up" versus "down"), what is the probability of getting the answer "up"?

The probability must be a function from the state (a point on S³) to a number between zero and one. This function must satisfy three requirements, each falling out of the three facts.

It must not depend on global phase, because global phase is physically meaningless. So it must be a function of points on S² (the Bloch sphere), not on S³ — it has to be invariant under the Hopf fibration's identifications.

It must transform smoothly when the measurement basis is rotated. If you rotate the apparatus by some angle, the probabilities should transform in the corresponding way. This is automatic if the probability function is geometrically natural — it's what mathematicians call SU(2)-equivariance.

It must be properly normalised, summing to 1 over the possible outcomes.

The remarkable fact — and the framework's central claim about quantum mechanics — is that *only one function* is selected by the three requirements simultaneously, up to overall normalisation, given that the state space is S³ with the Hopf fibration's phase identification. The only smooth function on S³ that is invariant under those phase identifications, transforms correctly under rotations, and sums to 1 over outcomes, is exactly |⟨φ|ψ⟩|². The squared magnitude of the inner product. The Born rule.

The rigorous uniqueness statement, including the precise specification of what "simultaneously satisfies" means and how the squared-magnitude form emerges from the three requirements, is in Companion Paper 2 of the framework's technical corpus. The chapter sketches the result; the paper proves it.

The exponent of 2 is selected by the geometry, given that the state space is what quantum mechanics says it is. It's not a free parameter we could choose differently while keeping the geometric setup the same. It's what the Hopf fibration produces when you ask for a probability on the quotient space.

## Why the Square Comes Out

For the reader who would like a more concrete sense of where the squaring comes from, here is the geometric picture without the equations.

The states on S³ can be written as pairs of complex numbers (z₁, z₂). The Hopf fibration identifies two points on S³ as the same physical state when they differ by a phase factor — which means multiplying both z₁ and z₂ by the same e^(iθ).

The function |z₁|² is invariant under this multiplication: |e^(iθ)z₁|² = |z₁|², because the phase factor does not affect the magnitude. It's the *simplest* function with this invariance property — the simplest function that ignores the phase and depends only on the magnitude.

If you ask "what is the probability of measuring 'up'?", the answer is: the squared magnitude of the up-component of the state, |z₁|². If you ask "what is the probability of measuring 'down'?", the answer is |z₂|². The two probabilities sum to 1 by the original normalisation constraint |z₁|² + |z₂|² = 1.

The "squaring," in this picture, is what *invariance under phase rotation* selects, given the geometric setup. Linear functions of z would change under phase rotation; cubic functions would not be normalisable; absolute-value functions are not smooth; |z|² is the simplest function that satisfies all the requirements at once.

The Born rule, geometrically, is the *simplest possible* probability function on the state space, given the constraints. The exponent of 2 emerges from the existence of a phase that has to be ignored.

## What the Framework Adds

A reader who has been following the argument may notice something. The derivation just sketched does not require the framework. It uses standard quantum mechanics — the state space is S³, the phase is U(1), the quotient is the Hopf fibration to S² — and the Born rule falls out from the geometry of these standard objects. Why does this chapter belong in a book about the framework, rather than in any quantum mechanics textbook?

The answer is that the framework explains *why* the state space is what it is. In standard quantum mechanics, the state space is S³ because spin-1/2 particles have two complex components and that is what their normalised state space looks like. Why two components? Because spin is a representation of SU(2). Why SU(2)? Because rotations in three dimensions form that group.

The framework provides a deeper account. The S³ that appears as the state space of a spin-1/2 particle is not just *similar in shape* to the S³ that is the universe — the two share specific structural features that matter. Both are three-spheres. Both have a U(1) phase that has to be quotiented out (in the quantum case, the global phase of the wavefunction; in the cosmological case, the U(1) gauge structure of electromagnetism that emerges at gauge birth, which Chapter 7 will develop). Both, when projected through the Hopf fibration, produce a two-sphere that captures the physically distinguishable content. The Hopf fibration is doing the same kind of geometric work in both contexts, and it's doing it on the same kind of underlying object.

We should be careful about how strong a claim this is. The framework's earlier drafts of this chapter said that the S³ in quantum mechanics *is* the same S³ as the universe — one three-sphere, one phase identification, one Hopf projection. That is more than what the structural argument supports. What the structural argument supports is the weaker but still substantive claim that the geometric apparatus of quantum mechanics — the three-sphere state space, the U(1) phase to be quotiented, the Hopf fibration to the Bloch sphere — *shares the Hopf fibration structure* of the universe's geometry as the framework reads it. The same kind of object, with the same kind of phase, projected the same way, in both contexts. Whether quantum-mechanical S³ and universe-S³ are *literally identified* — one geometric object playing both roles — is a stronger claim than the framework currently supports, and the chapter retreats from it.

The weaker claim is still doing structural work. If quantum mechanics's S³ and the universe's S³ shared none of this structure — if they merely happened to be three-spheres for unrelated reasons — the Born rule's specific form would be a coincidence, separate from the framework's geometric programme. What the shared Hopf-fibration structure says is that the Born rule's specific form follows from the same kind of geometric setup the framework attributes to the universe at large: a three-sphere with a phase to be quotiented, projected through the Hopf fibration. The framework's claim is that this is not a coincidence. Both contexts inherit the same geometric apparatus because both involve the kind of three-sphere-with-U(1)-phase structure the framework places at the heart of physics.

This is the unification claim the chapter is making, in its honest form. The reason quantum mechanics has the specific probability rule it has is that the state space of quantum particles is a three-sphere with a U(1) phase, and the framework's reading of the universe places the same kind of structure at the heart of physics. The Born rule is what falls out when you do the geometry on a spin-1/2 system. The unification is structural at the level of *shared Hopf-fibration apparatus*, not literal identification of one S³ with another. The number 2 emerges as a topological feature of the geometry that quantum mechanics has — and that the framework's reading of the universe shares.

The framework's signature move once again, applied here to the quantum-mechanics-and-cosmology pairing: one geometric apparatus appearing in two domains, with both real.

## The Tsirelson Bound, Revisited

In Chapter 2, we mentioned in passing the Tsirelson bound — the maximum violation of Bell's inequality that quantum mechanics produces, equal to 2√2. This number falls out of the Hopf fibration too, and we can now say more cleanly where it comes from.

The Tsirelson bound is the maximum CHSH correlation function that the geometry of S³ supports under the Hopf projection. The cos²(θ/2) correlation function, which determines the angular dependence of measurement correlations between entangled particles, is the angular overlap of states projected through the Hopf fibration. Its maximum CHSH violation works out to exactly 2√2.

In the standard interpretation, this number is a curious feature of quantum mechanics's mathematics — it shows that quantum correlations are stronger than any local theory can produce, but weaker than the maximum logically possible, and the specific value 2√2 sits between them with no further explanation. In the framework's geometric picture, 2√2 is what the geometry gives. The empirical fact that experiments saturate this bound in carefully prepared entangled systems is consistent with the underlying state-space being what the framework claims it is — a three-sphere with the same Hopf-fibration structure that the framework attributes to the universe's geometry, producing the cos²(θ/2) correlation as a structural rather than postulated feature.

This is the second test. Chapter 2 introduced entanglement as null-time geometry; Chapter 6 derives the probability rule that quantum mechanics uses to *predict* entanglement correlations from the same geometric structure. The two are aspects of one fact — a fact about the shape of the state space.

## What This Means For The Rest of the Book

The Born rule chapter pays off something the book has been quietly setting up since Chapter 1. The methodological frame from the book's opening — the working bet that apparently separate phenomena are often fingers of the same hand — finds another finger in this chapter. The photon's null-time, entanglement, the closed S³ universe, the boundary expansion field's role in time emergence, and the Born rule are not five separate puzzles. They are aspects of one geometric programme, and the structure shared across them is a three-sphere geometry with a phase to be quotiented and a Hopf projection that produces observable consequences.

What remains to be developed in the rest of the book is, broadly, the application of this geometric picture to specific physical phenomena. The next chapter takes up the gauge birth — the moment in cosmic history when the boundary expansion field stabilised into the form that gives well-defined proper time, when the algebraic reduction from octonions to quaternions occurred (the structural origin of the U(1) phase that this chapter has been quotienting), and when the Standard Model gauge structure switched on. After that, the neutrino chapter — a species barely embedded in the gauge-birth cascade pattern, with consequences for both dark matter and the framework's account of how the two CPN-conjugate orientations of the manifold are coupled. Then dark matter as cross-thickness gravity, dark energy as the asymptotic floor of the boundary expansion field at late cosmic times, and finally the structural questions about what the framework does and does not yet derive.

The Born rule chapter is, in some sense, the climactic geometric chapter. From here on, the framework's geometric apparatus is established, and the work is to apply it.

The rule that Max Born could not derive in 1926 is, on the framework's reading, the simplest possible probability function on the state space, given the constraints. The state space is a three-sphere. The Born rule is what falls out when you project through the Hopf fibration. The exponent of 2 is selected by the geometry quantum mechanics has — the same geometric structure the framework's reading attributes to the universe's boundary as well.

This is the shape of probability. It has been the shape all along.
