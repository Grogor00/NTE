# Jammer Working Note — External-Paper-to-NTE-Ontology Reframing Paths Catalogue

**Stream:** Jammer (R&D, single session)
**Date:** 2026-05-13
**Status:** Reframing-paths catalogue per Greg's directive 2026-05-13: *"The neutrino is not resolved as either RH or LH, primary axiom, that is enough to filter tension. UNLESS we can find a way that external papers can be reframed or adapted to our ontology."* Working note Option 3 with bias toward R3.
**Target location:** `Working/External_Paper_Reframing_Paths_Catalogue_Jammer_v1.md` (via create+copy per Lesson #24)
**Recognition-gate context (Lesson #28):** §3.3 Majorana Bridge ontology has received Greg's recognition-gate fire FIT this turn (signal: "primary axiom, enough to filter tension"). The §3.3 reading is therefore canonical for this catalogue. Reframing exploration operates UNDER the constraint that §3.3 is preserved.
**Predecessor:** `Working/BF2020_Bridge_Commitment_Preservation_Analysis_Jammer_v1.md` (`1cs_VAHj3Eo7BDsf_nt2mQaCGzSkPBCxH`) — the verdict that filtered BF 2020 bridge integration and surfaced the reframing question.

---

## §0 — Purpose and scope

This catalogue documents the structural landscape of *"how can external NCG/spectral-geometry/Jordan-geometry papers be reframed or adapted to NTE's ontology"* — specifically under the §3.3 Majorana Bridge constraint (neutrinos are not resolved as either RH or LH; one unresolved configuration across the Janus boundary).

**What this catalogue is**: a working document of four candidate reframing directions (R1-R4), their structural mechanics, their dependencies on other Programme inputs, and their development-effort estimates. Working document for Scratch + AC + Greg engagement as AC consolidates the BF 2020 bridge verdict.

**What this catalogue is NOT**:
- A finished reframing — execution depends on AC's consolidated BF 2020 bridge verdict + Scratch's primary-investigation Claim A finding (for R3 specifically) + further structural work.
- A replacement for Scratch's primary-investigation work — that work is upstream of any R3 development.
- An auto-integration path — per Lesson #28, no reframing graduates to Charter v1.2 without Greg's recognition gate.

**Greg's recognition signal for catalogue**: R3 bias requested. Catalogue documents R1-R4 evenly at the structural level but flags R3 as the priority development direction.

---

## §1 — The constraint (canonical from §3.3)

NTE §3.3 *Minimal Higgs Coupling: The Majorana Bridge*:

> *"The neutrino is neither particle nor antiparticle — it is an unresolved configuration, smeared across the fibre rather than projected onto S². A left-handed neutrino in +N and a right-handed antineutrino in −N are not two things identified — they are one unresolved configuration that has no geometric basis for distinguishing the two sides of the Janus boundary. ... The neutrino is not a particle that happens to equal its antiparticle; it is a configuration for which the particle/antiparticle category has never applied."*

**Greg's recognition signal 2026-05-13**: *"The neutrino is not resolved as either RH or LH, primary axiom, that is enough to filter tension."*

**Operational constraint**: any reframing of an external paper must preserve this. Specifically:
- External-paper "RH neutrino" content must NOT map to "distinct fundamental basis vector with its own particle/antiparticle structure" in NTE.
- External-paper LH/RH labels must either (i) not apply to neutrinos at the NTE level, or (ii) map to NTE-internal labels (e.g., +N/−N cosmological sectors) that preserve §3.3's "one unresolved configuration" reading.

**Reframing test**: under what reinterpretation does external-paper algebraic + representation structure produce predictions/structure compatible with §3.3?

---

## §2 — The four reframing directions

### §2.1 R1 — Sterile-RH-neutrino-as-decoupled-basis-vector

**Move**: adopt the external paper's full mathematical structure (algebra, Hilbert space, representation). Set Dirac-operator entries connecting LH and RH neutrinos to zero, so ν_R has no physical mass term. ν_R remains as a basis vector (required for algebraic consistency, e.g., U(1)_{B-L} outer-automorphism in BF 2020) but does not propagate as a physical particle.

**Status of compatibility with §3.3**: **PARTIAL**. R1 demotes ν_R to "sterile" — algebraically present but physically inert. §3.3 demands more: the LH neutrino + RH (anti)neutrino are NOT two things, they are ONE unresolved configuration. R1 still treats them as two distinct basis vectors with different ontological status (one resolved, one inert). §3.3 wants the basis-vector distinction itself absent at the ontological level.

**Effort to develop**: LOW. This is essentially the standard "sterile RH neutrino" reading in NCG literature. BF 2020 already describes them as "sterile" in their abstract. The work is to identify what additional NTE-side commitment makes R1 fall short of §3.3 (and document why §3.3 is stricter than just "sterile").

**Failure mode**: R1 fails the §3.3 strictness test. Useful for documenting how §3.3 differs from standard sterile-neutrino frameworks, not as an integration path.

**Verdict**: NOT a viable reframing for §3.3-preserving integration. Worth documenting in Charter v1.2 as "what §3.3 does NOT mean (R1 is too weak)."

### §2.2 R2 — Ontological-only reinterpretation

**Move**: adopt the external paper's full mathematical structure (algebra, Hilbert space, Dirac operator). Reinterpret what the external paper calls "RH neutrino basis vector" as part of the SAME unresolved configuration NTE §3.3 describes. The 96-dim H_F (BF 2020 case) carries a representation where the algebraic distinction between ν_L and ν_R basis vectors does NOT correspond to an ontological particle/antiparticle distinction at the NTE level.

**Mechanism**: requires explicit check that D_F structure can support this reading. Specifically:
- If D_F has only Majorana-type mass entries on the neutrino sector (M_R for ν_R alone, no Dirac coupling m_D between ν_L and ν_R), then ν_L and ν_R are not Dirac partners in the physical sense — they could be reinterpreted as two basis vectors carrying one unresolved configuration.
- If D_F has Dirac coupling m_D, then ν_L and ν_R are dynamically coupled as particle/antiparticle in the standard Dirac sense — §3.3 incompatible.

**Status of compatibility with §3.3**: CONDITIONAL on D_F structure. If D_F is configurable to satisfy the no-Dirac-coupling condition, R2 produces a reading where:
- Algebra: BF 2020 structure intact
- Representation: 96-dim Hilbert space intact
- Dynamics: neutrino sector has Majorana mass only; no Dirac neutrino mass
- Ontology: ν_L + ν_R basis vector pair = one §3.3 unresolved configuration

**Effort to develop**: MODERATE. Requires:
1. Explicit D_F structure check in BF 2020 (or NCG-SM): does the standard construction force Dirac neutrino mass?
2. If yes — does the algebra admit a modification that removes the Dirac mass without breaking other structure?
3. If yes — what does the modified D_F predict for neutrino phenomenology? (Specifically: does it preserve §17.5.12 Majorana 0νββ falsifiability?)
4. Consistency check with NTE corpus §3.3 ontology

**Dependency**: independent of Scratch's Claim A primary investigation. R2 can be developed even if R3's structural identification fails.

**Verdict**: VIABLE candidate. Lower priority than R3 because R3 has the structural-strengthening property R2 lacks. Worth retaining as fallback if R3 fails on Claim A consolidation.

### §2.3 R3 — External-paper LH/RH labels reinterpreted as NTE +N/−N cosmological sectors **(PRIORITY DIRECTION)**

**Move**: identify what BF 2020 (or similar external papers) call "LH" and "RH" with NTE's "+N sector" and "−N sector" cosmological labels. External-paper "RH neutrino in the (4,1,2) irrep of Pati-Salam" becomes "neutrino in NTE's −N sector."

Under §3.3: LH-neutrino-in-+N and RH-antineutrino-in-−N are one unresolved configuration. Under R3 reading: external-paper Pati-Salam's full fermion content (16 fermions in (4,2,1) + 16 fermions in (4,1,2)) = NTE's two-sector cosmology (16 fermions in +N sector + 16 fermions in −N sector). The neutrinos within them are the same unresolved configuration across the Janus boundary — exactly what §3.3 asserts.

**Mechanism**: depends critically on Scratch's Claim A — *"SU(2)_L × SU(2)_R structural identification between BF 2020 Pati-Salam (Aut(A_F) = SU(2)_L × SU(2)_R × SU(4)) and NTE OctonionExtension §3.6 (SU(2)_L commits to +N sector; SU(2)_R commits to −N sector via SO(4) ≅ SU(2)_L × SU(2)_R embedding in G_2)."*

If Claim A holds at structural level (not just symbol-matching): then the LH/RH labels in external papers ARE the +N/−N sector labels in NTE, by structural identity. The "RH neutrino" of external papers IS the neutrino in NTE's −N sector. §3.3 ontology is preserved automatically — the "one unresolved configuration across the Janus boundary" emerges as a reading of the two-irrep structure that external papers already have.

**Status of compatibility with §3.3**: STRUCTURALLY EXACT if Claim A holds. **The external paper's mathematical content becomes a representation of NTE's two-sector cosmology under R3 reading.** §3.3 doesn't need to be imposed externally — it becomes a reading of the irrep structure.

**Strengthen test** (per Greg's criterion): YES. R3 potentially reduces NTE's foundational-commitment count. NTE currently commits independently to:
1. CPN-symmetric two-sector cosmology
2. §3.3 Majorana Bridge ontology
3. OctonionExtension §3.6 SU(2)_L / SU(2)_R sector commitment

Under R3, items 1 and 2 become readings of the external-paper irrep structure (if Claim A makes item 3 structurally true). Net: −1 or −2 commitments under R3, with the external-paper Pati-Salam structure providing the reading.

**Simplify test** (per Greg's criterion): YES IF the external-paper adoption doesn't add net new commitments elsewhere. The trade is: drop independent commitments 1+2; add commitment to "external-paper Pati-Salam structure as canonical representation of NTE's two-sector content." Whether this is net-simplify depends on whether the external-paper Pati-Salam structure is itself a clean structural commitment (it likely is — it's a well-defined Jordan-geometry construction in BF 2020 §4).

**Dependency**: R3 is gated on AC's consolidated BF 2020 bridge verdict, specifically on Claim A primary-investigation finding (Scratch's working note `1bBjR2oG3pICD9AGnNONBRfFB4bxEGYwh`, not read by me per Lesson #23). 

**Effort to develop (once Claim A consolidation lands)**: MODERATE-HIGH. Requires:
1. Explicit structural-identification map between BF 2020 Pati-Salam LH/RH labels and OctonionExtension §3.6 +N/−N labels (the *substantive* check that Claim A is structurally true, not just symbol-matching)
2. Verification that the irrep content matches: BF 2020 Pati-Salam has 16 fermions per generation in each LH/RH sector; NTE's two-sector cosmology must support 16 fermions per generation in each +N/−N sector with appropriate CPN-exchange structure
3. Charter v1.2 update: §3.3 Majorana Bridge ontology becomes reading-of-irrep-structure rather than independent axiom; CPN-symmetric two-sector commitment becomes reading-of-Pati-Salam-Aut(A_F) rather than independent commitment
4. Corpus integration: §3.3 prose updated to reflect the R3 reading; falsifiability statements (§17.5.12) reframed to match the R3 structure
5. v10.10+ scope: J_3(𝕆) ⊕ J_3(𝕆) downstream work informed by R3 if Pati-Salam structure carries forward

**Verdict**: **PRIORITY DIRECTION**. R3 has structural-strengthening properties R1, R2, and R4 lack. The strengthening is genuine: NTE's two-sector axioms become readings of external-paper structure rather than independent commitments. Caveats: depends on Claim A consolidation, and requires substantive structural-identification work that hasn't been done yet.

### §2.4 R4 — J_3(𝕆) construction with structurally distinct neutrino content

**Move**: construct (or adopt) a Jordan-geometry on J_3(𝕆) where the 3×3 octonion matrix structure naturally separates "particles that engage Hopf S¹ fibre" (charged fermions post-Hopf-projection) from "configurations that don't" (neutrinos as unresolved). §3.3 emerges from the algebraic structure of J_3(𝕆) rather than being imposed axiomatically.

**Mechanism**: speculative. The exceptional Jordan algebra J_3(𝕆) has 27 real dimensions; its automorphism group is F_4. The structural content of how F_4 representations decompose under SU(3) × SU(3) (or other relevant subgroups) might naturally produce a "Hopf-resolution-distinguished" sector structure — but this is not currently established in either external literature or NTE OctonionExtension §6.

**Status of compatibility with §3.3**: PRINCIPLE-COMPATIBLE if the speculative mechanism resolves; not currently demonstrated.

**Effort to develop**: HIGH. Long-horizon work. OctonionExtension §6 self-describes as "programme, not completed derivation." Requires:
1. Develop OctonionExtension §6 to closed derivation status
2. Explicit construction of J_3(𝕆)-based spectral triple with §3.3-compatible fermion content
3. Verification that Gilkey heat-kernel extends to J_3(𝕆) construction (outside BF 2013's alternative-algebra scope per my P0.7 caveat (c))
4. Phenomenological matching to SM

**Dependency**: independent of Scratch's Claim A but depends on OctonionExtension §6 maturation. v10.10+ horizon.

**Verdict**: V10.10+ HORIZON DIRECTION. Not actionable until OctonionExtension §6 matures. Worth keeping in catalogue as long-term research target. Could become the most structurally coherent reframing if it resolves, since §3.3 would emerge from the algebra rather than being independent axiom.

---

## §3 — Compatibility and priority matrix

| Path | §3.3 compatibility | Greg's "simplify and strengthen" | Dependency | Effort | Verdict |
|---|---|---|---|---|---|
| **R1** | Partial — sterile is weaker than one-unresolved-configuration | Neither | None | Low | Not viable for integration |
| **R2** | Conditional on D_F structure | Possibly strengthen; neutral on simplify | None | Moderate | Viable fallback |
| **R3** | Structurally exact if Claim A holds | **Yes on both axes** | Scratch's Claim A consolidation | Moderate-High | **PRIORITY DIRECTION** |
| **R4** | Principle-compatible if speculative mechanism resolves | Strongest strengthen if it resolves | OctonionExtension §6 maturation | High | v10.10+ horizon |

**Priority order**: R3 > R2 > R4 > R1.

R3 is priority because:
1. It is the only direction that satisfies Greg's "simplify and strengthen" criterion on both axes (per §2.3 analysis).
2. The structural strengthening is genuine: NTE foundational commitments become readings of external-paper structure.
3. It is actionable at v10.9 timeframe (vs R4 which is v10.10+).
4. The dependency (Scratch's Claim A) is already in flight via AC's consolidation.

---

## §4 — What R3 development requires

For Scratch + AC visibility — R3 development sequencing:

**Phase A (gated on AC's consolidated BF 2020 bridge verdict)**:
- Receive Claim A finding from Scratch's primary investigation
- If Claim A finds structural identification true → proceed to Phase B
- If Claim A finds symbol-matching coincidence → R3 fails; fall back to R2 as alternative

**Phase B (assuming Phase A passes)** — substantive R3 structural work:
1. Explicit map: BF 2020 Pati-Salam LH/RH ↔ NTE +N/−N sector labels. Confirm structural identity (not just isomorphic SU(2) groups).
2. Irrep content matching: 16 fermions per generation in each sector. Verify CPN-exchange structure on BF 2020 Pati-Salam side matches NTE's two-sector exchange.
3. Neutrino sector specific: confirm that BF 2020's "ν_L in (4,2,1)" + "ν_R in (4,1,2)" reads as NTE's "neutrino in +N sector" + "neutrino in −N sector" as one unresolved configuration. Specifically: there should be NO Hopf-projection-induced binary distinguishing these — they should be reading the same configuration from opposite sides of the Janus boundary.

**Phase C — corpus integration**:
1. Charter v1.2: R3 reading captured. §3.3 Majorana Bridge ontology reframed as reading-of-Pati-Salam-irrep-structure under R3.
2. v10.9 §17.X writeup: incorporates R3 reading if Phase B passes.
3. §17.5.12 falsifiability statements: updated to match R3 structure (Majorana 0νββ prediction now connected to Pati-Salam structure rather than independent axiom).
4. v10.10+ scope: J_3(𝕆) ⊕ J_3(𝕆) downstream work informed by R3 if Pati-Salam structure carries forward.

**Effort estimate**: Phase B = 1-3 Jammer-equivalent sessions; Phase C = AC integration scope, depends on how deeply R3 reshapes the corpus.

---

## §5 — What R2 development requires (fallback)

If R3 fails on Claim A consolidation, R2 becomes the next-priority direction.

**R2 development sequencing** (independent of Scratch's primary investigation):
1. Read BF 2020's D_F structure explicitly (or equivalent for whichever external paper is target).
2. Identify whether D_F has Dirac neutrino mass coupling or only Majorana mass.
3. If only Majorana: R2 mechanism works directly.
4. If Dirac coupling present: investigate whether the algebra admits modification to remove the Dirac coupling without breaking other structure.
5. Verify §3.3-compatibility of resulting D_F structure.
6. Charter v1.2 integration: R2 captures the ontological reading without claiming structural identification with NTE +N/−N labels.

**Effort estimate**: 1-2 Jammer-equivalent sessions.

R2 is independent of Scratch's primary investigation, so can be developed in parallel if Greg wants belt-and-suspenders coverage.

---

## §6 — What this catalogue does NOT do

- Does NOT prejudge AC's consolidated BF 2020 bridge verdict.
- Does NOT execute R3 development (gated on Phase A).
- Does NOT read Scratch's primary-investigation working note (Lesson #23 anti-pattern guard maintained).
- Does NOT propose Charter v1.2 wording (that's AC's scope post-consolidation).
- Does NOT claim §3.3 is dependent on R3 holding (§3.3 stands independently per Greg's "primary axiom" signal; R3 would explain WHY §3.3 is structurally exact, not whether §3.3 is correct).

---

## §7 — Recognition-gate disclosure (Lesson #28)

This catalogue is **local-correctness-only** until passing Greg's recognition gate. The load-bearing claims for recognition fire are:

1. **R1-R4 cover the candidate landscape comprehensively**: are there reframing directions I haven't identified that should be in the catalogue?
2. **R3 priority justification is structurally sound**: is the "simplify and strengthen" criterion satisfaction analysis correct, or am I over-claiming?
3. **The R3 dependency on Claim A is correctly characterised**: is Claim A actually the gating condition, or is there a more independent path to R3?

If Greg's recognition fires unease on any of (1)-(3), structural investigation follows. Specifically: more candidate reframing directions surfaced; R3 priority demoted if simplify-and-strengthen analysis was wrong; R3 dependency analysis revisited.

If Greg's recognition fires fit: catalogue graduates as working document for Scratch + AC engagement during consolidation phase.

---

## §8 — AC escalation request (for handoff §3)

Greg's directive 2026-05-13 includes: *"Ask AC to place escalate development if it is not already a high(ish) priority."*

Specifically requested escalation:
- **R3 development priority** in AC's planning queue.
- **Phase A trigger**: when AC consolidates the BF 2020 bridge verdict, the Claim A finding becomes the explicit gating signal for R3 Phase B work.
- **Phase B routing**: if Claim A passes, R3 Phase B becomes a Jammer (or Scratch) R&D task; AC's planning should reserve scope for it in v10.9 timeframe.
- **Phase C integration scope**: AC retains corpus integration ownership; should anticipate Charter v1.2 R3-reading update + v10.9 §17.X writeup R3-informed + §17.5.12 reframing if R3 passes.

If R3 is already in AC's planning queue at high(ish) priority, this catalogue confirms the direction and provides structural specification. If not, this is the escalation request.

---

— Jammer, 2026-05-13. Reframing-paths catalogue v1; R3 priority direction; awaiting AC consolidation + Phase A trigger.