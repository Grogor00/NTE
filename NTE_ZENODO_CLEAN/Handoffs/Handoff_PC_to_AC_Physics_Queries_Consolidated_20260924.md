# Handoff — PC → AC: consolidated physics queries from the Book campaign

**From:** PC
**To:** AC (corpus custodian), for verification against primary sources
**Date:** 2026-09-24
**Occasion:** Cursor is unavailable until Greg reaches his laptop. Greg has directed that every physics question, tension and flag raised during today's Book campaign be routed to AC and examined before the campaign continues.
**Status:** Routing document. No corpus change proposed. Nothing here is PC's to rule on.

---

## 0. Read this first: the pattern

Eight chapters and two ledger documents were read against `NTE_Workflow_Manifest_v10_18.md` §3 today. The register work was the expected output. The unexpected output is this:

**Writing the pedagogy has functioned as an audit of the §3 snapshot, and it has found three places where the snapshot is ambiguous, self-contradictory, or possibly wrong.**

That is not a complaint about §3 — it is what §3 is for, and a compressed snapshot earns its keep by being compressible. But the pattern is worth naming, because it means the Book campaign is doing corpus work as a side effect, and the items below should be read as audit findings rather than as a pedagogy stream asking for permission.

The three: **T_GB's tier** (§1), **Ω_k against genuine closure** (§2), and **R_H's definition** (§3) — the last of which may reach into a numerically load-bearing corpus relation and is therefore first in priority despite being third in the list.

Everything is graded below by what it would cost if left alone.

---

## 1. PRIORITY — R_H: Hubble radius or event horizon? (Ch 3, flag N2)

**The Book-side finding, already patched.** `Chapter_03_A_Closed_Universe_v6_1.md` states:

> *"our access to the universe is bounded by the **Hubble horizon** — the proper distance beyond which space is expanding faster than light can carry information back… Whatever lies past the Hubble horizon is gone from our causal future. We cannot see it, signal it, or be influenced by it."*

This conflates two distinct surfaces. The Hubble radius is where recession velocity equals *c*. It is not a causal boundary: light emitted beyond it can still reach us, handed inward from one stretch of space to the next until it reaches a region receding more slowly than it travels, and we routinely observe galaxies whose recession velocity exceeded *c* at emission. The surface that bounds our causal future is the **cosmological event horizon**, which lies further out. Patch M6 corrects the Book and rebuilds the flatness anchor on the bounded observable patch, which survives the correction intact.

**Why this is AC's problem and not just PC's.** R_H does load-bearing *numerical* work in **Part 1 §V**, in the conformal-reset trigger condition — the same relation whose volume convention was ratified yesterday as **V_H ≡ R_H³** (and not (4π/3)R_H³), with T_reset and N_total depending on the choice. The question for AC:

> **Which surface is R_H in Part 1 §V — the Hubble radius, or the cosmological event horizon? And is the corpus's use of it consistent with whichever one the derivation needs?**

If Part 1 has inherited the same conflation the Book had, this is not a prose defect there. The two radii differ by an O(1) factor that is not 1, and the trigger condition n_γ·V_H = 1 goes as the cube of it. Yesterday's V_H convention fix moved T_reset by a factor of 1.612 in the volume; a radius misidentification would move it again, and in a way the earlier fix would not have caught, because the earlier audit was about the geometric prefactor and not about which radius the symbol names.

PC's position: this is probably fine — the corpus's Hubble-radius usage elsewhere reads correctly, and the λ ∼ R_H discussion closed cleanly on 2026-09-23. But "probably fine" is not the standard for a symbol inside a trigger condition, and PC has not read Part 1 this session and will not assert either way.

**Recommended:** AC reads Part 1 §V and Companion 21's §5 against M6. If the usage is correct, close N2 with a one-line note. If it is not, this is a corpus patch, and C21 §5 inherits it.

---

## 2. §3's T_GB entry contradicts itself (Ch 15, flag F5)

The snapshot grades T_GB three times, and not consistently:

| Location in §3 | Grade |
|---|---|
| *Derived / structural* | **"T_GB = M_Pl/√(2π) — closed at the Hartle–Hawking Gaussian saddle-width (Companion 9), fibre-modulus identification β_GB·M_Pl = √(2π) from the spectral side (Companion 12)"** |
| *Conditional — NOT fixed zero-parameter predictions* | **"T_GB = M_Pl/√(2π) conditional pending Companion 12 fibre-modulus grounding (raw-trace saddle ruled out)"** |
| *The chord (Companion 12)* | **"T_GB demoted to conditional pending fibre-modulus close"** |

One entry says Companion 12 closed it; two say Companion 12 has not. The Derived/structural line and the Conditional line cite the *same companion paper* for opposite conclusions.

PC wrote **conditional** into Chapter 15 v4 (patch B1) on the two-of-three reading, reinforced by Greg's 2026-09-18 ratification of Ch 12 v4.1, which explicitly authorised the v4.2 revision to carry "T_GB → conditional". Appendix C v1.3 independently agrees, carrying the promotion-then-demotion narrative in C.2 and C.3.

**Recommended:** AC reconciles §3 against Part 3, which wins. If Part 3 grades T_GB derived, patch B1 and the T_GB clause in B10 come back out of Chapter 15 and Appendix C's C.2 needs revisiting. If Part 3 grades it conditional, the *Derived / structural* line in §3 should lose the T_GB clause, since it currently reads as a closure claim the rest of the snapshot denies.

---

## 3. Ω_k = 0 against genuine closure (Ch 3, flag N1)

§3 lists **Ω_k = 0** under *Derived / structural*, alongside δ_J = π/2 and w = −1.

Chapter 3's position is that the universe is a closed S³ whose radius has grown so vast through the e-fold history that curvature is undetectable at every scale we can probe — *observed* flatness as a prediction of the structure rather than a coincidence it must survive. That is Ω_k ≈ 0, arbitrarily close but not equal.

Strictly, exact flatness and genuine closure are different geometries. A closed S³ of finite radius has Ω_k < 0 by definition in the density convention; Ω_k = 0 *is* the flat case. As written, §3's entry reads as a derived claim of exact flatness, which would contradict the closure the whole framework rests on — including the entire surface ontology, the bilateral structure, and the Hopf apparatus.

PC has not patched Chapter 3 on this point, because the chapter's own treatment is the sensible one and the defect, if there is one, is in the compression rather than the chapter.

**The question for AC:** does Part 3 claim Ω_k = 0 exactly, Ω_k → 0 as a consequence of the e-fold run, or Ω_k observationally indistinguishable from zero? These are three different claims at three different registers, and §3 currently carries the strongest of the three in the strictest tier. PC's expectation is that Part 3 says something more careful and §3 has compressed it past the point of accuracy — but that is an expectation, not a reading.

**Recommended:** if it is the compression, §3's entry becomes **"Ω_k → 0 (closed; radius vast after the e-fold run — observed flatness predicted, not assumed)"**. Chapter 3 then needs no change and this closes.

---

## 4. Claims the Book makes that PC could not verify against the corpus

Three, all of them places where a chapter asserts something the Manifest snapshot does not carry. None is patched; all are stated in the Book at a register the corpus may not support.

### 4.1 V_NTE — the boundary expansion field's potential (Ch 5, flag H1)

`Chapter_05_The_Eighth_Colour_v7.md` attributes to |Φ_NTE| a potential **V_NTE** with *"a different shape — one that the technical corpus develops in detail in the post-locking regime"*, and the chapter's **forced-addition argument depends on it**: the reason the SM Higgs cannot be |Φ_NTE| is given as V_SM locking its field while V_NTE does not lock its own.

PC found no V_NTE in §3 and has not read Parts 1–2. If the corpus does not carry a named potential with a developed shape, Ch 5's sharpest argument is resting on furniture that may not exist, and the sentence needs softening to "dynamics the corpus develops" without naming a potential — which weakens the argument but keeps it honest.

**Question:** does the corpus carry V_NTE, and at what register — named potential with a derived form, named potential with an assumed form, or informal shorthand for the field's post-locking dynamics?

### 4.2 The BBN field ratio (Ch 5, flag H2)

Ch 5 gives the boundary expansion field's strength at primordial nucleosynthesis two ways in two sections: **"roughly *three hundred million times* its present value"** and **"roughly 10^8.5 times its present strength"**, the latter glossed as *"a descent through eight and a half orders of magnitude"*.

3 × 10⁸ and 10^8.5 ≈ 3.2 × 10⁸ agree, so the two phrasings are consistent with each other. What PC cannot confirm is whether either matches the corpus. On H ∝ |Φ|², the field ratio is the square root of the Hubble-rate ratio between the two epochs, and PC's own back-of-envelope on that puts it nearer **10^8.8** — compatible with "roughly", but sitting at the top edge of it rather than in the middle.

PC will not move a corpus number on an envelope. **Question:** what does the corpus give for |Φ_NTE|(BBN)/|Φ_NTE|(today), and is 10^8.5 the corpus figure or a Book approximation that has drifted?

### 4.3 N_lock ≈ 0.1 (Ch 4, flag G5)

`Chapter_04_Time_as_Expansion_v8.md` places the gauge birth at *"N less than a value the framework calls N_lock, around 0.1"*. §3 carries no N_lock. Ch 4 v9 does not touch the figure.

**Question:** does Part 1 carry N_lock, and is 0.1 current?

---

## 5. Currency items — measurement-side, not corpus-side

These are places where the Book quotes the experimental landscape and PC has not verified against primary sources this session. Recommend routing as one literature-currency check, which is Scratch's lane rather than AC's, but AC should scope it.

**5.1 JUNO and the mass ordering (flag F4).** Chapter 15 says the ordering verdict is *"imminent"*, that *"present data lean normal at modest significance"*, and that *"JUNO rules on the mass ordering the framework requires"*. JUNO is now publishing oscillation results — the θ₁₂ withdrawal cites arXiv:2511.14593 — and PC does not know what its current data say about ordering, or whether "imminent" is still the right word. **This is the framework's sharpest near-term falsifier, so the Book should not be vague about its timeline.**

**5.2 The P-ACT-LB anchor (flag F6).** §3 says the (n_s, r) comparison shows *"Planck 2018 and P-ACT-LB shown side by side"*. Chapter 15 v4 patch B3 states that the corpus shows both but **quotes no P-ACT-LB value**, because PC has not verified one and declined to invent it. If the chapter is to print both anchors numerically, AC supplies the figure from Companion 17.

**5.3 DESI (flag F4).** Chapter 15 v4 and Appendix C both carry DESI DR2 at ~3.1σ, SN-independent, and Appendix C additionally records the 2026 DES recalibration moving the SN-based figure from ~4.2σ to ~3.2σ. Both are corpus-sourced and PC has not re-verified either. Worth including in the same check, since the verdict window is stated as 2027–2029.

**5.4 The CMB-S4 / LiteBIRD timeline.** Both documents put sensitivity near r ≈ 10⁻³ in the early 2030s, and Ch 15 v4's patch B5 now leans on r = 0.0053 sitting *inside* that window rather than below it — which upgrades it to "the nearest hard date the framework has". That claim is only as good as the timeline.

**5.5 Photon entanglement at range (flag J2).** Chapter 2 v7 claimed photons stay entangled *"across satellite links and decades-long delays"*. PC found no basis for the decades claim and patch E3 replaces it with "satellite links spanning more than a thousand kilometres", which PC has stated at a register not dependent on the exact figure. If the Book quotes a precise range anywhere, it belongs in this check.

---

## 6. Closed today — recorded so they are not re-raised

- **F1 (Appendix C (n_s, r) hold).** Retired as **raised in error**. Appendix C v1.3 already carried 0.9692 and 0.0053 and already framed the open item correctly. PC's caution, not a defect. The originally proposed A5 was withdrawn as redundant.
- **F2 (CLFV ratio).** Closed. tan²θ₂₃ is exactly 1 at θ₂₃ = π/4; replacement patch A5 states it plainly.
- **G6 / H3 (confinement and embedding depth).** Closed **without AC arbitration**. `Chapter_01_The_Photons_Journey_v10.md`, Greg-ratified 2026-09-21, already carries the rest-energy reading in full — *"Rest energy is what embeds a thing in the expansion, wherever the rest energy came from"* — and explicitly *"from the Higgs coupling for fundamental particles and from confinement for composite ones"*. The reading is ratified Book prose, not PC inference.
- **G3 (rest-energy propagation).** Closed by the same finding. Chapters 4 and 5 were **contradicting Chapter 1**, not lagging a new campaign.

---

## 7. The apply queue, since Cursor is down

Nothing here is lost, but it should be visible in one place. Ratified and awaiting Cursor:

| Target | Patches | Ratified |
|---|---|---|
| `Book\Appendix_C_The_Open_Ledger_v1_4_…` | A1–A4, A5 (CLFV) | 2026-09-24 |
| `Book\Chapter_15_The_Score_v4.md` | B1–B11 | 2026-09-24 |
| `Book\Chapter_04_Time_and_Expansion_v9.md` (+ rename) | C1–C15 | 2026-09-24 |

Proposed, awaiting Greg: Ch 5 (D1–D9), Ch 2 (E1–E6), Ch 1 v11 + Prelude v8 (F1–F9, P1–P2), Ch 3 (M1–M9).

**Two items in the queue depend on how AC rules above.** If Part 3 grades T_GB *derived*, Chapter 15's B1 and part of B10 must be pulled before Cursor applies them. If Part 1 §V's R_H is the wrong surface, Chapter 3's M6 is still correct but C21 §5 acquires a defect. **Recommend Chapter 15's apply be held until §2 of this document is closed**; the others are independent.

Also outstanding and not PC's: Part 1 §V vector reading; Companion 17's N_e; the two P4 definitional rulings; C21's Hawking-point literature currency and its `Core_Papers\` placement and title block; and the Scratch/Jammer adversarial programme, whose Cursor leg has never filed.

---

## 8. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **PC → AC consolidated physics queries** (`Handoff_PC_to_AC_Physics_Queries_Consolidated_20260924.md`, PC, 2026-09-24) — every physics flag from the 2026-09-24 Book campaign, routed at Greg's direction while Cursor is unavailable. Priority: **N2 — is R_H in Part 1 §V the Hubble radius or the cosmological event horizon? The Book conflated them; if the corpus did too, the conformal-reset trigger condition is affected numerically.** Then **F5** (§3 grades T_GB derived and conditional simultaneously, citing Companion 12 both ways) and **N1** (§3's Ω_k = 0 reads as exact flatness, which contradicts genuine S³ closure). Unverified Book claims: V_NTE (H1), the 10^8.5 BBN field ratio (H2), N_lock ≈ 0.1 (G5). Currency check for Scratch: JUNO ordering, P-ACT-LB value, DESI DR2/DES recalibration, CMB-S4/LiteBIRD timeline, photon-entanglement range. Closed today: F1 (raised in error), F2, G3, G6, H3. **Chapter 15's apply should be held until F5 closes.**
```

---

## 9. PC's own position, stated for the record

PC raised one flag in error today (F1) and framed a second correction on a weaker basis than the evidence supported (the Ch 4 rest-energy patch, which was contradicting ratified Chapter 1 prose rather than applying a new campaign rule). Both are recorded above. Neither changed a patch, but both cost Greg a ratification made on an incomplete account, and the pattern in both cases was the same: **asserting a corpus state from context rather than from the file.** Discipline 1 exists for precisely this, and PC re-read Appendix C and Chapter 1 in full only after having already characterised them.

The items in §1 through §4 are stated as questions rather than findings for the same reason. PC has not read Parts 1–3 this session. Where this document says the corpus may be wrong, it means PC cannot tell from §3 alone — not that PC has checked and found a defect.
