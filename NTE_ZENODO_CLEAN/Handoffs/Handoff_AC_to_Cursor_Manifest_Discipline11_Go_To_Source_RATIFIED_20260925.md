# Handoff — AC → Cursor: Manifest §6 discipline 11 (Greg-ratified) + read-state ledger

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-25
**Greg ratified 2026-09-25, 19:51 NZST.**
**Target:** `NTE_Workflow_Manifest_v10_18.md` §6 and §10.
**Ordering:** apply after any outstanding §6 patch. If discipline 10 is absent, report and stop — 11 anchors on it.

Byte-exact match-or-report.

---

## MF-D11 — Manifest §6, new discipline 11

```
OLD:
10. **A draft that is not registered does not exist.**

NEW:
10. **A draft that is not registered does not exist.**
11. **Go to the source. Name the file before you rule.** Before any stream issues a verdict, or AC arbitrates a corpus question, it must (a) name the deposited file(s) that would settle the question, and (b) confirm it has read them in full **in the current session**. If it cannot name a file, the question is not yet well-posed. If it can name one but has not read it this session, it reads it or it does not rule. **Recollection is not a source.** A recalled claim about corpus content is indistinguishable, from the inside, from a reconstruction — so the trigger for re-reading is the *type* of claim, never the degree of confidence. Four triggers, all mandatory regardless of certainty: stating what a corpus file says; issuing a negative finding; issuing a ruling; accepting another stream's finding. **A negative finding — "the corpus does not say X" — must list the files read and the search terms used, and justify why that set is exhaustive.** **Every verdict must state which corpus files it read in full and which it did not.** Where a claim about corpus content is stated without a current-session read, the sentence itself must say so. (Causes: the 2026-09-24 P4 "undefined by deposit" verdict, answered all along by Part 2 §8.5–8.6 and §IX, arbitrated by AC without having read Part 2; and the G8 render-lane report, which searched the top-level `paper-build\` and missed `Book\paper-build\`.)
```

*(Discipline 10's line continues past the text shown; insert after the whole of item 10.)*

---

## MF-D11R — Manifest §10 registration

```
- **RATIFIED 2026-09-25 — discipline 11 (go to the source).** Adopted after AC arbitrated the P4 definitional questions without having read Part 2 in full, passing through a verdict of "undefined by deposit" that Part 2 §8.5–8.6 and §IX already answered. Root cause: AC referencing volatile session context in place of canonical source, against standing instruction. Mitigations: discipline 11 above; `Working\AC_Read_State_Ledger.md`; spine-first session start (Parts 1–3 read in full before any arbitration); every stream verdict states its read set.
```

---

## Note for all streams

Discipline 11 binds **every** lane, not AC alone. From now on a verdict without a read set is incomplete and AC will return it. This is not a reflection on any lane's work — Jammer's P4 computation was sound and its conclusion followed from what it had; what was missing was the statement of what it had.

---

— AC, 2026-09-25.
