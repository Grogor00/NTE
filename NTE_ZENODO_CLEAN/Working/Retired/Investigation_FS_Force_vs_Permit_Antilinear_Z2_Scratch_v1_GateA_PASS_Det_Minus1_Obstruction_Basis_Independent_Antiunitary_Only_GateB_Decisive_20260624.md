# Investigation: FS Force-vs-Permit antilinear θ₂₃ Z₂ — GATE A VERDICT: PASS (σ₂-imaginariness is physical, not a basis artifact — it is the shadow of a basis-INDEPENDENT det = −1 obstruction; the swap is realizable only antiunitarily). Advances, does NOT yet close "forced." Gate B (Majorana condition) is decisive.

**From:** Scratch (lead, Claude model)
**To:** AC; Cc: Greg, Jammer, PC, Cursor
**Date:** 2026-06-24
**Charter:** `CHARTER_FS_Force_vs_Permit_Antilinear_Theta23_Z2_...20260624`. Gate A only. No corpus touch; P4 unedited; nothing adopted.

**GATE A: PASS.** The σ₂-imaginariness survives the basis-removal test — but the operative fact is stronger and basis-independent. **It does not by itself prove FORCED; it sharpens the question for Gate B.**

---

## What Gate A had to test
The charter's hook — "σ₂ is the imaginary Pauli generator (σ₂\* = −σ₂)" — is basis-dependent and could be a removable artifact. Gate A: can a unitary change of basis recast σ₁↔σ₂ (with σ₃ fixed as the Higgs-VEV/Cartan direction) as a swap of two *real* generators, making a linear implementation manifestly available?

## Result (computed, rigorous, basis-independent)
**No.** The σ₂-imaginariness is the basis-shadow of a determinant obstruction:
1. On the su(2) generator space, the map (σ₁→σ₂, σ₂→σ₁, σ₃→σ₃) is an **improper rotation: det = −1.**
2. **Det is a similarity invariant** ⇒ no change of basis makes it proper. Basis-independent.
3. Inner automorphisms σ_a → V σ_a V† (unitary conjugation, V∈SU(2)) realize **only det = +1** (SO(3)). Verified: 20,000 random unitary conjugations never approach the swap (closest distance 2.0 of 2.0). **No linear unitary conjugation realizes the swap, in any basis.**
4. The swap **is** realizable — but **only antiunitarily**: explicitly, M → V M\* V† with V = exp(−iπσ₃/4) reproduces (σ₁↔σ₂, σ₃ fixed) exactly. The antiunitary (complex-conjugation-carrying) operation supplies the missing det = −1.
5. The only **unitary** (det +1) alternative is σ₁↔σ₂ **with σ₃ → −σ₃** — proper, linear-realizable, **but it flips the Higgs-VEV/Cartan direction**, which the physical assignment forbids.

So: with σ₃ pinned to the VEV, the σ₁↔σ₂ swap on the spinor/chirality structure is an improper rotation that **cannot be linear-unitary in any basis** and **requires** an antiunitary realization. The hook is physical.

## The honest caveat (handed to Gate B — why this is not yet "FORCED")
The det = −1 obstruction is established for the action on the **2-dimensional spinor/chirality structure** (σ_a as 2×2 generators — the chirality-superposed sector). **P4 implements its Z₂ as a permutation ν_μ↔ν_τ on the 3-dimensional flavor Hilbert space**, where a det = −1 permutation is a perfectly good *linear unitary* operation. These are different spaces. Gate A therefore shows:
- At the **spinor/chirality level**, the swap is forced antiunitary. ✓
- At the **flavor-permutation level** (P4's choice), a linear implementation exists. ✗ (not obstructed)

**Gate B (the Majorana condition) must decide which level is physically operative.** If the chirality-superposed Majorana modes make the spinor/chirality level the operative one — i.e. the flavor permutation is an incomplete shadow of a spinor-level operation that must respect ψ = ψ^c (antilinear) — then antiunitary is FORCED and δ_CP = ±π/2 follows. If the flavor-permutation level stands on its own, P4's linear exchange is legitimate and the verdict degrades to PERMITTED-ONLY.

## Gate A disposition
- **PASS** — proceed to Gate B. The hook is not an artifact; it is a det = −1 improper-rotation obstruction, basis-independent, antiunitary-only at the spinor level, with the σ₃-flip escape forbidden by the physical VEV assignment.
- **Not yet FORCED** — the spinor-vs-flavor-level question is genuine and open; Gate B is where this is won or lost, and it can legitimately land on PERMITTED-ONLY.
- Bonus already banked: the antiunitary realization is V·K with V a 90° rotation about σ₃ — i.e. literally a (proper rotation)∘(complex conjugation), the textbook form of a μτ-reflection, and the complex-conjugation K is the same antilinear operation as ratified CPN (the Gate-C identification target).

— Scratch, 2026-06-24. Gate A: the σ₂-imaginariness isn't a basis trick — it's a det = −1 wall. With σ₃ pinned to the VEV, the swap can't be linear-unitary in any basis; it's antiunitary or it flips the VEV (forbidden). That makes the hook real. It does not yet make the prediction forced — that hinges on whether the Majorana condition makes the spinor level operative, which is Gate B. Honest advance, not a finish.
