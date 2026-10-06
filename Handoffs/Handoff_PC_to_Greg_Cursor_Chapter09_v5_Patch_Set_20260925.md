# Handoff — PC → Greg (ratify) → Cursor (apply): Chapter 9 v5 patch set

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-25
**Base file:** `Book\Chapter_09_The_Number_That_Could_Have_Failed_v4.md` (canonical, 42,043 B)
**Target:** `Book\Chapter_09_The_Number_That_Could_Have_Failed_v5.md` — v4 left in place
**Status:** PROPOSED — not ratified

Patch series **T**, flags series **V**.

---

## 0. Headline: Chapter 9 is in better shape than any chapter swept so far

This is the flagship chapter — the framework's one zero-parameter number worked end to end — and PC expected it to carry the campaign's corrections badly. It does not.

It is **A9-clean**: no photon-frame vocabulary, no two-readings refrain, no retired same-event language. It **pre-empts the rest-energy correction** without being asked, stating in §3 that the neutrino's bilateral support holds *"not because its Yukawa coupling is small, although it is, but because the projection that would have confined it to one face never completed."* Its **exactness language already matches §3's register** — "structurally exact at the projection step", "algebraically exact given its inputs" — rather than the "± 0" the snapshot explicitly warns against. And its §8 bimetric paragraph is almost word-for-word consistent with Appendix C's C.2 entry, down to naming the remaining exposure as whether the nonlinear completion could feed back into the averaged sector.

Three small patches, all verified against the corpus. Two flags.

---

## 1. Patches

### T1 — §2: proper time where the relation delivers cosmic time

The one instance of the rule in the chapter.

**OLD**

```
At the gauge birth — the moment the Standard Model gauge symmetries switched on and proper time crystallised — the universe locked into one of two CPN-conjugate orientations of the manifold's N-thickness.
```

**NEW**

```
At the gauge birth — the moment the Standard Model gauge symmetries switched on and cosmic time crystallised — the universe locked into one of two CPN-conjugate orientations of the manifold's N-thickness.
```

---

### T2 — §7: the stated difference does not match the stated significance

The chapter gives the gap as 0.12 and the significance as 0.83σ. Those disagree: 0.12/0.15 is 0.80. The 0.83σ figure is the corpus's and is correct — it comes from the unrounded prediction. κ₀ = 3/√(4π) = 0.84628, so κ = 0.84628/0.15372 = **5.5054**, and 5.5054 − 5.38 = **0.1254**, which over 0.15 gives 0.836σ. The rounded 5.50 in the headline is fine; the *difference* rounds to 0.13, not 0.12.

Small, but it is the arithmetic of the chapter's single load-bearing comparison, and it is the number a hostile reader checks first.

**OLD**

```
Side-by-side. The framework's prediction: κ = 5.50. Planck's measurement: κ = 5.38 ± 0.15. The difference is 0.12, which is about 0.83 standard deviations — well within statistical agreement between the framework's number and the universe's number.
```

**NEW**

```
Side-by-side. The framework's prediction: κ = 5.50. Planck's measurement: κ = 5.38 ± 0.15. The difference is about 0.13 — the unrounded prediction is 5.505 — which is about 0.83 standard deviations, well within statistical agreement between the framework's number and the universe's number.
```

---

### T3 — §9: the other two zero-parameter predictions carry qualifiers the summary drops

Chapter 15 v4 now grades the strictest tier carefully: θ₂₃ is *inherited from the μ–τ symmetry literature and credited*, and δ_J is |δ_J| = π/2 **with the sign free**, so the asymmetry's direction is not claimed. Chapter 9's forward pointer lists all three flat.

This matters more here than it would elsewhere, because Chapter 9 is the chapter whose entire subject is what "zero-parameter" means. A flat list in this chapter reads as three equally unqualified predictions.

**OLD**

```
Chapter 15 catalogues the framework's claims as a whole, each at its graded register — the dark-matter-to-baryon ratio joins the maximal CP phase and the maximal atmospheric angle in the strictest zero-parameter tier, with the spectral index and tensor ratio carried as conditional, the mass scales as cross-checks, and the framework's live tensions listed at full volume alongside.
```

**NEW**

```
Chapter 15 catalogues the framework's claims as a whole, each at its graded register — the dark-matter-to-baryon ratio joins the maximal CP phase and the maximal atmospheric angle in the strictest zero-parameter tier, though the company is worth reading closely: the atmospheric angle is inherited from an established symmetry literature and credited there rather than claimed, and the CP phase is fixed in magnitude only, its sign left free, so the direction of the matter–antimatter asymmetry is not among the framework's predictions. κ is the one of the three that is wholly the framework's own and fixed end to end. Beyond that tier, the spectral index and tensor ratio are carried as conditional, the mass scales as cross-checks, and the framework's live tensions are listed at full volume alongside.
```

---

## 2. Flags

**V1 — §6's "unrelated branch of theoretical physics" needs a citation or needs cutting.** The chapter offers an independent check on the factor of three:

> *"In an unrelated branch of theoretical physics — work on monopole couplings in field theory contexts unrelated to dark matter or cosmology — the same factor of three appears naturally, for the same reason: it counts the dimension of the adjoint representation of SU(2)."*

The chapter is honest about the check's limits in the next sentence — it says explicitly this is not an independent derivation, since the algebraic content is the same. But an unnamed literature doing corroborative work in the framework's flagship derivation is thin, and a reader who wants to follow it up cannot. Either AC supplies the reference, or the sentence should go: dim(adj SU(2)) = 3 is a standard algebraic fact and does not need corroboration from an unnamed source. **PC has not patched it, because cutting a corroboration is a judgement about what the chapter is claiming, not a register fix.** Recommend AC rule.

**V2 — n_s and r are not touched.** Stated for the record against the standing hold. Chapter 9 mentions the pair once, in §9's forward pointer, as tier labels only — *"the spectral index and tensor ratio carried as conditional"*. No value for either appears anywhere in the chapter, and T3 does not add one. If AC's N_e item moves the pair, Chapter 9 needs no repatch.

**V3 — everything else checked out, and PC verified rather than assumed.** κ₀ = 3/√(4π) = 0.84628; κ = 5.5054; the 0.36% bare-coupling adjustment needed to reach 5.38 exactly (κ₀ would have to be 0.84326); the amplification factor 1/(1−κ₀) = 6.5, which the chapter gives as "about six" in both places it appears and which correctly links the 0.36% bare-level gap to the 2.3% headline residual. Planck 5.38 ± 0.15 matches §3. The geometric-series closure and the fixed point T = T_b/(1−κ₀) are algebraically correct as written. No literature currency items beyond the CMB-S4 timeline already in F4.

---

## 3. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ Chapter 9 v5 patch set** (`Handoff_PC_to_Greg_Cursor_Chapter09_v5_Patch_Set_20260925.md`, PC, 2026-09-25) — T1–T3 on `Chapter_09_The_Number_That_Could_Have_Failed_v4.md`. Small pass: the chapter is A9-clean, already pre-empts the rest-energy correction (§3 disclaims the Yukawa reading unprompted), and its exactness language already matches §3's "exact given its structural inputs, not ± 0". T1 cosmic-not-proper time; T2 the §7 arithmetic — stated difference 0.12 disagrees with the stated 0.83σ, corrected to 0.13 with the unrounded 5.505 shown; T3 the strictest-tier summary drops θ₂₃'s inherited-and-credited status and δ_J's free sign. Flags V1 (§6's unnamed "unrelated branch" corroboration needs a citation or cutting — AC to rule), V2 (n_s/r untouched; clear of the hold), V3 (all arithmetic independently verified). **Status: PROPOSED, awaiting Greg.**
```

---

## 4. On ratification

Cursor applies T1–T3 byte-exact, saves as `Chapter_09_The_Number_That_Could_Have_Failed_v5.md`, leaves v4 in place, match-or-report, never force.

Chapter 10's set is filed separately and carries the more serious finding of the two.
