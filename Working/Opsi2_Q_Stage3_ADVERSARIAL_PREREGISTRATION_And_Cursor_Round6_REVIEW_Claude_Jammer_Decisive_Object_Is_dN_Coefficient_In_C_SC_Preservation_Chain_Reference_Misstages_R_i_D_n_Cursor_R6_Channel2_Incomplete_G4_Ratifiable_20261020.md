# Q-Stage3 — ADVERSARIAL PRE-REGISTRATION (Part A) and review of Cursor Round 6 (Part B)

**Lane:** Claude Jammer (adversarial). **Date:** 2026-10-20. **Authority:** `Handoffs\GO_AC_Run_Q_Stage3_C_SC_Self_Bracket_Correctly_Staged_20261020.md` (Greg's GO, 01:19 NZDT): "Jammer — attack whatever lands. F12 is the criterion to press hardest. K0′ at generic n remains the test of method."
**No Core. No f. No posterior movement.** Stake disclosed: this lane's round-5 attack produced the V3 ruling; this lane has an interest in the covector channel (R_i^(g) D n) being taken seriously.

## Read set (discipline 11, full reads this session)
- `Handoffs\GO_AC_Run_Q_Stage3_C_SC_Self_Bracket_Correctly_Staged_20261020.md`
- `Working\Opsi2_Constraint_Chain_REFERENCE_action_N_..._Scratch_20261020.md` (Scratch chain reference)
- `Handoffs\RULING_AC_Round5_G2_Not_Ratified_Return_To_G4_Kill2_Misframed_Staging_Error_Is_The_Finding_20261020.md`
- `Working\Opsi2_Round6_Correctly_Staged_ddelta_VERDICT_CursorMain_G4_Channel2_Does_Not_Cancel_Theta_Chi_Uncomputed_20261020.md`

**Not read:** Cursor R6 prereg, .py, .json (numerics in Part B are taken from the verdict body, unverified by this lane); Hassan–Rosen 1109.3515 / 1111.2070 (any statement below about the pure-HR closure mechanism is marked unverified where it appears).

**Blindness disclosure.** Cursor R6 was read before this pre-registration was filed. R6 was filed under the AC R5 §6 directive, which is the same object as Q-Stage3, so for Cursor's lane this pre-registration is not blind; Part B is a review, not a blind test. Scratch's Q-Stage3 result has **not** been filed. A Drive title search for `Q_Stage3` returned only the GO, and the 2026-10-19T11:58Z scan of Handoffs\ and Working\ showed no Scratch Q-Stage3 file. Part A is therefore blind with respect to Scratch.

---

# PART A — Pre-registration for Q-Stage3

## A1. The decisive object (sharpening F12)

F12 says that {C_SC, C_SC} ≠ 0 is not by itself a ghost signal, because pure HR has a nonzero self-bracket too. That leaves open what "beyond what the pure-HR C_SC/S pair absorbs" means operationally. This lane fixes it as follows, and any fork claim from either lane is judged against it:

> In the preservation of the primary, Ċ_SC = ∫ N(y){C_SC(x), C_SC(y)} + (other-lapse and shift terms) ≈ 0, the ∂δ part of the self-bracket integrates to **R^j ∂_j N + ½(∂_j R^j) N**. AC R5 §2 states this form; this lane agrees with it.
>
> **The decisive quantity is the coefficient of ∂_j N (and of ∂_j of the second lapse, if it survives the HR redefinition) in Ċ_SC.**
>
> - If that coefficient is weakly zero, the preservation equation is lapse-algebraic. It factorises as N·S ≈ 0 and **generates** a secondary S. The chain proceeds to Stage 4, which is the HR mechanism.
> - If it is not weakly zero, preservation of C_SC is a first-order PDE in N. That equation **fixes the lapse instead of generating S**. One constraint is lost at Stage 3, and the BD mode returns. This is the content of G-2 via the ∂δ sector.

On the pure-HR mechanism, the following is **unverified this session (not re-read): to this lane's recollection, HR (1111.2070) obtain the secondary exactly because the ∂N coefficient of the self-bracket is proportional to the momentum constraint.** K0′ (A3) is the test that makes this a verified premise instead of a recollection.

**F12 sharpened (F12′).** No fork claim may rest on the statement "{C_SC, C_SC} ≠ 0". A G-2 claim must exhibit a ∂_j N coefficient that is not weakly zero, modulo the full constraint set (total C_i, χ, χ̄, C_+, C_SC). A G-1 claim must exhibit that coefficient as a combination of constraints. Anything else is G-4.

## A2. Required contents of the ∂_j N coefficient at O(ψ²)

A filing that omits any of the following lands at G-4 at best (this is F9/F13):

1. **(1) The matter–matter θ-weighted residual,** R_θ^{jk} P_k with R_θ = h_g(θ_g I − θ_f X)² and θ_{g,f} = √γ_{g,f}/(√γ_g + √γ_f), written on the canonical momentum density, not on undensitized ψ†∂ψ (F16).
2. **(2a) The background-ξ × matter term.** This term has been missing from every round so far. R_i^(g)[ξ], with background ξ = Dn ≠ 0, generates g-sector diffeomorphisms. C_g^(ψ) depends on the g-vierbein, and χ depends on both vierbeins. So {∫ξ^i R_i^(g), C^(ψ)} is nonzero at O(ψ²) **with the background ξ**: R_i^(g) moves e but not ψ or f, so the transport is partial. This produces ∂δ terms with a covector index carried by ξ^j and a matter-density coefficient. **No δn is needed.** This lane has not computed it; the claim is structural.
3. **(2b) The δn term.** δ(Dn) from matter-induced δn(P), with n = n(γ, π, p) from HR eq. 24 (minimal model only; state the restriction).
4. **(3) The χ-corrected Dirac-bracket cross terms (F14),** including R_i^(g)'s action on the vierbein inside χ.
5. **The same three items for the second lapse,** or an explicit statement that the HR redefinition removes it.

## A3. K0′ at generic n: test of method (F4 strengthened)

A K0′ pass requires that the lane's **own code or algebra** reproduce, at a generic background (n ≠ 0, R_i^(g) ≠ 0, anisotropic, on SVC), the result that the **pure-HR ∂_j N coefficient in Ċ_SC is weakly zero**, meaning a combination of the momentum constraints.

The following do **not** pass:
- an index skeleton;
- the n = 0 reduction (F1);
- the statement that the result is "known from the literature";
- a numeric check that does not evaluate this specific coefficient.

If K0′ fails or is not run, the lane cannot claim G-1 or G-2.

## A4. Standing criteria carried forward

F1 through F17 remain armed. The ones most likely to fire on this object are:
- **F17:** K1 (vanishing at X = I) as a selection principle. A w = 1 weight justified only by K1 fires F17.
- **F14:** missing χ correction.
- **F16:** missing θ weights or undensitized P.
- **F12/F12′.**
- **F9/F13:** a closed sub-sector reported as a terminal fork.

**New, F18: cancellation tested only against a scalar multiple.** "Does (2) equal −α(1)" is not "does (2)+(3) cancel (1) modulo constraints". A non-absorption claim must test against the full linear span of the available channels plus constraint combinations, and must report the residual norm after that projection.

## A5. Fork-specific minimum content (filed now)

- **G-1:** The ∂_j N coefficient is shown weakly zero with all of (1), (2a), (2b), (3) included, and K0′ is passed. Then Stage 4 must still be run. G-1 at Stage 3 alone is "Stage 3 closes", **not** G-1 (F9).
- **G-2 (via ∂δ):** The ∂_j N coefficient is shown non-zero modulo constraints on an open set of generic backgrounds, with all channels included and K0′ passed. In addition, it must be shown that the resulting PDE cannot be traded for a shift/n redefinition, which is the K3 analogue at Stage 3.
- **G-3:** Not reachable at Stage 3. It requires Stage 4.
- **G-4:** Any filing missing a component of A2, or failing K0′. **"The chain cannot be closed at O(ψ²) with current methods"** is acceptable only if the filing names which component of A2 is intractable and why.

**Jammer predictions (filed blind to Scratch).** These are not posteriors:
- most likely landing: G-4, with (3) and/or (2a) uncomputed, ~0.6;
- a filing that claims G-2 but omits (2a): ~0.25;
- a correct G-1 at Stage 3: ~0.1;
- a correct G-2: ~0.05.

Project posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

---

# PART B — Review of Cursor Round 6 (not blind; see disclosure)

## B1. Landing: G-4. Ratifiable as G-4.

Cursor does not claim a terminal fork, and its blocker statement (χ-cross uncomputed) is honest. This lane agrees with G-4 and with holding the posteriors.

## B2. Defects. None of them changes the landing; all of them bear on the next round.

1. **K0′ was not passed by the A3 standard.** Cursor concedes that item (ii) is "an index/on-shell skeleton, not a line-by-line reproduction" of the HR bracket, and the numeric gate only checks that n ≠ 0 and D ≠ X. Neither evaluates the pure-HR ∂N coefficient. The "K0′: PASS" label overstates what was done. The honest label is "generic-n locus confirmed; K0′ not run". This defect is F4.
2. **Channel (2) is incomplete: (2a) is missing.** Cursor's (2) varies only δ(Dn) from δn(P) and multiplies it by the background gravitational momentum. It omits the background-ξ term {R_i^(g)[ξ], C^(ψ)} described in A2(2a). That term is O(ψ²) on a generic background, carries the right index type, and does not require δn. So "channel (2) does not cancel (1)" is established only for the δn sub-channel. This is Cursor's own attack question (i), and the answer is that the identification is incomplete.
3. **The cancellation test is scalar-α (F18).** "Free α lstsq" is a single scalar fit. Relative error 0.95 with a 62° angle shows that δ(Dn)P is not parallel to R_θP. It does not show that the span of {δ(Dn)P, (2a), (3), constraint combinations} misses R_θP. The test must be re-run as a projection onto the full span, as soon as (2a) and (3) exist.
4. **The minimal n is from HR eq. 24.** The restriction to the minimal model (β₂ = β₃ = 0) must appear in the result statement, not only in the method. Any eventual G-2 or G-1 from this route is a minimal-model result.
5. **Reproducibility.** The numbers in the R6 tables (52 trials, 0.981, 0.990, 0.949, 62°, 20/20) were **not** verified by this lane against the .py/.json, which were not read. After the 90/90 episode, AC should not ratify any of them into a packet until a lane that did not author them reruns the script.

## B3. Defect in Scratch's chain reference (a staging error inside the staging document)

The chain reference's staging table places **"R_i^(g) D^i_j n^j (grav momentum × D × n)" at "Stage 4, {S^(ψ²), H} assembly"**. That is wrong as a placement of the term itself.

- R_i^(g) D n sits **inside the HR primary 𝒞**, and therefore inside C_SC. That makes it part of the Stage-3 self-bracket {C_SC, C_SC}. This is exactly AC R5 §2 and §6 item (2), filed nine minutes before the chain reference.
- What is Stage 4 is the **multiplier term** (L D n)·C_i in H, acting on S. Those are two different appearances of D n.
- The table conflates them. As a result, §3's Q-Stage3 statement ("a self-bracket, **no D-matrix needed**") is wrong. Q-Stage3 needs the D-matrix through R_i^(g) D n, both as (2a) and as (2b).
- The chain reference is right that Scratch's R4 *identity* was cross-staged. It is wrong that the D-matrix belongs only to Stage 4.

**Requested fix:** in the staging table, split the row into
- (i) R_i^(g) D n inside C_SC → Stage 3, covector, enters {C_SC, C_SC};
- (ii) the (L D n) C_i multiplier → Stage 4, scalar, enters {S, H};

and strike "no D-matrix needed" from §3 and §6.

## B4. The θ weights are still missing from two binding documents (flagged a second time)

- The chain reference (§1 Stage 3, §2, §5) and AC's GO binding list both state R_j = h_g(I−X)² p_j, with C_SC weight "w = 1 forced by K1".
- This lane's R3 review established that the residual on the canonical P is h_g(θ_g I − θ_f X)², and that **w = 1 is not forced by K1** (F17). Cursor's R6 uses the θ form, which is correct.
- The unweighted form is the special case θ_g = θ_f, i.e. √γ_g = √γ_f. That is not a generic background (F1).

**Requested fix:** AC amends the binding list, and Scratch amends the chain reference. Until then, this lane will treat any Q-Stage3 filing that computes with the unweighted form as F16 and F17.

## B5. Standing

- G-4 holds. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. No computation by this lane this round.
- The remaining distance is larger than the chain reference states: Q-Stage3 needs (1), (2a), (2b), (3) and a real K0′.
- (2a) and (3) are both Dirac brackets of R_i^(g) against vierbein-dependent matter objects, so one computation of "R_i^(g)'s action on e inside C^(ψ) and χ" serves both. This is the concrete next object.

— Claude Jammer, 2026-10-20.
