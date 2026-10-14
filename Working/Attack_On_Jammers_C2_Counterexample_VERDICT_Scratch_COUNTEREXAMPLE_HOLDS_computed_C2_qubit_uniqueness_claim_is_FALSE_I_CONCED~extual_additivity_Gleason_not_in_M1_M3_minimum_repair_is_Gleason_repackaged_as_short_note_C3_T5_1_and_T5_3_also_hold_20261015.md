# VERDICT — Scratch: attack on Jammer's C2 counterexample. **The counterexample HOLDS (computed). C2's qubit-uniqueness claim is FALSE. I concede: my PUBLISHABLE grade was wrong.**

**One line, first and unsoftened:** I was tasked to attack the counterexample; I computed it and it survives every attack. **C2's central uniqueness claim is false as stated**, the paper **names the counterexample and misstates why it fails**, and **the exponent is fixed only at n ≥ 3 by non-contextual additivity (Gleason), which is not in M1–M3.** My earlier grade of C2 as PUBLISHABLE was wrong, and I correct it to **NOT PUBLISHABLE as a research paper** — salvageable only as a short expository note (Gleason repackaged). I converge with Jammer.

**Stream:** Scratch, per `Directive_AC_to_Scratch_Attack_Jammers_C2_Counterexample_20261015.md`. **Register:** adversarial check on a counterexample, by computation. Nothing patched; no Core. No-f.
**My stake, declared:** I graded C2 PUBLISHABLE in `Working/Publication_Readiness_...VERDICT_Scratch_...20261015.md`. The honest outcomes available here were: (i) counterexample fails → C2 stands → I was right; (ii) counterexample holds → C2 false → **I was wrong.** It is (ii). I did not defend the prior; I computed.
**Reads:** C2 at current state (verbatim quoted below), C3 §4/§5/§6 (for the second ask), this session.

---

## 1. The counterexample, computed (AC's question 1)
**P(x) = sin²(πx/2) with x = |⟨φ|ψ⟩|²:**
- **Normalised on the qubit:** orthonormal pair ⇒ x₂ = 1 − x₁; sin²(π(1−x₁)/2) = sin²(π/2 − πx₁/2) = cos²(πx₁/2); so P(x₁) + P(x₂) = sin²(πx₁/2) + cos²(πx₁/2) = **1**, for all x₁. ✓
- **Smooth** on S³ (composition of smooth maps) ✓; **U(1)-invariant** (depends only on |z|²) ✓; **invariant under joint SU(2) rotation** (function of the scalar |⟨φ|ψ⟩|², itself joint-SU(2)-invariant) ✓.
- **Fails only off the qubit:** at n = 3, (r₁,r₂,r₃)=(0.2,0.3,0.5): sin²(0.1π)+sin²(0.15π)+sin²(0.25π) = 0.0955 + 0.2061 + 0.5000 = **0.8016 ≠ 1.** So three-outcome additivity fails; two-outcome (qubit) normalisation holds.
- **A whole family passes at n=2:** f(r) = r + ε·sin(2πr): f(r)+f(1−r) = 1 + ε[sin(2πr) + sin(2π−2πr)] = 1 + ε[sin(2πr) − sin(2πr)] = **1.** ✓ (smooth, U(1)- and joint-SU(2)-invariant for small ε).
**Conclusion: the counterexample is valid.** AC's own quick check is confirmed by direct computation.

## 2. Does it meet C2's constraints *as C2 states them* (AC's question 2)
C2 abstract, verbatim: *"the only smooth function from S³ to [0,1] that is simultaneously U(1)-invariant, SU(2)-equivariant, and correctly normalised — with normalisation, additivity across basis partitions, continuity, and consistency under SU(2)-rotated bases jointly forcing linearity in |z|² — is |z|²."*
- The four headline constraints (smooth, U(1)-inv, SU(2)-equiv, normalised): sin² meets **all four** on S³ (§1). So the headline claim "the only smooth function from S³…" is **false**.
- The extra forcing conditions C2 lists — "additivity across basis partitions," "continuity," "consistency under SU(2)-rotated bases":
 - **Continuity:** sin² is continuous. Passes.
 - **Consistency under SU(2)-rotated bases:** P = f(|⟨φ|ψ⟩|²) uses the **same f in every basis**, so it is automatically consistent across rotated bases. sin² **passes** this too. (Jammer is right that this clause does not bite.)
 - **Additivity across basis partitions:** at n=2 this is just complementarity f(r)+f(1−r)=1, which sin² satisfies. It excludes sin² **only at n ≥ 3** ("higher-dimensional partitions"), i.e. **only by leaving the qubit S³** — the paper's own stated domain.
**So even against C2's full stated constraint list, uniqueness fails on S³.** It holds only on S^{2n−1}, n ≥ 3, via additivity — **not in M1–M3** (M1–M3 are the qubit).

## 3. Is there an unstated constraint that makes C2 repairable? (AC's question 3) — YES, and it is Gleason
The repair is to **add non-contextual additivity over partitions at n ≥ 3** as an explicit input. With it, f(r₁)+f(r₂)+f(1−r₁−r₂)=1 is Cauchy's equation; continuity forces **f(r)=r**. That is exactly **Gleason's theorem** (non-contextual measure on projections, d ≥ 3). So C2 is **repairable but not as stated**: the exponent is fixed by non-contextual additivity (Gleason), **not** "on S³ by the Hopf map." Consequences:
- The claim **"the exponent is the topological signature of the Hopf map"** is wrong: the quadratic is the **Hermitian norm |z|²** (= M1), and normalisation alone excludes f=√ but **not** f=sin² (so normalisation does not force exponent 2). **Confirmed.**
- §6's **"non-contextuality emerges as a consequence of the Hopf projection"** is false: the additivity-over-partitions step **assumes** the probability of an outcome is independent of which basis completes it — that **is** non-contextuality, assumed, not emergent. **Confirmed.**
- The abstract/§1 **"axiom without derivation since 1926 / never been derived"** contradicts C2's own **Gleason 1957** citation in §6. **Confirmed internal contradiction.**
- The **Layer-1 + Layer-2 reduction** of P to f(|⟨φ|ψ⟩|²) (§3.3) **is correct and is all that survives.** **Confirmed.**

## 4. Does C2 name the function and misstate its failure? (AC's question 4) — YES
C2 §3.3 "Selecting f(r)=r", verbatim: *"Any nonlinear f compatible with complementarity (e.g. sin²(πr/2)) fails additivity over higher-dimensional partitions, **or** fails consistency when SU(2) rotates the basis."* The **"or … consistency when SU(2) rotates the basis"** disjunct is **false** — sin² uses the same f in every basis and is consistent across rotated bases. Only the "additivity over higher-dimensional partitions" disjunct is true, and that one **contradicts the paper's claim that the exponent is fixed on the qubit S³**, because higher-dimensional partitions mean n ≥ 3. So the paper names its own counterexample and gives a disjunctive disqualification whose SU(2) half is wrong and whose additivity half refutes the on-S³ uniqueness thesis. **A referee finds this immediately.**

## 5. The minimum repair that saves the *result* (AC's key ask — I am the lane to answer it)
The salvageable **true** statement:
> *The phase-stabiliser symmetry — global U(1) unobservability (M2) together with the stabiliser of the measurement axis within SU(2) (M3) — reduces any qubit probability rule to f(|⟨φ|ψ⟩|²). At n = 2 this f is **not** unique (counterexample family: sin²(πr/2); r + ε sin 2πr). The Born value f(r)=r is forced only at n ≥ 3, by non-contextual additivity over partitions — i.e. by Gleason's theorem. The contribution is a geometric/gauge-symmetry repackaging of the Gleason route, not a uniqueness result on the qubit and not a topological consequence of the Hopf map.*

Changes to reach it (converging with Jammer's fix list): **retitle**; **strike** the qubit-uniqueness claims (abstract, §3.3 last para, §3.4 final sentences, §6 "non-contextuality emerges"); **add** the n=2 counterexample family; **state** n ≥ 3 non-contextual additivity as an explicit input; **fix Fact 3** ("the unique non-trivial principal U(1) bundle over S²" → Hopf is the c₁=±1 generator, the one with total space S³; bundles are classified by c₁∈ℤ); **strike** "since 1926 / never derived"; **strike** §7.2's Cayley–Dickson descent and the G₂→SM material; **drop** the C6 dependency; **cite Gleason** (and Busch 2003 for the d=2 POVM route). Note the exponent is the **Hermitian norm**, not Hopf topology.
**As a research paper: NOT PUBLISHABLE** (central novel claim false). **As a short expository note after the above: publishable but likely judged non-novel** (it is Gleason, geometrically narrated) — the novelty check is Cursor's literature leg.

## 6. Second ask — C3 T5-1 and T5-3 (brief, computed)
- **T5-1 (C3's thesis is a category error) — HOLDS.** Spectra belong to **operators**, not to the unit sphere of the Hilbert space. The Laplacian eigenfunctions on S³ live in **L²(S³)** (Peter–Weyl: ⊕ spin-j blocks), a different space from the qubit ℂ² whose states *are* points of S³. And discreteness of a Hamiltonian's spectrum depends on the operator + boundary conditions, not on compactness of the state-space sphere (hydrogen vs free particle: same L²(ℝ³), different spectra; the unit sphere of an ∞-dim Hilbert space is not even compact). "Discreteness because the state space is compact" conflates two different Hilbert spaces. Confirmed; C3 §4 "Energy" concedes the real mechanism (potential + normalisability), which **contradicts** the thesis — defect (c) is worse than heuristic.
- **T5-3 (CCR = symplectic structure of a compact phase space) — HOLDS.** [x̂,p̂]=iℏ has **no finite-dimensional representation** (trace of a commutator is 0, trace of iℏ·1 is not). A compact phase space ⇒ finite-dimensional Hilbert space ⇒ **no** [x̂,p̂]=iℏ (one gets Weyl clock-and-shift relations instead). Kostant–Souriau does not say what §5 attributes to it. Confirmed.
So on C3 I also converge with Jammer: T5-1 and T5-3 both hold.

## 7. Recognition-gate: the class of my error
My PUBLISHABLE grade for C2 rested on reading §3.3's "these force f linear" and §7's honest scope-language and **not computing the counterexample the paper itself names.** That is the "rule from reading, not computing / accept a source's own claim without checking" failure — the exact class Greg made standing practice to prevent. Re-examining the class in my prior readiness verdict: C1/C3/C6 I graded NOT-publishable / after-fixes (converging with Jammer), so the over-rating was isolated to C2 — but the **mechanism** (trusting a paper's stated forcing argument instead of testing its named counterexample) is the lesson, and it is why "compute, do not reason" is the right standing rule for any uniqueness claim. I should have computed sin² before grading C2.

## 8. Routing
- **C2: the counterexample holds; uniqueness claim false; NOT PUBLISHABLE as a research paper; repair = Gleason-repackaged short note per §5.** I converge with Jammer on C2, C1, C3, C6 (all NOT PUBLISHABLE) and on the spine.
- **The G₂ rank obstruction (Jammer §G)** — G₂ has rank 2, SM group rank 4, so "G₂ → SM as subgroup breaking" is impossible by rank; it bears on C16 §3 and Part 1's "gauge group from G₂" simplification, and on my own Task A axiom A9. **Flag: AC should commission the C16 §3 retest Jammer recommends** — it also affects A9's status in my axiom audit.
- AC adjudicates (both bodies now computed-convergent) → Greg rules publication. Nothing patched.

— Scratch, 2026-10-15. **Counterexample HOLDS; C2 uniqueness FALSE; I concede my PUBLISHABLE grade (wrong).** Exponent fixed only at n≥3 by non-contextual additivity (Gleason), not in M1–M3; paper names sin² and misstates its failure; minimum repair = retitled Gleason-repackaged note. C3 T5-1 and T5-3 also hold. Converges with Jammer. Routed to AC → Greg.
