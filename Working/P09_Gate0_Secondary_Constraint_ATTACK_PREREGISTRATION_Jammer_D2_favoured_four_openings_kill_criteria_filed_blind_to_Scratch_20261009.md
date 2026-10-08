# P09 Gate-0 — Secondary Constraint ATTACK PRE-REGISTRATION

**From:** Claude Jammer (adversarial lane)
**To:** AC, Cursor Main, Scratch, Greg, PC
**Date:** 2026-10-09
**Status:** PRE-REGISTERED BLIND — filed before seeing Scratch's secondary-constraint verdict
**Authority:** Greg GO 2026-10-09; Directive `Directive_Cursor_Main_to_Scratch_Jammer_Gate0_Secondary_Constraint_Algebra_GO_Original_Work_D1_vs_D2_20261009.md`
**Conflict declared:** I proposed the lapse-linearity opening (my conformal-literature handoff, 2026-10-08). I am now required to ATTACK the secondary-constraint claim. I do not build a rescue.

**Read set this session:**
- `Working/P09_Gate0_O1_ADM_ROUND_…UNDETERMINED_20261008.md` (Scratch's lapse-linearity analysis, my openings 1–3)
- `Handoffs/Directive_Cursor_Main_to_Scratch_Jammer_Gate0_Secondary_Constraint_Algebra_GO_…_20261009.md`
- `Handoffs/Handoff_Claude_Jammer_to_AC_…_Attack_On_Conformal_Literature_Verdict_…_20261008.md` (my honesty standard)
- arXiv:1111.2070, Hassan–Rosen — secondary constraint proof in massive/bimetric gravity (fetched, full text)
- arXiv:1203.5783, Hinterbichler–Rosen — vierbein multi-gravity, relative Lorentz, symmetric vierbein condition (fetched, full text)
- arXiv:1408.0487, Yamashita–De Felice–Tanaka — BD ghost appearance for doubly-coupled matter (fetched, full text)

---

## 0. PRIOR ON D1 vs D2 — stated before computation

**D2 favoured (ghost returns), credence ~65–70%.**

Reasoning:
1. Every known example of doubly-coupled matter that enters the kinetic sector of both metrics reintroduces the BD ghost (1408.0487, §III). The one proven exception is matter whose coupling to the second metric is purely through the potential (no kinetic coupling), i.e., P̃ = P̃(φ) only (1408.0487, §IV). A Dirac spinor kinetically coupled to both tetrads is NOT in this exception class — it has a kinetic term on each tetrad.
2. Lapse-linearity (the primary constraint) survived for the spinor because the first-order kinetic structure cancels the lapse. This is genuine. But the secondary constraint is a SEPARATE algebraic question that lives in the Poisson-bracket / relative-Lorentz sector, and lapse-linearity does not address it.
3. The relative local Lorentz symmetry, which is broken to the diagonal by the bimetric mass term, plays a central structural role in the HR proof. A spinor explicitly transforms under the Lorentz group (unlike a scalar, which is a Lorentz scalar). Coupling a single spinor to two tetrads forces it into the diagonal representation, promoting the relative boost from gauge to physical — exactly the sector where the BD mode hides.
4. My own prior from the conformal-literature attack (2026-10-08) already pointed toward D2; I identified three openings and stated that the lapse-linearity result "removes one obstruction; it does not prove ghost-freedom."

I would welcome D1 if Scratch can close every opening below. But I do not expect it.

---

## 1. ATTACK ON OPENING 1 — Dirac symplectic current enters the shift-redefinition sector

### The opening (restated)
The Dirac symplectic current π_ψ ∝ (√γ_g A_g + √γ_f A_f)ψ† depends on the relative boost between the two tetrads. The relative boost parameters live in the HR shift-like variables n^i (the n^i are defined by the relation N^i − L^i = (Lδ^i_j + N D^i_j)n^j, eq. (7) of 1111.2070). In the pure bimetric gravity proof, the constraint C_i(γ, π, n) = 0 (eq. (21) of 1111.2070) is independent of both lapses N and L, and crucially satisfies ∂C/∂n^k = C_i · ∂(D^i_j n^j)/∂n^k — so that when C_i = 0, the variation ∂C/∂n^i vanishes identically. This is the key identity that makes the Poisson bracket {C(x), C(y)} computable at fixed n^i (eq. (29) of 1111.2070).

### The attack
With a doubly-coupled Dirac field, the constraint C acquires a spinor contribution C_m (analogous to eq. (IV.5) of 1408.0487 for scalars). But unlike a scalar's C_m, the spinor's C_m depends on the relative boost Λ_rel between the two tetrads, because the spinor's coupling to each tetrad involves the normal projector A_{(I)} = e_{(I)a}^0, and the relative angle between these two normals is Λ_rel.

The n^i equation of motion will now include spinor-dependent terms. The question is whether the identity ∂C/∂n^k ∝ C_i still holds after the spinor is included. If it does NOT — if ∂C/∂n^k has a residual piece that does not vanish when C_i = 0 — then the Poisson bracket {C(x), C(y)} can no longer be evaluated at fixed n^i, and the elegant cancellation of eq. (46) in 1111.2070 fails.

**Kill criterion 1a:** For D1 to hold, Scratch must show that the spinor contribution to ∂C/∂n^k is proportional to C_i (or vanishes) when C_i = 0, after including the spinor's dependence on the relative boost encoded in n^i. A claim that "it probably works the same way" is not sufficient — the algebraic identity must be verified for the spinor case.

**Kill criterion 1b:** Alternatively, if Scratch works in the vierbein formulation (1203.5783), they must show that the spatial rotation constraints P_{(I)ab} from the vierbein formalism still close in the same way after the spinor is added — specifically, that the "other" (non-diagonal) rotation generators still lead to secondary constraints and do not generate new propagating modes.

---

## 2. ATTACK ON OPENING 2 (DECISIVE) — Relative local Lorentz broken to diagonal; relative boost becomes physical

### The opening (restated)
In bimetric gravity without matter, each metric has its own local Lorentz invariance SO(1,3). The mass term breaks this to the diagonal subgroup (Hinterbichler–Rosen, §2: "The mass term breaks this down to the diagonal subgroup of diffeomorphisms and LLI's, those transformations which act the same way on both metrics together"). The relative Lorentz transformation Λ_rel = Λ_{(1)} Λ_{(2)}^{-1} is gauge — the symmetric vierbein condition E_{(1)}^{-1}E_{(2)} η = η (E_{(1)}^{-1}E_{(2)})^T fixes it (1203.5783 eq. (3.14)ff).

A Dirac spinor transforms under the spinor representation of SO(1,3). If it couples to BOTH tetrads, it must be assigned to the diagonal spinor representation (since the mass term only preserves the diagonal Lorentz). This means:
- Under the diagonal Lorentz Λ_diag: ψ → S(Λ_diag)ψ — standard spinor transformation.
- Under the relative Lorentz Λ_rel: the spinor does NOT transform (it lives in the diagonal representation).

But the relative boost Λ_rel ACTS on the individual tetrads separately, and hence changes the coupling e_{(1)a}^μ ψ̄γ^a ∂_μ ψ relative to e_{(2)a}^μ ψ̄γ^a ∂_μ ψ. The spinor action is therefore NOT invariant under relative Lorentz transformations — the relative boost is promoted from gauge to PHYSICAL.

### The attack

This is where the BD ghost can hide. In the pure gravity sector, the symmetric vierbein condition (SVC) removes the D(D-1)/2 = 6 relative Lorentz parameters from the physical phase space. The SVC arises as an equation of motion / constraint from the bimetric action. In the vierbein Hamiltonian analysis of 1203.5783 (§2.2), the "other" combinations of Lorentz generators (not the overall diagonal sum) give rise to secondary constraints that remove these 6 relative Lorentz dof.

With a doubly-coupled spinor:
1. The spinor explicitly depends on both tetrads through its kinetic terms.
2. The relative-boost parameters are no longer gauge — the spinor sees them physically.
3. The constraint algebra for the relative Lorentz generators is MODIFIED by the spinor's contribution. The Poisson bracket of the relative rotation constraint P_{(1)ab} − P_{(2)ab} with the Hamiltonian will pick up spinor-dependent terms. If these terms prevent the secondary constraint from generating, the relative boost degrees of freedom propagate — and one of them is the BD ghost.

**Concrete mechanism (the D2 scenario):**
In the counting of 1203.5783 §2.2: with N metrics, the phase space is N × 2d² (from spatial vielbeins and their momenta). The overall diagonal Lorentz generates first-class constraints removing 2 × d(d−1)/2 dof. The other (N−1) combinations of Lorentz generators should give secondary constraints removing 2 × (N−1)d(d−1)/2 dof. For N=2, d=3: removes 2 × 3 = 6 from secondary constraints. If the spinor spoils even one of these secondary constraints, a BD-like mode propagates.

The reason this is DECISIVE: lapse-linearity is about the N_I lapse sector (the constraint C). Opening 2 is about the Lorentz-generator sector (the constraint P_{ab}). These are DIFFERENT parts of the constraint algebra. Scratch's B.3 (lapse-linearity) says nothing about the Lorentz sector. D1 requires BOTH sectors to close.

**Kill criterion 2a:** For D1, Scratch must show that the (N−1) = 1 relative Lorentz secondary constraints survive in the vierbein formulation after the spinor is added. Specifically: compute {P_{(1)ab} − P_{(2)ab}, H_total} and show it generates a secondary constraint rather than determining a Lagrange multiplier.

**Kill criterion 2b:** Alternatively, in the metric formulation: show that the symmetric vierbein condition is still enforced as an equation of motion when the spinor is present — i.e., that the relative boost is still gauge-fixed.

**Kill criterion 2c:** If Scratch claims the relative boost "doesn't matter because the spinor is a small perturbation" — KILL. The constraint algebra must close non-perturbatively. The proof in 1111.2070 and 1203.5783 is non-perturbative, and the ghost is a non-perturbative statement about the number of propagating dof.

---

## 3. ATTACK ON OPENING 3 — Lapse coefficients depend on both spatial metrics

### The opening (restated)
In the doubly-coupled Dirac Hamiltonian H = N_g H_⊥^(g) + N_f H_⊥^(f) + shifts, each H_⊥^(I) depends on BOTH spatial metrics γ_g and γ_f (because the spinor couples to both).

### Attack assessment
Scratch already ruled this non-fatal in their D4 filing (B.4, Opening 3): "This does not by itself reintroduce the ghost — the BD-removing primary constraint comes from lapse-linearity (∂H/∂N = constraint), which survives even when the constraint involves both spatial metrics."

**I concur that Opening 3 is non-fatal on its own.** Lapse-linearity is about ∂H/∂N being a constraint; the constraint can certainly involve both metrics and still function as a constraint. The cross-metric dependence only becomes dangerous if it spoils the SECONDARY constraint algebra — which is Opening 1's territory, not Opening 3's.

**Opening 3 is absorbed into Openings 1 and 2.** I do not attack it independently.

---

## 4. FOURTH OPENING (NEW) — Dirac second-class constraints modify the gravitational Dirac bracket

### The opening
This is not named in Scratch's B.4 or in the directive, and I name it now.

In single-tetrad GR, the Dirac field's canonical momentum is π_ψ = i√γ ψ†, which is a PRIMARY second-class constraint (it determines π_ψ in terms of ψ, not in terms of time derivatives of ψ). The standard procedure is to pass to the Dirac bracket, which modifies all Poisson brackets in the theory to account for these second-class constraints.

With two tetrads, the primary constraint becomes:

π_ψ ∝ (√γ_g A_g + √γ_f A_f) ψ†

where A_g, A_f are the normal projectors from each tetrad. This constraint:
1. Depends on BOTH spatial metrics γ_g, γ_f.
2. Depends on the RELATIVE BOOST between the two tetrads (through A_g and A_f, which are the 0-components of each tetrad, and their relative angle is the relative boost).

When passing to the Dirac bracket, the inverse of the matrix C_{αβ} = {χ_α, χ_β} (where χ_α are the second-class constraints) multiplies every subsequent Poisson bracket. Since the second-class constraint matrix C_{αβ} now depends on the relative boost, the Dirac brackets between the gravitational constraints C, C^L, C^L_i will receive ADDITIONAL contributions proportional to C_{αβ}^{-1}. These additional contributions are absent in the pure gravity case and absent in the single-tetrad fermion case.

### The attack
The question: do these Dirac-bracket modifications spoil the closure {C, C} ≈ 0?

In the single-tetrad case, the modifications are harmless because C_{αβ} depends on only ONE metric, and the standard proof (which uses R^0, R_i satisfying the same algebra with or without matter, as shown in 1408.0487 §IV) goes through by replacing R^0 → R^0' = R^0 − M_g^{-2} C_m.

But with TWO tetrads, C_{αβ} depends on both metrics AND the relative boost. The replacement trick R^0 → R^0' may fail because:
- R^0 and R^0' satisfy the standard diffeomorphism algebra only if the matter contribution C_m and the momentum contribution π_ψ ∂_i ψ transform correctly under spatial diffeomorphisms.
- With the spinor's second-class constraint depending on the relative boost, the Dirac bracket introduces corrections that are NOT simply absorbable into R^0'.

**Kill criterion 4a:** For D1, Scratch must explicitly address the second-class constraint structure of the doubly-coupled Dirac field and show that the Dirac bracket does not spoil the closure of the gravitational constraint algebra.

**Kill criterion 4b:** If Scratch works only with Poisson brackets (ignoring the Dirac field's second-class constraints), they must justify why the second-class constraints can be ignored for the purpose of determining whether the BD ghost appears. In the standard treatment, the second-class constraints reduce the fermionic phase space — but they also modify ALL brackets, including gravitational ones.

---

## 5. KILL CRITERIA SUMMARY — necessary conditions for a D1 (ghost-free) claim

A D1 verdict requires ALL of the following:

| # | Criterion | Status |
|---|---|---|
| K1 | {C(x), C(y)} ≈ 0 with the spinor contribution to C, including dependence on relative boost via n^i. The identity ∂C/∂n^k ∝ C_i must be verified for the spinor case. | OPEN |
| K2 | The (N−1) = 1 relative Lorentz secondary constraint must survive in the vierbein formulation, or equivalently the symmetric vierbein condition must remain enforced, with the spinor present. The relative boost must NOT become a propagating dof. | OPEN — this is the decisive test |
| K3 | The Dirac-bracket modifications from the spinor's second-class constraints must not spoil the closure of the gravitational constraint algebra. | OPEN |
| K4 | Any D1 claim must be non-perturbative (not valid only on a specific background or in a linearized limit). The 1408.0487 counterexample shows that FLRW-safe does not imply Bianchi-safe (§III.1.2). | Standing requirement |
| K5 | The analysis must account for the spinor mass term e(g)·mψ̄ψ + e(f)·mψ̄ψ if the deposited reading includes it. Even if massless, the mass term is the relevant case for the neutrino. | Standing requirement |

Failure of ANY ONE of K1–K5 → D2 (ghost returns).

---

## 6. EXPLICIT: EVEN D1 DOES NOT RESTORE SYMMETRIC ν

Stated for the record, regardless of the secondary-constraint outcome:

1. **N_eff ≈ 1.52 — excluded at ~10σ.** The symmetric doubly-coupled Z₂-even neutrino is excluded by the thermal count, parameter-free, against ACT 2.86 ± 0.13. This is independent of the ghost question. (Scratch Task A, confirmed; Jammer's count, confirmed.)
2. **No κ.** The broad amplifier κ = 5.50 is withdrawn; κ₀ is retained but earns no number. Nothing in this round restores κ.
3. **No f.** The energy-splitting fraction f is fixed at 1/2 by CPN symmetry; there is no tunable parameter.
4. **D1 would be a FOUNDATION result only** — confirming that two-orientation gravity with a doubly-coupled spinor is consistent in principle. It does NOT make the symmetric neutrino deposit-viable. A different (non-thermally-symmetric, non-DM) realization would be needed before N_eff could be revisited, which is Gate-2/P03 territory, not authorized here.
5. **Deposit position unchanged:** P04 / adopted ΛCDM / cosmological sector open.

---

## 7. HONESTY CHECK (against my 2026-10-08 standard)

In my conformal-literature attack, I stated: "An attack on a result that agrees with the attacker is only worth anything if it looks for where the agreement is unearned." Here my prior favours D2, and I am attacking a claim (the secondary constraint) that, if it fails, gives D2 — which I expect. So the honest question is: am I being fair to D1?

I believe so, because:
- I have given explicit kill criteria for D1. They are not impossible to meet — they are the standard requirements of the HR proof adapted to the spinor case. If Scratch can show the algebraic identities hold with the spinor included, D1 stands.
- I have identified Opening 3 as non-fatal, agreeing with Scratch against my own interest in finding attack surfaces.
- My Fourth Opening (the Dirac-bracket modification) is a genuine new concern, not a recycled version of Openings 1 or 2.
- I have stated that even D1 does not help the deposit, which removes any temptation to shade D2 for strategic reasons.

What would move me to D1: an explicit computation showing {C, C} ≈ 0 with the spinor, OR a clear argument that the spinor's relative-boost dependence is gauge-equivalent to the pure-gravity case (e.g., by a field redefinition that absorbs Λ_rel into the spinor without changing the constraint algebra). I have not found such an argument. Scratch may.

---

## 8. STANDING — armed and waiting

Scratch's secondary-constraint verdict has NOT been filed as of this pre-registration.

I will attack Scratch's verdict when it appears (look for `Handoffs/Handoff_Scratch_to_AC_*Secondary*` or `Working/P09_Gate0_Secondary_Constraint_VERDICT_Scratch*`). Attack to be filed at:

`Handoffs/Handoff_Claude_Jammer_to_AC_Scratch_CursorMain_Gate0_Secondary_Constraint_Attack_…_20261009.md`

Until then, this pre-registration stands as my declared attack surface. No algebra is invented for Scratch. The four openings and five kill criteria are armed.

---

**Sources (fetched this session):**
- [arXiv:1111.2070](https://arxiv.org/abs/1111.2070) — Hassan & Rosen, "Confirmation of the Secondary Constraint and Absence of Ghost in Massive Gravity and Bimetric Gravity"
- [arXiv:1203.5783](https://arxiv.org/abs/1203.5783) — Hinterbichler & Rosen, "Interacting Spin-2 Fields" (vierbein formulation, relative Lorentz, symmetric vierbein condition)
- [arXiv:1408.0487](https://arxiv.org/abs/1408.0487) — Yamashita, De Felice & Tanaka, "Appearance of Boulware-Deser ghost in bigravity with doubly coupled matter"

— Claude Jammer, 2026-10-09. Pre-registered blind to Scratch.

---

# POST-VERDICT ADDENDUM (2026-10-09, after Scratch's D4 filing)

**Scratch filed:** D4 (undetermined), structural lean D2 (~60–65%).
**Attack filed:** `Handoffs/Handoff_Claude_Jammer_to_AC_Scratch_CursorMain_Gate0_Secondary_Constraint_Attack_on_Scratch_D4_lean_D2_…_20261009.md`

## Pre-registration accuracy

| Item | Pre-registered | Scratch's finding | Accurate? |
|---|---|---|---|
| Prior (D2, ~65–70%) | ✓ | Scratch also leans D2 (~60–65%) | CONVERGENT — difference is ~5–10% credence |
| Opening 1 (shift sector) | Primary obstruction | Confirmed — non-polynomial S-dependence = K1 failure in different language | ✓ |
| Opening 2 (relative Lorentz) | Decisive | PARTIALLY RESOLVED — relative boost is auxiliary (genuine positive) but feeds into Opening 1 | PRE-REG OVERWEIGHTED this as standalone; Scratch correctly showed it's a relay |
| Opening 3 (non-fatal) | Non-fatal | Non-fatal | ✓ |
| Opening 4 (Dirac bracket) | New, genuine threat | Flagged by Scratch, not computed, listed as part of Lemma S1 | ✓ — correctly anticipated |
| K1 (∂C/∂n^k identity) | Must be verified | Effectively failed via Result 2 | ✓ |
| K2 (Lorentz secondary) | Must survive | K2b satisfied (SVC enforced); K2a still open | PARTIALLY MET |
| K3 (Dirac bracket) | Must not spoil | Uncomputed, open | UNMET as predicted |
| K4 (non-perturbative) | Standing requirement | Unmet | UNMET as expected |
| K5 (mass term) | Must account for | Mass term safe (polynomial); kinetic term unsafe | PARTIALLY MET |

## Updated credence: D2 at ~70–75%

The structural argument (non-polynomial S-dependence breaking the HR cancellation class) is stronger than Scratch's 60–65% gives it. The proposed D1 escape routes (Clifford miracles, Dirac-bracket cancellations) are structurally unfounded. I converge on D4 as the honest landing; I diverge by 10% on the D2 lean.

## Kill criteria summary: 0/5 fully met → D1 NOT established
