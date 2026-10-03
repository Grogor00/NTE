# NTE Provenance Audit — new vs re-derived vs imported (first comprehensive pass)

**Author:** AC · **Date:** 2026-06-22 · **Status:** internal working ledger (Working/). First pass; web-verified items marked [WEB ✓]; others from corpus reading + standard knowledge, marked [CHECK] where a deeper prior-art search is still owed.

**Purpose.** Per Greg's directive, classify every NTE claim against external prior art so the genuinely new content is separated from re-derivations and imports. Triggered by the F1 catch: the a₄-vanishing-on-S³×S¹ result was presented as fresh in two papers built this session, when it is Chamseddine–Connes 2008.

**Classification scheme.**
- **IMPORTED** — established external result, used as-is (cite, don't claim).
- **RE-DERIVED** — known result reached by an NTE route; not novel (credit prior art, frame route as the only increment).
- **NEW-ID** — NTE-specific identification/application of standard ingredients; novel as a claim, built on standard pieces.
- **NEW-DER** — genuinely original derivation within NTE.
- **OPEN** — not derived; conjecture or cross-check.

---

## A. Spectral-action / geometry

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| a₄ vanishes on S³×S¹ (F1) | **Chamseddine–Connes 2008** (arXiv:0812.0165) compute a₄=0 on S³×S¹, a₄≠0 on S⁴; **Mistry–Pinzul–Rachwał 2020** generalise [WEB ✓ + S1 v0.4 AC-ratified] | **IMPORTED** | explicit factorisation d(d−1)(d−3)(5d+2); product-of-spheres framing — "trivial" per AC's own S1 ruling |
| Heat-kernel a₀/a₂/a₄ machinery | Gilkey 1984; Vassilevich 2003; CC spectral action | **IMPORTED** | application to the specific S³×S¹×(𝕆⊕𝕆) substrate |
| κ₀ = 3/√(4π) (Hopf monopole projection) | 3 = dim adj su(2), Y₀₀=1/√(4π) standard; factor 3 anchored to Sonner–Tong 2009 | **NEW-ID** | the specific identification of κ₀ as 3×Y₀₀ on the Hopf base [CHECK: is 3/√(4π) as a coupling in any prior art?] |
| κ = κ₀/(1−κ₀) = 5.506 (idempotent closure) | x/(1−x) resummation = Dyson/RPA, Clausius–Mossotti, Neumann resolvent (paper credits these) | **NEW-ID** | applying the standard resummation to κ₀ via G=1 idempotency |
| a₄=0 ⇒ no R²/Starobinsky term on untwisted substrate | follows from CC 2008 | **IMPORTED** | — |

## B. Cosmology — dark sector, Λ

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| Ω_DM/Ω_b = κ₀/(1−κ₀) ≈ 5.5 | two-metric / bimetric cosmology (Hassan–Rosen; Petit "Janus"); DM-baryon coincidence problem long-known | **NEW-ID** | identifying the ratio with a cross-sector coupling fixed point (framework-dependent) |
| Λ structural cancellation (unimodular) | unimodular gravity (Weinberg; CC spectral-triple unimodular) | **IMPORTED** (mechanism) | the a₄-dependent *number* was retired this session — structural mechanism stands |
| T_GB = M_Pl/√(2π) | — | **NEW-ID / OPEN** | operator-setup value [CHECK] |

## C. Neutrino sector

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| θ₂₃ = π/4 from 2–3 (μ–τ) Z₂ | **Lam 2001; Harrison–Perkins–Scott 2002; Mohapatra–Nishiura 2001; Grimus–Lavoura** [WEB ✓] | **RE-DERIVED** | none at the angle level; credited |
| CLFV ratio \|A(μ→eγ)\|²/\|A(τ→eγ)\|² = tan²θ₂₃ | CLFV-ratio-as-discriminator is established: **Mohapatra et al. hep-ph/0211068** (B(μ→eγ)/B(τ→μγ) as seesaw probe); μ–τ-symmetric LFV literature (Joshipura–Rindani; SUSY SO(10)) [WEB ✓] | **NEW-ID** | the *clean amplitude-level* tan²θ₂₃ from R-matrix freezing (σ₁=σ₂ + real Z₂ → O(2,ℂ)→O(2)); increment on a crowded field |
| m(ν₃)/m(ν₂) = (flux)^(2/3), two branches (P5) | type-I seesaw standard | **NEW-ID** | Hopf-flux quantisation of the Yukawa (framework-specific); honest two-branch, magnitude free |
| M₁ = (8π)^(1/3)(M_Pl²H_GB)^(1/3); M_R ≈ 8.2×10¹⁴ | seesaw scales standard | **NEW-ID / OPEN** | the (8π)^(1/3) prefactor; cross-checks not derivations |

## D. Octonions / Standard Model

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| G₂ = Aut(𝕆) ⊃ SU(3) via stabiliser of e₁ ∈ Im(𝕆) | **Günaydin–Gürsey 1973; Dixon 1994; Furey 2014/2018; Dubois-Violette 2016; Todorov–Dubois-Violette 2018; Baez** — large active field, Perimeter 2021 workshop [WEB ✓] | **IMPORTED** | — |
| SM gauge group from 𝕆 / J₃(𝕆) | Todorov–Dubois-Violette 2018 (SM group = intersection of two maximal subgroups of F₄) [WEB ✓] | **IMPORTED** | — |
| Three generations + species count from J₃(𝕆) | Furey 2014 "Generations"; Todorov–Dubois-Violette [WEB ✓] | **IMPORTED** | the Majorana reduction to 90 + cross-consistency with the dark-sector Majorana condition (small) |
| **Associativity transition** (no time ⇒ non-associative ⇒ 𝕆; gauge birth = onset of associativity ⇒ 𝕆→ℍ) | — | **NEW-DER** | the cosmological *reading* of the division-algebra cascade — the genuine NTE contribution in this domain [CHECK for prior musings] |
| Cayley–Dickson ↔ cosmic epochs (𝕆→ℍ→ℂ→ℝ ↔ pre-temporal→gauge-birth→EWSB→classical) | — | **NEW-ID** | NTE mapping [CHECK] |

## E. Foundations (Companion papers)

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| Born rule = complex Hopf fibration S³→S² | Hopf/Bloch-sphere qubit geometry (Mosseri–Dandoloff 2001) [CHECK] | **RE-DERIVED?** | the gauge-birth activation framing [CHECK — likely known geometry] |
| Quantisation = compactness (discrete spectrum ⇐ compact manifold) | standard spectral theory; HO-via-Heisenberg-algebra standard | **IMPORTED** | the "compactness" framing |
| Hierarchy problem = resonance (β=1) (Companion 4) | — | **NEW-ID / [CHECK]** | classical-level resonance reading; radiative stability open |
| Entanglement as single-object geometry (Companion 1) | — | **[CHECK]** | — |

## F. Core thesis

| Claim | Prior art | Class | NTE increment |
|---|---|---|---|
| N fundamental, t emergent, t = iΔN | emergent/timeless time: Page–Wootters; **Connes–Rovelli thermal time** 1994; Barbour; Wick rotation standard | **NEW-DER** (in crowded space) | the specific N-as-fundamental-coordinate architecture with t = iΔN on the S³×S¹ bilateral substrate; must situate vs thermal-time + Page–Wootters [CHECK] |
| Bilateral S³×S¹ CPN-conjugate substrate | bimetric/two-sector (Hassan–Rosen; Petit) | **NEW-ID** | the specific CPN-conjugate construction |

---

## Genuinely new (the honest shortlist)

1. **The core thesis** — N fundamental / t = iΔN on a bilateral S³×S¹ CPN-conjugate substrate (NEW-DER, but in the crowded emergent-time field; must be situated against thermal-time / Page–Wootters).
2. **The associativity-transition reading** of the (otherwise imported) octonion→SM cascade (NEW-DER).
3. **A set of NTE-specific identifications** built on standard ingredients: κ₀ = 3/√(4π) and its closure κ₀/(1−κ₀); the DM-ratio fixed point; the Hopf-flux two-branch neutrino mass ratio; the clean CLFV amplitude ratio tan²θ₂₃ from R-freezing.

Everything else is **imported** (octonion SM, a₄ vanishing, heat-kernel machinery, unimodular Λ mechanism) or **re-derived** (θ₂₃=π/4, likely the Born-rule–Hopf geometry).

## Prior-art gaps to fix (introduced or inherited)

- **F1 clean paper** — credit CC 2008 + MPR 2020; reframe contribution to the trivial factorisation + framing; it may not stand as a standalone. *(caught this session)*
- **Heat-kernel paper** — a₄=0 must credit CC 2008, not present as fresh. *(caught this session)*
- **κ₀ paper** — verify 3/√(4π) is not a coupling already named in prior art. [CHECK]
- **P4** — credit the μ–τ-LFV / CLFV-ratio literature (Mohapatra hep-ph/0211068; Joshipura–Rindani) as the field the tan²θ₂₃ ratio increments.
- **Octonion paper** — already credits the field; verify the associativity-transition reading has no prior claimant. [CHECK]
- **Born-rule / Companion papers** — owed a prior-art pass (Mosseri–Dandoloff for Hopf-qubit; etc.).

## Method caveats

First pass. [WEB ✓] items verified against live literature this session (octonion-SM field; θ₂₃ priors; CLFV-ratio field; CC 2008 a₄ via S1). [CHECK] items rest on corpus reading + standard knowledge and are owed a dedicated prior-art search. The Companion-paper foundations (1–8) and the cosmology sector (n_s/r, T_GB) need a deeper pass than this first sweep gave them.
