# Handoff — PC → Cursor: the Book's opening arc, four sets ratified, with Ch 3 amendment M10

**From:** PC
**To:** Cursor Main · **Cc:** Greg, AC
**Date:** 2026-09-24
**Greg ratified 2026-09-24, 18:21 NZST** — all four sets, with the Ch 3 amendment folded in and the K1 title question settled.
**Cursor is offline as of the last check; this queues for its return.**

---

## 1. What is now cleared to apply

Eight target files across seven handoffs. All Greg-ratified. Nothing held; AC's standing line on the physics queries is *"Held: nothing of PC's."*

| # | Target | Patches | Source handoff |
|---|---|---|---|
| 1 | `Book\Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md` | A1–A4 | `…AppendixC_v1_4_Patch_Set_20260924.md` |
| 2 | ↑ same file | A5 (CLFV) | `…AppendixC_v1_4_Patch_A5_CLFV_20260924.md` |
| 3 | `Book\Chapter_15_The_Score_v4.md` | B1–B11, **with B3′ and B10′ replacing B3 and B10** | `…Chapter15_v4_Patch_Set…` + `…AC_Response_Revisions…` |
| 4 | `Book\Chapter_04_Time_and_Expansion_v9.md` **(rename)** | C1–C15, **plus C16** | `…Chapter04_v9_Patch_Set…` + `…AC_Response_Revisions…` |
| 5 | `Book\Chapter_05_The_Eighth_Colour_v8.md` | D1–D9, **plus D10, D11** | `…Chapter05_v8_Patch_Set…` + `…AC_Response_Revisions…` |
| 6 | `Book\Chapter_02_Entanglement_as_Geometry_v8.md` | E1–E6 | `…Chapter02_v8_Patch_Set…` |
| 7 | `Book\Chapter_01_The_Photons_Journey_v11.md` | F1–F9 | `…Chapter01_v11_and_Prelude_v8…` |
| 8 | `Book\Prelude_The_Forty_Million_Year_Instant_v8.md` | P1–P2 | ↑ same |
| 9 | `Book\Chapter_03_A_Closed_Universe_v7.md` | M1–M9, **plus M10 below** | `…Chapter03_v7_Patch_Set…` + this file |

**Three ordering rules.**

1. **Chapter 15: apply B3′ and B10′, not B3 and B10.** Both versions carry the same OLD blocks. Applying both would fail the second match and should be reported, but do not rely on that — take the primed versions from `Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md`.
2. **Chapter 4 is renamed as well as patched.** C1 changes the title line; the file becomes `Chapter_04_Time_and_Expansion_v9.md`. Ch 3's M7 changes the forward pointer to match, so **apply both or neither** — a half-applied retitle leaves the Book internally inconsistent in a way a reader would hit.
3. **Every predecessor version stays in place.** v10, v7, v6.1 and the rest are kept for audit, as with Ch 1 v9.

AC's two corpus handoffs (`…Omega_k_Register_And_TGB_Flag_RATIFIED…`, then `…Falsifiability_Item11_Curvature_Sign_RATIFIED…`, in that order) are independent of these and carry their own ordering constraint.

---

## 2. K1 settled — the repetition stays

`Time and Expansion` remains both Chapter 1's section heading (patch F2) and Chapter 4's chapter title (patch C1). Greg's call, 18:21. **No change to either patch.** The alternative heading offered in F2's patch note is not taken; ignore it.

---

## 3. M10 — Chapter 3 amendment

Additional patch to the Ch 3 v7 set, target `Book\Chapter_03_A_Closed_Universe_v6_1.md`.

### Why this patch exists

When M1–M9 were written, flag N1 was open and PC deliberately left the flatness argument's substance alone. AC has since read Part 3, Greg has ratified the Ω_k correction into Part 3 and Part 1, and a new falsifiability item 11 has been ratified into Part 3's register. Chapter 3 is where that material lives pedagogically — AC's note says so — and the chapter's existing paragraph on the curvature commitment now needs three things it did not need this morning.

**And it contains an overstatement that the new item 11 makes visible.** Ch 3 v6.1 says a detected closed curvature *"at any level, would be dramatic support"*. It would not. Every closed cosmology predicts the same sign, so a confirmed Ω_k < 0 would be consistent with NTE and would distinguish it from nothing. AC's item 11 is explicit that the falsifier is **one-sided** and **not NTE-distinguishing**, and warns against presenting it as a new prediction. The chapter is currently claiming the upside that item 11 declines. That is the §8 failure mode again, and it is worth noting that the corpus correction caught a Book overclaim rather than the other way round.

The honest framing, in AC's words, is *"here is what would prove us wrong, and we may never get to find out"* — which is a better note for the section than a falsifier that is merely hard.

### Patch M10

**OLD**

```
The framework's first sharp distinguishing empirical commitment — the dark-matter ratio κ — comes later. What flatness gives us here is consistency plus one standing one-way commitment. Consistency: the closed S³ picture is the structure the framework needs, and observation does not refute it — though near-perfect flatness is also what the standard picture expects, so agreement here distinguishes nothing. The commitment: the closure's *sign* is staked. If precision cosmology ever measured spatial curvature of the open kind — a genuinely negative curvature at any confidence — the framework's closed geometry would break outright, with no adjustment available; while a detected closed curvature, at any level, would be dramatic support. The framework does not expect either detection soon, and says so; but the sign is on the record.
```

**NEW**

```
The framework's first sharp distinguishing empirical commitment — the dark-matter ratio κ — comes later. What flatness gives us here is consistency plus one standing commitment, and the commitment is worth stating carefully, because it is smaller than it first looks and more honest for being so.

Consistency first: the closed S³ picture is the structure the framework needs, and observation does not refute it. Near-perfect flatness is also what the standard picture expects, so agreement here distinguishes nothing at all.

The commitment is the closure's *sign*. A closed three-sphere of finite radius cannot be exactly flat — exact flatness is a different geometry, and it is the one the framework's whole surface ontology rules out. So the framework is committed to spatial curvature of the closed kind: not zero, and not open. If precision cosmology ever established an open universe at significance, the framework would break outright, and not at the level of one derivation — there is no closed-S³ reading of an open universe, so the ontology itself would go. Current data sit comfortably inside the consistent range and impose no tension.

Three things keep this from being more than it is, and the framework states all three rather than the first. The falsifier is one-sided: confirming the closed sign would not confirm the framework, because every closed cosmology predicts exactly the same thing. It is not a distinguishing test, and it does not join the handful of measurements on which the framework's case actually rests. And it predicts the sign but not the magnitude — the long e-fold run drives the curvature toward values plausibly far below anything an instrument will reach, and curvature measurements are in any case entangled with the dark-energy sector, so the number may stay out of range indefinitely.

Which leaves the commitment in an unusual position, and an instructive one. Here is a thing that would prove the framework wrong, recorded on the understanding that we may never get to find out. A framework should say what would refute it even where refutation is unlikely to be reachable — especially there, because that is where the temptation to stay quiet is strongest.
```

---

## 4. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ opening arc — four sets ratified 2026-09-24, 18:21 NZST** (`Handoff_PC_to_Cursor_Book_Opening_Arc_Four_Sets_RATIFIED_20260924.md`, PC). Clears Ch 1 v11 (F1–F9), Prelude v8 (P1–P2), Ch 2 v8 (E1–E6), Ch 5 v8 (D1–D11) and Ch 3 v7 (M1–M10) for Cursor, alongside the already-ratified Appendix C v1.4 (A1–A5), Ch 15 v4 (B1–B11 with B3′/B10′) and Ch 4 v9 (C1–C16, renamed to `Chapter_04_Time_and_Expansion_v9.md`). **K1 settled: "Time and Expansion" stays as both Ch 1's section heading and Ch 4's chapter title.** **M10 added to Ch 3** — carries the ratified Ω_k → 0 reading and falsifiability item 11 into the Book at AC's warned register, and removes a Book overclaim the corpus correction exposed (v6.1 said a detected closed curvature "would be dramatic support"; item 11 is one-sided and not NTE-distinguishing). Ch 4's rename and Ch 3's M7 forward pointer must be applied together or not at all.
```

---

## 5. What this completes, and what it does not

**Completes:** the Book's opening arc — Prelude and Chapters 1 through 5 — plus both ledger documents, Chapter 15 and Appendix C. Every one of them now carries the A9 corrections, the emergence register, the cosmic-time distinction, and registers matching the corpus as AC has verified it today.

**Does not touch, and has never been touched by any pass:** **Chapters 6 through 14**, the **popular editions**, and **Appendix A**. That is the larger half of the Book by volume and it is entirely unswept.

**The next move there should be mechanical, not chapter-by-chapter.** Four rules now have settled replacements and are findable by search rather than by judgement: the photon-frame vocabulary, the "two readings / both vantages" refrain (which Ch 3 proved survives outside Ch 1 — flag N3), "proper time" where the relation delivers cosmic time, and Higgs-coupling-as-embedding-depth. PC recommends specifying those as one Cursor sweep across Chapters 6–14 and both popular editions, returning a located-instances report rather than applying blind — PC then writes patches only for the instances where the replacement needs judgement. That converts nine chapters of reading into one report plus a short patch set, and Appendix A follows from the Reader edition afterwards.

PC will write that specification on Greg's word.

---

— PC, 2026-09-24.
