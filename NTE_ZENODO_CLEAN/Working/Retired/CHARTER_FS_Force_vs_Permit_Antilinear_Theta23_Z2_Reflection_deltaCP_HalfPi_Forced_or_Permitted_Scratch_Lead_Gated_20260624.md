# CHARTER — FORCE-vs-PERMIT derivation: does NTE's chirality-superposed Majorana structure FORCE the θ₂₃ Z₂ to be the antilinear μτ-REFLECTION (→ δ_CP = ±π/2 predicted), or merely PERMIT it? Scratch-lead, gated, kill-conditions up front.

**From:** Scratch (FS-geometry charter lead, Claude model)
**To:** AC; Cc: Greg, Jammer, PC, Cursor
**Date:** 2026-06-24
**Parent:** FS-geometry finding (`FS_Geometry_Finding_Theta23_Z2_Should_Be_MuTau_REFLECTION_...20260624`). Couples to Paper P4 (θ₂₃) and ratified CPN/emergent-ℂ antilinear structure (C5).
**Status:** investigation pathway. No corpus touch. P4 unedited. Nothing adopted until the derivation clears and Greg ratifies.

---

## 0. Discipline (read first — this is the exciting-result trap)
This pathway is *promising*, which is exactly why the gate is strict. The failure mode is letting enthusiasm convert "the antilinear reading is *available*" into "it is *forced*." **"PERMIT, not FORCE" is a fully acceptable — and a priori likely — outcome.** If it lands there, δ_CP=±π/2 becomes "NTE naturally accommodates maximal CP violation," **not** a zero-parameter prediction, and we say so plainly. The δ=±π/2 result is itself textbook (Harrison–Scott μτ-reflection); the only thing of value here is whether NTE's structure *forces* the reflection. Derive-then-compare; data enters only after the force/permit verdict.

## 1. The precise question
A Z₂ swapping σ₁↔σ₂ on the neutrino sector can be implemented two ways:
- **Linear (exchange, what P4 uses):** real equalities U_{μi}=U_{τi} ⟹ θ₂₃=π/4, **θ₁₃=0**, δ_CP free.
- **Antilinear (reflection):** magnitude equalities |U_{μi}|=|U_{τi}| ⟹ θ₂₃=π/4, **θ₁₃≠0 natural**, **δ_CP=±π/2 forced**.

**Decision to render: FORCED-ANTILINEAR / PERMITTED-ONLY / FAIL.** "Forced" requires showing the chirality-superposed Majorana (charge-conjugation-coupled) structure makes the linear implementation *inconsistent* — not merely less natural.

## 2. The entry hook (promising, unproven — Gate A tests it)
In the Pauli basis, **σ₂ is the imaginary generator: σ₂\* = −σ₂, while σ₁\* = σ₁ and σ₃\* = σ₃.** So σ₁↔σ₂ exchanges a *real* generator with an *imaginary* one. Naively this cannot be a conjugation-commuting ("real") operation — it looks intrinsically tied to the complex structure. **But** this could be an artifact removable by a unitary basis change (e.g. rotating to σ_± = σ₁±iσ₂, where the "swap" becomes something else). Whether the imaginariness is *physical* (forces antilinearity) or *removable* (basis artifact) is Gate A. Do not assume it forces anything.

## 3. Gates (run in order; do not pass a failed gate)

**Gate A — Is σ₂'s imaginariness physical or removable?** Establish σ₂\*=−σ₂ in the working basis; then test whether a unitary change of basis can recast σ₁↔σ₂ as a swap of two *real* generators (making a linear implementation manifestly available). 
- KILL: if a basis exists in which σ₁↔σ₂ is a real swap with no conjugation, the imaginariness is not forcing → lean PERMIT (proceed to B only to confirm).
- PASS: if no such basis preserves the physical assignment (σ₃ = Higgs-VEV/Cartan fixed), the imaginariness is physical → continue.

**Gate B — Does the Majorana condition force it? (the core)** Write the Majorana reality condition ψ = ψ^c = C ψ̄^T explicitly for the σ₁- and σ₂-polarised chirality-superposed modes (C antilinear). Apply both candidate Z₂'s. 
- Test: does the **linear** exchange preserve the Majorana condition on these modes, or does preservation **require** the swap to carry the conjugation (antilinear)?
- KILL: linear exchange preserves ψ=ψ^c with no conjugation ⟹ C does **not** force antilinearity ⟹ PERMITTED-ONLY.
- PASS: the σ₁,σ₂ modes' charge-conjugation coupling makes the linear swap violate the Majorana condition, so only the antilinear swap is consistent ⟹ FORCED.
- *(Watch: a symmetry can commute with antilinear C and still be linear — commuting-with-C alone is NOT sufficient for forcing. The forcing, if real, must come from the swap exchanging the real/imaginary polarisations while preserving ψ=ψ^c. Be rigorous here; this is where motivated reasoning would slip.)*

**Gate C — CPN inheritance (the NTE-specific leg).** Is the σ₁↔σ₂ Z₂ identical to, or descended from, the **ratified antilinear CPN** operation (C5: emergent CPT = antilinear J; CPN structure)? If the corpus's CPN already acts on the σ₁,σ₂ chirality-superposed sector and implements (or contains) the swap, the Z₂ inherits antilinearity from ratified structure — the strongest possible "forced."
- KILL: CPN does not act as / contain the σ₁↔σ₂ swap ⟹ no ratified inheritance (fall back to B's verdict).
- PASS: CPN implements the swap antilinearly ⟹ FORCED, and tied to ratified canon.

**Gate D — derive-then-compare (only if A–C ⟹ FORCED).** 
- (i) Confirm the forced reflection reproduces θ₂₃=π/4, makes θ₁₃≠0 natural, and yields δ_CP=±π/2 (already verified numerically; re-confirm in the derived basis).
- (ii) **Sign sub-question (stretch):** can NTE fix the sign (+π/2 vs −π/2) via the CPN/Janus *orientation selection* (the same orientation that fixed the GW-chirality sign in C3)? If the orientation picks δ=−π/2, that matches the mild global-fit lean and is a sharper, sign-definite prediction. If the sign is not fixed, predict |δ_CP|=π/2 only.
- (iii) Data: δ≈−π/2 within ~1σ of some fits; T2K/NOvA unsettled; DUNE/Hyper-K decisive. Live + falsifiable, not confirmed.

## 4. Outcomes
- **FORCED-ANTILINEAR:** P4 upgrades exchange→reflection; gains a **δ_CP=±π/2 (poss. sign-definite) prediction** and a **natural θ₁₃**; ties θ₂₃ to ratified CPN. Candidate standalone-paper upgrade. → AC review, Greg ratify.
- **PERMITTED-ONLY:** δ_CP=±π/2 is an attractive option NTE accommodates, not a prediction; P4 stands as-is; honest "natural-but-not-forced" note. (Likely; fully acceptable.)
- **FAIL:** the reflection is inconsistent with NTE structure (e.g. breaks θ₂₃=π/4 or the Majorana condition) → drop; FS finding reverts to "angles = re-description, δ_CP lever closed."

## 5. Kill conditions up front
σ₂-imaginariness removable by basis (A); linear exchange preserves the Majorana condition (B); CPN does not implement the swap (C); or the forced reflection breaks θ₂₃=π/4 / the seesaw (D-i). Any one ⟹ not a forced prediction.

## 6. Deliverable + first step
Deliverable: `Investigation_FS_Force_vs_Permit_Antilinear_Z2_Scratch_v1` (Working/), Gate A first, explicit per-gate verdicts, no passing a failed gate. **First step: run Gate A** (cheap, sharp — the σ₂-imaginariness basis test). It tells us fast whether the hook is physical or an artifact.

— Scratch, 2026-06-24. Set up to fail honestly. The hook (σ₂ is the imaginary Pauli generator, so the swap exchanges real↔imaginary) is real and sharp, but it has to survive a basis-removal test, a Majorana-condition test, and a CPN-inheritance test before "permit" becomes "force." Promising is not proven — that's what the gates are for.
