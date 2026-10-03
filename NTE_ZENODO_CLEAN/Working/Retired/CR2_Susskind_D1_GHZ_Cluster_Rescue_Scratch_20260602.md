# Susskind D1 — the triviality is an artifact; cluster analog survives via global chirality GHZ (Scratch surge)

**From:** Scratch (Connes Programme lead) — Claude session, primary Scratch
**Convergence check:** Cursor Scratch (automated) — divergence to be flagged + investigated per Greg 2026-06-02
**Re:** `CR2_Susskind_D1_Cluster_Test_Cursor_Jammer_20260602.md` (AJ-21, verdict NEEDS-MORE) and `Paper_Mirror_of_Susskind_..._v0_2_Simplified_Cursor`
**Date:** 2026-06-02
**Register:** adversarial derivation. Results marked **[DERIVED]** / **[CONJECTURE]** / **[VERIFY-CORPUS]**. No corpus patch (outreach lane). Not ratified.

---

## 0. One-line result

The AJ-21 "trivially zero" is **not** a verdict against the parallel — it is an artifact of testing cluster decomposition in a space with **no spatial extent** and with the **wrong correlator**. In the canonical arena (global chirality cat across separated regions) the connected charge correlator is **O(1) and non-decaying**, mirroring Susskind's ⟨Z_p Z_h⟩ = 1. The parallel **survives on the ℤ₂-cluster/gauge axis** and **genuinely breaks on the time-reversal axis** — which is exactly the boundary v0.2 already drew, now with a reason.

---

## 1. Why AJ-21 came out zero (diagnosis)

AJ-21 used sector-diagonal observables 𝒪_R = Π_R Â Π_R, 𝒪_L = Π_L B̂ Π_L on the 2-state chirality space, and found ⟨Ψ_Janus|𝒪_R 𝒪_L|Ψ_Janus⟩ = 0.

Two independent reasons this is degenerate, not physical:

- **[DERIVED] No spatial extent.** Cluster decomposition is *intrinsically* a statement about correlations between **spatially separated regions**. A 2-dimensional chirality qubit has no regions, so the diagnostic is undefined, and "0" is the undefined-limit artifact, not a physical absence of cross-sector correlation. Susskind's own argument lives in a *large* finite-dim space with high-rank Π_f, Π_b and operators carrying both diagonal and off-diagonal structure.
- **[DERIVED] Wrong operator.** 𝒪_R, 𝒪_L are supported on orthogonal rank-1 sectors, so 𝒪_R 𝒪_L = 0 *as an operator* (Π_R Π_L = 0) — independent of the state. The vanishing is a triviality of disjoint support, not a cluster statement.

The 2-qubit embedding AJ-21 flagged as "non-canonical" (giving ⟨σ_x σ_x⟩ = 1) was actually a **hint in the right direction**: it accidentally restored a two-region tensor structure. The fix is to take that seriously and principled, not to discard it.

---

## 2. The canonical arena [VERIFY-CORPUS]

The correct space is the **chirality-graded spinor field algebra on S³** — the two Killing-spinor families ε_± (Bär 1993), the mirror M exchanging them, tied to Companion 5 (State Space) / Ch 10. Operators live at **points x, y on S³** with finite geodesic separation. This is precisely the "finite-dim model tied to Companion 5 / Ch 10" AJ-21 asked for.

The load-bearing corpus fact to confirm (Q1 for this surge):

> **Is the pre-bifurcation symmetric Janus state a GLOBAL chirality cat** — the whole surface coherently R, superposed with the whole surface coherently L — **or a LOCAL product** (each region independently (R+L)/√2)?

NTE physics points hard to **global**: the bifurcation selects one chirality **for the entire observable universe** (v0.1 §3: "the observable universe has a definite chirality"), and the Hopf-fibre obstruction is to a *globally* consistent assignment. So the symmetric state is the global GHZ cat. **This must be verified against Companion 5 / Ch 10 before the result is load-bearing** — it is the single assumption everything below rests on.

---

## 3. The computation [DERIVED]

Global chirality GHZ over regions 1…n:

  |Ψ_Janus⟩ = ( |R⟩₁…|R⟩ₙ + |L⟩₁…|L⟩ₙ ) / √2

Local chirality charge Z(x): Z|R⟩ₓ = +|R⟩ₓ, Z|L⟩ₓ = −|L⟩ₓ. Then:

- One-point: ⟨Ψ|Z(x)|Ψ⟩ = ½(+1) + ½(−1) = **0** (symmetric — required; the state carries no preferred chirality). Cross terms vanish (⟨R…|Z(x)|L…⟩ = 0).
- Two-point: ⟨Ψ|Z(x)Z(y)|Ψ⟩ = ½[(+1)(+1)] + ½[(−1)(−1)] = **1**.
- **Connected:** ⟨Z(x)Z(y)⟩_c = 1 − 0·0 = **1, for all separations** ⟹ **non-decaying ⟹ cluster-decomposition violation.**

This is the exact structural mirror of Susskind's ⟨Z_p Z_h⟩ = 1 for arbitrarily distant p, h.

**Control — the parallel would break if the state were local product** |Φ⟩ = ⊗ₓ(|R⟩ₓ+|L⟩ₓ)/√2: then ⟨Φ|Z(x)Z(y)|Φ⟩ = ⟨Z(x)⟩⟨Z(y)⟩ = 0, connected = 0, **no violation.** So the entire result is carried by GLOBAL-vs-LOCAL (§2 Q1). This is the make-or-break, and it is a corpus fact, not a free choice.

---

## 4. Pure-GHZ vs Susskind's maximally-mixed [DERIVED — disanalogy that does NOT bite]

Susskind's cluster violation is in ρ_max (mixed); NTE's Janus state is pure (GHZ). For the **Z–Z diagnostic** they agree: the classical mixture ρ = ½(|R…⟩⟨R…| + |L…⟩⟨L…|) also gives ⟨Z(x)Z(y)⟩ = 1. Pure-GHZ and maximally-mixed differ only in **coherences** (X-type / off-diagonal correlators), not in the charge correlator. So the **pure/mixed mismatch does not affect the cluster diagnostic** — good news for robustness. (It *may* matter for the full dressed-operator C̄ correspondence; see §5.)

---

## 5. Where it genuinely breaks — the residual divergence [DERIVED]

Susskind's dressed object C̄ = C·Π_− with C = [A(−s), A(s)] encodes **time-reversal-odd** content — the imaginary part of the Wightman function, generated by **antiunitary T** (FGC/BGC clock-momentum π is T-odd). NTE's mirror M is **unitary** and, under the CPN reframe, **arrow-preserving**. There is **no antiunitary structure on the NTE side to generate an Im-Wightman / clock-momentum analog.**

Consequence — the honest claim must be **narrowed**, and the narrowing is principled, not defensive:

- ✅ **Survives:** shared ℤ₂ projection bookkeeping, cluster-decomposition violation via the global charge cat, ℤ₂-as-gauge dressing.
- ❌ **Does not transfer:** the specifically *time-reversal* content (Im-Wightman, forward/backward clock momentum). NTE replaced T-reversal with arrow-preserving CPN, so by construction it has no counterpart to this.

This is exactly the line v0.2 Simplified already drew (T8 option (b): "shared ℤ₂ dressing, not mirror of T-breaking"). The derivation reaches the same boundary from the physics — an internal-consistency check that v0.2's honest scope is the *correct* scope, not merely a cautious one.

---

## 6. Verdict

- **AJ-21 NEEDS-MORE → upgraded to PARALLEL-SURVIVES-ON-ℤ₂-AXIS [CONJECTURE pending §2 Q1 corpus verify].** The cluster analog is real and computable once the arena has spatial extent and the state is the global cat.
- **D1 is rescuable** without ad hoc machinery — the GHZ structure is already implied by NTE's global chirality selection; no new postulate, just the correct arena and correlator.
- **The send-candidate claim should be tightened, not weakened:** state the ℤ₂-cluster/gauge parallel as the *computed* result (citing the global-cat ⟨Z Z⟩ = 1), and state the time-reversal non-transfer as a clean, owned boundary. That is a *stronger* outreach posture than "cluster violation, conjecture pending" — it converts the load-bearing test from promissory to derived-modulo-one-corpus-fact.

---

## 7. Divergence flag for Cursor-Scratch / Cursor-Jammer (per Greg's convergence protocol)

I **diverge** from the AJ-21 stopping point. Cursor-Jammer halted at "sector-local trivially zero, NEEDS-MORE." I claim the triviality is a double artifact (§1) and the global-GHZ + charge-correlator pathway (§3) gives a definite survival. This is Greg's **case (b)** — a pathway the automated lane has not surfaced — *unless* there is a corpus reason the pre-bifurcation state is **not** the global cat, in which case it is **case (a)** and I am wrong. **Investigation item:** confirm against Companion 5 / Ch 10 whether the symmetric Janus state is global GHZ or local product (§2 Q1). That single fact decides between (a) and (b).

---

## 8. Queue

1. **[VERIFY-CORPUS] Q1 — global-cat vs local-product** (Companion 5 / Ch 10). Load-bearing. Owner: Scratch next, or cross-assign.
2. **[DERIVE] dressed C̄_NTE** — does the coherence (pure-GHZ) structure reproduce *any* of Susskind's dressed-operator content, or only the diagonal charge correlator? Bounds how far §5's "survives" extends.
3. **[CROSS-CHECK] Cursor-Scratch** — run the same global-cat construction; confirm ⟨Z Z⟩_c = 1 independently or surface a defeater.
4. **[FRAMING] feed §6 into the next draft** — only after Q1 clears. Until then, send-candidate keeps cluster claims as conjecture.

---

— Scratch (Connes Programme lead), 2026-06-02. Sunshine surge on the D1 joint.
