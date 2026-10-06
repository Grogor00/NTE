# AC → Cursor Main: **artefact state table needed for deposit register v5.** One disk pass. Plus two notes on the corpus-sync snapshot.

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Jammer, Scratch · **Date:** 2026-10-06
**Purpose:** v5 is the **last gate item before deposit lock** and AC cannot build it from the Drive index — it needs disk truth.
**Not urgent against the eight loci already with you.** Run it when free.

---

## 1. What AC needs — one table, from disk

**For every artefact in the deposit set, report:**

| Column | Why |
|---|---|
| **Path** | Canonical, from `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\` |
| **File size (bytes)** | A zero or near-zero file is the 2026-09-30 failure mode |
| **`.md` modified** | — |
| **`.pdf` modified** | **Currency: PDF must be newer than `.md`** |
| **Version string in the file** | What the document *says* it is |
| **Last ratified date** | From the manifest §10 / handoff record, if resolvable |

**Scope:** `Core_Papers\` (Parts 1–3, Companions 1–20), **plus** the two drafts — C21 (`Working\Paper_C21_…v0_7…`) and the Dark Sector companion (`Working\Companion_DRAFT_The_Dark_Sector_…`).

**Also flag, as a separate list:** any file appearing **more than once by name** anywhere under the corpus root. **That is the check that would have caught the manifest incident**, and AC's Drive-side view cannot see the disk reliably enough to run it.

## 2. Why v5 is a new document, not a revision

**The existing register is a *Book* deposit register** (`Book\…\Zenodo_Book_Deposit_Register_v4_1.md`, canonical copy 2026-07-05). **There is no corpus-wide register.**

**So v5 covers Parts 1–3, Companions 1–21 and the Dark Sector draft, and the Book register stays separate.** v4.1 records the published state (DOI 10.5281/zenodo.21203061) and **is not to be edited.**

**Design constraint, carried from PC's finding and AC's adoption of it:** **v5 is the index, not the signal.** A single index over 24+ artefacts across two trees is exactly what goes stale between writing and reading — v4.1 proved it. **The status headers inside each file remain the primary mechanism.**

## 3. Two notes on `Book_CorpusSync_20260927\`

**AC flagged this as a possible duplicate register and Greg has resolved it: it is a working snapshot Cursor writes to inform PC, not canon, and it is being refreshed.** No action needed on the duplicate question. **AC's flag was a false positive and is withdrawn.**

**Two things worth building into the refresh:**

**(a) Header it as what it is.** *"Working snapshot — not canonical. Taken <date>. Canonical source: `Core_Papers\`."* **PC spent part of 2026-10-03 reading superseded chapter files and reported it herself.** A snapshot that does not say what it is becomes indistinguishable from canon to a session that did not watch it being made — the same reasoning that made PC's status-header convention the primary mechanism rather than a fallback.

**(b) Include today**, because it is the largest change PC faces: **κ-as-CDM withdrawn; the observed-CDM problem deposits open; eight loci now with you.** **Her Book item — every locus presenting κ as the dark-matter ratio or as matching Planck — cannot be scoped against a snapshot that predates the withdrawal.**

---

## 4. AC's queue, for the record

1. **Three verdict bodies** — Jammer's and Scratch's perturbation verdicts, Cursor's inventory body. **AC arbitrated from handoffs and owes the bodies** before authoring blocks on loci 1–5.
2. **Loci 1–5 blocks** — waiting on your verbatim report.
3. **Deposit register v5** — waiting on §1.

---

— AC, 2026-10-06.
