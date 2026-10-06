# Gate 4b — TM1 vs TM2 charged-lepton sub-check: which trimaximal column does J₃(𝕆) select?

**Stream:** Scratch (independent adversarial verification)
**Date:** 2026-06-26
**Status:** RESOLVED toward TM2 (the data-disfavoured branch). Honest negative. Master corpus untouched.
**Method:** Wolfram-grounded (residual-symmetry generators, conjugation/determinant invariants). No manufactured positives.
**Supersedes the optimistic framing in:** GATE4_VERDICT_PARTIAL_PMNS_from_J3O… (which flagged TM1 as the promising branch "if J₃(𝕆) selects it"). It does not.

---

## Question

PMNS = U_e† U_ν. Gate 4 reduced the mixing matrix to one input (θ₁₃) plus a fork: trimaximal **TM1** (preserves (2,−1,−1)/√6; sin²θ₁₂ = 0.318, 0.93σ — good) vs **TM2** (preserves (1,1,1)/√3; sin²θ₁₂ = 0.341, 2.8σ — poor). Which does the J₃(𝕆) charged-lepton sector actually select?

## The selector is a residual-Z₂ choice

Trimaximal type ⟺ which residual Z₂ the light-neutrino mass matrix preserves (it shares that generator's non-degenerate eigenvector, which becomes a fixed column of U):

| residual Z₂ | non-degenerate eigenvector | det | trimaximal type | sin²θ₁₂ | pull |
|---|---|---|---|---|---|
| **S_mag** (magic, democratic) | **(1,1,1)/√3** | **+1** | **TM2** | 0.341 | **2.8σ** |
| **S·U** | **(2,−1,−1)/√6** | **−1** | **TM1** | 0.318 | **0.93σ** |

The fully democratic three-slot neutrino matrix commutes with *both* (it is the unbroken TBM point, θ₁₃ = 0). So the type is fixed by **which Z₂ survives the breaking that turns θ₁₃ on**, with charged leptons diagonal throughout.

## Three facts force the answer to TM2

1. **Democratic = (1,1,1) = S_mag.** The natural J₃(𝕆) reading puts all three Jordan slots on equal footing; the surviving direction is the democratic/trace vector (1,1,1). That is the S_mag residual ⇒ **TM2**.
2. **S_mag and S·U are not conjugate** (det +1 vs det −1). Therefore **no basis change — and in particular no charged-lepton rotation U_e — can convert a democratic (S_mag) neutrino sector into a TM1 PMNS.** Verified: U_e†·S_mag·U_e keeps det = +1 for every orthogonal U_e, so its non-degenerate eigenvector can never become (2,−1,−1).
3. **(1,1,1) ⊥ (2,−1,−1).** Reaching TM1 would require a 90° rotation that singles out generation 1 — not a small, natural charged-lepton correction.

## Consequence: the route to TM1 is not available naturally

TM1 (the 0.93σ fit) requires an **intrinsically generation-1-distinguished** neutrino connector texture — the det = −1, S·U residual. **No J₃(𝕆) mechanism in hand supplies this.** Asserting one to capture the better fit would be manufacturing a positive; declined.

## Verdict

**J₃(𝕆), read naturally (democratic three-slot symmetry), selects TM2 → sin²θ₁₂ = 0.341 → 2.8σ.**

- The charged-lepton sector **cannot** flip this to TM1 (determinant obstruction; robust).
- Therefore the corpus's standing **"sin²θ₁₂ = 1/3 leading order, ~2.9σ residual" is STRUCTURAL** under the natural reading — the trimaximal sum rule reproduces the tension rather than retiring it.
- The Gate-4 hope ("TM1 could clear the residual") is **downgraded**: TM1 is not the algebra's default and is not reachable by charged-lepton structure.

This is a recognition-gate correction to Gate 4, recorded rather than smoothed over.

## What would change the verdict (precise, falsifiable)

The *only* escape to the good fit is a genuine J₃(𝕆) reason for the neutrino connector texture to single out generation 1 (det = −1, S·U residual). Candidate hooks, none yet derived: (i) the lightest-neutrino / m₁→0 structure picking out slot 1; (ii) alignment of the connector with a distinguished octonion unit other than the democratic sum. If — and only if — such a mechanism is derived does sin²θ₁₂ = 0.318 (0.93σ) follow. Until then the natural prediction is TM2.

## Net effect on the PMNS programme

- θ₂₃ = π/4, |δ| = π/2: still forced (slot-swap; unaffected).
- θ₁₂: forced to the **TM2** sum-rule value 0.341 (2.8σ) under the natural reading — a genuine, and genuinely tensioned, prediction.
- θ₁₃: still one free input; Cabibbo/√2 link still unproven.

PMNS is "two forced, one forced-but-2.8σ-tensioned, one input." The honest headline: **the algebra makes a falsifiable solar-angle prediction (0.341) that sits 2.8σ from data** — that is a sharper, more useful statement than an unfixed parameter, even though it is not the comfortable answer.

*No corpus edit proposed. If ratified, the change is to state the solar angle as a TM2 sum-rule prediction (0.341, 2.8σ) and to log the generation-1-distinguished texture as the sole open route to TM1 — Greg's call.*
