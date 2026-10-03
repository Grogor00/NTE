# AC Audit Response — §II.0 Graded-Criteria Discipline Proposal

**From:** AC
**To:** Jammer (audit response), Greg (strategic-call inputs), CR (visibility)
**Re:** Audit of `II_0_Graded_Criteria_Discipline_Proposal.md`. Jammer's §7 asks two questions: (a) is the proposed §II.0 paragraph concrete enough, and are the corpus examples in each scope correctly tagged? (b) does the (γ) unification work, or fall back to (β) with three separate entries?
**Corpus baseline:** v10.6 (canonical; shipped 2026-05-03).
**Status:** Audit complete. Verdict: **approve, with one minor refinement to the paragraph's opening sentence.** The (γ) unification holds; I do not see a case for (β) fallback. Strategic-call inputs for Greg attached at §3.

---

## 0. Headline verdict

The proposal is sound. It names a discipline the framework has been intermittently practising and gives it the right home (§II.0). The unification (γ) is structurally honest because the three findings — L1, L2, eta-reframing Refinement A — share a single underlying logic: §II.0's criteria are stated as binaries but apply with graded fulfilment in actual practice. The proposal closes L1 and L2 cleanly and gives Refinement A a citable home. I have one minor refinement to flag, noted in §1.1; it is at Jammer's discretion.

The corpus-wide grep that lesson #5 / #8 / #13 require is post-approval execution work and is *not* part of this audit. AC will run that grep when Greg authorises the v10.7 patch; expect 5–10 sites where summary prose collapses grades that the new discipline asks to be made explicit.

---

## 1. Audit findings

### 1.1 (a) Paragraph concreteness — APPROVED with one refinement to the opening sentence

The body of the paragraph is concrete: each of the three scopes is anchored to specific corpus examples drawn from v10.6, comparable in concreteness to the existing §II.0 paragraphs. Tagging is correct:

- **Unification scope, strong-grade examples:** gauge-group-from-G₂; Born rule from Hopf-on-S³; three generations from dim su(2); κ from S³ topology. All correctly tagged as forced-by-deeper-structure.
- **Unification scope, weak-grade example:** Janus = ODE branch structure under analytic continuation. Correctly tagged as consistency-between-existing-commitments rather than structural simplification. This is L1 absorbed.
- **Unification scope, mixed v10.6 example:** the surface-ontology programme producing one strong-grade simplification (gauge birth's geometric content corrected by Stage 3) and one weak-grade simplification (Janus = ODE branch consistency). Correctly tagged. The "corrected reading forced by Stage 3's calculation against the framework's existing commitments" framing is the right honesty: Stage 3 didn't merely confirm; it forced a correction.
- **Explanation scope:** C¹ kink as Wick rotation reading tagged as re-description without observable signature. Correctly tagged. This is L2 absorbed.
- **Prediction scope:** five grades — derivative-full / derivative-partial-or-approximate / derivative-with-observational-inputs / passthrough / observational — each with a corpus example (κ from S³ topology / M_R structure to factor 1.5 / θ_C Cabibbo / v_EW and Yukawa values / M₁). Correctly tagged. This is Refinement A absorbed.

The paragraph reads at the same register as the existing §II.0 paragraphs. Length (~600 words) fits the §II.0 voice band.

**One refinement.** The opening sentence —

> *"Underlying §II.0's criteria — does a structural move simplify, or accrete; does an accretion explain a phenomenon no simpler description can explain, or make a distinguishing prediction — is a discipline that those criteria are stated as binaries but apply with graded fulfilment in actual practice."*

— has subject-verb agreement that wobbles. The reader parses *"Underlying §II.0's criteria … is a discipline that those criteria …"* and the second-clause "those criteria" is awkward because the surface subject is "Underlying §II.0's criteria" but the grammatical subject is "a discipline". Suggested cleaner version:

> *"§II.0's criteria — does a structural move simplify or accrete; does an accretion explain a phenomenon no simpler description can explain or make a distinguishing prediction — are stated as binaries but apply with graded fulfilment in actual practice. The framework's discipline is to report which grade applies to each move, rather than collapsing distinctions in summary prose."*

This is the only place where the prose drags. The rest of the paragraph reads cleanly.

**Verdict on (a):** the paragraph is concrete enough; the corpus examples are correctly tagged in each scope; the only refinement is the opening-sentence clean-up above. Jammer's call on whether to apply.

### 1.2 (b) Does (γ) unification work, or fall back to (β)?

**(γ) works.** The three findings — L1 (unification grades), L2 (explanation grades), Refinement A (prediction grades) — share a single underlying structural logic: §II.0's criteria are stated as binaries (simplify-vs-accrete; explain-uniquely-vs-makes-distinguishing-prediction-vs-fails) but applied in domains where they have graded fulfilment. The graded-criteria discipline names that single underlying logic. (β) — three separate entries — would create §II.0 bloat without recognising that the three findings are three applications of one principle.

The (γ) gain over (β) is structural, not merely stylistic. (β) would record three separate methodological commitments; the framework would then have to maintain consistency between them across future work, with no anchor for noticing when they're misapplied. (γ) records *one* commitment (graded-not-binary) with three concrete scopes, and any future scope where the binary-vs-graded issue surfaces folds under the same paragraph rather than spawning a fourth entry.

The (β) fallback would be appropriate if the three findings turned out to be about different things — e.g., if Refinement A were about prediction *honesty* in a sense distinct from the structural-grade question. Audit verdict: they aren't. All three are about §II.0's binary-criteria-applied-where-grades-exist pattern. (γ) is the right move.

**Verdict on (b):** approve (γ). The (β) fallback is documented in the proposal's §3 and remains available if Greg or future-AC find practical reasons to split, but I see no current case for it.

### 1.3 What is NOT being changed by the proposal

For the audit trail (consistent with proposal §4):

- Numerical predictions: unchanged.
- §II.0 paragraphs 1–6: unchanged. The new paragraph extends, doesn't replace.
- §17.5 catalogue: structurally unchanged. L1 and L2 close out of the latent-finding list and into the methodology layer; this is correct §II.0 placement.
- Path B disclosure, surface ontology, V_NTE Stage 2 findings: untouched. The discipline applies to *presentation*, not substance.

Concur with proposal §4.

---

## 2. Risk and impact

Concur with proposal §5: risk is low. The discipline doesn't add structural commitment; it formalises calibration the framework has been intermittently practising (§VIII line 663 Yukawa inheritance honesty; §2.4.2 α empirical characterisation; §1314 θ₁₃ structural-similarity flag; v10.5.5 α numerology pass; §17.5 catalogue itself). Naming the discipline at the methodology layer makes future symmetric application enforceable.

The only execution-time risk is the corpus-wide grep AC will run post-approval. Lessons #5, #8, and #13 require it; the proposal correctly flags it (§7.(c)). AC stands ready to execute when Greg authorises v10.7.

---

## 3. Strategic-call inputs for Greg

Two calls remain for Greg per proposal §7:

### 3.1 (d) Option 1 (paired with eta v2) vs Option 2 (sequential)

**AC's read:** no strong preference; both options work.

The case for **Option 1 (paired)** is that the eta reframing v2 demonstrates the new §II.0 discipline at work on a fresh case — the §II.0 paragraph names the discipline, the eta v2 then applies it. Pedagogically reinforcing.

The case for **Option 2 (sequential)** is workflow-cadence: ship the §II.0 update first as v10.6.1 (a tight patch with low risk and self-contained scope), then ship the eta v2 as v10.7 (a larger reframing that benefits from a settled methodology backdrop). This pattern matches the v10.5.7 → v10.5.8 → v10.5.9 cadence: small methodology shifts shipping ahead of larger structural work.

If forced to pick: marginally Option 2, on workflow-cadence grounds. The §II.0 paragraph is a small, self-contained, low-risk patch; shipping it independently lets the corpus-wide grep happen in a clean session without the eta v2's larger scope competing for attention. But Option 1 is also clean.

Greg's call.

### 3.2 (e) Full scope vs smaller scope (only prediction-honesty)

**AC's read:** full scope is correct. Smaller scope (only the prediction-honesty grade-list) leaves L1 and L2 as separate latent findings on the register; the unifying structural logic is then unstated, and any future scope where the binary-vs-graded issue arises has no paragraph to fold under. The cost of the full scope is ~600 words of prose; the benefit is the framework's methodology layer carries the discipline as a named standing commitment.

If Greg has a specific reason to keep L1 and L2 latent (e.g., wants them visible as research targets in their own right rather than absorbed), the smaller-scope alternative remains tractable. AC does not see such a reason currently; both findings are about presentation, not about open structural research.

Recommendation: full scope (γ). Greg's call.

---

## 4. Awaiting

**For Jammer:**
- Optional: apply the opening-sentence refinement at §1.1 above. At Jammer's discretion; the proposal is approvable as-drafted if preferred.

**For Greg:**
- Strategic call (d): Option 1 (paired) vs Option 2 (sequential). AC marginally favours Option 2 on cadence grounds; either works.
- Strategic call (e): full scope (γ) vs prediction-only (smaller). AC recommends full scope.

**For AC (post-approval execution):**
- Insert the new §II.0 paragraph as paragraph 7 (after current paragraph 6, line 84 of `NTE_v10_6.md`). Length and voice fit; placement is correct.
- Run corpus-wide grep per lessons #5, #8, #13: identify summary-prose sites that collapse grades the discipline asks to be made explicit. Estimated 5–10 sites.
- Update §17.5 catalogue: L1 and L2 close (move from latent-research to closed-by-methodology-layer-update).
- Update register at v10.7 ship with full changelog including this addition.

**For CR (visibility):** standard v10.7 pre-ship pass will see this. The graded-criteria discipline itself is fair game for CR critique once landed.

---

## 5. AC's substantive comment

This proposal is the kind of methodology-layer update that pays compounding interest. The framework's structural content is now extensive (Path B, surface ontology, V_NTE Stage 2 findings, κ derivation chain, eight predictions). With that volume, the failure mode is summary prose that collapses grades for rhetorical compactness — claiming "the framework predicts X" when the more honest claim is "the framework derives X to factor 1.5 from S³ topology" or "the framework inherits X from the SM Yukawa structure with no additional NTE machinery." Naming the discipline at §II.0 gives every future summary a place to land.

The (γ) unification also has a methodological payoff worth flagging: it demonstrates that §II.0 is the *right* place for methodology-layer updates of this shape. Three separate findings (L1, L2, Refinement A) emerged from independent audit work (CR, AC) over independent topics (surface ontology, eta reframing); they share a common structural pattern; that pattern lives at §II.0. The shape of update — multiple findings sharing one underlying methodological issue, surfaced over time, unified at §II.0 — is repeatable. v10.5.7's symmetric-tracking update was the same shape; v10.7's graded-criteria update is the same shape. Future-AC should expect more of these.

Audit complete.

---

## END-OF-AUDIT FILE OPERATIONS

```
ADD TO PROJECT (new files):
  - II_0_Graded_Criteria_Discipline_AC_Audit.md
    (this audit response; queued for Jammer's optional refinement
     and Greg's strategic calls (d) and (e) before v10.7 execution)

REPLACE IN PROJECT:
  - None this turn.

DELETE FROM PROJECT:
  - None.
```

— End audit. AC, 2026-05-06.
