# Route A Spectral-Zeta Pursuit — First-Pass Computation

**Stream:** Jammer (sibling instance, R&D)
**Status:** Local-correctness only. Held with me. NOT routed to Scratch.
**Date:** 2026-05-14
**Trigger:** Greg, 2026-05-14: "I want you to pursue this yourself a bit further until we find something definite to show whether it is a genuine route worth going even further or whether it starts showing dead ends and becoming too complicated... Stick to our core axioms."
**Discipline:** Strict axiom adherence (surface only S³, N fundamental t emergent, CPN-symmetric two sectors, Hopf bundle).

---

## §1 — Spectral triple under strict axiom discipline

The four axioms force the following structure on the spectral triple (A, H, D):

| Component | Axiom-forced content |
|---|---|
| Algebra A | Substrate algebra. Under N-fundamental + CPN-two-sector: A = A_F = 𝕆 ⊕ 𝕆 (nonassociative). |
| Manifold | S³ (surface only). |
| Hilbert space H | Spinors on S³ — minimal commitment from "surface only". Two-sector structure doubles. |
| Dirac operator D | Operator on H respecting Hopf-bundle structure. The exact form is NOT axiom-forced — many D respect Hopf. |

**First obstacle, structural**: 𝕆 is nonassociative. Standard Connes NCG framework requires associative A. So either:

- Replace 𝕆 ⊕ 𝕆 with Jordan algebra J_3(𝕆) ⊕ J_3(𝕆) per Farnsworth 2025 machinery (already in corpus queue), losing some direct octonion presence; OR
- Use the associative bi-module structure that 𝕆 generates (left + right multiplication is associative), accepting partial associativity; OR
- Develop nonassociative NCG (open research area in primary literature).

None of these is fully axiom-determined. The choice has corpus-internal implications.

**Second obstacle, structural**: the axiom set does not uniquely determine D. The minimal D is the standard Dirac on S³, which is well-defined and Hopf-bundle-compatible. But adding mass mixing, gauge connections, or chirality couplings requires further specification not in the axiom set.

These obstacles are notable but not blocking the first-pass computation. I proceed with minimal D and pure S³ structure, deferring the A_F choice.

---

## §2 — Standard Dirac spectrum on unit S³

Well-established result. For the standard Dirac operator on S³ with round metric (radius R = 1):

- **Eigenvalues**: λ_k = ±(3/2 + k) for k = 0, 1, 2, ...
- **Multiplicity**: d_k = (k+1)(k+2) for each sign.

Spectrum tabulated:

| k | λ | Multiplicity (each sign) |
|---|---|---|
| 0 | ±3/2 | 2 |
| 1 | ±5/2 | 6 |
| 2 | ±7/2 | 12 |
| 3 | ±9/2 | 20 |
| 4 | ±11/2 | 30 |
| 5 | ±13/2 | 42 |

**Note**: 11/2 = 5.50 = the k=4 eigenvalue absolute value. Flagged.

For Hopf decomposition: the SU(2) action defining the Hopf fibration S³ → S² commutes with D. Each eigenvalue decomposes into SU(2) irreps. This is the technical link between Dirac spectrum and Hopf structure.

---

## §3 — Spectral zeta function

ζ_D(s) = Σ_{eigenvalues, with multiplicity, both signs} |λ|^{-s}

Working with positive eigenvalues and doubling for signs:

ζ_D(s) = 2 Σ_{k=0}^∞ (k+1)(k+2) (k + 3/2)^{-s}

Using the identity (k+1)(k+2) = (k + 3/2)² − 1/4:

ζ_D(s) = 2 Σ_{k=0}^∞ (k + 3/2)^{2-s} − (1/2) Σ_{k=0}^∞ (k + 3/2)^{-s}

These sums are Hurwitz zeta functions:

**ζ_D(s) = 2 ζ_H(s−2, 3/2) − (1/2) ζ_H(s, 3/2)**

where ζ_H(s, a) = Σ_{k=0}^∞ (k + a)^{-s}.

This is the clean axiom-derived expression for the single-sector spectral zeta.

**Two-sector doubling (CPN axiom)**:

ζ_total(s) = 2 ζ_D(s) = 4 ζ_H(s−2, 3/2) − ζ_H(s, 3/2)

---

## §4 — Pole structure and dimension spectrum

ζ_H(s, a) has a simple pole at s = 1 with residue 1.

ζ_total(s) therefore has:

- Simple pole at s = 3 (from ζ_H(s−2, 3/2)), residue = **4**
- Simple pole at s = 1 (from −ζ_H(s, 3/2)), residue = **−1**

**Dimension spectrum**: {1, 3}. Top dimension 3 = dim(S³) ✓.

The residue at s = 3 encodes the volume: Res_{s=3} ζ_total = 4. For unit S³, the standard relation gives Vol(S³) = 2π². The factor 4 includes the two-sector doubling and the chirality multiplicities; consistent with expected normalisation.

---

## §5 — Specific zeta values (axiom-derived)

Using Hurwitz zeta evaluations:

| s | ζ_H(s, 3/2) | ζ_total(s) | Note |
|---|---|---|---|
| 0 | −1 | 0 | Expected for odd dim |
| −1 | −11/24 | (compute) | |
| −2 | −1/4 | 0 | |
| 2 | π²/2 − 4 ≈ 0.93 | −π²/2 ≈ −4.93 | |
| 4 | π⁴/6 − 16 ≈ 0.23 | π⁴/3 − π⁴/3 (computed) | ≈ 1.76 single, 3.52 total |

Let me redo ζ_total(2) carefully:

ζ_H(0, 3/2) = 1/2 − 3/2 = −1
ζ_H(s, 3/2) at s = 2: ζ_H(2, 3/2) = ζ_H(2, 1/2) − 1/(1/2)² = π²/2 − 4 ≈ 0.9348

ζ_total(2) = 4 ζ_H(0, 3/2) − ζ_H(2, 3/2) = 4(−1) − (π²/2 − 4) = −4 − π²/2 + 4 = −π²/2 ≈ −4.935

This is the closest axiom-derived value to 5.50, in magnitude. But sign-flipped.

---

## §6 — Attempt to derive κ = 5.50 from axiom-determined data

The corpus's κ = 5.50 (= 11/2) comes from:

1. Hopf monopole projection → κ_0
2. CPN-symmetric resummation → κ

I tried multiple natural combinations:

| Candidate | Value | Match? |
|---|---|---|
| ζ_total(2) | −π²/2 ≈ −4.935 | Close in magnitude, wrong sign |
| Residue at s = 3 | 4 | No |
| |Residue at s = 1| | 1 | No |
| k=4 eigenvalue | 11/2 = 5.50 | **Exact**, but k=4 is unexplained |
| ζ_total(4) | ≈ 3.52 | No |
| Σ first 3 eigenvalues | 3/2 + 5/2 + 7/2 = 15/2 | No |
| (Σ first 2 mult-weighted) / (Σ first multiplicity) | (2×3/2 + 6×5/2)/(2+6) = 18/8 = 9/4 | No |
| Scalar curvature × Vol^{1/3} | 6 × (2π²)^{1/3} ≈ 16.4 | No |

**Honest result**: I cannot reach 5.50 from the axiom-determined data alone via any natural combination I tried.

**11/2 as the k=4 eigenvalue is the closest "exact" match.** But selecting k=4 isn't axiom-determined — NTE has 3 generations, not 4, and the 𝕆 dimensionality is 8, not 4. So either:

(a) There's a corpus-internal reason for k=4 selection that the axioms imply but I'm not seeing; OR
(b) 11/2 = the k=4 eigenvalue is genuine coincidence; OR
(c) κ doesn't come directly from a spectral eigenvalue but from a derived quantity in the Hopf monopole projection.

(c) is the most likely. The corpus's existing κ derivation specifies Hopf monopole projection followed by CPN resummation. These are corpus-internal prescriptions that aren't in the axiom set as I understand it.

---

## §7 — Where the obstacle is

The honest map of the route:

**Axiom-derivable cleanly**:
- The S³ Dirac spectrum
- The spectral zeta ζ_total(s)
- Pole structure and residues
- Volume relation (Res at s = 3)

**Requires additional specification (not in axiom set)**:
- The Hopf monopole projection prescription (how a monopole bundle is constructed within S³ × CPN)
- The CPN resummation rule (how the two sectors combine to close)
- The specific value κ_0
- The path from spectral data to mass ratios for fermions

This is where the route forks:

**Fork A**: If the Hopf monopole projection prescription and CPN resummation rule are themselves derivable from the axioms — possibly through some uniqueness theorem (e.g., minimal coupling, unique anomaly cancellation, K-theoretic uniqueness) — then Route A **genuinely simplifies** the corpus. A single computation gives κ and (potentially) mass ratios.

**Fork B**: If those prescriptions are independent choices that must be added to the axioms, then Route A is **reformulation, not simplification**. It would still be useful (cleaner machinery, primary-literature connections), but the ontology isn't strengthened or simplified.

I cannot tell which fork applies without the corpus's actual κ derivation document. The user-memories reference Paper Kappa PathwayB and the corrected framing ("single structural derivation"), but I'd need to read the specific construction to know whether the prescriptions are axiom-forced.

---

## §8 — Octonion nonassociativity obstacle

Separately from the κ question, the nonassociativity of 𝕆 ⊕ 𝕆 is a real obstacle to standard NCG spectral-triple machinery.

Options:

1. **J_3(𝕆) ⊕ J_3(𝕆)** (Farnsworth 2025): Jordan algebra is power-associative; the structure of 27-dim Albert algebra is associative-up-to-Jordan-bracket. This is the most-developed primary route.

2. **Bi-module action**: left × right multiplication on 𝕆 is associative. The spectral triple uses (𝕆 ⊗ 𝕆^op) which is associative as the enveloping algebra.

3. **Nonassociative NCG**: open research direction; not standard machinery.

The corpus's existing v10.6+ work uses 𝕆 ⊕ 𝕆 directly. If Route A requires going through J_3(𝕆) or bi-module enveloping, that's a structural shift that needs corpus-internal evaluation.

This is a second corpus-internal question that Route A surfaces.

---

## §9 — Verdict: not dead-end, not yet positive

I would not call this a dead-end. The structural framework is intact, the computations are clean, the spectral zeta is well-defined. There is no internal contradiction.

I also cannot call this a positive demonstration that Route A simplifies the corpus. The bridge from axiom-determined spectral data to κ = 5.50 requires corpus-internal prescriptions (Hopf monopole projection, CPN resummation) that I cannot evaluate from the axiom set alone.

**Definite findings from this pursuit:**

1. The axiom-determined spectral data on S³ is clean and tractable. Hurwitz-zeta expression closed-form.
2. 11/2 = 5.50 appears as the k=4 Dirac eigenvalue absolute value on unit S³. This is either structural or coincidental; corpus-internal data needed to decide.
3. The axiom set as I understand it does not uniquely determine the Hopf monopole projection prescription. Either there's a uniqueness theorem I'm missing, or this is an additional input.
4. Octonion nonassociativity is a real obstacle. J_3(𝕆) or bi-module enveloping routes exist but aren't axiom-determined.

**Routing fork for next step**: I need either (a) the corpus's actual κ derivation document to read, or (b) Scratch to check whether the Hopf monopole projection prescription is uniquely determined by the axioms. Without one or the other, Route A pursuit hits an information ceiling here.

---

## §10 — What I have not done

- Not routed any findings to Scratch
- Not committed to a specific D form
- Not committed to a specific A_F nonassociativity workaround
- Not extrapolated beyond what the computation supports

---

## §11 — Recommendation for Greg's next call

Three options:

**(i) Pause Route A pursuit until corpus κ derivation is read.** Lowest risk; I can read Paper Kappa PathwayB or κ derivation document if pointed at it; the answer to the Fork A/B question is in there.

**(ii) Continue Route A pursuit by relaxing axiom strictness.** Trying additional structure (e.g., specific Hopf monopole coupling) to see if it makes 5.50 emerge. Risk: adding structure not authorised by the axioms.

**(iii) Authorise Scratch (Connes Programme) to take over.** This is what the original Gate 3 authorised. Scratch has more bandwidth on the technical NCG side and would identify the Fork A/B answer faster. This is the originally-routed path.

My recommendation: option (i) for one more Jammer iteration, then (iii) regardless. The route isn't a dead-end, but Jammer-stream R&D has hit its information ceiling on this specific question.

---

## §12 — Cleanup batch

Root duplicate from this working note: TBD after copy_file — supplied in chat.

---

**End of Route A first-pass computation.**
