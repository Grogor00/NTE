---
title: "Octonionic Adoption: Gauge Group, Species Count, and the Associativity Transition"
author: "G. White"
date: "2026-08-03 (v10.19.0 companion)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0. Companion 16 to Parts 1–3. Technical development of Part 2 §§8.5–8.6.*

---

## Scope

The two structural facts this companion organises — that the octonions and the exceptional Jordan algebra $J_3(\mathbb{O})$ reproduce the Standard Model gauge group and a three-generation fermion content — are **established prior art** (Günaydin–Gürsey 1973; Dixon 1994; Furey 2014, 2018; Dubois-Violette 2016; Todorov–Dubois-Violette 2018; Baez 2002). The reading that motivates the octonions — that non-associativity corresponds to the absence of a fixed time-ordering — is **also prior art** (Gogberashvili 2004; Köplinger–Dzhunushaliev–Gogberashvili). **This companion makes no novelty claim for either.** Its role is to set out how NTE adopts these structures, and where the framework's premises make the adoption tight.

Framework-specific increments (flagged in the text): identification of the symmetry-breaking direction with the electroweak vacuum at gauge birth; the Cayley–Dickson ↔ cosmic-epoch mapping (structural correspondence, not a dynamical derivation); CPN-driven assignment of $SU(2)_R$ to the mirror sector; and the Majorana species-count cross-consistency with the dark-sector mechanism (Companion 7).

This companion **supersedes** the informal Desktop draft `Paper_OctonionExtension_v10_9.md` for corpus use. That draft's mathematics of $G_2\to\mathrm{SM}$ and $J_3(\mathbb{O})$ species counting is preserved in substance; its novelty language, version-stale cross-references, and retired Companion-7a ontology are not.

---

## Abstract

Within NTE, time and causal ordering are emergent. Following Gogberashvili, associativity of physical operations corresponds to time-ordering; pre-temporally there is no mechanism enforcing associativity, so the natural normed operator algebra is uniquely the octonions $\mathbb{O}$ (Hurwitz), with automorphism group $G_2$. At gauge birth, associativity is enforced ($\mathbb{O}\to\mathbb{H}$), and a selected imaginary direction $e_1\in\mathrm{Im}(\mathbb{O})$ — the electroweak vacuum direction — breaks $G_2\to SU(3)$. With the quaternionic subalgebra $\mathbb{H}\supset S^3\cong SU(2)$ and CPN parity selection, the observable gauge group is $SU(3)_C\times SU(2)_L\times U(1)_Y$. The exceptional Jordan algebra $J_3(\mathbb{O})$ supplies three generations; with the Majorana condition (required independently by Companion 7) the Dirac count $48$ reduces to $45$ Weyl species per sector ($90$ including conjugates). The cascade $\mathbb{O}\to\mathbb{H}\to\mathbb{C}\to\mathbb{R}$ maps to gauge birth → EWSB → classical limit and is geometrically realised by the Hopf-fibration tower. Yukawa couplings, the three-generation hypercharge completion, and a proposed non-associative resolution of technical naturalness remain open (Part 3 ledger).

---

## 1. The associativity transition

In a universe with a time coordinate, sequential operations compose associatively: time-ordering assigns a definite sequence, and once ordered, $(A\circ B)\circ C = A\circ(B\circ C)$. The converse — that **non-associativity corresponds to the absence of fixed causal/temporal ordering** — is Gogberashvili (2004) and related Köplinger–Dzhunushaliev–Gogberashvili work. NTE adopts that reading; it does not claim it.

NTE premises used here (not re-derived): (i) a pre-temporal boundary with no temporal ordering (Part 1); (ii) a closed spatial $S^3$ geometry carrying a norm (Companions 3, 5); (iii) CPN conjugation relating two sectors of the boundary (Part 1; Companion 7). Within these premises, the rest follows from standard division-algebra mathematics.

With no time coordinate there is no time-ordering operator, hence no mechanism enforcing associativity. The pre-temporal algebra is therefore **generically non-associative**, while still inheriting a norm from the $S^3$ geometry and Hilbert-space structure.

By Hurwitz's theorem the only normed division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ (dimensions $1,2,4,8$); only $\mathbb{O}$ is non-associative (equivalently, the only parallelisable spheres are $S^0,S^1,S^3,S^7$). A normed, non-associative pre-temporal algebra is therefore **uniquely the octonions**.

---

## 2. Cayley–Dickson sequence and Hopf tower

The Cayley–Dickson construction builds $\mathbb{O}$ from $\mathbb{R}$ by successive doubling, losing one algebraic property at each step. Run in reverse, structure is gained:

| Transition | Property gained | Physical event |
|---|---|---|
| $\mathbb{O}\to\mathbb{H}$ | associativity | gauge birth (causal ordering begins) |
| $\mathbb{H}\to\mathbb{C}$ | commutativity | EWSB ($U(1)_{\mathrm{EM}}$ selected) |
| $\mathbb{C}\to\mathbb{R}$ | ordering | classical limit (decoherence) |

The four algebras are the algebras of the four Hopf fibrations — $S^0\!\to\!S^1\!\to\!S^1$ ($\mathbb{R}$), $S^1\!\to\!S^3\!\to\!S^2$ ($\mathbb{C}$), $S^3\!\to\!S^7\!\to\!S^4$ ($\mathbb{H}$), $S^7\!\to\!S^{15}\!\to\!S^8$ ($\mathbb{O}$) — so the algebraic sequence has a geometric realisation: at each epoch the boundary spinor modes carry the Hopf fibration of the active division algebra. The complex Hopf fibration is the geometry underlying the Born rule (Companion 2); it becomes available once $U(1)$ phase is unobservable at gauge birth (Companion 6).

This epoch mapping is a **framework-specific structural correspondence**, not a dynamical derivation of transition temperatures. The gauge-birth temperature $T_{\mathrm{GB}}=M_{\mathrm{Pl}}/\sqrt{2\pi}$ is fixed elsewhere (Companion 9 / Companion 12 fibre modulus).

---

## 3. Gauge group: $G_2\to SU(3)_C\times SU(2)_L\times U(1)_Y$

*(This section restates established results — Günaydin–Gürsey; Dixon; Furey; Todorov–Dubois-Violette — with the framework-specific reading of the breaking direction noted below. NTE derives the gauge group octonionically via the $G_2$-stabiliser route; it is not a Pati–Salam left–right construction. Jordan-geometry encoding of SM / Pati–Salam fermion representations is prior art in this lineage — Pati–Salam 1974; Boyle–Farnsworth 2020 — which NTE credits without adopting the left–right gauge architecture; Part 2 §§8.5–8.6.)*

### 3.1 Pre-temporal symmetry $G_2$

$\mathrm{Aut}(\mathbb{O})=G_2$ (compact, dimension 14). Relevant maximal subgroups: $SU(3)$, stabiliser of a complex line in $\mathrm{Im}(\mathbb{O})$ ($G_2/SU(3)\cong S^6$); and $SO(4)\cong(SU(2)\times SU(2))/\mathbb{Z}_2$, stabiliser of a quaternionic subalgebra $\mathbb{H}\subset\mathbb{O}$.

### 3.2 Colour: electroweak vacuum direction

At gauge birth the electroweak vacuum selects $e_1\in\mathrm{Im}(\mathbb{O})\cong\mathbb{R}^7$. $G_2$ acts transitively on $S^6\subset\mathrm{Im}(\mathbb{O})$, so the stabiliser of $e_1$ has dimension $14-6=8$ and is $SU(3)$, acting on $\mathbb{R}^6\cong\mathbb{C}^3$, identified with $SU(3)_C$. Under $G_2\to SU(3)$,

$$\mathrm{Im}(\mathbb{O})=\mathbb{R}^7 \longrightarrow \mathbf{1}\oplus\mathbf{3}\oplus\bar{\mathbf{3}}.$$
The only framework-specific element is reading $e_1$ as the physical electroweak vacuum direction at gauge birth (Companions 4, 6).

### 3.3 Weak isospin, hypercharge, and parity

The physical spatial boundary is $S^3\cong SU(2)$, the unit quaternions, embedded in $S^7$; the corresponding $SU(2)$ is one factor of $SO(4)\subset G_2$, identified with $SU(2)_L$. The complex line $\mathbb{C}=\mathrm{span}\{1,e_1\}$ gives $U(1)_Y$.

**Parity.** The two factors of $SO(4)$ are $SU(2)_L$ and $SU(2)_R$. CPN conjugation combined with spatial parity maps left-handed modes in one sector to right-handed modes in the conjugate sector, so $SU(2)_R$ acts on conjugate-sector fields and is not a gauge symmetry of the observable $+N$ sector. Parity violation is built into the boundary. The surviving observable group is $SU(3)_C\times SU(2)_L\times U(1)_Y$.

$S^3$ here is forced, not fitted: it is the unit sphere of the quaternionic subalgebra $\mathbb{H}\subset\mathbb{O}$ that survives the $\mathbb{O}\to\mathbb{H}$ associativity transition — the same $\mathbb{H}$ whose $SU(2)$ factor is $SU(2)_L$. Resolved fermions localise on this $S^3$ while the CPN-even neutrino stays delocalised over the full $S^7$ (Part 2 §IX; Companion 7). That localisation does **not** independently derive three generations; generations remain $J_3(\mathbb{O})$.

### 3.4 Conditional uniqueness

Given NTE's premises — octonionic pre-temporal algebra, CPN boundary, emergent-time transition — the gauge group is *forced* in a conditional sense: Hurwitz excludes other normed division algebras; the vacuum direction's stabiliser is always $SU(3)$; the parity selection follows from CPN. Uniqueness is conditional on the premises, not absolute. In that sense NTE **adopts** — rather than postulates by hand — a gauge group whose octonionic origin is established in the literature (Part 1 Positioning; Part 2 §§8.5–8.6).

---

## 4. Species count from $J_3(\mathbb{O})$

*(One- and three-generation counts: Furey; Todorov–Dubois-Violette. Majorana reduction and dark-sector cross-consistency: framework-specific.)*

### 4.1 One generation

$\mathbb{C}\otimes\mathbb{O}$ carries a minimal left ideal of complex dimension 8; under $SU(3)\times U(1)$ it decomposes into a colour triplet, an antitriplet, and two singlets — one partial generation. The full 16-dimensional representation reproduces the 16 Weyl states of one generation.

### 4.2 Three generations

$J_3(\mathbb{O})$ — $3\times3$ Hermitian octonionic matrices, dimension 27, automorphism group $F_4$ — contains three copies of the $\mathbb{C}\otimes\mathbb{O}$ generation structure: $3\times 16=48$ Weyl states (Dirac counting).

### 4.3 Majorana reduction to 90

Companion 7 requires Majorana neutrinos independently (dark-sector / $\kappa$ mechanism). The Majorana condition removes one independent state per generation: $48-3=45$ Weyl species per sector; with conjugates, $90$. For spectral-triple computations the finite algebra is $A_F=\mathbb{O}\oplus\mathbb{O}$ (Companions 12–14). That a condition imposed for the dark sector reproduces the $J_3(\mathbb{O})$ species count is a non-trivial internal cross-consistency, not a fit.

---

## 5. What is delivered and what remains open

**Delivered (adopting prior art, conditional on NTE premises):** the gauge *group*; three generations; the species count $90$ with the independently motivated Majorana condition.

**Not delivered, not claimed.**

- *Yukawa couplings and the mass hierarchy* — three equal-weight generations; hierarchy needs a $J_3$ breaking not derived here. Yukawas inherited from observation, as in the SM (Part 3).
- *Three-generation hypercharge assignments* — single-generation hypercharges follow from octonionic multiplication (Furey 2018); the $J_3(\mathbb{O})$ extension to three generations is only partially verified — **open** (Part 3 ledger).
- *Cosmological observables* ($n_s$, $r$) — do not follow from $G_2$ representation content; they are conditional on open $K(\Phi)$ (Companion 15 §6.1: metric-only channel proven empty).
- *Technical naturalness* — see §6.

**Not helped by the octonionic reframing:** post-EWSB $\lvert\Phi_{\mathrm{NTE}}(N)\rvert$ evolution; finite $y_\nu$ correction to $\kappa_0$; Hubble-tension / $w$ phenomenology. Those are dynamical or geometric problems outside division-algebra structure.

---

## 6. Technical naturalness (open programme)

Companion 4 resolves the hierarchy problem at the classical resonance level ($\beta=1$) but does not address radiative stability. A proposed non-associative UV completion notes that $J_3(\mathbb{O})$ is alternative: $[A,A,B]=0$. With the Higgs embedded in $J_3(\mathbb{O})$, the collinear region driving the quadratic Higgs-mass divergence is where the alternative law acts. This is a **motivated programme, not a result** (Part 2 §§8.5–8.6; Part 3 open ledger). Required and not carried here: an explicit Higgs embedding, an octonionic loop (or spectral-action) formulation, and verification that the alternative law cancels the specific divergences.

Routing note (non-closing): the same spectral-triple / heat-kernel machinery that would close $K(\Phi)$ on Hopf-$S^3\times S^1_{\beta_{\mathrm{GB}}}\times A_{G_2}$ (Companions 12, 15; Farnsworth–Boyle non-associative spectral action) is the natural calculational home for this programme. Stages 0–5 and Companion 15 do **not** close it.

---

## 7. Relation to Companion 10 (Majorana spectrum)

The $\sigma_3$ Cartan-mode structural reading of the heavy-neutrino spectrum $M_1,M_2,M_3$ (Companion 10) is an $SU(2)_L$-internal statement for the observable sector. It is consistent with §3.3: $SU(2)_R$ is not part of the observable Cartan decomposition once CPN parity selection has assigned it to the conjugate sector. Explicit $M_2$ subleading splits and full Lagrangian-level vantage maps remain open where Companion 10 leaves them open.

---

## 8. Falsifiers

1. If a consistent NTE formulation required a normed division algebra other than $\mathbb{O}$, the construction fails — Hurwitz leaves none.
2. If three-generation hypercharges through $J_3(\mathbb{O})$ fail to reproduce the SM values, §4 fails at three generations (single-generation case established).
3. If $J_3(\mathbb{O})+$ Majorana gave other than 90 species, the §4.3 cross-consistency fails.

The second is the most pressing open check.

---

## 9. Accuracy note (source draft → this companion)

Desktop `Paper_OctonionExtension_v10_9.md` was checked against Parts 1–3 and Companions 1–15. Material **retained in substance:** Hurwitz → $\mathbb{O}$; $G_2$ stabiliser → $SU(3)_C$; quaternionic $S^3$ → $SU(2)_L$; CPN → $SU(2)_R$ in mirror; Cayley–Dickson / Hopf tower; $J_3(\mathbb{O})$ generations; Majorana → 90; technical naturalness as programme.

Material **corrected or dropped** relative to that draft:

| Draft claim / apparatus | Corpus status |
|---|---|
| "Gauge group derived rather than assumed" as novelty | **Adopted prior art**; conditional uniqueness only (Part 1; Part 2 §§8.5–8.6) |
| Companion 7a / chirality-superposition / δN "intrinsic-uniformity" additive ontology | **Not** in the deposited Core Papers; retired strobe / chirality-superposition language stays out |
| Programme S / Charter v1.3 / NTC issue numbers / v10.6 §VIII.7 line refs | Stale; replaced by Part 2 §§8.5–8.6, Companions 12–15 |
| §7 harmonic-oscillator fix as live content | Already integrated in Companion 3; omitted |
| Overclaim that $n_s$ is closed from G₂ content | $n_s$/$r$ conditional on $K(\Phi)$ (Part 3; Companion 15) |
| Missing Boyle–Farnsworth / Pati–Salam credit | Restored per Part 2 |

---

## References

1. A. Hurwitz, Gött. Nachr. (1898).
2. J. C. Baez, "The octonions," Bull. Amer. Math. Soc. **39**, 145 (2002).
3. M. Günaydin and F. Gürsey, "Quark structure and octonions," J. Math. Phys. **14**, 1651 (1973).
4. G. M. Dixon, *Division Algebras* (Kluwer, 1994).
5. C. Furey, Phys. Lett. B **785**, 84 (2018).
6. I. Todorov and M. Dubois-Violette, Int. J. Mod. Phys. A **33**, 1850118 (2018).
7. M. Gogberashvili, Adv. Appl. Clifford Algebras (2005) [hep-th/0409173].
8. J. Köplinger, V. Dzhunushaliev, M. Gogberashvili — non-associative quantum theory / emergent time (and related works).
9. J. C. Pati and A. Salam, Phys. Rev. D **10**, 275 (1974).
10. L. Boyle and S. Farnsworth, "The standard model, the Pati–Salam model, and 'Jordan geometry'," New J. Phys. **22**, 073023 (2020).
11. A. H. Chamseddine and A. Connes, Fortsch. Phys. **58**, 553 (2010) [arXiv:0812.0165].

---

*Companion 16 · NTE v10.19.0 · G. White · 2026-08-03*

*See also: Part 2 §§8.5–8.6; Companions 2, 3, 6, 7, 9, 10, 12, 15; Pedagogical note `Pedagogical_Notes/Paper_OctonionExtension_Pedagogical_Note_v10_19_0.md`.*
