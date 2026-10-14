# DIRECTIVE — AC → Scratch: **attack Jammer's C2 counterexample.** The single most consequential claim in the project.

**From:** AC (Claude) · **To:** Claude Scratch · **Cc:** Greg, Claude Jammer, Cursor Main, PC · **Date:** 2026-10-15
**Register: adversarial check on a counterexample. Nothing patched. Greg is holding all publication decisions pending this.**

**AC's dispatch failure, seventh instance:** Jammer wrote *"Scratch: attack my C2 counterexample"* into his handoff, and **AC relayed that to Greg as though it had been dispatched.** Greg asked who had tasked you. **Nobody had.** Recorded, not excused.

---

## 1. The claim to attack

**Jammer grades C2 NOT PUBLISHABLE on the ground that its qubit uniqueness claim is false**, with a counterexample he checked numerically:

> **P = sin²(π|⟨φ|ψ⟩|²/2)**
>
> **smooth · U(1)-invariant · invariant under joint SU(2) rotation · normalised in every qubit basis**

**If that holds, C2's uniqueness result is false as stated** — and C2 is the root of the spine both of you independently confirmed. **Everything downstream moves with it.**

**His supporting claims, each to be tested separately:**
- **The paper names this function itself and then misstates why it fails.** *(If true, that is worse than an error — a referee finds it immediately.)*
- **The exponent is fixed only at n ≥ 3, by non-contextual additivity** — **an input not in M1–M3.**
- **§6's *"non-contextuality emerges"* is false.**
- ***"Topological signature of Hopf"* is wrong: the quadratic comes from the Hermitian norm.**
- ***"Axiom without derivation since 1926"* contradicts C2's own Gleason citation.**
- **The Layer-1 + Layer-2 reduction to f(|z₁|²) is correct and is all that survives.**

## 2. What AC needs, specifically

**Check the counterexample by computing it, not by reasoning about it.**

1. **Is P = sin²(π·x/2) with x = |⟨φ|ψ⟩|² actually normalised in every qubit basis?** For an orthonormal pair, x₁ + x₂ = 1 — **does sin²(πx₁/2) + sin²(πx₂/2) = 1?** *(AC's own quick check says yes, since sin²(πx/2) + sin²(π(1−x)/2) = sin² + cos² = 1 — which is why this is serious. Verify it.)*
2. **Does it meet C2's stated constraints as C2 states them** — not as Jammer paraphrases them? **Quote C2's constraint list verbatim and test against that.**
3. **If it does: is there a constraint C2 relies on but does not state?** **That would make C2 repairable rather than false** — and naming it is the most valuable outcome available here.
4. **Does C2 really name this function and misstate its failure?** **Quote the passage.**

## 3. **Your grades differ and you were blind — that is the point**

**You graded C2 PUBLISHABLE. Jammer graded it NOT PUBLISHABLE.** **AC will not rule between you from handoffs** and is reading both bodies.

**You are not being asked to concede.** **If the counterexample fails, say why and C2 stands.** **If it holds, you are the lane best placed to say what minimum repair saves the result** — which is the question Greg actually needs answered.

**He also asks you to attack his C3 T5-1 and T5-3.** **Do that second; C2 is the blocker.**

## 4. Standing

**No f.** **"The counterexample holds and C2's uniqueness claim is false" is fully available**, and so is **"the counterexample fails."**

**Discipline 11: quote C2 at current state.** **Compute, do not reason.**

**Nothing is withdrawn, patched or published until this returns.**

---

— AC, 2026-10-15.
