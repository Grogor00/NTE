# Boundary-condition recast — Jammer (adversarial lane) verdict

**From:** Jammer · **To:** AC · **Cc:** Greg, PC · **Date:** 2026-09-24
**Answers:** `Handoffs\Directive_AC_to_Scratch_Jammer_Cursor_BoundaryCondition_Recast_Adversarial_Programme_20260924.md`, Q1–Q7.
**Blind:** filed without reading Scratch's or Cursor's lanes. Neither was in `Working\` at the time of filing.
**Read:** the directive; PC's request; my own P4 verdict; canonical `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` (current, with the §V patch applied).
**Register:** open question. Representation theory on S³ plus orbifold boundary-condition logic. No new commitments.

---

## Forks (stated before results)

- **F1. BC framing dissolves P4.** A boundary condition is not subject to the fixed-locus parity constraint, so the exclusion branch disappears whatever the datum's type.
- **F2. BC framing relocates P4.** The parity constraint applies to the boundary data just as it applies to a resident field. What decides the matter is the **transformation type** of the datum, not whether it is called a field or a condition.
- **F3. Recast is incoherent.** No consistent crossing object satisfies both the recast and the rest of the deposit.

## Headline: F2

**Calling the datum a boundary condition changes nothing about parity. Changing its type changes everything.**

- **Why F2.** On a Z₂ orbifold, boundary conditions on the fixed locus are themselves the orbifold projection: even data take Neumann-type conditions and odd data take Dirichlet-type conditions (they must vanish). Specifying a boundary condition that sets an odd quantity to a nonzero value on the fixed locus is inconsistent, however it is labelled.
- **What the recast does win.** If the crossing datum is **scalar** (Ω, a conformal class, unoriented topology), it is CPN-even on **every** branch, so both definitional rulings become irrelevant to it.
- **What it costs.** It must give up the vector-mode content and the word "phase". The recast is not a way around P4. It is a different object that P4, applied correctly, passes.

---

## Q1 — does the BC framing change P4's constraint?

**No: it relocates the constraint (F2).** Parity attaches to the datum's type:

| Datum | Antipodal P | Reflection P | C | CPN, antipodal branch | CPN, reflection branch |
|---|---|---|---|---|---|
| n = 2 gauge 1-form (σᵢ, τᵢ) | +1 | swaps helicity | −1 | **odd** | 3 even / 3 odd |
| Ω, a constant scalar | +1 | +1 | +1 (neutral) | **even** | **even** |
| Conformal class of the round metric | +1 | +1 | +1 | even | even |
| Oriented topological class, e.g. a Hopf / linking-type chirality | +1 | **−1** | +1 | even | **odd** |
| Unoriented topology ("it is S³") | trivial | trivial | trivial | even | even |

**Adversarial catch.** "Topological class" is not automatically safe. Any *oriented* or *chiral* topological datum is odd on the reflection branch. That includes a Hopf-type linking or helicity number, which is the natural candidate given NTE's Hopf substrate. On that branch the exclusion is only relocated, not escaped. The recast is safe on all branches only if the topological datum is unoriented.

## Q2 — is there a globally uniform datum on S³ outside the n = 2 multiplet?

**Yes, but only if "uniform" means homogeneous and isotropic, not merely homogeneous.**

- **Homogeneous only** (invariant under one SU(2) of translations): the left- or right-invariant 1-forms qualify, and they **are** the n = 2 multiplet. Each one singles out a direction in the other SU(2), so it is **not isotropic**. PC's A1 holds for this reading: "maximally smeared *vector* data" is the n = 2 multiplet and inherits its parity.
- **Homogeneous and isotropic** (SO(4)-invariant): the SO(4) representations (1,0) and (0,1) have no singlet, so **no invariant 1-form exists**. The only fully uniform data are **scalars** (constants), the **round metric** (its conformal class), and the **volume form**.
- **Consequence.** The recast's "completely smeared" is coherent only in the stronger sense, and only for scalar, metric or volume-type data. A2's claim that the object "is not a photon" does not remove the gauge-field option. See Q5.

## Q3 — trigger-as-perturbation versus uniform datum: must the corpus choose?

**It must choose, and the C21 mechanism needs the uniform datum.**

- A fully uniform datum has no feature, so it cannot seed inhomogeneity. A3 holds.
- The C21 mechanism does not need the seed to perturb anything in the daughter:
  - The **trigger** is a parent-side condition, n_γ V_H = 1 (Part 1 §V).
  - The daughter's **primordial perturbations** come from Φ vacuum fluctuations (T5: the seed has no channel into the primordial spectrum).
- **Resolution.** The word "trigger" belongs to the parent, the datum belongs to the daughter, and nothing needs to be a perturbation. Greg's "the seed is a trigger, and a trigger owes nothing to persistence" is consistent with this, provided "trigger" names the parent-side event and not a daughter-side feature.

## Q4 — is Ω + topological class + conformal class enough to fix β_NTE?

**Register: the information count is at most one real number. Sufficiency is not established. The circularity discipline applies.**

- **Conformal class carries zero information.** Every conformally flat metric on S³ is conformally equivalent to the round one, so "conformally flat S³" is a single point, not a parameter.
- **Unoriented topology carries zero information.** It is a label, and it is fixed.
- **Ω carries one real number.** At most ℓ_P/R_H,parent, and that ratio is built from the parent's H_dS, i.e. from the parent's own β and Λ. Using Ω to fix the daughter's β is therefore exactly the fixed-point recursion of `Working\Paper_Alpha_Cosmological_FixedPoint_CCC_Exploratory_v0_1_Scratch_20260603.md` §3.
- **Counting.** One real number can in principle map to one real number, so the count does not rule the idea out. But no map Ω → β is deposited. **Sub-case B is unbuilt, and the recast is merely consistent with it.**
- **Additional adversarial point.** Under the recast the parent's "photon phase" (Part 1 §V's list) does **not** cross, because a phase belongs to a vector mode. That removes one candidate information carrier and tightens the budget.

## Q5 — what is the crossing object on the Euclidean side?

- **Part 1 §III and Euclidean signature do block "photon"**, meaning a null, propagating quantum. They do **not** block **gauge-field data on the S³ slice**. S³ is Riemannian in *both* signatures, and a Euclidean Maxwell configuration A_i on it is well defined, with exactly the n = 2 decomposition and parity P4 computed.
- **So A2's naming point is not load-bearing by itself.** Renaming the object does not change its type. If what crosses is gauge-field data, P4 applies unchanged.
- **Proposed term.** In Hartle–Hawking language the object is an argument of the no-boundary wavefunction Ψ[h_ij, Φ, … | S³]: a **boundary datum**. For the recast specifically, **"inherited conformal datum"** would do, because it names the type (scalar/conformal) and so excludes the vector option by construction.
- **Does "which photon mode" arise?** On the **parent** side, yes: the trigger photon is a mode of the parent's field. On the **daughter** side it does not arise **if and only if** the corpus states that the crossing object is the conformal datum and not the gauge-field configuration. **That sentence is the whole recast.**

## Q6 — two-link reading; Part 1 §V and §2.1.4 as they stand

- **Two-link reading: correct.** The seed or datum is at N = 0. Time appears at N_lock via the signature-change saddle. The second link is the unbuilt constrained-system saddle (the P1–P3 open node), so the chain is one link stated and one link open.
- **§2.1.4 does not exist.** Current Part 1 has §§2.1, 2.1.1, 2.1.2, 2.2, 2.3 and 2.4. The directive's pointer is dangling. §2.1.2 is presumably meant; it states the Euclidean section and the signature-change saddle correctly, as reformulation.
- **§V states the vector-mode reading as canonical text.** It calls the seed "the universe's last electromagnetic mode — pure geometric information (conformal class, S³ topology, **phase**, Ω)". Under the recast:
  - "phase" must go (it is vector-mode content that does not cross);
  - "last electromagnetic mode" must be moved to the parent side ("triggered by the last electromagnetic mode").
- **As it stands, §V is the vector reading. It is therefore exposed to P4's exclusion branch pending Greg's two rulings.**

## Q7 — pricing the trade

**If the recast is adopted (datum = scalar/conformal):**

| §12.1 content | Fate |
|---|---|
| n = 2, six-fold, λ = πa | **Lost** as daughter content. It survives only as a parent-side description, and even there the parent's Hubble patch is a static de Sitter patch, not a closed S³. |
| "n = 2 because H¹(S³) = 0" | **Lost.** It explains a vector mode that no longer crosses. |
| Entropy ≤ k ln 6 | **Replaced and strengthened.** A single real number carries S = 0. |
| Weyl-free start (T4) | **Unaffected.** T4 already sourced it from the parent's conformal flatness, not from the seed. |
| Photon phase as information carrier | **Lost.** |

**If the vector reading is kept:**

- Its mode content produces **no observable** (T2, T3 and T5 all returned null) and **no derivation** (T1: the seed does not pin N_e).
- It is **descriptive content**, and it carries a live exclusion risk on the antipodal-plus-gauged branch.

**Adversarial conclusion.**
- The mode content is **not sufficient reason** to keep the vector reading against the exclusion risk. It buys nothing testable.
- The recast is the stronger position, **but only if stated at its true price**:
  - the photon triggers and the conformal factor crosses;
  - the seed's mode structure, phase and "photon-ness" do not survive into the daughter;
  - the result is structurally closer to Penrose (whose crossing datum is also conformal), and NTE's departure then lies only in *where* crossing happens (per Hubble patch, discrete, local), not in *what* crosses.
- That is a **smaller claim than §V currently makes**, and it should be stated as smaller.

## P4 status

**P4 stands unmodified.** It answered the question it was asked (parity of a vector datum on the fixed locus), and the recast does not overturn that answer. Under the recast the question changes type, and P4's own table then gives "even on all branches" for scalar data. That is a pass, not a revision.

## For AC's arbitration

1. The recast survives **only** as "the crossing object is scalar/conformal data". The BC-versus-field distinction is not what carries it.
2. The recast removes the seed's dependence on Greg's two definitional rulings. **The rulings are still needed** for the architecture (Part 2 and the relevant Companion), but no longer for C21.
3. On the reflection branch, **oriented or chiral topological data is excluded**. The recast must specify unoriented topology.
4. Part 1 §V needs a wording change if the recast is adopted: drop "phase"; move "last electromagnetic mode" to the trigger clause.
5. §2.1.4 is a dangling pointer, in the directive and possibly in C21. The intended target is §2.1.2.

— Jammer, 2026-09-24
