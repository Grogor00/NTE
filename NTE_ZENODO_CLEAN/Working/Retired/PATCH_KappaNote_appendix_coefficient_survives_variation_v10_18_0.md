# Patch instruction — add "coefficient survives the variation" appendix to the κ note (v10.18.0)

**Author:** AC · **Date:** 2026-07-05 · **For:** Cursor local render lane → Greg ratification
**Purpose:** defensive polish on the flagship κ = 5.50 result. One appendix in the existing κ note showing the cross-source coefficient in the two-orientation Einstein equations is exactly κ₀ under variation of the bilateral action — answering the referee question "why self-consistent, and why coefficient exactly κ₀?" It is honestly scoped to the averaged s-wave sector (the sector of the headline comparison), consistent with Part 2 §IX; it does **not** claim the full nonlinear bimetric completion.
**Status:** ready for Cursor once Greg approves the wording. Single target, single insertion (no existing text changed).

**Register note.** The note uses plain-unicode math (κ₀, √, ⁺/⁻, ∫, Ω), not LaTeX `$…$`. The appendix matches that. Preserve it — do not "upgrade" to LaTeX.

**Application rule:** match on the distinctive anchor sentence, not exact whitespace. This is a pure insertion between the last body section and "## Provenance"; no existing text is altered. After the edit, re-read and confirm the appendix is present and "## Provenance" still follows it. If the OLD anchor does not match cleanly, **stop and report — do not force.** Apply to the canonical source the render reads; keep the Core… no — this file lives in `Pedagogical_Notes/`; keep the `Pedagogical_Notes/` copy and any `paper-build/scratch-src/` copy in sync; re-render the note; confirm the set holds at 29/29.

---

## TARGET — `Pedagogical_Notes/Paper_Kappa_AB_Pedagogical_Note_v10_18_0.md`

Insert the appendix between the end of "What would break it" and the "## Provenance" heading.

**OLD:**
```
If the κ₀ derivation itself is wrong, the prediction breaks at the input level.

## Provenance
```
**NEW:**
```
If the κ₀ derivation itself is wrong, the prediction breaks at the input level.

## Appendix: the cross-source coefficient survives the variation

The closure in the body assumes one thing about the field equations: that the two orientations' Einstein equations cross-source each other at strength *exactly* κ₀ = 3/√(4π) — the same number the bare Hopf projection produced — with no extra factor introduced when those equations are obtained by varying an action. Because the whole result (5.50 rather than 0.846, a factor of about 6.5) rides on that coefficient, this appendix shows it explicitly.

**The action.** The framework's bilateral gravity is a single action spanning both orientations,

S = (1/16πG) ∫ √(−g⁺) R⁺  +  (1/16πG) ∫ √(−g⁻) R⁻  +  S_m[g⁺,ψ⁺]  +  S_m[g⁻,ψ⁻]  +  S_bridge[g⁺,g⁻,ν] :

two Einstein–Hilbert terms, ordinary matter on each side, and one shared bridge term — the Z₂-even unresolved neutrino ν, delocalised over the Hopf fibre, the only field carrying stress-energy on both metrics at once.

**The variation.** Varying with respect to the + metric, δS/δg⁺_μν = 0, gives the + orientation's Einstein equation with two sources,

G⁺_μν = 8πG ( T_b⁺ + T_bridge⁺ )_μν ,   with   T_bridge⁺_μν = −(2/√(−g⁺)) · δS_bridge/δg⁺^μν ,

and symmetrically on the − side. T_b⁺ is ordinary matter; the entire question is the magnitude of T_bridge⁺ — the stress-energy the − side deposits on our metric through the shared neutrino.

**Where the coefficient comes from.** The bridge field couples to each metric through its angular profile on the internal S² base of the Hopf fibration. Having failed the projection S³ → S², the neutrino is smeared *isotropically* across that base, so its normalised angular profile is the constant s-wave Y₀₀ = 1/√(4π). The stress-energy it transmits from the − side onto the + metric is that side's source projected onto this shared s-wave channel — the monopole projection — which for any normalised isotropic density returns its Y₀₀ weight, 1/√(4π), per channel. The bridge runs in the three su(2)-adjoint components (dim adj SU(2) = 3), so the transmitted coefficient is 3 × 1/√(4π) = 3/√(4π) = κ₀. It is the *same* overlap that fixed the bare coupling, reappearing here as the strength linking the two Einstein equations rather than as a coupling inside one of them.

**Why the variation does not renormalise it.** Three facts keep the coefficient from acquiring a spurious factor when the metric is varied:

1. *The overlap sits on a fixed base.* The dynamical fields are the two 4-dimensional orientation metrics; the overlap that sets κ₀ is an integral over the *internal* unit S² of the Hopf base, whose measure is not among the varied quantities. Varying g⁺ cannot rescale a number fixed on the internal base.

2. *The Jacobian cancels.* The √(−g⁺) produced by the variation multiplies both the geometric side (via G⁺_μν) and the matter side (in the definition of T_bridge⁺ above); it divides out in forming G⁺_μν = 8πG T⁺_μν, so it cannot re-weight the cross term relative to the ordinary-matter term. The universal factor of 2 in the stress-tensor definition is likewise common to T_b⁺ and T_bridge⁺ and drops from their ratio — and it is that ratio, not either term alone, that the closure uses.

3. *Idempotency holds it order by order.* The s-wave projector P = |Y₀₀⟩⟨Y₀₀| satisfies P² = P with ∫ Y₀₀² dΩ = 1, so a second cross-insertion carries exactly κ₀², and the n-th carries κ₀ⁿ. No overlap factor accumulates down the series — the reason the geometric sum closes to a clean 1/(1 − κ₀) rather than 1/(1 − G κ₀) with G ≠ 1. (This "G = 1" property has been checked independently in the monopole sector.)

With the coefficient pinned at κ₀ on every insertion, the CPN-symmetric closure T̃ = T_b + κ₀ T̃ is exactly the relation solved in the body, and its fixed point is κ = κ₀/(1 − κ₀).

**Scope.** This is established in the averaged, s-wave (monopole) sector — the sector in which κ = 5.50 is compared against Planck. The full non-averaged bridge (retaining the higher-ℓ structure of Θ) and the complete ghost-free nonlinear bimetric completion (Hassan–Rosen-class) remain open refinements of the two-orientation gravity, exactly as Part 2 §IX records; nothing here claims them. The claim is the narrower one the headline number needs: in the sector where 5.50 is quoted, the cross-source coefficient is κ₀ by construction of the action, not by choice.

## Provenance
```

---

## Notes for Greg (ratification points)

- **What it does / doesn't claim.** It shows the κ₀ coefficient is forced by the action's angular overlap and is not renormalised by the metric variation (three explicit protections: fixed internal base, Jacobian cancellation, idempotency). It does **not** claim the full nonlinear ghost-free bimetric completion — that stays "open refinement" per §IX, and the Scope paragraph says so. This keeps the appendix honest polish rather than a silent tier promotion.
- **It absorbs the G=1 work.** Point 3 is exactly the idempotency the Cursor/Jammer scripts checked; the appendix references it as an independent monopole-sector check without leaning on those (pre-decontamination) memos. If you want the numeric check cited by filename, re-base those scripts to v10.18.0 first — but the appendix stands without them.
- **Placement.** In the Kappa_AB note (`Pedagogical_Notes/`), where the closure is explained, rather than the DM-ratio standalone — keeps the derivation with its exposition, and it's a deposit file. No change to Part 2/3.
- **Register.** Plain-unicode math to match the note; explanatory voice; ~half a page. No LaTeX.
