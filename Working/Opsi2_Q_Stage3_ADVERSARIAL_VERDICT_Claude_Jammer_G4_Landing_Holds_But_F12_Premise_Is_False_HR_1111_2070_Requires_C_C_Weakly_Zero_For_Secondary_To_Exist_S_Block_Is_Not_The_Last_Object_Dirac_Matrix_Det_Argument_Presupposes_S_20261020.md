# Q-Stage3 — ADVERSARIAL VERDICT (Claude Jammer)

**Bottom line.** I agree with the G-4 landing. I do not agree with the reasoning AC ratified. The F12 premise, as it was written into the GO, the chain reference, and both verdicts, is contradicted by Hassan–Rosen 1111.2070. The consequence is that the S-block is not the last object; there is an object before it.

**Pre-registration (filed before reading either Q-Stage3 verdict):** `Working\Opsi2_Q_Stage3_ADVERSARIAL_PREREGISTRATION_And_Cursor_Round6_REVIEW_Claude_Jammer_..._20261020.md`. It was filed at 12:25:38Z. Scratch's pre-registration was filed at 12:26:47Z and Cursor's at 12:38Z.

**Read in full this session:**
- `Working\Opsi2_Q_Stage3_VERDICT_Scratch_lands_G4_sharpened_..._20261020.md`
- `Working\Opsi2_QStage3_C_SC_Self_Bracket_VERDICT_CursorMain_G4_Excess_hg_I_minus_2X_p_No_Class_Loss_From_Self_Bracket_Fork_Needs_S_Block_20261020.md`
- `Handoffs\RULING_AC_QStage3_Ratified_Excess_Is_Cross_Piece_S_Block_Is_The_Last_Object_20261020.md`. The text I received was truncated at §6.
- Hassan & Rosen, arXiv:1111.2070, *Confirmation of the Secondary Constraint and Absence of Ghost in Massive Gravity and Bimetric Gravity*. I read it through two web-extraction passes. The PDF extraction **dropped Poisson braces, ≈ signs and some indices**, so what follows is verbatim where it is prose and **paraphrased with equation numbers where it is an equation**. Any lane relying on this verdict should verify those equations against the PDF itself.

**Not read:** the Cursor .py, .wl and .json result files; Scratch's pre-registration body; Cursor's pre-registration body.

**No Core. No f. No computation by this lane. Posteriors held.**

---

## 1. What Hassan–Rosen actually say about {C, C}. This is the source that settles F12.

From 1111.2070:

- **§1:** "A condition for consistency is the preservation of this constraint in time, d𝒞/dt=0. This condition will lead to a secondary constraint, **provided the Poisson bracket of 𝒞 with itself vanishes on the constraint surface.**"
- **§3, case 1 (after eq. 3.4):** if the bracket does not vanish, "(3.4) becomes an **equation for N** and does not act as a constraint on" (γ, π). The result is "a theory with an odd dimensional phase space, or equivalently, with **5.5 propagating modes**."
- **§3, case 2 (eq. 3.5):** if the bracket vanishes, "the condition (3.4) is independent of N and thus acts as a secondary constraint." That secondary is C_(2) = {C, H₀}.
- **Eqs. 3.17 → 3.23 → 3.24 → 3.25 (paraphrased; symbols dropped in extraction):** {C(x), C(y)} is a combination of ∂δ terms acting on P^i. The n^i equations of motion give **P^i = C D^i_l n^l**. The bracket is therefore proportional to C itself (times D n ∂δ), and so it **vanishes weakly**.
- **§4 (bimetric):** "The primary constraint C **commutes with itself on the constraint surface.**" In the bimetric case, N multiplies C and the f-lapse L sits in H₀.

## 2. Consequences

**F-a. The F12 premise is false.**
- The chain reference (§4) says: "pure HR's {C_SC, C_SC} ≠ 0 is expected and healthy (handled by the second-class pair) — NOT by being weakly zero."
- Scratch's Q-Stage3 §1 repeats this, and the AC ratification §2 builds on it.
- HR say the opposite. In pure HR the self-bracket **is** weakly zero, and that is the condition for the secondary S to exist at all. A self-bracket that is not weakly zero is HR's case 1: the lapse is determined, 5.5 modes. That is the ghost-type failure.
- What survives of F12 is narrower: "non-zero off-shell" is not "non-zero weakly," because HR's bracket is non-zero off-shell and vanishes on C = 0. **"Non-zero weakly" is exactly the G-2 (via ∂δ) signal.**

**F-b. Cursor's Dirac-matrix argument is mis-ordered.**
- Cursor argues det[[a, b], [−b, c]] = ac + b², so with c = 0 and b ≠ 0, a is irrelevant.
- That presupposes S exists. In HR, S is generated **only if** a ≈ 0.
- If the matter-coupled a is not weakly zero, the preservation equation fixes N, and there is no S to pair with. The 2×2 matrix never forms.
- So a is not "one entry" whose value is immaterial. It is the gate that comes before the S-block.

**F-c. The S-block is not the last object.** AC §4 says "There is nothing smaller behind it." But per HR eqs. 3.17–3.25 there is a prior object:

> **Is the matter-coupled ∂δ coefficient of {C, C} proportional to the constraints (C itself, total C_i, χ) once the n^i equations are modified by matter?**

- This is the analogue of HR eq. 3.23/3.24. It is my pre-registered A1 object, the ∂_jN coefficient.
- If it is weakly zero, S exists and the S-block decides between G-1 and G-2.
- If it is not weakly zero, the result is G-2 via ∂δ (HR case 1), and the S-block is moot.

**F-d. The D n channel is HR's own closure mechanism.**
- HR close {C, C} through P^i = C D n, which uses the n equation of motion.
- Cursor's verdict lists channel (2a) as "R6 debt; not Q-Stage3 object." That is wrong. The D n route (both the matter-modified δn and the background-ξ × matter term) is *exactly* how the Q-Stage3 object closes or fails to close.
- This confirms AC R5 §6 item (2) and my pre-registration A2. It refutes the chain reference's "no D-matrix needed."

**F-e. The C_SC ≈ C_g − C_f construction may not be HR's C.**
- In HR bimetric (§4), C is the coefficient of N, and L multiplies H₀.
- If action (N) is mapped the same way, C_f^(ψ) sits in H₀, not in C. In that case the cross term {C_g^(ψ), C_f^(ψ)}, which is Scratch's −2h_g X p, would appear in {C, H₀}, i.e. in the **secondary**, and not in {C, C}.
- This is a structural reading of §4; I have not computed it. If it holds, the "cross piece" is mis-staged a second time.
- **This mapping must be settled before any lane computes further.**

**F-f. K0′ was not passed by either lane.**
- Scratch cites the HR literature and calls it structural; he did not re-derive it. His §1 claim that pure HR has "no gravitational ∂δ cross" may be correct, but his claim that pure HR's {C_SC, C_SC} "is absorbed by the C_SC/S pair" is the false premise above.
- Cursor's excess comes from a skeleton under π_g + π_f + p = 0. That is not HR eq. 3.17–3.24 reproduced.
- The proper K0′ is now concrete: **reproduce HR eq. 3.24, {C, C} ∝ C D n ∂δ, from the lane's own code at generic n**, then add matter.

**F-g. θ weights: third flag, and Cursor has regressed.**
- Both Q-Stage3 verdicts use the unweighted W = h_g(I − X)², and Scratch again writes "w = 1 K1-forced" (F16/F17).
- Cursor's R6 used the θ form. Its Q-Stage3 verdict does not.
- The unweighted form is the special locus √γ_g = √γ_f (F1).

## 3. Self-correction (this lane)

- My pre-registration A1 recalled that HR's ∂N coefficient is "proportional to the momentum constraint." **That was wrong in detail.** HR's coefficient is proportional to **C itself**, via the n equation of motion (eq. 3.23, P^i = C D n).
- The criterion is unchanged in substance: weakly zero means a secondary exists, and not weakly zero means the lapse is fixed. But the constraint set in A1 must include C.
- I am also re-examining the whole class of claims in my own filings: my pre-registration called the HR mechanism "unverified this session." It is now read via extraction and corrected here.

## 4. Fork and standing

- **Landing: G-4. I agree with both lanes on the landing, not on the route.** The decomposition (diagonal + cross) and the result "cross ∉ span{h_g, h_f}" are algebraically fine as statements about R_j. Their interpretation as "the excess, to be absorbed by the S-block" is not ratifiable until F-c and F-e are settled.
- **"The chain cannot be closed at O(ψ²) with current methods" is not yet well-supported.** The remaining object is smaller than the S-block and has a published template: HR eqs. 3.17–3.25 with matter added and the n equation modified. That is tractable.
- **Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. I ran no computation. F-a does make G-2-via-∂δ a sharp, decidable question.

## 5. The next object (requested GO content)

1. Settle the mapping of action (N) onto HR's (N·C + L·H₀) split: which matter pieces sit in C, and which in H₀ (F-e).
2. K0′: reproduce HR eq. 3.24 at generic n.
3. Compute the matter-coupled {C, C} ∂δ coefficient with:
   - the θ weights;
   - the χ Dirac correction;
   - the matter-modified n equation (δn(p));
   - the background-ξ × matter term (2a).

   Then decide whether it is ∝ (C, C_i, χ) on the constraint surface.
4. Only if it is weakly zero, compute the S-block.

— Claude Jammer, 2026-10-20.
