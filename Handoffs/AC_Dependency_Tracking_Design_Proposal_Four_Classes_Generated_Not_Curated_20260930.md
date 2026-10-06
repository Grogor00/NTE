# AC → Greg: **dependency tracking — design proposal.** Four failure classes, not one. And the map must be generated, never curated.

**From:** AC (Claude) · **To:** Greg · **Cc:** Cursor Main, PC, Scratch, Jammer · **Date:** 2026-09-30
**Origin:** Greg, 2026-09-30 — *"perhaps we need a complete map of dependencies… we are constantly discovering and rediscovering dependency issues."*
**Status: proposal. Nothing built.**

---

## 0. The diagnosis is right. One refinement before design.

**Ten failures this month look like one problem and are four.** Building a single "dependency map" would address one of them well and the others badly.

| Class | What it is | Evidence this month | Fix |
|---|---|---|---|
| **A — Phantom pointers** | X cites Y §Z for a claim Y §Z does not contain | C13 ref 4 → Part 3 (M_R formula never there); C6 §6 → C5 (closure lives in Part 2 §IX); C21 §6 → Part 2 §8.4.1 (**no such subsection**) | **Mechanical verification.** Already commissioned. |
| **B — Shared-object breakage** | X uses an object owned elsewhere; the object changes; X breaks silently | **C15 printing the Door A Lagrangian as "load-bearing today"**; C11's unimodular vs Door B's formulation; Door B cite drift in C8/C12/C15/C17; `N_e` used for two quantities | **Object registry + generated graph.** |
| **C — Tier desynchronisation** | A claim's *register* changes in one file and not others | **Part 1's abstract publishing withdrawn (n_s, r) while Part 3 said WITHDRAWN**; Part 3's Ω_k derived entry contradicting its own open-sector entry; C17's body lagging its own banner; C14/C16 "conditional" for withdrawn | **Claims ledger.** The most damaging class. |
| **D — Patch-induced local contradiction** | A correct patch contradicts adjacent untouched text | **§2.1: "not the lapse" applied next to "it is a lapse"**, with a dangling *"the Schwarzschild recovery above"* | **Apply-time adjacent-context report.** |

---

## 1. **The critical design constraint: generated, not curated**

**Every hand-maintained index in this corpus has gone stale and then been wrong in a way that cost real work:**

- **Manifest §3** — wrong three times (T_GB graded derived *and* conditional; Ω_k grading; folder IDs).
- **Manifest §4** — its folder IDs all resolved into the `My Laptop` duplicate.
- **`Zenodo_Book_Deposit_Register_v4_1.md`** — unchanged since 2026-07-05, known-wrong, and **the filename is currently the only working status signal.**
- **AC's own read-state ledger** — AC reported it updated when only the prose had been written.

**A dependency map maintained by hand would join that list within a fortnight**, and would then be worse than nothing, because people would trust it.

**So: the map is generated from the files, on every apply, and never edited directly.** If it is wrong, the files are wrong — which is the property we want.

**PC's status-header insight generalises here:** *a signal that travels with the file beats an index that must be looked up.* The source of truth lives in each paper; the graph is a view over it.

---

## 2. Proposed design — three artifacts, cheapest first

### **(i) Per-file header block** — the source of truth, in each paper

Extending the status header PC proposed and AC adopted. Machine-readable, in every `Core_Papers\` file:

```
<!-- NTE-DEPS v1
owns: kappa_0, kappa_closure, DM_baryon_ratio
uses: Phi_identity@Part1, gravitational_formulation@C11, S3_surface_only@Part2
claims:
  - id: kappa_5p50        tier: derived      basis: Part2#IX
  - id: sigma_M_minus_half tier: cross-check basis: Part2#IX
refs: Part2#IX, C07#4, C12#3
-->
```

**Three fields do the work:** `owns` (objects this file defines), `uses` (objects it depends on, with owner), `claims` (with tier).

### **(ii) Generated graph + checks** — Cursor, on every apply

From the headers alone, four automatic checks:

1. **Orphan check** — every `uses` resolves to a live `owns`. *Would have caught C15's μ(N) and eq. (1) the day Door B landed.*
2. **Tier consistency** — one `id` cannot hold two tiers across files. *Would have caught Part 1's abstract versus Part 3, and C17's body versus banner, immediately.*
3. **Blast radius** — given a file about to change, list every file whose `uses` names an object it `owns`. **This is the artifact Greg is actually asking for**, and it is a query, not a document.
4. **Pointer verification** — every `refs` target exists. *Would have caught all three phantom pointers.*

### **(iii) Apply-time adjacent-context report** — Cursor, per patch

For each applied patch, report **the paragraph before and after** the changed text. **Costs nothing and catches class D**, which is the one no graph can see.

---

## 3. What this will not fix — stated so it is not oversold

**It will not catch the §XVI failure.** AC read Part 2 in full twice and read past the parenthetical scoping the surface-only axiom, because AC was not asking that question. **No dependency graph catches an unasked question against text already read.**

**It will not catch genuine physics tension** — the junction density, the P-ACT anchor, the reheating gap. Those are findings, not bookkeeping.

**It will not remove the need to read.** It tells you *what to re-read when something changes*. That is a large gain and it is not the same as knowing.

**Honest estimate: it would have caught six of this month's ten failures outright, and shortened two more.** The C15 Door A remnant — the worst — would have been flagged automatically the moment Companion 9 was rewritten.

---

## 4. Sequencing — and AC's recommendation on timing

**Do not build this before the deposit.**

The deposit gate is close and the remaining items are verification. Adding header blocks to 23 papers is a corpus-wide edit that would itself need verifying — introducing exactly the class of churn the proposal exists to prevent, at the moment of least slack.

**Recommended order:**
1. **Finish the gate and deposit** (C12, the formulation ruling, the registers, v5).
2. **Then build headers** as the first post-deposit task, against a frozen, known-good corpus — which is also the ideal baseline, since a generated graph is only as good as the state it first indexes.
3. **Regenerate on every apply thereafter.**

**One thing worth doing now, at near-zero cost:** the **apply-time adjacent-context report** (iii). It needs no headers, catches class D, and can start on the next patch.

---

## 5. Why this is worth doing at all

The corpus is 23 deposited papers plus two drafts, with a spine that touches nearly all of them. **The rework this month was not caused by bad work — most of the findings came from lanes doing exactly what they were asked.** It was caused by **change propagation being discovered by reading rather than by construction.**

**Greg's framing is right: the system should be evaluable as a whole every time any part of it alters.** The proposal above is the cheapest form of that which does not itself become another stale index.

---

— AC, 2026-09-30.
