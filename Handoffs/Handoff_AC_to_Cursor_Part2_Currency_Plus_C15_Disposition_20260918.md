# Handoff — AC → Cursor: Part 2 currency fixes + C15 disposition

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-18
**Status:** READY TO APPLY. All items Greg-ratified 2026-09-18.
**Targets:** `Core_Papers/NTE_v10_19_0_Part2_Structure.md` (P2-1, P2-2); `NTE_Workflow_Manifest_v10_18.md` (M4, M5).
**Render:** Part 2 only, after P2-1/P2-2.

**ORDERING:** apply **after** `Handoff_AC_to_Cursor_Part1_Clarification_Set_Plus_Manifest_20260918.md`. M5 edits the line that handoff's M3 creates. If handoff 1 has not run, stop and report rather than applying M5.

Byte-exact match-or-report throughout. Do not force, fuzzy-match, or normalise whitespace.

---

## Part 2 — patch P2-1 (header date)

```
OLD: date: "2026-06 (NTE Corpus v10.19.0)"
NEW: date: "2026-09 (NTE Corpus v10.19.0)"
```

## Part 2 — patch P2-2 (trailer currency)

Ratified reading: the trailer is a **currency** statement, not provenance. "Faithful to v10.17.7" reads present-tense to an external reader and is now false — v10.17.7 predates the JUNO θ₁₂ withdrawal. Part 1 was corrected the same way. Part 3's trailer says "condensed **from** canonical v10.17.7", which is provenance and stays as written.

Minimal OLD deliberately — the surrounding trailer is long and this short string is unique in the file.

```
OLD: physics faithful to canonical v10.17.7
NEW: physics current to canonical v10.19.0
```

---

## Manifest — patch M4 (§10, Companion 15 cross-reference disposition)

**DECLINED by Greg, 2026-09-18.** Recorded so it does not resurface a third time. Insert the closed item immediately before the existing `**In progress:**` heading.

```
OLD:
**In progress:**

NEW:
**Declined 2026-09-18 (do not re-propose without Greg):**
- **Companion 15 cross-reference in C13 §6** — proposed in `Handoff_Cursor_to_AC_C13_Section6_Applied_20260803.md` (Step 2): a one-clause link from the free δ_J sign to Companion 15's open E(Φ)/K(Φ) framing, on the grounds that both are "free spectral data". **Declined.** That is a shared *register*, not a shared structure — a within-sector CP-parity and an open kinetic normalisation. Asserting the link implies a common origin nothing derives, which is the failure mode that produced the retired six-note chord framing (§II.0: a modification that re-describes without simplifying or predicting fails the test; Companion 12: "coherence, not tally").

**In progress:**
```

## Manifest — patch M5 (Last updated line — absorb this run)

OLD below is the text handoff 1's M3 introduces. If it does not match, handoff 1 has not yet run — stop and report.

```
OLD:
**Last updated.** 2026-09-18 — rev 10.5. Part 1 clarification set (lapse / velocity dilation; four-velocity and the two uses of c; null-time as reparameterisation freedom; θ₁₂ currency; trailer and header date). §3 μ–τ reflection θ₁₃ correction (Greg-ratified). κ-appendix watch-item closed — verified applied. Prior: rev 10.4 (2026-08-09) deposit set unify to **v10.19.0**.

NEW:
**Last updated.** 2026-09-18 — rev 10.5. Part 1 clarification set (lapse / velocity dilation; four-velocity and the two uses of c; null-time as reparameterisation freedom; θ₁₂ currency; trailer and header date) and matching Part 2 currency fixes (header date; trailer). §3 μ–τ reflection θ₁₃ correction (Greg-ratified). κ-appendix watch-item closed — verified applied. Companion 15 cross-reference declined. Standing convention: a clean-rebuild trailer is a **currency** statement ("physics current to …"), except Part 3's "condensed from", which is provenance. Prior: rev 10.4 (2026-08-09) deposit set unify to **v10.19.0**.
```

---

## Notes for Cursor

- Part 2's content was last genuinely edited 2026-09-05 (REPAIR 2, §X magnitude bars); §XII carries 2026-08 forward-modelling. The `2026-06` header understated currency by a quarter.
- Today's bulk mtime refresh across the tree remains a Drive sync touch, not content.
- Part 3 needs no trailer change under the ratified reading.

---

— AC, 2026-09-18.
