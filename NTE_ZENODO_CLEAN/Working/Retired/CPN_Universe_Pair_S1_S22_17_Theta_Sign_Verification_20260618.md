# §22.17 Θ-sign verification — S_bridge sign-consistency under the Hopf-charge flip (closes the item routed from the CPN-S1 Hopf determination)

**From:** AC-assessment (verification against primary §22.17 text)
**To:** AC (gate), Scratch; Cc: Greg, Jammer
**Date:** 2026-06-18
**Re:** The one verification item flagged in `CPN_Universe_Pair_S1_Hopf_Orientation_under_N_Scratch_Determination_20260618` §4 — explicit §22.17 Θ-sign / S_bridge sign-consistency under H(+N) = −H(−N). Read from **primary** Part 3 §22.17 (`NTE_v10_17_Part3_Accounting__C_S22_App.md`), not the handoff transcription.

---

## §0 — Result
**CONFIRMED sign-consistent. κ = κ₀/(1−κ₀) = 5.50 is robust under the Hopf monopole-charge flip.** Every factor of S_bridge is CPN-**even**; the charge-odd structure (monopole-charge sign, matter/antimatter) lives in the baryogenesis sector and does **not** enter the gravitational cross-thickness coupling. **One correction to the Scratch determination is required** (Θ identity — see §3); the conclusion is unchanged and in fact strengthened.

## §1 — The primary §22.17 form (verbatim structure)
The Janus action is S = S_grav + S_SM + S_ν + S_bridge + S_cons, with:

**S_bridge** = κ₀ ∫∫ √(−g₊)√(−g₋) · 𝒦(x,y) · g₊^{αβ} g₋^{ρσ} T_{αβ}^{(b,+)} T_{ρσ}^{(b,−)}, with κ₀ = 3/√(4π) and **𝒦 = Y₀₀·Θ** (Hopf monopole × **neutrino-bridge Green function**).

**S_cons** = Lagrange multipliers enforcing T̃_μν^(σ) = T_μν^(b,σ) + T_μν^(ν) + **κ₀ T̃_μν^(−σ)**; matrix inversion of these constraints **is** the geometric resummation κ₀/(1−κ₀) (§9.3). Also recorded: the crystallisation-shell fibre term 𝓘_fibre = κ₀ Y₀₀ with **λ_Hopf = 1** (coefficient match to the monopole sector of S_bridge) — i.e. the monopole-sector coupling enters with coefficient **+1**.

(Note: the handoff's transcription compressed this to "κ₀∫∫√(−g₊)√(−g₋)𝒦 T₊T₋, 𝒦 = Y₀₀·Θ" and omitted the metric contractions and the (b,±) stress-tensor structure. The full form is above.)

## §2 — Sign analysis under H(+N) = −H(−N) (the CPN deck transformation, + ↔ − orientations)
Factor by factor:
- **κ₀ = 3/√(4π):** positive constant (representation dimension × L²-norm); CPN-**even**. (Established in the Hopf determination §3.)
- **√(−g₊), √(−g₋):** metric-determinant volume factors, positive; the pair is symmetric under + ↔ −; CPN-**even**.
- **Y₀₀ = 1/√(4π):** the s-wave monopole **amplitude** (L²-norm of the constant harmonic), positive; CPN-**even**. The monopole **charge** (Chern/Hopf number) flips sign under the deck transformation (Reading X), but the *charge sign* does not appear in S_bridge — only its s-wave **amplitude** Y₀₀ does. This is the κ₀ topological-protection result (⟨ψ|Y₀₀|ψ⟩ depends only on ‖ψ‖²) at action level.
- **Θ = neutrino-bridge Green function:** the propagator of the **Z₂-even** unresolved neutrino across the thickness (§6.3, §8.7.9). A Z₂-even field's bridge Green function is symmetric under the + ↔ − deck swap; CPN-**even**.
- **g₊^{αβ} g₋^{ρσ} T_{αβ}^{(b,+)} T_{ρσ}^{(b,−)}:** inverse metrics are even; the stress-energy tensors T^{(b,±)} are **quadratic/bilinear in the matter fields**, hence **C-even** (T_{μν} is a real bilinear — e.g. ψ̄Γ_{(μ}∂_{ν)}ψ or F_{μα}F_ν{}^α — invariant under charge conjugation). So although the two orientations are matter vs antimatter (opposite charge), their stress tensors couple with the **same sign**; the contraction is CPN-**even**.

**Net: S_bridge → +S_bridge under the flip. Sign-consistent.** No relative minus is introduced.

## §3 — Required correction to the Scratch determination (§4)
The Scratch determination §4 stated "**Θ is the reflection relating the two faces**" (conflating it with the Wick/reflection operator Θ of C5, CPT = Θ∘CPN). **Primary §22.17 is explicit that Θ here is the *neutrino-bridge Green function*, not the reflection operator.** These are two different objects sharing the glyph Θ:
- **Θ (C5):** the Wick/reflection (antilinear) operator in CPT = Θ∘CPN.
- **Θ (§22.17, in 𝒦 = Y₀₀·Θ):** the Z₂-even neutrino's cross-thickness Green function.

The sign-consistency conclusion is **unchanged and strengthened**: it does not rely on "Θ carrying the reflection." It holds because **every** factor — including the §22.17 Θ (a Z₂-even neutrino propagator) and the stress tensors (C-even because quadratic in fields) — is CPN-even. **Action for AC:** correct §4 of `…Hopf_Orientation_under_N_Scratch_Determination…` (Θ = neutrino-bridge Green function; sign-consistency holds via all-even factors, not via a reflection). This is exactly the self-report-vs-primary-text discrepancy the standing discipline targets — caught by reading §22.17 rather than the transcription.

## §4 — κ = 5.50 closure sign-robustness (the load-bearing check)
S_cons gives the cross-orientation constraint T̃^(σ) = T^(b,σ) + T^(ν) + **κ₀ T̃^(−σ)** — each orientation's effective stress-energy receives **+κ₀** times the other's. Iterating yields the geometric series **κ₀ + κ₀² + κ₀³ + … = κ₀/(1−κ₀)** = 0.846/0.154 = **5.50**. Sign-robustness turns on the cross term being **+κ₀**:
- If the Hopf-charge flip injected a relative minus (cross term → −κ₀), the series would alternate: κ₀ − κ₀² + … = κ₀/(1+κ₀) = 0.458 — **not** 5.50.
- It does **not**, because the cross-coupling is mediated by the C-even, all-even S_bridge (§2): the registration is through **stress-energy** (mass/energy), not through the charge-odd monopole number. Hence the cross term is **+κ₀**, the series sums to **+5.50**, confirmed.

**Physical statement (clean):** antimatter has positive energy and gravitates like matter, so the gravitational cross-thickness registration is **charge-blind** — the two orientations register across the thickness with the same sign regardless of the matter/antimatter flip. κ (a DM:baryon **mass-energy** ratio) is therefore robust under a flip that lives entirely in the **charge** sector. The flip sources **baryogenesis** (charge-odd); κ is sourced by **mass-energy** (charge-even). They are cleanly separated — the same odd-charge / even-modulus split noted in the Hopf determination §3, now confirmed at the action level of §22.17.

## §5 — Verdict + routing
1. **S_bridge is sign-consistent (CPN-even) under H(+N) = −H(−N).** Verified against primary §22.17, all factors even.
2. **κ = κ₀/(1−κ₀) = 5.50 is sign-robust** — the constraint sector's cross term is +κ₀ (geometric series, not alternating), because the coupling is C-even stress-energy, not charge.
3. **Correction logged:** §22.17 Θ = neutrino-bridge Green function (not the C5 reflection operator); update Scratch determination §4 accordingly (conclusion unchanged).
4. **Closes** the §4 verification item from the Hopf determination. **No corpus patch** beyond the (optional, AC-gated) §6.6 entailment note already proposed in the Hopf determination, now with a clean §22.17 cross-ref: "S_bridge is CPN-even; the Hopf-charge flip is confined to the baryogenesis sector and leaves κ = 5.50 invariant."

— AC-assessment, 2026-06-18. §22.17 read from primary text; S_bridge sign-consistent under the Hopf-charge flip; κ = 5.50 robust; one Θ-identity correction to the Scratch determination logged. Routed to AC for gating; corpus untouched pending authorization.
