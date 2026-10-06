# AC → Greg (ratify) + Cursor (execute): **the version-string and status-header pass.** Deposit blocker 1. One pass over 23 artefacts.

**From:** AC (Claude) · **To:** Greg (ratification), Cursor Main (execution) · **Cc:** PC, Jammer, Scratch · **Date:** 2026-10-06
**Addresses:** `Handoffs\NTE_Corpus_Deposit_Register_v5_DRAFT_AC_20261006.md` blocker 1.
**Status: DRAFT specification. Nothing patched.**

---

## 1. The defect

**What the files say about themselves is roughly four months behind what they contain.**

Nearly every Companion stamps itself **"2026-06 (v10.19.0)"**. **Companion 11** says June while carrying its 2026-09-30 regrade to *adopted*. **Companion 12** says June while carrying 2026-10-03 patches. **Part 3** says *"2026-08-03 … Session 2026-08 edit manifest applied"* while carrying today's locus 5. Only **Companions 9 and 17** carry anything current.

**For a Zenodo deposit this is not cosmetic: the version string is what a reader cites.** A paper stamped June 2026 containing an October 2026 withdrawal misrepresents itself to anyone who reads it.

## 2. **The status header — format, fixed here so it is uniform**

**PC proposed this convention; AC adopted it on 2026-09-29 as the primary status mechanism, with the register as index only.** It has not yet been given a single format. **This is it.**

**Inserted immediately after the title line of every `Core_Papers\` artefact:**

```
> **Status.** Corpus v10.19.0 · last ratified change <YYYY-MM-DD> · <one line: what that change was>
> Canonical source: `Core_Papers\`. Open items affecting this paper: <list, or "none">.
```

**Three properties that make it work, and they are the point:**
- **It travels with the file** — survives folder moves, sync packs, snapshot copies.
- **It cannot be read without being seen** — unlike an index someone must think to consult.
- **It names open items**, so a reader meets the caveats before the content, not after.

**Where a paper carries a regrade or withdrawal, the status line says so.** Companion 17 already demonstrates the pattern with *"REGRADED 2026-09-26 Door B"*.

## 3. Execution — one pass, 23 artefacts

**Cursor:** for each `Core_Papers\` artefact,

1. **Update the version line** to a single corpus version and date. **AC proposes the version stays `v10.19.0`** — the physics version has not incremented — **and the date becomes that artefact's last ratified change.** Greg rules if he wants a version bump instead.
2. **Insert the §2 status header** after the title.
3. **Report the before/after version line** for each, so AC can check none was silently wrong.

**Ratified-change dates: take from §5 of the v5 draft.** For the ten artefacts with **no ratified change this campaign** — Companions 1–4, 7, 10, 13, 18–20 — the status line reads *"last ratified change: pre-campaign; read and found clean <date of AC's read>"*. **Do not invent a date.**

**Open-items field, from the v5 draft §4:**
- **Part 2, Part 3, Companion 5** — observed-CDM open; κ's referent open.
- **Part 1, Part 3, Companions 8, 9, 12, 17** — cosmological origin sector open.
- **Companion 11** — adopted-not-derived; CCM grounding not shown for NTE's algebra; Jiroušek condition.
- **Companions 6, 7** — κ's closure rests on the bilateral action, whose completion is open.
- **Companion 15** — Door A action historical; §6.1 and §6.3 stand.
- **Companion 13** — M_R pathway not derived; Yukawa 8π/4π branch.
- **Part 1** — §VII locking criterion never recomputed under Door B.

**Where AC's list is wrong or incomplete for a given paper, report rather than guess.**

## 4. Two cautions

**(a) This pass touches every deposit artefact.** It is the largest single edit the corpus has taken. **Verify-then-report (discipline 13) applies in full**, and AC wants the before/after report before the PDFs are re-rendered — a bad header is cheap to fix in `.md` and expensive after a 23-file render.

**(b) Do not let the header replace the content fixes it describes.** A status line saying *"observed-CDM open"* on a paper whose body still asserts κ as the dark-matter ratio is **worse than no header** — it signals the problem is handled when it is not. **Loci 1–4 must be applied before or with this pass, not after.**

## 5. Sequencing against the other blockers

**Blocker 2 (loci 1–4) goes first or together** — per 4(b).
**This pass second.**
**Blocker 4 (Cursor's five mechanicals) can run in parallel.**
**Blocker 3 (C21 and Dark Sector integration) is independent and gated on Greg and PC.**

---

## 6. Note on the encoding artefact in the state table

Cursor's artefact table renders em-dashes as `â€”` in the version-string column. **AC's standing rule applies — this is a report-side observation and unconfirmed until checked on disk.** Worth one check during this pass, since the pass rewrites those exact lines: **if the mojibake is in the files, this is the opportunity to fix it; if it is in the report only, say so and AC stops flagging it.**

---

— AC, 2026-10-06.
