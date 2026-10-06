---
title: "An octonionic origin for the Standard Model gauge group and fermion species count via the associativity transition"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-22 (v0.2 pre-submission draft)"
---

*Part of NTE Corpus v10.18.0 (deposited 2026-06).*

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

## Scope of this paper

The two structural facts this paper organises — that the octonions and the exceptional Jordan algebra $J_3(\mathbb{O})$ reproduce the Standard Model gauge group and a three-generation fermion content — are **established in the prior literature** (Günaydin–Gürsey 1973; Dixon 1994; Furey 2014, 2018; Dubois-Violette 2016; Todorov–Dubois-Violette 2018; Baez 2002). The reading that motivates the octonions in the first place — that non-associativity corresponds to the absence of a fixed time-ordering — is **also prior art** (Gogberashvili 2004; Köplinger–Dzhunushaliev–Gogberashvili). **This paper makes no claim of novelty for either.** Its role is to set out how a specific emergent-time framework (Non-Temporal Emergence, NTE) adopts these established structures, and to record where its premises make the adoption tight. The only framework-specific increments are the identification of the symmetry-breaking direction with the electroweak vacuum at "gauge birth," the Cayley–Dickson ↔ cosmic-epoch mapping, and the cross-consistency of the Majorana species count with the framework's dark sector — all flagged as such in the text.

---

## Abstract

We present an octonionic account of two structural facts about the Standard Model — its gauge group and its fermion species count — within a framework in which time and causal ordering are emergent rather than fundamental. Following an established reading (Gogberashvili 2004), associativity of physical operations corresponds to time-ordering; in a pre-temporal epoch with no time coordinate there is no mechanism to enforce associativity, so the natural operator algebra is the unique non-associative normed division algebra, the octonions $\mathbb{O}$ (Hurwitz). Its automorphism group is the exceptional Lie group $G_2$. At the onset of causal ordering ("gauge birth"), associativity is enforced, the algebra reduces $\mathbb{O} \to \mathbb{H}$, and a selected imaginary direction $e_1 \in \mathrm{Im}(\mathbb{O})$ — the electroweak vacuum direction — breaks $G_2 \to SU(3)$, whose stabiliser structure, with the quaternionic subalgebra $\mathbb{H} \supset S^3 \cong SU(2)$ and a parity selection, yields $SU(3)_C \times SU(2)_L \times U(1)_Y$. The exceptional Jordan algebra $J_3(\mathbb{O})$ supplies three generations; with the Majorana condition (required independently by the framework's dark-sector mechanism) the Dirac count $48$ reduces to $45$ Weyl species per sector, i.e. $90$ including conjugates. The four normed division algebras $\mathbb{O} \to \mathbb{H} \to \mathbb{C} \to \mathbb{R}$ map to four cosmological epochs, geometrically realised by the four Hopf fibrations. The gauge-group and species results are established prior art (see Scope); the construction derives neither the Yukawa couplings nor the mass hierarchy, and the three-generation hypercharge assignments and a proposed non-associative resolution of technical naturalness are flagged as open.

---

## 1. The associativity transition

In a universe with a time coordinate, sequential physical operations compose associatively: the time-ordering operation assigns a definite sequence to any product of fields, and once ordered, composition is associative, $(A \circ B) \circ C = A \circ (B \circ C)$. The converse reading — that **non-associativity corresponds to the absence of a fixed causal/temporal ordering** — is due to Gogberashvili (2004), who interprets the octonionic associator as encoding causality, and is developed further in the non-associative-quantum-theory programme of Köplinger, Dzhunushaliev and Gogberashvili ("emergent time from non-associative quantum theory"). We adopt that reading; we do not claim it.

We work within a framework (Non-Temporal Emergence, NTE) in which time is not fundamental but emerges at a transition we call gauge birth; before that transition there is no time coordinate. The premises we take from that framework, and do not re-derive here, are: (i) a pre-temporal boundary with no temporal ordering; (ii) a closed spatial $S^3$ geometry carrying a norm; and (iii) a conjugation symmetry (CPN) relating two sectors of the boundary. Within these premises, the rest follows from standard division-algebra mathematics.

The consequence of (i) with the Gogberashvili reading: with no time coordinate there is no time-ordering, hence no mechanism enforcing associativity. The algebra of operations on the pre-temporal boundary is therefore **generically non-associative**, while still inheriting a norm from the $S^3$ geometry and the Hilbert-space structure.

By Hurwitz's theorem, the only normed division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, of dimensions $1, 2, 4, 8$; of these, only $\mathbb{O}$ is non-associative (equivalently, the only parallelisable spheres are $S^0, S^1, S^3, S^7$). A normed, non-associative pre-temporal algebra is therefore **uniquely the octonions**.

---

## 2. The Cayley–Dickson sequence as cosmological emergence

The Cayley–Dickson construction builds $\mathbb{O}$ from $\mathbb{R}$ by successive doubling, each step losing one algebraic property: $\mathbb{R} \to \mathbb{C}$ loses ordering, $\mathbb{C} \to \mathbb{H}$ loses commutativity, $\mathbb{H} \to \mathbb{O}$ loses associativity. Run in reverse, structure is *gained* step by step, and we identify each gain with a physical transition:

| Transition | Property gained | Physical event |
|---|---|---|
| $\mathbb{O} \to \mathbb{H}$ | associativity | gauge birth (causal ordering begins) |
| $\mathbb{H} \to \mathbb{C}$ | commutativity | electroweak symmetry breaking (a commutative $U(1)_{\rm EM}$ is selected) |
| $\mathbb{C} \to \mathbb{R}$ | ordering | classical limit (definite outcomes; decoherence) |

The four algebras are also the algebras of the four Hopf fibrations — $S^0\!\to\!S^1\!\to\!S^1$ ($\mathbb{R}$), $S^1\!\to\!S^3\!\to\!S^2$ ($\mathbb{C}$), $S^3\!\to\!S^7\!\to\!S^4$ ($\mathbb{H}$), $S^7\!\to\!S^{15}\!\to\!S^8$ ($\mathbb{O}$) — so the algebraic sequence has a geometric realisation: at each epoch the boundary spinor modes carry the Hopf fibration of the currently-active division algebra. (The complex Hopf fibration $S^1 \to S^3 \to S^2$ is, in this framework, the geometry underlying the Born rule; developed separately, not needed here.) This epoch mapping is a framework-specific reading; it is a structural correspondence, not a dynamical derivation, and does not by itself fix the temperature or dynamics of each transition.

---

## 3. The gauge group: $G_2 \to SU(3)_C \times SU(2)_L \times U(1)_Y$

*(This section restates established results — Günaydin–Gürsey 1973; Dixon 1994; Furey 2018; Todorov–Dubois-Violette 2018 — with the framework-specific reading of the symmetry-breaking direction noted in §3.2.)*

### 3.1 The pre-temporal symmetry $G_2$

The automorphism group of $\mathbb{O}$ is the compact exceptional Lie group $G_2$ (dimension 14). It is the symmetry of the pre-temporal boundary, acting on the octonionic spinor modes. $G_2$ has two relevant maximal subgroups: $SU(3)$, the stabiliser of a complex line in $\mathrm{Im}(\mathbb{O})$ ($G_2/SU(3) \cong S^6$); and $SO(4) \cong (SU(2) \times SU(2))/\mathbb{Z}_2$, the stabiliser of a quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$.

### 3.2 Colour: the Higgs direction and $G_2 \to SU(3)$

At gauge birth the electroweak vacuum selects an imaginary octonionic direction $e_1 \in \mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. $G_2$ acts transitively on $S^6 \subset \mathrm{Im}(\mathbb{O})$, so the stabiliser of $e_1$ has dimension $14 - 6 = 8$ and is precisely $SU(3)$, acting on the orthogonal complement $\mathbb{R}^6 \cong \mathbb{C}^3$, identified with $SU(3)_C$. Under $G_2 \to SU(3)$, $\mathrm{Im}(\mathbb{O}) = \mathbb{R}^7 \to \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$. The identification of the SM symmetry inside the octonion/Jordan structures is established (refs above); the only framework-specific element is reading $e_1$ as the physical electroweak vacuum direction at gauge birth.

### 3.3 Weak isospin and hypercharge

The physical spatial boundary is $S^3 \cong SU(2)$, the unit quaternions, embedded in $S^7$; the corresponding $SU(2)$ is one factor of $SO(4) \subset G_2$, identified with $SU(2)_L$. The complex line $\mathbb{C} = \mathrm{span}\{1, e_1\}$ gives $U(1)_Y$.

**Parity.** The two factors of $SO(4)$ are $SU(2)_L$ and $SU(2)_R$. The framework's CPN conjugation relates the two boundary sectors; combined with spatial parity it maps left-handed modes in one sector to right-handed modes in the conjugate sector, so the right-handed isospin factor acts on conjugate-sector fields and is not a gauge symmetry of the observable sector. Parity violation is thus built into the boundary structure. The surviving observable gauge group is $SU(3)_C \times SU(2)_L \times U(1)_Y$.

### 3.4 The sense of uniqueness

Given the framework's premises — an octonionic pre-temporal algebra, a CPN boundary, an emergent-time transition — the gauge group is *forced*: Hurwitz excludes other normed division algebras; the vacuum direction's stabiliser is always $SU(3)$; the parity selection follows from CPN. The uniqueness is conditional on the premises, not absolute. It is in this conditional sense that the framework *adopts* — rather than postulates by hand — a gauge group whose octonionic origin is established in the literature.

---

## 4. Species count from $J_3(\mathbb{O})$

*(The one-generation and three-generation counts are established — Furey 2018; Todorov–Dubois-Violette 2018. The Majorana reduction and its dark-sector cross-consistency, §4.3, are the framework-specific elements.)*

### 4.1 One generation
The complex octonions $\mathbb{C} \otimes \mathbb{O}$ carry a minimal left ideal of complex dimension 8; under $SU(3) \times U(1)$ it decomposes into a colour triplet, an antitriplet, and two singlets — one partial generation (Furey 2018; Dixon 1994). The full 16-dimensional representation reproduces the 16 Weyl states of one generation.

### 4.2 Three generations
$J_3(\mathbb{O})$ — $3\times3$ Hermitian octonionic matrices, dimension 27, automorphism group $F_4$ — contains three copies of the $\mathbb{C}\otimes\mathbb{O}$ generation structure along its diagonal slots: $3 \times 16 = 48$ Weyl states (Dirac counting).

### 4.3 The Majorana reduction to 90 (framework-specific)
The framework requires Majorana neutrinos (imposed independently by its dark-sector mechanism). The Majorana condition removes one independent state per generation: $48 - 3 = 45$ Weyl species per sector; with conjugates, $90$. With the CPN two-sector doubling, the finite algebra for the framework's spectral-triple computations is $A_F = \mathbb{O} \oplus \mathbb{O}$, $N_F = 180$ [companion heat-kernel note]. That a condition imposed for the dark sector reproduces exactly the $J_3(\mathbb{O})$ species count is a non-trivial internal cross-consistency, not a fit.

---

## 5. Scope: what the construction does and does not deliver

**Delivered (adopting prior art):** the gauge *group* (conditional on the premises, §3.4); three generations; the species count (90, with the independently-motivated Majorana condition).

**Not delivered, not claimed.**
- *Yukawa couplings and the mass hierarchy* — three equal-weight generations; the hierarchy needs a $J_3$ symmetry breaking not derived here. Yukawas inherited from observation, as in the SM.
- *Three-generation hypercharge assignments* — single-generation hypercharges follow from octonionic multiplication (Furey 2018); the $J_3(\mathbb{O})$ extension to three generations is only partially verified — **open**.
- *Cosmological observables* ($n_s$, etc.) — do not follow from the $G_2$ representation content.

**Open programme: technical naturalness.** Since $J_3(\mathbb{O})$ is non-associative, products are defined up to the associator, with the alternative law $[A,A,B]=0$. It is conjectured that, with the Higgs embedded in $J_3(\mathbb{O})$, the collinear region driving the Higgs-mass quadratic divergence is where the alternative law acts. This is a motivated direction, not a result — it needs an explicit Higgs embedding and an octonionic loop formulation, neither carried out here.

---

## 6. Discussion and falsifiers

The construction ties three facts — the non-associativity of the pre-temporal algebra (Gogberashvili reading), the SM gauge group, and the generation/species count — to one premise set through standard division-algebra mathematics. Its appeal is economy of inputs, not novelty of the group theory.

Falsifiable in three senses: (1) if a consistent NTE formulation required a normed division algebra other than $\mathbb{O}$, the construction fails — but Hurwitz leaves none; (2) if the three-generation hypercharges through $J_3(\mathbb{O})$ fail to reproduce the SM values, §4 fails at three generations (the single-generation case is established); (3) if the $J_3(\mathbb{O})$ + Majorana species count gave other than 90, the §4.3 cross-consistency fails. The second is the most pressing open check.

---

## References

1. A. Hurwitz, Gött. Nachr. (1898).
2. J. C. Baez, "The octonions," Bull. Amer. Math. Soc. **39**, 145 (2002).
3. M. Günaydin and F. Gürsey, "Quark structure and octonions," J. Math. Phys. **14**, 1651 (1973).
4. G. M. Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics* (Kluwer, 1994).
5. C. Furey, "Three generations, two unbroken gauge symmetries, and one eight-dimensional algebra," Phys. Lett. B **785**, 84 (2018).
6. I. Todorov and M. Dubois-Violette, "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra," Int. J. Mod. Phys. A **33**, 1850118 (2018).
7. M. Gogberashvili, "Octonionic geometry," Adv. Appl. Clifford Algebras (2005) [hep-th/0409173] — non-associativity as causality.
8. J. Köplinger, V. Dzhunushaliev, M. Gogberashvili, non-associative quantum theory / emergent time (and related works).
9. A. H. Chamseddine and A. Connes, "Noncommutative geometry as a framework for unification," Fortsch. Phys. **58**, 553 (2010) [arXiv:0812.0165].

---

*v0.2 pre-submission draft. Changes from v0.1: added the up-front Scope statement; credited Gogberashvili (2004) and Köplinger et al. for the non-associativity↔time reading; section-level "restates established results" flags on §3 and §4; honest-scope language preserved. The paper makes no novelty claim for the octonion→SM structure or the associativity reading; it presents the framework's adoption of established work.*
