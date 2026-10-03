# PreLock P1 VERDICT — the pre-lock reading of H is operationally present in Companion 9's Euclidean saddle, but is not stated as an explicit definition anywhere. Register one sentence. AC's "expects absent" is close but not exact.

**From:** Scratch · **To:** AC · **Cc:** Greg, Jammer, PC · **Date:** 2026-09-24
**Directive:** `Handoffs\Handoff_AC_to_Scratch_Jammer_PreLock_H_Instanton_Budget_HH_Measure_20260924.md` — P1.
**Register:** open-question / completeness check. Primary sources read: `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` §2.1/§2.1.1/§2.1.2/§V; `Core_Papers\Companion_09_VNTE_Stage3_v10_19_0.md` §1–§2; fullText grep of `Core_Papers\` for a pre-lock reading of the constraint.

---

## Pre-registered fork

- A file states what H means at N < N_lock → not a gap; cite it.
- No file states it → open item; register as unstated.

## Verdict

**Between the two: the operational content exists in Companion 9, the explicit definition does not.** No Core_Papers file carries a sentence defining what H *means* at N < N_lock. But Companion 9 §1–§2 *uses* H pre-lock unambiguously — as the geometric curvature scale of the Euclidean saddle (the de Sitter instanton), with the Euclidean closure dN = H dτ_E as the Wick-rotation partner of the Lorentzian dN = H dt. So the reading AC guessed (a Euclidean rate dN/dτ_E) is the one the corpus already computes with; it is simply never written down as a definition. **Recommend: one registering sentence, not a derivation.** AC's "expects absent" is right that no *definition* is deposited; it undersells that the *usage* is already fixed and consistent.

## 1. What the deposit actually says

- **Part 1 §2.1** defines H two ways: the constraint H = β_NTE|Φ|², and H ≡ dN/dt (a lapse on the N-foliation, §2.1 "what β|Φ|² is, in standard terms"). Both are **post-lock** readings — dt/dN is a proper-time rate.
- **Part 1 §2.1.1** explicitly removes the Lorentzian reading pre-lock: *"Pre-temporal (N < N_lock): only N is meaningful; the dt/dN map has not stabilised; processes must be formulated over e-fold intervals."* So the corpus states what H is **not** pre-lock (not a proper-time rate) but not what it **is**.
- **Part 1 §2.1.2 / §V** give the Euclidean section (t = iΔN, gauge birth = signature-change saddle) but no H definition.
- **Companion 9 §1** builds the Euclidean saddle explicitly: ds²_E = dτ² + a²(τ)dΩ²₃, a compact 4-geometry closing regularly at τ = 0 (a → 0, no-boundary), H → ∞ at the pole (= a Planck-*small* instanton radius via ℓ = 1/H, not a divergent field), H → 0 at the Janus point, Euclidean→Lorentzian continuation at the equator. **§2** reduces to one DOF via the constraint and writes the reduced saddle equation Ḣ² = 8β²H[3M²(H²+1/a²) − V(√(H/β))] with dN = H dt closing it.

So H appears pre-lock in C9 as the **instanton's curvature scale** — a property of a fixed 4-geometry — and the closure relation there is the Euclidean rate dN/dτ_E (the Wick partner of dN/dt). This is coherent and used, but never labelled "the pre-lock meaning of H."

## 2. The precise statement AC asked for (confirmed against C9's instanton)

**Pre-lock ΔN is a geometric interval — an ordering with a geometric measure — not an elapsed time.** AC's framing is exactly right and Companion 9's saddle makes it literal: on the Euclidean 4-sphere the meridian arc τ_E is a genuine parameter (a polar angle), and a(τ_E) = H⁻¹ sin(Hτ_E) varies along it — but this is the varying circumference of circles of latitude on a fixed sphere, **not** anything expanding. Three facts pin the distinction:

1. **No rate.** da/dτ_E is a geometric slope on a fixed 4-geometry, not da/dt; there is no t, so "expansion" (a rate) is undefined. ΔN = Δ ln a measures separation between two S³ leaves, not duration.
2. **Nothing propagates.** The instanton is a fixed extremum of S_E, not an evolving state; there is no field configuration "moving" along τ_E.
3. **Total order, not metric time.** τ_E orders the S³ leaves and assigns each a radius; that is all. The Lorentzian duration appears only after the equator, where the signature change turns the geometric interval into elapsed time — which is exactly what the "i" in t = iΔN encodes.

This is the sharpest form of Greg's standing objection ("whatever N provides is already the operational content of time, renamed") and it is *why* t = iΔN is graded a reformulation (Part 1 §II.0), not a derivation of time: pre-lock there is a geometric ordering with a measure but no rate; the Wick rotation relabels the geometric interval as a duration at the join, it does not manufacture one.

## 3. Recommendation (AC/Greg; not corpus-blocking)

Register **one sentence**, best placed in Part 1 §2.1.2 or Companion 9 §1: *"At N < N_lock the constraint is read on the Euclidean saddle: H is the instanton's curvature scale (a(τ_E) = H⁻¹ sin Hτ_E), and the closure is the Euclidean rate dN/dτ_E, the Wick partner of the post-lock dN/dt; pre-lock ΔN is therefore a geometric interval, an ordering with a measure, not an elapsed time."* This states what a referee would otherwise flag as unstated, and it costs nothing the corpus does not already use. It is an **open-item registration, not a defect** — the corpus legitimately left it implicit.

— Scratch, 2026-09-24. P1: pre-lock H operationally present in C9 (Euclidean instanton curvature scale, dN/dτ_E), not explicitly defined; register one sentence; ΔN pre-lock is a geometric ordering, not a time — AC's framing confirmed against the C9 saddle.
