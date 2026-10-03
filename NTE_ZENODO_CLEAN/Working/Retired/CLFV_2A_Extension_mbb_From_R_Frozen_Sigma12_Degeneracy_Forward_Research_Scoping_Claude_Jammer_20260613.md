# CLFV-2A Extension: m_ββ from R-Frozen σ₁/σ₂ Degeneracy — Forward Research Scoping (Claude Jammer)

**From:** Claude Jammer (specialist session)  
**To:** AC (task formalisation authority); Scratch — Claude model (Connes lead, candidate primary derivation owner); Cursor Main (orchestration); Cursor Jammer + Cursor Scratch (potential cross-check lanes)  
**Cc:** Greg, PC  
**Date:** 2026-06-13  
**Priority:** P1 — Greg-directed extension of the ratified CLFV-2A discriminator  
**Re:** `Handoff_AC_to_Scratch_CLFV_Discriminator_RATIFIED_R_Freedom_Frozen_Both_Gates_Met_Qualified_Six_Caveats_20260613.md` (AC ratification 2026-06-13)

---

## §0 — One-line motivation

The CLFV ratio is ratified but **undetectable at NTE's M_R** (BR ~ 4×10⁻⁵⁹; ~46 orders below MEG II). The same R-freezing mechanism that forces tan²θ₂₃ may force a *separately detectable* observable in **neutrinoless double-beta decay (0νββ)** — because m_ββ is set by light-neutrino masses at the electroweak scale, not by the heavy M_R propagator.

This memo scopes the question: **does the σ₁/σ₂ R-freezing force the Majorana phase α relating m_1 and m_2 to a discrete value, yielding a forced m_ββ prediction in the testable next-generation 0νββ range?**

---

## §1 — The structural claim under derivation

**Established (ratified):** The σ₁ = σ₂ real degeneracy + real Z₂ swap symmetry freezes the Casas-Ibarra R-matrix freedom in the heavy 1-2 block to real O(2), which is unphysical. This forces the CLFV amplitude ratio |A(μ→eγ)|² / |A(τ→eγ)|² = tan²θ₂₃.

**Open question:** the *light* neutrino mass matrix in the flavor basis is m_ν = U PMNS · diag(m₁, m₂, m₃) · U_PMNS^T, where m_i are Majorana mass eigenvalues. The eigenvalues m_i carry **two Majorana phases** α (relating m_1 and m_2) and β (relating m_3 to m_1), which are physical and observable in 0νββ but cancel in conventional oscillation experiments.

**The candidate forced relation:**

- σ₁ and σ₂ are real geometric modes with equal real Yukawas — **no relative phase between them in the σ basis**
- The R-freezing argument forbids a *complex* relative rotation in the heavy 1-2 block
- **If "no relative phase between σ₁ and σ₂" propagates through the seesaw mapping to "α = 0 (or π) between m₁ and m₂"**, then α is fixed, not a free Majorana phase
- m_ββ depends on this α; if α is forced, m_ββ is forced (modulo β, which depends on σ₃ and is not constrained by the same mechanism)

The derivation question is whether this propagation holds — whether the R-freezing in the heavy sector genuinely forces the light-sector Majorana phase α, or whether the seesaw mapping introduces freedom that breaks the constraint.

---

## §2 — Order-of-magnitude estimate (illustrative; NOT derived)

With NTE's geometric inputs (m_3 ≈ 0.05 eV from Y_3 = 1 seesaw; m_1 = m_2 ≈ (8π)^(−2/3) m_3 ≈ 6 meV from Y_1 = Y_2 = (8π)^(−1/3) seesaw; normal hierarchy):

$$m_{\beta\beta} = \left| c_{12}^2 c_{13}^2 m_1 + s_{12}^2 c_{13}^2 m_2 e^{i\alpha} + s_{13}^2 m_3 e^{i\beta} \right|$$

If α = 0 forced (R-freezing extends to light-sector phase):
$$m_{\beta\beta} \approx c_{13}^2 m_1 + s_{13}^2 m_3 e^{i\beta}$$

Numerically (c₁₃² ≈ 0.978, s₁₃² ≈ 0.022, m₁ ≈ 6 meV, m₃ ≈ 50 meV):
- β = 0: m_ββ ≈ 5.9 + 1.1 ≈ **7.0 meV**
- β = π: m_ββ ≈ 5.9 − 1.1 ≈ **4.8 meV**
- range: **~5–7 meV**

**Disclaimer:** these numbers are *illustrative*, not derived. The forcing of α is the load-bearing claim that needs explicit derivation. β is not constrained by σ₁/σ₂ degeneracy — it depends on the non-degenerate σ₃ mode and remains free (or constrained by separate σ₃ geometric content not yet examined).

---

## §3 — Why this matters experimentally

**Current and near-term 0νββ sensitivities to m_ββ:**

| Experiment | Sensitivity to m_ββ |
|---|---|
| KamLAND-Zen 2024 | 28–122 meV (matrix-element uncertainty) |
| LEGEND-1000 | ~9–21 meV |
| nEXO | ~6–17 meV |
| Future ton-scale | ~few meV |

**NTE's prospective range ~5–7 meV is at the boundary of nEXO sensitivity and within reach of future ton-scale experiments.** Unlike the CLFV ratio, this is a *near-term testable* prediction if the forcing derivation closes.

The discrimination structure:
- **Generic seesaw:** α and β both free; m_ββ ranges from ~0 (cancellation) to ~50 meV (worst case for NTE input masses)
- **NTE if α forced:** m_ββ in narrow band ~5–7 meV, modulo β

A measured m_ββ outside the predicted band (with future nEXO / ton-scale precision) **falsifies the R-freezing extension to Majorana phases**. A measured m_ββ inside the band is positive (qualified — could be coincidence with generic seesaw at a fitted phase).

---

## §4 — Honest assessment

**Most likely outcomes (with priors):**

1. **R-freezing forces α (most interesting; ~25% prior).** Derivation goes through cleanly; α = 0 or π; m_ββ narrow band; testable at nEXO. This becomes the project's first **near-term testable** ratified discriminator.

2. **R-freezing does NOT force α (most likely; ~50% prior).** The seesaw mapping introduces complex phase freedom in the light-sector Majorana matrix that the heavy-sector R-freezing does not constrain. α remains free; m_ββ remains anywhere from 0 to ~50 meV; no new discriminator beyond CLFV ratio.

3. **R-freezing forces α but m_ββ is degenerate with generic-seesaw expectations (~15% prior).** α is forced but to a value that happens to coincide with what generic seesaw predicts at a typical PMNS configuration. Discrimination odds ~1:1; not useful.

4. **The σ₁/σ₂ degeneracy turns out to lock m_1 = m_2 exactly (~10% prior).** Then |m_1 + m_2 e^{iα}|² = |2 m_1 cos(α/2)|² — and α appears in the amplitude but is not strictly "forced." However, the degeneracy + R-freezing might force the *symmetric* combination, giving cos(α/2) → ±1 (so α = 0 or 2π).

**Outcome 2 is the most likely** — the heavy-sector R-freezing argument is operator-theoretically tight in the 1-2 block, but the seesaw is a many-stage construction (heavy Majorana → see-saw block matrix → diagonalization to light Majorana eigenstates), and Majorana phases of the light sector are not automatically inherited from R-freedom of the heavy sector.

**That said:** outcome 1 has high enough probability and high enough payoff (a near-term testable prediction) that the derivation is worth attempting. Outcomes 2–4 are all ratifiable honest results.

---

## §5 — Proposed task structure

Same architecture as class-2 2A (the ratified parent):

**Phase 1 — primary derivation.** Scratch (Connes lead) derives the seesaw mapping from heavy R-freezing to light Majorana phase α, blind to the m_ββ numerical estimate. Verdict format:
- **α-FORCED-TO-DISCRETE** (with displayed derivation chain; predicted m_ββ value(s))
- **α-NOT-FORCED-BY-R-FREEZING** (with displayed argument; m_ββ remains generic-seesaw-like)
- **NEEDS-MORE** (insufficient to determine)

**Phase 2 — independent verification.** Second independent Scratch session rebuilds the seesaw mapping from first principles, not from the pass-1 propagation argument. Tests whether the result is mechanism-real or pass-1 algebra artifact. Same verdict format.

**Phase 3 — AC ratification.** If both passes converge on α-FORCED with consistent derivation: ratify as *extended NTE prediction*. Add to corpus catalogue with appropriate qualifiers. If pass 2 returns NOT-FORCED or FAIL: bin the extension; CLFV ratio stands alone as the only ratified discriminator from the σ₁/σ₂ mechanism.

**Cursor lane support:**
- **Cursor Jammer:** if α-FORCED, compute m_ββ prediction at NTE's geometric input values (m_1 = m_2 ≈ 6 meV; m_3 ≈ 50 meV; standard PMNS NuFIT 5.3 NO). Histogram against anarchic-seesaw m_ββ distribution to give discrimination odds.
- **Cursor Scratch:** if α-FORCED, verify the result is robust to NuFIT central-value uncertainties and to matrix-element uncertainties in m_ββ extraction.

---

## §6 — Discipline (binding from established pattern)

- **NO number-dialing** — derivation must run heavy R-freezing → light Majorana phase α → m_ββ prediction; never use observed m_ββ bounds or generic predictions as inputs
- **NO smuggling** standard PMNS parameters into the derivation in a way that engineers the result
- **"R-freezing does NOT force α"** is a ratifiable honest result; **the m_ββ extension being null is the most likely outcome** and is fully acceptable
- **Same six-qualifier discipline as parent CLFV ratification** — any forced result must travel with appropriate caveats (single relation; conditional on observing 0νββ; matrix-element uncertainty; PMNS-dependent floor; tested band; intrinsic width)
- **Adversarial convergence required** — two independent Scratch passes + AC ratify before any external use
- **No corpus patch** from this scoping
- **Canonical bilateral / mirror / Janus discipline throughout**
- **Pre-ship grep applies** if results reach publication-bound material

---

## §7 — Awaits AC

This is a proposal. AC formal task issuance is the next step — same architecture as class-2 2A. If AC fires:

- Phase 1 to Scratch (Connes lead); deliverable `Handoffs/Handoff_Scratch_to_AC_CLFV_2A_Extension_mbb_Pass1_YYYYMMDD.md`
- Phase 2 to independent Scratch session; deliverable `Handoffs/Handoff_Scratch_Independent_Pass2_mbb_alpha_Forced_or_Not_YYYYMMDD.md`
- Cursor support as scoped above

If AC modifies the scoping or rejects: the memo is exploratory only and stands as historical.

---

— Claude Jammer (specialist session, CLFV-2A extension forward research scoping), 2026-06-13.
