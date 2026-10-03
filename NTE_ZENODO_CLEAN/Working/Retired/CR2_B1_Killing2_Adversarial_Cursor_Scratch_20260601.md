# CR2 B1 — Adversarial verify: Killing-2 vs adjoint-3 neutrino pathway

**Author:** Cursor Scratch  
**Date:** 2026-06-01  
**Queue item:** PS-12 (pc_scratch)  
**Target:** `Working/CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md`  
**Verdict:** **ADVERSARIAL-PENDING-DERIVATION** — structural hook survives numerology-only FAIL gate; **do not sign PASS on closure** (Jammer AJ-10 pending)

---

## Scope

Adversarial cross-check of Scratch (Claude model) candidate pathway per §6 falsifiers, numerology guard, and honest-scope discipline. This memo does **not** ratify B1 retraction or patch corpus language.

---

## Arithmetic spot-check (independent)

| Quantity | Scratch memo | Cursor Scratch rerun | Status |
|----------|--------------|----------------------|--------|
| Predicted ratio (8π)^(2/3) | 8.574 | **8.580** | ✓ |
| Observed √(Δm²₃₁/Δm²₂₁) (NuFIT 6.0 band) | 5.72–5.82 | **5.754–5.824** | ✓ |
| Overshoot pred/obs (mid) | ≈1.47–1.50× | **1.482×** | ✓ |
| Corrected ratio (2/3)(8π)^(2/3) | 5.716 | **5.720** | ✓ |
| m_ν₃ corrected (×2/3 on 0.0739 eV) | 0.0493 | **0.0493** | ✓ |
| m_ν₃ corrected / √Δm²₃₁ | 0.98× | **0.983×** | ✓ |
| m_ν₂ (solar) | 0.99× | unchanged | ✓ |

Scratch arithmetic is clean. The 2/3 lands both legs within ~2% from a single M_R, as claimed.

---

## Numerology guard (√2, π/2 vs 2/3)

The memo's §6 guard is honest: **2/3 is partly selected because it lands**. Adversarial check of near-alternative correction factors on m_ν₃ (same M_R, solar untouched):

| Correction on m_ν₃ | Factor | Corrected m_ν₃ (eV) | Implied ratio | vs obs mid (5.789) |
|--------------------|--------|------------------------|---------------|---------------------|
| **2/3 (Killing/adjoint)** | 0.667 | **0.0493** | **5.720** | **−1.2%** |
| 1/√2 | 0.707 | 0.0523 | 6.068 | +4.8% |
| 2/π | 0.637 | 0.0471 | 5.464 | −5.6% |
| π/2 applied as ratio divisor | — | — | 5.464 | −5.6% |

On the overshoot side (pred/obs ≈ **1.482×**), competing "mistaken multiplier" stories:

| Erroneous factor | Value | Distance from 1.482× |
|------------------|-------|----------------------|
| 3/2 (adjoint/Killing story) | 1.500 | **1.2%** |
| √2 | 1.414 | 4.8% |
| π/2 | 1.571 | 5.7% |

**Finding:** 2/3 is the best single-parameter fit among the named alternatives; fit alone is **not** derivation. The memo states this explicitly — adversarially acceptable honesty.

**Numerology-only gate:** **NOT FAIL.** The pathway carries a named structural object (Killing dim 2 vs adjoint dim 3), a B3 disambiguation payoff, and an internal falsifier that chirality-superposition amplitude alone gives ×1 not 2/3 — i.e. it does not reduce to "pick the number that works." That elevates it above pure curve-fitting, but **does not close** the counting chain.

---

## §6 falsifiers (adversarial status)

| Falsifier | Test | Status | Notes |
|-----------|------|--------|-------|
| **(a)** σ₃ derivation yields ×1 or √(2/3), not 2/3 | Explicit D_F Killing-spinor mass computation | **OPEN — pending AJ-10** | Memo concedes balanced LH⊕RH amplitude → ×1; load rests on normalisation/counting, **not yet computed** |
| **(b)** σ₁/σ₂ escape not derivable | Same construction shows definite modes skip 2/3 | **OPEN** | Stipulated ("not Killing modes"); no shared derivation displayed |
| **(c)** κ₀ (adjoint-3) vs neutrino (Killing-2) split not principled | Principled sector assignment, not post-hoc partition | **OPEN — CONDITIONAL** | Plausible gauge-bridge vs chirality-superposed spinor split; **could be wrong** (memo §6 item 3); if B3 conflation is genuine, pathway fails |
| **(d)** Δm² central values move ratio off 5.7–5.8 | NuFIT stability | **PASS (for now)** | Current band still centres corrected ratio; not a live falsifier trigger |

No falsifier (a)–(c) is resolved. Falsifier (d) does not kill the pathway today.

---

## Structural assessment

**What survives adversarial read:**

1. **Disambiguation framing** — preserving κ₀ = 3/√(4π) while correcting m_ν₃ is non-destructive vs naive B3 "force 3→2 everywhere" (κ → 1.3 catastrophe correctly flagged).
2. **Scope discipline** — memo does not claim closure; lists three explicit derivation gaps; warns against ratification and number-dialing.
3. **Internal tension acknowledged** — chirality superposition alone does not produce 2/3; counting normalisation must be derived or pathway collapses to fit.

**What does not survive closure gate:**

1. **No explicit σ₃ mass as Killing-spinor expectation value** on NTE D_F — the entire correction rests on a ratio-of-dimensions argument, not a displayed integral.
2. **σ₁/σ₂ exemption** is narrative, not derived from the same operator.
3. **"Use 3 for gauge, 2 for neutrino"** is testable but currently **post-hoc partition** until Jammer shows both counts emerge from distinct observables in one spectral-action calculation.

Sub-label on structure: **CONDITIONAL-STRUCTURE** — the Killing/adjoint split is a real hypothesis worth deriving, not numerology-only, but **conditional on AJ-10** delivering items §6(1)–(3).

---

## Verdict matrix

| Gate | Result |
|------|--------|
| Numerology-only? | **NO** → not FAIL-NUMEROLOGY |
| Derivation chain closed? | **NO** → not PASS |
| Structural hook present? | **YES** → CONDITIONAL-STRUCTURE (subordinate) |
| **Primary adversarial sign-off** | **ADVERSARIAL-PENDING-DERIVATION** |

**Do not:** patch corpus with ×2/3; retract B1 atmospheric ≈1.5× language; sign PASS on closure.

**Await:** Jammer **AJ-10** — explicit σ₃-mass-as-Killing-spinor-expectation derivation + σ₁/σ₂ escape + principled κ₀/neutrino sector split.

---

## Routing

| Owner | Action |
|-------|--------|
| **Jammer (AJ-10)** | Deliver §6(1)–(3) derivation chain or report falsifier (a)–(c) trigger |
| **AC** | Hold B1 disposition at honest-scope; candidate input only if AJ-10 PASS |
| **Cursor Main** | Programme pointer already filed (MAIN-14); no corpus patch until derivation PASS + AC ratify |

---

*Cursor Scratch adversarial lane — CR2 PS-12. ADVERSARIAL-PENDING-DERIVATION; Jammer AJ-10 blocks closure.*
