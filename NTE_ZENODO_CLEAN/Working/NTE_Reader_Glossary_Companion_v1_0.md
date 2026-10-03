---
title: "NTE Reader Glossary Companion"
author: "G. White"
date: "2026-05-31 (v1.4 — Lagrangian/Hamiltonian + PDF)"
---

**Purpose.** Short explainers for specialist terms that recur across NTE technical papers and pedagogical pivots. Written for the general reader (Greg-first), not as a substitute for the pivots themselves.

**Voice.** Same register as pedagogical pivots: plain language, honest scope, no formal-academic stiffness. See `Working/NTE_Book_Popular_Voice_Register.md`.

**How to use.** Look up a term in the index. Longer entries carry intuition; **Symbols & identifiers** are mostly one-liners with corpus pointers. Each substantive entry ends with *Where in NTE*.

**Owner.** Cursor seeds entries from corpus usage; PC may CR or rewrite for voice; Greg ratifies additions.

---

## Index

### Concepts (longer entries)

| Term | Status |
|------|--------|
| [Kac's drum question](#kacs-drum-question-can-you-hear-the-shape-of-a-drum) | v1.1 |
| [Heat-kernel expansion](#heat-kernel-expansion-seeleydewitt-expansion) | v1.0 |
| [Heat-kernel coefficients](#heat-kernel-coefficients-a₀-a₂-a₄-) | v1.0 |
| [Spectral triple](#spectral-triple) | v1.1 |
| [Spectral action](#spectral-action) | v1.1 |
| [Dirac operator (in NTE)](#dirac-operator-in-nte) | v1.2 |
| [Trace anomaly / conformal anomaly](#trace-anomaly--conformal-anomaly) | v1.2 |
| [Action · least action · least-action equilibrium](#action--least-action--least-action-equilibrium) | v1.2 |
| [Lie group](#lie-group) | v1.2 |
| [Hopf fibration](#hopf-fibration) | v1.2 |
| [Yukawa coupling](#yukawa-coupling) | v1.2 |
| [Boson · lepton · baryon](#boson--lepton--baryon) | v1.2 |
| [E-fold number (*N*~e~)](#e-fold-number-n_e) | v1.2 |
| [Majorana neutrino](#majorana-neutrino) | v1.3 |
| [CPN · Janus · bilateral thickness](#cpn--janus--bilateral-thickness) | v1.3 |
| [PMNS · seesaw (short)](#pmns--seesaw-short) | v1.3 |
| [Killing spinor](#killing-spinor) | v1.3 |
| [Tier register (A / B+ / B)](#tier-register-a--b--b) | v1.3 |
| [Lagrangian · Hamiltonian · effective action](#lagrangian--hamiltonian--effective-action) | v1.4 |
| [Physics & maths primer (non-specialist)](#physics--maths-primer-non-specialist) | v1.4 |

### Symbols & identifiers

| Block | Jump to |
|-------|---------|
| Couplings, scales, tiers | [§ Couplings & scales](#couplings--scales) |
| Neutrino masses & Yukawas | [§ Neutrino sector](#neutrino-sector) |
| Mixing & CP | [§ Mixing & CP](#mixing--cp) |
| Cosmology & inflation | [§ Cosmology](#cosmology) |
| Curvature & heat-kernel | [§ Curvature & heat-kernel](#curvature--heat-kernel) |
| Framework fields & modular flow | [§ Framework fields](#framework-fields) |
| Gauge, algebras, operations | [§ Gauge & algebras](#gauge-groups) · [Algebras](#algebras) · [Operations](#operations) |
| Geometries & harmonics | [§ Geometries](#geometries) · [Harmonics & spinors](#harmonics--spinors) |
| Bilateral / Janus labels | [§ Bilateral structure](#bilateral-structure) |
| Predictions & falsifiers | [§ Predictions & gates](#predictions--heat-kernel-labels) · [§ Absences & tests](#absences--experimental-gates) |
| **N** disambiguation | [§ Which *N*?](#which-n) |

---

## Heat-kernel expansion (Seeley–DeWitt expansion)

**One sentence.** A standard way to unpack quantum-field calculations on a curved background into a tidy power series, term by term, each term built from curvature of the background.

**The intuition (why “heat”).** Imagine dropping a hot spot of ink on a curved sheet and watching it spread. On a flat plane the spread is symmetric; on a curved surface the geometry steers how fast diffusion runs in different directions. Mathematicians encode that spreading with a *heat kernel* — a function that solves a diffusion-type equation tied to the Laplace or Dirac operator on the space. Physicists borrowed the same machinery decades ago because it organises divergent quantum calculations in curved spacetime.

**What the expansion actually does.** Fix a background geometry (for NTE, often **S³ × S¹** plus internal algebra). Fix an operator — usually the **Dirac operator** *D* or its square *D*². Consider the trace

Tr exp(−*t D*²)

for a small positive parameter *t* (often called the **proper-time** or **heat-time** parameter). For small *t*, that trace admits an asymptotic expansion in powers of *t*:

Tr exp(−*t D*²) ~ (4π*t*)^−*d*/2 [ *a*₀ + *a*₂ *t* + *a*₄ *t*² + *a*₆ *t*³ + … ]

The labels *a*₀, *a*₂, *a*₄, … are the **heat-kernel coefficients** (also **Seeley–DeWitt coefficients** after the physicists who systematised them). Each is an integral over the background of a specific **curvature invariant** — scalar combinations of *R*, *R*~μν~, *R*~μνρσ~, and their derivatives — plus contributions from any finite internal algebra wired into *D*.

**Why physicists care.** The expansion is not decorative. In the **spectral action** programme (Connes–Chamseddine), the effective action of gravity and gauge fields on the background is assembled from these coefficients. Low orders reproduce familiar physics:

- *a*₀ → volume / cosmological-constant scale  
- *a*₂ → Einstein–Hilbert (scalar curvature) term  
- *a*₄ → curvature-squared corrections, including the **conformal trace anomaly** for fermions  

So when NTE papers talk about “what the heat kernel gives,” they mean: *which terms survive in the effective action once you expand on this fixed geometry?*

**What it is not.** The expansion evaluates on a **chosen** background; it does not, by itself, prove that nature minimised an action or “selected” that geometry from data. Vanishing or simplifying a coefficient on S³ × S¹ is a **structural** statement about that substrate — observational filtering is downstream (κ, *n*~s~, neutrino masses, clean gates).

**Standard references.** Gilkey (1984) for the coefficient formulas; Chamseddine–Connes (1996, 2008) for spectral-action use; Vassilevich (2003) for a readable QFT-on-curved-spacetime survey.

**Where in NTE.** Paper S1 (a₄ polynomial on S^*d*); Paper S2 (six-note chord from one expansion); Paper S6 (*M*~R~ from heat-kernel structure); F1 companion (a₄ decomposition on S³ × S¹); S1 and S2 pedagogical pivots § “heat-kernel.”

---

## Heat-kernel coefficients (a₀, a₂, a₄, …)

**One sentence.** The numbered terms in the heat-kernel expansion — each a packaged dose of background curvature (and internal-algebra trace weight) at a definite order in *t*.

**Naming pattern.** Subscripts count **half the power of *t*** in the standard 4D Dirac expansion: *a*₀ is the constant term, *a*₂ picks up one power of *t*, *a*₄ two powers, and so on. (There is no *a*₁ in the minimal diagonal expansion — odd powers vanish for the operators NTE uses.)

**The three orders NTE cites most often**

| Coefficient | Typical curvature content | Plain-language role in NTE |
|-------------|---------------------------|----------------------------|
| **a₀** | Volume ∫√*g* × internal trace *N*~F~ | Sets the bare cosmological-constant / volume scale (S2 Note 5) |
| **a₂** | Scalar curvature *R* | Einstein–Hilbert piece; bare Hopf coupling κ₀ = 3/√(4π) links to *a*₂ structure (S1 Finding F2, S2 Note 1) |
| **a₄** | 5*R*² − 8*R*~μν~² − 7*R*~μνρσ~² (Dirac standard weights) | Curvature-squared / trace-anomaly sector; on S³ × S¹ much of this **vanishes**, leaving a clean algebraic identity (F1, S1) |

**The a₄ combination in words.** For the squared Dirac operator on a 4-dimensional Riemannian manifold, the *a*₄ integrand has the fixed linear combination

*a*₄ ∝ 5*R*² − 8*R*~μν~² − 7*R*~μνρσ~²

with standard relative weights (5, −8, −7) from Gilkey’s formulas. The numbers are not tuned for NTE — they come from the operator. What *is* special for the programme is **what value that combination takes** on candidate geometries: on a unit *d*-sphere it factorises to *d*(*d*−1)(*d*−3)(5*d*+2), so **only *d* = 3** among integer spheres *d* ≥ 2 gives a non-trivial zero (S1). On the product **S³ × S¹**, the same combination decomposes into Weyl-squared and Euler terms that cancel pointwise — the F1 uniqueness result.

**“Vanishing a₄” — what that means.** It does **not** mean “no curvature.” It means a particular **curvature-squared package** in the spectral action expansion adds nothing on that background, so higher-order effective-action clutter drops out and downstream predictions see a cleaner spine. That is a filter on **which geometries the spectral action uses cleanly**, not a proof that CMB data picked S³.

**Where in NTE.** Same map as the expansion entry; treat “Seeley–DeWitt coefficient” as the same object.

---

## Kac's drum question ("Can you hear the shape of a drum?")

**One sentence.** Mark Kac's famous 1966 question asks whether a drum's **shape** can be recovered from the **list of tones** it can produce — and that question is the intuitive door into everything NTE calls "spectral."

**The setup.** A drumhead has a geometry (round, square, size, tension). When struck, it vibrates in modes — a fundamental tone and overtones at definite frequencies. Kac asked: if a listener heard the **full spectrum** of those frequencies, could she infer the drumhead's shape without ever seeing it?

**The answer (short version).** Not always — Gordon, Webb, and Wolpert (1992) found pairs of differently shaped drums that sound **identically**. But the counterexamples are rare. For most shapes, the vibration spectrum encodes the geometry tightly. The Pythagorean insight generalises: **shape determines sound**, and in careful mathematics the sound carries shape back.

**Why NTE cares — it's not a side anecdote.** The book's unification arc (Chapter 11) uses Kac as the **calibration schema**: physics observes "sounds" (mass ratios, κ, *n*~s~, Λ, …); the framework claims those are modes of **one geometric instrument**, not independent knobs. Connes's programme then makes that literal: when visual pictures fail (exotic or higher-dimensional geometry), you can still specify an object by the algebra of vibrations it supports — that is a **spectral triple**. The **heat-kernel expansion** is the calculational tool that turns "what tones does this instrument allow?" into curvature integrals and then into numbers.

**The chain in one line.** Kac (shape ↔ spectrum) → Connes (geometry = vibration algebra) → spectral triple (the instrument) → spectral action (the effective physics assembled from its spectrum) → heat-kernel coefficients (the term-by-term unpack).

**What it is not.** Hearing the drum is **not** the same as proving which drum nature chose from CMB data. Kac's question is about **recoverability in principle**; NTE uses it as **pedagogy**, then separates structural filtering from observational testing (see S1 companion § observational scope).

**Standard references.** Kac (1966); Gordon–Webb–Wolpert (1992) isotopy counterexamples; Book Ch 11 develops the schema at popular depth.

**Where in NTE.** `Book/Chapter_11_What_the_Universe_Sounds_Like_v3_1.md` (central); Popular Full/Reader editions; Paper S2 ("six notes of one chord"); spectral pivots throughout Programme S.

---

## Spectral triple

**One sentence.** A **spectral triple** is Connes's three-piece package — algebra, Hilbert space, Dirac operator — that describes a geometric object **through the vibrations it can sustain**, when you can't (or shouldn't) rely on a picture.

**The three pieces (Connes notation (𝒜, ℋ, *D*))**

| Piece | Plain language | Ordinary instrument | NTE canonical choice |
|-------|----------------|---------------------|----------------------|
| **𝒜 — algebra** | What kind of object, what symmetries | "A string" vs "a drumhead" | Smooth functions on **S³ × S¹** ⊗ finite algebra **𝕆 ⊕ 𝕆** (two octonion copies) |
| **ℋ — Hilbert space** | Catalogue of all vibration patterns the object can hold | Fundamental + overtones | Spinors on the base × 180-dimensional finite sector (*N*~F~ = 180) |
| ***D* — Dirac operator** | Rule for how vibrations propagate and at what "pitch" | Wave equation along the string | Product Dirac on S³ × S¹, tensored with finite algebra, plus Higgs-portal coupling |

Specify all three and the **spectrum** of *D* (its allowed modes and frequencies) is determined — Kac's idea made rigorous. The name *spectral* refers to that spectrum; *triple* because three independent inputs are required.

**NTE's canonical triple (Paper S2).** Base **M = S³ × S¹** (Hopf 3-sphere × temporal circle at gauge-birth scale); finite algebra **A**~F~ = **𝕆 ⊕ 𝕆** (bilateral octonionic internal structure); **D** the standard product Dirac extended to the finite sector. This triple is **fixed by programme commitments**, not tuned per prediction — S2 checks that six observables emerge from **one** heat-kernel expansion on **this one** triple.

**Relation to the book.** Chapter 11 names the three pieces as "what kind of object," "space of vibrations," and "how vibrations propagate," then calls the package a spectral triple and the universe a particular instance — the **universe-instrument**.

**What it is not.** A spectral triple is a **mathematical specification**, not an observational fit. Fixing it is a structural commitment; testing it is downstream (κ, *n*~s~, neutrinos, clean gates).

**Standard references.** Connes (*Noncommutative Geometry*); Chamseddine–Connes spectral-action papers; Landi for pedagogy; Book Ch 11 for intuition.

**Where in NTE.** Paper S2 § spectral triple; Paper Kappa A+B (S³ substrate); OctonionExtension (𝕆 ⊕ 𝕆 algebra); Hopf bare-coupling pivot; S1 observational-scope chain ("once the programme fixes the spectral triple…"); Book Ch 11–12.

---

## Spectral action

**One sentence.** The **spectral action** is the Connes–Chamseddine recipe that turns the spectrum of the Dirac operator *D* into an effective action for gravity and gauge physics — assembled from the same heat-kernel expansion the glossary already introduced.

**The idea in steps.**

1. **Start with a spectral triple** (𝒜, ℋ, *D*) — the instrument is specified.  
2. **Form a functional** of *D*, schematically Tr *f*(*D*²/Λ²), where Λ is a high-energy cutoff (Planck scale in cosmological applications) and *f* is a smooth weight function.  
3. **Expand** that trace for large Λ using the **heat-kernel expansion** of exp(−*t D*²).  
4. **Read off** low-order **Seeley–DeWitt coefficients** *a*₀, *a*₂, *a*₄, … as terms in an effective action: volume/cosmological constant (*a*₀), Einstein–Hilbert (*a*₂), curvature-squared / trace-anomaly sector (*a*₄), etc.

So the spectral action is where "what tones does *D* allow?" becomes "what Lagrangian does the geometry induce?" — without inserting a separate gravitational action by hand.

**Why NTE keeps saying "spectral action prefers S³ × S¹".** Chamseddine–Connes (2008) showed that on **S³ × S¹** several heat-kernel contributions **cancel** (notably in the *a*₄ sector — see F1 and S1). Mistry–Pinzul–Rachwał (2020) stressed that this cancellation is **not** generic for all backgrounds; it happens for the **coefficients fixed by the spectral action** on this product. NTE reads that as a **structural filter**: among candidate substrates, S³ × S¹ is where the spectral action expansion is unusually clean — then separate papers extract numbers.

**What it is not.**

- **Not** a proof that nature minimised this action. The expansion is evaluated on a **chosen** background.  
- **Not** the same as the everyday word "action" in "least action" — no dynamical extremum is assumed when S1 checks vanishing *a*₄.  
- **Not** a substitute for data: the spectral action organises **structure**; observation still tests predictions (S2 chord, clean gates).

**Standard references.** Chamseddine–Connes (1996, 2008); Gilkey + Vassilevich for heat-kernel side; Boyle–Farnsworth octonionic specialisation cited in S1.

**Where in NTE.** Paper S1 (title + a₄ polynomial); Paper S2 (central computation); F1 (a₄ uniqueness on S³ × S¹); S6 (*M*~R~ from heat-kernel orders); Chamseddine–Connes outreach in Distribution Campaign §6.1; Book Ch 12 chord; Popular Full Edition § chord closure.

---

## Dirac operator (in NTE)

**One sentence.** The **Dirac operator** *D* is the third leg of the spectral triple — the rule that turns geometry into allowed fermion modes and their propagation speeds.

**Plain language.** Fermions (electrons, quarks, neutrinos) aren't just points; in quantum field theory they're described by **spinors**. The Dirac operator is the differential operator that generalises the gradient to spinors on curved space — it encodes how those modes move and what "mass" and "kinetic energy" mean on the background. Its **spectrum** (eigenvalues) is the precise mathematical version of Kac's drum tones.

**In NTE.** On the canonical triple, *D* = product Dirac on **S³ × S¹** ⊗ finite algebra **𝕆 ⊕ 𝕆**, with a Higgs-portal coupling between continuous and internal sectors. **Everything Programme S extracts** — κ₀, inflation sector, Λ closure, neutrino scales — comes from heat-kernel expansions of *D*² (or related traces), not from a separately postulated Lagrangian.

**What it is not.** Specifying *D* on a fixed background is **not** solving for the path history that minimises an action. NTE evaluates expansion coefficients on the chosen substrate; dynamics is a separate layer.

**Where in NTE.** Paper S2 § Dirac operator + Lichnerowicz; spectral triple entry above; Book Ch 11 ("how vibrations propagate"); OctonionExtension (finite-sector extension).

---

## Trace anomaly / conformal anomaly

**One sentence.** A **trace anomaly** is an extra curvature term quantum field theory injects when you try to scale a theory on curved space — and on most backgrounds it's messy; on **S³ × S¹** much of it **vanishes**.

**Plain language.** Classically, scaling all lengths by a constant might seem to leave physics unchanged (conformal symmetry). Quantum corrections break that on curved backgrounds. The breaking shows up as specific **curvature-squared** packages in heat-kernel coefficients — the same *a*₄ sector as F₁ = 5*R*² − 8*R*~μν~² − 7*R*~μνρσ~², re-expressed as −18*C*² + 11*E*₄.

**Why NTE cares.** On a generic 4-manifold you carry anomaly clutter through every spectral-action step. On **S³ × S¹**, *C*² and *E*₄ are zero pointwise, so F₁ vanishes identically — the "shape where the anomaly vanishes" (F1 pivot title). That cleanliness is a **structural filter**, not observational proof.

**Where in NTE.** F1 pivot + paper; S1 a₄ polynomial; S2 § a₄ / F₁ reinterpretation; Paper S2 consolidation § trace-anomaly normalisation.

---

## Action · least action · least-action equilibrium

**Action (general).** An **action** is a number assigned to a field configuration (or history). Varying it yields the equations of motion — the usual Lagrangian/Hamiltonian machinery of physics.

**Least action (classical).** **Least action** (more precisely: **stationary action**) is the principle that classical paths make the action extremal — δ*S* = 0. It's how you recover Newton's laws, Maxwell's equations, Einstein's equations from one functional.

**Spectral action (NTE-specific).** The **spectral action** is a *particular* action built from Tr *f*(*D*²/Λ²) — see [spectral action](#spectral-action). It is **not** the same word used in everyday "the universe took the path of least action."

**Least-action equilibrium (misread to avoid).** NTE papers repeatedly warn: **vanishing *a*₄ on S³ × S¹ does not mean nature sits in a least-action equilibrium** or that the universe "chose" that geometry by minimising *S*. The heat-kernel expansion is evaluated on a **fixed** background; cancellation means a term drops out of the expansion — not that dynamics extremised anything.

**Janus action (related).** The bilateral **Janus action** is a separate constructive step for cross-thickness gravity (κ resummation); it closes a gap Ch 9 once named. Still not the same as "spectral action prefers S³ × S¹."

**Where in NTE.** S1 pivot § observational scope; spectral action entry; Book Ch 9 (Gap 4b / Janus); Kappa A+B pivot; Ch 12 (Janus closes foundations).

---

## Lie group

**One sentence.** A **Lie group** is a symmetry set that is also a smooth geometric object — you can multiply group elements and differentiate the multiplication.

**Intuition.** Rotations in 3D form a Lie group (SO(3)). The unit **quaternions** form a Lie group that is the same as **SU(2)** — and NTE's spatial **S³** is exactly that group manifold. So "S³ is a Lie group" is one independent reason the 3-sphere is structurally special: it is not just a round shell; it carries compatible group structure (parallelisable, Hopf map, etc.).

**Where in NTE.** S1 pivot (parallelisability, Lie-group uniqueness); Octonion pivot (G₂, SU(2)_L from quaternions); Book Ch 6–7; Companion 2 (Hopf / state space).

---

## Hopf fibration

**One sentence.** The **Hopf fibration** is a way to decompose **S³** as a bundle of circles **S¹** over a base **S²** — each point on the 2-sphere carries a whole circle of points in the 3-sphere above it.

**Intuition.** Quantum **phase** lives on a circle; observable probabilities live on a 2-sphere after quotienting phase — that's the Hopf picture behind the Born rule in NTE (Ch 6). The fibration also threads **gauge-birth** structure: temporal **S¹** as Hopf fibre, monopole harmonic on **S²** base giving κ₀.

**Adams constraint.** Non-trivial Hopf fibrations S^*d* → S^*d*−1 exist only for *d* ∈ {1, 3, 7}. Only **d = 3** also satisfies S1's spectral cancellation — a correlation S1 names explicitly.

**Where in NTE.** Book Ch 6; Companion 2; Hopf bare-coupling pivot; Kappa pivot; S1 § Hopf + cancellation; Octonion pivot (Hopf tower / Cayley–Dickson).

---

## Yukawa coupling

**One sentence.** A **Yukawa coupling** is the dimensionless strength that tells a scalar (usually the Higgs) how strongly to give mass to a fermion — in the Standard Model these numbers are **measured**, not derived.

**In NTE.** The framework claims **ratios and structural slots** (e.g. solar *m*~ν2~ at ~0.993× observation via Companion 13) but is **honest that most Yukawa magnitudes are still inherited** like the SM — Octonion pivot lists this as open work. Yukawa is the right word whenever a paper ties fermion mass to a coupling constant rather than a raw mass insert.

**Where in NTE.** Companion 13; Paper P5 (solar neutrino); Octonion pivot § limits; S2 pivot (charged-lepton absolute scale open); Appendix A / Popular editions.

---

## Boson · lepton · baryon

**Boson** — particle with integer spin; force carriers (photon, *W*, *Z*, gluons) and the Higgs. NTE uses "bosonic spectral action" for the gravity/gauge sector assembled from heat-kernel traces.

**Lepton** — spin-½ matter particle without strong charge: electron, muon, tau, neutrinos. NTE's unresolved **Majorana neutrino** bridges bilateral thickness → dark matter (Ch 8–9).

**Baryon** — composite made of three quarks (protons, neutrons). **Baryon number** tracks ordinary matter; **κ ≈ 5.50** is the predicted dark-to-**baryon** density ratio.

**Where in NTE.** Book Ch 7–9; Kappa pivot; Clean Gates pivot; Appendix A particle table.

---

## E-fold number (*N*~e~)

**One sentence.** **E-folds** count how many times the universe stretched by a factor *e* during inflation; **N**~e~ (or *N*~e~) is that count to a defined exit surface — in NTE, tied to gauge birth / lock scale.

**Why it matters here.** Hilltop inflation gives *n*~s~ ≈ 1 − 2/*N*~e~; NTE lands *n*~s~ ≈ 0.9685. The **same *N*~e~** also enters the Λ closure Λ_NTE ∝ *e*^(−3*N*~e~)/(2π²) — one depth parameter, two predictions (S2 Note 3 & 5). Don't confuse *N*~e~ with *N*~lock~ (holographic locking width) or thermal scales at gauge birth (Popular § three clocks).

**Where in NTE.** S2 pivot Notes 3 & 5; Paper S2 §6–7; Companion 11 (Λ); Clean Gates pivot (*n*~s~ gate); Popular Full Edition § three clocks.

---

## Majorana neutrino

**One sentence.** A **Majorana neutrino** is its own antiparticle — and in NTE that incomplete "Hopf lock" is what lets the neutrino bridge bilateral thickness and mediate cross-orientation gravity (dark matter).

**Corpus discipline.** Majorana status is a **structural commitment** (not fitted for κ); test: neutrinoless double-beta decay (0νββ). If neutrinos are strictly Dirac, the bilateral dark-matter reading must be rebuilt.

**Where in NTE.** Book Ch 8–9; Octonion pivot (90-species count); S6 / P5 / P4; Clean Gates; Ch 15 (0νββ in inverted hierarchy).

---

## CPN · Janus · bilateral thickness

**CPN** — charge–parity–orientation conjugation relating the two faces of one thickened manifold (+N / −N sectors); not two separate universes glued at an edge.

**Janus boundary** — the shared surface at **N = 0** (e-fold / thickness coordinate) where orientations meet; distinct from gauge birth **t = 0** (time switch-on).

**Janus action** — bi-metric action reproducing κ = κ₀/(1−κ₀); closes Gap 4b (cross-thickness gravity had equations before; now an action).

**Where in NTE.** Book Ch 7, 9–10, 12; Kappa A+B pivot; Popular Reader § bilateral; OctonionExtension (𝕆 ⊕ 𝕆 sectors).

---

## PMNS · seesaw (short)

**PMNS matrix** — unitary matrix governing how flavour neutrinos (electron / muon / tau) mix during propagation; three angles *θ*~12~, *θ*~13~, *θ*~23~ plus CP phases.

**Seesaw** — light neutrino mass scales as *m*~ν~ ~ *Y*²*v*²/*M*~R~ with heavy Majorana scale *M*~R~; NTE **derives *M*~R~** (S6) and several *Y* / *m* slots rather than fitting them freely.

**Where in NTE.** P4 pivot (*θ*~23~ = 45°); P5 / Companion 13 (*m*~ν2~); S6 (*M*~R~, *m*~ν3~); Clean Gates Tier 1; Ch 15.

---

## Killing spinor

**One sentence.** A **Killing spinor** is a spinor field preserved by the geometry's symmetries — on **S³**, constant Killing spinors project through the Hopf map to the monopole harmonic *Y*₀₀, giving κ₀ = 3/√(4π).

**Where in NTE.** Hopf bare-coupling pivot; S6 (σ-projection); Companion 10 / Pathway α; Paper S2 § Killing-spinor spectrum on S³.

---

## Tier register (A / B+ / B)

**Tier A (clean)** — zero-parameter structural prediction; no observational dial in the derivation chain (*n*~s~, κ after resummation stated separately, *m*~ν2~ at 0.993×, *θ*~23~ leading order).

**Tier B+** — genuine structural test but **β_NTE-chain caveat** (Λ, *H*₀ partly anchored through Ω_Λ → β_NTE).

**Tier B** — framework-dependent identification or confluence tier (*M*~R~ cross-checks, some mass-scale slots).

**Where in NTE.** S2 pivot § honest scope; Clean Gates tiers; Ch 15; Companion 11; ledger `NTE_Chapter_State_Ledger.md`.

---

## Lagrangian · Hamiltonian · effective action

**Lagrangian.** A function (usually **Lagrangian density** *L* integrated over spacetime) that encodes the dynamics of fields and particles. You plug fields into *L*; varying the resulting **action** *S* = ∫*L* √*g* d⁴*x* gives the equations of motion. The Standard Model is normally written as a Lagrangian before anyone computes anything.

**Hamiltonian.** The energy-bookkeeping picture paired with the Lagrangian — often written **H** for the Hamiltonian operator or energy function. In quantum theory, **H** generates time evolution (Schrödinger equation). NTE's cosmological **H** (Hubble rate) is a different use of the letter: *H* = α\|Φ_NTE\|² links expansion to the boundary field — not the same object as the SM Hamiltonian, though both sit in "how things evolve."

**Effective action.** The action that **actually runs** at a given energy scale after quantum corrections and coarse-graining. The **spectral action** is one way to build an effective action from *D*; heat-kernel coefficients are the term-by-term expansion of that action on a fixed geometry.

**Chain in NTE.** Spectral triple → spectral **action** (from Tr *f*(*D*²/Λ²)) → heat-kernel expansion → Einstein–Hilbert (*a*₂), anomaly (*a*₄), etc. Papers say "Lagrangian" when they mean the SM sector written in field-theory language; "action" when integrating or varying; "spectral action" for the Connes–Chamseddine construction.

**Where in NTE.** Octonion pivot (SM Lagrangian input); S2 (*a*₂ as Einstein–Hilbert piece); [Action · least action](#action--least-action--least-action-equilibrium) entry; Book Ch 11–12.

---

## Physics & maths primer (non-specialist)

*Short entries for vocabulary that appears constantly but is rarely defined in the corpus. Symbols with dedicated rows live in the [symbol index](#symbols--identifiers) below.*

### Space, geometry, topology

**Manifold** — a space that looks locally like ordinary flat *n*-dimensional space but can curve globally (sphere, torus, S³×S¹). NTE's "universe-instrument" is a manifold plus internal algebra data.

**Riemannian metric** — the rule for measuring distances and angles on a manifold; determines curvature. "Round" S³ uses the standard unit-sphere metric.

**Topology** — global shape properties unchanged by smooth stretching (holes, handles, connectedness). **Euler characteristic** is a topological invariant; **Euler density** *E*₄ is its local curvature representative (F1 entry).

**Quotient / quotienting** — identifying points related by a symmetry. Hopf map **quotients phase** on S³ to probabilities on S² (Born rule, Ch 6).

**Parallelisable** — a manifold whose tangent directions can be aligned globally without singularities; S³ is parallelisable — one reason it is special (S1 pivot).

**Conformally flat** — a geometry that can be rescaled to flat space; S³×S¹ is conformally flat but F1 cancellation does **not** extend to all such spaces (Mistry–Pinzul–Rachwał 2020).

### Quantum & fields

**Spinor** — mathematical object for spin-½ particles (electrons, quarks, neutrinos); needs 720° rotation to return to itself on S³. **Killing spinors** are geometry-covariant spinors on S³ (Hopf / κ₀ route).

**Hilbert space** — complex vector space of quantum states with inner products; **ℋ** in a spectral triple lists allowed vibration patterns (Book Ch 11).

**Gauge symmetry** — redundant labelling of fields that leaves physics unchanged; local gauge symmetry forces force-carrying **gauge bosons**. **Gauge birth** — NTE's transition when SM SU(3)×SU(2)×U(1) locks in at *t* = 0 (Octonion pivot, Book Ch 7).

**Effective field theory (EFT)** — physics at one energy scale organised order-by-order in a controlled expansion; κ derivation assumes EFT validity (Ch 9).

**Spectrum / eigenvalue / mode** — allowed "tones" of an operator; Kac's drum question made rigorous. Dirac **eigenvalues** are mass/momentum scales in the spectral picture.

**Proper time** — parameter *t* in Tr exp(−*tD*²); heat-kernel expansion is for small *t* (not necessarily clock time).

**Wick rotation / modular flow** — standard (Wick) vs NTE (σ_t **KMS modular flow**) ways to relate quantum states to thermal/analytic continuation; Paper S1 replaces Wick with σ_t framing.

**Born rule** — probability = squared amplitude, **P = |overlap(ψ, φ)|²**; in NTE, the unique symmetric choice on S² after Hopf quotient (Companion 2, Ch 6).

**Entanglement** — correlations between systems with no classical joint state; Bell tests and BMV gravity–entanglement (Clean Gates Tier 2).

### Particles & Standard Model

**Standard Model (SM)** — established quantum field theory of known particles and forces (excluding gravity). NTE **extends** SM with \|Φ_NTE\| and bilateral geometry; gauge group derived in Octonion pivot.

**Higgs / VEV** — scalar field whose **vacuum expectation value** *v*~EW~ ≈ 246 GeV sets electroweak mass scale; distinct from boundary field **Φ_NTE**.

**Weak isospin / hypercharge** — quantum numbers labelling SU(2)_L and U(1)_Y reps; SU(2)_L tied to quaternionic S³ in NTE.

**Flavour vs mass eigenstate** — neutrinos propagate as mass states ν₁, ν₂, ν₃ but are produced in flavour (ν_e, ν_μ, ν_τ); **PMNS** mixes them (P4 pivot).

**Neutrino oscillation** — flavour changing with distance as mass states interfere; mixing angles *θ*~12,13,23~ are Tier 1 gates.

### Cosmology

**Inflation** — early rapid expansion stretching quantum ripples to cosmic size; NTE **hilltop** reading gives *n*~s~, *r* from one *N*~e~.

**CMB** — cosmic microwave background; snapshot of primordial **scalar perturbations** (density/temperature ripples) — tests *n*~s~, *r*, κ.

**Slow-roll** — inflation condition where field rolls gradually; hilltop *n*~s~ ≈ 1 − 2/*N*~e~ is a slow-roll formula.

**Unimodular gravity** — way to treat cosmological constant / volume constraint; Λ closure in Companion 11 uses unimodular projection.

### Algebra & structure (corpus-specific)

**Normed division algebra** — algebra with norm and division (ℝ, ℂ, ℍ, 𝕆 only — **Hurwitz**). Pre-temporal 𝕆 forced before time (Octonion).

**Cayley–Dickson sequence** — construction doubling algebras ℝ→ℂ→ℍ→𝕆; reversed as cosmic epochs in Octonion pivot.

**Associativity transition** — 𝕆→ℍ when causal time forces multiplication order to matter (gauge birth).

**Jordan algebra** — commutative but non-associative product; **J₃(𝕆)** carries three generations.

**Stabiliser** — subgroup fixing a chosen direction; Higgs direction's stabiliser in G₂ is **SU(3)**.

**Technical naturalness** — programme to explain small ratios without fine-tuning; octonionic alternative law in Octonion §6 (open).

### One-line corpus terms

| Term | One line |
|------|----------|
| **Einstein–Hilbert** | Gravity term ∝ ∫*R*√*g* — the *a*₂ piece of spectral action. → S2 |
| **Lichnerowicz formula** | Standard identity linking *D*² to curvature for Dirac operators; S2 §3 heat-kernel spine. |
| **Instanton** | Non-trivial vacuum tunneling config; Sonner–Tong route to κ₀. → Hopf pivot |
| **Monopole** | Magnetic monopole / s-wave **Y**~00~ on S² base; κ₀ projection. → Hopf pivot |
| **GNS representation** | Builds Hilbert space + operators from an algebra state; finite algebra in heat kernel. |
| **Renormalisation** | Systematic removal of infinities in QFT; trace **anomaly** is the curved-space residue. |
| **CKM matrix** | Quark mixing matrix; Cabibbo angle partly in corpus — full CKM open (master §22.3). |
| **Chirality / handedness** | Left- vs right-handed particle components; SU(2)_L and bilateral CPN structure. |
| **Falsifier / gate** | Observation that would break the framework; Clean Gates catalogue. |
| **Chords / six notes** | Metaphor for six predictions from one S2 heat-kernel computation. → Ch 12 |
| **Null-time / NTE** | Null-Time Extension — framework name; photon on boundary, time emergent. |
| **Programme S** | Spectral-action computational arc (S1, S2, S6, …). |
| **Tier 0 / 1 / 2 / 3** | Document epistemic tiers in standalone register — distinct from prediction Tier A/B+. |

**Where in NTE.** Book Ch 1–12; Appendix A; pedagogical pivots; Popular editions — follow row links for load-bearing uses.

---

## Symbols & identifiers

*One line each unless noted. Corpus links are the deep dive.*

### Which *N*?

| Symbol | Meaning |
|--------|---------|
| ***N*~e~** | Inflation **e-fold** count to lock / gauge birth — fixes *n*~s~, enters Λ. → [E-fold entry](#e-fold-number-n_e) |
| ***N*~lock~** | Holographic **locking width** ≈ 0.1 (crystallisation register) — **not** *N*~e~. → Companion 9, master §22 |
| **N = 0** | **Janus boundary** in thickness coordinate (bilateral seam) — **not** e-fold count. → Book Ch 9–10 |
| **+N / −N** | CPN-conjugate **orientation labels** on the bilateral manifold. → OctonionExtension, Ch 7 |

### Couplings & scales

| Symbol | Meaning in NTE |
|--------|------------------|
| **κ₀** | Bare cross-thickness coupling ≈ 3/√(4π) ≈ 0.846 from Hopf / heat-kernel *a*₂ — **not** the observed dark-matter ratio. → Hopf pivot, S2 Note 1 |
| **κ** | Dark-to-**baryon** ratio ≈ κ₀/(1−κ₀) ≈ **5.50** after bilateral resummation (Janus / Kappa A+B). → Book Ch 9, Kappa pivot |
| **ξ** | **Conformal coupling** = **1/6** (programme commitment; Einstein-frame *n*~s~ corrections ~10⁻⁴). → Paper S1 §2, S2 §6.4 |
| **ξ_V** | **Volume-matching** factor √(2π)/*M*~Pl~ in NCG normalisation — **not** κ₀. → OctonionExtension v10.9 §6 |
| **α_em** | Electromagnetic **fine-structure constant** ≈ 1/137; measured SM input in g_eff·α_em coincidence (Part 1 §2.4.2). → Part 1, Part 3 |
| **β_NTE** | Cosmological H-coefficient in **H = β_NTE \|Φ_NTE\|²** (≈ 2.38×10⁻⁴⁷ GeV⁻¹); partly **anchored through Ω_Λ** (β_NTE-chain caveat). → Companion 11, S2 Note 5 |
| ***M*~Pl~**, ***M*~Pl,nr~** | Planck mass (non-reduced *M*~Pl,nr~ in thermal identifications). → S6, S2, β_GB |
| ***N*~F~** | Finite-algebra trace dimension = **180** (90 species × 2 CPN sectors). → S2 §2 |
| **(8π)^1/3**, **(8π)^−1/3** | Cube-root / dual cube-root prefactors for *M*~1~ / *Y*~ν2~ (Pathway α / D5). → Companion 10, 13, P5 |
| **Tier A / B+ / B** | Epistemic rigour labels for predictions. → [Tier register](#tier-register-a--b--b) |
| **β_NTE-chain** | Loop where Ω_Λ feeds β_NTE anchoring upstream of Λ prediction — names honest caveat. → Companion 11 |

### Neutrino sector

| Symbol | Meaning in NTE |
|--------|------------------|
| ***M*~R~** | Heavy right-handed Majorana scale ≈ 8.2×10¹⁴ GeV; *M*~R~⁴ = *M*~Pl~³ × *v*~EW~. → S6 pivot, Ch 15 |
| ***M*~1~**, ***M*~2~** | Lighter Majorana scales in seesaw ladder; *M*~1~ ≈ 5.4×10⁹ GeV from (8π)^1/3 anchor. → S2 Note 4, Companion 10 |
| ***m*~ν1~, *m*~ν2~, *m*~ν3~** | Light neutrino masses; *m*~ν3~ ≈ 0.0738 eV (atmospheric); *m*~ν2~ ≈ 0.0086 eV (0.993× solar). → P5, S6, Companion 13 |
| ***Y*~ν1~, *Y*~ν2~, *Y*~3~** | Dirac Yukawa couplings in seesaw; *Y*~ν2~ = (8π)^−1/3; *Y*~3~ = 1 (Cartan-aligned). → P5, S6 |
| ***v*~EW~**, **v** | Higgs vacuum expectation value ≈ **246 GeV**. → S6, seesaw formulas |
| **Δ*m*²_solar**, **Δ*m*²_atm** | Squared mass-splitting observables; framework targets via *m*~ν2~, *m*~ν3~. → P5, oscillation gates |
| ***m*~ββ~** | Effective Majorana mass for 0νββ; specific NTE band still research target. → Clean Gates, master §19 |
| **0νββ** | Neutrinoless double-beta decay — Majorana falsifier. → Ch 15, Clean Gates |

### Mixing & CP

| Symbol | Meaning in NTE |
|--------|------------------|
| **PMNS** | Neutrino mixing matrix (flavour ↔ mass). → P4, Clean Gates |
| ***θ*~12~, *θ*~13~, *θ*~23~** | Mixing angles; leading *θ*~23~ = **45°** (π/4); sin²*θ*~12~ → **1/3** at leading order. → P4, Popular, Ch 15 |
| **δ_J**, **Jarlskog** | Leptonic CP invariant; Tier 1 prediction **±π/2** (maximal). → Clean Gates, Popular |
| **δ_CP** | CP phase in PMNS; DUNE target. → Clean Gates |

### Cosmology

| Symbol | Meaning in NTE |
|--------|------------------|
| ***n*~s~** | Primordial scalar spectral index ≈ **0.9685** (hilltop: 1 − 2/*N*~e~). → S2, Clean Gates |
| ***r*** | Tensor-to-scalar ratio ≈ **4×10⁻³**; linked to same inflation sector as *n*~s~. → S2 Note 3 |
| **Λ**, **Λ_obs**, **Λ_NTE** | Cosmological constant / dark energy; Λ_NTE ≈ **1.05×** Λ_obs. → Companion 11, S2 Note 5 |
| **Λ_*a*₄** | Raw *a*₄ residual before unimodular projection / volume measure. → S2 §7 |
| ***H*~0~** | Hubble constant; framework cosmic-mean ≈ **67.6 km/s/Mpc** (β_NTE-chain family with Λ). → Popular, Ch 15 |
| **Ω_Λ**, **Ω_m** | Dark-energy / matter density fractions; Ω_Λ enters β_NTE anchoring. → Companion 11 |
| **w** | Dark-energy equation of state; **w = −1** at leading order; Tier 2: slightly **> −1** at low *z*. → Clean Gates |
| ***T*~GB~** | Gauge-birth thermal scale *M*~Pl,nr~/√(2π) ≈ 10³² K scale. → S2 Note 2, Companion 9 |
| **β_GB** | Temporal **S¹** circumference √2π/*M*~Pl,nr~; inverse of *T*~GB~. → Paper S2 §2 |
| ***V*~lock~** | Comoving lock volume **2π² × e^(3*N*~e~)**. → S2 §7, Λ closure |
| **Vol(S³) = 2π²** | Unit 3-sphere volume; audit ratio with *V*~lock~ and Λ denominator. → S2 Note 6 |
| **η** | Baryon asymmetry magnitude ~6×10⁻¹⁰; sign from Janus δ_J = π/2. → Popular, Ch 15 |
| ***K*(Φ)** | Inflation kinetic term; **K(Φ) = 1** at leading heat-kernel order on canonical substrate. → S2 §6 |

### Curvature & heat-kernel

| Symbol | Meaning in NTE |
|--------|------------------|
| ***a*₀, *a*₂, *a*₄, *a*₆…** | Seeley–DeWitt / heat-kernel coefficients. → [Heat-kernel entries](#heat-kernel-coefficients-a₀-a₂-a₄-) |
| ***R*, *R*~μν~, *R*~μνρσ~** | Ricci scalar, tensor, Riemann — curvature ingredients in *a*₄. → S1 |
| ***C*, *C*²** | Weyl tensor / Weyl-squared (shape-distorting curvature). **Zero** on S³×S¹. → F1 pivot |
| ***E*₄** | Euler density (4D topological curvature integrand). **Zero** on S³×S¹. → F1 pivot |
| **F₁** | Trace-anomaly combination 5*R*² − 8*R*~μν~² − 7*R*~μνρσ~² = −18*C*² + 11*E*₄. → F1, S1, S2 |
| **Tr exp(−*tD*²)** | Heat-kernel trace whose expansion yields *a*~2*k~*. → [Heat-kernel expansion](#heat-kernel-expansion-seeleydewitt-expansion) |
| **Λ_cutoff** | Spectral action cutoff scale (~Planck). → [Spectral action](#spectral-action) |

### Framework fields

| Symbol | Meaning in NTE |
|--------|------------------|
| **\|Φ_NTE\|**, **Φ_NTE** | Boundary **expansion field**; *H* = α\|Φ\|². Distinct from SM Higgs. → Book Ch 1–3 |
| **σ_t** | Modular / KMS flow parameter replacing Wick rotation in NTE state framing. → Paper S1, master P0.10 |
| **KMS** | Kubo–Martin–Schwinger thermal equilibrium condition; σ_t modular flow. → Paper S1 |
| **H = α\|Φ\|²** | Hubble–expansion link to boundary field strength. → Book early chapters |

### Gauge groups

| Symbol | Meaning in NTE |
|--------|------------------|
| **U(1)** | Circle phase → electromagnetism; Hopf **fibre**. → Octonion pivot, Ch 6 |
| **SU(2)**, **SU(2)_L** | Weak isospin = unit quaternions / **S³** geometry. → Octonion pivot |
| **SU(3)** | Colour force; stabiliser of Higgs direction in **G₂**. → Octonion pivot |
| **G₂** | Aut(𝕆); 14D exceptional Lie group; breaks at gauge birth. → Octonion pivot |
| **su(2)**, **dim(adj) = 3** | Lie algebra of SU(2); three Killing-spinor channels → factor **3** in κ₀. → Hopf pivot |

### Algebras

| Symbol | Meaning in NTE |
|--------|------------------|
| **ℝ, ℂ, ℍ, 𝕆** | Cayley–Dickson tower: reals → complex → quaternions → octonions. → Octonion pivot |
| ***J*₃(𝕆)** | 3×3 Hermitian octonionic matrices; **3 generations**, 27D. → Octonion pivot |
| **Aut(𝕆) = G₂** | Symmetry of octonion multiplication. → Octonion pivot |
| **ℂ ⊗ 𝕆** | Single-generation template before *J*₃ lift. → OctonionExtension |
| **A_F** | Finite algebra **𝕆 ⊕ 𝕆** in spectral triple. → S2 §2 |
| **𝒜, ℋ, *D*** | Spectral triple algebra, Hilbert space, Dirac operator. → [Spectral triple](#spectral-triple) |
| **ℤ₂** | Two-valued exchange symmetries (e.g. P4 *θ*~23~ forcing). → P4 paper |

### Operations

| Symbol | Meaning in NTE |
|--------|------------------|
| **⊗** | Tensor product — geometry ⊗ internal sector (e.g. *D*~M~ ⊗ 1). |
| **⊕** | Direct sum — mirror copies **𝕆 ⊕ 𝕆**, Hilbert sectors **ℋ^(+N) ⊕ ℋ^(−N)**. |
| **×** (product manifold) | e.g. **S³ × S¹** with product metric. |

### Geometries

| Symbol | Meaning in NTE |
|--------|------------------|
| **S^d** | Unit *d*-sphere; S1 pivot polynomial in *d*. → S1 |
| **S³, S², S¹** | Spatial geometry; Hopf base; fibre / time circle. → Hopf entry |
| **S³ × S¹**, **M** | Canonical 4D spectral-action background. → S2, F1 |
| **Hopf-S³** | S³ with Hopf bundle structure (not just round sphere). → S2, Hopf papers |
| **M^ℂ** | Compactified Minkowski alias S¹×S³ topology. → Paper S2 §2 |

### Harmonics & spinors

| Symbol | Meaning in NTE |
|--------|------------------|
| ***Y*~ℓm~**, ***Y*~00~** | Spherical harmonics; *Y*~00~ = 1/√(4π) monopole / s-wave. → Hopf pivot |
| **Gaunt coefficient** | Integral of three harmonics; trivial for *Y*~00~ → κ₀ protected. → Hopf pivot |
| **Killing spinor** | Geometry-covariant spinor on S³. → [Killing spinor entry](#killing-spinor) |
| **Weyl spinor / species** | 16 Weyl d.o.f. per generation; 90 per sector with Majorana removal. → Octonion pivot |
| **BPS** | Bound saturating soliton state; (8π)^1/3 prefactor tier. → Companion 10, D5 notes |

### Bilateral structure

| Symbol | Meaning in NTE |
|--------|------------------|
| **CPN** | Charge–parity–orientation conjugation between manifold faces. → [CPN entry](#cpn--janus--bilateral-thickness) |
| **Janus** | Boundary at N=0; **Janus action** for κ resummation. → Kappa, Ch 9–12 |
| **+N / −N** | Bilateral orientation sectors in **A_F = 𝕆 ⊕ 𝕆**. → OctonionExtension |
| **T⁺, T⁻** | Stress-energy on each orientation; cross-coupled with κ₀. → Kappa pivot |
| **Pathway A / B** | κ closure (A: Janus resummation) vs bare κ₀ route (B: Hopf monopole). → Kappa, S2 |

### Predictions & heat-kernel labels

| Symbol | Meaning in NTE |
|--------|------------------|
| ***n*~s~, *r*, κ, Λ, *m*~ν2~, *θ*~23~, δ_J** | Tier 1 clean gates (five sharpest + δ_J). → Clean Gates pivot |
| **BMV** | Bose–Marletto–Vedral gravity–entanglement test (Tier 2). → Clean Gates, Ch 16 |
| **void / DESI *H*~0~ bias** | Tier 2: local *H*~0~ vs void sightlines. → Clean Gates, Book void chapters |

### Absences & experimental gates

| Symbol / term | Meaning in NTE |
|--------|------------------|
| **WIMP** | Cold dark-matter particle — framework predicts **none** (cross-thickness gravity instead). → Ch 10, Popular |
| **W_R** | Right-handed *W* boson of Pati–Salam — framework predicts **none**. → Popular Full Edition |
| **4th generation** | Falsifies *J*₃(𝕆) three-generation structure. → Octonion pivot |
| **CMB-S4, LiteBIRD, DUNE, Hyper-K** | Experiments tightening Tier 1 gates. → Clean Gates, Distribution Campaign |

### Particle types (quick)

| Term | One line |
|------|----------|
| **Quark** | Strongly interacting spin-½ constituent of hadrons; six flavours in three generations. Masses mostly **inherited** in NTE. |
| **Hadron** | Composite of quarks (baryons = 3 quarks; mesons = quark + antiquark). |
| **Fermion** | Half-integer spin matter (quarks, leptons); spectral action supplies kinetic/Yukawa structure. |
| **Higgs** | SM scalar giving mass via Yukawa; NTE also has separate **Φ_NTE** for expansion. |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-31 | v1.4 — Lagrangian/Hamiltonian/effective action; physics & maths primer; PDF via `build-pdfs.ps1` |
| 2026-05-31 | v1.3 — full symbol index (~120 identifiers); Majorana, CPN/Janus, PMNS, Killing spinor, tier register; *N* disambiguation |
| 2026-05-31 | v1.2 — Dirac operator, trace anomaly, action trio, Lie group, Hopf, Yukawa, particle types, *N*~e~; symbol index tables |
| 2026-05-31 | v1.1 — Kac drum question, spectral triple, spectral action entries; Seeley–DeWitt → alias |
| 2026-05-31 | v1.0 created — heat-kernel expansion + coefficients entries |
