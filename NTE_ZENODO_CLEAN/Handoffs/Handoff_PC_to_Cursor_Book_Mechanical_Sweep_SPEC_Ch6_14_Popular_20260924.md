# Handoff — PC → Cursor: mechanical sweep specification, Chapters 6–14 and both popular editions

**From:** PC
**To:** Cursor Main · **Cc:** Greg, AC
**Date:** 2026-09-24
**Greg ratified 2026-09-24, 22:24 NZST.**

**This is a READ-ONLY job. Cursor applies nothing, edits nothing, renames nothing, renders nothing.** The deliverable is a located-instances report. Every decision about what a hit means, and whether it changes, belongs to PC and then to Greg.

---

## 1. Why a sweep rather than another nine reading passes

Chapters 1–5, 15 and Appendix C were corrected chapter by chapter today. That was the right method while the rules were still being settled — three of them were discovered *by* reading, and two of the corrections changed what the corpus says rather than what the Book says.

The rules are settled now. Six of them have fixed replacements and are findable by string match rather than by judgement. Reading nine more chapters to find them would spend PC's attention on the part a search does better, and leave less of it for the part a search cannot do at all.

**What the sweep does not replace.** Chapters 9, 10, 12 and 13 carry substantive physics that needs a register check against the corpus regardless of what this sweep returns — κ's "exactness" language in Ch 9, the cross-thickness mechanism in Ch 10, the chord's tier structure in Ch 12, and the Λ / DESI material in Ch 13. Ch 12 additionally has an authorised v4.2 revision already ratified (2026-09-18): T_GB → conditional, (n_s, r) → 0.9692 / 0.0053 at N_e = 63.4 with dual anchors, no re-promotion to a zero-parameter chord note. **The sweep removes the mechanical half of those passes; it does not remove the passes.**

---

## 2. Scope — resolved by name and path, 2026-09-24

**Swept, in `G:\My Drive\NTE_ZENODO_CLEAN\Book\`:**

| File | Bytes |
|---|---|
| `Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6.md` | 23,536 |
| `Chapter_07_The_Gauge_Birth_v4.md` | 9,858 |
| `Chapter_08_The_Unresolved_Particle_v5.md` | 35,442 |
| `Chapter_09_The_Number_That_Could_Have_Failed_v4.md` | 42,043 |
| `Chapter_10_The_Silvered_Boundary_v7.md` | 29,836 |
| `Chapter_11_What_the_Universe_Sounds_Like_v4.md` | 21,824 |
| `Chapter_12_The_Chord_v4_1.md` | 34,048 |
| `Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md` | 26,505 |
| `Chapter_14_Strange_Geometries_and_Structural_Rhymes_v2_2_DRAFT_PC_20260705.md` | 22,663 |

**Swept, in `G:\My Drive\NTE_ZENODO_CLEAN\Popular_Editions\`:**

| File | Bytes |
|---|---|
| `Popular_Full_Edition_v10_19_0.md` | 79,332 |
| `Popular_Reader_Edition_v10_19_0.md` | 19,702 |

**Identity check only, in `Book\`:** `Appendix_A_Popular_Reader_Edition_v10_19_0.md` (19,702 B). Same byte count as the Reader edition, consistent with Appendix A being a synced copy. **Do not sweep it as a separate document.** Instead report one line: whether it is byte-identical to `Popular_Reader_Edition_v10_19_0.md`. If it is, one patch set will cover both by re-sync. If it is not, that divergence is itself a finding and PC needs the diff.

**Out of scope, explicitly.** Chapters 1–5, 15, the Prelude and Appendix C (corrected today). Everything under `Core_Papers\` (corpus, AC's lane, different disciplines). Anything not reached by descending from `G:\My Drive\NTE_ZENODO_CLEAN\` — treat as archive per manifest §4.

---

## 3. The six rules

Match **case-insensitively** across all swept files. Report **every** hit, including ones that look legitimate — the triage is PC's, and a filtered report hides exactly the marginal cases that matter. Where a rule lists known false positives, that is guidance for the *Note* column, **not** licence to omit the row.

---

### R1 — photon-frame vocabulary

Retired: the photon has no frame, no vantage and no clock. The question is *undefined*, not extreme, and the positive replacement is **the line has no ruler along it**.

Match any of:
`photon's frame` · `photon frame` · `frame of the photon` · `photon's rest frame` · `rest frame of the photon` · `photon's perspective` · `from the photon's` · `photon's point of view` · `photon's vantage` · `as far as the photon is concerned` · `for the photon, ` · `photon experiences` · `photon's own`

Also match `same event` and `same point` **only where** `photon`, `emission` or `absorption` occurs within the same sentence — this catches the same-event overclaim Chapter 1 v10 retired.

**Known false positives, still report:** "frame" or "perspective" attached to a massive observer, a laboratory, or a reader is legitimate and must stay. The Prelude's seed line *"The photon experienced no time at all"* is deliberately kept and is not a defect — if an equivalent appears in a popular edition, flag it as `SEED?` in the Note column and leave it to PC.

---

### R2 — the two-readings refrain

Retired by Ch 1 v10, and Chapter 3 proved the retirement was chapter-local: it survived in three places, including in a paragraph summarising Chapter 1. Expect it to survive here too.

Match: `two readings` · `both readings` · `two vantages` · `both vantages` · `two viewpoints` · `both viewpoints` · `two true things` · `one object with two` · `two perspectives`

**Known false positive, still report:** two readings of an *instrument*, or two measurements by two real observers, are fine. What is retired is the claim that one object is read two ways by two vantages when only one vantage exists.

---

### R3 — proper time where the relation delivers cosmic time

The rule: **dt/dN = 1/(β_NTE|Φ_NTE|²) delivers cosmic time** — the clock of an observer at rest in the mean expansion. Proper time is what a *local* clock makes of it, and the difference between the two is what gravitational dilation *is*. Proper time remains correct when describing a specific observer's own clock, a dilation ratio, or a massive particle's worldline.

Match: `proper time` · `dt/dN` · `dt = dN` · `accumulates proper` · `zero proper time` · `no proper time`

In the Note column, mark each hit **COSMIC** (the text is describing the output of the central relation, and the term is wrong) or **LOCAL** (the text is describing a particular clock, and the term is right) or **UNCLEAR**. That triage is a judgement call — give your best reading and PC will check it; an UNCLEAR is a perfectly good answer and is more useful than a confident wrong one.

`zero proper time` and `no proper time` applied to the photon are **also** R1 hits — cross-tag them `R1+R3`.

---

### R4 — Higgs coupling as embedding depth

Retired. **Rest energy** sets embedding depth. The Higgs supplies most of it for fundamental fermions; the strong interaction's binding energy supplies most of a hadron's, and arrives at confinement rather than at gauge birth. Chapter 1 v10 carries the corrected form and is the reference wording.

Match: `embedding depth` · `how deeply` · `deeply embedded` · `zero Higgs coupling` · `same dial` · `one dial` · `mass dial` · `time dial` · `decides who rides`

Also match `Higgs coupling` and `Yukawa` **only where** `embed`, `depth`, `participat`, `time` or `dial` occurs within the same sentence.

**Known false positive, still report:** the Higgs's ordinary Standard Model job — giving fundamental fermions their mass — is untouched and correct. What is retired is Higgs coupling being the thing that embeds.

---

### R5 — the emergence register

**Not in Greg's original four; PC is adding it, and here is why.** Chapter 1 carried five instances and Chapter 3 carried four, so the base rate across nine chapters is high. It is the same kind of search, it costs nothing extra in the same pass, and running it separately later would mean a second sweep and a second round of patches over the same files. If Greg would rather hold it, drop R5 and the rest of the spec stands unchanged.

The ruling: time and expansion are not two phenomena one of which produces the other. They are one structure, with a rate between them. **The corpus's N-primary / t-derived ontology is untouched** — that is a claim about which *coordinate* can be written without circularity, and it survives. What is retired is expansion *producing* time.

Match: `emerges from` · `emergent from` · `emerge from` · `emergence of time` · `time emerges` · `gives rise to time` · `produces time` · `time is emergent` · `Time as Expansion`

**Known false positive, still report:** "emergence" used of gauge structure, of the Standard Model switching on, or of any other emergent phenomenon is fine. Only time-from-expansion is retired. Note that `Non-Temporal Emergence` is the framework's name and appears in every masthead — **exclude exact matches of the framework name and its acronym expansion from the count**, but report them once per file as a masthead line so PC knows they were seen and skipped.

---

### R6 — the Chapter 4 retitle

`Chapter_04_Time_as_Expansion_v8.md` became `Chapter_04_Time_and_Expansion_v9.md` today. Chapter 3's forward pointer was the last one PC found by reading, but PC read only Chapters 1–5.

Match: `Time as Expansion` · `Chapter_04_Time_as` · `Chapter 4 — Time as` · and any reference to Chapter 4 by title rather than by number.

Report separately from R5 even though the string overlaps.

---

## 4. Report format

Write to **`G:\My Drive\NTE_ZENODO_CLEAN\Working\_book_mechanical_sweep_Ch6_14_Popular_20260924_REPORT.md`**.

One section per swept file, files in the order listed in §2. Within each file, one table:

```
| # | Rule | Line | Matched text | Context | Note |
```

- **Line** — line number in the `.md`.
- **Matched text** — the matched string only.
- **Context** — the full sentence containing it, verbatim. A sentence, not a window of N characters: PC has to judge register from it, and a truncated clause cannot be judged. Where the sentence exceeds ~400 characters, give the clause plus the sentence's first and last twenty words and mark it `TRUNC`.
- **Note** — the R3 triage (`COSMIC` / `LOCAL` / `UNCLEAR`), the R1 `SEED?` tag, cross-tags like `R1+R3`, or blank.

**A zero-hit file is a result and must be reported as such** — a line reading `Chapter_07: no hits on R1–R6` tells PC the file was checked. A file silently absent from the report does not.

**End the report with a totals block:** hits per rule, hits per file, and the Appendix A identity result.

Then a completion handoff to `Handoffs\`, addressed to PC, giving the totals and nothing else — the detail belongs in the report.

---

## 5. What happens next, so the shape of the job is clear

PC reads the report, not the nine chapters. Every hit resolves into one of three buckets:

1. **Mechanical** — the replacement is the settled one and needs no thought. PC writes these as a single patch set covering all files.
2. **Judgement** — the hit is real but the replacement depends on what the passage is doing. PC reads only those passages, in context.
3. **Correct as written** — the false positives. PC records them in the handoff so the next sweep does not re-raise them.

Then the four chapters carrying substantive physics — 9, 10, 12, 13 — get their register passes, with Ch 12's authorised v4.2 revision folded into its set.

Nine chapters of reading becomes one report, one patch set, and four targeted passes. Appendix A follows from the Reader edition by re-sync.

---

## 6. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ mechanical sweep, Ch 6–14 + popular editions** (`Handoff_PC_to_Cursor_Book_Mechanical_Sweep_SPEC_Ch6_14_Popular_20260924.md`, PC, 2026-09-24, Greg-ratified 22:24 NZST). READ-ONLY located-instances sweep, no apply. Six rules: R1 photon-frame vocabulary, R2 two-readings refrain, R3 proper-vs-cosmic time, R4 Higgs-coupling-as-embedding-depth, R5 emergence register (PC addition), R6 Chapter 4 retitle pointers. Report to `Working\_book_mechanical_sweep_Ch6_14_Popular_20260924_REPORT.md`. Appendix A checked for byte-identity with the Reader edition rather than swept. Does not replace the register passes owed on Ch 9, 10, 12 and 13; Ch 12 additionally carries its authorised v4.2 revision from 2026-09-18. **Status: SPEC ISSUED, awaiting Cursor.**
```

---

## 7. One standing instruction

If a rule as written turns out to be unrunnable, ambiguous, or to return an implausible number of hits — more than roughly a hundred and fifty on any single rule would be implausible and probably means the pattern is too loose — **stop that rule, report what you have, and say so.** Do not widen or narrow a pattern to make the output look reasonable. A rule that misfires is information PC needs; a quietly adjusted rule is a report PC cannot trust.

---

— PC, 2026-09-24.
