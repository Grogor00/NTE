---
title: "The Born Rule as a Hopf Projection"
subtitle: "A tier-3 explanatory note on the Born rule as a Hopf projection on S³, and its activation at gauge birth"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06 (v10.19.0)"
---

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## Scope of this note

The geometric fact at the centre of this note — that a single qubit's state space is the 3-sphere $S^3$, and that the Hopf fibration $S^3 \to S^2$ realises the Bloch sphere as its base with the circular fibre carrying the overall phase — is **established in the literature** (Mosseri & Dandoloff, *J. Phys. A* **34**, 10243 (2001); extended by Lévay, Wie, and others). The same $S^3 \to S^2$ Hopf map is a well-known cross-context object: it is the qubit/Bloch geometry, the Dirac/Wu–Yang monopole bundle, and a recurring structure in pre-geometric quantum gravity. **This note makes no claim of novelty for the geometry.** It is an explanatory piece for the curious reader, written to make the geometry vivid and to record the one framework-specific reading the Non-Temporal Emergence (NTE) framework adds: that the Hopf structure becomes physically operative at "gauge birth."

---

## 1. The single qubit is a 3-sphere

A normalised qubit state $|\psi\rangle = z_1|0\rangle + z_2|1\rangle$ with $|z_1|^2 + |z_2|^2 = 1$ is a point of the unit sphere $S^3 \subset \mathbb{C}^2$. Two states that differ only by an overall phase, $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$, are physically identical — so the physical states are not the points of $S^3$ but the *orbits* of the overall-phase circle $U(1)$ acting on it.

Quotienting $S^3$ by that circle is exactly the **Hopf fibration**

$$S^1 \hookrightarrow S^3 \xrightarrow{\;\pi\;} S^2,$$

whose base $S^2$ is the **Bloch sphere** of physically distinct qubit states, and whose fibre $S^1$ is the unobservable global phase. This is Mosseri & Dandoloff's reading of the Bloch sphere; everything below is built on it.

## 2. The Born rule is the projection

Write a measurement direction as a point on the Bloch sphere $S^2$. The probability the qubit yields that outcome is the Born rule $P = |\langle\phi|\psi\rangle|^2$, and in Bloch-sphere terms it is the angular overlap

$$P = \cos^2(\theta/2),$$

where $\theta$ is the angle on $S^2$ between the state and the measurement direction. This $\cos^2(\theta/2)$ is precisely the **Hopf-projected overlap** between the two spinor directions on $S^3$ — the geometry does the work the algebra usually does.

Why $|\cdot|^2$ and not some other function? Because the probability map must be (i) invariant under the global-phase $U(1)$ (the fibre is unobservable) and (ii) equivariant under the $SU(2)$ that rotates the sphere, and must be normalised, additive, and continuous. Those requirements fix the map uniquely to the squared overlap. (This is a geometric instance of the kind of uniqueness result long known from Gleason's and Busch's theorems; the contribution here is to read it off the Hopf symmetry rather than to derive the Born rule afresh.)

## 3. The one framework-specific reading: activation at gauge birth

In NTE, the $U(1)$ that makes global phase unobservable is a *gauge* symmetry, and gauge symmetry comes into existence only at "gauge birth," when emergent time switches on (developed in the main framework). The reading this note records is therefore simple: **before gauge birth there is no $U(1)$, so global phase is not unobservable, so there is no Hopf fibre and no Born rule; at gauge birth the $U(1)$ activates, the fibre becomes physical, the projection $S^3 \to S^2$ becomes mandated, and the Born rule "switches on" with it.** This activation reading is the framework's only addition; the geometry it activates is the established Hopf–Bloch structure of §1–§2.

## 4. For the curious reader: the same sphere keeps showing up

The $S^3 \to S^2$ Hopf map is:
- the qubit Bloch geometry (this note);
- the Dirac/Wu–Yang magnetic monopole bundle, whose lowest harmonic $Y_{00}(S^2) = 1/\sqrt{4\pi}$ is the monopole amplitude;
- and, in NTE, the structure on which the dark-matter coupling $\kappa_0 = 3/\sqrt{4\pi}$ is read (three $\mathfrak{su}(2)$ modes times that same $Y_{00}$).

That a single classical fibration underlies the qubit, the monopole, and the framework's cross-sector coupling is the kind of recurrence that makes the geometry feel less like a coincidence and more like a piece of the furniture. None of those three facts is new on its own; the note simply puts them side by side.

---

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

*Pedagogical / explanatory note. The Hopf–Bloch geometry (§1–§2) is established (Mosseri & Dandoloff 2001 and successors); no novelty is claimed for it. The gauge-birth activation reading (§3) is the NTE-specific framing. Companion to the technical papers Companion 2 and Companion 6.*

— G. White, 2026-06 (tier-3 explanatory note, v10.19.0 light-currency update).
