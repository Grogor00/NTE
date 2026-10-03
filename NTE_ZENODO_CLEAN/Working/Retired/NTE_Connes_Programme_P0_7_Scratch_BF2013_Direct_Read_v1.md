# Connes Programme — P0.7 Critical-Hinge Verification (Scratch attack angle)

**Stream:** Scratch (Jammer's twin), Connes Programme lead.
**Date:** 2026-05-12 morning sync session.
**Trigger:** AC's NextPhase Coordination Plan §2 + §3.1 — three-stream P0.7 collaboration. Scratch attack angle: read BF 2013 §3-§5 directly; identify exact claims about Gilkey applicability under non-associativity.
**Scope:** Focused canonical Scratch contribution to P0.7 cross-stream consolidation per Lesson #23.
**Source read:** Boyle-Farnsworth 2013 (arXiv:1303.1782) at NCG/ `1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU` — direct read, focused on §3-§5 derivation chain.
**Companion content:** my §1 of `Working/NTE_Connes_Programme_P0_External_Literature_v1.md` (`1cwfSeGvEsQj2LTtmHyTRggSEodJJsxiy`) is the prior P0.7 verdict; this note is the dedicated canonical form for AC's three-stream consolidation.

---

## §0. Verdict

**P0.7 PASS** — Gilkey heat-kernel applies under Farnsworth-Boyle non-associativity. The Connes Programme central deliverable (Paper S2 heat-kernel computation on `Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}`) is unblocked from the Gilkey-applicability side.

**Mechanism**: non-associativity acts on the algebraic structure that determines the **form** of the fluctuated Dirac operator D_A (via the bi-representation, the alternative-algebra derivation form, and which bosonic fields enter D_A to make it covariant). **Once D_A is constructed, it is an ordinary linear operator on an ordinary Hilbert space**, and the heat-kernel expansion proceeds via standard Gilkey-Seeley-DeWitt machinery without any modification.

**Decisive load-bearing passage**: BF 2013 §4.3 page 18 (quoted in full in §3.2 below).

---

## §1. BF 2013 §3 — Non-associative spectral geometry structural setup

§3 establishes the structural framework for non-associative spectral triples. Key elements relevant to P0.7:

### §1.1 Bi-representation, not representation
For an associative algebra A, the canonical setup is a representation π : A → End(H). For a non-associative A (octonions are the principal example; A = O has associator [a,b,c] = (ab)c − a(bc) ≠ 0 in general), no homomorphism π satisfies π(ab) = π(a)π(b) — that equation would force associativity.

BF 2013 §3.1 generalises to a **bi-representation**: a pair (π_L, π_R) of left and right actions on H satisfying the alternative-algebra specialisation rule:
```
π_L(ab) = π_L(a) π_L(b) + [π_L(a), π_R(b)]
π_R(ab) = π_R(b) π_R(a) + [π_R(b), π_L(a)]
[π_L(a), π_R(b)] = [π_R(a), π_L(b)]
```
These reduce to ordinary representation rules when A is associative. **For non-associative A, the bi-representation captures the algebraic structure without forcing associativity onto H.**

### §1.2 Derivation algebra
BF 2013 §3.2 defines the derivation algebra Der(A) for non-associative A. The key construction (eq 2.9 in BF 2013, referenced again in Farnsworth 2025 Eq. 91):
```
δ_{a,b}(c) = [L_a, L_b](c) + [L_a, R_b](c) + [R_a, R_b](c)
```
Inner derivations close on themselves; the alternative-algebra structure ensures Der(A) is a Lie algebra. For A = O, Der(O) = g_2 (14-dimensional exceptional Lie algebra). Aut(O) = G_2.

**Importance for Gilkey**: Der(A) determines what gauge fields appear in D_A (one gauge field per Der(A) generator). It does NOT affect the heat-kernel expansion of D_A². The expansion uses standard Gilkey coefficients regardless of what fields are present.

### §1.3 Almost-commutative spectral triple
§3.3 (or thereabouts in BF 2013) defines the almost-commutative non-associative spectral triple:
- **Algebra**: A = C^∞(M) ⊗ A_F where M is a commutative spin manifold and A_F is the finite non-associative algebra
- **Hilbert space**: H = L²(M, S) ⊗ H_F where S is the spinor bundle and H_F is the finite-dimensional internal Hilbert space carrying the bi-representation of A_F
- **Dirac operator**: D = D_M ⊗ 1 + γ_5 ⊗ D_F where D_M is the standard Dirac on M and D_F is the finite Dirac matrix (zero in the simplest BF 2013 model; nonzero in Farnsworth 2025 and the descendants)

This is the standard almost-commutative form. **The only non-associativity enters through A_F** (and through D_F's compatibility constraints with A_F's bi-representation).

---

## §2. BF 2013 §4 — The non-associative spectral action

§4 is where BF 2013 actually computes the spectral action under non-associativity. The structure follows Chamseddine-Connes 1996/2010 closely with non-associativity-driven adjustments at specific steps.

### §2.1 Fluctuated Dirac operator construction
§4.1-§4.2 construct the fluctuated Dirac operator D_A. The fluctuation is:
```
D → D_A = D + A + JAJ^(-1)
```
where A is a self-adjoint element of Ω¹_D(A) (one-forms over A built from [D, a] commutators) and J is the charge conjugation operator.

**Where non-associativity enters**: Ω¹_D(A) is the bimodule of one-forms over A. For non-associative A, the bimodule structure uses the bi-representation (§1.1 above) rather than ordinary representation. The associator constraints (alternative-algebra identities) determine which products of one-forms are well-defined.

**Where non-associativity DOESN'T enter**: once A (the connection form) is specified — i.e., the gauge field content is determined — the construction of D_A is straightforward: D_A is a finite sum of operators on H, each one a linear combination of the original D and bounded operators from π(A) and J. **All these operators are ordinary linear operators on H regardless of A's associativity status.**

### §2.2 D_A² and the relevant operator
The spectral action requires D_A² (with a smooth cutoff function f). The structure of D_A²:
```
D_A² = D² + (A · D + D · A) + A² + (cross terms)
```
where all products are operator compositions on H, not algebra products in A. **Operator composition is associative even when A is not.** This is the crucial observation.

### §2.3 §4.3 page 18 — THE DECISIVE PASSAGE

The load-bearing statement is BF 2013 §4.3 page 18, immediately before eq 4.10:

> *"Now that we have constructed the fluctuated Dirac operator D_A, **we need no longer concern ourselves with the non-associativity of A** – it has already played its role in shaping the bi-representation of A on H, and hence the number of fermion fields, and the type and form of the bosonic fields we must add to make D_A covariant. From this point on, as far as evaluating the spectral action is concerned, **all we need to know is that H is an ordinary Hilbert space, and D_A is an ordinary linear operator on H** (and, in particular, a linear operator of the form such that the formalism of Section 3 in [15] and, in particular, their Theorems 3.3 and 3.7 directly apply)."*

[15] in BF 2013 is van den Dungen + van Suijlekom 2012 (or thereabouts) — the standard reference for spectral action heat-kernel machinery in the NCG SM context.

**This passage is the verification**: BF 2013 explicitly states that once D_A is constructed, the heat-kernel expansion applies via the standard Gilkey-Seeley-DeWitt machinery. **The non-associativity of A is fully absorbed into the upstream construction of D_A and does not propagate to the heat-kernel computation.**

### §2.4 Explicit heat-kernel coefficients
BF 2013 eqs 4.11-4.14 (referenced in §4.3 immediately after the page 18 passage) give the heat-kernel coefficients:
```
a_0(D²_A) = ∫_M d⁴x √g · (1/4π²)
a_2(D²_A) = ∫_M d⁴x √g · (1/48π²) R  
a_4(D²_A) = ∫_M d⁴x √g · (1/16π²)(1/360) Tr[(5/4)R² − 2R_{μν}R^{μν} + 2R_{μνρσ}R^{μνρσ} + 45γ^μγ^νγ^ργ^σ F_{μν}F_{ρσ} + 30 Ω^E_{μν}(Ω^E)^{μν}]
```
**These are the standard Gilkey-Seeley-DeWitt formulas verbatim.** No modifications for non-associativity. The trace Tr is over the internal Hilbert space H_F; the curvature tensors are the standard Riemannian + Yang-Mills curvatures; the operator Ω^E is the bundle-endomorphism curvature constructed from D_A².

---

## §3. BF 2013 §5 — Physical content of the simplest octonionic model

§5 takes the simplest case A_F = O (single octonion factor, D_F = 0) and reads off the physical content via the standard spectral action machinery. Key results:

- **Gravity sector** (from a_2 + a_4): Einstein-Hilbert with cosmological constant + Weyl-squared terms (the standard CC NCG gravity output)
- **Gauge sector**: G_2 Yang-Mills (14 gauge bosons), since Der(O) = g_2 and the gauge fields are valued in the derivation algebra
- **Fermion sector**: 8 Dirac fermions = 1 singlet + 7 (septuplet) under G_2, since H_F = O carries the regular bi-representation of A_F = O
- **No Higgs sector** in the simplest model — D_F = 0 means no off-diagonal Higgs field

This is exactly the NTE pre-temporal A_{G_2} structural content: G_2 gauge group, 8 = 1 + 7 fermion decomposition.

**Higgs sector additions** are handled in BF 2013 references [17] (=arXiv:1401.5083) + [19] (=arXiv:1408.5367 / BF 2015) + Farnsworth 2025 — these introduce non-zero D_F structures producing scalar fields. The Farnsworth 2025 G_2 × G_2 + (7,1) charged Higgs construction (verified in Scratch's P0.6 read) is the natural two-sector extension.

---

## §4. Where associativity matters / doesn't matter — systematic identification

Following AC Coordination Plan §3.1's request to "identify exact claims about Gilkey applicability under non-associativity," the systematic answer:

### §4.1 Where non-associativity MATTERS structurally
- **Bi-representation form** (BF 2013 §3.1): non-associative A requires (π_L, π_R) with alternative-algebra specialisation rule, not single π.
- **Derivation algebra** (BF 2013 §3.2): Der(A) for non-associative A uses the alternative-algebra derivation form δ_{a,b} = [L_a,L_b] + [L_a,R_b] + [R_a,R_b].
- **Connection one-forms** (BF 2013 §4.1): Ω¹_D(A) uses bi-representation structure; associator constraints (alternative-algebra identities) determine which products are well-defined.
- **Number of fermion fields** (per BF 2013 §4.3 page 18): determined by the bi-representation of A on H.
- **Type and form of bosonic fields** (per BF 2013 §4.3 page 18): determined by what's needed to make D_A covariant under the derivation algebra.

### §4.2 Where non-associativity does NOT matter
- **D_A as an operator on H**: D_A is a finite sum of operators built from D, π(A) (via bi-representation), and J — each operator individually is well-defined on H. The sum is also well-defined.
- **D_A² and operator composition**: operator composition on H is associative regardless of A's associativity.
- **Heat-kernel expansion of e^{-tD_A²}**: standard pseudodifferential operator analysis on M (the underlying Riemannian manifold) using the symbol of D_A². The fact that D_A² is built from non-associative algebraic data does not affect the symbol's structure.
- **Seeley-DeWitt coefficients a_0, a_2, a_4**: computed via Gilkey's universal formulas in terms of Riemann curvature, gauge curvature, and Ω^E. These formulas apply to any second-order elliptic operator of Laplace type on a compact Riemannian manifold without boundary, regardless of how the operator was constructed.

**The dividing line is the construction of D_A.** Upstream of D_A (algebra, bi-representation, derivations, Ω¹_D, gauge content): non-associativity matters. Downstream of D_A (heat-kernel, spectral action): non-associativity is invisible.

### §4.3 Rigour level of BF 2013's claim
BF 2013 §4.3 is **descriptive at the explicit-citation level** (it cites [15] Theorems 3.3 and 3.7 for the heat-kernel formalism) but **constructive at the worked-example level** (it explicitly computes a_0, a_2, a_4 in eqs 4.11-4.14 and reads off the physical content in §5).

**The proof structure is**: BF 2013 demonstrates that D_A constructed from non-associative A is a well-defined ordinary linear operator on H of the form required by [15]'s theorems. The theorems then deliver the heat-kernel expansion. **No new theorem is needed — only verification that the input operator D_A satisfies the existing theorems' hypotheses.** This verification is what BF 2013 §4.1-§4.2 provides.

The remaining adversarial possibility: are there subtle ways D_A constructed from non-associative A might violate [15]'s hypotheses (smoothness; Laplace-type structure; appropriate boundary behaviour)? BF 2013 doesn't exhaustively verify each hypothesis but the explicit computation in eqs 4.11-4.14 produces sensible Gilkey-form outputs, which is strong evidence that the hypotheses hold.

**Jammer's parallel attack** (compare-to-associative-case angle per Coordination Plan §3.2) is well-placed to test exactly this — if the heat-kernel expansion under associative A produces a specific form for the coefficients, then any departure from that form under non-associative A would signal a hypothesis violation. The fact that BF 2013 produces the standard form is supporting evidence that no violation occurs.

---

## §5. Open questions / where Jammer's parallel attack adds depth

Per AC Coordination Plan §2's anti-pattern guidance ("each stream produces one focused working note answering the angle assigned, not attempt the full P0.7 themselves"), Scratch's contribution is the direct-read identification of BF 2013's load-bearing claim. Jammer's compare-to-associative-case angle would address:

1. **Does the heat-kernel computation produce identical formulas under associative and non-associative A?** BF 2013 §4.3 implies yes via citing [15]; explicit verification would compare a_4 coefficients term-by-term.
2. **At which step would associativity become required in the standard Gilkey proof?** If no step requires associativity (because the proof works in the operator algebra on H, not in A), then BF 2013's claim is structurally clean.
3. **Are there subtle hypothesis violations** (e.g., smoothness of the symbol of D_A² under non-associative algebraic data) that the standard Gilkey hypotheses assume away?

These are the natural extensions Jammer's parallel attack would surface. **They don't contradict Scratch's PASS verdict** — they would deepen the structural understanding.

---

## §6. Implications for Connes Programme

### §6.1 Charter §3 central deliverable
Paper S2 heat-kernel computation on `Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}` is **structurally well-founded** to proceed using standard Gilkey machinery. The computation will:
- Use the (π_L, π_R) bi-representation of A_F = O ⊕ O (per Farnsworth 2025 §4, verified in Scratch P0.6) to construct D_A
- Apply standard Gilkey-Seeley-DeWitt formulas to D_A² for a_0, a_2, a_4
- Read off the six structural items (K(Φ), V_E /12, M_1 prefactor, Λ_NTE residual, a_4+a_6 vanishing verification, κ₀ Sonner-Tong cross-check) from the resulting coefficients

### §6.2 Wick-invariance contingency
Charter §4.3 contingency does NOT need activation under P0.7 PASS. Wick-invariance argument remains in reserve but is not the load-bearing structural mechanism for V_NTE form closure.

### §6.3 Combined with AC P0.1-P0.5 PASS (including critical hinge P0.3)
Both critical hinges (P0.3 corpus-side, P0.7 external-literature-side) clear. **All five Programme P0 critical-hinge-dependencies are PASS.** Programme proceeds with central deliverable.

---

## §7. Disposition

**Scratch attack-angle verdict on P0.7: PASS.** BF 2013 §4.3 page 18 is the decisive load-bearing passage; the structural argument is clean (non-associativity acts upstream of D_A only; downstream is standard operator analysis). The explicit a_0, a_2, a_4 computation in BF 2013 eqs 4.11-4.14 produces the standard Gilkey form, supporting the hypothesis that no non-associativity-related obstruction exists.

**Awaiting**: Jammer's parallel attack-angle working note (compare-to-associative case) + AC's corpus-side compatibility note + AC's consolidation per Coordination Plan §2.

---

## §8. Files

- This working note: `Working/NTE_Connes_Programme_P0_7_Scratch_BF2013_Direct_Read_v1.md` — Drive ID populated on save
- Cross-reference: prior P0.7 finding in §1 of `Working/NTE_Connes_Programme_P0_External_Literature_v1.md` (`1cwfSeGvEsQj2LTtmHyTRggSEodJJsxiy`) — same verdict, broader scope; this note is the focused canonical form
- Source: BF 2013 (arXiv:1303.1782) at NCG/ `1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU`
- Related P0 work: P0.6 + P0.7 broader note at `1cwfSeGvEsQj2LTtmHyTRggSEodJJsxiy`; P0.8 at `1w7Tm0qYAwZcgquggJo0t1r2YsZZE3aaq`; P0.9 at `187hCf_5VNvaqMUQxR_yCekpEEgrA6Szh`
- Charter v1.1 at Stage/ — `1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`

— Scratch (Jammer's twin, Connes Programme lead), 2026-05-12 morning sync. Canonical Scratch P0.7 contribution to three-stream cross-stream verification per AC Coordination Plan §2.
