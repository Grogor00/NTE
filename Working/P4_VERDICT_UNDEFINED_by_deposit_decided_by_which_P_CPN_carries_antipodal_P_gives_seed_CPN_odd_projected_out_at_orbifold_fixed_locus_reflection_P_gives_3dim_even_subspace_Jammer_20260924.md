# P4 VERDICT — is a single S³ seed mode compatible with CPN and the Janus pair?

**From:** Jammer · **To:** AC · **Cc:** Greg, Scratch, PC · **Date:** 2026-09-24
**Answers:** `Handoffs\Handoff_AC_to_Scratch_Jammer_P4_Seed_Mode_CPN_Janus_Compatibility_20260924.md`
**Fork:** AC's four outcomes, pre-registered in the handoff before this computation.
**Register:** representation theory on S³ plus the corpus's own orbifold statement (Part 1 §VI). No new commitments.

---

## Verdict: Outcome 4 (undefined by the deposit), with the decision tree fully resolved

The answer depends on one item the corpus has not fixed: **what the "P" in CPN does on the boundary S³.** The corpus uses two readings:
- **Antipodal.** "CPN = unitary antipodal map on S³" (canonical definition, quoted in GATE6b).
- **Orientation-reversing parity.** Any genuine P.

These are different maps, and they give opposite answers.

## 1. The n = 2 photon modes (standard; verified by construction)

On unit S³ ≅ SU(2), the coexact 1-form (transverse photon) spectrum is *d-eigenvalue ±n, n ≥ 2, with multiplicity n²−1 per sign. At **n = 2** the six modes are exactly:
- the **three left-invariant 1-forms** σᵢ, SO(4) rep (1,0), one helicity; and
- the **three right-invariant 1-forms** τᵢ, rep (0,1), the other helicity.

For example, σ₁ = x₀dx₁ − x₁dx₀ + x₂dx₃ − x₃dx₂ and τ₁ = x₀dx₁ − x₁dx₀ − x₂dx₃ + x₃dx₂.

**On the six (as AC required).** 6 = dim so(4). The n = 2 modes are the Killing 1-forms of S³, and the integral curves of σᵢ are **Hopf fibres**. This is a representation-theory fact. It asserts no physics connection, and no significance is claimed. Noted only because the corpus's substrate is Hopf S³.

## 2. How each piece of CPN acts on the n = 2 space

| Piece | Action on n = 2 | Basis |
|---|---|---|
| **C** | −1 on every mode (A → −A) | Photon is C-odd. Note: "self-conjugate" means its own antiparticle, **not** C-even. The NTFN line "CPN(γ) = γ" conflates the two. |
| **P = antipodal x → −x** | **+1** on all six | x → −x is the central element of SU(2), both a left and a right translation, so it fixes σᵢ and τᵢ. In general, coexact modes have antipodal parity (−1)ⁿ. |
| **P = reflection (e.g. x₃ → −x₃)** | **swaps** σᵢ ↔ τᵢ (helicity flip) | This is the orientation-reversing element of O(4), which exchanges SU(2)_L and SU(2)_R. |
| **N** | trivial on an N-independent boundary datum (unitary, per canonical) | The photon has zero embedding depth, so its boundary datum carries no N-dependence. |

## 3. The decision tree

**(A) P = antipodal**, the canonical definition's reading. Then CPN = C·(+1)·1 = **−1 on every n = 2 one-photon state.** Every single-quantum seed is CPN-odd.
- **If CPN is a global symmetry:** the −1 is an overall phase on a ray. Sheet B's state is −|seed⟩, the same physical state. The shared seed survives, and the sign is unobservable (**Outcome 2, harmless**). It is a separate freedom from the δ_J within-sector CP-parity: that is a fermion-sector phase, this is a photon ray phase, and neither fixes the other.
- **If CPN is gauged, which is what the corpus says:** Part 1 §VI calls the Janus pair a **Z₂ orbifold**, and N± has been treated as a discrete gauge redundancy. Orbifold-odd fields obey **Dirichlet conditions on the fixed locus**, and the fixed locus of N → −N is **the N = 0 boundary itself**. This is the standard mechanism by which an orbifold that includes C projects gauge-field components off the fixed plane.
  - **So a CPN-odd tangential photon mode vanishes exactly where the seed is supposed to live.**
  - **The single shared seed is excluded (Outcome 3).** C21's boundary-data reading would then need, for example, a two-photon (C-even) seed, or a statement that the seed is not a tangential field mode on the fixed locus.

**(B) P = orientation reversal.** Then CPN maps σᵢ → −τᵢ. The six-dimensional space splits into two three-dimensional eigenspaces:
- **CPN-even:** σᵢ − τᵢ;
- **CPN-odd:** σᵢ + τᵢ.

A single quantum in the **even** subspace (zero net helicity, a linear-polarisation-type combination) is **shared by both sheets without sign** and survives the orbifold with Neumann conditions. This is **Outcome 1, conditional**: the seed must lie in the even three-plet. That is a restriction on the seed, not an automatic result.

## 4. The side check: why n = 2 and not n = 1

- **Not from the antipodal identification.** There is no n = 1 coexact 1-form on S³ at all, because H¹(S³) = 0 and the transverse spectrum starts at n = 2.
- If the antipodal map were used as a **spatial** quotient S³ → RP³, it would remove the odd-n modes (n = 3, 5, …) and keep n = 2. So it constrains the tower above the seed, not the seed itself.

## 5. What would resolve it (routed to AC; Part 2 / Companion matter, not C21)

The corpus must state **which P** its CPN contains when acting on boundary vector fields.
- The canonical wording, "antipodal map on S³", is orientation-**preserving** on S³. It is therefore not a parity in the 3D sense, and calling it "P" is a register problem in its own right.
- If the canonical wording stands and the orbifold is gauged, **a single-photon seed on the fixed locus is excluded.**
- If CPN's P is a genuine reflection, the shared seed survives in the even three-plet.
- This is a definitional choice with physical consequences. **Greg's call. It should not be resolved by preference for the outcome.**

## Caveat
The orbifold-parity argument treats the N = 0 boundary as the Z₂ fixed locus, as Part 1 §VI's orbifold implies. If the corpus intends CPN to act freely (no fixed points) on the N-thickness, the Dirichlet step does not apply, and branch (A) reverts to harmless Outcome 2. That too needs one sentence of specification.

— Jammer
