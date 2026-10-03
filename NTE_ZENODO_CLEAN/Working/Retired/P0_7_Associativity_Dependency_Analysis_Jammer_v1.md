# Jammer Working Note — P0.7 Associativity-Dependency Analysis

**Stream:** Jammer (R&D, single session)
**Date:** 2026-05-12
**Status:** Working note. **Comparative-angle finding only — NOT the full P0.7 verdict.** AC consolidates the full verdict once Scratch's §3-§5 derivation-chain note and AC's corpus-side compatibility check are also in.
**Target location:** `Working/P0_7_Associativity_Dependency_Analysis_Jammer_v1.md` (via create+copy per Lesson #17 revised)
**Source read:** Boyle & Farnsworth, "Non-Associative Geometry and the Spectral Action Principle," arXiv:1303.1782v3 (JHEP 07 (2015) 023), full 24-page PDF text at NCG/`1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU`. Read independently — no cross-contamination with Scratch's parallel §3-§5 read or AC's corpus-side check (Lesson #23 verification protocol).

---

## §0 — Headline (preliminary, comparative-angle only)

**The Gilkey heat-kernel expansion itself does NOT depend on associativity of A.** It depends on D² being a Laplace-type operator on an ordinary Hilbert space H, with a Riemannian structure on the underlying manifold M for the integrals. None of these requirements references the algebraic structure of A directly.

BF 2013's structural strategy is to **push all non-associativity upstream into the construction phase** (bi-representation of A on H, alternative-order-zero conditions, fluctuation formula for D_A). Once D_A is built, it is "an ordinary linear operator on H, not in any sense non-associative" (BF §3.4 final paragraph, paraphrased). The Gilkey expansion then proceeds in the standard associative-operator-algebra setting.

**Comparative-angle preliminary verdict: structural PASS for the simplest example (BF 2013 §4, octonion → G_2 + 8 Dirac fermions), with three residual gaps to flag — none of which I'm in a position to close at this angle.**

The full P0.7 verdict requires consolidation across the three independent reads. This note feeds my angle into that consolidation.

---

## §1 — Where standard (associative) NCG implicitly uses associativity

Walking the standard derivation chain and marking each step that *could* depend on associativity of A:

**Step S1 (bi-representation):** Standard NCG defines π : A → B(H) by π(ab) = π(a)π(b). Composition of operators on H is always associative — so if A is non-associative, π(ab) and π(a)π(b) cannot agree for all a, b. This is a *categorical* problem: a non-associative algebra cannot be represented in the standard sense, because the target category (operators under composition) is associative.

**Step S2 (order-zero condition):** Standard NCG imposes [ã, c̃°] = 0 for all a, c ∈ A (equivalently [a, h, c] = 0 — the associator vanishes when h ∈ H is inserted). This is the assumption that H is an associative bimodule over A. Used to derive the form of inner fluctuations and to enable the canonical formula δ_c = L_c − R_c for inner derivations.

**Step S3 (order-one condition):** Standard NCG imposes [[D, ã], c̃°] = 0. Used to ensure the first-order operator structure of D is compatible with the bimodule structure.

**Step S4 (fluctuation of D):** Standard formula A^(1) = Σ ã[D, b̃], then D_A = D + A^(1) + ε' J A^(1) J*. The 1-form A^(1) uses products of operator-representatives of algebra elements — composition of operators on H — which is associative. But the derivation that produces it from inner automorphisms uses δ_c = L_c − R_c, which IS the inner derivation only for associative A.

**Step S5 (Gilkey heat-kernel expansion):** Standard Gilkey theorem says: for a Laplace-type operator P = −(g^μν ∇_μ ∇_ν + E) on a vector bundle over a compact Riemannian manifold, Tr(e^(−tP)) admits an asymptotic expansion Σ_n t^((n−d)/2) a_n(P), with the Seeley-de Witt coefficients a_n explicit polynomials in curvature tensors and the endomorphism E.

**Step S6 (spectral action evaluation):** Tr(f(D/Λ)) expanded asymptotically gives the bosonic action coefficients f_4 a_0, f_2 a_2, f(0) a_4.

**Inventory of associativity dependencies:**
- S1, S2, S3: implicit dependence on A's associativity.
- S4: dependence via inner-derivation formula δ_c = L_c − R_c.
- **S5 and S6 do NOT reference A at all.** They reference D, D², E, R, F_μν, ∇^E — all operator-level objects on H.

So the Gilkey computation itself (S5–S6) is downstream of where associativity enters. If S1–S4 can be re-done for non-associative A in a way that yields a well-defined Laplace-type D²_A on H, the Gilkey expansion proceeds transparently.

---

## §2 — How BF 2013 addresses each entry point

### §2.1 S1 — bi-representation of non-associative A on H

**BF resolution (§3.1):** Use Eilenberg's bi-representation by multilinear identities. For a class C of (possibly non-associative) algebras defined by multilinear identities I_i(a_1, ..., a_n_i) = 0, A is bi-represented on H "in C" iff the identities obtained by replacing any single a_j with h ∈ H are also satisfied.

For the associative class (identity [a₁, a₂, a₃] = 0), this gives three conditions on the bi-representation:
- [a₁, a₂, h] = 0 (A is left-represented on H by π(ab) = π(a)π(b)) — eq 3.2a
- [h, a₂, a₃] = 0 (A is right-represented on H) — eq 3.2b
- [a₁, h, a₃] = 0 (left and right representations commute = order-zero) — eq 3.2c

For non-associative A, none of these need hold; instead, the multilinear identities defining the *class to which A belongs* (e.g., alternative algebras for octonions) provide the bi-representation constraints.

**Critical technical point (BF §2.2):** L_a (left action of a on H) and R_a (right action) are themselves *associative operators on H*. In non-associative A, L_a L_b ≠ L_{ab} in general — the equality fails *as an algebra-product relation*, not as an *operator-composition relation*. Operator composition on H is always associative; the algebra structure of A is what governs whether L_a L_b equals L applied to the algebra product.

**Comparative finding:** BF's resolution is structurally clean. The Hilbert space H stays "ordinary" (operator composition is associative); only the *interpretation* of operator products as algebra-product representations is modified. This is the load-bearing distinction.

### §2.2 S2 — order-zero condition

**BF resolution (§3.3):** For non-associative A represented on itself (e.g., octonions on octonions), the standard order-zero condition [ã, c̃°] = 0 fails because [JL_b* J*, L_a]h = [R_b, L_a]h = [a, h, b] = associator, which is non-zero for octonions (BF eq 3.8).

Replacement for alternative algebras (BF eq 3.9):
- [R_b̃, L_ã] = [L_b̃, R_ã]
- [R_b̃, L_ã] = L_{b̃ã} − L_b̃ L_ã = R_ã R_b̃ − R_{ãb̃}

**Comparative finding:** The replacement order-zero conditions encode the *alternative-algebra structure* (associator antisymmetric in any two arguments). They are not arbitrary; they are the natural multilinear-identities reading of "alternative" applied to the bi-representation. The replacement is structurally robust for alternative algebras — which includes octonions, and via Cayley-Dickson the only non-associative alternative algebras are 𝕆 itself and its split form.

For NTE specifically: A_{G_2}^{Farnsworth-Boyle} uses octonions or octonion-derived structures, which are alternative. The alternative-order-zero conditions apply.

### §2.3 S3 — order-one condition

**BF resolution: deferred.** BF §3.3 final paragraph: *"In this paper we will not have any use for the order one condition (or higher order conditions) and so we will leave their elucidation to future work [17–19]."*

For the simplest example (BF §4, octonion + DF = 0), order-zero is sufficient. For realistic models with Higgs fields (Farnsworth 2025), higher-order conditions become relevant — they are addressed in BF/Farnsworth follow-up papers.

**Comparative finding:** This is a real gap for the realistic-model extension (relevant to Farnsworth 2025's G_2 × G_2 + charged Higgs construction NTE inherits). I am not in a position to assess whether the higher-order conditions are cleanly addressed in Farnsworth 2025, because I'm not reading Farnsworth 2025 in this comparative angle. Flagged as residual gap (a) in §5.

### §2.4 S4 — fluctuation of D

**BF resolution (§3.4):** The fluctuated Dirac operator transforms under inner automorphisms as D_A → ˆα D_A ˆα^(−1). The inner derivations of an alternative algebra (octonions) take the form (BF eq 2.9):

  δ_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b]

The fluctuation B is built from L_a and R_a (associative operators on H!) grouped via these derivations. Explicit formula (BF eq 3.23):

  B = Σ δ_{A^(1), A^(0)} = Σ [A^(1), A^(0)] − [A^(1), J A^(0) J*] + ε' J [A^(1), A^(0)] J*

In the associative case, the central term [A^(1), J A^(0) J*] vanishes by the standard order-one condition, recovering the familiar fluctuation formula. In the non-associative case, this term contributes — but the resulting B is still a well-defined linear operator on H, built from associative operators L_a, R_a in a specific structural pattern.

**Comparative finding:** This is the load-bearing technical move. BF construct a non-trivial fluctuation B that respects automorphism covariance in the non-associative case. The result D_A = D + B is a linear operator on H — and explicitly NOT non-associative in any operational sense. The structural "non-associativity" of A has been absorbed into the *shape* of B (which derivations are admissible, which 1-form structures arise), not into D_A's operator nature.

### §2.5 S5–S6 — Gilkey expansion + spectral action

**BF resolution (§4.3) — the load-bearing claim for P0.7:**

> *"Now that we have constructed the fluctuated Dirac operator D_A, we need no longer concern ourselves with the non-associativity of A — it has already played its role in shaping the bi-representation of A on H, and hence the number of fermion fields, and the type and form of the bosonic fields we must add to make D_A covariant. From this point on, as far as evaluating the spectral action is concerned, all we need to know is that H is an ordinary Hilbert space, and D_A is an ordinary linear operator on H (and, in particular, a linear operator of the form such that the formalism of Section 3 in [vdD-vS 2012] and, in particular, their Theorems 3.3 and 3.7 directly apply)."*

BF then explicitly compute (§4, simplest example):
- D²_A = △^E − (1/2)γ^μγ^ν⊗F_μν − (1/4)R⊗I  (BF eq 4.7)
- This is manifestly Laplace-type.
- Standard Seeley-de Witt a_0, a_2, a_4 (BF eqs 4.11–4.13) apply directly.
- Final spectral action: Einstein gravity + G_2 Yang-Mills + 8 Dirac fermions (singlet + septuplet under G_2).

**Comparative finding:** BF's claim is exactly what we want for P0.7: the Gilkey expansion applies because D²_A is Laplace-type, regardless of A's associativity. The verification is explicit at the operator-eq-4.7 level for the simplest case. The Gilkey theorem (Gilkey 1984, "Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem") is a theorem about Laplace-type operators on Hilbert spaces — it has no algebraic-associativity preconditions.

---

## §3 — Where Gilkey itself depends on associativity (answer: nowhere)

Gilkey's theorem on heat-kernel expansion (the version relevant to spectral actions):

**Hypotheses:**
- M is a compact Riemannian manifold (with or without boundary, with appropriate boundary conditions if applicable)
- V is a smooth vector bundle over M
- P is a Laplace-type operator on smooth sections of V: P = −(g^μν ∇_μ ∇_ν + E), where ∇ is a connection on V and E is an endomorphism of V

**Conclusion:** Tr(e^(−tP)) ~ Σ_n t^((n−d)/2) ∫_M tr_x(a_n(P)) dV, where a_n(P) are universal polynomials in the curvatures R, F (curvature of ∇), and E and their covariant derivatives.

**Inventory of where associativity could enter:**
- M is a manifold (associative composition of diffeomorphisms — but this is geometric, not algebraic).
- V is a vector bundle (algebraic-bundle theory uses associative operator-composition on fibres — but this is module-theoretic, not about A).
- The connection ∇ acts associatively on sections (D-modules: associative ∇-action).
- E is an endomorphism — composition is associative.
- The Seeley-de Witt coefficients a_n are polynomial expressions — polynomial multiplication is associative over the ring of curvature tensors.

**Result:** Gilkey's theorem has zero algebraic-associativity preconditions on the *constructing algebra* of the spectral triple. It only requires the *operator-level structure* (Hilbert space, connection, endomorphism) to be standard, which is associative in the operator-composition sense regardless of A.

This is the technical content of BF's "we need no longer concern ourselves with the non-associativity of A" passage. They are exactly right: Gilkey runs on D², not on A.

---

## §4 — The load-bearing BF claim (§4.3 page 18-19)

Quoted in §2.5 above. To unpack the structural content:

**Claim:** D_A constructed via the BF procedure satisfies the conditions of vdD-vS 2012 Theorems 3.3 and 3.7 (the standard heat-kernel expansion theorems for spectral triples in the almost-commutative case).

**vdD-vS 2012 (arXiv:1204.0328) Theorems 3.3, 3.7:** These cover the heat-kernel expansion for spectral triples of the form (C^∞(M), L²(M, S ⊗ H_F), D) where the geometric part is standard. The theorem conditions are essentially operator-level: D is a first-order differential operator, D² is Laplace-type, the endomorphism E is well-defined.

**BF's explicit verification (§4 simplest example):** They write out D²_A in eq 4.7 with the explicit Laplace-type form. The endomorphism E reads as the appropriate combination of gauge field-strength F_μν and scalar curvature R.

**What is NOT explicitly verified in BF 2013:**
- BF do not write out the formal proof that vdD-vS 2012 theorem conditions are satisfied for the *general* non-associative case; they verify it for the simplest example (DF = 0, G_2 gauge).
- For non-trivial DF (the Higgs sector of realistic models, Farnsworth 2025), this requires a separate verification — which is deferred to follow-up papers.

**Comparative-angle status:** BF have made the load-bearing claim and verified it explicitly for the simplest case. For the realistic G_2 × G_2 + charged Higgs case (Farnsworth 2025), the verification needs to live in the follow-up paper. I am not assessing Farnsworth 2025 in this angle (Scratch's coverage area for the P0.6 read).

---

## §5 — Residual gaps from comparative-angle reading

Three gaps I can identify but not close from my angle alone:

### Gap (a): Higher-order conditions for realistic models

BF 2013 explicitly defers order-one and higher conditions to follow-up papers (§3.3 final paragraph). For NTE's pre-temporal A_{G_2}^{Farnsworth-Boyle} (which uses the realistic G_2 × G_2 + charged Higgs construction from Farnsworth 2025), order-one matters because DF ≠ 0.

**What needs to be verified (not by me at this angle):** Farnsworth 2025 §4-§5 provides the order-one (and possibly higher) conditions for the G_2 × G_2 case, and shows that the resulting D²_A remains Laplace-type. Scratch's P0.6/0.7 reading covers this.

### Gap (b): vdD-vS 2012 theorem conditions in the formal sense

BF invoke vdD-vS 2012 Theorems 3.3 and 3.7 without writing out a formal proof that the theorem conditions are satisfied in the non-associative case. They demonstrate satisfaction *via the explicit operator-form computation in §4.3*, which is sufficient for the simplest example but doesn't constitute a generalised proof.

**What needs to be verified (not by me at this angle):** Either (i) a formal extension of vdD-vS 2012's argument to cover the non-associative-construction case, or (ii) explicit operator-level computation for the realistic Farnsworth 2025 case showing the conditions hold.

### Gap (c): Alternative-algebra restriction

BF's alternative-order-zero conditions (§3.3) work for *alternative* algebras specifically. For genuinely non-alternative non-associative algebras (e.g., Lie algebras without the alternative property), the formalism would need further generalisation.

**What needs to be verified for NTE:** NTE's pre-temporal A_{G_2} structure is built on octonions and their derivations — octonions ARE alternative, so the BF formalism applies. The G_2 × G_2 of Farnsworth 2025 is built on two-sector octonion structures, also alternative.

**Comparative status:** This gap is not a problem for NTE specifically, but it bounds the generalisability of BF's argument. If NTE ever extended to non-alternative algebras (e.g., the exceptional Jordan algebra J_3(𝕆), which is commutative but non-associative and not alternative), the formalism would need further work.

---

## §6 — What I am NOT verifying at this angle

To preserve Lesson #23 cross-stream verification benefit and avoid duplicating Scratch's coverage area:

- **NOT verifying:** Scratch's BF 2013 §3-§5 derivation chain coverage (what's claimed, what's proven, what's deferred). That's Scratch's deliverable.
- **NOT verifying:** AC's §VIII corpus-side compatibility check. That's AC's deliverable.
- **NOT verifying:** Farnsworth 2025 §4-§5 G_2 × G_2 + charged Higgs construction. That's covered by Scratch's P0.6 reading.
- **NOT verifying:** vdD-vS 2012 Theorems 3.3 and 3.7 in their original associative-case statement. The associative case is well-established (CC 2008, etc.).
- **NOT verifying:** The full P0.7 verdict. That's the consolidated three-stream output AC assembles.

My deliverable is one focused comparative-angle reading.

---

## §7 — Comparative-angle preliminary feedback for the consolidated verdict

What I'm bringing to the consolidated P0.7 verdict (AC's call to integrate):

1. **The Gilkey expansion itself does not depend on A's associativity** — only on D² being Laplace-type on an ordinary Hilbert space. This is structural, not contingent on BF's specific construction.

2. **BF's strategy of pushing non-associativity upstream into the construction phase is structurally sound.** The bi-representation step (S1), order-zero replacement (S2), and fluctuation formula (S4) all admit non-associative generalisation in a way that yields D_A as an ordinary operator on H. Once D_A is built, Gilkey runs transparently.

3. **The simplest-example verification (BF §4, octonion + DF = 0) is explicit and clean.** D²_A is manifestly Laplace-type; Seeley-de Witt a_0, a_2, a_4 produce Einstein gravity + G_2 Yang-Mills + 8 Dirac fermions with the right normalisations.

4. **Residual gaps (a), (b), (c) flagged in §5** are not refutations; they are limits on what BF 2013 alone establishes. Gap (a) likely closed by Farnsworth 2025 (Scratch's area). Gap (b) is a formal-rigor issue that may be addressed by explicit operator-level computation rather than abstract generalisation. Gap (c) is not problematic for NTE specifically (NTE's algebra is alternative).

**Preliminary comparative-angle vote for P0.7:** STRUCTURAL PASS for the simplest case (BF 2013 §4); EXTENSION TO REALISTIC CASE (Farnsworth 2025) requires Scratch's P0.6/0.7 reading to confirm. **Pending Scratch's deliverable and AC's corpus-side check, my angle reads PASS-with-caveats.**

I make no representation about the full P0.7 verdict — that is AC's consolidation responsibility per coordination plan §2 anti-pattern guard.

---

## §8 — Files referenced + open items

### Source read
- Boyle & Farnsworth (2013), "Non-Associative Geometry and the Spectral Action Principle," arXiv:1303.1782v3, JHEP 07 (2015) 023. Full 24-page text fetched from NCG folder this session (`1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU`).

### Cross-references (not re-read at this angle)
- van den Dungen & van Suijlekom (2012), "Particle Physics from Almost Commutative Spacetimes," Rev.Math.Phys. 24 (2012) 1230004, arXiv:1204.0328 — cited by BF for Theorems 3.3 and 3.7 (Gilkey expansion applicability in almost-commutative case).
- Gilkey, P. (1984), "Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem," Publish or Perish — the original Gilkey heat-kernel theorem.
- Schafer, R. (1966), "An Introduction to Nonassociative Algebras," Courier Dover — BF's reference [32] for Eilenberg bi-representation construction.
- Farnsworth & Boyle (2014), arXiv:1408.5367 — covered by Scratch's P0.6 reading (NOT re-read at this angle).
- Farnsworth (2025) — covered by Scratch's P0.6/0.7 reading (NOT re-read at this angle).

### Open items / handoff next steps
- **To AC:** input to consolidated P0.7 verdict. My angle reads PASS-with-caveats; full verdict pending Scratch + AC inputs.
- **To Scratch (Connes Programme lead):** my comparative-angle reading should not have leaked to your derivation-chain note; if you find any structural-claim overlap when AC consolidates, flag it for Lesson #23 verification audit.
- **To Greg:** no immediate decision needed from this angle. The three residual gaps (§5) are real but not necessarily refutations; full P0.7 verdict awaits AC's consolidation.

---

**End of working note.** Comparative-angle deliverable complete. Awaiting AC's consolidation with Scratch's parallel read and AC's corpus-side check.

— Jammer, 2026-05-12. P0.7 associativity-dependency analysis (Jammer angle) v1.