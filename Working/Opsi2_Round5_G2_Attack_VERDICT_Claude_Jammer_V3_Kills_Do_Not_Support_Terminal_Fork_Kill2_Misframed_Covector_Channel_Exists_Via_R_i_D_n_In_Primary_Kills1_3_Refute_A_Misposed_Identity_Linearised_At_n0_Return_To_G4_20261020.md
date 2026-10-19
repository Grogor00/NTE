# Round-5 G-2 attack: VERDICT (Jammer). **V3: the kills do not support a terminal fork. Return to G-4, with the gap named.**

- Directive: Handoffs\Directive_AC_to_Jammer_Attack_Cursor_Round5_G2_Terminal_Landing_20261020.md
- Pre-registration (filed before reading the target): Working\Opsi2_Round5_G2_Attack_PREREGISTRATION_Claude_Jammer_Filed_Before_Reading_Cursor_R5_20261020.md

**Read in full this session:**
- the target: Working\Opsi2_Round5_X_Identity_VERDICT_CursorMain_G2_Absorption_Identity_Fails_Computational_Suite_20261019.md
- Cursor R4: Working\Opsi2_Round4_D_Matrix_Preservation_VERDICT_CursorMain_G2_..._20261019.md
- Scratch R4: Working\Opsi2_Round4_VERDICT_Scratch_lands_G4_new_reason_..._20261019.md
- Cursor's verification of AC's read: Working\Opsi2_AC_R5_G2_READ_VERIFICATION_CursorMain_20261020.md

**Not read:**
- the R5 compute script and JSON. I rely on the verdict text, and on Cursor's own audit of the script for the 90/90 and SymPy points.
- Cursor's R4 amendments. I know their withdrawal content only from their titles and from R5 §4.

## 1. Kill 2 ("type mismatch: scalar vs covector") is misframed, and a covector channel exists

**(i) Both sides end up as scalar equations.**
- R^j enters {C_SC(x), C_SC(y)} as the coefficient of ∂_jδ.
- In the preservation equation Ċ_SC(x) = ∫N(y){C_SC(x), C_SC(y)} + …, that piece becomes R^j∂_jN + ½(∂_jR^j)N, which is a **scalar**.
- So "a scalar cannot cancel three covector components" compares an *integrated* equation with a *pre-integration coefficient*. It is not a kill.
- The correct statement: the ∂δ coefficient must vanish weakly, or else the preservation equation involves ∂N. Any cancellation must therefore come from **another ∂δ coefficient of covector type** in the same bracket.

**(ii) Such a covector-type ∂δ channel exists, and Cursor's own R4 names it.**
- R4 §1–§2: the HR primary is 𝒞 = M_g²R^0(g) + **M_g² R_i^(g) D^i_j n^j** + 2m²M²_eff√γ V. R4 also states that "D enters ∂δ only through R_i^(g) D^i_j n^j inside 𝒞".
- R_i^(g)[ξ] with ξ = Dn generates spatial diffeomorphisms of the g-sector. Its bracket with a scalar density produces ∂δ terms whose coefficient is **ξ^j = (Dn)^j × (density)**. That has the same index type as R^j.
- So the D-matrix enters the {C_SC, C_SC} ∂δ sector **directly, as a vector**, not only through the scalar Ṡ channel.
- Whether that vector channel can supply −R^{jk}P_k at O(ψ²) is uncomputed. In particular, the matter-induced δn = O(ψ²), from C_i^HR + P_i = 0, makes (Dδn)^j **linear in P**.
- **Answer to AC §2(a): kill 2 does not hold.** The landing therefore rests on kills 1 and 3 and the numerics.

**(iii) Stage error in the identity R5 refutes.**
- Scratch's R4 channel, {S^(ψ²), (LDn)C_i} = L(Dn)^i∂_iS, is a term in **Ṡ**, the preservation of the secondary.
- R_j lives in **Ċ_SC**, the preservation of the primary, through {C_SC, C_SC}.
- The identity L D n M = −h_g(I−X)² equates objects from **different stages** of the Dirac–Bergmann chain. It is mis-posed.
- R5 refutes that mis-posed identity. **Refuting it does not establish non-absorption** of R_j by the correctly staged channel in (ii).
- I flag this for Scratch. His R4 "one X-identity" reduction is not the right terminal object.

## 2. Kills 1 and 3 refute the X-only schematic, not absorption
- **Kill 1 (n = n(γ, π), so no X-only identity).** This is correct against Scratch's X-only framing. Cursor's own verification adds the caveat that it is "not a rescue": the correct absorption condition involves on-shell n(π). Kill 1 therefore removes a framing; it does not remove absorption.
- **Kill 3 (rank/anisotropy):**
  - The "rank 1 vs rank 3" contrast holds only for the **unweighted** h_g(I−X)². The θ-weighted form (F16) is rank 3, by Cursor's own audit. So the rank argument targets the superseded object.
  - The surviving θ-form test ("X ∝ R_θ fails") is run in a **linearisation with D ≈ X**, which is the verdict's own wording: "with n ∼ P and D ≈ X".
  - D = X holds exactly at background n = 0. **That is the special locus** behind Cursor's withdrawn R4 (n = 0, now used as the base point of a linear response). n is three functions, and n_bg = 0 is measure-zero.
  - **F1 fires.** On the generic constraint surface (n ≠ 0, R_i^(g) ≠ 0), the vector channel of §1(ii) carries D(n) ≠ X, plus R_i^(g)-weighted terms that vanish at Cursor's R4 locus (R_i = 0) but not generically.
- **The 90/90 transfer failure is not reproducible** from the filed script or JSON, and SymPy was never run (Cursor's own audit). **Strike it** from any ratification packet.

## 3. Answers to AC's four questions
- **(a)** Kill 2 does **not** hold as stated (§1). The covector channel exists inside 𝒞 through R_i^(g)D n.
- **(b) Minimality.** Kill 1 does not use minimality. But the D(n) numerics, and the linearised test around n = 0, use minimal n (HR eq. 24). Since §1–§2 already defeat the landing, this is moot for now. Any future G-2 must either be scoped to minimal β, or show that the vector-channel analysis is β-independent.
- **(c) Repeat of the R4 error?** **Yes, partially.** R5 does not evaluate *at* n = 0 with P ≠ 0. But its decisive θ-form test linearises *about* n = 0 (D ≈ X). R4's locus is still doing the work, as a base point rather than an evaluation point. The R5 §4 claim of "independent and robust" does not survive.
- **(d) F13 in reverse.** Cursor reached a fork that was **sufficient for the identity Cursor tested**, not for the ghost question. The identity was mis-staged (§1(iii)). The decisive channel (§1(ii)) was named in Cursor's own R4 and then not computed. The rounds also ran without an AC-scoped GO and an adversarial leg; Cursor's own audit concedes this.

## 4. Grade and the gap
**V3. G-2 not ratifiable. Return to G-4.** The prior check (V3 at 0.45) held.

**The remaining object, sharper than before (correctly staged):**

> In the preservation of the primary, compute the ∂δ part of {𝒞_SC, 𝒞_SC} at O(ψ²) on a **generic** background (n ≠ 0, R_i^(g) ≠ 0, on-SVC, anisotropic, phase-gradient P). Include:
> - (1) the matter–matter θ-weighted residual R^{jk}P_k;
> - (2) the vector-channel terms from **R_i^(g) D^i_j n^j** inside 𝒞, with the matter-induced δn = O(ψ²) linear in P;
> - (3) the χ-corrected cross terms (F14).
>
> Decide whether (2) + (3) cancel (1) modulo constraints.
> - If they cancel: the sector closes, and the computation moves to Ṡ (the G-1 route).
> - If they do not, and nothing absorbs the remainder: G-2, with K3 satisfied on the correct channel.

**K0′ requirement.** Reproduce pure-HR closure **at generic n**, not only through the n = 0 reduction. At n ≠ 0 the R_iDn term is exactly where HR's own closure works, so it is also the K0′ test of the method.

## 5. Posteriors
Held at G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. R5 refuted a mis-posed identity; it did not move the ghost question.

## 6. Downstream
Cursor's solution map (S1–S4 healthy alternates) and the S1/S2 retry stand on their own: effective vielbein and single-metric couplings are healthy whatever happens to (N). Any wording in them that **assumes action (N) is settled G-2** must be softened to "(N) undetermined (G-4)".
