# Handoff — AC → Scratch, Jammer: C21 seed-as-boundary-data — research directive

**From:** AC (Claude) · **To:** Scratch, Jammer · **Cc:** Greg, PC, Cursor · **Date:** 2026-09-24
**Origin:** Greg, 2026-09-24 — directive to flesh out the physics of the seed-as-S³-boundary-data reading and find what, if anything, is testable.
**Register: speculation throughout. Nothing here is a claim.** The purpose is to find out whether the reading has computable consequences or is only a picture. **A verdict of "no testable content" is a result and should be returned as one.**

---

## The reading being developed

Not "the seed photon is the Euclidean section" — that is blocked by Part 1 §III (null-time is null *from* time, not existence in its absence) and by Euclidean signature admitting no null vectors at all.

Instead: **the seed is data on the S³ boundary at the signature change.** The daughter's Euclidean section need not contain a photon; it needs a boundary condition, and a null object of zero embedding depth is the kind of thing a boundary can carry. This is coherent with NTE's boundary-only architecture rather than bolted onto it.

**The sharpening that makes it computable.** C21 has the seed at wavelength λ ∼ R_H, and the conformal map carries R_H to ℓ_P. S³ is compact, so fields on it have a discrete spectrum. A single quantum at the horizon scale maps to **the lowest non-trivial mode of the boundary S³**. The proposed initial condition is therefore not an arbitrary boundary datum but the **fundamental mode, singly excited**.

Everything below follows from testing that.

---

## T1 — **Does this pin N_e?** *(highest priority — the only thread that touches a live prediction)*

**Why it matters more than the rest.** Companion 17's (n_s, r) = (0.9692, 0.0053) is **conditional on N_e = 63.4**, which is currently an input, not derived. At N_e = 55 it moves to (0.9646, 0.0070). Part 3 lists N_e pinning among the open conditions. CMB-S4 and LiteBIRD will measure n_s and r at σ(r) ~ 0.001–0.003.

**If C21 fixes the total expansion budget, N_e stops floating and NTE's conditional becomes a prediction.** That is the single largest available upgrade to the corpus's empirical standing, and it is the reason to pursue this thread first.

**Compute:**
1. Under the reading, the daughter begins at Planck scale with the S³ fundamental mode singly excited. Does that fix N_total from reset to the present? Naively ln(R_H,now/ℓ_P) ≈ ln(10⁶¹) ≈ 140 — **verify, do not assume.**
2. The standard relation pins N_e (pivot-scale horizon exit) via the total expansion budget and the post-inflationary history. Combined with NTE's own H(N) = β_NTE|Φ|², does the budget close and yield a determinate N_e?
3. If it does: report the value with its uncertainty, and the resulting (n_s, r).

**Pre-registered fork — declare before computing:**
- N_e lands near 63.4 → the existing prediction is reinforced and, more importantly, *derived*.
- N_e lands elsewhere → **C21 falsifies NTE's current (n_s, r), or is itself falsified.** Either way it is a real result and must be reported as such, not smoothed.
- The budget does not close without new commitments → say so; the thread is then no better than the others.

**This fork must be stated before the calculation runs.** The temptation to land on 63.4 is exactly why.

---

## T2 — Largest-angular-scale structure

A compact S³ with a singly-excited fundamental mode imposes an **infrared cutoff** on the primordial spectrum at the curvature scale. Generically that suppresses power at the largest angular scales.

**Compute:** the S³ Laplacian spectrum (eigenvalues −(n²−1)/a², n ≥ 1 — verify the convention), the induced cutoff, and the resulting low-ℓ CMB prediction.

**Confront honestly with two things:**
- The observed low-ℓ power deficit is real but modest (~2–3σ in Planck) and **cosmic variance at low ℓ is brutal**. Do not present a 2σ feature as support. State what the model predicts and what the data can distinguish.
- NTE already has **Ω_k = 0**, i.e. R_S³ ≫ R_H. A cutoff at the curvature scale may therefore fall far outside the observable range, in which case **there is no observable and that is the answer.** Check this first — it may kill T2 in one line.

---

## T3 — Matched circles: a live falsifier, probably already passed

Compact S³ topology predicts matched circle pairs in the CMB if the S³ radius is comparable to or smaller than the horizon. Planck's topology searches found none.

**Compute:** the lower bound on R_S³ that the null result imposes, and whether NTE's construction is compatible with it. Report whether the bound is already satisfied trivially (likely, given Ω_k = 0) or whether it constrains anything.

This is the shape of test Greg anticipated — **absence of evidence as a constraint**. Worth having stated precisely rather than gestured at.

---

## T4 — Entropy, and Penrose's own motivation

A single quantum in one mode carries entropy of order k. The daughter therefore begins in an **essentially zero-entropy state**, and a single mode has no Weyl curvature to speak of.

**This is the Weyl Curvature Hypothesis satisfied by construction rather than assumed** — and the low-entropy past is precisely what drove Penrose to CCC in the first place. If it holds, NTE's variant delivers Penrose's motivating problem as an output of its trigger condition.

**Compute:** the entropy of the boundary datum; whether "one mode, one quantum" genuinely implies vanishing Weyl at the interface; and how this relates to §12's entropy-bookkeeping question, which it may partly answer.

**Register discipline:** this is **explanatory, not predictive.** It explains something already known. Under §II.0 that is a reformulation unless it also yields a distinguishing prediction. It should be stated as a structural payoff and must not be counted as a test. Say so explicitly in the verdict so nobody downstream promotes it.

---

## T5 — Consistency check that could kill the whole reading

Does a single S³ boundary mode **conflict with NTE's existing inflationary perturbation sector?** The corpus generates n_s and r from the Φ sector via K(Φ) and ξ = 1/6. If C21's seed supplies a *second*, independent origin for primordial structure, the two must either coincide or compete.

**If they compete, C21's reading is inconsistent with the deposited corpus and must be withdrawn or reconciled.** This is the check most likely to fail, so run it early — before T1's budget calculation, if resources are tight. There is no point pinning N_e inside a framework the reading contradicts.

---

## What AC expects, honestly

T5 is the most likely to fail. T2 is likely to die on Ω_k = 0. T3 is probably a bound already satisfied. T4 is real but explanatory only.

**T1 is the one worth the effort**, and it is worth it because it touches a live, soon-measurable prediction rather than because it is likely to succeed.

If the honest outcome is "the reading is coherent but has no testable content beyond what the corpus already predicts," **that is the result**, and C21 §12 should say it in one sentence. A speculative companion that says plainly what it cannot test is worth more than one that gestures at observability it does not have.

---

## Deliverables

One verdict file per thread in `Working\`, in the existing VERDICT naming convention, plus a completion handoff to `Handoffs\` addressed to AC. Register each on Manifest §10 as part of delivery (discipline 10). Pre-registered forks stated **before** results in each file.

---

— AC, 2026-09-24.
