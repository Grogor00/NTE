# Handoff — PC → Greg (ratify) → Cursor (apply): Chapter 13 v7 patch set

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-24
**Base file:** `Book\Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md` (canonical, 26,505 B)
**Target:** `Book\Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v7.md` — v6 left in place
**Status:** PROPOSED — not ratified

Patch series **Q**, flags series **S**.

---

## 0. Why Chapter 13 and why now

The mechanical sweep is out with Cursor and covers the four settled string-level rules. It explicitly does not cover the register passes owed on Chapters 9, 10, 12 and 13, and those are the part that needs reading rather than searching.

Chapter 12 is blocked in part: its authorised v4.2 revision carries (n_s, r) → 0.9692 / 0.0053, and the standing constraint is to flag rather than write where a chapter's targeting touches n_s or r until the N_e item lands. So Ch 12 waits.

**Chapter 13 is clear of that constraint, and PC checked rather than assumed.** The chapter mentions the spectral index twice, both times inside the a₄ = 0 narrative — *"it closed the route that would have made the spectral index a note of the chord"* — and prints **no value for n_s and no value for r anywhere**. Nothing in this patch set targets either. Chapter 13 is also the chapter most exposed to today's corpus corrections, because it owns the reading that Chapter 15 now says is under pressure.

---

## 1. The principal finding

**Chapter 13 lists the named ways its central claim can fail, and the list omits the one that is currently firing.**

The chapter's failure clause reads:

> *"a demonstration that the framework's spectral triple does not in fact carry the volume constraint, or that a boundary-only ontology nonetheless requires a gravitating extensive vacuum term, would break the resolution at its root."*

Both are internal — theoretical demonstrations about the framework's own machinery. **No observational falsifier is named.** But there is one, it is live, and the corpus carries it at the sharpest register in the snapshot: **w = −1 naked at ~3.1σ against DESI DR2 (BAO + CMB, supernova-independent), with the void mechanism signed anti-DESI and no internal mitigation available.**

That is not a peripheral result for this chapter. Chapter 13's entire claim is that Λ is *structural quietness* — a residual constant the geometry permits and nothing drives. If dark energy is genuinely evolving, it is not a residual constant, and the quietness reading does not describe it. Chapter 15 v4 already says so in as many words: *"the reading of Λ as structural quietness rather than dynamics fails with it."*

So the scorecard chapter states the exposure and the chapter that owns the claim does not. That is the wrong way round. A chapter whose closing move is *"the quietness claim is a genuine stance, not a tautology, and it can fail in named ways"* has to name the way it is currently failing, or the sentence is doing the opposite of its stated job.

Q3 fixes it. Everything else in this pass is small.

---

## 2. Patches

### Q1 — the Planck mass figure is wrong

The chapter gives the Planck mass as *"about a tenth of a milligram"*. It is about **22 micrograms** — roughly a factor of 4.6 smaller. The Planck volume figure in the same sentence (10⁻¹⁰⁴ m³) is right and stays.

**OLD**

```
The Planck mass and the Planck volume are the natural units physics uses for the deepest scales — about a tenth of a milligram and ten to the minus a hundred and four cubic metres, respectively, for readers who want concrete numbers.
```

**NEW**

```
The Planck mass and the Planck volume are the natural units physics uses for the deepest scales — about twenty-two micrograms and ten to the minus a hundred and four cubic metres, respectively, for readers who want concrete numbers.
```

---

### Q2 — the chord list should not flatten the registers

The chapter lists the chord's notes in passing. T_GB now sits at conditional register, and Chapter 12's authorised v4.2 revision will say so. A bare list beside κ₀ reads as though they held the same grade. This is a light touch that defers to Ch 12 rather than pre-empting it.

**OLD**

```
The bare coupling, the gauge-birth temperature, the mass scales, the recurring volume signature — these are sounds the universe-instrument makes when its modes are excited.
```

**NEW**

```
The bare coupling, the gauge-birth temperature, the mass scales, the recurring volume signature — these are sounds the universe-instrument makes when its modes are excited, each at its own register, which Chapter 12 sets out and does not treat as equal.
```

---

### Q3 — the missing observational falsifier

**OLD**

```
The quietness claim is a genuine stance, not a tautology, and it can fail in named ways: a demonstration that the framework's spectral triple does not in fact carry the volume constraint, or that a boundary-only ontology nonetheless requires a gravitating extensive vacuum term, would break the resolution at its root. Within gravity research at large, the same commitment is the well-defined content of the trace-free formulation, whose consequences are studied independently — the framework's stance is tied to that programme's fate as well as to its own.
```

**NEW**

```
The quietness claim is a genuine stance, not a tautology, and it can fail in named ways. Two of them are internal: a demonstration that the framework's spectral triple does not in fact carry the volume constraint, or that a boundary-only ontology nonetheless requires a gravitating extensive vacuum term, would break the resolution at its root. Within gravity research at large, the same commitment is the well-defined content of the trace-free formulation, whose consequences are studied independently — the framework's stance is tied to that programme's fate as well as to its own.

The third way is not internal, and it is not hypothetical. Everything in this chapter treats the surviving cosmological constant as a *constant* — a residual the equations permit, that nothing in the vacuum drives, sitting at whatever value it sits at and staying there. That is the whole content of reading it as quietness rather than as dynamics. If the dark energy is not constant, this chapter is describing the wrong object.

And the measurements are not currently comfortable. DESI's second data release, combining baryon acoustic oscillations with the microwave background and independent of the supernova samples, prefers an evolving equation of state over a fixed one at about three standard deviations. The framework has no way to absorb that. Its void mechanism, which does real work on the Hubble tension, is signed the wrong way here and works against the DESI preference rather than explaining it away — the corpus says so explicitly rather than leaving the option quietly open. So the position is exposed: a quiet constant is what the geometry delivers, a dynamical field is what the data currently leans toward, and there is no adjustment between them.

The verdict window is the rest of this decade. If the preference softens as the surveys complete and the systematics settle, the quietness stands and this chapter was right. If it hardens, then whatever is accelerating the late universe is not the still residual the instrument permits, and the reading fails — not at the edges, but at the thing it was a reading of. The mechanism that forbids the catastrophic term would survive that; the identification of what is left with the dark energy we observe would not.
```

---

### Q4 — the closing seed line, A9

The book's last chapter of the arc reaches back to the Prelude's seed and states it in the retired form. The Prelude's own wording was corrected at v7; this echo was not.

**OLD**

```
The framework's working bet, from the prelude, was that the photon's zero proper time is the seed from which a structural account of physics could grow.
```

**NEW**

```
The framework's working bet, from the prelude, was that the photon's null-time — a connection with no ruler along it, nothing on it to count — is the seed from which a structural account of physics could grow.
```

---

### Q5 — the same sentence's emergence register

Continues from Q4's sentence into the summary of the whole picture.

**OLD**

```
The growth is this picture: a closed three-sphere boundary, a field |Φ_NTE| that sets how expansion becomes experienced time through the central equation H = β_NTE|Φ_NTE|², a cascade that hands the Standard Model its symmetries at birth, a chord of structural results read from one computation — and a silence where physics expected a catastrophe, explained not by turning the noise down but by showing that the loud version of empty space was never the right calculation to run.
```

**NEW**

```
The growth is this picture: a closed three-sphere boundary, a field |Φ_NTE| that sets the rate at which expansion is counted as time through the central equation H = β_NTE|Φ_NTE|², a cascade that hands the Standard Model its symmetries at birth, a chord of structural results read from one computation — and a silence where physics expected a catastrophe, explained not by turning the noise down but by showing that the loud version of empty space was never the right calculation to run.
```

---

## 3. Flags

**S1 — Chapter 13 handles the non-uniqueness point better than Chapter 15 did, and no patch is needed.** Worth recording because it is the first place today a chapter was *ahead* of the corpus snapshot rather than behind it. Ch 13 already credits Chamseddine and Connes by name and date, already says the constraint is *"imported machinery, not an NTE discovery"*, and already ties the framework's stance to the trace-free programme's fate. Chapter 15's B9 patch was bringing the scorecard up to what this chapter already said. Nothing to fix.

**S2 — the arithmetic checks out, all of it except Q1.** PC verified the chapter's numerical claims independently: 10¹²⁰ overshoot; observed ~10⁻¹²² in Planck units; electroweak cutoff giving ~10⁻⁵⁹ and therefore 63 orders too large; QCD-scale cutoff 42 orders too large; Planck volume ~10⁻¹⁰⁴ m³. All consistent. Only the Planck mass was wrong, and only by a factor of 4.6 in a parenthetical. Literature also clean: Weinberg 1989, the 2011 Nobel, Chamseddine–Connes 1997–2010 and the 2008 a₄ result all correctly attributed and consistent with Manifest §3.

**S3 — n_s and r are not touched by this pass.** Stated explicitly for the record, since the standing constraint makes this a checkable condition rather than a judgement. Chapter 13 prints neither value. The two mentions of the spectral index are both narrative — the a₄ = 0 route closing — and carry no number and no targeting claim. If AC's N_e item moves the pair, Chapter 13 needs no repatch.

**S4 — Companion 5's §9 now contradicts the Book, not just item 11.** Not PC's to fix, and AC has it drafted and waiting on one word, but it is worth recording that the exposure grew this evening. Chapter 3's M10 went in tonight carrying the ratified reading: exact flatness excluded, closed curvature required, an open universe falsifying the ontology. Companion 5 §9 reportedly still says non-zero curvature falsifies NTE. So the contradiction is no longer confined to two deposited corpus statements — a reader holding Chapter 3 and Companion 5 would hit it too. **The Book side is correct and needs nothing.** The exposure closes when Companion 5 does.

---

## 4. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ Chapter 13 v7 patch set** (`Handoff_PC_to_Greg_Cursor_Chapter13_v7_Patch_Set_20260924.md`, PC, 2026-09-24) — Q1–Q5 on `Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md`. **Principal finding (Q3): the chapter names the ways its central claim can fail and omits the only one currently firing — w = −1 against DESI DR2 at ~3.1σ, with the void mechanism signed anti-DESI and no internal mitigation. Ch 15 v4 already carries the exposure; the chapter that owns the Λ-as-quietness reading did not.** Also: Planck mass corrected from "a tenth of a milligram" to ~22 micrograms (Q1); chord-list register qualifier deferring to Ch 12 (Q2); A9 seed line (Q4); emergence register (Q5). Flags S1 (Ch 13 was ahead of the snapshot on Λ non-uniqueness — no patch), S2 (all other arithmetic and literature verified clean), **S3 (n_s and r not touched — chapter prints neither value, so it is clear of the standing hold)**, S4 (Companion 5 §9 now contradicts ratified Book prose as well as item 11; Book side correct). **Status: PROPOSED, awaiting Greg.**
```

---

## 5. On ratification, and what PC takes next

Cursor applies Q1–Q5 byte-exact, saves as `Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v7.md`, leaves v6 in place, match-or-report, never force.

PC then takes **Chapter 9** (κ — the framework's flagship number, and the chapter most likely to carry exactness language that the corpus grades more carefully: §3 says κ is *"algebraically exact given its structural inputs, **not '± 0'**"*), then **Chapter 10** (the cross-thickness mechanism and the coherence scale). Both are clear of the n_s/r hold.

**Chapter 12 stays held** until the N_e item lands, since its authorised v4.2 revision carries the (n_s, r) pair directly. When it clears, Ch 12's set will be the largest of the four — the v4.2 revision plus whatever the mechanical sweep returns for it.
