# Gate 4 — PMNS from J₃(𝕆): how far does the algebra force the mixing matrix?

**Stream:** Scratch (independent adversarial verification)
**Date:** 2026-06-26
**Status:** PARTIAL — not end-to-end; reduces to one free input + a resolvable fork. Master corpus untouched (draft).
**Method:** Wolfram-grounded (Takagi factorisation, Jarlskog, trimaximal construction). No manufactured positives.

---

## Question

Convert "PMNS inherits by composition" into "derived end-to-end on J₃(𝕆)."
Concretely: with the inter-generation connectors restricted to the colour-singlet ℂ = {1, e₁} line (Gate 3), does the Albert-algebra structure force all four PMNS observables (θ₁₂, θ₁₃, θ₂₃, δ), or only some?

## Result 1 — the slot-swap (μ–τ reflection) forces θ₂₃ and δ, and ONLY those

The J₃(𝕆) Hermitian slot-swap, on the e₁ line, is the antilinear μ–τ reflection acting on the complex-symmetric Majorana matrix: **S · M̄ · S = M**, S the μ↔τ exchange.

Verified over random reflection-compliant M (Takagi factorisation, eigen-decomposition of M†M):

- constraint residual = 0 (exact), and
- **sin²θ₂₃ = 0.5 exactly** ⇒ θ₂₃ = π/4, for every compliant M;
- **|U_μi| = |U_τi| exactly** for all i;
- **|J| = J_max exactly** for every compliant M ⇒ sin δ = ±1 ⇒ **|δ| = π/2**.

But across the same sample:
- sin²θ₁₂ roamed **0.06 → 0.85**,
- sin²θ₁₃ roamed **0.01 → 0.45**.

**θ₁₂ and θ₁₃ are completely free under the reflection alone.** (This reproduces the Grimus–Lavoura / Harrison–Scott μτ-reflection theorem from the algebra side, and it re-grounds Gates 2–3.) PMNS is therefore **not closed** by the slot-swap: two real parameters remain open.

## Result 2 — the democratic S₃ (all three slots equal) adds a trimaximal sum rule for θ₁₂(θ₁₃)

Promoting the Z₂ slot-swap to the full democratic S₃ of the three Jordan slots forces trimaximal mixing: one column of U_TBM survives. Which column survives is the open fork, and it fixes the θ₁₂–θ₁₃ sum rule. With θ₁₃ at its measured value (sin²θ₁₃ = 0.0222):

| structure | preserved column | sin²θ₁₂ closed form | value | pull vs 0.307(12) |
|---|---|---|---|---|
| TBM (exact S₃, θ₁₃=0) | — | 1/3 | 0.333 | 2.2σ |
| **TM2** | (1,1,1)/√3 | 1/(3cos²θ₁₃) | 0.341 | **2.8σ** |
| **TM1** | (2,−1,−1)/√6 | (1−3sin²θ₁₃)/(3cos²θ₁₃) | **0.318** | **0.93σ** |

Two consequences:

1. **The corpus's standing "sin²θ₁₂ = 1/3 leading order, ~2.9σ residual" is the TM2/TBM branch.** The residual is exactly the θ₁₃-induced trimaximal shift — now identified, not mysterious.
2. **The TM1 branch predicts sin²θ₁₂ = 0.318 (0.93σ)** — materially better than 1/3 (2.2σ) or TM2 (2.8σ). If J₃(𝕆) selects TM1, the long-standing solar-angle residual is *resolved*, and θ₁₂ becomes a genuine sum-rule prediction in terms of θ₁₃.

## Result 3 — θ₁₃ is the single remaining free input

θ₁₃ parametrises the S₃ → Z₂ (democratic → reflection) breaking. It is **not fixed by J₃(𝕆) alone**. Once θ₁₃ is given, θ₁₂ follows by the sum rule and θ₂₃, δ are already forced — so the whole PMNS reduces to **one real input plus the TM1/TM2 fork.**

*Candidate external closure (flagged, NOT banked):* θ₁₃ ≈ θ_C/√2 ≈ 9.2° sits near the measured 8.6°; the corpus already carries "Cabibbo from Killing-spinor texture zero." If the same texture zero feeds θ₁₃, the last input closes. Separate investigation.

---

## Verdict

**PARTIAL — not end-to-end, but materially advanced and corpus-improving.**

- θ₂₃ = π/4: **forced** (slot-swap). ✓
- δ = ±π/2: **forced** (slot-swap; sign still open, +π/2 corpus vs −π/2 fits, left to DUNE/Hyper-K). ✓
- θ₁₂: **forced by a trimaximal sum rule** once θ₁₃ is input; TM1 gives 0.318 (0.93σ), TM2 gives 0.341 (2.8σ).
- θ₁₃: **one free input** (= S₃→Z₂ breaking); candidate Cabibbo/√2 link unproven.

PMNS goes from "all four inherited by composition" to **"two forced outright, one forced by sum rule, one input"** — with a concrete, testable, corpus-improving fork (TM1 vs TM2) and a clear next sub-check.

## Open sub-check (the next deep-dive)

**Which trimaximal column does J₃(𝕆) preserve — TM1 or TM2?** This is set by the charged-lepton-sector residual (PMNS = U_e† U_ν) and by which slot is the reflection-fixed one. Resolving it decides whether the algebra delivers sin²θ₁₂ = 0.318 (and retires the 2.9σ residual) or stays on the TM2 branch. This is the recommended next investigation, routed to the J₃(𝕆) charged-lepton embedding.

*No corpus edit proposed here. If ratified, the natural change is to replace the standing "sin²θ₁₂ = 1/3 leading order" with the θ₁₃-dependent trimaximal sum rule and to foreground the TM1/TM2 fork — Greg's call (sole ratification authority).*
