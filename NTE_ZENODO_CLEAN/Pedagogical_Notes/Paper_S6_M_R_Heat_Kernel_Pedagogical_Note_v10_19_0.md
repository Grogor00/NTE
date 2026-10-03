---
title: "Three Planck Powers and a Higgs Anchor"
subtitle: "A tier-3 explanatory note on the right-handed neutrino mass scale M_R from spectral geometry"
author: "G. White"
date: "2026-06 (v10.19.0)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

---

## The result in one paragraph

The seesaw mechanism for neutrinos requires a heavy right-handed neutrino with mass M_R, somewhere around 10¹⁵ GeV in the natural-scale regime. Setting M_R is the hardest single number in the seesaw picture, because the right-handed neutrino is too heavy to produce in any current experiment. The companion paper derives M_R = M_Pl^(3/4) × v_EW^(1/4) ≈ 8.2 × 10¹⁴ GeV from geometry — combining three powers of the Planck mass with one power of the Higgs vacuum value, in a specific 3:1 weighting that comes from three spatial dimensions of the framework's spatial geometry plus one Higgs anchor. The framework's prediction for the heaviest light neutrino's mass, m_{ν₃} = v²/M_R = 0.0738 eV, exceeds the normal-ordering atmospheric oscillation scale √Δm²₃₁ ≈ 0.0495 eV by ≈1.49×. With a geometry-fixed Yukawa on the second generation, the solar splitting lands at 0.993× sub-1% precision *on the 8π branch of an open 8π/4π normalisation choice* (the 4π branch fits the mass ratio instead, and no single M_R fits both legs at sub-1%); the structural mass ratio m_{ν₃}/m_{ν₂} = (8π)^(2/3) ≈ 8.57 sits above the observed √(Δm²₃₁/Δm²₂₁) ≈ 5.82 by the same ≈1.5× factor. The genuine content is the ratio shape and the Majorana–Dirac trade-off, not a parameter-free solar mass. The derivation uses standard mathematical tools (heat-kernel expansion on a curved background, Hopf bundle topology) and partially closes at strict mathematical rigour with one explicit coefficient extraction still pending.

## Why this matters in one paragraph

Most particle physics extensions of the Standard Model add the right-handed neutrino's Majorana mass as a free parameter, choosing it to give the observed light neutrino masses via the seesaw formula. The free choice has nothing to constrain it; M_R could be 10¹⁴, 10¹⁵, or 10¹⁶ GeV with equal theoretical legitimacy, depending on what gives the right answer for the light neutrinos. The present framework supplies a structural reason for the specific value — three Planck mass powers from the three spatial dimensions of the framework's S³ geometry, one electroweak mass power from the Higgs anchor, combined as M_R⁴ = M_Pl³ × v_EW. The fourth root sets M_R at 8.2 × 10¹⁴ GeV, and that value combined with the seesaw formula gives the solar neutrino mass at 0.993× *on the 8π branch of an open normalisation choice* while the atmospheric leg sits at a structural ≈1.5× overshoot relative to √Δm²₃₁. The structural derivation moves M_R from a free parameter to a derived quantity, and the ratio shape and Majorana–Dirac trade-off — the branch-independent content — are what make the structural reading worth taking seriously.

---

## The seesaw mechanism, briefly

The seesaw mechanism — the most economical explanation in physics of why neutrinos are so light — assumes a heavy right-handed neutrino partner for each light left-handed neutrino, with a Majorana mass M for the right-handed partner. The light-neutrino mass comes out as

*m_ν ≈ Y² v² / M*

where Y is the Dirac Yukawa coupling and v ≈ 246 GeV is the Higgs vacuum value. If M is around 10¹⁵ GeV and Y is around 1, then m_ν ≈ 10⁻² eV — the right order of magnitude for neutrino masses.

The mechanism's elegance is that it explains why neutrinos are *light* without making their Yukawa couplings *small*. The heavy partner M does the work of suppression. The structural question is where the heavy scale M comes from.

In the most economical seesaw setups, M is a free parameter chosen to fit observation. The framework presented here gives M from geometry: the heavy mass M_R combines three powers of the Planck mass with one power of the electroweak Higgs value, in a specific weighting that has a structural origin.

## The formula and where it comes from

The structural formula is

*M_R = M_Pl^(3/4) × v_EW^(1/4)*

where M_Pl ≈ 1.22 × 10¹⁹ GeV is the (non-reduced) Planck mass and v_EW ≈ 246 GeV is the Higgs vacuum value. Working out the arithmetic:

*M_R = (1.22 × 10¹⁹ GeV)^(3/4) × (246 GeV)^(1/4) ≈ 8.2 × 10¹⁴ GeV*

Where do the powers come from? The framework's mathematical setting is a closed spatial geometry — specifically a 3-sphere with a Hopf-bundle structure — combined with a finite "internal" algebra that encodes the matter content of the Standard Model. The heat-kernel expansion of a fundamental differential operator on this combined geometry produces mass scales at successive orders, each scale weighted by the natural mass scale of the operator (here, the Planck mass) and by the dimensionality of the underlying spatial structure.

The specific combination M_Pl³ × v_EW emerges from a particular contribution to the heat-kernel coefficient. The three Planck-mass powers correspond to the three spatial dimensions of the 3-sphere; the one Higgs-anchor power v_EW corresponds to the electroweak symmetry-breaking direction in the algebraic sector. Taking the fourth root gives the formula above.

## The 3:1 structure: two equivalent readings

The structural content of the formula has two equivalent geometric readings:

The first reading is *flux integration*: the heat-kernel expansion contains contributions from each spatial dimension separately, with each dimension contributing one Planck-power weight when integrated against the spectral measure. Three dimensions of the 3-sphere give M_Pl³; the Higgs symmetry breaking direction in the internal algebra gives v_EW. Their product is M_R⁴.

The second reading is *Hopf base-and-fibre*: the 3-sphere admits a Hopf fibration into a 2-sphere base and a circle fibre. The 2-sphere base contributes M_Pl² (two Planck-power weights, one per dimension); the circle fibre contributes M_Pl¹ (one Planck-power weight); the Higgs anchor contributes v_EW. Their product is the same M_R⁴.

These two readings are not independent derivations — they're two different ways of distributing the same three Planck-power weights across the geometry. The companion paper establishes the equivalence of the two readings via a reconciliation step (volume factorisation on the standard round 3-sphere — strict mathematical, by Fubini integration) combined with the structural identification of one Planck-power per spatial dimension (which sits at the framework's spectral-action register, not at strict-math rigor).

## The numerical match — and the open normalisation

The heaviest light-neutrino mass follows from the seesaw formula with this M_R and the Cartan-aligned Yukawa coupling Y₃ = 1:

*m_{ν₃} = Y_3² × v_EW² / M_R = (246 GeV)² / (8.2 × 10¹⁴ GeV) = 0.0738 eV*

The PDG 2024 normal-ordering atmospheric comparand is √(Δm²₃₁) ≈ 0.0495 eV. The ratio m_{ν₃}/√(Δm²₃₁) is **≈1.49×** — a structural overshoot, not a sub-1% match (prior 0.997× claims used a mis-cited atmospheric scale).

The same M_R, combined with the Dirac Yukawa coupling for the second-generation neutrino (Companion 13), gives m_{ν₂} = 0.00860 eV at **0.993×** the observed solar mass scale √Δm²₂₁ — *but only on the 8π branch of an open 8π/4π normalisation choice*. The representation-consistent 4π branch gives ≈1.57× instead, and fits the mass ratio better. The structural ratio m_{ν₃}/m_{ν₂} = (8π)^(2/3) ≈ 8.57 exceeds the observed √(Δm²₃₁/Δm²₂₁) ≈ 5.82 by the same ≈1.5× factor. **A single M_R cannot fit both legs at sub-1%.** The genuine branch-independent content is the ratio shape and the Majorana–Dirac trade-off.

## Status of the derivation: what's tight, what's still open

*Strict mathematical*: the Hopf bundle's Chern number is exactly 1 (standard topology). The volume factorisation of the 3-sphere into Hopf base × Hopf fibre is exact Fubini integration on the standard round metric. These are strict mathematical results.

*Structural*: the identification of the Higgs vacuum direction with a specific Pauli matrix direction in the algebraic sector; the dominance of the Cartan-aligned (heaviest) right-handed neutrino mode in the relevant heat-kernel trace; the electroweak-scale matching via the spectral-action Higgs inner-fluctuation. These are not strict theorems but structural identifications at the framework's spectral-action register.

*Partially open*: the explicit numerical coefficient of the heat-kernel trace, computed from a fully displayed Dirac operator matrix on the framework's finite algebra. The framework predicts the value from the structural identifications above, but the direct computation from an explicit matrix is still pending and is the next step in the development.

## What would break it

If the heaviest light-neutrino mass turns out to be substantially different from the framework's predicted m_{ν₃} = 0.0738 eV, the input M_R = 8.2 × 10¹⁴ GeV is wrong. If neutrinos turn out to be Dirac rather than Majorana, the seesaw framework's underlying assumption fails. If the 8π/4π normalisation choice is resolved definitively and neither branch fits both legs simultaneously, the structural mass-ratio prediction would need revision at a deeper algebraic level. If the explicit Dirac-operator matrix derivation yields a different numerical factor, the structural derivation breaks at the explicit-computation step.

## Provenance

This is a tier-3 explanatory note. It is a companion to the standalone technical paper *The Right-Handed Neutrino Mass Scale (M_R) from Spectral Geometry* (Paper S6 M_R Heat Kernel v1.0). The companion paper *The second neutrino Yukawa from the D5 inverse* (Companion 13) covers the second-generation Yukawa duality (8π)^(−1/3) that combines with this M_R to give the solar neutrino mass prediction, with the 8π/4π open normalisation and the branch-contingent scope stated explicitly.

---

*Corpus version: NTE v10.19.0 (decontaminated Zenodo release, 2026-06).*

— G. White, 2026-06 (tier-3 explanatory note, v10.19.0 rebuild).
