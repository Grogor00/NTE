# {C_N, C_N}_D through χ — ADVERSARIAL VERDICT (Claude Jammer)

**Lane:** Claude Jammer (adversarial). **Date:** 2026-10-21.

**Pre-registration:** `Working\Opsi2_Steps_1_to_3_ADVERSARIAL_PREREGISTRATION_Claude_Jammer_Greg_GO_20261021_..._Filed_Blind_20261021.md`. It was filed before any lane's step-1/2/3 result existed.

**Stake.** My pre-registration favoured M-b (0.55), and M-b is where both lanes landed. I am attacking the result harder for that reason.

**Read in full this session:**
- `Handoffs\RULING_AC_Scratch_Self_Correction_Accepted_K0prime_Passed_Three_Lanes_G4_Blocker_Is_Dirac_Chi_Channel_20261021.md`
- `Working\Opsi2_CN_Dirac_Chi_VERDICT_CursorMain_Mb_W1_Weight_Sigma_g_Squared_Over_Sigma_Not_Constraint_Weight_20261021.md`
- `Working\Opsi2_CN_Dirac_Chi_PARALLEL_CursorMain.py`
- `Working\Opsi2_CN_Dirac_Chi_CROSSCHECK_VERDICT_Scratch_Converges_Mb_W1_G2_..._20261021.md`
- Literature, read via web extraction: Yamashita–De Felice–Tanaka arXiv:1408.0487; de Rham–Heisenberg–Ribeiro arXiv:1409.3834.

**Not read:**
- Scratch's Step-1 and Step-2 verdicts;
- AC's "BD gate is coefficient of N_g" ruling;
- Cursor's Steps-1–3 verdict and its K0′ files;
- both Scratch directives to Cursor;
- Cursor's CN pre-registration, .wl and .json.

I do **not** rule on K0′. AC's ruling says K0′ was passed by Cursor in two engines; I have not read those files.

No Core. No f. No computation by this lane. Posteriors held.

---

## 1. The numerics are tautological; all the evidential content is one unwritten analytic step

`Opsi2_CN_Dirac_Chi_PARALLEL_CursorMain.py`, `run_numpy`, does the following:
- **sets** a = Σ_g²/Σ and b = Σ;
- draws random 3-vectors R and p;
- reports how far R + a·p is from parallel to R + b·p.

That residual is non-zero whenever a ≠ b, which is whenever Σ_f ≠ 0. That is true by construction. So the "200 backgrounds, median 0.425, fraction 1.0" figures, the K5 swap figure, and the Σ_f = 0 control are **consequences of the input formula, not tests of it.** Scratch's 400-background Wolfram reproduction and his enlarged-span test are the same structural model with one more vector; he says so himself ("structural models of the HR constraint algebra, not the explicit algebra").

**What actually carries the result** is the claim that the χ-corrected diagonal ∂δ coefficient has matter weight **Σ_g²/Σ** on the monomial p_j. Cursor states this as a scaling argument ("E_g ⊃ Σ_g ψ†α∇ψ and C⁻¹ ~ Σ⁻¹"). **Neither verdict body writes out the derivation**: no index structure, no Grassmann ordering, no h_g^{ij} factors.

**Requirement for ratification:** a written derivation of {E_g(x), E_g(y)}_D|_∂δ, with tensor indices and Grassmann signs. The statistics must not appear in any ratification packet as independent evidence. This is the same class of problem as the 90/90 statistic.

## 2. Independent structural check (this lane, analytic, no code): the weight is plausible and the mechanism is transparent

- The second-class pair χ, χ̄ has a bracket matrix proportional to the **total** kinetic weight Σ = Σ_g + Σ_f. So the reduced bracket is {ψ(x), ψ†(y)}_D ∝ δ/Σ.
- Write E_g in the reduced (ψ, ψ†) representation, with no π_ψ. Its derivative-carrying matter part is Σ_g × (a unit bilinear with one spatial derivative).
- Two such densities bracket to (Σ_g·Σ_g/Σ) × (unit current J_j = ψ†∂_jψ-type) on ∂δ. The extra terms from ∂Σ come at δ order, not as p_j.
- The diffeomorphism generator (the matter piece of C_i^tot) must move ψ with unit strength under this bracket, so it carries weight Σ on J_j.
- **The ratio is θ_g² with θ_g = Σ_g/Σ.** Physically, E_g moves only the fraction θ_g of the shared spinor. In the single-frame limit, θ_g = 1 and closure is restored.

This agrees with Cursor's weight. It also ties the result to the θ weights flagged since R3: the fork-deciding mismatch is the θ structure. **It is structural reasoning, not a computation, and it does not substitute for §1's requirement.**

## 3. Attacks on the remaining escape routes

**(a) F19 is asserted, not computed.**
- HR close {C, C} through the **n equation of motion**: Cⁱ = 0 on the n equations, giving P^i = C(Dn)^i (eq. 3.23).
- Cursor projects onto C_i^tot. Scratch projects onto C_i^tot plus a modelled L-shift constraint.
- **Neither projects onto the matter-modified n-EOM constraint Cⁱ**, which is the object HR's closure actually uses.
- Cursor's "the matter-modified multiplier does not set Σ_g = Σ_f" is true but beside the point. The question is the **p weight inside the n-EOM Cⁱ**.
- My structural expectation: the g-shift coupling carries weight Σ_g, giving a mismatch factor θ_g instead of θ_g². That still fails, but it needs to be computed and shown.

**(b) Undischarged item (A), spin connection and Grassmann terms. These cannot rescue W-0 on the p_j monomial.**
- Spin-connection terms in E_g are bilinears with **no** ψ-derivative, of the form ψ†M(∂e)ψ.
- Their Dirac brackets produce ∂δ coefficients that are spin-density bilinears, a different monomial from J_j.
- Cursor's own argument (p_j is an independent monomial) therefore cuts both ways: (A) can add new non-vanishing monomials, but it **cannot** cancel the θ_g² mismatch on J_j.
- So (A) is needed for a complete coefficient, not as a live escape. This is structural; whoever runs (A) should confirm it.

**(c) Undischarged item (B), φ = Σ^{1/2}ψ, is an invariance check, not an escape.**
- Whether {C, C} vanishes weakly is invariant under canonical transformations. The constraint surface and the Dirac bracket transform covariantly.
- φ = Σ^{1/2}ψ with metric-dependent Σ is a point transformation that also shifts the gravitational momenta. Done correctly, it **cannot** change W-0 versus W-1.
- If the densitized recomputation moves the ratio, that **reveals an error**, either in it or in the current calculation. It does not show the landing is normalization-dependent.
- Cursor's caveat ("if the canonical momentum is normalised differently, the ratio changes and this landing moves with it") is therefore wrong as stated. Correct statement: a ratio that moves under a canonical change of variables indicates a mistake.
- Recommendation: run (B) as a consistency control, keeping the gravitational-momentum shift.

**(d) A shift-factorization escape (my pre-registered M-c) has not been closed.**
- de Rham–Heisenberg–Ribeiro (1409.3834) state generally that any matter field with a kinetic term contributes to the Hamiltonian so as to make the **shift dependence non-factorizable**, i.e. HR's shift redefinition fails.
- If that holds for Dirac double coupling, the issue arises at **step 1**, before {C_N, C_N}. Then C_N as constructed is not the HR gate.
- The physics outcome (a ghost) would be the same, but the mechanism, and therefore the publishable statement, would differ.
- Step 1 must show explicitly that the matter shift couplings (the g- and f-frame momentum densities, with weights Σ_g, Σ_f) factorize under the HR redefinition. I have not read Scratch's Step-1 verdict, so this is a requirement, not a finding against it.

## 4. Prior art: the headline is not novel, so the novelty ledger must change

- **Yamashita, De Felice, Tanaka, arXiv:1408.0487, "Appearance of Boulware-Deser ghost in bigravity with doubly coupled matter".**
  - Claim (extracted quote): "the Boulware-Deser ghost generally revives in the presence of doubly coupled matter."
  - Matter: a k-essence scalar with kinetic terms in both metrics.
  - Mechanism: the matter momentum makes the Lagrangian **non-linear in the lapses**, so "we will not have the constraint that corresponds to C." Ghost-free only if the second coupling is potential-only.
  - Per the extraction, in their setting {C, C} = 0 still holds. The failure is that C does not exist.
- **de Rham, Heisenberg, Ribeiro, arXiv:1409.3834.** The same matter coupled to two metrics with kinetic terms in both "leads to a BD ghost at an unacceptably low scale." No fermion analysis.
- **Searches for fermion-specific prior art.**
  - Search strings: "fermions Dirac spinor coupled to both vierbeins bimetric gravity ghost Hamiltonian analysis" (standard); "doubly coupled fermions bigravity Boulware-Deser ghost spinor two vielbeins first-order kinetic term lapse linear" (extended).
  - These found no paper treating a Dirac field doubly coupled through two vierbein kinetic terms.
  - Results not opened: 1409.1909, 1409.2860, 1410.6164.
  - **Not exhaustive.**

**Consequence for the ledger.** "Doubly coupled matter revives the BD ghost" is **established prior art (2014)** and cannot be NTE's novel claim.

What may be novel is narrower:
- Dirac double coupling **evades** the YdFT mechanism. The kinetic term is first order, so the theory stays lapse-linear and C exists; that is Claim 2, itself Nelson–Teitelboim-type.
- But the ghost still returns through a **different** mechanism: the χ Dirac bracket gives the gate's self-bracket the θ_g² weight. This is HR case 1, with 5.5 modes.
- That is a mechanism-level result. It stands only if §3(d) is closed. If the shift fails to factorize, the fermion case reduces to the dRHR mechanism and the novelty shrinks further.

The ledger must carry YdFT 2014 and dRHR 2014 alongside Nelson–Teitelboim 1977.

## 5. Landing

| | |
|---|---|
| **M-b / W-1 (G-2, 5.5-mode)** | **Strong indication, structurally robust (§2, §3b, §3c). Not ratifiable yet.** |
| Blocking items | (1) the written two-leg derivation (§1); (2) projection onto the matter-modified n-EOM Cⁱ (§3a); (3) the step-1 shift-factorization check against dRHR (§3d); (4) (A) and (B) as completion and invariance controls (§3b, §3c) |
| Novelty | Narrowed to the mechanism. YdFT 2014 and dRHR 2014 are prior art for the headline (§4). |

My assessment is that W-1 is likely to survive (1)–(4). This lane's prediction, not a posterior, is about 0.75 that W-1 survives.

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. The two-lane result is structural; a posterior move should follow item (1), the written derivation, and should be AC's call.

— Claude Jammer, 2026-10-21.
