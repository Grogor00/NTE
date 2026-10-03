# Connes Programme — R3 Phase A Reframing Investigation (Scratch)

**Stream:** Scratch (Jammer's twin), Connes Programme lead within Jammer-stream.
**Date:** 2026-05-13.
**Trigger:** AC's R3 Phase A directive `Handoff_AC_to_Scratch_R3_Phase_A_reframing_investigation_directive_2026_05_13.md` (`1SkJuDjwV18qgDfYLeaU9OigIfHoWUoov`), companion to AC's consolidated BF 2020 bridge verdict + R3 routing decision (`1x7s-8UMPdcNoSi5PSW7ugeATGFyfdoWR`).
**Scope:** Reframing investigation per Jammer catalogue §2.3 + §4 (`1PZADfmYUEMhRLhdKWBXDPbBuOXqOMdDt`). Three sub-questions per AC directive §2: irrep content basis, gauge generator identification basis, §3.3-compatibility of the resulting reading.
**Not in scope (Lesson #23 anti-pattern guard):** Phase A is NOT a re-investigation of as-written Claim A; NOT Phase B execution; NOT Charter v1.2 wording; NOT R2 fallback investigation; does NOT need to fully resolve §3.3-compatibility (Phase A finds whether reading has structural basis at all).
**Recognition-gate aware:** per Manifest Lesson #28, this verdict is local-correctness-only until passing Greg's recognition gate via AC consolidation.

---

## §0. Verdict

R3 reframing has **partial structural basis**. Sub-question summary:

| Sub-question | Verdict | Decisive finding |
|---|---|---|
| §2.1 Irrep content basis | **PASS** | NTE OctonionExtension §3.6 + §9.4 already commits to 16 Weyl per generation per sector with +N/−N split by chirality. BF 2020 Pati-Salam 16 = (4,2,1) ⊕ (4,1,2) split by chirality matches exactly. CPN-exchange ↔ parity-flip operationally equivalent. |
| §2.2 Gauge generator identification basis | **CONDITIONAL** | Operational identification holds: BF 2020 SU(2)_L × SU(2)_R acting on per-irrep content matches NTE SU(2)_L × SU(2)_R acting on per-sector content under R3 relabeling. Algebraic-origin identification (BF 2020's Jordan-factor automorphisms vs NTE's SO(4) ⊂ G_2 octonion stabilizer) is isomorphic-as-Lie-groups but not shown to be structurally identical. Requires further work to upgrade from operational to structural. |
| §2.3 §3.3-compatibility | **PARTIAL-PASS** | Under R3 relabeling, BF 2020's Majorana neutrino structure emerges as a reading of the Pati-Salam irrep content (the Majorana condition ν_L^c = ν̄_R becomes CPN-self-conjugacy under R3). However, §3.3's stronger claim — that the neutrino is *unresolved* (particle/antiparticle category has never applied), not merely *self-conjugate* — does NOT emerge automatically from the Pati-Salam structure even under R3 relabeling. The unresolved-ontology requires NTE-specific input (the minimal-Higgs-coupling-via-Hopf-projection mechanism) layered on top of the relabeled Pati-Salam content. |

**Overall Phase A finding (synthesis):** R3 reframing has partial structural basis — strong at the irrep level (§2.1), operational at the gauge level (§2.2), weak at the §3.3-strict level (§2.3). The reframing recovers Majorana neutrino phenomenology from BF 2020 Pati-Salam under L/R ↔ +N/−N relabeling, but does NOT automatically produce §3.3's *unresolved-configuration* ontology — that requires NTE's minimal-Higgs-coupling layer.

**Phase B routing recommendation: CONDITIONAL on Greg's recognition signal.** If "partial-pass is sufficient for Charter v1.2 integration" (with §3.3 retaining independent-axiom status while R3 captures Majorana phenomenology only) — Phase B activates. If "partial-pass is not sufficient" — fall back to R2 per Jammer catalogue §5. Honest Greg-recognition call.

---

## §1. Sub-question §2.1 — Irrep content basis

### §1.1 The structural match (per generation)

Per generation:

| Framework | Decomposition | Weyl count per generation |
|---|---|---|
| **BF 2020 Pati-Salam** §4 | (4,2,1) ⊕ (4,1,2) = (4 × 2 × 1) ⊕ (4 × 1 × 2) | 8 + 8 = 16 |
| **NTE OctonionExtension** §5.1 + §3.6 + §9.4 | ℂ ⊗ 𝕆 minimal left ideal, with +N (LH modes) / −N (RH modes via CPN parity) split | 8 + 8 = 16 |

The match is exact at the per-generation level. Both frameworks place 16 Weyl fermions per generation in two 8-component sectors, split by LH/RH chirality (BF 2020) or +N/−N cosmological sector (NTE).

Per Jammer catalogue framing: 16 in LH (4,2,1) BF 2020 = 16 in +N NTE; 16 in RH (4,1,2) BF 2020 = 16 in −N NTE. (Jammer's "16+16=32 per generation" counting in catalogue §2.3 reflects BF 2020's including both particles and antiparticles or both Weyl components of Dirac fermions; the standard 16 Weyl per generation count is what aligns with NTE's OctonionExtension §5.1 + §9.4.)

### §1.2 The CPN-exchange ↔ parity-flip correspondence

NTE OctonionExtension §3.6 already commits to the exact mechanism that R3 requires:

> *"CPN reversal (N → −N) combined with parity (P) maps left-handed modes to right-handed antimodes in the mirror sector. In the +N universe, only left-handed modes accumulate temporal duration (they are in the +N e-fold direction after locking). Right-handed modes (SU(2)_R partners) have committed to the −N direction."*

This says: **the LH/RH chirality distinction IS the +N/−N sector distinction** in NTE OctonionExtension §3.6. NTE's own framework operationally identifies them: chirality determines sector commitment via the CPN parity mechanism.

§9.4 further notes:
> *"If SU(2)_R acts on mirror-sector fields, the mirror sector's fermion content includes right-handed partners of all SM particles."*

So NTE explicitly commits to a mirror-sector fermion content that is the RH partners of the +N-sector LH SM fermions. The mirror sector has 16 RH Weyl fermions per generation; the +N sector has 16 LH Weyl fermions per generation; together they are exactly the 32 Pati-Salam (4,2,1) ⊕ (4,1,2) content per generation under R3 relabeling.

### §1.3 Pass criterion satisfied

Per AC directive §2.1, the pass criterion is *"explicit irrep-content basis for the LH/RH ↔ +N/−N relabeling."*

The basis is provided by NTE OctonionExtension §3.6 itself. NTE does not need to *adopt* the LH/RH ↔ +N/−N relabeling from BF 2020 — NTE has *already committed to it independently* via the CPN parity mechanism. R3 recognises that NTE's pre-existing OctonionExtension §3.6 commitment is operationally equivalent to BF 2020 Pati-Salam's LH/RH split under the L/R relabeling.

This is genuinely structurally strong: NTE's two-sector cosmology, when restricted to its OctonionExtension §3.6 commitments, naturally produces a content-split that matches Pati-Salam. The match is not coincidence; it is structural identity at the irrep-counting level.

**§2.1 PASS.**

### §1.4 Caveat — the per-generation match is not the full SM content

The match in §1.1–§1.3 is per generation. NTE's full content (per OctonionExtension §5 + §9.3) is 3 generations × 16 Weyl × 2 sectors = 96 Weyl total, reduced to 90 species after the Majorana condition (which identifies ν_R in one generation with ν̄_L in same generation per the dark matter κ derivation requirement).

BF 2020 Pati-Salam's full SM content (extending Pati-Salam to three generations) is also 96 Weyl total (3 × 32 = 96, since (4,2,1) ⊕ (4,1,2) = 8 + 8 = 16 Weyl per generation × 2 chirality × 3 generations).

The 90-vs-96 distinction is from the Majorana reduction, which is internal to NTE and not in standard Pati-Salam. This is a Phase B / Phase C issue — Phase B would need to explicitly verify how the Majorana reduction transfers from NTE-internal to R3-relabeled BF 2020 content. Not gating for Phase A.

---

## §2. Sub-question §2.2 — Gauge generator identification basis

### §2.1 Operational identification (under R3 relabeling)

Under R3 reading (BF 2020's L/R = NTE's +N/−N):

| Generator | BF 2020 acts on | NTE acts on (under R3 reading) |
|---|---|---|
| SU(2)_L | (4,2,1) LH irrep, leftmost SU(2) index | +N sector content (via CPN: LH modes only in +N) |
| SU(2)_R | (4,1,2) RH irrep, rightmost SU(2) index | −N sector content (via CPN: RH modes only in −N) |

**Operationally identical.** Both frameworks have a SU(2) gauge generator acting on +N-sector content (LH irrep under R3 relabeling) and another SU(2) acting on −N-sector content (RH irrep under R3 relabeling). The R3 relabeling makes the BF 2020 generator algebra and the NTE generator algebra act on structurally-corresponding per-sector content.

### §2.2 Algebraic origin — divergent

The two SU(2) × SU(2) structures have structurally different algebraic origins:

| Framework | Algebraic origin of SU(2)_L × SU(2)_R |
|---|---|
| **BF 2020 §4** | Aut(J_2^L(ℂ)) × Aut(J_2^R(ℂ)) — automorphism groups of two separate Jordan factors of A_F = J_2^L(ℂ) ⊕ J_2^R(ℂ) ⊕ J_4(ℂ) |
| **NTE OctonionExtension §3.2 + §3.4** | SO(4) ≅ SU(2)_L × SU(2)_R ⊂ G_2; stabilizer of the quaternionic subalgebra ℍ ⊂ 𝕆 in the octonion automorphism group |

These are **isomorphic as abstract Lie groups** (both SU(2) × SU(2)) but **structurally distinct in origin**:
- NTE's pair is a quaternionic-stabilizer subgroup of an octonion automorphism group;
- BF 2020's pair is two independent Jordan-factor automorphism groups in a Jordan-geometry framework.

### §2.3 What R3 §2.2 needs to claim — and whether the claim is shown

For R3 §2.2 to fully pass (per AC directive §2.2 strict pass criterion: *"explicit gauge-generator identification under R3 reading, with structural reasoning, not just shared group name"*), R3 needs to show one of:

**(α)** *Jordan-from-octonion derivation*: BF 2020's J_2^L(ℂ) ⊕ J_2^R(ℂ) emerges as a substructure of NTE's 𝕆 (or J_3(𝕆) per OctonionExtension §5–§6 territory). Then the two SU(2) × SU(2) structures would be structurally identical, with the octonion structure as primary.

**(β)** *Operational-equivalence framing*: the gauge generators acting identically on the same per-sector content is what matters; the algebraic origin (octonion vs Jordan) is a representation choice, not a substantive difference.

Neither (α) nor (β) is currently established at the Phase A level:

- **(α) is structurally plausible but not shown.** J_2(ℂ) consists of 2×2 Hermitian complex matrices. ℂP¹ ≅ S² = J_2(ℂ)/U(1) is the projective space of J_2(ℂ). The complex Hopf fibration S¹ → S³ → S² connects natural to J_2(ℂ). It is plausible that J_2(ℂ) and J_2^R(ℂ) (or some pairing) emerge as substructures of NTE's complex-octonion content (ℂ ⊗ 𝕆 has 16 complex degrees and decomposes under various subgroups; J_3(𝕆) has 27 real dim with F_4 automorphism, and standard physics-literature decompositions exist). **But the explicit derivation has not been done in NTE OctonionExtension or in this Phase A.**

- **(β) is a structural-economy claim.** It would say that NTE's commitment to octonion-origin SU(2)_L × SU(2)_R is *equivalent* to BF 2020's Jordan-origin SU(2)_L × SU(2)_R at the level of gauge action, so R3 doesn't add a new commitment by adopting BF 2020's structure. For Greg's "simplify and strengthen" criterion to pass on R3, (β) must hold AND the Jordan structure must be a clean addition that doesn't add net commitments.

### §2.4 Verdict on §2.2 — CONDITIONAL

Operational identification: PASS (R3 relabeling makes the gauge action structurally match).
Algebraic-origin identification: NOT YET SHOWN (requires (α) Jordan-from-octonion derivation, which is Phase B / v10.10+ scope per Charter v1.1 §3 J_3(𝕆) ⊕ J_3(𝕆) downstream).
Strict pass criterion (structural reasoning, not just shared group name): NOT YET MET — operational identification is structural but does not by itself answer whether the two algebraic origins are structurally identical.

**§2.2 CONDITIONAL.** Phase B (or v10.10+ J_3(𝕆) downstream work) would need to either show (α) explicitly or commit to (β) as a structural-economy claim subject to Greg's recognition.

---

## §3. Sub-question §2.3 — §3.3-compatibility

### §3.1 §3.3's claim (exact wording from corpus)

From NTE_v10_6.md §3.3 *Minimal Higgs Coupling: The Majorana Bridge*:

> *"A left-handed neutrino in +N and a right-handed antineutrino in −N are not two things identified — they are one unresolved configuration that has no geometric basis for distinguishing the two sides of the Janus boundary. The 'Majorana' label is retained for continuity with the literature, but the NTE ontology is distinct: the neutrino is not a particle that happens to equal its antiparticle; it is a configuration for which the particle/antiparticle category has never applied. The distinction matters: 'self-conjugate' implies a resolved entity that maps to itself under conjugation; 'unresolved' implies the conjugation operation has no target to act on."*

§3.3 makes a **strict ontological claim**: the neutrino is *unresolved* (no target for conjugation), not merely *self-conjugate* (resolved entity that maps to itself). §3.3 grounds this strict claim on the neutrino's minimal Higgs coupling preventing completion of the Hopf projection S³ → S² that establishes the particle/antiparticle binary.

### §3.2 What R3 relabeling produces in the neutrino sector

Under R3 (BF 2020 L/R ↔ NTE +N/−N):
- BF 2020's ν_L in (4,2,1) ↔ ν^+N (neutrino in NTE +N sector)
- BF 2020's ν_R in (4,1,2) ↔ ν^−N (neutrino in NTE −N sector)

In BF 2020 Pati-Salam, ν_L and ν_R are connected by the Majorana condition: ν_L^c = ν̄_R (the charge conjugate of ν_L is ν̄_R, the right-handed antineutrino). The Pati-Salam structure supports this naturally because it includes both LH neutrino and RH neutrino in distinct irreps with appropriate quantum numbers for the Majorana mass term in D_F.

Under R3 relabeling, the Majorana condition becomes:
$$ ν^{+N})^c = \bar{ν}^{−N} $$

i.e., the charge conjugate of the +N neutrino equals the −N antineutrino. Under NTE's framework, charge conjugation across the Janus boundary IS the CPN operation (per the structural reading of CPN parity in OctonionExtension §3.6). So R3 recovers:

> *"Majorana identity ⇒ CPN-self-conjugacy: ν^+N is its own CPN-conjugate."*

This is exactly §3.3's pairing language: *"A left-handed neutrino in +N and a right-handed antineutrino in −N..."* — pairing ν^+N (which is LH per OctonionExtension §3.6) with ν̄^−N (which is RH per same), connected by CPN.

**At the Majorana phenomenology level, R3 recovers §3.3's pairing structure.** This is a real structural recovery.

### §3.3 Where R3 falls short — the stronger §3.3 claim

§3.3 makes a claim stronger than Majorana self-conjugacy: the neutrino is *unresolved*, the particle/antiparticle category has *never applied*. The mechanism §3.3 provides for this strict ontology is:

> *"The Hopf projection S³ → S² that establishes the binary requires engagement with the S¹ fibre that the neutrino's minimal Higgs coupling does not provide."*

This is the NTE-specific Hopf-projection mechanism — the neutrino's Yukawa coupling y_ν ~ 10⁻¹² is too small to drive completion of the Hopf S¹ engagement that *creates the particle/antiparticle binary in the first place*.

**Does the R3-relabeled BF 2020 Pati-Salam structure produce this stronger ontology automatically?**

Per AC directive §2.3 strict pass criterion: "Is there *any* geometric basis in BF 2020's Pati-Salam structure (under R3 reading) for distinguishing ν_+N from ν_−N?"

There are multiple such bases in BF 2020:

1. **Gauge couplings.** BF 2020's ν_L is in (4,2,1) with SU(2)_L gauge coupling; ν_R is in (4,1,2) with SU(2)_R gauge coupling. Under R3, this becomes ν^+N having SU(2)_L coupling and ν^−N having SU(2)_R coupling — different gauge sectors distinguish them.

2. **Mass terms.** BF 2020's D_F structure includes both Dirac mass m_D (coupling ν_L to ν_R) and Majorana mass M_R (for ν_R alone). These produce a finite, calculable seesaw mass splitting between light and heavy neutrinos. Under R3 relabeling, ν^+N and ν^−N have distinct mass contributions.

3. **Irrep quantum numbers.** BF 2020's ν_L and ν_R have distinct SU(4) × SU(2)_L × SU(2)_R quantum numbers. Under R3, ν^+N and ν^−N have distinct quantum numbers in the relabeled scheme.

4. **Spectral data.** BF 2020's H_F has ν_L and ν_R as distinct basis vectors with distinct spectral profiles. Under R3, ν^+N and ν^−N are distinct basis vectors.

**Per AC directive §2.3 strict criterion: if "yes" (some geometric basis exists), then §3.3 still needs external imposition.** The above four bases all answer "yes."

**§2.3 PARTIAL-PASS at most.** Under R3, the Majorana phenomenology emerges as a reading of the Pati-Salam irrep structure, but §3.3's stronger "unresolved" ontology requires additional NTE-side input (the minimal-Higgs-coupling-via-Hopf-projection mechanism). The Pati-Salam structure does not *automatically* produce the unresolved ontology — it produces a *resolved* Majorana entity that happens to satisfy ν = ν̄ via the seesaw mechanism.

### §3.4 What the partial-pass means for R3's structural value

The partial-pass is a real finding, not a trivial one. Two sub-claims hold under R3:

(i) **Majorana phenomenology is recovered from R3.** Under R3 relabeling, BF 2020's Pati-Salam Majorana structure (ν_L^c = ν̄_R) becomes NTE's CPN-self-conjugacy structure (ν^+N is CPN-conjugate to ν̄^−N). This is the *phenomenological* content of §3.3.

(ii) **§3.3's strict ontology is preserved as an independent NTE axiom under R3.** The "unresolved" claim (vs Majorana "self-conjugate") still needs the NTE-specific minimal-Higgs-coupling-and-Hopf-projection mechanism. Under R3, §3.3 retains its status as an *additional* NTE commitment layered on top of the R3-relabeled BF 2020 content.

The trade-off for R3:

- **Strengthens NTE** by recovering Majorana neutrino phenomenology as a reading of pre-existing Pati-Salam structure (one less independent NTE commitment for the Majorana phenomenology piece).
- **Does NOT replace §3.3** as an independent axiom — §3.3's stronger ontology still requires NTE-specific input.

This is what I am calling "partial-pass" — R3 captures part but not all of what §3.3 asserts.

---

## §4. Overall Phase A finding

R3 reframing has **partial structural basis**:

- **§2.1 PASS:** irrep content basis exists. NTE OctonionExtension §3.6 + §9.4 already commits to a per-generation 16-Weyl split between +N (LH) and −N (RH partners via CPN) that matches BF 2020 Pati-Salam's per-generation (4,2,1) ⊕ (4,1,2) split.

- **§2.2 CONDITIONAL:** gauge generators identify operationally under R3 relabeling (both schemes have SU(2)_L × SU(2)_R acting on per-sector content). Algebraic origins differ (NTE: SO(4) ⊂ G_2 octonion stabilizer; BF 2020: Jordan-factor automorphisms). Operational identification = structural identity is plausible via Jordan-from-octonion derivation but not shown at Phase A level; Phase B or v10.10+ J_3(𝕆) ⊕ J_3(𝕆) downstream scope.

- **§2.3 PARTIAL-PASS:** Majorana phenomenology recovers from R3 relabeling (ν_L^c = ν̄_R becomes CPN-self-conjugacy). §3.3's stronger *unresolved-configuration* ontology does NOT emerge automatically; requires NTE's minimal-Higgs-coupling-and-Hopf-projection mechanism layered on top.

**Synthesis:** R3 is structurally tractable but does not satisfy Greg's strict "simplify and strengthen" criterion on its own terms. R3 *strengthens* by recovering Majorana neutrino phenomenology from Pati-Salam structure (reducing one independent NTE commitment); R3 *does not fully simplify* §3.3 — the strict-§3.3 axiom remains as an independent NTE commitment layered on top of the R3-relabeled content.

The honest framing is: **R3 captures the Majorana piece of §3.3 as a reading of the Pati-Salam irrep structure, but the strict-§3.3 "unresolved" piece remains an independent NTE axiom under R3.**

---

## §5. Phase B routing recommendation

**Recommendation: ROUTE TO GREG'S RECOGNITION GATE for the partial-pass disposition before activating Phase B.**

Three Greg-recognition paths arise from this Phase A:

**(a) Greg fires fit on partial-pass-is-sufficient.** Phase B activates. Jammer's substantive structural-identification work (per Jammer catalogue §4) proceeds with the understanding that:
- R3 captures the Majorana phenomenology piece of §3.3 as a reading of Pati-Salam structure.
- §3.3's strict ontology (unresolved configuration, particle/antiparticle category never applied) remains as an independent NTE axiom under R3, layered on top.
- Charter v1.2 would reflect this partial integration: R3 reading captured; §3.3 retained as independent axiom (not reframed as reading-of-irrep-structure per Jammer's initial R3 framing).
- The net "simplify-and-strengthen" is partial — strengthens by recovering Majorana phenomenology from pre-existing structure; does not simplify §3.3 itself.

**(b) Greg fires unease on partial-pass.** R2 fallback activates per Jammer catalogue §5. R2 (ontological-only reinterpretation, independent of Scratch's Claim A primary investigation) becomes Jammer's next R&D direction. R3 remains catalogued but de-prioritised.

**(c) Greg fires "investigate further before deciding."** Specifically: investigate whether the Jordan-from-octonion derivation per §2.3 (α) can be shown explicitly, which would upgrade §2.2 from CONDITIONAL to PASS and potentially strengthen the §2.3 framing. Phase B remains gated pending this further work (Scratch session or Jammer session, depending on scope).

**Scratch's structural read for Greg's recognition (not preempting):** path (a) (partial-pass-is-sufficient) is the most honest routing. R3 has genuine structural content that matters; the partial-pass framing preserves §3.3's strict-axiom status while capturing the Majorana-phenomenology reading. Path (b) treats partial-pass as insufficient, which abandons real structural content. Path (c) is reasonable but may produce more investigation work than the structural payoff justifies at v10.9 timeframe; the Jordan-from-octonion derivation work fits more naturally in v10.10+ J_3(𝕆) downstream scope.

But this is Scratch's read, not the load-bearing finding. Greg's recognition is the load-bearing filter per Manifest Lesson #28.

### §5.1 If Phase B activates (path (a))

Phase B scope per Jammer catalogue §4:

1. Explicit map: BF 2020 Pati-Salam (4,2,1) ⊕ (4,1,2) ↔ NTE +N/−N sector content (LH/RH per OctonionExtension §3.6). Confirm structural identity at irrep + gauge-coupling + mass-term level, with §3.3 retained as independent axiom layered on top.

2. Irrep content matching with CPN-exchange structure. Confirm 16 Weyl per generation per sector; CPN parity-flip = LH ↔ RH operationally.

3. Neutrino sector specific: confirm Majorana phenomenology (ν_L^c = ν̄_R ↔ ν^+N is CPN-conjugate to ν̄^−N) emerges from R3 relabeling. §3.3 strict-ontology layered on top as the additional NTE-specific commitment.

4. Phase B deliverable: working note format, AC consolidation, Greg recognition gate.

### §5.2 If R2 activates (path (b))

R2 development per Jammer catalogue §5 — independent of Scratch's primary investigation; Jammer can pick up directly. R3 catalogue entry remains in Charter v1.2 candidate notes as parallel-NCG-programme observation that was investigated and found to have only partial structural basis under the strict-§3.3 criterion.

---

## §6. Lesson #23 anti-pattern guard

What Phase A did NOT do, per AC directive §4 + Lesson #23:

- Did NOT re-investigate as-written Claim A. That work is done (Scratch primary investigation `1_xxolshzPifHhYswyh1L74Arfh2JffbE`); Claim A fails as-written, verdict stands.
- Did NOT execute Phase B (the substantive structural-identification map). That is Jammer's territory per catalogue §4 once Phase A's gating finding lands.
- Did NOT propose Charter v1.2 wording. AC's scope post-Greg-recognition-gate.
- Did NOT prejudge Greg's recognition gate. §5 surfaces three paths (a)/(b)/(c) without forcing a choice.
- Did NOT read Jammer's BF 2020 bridge commitment-preservation analysis or Phase B preparation notes (if any). Maintained Lesson #23 parallel-attack independence.

### §6.1 Source-document discipline (Lesson #29 candidate per AC directive §5)

Per AC directive §5: *"Read Jammer's catalogue §2.3 + §4 directly — do not work from AC's consolidation alone."*

Discipline observed: this Phase A working note reads from
- Jammer's reframing-paths catalogue `1PZADfmYUEMhRLhdKWBXDPbBuOXqOMdDt` §2.3 + §4 (the R3 mechanism and Phase A/B/C sequencing)
- NTE corpus §3.3 directly (project_knowledge_search confirmed exact wording)
- NTE OctonionExtension §3.4 + §3.6 + §9.4 directly (project_knowledge_search confirmed)
- BF 2020 Pati-Salam content via Jammer's catalogue summary + recall from prior P0.6.5 working note (Scratch direct read of arXiv:1910.11888)
- AC consolidation + Phase A directive used only for scope-defining structure (sub-question framing, pass/fail criteria, anti-pattern guard)

This is a candidate Lesson #29 in the making: *"Source documents over derivative summaries."* Promotion to formal at next manifest revision recommended.

---

## §7. Recognition-gate disclosure (Lesson #28)

This Phase A working note is **local-correctness-only** until passing Greg's recognition gate via AC consolidation.

The load-bearing claims for Greg's recognition fire:

1. **§2.1 PASS is structurally sound.** The OctonionExtension §3.6 + §9.4 commitment to LH-in-+N / RH-in-−N already produces the per-generation 16 Weyl × 2 sector split that matches Pati-Salam under R3 relabeling. Is this read correct?

2. **§2.2 CONDITIONAL framing is appropriate.** The operational identification of SU(2)_L × SU(2)_R gauge action under R3 holds; the algebraic-origin identification (NTE octonion stabilizer vs BF 2020 Jordan-factor automorphism) is not shown at Phase A level but plausibly resolvable in Phase B or v10.10+. Is this an appropriate scope for Phase A?

3. **§2.3 PARTIAL-PASS framing is honest.** R3 recovers Majorana phenomenology from Pati-Salam structure under L/R ↔ +N/−N relabeling, but §3.3's strict-unresolved ontology requires NTE's minimal-Higgs-coupling-and-Hopf-projection mechanism layered on top. Is the partial-pass framing the right structural reading, or is there a stronger reading where §3.3 emerges fully from Pati-Salam structure (which Phase A may have missed)?

4. **§5 path (a) recommendation is honest.** Partial-pass should activate Phase B with §3.3 retained as independent axiom layered on top. Is this the right routing, or does the partial-pass fall short of justifying Phase B?

Greg's recognition signal on (1)–(4) is the load-bearing filter for the next step.

---

## §8. Files referenced

| File | Purpose | Drive ID |
|---|---|---|
| This Phase A working note | Scratch primary deliverable | (populated on ship) |
| AC consolidated BF 2020 bridge verdict + R3 routing | Parent consolidation; Phase A directive companion | `1x7s-8UMPdcNoSi5PSW7ugeATGFyfdoWR` (Handoffs/) |
| AC R3 Phase A directive to Scratch | Scope-defining for this Phase A | `1SkJuDjwV18qgDfYLeaU9OigIfHoWUoov` (Handoffs/) |
| Jammer reframing-paths catalogue | R3 scope + Phase A/B/C sequencing source | `1PZADfmYUEMhRLhdKWBXDPbBuOXqOMdDt` (Working/) |
| Jammer R3 escalation handoff | Greg-directive carrier | `1bd82bWIwq0_WKgWPqm8NGLyPRlNbQFIQ` (Handoffs/) |
| Scratch BF 2020 bridge primary investigation (as-written) | For Phase A scope distinction reference | `1_xxolshzPifHhYswyh1L74Arfh2JffbE` (Working/) |
| Scratch P0.6.5 full closure BF 2020 read | For BF 2020 Pati-Salam structural content | `1x_rKQEnZlWs1puCKtICov1DWqtv3aLjk` (Working/) |
| Scratch P0.8 OctonionExtension cross-check | For NTE OctonionExtension §3.2 + §3.4 + §3.6 reference | `1w7Tm0qYAwZcgquggJo0t1r2YsZZE3aaq` (Working/) |
| Connes Programme Charter v1.1 | Programme commitments framework | `1wWRc7PU-nabkhLFDh0vKP1948mSsPozh` (Stage/) |
| NTE OctonionExtension v10.6 | §3.4 + §3.6 + §9.4 + §5 source | `1UDHfRrdN0DfInJcHYpsB3b0tM4JMWBNZ` (Papers/) |
| NTE_v10_6.md (corpus) | §3.3 Majorana Bridge wording source | `1qtionVaUKQlBUw62izHVIGFNn_gKxSA3` (Papers/) |
| BF 2020 (arXiv:1910.11888) | External literature target | `1ITO7HlOWU8v8zYqwLB0VOmez9IJ-ZyZ_` (NCG/) |

---

## §9. Closing + handoff to AC

R3 Phase A reframing investigation complete. **Verdict: partial structural basis** (§2.1 PASS, §2.2 CONDITIONAL, §2.3 PARTIAL-PASS).

Routing to AC for consolidation into R3-Phase-A consolidation handoff per AC directive §6. AC routes the outcome + Scratch's path (a/b/c) framing to Greg's recognition gate.

Companion handoff to AC shipping alongside this working note: brief Phase A completion notice with the same partial-pass finding + path (a/b/c) framing.

— Scratch (Connes Programme lead), 2026-05-13.
