# Handoff: AC → Scratch + Jammer — resolve the δ_J sign (CR S1)

**From:** AC · **To:** Scratch (derive) + Jammer (adversarial) · **Cc:** Greg, CR · **Date:** 2026-07-06
**Priority:** P1 — δ_J is one of only two near-term empirical exposures of NTE (the other is κ), and per CR's O1 it is the *sole* near-term test of the bilateral CPN ontology. It currently leans against data.
**Guardrail:** derive the sign, do **not** fit it. We just shipped a θ₁₃ = 0 blocker by lifting a value that flattered a symmetry rather than checking it — the opposite error (asserting −π/2 because data wants it) is exactly as bad. If the geometry forces a sign, report which; if it doesn't, say so.

## The problem

- Part 1 §III writes **|δ_J| = π/2** (magnitude); the abstract and Part 3 (A) write **δ_J = +π/2** (signed). Inconsistent across the deposit.
- The mixing-sector paper concedes "the corpus commits to +π/2 while fits lean −π/2." NuFIT prefers **δ_CP ≈ −π/2**. So the committed +π/2 is ~1.5–2σ disfavoured.

## The question

Does the antilinear μ–τ reflection on J₃(𝕆), together with the CPN bilateral structure, **fix the sign of δ_J** — and if so, which? Three possible verdicts, each with a clear consequence:

1. **Geometry forces −π/2** → matches NuFIT; NTE gains a second genuine prediction. Best case. Derive it explicitly (the reflection's action on the CP-odd invariant / the sign of the Jarlskog J).
2. **Geometry forces +π/2** → a real ~1.5–2σ tension, falsifiable at DUNE/Hyper-K. Not a disaster — state it as an honest standing prediction that current data disfavours, and let the experiments decide.
3. **Sign genuinely unfixed** (only |δ| = π/2 is geometric) → then the corpus must retreat to the magnitude claim everywhere, and stop writing +π/2. Weaker but honest.

## Roles

- **Scratch (derive):** work the antilinear reflection's action on the PMNS phase concretely — does the octonion conjugation x₃ → x̄₃, composed with the CPN orientation map, pin the sign of J, or only |δ|? This is the constructive computation.
- **Jammer (adversarial):** independently check whether the committed +π/2 is a convention artifact (basis/phase choice) rather than a physical prediction. Recompute in a different convention; if the sign flips with convention, it isn't predicted.

## Deliverable

A Working note with a one-line verdict (FORCED −π/2 / FORCED +π/2 / MAGNITUDE-ONLY), the computation, and a ready-to-cite sentence for §III and Part 3. Route to AC → Greg. This is also the input AC needs to fix §III's δ_J wording once, cleanly (it sits in the same sentence as the θ₁₃ blocker fix).

— AC, 2026-07-06.
