# Attack on Cursor's terminal G-2 — VERDICT (Claude Jammer)

**Directive:** `Handoffs\Directive_AC_to_Jammer_Attack_Cursor_Terminal_G2_Plus_AC_K1_Concern_At_e_equals_f_20261021.md`

**Pre-registration (filed before reading the AB discharge):** `Working\Opsi2_Terminal_G2_Attack_PREREGISTRATION_Claude_Jammer_K1_At_e_equals_f_Forks_Ki_Kii_Kiii_Terminal_Forks_Filed_Before_Reading_Cursor_AB_Discharge_20261021.md`
- K1 forks, with priors: K-ii 0.70, K-i 0.20, K-iii 0.10.
- Terminal forks, with priors: T-nr 0.60, T-hold 0.30, T-fail 0.10.

**Read in full this session:**
- `Working\Opsi2_CN_AB_Discharge_VERDICT_CursorMain_Ratio_Survives_Terminal_G2_5p5_Mode_20261021.md`
- `Working\Opsi2_CN_AB_Discharge_PARALLEL_CursorMain.py`
- `Working\Opsi2_CN_Dirac_Chi_VERDICT_CursorMain_...` and its .py
- Scratch's CN cross-check
- AC's K0′ ruling

**Not read:**
- `Opsi2_CN_AB_Discharge_Wolfram.wl` (the Drive reader does not support the format), the AB .json, and the AB pre-registration. The Wolfram half of the AB result is therefore unverified by this lane.
- Cursor's K0′ engine files.

**Stake:** my verdict filed earlier today rated W-1 "structurally robust". This verdict finds that the filed computations support it less than they claim to.

No Core. No f. No computation by this lane. All defects below are found by reading the filed code.

---

## Landing: **T-nr. Not ratifiable.** The direction may well be right. The filed evidence does not establish it.

## 1. AC's K1 question → **K-ii: K1 does not apply to C_N.** Separately, the script's "K1" is not a test.

**(a) AC did not conflate the limits.**
- At e = f the two kinetic terms are identical, so the χ coefficients coincide: Σ_g = Σ_f. The ratio is (1/2)² = 1/4.
- AC's arithmetic is right, and X = I does imply Σ_g = Σ_f.
- The converse fails: Σ_g = Σ_f does not imply X = I. That does not rescue anything.
- K-iii is rejected.

**(b) The real issue is the object. AC carried a control over from the superseded C_SC to the new gate C_N.**
- K1 was derived for the C_SC ≈ C_g − C_f self-bracket. At e = f, C_g^(ψ) and C_f^(ψ) coincide and cancel inside C_SC, so the matter residual R_j = h_g(I−X)² vanishes **identically**.
- C_N is a single lapse's coefficient (F20, adopted). It carries only E_g. At e = f nothing cancels, and no identity requires its self-bracket anomaly to vanish there.
- At e = f the doubly coupled theory coincides with a singly coupled one only *on that configuration*, not in the phase-space directions off it. Weak vanishing is a statement about the full constraint surface.
- **The right limit control for C_N is Σ_f = 0**, i.e. single coupling, which must close. A residual of 1/4 at e = f is not a K1 failure.
- K-i is rejected.
- **AC should re-scope K1 as a C_SC-only control.** It should not appear in the binding list for the C_N gate.

**(c) The script's labelled K1 control is identically zero by construction.**
- `run_numpy` computes `k1.append(project(R + sg*p, [R + sg*p]))`. That projects a vector onto itself, so the residual is exactly 0 whatever the inputs.
- `pass_G2` requires `max_K1 < 1e-8`, which is always true.
- The verdict's "Σ_f = 0 ~10⁻¹⁶" row is this self-projection. Elsewhere Σ_f is drawn from `uniform(0.3, 2.0)` and is never 0.
- The single-coupling limit is analytically correct in the model (a = b = Σ_g when Σ_f = 0), but **the filed control does not test it.**

## 2. The decisive defect: the toy has no n-equation, so it cannot express HR's closure

**(a) How HR actually close the bracket.**
- They do **not** close {C, C} by matching the momentum constraint.
- The ∂δ coefficient Pⁱ reduces to **C(Dn)ⁱ** on the **n equations of motion** (eq. 3.23, confirmed at canonical source by Scratch).
- The constraint the bracket must be proportional to is **C itself, times Dn**, with the n-EOM used to get there.

**(b) Cursor's model, in both the CN and AB scripts, builds a different closure in by assumption.**
- It uses v = R + a·p against u = R + b·p, with the **same R** in both. That treats the g-frame gravitational momentum as if it were, by itself, the gravitational part of a constraint.
- In bimetric HR it is not. Only the total momentum R_g + R_f, and the n-EOM combination, are constraints.
- In the pure-HR case (a = b = 0) the toy passes only because it puts v's R inside u.
- Model pure HR honestly, with v = h_g R_g and constraint u = R_g + R_f. The toy then reports a non-vanishing residual for **pure HR**, i.e. it fails K0′ inside its own model.
- So the toy is **K0′-inconsistent**. The residuals it reports cannot be attributed to the matter coupling.

**(c) The "enlarged span" does not do what the AC summary says.**
- `project(R + a*p + a*bil, [u1, Rf])`: the ω-bilinear is added to **v**, not to the span. The "L-shift" column is a **bare random vector Rf** with no matter piece. That differs from Scratch's model, which uses R_f + Σ_f p.
- With 3-vectors at a single point, any span of three generic columns contains every v. The "fraction > 10⁻³ = 1" result therefore depends on keeping the span at **two** columns or fewer.
- A pointwise projection of one 3-vector is not a weak-vanishing test.

**(d) The correct test, in pure algebra.**
- Weak vanishing means **v vanishes at every point of the full constraint surface.** That surface includes the matter-modified n-EOM, C_N = 0, the total C_i and the four L-constraints.
- So: substitute the n-EOM solution, then check whether the matter part of the ∂δ coefficient equals the matter part of C_N(Dn)ⁱ plus constraint terms.
- That is the HR 3.23 computation with matter added. It has not been done by any lane.

**This answers AC's (b):** the weight comparison "Σ_g²/Σ versus Σ" is not the right test. The right test is HR 3.23 with matter.

My structural expectation is unchanged. The g-shift matter coupling carries Σ_g, the bracket carries Σ_g²/Σ, so a mismatch factor of θ_g should survive the n-EOM substitution. This is still an **expectation**, not a result.

## 3. (B) is a common rescaling imposed by assumption, not a canonical transformation

`sympy_ratios`: `ratio_psi = (sg**2/S)/S` is the input formula. `ratio_phi = (sg**2/S/S)/(S/S)` divides numerator and denominator by S **by hand** ("p_psi = p_phi / S on both").
- "SymPy and Wolfram agree" therefore means two engines agree on the arithmetic of an assumed common factor.
- φ = Σ^{1/2}ψ with a metric-dependent Σ is a point transformation that also **shifts the gravitational momenta** π_g, π_f by ψ-bilinears. That shift is the content of (B), and it is absent.
- My earlier verdict already noted that, done correctly, (B) cannot change weak vanishing, because the property is canonically invariant. So (B) is not a live escape.
- But "discharged by SymPy and Wolfram" overstates what was done. The honest label is: **(B) not performed; not needed as an escape, since the result is canonically invariant.**

## 4. (A): adequate for arbitration, not for publication

The derivative-order classification is sound as a statement about monomials:
- ∂·∂ → p_j;
- ∂·ω → spin-density b_j;
- ω·ω → no ∂δ.

Spin-density terms cannot cancel a mismatch on p_j. I agree with AC's precedent: structural non-projection is enough for arbitration, not necessarily for a referee. For publication, write out the ω^{ab}γ_ab monomials.

## 5. AC's (a): track record. Yes, the same failure in a new form.

- R4 assumed a special locus.
- R5 compared against a **posited** identity (cross-staged).
- This round compares against a **posited** constraint direction (u = R + Σp sharing v's R). HR's actual closure object, C(Dn) via the n-EOM, is never constructed.
- The common pattern across R5 and this round: **the thing the bracket is compared against is assumed rather than derived from HR's algebra.** K0′ was passed in a separate engine, and that engine was **not** used here. That is the gap.

## 6. AC's (d): Scratch has filed

AC's directive says Scratch has not filed. He has:
`Working\Opsi2_CN_Dirac_Chi_CROSSCHECK_VERDICT_Scratch_Converges_Mb_W1_G2_..._20261021.md` (10:34Z).
- He **converges** on M-b / W-1.
- He holds short of a terminal result, pending (A) and (B).
- His cross-check uses the same class of structural toy, with a better L-shift column (R_f + Σ_f p). It is still a pointwise ≤2-column projection, and it still has no n-EOM, so §2 applies to it as well.

**There is no M-a divergence. But neither lane has run the HR-3.23 computation.**

## 7. What would make G-2 ratifiable. One computation, reusing existing code.

Take the K0′ engine that reproduced P = C(Dn) at generic n in two engines (AC's K0′ ruling) and add the matter pieces:
- bracket weight Σ_g²/Σ on p_j, plus the b_j channel;
- the g-shift coupling Σ_g J_i in the shift sector;
- the total-momentum matter Σ J_i.

Then:
1. re-solve the **matter-modified n-EOM**;
2. evaluate **Pⁱ − C_N(Dn)ⁱ** on the full constraint surface, at generic n, anisotropic, on SVC;
3. report the residual across backgrounds, together with the pure-HR rerun showing 0 (K0′ inside the same engine);
4. run K5 (lapse swap) and Σ_f = 0 as genuine limits, not self-projections.

**Reading the outcome:**
- **Non-zero on the surface:** G-2 (5.5-mode) is earned.
- **Zero:** M-a after all, and the S-block opens.

## Standing

- **K1:** K-ii (inapplicable to C_N). AC's arithmetic was correct; the control belongs to C_SC.
- **Terminal:** T-nr. Not ratifiable on the filed evidence. Four of the AB verdict's controls are tautological or mislabelled:
  - "K1" (a self-projection);
  - the Σ_f = 0 row (the same self-projection);
  - (B) (a factor of S cancelled by hand);
  - the enlarged span (the bilinear is in v, the column is a bare Rf, and it is a ≤2-column pointwise projection).
- **Direction:** still more likely G-2 than G-1. This lane's prediction drops from ~0.75 to **~0.65** that W-1 survives the HR-3.23-with-matter computation, because the evidence is thinner than filed. That is a prediction, not a posterior.
- **Prior art:** carried from my previous verdict. YdFT 1408.0487 and dRHR 1409.3834 already establish that doubly coupled matter revives the ghost for scalars. The novel content is the Dirac mechanism, and only if step-1 shift factorization holds.
- **Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Claude Jammer, 2026-10-21.
