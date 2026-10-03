# Handoff — PC → Greg (Cc AC, Cursor): Appendix C v1.4 patch set

**From:** Claude_PC · **To:** Greg · **Cc:** AC, Cursor · **Date:** 2026-09-24
**Status:** **PROPOSED — not ratified.** Cursor: do not apply until Greg confirms.
**Target:** `G:\My Drive\NTE_ZENODO_CLEAN\Book\Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` (22,633 bytes, unmodified since 2026-09-18) → `Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md`.
**Campaign:** Book bring-up, ship-order position 1.

---

## Scope — smaller than planned, and why

Four items were queued for this pass. **Two are blocked upstream and are flagged rather than written.**

| Item | Status |
|---|---|
| Solar-mixing entry — S3 sharpening | **Write.** A1, A2 below. |
| CFL into C.4 | **Write.** A3. |
| (n_s, r) dual anchors | **HELD.** AC's instruction: flag rather than write anything touching n_s or r, because Companion 17's N_e may move them. A4 fixes register only, with no numbers. |
| M_R | **No change needed.** v1.3 already carries it at *"identified structural pathway … but no closed derivation"*, which is the correct register, and being a popular appendix it cites nothing, so there is no Part 3 mis-attribution to repair. |

Three small patches and two flags. Stating the size plainly rather than padding it.

---

## A1 — C.1, the solar-mixing entry. The S3 sharpening.

This is the substantive change. v1.3 says solar mixing is gated on the σ↔generation dictionary. **S3 (2026-09-23) established that the dictionary is necessary but not sufficient** — it fixes the slot, not the fork. The fork is one free parameter in the μ–τ-odd breaking, with TM1 and TM2 as exact endpoints, and **it is not fixed by the algebra**. AC notes Manifest §3's wording understates the problem for the same reason.

That is a worse result stated more precisely, which is exactly what an open ledger is for.

**OLD**
Solar mixing is now an *open* problem, gated on a piece of structural homework — the dictionary that would connect the framework's own geometric labels to the three generations.

**NEW**
Solar mixing is now an *open* problem, and a 2026 investigation sharpened how open. It was thought to be gated on one piece of structural homework — the dictionary connecting the framework's geometric labels to the three generations. That dictionary turns out to be necessary but not sufficient. It fixes which slot the solar angle lives in; it does not fix the angle. The remaining freedom is a single number in the way the symmetry is broken, with the two candidate mixing patterns sitting at its two endpoints, and **the algebra does not choose between them**. The framework fixes the atmospheric angle and the magnitude of the CP phase, and does not determine the solar angle at all.

---

## A2 — C.2, the matching entry, kept consistent

**OLD**
Solar mixing is a different case since the withdrawal — it is not a matter of correction terms on a value the framework still holds, but of establishing the dictionary between the framework's geometric structure and the three generations. No solar-angle commitment is available until that lands.

**NEW**
Solar mixing is a different case since the withdrawal — it is not a matter of correction terms on a value the framework still holds. Establishing the generation dictionary is necessary, but it would place the angle rather than predict it: a further free parameter in the symmetry breaking remains, and nothing in the algebra pins it. No solar-angle commitment is available, and none will be until that freedom is closed from the geometry rather than fitted to the measurement.

---

## A3 — C.4, insert CFL as a neighbourhood

Shipped into Part 1 Positioning on 2026-07-06, one day after the Book freeze, and the only C.4 neighbourhood currently missing. Register: **convergence, not confirmation.**

**Insert immediately after the paragraph ending** "...Progress and constraints in their programme bear directly on this one, in both directions." **(the CPT-symmetric universe entry), before** "**The exceptional-Jordan and octonionic algebra programme.**"

**NEW**
**Null-hypersurface quantisation.** The closest external relative on the emergent-time axis rather than the cosmological one: a programme in which time appears as a quantum effect on a null surface, and the area form has to be treated as a discrete operator (Ciambelli, Freidel and Leigh, 2024). The resemblance is real and the framework credits it as convergence rather than confirmation — that construction starts on a surface where the light-cone structure already exists, and yields a preferred clock downstream of the moment this framework is trying to describe. The two are stacked layers, not rivals. Which is the more interesting relationship: independent programmes arriving at overlapping structure from different directions is weak evidence that the structure is real, and it is the only kind of evidence available for a claim that makes no post-lock observable.

---

## A4 — C.2, register only. No numbers.

The expansion depth the conditional pair is quoted at is under active review. v1.3 already names the sensitivity and already gives the alternative at 55 e-folds, which was well-placed. One clause records that the question is live, without touching any value.

**OLD**
So the pair is conditional with its inputs stated — no longer "awaiting any derivation at all," not yet zero-parameter.

**NEW**
So the pair is conditional with its inputs stated — no longer "awaiting any derivation at all," not yet zero-parameter. The expansion depth itself is under review at the time of writing, and the reader should expect these two numbers to move before they settle.

---

## Post-apply verification

- `Ciambelli` [1] · `necessary but not sufficient` [1] · `does not determine the solar angle` [1]
- `0.9692` and `0.0053` — **unchanged in count and value.** If either moved, the patch overreached; report it.
- `TM1`, `TM2`, `0.318`, `trimaximal` [0] — the appendix names no mixing pattern, per the S3 constraint.

---

## Flags — not written, for Greg and AC

**F1 — (n_s, r) anchors, held.** v1.3 states the pair with no observational comparison, which reads as more determinate than the register warrants. The fix is Planck 2018 and P-ACT-LB side by side with their σ. **Not written**, per AC's instruction that Companion 17's N_e may move the pair. This remains the appendix's weakest passage and should be the first thing revisited once that ratifies.

**F2 — CLFV amplitude ratio, unverified.** C.4 states that if charged-lepton flavour violation is observed the framework fixes |A(μ→eγ)|²/|A(τ→eγ)|² = tan²θ₂₃. With θ₂₃ = π/4 that ratio is **exactly 1**, which is a sharper and more checkable claim than the formula makes it look. PC has not verified it against Part 3 and is not the lane to. Worth AC confirming before deposit, and worth stating as "equal amplitudes" in the text if it holds, since that is what a reader can actually test.

**F3 — does C21's interface question belong in this appendix?** The unreconciled relation between the conformal reset and the Hartle–Hawking Euclidean section is a genuine open item about two *ratified* pieces of the corpus, not about C21's own speculation. AC has it queued for Manifest §10. Whether the Book's public ledger should also carry it depends on a prior question PC is not going to answer alone: **does the Book mention the conformal reset at all, and at what register?** C21 is [SPECULATIVE and NON-LOADBEARING], and the Book currently says nothing about nucleation. Greg's call, and it may be better handled in the final chapter than in the ledger.

---

## Next

On ratification: Ch 15 (score ↔ ledger sync), which inherits A1 and A2 and must not re-introduce a solar-angle claim. Then Ch 4 with the emergence sweep.

Ch 15 is the tier ledger chapter, so **F1 blocks part of it too** — the scorecard's n_s/r row cannot be finalised while the expansion depth is under review. PC will write the rest and mark that row held.

---

— Claude (PC lane), 2026-09-24.
