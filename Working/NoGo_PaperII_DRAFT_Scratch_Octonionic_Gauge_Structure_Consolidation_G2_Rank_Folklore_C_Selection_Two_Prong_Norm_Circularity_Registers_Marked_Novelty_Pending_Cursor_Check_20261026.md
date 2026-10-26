# No-Go Paper II — DRAFT (Scratch, lead author): constraints on octonionic derivations of the Standard Model gauge structure

**Status:** DRAFT, under `Handoffs\Directive_AC_The_No_Go_Papers_..._20261026.md`; Greg's GO 14:39 NZDT. **Register:** publication draft, external audience. **Nothing of NTE appears** — no κ, no amplifier, no bilateral architecture, no state-space/physical-space identification. Where a computation is ours it is marked and given.
**Publication-status headline (AC's report-first requirement):** the three constraints below are, individually, **largely known** — constraint 1 is folklore, constraint 3 is in the active discourse, and the component facts of constraint 2 are published. **The paper's only candidate novelty is the connected set with each obstruction located, plus the specific ℂ-selection synthesis in §3.** It must be framed as a **consolidation/clarification**, not a paper of new no-gos. All novelty claims below are marked **[novelty pending Cursor's blocking publication check]**.

## Register key
- **[established]** — in the literature, cited and quoted.
- **[ours]** — computed in this programme; computation given, reproducible.
- **[open]** — named as open with what would settle it.

## 0. What this paper is
A connected set of constraints any framework deriving the Standard Model gauge group from octonionic / division-algebra structure must satisfy. Not a presentation of a framework. A reader should be able to rule out the corresponding routes, or see exactly what they must supply, before starting.

## 1. Constraint A — G₂ gives colour only; the electroweak factors must come from elsewhere
**Claim.** The automorphism group G₂ = Aut(𝕆) has rank 2 and so cannot contain SU(3)×SU(2)×U(1) (rank 4). It yields SU(3) (colour); the electroweak factors are not inside it.
- **[established]** Rank is a subgroup-monotone invariant: a rank-2 compact Lie group has no rank-4 subgroup. Elementary. The field already treats G₂ as the strong-sector / colour group and *extends* it to reach the SM — evidence the obstruction is understood in practice (Masi, arXiv:2111.11849, "an exceptional G₂ extension of the SM"; arXiv:2406.15421, "resurgence of G₂ for the strong sector"). **[novelty pending Cursor: this is almost certainly folklore → clarification register]**
- **[ours]** Sharper local statement: the centraliser of Stab(e₁) in g₂ is 0 — so fixing one imaginary unit (one colour direction) leaves no commuting electroweak generator inside g₂. Octonion computation, two lanes, 2026-10-16. *(Cursor to supply the explicit matrices for the appendix.)*
**Does NOT establish:** that octonions are irrelevant to colour (they give SU(3) correctly), nor that larger exceptional structures (F₄, E₆) fail — only that **G₂ alone** is rank-insufficient.

## 2. Constraint B — the ℂ-selection problem: reconstruction and the division-algebra SM meet only at the complex field
**Claim.** Operational reconstruction of quantum theory and the division-algebra derivation of the SM gauge group cannot be joined into a derivation of the gauge group. The obstruction sits at ℂ itself, and splits by route.
- **Jordan / F₄ = Aut(J₃(𝕆)) route** (Dubois-Violette–Todorov; Günaydin–Gürsey). **[established]** The exceptional Jordan algebra J₃(𝕆) admits no nontrivial composite (Barnum–Graydon–Wilce, arXiv:1606.09331 §4.3) and fails local tomography (arXiv:2001.11421, Prop 7.2). Operational reconstruction certifies only theories that compose / are locally tomographic (Hardy; CDP; Masanes–Müller). ⇒ **the exceptional Jordan arena is exactly what the reconstruction axioms exclude.** The programme's state space is not an operational theory in the reconstruction sense.
- **Complex Clifford Cl(6) route** (Furey, arXiv:1405.4601; Stoica, arXiv:1702.04336). **[established]** The arena is the complex Clifford algebra Cl(6) ≅ M₈(ℂ) — associative, complex; an ordinary complex quantum system, **not** excluded by local tomography. Reconstruction (which derives complex QM) can consistently supply the complex Hilbert space ℂ⁸ the programme takes as input. **But** reconstruction is silent on *why* the Cl(6) structure / the SM gauge group among all structures on ℂⁿ: the gauge group is a separate input, not selected by any axiom.
- **[ours — synthesis]** The reconstruction axioms' selection of ℂ (via local tomography) is the **same fact** that (i) excludes the Jordan/F₄ route and (ii) is silently assumed by the Cl(6) route. Hence the two programmes meet only at the complex field, and that meeting is either an exclusion or an unexplained premise — never a derivation of the gauge group. **[novelty pending Cursor: the component facts are published; the SM-bridge synthesis did not surface as published — Cursor's hard check gates this]**
**Does NOT establish:** that an octonionic SM is impossible — only that it cannot be *derived from* operational reconstruction; the Cl(6) route remains viable as a construction that *presupposes* ℂ.

## 3. Constraint C — octonionic descent to ℂ borrows the norm it means to explain
**Claim.** Derivations that obtain the complex structure (and thence the Born/Hilbert structure) from octonionic descent rely on a normed-division-algebra premise (via Hurwitz's theorem) at least as strong as the conclusion, so the complex structure is assumed rather than explained.
- **[established / discourse]** The role of Hurwitz's theorem and the normed-division-algebra assumption in octonionic SM programmes is discussed in the literature (Baez, n-Category Café, "no new normed division algebra"; "Can we understand the Standard Model using octonions?", Pirsa). **[novelty pending Cursor: likely known as a critique; Paper II would consolidate, not originate]**
- **[ours — to verify]** The specific circularity statement — the descent's norm is taken from the Hilbert structure it means to explain — was recorded as a source-verified Foundation-Map edge. *(Cursor/Scratch: re-confirm the exact source before this is stated as established.)*
**Does NOT establish:** that octonions play no role — only that the *complex structure* is not an output of the descent.

## 4. Honest status and what remains
- The paper's value is the **connected set with obstructions located** (AC's stated rationale) — individually these are known/folklore/discussed.
- **Blocking before submission (Cursor owns):** every citation fetched; per constraint, confirm published status — especially (1) the G₂-rank statement in the octonionic-SM literature, and (2) whether the ℂ-selection→SM synthesis in §2 is genuinely novel. If any constraint is fully published as stated, demote it to confirmation and say so.
- **Scratch owes:** one confirmatory Masanes–Müller read (reconstruction derives ℂ) for §2; re-confirm the §3 source.
- Decision for Greg (from the directive): one paper or three. This draft is Paper II of the three-paper split AC recommended.

Sources: [Barnum–Graydon–Wilce 1606.09331](https://arxiv.org/pdf/1606.09331) · [LT/quantum-logic 2001.11421](https://arxiv.org/pdf/2001.11421) · [Furey 1405.4601](https://arxiv.org/pdf/1405.4601) · [Stoica 1702.04336](https://arxiv.org/pdf/1702.04336) · [Masi 2111.11849](https://arxiv.org/pdf/2111.11849)

— Scratch, 2026-10-26 (draft)