# Handoff — PC → Greg (ratify) → Cursor (apply): review response — Ch 4 v10, Ch 5 v9, Ch 10 (Z supersedes U2), Ch 15 v5

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-25
**Arising from:** the comparative review canvas (B+ → A−, 2026-09-25) and `Handoffs\Handoff_Cursor_to_AC_G6_G7_G8_Reports_20260925.md`
**Status:** PROPOSED — not ratified

Four target files, one handoff, because they arise from one input and Cursor wants one apply manifest. Series by target: **X** → Ch 4, **Y** → Ch 5, **Z** → Ch 10, **AA** → Ch 15.

---

## 0. Two of the review's three soft leftovers are real, and both are mine

PC verified all three against the live applied files rather than taking the review's word for them. Results:

**Ch 4 "emergence lexicon leaks" — confirmed, and worse than one instance.** Five survivors of the C-series, in the chapter whose retitle was the point of the exercise. The flagship one is in *Where This Leaves the Photon (Again)*: *"Here, with the **time-emergence picture** in place"* — five paragraphs of the chapter's own opening are spent repudiating exactly that phrase. Four more in the pre-temporal and two-coordinates sections. **This is the same failure mode as the Chapter 1 v9 patch set earlier in the campaign: a sweep that caught the prominent instances and missed the quiet ones.** Reported as mine.

**Ch 5 "V_NTE name scraps" — confirmed.** D10 scrubbed the potential from *The Field's Variability*, which is where the forced-addition argument lives, and left two behind. The worse of the two is in *What Comes Next*: *"Why does its potential V_NTE have the form it has, with the specific dynamics the technical corpus develops?"* — which asserts precisely the thing flag H1 says is unverified, and which D10 existed to stop the Book depending on. D10 narrowed the exposure; it did not close it. Also mine.

**Prelude "experienced" — not a defect. PC declines to patch, and recommends Greg does too.** The review reads *"The photon experienced no time at all"* as an A9 slip. It is the deliberately retained seed: Manifest §10 records Prelude v7 as *"keeps seed 'experiences/experienced no time'"*, Greg-ratified 2026-09-21. And the guard is immediate — the next paragraph is *"Not very little time. Not so little that we have to round it down. Not even zero on a clock — because relativity gives the photon no clock, and no point of view from which to read one."* The line states the folk fact in the reader's own words and the framework corrects it in the following breath, which is the whole rhetorical move of the Prelude.

Worth one note, though: a careful reader has now independently scored it as a slip. That does not make it one, but it is evidence the seed is doing exactly the work it was kept for — landing hard enough to be noticed. **Greg's call. PC's recommendation is to keep it and to record the ratification against it so the next reviewer does not re-raise it.**

---

## 1. The ~40 Mpc coherence length is not in the corpus at all

Flag W4 asked whether the figure was derived or candidate. Cursor's G6 sweep of `Core_Papers\` answers something else: **it is neither, because the corpus does not deposit a length.**

What the corpus deposits, in `NTE_v10_19_0_Part2_Structure.md` §IX and echoed in Part 3, is a **coherence mass**:

> *"A mass-dependent DM:baryon variance σ(M) ∝ M^(−1/2) above the **neutrino free-streaming coherence mass** M_c ~ 4×10¹⁴ M_☉, with large scatter below it… The M^(−1/2) scaling is a generic CLT consequence; the **NTE-specific content is its combination with the mean κ ≈ 5.50 and the coherence scale M_c**. … (The amplitude within one coherence volume is open.)"*

Cursor found **no `40 Mpc`, no `forty megaparsec`, and no `coherence length` as a length** anywhere in `Core_Papers\`. Part 3's falsifier is on the **scaling above M_c**, not on a transition length.

Three consequences, all of which the Book currently gets wrong:

1. **The quantity is a mass, not a length.** Chapters 10 and 15 both carry a length the corpus does not deposit.
2. **The Book omits a stated caveat.** Part 2 says the amplitude within one coherence volume is open. Chapter 10 says the below-scale scatter is the framework's prediction and does not mention that its size is not predicted.
3. **PC cannot reproduce 40 Mpc as a conversion of M_c, either.** At mean cosmic density, 4×10¹⁴ M_☉ encloses a comoving radius near 13 Mpc — a diameter near 27 Mpc. Order-of-magnitude compatible, but not 40, and the convention is unstated. **That arithmetic is PC's envelope, not a corpus figure; flagged as AB1 rather than asserted.**

The Z and AA patches convert both chapters to the deposited quantity and add the open-amplitude caveat.

**Also from Cursor, and favourable:** G7 confirms the corpus *rejects* mediation for the dark-matter bridge — Part 1 §III says *"This bilateral support — **not a mediating role** — is the geometric structure on which the dark-matter cross-thickness coupling acts"*, and Companion 5's abstract says *"a geometric coupling, **not a particle mediator**"*. So Chapter 10's "mediated through" is Book-local, not inherited, and patches U1/U2 restore the corpus's own language. That closes the question PC routed in §2 of yesterday's AC document.

---

## 2. Chapter 4 — X-series (base `Chapter_04_Time_and_Expansion_v9.md` → v10)

### X1 — the flagship survivor

**OLD**

```
Both Chapter 1 and Chapter 3 returned to the photon at their close, because the photon is the framework's first and clearest test case. Here, with the time-emergence picture in place, we can give the cleanest version yet.
```

**NEW**

```
Both Chapter 1 and Chapter 3 returned to the photon at their close, because the photon is the framework's first and clearest test case. Here, with the binding of time to expansion in place, we can give the cleanest version yet.
```

### X2 — the post-temporal paragraph, two instances

**OLD**

```
The *post-temporal* regime is everything we usually mean when we talk about the universe. It's the era from very shortly after the Big Bang to the present. In this regime, *t* has emerged, the relationship dt/dN = 1/(β_NTE|Φ_NTE|²) is well-defined and stable, and ordinary time-based physics works. General relativity, quantum mechanics, thermodynamics, nuclear physics — all of them apply normally. Using *t* in this regime is correct, not an approximation. The deeper structure (*N*) is always there, but the emergent description (*t*) is complete and self-consistent within its domain of validity.
```

**NEW**

```
The *post-temporal* regime is everything we usually mean when we talk about the universe. It's the era from very shortly after the Big Bang to the present. In this regime *t* is well-defined, the relationship dt/dN = 1/(β_NTE|Φ_NTE|²) is stable, and ordinary time-based physics works. General relativity, quantum mechanics, thermodynamics, nuclear physics — all of them apply normally. Using *t* in this regime is correct, not an approximation. The deeper structure (*N*) is always there, but the derived description (*t*) is complete and self-consistent within its domain of validity.
```

### X3 — the pre-temporal definition

**OLD**

```
The *pre-temporal* regime is everything before time emerged. In the framework's picture, this is not "the early universe before the Big Bang" in any conventional sense.
```

**NEW**

```
The *pre-temporal* regime is everything below the range of *N* in which *t* is definable at all. In the framework's picture, this is not "the early universe before the Big Bang" in any conventional sense.
```

### X4 — the two-coordinates section

**OLD**

```
You can use it pre-temporally, when the framework explicitly says no temporal structure has yet emerged, and the equations still make sense.
```

**NEW**

```
You can use it pre-temporally, where the framework explicitly says no temporal structure is yet in place, and the equations still make sense.
```

### X5 — cosmic time, the epigraph section

**OLD**

```
For now, the picture to hold is this: the boundary expansion field does not just regulate the rate of proper time accumulation.
```

**NEW**

```
For now, the picture to hold is this: the boundary expansion field does not just regulate the rate at which cosmic time accumulates.
```

### X6 — cosmic time, What Comes Next

**OLD**

```
The framework's central scalar is |Φ_NTE|, the geometric scalar whose strength regulates the rate at which proper time accumulates per unit expansion.
```

**NEW**

```
The framework's central scalar is |Φ_NTE|, the geometric scalar whose strength regulates the rate at which cosmic time accumulates per unit expansion.
```

### X7 — the closing line of the rest-energy argument still says "coupling"

The chapter spends two pages establishing that rest energy, not coupling, is the dial — then closes the argument on the old word.

**OLD**

```
This is not a metaphor. It's the framework's specific claim. Time, for any physical system, is the integrated outcome of that system's embedding in the universe's expansion. A different coupling pattern would give a different time.
```

**NEW**

```
This is not a metaphor. It's the framework's specific claim. Time, for any physical system, is the integrated outcome of that system's embedding in the universe's expansion. A different distribution of rest energy would give a different time.
```

---

## 3. Chapter 5 — Y-series (base `Chapter_05_The_Eighth_Colour_v8.md` → v9)

### Y1

**OLD**

```
Before the gauge birth, in the pre-temporal regime, |Φ_NTE| existed as a geometric scalar without the dynamics that V_NTE imposes post-locking.
```

**NEW**

```
Before the gauge birth, in the pre-temporal regime, |Φ_NTE| existed as a geometric scalar without the post-locking dynamics it later acquires.
```

### Y2 — the one that matters

**OLD**

```
What it has not done is develop the geometric *origin* of |Φ_NTE|. Where does the field come from? Why does its potential V_NTE have the form it has, with the specific dynamics the technical corpus develops? What is the relationship between |Φ_NTE|'s pre-temporal identity as a geometric scalar and its post-temporal identity as the field that sources H?
```

**NEW**

```
What it has not done is develop the geometric *origin* of |Φ_NTE|. Where does the field come from? What governs its post-locking dynamics, and why those rather than others? What is the relationship between |Φ_NTE|'s pre-temporal identity as a geometric scalar and its post-temporal identity as the field that sources H?
```

---

## 4. Chapter 10 — Z-series (base `Chapter_10_The_Silvered_Boundary_v7.md` → v8)

**Z1 supersedes U2.** Apply Z1, not U2. U1, U3, U4 and U5 stand unchanged.

### Z1 — §5 opening (supersedes U2)

**OLD**

```
The framework's reading of dark matter has specific testable predictions beyond κ = 5.50. The cross-thickness coupling, mediated through the unresolved neutrino's bilateral wavefunction, has a *coherence length* set by the neutrino's free-streaming distance — the typical scale over which an unresolved neutrino's wavefunction maintains its bilateral structure before decoherence and gravitational scattering disrupt the coherent superposition.
```

**NEW**

```
The framework's reading of dark matter has specific testable predictions beyond κ = 5.50. The coupling acts wherever the neutrino's bilateral wavefunction gives it a structure to act on, and that wavefunction does not hold its bilateral character over unlimited distances. So the coupling inherits a scale from it — the neutrino's free-streaming scale, the reach over which an unresolved neutrino's wavefunction maintains its bilateral structure before decoherence and gravitational scattering disrupt the coherent superposition. The framework states that scale as a *coherence mass* rather than a length, because a mass is what the gravitational accounting of a system actually turns on: above roughly 4 × 10¹⁴ solar masses, a system is large enough to average over many independent patches of the coupling; below it, it is not.
```

### Z2 — §5, the figure and its context

**OLD**

```
This scale is roughly forty megaparsecs — about a hundred and thirty million light-years.

To put that in context: a typical dwarf galaxy is a few thousand light-years across. A typical large galaxy like our own Milky Way is about a hundred thousand light-years across. A typical galaxy cluster is a few million light-years across. A typical large-scale structure (a filament or supervoid in the cosmic web) is tens to hundreds of millions of light-years across. The framework's coherence length sits roughly at the boundary between galaxy-cluster scale and large-scale-structure scale.
```

**NEW**

```
Four hundred trillion solar masses is a rich galaxy cluster. To put it in context: a typical dwarf galaxy holds perhaps a hundred million solar masses in total; our own Milky Way, a trillion or so; a large galaxy cluster, a few hundred trillion. The coherence mass therefore sits at the boundary between the cluster scale and the scale of the cosmic web's filaments and voids — which is the boundary the next section's prediction turns on.

One caveat travels with this, and the framework states it rather than leaving it implicit: the free-streaming scale is standard neutrino physics, not an NTE derivation. What is the framework's own is the *combination* — this scaling law, around this particular mean of 5.50, with the transition at this scale. And the *size* of the scatter within a single coherence patch is not predicted at all; the corpus carries that amplitude as open. The framework predicts that the scatter is there and how it falls away with mass, not how large it is at the bottom.
```

### Z3 — §8

**OLD**

```
The framework predicts that dwarf-galaxy dark-matter fractions will continue to show wide scatter, while galaxy-cluster fractions will converge toward the cosmic mean — with the scatter falling as σ(M) ∝ M^(−1/2) and the transition near the coherence length, ~40 megaparsecs. As galaxy surveys map increasingly large samples, the distribution should settle into that three-part pattern: shape, mean, and scale. A failure of any part would break the framework's specific claim.
```

**NEW**

```
The framework predicts that dwarf-galaxy dark-matter fractions will continue to show wide scatter, while galaxy-cluster fractions will converge toward the cosmic mean — with the scatter falling as σ(M) ∝ M^(−1/2) above the coherence mass, around 4 × 10¹⁴ solar masses. As galaxy surveys map increasingly large samples, the distribution should settle into that three-part pattern: shape, mean, and scale. The sharpest of the three is the shape: the corpus's own falsifier is the absence of the M^(−1/2) scaling above the coherence mass, and that is the leg that would break the two-sector mechanism outright.
```

---

## 5. Chapter 15 — AA-series (base `Chapter_15_The_Score_v4.md` → v5)

### AA1 — §4, the variance-scaling entry

**OLD**

```
Chapter 10's companion claim: the transition to tight convergence near ~40 Mpc.
```

**NEW**

```
Chapter 10's companion claim: the transition to tight convergence above a coherence mass of around 4 × 10¹⁴ solar masses, the neutrino free-streaming scale — which the framework adopts rather than derives, its own contribution being the combination of that scale with the scaling law and the mean.
```

---

## 6. Flags

**AB1 — PC cannot reproduce 40 Mpc from M_c and is not guessing at the conversion.** At mean cosmic density, 4 × 10¹⁴ M_☉ encloses a comoving radius near 13 Mpc, a diameter near 27 Mpc. That is PC's own back-of-envelope, and it is order-of-magnitude compatible with 40 Mpc without landing on it; the discrepancy could be convention (virial versus mean density, radius versus diameter) or the Book's figure could simply be wrong. **The patches sidestep it by quoting the mass the corpus deposits and giving no length.** If anyone wants a length in the Book, AC should supply it with its convention stated.

**AB2 — the Book is seventeen chapters, and PC's scope statements have been wrong.** PC has repeatedly described the unswept remainder as "Chapters 6–14". The review names **Chapter 16 (*Stranger and Stranger*, v2) and Chapter 17 (*Working Bet*)**, neither of which PC has read or listed. The corrected remainder is **Chapters 6, 7, 8, 11, 14, 16 and 17**, plus the popular editions and Appendix A. PC's fault; the earlier sweep specification's scope should be read as incomplete for the same reason.

**AB3 — Ch 16 heading, not patched because PC has not read the chapter.** The review reports Chapter 16 still carries a section headed *"Toward the Score"* despite sitting after Chapter 15. That is a one-line fix and PC will draft it as part of a Ch 16 pass rather than patch a chapter sight-unseen.

**AB4 — DRAFT filename hygiene, Cursor's to execute on Greg's word.** `Book\Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md` carries campaign-current content under a DRAFT label; `Chapter_14_Strange_Geometries_and_Structural_Rhymes_v2_2_DRAFT_PC_20260705.md` likewise. Both are renames, not edits. **PC recommends holding Ch 14's until its content pass, and doing Appendix C's now** — its content is current and the label is the only thing lying.

**AB5 — the N_e interim staging is correct and needs nothing.** The review notes Chapter 15 still prints 0.9692 and N_e = 63.4 while Appendix C says both move with depth. That is the intended interim: the values are the corpus's current ones, the σ figures were deliberately removed in B3′ so nothing needs repatching when the depth settles, and Appendix C already carries the depth dependence explicitly. No action.

---

## 7. Registration (discipline 10)

```
- **Book/ review-response patch set** (`Handoff_PC_to_Greg_Cursor_Review_Response_Ch4_Ch5_Ch10_Ch15_20260925.md`, PC, 2026-09-25). X1–X7 on `Chapter_04_Time_and_Expansion_v9.md` → v10 (five emergence-lexicon survivors of the C-series, two cosmic-time, one "coupling pattern" after the rest-energy correction — **PC's incomplete sweep, same failure mode as the Ch 1 v9 set**). Y1–Y2 on `Chapter_05_The_Eighth_Colour_v8.md` → v9 (two V_NTE survivors of D10, one asserting a corpus form flag H1 says is unverified). **Z1–Z3 on Ch 10, Z1 SUPERSEDING U2**, and AA1 on `Chapter_15_The_Score_v4.md` → v5: **the corpus deposits a coherence MASS M_c ~ 4×10¹⁴ M_☉ (Part 2 §IX), not a ~40 Mpc length — Cursor's G6 found no such length anywhere in Core_Papers — and the Book also omits Part 2's stated caveat that the within-patch amplitude is open.** Closes W4. **G7 closes the mediation question favourably: Part 1 §III and Companion 5 both explicitly reject mediation, so Ch 10's defect is Book-local and U1/U2 restore corpus language.** Prelude "experienced" examined and **declined** — it is the Greg-ratified seed with an immediate guard. Flags AB1 (40 Mpc not reproducible from M_c; no length quoted), **AB2 (the Book is 17 chapters; PC's "Ch 6–14" scope statements and the sweep spec were incomplete — remainder is 6, 7, 8, 11, 14, 16, 17)**, AB3 (Ch 16 "Toward the Score", unread), AB4 (DRAFT labels), AB5 (N_e staging correct). **Status: PROPOSED, awaiting Greg.**
```

---

## 8. On ratification

Cursor applies X1–X7 → `Chapter_04_Time_and_Expansion_v10.md`; Y1–Y2 → `Chapter_05_The_Eighth_Colour_v9.md`; **Z1 in place of U2**, with U1/U3/U4/U5, → `Chapter_10_The_Silvered_Boundary_v8.md`; AA1 → `Chapter_15_The_Score_v5.md`. Predecessors left in place. Byte-exact, match-or-report, never force.

PC then takes **Chapter 16** — the shortest real gap, one known heading defect and a chapter PC has never read — and after it Chapter 17, which closes the book and has never been checked against the corrected registers. Chapters 6, 7, 8, 11 and 14 stay behind the sweep.
