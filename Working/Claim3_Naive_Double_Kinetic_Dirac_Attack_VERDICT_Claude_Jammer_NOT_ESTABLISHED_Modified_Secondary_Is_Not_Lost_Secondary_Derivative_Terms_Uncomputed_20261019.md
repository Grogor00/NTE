# Claim 3: cold attack. VERDICT (Jammer)

**Landing: Claim 3 is NOT ESTABLISHED as stated.** The gap is real and probably natural, but no work on file supports the conclusion "the BD ghost returns".

- Directive: Handoffs\Directive_AC_to_Jammer_Attack_Claim3_Cold_The_Only_Publishable_Candidate_20261019.md
- Pre-registration: Working\Claim3_Naive_Double_Kinetic_Dirac_Attack_PREREGISTRATION_Claude_Jammer_20261019.md (filed before reading the target)

**Read in full this session:**
- Working\NAIVE_DOUBLE_KINETIC_DIRAC_BD_Secondary_SOLUTION_CursorMain_20261019.md (the target)
- Working\DEEP_LIT_Dirac_Two_Vierbeins_BD_Ghost_Gap2_VERDICT_CursorMain_20261018.md
- Working\P09_Gate0_Lemma_S3_VERDICT_Scratch_D2_3plus1d_..._20261010.md (27.6 kB)
- Working\P09_Gate0_Lemma_S3_PHASE2_REVIEW_Jammer_on_Scratch_D2_..._20261010.md (my lane, 13.8 kB)
- Working\P09_Gate0_Secondary_Constraint_PREREGISTRATION_Scratch_forks_D1_D2_D4_..._20261009.md (where the D1/D2 forks are defined)

**Not read:** the S2 verdict, the S2 and S3 arbitrations, and the Gate-0 ADM round. My review does **not** depend on either arbitration. It rests on the S3 verdict body and the fork definitions, so the attribution question does not touch it.

[k] marks my own background knowledge, not read this session.

---

## 1. The central defect: a *modified* secondary is not a *lost* secondary

The Gate-0 forks (Scratch's pre-registration §1–§2) defined the outcomes as follows:
- D1: "bracket yields a secondary constraint; BD ghost removed".
- D2: "secondary constraint lost / spoiled … ghost returns".

S3 landed D2 on the finding ΔS ≢ 0, i.e. {C_g, C_f} ≈ S⁽⁰⁾ + ΔS with ΔS outside the HR polynomial class.

Two lapse-linear constraints exist (Claim 2, which I accept; see §3). With them, the logic of the HR/vierbein argument runs like this:
1. Preserving C_g requires ∫N_f {C_g, C_f} + ∫N_g {C_g, C_g} + (shift terms) ≈ 0.
2. If the derivative-of-δ parts of these brackets vanish weakly, the ultralocal part of {C_g, C_f} must vanish. That gives a secondary S′ := S⁽⁰⁾ + ΔS_ultralocal ≈ 0, whatever ΔS is.
3. Preserving S′ then fixes the lapse ratio N_g/N_f generically. The pair (second-class combination of C, S′) removes the BD mode, and the ghost stays out.

S3 states the first half of this itself (§4.4): "consistency for free N_f forces the **modified secondary** S^(ψ²) ≡ S⁽⁰⁾ + ΔS_ultralocal ≈ 0 as a candidate phase-space constraint." It then lands D2 because "the HR preservation proof does not extend" (§4.5). That is **absence of a proof**, not proof that the ghost returns.

Cursor's note (★) goes a step further than S3 does: "ΔS ≉ 0 ⇒ BD secondary lost ⇒ ghost returns (12 vs 11)". The middle implication is the one that is unsupported.

**The ghost returns only if one of these holds:**
- (i) **Derivative-of-δ terms in {C_g, C_f}, {C_g, C_g} or {C_f, C_f} do not vanish weakly.** Then preserving the primary becomes a differential condition that fixes a lapse instead of generating S′, and the secondary really is lost.
- (ii) **The modified secondary fails to fix the lapse ratio.** That would mean {S′, C_g} and {S′, C_f} both vanish weakly, giving a tertiary constraint and a different count.
- (iii) **The relative Lorentz parameters stop being auxiliary.** S3a says they remain auxiliary at O(ψ²).

Neither (i) nor (ii) has been computed anywhere on file.

**Route (i) is where S3 has a specific error that matters.** Its Term III dismisses the kinetic–kinetic piece as "(C_i^(D)(x) + C_i^(D)(y))∂δ, hence weakly zero on C_i ≈ 0". But **C_i^(D), the Dirac part of the momentum constraint, is not a constraint by itself.** Only the total C_i = C_i^g + C_i^f + C_i^ψ (diagonal diffeomorphisms) is. So that piece is not weakly zero as stated.

That uncomputed derivative-of-δ sector is **the most plausible actual mechanism of ghost return**. Pure HR needed a nontrivial cancellation there (1111.2070). Whether the Dirac insertions spoil that cancellation is the real question, and nobody has answered it.

**Self-correction (my lane).** The 2026-10-10 Jammer Phase-2 review converged on S3's D2. Its falsification criteria were all aimed at a fake D1 (a cancellation claimed but not shown). None of them tested whether ΔS ≠ 0 implies ghost return, so the inference error passed through adversarial review unexamined. The same reasoning appears in S2's D2, since the method and the fork definitions are the same. **The class finding is that the S2 and S3 "D2 = ghost returns" labels rest on the same non-sequitur.** I record this for AC. Under the directive's fences I do not reopen S2 or S3; AC decides whether the labels stand.

## 2. Answers to AC's three attacks

**(a) Is action (N) the right object?** Probably yes; it is natural.
- Minimal coupling of the *same* matter to both metrics, S_m[g] + S_m[f], is the "doubly coupled matter" proposal of Akrami–Koivisto–Mota–Sandstad (2013) [k; arXiv:1306.0004, which Cursor should fetch].
- Yamashita–De Felice–Tanaka (1408.0487) was written partly in response to that proposal and showed the scalar version is ghostly.
- (N) is the spinor member of that family. The referee's "why would anyone write it?" has a sourced answer, and the gap is interesting rather than contrived.
- My pre-registered a2 (unnatural, 0.5) fails, pending the fetch.
- a3 (already covered) is not supported by the deep-literature pass. Two further checks are needed before submission [k]: Hinterbichler–Rosen 2015 on vielbein matter couplings, and the de Rham–Heisenberg–Ribeiro vielbein-coupling papers.

**(b) Does S2/S3 transfer to (N)?** As a *setting*, yes. S3 §1 writes exactly action (N): two first-order kinetic terms, one spinor, diagonal Spin(1,3). So the import is not invalid on setting grounds. But what transfers is **ΔS ≢ 0 and "HR proof does not extend"**, not "ghost returns" (§1). There are also two technical issues:
- S3 evaluates at "time-gauge alignment φ₀ = 0 … without loss of generality". The relative boost is not gauge; only the diagonal Lorentz is. In the HR vierbein form it is tied to the shift sector. Evaluating at φ₀ = 0 is a special locus. That is acceptable for showing ΔS ≢ 0 (nonvanishing somewhere implies nonvanishing generically), but it is **not WLOG** for anything stronger.
- tr(S B) only sees the γ_g-symmetric part of B, because S is γ_g-self-adjoint. The residual outside span{I, S, S²} is therefore 6 − 3 = **3**, not "≥ 6". It is still nonzero, so the conclusion ΔS ≢ 0 survives; the stated count is wrong.

**(c) The dimension argument.** It is adequate for ΔS ≢ 0, the claim it supports. It is **not** adequate for ghost return, and a referee would rightly call it irrelevant to that claim. A referee would also ask for at least one explicit configuration with ΔS_ultralocal ≠ 0, which is cheap to supply. A full Fierz catalogue is not the missing piece. The missing piece is (i)/(ii) above.

## 3. Supporting claims
- **Claim 1** (single-tetrad lapse-linearity): correct and standard (Nelson–Teitelboim). Not novel; the note says so.
- **Claim 2** (both lapses linear for (N)): **sound.**
  - My own check: in time gauge, det F · F_A⁰ ∝ √γ_f Λ_A⁰(p), which is lapse-free. det F · F_Aⁱ = √γ_f(−Λ_A⁰ Mⁱ + M Λ_Aᵃ f_aⁱ), which is linear in the f-lapse and shift, including the relative boost.
  - Mini-superspace agrees: π = (i/2)(a³ + b³)ψ̄γ₀.
  - Yamashita's mechanism does not fire. This is elementary but correct.
- **Claim 4** (effective vielbein / single-metric as ghost-free alternatives): consistent with the deep-literature pass. I did not re-fetch Melville–Noller. It is phrased correctly as "not (N)".
- **"12 phase-space dof vs 11":** the label is wrong. Ghost-free bigravity has 7 dof (14 phase-space dimensions), and Dirac has 8 real phase-space dimensions (4 dof). So 11 vs 12 is a count of **dof**, i.e. 22 vs 24 phase-space dimensions. And the "12" follows only if the secondary is genuinely lost, which is the open question.

## 4. Grades
| Item | Grade |
|---|---|
| Claim 1 | Sound; not novel |
| Claim 2 | **Sound** (elementary extension) |
| **Claim 3** | **NOT ESTABLISHED.** The inference from a modified secondary to a lost secondary is invalid; the decisive derivative-of-δ / lapse-fixing sector is uncomputed; S3's Term III dismissal of it is erroneous |
| Claim 4 | Consistent with the literature on file |
| Dof count | Mislabelled; conditional on Claim 3 |

**Global: G4-adjacent, "unsupported as stated, open question real".** The pre-registered G-forks map as follows:
- not G1;
- not G3 (the action looks natural);
- G2/G4. The result is not publishable now. The issue is not missing polish: the stated conclusion does not follow from the work on file.

## 5. What would make it publishable
1. **Compute the full bracket set** {C_g, C_f}, {C_g, C_g}, {C_f, C_f} for (N) at O(ψ²), **including the derivative-of-δ terms**. Track C_i^(D) against the total C_i, not against itself.
2. **Run the Dirac–Bergmann chain to the end.** Find whether preserving the primaries generates S′ (then the ghost is removed at this order) or fixes a lapse (then the ghost returns). If S′ arises, find whether its preservation fixes N_g/N_f.
3. **Give one explicit non-isotropic configuration** that shows whichever outcome holds.
4. Then state the dof count with its convention.

Either outcome is publishable as a short note:
- "Dirac double coupling is ghost-free at O(ψ²), unlike scalars" would be the *more* surprising result.
- "Ghost returns via the derivative sector" would be the expected one.

The current filing claims the second without the computation that decides between them.

## 6. Prior check
| Pre-registered | Result |
|---|---|
| a2 at 0.5 | Fails (pending fetch) |
| b3 (partial transfer) at 0.4 | Closest |
| c2 (referee wants more) at 0.75 | Holds, but for a different reason than expected |
| Claim 2 true at 0.7 | Holds |
| Count ambiguous at 0.5 | Holds |

I did not pre-register the central finding (the inference gap). It came from reading S3 §4.4 against the fork definitions.

## 7. On "AC wants it to be true"
The result AC wants (the ghost returns, so a clean no-go) may well be true; the derivative sector is a live mechanism for it. It is not shown. Publishing it now would invite a referee to make the §1 point in one paragraph.
