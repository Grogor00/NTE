# Directive — AC → Scratch, Jammer: sunshine audit of Companion 5's flatness derivation

**From:** AC (Claude) · **To:** Scratch (constructive), Jammer (adversarial) · **Cc:** Greg, PC, Cursor · **Date:** 2026-09-24
**Greg's direction:** sunshine / rabbit-hole style — follow it down, report what is actually there.
**Source:** `Core_Papers\Companion_05_StateSpace_v10_19_0.md` §4 and §9.

---

## Standing instruction, stated first

Greg's framing was *"there must be a solution that works."* **That is not the brief.** A lane told a solution exists will produce one, and this corpus has withdrawn four claims found that way — the six-note chord, the β_NTE √6/π characterisation, the θ₁₃ formula, the Cabibbo formula.

**"The flatness derivation does not hold and should be withdrawn" is a permitted, and possibly correct, outcome.** Greg's own standing position (2026-09-24): *if the evidence is against a foundational number, we go with the evidence.* State forks before results, as always.

---

## The problem

Companion 5 §4:

> The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and **zero total energy requires zero spatial curvature, Ω_k = 0**. … NTE **derives flatness** both dynamically (from H(N) = β_NTE|Φ_NTE(N)|²) and topologically (from Euler closure).

§9 restates it as a falsifier: *"Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)."*

**This now contradicts two same-day ratified items:**
- **Part 3** (patched 2026-09-24): Ω_k → 0, with *"Exact Ω_k = 0 is not claimed"*, because a closed S³ of finite radius has Ω_k < 0.
- **Falsifiability item 11** (added 2026-09-24): NTE **requires** Ω_k < 0 strictly; a confirmed Ω_k > 0 falsifies.

Item 11 and Companion 5 §9 **point in opposite directions**: one requires non-zero curvature, the other says non-zero curvature falsifies. They cannot both stand.

---

## Q1 (core). Does the bilateral zero-energy condition imply anything about spatial curvature at all?

**AC's suspicion, to be tested not assumed:** Companion 5 uses *"zero total energy"* for two different quantities.

- **The Janus/bilateral sum** — the two CPN-conjugate sectors have total energy, charge and baryon number exactly zero. A statement about the *pair*.
- **The FRW energy of one sector** — in the Newtonian reading of the Friedmann equation, E = 0 ↔ k = 0 (flat, critical density); E < 0 ↔ k = +1 (closed).

If these are conflated, the flatness conclusion does not follow: the bilateral sum can vanish with each sector individually closed and negative, summing to zero. **Determine whether Companion 5's argument survives the distinction.**

## Q2. Is the Euler-identity step doing any work?

e^{iπ} + 1 = 0 is an algebraic identity about complex exponentials. Establish whether it is (a) a genuine structural premise here, (b) notation for the antipodal map e^{iπ} that Companion 5 elsewhere uses correctly, or (c) decoration on a conclusion reached another way. **If (c), say so plainly** — the corpus has a documented history of retiring exactly this pattern.

## Q3. The second claimed route.

Companion 5 also claims flatness is derived *"dynamically (from H(N) = β_NTE|Φ_NTE(N)|²)"*. Audit this independently of Q1. Does the constraint imply spatial flatness, or only that H is sourced by the field? **AC expects the latter** — the constraint fixes the expansion rate, not the curvature term — but it must be checked, because if this route holds it survives even if Q1 fails.

## Q4. Reconciliation, if any survives.

Given NTE requires a closed S³ of finite radius (Ω_k < 0 strictly, item 11), and given Planck's Ω_k = 0.0007 ± 0.0019 is consistent with zero and has a **positive** central value which closure forbids:

- Is there a defensible sense in which the boundary condition sets Ω_k → 0 *asymptotically* without claiming exact zero?
- Does anything in NTE constrain the **magnitude** of |Ω_k|, or only its sign? (AC expects sign only: the P1–P4 round found the crossing datum carries at most one real number, Ω, already built from the parent's β — no spare content to set a second parameter.)

## Q5. What replaces §9's falsifier?

If Q1–Q3 fail, Companion 5 §9's *"non-zero curvature would falsify"* is simply wrong and must be replaced by item 11's converse. Draft the replacement.

---

## Pre-registered forks — state before computing

1. **The bilateral argument does bear on curvature.** Report how, and reconcile with closure. Strongest outcome.
2. **Two-quantity conflation confirmed; flatness derivation fails.** Companion 5 §4's derivation claim is **withdrawn**, §9's falsifier replaced. Both instances of "derives flatness" come out. **AC's expectation.**
3. **Dynamical route (Q3) survives alone.** Then flatness is derived, but not from Euler closure; §4 keeps one route and loses the other.
4. **Undetermined without a commitment NTE has not made.** Then it joins the open list, and neither the derivation nor its falsifier may stand as written.

---

## Scope

- Do **not** revisit item 11 or the Part 3 Ω_k wording; both are Greg-ratified and stand while this runs. Companion 5 is the outlier under audit.
- Do **not** attempt to source Ω_k from the seed photon. Settled: Ω_k is defined as the deviation 1 − Ω_total, not a component with an energy budget; and the magnitude is ~117 orders beyond the seed in any case.
- This is a **corpus** question, not a C21 question.

## Deliverables

One verdict file each in `Working\`, existing naming convention; completion handoff to `Handoffs\` addressed to AC; register on Manifest §10 (discipline 10).

---

— AC, 2026-09-24.
