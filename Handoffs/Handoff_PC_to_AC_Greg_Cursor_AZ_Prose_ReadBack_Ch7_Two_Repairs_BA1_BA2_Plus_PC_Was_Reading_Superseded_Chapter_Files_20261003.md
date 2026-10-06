# Handoff — PC to AC, Greg, Cursor Main

**Date:** 2026-10-03
**Subject:** AZ1–AZ7 prose read-back complete. Chapter 7 needs two repairs (BA1, BA2). Separately, and more seriously: PC has been registering patches against superseded chapter files.
**Status:** BA1–BA2 proposed, not applied. Section 3 is a self-report, not a patch.

---

## 1. Why this read-back happened

Greg applied a prose test to Part 2 §XIII: four edits in close succession can read as stacked caveats rather than a passage. Chapter 7 had just taken three edits in one passage (AZ5–AZ7), and two of the DESI replacements are substantially longer than what they replaced. Same risk; prose coherence is PC's lane. So all seven applied AZ edits were read back in situ, not as diffs.

**Chapter 15 v6 — reads well.** AZ1's longer dark-energy entry sits naturally among the parallel long entries around it; the length is not conspicuous. AZ2's clause swap in §6 is clean.

**Appendix C v1.7 — reads well.** AZ3's replacement flows inside C.1's five-entry list. AZ4's clause swap in C.5 is clean.

**Chapter 7 v5 — three problems, two repairs proposed.** Below.

---

## 2. Chapter 7 v5 — what the read-back found

File: `Book\Chapter_07_The_Gauge_Birth_v5.md`, section *"What Happens at N_lock — Four at Once"*, lines 69–87.

### 2a. The missing blank line is worse than registered (BA1)

PC registered this on 2026-09-26 as AX1 defect #4 and described it as a cosmetic paragraph break. It is not cosmetic. Lines 80 and 81 are adjacent with no blank line between them:

```
80 | A word about **embedding depth**, because the term has two jobs ... The two readings
     coincide for a fundamental fermion and part company for everything built out of them.
81 | **4. The bang.** Pre-temporal matter sat at enormous density **without** gauge forces ...
```

In Markdown these render as **one paragraph**. Item 4 does not begin a new block; the bold `4. The bang.` appears mid-paragraph, immediately after a sentence about protons and gluon binding energy. A reader meets the fourth member of a four-item list as a bolded phrase inside a digression about terminology. AZ5 was applied on top of this, so AZ5's text inherits the fault.

Seven days outstanding. PC owns the under-grading: it was filed as a formatting nit and should have been filed as a rendering defect.

### 2b. Item 4 is now four paragraphs against one each for items 1–3

Items 1 (Time), 2 (Gauge structure) and 3 (Mass) are one paragraph each. Item 4 now runs lines 81, 83, 85, 87 — the bang, the thermal-scream statement, the open-question passage AZ5 added, and the Higgs/|Φ_NTE| line.

The list's rhetorical point is its first line: *"Several identities crystallise at the **same** e-fold. That is why the framework calls it a birth, not a slow dimmer switch."* Four things arriving at once is the claim, and the form carries it. One item four times the length of the others reads as three things and then an essay.

### 2c. The closing line is orphaned

*"The **SM Higgs** and **\|Φ_NTE\|** acquire their distinct post-locking identities here too — same moment, different jobs forever after."*

That sentence closed the list — "here too", "same moment" both point back at the four. It now sits after a long paragraph about what the framework cannot yet select between, so "here" and "same moment" have to reach back past an open question to find their referent.

### 2d. Not proposed, flagged only

The embedding-depth paragraph (line 80) also sits **between items 3 and 4** with no marker of its own. It is good and necessary material, and BA1 will at least let it render as its own paragraph. Whether it should be lifted out of the list entirely is a composition question, not a defect; PC is not patching it here.

---

## 3. PC has been reading superseded chapter files

This matters more than section 2 and is reported against PC.

A directory listing of `Book\` taken for this read-back shows later versions, dated **2026-09-25 11:12**, of five chapters PC has been registering patches against at earlier versions:

| PC has been reading | Live file also present | Lines differing |
|---|---|---|
| Chapter_03 v8 | **Chapter_03_A_Closed_Universe_v9.md** | 2 |
| Chapter_06 v6_1 | **Chapter_06_Why_Quantum_Mechanics_is_Geometry_v7.md** | 12 |
| Chapter_08 v5 | **Chapter_08_The_Unresolved_Particle_v7.md** (v6 also exists) | 10 |
| Chapter_11 v4 | **Chapter_11_What_the_Universe_Sounds_Like_v5.md** | 2 |
| Chapter_14 v2_2_DRAFT_PC | **Chapter_14_..._v2_3.md** | 8 |

Two spot checks, both of which land on live PC register items:

- **AS1 (Chapter 11, T_GB register) is already applied.** v5 line 117 reads *"...on the reading that the relation fixing the circle's size is the one the framework has identified, which is the open grounding here rather than a settled one... Chapter 12 grades it."* PC has been carrying AS1 as outstanding.
- **AN4 (Chapter 3, "sixty e-folds") is already changed.** v9 line 64 reads *"after fifty e-folds, it's e⁵⁰ ≈ 5 × 10²¹ times larger."*

So some unknown fraction of the yielded Book queue — AO2–AO5, AV1–AV7 (Ch 6), AQ1–AQ3, AW1, AW2 (Ch 8), AS1 (Ch 11), AT1–AT4 (Ch 14), the Chapter 3 scoping patch — is aimed at text that no longer exists in that form, and some of it may already be satisfied.

**What this does not touch.** Chapters 7, 12, 15 and Appendix C have no later versions in the folder, so AZ1–AZ7, AY1–AY3 and the Chapter 7 defect register are aimed at live files. Section 2 above stands.

**What PC got wrong.** PC read each chapter once, at whatever version it opened, and then kept registering against that version without re-checking the folder. Discipline 11 says name the file before you rule; PC named the file but did not check it was the current one. Proposed as a standing addition, in PC's lane and offered to all streams: **before registering a patch against a file read in an earlier session, re-list the directory and confirm no later version exists.**

**What PC is not doing.** Not re-aiming the Book queue now. The Book is yielded to channel work under the ratified priority, and re-reading five chapters at their live versions is a full pass, not a correction. This is filed so that nobody applies a stale register in the meantime. When the Book comes off yield, PC's first action is a version reconciliation across all seventeen chapters before any further patch work.

---

## 4. Patches proposed

New series **BA**, because these arose from the read-back rather than from the original register.

### BA1 — Chapter 7 v5, restore the paragraph break

**File:** `Book\Chapter_07_The_Gauge_Birth_v5.md`
**Location:** between line 80 and line 81.
**Action:** insert one blank line, so that `**4. The bang.**` begins its own block.
**No text changes.** This is the outstanding AX1 defect #4, regraded from cosmetic to rendering.

### BA2 — Chapter 7 v5, lift the open question out of item 4

**File:** `Book\Chapter_07_The_Gauge_Birth_v5.md`
**Location:** line 85 (the paragraph beginning *"How that scream connects to the hot radiation bath..."*).

**Action, in three moves, no words of AZ5 changed:**

1. **Move line 87** — *"The **SM Higgs** and **\|Φ_NTE\|** acquire their distinct post-locking identities here too — same moment, different jobs forever after."* — to sit immediately after line 83 (the thermal-scream statement), closing the four-item list as it did before.
2. **Insert a subsection heading** after that, in the chapter's voice:
   `## Where the Bang's Account Stops`
3. **Place line 85 unchanged** under that heading.

**Why.** Item 4 returns to list-item length, so the four-at-once form carries its claim again. The Higgs/|Φ_NTE| line regains its referent. And the open question gets its own heading, which is the more honest placement: it is a **boundary on the chapter's claim**, not a fifth thing that crystallises at N_lock. AZ5's substance — the energy-conservation cap, the two histories, *"The framework does not currently select between those histories"* — is preserved verbatim and is, if anything, harder to skip under a heading than buried as the third paragraph of a list item.

**Ruling needed:** the heading wording. `## Where the Bang's Account Stops` is PC's draft; AC or Greg may prefer something flatter. The structural move does not depend on the wording.

---

## 5. Status

- AZ1–AZ7: applied by Cursor, verified by Cursor, **prose read-back now complete across all seven**. Chapter 15 and Appendix C clear.
- BA1, BA2: proposed, awaiting ruling. Chapter 7 is a protected file under the ratified priority, so these go to Greg/AC before Cursor.
- Section 3: self-report, no action requested beyond not applying stale Book registers.
- C21 v0.7: cut, three cleared items present, no Cursor edit needed.

— PC
