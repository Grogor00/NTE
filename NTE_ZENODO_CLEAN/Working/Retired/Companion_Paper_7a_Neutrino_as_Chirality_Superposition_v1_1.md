# Companion Paper 7a — The Neutrino as Chirality Superposition: Vantage-Point Projection and the Structural Mechanism for the Majorana Bridge

**Status:** First refinement (v1.1), 2026-05-15. Working note in `Working/`. Incorporates AC §6.4 (Phase B substantively closed framing for §4.5) + §6.5 (δN intrinsic-uniformity reading for §2.3) + §6.6 (references list expansion for arxiv-target preparation) per Greg Tier A FIT 2026-05-14 Option A absorption (Scratch incorporates). Plus minor coherence repairs to §1.4, §7.1, §7.4 flowing from §4.5 update.
**Supersedes:** v1 (`1SzbN-pbv1HSsYJu42nrCifd6E-HcvPAU`, 2026-05-13).
**Author stream:** Scratch (Connes Programme lead).
**Companion relationship:** Extends Companion Paper 7 (*Neutrino As Unresolved Geometry*). Paper 7 establishes the flavor sliding-superposition framing and the Hopf-projection-failure ontology; Paper 7a generalises the sliding-superposition framing from flavor to chirality and develops the structural mechanism that produces §3.3 Majorana Bridge as derivable consequence rather than asserted axiom.
**Source basis:** Greg's chirality-as-tendency proposal (Connes Programme Option (c) Track 2, recognition-gate fit 2026-05-13); Scratch Track 2 structural working note `19X8CF7rBssCxOfFdtKtPqedmw5Aeryu6`; Phase A §2.3 reframing per Track 2 (PARTIAL-PASS → PASS upgrade); Jammer Phase B v1 + v1.1 (δN intrinsic-uniformity) + v1.2 (prediction-mapping) working notes (canonical Phase B closure at v10.9 framing); corpus §3.3 Majorana Bridge ontology and OctonionExtension §3.6 CPN parity mechanism; v10.8 §17.5.3 structural-identity reading (T1-CORPUS-8/9); Charter v1.2 §3 R3 substantive-pass canonical.

---

## Abstract

The NTE corpus §3.3 *Majorana Bridge* states that the neutrino has not undergone the Hopf-projection-driven topological resolution that creates the particle/antiparticle distinction — it is *"an unresolved configuration smeared across the fibre rather than projected onto S²."* The category of particle vs antiparticle has never applied to it. This paper presents the structural mechanism that produces this ontology as a derivable consequence rather than an asserted axiom. The mechanism is: (i) the neutrino exists fundamentally in N as a chirality superposition, with both left-handed (LH) and right-handed (RH) amplitudes coexisting; (ii) its minimal Higgs coupling (y_ν ~ 10⁻¹²) prevents completion of the Hopf-projection S³ → S² that would lock the U(1) fibre phase and produce a definite chirality eigenstate; (iii) without chirality commitment, sector commitment (+N or −N via the OctonionExtension §3.6 CPN parity mechanism) is also undetermined; (iv) the apparent chirality observed in each sector's experiments is the gauge-projection of the underlying superposition through that sector's active gauge symmetry (SU(2)_L in +N; SU(2)_R in −N), not a fundamental chirality assignment. The mechanism: specifies the structure of the unresolved state (chirality superposition); enables a reading of NCG Pati-Salam constructions (notably Boyle-Farnsworth 2020) wherein the two chirality irreps are vantage projections of one underlying configuration rather than two distinct entities; opens new prediction territory (possible quantitative scaling of vantage-bias magnitude vs y_ν; possible small deviations from pure-Majorana 0νββ rates); and preserves the existing §17.5.12 Majorana 0νββ falsifier as the current observational anchor. The paper presents the mechanism (§2), derives §3.3's claims from it (§3), develops the reading of the BF 2020 Pati-Salam construction under this ontology (§4), discusses falsifiability and adjacent literature (§5–§6), and lists open structural work (§7).

---

## §1. Introduction and motivation

### §1.1 Paper 7's sliding superposition for flavor

Companion Paper 7 (*Neutrino As Unresolved Geometry*) establishes that neutrinos in the NTE framework exhibit a sliding superposition structure for flavor: flavor eigenstates are not fixed quantum-number assignments but sliding projections of underlying mass eigenstates on the Hopf-projected geometry. The framing is structurally enabled by the neutrino's failure to complete the Hopf-projection S³ → S² that establishes binary projections for charged fermions — the sliding character of flavor reflects the unprojected nature of the underlying configuration.

Paper 7's specific argument operates at the level of *flavor* superposition. The natural question is whether the same structural mechanism — Hopf-projection failure leaving a superposition unresolved — applies to other neutrino quantum-number assignments. This paper extends the sliding-superposition framing from flavor to chirality.

### §1.2 What §3.3 Majorana Bridge currently commits to

The NTE corpus §3.3 (*Minimal Higgs Coupling: The Majorana Bridge*) commits to the following ontological statement about the neutrino:

> *"The neutrino is neither particle nor antiparticle — it is an unresolved configuration, smeared across the fibre rather than projected onto S². A left-handed neutrino in +N and a right-handed antineutrino in −N are not two things identified — they are one unresolved configuration that has no geometric basis for distinguishing the two sides of the Janus boundary. ... The neutrino is not a particle that happens to equal its antiparticle; it is a configuration for which the particle/antiparticle category has never applied. The distinction matters: 'self-conjugate' implies a resolved entity that maps to itself under conjugation; 'unresolved' implies the conjugation operation has no target to act on."*

This is a strong ontological claim. It commits the corpus to a non-Majorana reading of the neutrino in the strict sense (not "Majorana-as-self-conjugate" but "fully unresolved"). The §3.3 framing has supported the dark matter κ derivation (the unresolved geometry produces the bridge cross-section S² = S³/S¹) and grounds the §17.5.12 falsifiability prediction (Majorana 0νββ detection in next-generation experiments).

But §3.3 as written is an *axiom*. It states what the neutrino is and is not, without specifying the structural mechanism that produces this state. The connection to OctonionExtension §3.6's CPN parity mechanism (LH commits to +N, RH commits to −N) is gestured at via the Hopf-projection language but not made explicit. The "smearing across the fibre" is described but not derived from a specific structural specification of *what* is smeared.

This paper addresses that gap. We present the mechanism: chirality superposition in N + Hopf-projection failure + vantage-point projection through CPN-sector gauge symmetries.

### §1.3 The open question that motivates this paper

What is the structural specification of the unresolved state? §3.3 says the neutrino is "unresolved" and "smeared," but unresolved *in what degree of freedom*? Smeared *across what specifically*? Without specification, the axiom is content-light: it tells us what the neutrino isn't but not what its underlying configuration *is*.

Greg's chirality-as-tendency proposal (Track 2 of the Connes Programme Option (c) investigation, 2026-05-13) provides the specification: the unresolved degree of freedom is *chirality*. The smearing is *across the LH/RH chirality basis* in N. The unresolved status of LH-in-+N vs RH-antineutrino-in-−N — already in §3.3 — becomes a consequence of the chirality being in superposition prior to Hopf projection.

The structural payoff is substantial: §3.3 becomes mechanism-derived rather than asserted; the connection to OctonionExtension §3.6 becomes explicit; the corpus gains a reading of NCG Pati-Salam constructions (notably BF 2020) wherein the two chirality irreps are vantage projections of one configuration; new prediction territory opens.

### §1.4 Scope and outline

This paper develops the mechanism (§2), derives §3.3's claims from it (§3), develops the reading of the Boyle-Farnsworth 2020 Pati-Salam construction under this ontology (§4), discusses falsifiability (§5), positions the work relative to adjacent literature (§6), and lists open structural work (§7).

What this paper does NOT do:
- Execute the substantive R3 Phase B structural-identification map at full depth — Phase B has been substantively completed by Jammer R&D (canonical Phase B v1 + v1.1 + v1.2 working notes, R3 substantive closure at v10.9 framing per Charter v1.2 §3); Paper 7a presents the structural mechanism and the R3 reading at the §3.3-compatibility level, with substantive Phase B verification carried in Jammer's working note family;
- Develop the Jordan-from-octonion derivation (deferred to v10.10+ J_3(𝕆) ⊕ J_3(𝕆) downstream scope per Charter v1.2 §3 / Greg Q5 FIT 2026-05-13);
- Develop quantitative predictions beyond identifying candidate territory (vantage-bias magnitude scaling; 0νββ deviations);
- Propose a revision of Paper 7's flavor sliding-superposition argument — this paper extends, not modifies.

---

## §2. The chirality-superposition mechanism

### §2.1 Strong vs minimal Higgs coupling: Hopf-projection completion vs failure

The NTE corpus §3 establishes a categorisation of fermions by Higgs coupling magnitude:

- **Strong Higgs coupling (y >> 0):** charged leptons, quarks, W/Z bosons. Yukawa coupling is sufficient to drive completion of the Hopf-projection S³ → S² on the boundary geometry. The U(1) phase of the Hopf S¹ fibre locks to a definite value, producing a chirality eigenstate (LH or RH). The fermion commits to one e-fold direction (+N for LH, −N for RH) per the OctonionExtension §3.6 CPN parity mechanism, and accumulates temporal duration in its committed direction. The particle/antiparticle binary is established by the Hopf projection's completion.

- **Minimal Higgs coupling (y_ν ~ 10⁻¹²):** neutrinos. Yukawa coupling is many orders of magnitude smaller than the smallest charged-lepton coupling (y_e ~ 10⁻⁶). The Higgs VEV's effect on the neutrino's U(1) phase is correspondingly suppressed; the phase does not lock to a definite chirality. The Hopf-projection S³ → S² is not completed for the neutrino. The fermion does not commit to a chirality eigenstate, does not commit to one e-fold direction, and does not have the binary particle/antiparticle structure created by Hopf-completion.

The corpus §3.3 already names this distinction: the neutrino "is barely embedded in the e-fold structure — not locked into a single e-fold direction." Paper 7a makes explicit what structural content the failure-to-lock involves: the chirality superposition.

### §2.2 The neutrino's chirality superposition in N

For a neutrino in NTE, the fundamental content in N is a chirality superposition:

$$|\nu\rangle = \alpha |\nu_L\rangle + \beta |\nu_R\rangle$$

with $|\alpha|^2 + |\beta|^2 = 1$ and both $\alpha, \beta$ nonzero. The superposition lives in N — the fundamental boundary dimension before t emerges via temporal locking. The Hopf-projection failure prevents the U(1) fibre phase from selecting a chirality eigenstate; both amplitudes persist.

The relative magnitudes of $|\alpha|^2$ and $|\beta|^2$ are not strongly asymmetric in general — the corpus framing supports comparable amplitudes (the "in the middle" reading of Greg's chirality-as-tendency proposal). The neutrino is, fundamentally, in a roughly equal superposition of LH and RH chirality content.

The natural question is: how does this reconcile with the strongly asymmetric SM weak-interaction phenomenology, where LH neutrinos interact via the weak force and RH (sterile) neutrinos do not? The answer is in §2.4 — through gauge-projection, not through underlying asymmetry.

### §2.3 CPN-symmetric two-sector structure under δN intrinsic-uniformity reading

The Janus boundary at N=0 separates the manifold's two CPN-conjugate sectors. The +N and −N sectors share the S³ boundary at N=0 but neither occupies it. Per OctonionExtension §3.6, the CPN parity mechanism establishes the chirality-bearing gauge structure: SU(2)_L acts as gauge symmetry projector on left-handed (LH) spinors from the +N vantage; SU(2)_R acts as gauge symmetry projector on right-handed (RH) spinors from the −N vantage. Cross-sector CPN parity exchanges the two factors.

**δN intrinsic-uniformity reading** (Phase B v1.1 supplement canonical, Greg direct affirmation 2026-05-13). From each sector's intrinsic perspective, δN points "forward toward more N-thickness" — both sectors are locally δN-aligned to the same intrinsic geometry. The two sectors are globally CPN-conjugate opposites but intrinsically identical in their local δN-aligned geometric structure. All three gauge generator structures (SU(2)_L, SU(2)_R, SU(4)_c) are intrinsically uniform across both sectors; the apparent "SU(2)_L vs SU(2)_R" distinction at gauge-bearing chirality-projecting operators is a meta-vantage signature of CPN-mirroring on chirality-bearing gauges, not an asymmetric structural assignment.

For the unresolved neutrino, the chirality superposition |ν⟩ = α|ν_L⟩ + β|ν_R⟩ in N lives across the Janus boundary in a structurally bilateral manner. The CPN-mirroring relationship between the two sectors means the chirality superposition is observed via different vantage projections from each sector: an observer in +N applies the SU(2)_L gauge-projector to the superposition and registers the LH amplitude; an observer in −N applies the SU(2)_R gauge-projector and registers the RH amplitude. Both vantage projections operate on the same underlying configuration. The bilateral support is structurally symmetric from each sector's intrinsic perspective under δN intrinsic-uniformity; the meta-vantage observer who notes the LH-on-+N / RH-on-−N pattern is reading the CPN-mirroring signature on chirality-bearing gauges, not an asymmetric structural property of the underlying superposition.

This is the deeper structural reading made explicit by Phase B v1.1 + v1.2 (canonical Phase B closure at v10.9 framing): NTE's two-sector cosmology is structurally one sector viewed under CPN parity, not two distinct asymmetric structural assignments.

### §2.4 Vantage-point projection through each sector's gauge symmetry

When a neutrino is observed through gauge-mediated interactions (which is how all neutrino detection happens in the SM), the observation occurs from one CPN-conjugate sector vantage point — the experimenter is in +N. The gauge symmetry active in +N is SU(2)_L, which couples to LH content only. The gauge interaction acts as a *projector*: it projects out the LH-amplitude component of the neutrino's superposition for gauge coupling and leaves the RH-amplitude component untouched.

From the +N vantage:
- The LH component is gauge-active, weakly interacting, detected as "the neutrino" in standard SM phenomenology;
- The RH component is gauge-inactive (SU(2)_L doesn't couple to it), not detected as a weakly-interacting object, structurally inert from the +N viewpoint;
- The apparent "left-handed neutrino" is the gauge-projection of the chirality superposition, not the full underlying state.

From the −N vantage (the mirror sector):
- The RH component would be gauge-active under SU(2)_R, detected as a weakly-interacting object in mirror-sector phenomenology;
- The LH component would be gauge-inactive from −N's viewpoint;
- The apparent "right-handed neutrino" of mirror physics is the gauge-projection of the same underlying configuration from the opposite sector vantage.

**This is the vantage-point projection mechanism.** The chirality observed in each sector is not a chirality assignment intrinsic to the neutrino; it is the gauge-projection of the underlying chirality superposition through that sector's active gauge symmetry. The same superposition presents differently from the two vantages.

The SM's strong LH-RH asymmetry in weak-interaction phenomenology is recovered: the LH-only weak interaction in +N is the gauge-projection of a 50/50 (or near-50/50) chirality superposition. The RH content of the neutrino does not "interact weakly" in +N because SU(2)_L is not coupled to it — but the RH content exists. It is gauge-inactive from the +N vantage, not absent.

This reconciles Greg's "in the middle" chirality assignment (the underlying superposition is roughly symmetric) with SM phenomenology (the observed weak interaction is strongly LH-biased): both are correct simultaneously — the underlying state is symmetric; the gauge-projection through the +N-active SU(2)_L is asymmetric.

---

## §3. Why §3.3 emerges naturally from the mechanism

### §3.1 The Hopf-projection-failure structural origin

§3.3 commits to: *"The Hopf projection S³ → S² that establishes the binary requires engagement with the S¹ fibre that the neutrino's minimal Higgs coupling does not provide."*

The mechanism in §2 specifies the structural content of this statement. Strong Higgs coupling provides the U(1)-phase-locking dynamic that completes the Hopf projection; minimal Higgs coupling does not. The S¹ fibre engagement is specifically the U(1) phase locking that selects a definite chirality. Without it, the chirality remains in superposition.

§3.3's "smeared across the fibre rather than projected onto S²" framing reads, under the mechanism: the U(1) phase circle of the Hopf S¹ fibre has not been collapsed to a definite phase; the chirality content is distributed across the phase circle (the "smearing"); no chirality eigenstate has been selected; no projection onto a definite S² point has occurred.

### §3.2 No chirality commitment → no sector commitment → no particle/antiparticle binary

Per OctonionExtension §3.6, chirality determines sector commitment: LH modes → +N, RH modes → −N (via the CPN parity mechanism). For charged fermions with definite chirality, this produces a definite sector commitment.

For the neutrino in chirality superposition, the sector commitment is also not fixed. The LH-amplitude content has support on +N; the RH-amplitude content has support on −N; the neutrino's wavefunction straddles the Janus boundary in the chirality basis. This is the bilateral temporal extent of §3.3 in structural form.

The particle/antiparticle binary in NTE is established by the combination of: (i) chirality commitment (LH vs RH), (ii) sector commitment (+N vs −N), (iii) Hopf-projection completion onto S² with definite orientation. All three are absent for the neutrino — no chirality eigenstate, no sector commitment, no Hopf completion. The particle/antiparticle binary is therefore not established for the neutrino.

§3.3 reads: *"the conjugation operation has no target to act on."* Under the mechanism: the conjugation operation that maps particle ↔ antiparticle in the SM requires the particle/antiparticle binary to exist. For the neutrino, the binary has never been established because the structural process that creates it (Hopf-projection completion) has not occurred. The conjugation operation has no target because the target — the binary distinction — does not exist for this configuration.

### §3.3 The "particle/antiparticle category has never applied" claim derived

§3.3's strongest ontological claim is: *"the neutrino is not a particle that happens to equal its antiparticle; it is a configuration for which the particle/antiparticle category has never applied."*

Under the mechanism:
- The particle/antiparticle category is *created* by the Hopf projection's completion, which establishes the binary distinction.
- For the neutrino, the Hopf projection does not complete.
- The category is therefore not created for this configuration.
- The statement *"the particle/antiparticle category has never applied"* is a direct consequence of *"the Hopf projection has never completed."*

This is the load-bearing structural deepening Paper 7a accomplishes for §3.3: the claim that the category has never applied is derived from the failure of the mechanism that would create the category, not asserted as an axiom about neutrino ontology.

### §3.4 Bilateral temporal extent emerges naturally

§3.3 commits to: *"its wavefunction occupies an interval of the manifold's N-thickness larger than the local thickness almost everywhere — it has bilateral support across both CPN-conjugate orientations."*

Under the mechanism: the chirality superposition has both LH (committing to +N) and RH (committing to −N) amplitudes. The wavefunction has support on both the +N and −N CPN-conjugate orientations — this is the bilateral support. The "larger than the local thickness" reflects that the wavefunction is not localised in one e-fold direction; it spans the Janus boundary in the chirality basis.

The bilateral temporal extent is not a separate property requiring its own structural explanation — it is the same property as the chirality superposition in N, viewed through the CPN-sector content.

---

## §4. Reading the BF 2020 Pati-Salam construction under this ontology (the R3 reading)

### §4.1 BF 2020 Pati-Salam structural content

Boyle and Farnsworth (2020, arXiv:1910.11888) develop a noncommutative geometry construction extending the Connes formulation of the Standard Model. Their §4 Pati-Salam construction places SM matter content in the gauge group SU(4) × SU(2)_L × SU(2)_R, with per-generation fermion content:

- ψ_L in (4, 2, 1): 8 left-handed Weyl fermions per generation;
- ψ_R in (4, 1, 2): 8 right-handed Weyl fermions per generation;
- Total: 16 Weyl fermions per generation, distributed across the two chirality irreps.

The Dirac operator D_F includes Yukawa couplings producing mass terms, including a Majorana mass term for the RH neutrinos (M_R) and a Dirac coupling (m_D) producing the seesaw mass mechanism.

As-written, BF 2020's construction treats ψ_L and ψ_R as distinct fermion content with distinct gauge quantum numbers, distinct mass-term structure, and distinct basis-vector representation in the Hilbert space H_F. The Pati-Salam framework's RH neutrino is a fundamental basis vector, not an emergent vantage-projection.

### §4.2 R3 relabeling: LH ↔ +N, RH ↔ −N

The Connes Programme R3 reframing reads BF 2020's chirality labels (LH/RH) as NTE's CPN-sector labels (+N/−N). Under R3:

- BF 2020's (4, 2, 1) LH content ↔ NTE's +N-sector content (the LH fermion content of OctonionExtension §3.6's parity-violation mechanism, gauge-active in +N under SU(2)_L);
- BF 2020's (4, 1, 2) RH content ↔ NTE's −N-sector content (the RH fermion content gauge-active in the mirror sector under SU(2)_R per §9.4);
- BF 2020's "RH neutrino" ↔ NTE's neutrino in the −N CPN-conjugate orientation.

Phase A of the Connes Programme verified the irrep content basis at PASS: NTE OctonionExtension §3.6 + §9.4 already commits to 16 Weyl fermions per generation per CPN sector with LH/RH split, matching BF 2020 Pati-Salam (4, 2, 1) ⊕ (4, 1, 2) split exactly. The R3 relabeling has structural basis at this level.

### §4.3 Four BF 2020 "distinctions" reframed as vantage-projections

Phase A initially found that R3 reached only partial structural basis at the §3.3-compatibility level, because BF 2020 Pati-Salam has four real structural distinctions between ν_L and ν_R that did not appear to reduce to "one unresolved configuration":

1. **Gauge couplings differ.** ν_L is gauged by SU(2)_L; ν_R is gauged by SU(2)_R. Distinct gauge-coupling structures.
2. **Mass terms differ.** Dirac m_D couples ν_L to ν_R; Majorana M_R is on ν_R alone. Distinct mass-term structures.
3. **Irrep quantum numbers differ.** ν_L is in (4, 2, 1); ν_R is in (4, 1, 2). Distinct SU(4) × SU(2)_L × SU(2)_R representation labels.
4. **Spectral data differ.** ν_L and ν_R are distinct basis vectors in H_F with distinct propagator structures.

Each of these *appears* to count as a "geometric basis for distinguishing the two sides of the Janus boundary" for the neutrino — and §3.3's strict claim is that no such basis exists for the neutrino. Phase A concluded that §3.3 required external imposition beyond what R3 produced from the BF 2020 structure.

Under the Paper 7a mechanism (chirality superposition + Hopf-projection failure + vantage-projection), each of these four distinctions reframes:

1. **Gauge couplings as vantage-projections.** ν_L being SU(2)_L-gauged reflects the +N-vantage projection of the chirality superposition — SU(2)_L is the +N-active gauge, coupling to the LH-amplitude component of the underlying superposition. ν_R being SU(2)_R-gauged reflects the −N-vantage projection — SU(2)_R is the −N-active gauge, coupling to the RH-amplitude component. The gauge-coupling distinction is real but reflects the projection structure, not an ontological distinction between two distinct fermions.

2. **Mass terms as cross-amplitude and self-amplitude structures.** The Dirac m_D coupling between ν_L and ν_R reflects the LH-RH cross-amplitude in the chirality superposition (the overlap of the same configuration viewed from different vantages). The Majorana M_R reflects the self-amplitude in the RH projection. Both mass-term structures are properties of the underlying chirality superposition under each vantage's projection.

3. **Irrep quantum numbers as vantage-projected gauge representations.** The (4, 2, 1) and (4, 1, 2) irreps are how the same underlying configuration presents under each vantage's gauge projection. Different projections produce different irrep labels — real differences in projection structure, not ontological differences in underlying content.

4. **Spectral data as representational choices.** BF 2020's distinct basis vectors for ν_L and ν_R reflect a representation choice — one basis vector per vantage projection. The underlying physical state is the chirality superposition; the basis-vector distinction is a representational structure of the projection, not a count of ontologically distinct entities.

### §4.4 §3.3 emerges as reading of the two-irrep structure

Under the Paper 7a mechanism, BF 2020's Pati-Salam two-irrep structure (4, 2, 1) ⊕ (4, 1, 2) reads as the two vantage projections of a single chirality superposition. The §3.3 statement *"one unresolved configuration that has no geometric basis for distinguishing the two sides of the Janus boundary"* emerges as:

- The underlying chirality superposition exists *before* any vantage projection — it has no chirality assignment, no sector commitment, no particle/antiparticle binary, no geometric basis for being "on" one side of the Janus boundary or the other.
- From each CPN-sector vantage, the projection produces what appears to be a distinct entity (the apparent ν_L from +N; the apparent ν_R from −N) — but this distinctness is the projection structure, not the underlying configuration.
- The four distinctions BF 2020 places between ν_L and ν_R are projection-artifact distinctions on the same underlying superposition. They are real (the projections do differ structurally) but not ontological (both projections are of one underlying state).

§3.3 *emerges* as a reading of the Pati-Salam two-irrep structure under the chirality-superposition + vantage-projection mechanism — not as a separate axiom layered on top. The strict §3.3 claim that "no geometric basis exists for the distinguishing" reads under the mechanism as "the apparent distinguishing is projection structure, not ontological commitment to two distinct things."

This is the structural deepening that Paper 7a accomplishes for the R3 reading: BF 2020's content, read through the Paper 7a mechanism, *produces* §3.3's ontology rather than conflicting with it. The Connes Programme R3 reading is substantively passed at the §3.3-strict criterion under this mechanism.

### §4.5 Open work, current scope, and deferred future investigations

**Phase B substantively completed** (Jammer Working/ canonical Phase B finding, v1 `10dZ800TOICC_0s7AnPJL9m8ipjETK75a` + v1.1 δN intrinsic-uniformity supplement `1YRS68mtA6uNdlLMgK6MU7PVlqmFTzNIU` + v1.2 prediction-mapping verification `1pIw4YWqQ6UBeEEayxfn4e2oLo0o4hYcU`). All four Phase B sub-questions pass at substantive level:

- §1 Irrep map: 8+8=16 Weyl fermions per generation per CPN sector; vantage projections of underlying chirality superposition + two-sector content
- §2 Gauge generator identification at projector level: SU(2)_L × SU(2)_R × SU(4)_c intrinsically uniform across both sectors per δN reading; meta-vantage distinction is CPN-mirroring signature on chirality-bearing gauges
- §3 Mass-term structure: Yukawa as Hopf-projection completion measure; Majorana M_R as CPN-self-identity across Janus boundary; §17.5.12 falsifier preserved (Greg Q3 FIT)
- §4 Phenomenology reproduction: 14-prediction map verified (κ, δ_J, θ_23, θ_12, n_s, r, w, H_0, three generations, three neutrino species, no sterile neutrinos, baryon asymmetry mechanism, 0νββ falsifier, lithium-7 partial resolution); SM weak-interaction LH-bias as gauge projection; no-W_R observable in +N universe added as new falsifier (Phase B v1.2 §3.4)

R3 substantive closure at v10.9 framing established (Phase C activation canonical 2026-05-14, Charter v1.2 §3 canonical record). Two NTE axioms (CPN-symmetric two-sector + §3.3 Majorana Bridge) collapse to one commitment (chirality-superposition + vantage-projection mechanism under Track 2 + δN intrinsic-uniformity); net commitment-count reduction at v10.9 framing.

**Track 1 (Jordan-from-octonion algebraic-origin derivation)** remains deferred to v10.10+ scope per Greg Q5 FIT 2026-05-13. The Track 1 question — whether the BF 2020 Pati-Salam algebraic structure derives from NTE's octonionic substrate via J_3(𝕆) ⊕ J_3(𝕆) machinery — is a productive future research arc. Successful Track 1 derivation would close the M₁ leptogenesis mass scale derivation (per Phase B v1.2 §1.12) and complete the η = 6.1×10⁻¹⁰ baryon asymmetry magnitude prediction as zero-parameter. Currently open structural research; Connes Programme's authorised Scratch routing arc (Charter v1.2 §5.5) includes spectral-zeta Route A as related machinery development.

**Quantitative extensions of the chirality-superposition + vantage-projection mechanism**:
- Vantage-bias magnitude scaling vs y_ν (e.g., low-y_ν → enhanced bilateral support correlation)
- 0νββ rate deviations from pure Majorana under vantage-projection geometry
- Flavor-chirality structural relationships under Track 2 + δN

Each is candidate quantitative-prediction territory identified by this paper; development is future work. Paper 7a's primary commitment is the structural mechanism; quantitative-prediction territory is identified, not developed.

**§3.3 corpus prose update** (AC scope, Phase C kickoff 2026-05-14): when AC ships the v10.9 §3.3 corpus prose update absorbing the mechanism-derivation content + CPN ↔ U(1) half-cycle phase framing (per Ch 8 v4 audit §3.2 + Greg FIT 2026-05-14), Paper 7a should reciprocally cross-reference the §3.3 canonical content. Currently deferred to Paper 7a v1.2 or v2 pass following AC's §3.3 prose update.

---

## §5. Falsifiability — §17.5.12 Majorana 0νββ preserved

### §5.1 The Majorana condition under the mechanism

The standard Majorana condition states: ν_L^c = ν̄_R (the charge conjugate of the LH neutrino is the RH antineutrino). In Pati-Salam constructions, this is realised through Majorana mass terms in D_F for ν_R.

Under the Paper 7a mechanism with R3 relabeling:

- ν_L = +N-vantage projection of the chirality superposition (LH-amplitude in N projected through +N's SU(2)_L);
- ν̄_R = −N-vantage projection of the same configuration's antineutrino content (RH-amplitude projected through −N's SU(2)_R, with charge conjugation across the Janus boundary).

Both vantage projections are of the same underlying chirality superposition. The Majorana cross-identification ν_L^c = ν̄_R becomes: *"the +N-vantage projection's charge conjugate equals the −N-vantage projection of the same configuration."* This is structurally automatic — the cross-identification reflects that both projections see the same configuration; charge conjugation across the Janus boundary is the CPN operation.

The Majorana condition is preserved as a *consequence* of the chirality-superposition + vantage-projection mechanism, not as an independent assertion about neutrino physics.

### §5.2 Standard 0νββ falsifier preserved

§17.5.12 of the master corpus commits to Majorana 0νββ detection in next-generation experiments as a falsifier of §3.3's unresolved-configuration ontology. The standard 0νββ phenomenology (neutrinoless double-beta decay enabled by Majorana cross-identification of ν and ν̄) is preserved under Paper 7a's mechanism: the Majorana condition still holds (per §5.1); the 0νββ amplitude calculation proceeds as in standard Majorana phenomenology; the detection prediction is unchanged.

Paper 7a does *not* propose a different observational signature for 0νββ. The mechanism deepens the structural origin of the Majorana ontology but does not change the standard observational falsifier as the current commitment.

### §5.3 Candidate quantitative extensions

The mechanism opens new prediction territory beyond the standard 0νββ falsifier, though development of quantitative predictions is future work and not within the scope of this paper:

- **Vantage-bias magnitude scaling vs y_ν.** The "very slight tendency" of Greg's proposal may admit quantitative specification: the vantage-projection bias might scale with the failure-to-Hopf-project parameter, which is set by y_ν. A quantitative prediction of vantage-bias magnitude vs y_ν, if developed, could provide a new observational test.

- **Possible 0νββ rate deviations from pure-Majorana expectations.** If the underlying superposition has |α|² ≠ |β|² slightly (small deviation from the strict 50/50 reading), the effective Majorana mass m_ββ entering the 0νββ rate may differ from pure-Majorana expectations. The deviation magnitude would scale with the underlying amplitude asymmetry, which would itself be set by structural details of the chirality-superposition.

- **Connection to flavor mixing phenomenology.** Paper 7's flavor sliding-superposition framing and Paper 7a's chirality-superposition framing both reflect Hopf-projection-failure structure. A unified structural account may connect chirality indeterminacy to flavor mixing in ways that produce testable structural relationships between mixing angles, mass-eigenstate hierarchy, and chirality-bias parameters.

Development of any of these candidate predictions is future work. Paper 7a's primary commitment is the structural mechanism; quantitative-prediction territory is identified, not developed.

---

## §6. Adjacent-literature positioning

### §6.1 Relational quantum mechanics (Rovelli)

The framing "superposition that never collapses, with observer-relative properties" has structural overlap with relational quantum mechanics (RQM), in which quantum properties are observer-relative rather than absolute. Paper 7a's mechanism is structurally tighter than generic RQM:

- The "observer" is not arbitrary in Paper 7a — it is the CPN-conjugate sector (+N or −N), built into the cosmology;
- The vantage-bias is not generated by interaction with an arbitrary observer — it is the projection through each sector's active gauge symmetry (SU(2)_L for +N; SU(2)_R for −N);
- The relational structure is cosmologically grounded, not interpretive.

NTE's version is not an adoption of RQM. Reviewers familiar with RQM will recognise the kinship; the structural distinction (CPN-vantage vs arbitrary observer) makes Paper 7a a positive structural commitment rather than an interpretive layer over standard QM.

### §6.2 Chirality-as-emergent (various authors)

Several theorists treat chirality as emergent through interactions rather than fundamental. Paper 7a's mechanism is structurally specific in a way these proposals generally are not:

- Chirality is not emergent through arbitrary interactions — it is the t-emergent gauge-projection through each CPN-sector's active gauge symmetry;
- The fundamental N-structure is the chirality superposition; what is emergent is the perceived chirality assignment in each vantage;
- The mechanism (Hopf-projection completion or failure depending on Higgs coupling magnitude) is structurally specific and ties to the corpus's existing OctonionExtension framework.

Paper 7a's version is NTE-native; the adjacent-literature connections are landing-pad context for reviewers, not integration paths.

### §6.3 Octonion-and-Pati-Salam programmes (Furey, Boyle-Farnsworth, Dixon)

Several NCG and division-algebra-based SM-extension programmes have developed Pati-Salam structures from octonion or related algebraic content:

- Furey (2018) on ℂ ⊗ 𝕆 minimal left ideals as a generation-content framework;
- Dixon (1994) on division algebra approaches to SM matter content;
- Boyle and Farnsworth (2020, the paper Paper 7a's R3 reading reframes) on Connes-NCG extensions including Pati-Salam.

Paper 7a's R3 reading provides a structural interpretation of these programmes' two-chirality-irrep content under NTE's chirality-superposition + vantage-projection mechanism. The reading is NTE-specific (the CPN-cosmology grounding is not present in the parent programmes) but compatible with the parent programmes' irrep content. This positions Paper 7a as offering a structural reading of an existing NCG construction, not a wholesale alternative to it.

---

## §7. Open work

### §7.1 Phase B substantive structural-identification map (Jammer territory) — closed

The substantive map between BF 2020 Pati-Salam content and NTE's two-sector content under R3 relabeling has been substantively completed by Jammer R&D (canonical Phase B v1 + v1.1 + v1.2 working notes; see §4.5 for verdict summary and references). R3 substantive-pass closure at v10.9 framing canonical per Charter v1.2 §3. Remaining substantive depth refinements (e.g., Track 1 algebraic-origin derivation, Phase B prediction-mapping further extensions) carry as downstream future work per Jammer R&D scope under Charter v1.2.

### §7.2 Jordan-from-octonion derivation (v10.10+ J_3(𝕆) downstream scope)

The deeper algebraic-origin identification between BF 2020's Jordan-factor automorphism gauge structure and NTE's octonion-internal SO(4) ⊂ G_2 stabiliser is naturally placed in v10.10+ J_3(𝕆) ⊕ J_3(𝕆) downstream scope per Charter v1.2 §3 (Track 1 of Option (c) investigation, deferred per Greg's recognition signal 2026-05-13).

### §7.3 Quantitative prediction development

The candidate prediction territory identified in §5.3 (vantage-bias magnitude scaling vs y_ν; possible 0νββ deviations from pure-Majorana; flavor-chirality structural relationships) admits quantitative development. The work would extend Paper 7a's mechanism with specific scaling relations, observational deviation predictions, and connections to existing neutrino mixing phenomenology. Estimated 2–3 focused R&D sessions per prediction line.

### §7.4 §3.3 corpus prose update (v10.9 timing canonical)

The Paper 7a mechanism should be integrated into corpus §3.3 prose at v10.9 (timing fired by Greg recognition gate 2026-05-13). The integration extends §3.3's existing ontological commitment (preserved as-is) with the explicit mechanism (chirality superposition + Hopf-projection failure + vantage-projection through CPN-sector gauge symmetries), plus CPN ↔ U(1) half-cycle phase framing (per Ch 8 v4 audit §3.2 + Greg FIT 2026-05-14). AC scope per Charter v1.2 §7.1; candidate inline text drafted by AC 2026-05-15 (Handoff `1YO09npybRo9L_0ja4HoqSXJY6UN-BMRp`) pending integration via v10.9 §17.X writeup pass.

### §7.5 Companion-paper consolidation

Paper 7a's chirality-superposition framing and Paper 7's flavor sliding-superposition framing reflect the same structural mechanism applied to different neutrino quantum-number assignments. A future consolidation pass would explicitly unify the two framings, possibly identifying additional structural relationships between chirality and flavor indeterminacy.

---

## §8. Conclusion

This paper presents the structural mechanism that converts the NTE corpus §3.3 *Majorana Bridge* from asserted axiom into derivable consequence. The mechanism — chirality superposition in N + Hopf-projection failure at minimal Higgs coupling + vantage-point projection through each CPN-sector's active gauge symmetry — specifies the structure of the previously-underspecified unresolved state, enables a Connes Programme R3 reading of NCG Pati-Salam constructions (notably Boyle-Farnsworth 2020) wherein the two chirality irreps are vantage projections of one underlying configuration, and opens new prediction territory while preserving the existing §17.5.12 Majorana 0νββ falsifier as the current observational anchor.

The mechanism is structurally consistent with all five core NTE axioms (N fundamental, t emergent; surface only; S³ boundary; CPN-symmetric two-sector; Hopf projection). It does not introduce new ontological primitives; it makes explicit a structural mechanism that the existing axioms imply but did not fully spell out. Its primary structural payoff is in upgrading what §3.3 currently asserts to what §3.3 can now derive.

Phase B substantive structural-identification work (Jammer R&D territory) has been completed (R3 substantive closure at v10.9 framing canonical per Charter v1.2 §3). Jordan-from-octonion derivation (v10.10+ scope) is the next major Connes Programme research arc. Quantitative prediction development, §3.3 corpus prose update, and Paper 7 / Paper 7a consolidation are the medium-term programme.

---

## References

**NTE Corpus and Companion Papers:**

[1] White, G. *Null-Time Extension: Master Corpus* v10.8 (canonical v10.6.1 file pending v10.8 render). NTE Drive `1qtionVaUKQlBUw62izHVIGFNn_gKxSA3`. 2026.

[2] White, G. *Companion Paper: OctonionExtension* v10.6. NTE Papers/ `1UDHfRrdN0DfInJcHYpsB3b0tM4JMWBNZ`. 2026.

[3] White, G. *Companion Paper 7: Neutrino as Unresolved Geometry* v10.6. NTE Papers/ `1tdAeW99V4H-8aUHakGRlyimWMNTPJXYx`. 2026.

[4] White, G. *Companion Paper 6: Born Rule Activation at Gauge Birth.* NTE Papers/ (relevant for Born rule territory connections; §3.4 bilateral temporal extent — chirality superposition correspondence). 2026.

[5] White, G. *Companion Paper 1: Entanglement* v10.6. NTE Papers/ (relevant for relational quantum mechanics positioning depth, §6.1 RQM discussion). 2026.

**NTE Programme Documents:**

[6] White, G. *Connes Programme Charter v1.2.* NTE Stage/ `1gaOiRvXk_3niGm3j91WmR9j_SeaGgmmn`. 2026-05-14. Canonical Programme document; R3 substantive-pass reading captured in §3.

[7] AC consolidation. *v10.8 Elevation Supplement T1-CORPUS-8/9/10 (including §17.5.3 sharpening).* NTE Handoffs/ `1_KAC1GTSB6ksRXQOghs5JUQsHp-VJOfX`. 2026-05-12.

**Scratch Working Notes (Connes Programme R&D arc):**

[8] Scratch. *R3 Phase A Working Note: BF 2020 Sub-Question Analysis.* NTE Working/ `1qE8Wx4Ex9rMsq3I-tuQAC3NH0YpzajRv`. 2026-05-12.

[9] Scratch. *Track 2 Chirality-Superposition Mechanism Working Note.* NTE Working/ `19X8CF7rBssCxOfFdtKtPqedmw5Aeryu6`. 2026-05-13.

**Jammer Working Notes (Connes Programme R&D arc):**

[10] Jammer. *R3 Phase B Working Note: BF 2020 NTE Identification Map under Track 2 (v1).* NTE Working/ `10dZ800TOICC_0s7AnPJL9m8ipjETK75a`. 2026-05-13.

[11] Jammer. *R3 Phase B v1.1 Supplement: δN Intrinsic-Uniformity Reading.* NTE Working/ `1YRS68mtA6uNdlLMgK6MU7PVlqmFTzNIU`. 2026-05-13.

[12] Jammer. *R3 Phase B v1.2 Supplement: Prediction-Mapping Verification under R3 + Track 2.* NTE Working/ `1pIw4YWqQ6UBeEEayxfn4e2oLo0o4hYcU`. 2026-05-13. 14-prediction map canonical.

**External NCG / Pati-Salam Literature:**

[13] Boyle, L., and Farnsworth, S. *A new algebraic structure in the standard model of particle physics.* JHEP 06 (2018) 071. (BF 2018 — predecessor.)

[14] Boyle, L., and Farnsworth, S. *The standard model, the Pati-Salam model, and `Jordan geometry'.* arXiv:1910.11888 (2020). (BF 2020 — canonical Pati-Salam construction; R3 reading source per Charter v1.2 §3.)

[15] Furey, C. *Standard model physics from an algebra?* arXiv:1611.09182 (2018). (Octonion-based SM derivation programme.)

[16] Dixon, G. *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics.* Kluwer 1994. (Predecessor octonion-physics programme.)

**Adjacent Positioning Literature:**

[17] Rovelli, C. *Relational Quantum Mechanics.* Int. J. Theor. Phys. 35 (1996) 1637-1678. arXiv:quant-ph/9609002. (§6.1 RQM positioning.)

[18] Adamo, T., et al. *Lectures on Twistor Theory.* arXiv:1712.02196 (2017). (Forward-pointer for arxiv-target preparation; relates to M^C topology identity per Charter v1.2 §2.4.)

[19] Marcolli, M., and Penrose, R. *Gluing Non-Commutative Twistor Spaces.* Quart. J. Math. (2021), doi:10.1093/qmath/haab024. (Forward-pointer for arxiv-target preparation; NCG-twistor crossover canonical per Jammer corrective handoff 2026-05-14.)

---

*Paper 7a v1.1, 2026-05-15. Working note in `Working/`. Internal companion paper at current canonical status per Greg Tier A FIT 2026-05-14 publication-trajectory routing (a → b → c). Not for external circulation pending: AC v10.9 §3.3 corpus prose update integration; eventual arxiv-target preparation pass (b); PC book-side interpretation (c, per PC working note `1d3tTboR5ygUIEDNHH14_OMmqwVBdNWvX`).*

— Scratch (Connes Programme lead), 2026-05-15.
