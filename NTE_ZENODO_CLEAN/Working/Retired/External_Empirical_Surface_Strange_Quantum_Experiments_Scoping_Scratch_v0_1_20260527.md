# External Empirical Surface — Strange-Quantum-Experiment Scoping for NTE Axiom Filter

**From:** Scratch (Connes Programme lead)
**Date:** 2026-05-27
**Trigger:** Greg request after Two Slits in Time popular paper (2026-05-27): catalogue other "strange" published experimental results NTE should cross-check against, identify candidates for axiom-filter passes, flag potential falsifiers and uniquely-informative tests.
**Scope:** Quantum foundations, gravity-quantum interface, cosmology beyond Charter-14 surface. Excludes already-catalogued items (κ, n_s, r, δ_J, θ_{23}, 0νββ, 3 gens, no WIMP, no W_R, void H_0/w, σ(κ;M), Ω_K).

---

## §1 — Why this matters

The Predictions Catalogue (Cursor render 2026-05-27) maps NTE's 14-prediction surface + §17.5.12 falsifiers + chord-six + V_NTE genuine-empirical layer. That surface is heavily cosmological and neutrino-sector. The quantum-foundations and gravity-quantum-interface literature contains a substantial body of published results that NTE has commitments about but has not been explicitly cross-checked against. Most will pass cleanly (compatibility, like the temporal double-slit). Some may resonate productively (Hopf-native phenomena). One or two have a non-trivial chance of being genuine tests.

This doc is a **scoping survey** for Jammer triage. It does not perform the axiom-filter passes; it identifies candidates ranked by NTE-relevance and recommends triage order.

---

## §2 — Tier A: Directly resonant with NTE structure

These touch axioms NTE has explicit commitments about. Axiom-filter passes here are potentially deeply informative — either reinforcing structural compatibility or surfacing tension that would refine the corpus.

### A1. Berry phase / geometric phase / Aharonov-Bohm-Casher
- **What:** Quantum phases that depend only on the path topology of parameter space (Berry 1984; AB-Casher 1984; Aharonov-Anandan 1987). Directly experimentally confirmed in many systems.
- **Why NTE-relevant:** NTE's Born rule derivation (Companion 2, Companion 6) is built on Hopf fibration geometry. Geometric phases are the *native* objects of that machinery. A clean axiom-filter pass should show that all Berry-phase phenomena are natural NTE outputs.
- **Filter-pass priority:** HIGH. Could be load-bearing for the Hopf/Born derivation cleanliness claim.

### A2. Neutron interferometry — 4π spinor rotation
- **What:** Spin-1/2 wavefunction picks up a sign under 2π rotation; only 4π gives identity. First observed Werner et al. 1975; Rauch 1975; extensively replicated. Direct test of SU(2) double-cover structure.
- **Why NTE-relevant:** NTE's gauge birth (Companion 6) generates SU(2) from the Hopf bundle. The 4π spinor result is exactly what that structure must reproduce.
- **Note:** COW neutron-gravity interferometry shows a persistent ~0.8% discrepancy between theory and experiment (Werner et al. follow-ons). Almost certainly systematic, but worth noting.
- **Filter-pass priority:** HIGH. Foundational SU(2) sanity check for gauge birth.

### A3. Time crystals — discrete, continuous, quasicrystal, rondeau
- **What:** Broken time-translation symmetry in non-equilibrium systems. Discrete time crystals (Choi 2017 NV centers; Mi 2022 Google Sycamore); continuous time crystals in dissipative driven-Rydberg systems (Jiao 2025 *Nat. Commun.*); time quasicrystals (He et al. 2025 *Phys. Rev. X*); **time rondeau crystals** (Moon et al. 2025 *Nat. Phys.* 21, 1813); inherent time crystal in erbium-doped solid (Russo & Pohl 2025 *Phys. Rev. Lett.*).
- **Why NTE-relevant:** "Broken time-translation symmetry" is a phrase that becomes interesting when t is emergent. NTE's commitment is that t emerges from |Φ_NTE| in the bulk; what does "breaking" of an emergent symmetry look like structurally? Likely cleanly compatible (the breaking is operational, well above the |Φ_NTE| coherence scale) — but the framing deserves an explicit pass.
- **Filter-pass priority:** HIGH. Most active area; new results landing 2025–2026; sits exactly on the emergent-t axiom.

### A4. Quantum time-of-arrival operator
- **What:** Aharonov-Bohm 1961 quantum-clock operator; revisited extensively 2024–2026 (Galapon group; Kijowski distribution; recent photon arrival-time experiments Ono 2024, Yu 2025; multi-particle interference in arrival time Ayatollah Rafsanjani et al. 2024). Direct experimental probe of time-as-observable.
- **Why NTE-relevant:** This is the formal QM machinery for treating time operationally as an observable rather than a parameter. An emergent-t framework should have a natural home for this; in fact, it should *prefer* this formulation. Could be a productive integration point with the Connes-Rovelli thermal-time hypothesis.
- **Filter-pass priority:** HIGH. Direct conceptual contact with the corpus core.

### A5. Wigner's friend and extensions
- **What:** Frauchiger-Renner 2018 paradox; Bong et al. 2020 *Nat. Phys.* extended Wigner's-friend test ruling out "observer-independent facts" under local-friendliness; Polychronakos 2024 *Nat. Commun.*; Wiseman-Cavalcanti-Rieffel 2023; Wigner's friend Qiskit IBM 2024; ongoing Brukner, Baumann theoretical work 2024–2025.
- **Why NTE-relevant:** "Surface only" + the emergent observer ontology. NTE's commitments about observer-relative facts on the S³×S¹ leaf need to be articulated against this no-go theorem landscape.
- **Filter-pass priority:** MEDIUM-HIGH. Genuinely deep question; not just compatibility.

### A6. Delayed-choice and quantum eraser
- **What:** Wheeler delayed-choice (Jacques 2007 single photons; Manning 2015 single atoms); quantum eraser (Walborn et al. 2002); now done at cosmological scales with quasar light (Rauch et al. 2018).
- **Why NTE-relevant:** Tests the temporal structure of measurement and the meaning of "moment of decision." In an emergent-t ontology, what's the status of "the photon hasn't decided yet"? Likely operational, but the axiom-filter framing is non-trivial.
- **Filter-pass priority:** MEDIUM. Direct philosophical contact with the "moment" ontology of NTE.

---

## §3 — Tier B: Foundational quantum tests NTE must pass cleanly

Sanity checks. Expected outcome: compatibility through standard QM machinery (Born rule + Hopf-derived gauge structure). Worth quick passes to make explicit; not load-bearing unless something unexpected surfaces.

### B1. Bell tests (loophole-free)
- Hensen 2015 Delft (electron spins); Giustina 2015 / Shalm 2015 (photons); ongoing tests. Local realism dead at >5σ.
- NTE: must accommodate non-local correlations. Likely clean via surface-ontology + entanglement on the leaf.

### B2. Leggett inequality tests
- Gröblacher 2007. Rules out non-local *realistic* theories of certain class.
- NTE: similar pass-through to B1, with the additional question of how surface-ontology relates to realism class.

### B3. PBR theorem tests
- Pusey-Barrett-Rudolph 2012; Ringbauer et al. 2015 experimental. Quantum state is ontic, not just epistemic.
- NTE: state lives on the surface; ontic. Likely clean.

### B4. Hong-Ou-Mandel
- HOM 1987. Two-photon bunching at beam splitter.
- NTE: bosonic statistics flows from gauge birth; should be a one-liner.

### B5. Hardy's paradox / weak values
- Aharonov-Vaidman framework; Lundeen-Steinberg 2009 experimental.
- NTE: weak measurement framework is QM-standard; passes through.

### B6. Quantum contextuality / Kochen-Specker
- Kochen-Specker 1967; Cabello group experimental tests.
- NTE: measurement outcomes context-dependent; aligned with Wigner's-friend A5 territory.

---

## §4 — Tier C: Gravity / vacuum / cosmology — NTE has direct commitments

### C1. BMV gravitationally-induced entanglement
- **What:** Bose-Marletto-Vedral 2017 proposal; tabletop test that gravity-mediated entanglement implies quantum nature of gravity. Not yet definitively performed; Selvam et al. 2025 (*arXiv* 2506.04300) propose fidelity-susceptibility probes beyond entanglement; Großardt 2025 *Phys. Rev. D* L121101 shows the (parameter-free) Diósi-Penrose model itself predicts entanglement at sub-critical separations.
- **Why NTE-relevant:** NTE has emergence-of-gravity commitments. Does NTE predict BMV-positive (gravity quantum), BMV-negative (gravity classical/emergent), or context-dependent? **This is potentially load-bearing.**
- **Filter-pass priority:** HIGH. The most likely place a published or imminent experiment could create real friction.

### C2. Diósi-Penrose collapse model (now experimentally constrained)
- **What:** Parameter-free DP model now ruled out by null underground X-ray emission searches (Donadi et al. 2021; follow-ups through 2024–2025). DP-type models constrained at unprecedented levels.
- **Why NTE-relevant:** NTE doesn't *need* gravitational collapse — the surface ontology + Born-rule structure handles the quantum-classical boundary without a collapse mechanism. The DP falsification is *evidence consistent with* NTE's structural choice. Worth explicit noting.
- **Filter-pass priority:** MEDIUM. Confirmatory, not load-bearing.

### C3. Casimir effect / vacuum energy
- Casimir 1948; Lamoreaux 1997 precision; ongoing high-precision tests.
- NTE: vacuum-energy hierarchy relates to Λ (§17.5.18). The "Casimir energy in finite cavities is real" result needs to coexist with the corpus's Λ closure. Likely clean; explicit pass would document the bookkeeping.

### C4. Unruh effect — BEC analogues
- Unruh effect not directly detected; analogue experiments in BECs (Steinhauer 2016 black-hole analogue Hawking radiation; Hu et al. 2019).
- NTE: thermal-time-hypothesis territory; aligns with the Jammer Connes-Rovelli 1994 filter pass already in corpus. Worth explicit cross-link.

### C5. **Cosmic dipole anomaly** (SERIOUS — flagging)
- **What:** Matter dipole (radio galaxies + quasars + JWST galaxies) is 3–4× the CMB kinematic expectation. **>5σ tension** in 2025 data. Secrest et al. 2025 *Rev. Mod. Phys.* colloquium (97, 041001, Dec 2025) is the canonical review. Wagenveld et al. 2025; Singal 2025 *Sci. Rep.* with Quaia catalogue (1.3M quasars, ~1700 km/s peculiar velocity inferred); Böhme et al. 2025 *Phys. Rev. Lett.* radio dipole. Shamir 2024–2025 JWST JADES: spiral-galaxy rotation asymmetry visible in deep field.
- **Why NTE-relevant:** **Directly impinges on the cosmological principle, hence on FLRW assumption, hence on the κ / n_s / Λ derivation chain.** NTE has commitments about cosmological isotropy (S³ closed). The anomaly is at this point well-established; ΛCDM has no clean explanation.
- **Filter-pass priority:** **TOP**. This is the most likely external result to either give NTE a unique purchase (closed-S³ topology + emergence dynamics could yield a directional signature) or generate friction with the corpus's isotropy assumptions.

### C6. Antimatter gravity — ALPHA-g 2023
- ALPHA-g 2023 *Nature*: antihydrogen falls at g ± small uncertainty. No anti-gravity.
- NTE: no anti-gravity commitment; clean pass.

---

## §5 — Tier D: NTE-specific commitments worth checking against bench results

### D1. Macroscopic quantum superpositions
- Arndt group molecular interferometry up to ~25,000 amu (Fein et al. 2019); mechanical-oscillator superpositions; ongoing pushes.
- NTE: where does the classical-quantum boundary live? Decoherence-based, no collapse — so no preferred mass scale. The continued pushing-up of the superposition mass ceiling is *consistent* with NTE's no-collapse stance.

### D2. CSL / continuous spontaneous localization constraints
- Adler-Pearle CSL model; experimental bounds from cantilever, X-ray emission, neutron interferometry. Parameter window narrowing.
- NTE: similar to C2 — NTE doesn't need CSL; the constraints are confirmatory.

### D3. Atomic clock gravitational time dilation precision
- Pound-Rebka 1959; Chou 2010 optical-clock at 33 cm height difference; ongoing precision push (~10^{-19}).
- NTE: emergent-t at varying |Φ_NTE| is structurally far from observable here; clean compatibility.

### D4. CMB-S4 / LiteBIRD upcoming r constraints
- Already in §17.5.12 catalogue. Worth re-noting that the next-gen CMB experiments will either confirm r ~ 4×10^{-3} hilltop or push the bound below.

### D5. Pendulum / torsion-balance equivalence-principle tests
- MICROSCOPE 2022 (~10^{-15} precision). No EP violation.
- NTE: no EP-violation commitment; clean pass.

---

## §6 — Recommended axiom-filter priority queue

For Jammer triage. Each axiom-filter pass is approximately the scope of the existing `Penrose_Palatial_Twistors_Axiom_Filter_Pass_Jammer_v1.md` / `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md` documents in corpus.

1. **C5 — Cosmic dipole anomaly** (TOP — possibly load-bearing for cosmology chain)
2. **C1 — BMV gravitationally-induced entanglement** (possibly load-bearing for gravity emergence)
3. **A3 — Time crystals / rondeau / quasicrystals** (sits exactly on emergent-t axiom; new results)
4. **A1 — Berry phase / Aharonov-Bohm-Casher** (load-bearing for Hopf/Born derivation)
5. **A2 — Neutron interferometry 4π spinor** (load-bearing for gauge birth)
6. **A4 — Quantum time-of-arrival** (productive integration point with thermal time)
7. **A5 — Wigner's friend extensions** (surface ontology + observer)
8. **A6 — Delayed-choice / quantum eraser** ("moment" ontology)
9. Tier B sweep (combined; expected clean)
10. Tier C2, C3, C4, C6 (confirmatory)
11. Tier D sweep (combined; expected clean)

## §7 — Format for individual filter passes

Recommended template, modelled on existing axiom-filter passes:
- §1 Experiment summary (cite primary published source)
- §2 What it tests / what it found
- §3 NTE axioms touched
- §4 Axiom-by-axiom check
- §5 Verdict (compatible / illuminating / tense / falsified)
- §6 Falsifier-screen against §17.5.12
- §7 If illuminating: candidate book/popular-paper material
- §8 If tense: derive queue addition

## §8 — Open question to Greg

The 25+ candidate items here are roughly 25 axiom-filter passes if each gets dedicated treatment. Possible sequencing:
- **(a)** Full filter-pass on top 3 (C5, C1, A3) before any others; defer rest
- **(b)** Light-touch one-liner verdicts for all 25, full passes only on those that surface tension
- **(c)** Open the queue and let Jammer/Scratch work through it organically
- **(d)** Spawn a "Compatibility Catalogue" Drive doc that aggregates all light-touch verdicts as a companion to §17.5.12

Scratch recommendation: **(d) plus full passes on C5, C1, A3 as Priority 1, 2, 3** in that order. C5 in particular looks like it could yield a unique-prediction promotion if the closed-S³ topology + emergence dynamics combine to give a directional signature.

---

— Scratch (Connes Programme lead), 2026-05-27
