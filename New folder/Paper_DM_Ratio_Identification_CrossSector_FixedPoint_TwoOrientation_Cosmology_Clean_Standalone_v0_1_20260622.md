---
title: "A structural identification of the dark-matter-to-baryon ratio as a cross-sector coupling fixed point in two-orientation cosmology"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-22 (v0.1 pre-submission draft)"
---

*Part of NTE Corpus v10.18.0 (deposited 2026-06).*

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

## Abstract

The cosmological dark-matter-to-baryon ratio Ω_DM/Ω_b ≈ 5.36 (Planck 2018) is one of the few dimensionless numbers in cosmology with no accepted first-principles value. We present a structural identification of this ratio with a cross-sector gravitational coupling in a two-orientation cosmological model, and show that, given two inputs established in companion notes, the ratio takes the parameter-free value κ = κ₀/(1−κ₀) ≈ 5.506. The two inputs are (i) a bare cross-sector coupling κ₀ = 3/√(4π) ≈ 0.846, a structural identity on the unit Hopf bundle [1], and (ii) a derived fixed-point closure κ = κ₀/(1−κ₀), which follows from the idempotency of the s-wave monopole projector mediating the coupling [2]. The identification is conditional and framework-dependent: *if* the apparent dark sector in one orientation is the gravitational echo of the conjugate orientation's total stress-energy, mediated by a bilinear cross-sector bridge and regularised by a self-consistency constraint, *then* the dark-to-baryon ratio is the fixed point κ₀/(1−κ₀). We state the resulting numerical agreement κ ≈ 5.506 ↔ 5.36 as a consistency at the ~2.6% level (0.84σ against the Planck value 5.38 ± 0.15), **not** as a confirmed prediction, and we give the falsifiers and the conditions under which the identification could be promoted to a risky prediction. The novel content of this note is the identification and its conditional structure; the two quantitative inputs are imported from [1, 2].

---

## 1. The dark-to-baryon ratio as a target

In the standard cosmological model the densities of cold dark matter and baryons are independent fit parameters. Their ratio, Ω_DM/Ω_b ≈ 5.36 (Planck 2018 [3]), is measured to better than a few percent but is not predicted: ΛCDM accommodates it without explaining it, and most dark-matter candidates leave the coincidence that the two densities are within an order of magnitude of one another unaddressed.

We distinguish two questions:

- **(Identification)** *With what theoretical quantity should Ω_DM/Ω_b be identified?*
- **(Derivation)** *What value does that quantity take?*

This note addresses the identification; the value follows from results derived elsewhere [1, 2]. We are explicit throughout that the identification is **framework-dependent** — it is a structural assignment within a particular two-orientation cosmological model, not a model-independent measurement. We register it as a **Tier B** claim: a structural identification whose precision is limited by cosmological inference systematics, distinct from a direct laboratory determination.

## 2. The two-orientation setup

We consider a cosmological model carrying two conjugate orientations of a single spatial substrate, related by a discrete conjugation symmetry C. The two orientations share a common boundary geometry (the unit 3-sphere S³ ≅ SU(2)) and a common unresolved fermionic backbone, but carry independent induced metrics g_μν^(±). Constructions of this two-metric type have a long history in bimetric and bigravity model-building; a ghost-free embedding in the Hassan–Rosen class [4] is a natural question but is **not** assumed here, and is left as open work (§6). We use the neutral term *two-orientation* (rather than any branded label) to avoid collision with the several distinct "two-metric" and "Janus-type" constructions already in the literature.

The physical hypothesis is the following. The apparent dark matter observed gravitationally in one orientation (+) is not a new particle species in that orientation; it is the **gravitational echo** of the total stress-energy of the conjugate orientation (−), communicated through a weak cross-sector coupling. Baryonic matter is present in both orientations; under the conjugation symmetry the two orientations carry identical baryonic content.

## 3. The cross-sector bridge and its fixed point

Let T_μν^(b,σ) denote the baryonic stress-energy in orientation σ ∈ {+,−}. We posit a cross-sector coupling of bilinear form with a single dimensionless strength κ₀,

S_bridge = κ₀ ∫∫ √(−g₊)√(−g₋) $\mathcal{K}$ g₊^{αβ} g₋^{ρσ} T_{αβ}^{(b,)} T_{ρσ}^{(b,−)},

together with a self-consistency constraint that closes the back-reaction: the *effective* (gravitating) stress-energy in each orientation is its own matter content plus the κ₀-weighted echo of the effective content of the other,

T̃_μν^(σ) = T_μν^(b,σ) + κ₀ T̃_μν^(−σ).

(A subdominant neutrino term is neglected here; it does not affect the ratio at leading order.) The conjugation symmetry C imposes T_μν^(b,) = T_μν^(b,−) ≡ T_μν^(b) and T̃_μν^(+) = T̃_μν^(−) ≡ T̃_μν, so the constraint becomes a scalar fixed-point equation,

T̃_μν = T_μν^(b) + κ₀ T̃_μν => T̃_μν = T_μν^(b)/(1 − κ₀).

The gravitating excess over the baryonic content — the quantity an observer in orientation (+) attributes to dark matter — is therefore

ρ_DM/ρ_b = κ₀/(1 − κ₀) ≡ κ.

**The closure is derived, not posited.** The geometric series κ₀ + κ₀² + ⋯ implicit in the fixed point is exactly the Neumann resolvent of the s-wave monopole projector that mediates the bridge; because that projector is idempotent (verified directly, second-order insertion ratio G = 1.000000), the series telescopes to κ₀/(1−κ₀) with no higher-order corrections [2]. Had the mediating insertion carried non-unit overlap factors, the resummation would take a different form and κ would lose its parameter-free value. The derivation of that closure, and the three independent realisations of the same x/(1−x) algebra (feedback gain, Dyson/RPA resummation, Clausius–Mossotti effective medium) that corroborate it, are given in the companion note [2]; we import the result here.

## 4. Numerical identification

With the bare coupling κ₀ = 3/√(4π) ≈ 0.84628 imported from [1],

κ = κ₀/(1 − κ₀) = (3/√(4π)) / (1 − 3/√(4π)) = 0.84628/0.15372 ≈ 5.5055.

The comparison with observation is:

| Quantity | This model | Observation (Planck 2018) |
|---|---|---|
| κ₀ | 0.846 | — |
| κ = κ₀/(1−κ₀) | 5.506 | — |
| Ω_DM/Ω_b | 5.506 | 5.38 ± 0.15 |

The predicted ratio is **1.03×** the central Planck value — a residual of 0.84σ against 5.38 ± 0.15, or ~2.6% against the commonly quoted central ratio 5.36. We state this as a **numerical consistency**, not a confirmed prediction (see §5).

It is worth recording what the model does *not* permit. A linear bridge with no self-consistency loop would give κ_alt = κ₀ ≈ 0.846 — low by a factor ~6.4, excluded by Planck at roughly 30σ. The observed ratio is reproduced only by the *amplified*, fixed-point form, whose amplification factor is 1/(1−κ₀) ≈ 6.49. The identification therefore has empirical content beyond the choice of κ₀: it requires the closure, not merely the bare coupling.

## 5. Honest scope

We separate cleanly what is derived, what is imported, and what remains a consistency.

- **Imported (not re-derived here).** The bare coupling κ₀ = 3/√(4π) is a structural identity on the Hopf bundle [1]. The closure κ = κ₀/(1−κ₀) is a derived consequence of idempotent monopole projection [2]. Neither is established in the present note; both are inputs.
- **The contribution of this note.** The *identification* of Ω_DM/Ω_b with the cross-sector fixed point κ, and the conditional structure that makes it parameter-free given [1, 2]. This is a structural assignment within the two-orientation model.
- **Consistency, not confirmed prediction.** A derived value coinciding with a measured ratio is a consistency until an independent observation — one capable of having landed elsewhere — lands on the predicted value. The 2.6% agreement is suggestive, not decisive, and we do not claim more. Tier B.

## 6. Falsifiers and the promotion path

The identification is falsifiable on several independent fronts:

1. **κ outside [1, 7]** at precision-cosmology level, or a measured Ω_DM/Ω_b excluded at >3σ from 5.50 under a fixed identification premise, falsifies the assignment.
2. **A fourth light species** opening an independent cross-sector channel would push κ₀ → 1, breaking the convergence κ₀ < 1 required for a finite ratio; the same κ₀ < 1 bound is the stability boundary of the cross-sector loop [2].
3. **Non-idempotent mediation** (a direct computation returning G ≠ 1) would remove the closure and return κ ≈ 5.50 to coincidence status [2].
4. **Direct dark-matter detection** of a particle whose abundance is inconsistent with the purely gravitational, echo interpretation would falsify the identification premise itself.

**Promotion to Tier A** requires deriving, from the same structure and with no new free parameters, an observable that the identification does not currently fix — in particular a dark-sector mass scale, an effective free-streaming length, or a cross-section — and confronting it with structure-formation or direct-detection data. Until such an independent observable is predicted and tested, the ratio identification remains a structural consistency.

## 7. Conclusion

Within a two-orientation cosmology with a conjugation symmetry between orientations and a bilinear cross-sector bridge of strength κ₀, the dark-matter-to-baryon ratio is the fixed point κ₀/(1−κ₀). With κ₀ = 3/√(4π) and the derived idempotent closure imported from companion notes [1, 2], this is the parameter-free value 5.506, consistent at ~2.6% with the observed 5.36. The identification is conditional and framework-dependent — a Tier B structural assignment — and we have stated its falsifiers and the conditions for promotion to a risky prediction. The note introduces no new mathematics and no new free parameters; its content is the identification and its conditional structure.

---

## References

1. G. White, "A structural derivation of the bare dimensionless coupling 3/√(4π) from monopole projection on the unit Hopf bundle," companion note (2026).
2. G. White, "A derived fixed-point closure for the bare Hopf coupling: κ = κ₀/(1−κ₀) from idempotent monopole projection," companion note (2026).
3. Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. **641**, A6 (2020).
4. S. F. Hassan and R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP **02**, 126 (2012) [arXiv:1109.3515].

---

*v0.1 pre-submission draft. The two quantitative inputs (κ₀ and the closure) are imported from the companion notes [1, 2]; the dark-to-baryon identification and its conditional structure are the content of this note.*
