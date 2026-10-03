# Patch instruction — cite Boyle–Finn–Turok in Part 2 §IX (v10.18.0)

**Author:** AC · **Date:** 2026-07-05 · **For:** Cursor local render lane → Greg ratification
**Origin:** Scratch handoff (2026-07-05, HIGH-PRIORITY / pre-deposit). **AC-revised to a single edit** on Greg's direction.
**Status:** ready for Cursor once Greg approves the wording. Single target, single OLD/NEW block.

**What changed from Scratch's handoff, and why.** Scratch proposed three edits (§IX credit, §8.4 append, Part 1 positioning) plus a §XVI disambiguation of the phrase "occupy the same N-range from opposite directions." **The §8.4 append and the §XVI disambiguation are dropped.** They rested on a concern that "opposite directions" could be read as opposite proper-time arrows and blur C5. It can't: §XVI already says the radial axis *"is the e-fold accumulation N,"* and Part 1 §2.1.2 fixes t = i·ΔN as **orthogonal** to N — so the CPN N-flip leaves the proper-time arrow untouched (common arrow). Opposite-N ≠ opposite-t is settled framework physics; no disambiguating edit is warranted. What remains is the citation itself, in §IX, which stands on priority grounds alone.

**Verification done by AC:** both sources confirmed in `References/` (PRL 121, 251301 via the 2026-07-05 triage; companion arXiv:1803.08930 sourced by Greg). Current §IX text read from the canonical Core_Papers source. No tier changes — the distinctions are already true in the corpus; this states them.

**Application rule:** match on the distinctive prose, not exact whitespace. The target is the italicised "Relationship to prior work" paragraph that opens §IX (the whole paragraph is wrapped in single `*` for italics — preserve that). After the edit, re-read and confirm the NEW text is present and the OLD text is gone. If the OLD block does not match cleanly, **stop and report — do not force.** Apply to the canonical source the render reads; keep the Core_Papers and scratch-src copies in sync; re-render Part 2; confirm the set holds at 29/29.

---

## TARGET — `NTE_v10_18_0_Part2_Structure.md`, §IX opening "Relationship to prior work" paragraph

**OLD:**
```
*Relationship to prior work: mirror-matter dark matter has an extensive literature (Foot; Berezhiani); the bimetric structure connects to ghost-free bimetric gravity (Hassan–Rosen). NTE differs in that the "mirror" is the CPN-conjugate orientation of one manifold's N-thickness, the coupling is purely gravitational/geometric (no kinetic mixing), and the DM:baryon ratio is fixed by the Hopf-projection geometry.*
```
**NEW:**
```
*Relationship to prior work: the closest published predecessor is the CPT-symmetric universe of Boyle, Finn & Turok (2018; dark-matter companion arXiv:1803.08930), which shares the core architecture — a universe–antiuniverse pair from the bang, the matter–antimatter asymmetry sorted to opposite sides rather than annihilated, a CPT-selected preferred vacuum, and a Z₂ symmetry on the neutrino sector stabilising dark matter. NTE is distinct on four axes. (i) Pairing symmetry: Boyle–Finn–Turok relate the two halves by a genuine time reversal (τ→−τ across the bang, the antiuniverse being the CPT/Stueckelberg image), whereas NTE's mirror is the CPN-conjugate orientation and the emergent proper time is held orthogonal to the N-direction that CPN flips (t = i·ΔN, Part 1 §2.1.2) — so the proper-time arrow is common to both halves and there is no time-reversed antiuniverse. (ii) Dark matter: here it is the gravitational footprint of mirror-orientation matter through the Z₂-even neutrino, fixing the ratio κ by Hopf-projection geometry, not a sterile-neutrino particle of definite mass. (iii) Substrate: NTE's two observable universes are the boundary surfaces of a bubble formed in a pre-temporal Euclidean bulk — a surface-only ontology once time has emerged, the conjugate twin being the opposite surface with only residual pre-temporal bulk between them — parameterised by the count coordinate N with t = i·ΔN, not a 4-dimensional FRW cosmology continued through a Weyl-singular bang. (iv) NTE retains a Hartle–Hawking Euclidean sub-phase (its inflationary observables conditional, Part 3), whereas the Boyle–Finn–Turok scenario is inflation-free with r = 0. Mirror-matter dark matter more broadly has an extensive literature (Foot; Berezhiani), and the bimetric structure connects to ghost-free bimetric gravity (Hassan–Rosen); NTE differs from these in that the "mirror" is the CPN-conjugate orientation of one manifold's N-thickness, the coupling is purely gravitational/geometric (no kinetic mixing), and the DM:baryon ratio is fixed by the Hopf-projection geometry.*
```

---

## Notes for Greg (ratification points)

- **The arrow-of-time distinction (axis i) is stated your way** — CPN flips N, t is orthogonal (t = i·ΔN), common proper-time arrow, no τ-reversed antiuniverse. It points at the *existing* Part 1 §2.1.2 result rather than adding any new hedge, and it's the axis that most cleanly separates NTE from BFT (whose whole construction *is* the τ→−τ isometry).
- **Placement.** Kept entirely in §IX, where the universe–antiuniverse / Z₂-neutrino-DM architecture lives, and where the Foot/Berezhiani/Hassan–Rosen credits already sit. The original three sentences are preserved (moved to the end). §8.4, §X, §XVI untouched.
- **Citation style.** Name + year inline, matching house style (§IX's Foot/Berezhiani/Hassan–Rosen; §8.5's Günaydin–Gürsey etc.). Full refs for a bibliography: L. Boyle, K. Finn, N. Turok, *CPT-Symmetric Universe*, Phys. Rev. Lett. 121, 251301 (2018); companion *The Big Bang, CPT, and Neutrino Dark Matter*, arXiv:1803.08930.
- **Part 1 positioning.** Not included. BFT is a cosmology-architecture relative, not part of Part 1's emergent-time / division-algebra / NCG family, so §IX is the coherent home. If you want a one-line cosmology-relative nod in Part 1 too, say so and I'll add it — but it isn't needed to close the priority gap.
