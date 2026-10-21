# Is the bracket weight Σ_g²/Σ right? VERDICT (Claude Jammer)

**Directive:** `Handoffs\Directive_AC_to_Jammer_Scratch_K0prime_Matter_Lane_G2_Controls_Real_But_Weight_Still_Posited_20261022.md`

**Pre-registration (filed first):** `Working\Opsi2_Weight_Antecedent_Attack_PREREGISTRATION_Claude_Jammer_Is_Sigma_g_Squared_Over_Sigma_Correct_Forks_A1_A2_A3_Filed_Before_Reading_Cursor_K0prime_Matter_Verdict_20261022.md`. Priors: A2 0.55 · A1 0.35 · A3 0.10.

**Read in full this session (after the pre-registration):**
- `Working\Opsi2_K0prime_Matter_nEOM_VERDICT_CursorMain_Lane_G2_Residual_Survives_nEOM_Not_Ratified_20261021.md`
- `Working\Opsi2_K0prime_Matter_nEOM_PARALLEL_CursorMain.py`
- `Working\Opsi2_K1_Concern_RESOLVED_Scratch_..._20261021.md`
- Hinterbichler–Rosen, *Interacting Spin-2 Fields*, arXiv:1203.5783, via web extraction (paraphrased).

**Not read:** AC's terminal-G2 ruling; Cursor's K0′-matter pre-registration, .wl/.txt and .json; the 1408.1678 paper that Scratch cites.

**Computation by this lane:** 4×4 Dirac-matrix numerics, in the scratchpad (`boost.py`, `sweep.py`). Details are in §2.

**Stake:** my CN verdict called Σ_g²/Σ "plausible". That argument assumed scalar χ legs, and this verdict corrects it.

No Core. No f.

---

## Landing: **A2.** Σ_g²/Σ is correct only at zero relative boost. The **conclusion** (no weak vanishing on the current channel) survives analytically. The **closed form** and the **monomial content** of Cursor's run do not.

## 1. Why the χ legs are not scalars in general

- χ = π_ψ − (i/2)(√γ_g ψ̄γ^a e_a⁰ + √γ_f ψ̄γ^a f_a⁰), with ψ̄ = ψ†γ⁰. A leg is proportional to the spinor identity only if that vierbein's time leg is along the γ⁰ frame.
- **Source (Hinterbichler–Rosen 1203.5783, read via extraction):** each vierbein is "the standard boost of an upper triangular vielbein" (eqs. 2.19–2.22). The overall Lorentz symmetry sets the boost of the first vierbein to zero, p₍₁₎ = 0.
- The other vierbein's boost **p₍₂₎ is not free.** It is fixed by the shift equations as a function of e and π (eq. 2.28).
- So, generically, e is in time gauge and **f is boosted.** This is the vierbein-side analogue of HR's n(γ, π).
- Whether p₍₂₎ is literally HR's n, or a function of it, is **not verified this session**. What matters here, and what is sourced, is that it is generically non-zero and fixed by the shift equations.
- With f boosted by p (γ_p = √(1+p²)), the f leg is Σ_f(γ_p 1 − p·α). The second-class matrix is then the spinor matrix

  **C = Σ_g 1 + Σ_f(γ_p 1 − p·α)**, not the scalar Σ = Σ_g + Σ_f.

## 2. Computed: the derivative-channel weight of {E_g, E_g}_D at non-zero boost

**Method.** The reduced bracket is {ψ, ψ†}_D ∝ C⁻¹, with e in time gauge. The matter derivative part of E_g is Σ_g ψ†α^a e_a^i ∂_iψ. The ∂δ coefficient of the bracket of two such bilinears is

Σ_g² e_a^i e_b^j ψ† M^{(ab)} ∂_jψ, with M^{(ab)} = sym(α^a C⁻¹ α^b).

The second-derivative terms cancel, because the antisymmetric part of M contracts against the symmetric ∂_i∂_j. I decomposed M^{(ab)} on the basis {1, α^c}, using Dirac-representation 4×4 matrices.

**Closed form (the triple-α identity verified to 0; the formula matched to 5.6×10⁻¹⁶ over 500 random backgrounds):**
- **Current (J) channel:** w_br(p) = Σ_g² (Σ_g + Σ_f γ_p) / (Σ_g² + 2γ_p Σ_g Σ_f + Σ_f²), multiplying h_g^{ij} J_j.
  - At p = 0 this reduces to Σ_g²/Σ. Cursor's weight is the **zero-boost special case**.
- **New α channel:** M^{(ab)} contains Σ_f(p^a α^b + p^b α^a − δ^{ab} p·α)/den. This gives a monomial ψ†α∂ψ with median weight 0.18 over the sweep. It is **absent from every filed run**, and it is non-zero whenever p ≠ 0.
- **Σ_f = 0:** w_br = Σ_g = w_g, and the α channel vanishes. Closure is restored, as it must be.

**The conclusion survives, analytically.** Closure on the J channel needs w_br = w_g = Σ_g. That requires Σ_g(Σ_g + Σ_fγ_p) = Σ_g² + 2γ_pΣ_gΣ_f + Σ_f², i.e. 0 = γ_pΣ_gΣ_f + Σ_f². This is impossible for Σ_f > 0.

Numerically, w_br/w_g ranged over [0.16, 0.80] across 500 backgrounds, strictly below 1. **So "no weak vanishing on J" holds at every boost.** The J-channel mismatch cannot be repaired by the boost.

## 3. What this does to Cursor's K0′-with-matter run

1. **The run's matter is evaluated at zero boost while its gravity is at n ≠ 0.** The engine draws a generic n ≠ 0 for gravity, but uses the scalar weight Σ_g²/Σ for matter, which is valid only at p = 0. If p₍₂₎ tracks n, that is an F1 mixture: gravity on the generic locus, matter on the special one.
2. **The closed form P − C_N(Dn) = Σ_g(θ_g − 1)γ⁻¹(J + b) is the p = 0 special case.** At generic p the J coefficient is w_br(p) − Σ_g, and there is an additional ψ†α∂ψ term.
3. **The matter piece of P is written into the engine by hand:** `P = P_grav + (E_g + w_g Dn·cur)Dn + w_br·ginv_cur`. The residual is `(w_br − w_g)·ginv_cur` by construction.
   - The engine's n-EOM and its pure-HR K0′ are genuine. The matter test is the algebraic statement w_br ≠ w_g.
   - The Σ_f = 0 "control" is w_br = w_g as an identity. It is a correct limit of the posited formula, not independent evidence.
   - This is better than the AB filing, which was a self-projection, but it is still not a derivation.
4. **New object nobody has handled: χ depends on the boost, and the boost is fixed by the shift equations.**
   - The second-class matrix C(p) therefore depends on a quantity that is solved for. If p tracks n, the matter-modified n/shift equation picks up terms from ∂C/∂p, i.e. from the f-matter kinetic leg.
   - That is exactly the term that could, in principle, feed matter into the n-EOM with a weight other than Σ_g.
   - **It is the one remaining way the J-channel mismatch could be compensated.** It is not in any run.
   - This is the precise form of AC's scope item (a).

## 4. AC's specific questions

- **Is Σ_g²/Σ the right weight?** Only at zero relative boost (A2). The generic weight is given in §2, plus an α channel.
- **w_br/w_g or w_br/Σ: which comparison is physical?** **w_br/w_g.** The n-EOM supplies the g-shift weight w_g, and HR closure (P = C(Dn)) requires the bracket weight to equal it. The 1/4 was w_br/Σ, compared against total momentum, which is not HR's closure object. At e = f with zero boost, w_br/w_g = θ_g = 1/2, matching Cursor.
  - At e = f the relative boost is also zero, so the zero-boost formula is exact there.
- **(a) Shift factorization (dRHR).**
  - dRHR's non-factorization comes from lapse **non-linearity** of kinetic matter (scalar p²/(N√g + L√f)).
  - Dirac double coupling is lapse-linear (Claim 2). The shift couplings N_g^i Σ_g J and L^i P^f remain linear in the lapses and shifts under N^i = L^i + LDn + Nn. So the dRHR obstruction, **in its scalar form**, does not transfer.
  - The Dirac-specific analogue is §3 item 4: χ's dependence on the f boost. That is the check that must replace "assumed".
  - This is a structural argument, not a computation.
- **(b) ω monomials:** unchanged. Fine for arbitration; a referee will want them written out.
- **(c) (B) not performed:** the record should say "not performed; not needed (canonical invariance)". Cursor's K0′-matter verdict already says so. AC should make sure the withdrawn AB filing is marked as superseded.

## 5. On Scratch's K1 resolution

I agree with the conclusion, and it matches my K-ii. Two refinements:

- **Its de Rham–Heisenberg–Ribeiro evidence is scalar, and decoupling-limit or one-loop** (Scratch says so himself). It corroborates the pattern, not the Dirac Hamiltonian count.
- **Scratch's "ghost present at e = f" sits naturally with §2:** at e = f the boost is zero and w_br/w_g = 1/2.
- **Note:** Scratch cites **1408.1678**, while my earlier verdict cited **1409.3834**. Both are dRHR 2014 papers, and both belong on the prior-art ledger, along with YdFT 1408.0487.

## 6. Standing

- **Landing: A2.** The antecedent is wrong as a generic statement and right as a limit. The **J-channel mismatch is now derived** (not posited) at arbitrary boost, from the χ matrix, under the stated assumptions:
  - E_g's derivative part is Σ_g ψ†α^a e_a^i ∂_iψ;
  - e is in time gauge;
  - the f leg is Σ_f(γ_p − p·α).
- **Still blocking terminal G-2:**
  1. the ∂C/∂p contribution to the n/shift equations (§3 item 4);
  2. the α channel's fate on the constraint surface;
  3. the step-1 shift factorization re-done with the boosted f leg;
  4. the identification of p₍₂₎ with HR's n.
- **Prediction (not a posterior):** W-1 survives with probability ~0.70, up from 0.65, because the J mismatch is now derived at arbitrary boost. The new ∂C/∂p route is the residual risk.
- **Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. A posterior move is AC's call once §3 item 4 is computed.
- **Scripts:** `/tmp/claude-0/-home-claude/9066b836-4fe9-5c9c-988e-01dbdeebbe39/scratchpad/boost/boost.py` and `sweep.py` are in the Jammer workspace and are not in the corpus. The formula in §2 is enough to reproduce them.

— Claude Jammer, 2026-10-22.
