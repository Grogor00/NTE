---
title: "Why three: a measure-theoretic floor and a least-action ceiling on the dimension of a surface ontology"
author: "G. White (Gregory Lyndon White)"
date: "2026-06-24 (v0.1 — DRAFT, HOLD)"
status: "DRAFT v0.1 — HOLD (development, not for send). Foundational deep-dive companion to the 'Quantum Mechanics is Geometry' chapter and the surface-ontology axiom. Derivation by the Scratch operator-theory lane (Wolfram-grounded); awaits independent check, AC ratification, Greg sign-off. Honesty scope: the two dimensional brackets are KNOWN physics; the NTE-specific claim is only that the Hopf structure could IDENTIFY them — that identification is OPEN, not established."
---

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*[Deep-dive companion to the QM-is-Geometry / surface-ontology foundations. One of a planned series; the main papers remain the master linking documents.]*

---

## Abstract

NTE makes a surface fundamental: the universe is the shape of the quantum state space, and the Born rule is invariant area on that surface (the Hopf base ℂP¹ = S²). This note asks what *constrains the dimension* of such a surface, and finds the dimension three bracketed from two sides by independent principles. **Floor (measure/quantum):** the rotation group of the Bloch sphere, SO(3), contains a free group F₂ and is therefore non-amenable, so the sphere admits Banach–Tarski paradoxical decompositions; the invariant area that defines probability is unique *only* when measurability is imposed. Measurability is thus a load-bearing physical constraint, non-trivial precisely because the fundamental surface is non-amenable. Gleason's theorem then forces the Born measure uniquely, but only at Hilbert dimension ≥ 3; the single qubit (ℂP¹ = S²) is doubly deficient — it is both the first non-amenable sphere and the dimension at which Gleason fails. **Ceiling (dynamical/least-action):** the stability of the action's bound-state extrema gives V''(r₀) ∝ (3 − d) at the circular orbit, so stable orbits and atoms exist only for spatial dimension d ≤ 3; with the requirement that gravity propagate (no local degrees of freedom below d = 3) this is a self-contained dynamical bracket d_space = 3 (Ehrenfest–Tangherlini–Whitrow). We are explicit that both brackets are established physics, and that they bound *different* dimensions — a quantum *state-space* floor and a dynamical *spatial* ceiling. The NTE-specific proposal is that the **Hopf fibration S¹ → S³ → S²**, which makes the spatial 3-sphere the unit sphere of the qubit state space, is the structure that could *identify* these two dimensions, so that a single integer is squeezed to three from both sides. That identification is stated as an open derivation, not a result. No new numerical prediction is claimed; the contribution is to make the dimension-selection question precise and to locate exactly where a genuine forcing would have to come from.

---

## 1. The question

The surface-ontology axiom ("the universe is the shape of the state space"; Born rule = area on the Hopf base S²) is silent on *why the surface has the dimension it does*. This note asks whether anything forces it. We find two independent constraints that each point at three, and identify the one structural step — internal to NTE — that would be needed to make them bound a single quantity.

Throughout we keep three "dimensions" distinct and never silently identify them: the **spatial** dimension d_space (the manifold, S³), the **state-space / Hilbert** dimension d_H (the qubit ℂ², base ℂP¹ = S²), and the **sphere** dimension appearing in the amenability argument. Conflating them is the standard way a dimension-selection argument fools itself; we flag every crossing.

## 2. The floor: measurability is load-bearing because the Bloch sphere is non-amenable

The amenability switch is sharp and dimension-located. The isometry group of the circle, SO(2), is abelian, hence amenable: invariant length exists on all subsets and no paradox arises. The rotation group of the 2-sphere, SO(3), **contains a free group F₂** — generated, in the classical construction, by rotations through arccos(1/3) about two perpendicular axes (verified here numerically: 1456 reduced non-trivial words of length ≤ 6 all sit ≥ 0.13 from the identity, with no relations). A group containing F₂ is non-amenable, and a non-amenable rotation group makes the sphere **paradoxical** (Hausdorff–Banach–Tarski): it can be cut into finitely many pieces and reassembled into two spheres of the same area — *using non-measurable pieces*. The switch flips once, at S²/SO(3), and stays flipped for all higher spheres (each contains SO(3)).

The consequence for a surface ontology where probability is area: **the invariant area measure is unique only on the σ-algebra of measurable sets.** Drop measurability and paradoxical decompositions let one "create probability from nothing" on the fundamental surface. Hence measurability/σ-additivity is not a technical footnote but a *physical constraint* doing real work — and it is non-trivial precisely because the surface is non-amenable (on the amenable circle, by contrast, invariant means are not even unique, and the issue does not arise in the same form). This sharpens the Born-rule-as-area picture by naming which constraint is essential and why it cannot be relaxed.

## 3. From "an invariant area exists" to "the Born rule": Gleason, and the deficient qubit

Uniqueness of an invariant *area* is not yet the Born *rule*. Gleason's theorem supplies the latter: every measure on the projections of a Hilbert space of dimension ≥ 3 is given by a density operator (Born). Crucially, **Gleason fails at dimension 2** — the single qubit, whose projective space is exactly ℂP¹ = S². So the bare qubit is **doubly deficient**: it is the first non-amenable sphere (§2) *and* the dimension at which the Born rule is not forced by non-contextuality. A surface ontology cannot rest the *forcing* of Born on the bare Hopf qubit; it requires the Hilbert dimension ≥ 3 that NTE supplies through its three-generation / octonionic structure. The minimal dimension at which the area-probability is both unique-invariant (§2) and Gleason-forced is **d_H = 3** — a floor, not a selection (Gleason holds for all d_H ≥ 3; nothing here forbids more).

> **Floor.** A surface-ontology Born-area is well-defined-and-forced only for state-space (Hilbert) dimension d_H ≥ 3. The qubit S² is the doubly-special boundary case.

## 4. The ceiling: least action forbids spatial dimension above three

The action's bound-state extrema must be stable for atoms and orbits to exist. For a central potential from Gauss's law in d spatial dimensions, V(r) ∝ −r^{2−d}, the effective potential V_eff = L²/2r² − k r^{2−d} has a circular-orbit extremum whose curvature satisfies (computed here)

> **V''(r₀) ∝ (3 − d).**

So the extremum is a stable minimum only for **d < 4, i.e. d_space ≤ 3**: d = 3 is Kepler (stable, closed orbits), d = 4 is exactly marginal, d ≥ 5 is unstable (no bound orbits or atoms). This is the Ehrenfest–Tangherlini stability ceiling. Pairing it with the requirement that gravity carry propagating degrees of freedom — absent for d_space ≤ 2, where general relativity is topological — gives a **self-contained dynamical bracket**:

> **Ceiling + dynamical floor.** Stable bound states ⇒ d_space ≤ 3; propagating gravity ⇒ d_space ≥ 3. Hence d_space = 3, entirely from the action (Ehrenfest–Tangherlini–Whitrow).

## 5. The synthesis — and the open step that would make it a forcing

We now have two brackets, each independently pointing at three:

| bracket | principle | quantity bounded | result |
|---|---|---|---|
| quantum / measure | non-amenability + Gleason | state-space dim d_H | d_H ≥ 3 |
| dynamical | least action (stability) + propagating gravity | spatial dim d_space | d_space = 3 |

They are **different dimensions**, and nothing in standard physics ties them. This is exactly where a surface ontology built on the **Hopf fibration** has something to say that a generic framework does not: in NTE the spatial 3-sphere is *the unit sphere of the qubit state space*, S³ ⊂ ℂ², with S¹ → S³ → S² the Hopf map. The spatial manifold and the state space are **not independent** — they are the total space and (projectivised) base of one fibration. If that identification is genuine at the level that the two brackets act on, then the dynamical ceiling on d_space and the quantum floor on d_H are squeezing **one** integer, and three is forced from both sides by independent physics: dynamics forbids more, measure-plus-Gleason forbids less.

**This identification is the open derivation, not a result.** The honest gap: the dynamical bracket fixes d_space = 3 (the Hopf *total* space S³), while the Gleason floor is about d_H (the Hilbert space ℂ² of the qubit, dimension 2, with the ≥ 3 forcing coming from generations). The Hopf map relates S³ and ℂ², but a derivation that the *same* "3" is being bounded — that the dynamical spatial three and the quantum state-space three are one object and not a numerical coincidence — has not been given here. Until it is, this is a **strong consistency with a candidate forcing mechanism identified**, not a forcing.

## 6. Honest scorecard

- **New sharpening (real):** in a Born-is-area ontology, measurability is a load-bearing axiom, non-trivial because the Bloch sphere is non-amenable. This belongs in the QM-is-Geometry chapter.
- **New caveat (real):** the single qubit is doubly deficient (non-amenable *and* Gleason-failing); the forcing of Born requires the dimension-≥-3 structure, not the bare Hopf qubit.
- **Known physics (not claimed as new):** the non-amenability switch at SO(3); Gleason's dimension-≥-3 requirement; the Ehrenfest–Tangherlini stability ceiling; the propagating-gravity floor. NTE imports these; it does not discover them.
- **NTE-specific candidate forcing (open):** the Hopf fibration as the bridge identifying d_space with d_H, which would convert two independent "≥/≤ 3" brackets into a single forced d = 3. **This is the deliverable's one genuinely new claim, and it is stated as an open derivation.**
- **No new numerical prediction.** As with the Fubini–Study mixing-angle deep-dive, the value here is consolidation and the precise location of where a forcing would have to come from — not a new observable.

## 7. The next step

Close §5's gap: derive whether the Hopf identification S³ ⊂ ℂ² makes the dynamical (spatial) and quantum (state-space) dimensions the same object at the level the two brackets act on. Concretely — does the least-action stability functional, written on the Hopf *total* space, descend to a constraint on the *base* state-space dimension (and vice versa), so that the ceiling and floor provably bound one integer? If yes, d = 3 is doubly forced and this becomes a genuine selection result. If the descent fails, the two threes are a coincidence and this remains a consistency note. Gated, derive-then-claim, with "coincidence-not-forcing" a fully acceptable outcome.

---

## References

1. F. Hausdorff, "Bemerkung über den Inhalt von Punktmengen," Math. Ann. **75**, 428 (1914).
2. S. Banach, A. Tarski, "Sur la décomposition des ensembles de points...," Fund. Math. **6**, 244 (1924).
3. J. von Neumann, "Zur allgemeinen Theorie des Masses," Fund. Math. **13**, 73 (1929) (amenability).
4. A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," J. Math. Mech. **6**, 885 (1957).
5. P. Ehrenfest, "In what way does it become manifest in the fundamental laws of physics that space has three dimensions?" Proc. Amsterdam Acad. **20**, 200 (1917).
6. F. R. Tangherlini, "Schwarzschild field in n dimensions...," Nuovo Cimento **27**, 636 (1963).
7. NTE corpus, "Quantum Mechanics is Geometry" (Ch. 6); surface-ontology axiom; Hopf fibration S¹→S³→S².

---

*Draft v0.1 — Scratch operator-theory lane, 2026-06-24. Wolfram-grounded (F₂ ⊂ SO(3) numeric; V'' ∝ 3−d). For adversarial reading and AC ratification. The two dimensional brackets are known physics; the only new claim is that NTE's Hopf structure could unify them into a forced d = 3 — flagged as an open derivation, not banked.*
