# Handoff: AC → Scratch + Jammer — PUSH FOR THE SIGN: compute sign(δ_J) from the two missing pieces

**From:** AC · **To:** Scratch (constructive) + Jammer (adversarial) · **Cc:** Greg, CR · **Date:** 2026-07-06
**Priority:** P1 — upgrades δ_J from FORCED-in-principle to a signed, testable second prediction — or pins down precisely why it can't yet be computed.
**Foundation verified by AC:** mixing-sector paper Theorem 3 read against source — e₁ uniquely carries the phase (colour-fixed), J = L_{e₁}, Im(𝕆)=1⊕3⊕3̄, so e₁ orientation = particle/antiparticle split. The FORCED verdict (sign(J) locked to the e₁/matter orientation, no unbroken flip) stands and is AC-adjudicated. This directive builds on it.

## The target

Scratch's FORCED verdict established sign(J) is not free but named two missing pieces that block the specific value. **Construct them, and compute the sign — or identify exactly which piece is uncomputable and why.**

**Piece A — the octonion-orientation → PDG-δ dictionary.** Given the antilinear reflection x₃ → x̄₃ carried on e₁ (Thm 2–3), work out the resulting PMNS matrix in the standard PDG parameterisation and extract **sign(δ_CP) as a function of the e₁ orientation**. This is a representation/basis computation: map the fixed octonionic structure onto U_PMNS and read off the sign of the Jarlskog J = Im(U_e1 U_μ2 U*_e2 U*_μ1). Flag every convention introduced and confirm sign(J) is convention-independent once e₁ is fixed.

**Piece B — the physical pinning of the e₁ orientation.** Determine how B > 0 fixes the e₁ orientation, and whether the quark→lepton link is:
- **Direct** — the *same* e₁ carries the quark 3/3̄ split (hence B, via sphaleron+quark counting) and the neutrino phase (Thm 3), so B > 0 pins the e₁ orientation algebraically and no leptogenesis is needed; or
- **Dynamical** — the sign of B is set by the CP asymmetry ε in the heavy-neutrino (seesaw) decays, and sign(B) ↔ sign(δ_PMNS) runs through the high-scale flavour structure (the relation between the high-scale CP phases driving leptogenesis and the low-energy PMNS phase). If so, construct that sign-link within NTE's J₃(𝕆) seesaw (Companions 10, 13).

Decide which regime NTE is in, and build whichever link the answer requires. **If the shared-e₁ route (direct) closes it, say so — that would be the clean result.**

## Guardrails (hard — this is where it lives or dies)

- **DERIVE the sign; do not fit it.** The computation must yield sign(δ) from the structure with B > 0 as a *physical input*. **If it comes out +π/2 — against NuFIT's −π/2 lean — that is the answer, and you report it.** Choosing −π/2 because data wants it is the exact mirror of the θ₁₃ = 0 error and is void. Neither sign is privileged going in.
- **sign(J) is the observable**, rephasing-invariant. Keep it distinct from domain conventions (−π/2 ≡ 3π/2).
- **No smuggled convention in Piece A.** The PDG map introduces basis choices; show sign(J) is invariant under them once e₁ is fixed, or the "dictionary" is just relocating the freedom.
- **Honest ceiling if you hit it:** if a piece is genuinely uncomputable from current corpus structure, say exactly what object is missing (e.g., "the RH-sector Yukawa phases are free spectral data — Companion 13"), and the verdict is FORCED-uncomputed with the gap named. That is a valid, valuable outcome.

## Roles
- **Scratch (constructive):** build Piece A (the PDG dictionary) and Piece B (the pinning/link); compute sign(δ). You own the octonion/Jordan and seesaw structure.
- **Jammer (adversarial):** stress-test both — hunt for a hidden convention in the PDG map that fakes a determinate sign; check whether Piece B's B→δ link is actually forced or smuggles a phase choice; try to show the sign is still undetermined by a freedom the forcing analysis missed. If you can't break it, the sign stands.

## Honest outcomes
- **Computed +π/2** → genuine second prediction, ~1.5–2σ tension with NuFIT, stated openly; DUNE/Hyper-K decisive.
- **Computed −π/2** → genuine second prediction matching data — banked *only* if derived, not reverse-engineered.
- **FORCED-uncomputed, gap named** → we know exactly what NTE must build to make δ_J a signed prediction; not pre-deposit-blocking; deposit stays at |δ_J| = π/2 with the "forced, value-uncomputed" framing.

## Deliverable
Working note, one-line verdict (SIGN = +π/2 / SIGN = −π/2 / FORCED-UNCOMPUTED[gap]), Pieces A and B explicit, the sign(J) computation, and the per-convention invariance checks. Route to AC → Greg. AC will verify the computation against the paper before any signed value reaches the deposit.

— AC, 2026-07-06.
