# Foundation Map Step 4: adversarial pass on the edge SPECIFICATIONS, plus pre-registered criteria for Scratch's built objects (Claude Jammer)

**Directive:** `Handoffs\DIRECTIVE_AC_Foundation_Map_Step4_Begin_Six_Edges_After_CPN_Correction_20261027.md` (Greg GO 02:50). Read in full.
**Scope authority:** `Handoffs\FOUNDATION_MAP_Step4_Scope_..._20261026.md` (as modified 10-26 02:08Z). Read in full.
**Scratch's built objects:** none filed yet. I searched `Handoffs\` and `Working\` for files modified after 2026-10-26T13:44Z; the only hit was the directive.

**Process disclosure:**
- **Part A** attacks the edge wording in the two AC documents. Scratch builds from that wording, so errors in it would propagate. It is **not pre-registered**: the specifications were read before filing.
- **Part B** pre-registers the per-edge criteria I will apply to Scratch's objects. It is filed **before** any object exists.
- A second "Claude Jammer" pre-registration covering overlapping ground (`Working\NoGo_Papers_And_Map_Step4_Edges_Novelty_Triage_PREREGISTRATION_Claude_Jammer_...`, 10-26 01:36Z) was **not written by this session**. Its authorship is still unresolved.

**Sources used** (all read this week; web extraction where marked):
- Ciarcelluti–Wallemacq 1401.4763 (extraction: formula and bounds only)
- YdFT 1408.0487 (extraction)
- dRHR 1409.3834 (extraction)
- BMU 1403.4147 (extraction)
- BGW 1606.09331 (extraction; Scratch read it at source)
- Furey–Hughes 2210.10126 (extraction)
- the Cursor fetch notes for Paper II

**Not read:** Zhang PRA 114 042208; arXiv:2603.07745; Busch quant-ph/0306179; Berezhiani–Comelli–Villante.

No Core. No f.

---

# PART A: the edge specifications

## E1. "An exact mirror symmetry does not force T′ = T; x is free." Verdict: **not a closed door**

- The statement is correct for a symmetry **of the Lagrangian**.
- But it is the *negation* of a constraint, not a tested-and-failed edge. A reader cannot rule anything out with it.
- **The closed door that does exist:** a **state**-symmetric, co-present mirror sector (x = 1) is excluded by ΔN_eff ≈ 6.14x⁴. This is **published**: Berezhiani–Comelli–Villante (per the scope document's note on eq. 9) and Ciarcelluti–Wallemacq (bounds x < 0.456 CMB, x ≲ 0.7 BBN).
- **Proposed edge:** "Mirror sector with x = 1 (state-symmetric, co-present) excluded by N_eff. Published."
  - **Does not establish:** anything about Lagrangian-symmetric mirrors with x ≲ 0.3–0.5, or about Boyle–Finn–Turok-type sheets that are not co-present.
  - **Attribution:** entirely external. Our only contribution is the correction of our own earlier claim, which belongs in the closure record.

## E2. "G₂ rank 2 ⊅ SU(3)×SU(2)×U(1)." Verdict: **stated correctly, attributed correctly**

- The "does not establish" field must say: *that octonionic structures cannot yield the Standard Model group.*
  - The F₄ / J₃(𝕆) route (Todorov–Dubois-Violette, eq. 1.4: G_{F₄} = S(U(2)×U(3)), from Cursor's fetch) yields it.
  - The ℂl(6) route (Furey) yields it.
- **Risk to guard:** the edge must not be read as "octonions fail". It says only that the automorphism group of 𝕆 alone is too small.

## E3. "Octonionic descent cannot derive QM's complex scalar field without presupposing the norm." Verdict: **overstated; should be NTE-scoped, like the CPN row**

- **"Cannot" asserts an impossibility.** What was actually tested:
  1. NTE's Companion 16 took its norm from the Hilbert structure (a diagnosis of one instance).
  2. No published framework claims the derivation (Cursor's search: NONE).
- **Absence of a target is not a theorem.** AC's directive says this itself.
- The general part ("a Hurwitz-type uniqueness argument presupposes a composition norm") is a **textbook** property of Hurwitz's theorem, not a tested edge.
- By the scope document's own logic for the CPN row ("a statement about NTE, not about mirror sectors… belongs in the closure record"), **E3 is in the same position**. Its tested content is about NTE.
- **Proposal:** remove E3 from the general edges. Place it in the closure record as "NTE's descent presupposed its norm; no external target exists."
  - **If AC keeps it as an edge**, the wording must be: "Derivations of ℂ via Hurwitz presuppose a composition norm (textbook). No published framework claims to derive QM's ℂ from octonion descent. The nearest, Günaydin 1976, takes the complex scalar product as input (per De Leo–Abdel-Khalek)."
  - **Does not establish:** that no future derivation could succeed.
- **Corpus-leak flag:** the scope document's basis column for this row cites "C16", which is an NTE corpus file. A map edge for other frameworks cannot rest on our corpus.

## E4. "Additivity is the irreducible probabilistic input." Verdict: **attribution correct in form; strength unverified by this lane**

- **Attribution:** "irreducible" is Zhang's claim. The edge must read "per Zhang 2026", with its scope (the derivations he surveys).
- **Not verified:** I have not read Zhang. Someone must confirm the "five major derivations" scope at source before the edge is built.

## E5. "Qubit underdetermined for projector-valued measures; Busch recovers uniqueness on effects." Verdict: **the directive's wording is right; the scope document's wording is wrong; credit is missing**

- **Directive vs scope document:** the directive has the PVM qualifier. The scope document's row ("Born rule underdetermined at d = 2") omits it, and it lists the basis as "computed; Busch 2003".
- **Scratch must build from the directive's wording.**
- **Credit:** arXiv:2603.07745 (cited in the ratified plan §5 as a published counterexample family) must be the attribution. Our sin² and r + ε·sin2πr examples are **instances, after that publication**.
- **Not verified:** I have not read 2603.07745 or Busch.

## E6. "Doubly-coupled matter revives the BD ghost except single-kinetic; the Dirac case is OPEN." Verdict: **the exception is overstated, and the general clause is broader than tested**

- **The general clause rests on scalar computations.** YdFT used a k-essence scalar with kinetic terms on both metrics; dRHR used a massless scalar. The edge must say "for scalar matter with kinetic terms on both metrics".
- **The single-kinetic exception is classical only.** dRHR 1409.3834, as extracted: the variant with the kinetic term on one metric and the potential on several is "classically ghost-free", but the ghost "always reappears at an unacceptable low scale at the quantum level". The edge as written ("except single-kinetic") states a quantum-level exception the source denies.
- **There is a third class the edge omits.** The composite (effective) metric/vielbein coupling (dRHR; Melville–Noller 1511.01485, partial) has the ghost present but **above** the strong-coupling scale. That is a different status from "revived".
- **Dirac case:** OPEN is the correct label.
  - The supporting text must say: "aligned-sector non-closure derived by this project, unratified; boost sector outstanding". It must be clearly marked **ours**.
  - The scope document's row also states "aligned-sector weight Σ_g²/Σ". That should carry the same "ours, unratified" label.

## Surviving items (b)

- **κ₀:** correctly registered as a geometric identity. "Touches nothing" remains permitted.
- **Phase-stabiliser reduction:** placed "strictly under Gleason and Busch". **Cursor should check whether it is published**; it is a standard unitary-invariance step, so a likely PARTIAL/PUBLISHED. If it is, credit it.
- **Ω_k < 0:** correct and not distinguishing.

## Gap 1 entry (c)

- The directive says "Gap 1 landed B3: no derivational bridge."
- The **obstruction is published**: BMU 2014 (energy observability excludes 3-level octonionic theory) and BGW 2020 (no non-classical composite with the exceptional algebra), confirmed at source by Scratch.
- The gap edge must credit those papers. Otherwise it reads as ours.
- Add the Clifford-route clause from my 10-26 note: ℂl(6) is composable but makes the octonions scaffolding.

---

# PART B: pre-registered criteria for Scratch's built objects (filed before any exist)

For each object, the outcome will be one of:
- **S:** stated at supported strength, attribution right.
- **O:** overstated (scope broader than the test).
- **U:** understated.
- **A:** attribution wrong (ours presented as the field's, or the field's as ours).
- **L:** corpus leak (an NTE file cited as basis for a general edge).

**Predictions:**
- E2, E4: S.
- E5: A, unless 2603.07745 is credited.
- E6: O, unless the scalar scope and the classical-only exception are written in.
- E3: O or L, unless NTE-scoped.
- E1: built as a negation (not a closed door), unless restated per Part A.

— Claude Jammer, 2026-10-27.
