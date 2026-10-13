# §6 — BFT production with NTE's geometric heavy mass — VERDICT (Claude Jammer)

**Date:** 2026-10-14
**Commission:** `Handoffs\DISPATCH_AC_Cursor_GO_Five_Answers_Plus_Jammer_Section6_Commissioned_Plus_Ninth_Propagation_Failure_20261014.md` §3 (Greg's GO, 23:18 NZDT: *"just to get an early look"*).
**Pre-registration:** §6 of `Working\DarkMatter_Rebuild_Candidates_From_An_NTE_Perspective_What_Does_Not_Work_And_Why_Plus_BFT_Z2_Stable_RH_Neutrino_As_Starting_Point_Preregistered_Next_Computation_Claude_Jammer_20261014.md`. Forks A-1…A-4 and the kill rules were filed **before** I read BFT's abundance formula. My prior was A-3 or A-4, and AC's was the same.
**Register:** an early look at Stage 4 material. **Nothing enters Core or the closure record.** No f.

**Sources read this session:**
- **BFT, PRL companion, arXiv:1803.08928.** The abundance estimate was fetched and quoted verbatim below.
- **BFT, long paper, arXiv:1803.08930.** Abstract and §1–§4.2 fetched. Its §5.1 (the precise calculation) **could not be retrieved**: the text extraction truncates at §4.2.2, and the sandbox's direct download was refused.
- **NTE Companion 10** (M₁; read 2026-10-12, unchanged since).

---

## BFT's abundance (arXiv:1803.08928, verbatim)
- The dark-matter neutrino obeys (i∂̸ − μ)N₁ = 0 with μ = γτ when a ∝ τ, where *"γ = (m_dm/m_pl)√ρ₁ … m_pl = (8πG/3)^{−1/2} ≈ 4 × 10¹⁸ GeV … ρ₁ = a⁴ρ … is a constant."*
- *"n_dm ∼ (2πa)⁻³ γ^{3/2} ∼ (2π)⁻³ (m_dm/m_pl)^{3/2} ρ^{3/4}, where ρ^{3/4} ∼ s"*. The ratio n/s is conserved and matched to today, with s₀ ∼ 2.3 × 10⁻³⁸ GeV³ and ρ_dm,0 ∼ 9.7 × 10⁻⁴⁸ GeV⁴.
- *"Thus, we estimate m_dm ∼ [(ρ_dm,0/s₀)(2π)³ m_pl^{3/2}]^{2/5} ≈ few × 10⁸ GeV. A more precise calculation [2] yields m_dm = 4.8 × 10⁸ GeV."*

**Consequence:** n/s ∝ m^{3/2}, so **Ω_dm ∝ m · n/s ∝ m^{5/2}**.

*Assumption, stated:* I take the m^{5/2} scaling from BFT's own estimate. The precise calculation in their companion paper (unread) is assumed to change the prefactor, not the power.

## Computation (script run this session)
- **BFT's estimate, reproduced from the quoted inputs: m ≈ 2.34 × 10⁸ GeV.** That matches "few × 10⁸". BFT's precise value is 4.8 × 10⁸ GeV.
- **NTE's masses (C10):** M₁ = (8π)^{1/3}(M_Pl²H_GB)^{1/3} ≈ 5.4 × 10⁹ GeV; M₂ ≈ M₁(1 + sin²θ₁₃); M_R ≈ 8.2 × 10¹⁴ GeV (pathway only).

| Stable state | m / 4.8 × 10⁸ | **Ω_pred / Ω_obs** (normalised to BFT precise) | Ω_pred / Ω_obs (normalised to BFT estimate) |
|---|---|---|---|
| N₁ (M₁) | 11.2 | **≈ 425** | ≈ 2.6 × 10³ |
| N₂ (M₂) | 11.5 | **≈ 446** | ≈ 2.7 × 10³ |
| N₃ (M_R) | 1.7 × 10⁶ | ≈ 4 × 10¹⁵ | ≈ 2 × 10¹⁶ |

For comparison, A-1 needed agreement within the residue NTE already carries on M₁ (a mass factor of about 1.12, so Ω within about 1.33).

## Landing: **A-3, conditional on A-4**
- **A-4 holds first.** The computation exists **only on BFT's background**: a ∝ τ continued through τ = 0, and the CPT-invariant in/out-vacuum offset. NTE's own beginning, a no-boundary handover at ȧ = 0, gives no production formula, and it is the obstruction that blocks NTE's origin sector anyway. So this is **"NTE's mass on BFT's universe"**, not an NTE computation.
- **On that background, A-3.** NTE's geometric heavy mass **overproduces dark matter by a factor of roughly 400 to 2,600**, depending on whether BFT's precise or estimated normalisation is used. Either way it is more than two orders of magnitude. **NTE's heavy-mass geometry is not the dark-matter mass.**
- **"Is the factor ≈ 11 doing the work?"** (AC's constraint c). It does the opposite. Because Ω ∝ m^{5/2}, a factor of 11 in mass becomes about 400 in abundance. The near-coincidence in mass hides a large miss in the observable.

**Kill rules, checked:**
- **No choice of stable state after the fact:** all three were computed and all miss.
- **No O(1) correction invoked:** none can close it. A-1 would need the mass shifted down by a factor of about 11, and C10's own residue points the other way (M₁ already sits about 1.12 *below* the leptogenesis value of ≈ 6.1 × 10⁹).
- **No tuned input:** none was used.

## In kind, for the "what doesn't work" list
**A geometrically fixed heavy-neutrino mass and BFT's gravitational production cannot both hold with the observed abundance.**
- Production scales as m^{5/2}, so the dark-matter mass is pinned to within a few tens of percent by Ω_dm.
- NTE's flux-quantised M₁/M₂ sit an order of magnitude above that.
- **Would reopen if:** a deposited NTE mass scale lands near 4.8 × 10⁸ GeV for a reason that does not look at Ω_dm. **None exists.** Rescaling the C10 construction to reach it would be fitting.

## What this leaves for the rebuild
- **Candidate 1 (BFT) stays at rank 1, adopted and credited with BFT's own mass.** That mass is fixed *inside BFT* by the abundance; it is not an NTE prediction.
- Its sharp test survives unchanged: **one exactly massless light neutrino.** So does its cost: adopting BFT's CPT pair and radiation bang instead of NTE's CPN pair and no-boundary handover.
- **Seesaw bookkeeping, if adopted:** a fourth, BFT-mass singlet would be **new content**. Repurposing N₁ or N₂ at their NTE masses is excluded by this computation.

## Score against the pre-registration
- **Prior A-3 or A-4; landed A-3 conditional on A-4.**
- **Not anticipated:** how steep the scaling is (m^{5/2}). The miss is about 400×, not "an order of magnitude".

No f. Nothing patched. Not a route to κ or κ₀.

— Claude Jammer, 2026-10-14.
