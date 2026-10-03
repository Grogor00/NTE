# Master v10.8 → v10.9 Patch Instructions

## A6 Ship — §17.5 Falsifiability Catalogue Consolidation + §17.5.10 Closure + Tier 2/3 Recommendations

**AC, 2026-05-23.** Per Lesson #31 protocol: AC produces patch instructions for the master corpus; Greg renders into the local master. Four surgical passages affected across master Part 2 (§8.7.7) and master Part 3 (§17.5.10, §XVII Parameter Accounting, §17.5.12).

**Scope ratification:** Greg ratified Reading C with Tier 2/3 recommendations included (2026-05-23). The May 2026 AC→Jammer audit verdict on §17.5.10 was APPROVED clean with three integration recommendations (Tier 1 closure, Tier 2 §8.7.7 helicity clarification, Tier 3 §XVII parameter accounting upgrade) that were queued for the v10.X = v10.9 ship arc but did not land in v10.7/v10.8. A6 adopts all three plus the falsifiability catalogue consolidation. Source audit: `Handoff_AC_to_Jammer_17_5_3_and_17_5_10_audit_response.md` (Drive ID `11e1A8XITBGnbVPfE9uCjZQ8cdmS7E0hv`, in Handoffs/).

**Relationship to A5:** A6's patches do not conflict with A5's standalone surgical ship (Master Part 3 v10.8 → v10.8 v2 Born rule scope alignment, patch instructions at Working/ Drive ID `1r4twq1yqEq3NvUmBDco5K1kfNIpsBc-2`). The two ship arcs can ride together as a v10.9 candidate, or A5 can land first as v10.8 v2 with A6 landing afterward as v10.9. Greg's call on sequencing. Patches below are written against v10.8 baseline.

---

## Patch 1: §17.5.10 — closure status update (Tier 1)

**Location:** Master Part 3 (Drive ID `1eiXLCZE2bLlhdIpjGtzFVBzOsUzdGFTg`), §17.5.10 in full.

**Find (current text in v10.8):**

```
17.5.10 The 90 Species Count vs SM Particle Content

NTE derives 90 species from J₃(𝕆) + Majorana condition. The Standard Model has fewer than 90 fundamental fields. The framework's account of how the 90-species count reduces to the observed SM particle content — including which species the count includes (left/right components separately? particle/antiparticle? generation-multiplied?) and which are identified with each other under the Majorana condition — is not explicit in the corpus. Research target: explicit reduction of the 90 species count to observed SM fields, with the identifications named.
```

**Replace with:**

```
17.5.10 The 90 Species Count vs SM Particle Content (Closed by Enumeration, v10.9)

NTE derives 90 species from J₃(𝕆) + Majorana condition. **Closed by enumeration v10.9** (May 2026 AC audit, integrated this version; predecessor framing in v10.8 carried the reduction as "research target — not explicit in the corpus"). The reduction to observed SM fields is explicit:

(i) **Furey 16 states per generation:** L_L (2) + e^c_L (1) + Q_L × 3 colours (6) + u^c_L × 3 (3) + d^c_L × 3 (3) + ν^c_L (1) = 16 LH Weyl states under the SU(3)_c × SU(2)_L × U(1)_Y gauge decomposition (Furey 2018; Dixon 1994; cf. §8.7.7).

(ii) **Majorana identification:** ν^c_L = ν_L removes one LH Weyl field per generation, giving 16 → 15 LH Weyl states per generation. Across three generations: 15 × 3 = 45 independent LH Weyl fields.

(iii) **Helicity doubling:** Each LH Weyl spinor carries 2 on-shell physical degrees of freedom (LH-particle helicity + RH-antiparticle helicity per field). 45 × 2 = 90 physical fermionic d.o.f.

(iv) **SM-content cross-check (independent enumeration):** 72 (quarks Dirac: 6 flavours × 3 colours × 4 d.o.f.) + 12 (charged leptons Dirac: 3 flavours × 4 d.o.f.) + 6 (Majorana neutrinos: 3 flavours × 2 d.o.f.) = 90. ✓

(v) **g_eff cross-check (structural self-consistency):** above-EWSB bosonic degrees of freedom = 16 (gluons) + 6 (W^a) + 2 (B) + 4 (Higgs complex doublet) = 28. g_eff(T > T_EW) = 28 + (7/8)(90) = 106.75. Matches §2.4.2's β_NTE characterisation g_eff input exactly. The match ties two structurally independent derivation chains (J₃(𝕆) + Majorana for fermion d.o.f.; SM gauge group + Higgs sector for boson d.o.f.) into one mutually self-consistent enumeration; either chain failing would have produced inconsistency.

**Status:** closed. The framework's species enumeration and β_NTE characterisation are mutually self-consistent at the d.o.f. level. The Majorana condition's role as the identification mechanism (16 → 15 per generation) is what removes the apparent gap between the 90-count and observed SM fields — under Majorana convention, the SM has exactly 90 physical fermionic d.o.f.

**Falsifiability footprint (cross-reference §17.5.12 category E):** any precision determination of g_eff at T > T_EW deviating from 106.75 at greater than Planck-era uncertainty, or independent SM-content enumeration finding ≠ 90 physical d.o.f. under Majorana convention, would falsify either the J₃(𝕆) + Majorana enumeration above or the β_NTE characterisation (§2.4.2) — these are now structurally coupled at the cross-check level.
```

**Rationale:** The May 2026 audit established the reduction cleanly; v10.7/v10.8 did not integrate the closure. Patched section reframes §17.5.10 from research target to closed-by-enumeration with the five-step structural argument explicit, the g_eff self-consistency made canonical, and the falsifiability footprint cross-linked to §17.5.12 (Patch 4 below). Above-EWSB boson labels used throughout (per audit Concern 2.1).

---

## Patch 2: §8.7.7 — helicity bookkeeping clarification (Tier 2)

**Location:** Master Part 2 (Drive ID `1LQQqg7TDoCL9uVCc7zZ2KLhwPzLN9ts3`), §8.7.7 paragraph 3 (the Majorana count paragraph).

**Find (current text in v10.8 Part 2 §8.7.7):**

```
The Majorana condition — required independently by the dark matter κ derivation (Section IX) — removes the independence of right-handed neutrinos from left-handed antineutrinos: 48 − 3 = 45 independent Weyl fermion species per sector. Including antiparticles: 45 × 2 = 90 = NTE species count ✓.
```

**Replace with:**

```
The Majorana condition — required independently by the dark matter κ derivation (Section IX) — removes the independence of right-handed neutrinos from left-handed antineutrinos: 48 − 3 = 45 independent Weyl fermion species per sector. Including helicity (counting LH-particle helicity and RH-antiparticle helicity separately per LH Weyl field, on-shell): 45 × 2 = 90 physical fermionic d.o.f. = NTE species count ✓.
```

**Rationale:** The phrase "× 2 antiparticles" was pedagogically opaque — it read as suggesting two distinct particles being counted, when the count is actually two helicity states per LH Weyl field. Audit (May 2026) recommended the clarification to make the bookkeeping transparent for non-specialist readers and to align §8.7.7 explicitly with §17.5.10's helicity-doubling step. The clarification preserves the numerical result (45 × 2 = 90) and the cross-check sentence that follows unchanged.

---

## Patch 3: §XVII Parameter Accounting — framing upgrade (Tier 3)

**Location:** Master Part 3 (Drive ID `1eiXLCZE2bLlhdIpjGtzFVBzOsUzdGFTg`), two passages in §XVII PARAMETER ACCOUNTING.

### Patch 3a — "Derived Within Framework" listing

**Find (current text):**

```
- Three generations and 90 species from J₃(𝕆) + Majorana condition (v10.4)
```

**Replace with:**

```
- Three generations and 90 species from J₃(𝕆) + Majorana condition (v10.4; explicit reduction to SM physical fermionic d.o.f. closed by enumeration v10.9, §17.5.10)
```

### Patch 3b — "(E) Postdictions" listing

**Find (current text):**

```
- 90 species from J₃(𝕆) + Majorana (consistent with SM count; same status as three generations).
```

**Replace with:**

```
- 90 species from J₃(𝕆) + Majorana — derivation chain (J₃(𝕆) → 16/gen → Majorana → 15/gen × 3 = 45; helicity doubling → 90) and identification with SM content (72 Dirac quarks + 12 Dirac charged leptons + 6 Majorana neutrinos = 90) both complete v10.9 (§17.5.10), with g_eff = 106.75 cross-check tying species count and β_NTE characterisation (§2.4.2) into one mutually self-consistent enumeration.
```

**Rationale:** Tier 3 framing upgrade per audit. The "consistent with SM count; same status as three generations" framing was honest understatement against v10.6/v10.8 baseline; under §17.5.10 v10.9 closure the framing is "derivation + identification both complete, with structural self-consistency cross-check" — stronger than mere consistency, tied explicitly to β_NTE characterisation through g_eff. The "Derived Within Framework" entry gets a parenthetical tag pointing at the closure section.

---

## Patch 4: §17.5.12 — falsifiability catalogue consolidation

**Location:** Master Part 3 (Drive ID `1eiXLCZE2bLlhdIpjGtzFVBzOsUzdGFTg`), §17.5.12 in full.

**Find (current text in v10.8):**

```
17.5.12 Falsifiability Statements for All Zero-Parameter Predictions

The framework's zero-parameter predictions (§17 category A) carry falsifiability commitments that should be made explicit:

- κ = 5.50 ± 0: falsified if observed DM:baryon ratio moves beyond the framework's claimed precision under improved measurement; or if direct DM detection observes a signal inconsistent with mirror-universe gravity coupled through the neutrino backbone.

- n_s = 0.9685: falsified if CMB-S4 / LiteBIRD measurements tighten n_s constraints to ±0.001 with central value remaining at 0.9649 ± 0.002 (push to >2σ discrepancy).

- r = 0.0030: falsified if CMB-S4 / LiteBIRD bound r < 0.0010 at 95% confidence.

- δ_J = π/2: falsified if DUNE / Hyper-K measurements of δ_CP converge on a value significantly different from -π/2 (the Janus-geometry prediction is for maximal violation).

- θ₂₃ = π/4 in limit δ_CP → 0: falsified if combined long-baseline measurements (NOvA + T2K + Super-K + DUNE) produce a central value departing from π/4 by more than the framework's δ_CP-correction allows.

- 0νββ Majorana prediction: KamLAND-Zen, GERDA, LEGEND limits on m_ββ tightening into the inverted-hierarchy regime without observation would push against the Majorana commitment. The framework should commit to a specific m_ββ prediction within the next major version.

Research target: every zero-parameter prediction should carry an explicit falsifiability commitment of the form *"this prediction is falsified by observation X with significance threshold Y."* The list above is a starting catalogue; making each commitment precise (with the experiment, the observable, and the threshold) is structural work.
```

**Replace with:**

```
17.5.12 Falsifiability Catalogue: Zero-Parameter and Structural Predictions (Consolidated v10.9)

The framework's zero-parameter predictions (§XVII category A), structural commitments with falsifiability footprints (§XVII category G), postulates (§XVII category F), and post-derivation enumerations (§XVII category E) carry explicit falsifiability commitments in the form *"prediction P is falsified by experiment E observing observable O at threshold T by programme milestone M."* The catalogue is calibrated to current public-roadmap programme sensitivities; revisions track programme reports.

**Category A — zero-parameter predictions:**

- **κ = 5.50 ± 0** (DM:baryon ratio): Planck 2018 measures κ_obs = 5.38 ± 0.15 (0.83σ from prediction). Falsified by CMB-S4 reaching σ(κ) ~ 0.075 with central value > 3σ from 5.50 (i.e. outside [5.27, 5.73] band under tightened uncertainty), milestone CMB-S4 first cosmology results mid-2030s. Complementary falsification: direct DM detection (XENONnT, LZ, PandaX-4T, DarkSide-20k) observing a WIMP-like signal whose phenomenology is inconsistent with mirror-gravity coupling through the unresolved neutrino backbone (§9.1) — milestone ongoing through current and next-generation runs.

- **n_s = 0.9685** (CMB scalar spectral tilt): Planck 2018 measures n_s = 0.9649 ± 0.0042 (0.85σ from prediction). Falsified by CMB-S4 / LiteBIRD reaching σ(n_s) ~ 0.0005 with central value > 3σ from 0.9685 (i.e. outside [0.967, 0.970] band under tightened uncertainty), milestone CMB-S4 / LiteBIRD first cosmology results late-2020s through 2030s. The η-correction route (§18.6) provides post-derivation tightening pending V_NTE boundary action work (Programme S Paper S2); pre-derivation tightening would close the residual 0.85σ.

- **r — three-readings status per §18.4 v10.8:** NTE has three structural readings of the effective inflaton dynamics with different r predictions: (i) Literal NTE constraint Φ⁴-chaotic → r = 0.25 (already 7σ ruled out by current Planck/BICEP bound r < 0.036; ruled-out reading); (ii) Stage 3 Session 3 Gaussian saddle Φ²-chaotic → r = 0.126 (already 3.5σ disfavoured under current bound; disfavoured reading); (iii) Hilltop from V_NTE^pre Φ⁴ − Φ⁶ smooth connection → r ≈ 4×10⁻³ (Session 4 §4.5 structurally favored; consistent with current bound). Reading (i) falsified definitively at Simons Observatory sensitivity (σ(r) ~ 0.003), milestone first results 2025-2027. Reading (ii) falsified definitively at CMB-S4 / LiteBIRD sensitivity (σ(r) ~ 10⁻³), milestone 2030s. Reading (iii) — the structurally favored reading — falsified by either (a) CMB-S4 / LiteBIRD bound r < 10⁻³ at 95% CL with no detection in [10⁻³, 10⁻²] (ruling out hilltop ≈ 4×10⁻³), or (b) detection r > 10⁻² at >5σ. Full first-principles closure of which reading is the true derivation depends on K(Φ) functional form via Connes spectral-triple programme (Paper S2).

- **δ_J = π/2** (PMNS CP-violating phase, maximal violation from Janus geometry; §10.1): Current T2K 2020 + NOvA combined fits hint at near-maximal violation (δ_CP near −π/2) with σ(δ_CP) ~ 30°. Falsified by DUNE + Hyper-Kamiokande reaching σ(δ_CP) ~ 10° with central value > 3σ from ±π/2 (i.e. outside ±[60°, 120°] band), milestone DUNE first oscillation results mid-2030s; Hyper-K first results late-2020s through 2030s. The Janus-geometry prediction is for maximal violation in absolute value; the sign (+π/2 vs −π/2) is set by the spontaneous CPN selection at temporal locking.

- **θ₂₃ = π/4 in limit δ_CP → 0** (PMNS atmospheric mixing angle; §19.1): Current combined fits (NOvA + T2K + Super-K) give sin²θ₂₃ near 0.5 with mild preference for upper octant; observed 45.0° ± 1.0° (consistent with prediction). Falsified by DUNE + Hyper-K combined long-baseline measurements reaching σ(θ₂₃) ~ 0.5° with central value > 3σ outside the prediction band π/4 ± Δ_CPV (where Δ_CPV is the framework's δ_CP-correction allowance — currently bounded by the δ_J = π/2 maximal-violation commitment to give Δ_CPV ≲ 2°; tightening Δ_CPV is a research target — see closing list below), milestone DUNE / Hyper-K through 2030s.

- **0νββ Majorana commitment** (Majorana neutrinos forced by §8.7.9 orbifold convergence + §9.3 cross-thickness κ): Current KamLAND-Zen bound m_ββ < ~50 meV (90% CL). Falsified by next-generation experiments (LEGEND-1000 target σ(m_ββ) ~ 10 meV; nEXO ~5-10 meV; CUPID-Mo / CUPID; KamLAND2-Zen) producing a null result deep into the inverted-hierarchy regime (specifically: bound m_ββ < 5 meV at 90% CL under IH, milestone late-2020s through 2030s) without observation, which would push against the Majorana commitment under any plausible NH/IH realisation given M_R = 8.2 × 10¹⁴ GeV (§19.2). Note: a specific NTE m_ββ prediction (NH/IH dependence + Majorana phases anchored on M_R and Janus structure) is research target for v10.9+ — until that prediction is in place, the catalogue commitment is the Majorana convention itself, not a specific m_ββ band.

**Category G — structural commitments with falsifiability footprints:**

- **σ(κ; M) ∝ M^{−1/2}** (DM:baryon variance scaling above coherence scale M_c ~ 4.4 × 10¹⁴ M_☉; Gap 4 closed, §9.4): Falsified by precision DM:baryon distribution measurements (DESI, SDSS, LSST/Vera Rubin, Euclid) showing scaling significantly different from M^{−1/2} in the super-coherence regime (M > 10¹⁴ M_☉) at >3σ, milestone DESI DR3+ through 2027, LSST first 10-year data through 2030s. Note: M^{−1/2} scaling is generic to spatially uncorrelated DM-lump models; the NTE-specific commitment is the combination of the scaling law with the mean value κ ≈ 5.50 and the specific coherence scale M_c set by neutrino free-streaming.

- **Void-enhanced local H₀ directional signature** (Hubble tension reading; §13.2): NTE predicts σ(H₀) ~ 2-4 km/s/Mpc directional scatter correlated with line-of-sight matter density (overdense LOS → lower H₀, underdense → higher H₀). Falsified by directional analysis of SNe Ia catalogues (Pantheon+, DES SN, LSST/Vera Rubin) showing no correlation between local H₀ and line-of-sight matter density at the predicted amplitude or higher, milestone Pantheon+ extensions through 2026-2027, LSST through 2030s.

- **w_obs > −1 at low z with diagnostic signatures, vs constant w deviation** (dark-energy as geometric unloading; §12.4): NTE predicts w_true = −1 exactly with w_obs > −1 at low z arising from void-enhancement bias, growing with structure formation, vanishing at high z. Falsified by persistent evidence for w ≠ −1 that does NOT show the four diagnostic signatures: (a) departure correlated with void fraction along line-of-sight; (b) departure diminishing at higher z, tracking σ_8²(z)/Ω_Λ(z); (c) departure vanishing under cosmic-variance correction; (d) CMB κ at z ~ 1100 not showing the same bias. Milestone DESI DR3+ (2026-2027), Euclid first cosmology results (2026-2027), LSST through 2030s.

**Category F — postulates with falsifiability footprints:**

- **Ω_K = 0** (closed S³ universe with sufficiently large curvature radius): Current Planck 2018 measures Ω_K = -0.001 ± 0.002 (consistent with flat). Falsified by future combined CMB + BAO + lensing measurement (LiteBIRD + Simons Observatory + DESI + Euclid combined) reaching σ(Ω_K) ~ 5×10⁻⁴ with central value > 5σ from 0 in either direction, milestone late-2020s through 2030s. NTE's commitment is Ω_K = 0 by boundary-only ontology (§16); the falsification threshold tracks the curvature-radius lower bound set by current measurements — the framework requires sufficiently large S³ curvature radius such that current measurements bound rather than refute it.

**Category E — derived enumerations with falsifiability footprints:**

- **Three generations** (from dim su(2) = 3): Falsified by direct discovery of a fourth-generation fermion (quark or charged lepton) at any collider — current LHC bounds m_4 > 1.5 TeV — or by robust observation of a fourth light neutrino species from BBN/CMB N_eff measurements consistent with N_eff > 3.5. Milestone LHC continuing through 2030s; HL-LHC through 2040s; future colliders (FCC-hh, muon collider) extending coverage.

- **90 species from J₃(𝕆) + Majorana** (§17.5.10 v10.9 closure): The species enumeration and the β_NTE characterisation (§2.4.2) are mutually self-consistent at g_eff = 106.75. Falsified by any precision determination of g_eff at T > T_EW deviating from 106.75 at greater than Planck-era uncertainty, OR by independent SM-content enumeration finding ≠ 90 physical fermionic d.o.f. under Majorana convention. Milestone via electroweak precision observables (continued LHC + future colliders + cosmological g_eff inference from N_eff and CMB precision); current cross-check at Planck-era uncertainty already in place.

**Closing.** The catalogue tightens the §II.0 working bet: predictions whose failure modes are not specified are not predictions. Each entry above specifies the falsification threshold against current public-roadmap programme sensitivities. The list closes the consolidation work flagged in v10.4–v10.8; ongoing maintenance requires updating milestone dates and central-value statistics as programmes report. New entries for predictions added in future versions follow the same canonical form.

**Research targets for v10.9+ falsifiability catalogue tightening:**
- (i) Explicit m_ββ prediction for the 0νββ commitment (NH/IH dependence + Majorana phases anchored on M_R and Janus structure).
- (ii) σ_c amplitude calculation for the σ(M) ∝ M^{−1/2} variance scaling (referenced in §9.4 as open).
- (iii) Sharper Δ_CPV bound on the θ₂₃ falsification band once full δ_J phenomenology is computed.
- (iv) Quantitative δw(z) bias profile from the void-enhancement mechanism, calibrated against current N-body + cosmic-variance baselines for direct comparison with DESI DR3+ / Euclid / LSST analyses.
```

**Rationale:** Six existing commitments tightened to canonical form (experiment / observable / threshold / milestone) with current statistical status preserved where available. The r-commitment updated to v10.8 three-readings structure per §18.4, with each reading getting its own falsification threshold — this is the most substantive content update, since v10.4's "r = 0.0030 falsified if r < 0.0010" is no longer the corpus's r-prediction structure. Five new commitments added (σ(M) variance, void-enhanced H₀, w(z) low-z signature, Ω_K = 0, three generations, 90 species — covering categories E/F/G from §XVII that were missing falsifiability footprints). Cross-link to §17.5.10's enumeration closure makes the 90-species count a falsifiability anchor in the consolidated catalogue. Closing paragraph reframes from "research target / starting catalogue" to "consolidation closed / ongoing maintenance" with four explicit v10.9+ tightening targets named.

---

## What is NOT patched

The following passages were considered and judged not in scope for A6:

- **§XVII Parameter Accounting Category B (Tested Predictions With Caveats)**: σ(M) ∝ M^{−1/2} and void-enhanced local H₀ entries — referenced in §17.5.12 Category G (Patch 4) for falsifiability, but the Category B prose itself is at the right register and not modified.
- **§XVII Category C (Partial Predictions / Work in Progress)**: ⁷Li/H, sin²θ₁₂, θ₁₃ entries — these are work-in-progress with partial closures, not zero-parameter predictions, and live in the partial-predictions register that §17.5.12 does not cover. Future falsifiability commitments may add these when their closures complete.
- **§17.5.10's cross-references to other sections** (§II.0, §9.3, §VIII): no changes — the closure does not propagate into structural arguments elsewhere; it's a status update internal to §17.5.10's content.
- **§17.5.11 (graded fulfilment) / §17.5.13 (Born rule scope) / §17.5.14 (n_s status) / §17.5.15 (ξ = 1/6)**: all canonical; no changes.
- **§II.0 working bet closing paragraph**: untouched. A6 tightens the §17.5.12 catalogue; the §II.0 discipline statement that motivates the catalogue stands unchanged.
- **Companion 7 v10.8** (neutrino backbone) and **Companion 5 v10.8** (state space) cross-references to §17.5.12: reference the catalogue but don't reproduce its content; no companion-level ripple required. A6 deliverable is master-corpus-only.
- **Book Chapter 8 or Chapter 9** (if/when those discuss the falsifiability catalogue): no chapter-level patches required at this version; chapter alignment can ride a future Book/ ship arc once master v10.9 is canonical.

---

## Cleanup batch reference

Once Greg has rendered Patches 1–4 into the local master (Part 2 §8.7.7 + Part 3 §17.5.10, §XVII §17.5.12 ×4), master v10.9 will be ready for Drive re-upload (replacing or supplementing the current v10.8 files). At that point:

- Old `NTE_v10_8_Part2_Structure.md` (Drive ID `1LQQqg7TDoCL9uVCc7zZ2KLhwPzLN9ts3`) → v10.8 predecessor (Papers/depreciated/).
- Old `NTE_v10_8_Part3_Accounting.md` (Drive ID `1eiXLCZE2bLlhdIpjGtzFVBzOsUzdGFTg`) → v10.8 predecessor (Papers/depreciated/).
- Old `NTE_v10_8_Part1_Foundations.md` (Drive ID `1JfYKKsi1elHM1tK3bO2GYVzpmY_5xcaP`) → v10.8 predecessor (Papers/depreciated/) if v10.9 carries any Part 1 patches; otherwise this part is unaffected by A6 and can be carried across without renaming.
- New v10.9 Parts uploaded to Papers/; AC's next session reconciles Project State + Live Register + Chapter State Ledger against the new master.

This patch-instruction document is itself a working artifact; once rendering is complete, it can be moved to Working/depreciated/ at Greg's convenience.

**Sequencing with A5:** Greg's call. Options:
- (i) A5 lands first as v10.8 v2 (Born rule scope alignment only, surgical), then A6 lands as v10.9 — two render passes;
- (ii) A5 + A6 bundle as v10.9 — one render pass, larger;
- (iii) Other sequencing per Greg's preference.

---

**Cross-references:**

- §17.5.10 v10.9 (Patch 1) — closure of 90 species → SM content reduction
- §8.7.7 v10.9 (Patch 2) — helicity bookkeeping clarification
- §XVII v10.9 (Patch 3a, 3b) — Parameter Accounting framing upgrade
- §17.5.12 v10.9 (Patch 4) — falsifiability catalogue consolidation
- §2.4.2 — β_NTE characterisation (g_eff = 106.75 anchor; unchanged, referenced by Patches 1, 3, 4)
- §17.5.11 v10.6.1 — graded fulfilment register (governing for §17.5.12's Category E entries; unchanged)
- §18.4 v10.8 — r prediction three-readings status (governing for §17.5.12 r-commitment update; unchanged)
- §10.1, §19.1 — Janus / PMNS structural inputs (governing for δ_J and θ₂₃ commitments; unchanged)
- §8.7.9, §9.3 — orbifold + cross-thickness κ Majorana convergence (governing for 0νββ commitment; unchanged)
- §9.4 — Gap 4 (DM:baryon variance scaling; governing for σ(M) commitment; unchanged)
- §12.4 — DESI / w(z) diagnostic signatures (governing for low-z dark-energy commitment; unchanged)
- §13.2 — Hubble tension reading (governing for void-enhanced H₀ commitment; unchanged)
- §16 — boundary-only ontology (governing for Ω_K = 0 commitment; unchanged)
- May 2026 AC→Jammer audit handoff `11e1A8XITBGnbVPfE9uCjZQ8cdmS7E0hv` — source of Tier 1/2/3 recommendations
- A5 patch instructions `1r4twq1yqEq3NvUmBDco5K1kfNIpsBc-2` — independent surgical ship; sequencing with A6 at Greg's discretion

— AC (2026-05-23, A6 ship deliverable)
