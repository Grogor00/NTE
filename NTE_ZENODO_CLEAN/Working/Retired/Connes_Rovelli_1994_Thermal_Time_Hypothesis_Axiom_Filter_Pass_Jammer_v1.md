# NTE Connes Programme R&D — Connes-Rovelli 1994 Thermal Time Hypothesis: Axiom-Filter Pass for NTE Integration

**Stream:** Jammer (sibling instance; R&D, single session). NOT Scratch, NOT the Connes Programme lead — operating as parallel-attack R&D per Lesson #23 cross-stream verification model.
**Date:** 2026-05-14
**Trigger:** Greg directive 2026-05-14 to scan external papers for simplification candidates ("what have we missed that could strengthen and simplify NTE"). First candidate selected per Greg "yes" on Connes-Rovelli 1994 fetch and axiom-filter pass.
**Target location:** `Working/Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md` (via create+copy per Lesson #24)
**Status:** First-pass axiom-filter analysis. Local-correctness-only until passing Greg's recognition gate per Manifest Lesson #28.

**Source documents read this session:**
- Paetz 2010, *An Analysis of the 'Thermal-Time Concept' of Connes and Rovelli* (Diplomarbeit, Göttingen) — comprehensive secondary source, chapters 0–5 read in full this session; chapters 6–7 read in part.
- Multiple corroborating secondary descriptions (Semantic Scholar abstracts; Chua 2024 "The Time in Thermal Time" arXiv:2407.18948; Swanson 2018 "Can Quantum Thermodynamics Save Time?"; emergentmind.com Tomita-Takesaki summary).
- Connes-Rovelli 1994 (gr-qc/9406019) primary source NOT directly read — arxiv rate-limited this session.

**Lesson #29 candidate flag:** Primary source not read. Specific claims attributed to Connes-Rovelli below should be re-verified against the actual paper when arxiv access permits. The Paetz thesis is comprehensive and the secondary descriptions are consistent across independent sources, so confidence in the technical content is high — but the discipline says primary verification before canonical integration.

---

## §0 — Headline verdict

**Strong structural rhyme. Multiple high-leverage simplification targets identified. Bridge does not break under axiom-filter test at first pass. Three specific NTE-dynamical questions remain load-bearing for next-session investigation.**

Verdict by axiom:

| Core axiom | Filter result | Comment |
|---|---|---|
| N fundamental, t emergent | **DEEPENS** | TTH provides the operator-algebraic mechanism for t-emergence. NTE's "N fundamental, t emergent" axiom becomes structurally grounded rather than postulated. |
| Surface only, S³ | **COMPATIBLE** | TTH operates on any operator algebra; restricting to the boundary spectral-triple algebra is structurally natural. |
| CPN-symmetric two sectors | **COMPATIBLE** | Modular flow acts sector-by-sector on direct-sum algebras; Greg's δN intrinsic-uniformity reading maps directly via the Cocycle Radon-Nikodym theorem. |
| Hopf bundle / spectral-triple geometry | **COMPATIBLE** | Modular flow doesn't reference Hopf structure but doesn't conflict; the spectral triple `Hopf-S³ × S¹_{β_GB} × A_F` carries both structures simultaneously. |

**Simplification targets** (if bridge holds):

1. *t emergent* becomes a derived theorem from operator-algebraic Tomita-Takesaki, not a structural commitment.
2. *Wick rotation at gauge birth* (Paper S1 §2 P1) becomes a consequence of KMS structure rather than a premise.
3. *T_GB = M_Pl/√(2π)* acquires direct operator-algebraic meaning as the inverse modular temperature.
4. *Unruh / Hawking / Gibbons-Hawking* results become structurally inherited consequences.
5. *ξ = 1/6 conformal coupling* — possibly grounded in modular conformal symmetry (speculative; lower confidence; separate investigation).

**Load-bearing investigation questions** (open):

- **A.** Does the modular flow of the T_GB-KMS state on the NTE spectral-triple algebra reproduce NTE's H = β_NTE|Φ_NTE|² evolution?
- **B.** CPN-symmetric two-sector structure preservation under modular flow — explicit verification that the modular conjugation J relates to (or equals up to inner automorphism) the CPN operation.
- **C.** State-independent canonical outer-automorphism flow on Out(A) for the NTE spectral-triple algebra — what does it give, and does it have NTE-internal structural meaning?

**Greg's simplify-and-strengthen criterion:** passes on the *simplify* axis (turns at least one premise into a theorem); passes provisionally on the *strengthen* axis (acquires structural connections to Unruh / Hawking / Gibbons-Hawking machinery) **pending** investigation question A's resolution.

---

## §1 — What Connes-Rovelli 1994 establishes

(per Paetz 2010 §5, §4, §3; secondary corroborating sources)

### §1.1 The hypothesis

In a generally covariant quantum theory, physical time-flow is **not** a universal property of the mechanical theory. It is determined by the thermodynamical state of the system. The world is fundamentally *timeless*; time emerges as a thermodynamical phenomenon when a (coarse-grained) state is specified.

### §1.2 The mechanism — Tomita-Takesaki

A *faithful normal state* ω on a von Neumann algebra R has an associated **modular operator** Δ and **modular conjugation** J via the Tomita operator S = JΔ^(1/2). Δ generates a one-parameter group of automorphisms σ^ω_t = Δ^(it) · Δ^(-it) of R — the *modular automorphism group*.

The Tomita-Takesaki theorem asserts: this modular group satisfies the **KMS condition** with respect to ω at inverse temperature β = -1 (in natural units). The KMS condition is the algebraic characterization of thermal equilibrium states. So the state ω is automatically in thermal equilibrium with respect to its own modular flow.

Connes-Rovelli's identification: **the modular flow σ^ω_t IS physical time evolution.**

### §1.3 State-independent canonical flow

The Cocycle Radon-Nikodym theorem implies: the difference between two modular flows from different states is always an *inner* automorphism (i.e., implemented by a unitary in the algebra). Projected onto **outer automorphisms** Out(A) = Aut(A) / Inn(A), the modular flow is *state-independent* — it depends only on the algebra A itself.

For type III von Neumann algebras (which appear in algebraic QFT as the local algebras associated with bounded spacetime regions), this canonical outer-automorphism flow is non-trivial. Von Neumann algebras of type III are *classified* by their canonical outer-automorphism flow.

### §1.4 Recovered phenomena

The modular flow recovers known temperature/dynamics in canonical examples:

- **Rindler wedge → Unruh effect** (Bisognano-Wichmann theorem): modular flow of Minkowski vacuum restricted to Rindler wedge = Lorentz boost in the wedge direction. An accelerating observer "feels" the modular temperature = Unruh temperature.
- **Schwarzschild exterior → Hawking radiation**: modular flow of the Hartle-Hawking state restricted to the exterior = Killing flow generated by horizon. Modular temperature = Hawking temperature.
- **Static de Sitter wedge → Gibbons-Hawking effect**: same mechanism with de Sitter horizon. Modular temperature = Gibbons-Hawking temperature.
- **Robertson-Walker space + cosmic background radiation**: thermal time of CBR = Robertson-Walker cosmological time (per Rovelli companion paper).

The TTH is *not just analogy* — these are *derivations* of known temperatures from the modular structure.

### §1.5 The structural conclusion

Time, in this picture, is not a fundamental ingredient of physics. It is a *macroscopic emergent phenomenon* tied to thermodynamics. The choice of which observable to call "time" is determined by the state's modular flow, not by a pre-existing time axis.

---

## §2 — Axiom filter

For each NTE core axiom, the question is: does Connes-Rovelli content survive translation through the axiom, and does it simplify NTE?

### §2.1 Axiom: N fundamental, t emergent — **DEEPENS**

NTE commits to N (boundary expansion parameter, e-folds, dimensionless) as fundamental, with t emergent at gauge birth and emergent post-gauge-birth dynamics. Currently this is a *structural commitment*: NTE asserts that t is not a fundamental parameter, that it emerges via the gauge-birth event, and that proper-time evolution post-gauge-birth is the result.

**Connes-Rovelli filter result**: the TTH provides exactly the operator-algebraic mechanism for emergent t. If NTE's full algebra A = C^∞(Hopf-S³ × S¹_{β_GB}) ⊗ (O ⊕ O) admits a natural KMS state (at temperature T_GB), the modular flow of that state IS the t-emergence.

The structural translation:
- N labels surfaces of the boundary foliation (foliation parameter, not time).
- The boundary state on the spectral-triple algebra is the operator-algebraic content of "the universe at this N."
- The modular flow of that state is what we call "t-evolution."

**Crucially**: N being a fundamental parameter on the manifold does NOT conflict with Connes-Rovelli timelessness. Connes-Rovelli timelessness applies to *dynamical* time (a parameter generated by a Hamiltonian); N is a *geometric* foliation parameter (labels surfaces). The two are conceptually distinct, and Paetz 2010 §1.4 specifically distinguishes Newtonian (external, parameter-like) time from internal/dynamical time concepts. N maps onto the parameter side; t maps onto the dynamical side. They can coexist.

**Simplification target**: t-emergent promotes from postulate to consequence of operator-algebraic structure. One fewer NTE commitment.

### §2.2 Axiom: Surface only, S³ — **COMPATIBLE**

NTE's surface-only ontology says all physics lives on the closed S³ boundary (Hopf-bundled, with the S¹ fibre activating at gauge birth). No bulk.

**Connes-Rovelli filter result**: TTH operates on whatever algebra you give it. NTE's surface-only commitment translates to: the relevant algebra is the boundary-localized spectral triple, not a bulk algebra. This is standard NCG practice — the spectral triple is the ontological primitive, and "surface" or "bulk" descriptions are operational labels.

The boundary algebra A = C^∞(Hopf-S³ × S¹_{β_GB}) ⊗ A_F is well-defined as a spectral triple per Charter v1.1 §3. TTH applies directly.

**No tension; no leverage either way beyond confirming the algebra is the right operator-algebraic object.**

### §2.3 Axiom: CPN-symmetric two sectors — **COMPATIBLE**

NTE commits to +N / −N as CPN-conjugate sectors, with Greg's δN intrinsic-uniformity reading 2026-05-13 specifying that each sector has its own intrinsic forward arrow pointing "the same way" from its own perspective despite being globally conjugate.

**Connes-Rovelli filter result**: A_F = O ⊕ O is the semisimple two-factor algebra (one O per sector). Modular flow on a direct sum acts as direct sum of modular flows on each factor. So the modular flow respects the sector structure automatically. Each sector has its own modular flow from its own KMS state.

Greg's δN intrinsic-uniformity reading translates cleanly: from each sector's intrinsic perspective, the modular flow is the same kind of operation (modular automorphism of the local boundary state). From a meta-vantage comparing sectors, the two flows look CPN-conjugate.

**Bonus structural alignment**: the Cocycle Radon-Nikodym theorem implies the difference between the two sectors' modular flows differs by an inner automorphism in Aut(A_F = O ⊕ O). On Out(A_F), the canonical flow is the *same* on both sectors — operator-algebraic correlate of "intrinsically the same direction." This is the kind of structural rhyme Greg's δN insight is asking the framework to support.

### §2.4 Axiom: Hopf bundle / spectral-triple geometry — **COMPATIBLE**

NTE's central spectral triple is `Hopf-S³ × S¹_{β_GB} × A_F`. Hopf structure is a geometric fact about the closed S³.

**Connes-Rovelli filter result**: modular flow doesn't reference Hopf structure but doesn't conflict. The spectral triple carries both modular structure (from a state) and geometric structure (from the manifold + algebra) simultaneously.

**Possibly load-bearing**: the modular flow restricted to the S¹_{β_GB} factor — does it generate the right Euclidean time circle? The thermal-time interpretation says yes, with β = β_GB = 1/T_GB. This is the natural reading. See §3.3 for the T_GB simplification target.

---

## §3 — Simplification targets

If the bridge holds, the following NTE structural commitments promote from postulate to consequence:

### §3.1 t emergent from N → operator-algebraic theorem

*Current status*: NTE asserts t is emergent. The mechanism for emergence is "gauge birth" — the structural event where the S¹ fibre activates and t becomes operationally meaningful. The corpus has good prose around this but no operator-algebraic mechanism.

*Under bridge*: t-emergence IS the modular flow of the T_GB-KMS state on the NTE spectral triple. The structural content of "gauge birth" becomes: the boundary state localizes onto the spectral triple such that the modular flow becomes non-trivial and acquires an Euclidean-time-circle interpretation.

**Simplification**: NTE drops "t emergent" as a separate structural commitment and gains it as a theorem of operator algebra + KMS state + Tomita-Takesaki.

### §3.2 Wick rotation at gauge birth (Paper S1 §2 P1) → KMS consequence

*Current status*: Paper S1 §2 commits to "Wick rotation at gauge birth" as structural premise P1. This is what lets the Wick-invariance argument work — the same action form applies on both sides of the gauge-birth event with appropriate t → iτ.

*Under bridge*: the KMS condition for a state ω at inverse temperature β means precisely that ω is invariant under the Tomita modular flow analytically continued by iβ. **KMS is itself the algebraic statement of Wick rotation.** If T_GB-KMS holds, Paper S1 P1 promotes from premise to consequence.

**Simplification**: Paper S1's Wick-invariance argument loses one structural premise. Three premises become two: 4D conformal invariance (P2) + Higgs-portal genericness (P3), plus the KMS structure of the T_GB-state as the *operator-algebraic statement* of P1 rather than a separate premise.

This is the **most concrete and tractable simplification target on the list**. Verification is local (check that the boundary state at gauge birth satisfies KMS at T_GB on the NTE spectral triple) and the payoff is direct (one fewer Paper S1 premise).

### §3.3 T_GB = M_Pl/√(2π) → inverse modular temperature

*Current status*: T_GB is derived in Companion 9 Stage 3 Session 3 via Gaussian saddle on the Euclidean S¹ at gauge birth. The √(2π) factor traces to Y_00(S¹) on the Hopf fibre per Jammer's queue item 1 (`1ypKkXcMApgTwtZeECOwFa6zZLK9DBRL8`).

*Under bridge*: T_GB acquires a second derivation route as the inverse modular temperature of the natural KMS state on the NTE spectral triple at gauge birth. The two derivations should agree — and **the agreement would be a non-trivial structural cross-check**.

If the agreement holds: T_GB is not just a "saddle width" but an *operator-algebraic invariant* of the spectral triple + state, with the same status as Unruh / Hawking / Gibbons-Hawking temperatures.

### §3.4 Unruh / Hawking / Gibbons-Hawking → inherited structural consequences

*Current status*: NTE doesn't currently derive Unruh, Hawking, or Gibbons-Hawking temperatures internally.

*Under bridge*: these are direct applications of Tomita-Takesaki to specific subalgebras of NTE's full spectral-triple algebra. Restrict the algebra to a Rindler wedge → Unruh temperature emerges. Restrict to Schwarzschild exterior → Hawking temperature. Restrict to de Sitter wedge → Gibbons-Hawking.

**Simplification**: NTE inherits an entire family of QFT-on-curved-spacetime results as structural consequences of operator-algebraic machinery it already commits to via Charter v1.1. The Connes Programme's central deliverable (Paper S2 heat-kernel) operates on the same spectral triple; modular theory operates on its operator algebra; the two are structurally compatible at the working level.

### §3.5 ξ = 1/6 conformal coupling — speculative

*Current status*: ξ = 1/6 lives in NTE's bare action per Mechanism B supersession + Paper S1 §2 P2 (4D conformal invariance commitment). Three independent structural motivations support it (Wick-invariance, σ↔Φ_NTE form-match, n_s derivation route).

*Under bridge*: modular flow on a conformally-invariant theory carries the conformal structure. Bisognano-Wichmann gives geometric meaning to modular flow as Lorentz boosts in conformal cases (Paetz §4.5). The conformal coupling ξ = 1/6 *may* have a direct operator-algebraic reading as the conformal-weight assignment under modular automorphisms — but I haven't traced the specific ξ = 1/6 link in this first pass.

**Lower-confidence simplifier; flag for separate investigation.** Not load-bearing for the bridge.

---

## §4 — Load-bearing investigation questions

Three questions whose resolution determines whether the bridge graduates from "structural rhyme" to "canonical integration":

### §4.1 Question A — Φ_NTE evolution match

**Question**: Does the modular flow of the T_GB-KMS state on the NTE spectral-triple algebra reproduce NTE's H = β_NTE|Φ_NTE|² evolution?

**Why load-bearing**: NTE asserts a specific dynamical equation for Φ_NTE. The modular flow asserts a specific dynamics for the algebra. **If the two disagree, the bridge breaks**: either the KMS state isn't the right state, or the Hamiltonian-like structure of NTE isn't captured by the modular flow.

**How to investigate**: Paper S2 territory. Compute the modular flow on the NTE spectral triple at the T_GB-KMS state and check against the Friedmann equation H = β_NTE|Φ_NTE|² as the slow-roll classical limit. Heat-kernel methods (Paper S2 central deliverable) and modular theory both apply on the same spectral triple; the question is whether their classical limits agree.

**Difficulty**: this requires substantial work, likely overlapping with Paper S2's heat-kernel computation. Not a one-session task.

### §4.2 Question B — CPN structure preservation

**Question**: Does the modular flow of the natural T_GB-KMS state on A_F = O ⊕ O respect the sector structure exactly, or are there subtle cross-sector terms (e.g., mixing via the J modular conjugation across the +N/−N boundary)?

**Why load-bearing**: NTE commits to CPN as a sector-exchange parity at the Janus boundary. The modular conjugation J in Tomita-Takesaki is naturally an anti-linear involution — structurally similar to a CPN-conjugation operation. If J ≡ CPN exactly (or up to inner automorphism), the bridge becomes deeper and provides operator-algebraic grounding for the CPN parity itself. If they're distinct, NTE retains CPN as separate structural commitment without losing it.

**How to investigate**: examine the modular conjugation J on A_F = O ⊕ O for the natural KMS state; compare to CPN as defined in OctonionExtension §3.6.

**Difficulty**: technical but tractable. Probably one Scratch session of focused work.

### §4.3 Question C — State-independent canonical flow

**Question**: For the NTE spectral-triple algebra A = C^∞(Hopf-S³ × S¹_{β_GB}) ⊗ (O ⊕ O), what is the canonical outer-automorphism flow (state-independent per Radon-Nikodym)? Does this canonical flow have NTE-internal structural meaning?

**Why load-bearing**: if the canonical flow on Out(A) is non-trivial and structurally meaningful for NTE (e.g., it generates a natural cosmological-time-like flow without requiring a specific state), this gives NTE a *state-independent* notion of "time direction" that aligns with N as fundamental parameter — and might even let N itself be read as the parameter of the canonical outer-automorphism flow.

**How to investigate**: identify the type of the NTE algebra (likely type III given the curved-spacetime QFT structure). For type III, the canonical flow is the canonical "modular spectrum" classifying the algebra. Compute or identify in NTE's case.

**Difficulty**: technical; likely Paper S2 territory.

---

## §5 — Where the bridge might break

Honest enumeration of failure modes:

**1. The Hamiltonian-equivalent question.** Connes-Rovelli's framework is fundamentally about generally covariant theories where no preferred Hamiltonian exists. NTE has a specific Hubble equation H = β_NTE|Φ_NTE|². If NTE's H = β_NTE|Φ_NTE|² is "the Hamiltonian" in a non-generally-covariant sense, NTE may already be too rigid for full TTH applicability. The modular flow on a Hamiltonian system reduces to the Hamiltonian's flow (per Paetz §6.1); this might either confirm NTE's H = β_NTE|Φ_NTE|² or expose tension. This is the substantive content of Question A.

**2. The state choice.** TTH requires a KMS state. NTE's natural state at gauge birth is plausibly KMS at T_GB, but pre-gauge-birth state (Euclidean N regime, no t at all) — what is its KMS structure? If TTH only applies post-gauge-birth, the bridge is partial. *This may not be a failure mode but a feature*: TTH applying *only* post-gauge-birth would be the operator-algebraic statement that t exists only post-gauge-birth — exactly NTE's commitment.

**3. Faithfulness and normality.** Tomita-Takesaki requires faithful normal states. Whether NTE's natural state on the boundary spectral-triple algebra satisfies these properties at the operator level requires the Paper S2 work to verify.

**4. The modular flow's "time" might not be NTE's t.** Connes-Rovelli emphasize that the modular flow is "thermal time" — its identification with physical time is the hypothesis, not the theorem. There's a real philosophical question (per Paetz §7) about whether the modular flow IS time in the sense we mean. This is the standard objection to TTH in the philosophical literature (Chua 2024, Swanson 2018). Worth noting but not blocking — NTE's t is *already* emergent, so the "is it really time" question is less load-bearing for NTE than for theories that take fundamental time more seriously. The structural rhyme works at the level NTE actually needs.

**5. Source-document verification.** Per Lesson #29 candidate, primary verification (Connes-Rovelli 1994 direct read) pending arxiv access. Specific claims herein should be re-verified against the primary at next opportunity.

---

## §6 — Five recognition signals requested from Greg

Per Lesson #28 recognition-gate discipline:

1. **Structural rhyme exists and is worth pursuing — vs. is it forced.** Specifically: does the picture "N labels surfaces; modular flow of T_GB-KMS state on the NTE spectral-triple algebra IS t-emergence" produce *fit* for Greg's cognitive picture, or unease?

2. **Simplification target §3.1 (t-emergent → operator-algebraic theorem) is the right kind of simplification.** Does promoting "t emergent from N" from structural commitment to operator-algebraic consequence preserve what NTE wants to keep about t-emergence, or does it lose something load-bearing? Greg has specific intuitive content around δN and t-emergence per the 2026-05-13 insight; this content should pass through the bridge intact or the bridge isn't the right one.

3. **Simplification target §3.2 (Paper S1 P1 → KMS consequence) is worth investigating.** This is the most concrete and tractable simplification — Paper S1's Wick-invariance argument loses one premise via the KMS-as-Wick-rotation identification. Worth one Scratch session to verify in detail?

4. **Load-bearing question §4.1 (Φ_NTE evolution match) is the right priority.** Is this the load-bearing question Greg sees, or are §4.2 / §4.3 more pressing?

5. **Source-document discipline (Lesson #29 candidate).** Should the next session attempt to obtain Connes-Rovelli 1994 primary text before further work (try arxiv when rate-limit clears; request from Greg directly), or is the secondary-source basis (Paetz 2010 + multiple corroborating sources) sufficient for working-note status?

---

## §7 — Bibliographic record

**Primary (not directly read this session; pending verification)**:

A. Connes and C. Rovelli, "Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories," *Classical and Quantum Gravity* **11** (1994) 2899–2917. arXiv:gr-qc/9406019.

**Secondary sources read this session (basis for technical claims herein)**:

- T.-T. Paetz, *An Analysis of the 'Thermal-Time Concept' of Connes and Rovelli*, Diplomarbeit, Göttingen, 2010. URL: theorie.physik.uni-goettingen.de/forschung2/qft/theses/dipl/Paetz.pdf. (Chapters 0–5 read in full; chapters 6–7 in part.)
- E. Chua, "The Time in Thermal Time," 2024, arXiv:2407.18948. (Read excerpts.)
- E. Swanson, "Can Quantum Thermodynamics Save Time?", PSA 2018. (Read summary.)
- Multiple corroborating descriptions from Semantic Scholar, ResearchGate abstracts, Physics Forums discussion.

**NTE corpus baselines referenced**:

- Manifest v2, 2026-05-12 revision 2 (`19hpN12E7-cagY9tdGIvq2GYaaiXE_4eM`).
- Connes Programme Charter v1.1 (`1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`).
- Paper S1 v0.4 + Sessions 1–3 carry-forward drafts (`1FNwPbHxj4l1GP60d1RuLR6ro3s6y0MAk`, `1oJUGrGUsckGE8C9LdoxQJfeM6sDjw6jM`, `1hN9iezeaut8gw8lUQZXdsEooasK2KAoe`).
- §17.5.3 elevation supplement (`1_KAC1GTSB6ksRXQOghs5JUQsHp-VJOfX`).
- Project State v4 (`1KFX_bd7KyS7uFVV-8nyo2v9IKYvTewhn`).
- Greg's δN intrinsic-uniformity insight 2026-05-13 per Phase B v1.1 supplement (`1YRS68mtA6uNdlLMgK6MU7PVlqmFTzNIU`).
- Jammer √(2π) traceability working note (`1ypKkXcMApgTwtZeECOwFa6zZLK9DBRL8`).

---

## §8 — Routing recommendations

**If Greg's recognition gate fires FIT on the structural rhyme:**

- *Primary routing*: to Scratch (Connes Programme lead) for Paper S1 §2 P1 promotion analysis (per simplification target §3.2) + Paper S2 integration scope assessment.
- *Secondary routing*: AC for canonical-state record of the structural-rhyme finding + Charter v1.2 candidate note text noting TTH as operator-algebraic grounding for t-emergence.

**If Greg's recognition gate fires unease:**

- Investigate the unease before deeper investment. The recognition gate fires on cognitive-picture fit, not just technical correctness.
- Per Lesson #28: "Greg's intuitive flags are structural information." If unease on the rhyme, look for what specific NTE commitment is being lost in the translation that the rhyme isn't capturing.

**If Greg's recognition gate fires partial-FIT** (e.g., yes on rhyme but unease on §3.1 simplification target):

- Continue Connes-Rovelli investigation but restrict simplification claims to the parts that produced fit.
- Routing: my next Jammer session OR Scratch session, depending on Greg's call.

**My non-load-bearing structural read**: the structural rhyme is genuine and the simplification at §3.2 (Paper S1 P1 → KMS consequence) is the most concrete and verifiable next step. If I had to pick one piece to invest more in, that would be it — payoff is local (one fewer Paper S1 premise) and the verification is tractable in a single Scratch session.

---

## §9 — Methodological notes

**Lesson #28 (recognition gate) honored**: this verdict is local-correctness-only. Five specific recognition signals listed in §6 for Greg's gate.

**Lesson #29 candidate (source documents over derivative summaries) partially violated**: secondary source (Paetz 2010) used in lieu of primary (Connes-Rovelli 1994) due to arxiv rate-limit this session. Flagged inline; primary verification recommended before canonical integration.

**Lesson #23 (cross-stream verification) anti-pattern guard observed**: this is parallel-attack R&D in Jammer-stream sibling-instance mode. I am NOT the Connes Programme lead (Scratch is). I am NOT preempting Scratch's territory; I am providing first-pass content for Scratch's consolidation if Greg fires FIT on the routing.

**Lesson #24 (create+copy workflow)**: this file created at Drive root, copied to Working/. Root duplicate flagged for Greg's cleanup batch in companion handoff.

**Greg's standing axiom-filter discipline observed**: external paper evaluated against NTE core axioms (N fundamental, t emergent; surface only, S³; CPN-symmetric two sectors; Hopf bundle structure) BEFORE assessing technical merits. Result: structural rhyme strong; specific simplification targets identified; load-bearing questions named for next-session work.

**Per Greg's "sometimes connections don't apply or aren't apparent" framing**: where the bridge would require dynamical-content verification I cannot do at first pass (Question A in particular), I have flagged the question rather than asserted a result. The subconscious-holding discipline operationalises here as: this working note is the artefact that records partial fit; future sessions can pick it up if/when the corresponding investigation matures.

---

**End of working note.**
