# Handoff: AC → Cursor — B1 + B2 blocker fixes (deposit-gating), render

**From:** AC · **To:** Cursor (apply + render) · **Cc:** CR, Greg · **Date:** 2026-07-06
**Status:** Greg-ratified. Two shipped defects flagged by CR's 2026-07-06 adversarial pass. **Do not deposit until these are applied and re-rendered.** Both are AC-introduced errors from the CR-response batch.

**Application rule:** match on distinctive prose, not whitespace; preserve LaTeX `$…$`. After each edit re-read, confirm NEW present / OLD gone. **If an OLD block doesn't byte-match, stop and report — do not force.** Keep Core_Papers and paper-build/scratch-src in sync; re-render the touched files; confirm 29/29.

**Not in this batch (pending):** the δ_J sign vs magnitude reconciliation (CR S1) is with Scratch/Jammer — B1 leaves §III at |δ_J| = π/2 (magnitude), untouched, so it does not prejudge that verdict.

---

## B1 — Part 1 §III: θ₁₃ = 0 is false (>5σ) and self-refuting. Correct to naturally-nonzero.

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §III

**OLD:**
```
What this ontology forces is symmetry structure, and that is where its clean content sits: the Majorana character (a falsifier at neutrinoless double-beta decay) and, from the antilinear $\mu$–$\tau$ reflection on $J_3(\mathbb{O})$ (Jordan Hermiticity), the maximal atmospheric angle $\theta_{23} = \pi/4$, $\theta_{13} = 0$, and the maximal phase $|\delta_J| = \pi/2$ (matching observation). That reflection fixes $\theta_{23}$, $\theta_{13}$, and $\delta$ — but not the solar angle: $\sin^2\theta_{12} = 1/3$ is a separate leading-order value from a distinct, still-open route (currently $2.9\sigma$).
```
**NEW:**
```
What this ontology forces is symmetry structure, and that is where its clean content sits: the Majorana character (a falsifier at neutrinoless double-beta decay) and, from the antilinear $\mu$–$\tau$ reflection on $J_3(\mathbb{O})$ (Jordan Hermiticity), the maximal atmospheric angle $\theta_{23} = \pi/4$, a naturally nonzero reactor angle $\theta_{13}$ (consistent with the measured $\approx 8.6^\circ$ — the reflection's advantage over a $\mu$–$\tau$ permutation, which would force $\theta_{13} = 0$), and the maximal phase $|\delta_J| = \pi/2$ (matching observation). That reflection fixes $\theta_{23}$ and the magnitude of $\delta$, and makes $\theta_{13}$ naturally nonzero — but not the solar angle: $\sin^2\theta_{12} = 1/3$ is a separate leading-order value from a distinct, still-open route (currently $2.9\sigma$).
```

*Why:* θ₁₃ ≈ 8.6° (Daya Bay/RENO, >5σ). "θ₁₃ = 0 matching observation" was false and self-refuting (Jarlskog J ∝ sin θ₁₃, so θ₁₃ = 0 kills the very CP phase claimed observed). The mixing-sector paper's actual result is that μ–τ *reflection* gives *naturally nonzero* θ₁₃ — its advantage over the permutation baseline. The correction is faithful to the source and stronger for NTE.

---

## B2 — Part 3: the distinctiveness paragraph contradicts the CC section on a₄. Strike the a₄ clause.

**TARGET:** `NTE_v10_18_0_Part3_Accounting.md`, Empirical-distinctiveness paragraph

**OLD:**
```
via the absence of a gravitating 4-bulk vacuum and the $a_4 = 0$ suppression on $S^3\times S^1$
```
**NEW:**
```
via the absence of a gravitating 4-bulk vacuum and a trace-free/unimodular treatment in which the vacuum energy does not gravitate
```

*Why:* the CC section of the same file already states the mechanism is "independent of a₄." The CC-problem magnitude is an a₀/a₂-order quantity; a₄ is irrelevant to it. This aligns the distinctiveness paragraph with the CC section (boundary-only + trace-free/unimodular).

---

## After apply

Re-render Part 1 and Part 3; confirm 29/29; return a completion handoff. Deposit unblocked on B1/B2 once this lands (CR S1/S2/S3 and O1 remain open, non-blocking-by-CR-ranking except where Greg rules otherwise).

— AC, 2026-07-06.
