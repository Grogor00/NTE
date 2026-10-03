# Handoff — PC → Greg (ratify) → Cursor (apply): Ch 17 v4, Appendix C v1.5, Ch 9 T4

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-25
**Answers AC's three requests to PC** in `Handoff_AC_Reexamination_Pass_C9_C12_C17_C18_Six_Findings_20260925.md` §Requests.
**Status:** PROPOSED — not ratified

---

## 0. PC read-state ledger (discipline 11)

| Source | Read this session | Note |
|---|---|---|
| `Book\Chapter_17_The_Working_Bet_v3.md` | **Yes, in full** | First read ever by PC |
| `Book\Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md` | **Yes, in full** | Post-apply state |
| `Book\Chapter_09_The_Number_That_Could_Have_Failed_v4.md` | **Yes, in full** (earlier today) | T-series still unratified |
| `Book\Chapter_16_Stranger_and_Stranger_v2.md` | Yes, in full (earlier today) | |
| `Handoff_AC_Reexamination_Pass_…` / `…Verifications_1_and_3_…` | **Yes, both in full** | |
| `NTE_Workflow_Manifest_v10_18.md` | **NO — last read 2026-09-23** | It has grown from 26,739 to 33,448 B since. **Any claim below about §3 or §6 is recollection, marked as such.** |
| Companions 9, 12, 17, 18; Parts 1–3 | **NO — never read by PC** | All corpus claims below are AC's, attributed |

---

## 1. AC's three requests, answered

**Request C — the Ch 9 §6 corroboration: revised ruling accepted, and it is better than PC's.** PC recommended cutting. AC found that Companion 12 §3 supplies the proper grounding *and* a negative PC did not know existed — the factor 3 is three gauge-field components on the base, **not** three Killing-spinor polarisations, the fixed-sign Killing-spinor space on round S³ being two-dimensional, citing Bär, *Commun. Math. Phys.* **154**, 509 (1993). Replacing beats cutting: it is corpus-internal, carries a real external reference, and pre-empts the objection a knowledgeable reader would raise. **T4 below.**

**Request E — the CLFV qualifier set: this is a defect in already-applied Book text, and it is mine.** PC's A5 went into Appendix C v1.4 carrying one caveat. AC reports C18 §3 carries **six** qualifiers explicitly marked to travel with the claim, and that **qualifier 4 matters more than the one PC carried**: a Monte Carlo over random Casas–Ibarra matrices hits a ratio this close roughly once in ten — *"substantial, not overwhelming."* A5 as applied says an observed inequality *"falsifies either the maximal atmospheric angle or the structure that carries it into the flavour sector"* with no indication that a random model reproduces the relation 10% of the time. **It reads far stronger than the corpus allows, and PC made it stronger than v1.3 was.** AF1 below.

**Request D — H1 closes, and the Book needs nothing.** AC confirms V_NTE's form is *not* derived: Companion 9 §3 takes the simplest extension, Companion 8's F3 found it under-constrained off-trajectory, and that simplest form gives n_s = 1, ~8σ off Planck. PC's D10 and Y2 already removed every Book dependency — Cursor's post-apply grep reports `V_NTE` = 0 hits in Ch 5 v9. **No further Book action. H1 closed.**

---

## 2. A second defect I introduced, and one I missed

**AF2 — Appendix C still says "~40 Mpc", and PC read this file in full on the 24th and called it campaign-current.**

`Appendix_C_…_v1_4` §C.5, Rubin and Euclid: *"the coherence-length transition near ~40 Mpc"*. Same defect as Chapters 10, 15 and 16. PC read v1.3 end to end on 2026-09-24, wrote that it was *"more current than PC credited it"*, and withdrew a patch on the strength of that reading — while this line sat in it.

That is the fifth instance of the same failure this campaign, and the worst kind: not a term missed inside a patch set, but a term missed during a **full read undertaken specifically to assess the document's currency**. The §0 correction PC adopted this morning — re-read the target and report counts — would not have caught it either, because the retired term was not yet retired when PC read the file. What would have caught it is re-scanning every previously-cleared document when a *new* term is retired. **PC adds that: retiring a term now triggers a sweep of the documents already declared clean, not only the document in hand.**

Term count in Appendix C v1.4, from this session's full read: `40 Mpc` ×1, `coherence-length` ×1, `coherence mass` ×0.

---

## 3. Chapter 9 — T4 (extends the unratified T-series)

**OLD**

```
Worth one independent check on the count of three before moving on. In an unrelated branch of theoretical physics — work on monopole couplings in field theory contexts unrelated to dark matter or cosmology — the same factor of three appears naturally, for the same reason: it counts the dimension of the adjoint representation of SU(2), the algebraic content the framework's gauge sector lives in. The match is not an independent derivation of κ₀ within this framework (the underlying algebraic content is the same), but it tells us something useful: the framework's identification of dim(adj SU(2)) = 3 as the load-bearing count is structurally well-grounded rather than peculiar to NTE's specific construction. The factor of three has a single structural home in the gauge algebra; multiple physical contexts find it there independently.
```

**NEW**

```
Worth pinning the count of three down before moving on, because there is a wrong three sitting right next to the right one. The three is the dimension of the adjoint representation of SU(2) — three gauge-field components on the base sphere. It is *not* a count of Killing-spinor polarisations, which is the natural guess for anyone who has worked with spinors on the round three-sphere and which would give a different answer: that space is two-dimensional, a result established in the mathematical literature on spinors of constant curvature. The framework's technical corpus states the distinction explicitly and cites it, precisely because the coincidence of nearby counts is the kind of thing that turns a derivation into an accident. The factor of three has one structural home, and it is the gauge algebra.
```

---

## 4. Appendix C — AF series (v1.4 → v1.5)

### AF1 — §C.4, the CLFV entry: the qualifier PC left out

**OLD**

```
An almost-certainly-untestable prediction, stated plainly rather than in disguise, because stating it costs nothing and a surprise observation would score it.
```

**NEW**

```
Two things keep that from being more than it is. The heavy scale makes observation almost certainly impossible, so this is a prediction stated for the record rather than one anybody expects to collect on. And equality is less rare than it sounds: sampling the relevant mixing structures at random reproduces a ratio this close to one about one time in ten. That is substantial and it is not overwhelming, and the framework says so rather than letting the reader supply their own estimate. What the claim is worth, in the end, is that the framework committed to a specific value of a ratio it had no obligation to address at all — stated plainly rather than in disguise, because stating it costs nothing and a surprise observation would score it.
```

### AF2 — §C.5, Rubin and Euclid: the 40 Mpc length

**OLD**

```
**Rubin Observatory and Euclid** — the coherence-length transition near ~40 Mpc, the dark-matter-fraction scatter pattern across hundreds of millions of systems, and the void anatomy of the Hubble tension (framework: directional scatter of 2–4 km/s/Mpc correlated with line-of-sight density).
```

**NEW**

```
**Rubin Observatory and Euclid** — the transition in the dark-matter-fraction scatter at the neutrino free-streaming coherence mass, around 4 × 10¹⁴ solar masses, mapped across hundreds of millions of systems; and the void anatomy of the Hubble tension (framework: directional scatter of 2–4 km/s/Mpc correlated with line-of-sight density). The free-streaming scale is standard neutrino physics rather than an NTE derivation; what the framework claims is the combination of that scale with the M^(−1/2) scaling law and the mean of 5.50, and the corpus carries the scatter's amplitude within a single coherence patch as open.
```

### AF3 — §C.2, a forward reference to a chapter that does not yet say it

**OLD**

```
Until it closes, the temperature is conditional, and Chapter 12 says so.
```

**NEW**

```
Until it closes, the temperature is conditional, and the scorecard of Chapter 15 carries it that way.
```

*Rationale: Chapter 12 v4.1 is the live text and does not yet carry T_GB as conditional — its v4.2 revision is authorised but unapplied and is blocked behind item (a). Chapter 15 v5 does carry it, applied. The appendix should point at a chapter that currently says the thing.*

---

## 5. Chapter 17 — AG series (v3 → v4), PC's first reading

The book's last chapter. Term counts from this session's full read: `proper time` ×4, `emerg*` in the time sense ×2, `K(Φ)` ×1, `kinetic normalisation` ×1.

**What is good and untouched:** the Feynman fingers-of-the-same-hand framing; the six-commitments structure; the octonionic credit, which is stated exactly as Manifest §3 grades it (adopted with credit, the framework's own stake being the *reading*); and §5's refusal to ask the reader to decide — *"You do not need to decide today whether the framework is true."* That is the right last note and nothing here alters it.

### AG1 — §1, the opening sentence of the closing chapter

**OLD**

```
The book began with a fact almost everyone in physics knows and almost nobody follows up: a photon accumulates zero proper time between emission and absorption.
```

**NEW**

```
The book began with a fact almost everyone in physics knows and almost nobody follows up: between a photon's emission and its absorption there is no interval to divide, and no vantage from which to divide it. The line has no ruler along it.
```

### AG2 — §1, the précis

**OLD**

```
The argument, in brief: null-time and entanglement as one geometric pattern on a closed expanding S³; proper time emerging from e-folds through the boundary expansion field |Φ_NTE| (distinct from the Standard Model Higgs); quantum mechanics as state-space geometry with the Born rule a theorem, not an axiom;
```

**NEW**

```
The argument, in brief: null-time and entanglement as one geometric pattern on a closed expanding S³; cosmic time and e-folds as one structure with the boundary expansion field |Φ_NTE| setting the rate between them (that field distinct from the Standard Model Higgs); quantum mechanics as state-space geometry, with the Born rule reformulated rather than assumed;
```

*See flag AH1 — the Born-rule register is the one change here PC cannot verify and is proposing at the weaker reading deliberately.*

### AG3 — §3, the second commitment

**OLD**

```
- **Time from expansion** — *N* is primary; proper time emerges via H = β_NTE|Φ_NTE|².
```

**NEW**

```
- **Time and expansion as one structure** — *N* is primary as a coordinate, because it is the one that can be written without circularity; cosmic time is that expansion counted, at the rate H = β_NTE|Φ_NTE|² sets.
```

### AG4 — §4, the retired conditional framing

**OLD**

```
Open work remains in any case, and Appendix C carries the full ledger: the kinetic normalisation K(Φ) that would convert the inflationary pair into hard tests; the derivation of the heavy seesaw scale M_R;
```

**NEW**

```
Open work remains in any case, and Appendix C carries the full ledger: the spectral origin of the conformal coupling that would convert the inflationary pair into hard tests — the kinetic normalisation it took to get there is closed, and what is open now sits one level beneath it; the derivation of the heavy seesaw scale M_R;
```

### AG5 — §4, the chord's grading stops halfway

The sentence records the demotion and the promotion but not the second demotion. Chapter 15 v4 now says the accounting *"promoted another and then demoted it again."*

**OLD**

```
with the notes graded, one removed by the framework's own accounting, one promoted when its derivation closed.
```

**NEW**

```
with the notes graded, one removed by the framework's own accounting, and one promoted when its derivation closed and then demoted again when the argument under it was found to rest on a truncation artefact — a tally that is allowed to shrink.
```

### AG6 — §5, the last paragraph of the book

**OLD**

```
The shape of time, in this reading, is the shape of expansion. Massive matter accumulates proper time; the photon does not; the neutrino almost does not.
```

**NEW**

```
The shape of time, in this reading, is the shape of expansion. Matter with rest energy accumulates duration; the photon, having none, takes no part in it; the neutrino, with barely any, barely does.
```

*This also carries the rest-energy correction into the book's closing image, where the old version implied the photon has a proper time that reads zero.*

---

## 6. Flags

**AH1 — the Born rule's register: PC is proposing the weaker reading and cannot verify it.** Ch 17 v3 says *"the Born rule a theorem, not an axiom."* PC's recollection of Manifest §3 — **read 2026-09-23, not this session, and the file has grown 6.7 kB since** — is that CR point 5 regraded Born and *t* to *reformulations*. If that recollection is right, "a theorem, not an axiom" sits a tier above what the corpus grants, in the book's summary of itself. AG2 proposes "reformulated rather than assumed", which is safe under either grading. **PC has not read Part 1 §II.0 and is not ruling.** AC to confirm; if Born is genuinely graded a theorem, AG2's clause should revert.

**AH2 — Appendix C v1.4 may be truncated.** The file as PC read it this session ends `whichever way the sky rules` with no terminal punctuation. v1.3 ended the same sentence with a full stop. That is one character and it may be an artefact of how PC read the file rather than of the apply. **Not patched — Cursor to check the byte at end-of-file and fix if the apply dropped it.**

**AH3 — Chapter 17's currency items are the same two as everywhere.** *"JUNO on the neutrino mass ordering"* belongs to the F4 bundle. Nothing else in the chapter is time-sensitive.

**AH4 — item (a) is not ready and the hold stands.** AC's verification 1 puts the value at a band, not a point — AC's own independent estimate gives N_* ≈ 60.2 against Jammer's ≤56 and Scratch's ≈55.5, with the disagreement being the reheating history. AC's locus 11 confirms Book Ch 15 v5 needs a **final pass only**, σ already removed. **PC's B3′ decision holds up: nothing in the Book needs repatching when the band settles.** Chapter 12 stays held.

**AH5 — Companion 12's T_GB contradiction touches the Book's Chapter 12.** AC reports C12 §4 lists T_GB under *"cleanly derived on the spine"* and asserts the master accounting grades it derived/structural, while Part 3 and Companion 9 both call it conditional. Greg's ruling is requested on the corpus side. **For PC's planning: Chapter 12's authorised v4.2 revision — T_GB → conditional — sits on the Part 3 side of that contradiction, which is the side AC's evidence favours.** If Greg rules the other way, the v4.2 authorisation needs revisiting before Ch 12 is written.

---

## 7. Registration (discipline 10)

```
- **Book/ Ch 17 v4 + Appendix C v1.5 + Ch 9 T4** (`Handoff_PC_to_Greg_Cursor_Ch17_v4_AppC_v1_5_Ch9_T4_20260925.md`, PC, 2026-09-25). Answers AC's three requests to PC. **T4** replaces Ch 9 §6's unnamed corroboration with Companion 12 §3's grounding, including the Killing-spinor negative (Bär 1993) — AC's revised ruling, better than PC's recommended cut. **AF1** repairs a defect PC introduced: A5's CLFV entry carried one of C18 §3's six travelling qualifiers and omitted the ~9:1-versus-anarchy figure, making the claim read stronger than the corpus allows. **AF2** removes the ~40 Mpc length from §C.5 — **a term PC missed during a full currency read of v1.3 on 2026-09-24, the fifth instance of PC's incomplete-scan pattern and the first inside a document PC had declared clean.** New PC practice: retiring a term triggers a re-scan of documents already cleared, not only the document in hand. **AF3** re-points a T_GB forward reference from Ch 12 (v4.1 does not yet say it) to Ch 15 (v5 does). **AG1–AG6** on `Chapter_17_The_Working_Bet_v3.md` → v4, PC's first reading: A9 residue in the chapter's opening sentence and in the book's closing image; emergence register in the précis and in commitment 2; the retired kinetic-normalisation framing; and a chord-grading sentence that records the promotion but not the later demotion. **H1 closed — AC confirms V_NTE's form is not derived; D10/Y2 already removed every Book dependency and Cursor's grep reports zero hits.** Flags AH1 (Born-rule register — PC proposing the weaker reading, has not read Part 1 §II.0, not ruling), AH2 (possible one-character truncation at Appendix C EOF), AH4 (item (a) is a band not a point; B3′ holds; Ch 12 stays held), AH5 (C12 vs Part 3 on T_GB — Ch 12's authorised v4.2 sits on the Part 3 side). **Status: PROPOSED, awaiting Greg.**
```

---

## 8. On ratification, and what is left

Cursor applies T4 with T1–T3 → `Chapter_09_…_v5.md`; AF1–AF3 → `Appendix_C_The_Open_Ledger_v1_5_PC_20260925.md` (**and the DRAFT_PC label drops on this rename, per AB4 — the content is current and the label was the only thing lying**); AG1–AG6 → `Chapter_17_The_Working_Bet_v4.md`. Byte-exact, match-or-report, never force. Plus the AH2 end-of-file check.

**Every chapter of the Book has now been read by PC except six: 6, 7, 8, 11, 12 and 14.** Twelve of eighteen files are patched or proposed. Chapter 12 is held behind item (a). Chapters 6, 7, 8, 11 and 14 are waiting on the mechanical sweep, which has not returned — and per PC's note to AC yesterday, that sweep is not coverage: two of the campaign's three most serious findings were collapsed distinctions invisible to string matching, so those five need reading passes regardless.
