# Handoff — PC → Greg (ratify) → Cursor (apply): Ch 12 partial pass, M_c dependence round, mirror question answered

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply) · **Cc:** AC
**Date:** 2026-09-25
**Answers:** `Handoff_AC_to_PC_Corpus_State_For_Rewrite_20260925.md` §§1, 2, 3
**Status:** PROPOSED — not ratified

---

## 0. PC read-state ledger (discipline 11)

| Source | Read in full this session | Note |
|---|---|---|
| `Book\Chapter_12_The_Chord_v4_1.md` | **Yes** | First read ever by PC |
| `Book\Chapter_10_The_Silvered_Boundary_v8.md` | **Yes** | Post-apply state |
| `Book\Chapter_03_A_Closed_Universe_v7.md` | **NO** | Read at v6.1 on 2026-09-24. **AC named it as a likely site for §2. PC is not ruling on it — see AM3.** |
| `Handoff_AC_to_PC_Corpus_State_For_Rewrite_20260925.md` | **Yes** | |
| Part 2; Companions 5, 12, 18 | **NO — never read by PC** | Every corpus claim below is AC's or Cursor's, attributed |
| `NTE_Workflow_Manifest_v10_18.md` | **NO** — last read 2026-09-23 | Still stale by 6.7 kB. No claim below rests on it |

---

## 1. AC §2 — the mirror question, answered from source

AC asked whether any chapter describes the mirror as a bookkeeping device, a redundancy, or the same universe counted twice, and named Chapters 10 and 3 as the likely sites, having read neither at current version.

**Chapter 10 v8 passes, and it is not close.** Read in full this session; three places state the opposite explicitly:

- §1 — *"The other is real, with its own galaxies and stars and (possibly, in some loose sense) observers, all evolving under the same physics."*
- §4 — *"The other has its own matter — its own galaxies, its own large-scale structure — under the same physics, in the same forward direction of emergent time."*
- §8 — *"hosting its own galaxies and stars and structure… The mirror's other side is no closer than the fork's, and no less real."*

No occurrence of the redundancy reading anywhere in the chapter. Searched the full text for: `redundan`, `bookkeeping`, `counted twice`, `same universe`, `gauge choice`, `not real`. Zero hits on all six.

**One phrase is worth a sentence of insurance, now that the P4 ruling has raised the stakes.** §1 opens the mirror description with *"They are not two parallel realities, exactly"*. In context that is disclaiming the many-worlds branching-reader reading, and the next sentence says the other is real — but a careless reader can take "not two parallel realities" as "not really two", which is precisely the position Part 2 §IX now rules out. **AL1 below** closes that gap; it is optional and cheap.

**Chapter 3 is not answered.** PC read v6.1 yesterday, not v7 this session. The relevant section — *"What 'The Other Side' Means"* — was not touched by the M-series, so the text is almost certainly unchanged, but that is an inference and discipline 11 does not accept it. **PC will read Ch 3 v7 and report; see AM3.**

---

## 2. AC §3 — the M_c dependence: a third round on the same item, and my patches need it too

AC's new finding is that **both** figures are functions of m_ν, and live Part 2 §IX quotes M_c ~ 4 × 10¹⁴ M_☉ as though fixed. So swapping the length for the mass — which PC did across four files — fixed the wrong-quantity problem and left the false-determinacy problem exactly where it was.

Three places in Chapter 10 v8 print the mass as a fixed threshold, all of them text PC wrote:

| Locus | Text as applied |
|---|---|
| §5 opening (Z1) | *"above roughly 4 × 10¹⁴ solar masses"* |
| §5 figure (Z2) | *"Four hundred trillion solar masses is a rich galaxy cluster"* |
| §8 (Z3) | *"above the coherence mass, around 4 × 10¹⁴ solar masses"* |

Plus Chapter 15 v5's AA1 and the still-proposed Appendix C AF2. **Chapter 16's AD4 is already safe** — it names the coherence mass without a number.

This is the same defect migrating: a figure whose determinacy the Book asserts and the corpus does not. First as a length, now as a mass. **The patches below give the number once, with its dependence attached, and stop repeating it.**

---

## 3. Chapter 10 — AC4–AC6 (additional to the proposed AC1–AC3)

### AC4 — §5 opening, the threshold

**OLD**

```
The framework states that scale as a *coherence mass* rather than a length, because a mass is what the gravitational accounting of a system actually turns on: above roughly 4 × 10¹⁴ solar masses, a system is large enough to average over many independent patches of the coupling; below it, it is not.
```

**NEW**

```
The framework states that scale as a *coherence mass* rather than a length, because a mass is what the gravitational accounting of a system actually turns on: above it, a system is large enough to average over many independent patches of the coupling; below it, it is not. The mass itself is around four hundred trillion suns — but that figure is not a constant of the theory, and the next paragraph says why.
```

### AC5 — §5 figure and context

**OLD**

```
Four hundred trillion solar masses is a rich galaxy cluster. To put it in context: a typical dwarf galaxy holds perhaps a hundred million solar masses in total; our own Milky Way, a trillion or so; a large galaxy cluster, a few hundred trillion. The coherence mass therefore sits at the boundary between the cluster scale and the scale of the cosmic web's filaments and voids — which is the boundary the next section's prediction turns on.

One caveat travels with this, and the framework states it rather than leaving it implicit: the free-streaming scale is standard neutrino physics, not an NTE derivation. What is the framework's own is the *combination* — this scaling law, around this particular mean of 5.50, with the transition at this scale. And the *size* of the scatter within a single coherence patch is not predicted at all; the corpus carries that amplitude as open. The framework predicts that the scatter is there and how it falls away with mass, not how large it is at the bottom.
```

**NEW**

```
Four hundred trillion solar masses is a rich galaxy cluster. To put it in context: a typical dwarf galaxy holds perhaps a hundred million solar masses in total; our own Milky Way, a trillion or so; a large galaxy cluster, a few hundred trillion. The coherence mass therefore sits at the boundary between the cluster scale and the scale of the cosmic web's filaments and voids — which is the boundary the next section's prediction turns on.

Three caveats travel with that figure, and the framework states them rather than leaving them implicit. The free-streaming scale is standard neutrino physics, not an NTE derivation; what is the framework's own is the *combination* — this scaling law, around this particular mean of 5.50, with the transition at this scale. The *size* of the scatter within a single coherence patch is not predicted at all, and the corpus carries that amplitude as open: the framework predicts that the scatter is there and how it falls away with mass, not how large it is at the bottom. And the threshold is not a fixed number. Free-streaming scales inversely with the neutrino's mass, so the coherence mass moves as the neutrino mass moves, and the neutrino mass is not something the framework has pinned. Four hundred trillion suns is the value at a standard reference mass, not a constant the geometry hands down. A reader should hold it as an order of magnitude with a dial attached, and the surveys that test the transition will have to be read against whatever the neutrino mass turns out to be.
```

### AC6 — §8

**OLD**

```
with the scatter falling as σ(M) ∝ M^(−1/2) above the coherence mass, around 4 × 10¹⁴ solar masses.
```

**NEW**

```
with the scatter falling as σ(M) ∝ M^(−1/2) above the coherence mass — cluster-scale, and moving with the neutrino mass as §5 described.
```

---

## 4. Chapter 15 — AK1 (v5 → v6)

**OLD**

```
Chapter 10's companion claim: the transition to tight convergence above a coherence mass of around 4 × 10¹⁴ solar masses, the neutrino free-streaming scale — which the framework adopts rather than derives, its own contribution being the combination of that scale with the scaling law and the mean.
```

**NEW**

```
Chapter 10's companion claim: the transition to tight convergence above the neutrino free-streaming coherence mass, which is cluster-scale — of order 10¹⁴ solar masses — and which the framework adopts rather than derives. It is also not a fixed threshold: free-streaming scales inversely with the neutrino mass, so the transition moves with a quantity the framework has not pinned. What the framework claims is the combination of that scale with the scaling law and the mean, not the scale itself.
```

---

## 5. Appendix C — AF2′ supersedes AF2

**Apply AF2′, not AF2.** Same OLD block.

**OLD**

```
**Rubin Observatory and Euclid** — the coherence-length transition near ~40 Mpc, the dark-matter-fraction scatter pattern across hundreds of millions of systems, and the void anatomy of the Hubble tension (framework: directional scatter of 2–4 km/s/Mpc correlated with line-of-sight density).
```

**NEW**

```
**Rubin Observatory and Euclid** — the transition in the dark-matter-fraction scatter at the neutrino free-streaming coherence mass, mapped across hundreds of millions of systems; and the void anatomy of the Hubble tension (framework: directional scatter of 2–4 km/s/Mpc correlated with line-of-sight density). Two honest qualifications on the transition. The free-streaming scale is standard neutrino physics rather than an NTE derivation — what the framework claims is its combination with the M^(−1/2) scaling and the mean of 5.50, and the scatter's amplitude within a single coherence patch is carried as open. And the threshold is not fixed: free-streaming scales inversely with the neutrino mass, so the transition sits at a cluster-scale mass of order 10¹⁴ suns for a standard reference neutrino mass and moves as that mass moves. A survey result on the transition has to be read against whichever neutrino mass turns out to be right.
```

---

## 6. Chapter 12 — AJ series, partial pass (v4.1 → v4.2a)

**This is deliberately a partial pass.** Chapter 12's section *The Note Taken Off the Chord* carries n_s = 0.9685, N_e ≈ 63.4, a σ figure and the retired K(Φ) framing — all of it inside the authorised v4.2 revision's scope and all of it behind the item (a) hold. **PC is not touching that section.** Half-patching a section that is about to be rewritten wholesale creates two edits where one will do. The four patches below are the T_GB register items, which are independent of item (a) and are wrong in the live text today.

Suggested target name `Chapter_12_The_Chord_v4_2a.md` to mark it as the partial; Greg may prefer a different convention.

**First, a positive, because AC flagged a risk that does not bite.** AC warned that a chapter leaning on a count of clean-spine results would be damaged by the spine thinning from three to two. **Chapter 12 does not count.** Its second paragraph states the opposite as the chapter's thesis — *"the chord is not a fixed list… the count of notes named at any moment reflects where the mathematical work has reached, not a structural promise… the coherence, not the tally."* The chapter survives the thinning intact, and its closing section says so again. Nothing to repair there.

### AJ1 — the register paragraph, which is now backwards

**OLD**

```
A word on the register, because the book grades every note. The bare coupling sits in the framework's derived tier, and so — as of the corpus's current accounting — does the gauge-birth temperature: its derivation closed through the width of the saddle at which the Lorentzian universe is born, work carried in the framework's technical companions. For a period of the framework's development this note was held one grade lower, as a candidate identification awaiting closure, and it earned its promotion the only way the framework permits — by the derivation being finished, not by the claim being repeated. The first and second notes now match at register as well as in method.
```

**NEW**

```
A word on the register, because the book grades every note — and this note's grade has moved twice, which makes it the chapter's best worked example of grading. The bare coupling sits in the framework's derived tier. The gauge-birth temperature does not. For a period of the framework's development it did: its derivation was taken to have closed through the width of the saddle at which the Lorentzian universe is born, and it was promoted. Then the argument underneath was examined directly and the saddle it assumed turned out not to be there — an artefact of where the expansion had been cut off — and the note was demoted again, to a cross-check held at conditional register. A candidate route to grounding it independently remains open, through a modulus of the framework's fibre geometry, and until that closes the temperature is conditional.

So the first and second notes do not match at register, and the chapter should not pretend otherwise. Of the results the chord sounds cleanly, two stand at the derived tier: the bare coupling and the volume signature a later section develops. That is a thinner spine than the framework carried a year ago, and the thinning was the framework's own doing.
```

### AJ2 — the fibre-modulus claim states as settled what the corpus calls open

**OLD**

```
In the framework's committed geometry, the relation is even tighter than an analogy: the size of the temporal circle itself is fixed by this single √(2π) relation, so the statement "the fibre has this modulus" and the statement "gauge birth happened at this temperature" are one statement, not two.
```

**NEW**

```
In the framework's committed geometry the relation is meant to be tighter than an analogy: the size of the temporal circle and the temperature of the gauge birth would be one statement rather than two, joined by this single √(2π) relation. That identification is the framework's proposal and it is not yet established — it is the candidate grounding named above, and it is the open item on which the note's register turns. If it closes, the two statements become one and the note is derived. Until then the chapter states it as what it is: an identification the framework has made and not yet earned.
```

### AJ3 — the falsification clause describes as hypothetical something that has partly happened

**OLD**

```
If the saddle-width derivation behind the gauge-birth temperature fails under independent audit — if the closure delivers something other than the Planck mass over the square root of 2π — the second note is wrong, and the single relation that fixes the temporal circle goes with it, taking the volume audit along.
```

**NEW**

```
The gauge-birth temperature has already had one audit go against it — the saddle the width argument assumed was found not to exist, which is why the note sits at conditional rather than derived. What remains at risk is the surviving route: if the fibre-modulus identification fails to close, or closes on something other than the Planck mass over the square root of 2π, the second note does not recover, and the single relation that would have fixed the temporal circle goes with it.
```

### AJ4 — "Where This Leaves Us", the grading sentence

**OLD**

```
And the count was never the point. The framework commits to the chord — the joint sound the instrument makes — not to a tally of notes, and the tally has changed as the mathematics matured: one note removed by the framework's own accounting, another promoted to the derived tier when its closure was finished, perhaps others still to be identified as the work continues.
```

**NEW**

```
And the count was never the point. The framework commits to the chord — the joint sound the instrument makes — not to a tally of notes, and the tally has changed as the mathematics matured: one note removed by the framework's own accounting, another promoted to the derived tier and then demoted again when the argument under it was found to rest on a truncation artefact, perhaps others still to be identified as the work continues. A tally that only ever grows is a sales figure.
```

---

## 7. Flags

**AM1 — Chapter 12's held section, stated precisely so nothing is lost.** *The Note Taken Off the Chord* requires, when item (a) lands: n_s from 0.9685 to whatever the band settles on or no value at all; N_e from 63.4; the 0.85σ figure removed per AC §7; and the open input re-pointed from K(Φ) to the spectral origin of ξ. Its N_lock-versus-N_e disambiguation paragraph is good writing and should survive — though note that per AC's item (a) analysis it guards the conflation the corpus already guards, and not the one that actually went wrong.

**AM2 — Ch 12's "three, because that is the dimension of the relevant rotational structure".** The lay-register version of the count Ch 9's T4 now grounds in Companion 12 §3. Ch 12 does not name SU(2) and does not need the Killing-spinor negative at this register. **No patch; recorded so it is not raised again.**

**AM3 — Chapter 3 v7 is the one open site from AC §2, and PC has not read it this session.** Next action. PC's expectation from the v6.1 read is that it passes — the two-ants-on-paper analogy treats the other side's mass as real and gravitating — but expectation is not a read, and AC asked a direct question about a chapter neither of us has verified at current version.

**AM4 — the M_c item has now cost three rounds, and the pattern is worth naming.** Round one: the Book said 40 Mpc, the corpus said a mass. Round two: the Book said a mass, the corpus said the mass is derived from a length. Round three: both figures float with m_ν and neither document said so. Each round was a true correction that did not go deep enough, and each time the residual was found by someone reading further down than PC had. **The generalisable lesson: when a figure turns out to be the wrong quantity, check whether the right quantity is itself determinate before substituting it.** PC substituted twice without asking that question.

**AM5 — AC's §3 says the corpus item is AC's.** Live Part 2 §IX quoting M_c as fixed is a corpus-side defect and AC has taken it. The Book patches above do not wait on it: they are honest under either resolution, because they say the threshold moves rather than naming what it moves to.

---

## 8. Registration (discipline 10)

```
- **Book/ Ch 12 partial + M_c dependence round + mirror verification** (`Handoff_PC_to_Greg_Cursor_Ch12_Partial_Mc_Dependence_Mirror_Verified_20260925.md`, PC, 2026-09-25). **AC §2 answered from source: Chapter 10 v8 read in full, passes — three explicit statements that the mirror sector is real, zero hits on six redundancy-reading search terms; AL1 offered as optional insurance on one phrase. Chapter 3 v7 NOT read this session, not ruled on (AM3).** **AC4–AC6** on Ch 10 v8 and **AK1** on Ch 15 v5 and **AF2′ superseding AF2** on Appendix C: all three files printed M_c as a fixed threshold, which is PC's own text in every case — AC's finding is that M_c floats with m_ν and live Part 2 §IX hides the dependence. Ch 16's AD4 already safe. **AJ1–AJ4** on `Chapter_12_The_Chord_v4_1.md` → v4.2a, deliberately partial: the T_GB register items only, which are independent of item (a); *The Note Taken Off the Chord* is left whole for the authorised v4.2 rather than half-edited. Ch 12's live text grades T_GB derived and says it "earned its promotion" — backwards since August and now formally so after Greg's ratification today. **Positive: Ch 12 does not count its clean-spine results — its stated thesis is coherence-not-tally — so the spine thinning from three to two damages nothing, contrary to AC's flagged risk.** Flags AM1 (held section's exact debt), AM4 (**the M_c item took three rounds; when a figure is the wrong quantity, check the right quantity is determinate before substituting**), AM5. **Status: PROPOSED, awaiting Greg.**
```

---

## 9. Optional — AL1, Chapter 10 §1

Offered separately because it is insurance rather than a defect.

**OLD**

```
They are not two parallel realities, exactly — no alternate version of the reader who took a different career lives in the other orientation as a separate fiction.
```

**NEW**

```
They are not two parallel realities in the science-fiction sense — no alternate version of the reader who took a different career lives in the other orientation. But they are two, and both are real: the framework's own structure requires it, because a mirror that were merely our own sector counted twice would supply no extra matter for the dark-matter ratio to measure.
```

---

## 10. On ratification

Cursor applies AC1–AC6 → `Chapter_10_The_Silvered_Boundary_v9.md` (AC1–AC3 from the earlier handoff, AC4–AC6 here, plus AL1 if Greg takes it); AK1 → `Chapter_15_The_Score_v6.md`; **AF2′ in place of AF2** in the Appendix C v1.5 set; AJ1–AJ4 → `Chapter_12_The_Chord_v4_2a.md`.

PC reads **Chapter 3 v7** next to close AM3, then Chapters 6, 7, 8, 11 and 14 — the five that have never had a pass and that the mechanical sweep, still unreturned, would not cover anyway.
