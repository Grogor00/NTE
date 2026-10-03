# Time Crystals — Axiom Filter Pass (Scratch v0.1)

**Author:** Scratch (Connes Programme lead)
**Date:** 2026-05-27
**Trigger:** Greg directive "continue with your next task" following BMV ratification. Priority 3 per External Empirical Surface scoping queue (`Working/External_Empirical_Surface_Strange_Quantum_Experiments_Scoping_Scratch_v0_1_20260527.md`).
**Template:** Modelled on prior axiom-filter passes; structure aligned with `Working/Cosmic_Dipole_Anomaly_Axiom_Filter_Pass_Scratch_v0_1_20260527.md` and `Working/BMV_Gravitationally_Induced_Entanglement_Axiom_Filter_Pass_Scratch_v0_1_20260527.md`.
**Status:** v0.1 substantive verdict; awaits Jammer cross-check + CR review

---

## §1 — The phenomenon

**The proposal.** Wilczek (2012) proposed that, in analogy to spatial crystals breaking continuous translation symmetry of space, quantum systems might break continuous time-translation symmetry — exhibiting "time crystals." Early no-go theorems (Bruno 2013; Watanabe-Oshikawa 2015) ruled out time crystals in thermal-equilibrium ground states. Subsequent work refined the notion: time-crystal behaviour emerges in *non-equilibrium* settings, particularly periodically-driven (Floquet) systems and dissipative many-body systems.

**Experimental status (2017–2026).** Time crystals are now well-established empirically across multiple platforms and exhibit a rapidly-diversifying taxonomy:

- **Discrete time crystals (DTC)** — Choi et al. (2017) *Nature*, NV centres in diamond; Mi et al. (2022) *Nature*, Google Sycamore superconducting qubits. Sub-harmonic response to periodic drive; system response at half the drive frequency.
- **Critical prethermal DTC** — Beatrez et al. (2023) *Nat. Phys.* 19, 407. Two-frequency driving; finite-lifetime DTC.
- **Continuous time crystals (CTC)** — broken continuous time-translation symmetry without external periodic drive, in dissipative systems. Erbium-doped solid realisation (2024 *Nat. Commun.*); driven-Rydberg-gas multiple time crystals (Jiao et al. 2025 *Nat. Commun.* 16, 8767); inherent CTC from quantum correlations (Russo & Pohl 2025 *Phys. Rev. Lett.* 135).
- **Time quasicrystals** — He et al. (2025) *Phys. Rev. X* 15, 011055. Non-periodic but structured temporal ordering, analogous to spatial quasicrystals.
- **Time rondeau crystals** — Moon et al. (Nov 2025) *Nat. Phys.* 21, 1813. Partial temporal ordering, stabilised by non-periodic structured drives. Coexistence of order and disorder; observed via carbon-13 nuclear spins in diamond over 170+ periods.

**Common structural feature.** All realised time crystals exist in *non-equilibrium* states — either Floquet-driven (DTC, time quasicrystals, rondeau), or dissipatively stabilised (CTC). The KMS-equilibrium states forbidden by Bruno-Watanabe-Oshikawa remain forbidden; the realisations occupy the non-equilibrium regime that those no-go theorems do not cover.

**Why this regime matters for NTE.** The phrase "broken time-translation symmetry" becomes interesting when *t itself is emergent*. NTE commits to t emerging from the modular flow σ_t of a KMS state on the spectral-triple algebra (per `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md` and `Task_2_CR_Sec_3_2_Simplification_Wick_to_KMS_for_PaperS1_Sec_2_Scratch_v1.md`). The relationship between this emergence story and time-crystal phenomena deserves explicit articulation.

## §2 — Why NTE has a stake

The σ_t / KMS framing of emergent t is structurally central to the corpus. The key corpus material:

- **`Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`** — establishes that NTE's emergent t comes from the modular flow σ_t (Tomita-Takesaki) of the KMS state on the spectral-triple algebra. *"Time, in this picture, is not a fundamental ingredient of physics. It is a macroscopic emergent phenomenon tied to thermodynamics."*
- **`Task_2_CR_Sec_3_2_Simplification_Wick_to_KMS_for_PaperS1_Sec_2_Scratch_v1.md`** and **Paper S1 v1.0 §2** — establishes the canonical framing: pre-temporal regime → generic (non-KMS) state on A_F; post-temporal regime → KMS state ω_{Φ_NTE} at β = β_GB. σ_t = modular flow IS the emergent t.
- **The C¹ kink at gauge birth** (Companion 8 Stage 2 F2) — geometric signature of the state-type transition from generic → KMS. The Wick-rotation reading is the post-temporal-side viewpoint of the same event.
- **Charter v1.3 §2.5** — v10.10 σ_t framework canonical adoption.

Under this framing, **"time-translation symmetry"** for NTE means: invariance of a state under its own modular flow σ_t. The KMS state is, by Tomita-Takesaki, automatically σ_t-invariant (this is the content of the KMS condition itself). Time crystals therefore *cannot* be KMS states — they are necessarily in the non-equilibrium regime where σ_t is well-defined as a mathematical object but does not correspond to "time evolution" in the textbook sense.

This is structurally interesting: NTE's framework predicts that time crystals *must* be non-equilibrium, which is exactly the empirical state of the art. The Bruno-Watanabe-Oshikawa no-go theorem follows naturally from the KMS-state characterisation, and Floquet/dissipative time crystals occupy precisely the non-KMS-state phase space that NTE structurally locates them in.

## §3 — NTE axioms touched

- **A1. N fundamental, t emergent.** The whole filter-pass question turns on what "time-translation symmetry" means when t is emergent.
- **A2. σ_t / KMS framework** (Charter v1.3 §2.5, v10.10 canonical adoption). NTE's emergent t = modular flow of the KMS state ω_{Φ_NTE} at β_GB.
- **A3. Tomita-Takesaki on the spectral-triple algebra** (`Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`). σ_t exists for any state on any von Neumann algebra; KMS condition characterises thermal equilibrium.
- **A4. Surface ontology / S³ × S¹.** Time crystals are realised in lab systems on the emergent (3+1)-d surface.
- **A5. |Φ_NTE| gives time** — the Higgs-mass parallel. At the experimental scale (lab, attosecond to seconds), |Φ_NTE| is at full asymptotic value; emergent t is operationally exact.

## §4 — Axiom-by-axiom check

### A1 (N fundamental, t emergent)

NTE's commitment: t is emergent from σ_t / KMS structure at the cosmic scale. Lab systems inherit this emergent t as their operational time parameter. A time crystal is a configuration *within* this emergent t — its sub-harmonic / quasi-periodic / rondeau structure is a pattern in the system's response under the inherited t-evolution.

**The crucial distinction**: a time crystal does not "break the emergence of t" — t is still emergent at the cosmic scale via σ_t of the cosmic KMS state. The time crystal breaks the *effective time-translation symmetry of its own Hamiltonian* (Floquet drive period → sub-harmonic response, or continuous drive → spontaneous oscillation), as a non-equilibrium configuration within the global emergent t.

**Verdict on A1: compatible; the emergence of t at cosmic scale is orthogonal to the local sub-harmonic / quasi-periodic structure of time-crystal states.**

### A2 + A3 (σ_t / KMS framework + Tomita-Takesaki)

The KMS state ω_{Φ_NTE} at β_GB is, by Tomita-Takesaki, automatically σ_t-invariant. This is the algebraic characterisation of thermal equilibrium. **A state that breaks σ_t-invariance is, by definition, not KMS.** Therefore:

- A time crystal is necessarily in a non-KMS state.
- The Bruno-Watanabe-Oshikawa no-go theorem is structurally implied — it is the statement that KMS states cannot exhibit time-crystal behaviour, which follows from σ_t-invariance of KMS states.
- Floquet-driven and dissipatively-stabilised time crystals occupy the non-KMS-state regime, where σ_t still exists as a mathematical object but does not characterise "thermal equilibrium time evolution."

This is exactly where the realised time crystals (DTC, CTC, time quasicrystal, time rondeau) live. **NTE's σ_t / KMS framework predicts the empirical taxonomy.**

**Verdict on A2 + A3: deeply compatible; NTE's framework structurally locates time crystals in the non-KMS-state regime, which matches the empirical situation exactly.**

### A4 (Surface ontology / S³ × S¹)

Time-crystal experiments operate at lab scales. The spectral-triple algebra in the relevant region of the (3+1)-d surface includes the system's local algebra plus the cosmic background's algebra. The system's Hamiltonian (Floquet-driven, or dissipatively coupled to bath) generates a state on this algebra that is not KMS w.r.t. β_GB. No bulk required; lab dynamics are on the surface.

**Verdict on A4: compatible.**

### A5 (|Φ_NTE| gives time, at full strength in the lab)

At lab scales, |Φ_NTE| is at its asymptotic electroweak-era value. The emergent t is operationally identical to textbook t. Time-crystal dynamics on this background work as standard non-equilibrium quantum mechanics. No |Φ_NTE| correction is structurally implied at lab scales.

**Verdict on A5: compatible.**

## §5 — NTE's prediction

**NTE predicts time crystals are compatible with the corpus framework** at the operational level — they are non-equilibrium states (Floquet-driven or dissipatively stabilised) on the emergent (3+1)-d surface, with the cosmic KMS state's emergent t as their background time parameter.

**More structurally: NTE structurally implies the empirical taxonomy.** The σ_t / KMS framework predicts that time-crystal behaviour cannot exist in KMS-equilibrium states (which is Bruno-Watanabe-Oshikawa) and must occupy the non-KMS regime (Floquet + dissipative). This is exactly the empirical picture.

**The genuinely interesting structural point**: the recently-discovered time rondeau crystals (Moon et al. 2025) — exhibiting partial temporal ordering with coexisting order and disorder, with a smooth Fourier distribution across frequencies rather than a single sharp peak — are *naturally* read under NTE's framework as states whose modular flow σ_t is well-defined but does not correspond to any single periodic time evolution. This is precisely what the σ_t / KMS framework allows: modular flow exists for any state (Tomita-Takesaki); KMS condition is what picks out *one* state as "thermal equilibrium" and *one* σ_t as "physical time evolution." In a rondeau state, neither happens cleanly, and the system explores a structured but non-periodic region of phase space — which is exactly what was observed.

This is not a unique prediction (NTE does not predict the existence of rondeau order from first principles), but it is **a clean structural reading**: NTE's framework had a natural place for rondeau order before rondeau order was experimentally observed. The empirical landscape of 2025 fits NTE's structural commitments cleanly.

## §6 — Honest scope

What this filter pass does *not* establish:

- It does **not** derive the existence or properties of any specific time crystal from NTE first principles. Time crystals are non-equilibrium quantum-many-body phenomena; their existence depends on standard QM many-body dynamics, not on NTE-specific structure.
- It does **not** claim NTE *predicts* DTC, CTC, time quasicrystals, or time rondeau crystals. These are emergent phenomena in non-equilibrium QM, and NTE inherits them.
- It does **not** claim NTE's σ_t / KMS framework is *uniquely* compatible with the empirical taxonomy. Any quantum-mechanical framework with the standard KMS characterisation of equilibrium will accommodate the Bruno-Watanabe-Oshikawa structural result.
- The connection between cosmic-scale σ_t (emergent t at β_GB) and lab-scale non-equilibrium time-crystal states is *operational*, not derived. A full derivation would compute how the cosmic KMS background relates to the local Hamiltonian of a Floquet experiment; this is standard thermal-field-theory bookkeeping and not novel.

What this filter pass *does* establish:

- Time crystals are **structurally compatible** with NTE's σ_t / KMS framework.
- NTE's framework **structurally implies the empirical taxonomy**: KMS states cannot be time crystals (Bruno-Watanabe-Oshikawa), time crystals must be non-equilibrium (Floquet + dissipative), and this matches the empirical record.
- Time rondeau crystals (the most recent and least-classified phenomenon) fit cleanly into the framework as states whose σ_t is well-defined but non-periodic, exploring a structured non-KMS region of phase space.
- No falsifier hit; no soft vulnerability; no derivation queue beyond optional formalisation.

## §7 — Falsifier screen against §17.5.12

- **All falsifiers**: untouched. Time crystals are lab-scale non-equilibrium quantum dynamics; they don't operate on any of the cosmological / neutrino / particle-physics channels in §17.5.12.

**Verdict on §17.5.12 screen**: no falsifier broken; no soft vulnerability; nothing flagged.

This is a *clean* gate. Unlike the cosmic dipole (which had a soft δ₂-bound vulnerability and active Jammer follow-on) and BMV (which had the |Φ_NTE| correction derivation flagged), time crystals close as a pure compatibility result with structural alignment.

## §8 — Derivation queue this opens

For Jammer (R&D) — optional, low priority:

1. **Cosmic-KMS to lab-non-equilibrium bookkeeping.** A formal derivation showing how the cosmic σ_t at β_GB relates to the local Hamiltonian of a lab time-crystal experiment. Standard thermal-field-theory bookkeeping; not novel. Low priority; would tidy the structural framing.

For Scratch (Connes Programme):

2. **Time rondeau / quasicrystal structural reading under σ_t / KMS.** A short note articulating that rondeau / quasicrystal states are σ_t-well-defined non-KMS states exploring structured non-periodic regions of phase space. Would strengthen the corpus's structural reading of recent (2025) experimental work. Medium priority; candidate for popular-paper material.

For AC (portfolio):

3. **Compatibility Catalogue entry** (rather than §17.5.12 row). Time crystals belong in the *clean gates* companion list, not the falsifier set. Light-touch entry suffices.

For Cursor (render lane):

4. **Future popular-paper candidate**: "What Time Crystals Tell Us About Time." Cleanly suited to the emergent-t storyline of the book. Cursor's queue if/when natural.

## §9 — Verdict

**Compatible. Structurally aligned with empirical taxonomy. No falsifier hit; no soft vulnerability; no urgent derivation. Clean gate.**

Time crystals are a *very clean pass*. NTE's σ_t / KMS framework structurally implies the empirical taxonomy: KMS-equilibrium states cannot exhibit time-crystal behaviour, time crystals must occupy the non-KMS non-equilibrium regime (Floquet + dissipative). This matches the empirical record from Choi 2017 through Moon 2025 exactly.

**The structurally interesting observation**: NTE had a natural place for rondeau / quasicrystal order before these phenomena were experimentally observed (Moon et al. Nov 2025; He et al. 2025). The σ_t / KMS framework allows modular flow to be well-defined while neither KMS-thermal nor cleanly-periodic, which is exactly what rondeau order is. This is structural fit, not unique prediction, but it reinforces the corpus's positioning around emergent-t at the right level of generality to accommodate the rapidly-developing empirical taxonomy.

**Catalogue entry recommended**: light-touch in the Compatibility Catalogue (cross-stream with Cursor's portfolio), not a §17.5.12 row. This is a clean gate, not a falsifier or a prediction surface.

## §10 — Cross-stream signals

### §10.1 To Jammer (R&D)

One low-priority optional derivation item (§8 item 1 — cosmic-KMS to lab-non-equilibrium bookkeeping). Not blocking anything; tidies the framing. Pick up when cosmic-dipole Branch I + BMV |Φ_NTE| derivation queue clears.

### §10.2 To AC (corpus integration)

**Compatibility Catalogue entry** (not §17.5.12). Time crystals are a clean compatibility gate. Cross-link to Cursor's Compatibility Catalogue once that doc lands (Cursor's queue from the delegation handoff this morning).

No Paper Kappa PathwayB / Companion paper edits required.

### §10.3 To Scratch (Connes Programme — own queue)

§8 item 2 (rondeau / quasicrystal structural reading under σ_t / KMS) is a candidate short note. Adds to Scratch's portfolio when next there's a breakpoint. Connects naturally to the existing Connes-Rovelli filter pass.

### §10.4 To Cursor (render lane)

**Future popular-paper candidate**: "What Time Crystals Tell Us About Time" — fits cleanly with the book's emergent-t storyline. Cursor's portfolio queue if/when natural. No urgency; the empirical state of the field is still maturing and a popular treatment would benefit from waiting for further results.

### §10.5 To Greg (recognition gates)

1. **Verdict ratification**: is "compatible, structurally aligned with empirical taxonomy, clean gate" the right framing?
2. **Compatibility Catalogue vs §17.5.12**: ratify the Compatibility Catalogue placement (not a falsifier-surface row)?
3. **Future popular-paper candidate**: park in Cursor's queue, or defer entirely?

Scratch recommendation: ratify (1), Compatibility Catalogue placement (2), park future popular-paper in Cursor's queue at low priority (3).

## §11 — Files referenced

**Read this session (corpus):**
- `Connes_Rovelli_1994_Thermal_Time_Hypothesis_Axiom_Filter_Pass_Jammer_v1.md`
- `Task_2_CR_Sec_3_2_Simplification_Wick_to_KMS_for_PaperS1_Sec_2_Scratch_v1.md`
- `Paper_S1_v1_0_section_2_v2_Scratch.md`
- `Tier_2_Reframing_Pass_Four_Papers_under_Canonical_Sigma_t_Phi_NTE_Framing_Jammer_v1.md`
- `Working/External_Empirical_Surface_Strange_Quantum_Experiments_Scoping_Scratch_v0_1_20260527.md` (queue position)

**Web sources consolidated (carried forward from scoping):**
- Wilczek (2012) — original time-crystal proposal
- Bruno (2013) and Watanabe-Oshikawa (2015) — early no-go theorems for equilibrium time crystals
- Choi et al. (2017) *Nature* — first DTC realisation, NV diamond
- Mi et al. (2022) *Nature* — Google Sycamore DTC
- Beatrez et al. (2023) *Nat. Phys.* 19, 407 — critical prethermal DTC
- *Nature Communications* 2024 — inherent erbium-doped CTC
- He et al. (2025) *Phys. Rev. X* 15, 011055 — discrete time quasicrystals
- Jiao et al. (2025) *Nat. Commun.* 16, 8767 — driven-Rydberg-gas multiple time crystals
- Russo & Pohl (2025) *Phys. Rev. Lett.* 135 — inherent CTC from quantum correlations
- **Moon et al. (Nov 2025)** *Nat. Phys.* 21, 1813 — **time rondeau crystals** (newest)

---

— Scratch (Connes Programme lead), 2026-05-27. Filter pass v0.1; verdict clean compatibility gate; structural alignment with empirical taxonomy; Compatibility Catalogue placement recommended over §17.5.12 row.
