# Cosmic Dipole Anomaly — Axiom Filter Pass (Scratch v0.1)

**Author:** Scratch (Connes Programme lead)
**Date:** 2026-05-27
**Trigger:** Greg directive 2026-05-27 ("we should start immediately on the Cosmic Dipole") following External Empirical Surface scoping (`Working/External_Empirical_Surface_Strange_Quantum_Experiments_Scoping_Scratch_v0_1_20260527.md`)
**Template:** Modelled on `Penrose_Palatial_Twistors_Axiom_Filter_Pass_Jammer_v1.md`, `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`
**Status:** v0.1 substantive verdict; derivation queue open; awaits Jammer cross-check + CR review

---

## §1 — The phenomenon

**Empirical summary.** The CMB temperature dipole, of amplitude ~3.36 mK, is conventionally interpreted as the Doppler signature of our peculiar velocity ~370 km/s relative to the CMB rest frame. The Ellis-Baldwin (1984) test predicts that, if the matter distribution shares this rest frame (i.e. the cosmological principle holds), then galaxy and quasar number-count distributions should show a *matching* dipole of Doppler-aberration origin with the same direction and magnitude.

Observations disagree. The most thorough current analyses:

- **Secrest et al. (2021)** *ApJ Letters* — 1.36M CatWISE2020 quasars. Direction within ~28° of CMB dipole; amplitude **2.7× the kinematic expectation**. Significance 4.9σ (one-sided), p ~ 5×10⁻⁷.
- **Bayesian reanalysis (Dam et al. 2023)** — same CatWISE sample. Direction confirmed; amplitude 2.7×; significance pushed to **5.7σ**.
- **Wagenveld et al. (2025)** — NVSS + RACS-low radio galaxy catalogues. Confirmed matter dipole amplitude ~3–4× kinematic; direction aligned with CMB.
- **Singal (2025)** *Sci. Rep.* — Quaia catalogue (1.3M quasars) redshift dipole implies peculiar velocity **~1700 km/s**, with direction pointing **near the Galactic Centre — ~90° away from the CMB dipole**.
- **Böhme et al. (2025)** *Phys. Rev. Lett.* 135, 201001 — "Overdispersed Radio Source Counts and Excess Radio Dipole Detection." Confirms excess.
- **Shamir (2024/2025 JADES)** — JWST deep field near Galactic pole shows ~50% more galaxies rotating one way than the other.
- **Secrest, von Hausegger, Rameez, Mohayaee, Sarkar (2025)** *Rev. Mod. Phys.* 97, 041001 (Dec 2025) — colloquium consolidating the case as a serious challenge to FLRW.
- **Pushback (Abghari et al. 2024)** — argues mask-coupling between ℓ=1 and higher multipoles inflates significance. Rebutted by Secrest et al. (2025).

The empirical pattern, robustly: **matter dipole magnitude is 3–4× the kinematic expectation from the CMB dipole**, with broad directional alignment to CMB for radio/IR samples but a differently-directed redshift dipole for Quaia. ΛCDM has no clean explanation. The cosmological principle, an assumption of the FLRW substrate, is under direct empirical strain at >5σ.

## §2 — Why NTE has a stake

The κ derivation in `Paper_Kappa_PathwayB_v10_6.md` §4.3 and §5 makes explicit use of two things to fix κ₁ = Y₀₀:

1. **The coupling channel is the monopole (ℓ = 0).** This is enforced by (a) the CPN parity selection rule (which forbids odd-ℓ couplings of the cross-thickness gravitational kernel) and (b) the isotropy of the gravitational interaction (no preferred direction on S²) which means the dominant coupling is at lowest permitted ℓ.

2. **The normalisation of the monopole harmonic on unit S²** — Y₀₀ = 1/√(4π).

§5.2 explicitly invokes the cosmological-principle isotropy assumption as observational input: *"on cosmological scales, observations confirm the dark matter distribution is statistically isotropic (consistent with spatial flatness and the cosmological principle). The ℓ = 2 contribution is therefore zero at leading cosmological order and contributes only at the level of large-scale structure anisotropies (δρ/ρ ~ 10⁻⁵ at last scattering)."*

The quoted bound δ₂ ≲ 10⁻³ comes from Planck CMB constraints on CMB quadrupole anomalies. The κ correction is then bounded at ~10⁻³, "comparable to the current measurement uncertainty."

**The dipole anomaly is at ℓ = 1, not ℓ = 2.** The CPN parity selection rule forbids ℓ = 1 in the cross-thickness coupling. So a real cosmic dipole anomaly at the matter-distribution level — *if it propagates to the gravitational coupling kernel* — would either:

(a) be parity-forbidden in NTE's cross-thickness coupling (and therefore *intrinsically expected to be small* in the channel relevant to κ), or
(b) signal a breakdown of the CPN parity assumption, which is a structural axiom of the corpus, not just empirical input.

The corpus has more stake here than the κ-derivation alone. NTE's S³ × S¹ topology and the Hopf-fibration structure of the gauge birth (Companion 6) carry directional information at the level of the manifold. The cosmic dipole is exactly the regime where such directional information would imprint on observations.

## §3 — NTE axioms touched

- **A1. N fundamental, t emergent.** The "cosmic rest frame" is defined by Φ_NTE coherence + thermal time (Connes-Rovelli affinity, per `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`). Not by a textbook FLRW frame.
- **A2. Surface only / S³ × S¹ uniqueness** (Paper S2 §5.4). Closed spatial S³; finite volume; intrinsically isotropic at manifold level.
- **A3. Hopf fibration S³ → S²** (Companion 2, 4, 6). Selects a U(1) axis on S³ — the "gauge-birth axis." Locally meaningful (sets SU(2) orientation); globally fixed by field configuration.
- **A4. CPN parity selection rule** (Paper Kappa PathwayB §5). Forbids odd-ℓ in cross-thickness gravitational kernel. Load-bearing for κ derivation.
- **A5. Mirror-orientation dark matter** (Part 1 §6.3, Part 2 mirror-matter section). Z₂-even on the orbifold; gravitationally coupled across the N-thickness.
- **A6. Void-bias mechanism** (Part 2 §12.4, §13.2; Jammer 2026-05-27 worksheet). Local underdensity gives H_local > H_hom; geometrically explained.

## §4 — Axiom-by-axiom check

### A1 (N fundamental, t emergent — and the cosmic rest frame)

The standard interpretation of the CMB dipole — "we are moving at 370 km/s relative to the cosmic rest frame" — assumes the existence of a single preferred frame in which both radiation and matter distributions are isotropic. In NTE, the cosmic rest frame is a **derived** concept: it's the frame in which Φ_NTE has its uniform asymptotic value and in which the thermal-time modular flow corresponds to global cosmic time.

There is no axiom-level requirement that the *kinematic* matter rest frame coincide with the *thermal* radiation rest frame. In the FLRW idealisation they do; in a universe with structure (voids, filaments, |Φ_NTE| inhomogeneity per Part 2 §13.2), they may not. **NTE is structurally compatible with a discrepancy between the matter dipole frame and the CMB dipole frame** — the discrepancy reflects the structure that has accumulated since recombination, including any |Φ_NTE| field gradients on cosmological scales.

**Verdict on A1: compatible, possibly illuminating.** The dipole anomaly's natural reading is "the matter frame and the radiation frame don't coincide." NTE makes structural room for this without strain.

### A2 (S³ × S¹ topology)

S³ as a manifold is isotropic. A closed S³ has finite volume and no preferred direction at the geometric level. So at the manifold level alone, NTE does not predict a global preferred direction.

**Verdict on A2: neutral.** Closed S³ does not by itself yield a dipole. (See A3.)

### A3 (Hopf fibration — the gauge-birth axis)

Here is where it gets interesting. The Hopf fibration S³ → S² × S¹ is *not* unique — there is a 3-parameter family of Hopf fibrations on S³, related by SO(4) rotations. **But for the gauge-birth construction (Companion 6) to define a consistent SU(2) structure, one Hopf fibration must be selected globally.** Once selected, it picks out a U(1) axis on S³ — the "gauge-birth axis."

This axis is *physically* the direction along which the U(1) ⊂ SU(2) gauge action winds the Hopf fibres. Locally it sets the orientation of the SU(2) gauge structure; globally it is a *fixed direction in the cosmic S³*.

If matter distributions formed during or after gauge birth inherit anisotropy aligned with this axis (e.g., from primordial inflationary fluctuations with a Hopf-axis-preferred power), this would imprint as a dipole in matter at all subsequent redshifts.

**This is a candidate mechanism**, not a derivation. The actual question is whether the |Φ_NTE| field configuration at gauge birth respects or breaks the Hopf-axis isotropy in the angular distribution of resulting matter perturbations. If it preserves isotropy (the gauge axis is locally meaningful but globally averaged), no dipole is predicted from this mechanism. If it doesn't, a dipole aligned with the Hopf axis is predicted.

**Verdict on A3: candidate mechanism; open derivation; *potentially load-bearing*.**

### A4 (CPN parity selection rule)

The CPN parity selection rule forbids ℓ = 1 in the cross-thickness *gravitational coupling kernel*. This is a structural axiom of the κ derivation. The matter dipole observed in quasars/radio galaxies is in *visible matter*, not in the cross-thickness coupling kernel.

These are different objects. The visible matter dipole is the spatial number-count anisotropy of quasars/galaxies. The cross-thickness coupling kernel is a tensorial coupling between the two CPN-conjugate orientations. The visible matter dipole *cannot directly affect* κ — the parity rule is preserved at the kernel level regardless of what the matter distribution does.

**However**, the κ derivation §5.2 also uses the matter distribution's quadrupole δ₂ ≲ 10⁻³ as input to bound the ℓ = 2 correction to κ₁. If the dipole anomaly indicates that the matter distribution has unexpected large-scale anisotropy, the *same systematics* could be hiding a larger-than-assumed quadrupole. The bound δ₂ ≲ 10⁻³ from Planck would need to be re-examined under a non-FLRW interpretation of the CMB observations.

**Verdict on A4: structurally protected at the parity-rule level; potentially vulnerable at the δ₂ bound level. Soft tension, requires bound re-derivation.**

### A5 (Mirror-orientation dark matter)

The mirror-orientation matter is Z₂-even on the orbifold and bound to both metrics through the unresolved neutrino's delocalisation across the N-thickness. It registers in our metric only gravitationally, at strength κ.

Does the cosmic dipole say anything about the mirror-orientation matter distribution? Conventionally, the matter dipole is measured in *electromagnetically luminous* tracers — quasars (radio + IR + optical), galaxies. Mirror-orientation matter is electromagnetically invisible. So the observed matter dipole is the dipole of *visible-orientation* matter.

**One illuminating point**: if there were a comparable dipole in mirror-orientation matter, it would only show up gravitationally (via lensing, BAO geometry, growth of structure). Disentangling visible-matter-dipole from mirror-orientation-matter-dipole would be a future test. NTE structurally allows the two to be different.

**Verdict on A5: compatible; suggests new test (mirror-matter dipole via lensing/BAO).**

### A6 (Void-bias mechanism)

Jammer's `LCDM_Void_Bias_BAO_Worksheet_Jammer_v0_1_20260527.md` establishes that NTE's void-bias mechanism (Part 2 §12.4, §13.2) produces H_eff(z) > H_hom(z) where we live in an underdensity, giving D_M and D_H shifts in a specific (D_M, D_H) directional pattern (D_M shifts more than D_H fractionally).

**A void with a preferred long axis** would yield not only a magnitude bias on H₀ but also a *directional* bias on matter-count distributions. If we are in a void whose long axis points roughly toward the CMB dipole direction, then:
- The local Hubble flow has additional anisotropy along the void axis
- Galaxy number counts at low-to-moderate z get an extra dipole contribution beyond the cosmic kinematic dipole
- This contribution adds (vectorially) to the kinematic dipole; could enhance the apparent total dipole 3–4×

**This is structurally exactly the right shape** for the observed phenomenon, and it ties directly to Jammer's void-bias work. The Singal-Quaia direction near the Galactic Centre is consistent with a local-structure (Galactic + Local Group + local void) origin pulling the apparent dipole direction toward our local mass distribution rather than the cosmic kinematic frame.

**Verdict on A6: highly compatible; this is the leading-candidate NTE-internal explanation. Directly couples to Jammer's existing void-bias H₀ work.**

## §5 — Candidate NTE-distinctive readings (three branches)

The axiom check leaves NTE with **three structurally-viable readings** of the cosmic dipole anomaly. They are not mutually exclusive; in fact each captures a different physical scale.

### Branch I: Local-void anisotropy (low-z dominated)

We are in a local underdensity with a preferred long axis. The local void's gradient adds anisotropy to galaxy number counts at z < ~0.5, giving an additional dipole contribution on top of the kinematic dipole. This is *local cosmology*, not new physics — but it inherits NTE's void-bias framework (Part 2 §12.4, §13.2; Jammer 2026-05-27 worksheet).

**Predictions**:
- Matter dipole amplitude redshift-dependent: large at low z, declining at high z
- Direction aligned with local void's long axis (close to CMB direction by coincidence of structure)
- Should correlate with anomalies in nearby galaxy peculiar-velocity surveys (the "cosmic flow" puzzle)
- Connects directly to Jammer's H₀ + w_obs bias story

**Status**: most structurally connected to existing corpus; immediately actionable via Jammer's worksheet framework extended to directional data.

### Branch II: Hopf-axis primordial imprint (all-z)

Gauge birth at N_lock with a globally-fixed Hopf fibration leaves a residual anisotropy in the primordial matter power spectrum aligned with the Hopf-axis. This anisotropy persists at all redshifts after recombination.

**Predictions**:
- Matter dipole amplitude approximately z-independent (modulo growth factors)
- Direction fixed by the global Hopf axis — *which we cannot directly measure*, but it should be consistent across independent tracers at different redshifts
- The CMB temperature dipole would itself have an intrinsic component aligned with the Hopf axis
- The CMB *polarisation* dipole would carry distinct signatures (parity structure of the Hopf-axis imprint)

**Status**: speculative; would require an inflationary/primordial calculation under NTE that has not yet been done. Sits in the "candidate unique prediction" territory if it could be derived.

### Branch III: Thermal-time frame discrepancy (intrinsic)

If the matter rest frame is defined by Φ_NTE coherence and the radiation rest frame by photon thermal equilibrium at last scattering, the two frames may not coincide globally. The CMB dipole is *partly kinematic* (our local motion) and *partly intrinsic* (the frame mismatch). The matter dipole then reveals more of the intrinsic component.

**Predictions**:
- Direction of matter dipole and CMB dipole may differ — exactly the Singal-Quaia anomaly direction toward Galactic Centre
- Amplitude of "true" peculiar velocity (from Φ_NTE frame) somewhere between 370 and 1700 km/s
- Could couple to Φ_NTE field-gradient measurements (do these exist?)

**Status**: deepest of the three; requires Φ_NTE-frame analysis that has not been formalised. Connects to the Connes-Rovelli thermal-time filter pass.

### Which branch is operative?

Most likely: **Branch I dominant at low z, Branch III subdominant at high z**, with Branch II providing the boundary condition. The empirical signature distinguishing them is the *redshift dependence* of the matter dipole amplitude. The CatWISE quasar sample is heavily z ~ 0.5–2; Quaia covers z up to ~3. If the matter dipole is local-structure-dominated, it should decline with z; if Hopf-axis-primordial, roughly flat; if thermal-time-intrinsic, roughly flat with possible directional drift.

**Existing data partially distinguishes**: the Quaia direction toward Galactic Centre versus CatWISE direction near CMB *is* a hint of redshift-dependence in the dipole vector. Jammer follow-up needed.

## §6 — Honest scope

What this filter pass does *not* establish:

- It does **not** derive the cosmic dipole magnitude from NTE first principles.
- It does **not** prove any of the three branches; they are *structurally-viable candidates*.
- It does **not** claim that NTE predicts the observed dipole. It claims that NTE's structural ingredients (Hopf axis, void bias, Φ_NTE frame) provide **three independent candidate mechanisms**, any of which could yield such a signature.
- Branch II in particular requires explicit primordial-anisotropy derivation under the Hopf-fibration structure that has not been done. *Vocabulary-inheritance trap (Lesson #34): "Hopf-axis dipole prediction" is not yet earned.*
- The δ₂ bound used in the κ derivation (≲ 10⁻³ from Planck) needs explicit re-examination under a non-FLRW interpretation of the CMB.

What this filter pass *does* establish:

- The cosmic dipole anomaly is **structurally compatible** with NTE. It is not a falsifier as currently understood.
- It is **potentially illuminating** — three NTE-distinctive candidate mechanisms suggest themselves and at least one (Branch I, void-bias) is directly continuous with active corpus work (Jammer 2026-05-27).
- The κ derivation has a **soft vulnerability** at the δ₂ ≲ 10⁻³ input; this bound was extracted under FLRW assumptions and should be re-derived under whatever cosmology resolves the dipole anomaly. The vulnerability is *probably benign* — δ₂ is the ℓ=2 quadrupole and the dipole anomaly is at ℓ=1, but the bound was derived from a global FLRW fit that the dipole results undermine.
- The CPN parity selection rule is **structurally protected** at the kernel level — visible-matter dipole anisotropy cannot directly affect κ regardless of magnitude.

## §7 — Falsifier screen against §17.5.12

The §17.5.12 falsifier set (per `Cursor_NTE_Unique_Predictions_Catalogue_v0_1_20260527.md`) covers κ band, n_s band, r threshold, δ_J maximal, θ_{23} maximal, 0νββ Majorana, 3 generations, no W_R, no WIMP, void H₀/w diagnostics, σ(κ;M) scaling, Ω_K = 0, 90 species g_eff.

**Cross-check:**

- κ band: §6 soft vulnerability flagged (δ₂ bound re-derivation needed). Probably benign at the dipole level (ℓ=1, not ℓ=2). Jammer follow-up should re-derive δ₂ under whatever cosmology resolves the dipole.
- void H₀/w diagnostics: **strengthened, not threatened.** Branch I directly extends Jammer's existing void-bias H₀ work to a directional signature.
- Ω_K = 0: closed-S³ flat-universe statement — dipole anomaly is orthogonal to spatial curvature. Untouched.
- All other falsifiers: untouched (none operate on the dipole channel).

**Verdict on §17.5.12 screen**: No existing falsifier is broken. One (κ band) has a *soft vulnerability* requiring follow-up. One (void H₀/w) is *strengthened*. Net: positive structural finding.

## §8 — Derivation queue this opens

For Jammer (R&D primary):

1. **Branch I (highest priority).** Extend the void-bias D_M/D_H framework (Jammer 2026-05-27 v0.1) to include directional anisotropy from local void's long axis. Predict matter dipole contribution from void-axis + kinematic vector sum. Compare to Singal-Quaia direction (Galactic Centre) and CatWISE-radio direction (~CMB).
2. **Branch II derivation.** Compute the primordial matter power spectrum under NTE's Hopf-fibration gauge-birth assuming a globally-fixed Hopf axis. Test whether anisotropic perturbation channels open at ℓ=1. (This is genuinely open theoretical work; significant.)
3. **Branch III formalisation.** Define the Φ_NTE rest frame operationally. Does the thermal-time hypothesis (Connes-Rovelli filter pass) give a calculable offset between the matter and radiation rest frames?
4. **δ₂ re-derivation.** Re-extract the Planck quadrupole bound under a cosmology that accommodates the dipole anomaly. Tighten or loosen the κ derivation's ℓ=2 correction bound as appropriate.

For Scratch (Connes Programme):

5. The Hopf-fibration global selection question (Branch II) connects to the corpus's understanding of *which* Hopf fibration is gauge-birth-selected. This is a Connes-Programme question about the rigidity of the spectral-triple gauge structure. Worth a parallel investigation.

For AC (portfolio):

6. If Branch I yields a quantitative directional prediction matching CatWISE-or-Quaia within 2σ, the dipole becomes a candidate for the §17.5.12 / Charter-14 prediction surface. Until then it sits in the "compatibility + illumination" category, not the prediction category.

For Cursor (render lane):

7. Future popular-paper material once the derivation work matures. Probably 3–6 months out, contingent on Branch I numerical work.

## §9 — Verdict

**Compatible. Potentially illuminating. Three candidate mechanisms identified. No falsifier hit; one soft vulnerability flagged in the κ derivation's δ₂ bound; one corpus thread (void-bias H₀ work) strengthened.**

The cosmic dipole anomaly is not a threat to NTE. It is, in fact, an empirical signature whose existence the standard cosmological picture struggles with and whose shape NTE's structural ingredients (Hopf axis, void bias, Φ_NTE frame) are *unusually well-suited to accommodate*. The three candidate branches differ in their redshift dependence, which existing and upcoming data can distinguish.

**The strongest single observation** from this pass: Branch I (local-void anisotropy) is *directly continuous* with Jammer's active void-bias work. Extending the (D_M, D_H) directional signature from Jammer's morning worksheet to include local-void-axis anisotropy is the most tractable next step. If this branch closes with a quantitative match to CatWISE-or-radio dipole direction and amplitude, the cosmic dipole moves from "compatible-illuminating" to "Charter-14 prediction surface candidate."

**The most speculative-but-interesting observation**: Branch II (Hopf-axis primordial imprint) would, if derivable, constitute a genuine unique NTE prediction — a globally-fixed direction in cosmic S³ inherited from the gauge-birth construction. This is a substantial piece of theoretical work, but it sits exactly on the structural ingredients NTE has and that no other framework has. Worth Connes-Programme attention.

## §10 — Cross-stream signals

### §10.1 To Jammer (R&D primary)

The directional extension of the void-bias worksheet (your v0.1 from this morning) is the highest-priority follow-on for the dipole work. Specifically: add a local-void-axis direction to the H_eff(z, x) parameterisation in §2.1 and propagate to (D_M, D_H) per-bin. Compute resulting matter-count dipole from the void-axis component (vector-summed with kinematic dipole). Compare to CatWISE / Wagenveld / Singal data. This is potentially the closure piece for "NTE matching observation" that Greg flagged yesterday.

### §10.2 To AC (corpus integration)

§17.5.12 update candidate: add a *soft-flag* row under Category G (cosmological diagnostics) — "matter dipole excess: compatible via void-axis (Branch I); directional prediction pending Jammer derivation." Not yet a hard falsifier; not yet a prediction. *Watch-list* status.

Note also the κ-derivation δ₂ bound soft vulnerability (§6) — `Paper_Kappa_PathwayB_v10_6.md` §5.2 may need a footnote noting that the cited Planck δ₂ ≲ 10⁻³ was extracted under FLRW assumptions and that NTE's resolution of the dipole anomaly may require re-derivation of this bound.

### §10.3 To Cursor (render lane)

No render work this session. If Branch I closes, a future popular-paper "The Universe is Not Quite What We Thought It Was" piece is candidate material. Defer.

### §10.4 To Greg (recognition gates)

1. **Verdict ratification**: is "compatible, potentially illuminating, three candidate branches, void-bias is the highest-priority follow-on" the right framing?
2. **§17.5.12 watch-list addition**: ratify or defer the soft-flag row?
3. **κ derivation δ₂ vulnerability footnote**: AC patch this session, or wait for Jammer's re-derivation?
4. **Branch II Connes-Programme spawn**: spawn a dedicated Scratch Connes-Programme arc on Hopf-fibration global rigidity, or hold until Branch I closes?

## §11 — Files referenced

**Read this session:**
- `Working/LCDM_Void_Bias_BAO_Worksheet_Jammer_v0_1_20260527.md` (Jammer's 06:22Z ship)
- `Cursor_NTE_Unique_Predictions_Catalogue_v0_1_20260527.md` (Predictions Catalogue baseline)
- `NTE_Workflow_Manifest_rev6.md` rev 9 (morning sync canonical)
- Project snapshots: `Companion_4_Hierarchy_Resonance_v10_6__1_.md`, `Paper_Kappa_PathwayB_v10_6.md`, `NTE_v10_8_Part1_Foundations.md`, `NTE_v10_8_Part2_Structure.md`, `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`

**Web sources consolidated:**
- Secrest et al. (2021) *ApJL* 908 L51 — CatWISE2020 4.9σ
- Dam et al. (2023) Bayesian reanalysis — 5.7σ
- Wagenveld et al. (2025) — NVSS/RACS-low confirmation
- Singal (2025) *Sci. Rep.* — Quaia redshift dipole
- Böhme et al. (2025) *Phys. Rev. Lett.* 135, 201001
- Shamir (2024 / 2025) — JWST JADES rotation asymmetry
- Secrest, von Hausegger, Rameez, Mohayaee, Sarkar (2025) *Rev. Mod. Phys.* 97, 041001 — colloquium

---

— Scratch (Connes Programme lead), 2026-05-27. Filter pass v0.1; verdict compatible-illuminating; derivation queue open; Jammer follow-on highest-priority for closure.
