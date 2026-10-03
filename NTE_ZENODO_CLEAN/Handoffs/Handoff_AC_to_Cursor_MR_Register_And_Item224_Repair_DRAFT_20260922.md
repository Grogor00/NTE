# Handoff — AC → Cursor: M_R register + "item 22.4" repair (Companions 10, 13; Part 3)

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-22

> ## ⛔ STATUS: DRAFT — DO NOT APPLY
> Awaiting Greg's ratification. AC will file a one-line go-handoff naming this file when ratified. Until then: read, pre-check that every OLD matches exactly once, report any that don't — **but make no edits.**

**Targets:** `Core_Papers\Companion_10_M1_Majorana_v10_19_0.md` (C10-1…5); `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` (P3-1, P3-2); `Core_Papers\Companion_13_Yukawa_Nu2_v10_19_0.md` (C13-2…7).
**Order when ratified:** P3 first (it creates the item C13 will point to), then C13, then C10. C13-2…7 assume `Handoff_AC_to_Cursor_Companion13_Ref4_Repoint_20260922.md` has already been applied.
**Render:** Part 3, Companion 10, Companion 13.
**Nature:** register corrections and pointer repair. **No claim is upgraded.** One open item is *added* to Part 3.

Byte-exact match-or-report. OLD anchors kept short and LaTeX-free where possible.

---

## Part A — Companion 10: M_R register

Part 3 grades M_R *pathway identified, not derived*, with its derivation open. Companion 10 currently (i) says the corpus "derives" M_R, (ii) uses M_R as the benchmark of rigour M₁ matches, and (iii) cites Part 3 for a formula Part 3 does not carry. M₁'s own derivation claims are untouched — §7 already scopes them correctly.

**C10-1 — preamble (italic lead paragraph)**
```
OLD:
at the same level of rigour the corpus uses for the heaviest scale M_R.

NEW:
at the flux-quantisation / tree-BPS register stated in §7.
```

**C10-2 — abstract, the M_R comparison sentence**
```
OLD:
This is the same rigour the corpus uses for the heaviest scale

NEW:
It is distinct from, and not benchmarked against, the heaviest scale
```
And, within the same sentence:
```
OLD:
and the two are distinct, non-competing derivations set by different inputs

NEW:
whose pathway is identified but whose derivation is open (Part 3); the two are non-competing constructions set by different inputs
```
Resulting sentence should read: *"It is distinct from, and not benchmarked against, the heaviest scale M_R = M_Pl^{3/4} v_EW^{1/4} ≈ 8.2 × 10¹⁴ GeV, whose pathway is identified but whose derivation is open (Part 3); the two are non-competing constructions set by different inputs (cosmological H_GB for M₁, electroweak v_EW for M_R)."*

**C10-3 — §1, "derives" → "identifies a pathway"**
```
OLD:
The corpus derives M_R

NEW:
The corpus identifies a pathway to M_R
```

**C10-4 — §1, register sentence appended to the same bullet**
```
OLD:
with v_EW the electroweak input.

NEW:
with v_EW the electroweak input. Part 3 grades this *pathway identified, not derived*; the derivation of M_R is an open item.
```

**C10-5 — §6, "as derived"**
```
OLD:
with M_R as derived,

NEW:
with M_R at its pathway value,
```

**C10-6 — reference 1**
```
OLD:
the heavy Majorana sector (M_R = M_Pl^{3/4} v_EW^{1/4}; Hopf base/fibre weighting) and the leptogenesis sector.

NEW:
the tier placements of M_R (pathway identified, not derived; derivation open) and M₁ (geometric cross-check, O(1) residue), and the leptogenesis sector. The M_R formula itself is stated in §1 above.
```

---

## Part B — Part 3: name the missing open item

Companion 13 cites a "corpus item 22.4" six times as the home of the open finite-Dirac Yukawa normalisation. No file in `Core_Papers\` defines an item 22.4 — it is pre-rebuild master numbering. Part 3's open list names the Yukawa hierarchy but not this narrower, load-bearing item: the 8π-vs-4π Dirac branch on which the solar-leg agreement depends, and whose computation would also fix the sign of δ_J. Adding it makes Part 3's open list complete and gives Companion 13 a real target.

**P3-1 — §XVII "Open (named, not derived)" line**
```
OLD:
the three-generation hypercharge verification through

NEW:
the finite-Dirac Yukawa normalisation (the 8π-vs-4π Dirac branch on which the solar-leg agreement depends; the same computation would fix the sign of $\delta_J$ — Companion 13); the three-generation hypercharge verification through
```

**P3-2 — "Open work" paragraph**
```
OLD:
verify three-generation hypercharges through

NEW:
settle the finite-Dirac Yukawa normalisation (Companion 13; the same computation would fix the sign of $\delta_J$); verify three-generation hypercharges through
```

---

## Part C — Companion 13: retire "item 22.4"

Six occurrences, each patched in context so every sentence still reads. After applying, **grep the file for `22.4` — it must return zero.** Report the count found before patching (expected: six).

**C13-2 — abstract**
```
OLD:
derives no Yukawa magnitude at all (corpus item 22.4)

NEW:
derives no Yukawa magnitude at all (Part 3, open item: finite-Dirac Yukawa normalisation)
```

**C13-3 — §3 closing parenthesis**
```
OLD:
The magnitude is open: corpus item 22.4.

NEW:
The magnitude is open (Part 3, open item: finite-Dirac Yukawa normalisation).
```

**C13-4 — §6, first occurrence**
```
OLD:
would ground any Yukawa magnitude (corpus item 22.4) is the same computation

NEW:
would ground any Yukawa magnitude (Part 3, open item: finite-Dirac Yukawa normalisation) is the same computation
```

**C13-5 — §6, second occurrence (no "corpus" prefix)**
```
OLD:
the finite-Dirac computation of item 22.4

NEW:
the finite-Dirac normalisation computation
```

**C13-6 — §7**
```
OLD:
The magnitude is corpus item 22.4, open.

NEW:
The magnitude is open (Part 3, open item: finite-Dirac Yukawa normalisation).
```

**C13-7 — §7 closing sentence and reference 4 (same string, two occurrences — replace both)**
```
OLD:
(in preparation; corpus item 22.4)

NEW:
(Part 3, open item: finite-Dirac Yukawa normalisation)
```

---

## Part D — manifest §10 (on ratification)

Mark the two watch-items registered by `Handoff_AC_to_Cursor_Companion13_Ref4_Repoint_20260922.md` (M-2) as **CLOSED** with today's date, citing this handoff.

---

## Deliverables (on ratification)

1. All patches applied; per-patch match report.
2. `22.4` grep result on Companion 13 (must be zero).
3. Part 3, Companion 10, Companion 13 re-rendered; PDF newer than `.md` for each.
4. Completion handoff to `Handoffs\`, addressed to AC.

---

— AC, 2026-09-22.
