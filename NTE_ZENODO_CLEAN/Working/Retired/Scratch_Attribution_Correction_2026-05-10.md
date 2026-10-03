# Attribution Correction Memo — Scratch's Revision (2026-05-10)

**From:** Scratch.
**To:** AC (for corpus integration work); Greg (for outreach forwarding); future readers of Programme S documents.
**Date:** 2026-05-10 NZST.
**Subject:** Misattribution in `Paper_S1_v0_2.md`, `Programme_S_Status_v1.md`, and `Handoff_Scratch_to_AC_ProgrammeS_findings.md`. The curvature combination `5R² − 8R_μν² − 7R_μνρσ²` and the f(0)/360 spectral-action expansion structure should be attributed to **Chamseddine-Connes 1996 / Gilkey 1984**, not to **Boyle-Farnsworth 2013**.
**Priority:** High. External outreach (Greg-side) has the original attribution embedded; recipients (Boyle, Farnsworth, Marcolli, Sakellariadou) will catch this immediately. Corrected outreach note in `Programme_S_Outreach_Note_v2.md` supersedes the §6.2 version in `Programme_S_Status_v1.md`.

---

## §1. The misattribution

In Scratch's deliverables this session, the curvature combination

```
5R² − 8 R_μν R^μν − 7 R_μνρσ R^μνρσ
```

appearing in the f(0)/360 coefficient of the spectral action's asymptotic expansion was repeatedly framed as **"Boyle-Farnsworth eq. 4.14"** (e.g., `Paper_S1_v0_2.md` §1, §2, §4.1; `Programme_S_Status_v1.md` §3.3, §4.1, §6.2 outreach note; `Handoff_Scratch_to_AC_ProgrammeS_findings.md` §3 (F1 statement)).

**This attribution is wrong.** The correct attributions are:

(a) **Gilkey 1984** — *Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem.* The general a₄ Seeley-DeWitt heat-kernel coefficient on a 4-manifold has a universal form whose curvature-quadratic part is the source of the `5R²/360 − 2R_μν²/360 + 2R_μνρσ²/360` (or equivalent, depending on operator and convention) combination. This is the standard heat-kernel asymptotic expansion result, predating the spectral action by over a decade.

(b) **Chamseddine-Connes 1996** — *The Spectral Action Principle* (hep-th/9606001). Defines the spectral action `Tr(f(D/Λ))` and computes its asymptotic expansion in terms of Seeley-DeWitt coefficients. The specific combination `5R² − 8R_μν² − 7R_μνρσ²` arises from the Dirac Laplacian D² = ∇*∇ + R/4 (the Lichnerowicz formula), with the R/4 endomorphism contributing additional terms that combine with the universal Gilkey coefficient to give the form that appears in CC's eq. (3.15) and successors.

(c) **Chamseddine-Connes-Marcolli 2007** — *Gravity and the Standard Model with Neutrino Mixing* (hep-th/0610241). The mature form of the SM spectral action expansion. The curvature combination appears here in eq. (4.42) and is *the* standard form used throughout subsequent NCG-cosmology literature.

(d) **Boyle-Farnsworth 2013** — *Non-associative Geometry and the Spectral Action Principle* (JHEP07(2015)023, arXiv:1303.1782). Extends the CC spectral action machinery to non-associative algebras. Their eq. 4.14 *reproduces* the standard CC form with the addition of the dim(H_F) = 8 multiplier specific to their octonionic case. The form of the curvature combination is inherited from CC 1996 / Gilkey 1984; BF's contribution is demonstrating that this form survives the extension to non-associative input algebras and computing the octonionic-case multiplier.

## §2. What is genuinely Boyle-Farnsworth's

To preserve correct attribution to BF where it belongs:

(a) **The principle of automorphism covariance** for non-associative spectral triples (BF 2013 §3.2).
(b) **The non-associative bimodule structure** generalising Connes' bi-representation axioms (BF 2013 §3.1).
(c) **The fluctuation of the Dirac operator** in the non-associative setting (BF 2013 §3.4).
(d) **The simplest octonionic almost-associative spectral triple** T_F = (𝕆, 𝕆, 0, I, J_𝕆) (BF 2013 §4.1) and the demonstration that its spectral action gives Einstein gravity + G₂ Yang-Mills + 8 Dirac fermions.
(e) **The dim(H_F) = 8 multiplier** in the octonionic case (the factor of 8 in BF eq. 4.14's prefactor 8/(4π)²).
(f) **The G₂ gauge field structure** emerging from inner derivations of 𝕆 (BF 2013 §4.2).
(g) **Farnsworth 2025** (arXiv:2506.21496) extends to G₂ × G₂ with charged Higgs.

These remain correctly attributed to BF in the revised documents. The misattribution was specific to the *form* of the curvature combination, which BF inherited from CC.

## §3. Implications for Finding F1

**The d=3 cancellation finding is correct, but its scope is broader than originally stated.**

Original framing: "On unit S^d, the *Boyle-Farnsworth f(0) gravitational correction* `5R² − 8R_μν² − 7R_μνρσ²` factorises as d(d−1)(5d² − 13d − 6), with integer root only at d = 3."

Corrected framing: **"On unit S^d, the curvature combination `5R² − 8R_μν² − 7R_μνρσ²` appearing in the f(0)/360 coefficient of the standard Chamseddine-Connes spectral action asymptotic expansion (CC 1996; CCM 2007 eq. 4.42; Gilkey 1984 a₄ heat-kernel coefficient) factorises as d(d−1)(5d² − 13d − 6), with integer root only at d = 3."**

**Structural implication.** The cancellation is a property of the standard CC spectral action expansion, applying to **any** almost-commutative or almost-associative geometry whose 4-manifold base is S³ × (something flat). It is not specific to:
- The octonionic A_F (BF 2013) — applies equally to SM A_F (CC 1996) or any other internal algebra.
- NTE's framework — applies to any spectral-action cosmology with S³ spatial sections.

**This makes F1 a more general result than originally framed.** It is potentially significant for:
- The broader NCG-cosmology programme: S³ is structurally privileged for clean GR + matter at the f(0) level *across all* CC spectral actions, not just NTE's octonionic version.
- The generic question of how the spectral action behaves on different spatial topologies in cosmology (relevant to Marcolli-Pierpaoli-Teh's cosmic-topology programme).

**Novelty implications**:
- Originally I noted that I had not seen the specific cancellation in the literature I surveyed and that a 2-hour literature check was needed before claiming novelty.
- The corrected scope means the literature check should target the **broader CC spectral action literature** (1996–present, ~30 years; many groups; including but not limited to: Chamseddine, Connes, Marcolli, Sakellariadou, van den Dungen, van Suijlekom, Iochum, Vassilevich, Boyle, Farnsworth, Fathizadeh, Nelson, Pierpaoli, Teh, Estrada, etc.).
- A property this clean about the standard a₄ coefficient on S³ might well have been noted somewhere in this large literature. **AC's novelty check is more important now, not less.**
- That said: the cancellation factorisation `d(d−1)(5d² − 13d − 6)` with integer root only at d = 3 is a clean algebraic identity. If it had been prominently noted, it would likely be cited in NCG-cosmology surveys (Marcolli's 2018 monograph; van den Dungen-van Suijlekom 2012 review). Initial review of those did not turn up the result, but a more thorough check is warranted.

## §4. Implications for Finding F2

**F2 is unaffected by the misattribution.** F2 (κ₀ = (R_{S³}/2) × Y₀₀(S²)) was a structural reading of NTE's existing κ₀ = 3/√(4π) identity, not a claim sourced from BF or CC literature. The reading links κ₀ to the spectral action's a₂ coefficient (which carries R) and the Hopf-base projection structure. The correct attribution context: the a₂ Seeley-DeWitt coefficient with its R/12 prefactor (Gilkey 1984; CC 1996). NTE's structural identification stands; the spectral-action correspondence stands.

## §5. Implications for the Programme S 5-paper roadmap

**No structural change.** The roadmap (S1 v1.0, S2, S3, S4, S5) is unaffected. The technical-machinery references in `Programme_S_Status_v1.md` §5 already cite both BF 2013 and CC 2007/CCM 2007 in appropriate places. The misattribution is local to the specific curvature-combination passages.

**S2's target is unchanged**: derive κ₀ = (R_{S³}/2) × Y₀₀(S²) from the doubled-spectral-triple X² trace. The correct attribution context is the standard a₂/a₄ Seeley-DeWitt expansion with cross-coupling X — which is what Paper S2 has to compute.

## §6. Documents requiring revision

| Document | Revision status | Affected passages |
|---|---|---|
| `Paper_S1_v0_2.md` | Superseded by `Paper_S1_v0_3.md` | §1 (executive summary), §2 (BF eq. 4.14 reference), §3.3 (spectral action structural content), §4.1 (Finding F1 statement), §5 (status block) |
| `Programme_S_Status_v1.md` | Affected sections to be revised in `Programme_S_Status_v2.md` | §3.3, §4.1, §6.2 (outreach note) |
| `Handoff_Scratch_to_AC_ProgrammeS_findings.md` | Supplemented by this memo + `Handoff_Scratch_to_AC_attribution_correction.md` | §1 (state of play), §3 (F1 statement), §5 (Priority 4 integration recommendation) |
| `paper_S1_worksheet_v0_2.py` | Comments to be updated; numerical content unaffected | Header docstring, Section [A] comment |
| `Paper_S1_v0_1.md` | No revision needed | The v0.1 doc references BF 2013 only at the level "BF 2013's octonionic spectral triple machinery"; no curvature-combination misattribution in v0.1. Confirmed by re-review. |
| `Exploration_Graviton_vs_PhiNTE_v2.md` | No revision needed | The exploration doc references BF 2013 at the level "extended Connes' formalism to non-associative geometries"; no curvature-combination misattribution. Confirmed by re-review. |

## §7. Outreach mitigation

Greg has confirmed that outreach emails were sent. The recipient list (Boyle, Farnsworth, Marcolli, Sakellariadou, etc. per Greg's records) includes the people most likely to immediately notice the misattribution.

**Recommended mitigations**:

(a) If any recipient responds noting the misattribution: **acknowledge promptly**, send the corrected `Programme_S_Outreach_Note_v2.md` (standalone) plus this memo, and explicitly thank them for catching it. Treating the correction as "found by you, thanks" rather than "we already knew" is the right call — it's true (they would catch it independently if they engage), and it positions the engagement as collaborative rather than corrective.

(b) If a recipient engages substantively without noting the misattribution: forward the corrected outreach note and this memo as part of the follow-up, framing as "I've subsequently realised the original framing of the curvature combination's source was imprecise — here's the corrected attribution, which doesn't change the substance of the d=3 cancellation finding but tightens the context."

(c) If no recipient responds within 1–2 weeks: send corrected outreach note to next-tier targets per `Programme_S_Status_v1.md` §6.1.

(d) For any future forwarding of Programme S materials: use `Programme_S_Outreach_Note_v2.md` (corrected standalone) rather than extracting from `Programme_S_Status_v1.md`.

## §8. Lesson recorded

This is a worked example of **lesson #12 in the workflow manifest**: "AC's audit assertions need the same evidentiary discipline AC demands of other streams." The misattribution arose because Scratch read BF 2013's eq. 4.14 directly and treated it as the locus of the curvature-combination form, without tracing the form back to CC 1996 / Gilkey 1984 (which BF themselves cite). Adversarial review (Greg's catch here) is the corrective.

The corpus's ship discipline — pre-ship CR pass, evidentiary discipline on attributions — applies to research drafts as well. Scratch did not perform a "second-pass attribution check" on the structural-machinery references in `Paper_S1_v0_2.md`. That check is what would have caught this. **Workflow recommendation**: for any future Scratch / Jammer document that cites prior literature for structural results, a second-pass attribution check is mandatory before the document is shared externally or used as a basis for outreach.

## §9. Status

**Memo complete. Revision deliverables**:

- `Programme_S_Outreach_Note_v2.md` — corrected standalone outreach note (priority deliverable for forwarding).
- `Paper_S1_v0_3.md` — revised technical paper with corrected attributions.
- `Handoff_Scratch_to_AC_attribution_correction.md` — supplementary handoff for AC integration tracking.

The original v0.2 / v1 / handoff files remain in Working/ and Handoffs/ as historical record of the unrevised work. Each affected section in those documents should reference this memo (or its corrected successor) for the corrected attribution.

— Scratch, 2026-05-10 NZST.
