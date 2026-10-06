# Handoff — PC → Greg (ratify) → Cursor (apply): Ch 10 v9 coherence residual, Ch 16 v3 first pass

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-25
**Arising from:** `Handoffs\Handoff_Cursor_to_PC_AC_40Mpc_Origin_and_Apply_Complete_20260925.md` §3, and PC's first reading of Chapter 16
**Status:** PROPOSED — not ratified

Series **AC** → `Book\Chapter_10_The_Silvered_Boundary_v8.md` → v9. Series **AD** → `Book\Chapter_16_Stranger_and_Stranger_v2.md` → v3.

---

## 0. First: a pattern in PC's own work that needs stating

Cursor's residual report is the fourth time this campaign that a PC patch set has fixed the prominent instances of a retired term and left the quiet ones standing in the same document:

| Set | Missed |
|---|---|
| Ch 1 v9 (P-series) | refrain replaced at 2 of 6 joints; "Revisited" section untouched |
| Ch 4 (C-series) | five emergence-lexicon survivors |
| Ch 5 (D10) | two V_NTE references |
| Ch 10 (Z-series) | **six "coherence length" / "forty megaparsecs" in §5–§6 mid-section prose** |

Each time the mechanism is identical. PC finds the term where the argument turns on it, writes the patch against that passage, and does not re-scan the whole document for the term before filing. Three of the four were caught by someone else — Greg, the reviewer, Cursor.

**The working correction, from this handoff forward:** after authoring any patch set that retires a term, PC re-reads the full target for every instance of that term and lists the count in the handoff, including zero. That is a cheap step and it would have caught all four. It is applied below — AC1–AC3 are the result of doing it to Chapter 10, and §3's counts are the result of doing it to Chapter 16.

---

## 1. The 40 Mpc origin, and what it changes

Cursor located the formula in the historical archive, stable from v10.5 through the superseded v10.17 Part 2 §9.4:

> *R_c ~ 40 Mpc × (0.1 eV / m_ν), giving coherence mass M_c ~ 4.4 × 10¹⁴ M_☉*

So **the length was the input and the mass was derived from it** — the reverse of what PC assumed when flagging AB1. The live corpus kept the mass and dropped the length; the Popular editions kept the length shorthand without the formula, and that is the path by which it reached the Book.

That resolves AB1's arithmetic puzzle: PC's ~13 Mpc radius was a ball of mass M_c at mean cosmic density, which is not what the corpus computed. No contradiction. **PC's envelope was answering a question the corpus never asked.**

But the origin makes the Book's usage worse, not better, in one specific way that is worth recording: **the 40 Mpc figure is mass-dependent, and the Book quotes only the instance.** R_c scales as 1/m_ν, so 40 Mpc is the value *at the reference m_ν = 0.1 eV* and nowhere else. Chapter 15 carries the framework's own second-generation neutrino mass at 0.0086 eV. A reader who took the Book's 40 Mpc as a framework output, and then met 0.0086 eV two chapters earlier, would be holding two numbers that do not sit together without the scaling law neither chapter prints.

Quoting the deposited mass, as Z2 and AA1 now do, sidesteps this entirely. **The patches below finish the job rather than changing its direction.**

---

## 2. Chapter 10 — AC series (v8 → v9)

Cursor reports the load-bearing openers now read *coherence mass* while the mid-section still reads *coherence length*, which is worse than either alone: a reader meets a mass, then six paragraphs of a length, with no statement that they are the same scale. Full count from PC's re-read of the unpatched passages: **six instances across three paragraphs.**

### AC1 — §5, the physics paragraph (3 instances)

**OLD**

```
What this means physically: below the coherence length, the cross-thickness coupling fluctuates significantly. The bilateral wavefunction is intact at small scales, but the coupling's contribution to the gravitational signal varies from place to place, depending on local conditions of the unresolved neutrino's distribution. Above the coherence length, the coupling averages out. The cosmic-scale signal is the geometric mean of the framework's structural calculation; below the coherence length, the local signal can deviate substantially from that mean.
```

**NEW**

```
What this means physically: below the coherence mass, the cross-thickness coupling fluctuates significantly. The bilateral wavefunction is intact in small systems, but the coupling's contribution to the gravitational signal varies from place to place, depending on local conditions of the unresolved neutrino's distribution. Above the coherence mass, a system spans enough independent patches for the coupling to average out. The cosmic-scale signal is the mean of the framework's structural calculation; in systems below the coherence mass, the local signal can deviate substantially from that mean.
```

### AC2 — §5, the sharp prediction (2 instances)

**OLD**

```
The prediction this gives the framework is sharp. *Below* the coherence length — at galaxy and small-cluster scales — the dark-to-ordinary ratio should show wide scatter from system to system. Some systems should be dominated by dark matter; others should have very little. *Above* the coherence length — at large-cluster and cosmic scales — the ratio should converge toward 5.50, with the residual scatter shrinking as M^(−1/2), down to the width of measurement uncertainty at the largest scales.
```

**NEW**

```
The prediction this gives the framework is sharp. *Below* the coherence mass — at galaxy and small-cluster scales — the dark-to-ordinary ratio should show wide scatter from system to system. Some systems should be dominated by dark matter; others should have very little. *Above* it — at large-cluster and cosmic scales — the ratio should converge toward 5.50, with the residual scatter shrinking as M^(−1/2), down to the width of measurement uncertainty in the largest systems.
```

### AC3 — §6, the dwarf/cluster paragraphs and the verdict (3 instances, including the last "forty megaparsecs")

Three separate edits in one section; given as three blocks so Cursor can match each independently.

**OLD (a)**

```
At dwarf galaxy scales — systems much smaller than the coherence length — the dark-matter fractions show wild variation.
```

**NEW (a)**

```
At dwarf galaxy scales — systems far below the coherence mass — the dark-matter fractions show wild variation.
```

**OLD (b)**

```
The framework's reading is that the scatter is structural. Below the coherence length, the cross-thickness coupling fluctuates pointwise, depending on local conditions of the unresolved neutrino's bilateral wavefunction.
```

**NEW (b)**

```
The framework's reading is that the scatter is structural. In systems below the coherence mass, the cross-thickness coupling fluctuates pointwise, depending on local conditions of the unresolved neutrino's bilateral wavefunction.
```

**OLD (c)**

```
At galaxy-cluster scales — systems comparable to or larger than the coherence length — the dark-matter fractions converge.
```

**NEW (c)**

```
At galaxy-cluster scales — systems at or above the coherence mass — the dark-matter fractions converge.
```

**OLD (d)**

```
The framework does not merely predict "scatter below, convergence above"; it predicts the *shape* of the convergence — σ(M) ∝ M^(−1/2) around a mean of 5.50 with the transition near forty megaparsecs.
```

**NEW (d)**

```
The framework does not merely predict "scatter below, convergence above"; it predicts the *shape* of the convergence — σ(M) ∝ M^(−1/2) around a mean of 5.50, with the transition at the coherence mass.
```

**Post-apply check requested:** Cursor to report the count of `coherence length` and `megaparsec` in `Chapter_10_The_Silvered_Boundary_v9.md`. Expected: zero and zero.

---

## 3. Chapter 16 — AD series (v2 → v3), PC's first reading

The review flagged one defect here. There are four, and the heading is the least of them. Term counts from the full re-read: `proper time` ×1, `40-megaparsec` ×1, `kinetic normalisation` ×2, `0.9685` ×1.

**What is good, and needs nothing.** The chapter's discipline is excellent and in places ahead of the chapters it summarises. Case C states the Tsirelson register exactly as Chapter 2 v8 now does — *"the framework's derived leg is the probability rule that computes the bound; the first-principles derivation of the entangled correlation functions themselves remains named open work"*. Case F's BMV treatment is the best forward-commitment writing in the book: it separates the unconditional laboratory channel from the conditional cosmological one and says plainly that a clean negative is a direct strike *"regardless of what the CMB says"*. The opening refuses credit for retrospective passes in the first three sentences. None of that is touched.

### AD1 — the section heading

Chapter 16 sits after Chapter 15, and the section's own closing line already knows it: *"this chapter belongs beside The Score rather than in place of it."* The heading contradicts the paragraph under it. The section's actual thesis is in its penultimate sentence.

**OLD**

```
## Toward the Score
```

**NEW**

```
## Permission, Not Proof
```

### AD2 — Case D, A9 residue

**OLD**

```
That denial is already built into the earlier chapters. The photon does not accumulate proper time along its own path. The entangled object is not two completed local particles carrying independent facts.
```

**NEW**

```
That denial is already built into the earlier chapters. The photon's line has no ruler along it and nothing on it to count. The entangled object is not two completed local particles carrying independent facts.
```

### AD3 — Case F, the retired conditional framing

The chapter names the conditional pair's open input as *"the kinetic normalisation"*. K(Φ) is closed; the open item is the spectral origin of ξ. Same correction as Chapter 15's B3′ and Chapter 10's U5.

**OLD**

```
Chapter 15 placed the tensor-to-scalar ratio in the conditional tier: under the framework's inflationary reading, r sits near a few parts in a thousand, within reach of CMB-S4 and LiteBIRD — but the prediction's full force waits on the framework closing a named piece of homework, the kinetic normalisation, and only one verdict is live even now (an r measured far above that scale would mean the reading has missed something at the dynamics level).
```

**NEW**

```
Chapter 15 placed the tensor-to-scalar ratio in the conditional tier: under the framework's inflationary reading, r sits within reach of CMB-S4 and LiteBIRD — but the prediction's full force waits on the framework closing a named piece of homework. The kinetic normalisation, which used to be that piece, is now closed; what remains open is the spectral origin of the conformal coupling it took to close it, a value the framework selects on frame-closure grounds rather than deriving. Chapter 15 carries the current figure and the two CMB anchors; this chapter will not duplicate them. Even now only one verdict is live: an r measured far above the framework's value would mean the reading has missed something at the dynamics level.
```

### AD4 — the closing catalogue of Chapter 15

Four defects in one sentence: a superseded n_s, a superseded r, the retired K(Φ) framing again, and the 40 Mpc length. Plus two omissions — the strictest tier's qualifiers, and the fact that Chapter 15 now catalogues losses as well as claims.

**On the n_s/r hold.** The standing constraint is to flag rather than write where a chapter's targeting touches n_s or r. **This patch satisfies that constraint by removing the values rather than updating them.** Chapter 16 is a summary chapter pointing at Chapter 15; it does not need to print the pair, and a summary that quotes no figure cannot go stale when the depth settles. Leaving `0.9685` in place was not an option either — it is not the held value, it is the superseded one.

**OLD**

```
Chapter 15 is where the framework puts numbers and absence claims on the table, each at its graded register: the three zero-parameter predictions — κ at 5.50, the maximal CP phase, the maximal atmospheric angle; the conditional pair — n_s near 0.9685 and r near a few times 10⁻³, both awaiting the kinetic normalisation; the required normal mass ordering, with JUNO ruling soon; no WIMP, no fourth generation, no W_R; the double-beta window in the few-meV range; the 40-megaparsec coherence transition and the scatter law around the cosmic mean; the quietness of empty space as structure, with its numerical value honestly on the open ledger.
```

**NEW**

```
Chapter 15 is where the framework puts numbers and absence claims on the table, each at its graded register: the three zero-parameter predictions — κ at 5.50; the CP phase at maximal magnitude, its sign free and the asymmetry's direction therefore not claimed; the maximal atmospheric angle, inherited from an established symmetry literature and credited there rather than claimed. Then the conditional pair, n_s and r, whose values Chapter 15 prints against two CMB anchors and which rest on a conformal coupling the framework selects rather than derives. Then the required normal mass ordering, with JUNO ruling soon; no WIMP, no fourth generation, no W_R; the double-beta window in the few-meV range; the scatter law around the cosmic mean, with its transition at the neutrino free-streaming coherence mass; the quietness of empty space as structure, with its numerical value honestly on the open ledger. And the losses in the same table as the claims — the dark-energy equation of state currently running about three standard deviations against the framework, the atmospheric mass ratio, lithium-7, and a solar mixing angle the framework withdrew rather than refit.
```

---

## 4. Flags

**AE1 — AB1 is closed, and PC's envelope was answering the wrong question.** The ~13 Mpc figure assumed a ball of mass M_c at mean cosmic density. The corpus computed a free-streaming length at a reference neutrino mass and derived M_c from it. No contradiction, and PC's arithmetic was irrelevant rather than wrong. Recorded because a flag that dissolves should be closed explicitly rather than left hanging.

**AE2 — the 40 Mpc figure is mass-scaled, and nothing in the Book says so.** R_c ~ 40 Mpc × (0.1 eV/m_ν). The Book quoted the instance at m_ν = 0.1 eV as though it were a fixed scale, two chapters away from Chapter 15's m_ν₂ = 0.0086 eV. The patches remove the length from the Book entirely, so this needs no further action there — **but the Popular editions still carry the length shorthand, per Cursor's origin trace, and they are unswept.** Worth adding to the mechanical sweep's scope as a seventh rule: `40 Mpc`, `forty megaparsec`, `coherence length`.

**AE3 — Chapter 16's currency items.** Two, neither patched. *"with JUNO ruling soon"* belongs to the F4 bundle. And Case E cites a **2025 observation of a time rondeau crystal** using carbon-13 spins in diamond as a quantum simulator — a specific empirical claim PC cannot verify and which is load-bearing for that case's argument. **Recommend it join the Scratch currency check.**

**AE4 — Chapter 17 remains unread.** It closes the book. On the review's grades it is unchanged since 21 September, which means it has never been checked against any of the corrected registers.

---

## 5. Registration (discipline 10)

```
- **Book/ Ch 10 v9 + Ch 16 v3** (`Handoff_PC_to_Greg_Cursor_Ch10_v9_Residual_and_Ch16_v3_20260925.md`, PC, 2026-09-25). AC1–AC3 on `Chapter_10_The_Silvered_Boundary_v8.md` → v9: six residual `coherence length` / `forty megaparsecs` instances in §5–§6 mid-section prose that the Z-series left behind (reported by Cursor) — after AC, expected count zero. AD1–AD4 on `Chapter_16_Stranger_and_Stranger_v2.md` → v3, PC's first reading: section heading `Toward the Score` → `Permission, Not Proof` (the chapter sits after Ch 15 and its own closing line says so); A9 residue in Case D; the retired kinetic-normalisation framing in Case F and in the closing catalogue; and a stale Ch 15 summary carrying superseded n_s = 0.9685, a superseded r, the 40 Mpc length, and no tier qualifiers — **values removed rather than updated, which satisfies the n_s/r hold rather than breaching it**. **40 Mpc origin closed (AE1): archive Part 2 §9.4 formula R_c ~ 40 Mpc × (0.1 eV/m_ν) → M_c; the length was the input, the mass was derived from it, and PC's mean-density envelope was answering a question the corpus never asked.** Flags AE2 (the length is mass-scaled and the Popular editions still carry it — add as a seventh sweep rule), AE3 (Ch 16 currency: JUNO, and the 2025 rondeau time-crystal observation), AE4 (Ch 17 never read). **Also recorded: a repeated PC failure mode — four patch sets this campaign fixed the prominent instances of a retired term and left the quiet ones; from this handoff PC re-reads the full target for every instance and reports the count, including zero.** **Status: PROPOSED, awaiting Greg.**
```

---

## 6. On ratification

Cursor applies AC1–AC3 → `Chapter_10_The_Silvered_Boundary_v9.md` and AD1–AD4 → `Chapter_16_Stranger_and_Stranger_v3.md`; predecessors left in place; byte-exact, match-or-report, never force; and reports the post-apply counts requested in §2.

PC takes **Chapter 17** next — the last chapter, never read, and the one place where a stale register would be the final thing a reader sees.
