# Candidate pathway: resolving the ≈1.5× neutrino atmospheric-leg discrepancy via the chirality-superposed σ₃ mode (Killing-spinor count 2, not adjoint 3)

**From:** Scratch — Claude model (Connes Programme lead)
**To:** AC (B1 disposition), Jammer (B3 + neutrino sector)
**Cc:** Greg
**Date:** 2026-06-01
**Status:** CANDIDATE pathway — structurally motivated, lands both legs, but **not a closed derivation.** Honest scope in §6. Do not ratify as closed; adversarial cross-check welcome.
**Authority:** Greg directive — find a corpus-internal pathway that resolves the 1.5× using the chirality-superposition nature of the unresolved neutrino.
**Constraint:** Drive writes down this session; local for persistence.

---

## §1 — The discrepancy, precisely

The corpus predicts a **ratio** fixed independently of M_R (Companion 13 / S2 §8.3):

$$m_{\nu_3} = \frac{v^2}{M_R}\ (\sigma_3),\qquad m_{\nu_2} = (8\pi)^{-2/3}\frac{v^2}{M_R}\ (\sigma_1/\sigma_2)\ \Rightarrow\ \frac{m_{\nu_3}}{m_{\nu_2}} = (8\pi)^{2/3} = 8.574.$$

Observed (NuFIT 6.0; Δm²₂₁ ≈ 7.4×10⁻⁵, Δm²₃₁ ≈ 2.45–2.51×10⁻³ eV², NO, m₁≈0):

$$\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.72\text{–}5.82.$$

The prediction is **≈ 1.47–1.50× too large** — the same factor whichever leg you anchor. Anchoring solar (clean): v²/M_R = m_ν₂·(8π)^(2/3) = 0.00862 × 8.574 = 0.0739 eV ⇒ M_R = 8.2×10¹⁴ GeV (corpus value ✓), and then naive m_ν₃ = 0.0739 eV = **1.47× the atmospheric** 0.0501 eV. This is exactly the B1-confirmed honest position: **solar sub-1%, atmospheric structural at ≈1.5×.**

## §2 — The clean missing factor is 2/3

$$\boxed{\ \tfrac{2}{3}\,(8\pi)^{2/3} = 0.6667 \times 8.574 = 5.716\ }\approx \sqrt{\Delta m^2_{31}/\Delta m^2_{21}}.$$

Equivalently, the atmospheric leg needs **m_ν₃ → (2/3)·v²/M_R**, with m_ν₂ untouched (so solar stays clean). Quantitatively, from the *same* M_R that fixes solar:

| leg | naive | corrected (×2/3 on σ₃) | observed | corrected/obs |
|-----|-------|------------------------|----------|---------------|
| m_ν₂ (solar, σ₁σ₂) | 0.00862 | 0.00862 | 0.00862 | **0.99×** |
| m_ν₃ (atm, σ₃) | 0.0739 | **0.0493** | 0.0501 | **0.98×** |

Both legs land within ~2% from a single M_R. Σm_ν improves to ≈ 0.058 eV (was 0.082), comfortably under the cosmological bound.

The factor 2/3 must not be merely fitted. The claim of this memo is that it has a **specific structural origin** in the chirality-superposition ontology — and that the origin is the *same* 2-vs-3 count B3 is fighting over.

## §3 — The pathway: the σ₃ neutrino is a chirality-superposed mode, and its mass scale is set by the **Killing-spinor** count (2), not the **adjoint** count (3)

Greg's hint is the key: the unresolved neutrino is **neither LH nor RH — a superposed chirality, and yet both** (Companion 7a). In the corpus σ-mode ontology (S2 §8.3): σ₃-aligned = strongly Higgs-VEV coupled = m_ν₃; σ₁/σ₂ = Higgs-orthogonal = m_ν₂. The σ₃ mode is precisely *the* chirality-superposed state.

Proposed structural reading:
- The σ₃ neutrino, being a coherent LH⊕RH superposition tied to the S³ geometry, is a **Killing-spinor mode**. The dimension of the space of fixed-sign Killing spinors on the round S³ is **2** (Bär 1993; S³ carries 2^{⌊3/2⌋} = 2 Killing spinors per sign).
- The naive m_ν₃ = v²/M_R implicitly normalised the σ₃ coupling over the **3 adjoint su(2) channels** — i.e. it imported the *same* "×3 = dim adj su(2)" that enters κ₀ = 3/√(4π) (and that B3 is questioning).
- But the chirality-superposed σ₃ mode does not live in the adjoint-3 space; it lives in the **Killing-2** space. Re-normalising the σ₃ coupling from the adjoint count (3) to the Killing count (2) multiplies m_ν₃ by **2/3**.
- σ₁/σ₂ are the *definite*, Higgs-orthogonal modes — not the chirality-superposed Killing mode — so they retain their (8π)^(−2/3) flux suppression and **do not** pick up the 2/3. Hence only the ratio's σ₃ leg moves.

Result: m_ν₃/m_ν₂ → (2/3)(8π)^(2/3) = 5.72. Solar clean, atmospheric fixed.

## §4 — The structural payoff: this **disambiguates B3** rather than breaking κ₀

B3's charge is that the corpus conflates the **2-dim** fixed-sign Killing-spinor space with the **3-dim** adjoint su(2) used in κ₀ = 3/√(4π). Naively "resolving" B3 by forcing κ₀'s 3→2 would be catastrophic — κ₀ → 2/√(4π) = 0.56, κ = κ₀/(1−κ₀) → 1.3, destroying the dark-matter ratio κ = 5.50.

This pathway offers the opposite, non-destructive resolution: **the 2 and the 3 are different objects entering different observables, and each uses the correct one.**
- **κ₀** is a *gauge-sector bridge* coupling — the adjoint su(2) (3 directions) is its correct home. κ₀ = 3/√(4π), κ = 5.50 **preserved**.
- **m_ν₃** is a *chirality-superposed spinor* mode — the fixed-sign Killing space (2 dim) is its correct home.
- The **≈1.5× neutrino discrepancy is the empirical fingerprint** that the neutrino leg had mistakenly imported the adjoint-3 count where the Killing-2 belonged.

If this holds, one structural insight resolves **two P0 blockers at once** (B1 atmospheric + B3 conflation) while leaving κ untouched — a strong indicator the 2/3 is structural, not coincidental.

## §5 — What is and isn't disturbed

- **M₁ = (8π)^{1/3}(M_Pl² H_GB)^{1/3}** (Pathway α): untouched — its (8π) is Majorana-doubled *flux quantisation*, a different object from the σ₃ channel count.
- **m_ν₂ / solar**: untouched (the whole point) — stays at 0.99×.
- **κ₀ = 3/√(4π), κ = 5.50**: preserved.
- **M_R = 8.2×10¹⁴**: unchanged; the fix is a coupling re-count on the σ₃ leg, not a rescale of M_R.

## §6 — Honest scope (this is a candidate, not a closure)

**What lands:** the number — (2/3)(8π)^(2/3) = 5.72 puts both legs within ~2% from a single M_R; and the 2/3 has a named structural source (Killing-2 vs adjoint-3) that *also* defuses B3.

**What is NOT yet derived (required to close):**
1. **The 2/3 itself must be derived, not asserted.** I have *motivated* it (Killing dim 2 / adjoint dim 3) but not shown it falls out of an explicit computation of the σ₃ neutrino mass as a Killing-spinor expectation value on the NTE D_F. Note: a naive *chirality-superposition amplitude* argument gives ×1 (a balanced LH⊕RH superposition maximises the off-diagonal Dirac coupling), **not** 2/3 — so the factor rests on the **counting/normalisation** (which spinor space the σ₃ mode's coupling is normalised over), with the chirality-superposition being the *reason* the Killing space is the right home. That chain must be made explicit.
2. **Why σ₁/σ₂ escape the 2/3** must be shown from the same construction (they are not Killing modes), not just stipulated.
3. **The κ₀↔neutrino separation must be principled**, not "use 3 where you need 3, 2 where you need 2." The principle offered (gauge-bridge adjoint vs chirality-superposed Killing) is plausible and testable, but it is the load-bearing claim and could be wrong.

**Numerology guard:** 3/2 is selected partly *because* it lands the number; other near factors (√2 = 1.41, π/2 = 1.57) fit worse, which favours 3/2, but fit alone is not derivation. The B3/Killing-spinor structural motivation is what — *if derived* — elevates this above curve-fitting.

**Falsifiers:** the pathway fails if (a) the explicit σ₃-mass derivation yields ×1 or √(2/3) rather than 2/3; (b) the σ₁σ₂-escape can't be derived from the same structure; (c) the κ₀ (adjoint-3) vs neutrino (Killing-2) separation cannot be made principled, i.e. B3's conflation is genuine and one of the two counts is simply wrong; (d) updated Δm² central values move the observed ratio off 5.7–5.8.

## §7 — Routing

- **Jammer:** this is the natural companion to your B3 work. If you take B3, this pathway predicts B3 resolves *by disambiguation* (adjoint-3 for κ₀ stays; Killing-2 is a separate object) rather than by changing κ₀. The explicit σ₃-mass-as-Killing-spinor-expectation derivation is the deliverable that would close it.
- **AC:** candidate input to B1 disposition — if it closes, the atmospheric leg moves from "structural ≈1.5×" to "≈0.98× via Killing-count correction," and B1's retraction can be paired with a forward pathway rather than left as a bare miss.
- **Discipline:** do **not** ratify as closed; do **not** number-dial the 2/3. It is a lead with a real structural hook, offered for derivation and adversarial test.

— **Scratch (Claude model)**, Connes Programme lead, 2026-06-01. Candidate: σ₃ neutrino as chirality-superposed Killing-spinor mode (dim 2) vs naive adjoint count (dim 3) ⇒ m_ν₃ ×(2/3) ⇒ ratio (2/3)(8π)^(2/3) = 5.72 ≈ observed; solar untouched; κ₀ preserved; disambiguates B3. Needs explicit derivation — not closed.
