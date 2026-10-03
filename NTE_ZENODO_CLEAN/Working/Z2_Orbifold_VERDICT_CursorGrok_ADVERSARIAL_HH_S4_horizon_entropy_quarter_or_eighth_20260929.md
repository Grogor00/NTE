# Z₂-orbifold verdict — does CPN change the Hartle–Hawking horizon coefficient?

**From:** Cursor Grok · **To:** AC · **Cc:** Greg, Scratch · **Date:** 2026-09-29
**Register:** verification. **Nothing patched.**
**Blind:** this leg was written without reading Scratch's Derivation_Progress, the Dark Sector companion draft, the GHY derivation scratch, the DE-magnitude exploration scratch, or the Dark Sector skeleton. Independent reading of the deposit only. AC reconciles after both legs file.

**Question.** Does NTE's CPN symmetry act on the Hartle–Hawking S⁴ as a quotient that changes the horizon entropy coefficient — S = A/4G, S = A/8G, or something else?

**Context fact used (given, not re-derived).** The Bekenstein–Hawking 1/4 is the on-shell Euclidean action of the round S⁴: I_E = −π/(GH²) ⇒ S = −I_E = A/4G (Gibbons–Hawking). That S⁴ is NTE's Hartle–Hawking saddle (Part 1 §2.1.2). The 1/4 is native to the base manifold. This leg asks only whether CPN imposes an extra factor.

---

## Forks declared before results

- **Z-A1** — CPN is an equatorial reflection of the S⁴, or otherwise a fixed-point involution, or a descriptive / spin-structure symmetry that does not quotient the saddle. Horizon coefficient unmodified: **S = A/4G**.
- **Z-A2** — CPN acts freely on the saddle (S⁴ → ℝP⁴, no fixed points). Volume halves. **S = A/8G**. That would be a new, falsifiable NTE prediction, with the registered consequence **ρ_Λ = 6 M_Pl² H²** (twice the standard de Sitter density 3 M_Pl² H² in reduced Planck units).
- **Z-A3** — The deposit does not fix CPN's action on the saddle. Name the commitment that would.

Scratch's constructive lean, attacked and not adopted: Z-A1 by identifying §VI's "one manifold, two CPN-conjugate orientations" with the two ±N Lorentzian continuations off the Hartle–Hawking equator, already inside A/4G, and by reading "Z₂-orbifold (Pin⁻)" as a spin-structure statement rather than a volume-halving quotient. The pressure applied below is whether that reading is convenient, and whether the deposited antipodal map plus Pin⁻ instead forces a free action.

---

## Read set (discipline 11)

Read in full for the sections that carry the claim, and searched across the Core_Papers companions for CPN action, Pin⁻, Z₂-orbifold, ℝP⁴, antipodal, equatorial reflection:

1. `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` — §II.0, §2.1.2, §VI (and the surrounding Euclidean / Janus text).
2. `Core_Papers\NTE_v10_19_0_Part2_Structure.md` — §VIII–IX, §XVI, and the CPN / Z₂ / Janus passages in between.
3. `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` — the Pin⁻ / orbifold ledger line.
4. `Core_Papers\Companion_05_StateSpace_v10_19_0.md` — §5, the only place the CPN map is written as a transformation.
5. `Core_Papers\Companion_07_Neutrino_v10_19_0.md` — charge conjugation as the antipodal exchange on S³.
6. `Core_Papers\Companion_12_Chord_v10_19_0.md` — antiperiodic spin structure on the S¹ factor (adjacent spin-structure language; not a 4-volume quotient).
7. Companion search (01–20 and the three Parts) for Pin, orbifold, antipodal, ℝP⁴. No companion states a free quotient of the Euclidean saddle. ℝP⁴ is not named anywhere in the deposit.
8. `Handoffs\Directive_Scratch_to_Cursor_Grok_ADVERSARIAL_Z2_orbifold_factor_on_HH_S4_horizon_entropy_quarter_or_eighth_20260928.md`.

External mathematical fact used only as an obstruction, not as a deposit claim: ℝP⁴ admits Pin⁺ and does not admit Pin⁻ (w₂(ℝP⁴) = 0, w₂ + w₁² ≠ 0). See Kirby–Taylor, *Pin structures on low-dimensional manifolds*; Stolz, *On the eta-invariant of the Pin⁺ operator* (Compositio Math. 78 (1991)); the ℝP⁴ example in the Pin± Lefschetz-fibration notes.

---

## Result

**Chosen fork: Z-A1.** CPN does not quotient the Hartle–Hawking saddle. The horizon coefficient stays the native Gibbons–Hawking value **S = A/4G**. NTE does **not** predict S = A/8G and does **not** predict ρ_Λ = 6 M_Pl² H².

The landing is the descriptive / spin-structure branch of Z-A1, together with a fixed Janus locus under N-reversal. It is **not** Scratch's equatorial-reflection mechanism. That mechanism gets the coefficient right and the map wrong. The free-quotient reading that would have produced Z-A2 was the live alternative; it is closed by the deposit, not left open as Z-A3.

---

## What the deposit actually says CPN does

**Orientations of one manifold, not an orbit space.** Part 1 §VI:

> "The Janus pair is one manifold viewed from two CPN-conjugate orientations related by the symmetry at the boundary; each orientation looks complete, the other appearing CPN-conjugate."

**The Z₂-orbifold sentence is a spin-structure sentence, and it names its locus.** Part 1 §VI:

> "The boundary symmetry is CPN (charge, parity, e-fold-direction reversal); summed over both orientations, energy, charge, and baryon number vanish at N = 0. CPN reduces to CPT post-locking (CPT is the emergent description; CPN the deeper structure). The Janus pair admits a Z₂-orbifold description whose spinor bundle has exactly two spin structures; the twisted one (Pin⁻) produces baryogenesis and matches observation, so "why CPN?" is answered by "Pin⁻ is the topological twist of the manifold's N-thickness.""

Part 3's derived-ledger line is the same object, listed beside S³, not instead of it:

> "CPN selection (Pin⁻ on the ℤ₂ orbifold); the Majorana condition (forced by orbifold convergence κ₀<1); S³ as the unit sphere of the surviving quaternionic subalgebra ℍ ⊂ 𝕆."

**The only explicit point-map is the antipodal map on the boundary S³.** Companion 5 §5:

> "The CPN transformation is the antipodal map on S³, (z₁, z₂) → (−z₁, −z₂): multiplication by e^{iπ}, the Euler rotation on the state space, reversing every coordinate while preserving the S³ structure. The CPN-conjugate sector is not a separate manifold but the same S³ under the antipodal identification."

The selection rule that comes with that map keeps both parities (Companion 5 §5):

> "The S³ harmonics transform under the antipodal map as Y_l^m(antipodal) = (−1)^l Y_l^m(original): even-l harmonics are symmetric and couple to their antipodal images, odd-l harmonics are antisymmetric and decouple."

Companion 7 places the same map at the boundary and identifies it with charge conjugation:

> "charge conjugation exchanges antipodal points on S³, which is the CPN transformation at the Janus boundary."

**N-reversal is not a time-reversal quotient of the saddle.** Part 2 §IX:

> "Boyle–Finn–Turok relate the two halves by a genuine time reversal (τ→−τ across the bang, the antiuniverse being the CPT/Stueckelberg image), whereas NTE's mirror is the CPN-conjugate orientation and the emergent proper time is held orthogonal to the N-direction that CPN flips (t = i·ΔN, Part 1 §2.1.2) — so the proper-time arrow is common to both halves and there is no time-reversed antiuniverse."

> "NTE's two observable universes are the boundary surfaces of a bubble formed in a pre-temporal Euclidean bulk — a surface-only ontology once time has emerged, the conjugate twin being the opposite surface with only residual pre-temporal bulk between them."

**The Euclidean geometry that is named is the 4-ball bounded by S³, and the two orientations share one N-range.** Part 2 §XVI:

> "The 4-ball "interior" is not a place for observers on the S³ surface: the radial direction is not spatial — it *is* the e-fold accumulation N, and the two CPN-conjugate orientations occupy the same N-range from opposite directions. […] A boundary-only analogue of Ryu–Takayanagi, S(A) = 𝒜(∂A)/4G_N, follows from counting the null-time exchange modes crossing the S² that separates A from its complement on S³. […] (The area-counting is standard Bekenstein–Hawking; the 1/4 coefficient is not yet derived from NTE.)"

Part 1 §2.1.2 and §II.0 call this the Hartle–Hawking Euclidean section / no-boundary condition in NTE vocabulary (t = i ΔN), kept as a reformulation, not as a derived modification of the instanton action.

**The orbifold's factor of 2, where one is actually computed, is fermion mode-counting.** Part 2 §IX:

> "on the ℤ₂ orbifold Dirac neutrinos would give κ₀ = 6/√(4π) > 1 — so the Majorana condition is topologically forced, not assumed."

6/√(4π) against 3/√(4π) is a doubled eigenmode count (Dirac versus Majorana) under the Z₂. It is not a halved ∫ √g d⁴x.

---

## Attack on the lean

### The equatorial-reflection identification is not the deposited map

Equatorial reflection of the round S⁴, χ → π − χ with the S³ coordinate n held fixed, fixes the equatorial S³ **pointwise**. Its restriction to the Janus slice is the identity.

The deposited CPN transformation is (z₁, z₂) → (−z₁, −z₂). That map is free on S³: no point of the slice is fixed. Companion 5 says this map **is** the CPN transformation, and Companion 7 repeats it as charge conjugation at the Janus boundary. So "CPN = τ → π − τ, the two standard Lorentzian continuations already inside A/4G" is a convenient substitute for the map the deposit writes. The two ±N readings are real — Part 2 §XVI's "same N-range from opposite directions," and Part 2 §IX's refusal of τ → −τ — but they are the N-reversal, not the antipodal map. Collapsing those into one involution is the soft step in the lean.

N-reversal alone, N → −N, does fix a hypersurface: the Janus locus N = 0, the whole S³, setwise. That is a fixed-point involution. It is not free, and it is not the antipodal map. The deposit runs both structures and does not identify them.

### The free extension is the reading that had to be killed, and it dies

The S⁴ antipodal map in polar coordinates is (χ, n) → (π − χ, −n): polar reflection composed with the S³ antipodal map. It is free. The quotient is ℝP⁴, the volume is half, and the on-shell Euclidean action becomes I_E[ℝP⁴] = ½ I_E[S⁴] = −π/(2GH²). If that quotient were the physical saddle, and if S = −I_E with the horizon area still the S² area 4π/H² of the covering geometry, the coefficient would be **S = A/8G**. That is Z-A2, and the directive's registered density consequence is **ρ_Λ = 6 M_Pl² H²**.

Nothing in the deposit takes that last step, and four deposited facts block it.

1. **Wrong Pin group.** ℝP⁴ has w₂ = 0 and w₂ + w₁² ≠ 0, so it admits two Pin⁺ structures and no Pin⁻ structure. The deposit selects Pin⁻ and locates it as "the topological twist of the manifold's N-thickness." A free antipodal quotient of the saddle would be the structure the sentence does not name. Part 3 keeps that Pin⁻ selection on the same line as "S³ as the unit sphere of ℍ."

2. **Odd modes are demoted, not deleted.** On ℝP³ = S³/Z₂ the odd-l harmonics do not descend to functions. Companion 5 keeps them and says they decouple from cross-boundary coupling. That is a Z₂ representation grading of fields on S³. "Preserving the S³ structure" is the same point: the map is an automorphism of S³, not a replacement of S³ by ℝP³. Part 1 §II.0 records that a Klein-bottle topology was abandoned when parallelisability, Lie-group structure, and boundary parity converged on S³. The free quotient of the equator would throw that convergence out.

3. **The named 4-geometry is the 4-ball, not ℝP⁴.** Companion 5 and Part 2 §XVI: ∂B⁴ = S³, the radial direction re-read as N. ℝP⁴ is closed and non-orientable. It is not a 4-ball with boundary S³. Part 2 §IX(iii) puts residual Euclidean bulk **between** two boundary surfaces. A free antipodal quotient has no such pair of boundary surfaces.

4. **The phrase that looks like a quotient is immediately glossed as orientations plus a spinor bundle.** "Admits a Z₂-orbifold description whose spinor bundle has exactly two spin structures" is the content of the orbifold claim. "Exactly two spin structures" and "the twisted one" are the periodic/antiperiodic choice along the thickness — the same family of fact as Companion 12's antiperiodic S¹, spin structure θ = 1/2 — not a statement that the Einstein–Hilbert integral is taken on half of S⁴. The one place a factor of 2 is evaluated on this orbifold (Dirac κ₀ = 6/√(4π)) is that mode doubling.

"The same S³ under the antipodal identification" is the sentence that could still be misread as a quotient. Read against the odd-harmonic rule, "preserving the S³ structure," the 4-ball, and Pin⁻, it means the conjugate sector is the antipodal re-description of this S³, not a second manifold and not S³/Z₂.

### The fixed-point case does not silently become A/8G either

N → −N has a fixed hypersurface. The quotient by that reflection is an orbifold with a mirror stratum, or equivalently the hemisphere (the 4-ball) as a fundamental domain. The bulk Einstein–Hilbert integral over one hemisphere is half the full-sphere bulk integral, and the Gibbons–Hawking–York term on the equatorial S³ appears. The deposit never evaluates that boundary term, and it never replaces the coefficient it does write.

The coefficient it writes is already 1/4. Part 2 §XVI: S(A) = 𝒜(∂A)/4G_N, "standard Bekenstein–Hawking; the 1/4 coefficient is not yet derived from NTE." "Not yet derived" means NTE has not earned the 1/4 from its own axioms. It does not mean CPN has changed it. This verdict does not upgrade that sentence into a derivation. It says the deposited CPN action does not modify the base-manifold result the context fact already records.

A bilateral Einstein–Hilbert term is not a second halving. Part 1 §VI and Part 2 §IX: the two-metric equations are the metrics on the two orientations of **one** thickness, from a single bilateral action, "not independent manifolds."

---

## Why not Z-A3

Z-A3 would be right if a free action on the saddle were still an open reading of the same sentences. It is not. The diffeomorphism on the 4-ball is not written down as χ → π − χ, so Scratch's particular mechanism is not forced — that much is a gap. The coefficient is not similarly open: every reading that survives the Pin⁻ locus, the retained odd spectrum, the S³/4-ball ontology, and the orientation language leaves the Euclidean 4-volume of the round saddle unquotiented. S = A/4G.

Commitments that would move the fork, named so the gap is sharp:

- **To Z-A2.** An explicit statement that the on-shell Euclidean manifold is the free quotient S⁴/Z₂ ≅ ℝP⁴, with the Einstein–Hilbert integral taken on that quotient, and a revision of the selected structure from Pin⁻ to Pin⁺ (the group ℝP⁴ actually admits). Until that is deposited, ρ_Λ = 6 M_Pl² H² is not an NTE prediction and must not be entered as one.
- **To lock the equatorial-reflection mechanism inside Z-A1.** An explicit statement that N-reversal acts on the saddle by reflection through a pointwise-fixed equatorial S³, and that (z₁, z₂) → (−z₁, −z₂) is only the action of C on fields on that fixed slice, not a quotient of the 4-volume. The coefficient conclusion does not wait on that sentence.

---

## Coefficient

| Object | Deposit | Effect on S |
|---|---|---|
| Round S⁴, base saddle | Part 1 §2.1.2, context fact | S = −I_E = A/4G |
| CPN as two orientations of one manifold | Part 1 §VI; Part 2 §XVI | no extra volume factor |
| Antipodal map | Companion 5, Companion 7; on the boundary S³; odd modes kept | symmetry of S³, not S⁴ → ℝP⁴ |
| Z₂-orbifold / Pin⁻ | Part 1 §VI; Part 3; twist of the N-thickness; two spin structures | spin structure, not a 4-volume quotient |
| Orbifold factor of 2 that is computed | Part 2 §IX, κ₀ = 6/√(4π) for Dirac | fermion doubling, not horizon area |
| Entropy coefficient written in the deposit | Part 2 §XVI, 𝒜/4G_N | 1/4, explicitly not NTE-derived |

**S = A/4G, unmodified.** No loud flag: Z-A2 does not fire. The standard de Sitter density ρ_Λ = 3 M_Pl² H² is untouched. The 1/4 remains native to the Euclidean base manifold and is still, as Part 2 §XVI says, not derived from NTE.

— Cursor Grok, 2026-09-29.
