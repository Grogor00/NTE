# NTE Book — Title & Pratchett Discipline v0.1

**Status:** Greg-ratified 2026-05-26 (stabilisation)  
**Book title (canonical):** **The Shape of Time**  
**Custodian:** PC (chapters); AC (ledger + Drive canonical); Cursor (local patch blocks / templates)

---

## §1. Chapter header template (all chapters + Prelude)

Every file in `Book/` should open with this block (adjust chapter number/title only):

```markdown
# The Shape of Time

## Chapter N — [Chapter subtitle]

*Non-Temporal Emergence (NTE): the Null-Time Extension to the Standard Model*

G. White

---

[Optional epigraph — one Pratchett quote per chapter maximum; see §3]

---

[Chapter body begins]
```

**Prelude** uses `## Prelude` instead of `Chapter N`.

**Rules:**
- **The Shape of Time** = book title on **every** chapter (and Prelude).
- NTE identity sentence once in front matter (per `NTE_Acronym_Naming_Discipline_v0_1_20260526.md`).
- Do **not** use "Null-Time Extension" alone as the book title.

---

## §2. Integration queue (Drive — PC pass)

| Ch | Ledger version | Action |
|----|----------------|--------|
| Prelude | v4 | Add book title block |
| 1–6 | v7.3 … v5.2 (+ v5.3 patch) | Add book title block |
| 7–10 | various | Add book title block |
| 11–16 | v3.1 … v1 / v4 (Ch 13) | Add book title block |

**Ledger note:** `Workflow/MB/NTE_Chapter_State_Ledger` is stale on Ch 6 v5.3 / Ch 13 v4 — reconcile on PC pickup.

---

## §3. Pratchett inventory (corpus audit from handoffs + audits)

**Policy:** At most **one** Pratchett epigraph per chapter. Body references sparingly; no duplicate *same* line in adjacent paragraphs unless deliberate echo (flag for Greg).

| Ch | Source / status | Quote or theme | Suitability | Verify source |
|----|-----------------|----------------|-------------|---------------|
| **1** | §A Note on Method (body) | *"Reality is whatever doesn't go away when you stop believing in it"* (attributed Pratchett) | **Strong** — empirical-honesty beat; compress §A if stacked with other Pratchett | Often attributed to Pratchett; **exact book/line unverified** |
| **3** | Epigraph v3.3 | *"Great A'Tuin… stares fixedly at the Destination. No one knows what the Destination is."* | **Strong** — closed-universe / unknowable-future metaphor; expanded for non-fans | **Working paraphrase** — not verbatim TP; Greg verify |
| **4** | §Pratchett / arrow-of-time block (~lines 94–108 in v3/v7) | *Thief of Time*: *"everything that happens, stays happened"* (Death) | **Strong** — geometric past vs block-universe; distinguished from strong eternalism in prose | Verify *Thief of Time* wording |
| **5** | Epigraph (held) | *"There were, of course, eight colours in the Discworld; the eighth being octarine…"* | **Strong** — eighth-colour chapter conceit | Standard *Colour of Magic* territory — verify edition |
| **7** | Epigraph + body close | *"In the beginning, there was nothing, which exploded."* | **Strong** — gauge-birth / Big Bang rhetoric | **Verified** — *Lords and Ladies* (Discworld #14, 1992); Greg 2026-05-26. Extended in novel: *"Much human ingenuity has gone into finding the ultimate Before. The current state of knowledge can be summarized thus: In the beginning there was nothing, which exploded."* — optional footnote only; epigraph keeps short line |
| **9** | Epigraph + §9 close | Same family: *"Reality is whatever doesn't go away…"* echoed at close with κ / Planck | **Strong** — deliberate head/tail echo **within chapter** | Same verification as Ch 1 |
| **10** | Epigraph | *"Universes spill into other universes, casual and indifferent"* — *trousers of time* chapter | **Strong** — bilateral / other-orientation; **not** the Ch 7 Big Bang gag | Same novel (*Lords and Ladies*); **exact wording still to verify** against text |
| **12** | Closing (v1/v3) | *Hogfather*: Death on believing in things that aren't true | **Strong** for closing posture | Verify exact Death monologue |
| **12** | Closing echo (CR) | *"everything that happens, geometrically, stays happened"* | **Bookend with Ch 4** — intentional frame completion, not error | Do not place adjacent to Ch 4 quote in same chapter |
| **13** | Epigraph | **Empty** (v1–v4) — slot TBD | Silence / Λ theme appropriate | Still open |
| **15** | Epigraph (subtitle) | *"Million-to-one chances crop up nine times out of ten"* | **Strong** for predictions / falsifiers chapter | **Discworld trope** — verify source novel |
| **16** | (per audit) | Possible *Hogfather* / closing posture | TBC on Drive read | — |
| **Popular** | §Arrow of Time (body) | Same *Thief of Time* / *everything that happens, stays happened* | **OK** for popular paper; **duplicates Ch 4 theme** — acceptable cross-format if Ch 4 is canonical book version | Same as Ch 4 |

**Not Pratchett:** Popular v6 *Thief of Time* paragraph is **in-body analogy**, not an epigraph.

---

## §4. Duplicate / “twice in a row” findings

### A. Likely Greg flag: **same quote twice in one chapter**

| Location | Issue | Recommendation |
|----------|--------|----------------|
| **Ch 9** | Epigraph + §9 closing both use *"reality doesn't go away…"* | **Deliberate echo** per AC audit — keep **one** phrasing; ensure closing is **paraphrase echo**, not copy-paste duplicate paragraph |
| **Ch 1 §A** | Pratchett + dense Heisenberg/Feynman stack | Not duplicate quote; **crowding** — Option B compression (AC/PC queued) |

### B. **Adjacent duplicate risk (Ch 3 epigraph expansion)**

When v3.2 → v3.3 shipped, short line was *"He stares fixedly at the Destination"* and long line added A'Tuin context. **Drive-verify Ch 3 v5:** if **both** short and long epigraph survived, that is **duplicate text in a row** — **delete the short fragment**, keep v3.3 block only.

### C. **Cross-chapter repetition (intentional bookends)**

| Quote family | Chapters | Verdict |
|--------------|----------|---------|
| *everything that happens… stays happened* | **Ch 4** (body) + **Ch 12/16** closing echo + **Popular** | **Intentional** book frame — OK if reader has chapters between; **avoid** placing both in **consecutive** chapters without narrative distance |
| *reality doesn't go away* | **Ch 1** + **Ch 9** | **Different jobs** — method vs κ empirical close — OK if wording differs slightly |
| *nothing… exploded* | **Ch 7** only (epigraph) | **Ch 10** uses different *Lords and Ladies* material (*trousers of time* / universes spill) — **no cross-chapter duplicate** of explosion gag |

### D. **Not found in local corpus**

No local `Book/Chapter_*.md` full prose to grep for adjacent duplicate lines. **PC: run Drive fullText** on `Book/` for:

- `stares fixedly at the Destination` (count occurrences per file)
- `everything that happens`
- `doesn't go away when you stop believing`
- `eight colours in the Discworld`
- `million-to-one`

---

## §5. Suitability rubric (Greg editorial)

| Grade | Meaning |
|-------|---------|
| **Keep** | Metaphor matches chapter geometry/time thesis; lay-reader can get it without footnotes |
| **Keep + verify** | Right idea; exact words need TP source check |
| **Revise** | Right author, wrong passage, or over-long Discworld setup |
| **Replace** | Duplicate of another chapter's epigraph within 3 chapters |
| **Drop** | Epigraph adds tone only; chapter already long (Ch 1 §A case) |

---

## §6. PC patch checklist (one session)

1. Apply §1 header template to all `Book/Chapter_*` + Prelude on Drive.
2. Run §4D grep; fix Ch 3 if double epigraph.
3. Ch 9: confirm head/tail are echo not paste duplicate.
4. Ch 7 vs Ch 10: dedupe Big Bang quote if identical.
5. Ch 13: choose epigraph or ship without (Greg call).
6. Update Chapter State Ledger + note book title in Manifest.

---

## §7. Greg decisions queued

| # | Decision |
|---|----------|
| 1 | Confirm **The Shape of Time** on every chapter header (yes per 2026-05-26) |
| 2 | Ch 3: confirm single A'Tuin epigraph on Drive |
| 3 | Ch 9 head/tail echo: keep vs shorten closing |
| 4 | Ch 4 ↔ Ch 12 *Thief of Time* bookend: keep distance vs reword one |
| 5 | Ch 13 Pratchett: fill slot or none |

— Cursor 2026-05-26. Local `Book/` has only Ch 6 patch block; **Drive pass required** for full apply.
