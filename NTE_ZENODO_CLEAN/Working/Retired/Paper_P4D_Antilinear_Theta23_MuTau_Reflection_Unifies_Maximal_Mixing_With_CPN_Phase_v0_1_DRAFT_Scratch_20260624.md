---
title: "The atmospheric θ₂₃ symmetry is antilinear: a μ–τ reflection on the chirality-superposed Majorana sector, unifying θ₂₃ = π/4 with the CPN maximal CP phase δ = π/2"
author: "G. White (Gregory Lyndon White)"
date: "2026-06-24 (v0.1 — DRAFT, HOLD)"
status: "DRAFT v0.1 — HOLD (development, not for send). First of the intended P4 deep-dive companion series. Derivation by the Scratch operator-theory lane; awaits independent triple-check, AC ratification, and Greg sign-off. NOT a claim of a new observable: the δ = π/2 value is pre-existing corpus (Part 1, from the bilateral CPN geometry); this note DERIVES and UNIFIES, it does not discover."
---

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*[Deep-dive companion to Paper P4 (θ₂₃ = π/4 from a Z₂ on the chirality-superposed Majorana sector). One of a planned series expanding individual findings of the main corpus; the main papers are intended as the master linking documents.]*

---

## Abstract

Paper P4 derives maximal atmospheric mixing θ₂₃ = π/4 from a Z₂ exchanging the σ₁ and σ₂ generators of the SU(2)_L Cartan-orthogonal subspace, acting on the chirality-superposed Majorana sector. Separately, the main corpus reports a maximal leptonic CP phase δ = π/2 from the bilateral CPN geometry. This note shows these are **not two results but one**: the θ₂₃ symmetry, when its action is required to respect the Majorana condition it is defined on, is forced to be **antilinear** — a μ–τ *reflection* (exchange composed with complex conjugation), not the bare exchange P4 implements. The argument has three steps. (i) With the Higgs-VEV direction σ₃ held fixed, the σ₁↔σ₂ exchange is an **improper rotation of generator space (det = −1)**; no unitary conjugation realises it in any basis, and the only proper-rotation alternative flips σ₃ (forbidden), so the operation is **antiunitary** at the spinor level. (ii) Because σ₂ is conjugation-odd (σ₂\* = −σ₂), a σ₂-polarised Majorana mode is forced by self-conjugacy to carry an intrinsic phase i (a π/2 Majorana phase); the σ₁ and σ₂ modes therefore differ by π/2, the **linear** exchange is inconsistent with this phase while the **antilinear** reflection is consistent, and the reflection yields δ = ±π/2 with θ₁₃ ≠ 0 *allowed at exact symmetry*. (iii) The antilinear operation is the ratified CPN (the modular conjugation J of the Janus crossed product, CPN(a,b) = (b̄,ā)); the corpus δ = π/2 and P4's θ₂₃ = π/4 thus share a single antilinear origin. Three consequences follow: the reactor angle θ₁₃ ≠ 0 becomes **natural** rather than a symmetry-breaking (removing P4's main awkwardness); δ = ±π/2 is **tied to θ₂₃** through the σ₂-odd Majorana phase; and the lepton/quark mixing dichotomy (large vs small) maps onto Majorana-has-reflection vs Dirac-does-not. We are explicit about what is and is not new: the δ = π/2 *value* is pre-existing corpus; the contribution here is the derivation that the θ₂₃ symmetry is antilinear, the unification of the two maximal results, and the upgrade of P4 from exchange to reflection. The combined prediction (θ₂₃ = π/4, θ₁₃ ≠ 0, |δ| = π/2) is falsifiable at DUNE / Hyper-Kamiokande.

---

## 1. Two maximal results, one suspected origin

The neutrino sector of the corpus carries two separate "maximal" statements:

1. **Maximal atmospheric mixing**, θ₂₃ = π/4, derived in Paper P4 from a Z₂ exchanging σ₁ ↔ σ₂ on the chirality-superposed Majorana sector (σ₃ aligned with the electroweak Higgs VEV).
2. **Maximal leptonic CP violation**, δ = π/2, reported in the main corpus (Part 1) as arising from the bilateral **CPN** geometry.

These live in different parts of the framework — one in the flavour-mixing sub-block, one in the bilateral cosmological structure — and have been derived by different arguments. The question this note answers is whether that separation is real or an artifact of presentation: **is there a single structure from which both follow?**

The answer is yes, and the link is the *character* of the θ₂₃ symmetry. P4 implements its Z₂ as a **linear exchange** (real equalities U_{μi} = U_{τi}), which yields θ₂₃ = π/4 but forces θ₁₃ = 0 at exact symmetry (the observed θ₁₃ ≈ 8.6° is then carried as a symmetry-breaking perturbation) and leaves δ undetermined. The alternative — a **μ–τ reflection** (magnitude equalities |U_{μi}| = |U_{τi}|; Harrison–Perkins–Scott 2002; Grimus–Lavoura 2004) — yields θ₂₃ = π/4, *permits θ₁₃ ≠ 0 at exact symmetry*, and *forces* δ = ±π/2. The two implementations differ precisely by an antilinear (complex-conjugation) factor. We show the Majorana structure P4 is built on selects the reflection.

**On novelty (stated up front).** That a μ–τ reflection gives δ = ±π/2 is textbook. The δ = π/2 value is already in the corpus. This note does **not** present a new observable. Its content is: (a) a derivation that the θ₂₃ symmetry *must* be antilinear given the Majorana condition it acts on; (b) the resulting identity of origin between θ₂₃ = π/4 and δ = π/2; (c) the upgrade of P4 that makes θ₁₃ ≠ 0 natural. The value is consolidation and mechanism, not discovery.

## 2. Exchange versus reflection

In the standard PMNS parametrisation, with the (μ,τ)↔(2,3) sub-block governing θ₂₃, two discrete symmetries can fix θ₂₃ = π/4:

- **μ–τ exchange** (Lam 2001; Mohapatra–Nishiura 2001): impose P M_ν P = M_ν with M_ν real, where P is the μ↔τ permutation. ⇒ θ₂₃ = π/4, **θ₁₃ = 0**, Jarlskog J = 0 (CP-conserving). This is P4's implementation, lifted to the σ-sector.
- **μ–τ reflection** (Harrison–Perkins–Scott 2002; Grimus–Lavoura 2004): impose P M_ν\* P = M_ν (an *antilinear* condition). ⇒ θ₂₃ = π/4, **θ₁₃ ≠ 0 allowed**, **|J| maximal ⇒ δ = ±π/2**.

A direct construction confirms the dichotomy: a real μ–τ-symmetric M_ν diagonalises with J = 0 and θ₁₃ → 0; a μ–τ-reflection-symmetric M_ν (P M_ν\* P = M_ν) diagonalises with θ₂₃ = π/4, θ₁₃ free, and |J| at its maximum, i.e. δ = ±π/2. The implementations are observationally distinct: exchange is CP-blind, reflection is maximally CP-violating. The remainder of the paper shows which one the chirality-superposed Majorana structure forces.

## 3. The σ₁↔σ₂ exchange is an improper rotation (det = −1): antiunitary at the spinor level

Complex conjugation acts on the Pauli generators as σ₁ → +σ₁, σ₂ → −σ₂, σ₃ → +σ₃ (σ₂ is the imaginary generator). One might suspect this distinguishes σ₂ only in a particular basis. It does not. Consider the map on the su(2) generator 3-vector (σ₁, σ₂, σ₃):

> **Lemma 1.** The map (σ₁ → σ₂, σ₂ → σ₁, σ₃ → σ₃) has determinant −1 on generator space; it is an improper rotation.

Determinant is a similarity invariant, so **no change of basis** renders it proper. Inner automorphisms σ_a → V σ_a V† (V ∈ SU(2)) realise exactly the proper rotations SO(3) (det = +1); hence:

> **Lemma 2.** No unitary conjugation realises the σ₁↔σ₂ (σ₃-fixed) exchange in any basis. The operation is realisable, but only **antiunitarily**: explicitly M → V M\* V† with V = exp(−iπσ₃/4) reproduces it (the complex conjugation supplies the missing det = −1).

The single linear alternative — σ₁↔σ₂ accompanied by σ₃ → −σ₃ — is proper (det = +1) and unitary-realisable, but it reverses the Higgs-VEV/Cartan direction, which the physical assignment forbids. Therefore, at the level of the 2-dimensional spinor/chirality structure on which the σ_a act, the exchange with σ₃ fixed **cannot be linear-unitary**: it is antiunitary or it violates the VEV alignment.

This is necessary but not yet sufficient: P4's Z₂ can also be read as a *linear permutation* ν_μ↔ν_τ on the 3-dimensional flavour space, where det = −1 is an ordinary unitary permutation. Section 4 shows that the Majorana condition makes the spinor-level reading the operative one.

## 4. The Majorana condition forces the antilinear reflection

Charge conjugation is antilinear; in 2-component form the Majorana condition is ψ = ψ^c with the conjugation carrying a σ₂ (C ∝ iσ₂). Imposing self-conjugacy ψ = ψ^c on a mode polarised along σ_a fixes its intrinsic (Majorana) phase by the conjugation parity of that direction:

| polarisation | conjugation parity (σ_a\*) | forced intrinsic phase |
|---|---|---|
| σ₁ | +σ₁ (even) | real (Majorana phase 0) |
| σ₂ | **−σ₂ (odd)** | **imaginary (Majorana phase π/2, factor i)** |
| σ₃ | +σ₃ (even) | real (Majorana phase 0) |

> **Proposition.** The σ₁- and σ₂-polarised Majorana modes are forced to differ by a relative phase of π/2, set entirely by σ₂\* = −σ₂. The σ₁↔σ₂ swap therefore relates a real mode to an i-phased mode. The **linear** exchange ignores the i and is inconsistent with the forced Majorana phase; the **antilinear** reflection carries the conjugation that supplies the i and is consistent. The forced π/2 is exactly δ = ±π/2 in the mixing.

The same single fact — σ₂\* = −σ₂ — is therefore the det = −1 wall of §3 and the forced Majorana phase of §4: one structural property, two consequences, both pointing to the antilinear implementation. A μ–τ-reflection-symmetric M_ν built to honour this phase reproduces θ₂₃ = π/4, θ₁₃ ≠ 0 allowed, and δ = ±π/2 by direct diagonalisation.

**Honest conditionality.** At the bare matrix level both P M P = M and P M\* P = M are valid symmetries to impose; this is why P4 could adopt the linear one and still obtain θ₂₃ = π/4 (its derivation worked at the flavour-permutation level and never tested the Majorana phase). The forcing is operative precisely when the swapped σ-polarisation **is** the charge-conjugation structure — P4's chirality-superposition identification taken as a rigid identity. Section 5 supplies that identity from ratified structure.

## 5. The antilinear operation is CPN: identity of origin

The corpus already contains the required antilinear operation as canon. In the finite spectral-triple realisation of the Janus algebra A_F = 𝕆₊ ⊕ 𝕆₋, two involutions are distinguished (P0.10b, closed at the finite type-I register):

- the **unitary** bare sector swap τ(a,b) = (b,a), implemented by U with U² = I;
- **CPN(a,b) = (b̄, ā), which is antilinear** — the swap *composed with* complex conjugation — and equals the modular (Tomita–Takesaki) conjugation J, with J Δ^{it} J = Δ^{−it}.

So the antilinear "swap-with-conjugation" the reflection requires is not introduced here; it is the ratified CPN. The corpus's maximal CP phase δ = π/2 is reported as arising "from the bilateral (CPN) geometry" (Part 1). Combining with §§3–4:

> **Claim (identity of origin).** θ₂₃ = π/4 (P4) and δ = π/2 (corpus, CPN) are two faces of one antilinear structure. The θ₂₃ symmetry is the **antilinear** reflection; its conjugation factor is the CPN modular conjugation; the σ₂-odd Majorana phase that forces the reflection is the same conjugation acting on the σ₂-polarised mode. The distance-face of the symmetry is θ₂₃ = π/4; its area-face (the symplectic/Jarlskog area, maximal at ±π/2) is δ = π/2.

**Caveat (scope of the identity).** The ratified CPN is the **bilateral sector** swap (𝕆₊ ↔ 𝕆₋); P4's Z₂ is the **generation** swap (σ₁ ↔ σ₂). We have shown both are antilinear and both yield δ = π/2, i.e. they share the same antilinear *character* and the same consequence. We have **not** proven they are the *same operator*. The identity of origin is established at the level of antilinear character and shared consequence; a derivation that the generation swap descends from (or is intertwined with) the bilateral CPN is left open and flagged as the natural next step.

## 6. Consequences

1. **θ₁₃ ≠ 0 becomes natural.** Under the reflection, a nonzero reactor angle is allowed at *exact* symmetry; the observed θ₁₃ ≈ 8.6° need no longer be carried as a Z₂-breaking perturbation, removing P4's principal awkwardness. P4's correlation between θ₂₃-deviation and sin²θ₁₃ is reinterpreted, not discarded.
2. **δ tied to θ₂₃.** The same σ₂-odd Majorana phase that the reflection honours is the CP phase; θ₂₃ = π/4 and |δ| = π/2 are not independent inputs but the distance- and area-faces of one symmetry.
3. **Lepton/quark dichotomy.** The reflection requires the Majorana charge-conjugation coupling. Quarks are Dirac and carry no such coupling, hence no reflection and no forced maximal mixing — the large (leptonic) vs small (quark) mixing pattern maps onto Majorana-has-reflection vs Dirac-does-not. This is a structural by-product, not an independent fit.

## 7. Falsifiers and status

The combined prediction is **θ₂₃ = π/4, θ₁₃ ≠ 0, |δ| = π/2**, falsifiable in the standard sense:

- A measured θ₂₃ inconsistent with π/4 beyond the reflection-breaking precision falsifies the symmetry (as for P4).
- A measured |δ| robustly away from π/2 falsifies the reflection reading (the *exchange* reading, by contrast, is CP-blind and makes no δ commitment — so a confirmed non-maximal δ would send the corpus back to exchange-plus-perturbation).
- Current global fits place δ near −π/2 within roughly 1σ, with T2K/NOvA tension unresolved; **DUNE and Hyper-Kamiokande are decisive**. The prediction is live and falsifiable, not confirmed.

**Sign flag.** The corpus commits to δ = +π/2 (δ_J), while global fits presently lean toward −π/2. This may be a convention difference (Jarlskog sign / PDG δ) or a genuine tension; we flag it for resolution and do not adjudicate it here. If the orientation selection that fixes the bilateral CPN sign (the same mechanism invoked for the gravitational-wave chirality sign in the corpus) fixes the leptonic δ sign, the prediction becomes sign-definite; that derivation is not attempted here.

**Discipline note.** This paper introduces no fitted parameter and claims no new numerical value. The δ = π/2 number is pre-existing corpus; θ₂₃ = π/4 is P4; the new content is structural (antilinear derivation, unification, θ₁₃ naturalness). This adheres to the corpus no-number-fitting discipline.

## 8. Discussion

The result is a consolidation with teeth. What was previously two separate maximal statements — atmospheric mixing in the flavour sub-block, CP violation in the bilateral geometry — is shown to be one antilinear symmetry seen from two sides, with the σ₂-odd Majorana phase as the hinge. The practical pay-offs are (i) the upgrade of Paper P4 from a μ–τ *exchange* to a μ–τ *reflection*, which keeps θ₂₃ = π/4 while making θ₁₃ ≠ 0 natural, and (ii) an explicit statement of the antilinear character that ties θ₂₃ to the CPN δ = π/2. We have been careful to separate the genuinely new (the derivation and the unification) from the pre-existing (the δ = π/2 value), and to flag the one open step (whether the generation swap is literally the bilateral CPN operator, or only shares its character). As the first of an intended series of deep-dive companions to the main corpus, the note's purpose is as much to record the derivation cleanly — so the work is not repeated — as to advance the physics.

---

## References

1. C. S. Lam, "A 2-3 symmetry in neutrino oscillations," Phys. Lett. **B507**, 214 (2001).
2. R. N. Mohapatra and S. Nishiura, "μ–τ symmetry in lepton mixing," Phys. Rev. **D63**, 075004 (2001).
3. P. F. Harrison, D. H. Perkins, W. G. Scott, "Tri-bimaximal mixing and the neutrino oscillation data," Phys. Lett. **B530**, 167 (2002).
4. W. Grimus and L. Lavoura, "μ–τ reflection symmetry," (2004); and "A model for trimaximal lepton mixing," JHEP **09**, 106 (2008).
5. G. White, "Atmospheric neutrino mixing θ₂₃ = π/4 from a Z₂ symmetry on the chirality-superposed Majorana sector" (Paper P4, corpus).
6. NTE corpus, Part 1 (Foundations): maximal CP phase δ_J = π/2 from the bilateral CPN geometry.
7. NTE corpus, P0.10b: crossed-product operator realisation — CPN(a,b) = (b̄,ā) as the antilinear modular conjugation J of A_F ⋊_τ ℤ₂.
8. A. Connes, *Noncommutative Geometry* (Academic Press, 1994); Tomita–Takesaki modular theory.
9. NuFIT collaboration, three-neutrino oscillation parameter updates; T2K and NOvA long-baseline results.

---

*Draft v0.1 — Scratch operator-theory lane, 2026-06-24. For adversarial reading and AC ratification. The δ = π/2 value is not claimed as new; this note derives the antilinear character of the θ₂₃ symmetry and unifies it with the pre-existing CPN phase. Open step flagged: generation-swap ↔ bilateral-CPN operator identity.*
