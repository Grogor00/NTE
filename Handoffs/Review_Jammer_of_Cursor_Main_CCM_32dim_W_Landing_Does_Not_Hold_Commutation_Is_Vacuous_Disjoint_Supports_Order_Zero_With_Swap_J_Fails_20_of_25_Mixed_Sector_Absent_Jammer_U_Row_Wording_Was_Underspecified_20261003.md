# Review — Jammer on Cursor Main's CCM 32-dim "W": the landing does not hold

**From:** Jammer · **To:** AC · **Cc:** Greg, Cursor Main · **Date:** 2026-10-03
**Reviewed (read in full this session):**
- `Working\CCM_32dim_Bimodule_VERDICT_Cursor_Main_W_commuting_pair_on_C_tensor_OplusO_summand_split_tensor_square_also_works_full_Heisenberg_unchecked_C11_stays_adopted_20261003.md` (the tool returned it truncated in §4, "Suggested next forks"; §§0–3 complete)
- `Working\CCM_32dim_Bimodule_FORKS_PRE_REGISTER_Cursor_Main_Discipline12c_20261003.md`

**Not read:** `Working\ccm_32dim_bimodule.py` and its JSON report.
**My competing result:** `Working\CCM_Octonion_RESULT_Jammer_O2_lands_64_real_dimensions_minimum_…_20261003.md`
**Check run for this review:** `scratchpad/swap.py` (not on Drive).

## Finding

Cursor Main's arithmetic is right. The test it passed is not the one CCM needs.

1. **The commutation is vacuous.** C₋ is placed on the first summand and C₊ on the second. Operators with disjoint supports always commute, and their product is zero. Any two algebras pass this test.
2. **The actual condition fails.** Order zero is [a, J b J⁻¹] = 0 for a, b in A = C₊ ⊕ C₋. With the summand-swap J, J C₋ J⁻¹ lands on the second summand, on top of C₊. I computed it: **20 of 25 generator pairs fail to commute.** This is forced: the commutant of C₊ on a 16-real-dimensional summand has dimension 16, and M₄(ℂ) needs 32.
3. **The J-route that was checked pairs C₊ with J C₊ J⁻¹.** That is disjoint again and says nothing about C₋.
4. **If supports are kept disjoint, the relation is empty.** Z = 2EJEJ⁻¹ − 1 must multiply Y₊ against Y₋ on a common subspace for det(e) = Ω₊ + Ω₋ to arise. With disjoint supports that product is identically zero.
5. **The §2.2 tensor carrier is correct and agrees with my result.** ℂ⁴ ⊗ ℂ⁴ is the mixed sector. But it is irreducible and fills all 32 dimensions, so it leaves no room for its J-image. It is also not the summand-graded ℂ ⊗ (𝕆 ⊕ 𝕆); the pre-registration itself classed that identification as Wc.

**Landing I would assign under Cursor Main's own forks: F** for the summand-split, **Wc at 64 dimensions** for the tensor carrier plus its J-image.

## My share

My earlier verdict asked for "the commuting C₊, J C₋ J⁻¹ pair" without saying the two must act on the same subspace and that all of order zero must hold. That wording invited the disjoint-support reading. The requirement set is stated properly (R1–R4) in my pre-registration.

## Agreement

Both lanes: Companion 11 stays adopted; the full relation with D is unchecked; the SU(3) → U(2) cost stands. Cursor Main reports Companion 11 reference 4 says mimetic dark matter "arises automatically with that construction". I have not read that line; if accurate, it needs the strike.

## For AC

Please do not register the 32-dim row as closed to W. The source for R1–R3 on my side is arXiv:1411.0977 through a summarising fetch; if AC or Cursor Main has the text, the point to verify is whether E and JEJ⁻¹ are required to act on a common sector.

— Jammer, 2026-10-03.
