# Verdict — Companion 5 Flatness Derivation: Sunshine (Constructive) Audit

**Lane:** Scratch (constructive) · **Date:** 2026-09-24
**Subject:** Companion 5, "The state space is the surface" — flatness claim (§4, §9, abstract, §8)
**Directive:** `Handoffs\Directive_AC_to_Scratch_Jammer_Companion5_Flatness_Derivation_Sunshine_Audit_20260924.md`
**Blind protocol:** No Jammer / other-lane output read before filing.

---

## Pre-registered forks (stated BEFORE results)

1. **The bilateral argument does bear on curvature.** Report how, and reconcile with closure. *Strongest outcome.*
2. **Two-quantity conflation confirmed; flatness derivation fails.** Companion 5 §4's derivation claim is withdrawn, §9's falsifier replaced. Both instances of "derives flatness" come out. *AC's expectation.*
3. **Dynamical route (Q3) survives alone.** Flatness is derived, but not from Euler closure; §4 keeps one route and loses the other.
4. **Undetermined without a commitment NTE has not made.** Joins the open list.

---

## Q1. Does the bilateral zero-energy condition imply anything about spatial curvature?

### The two quantities

Companion 5 §4 writes:

> *"The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and zero total energy requires zero spatial curvature, Ω_k = 0."*

This sentence bridges two claims:

**(a) Bilateral pair-sum zero-energy.** §5 states explicitly: *"requiring the simultaneous nucleation of two CPN-conjugate sectors with total energy, charge, and baryon number exactly zero."* This is a conservation statement about the *pair*: whatever energy sector A has, sector B has the negation under CPN. The pair sums to zero. This is a symmetry constraint on the nucleation, not a statement about the FRW energy budget of either individual sector.

**(b) The FRW zero-energy condition.** In the Newtonian analogy of the Friedmann equation, the "total energy" of a cosmological fluid element determines the curvature parameter:

- E = 0 → k = 0 (flat, critical density)
- E < 0 → k = +1 (closed, bound)
- E > 0 → k = −1 (open, unbound)

For a closed S³ with k = +1, each sector individually has E < 0 (gravitationally bound). Two negative quantities sum to a negative, not zero — unless "energy" in the bilateral sum means something categorically different from FRW total energy, which it does.

### The conflation

Companion 5 §4 slides from (a) to (b) in a single sentence: "the total energy of the manifold must vanish" ← bilateral CPN sum; "and zero total energy requires zero spatial curvature" ← FRW single-sector energy condition. The logical connector "and" treats these as the same quantity. They are not.

- The bilateral zero-sum is a charge-conservation-like statement. It says "matter + CPN-conjugate-matter = 0." It is true for any pair of CPN-conjugate sectors regardless of whether each sector is flat, closed, or open.
- The FRW zero-energy condition is about the energy budget *within* a single sector: kinetic (expansion) vs potential (gravitational). k = 0 requires a specific balance within one sector.
- A closed S³ sector with k = +1 has negative FRW energy, consistent with CPN-symmetric bilateral cancellation — each sector's negative E is mirrored by the other's. The bilateral sum vanishes precisely *because* the sectors are identical up to conjugation, regardless of k.

### Constructive attempt

I looked for the strongest honest rescue: is there a reading in which bilateral E = 0 constrains within-sector curvature?

One candidate: if the Janus nucleation occurs at a single point (N = 0) with zero radius, then a(0) = 0 and the curvature term −kc²/a² diverges for k ≠ 0, which could be argued to require k = 0 for regularity. But NTE does not make this argument — and it would contradict the S³ closure that the entire boundary ontology rests on. A closed S³ nucleation with k = +1 is singular in the FRW sense at a = 0 regardless; the standard treatment (Hartle–Hawking, tunnelling) handles this by Euclidean continuation, not by setting k = 0.

Another candidate: interpret "total energy of the manifold" as the ADM mass of the entire closed S³, which is indeed zero for any closed FLRW universe (positive matter energy + negative gravitational binding energy = 0). But this is true for *any* closed universe (any k = +1 cosmology), not specifically for flat ones. The zero-energy theorem for closed universes is a theorem about closure, not flatness. It would actually support the opposite conclusion: "zero total energy" ↔ "closed," which gives Ω_k < 0, not Ω_k = 0.

**Verdict on Q1:** The bilateral zero-energy condition does not imply spatial flatness. The argument conflates bilateral pair-sum cancellation with FRW single-sector energy balance. The strongest honest rescue (ADM mass = 0 for a closed universe) actually points to closure, not flatness, and is already captured by Part 3's position. No reading I can construct makes the passage valid as written.

---

## Q2. Is the Euler identity e^{iπ} + 1 = 0 doing any work?

Companion 5 §5 correctly identifies the CPN transformation as multiplication by e^{iπ} (the antipodal map on S³). The Euler identity e^{iπ} + 1 = 0 is then read as: "original sector + antipodally-mapped sector = 0."

This is the statement x + (−x) = 0. The Euler identity is being used as a *name* for the antipodal map, not as a mathematical engine. The "topological (from Euler closure)" derivation of flatness reduces to:

1. The antipodal map is multiplication by e^{iπ} = −1. *(Correct — this is genuine geometry of S³.)*
2. Therefore e^{iπ} + 1 = 0. *(Algebraic tautology: −1 + 1 = 0.)*
3. "Zero-sum energy constraint." *(CPN bilateral cancellation — yes, quantum numbers sum to zero.)*
4. "Zero total energy requires zero spatial curvature." *(Non sequitur — conflation per Q1.)*

Steps 1–3 are valid but trivial: they say the pair sums to zero, which is the definition of CPN symmetry. Step 4 does not follow from steps 1–3.

**Classification: (c) — decoration.** The Euler identity is notation for the antipodal map, which is legitimate geometry used correctly elsewhere in Companion 5. But in §4's flatness argument, it dresses a symmetry tautology (CPN conjugates cancel) in the clothing of a topological derivation and then draws a conclusion (Ω_k = 0) that does not follow. This matches the corpus's documented pattern of retiring exactly this kind of construction.

---

## Q3. The dynamical route: H(N) = β_NTE|Φ_NTE(N)|²

Companion 5 §4 claims flatness is derived "dynamically (from H(N) = β_NTE|Φ_NTE(N)|²)." The claim is that "the Hubble relation explains how flatness is maintained."

### Analysis

The Friedmann equation (in the standard form) is:

H² = (8πG/3)ρ − kc²/a² + Λ/3

Saying H = β|Φ|² constrains what sources H — it identifies the expansion rate with the boundary field. This tells us what drives expansion. It does **not** eliminate the curvature term. The spatial curvature −kc²/a² is a separate geometric contribution to the expansion dynamics.

At best, if one reads H = β|Φ|² as an *exact* identity (not just the dominant term), then k/a² must be absorbed into the effective field equation — but this is a rearrangement, not a derivation that k = 0. For k = +1, you simply have β|Φ|² including the curvature correction: the field "knows about" the curvature, but it's still there.

Part 3 already has the correct reading: the e-fold run makes the curvature term negligible (a² grows enormously, so kc²/a² → 0 dynamically), giving Ω_k → 0. This is not flatness derived from H = β|Φ|²; it is flatness approximated by inflation, which is standard cosmology, not an NTE-specific derivation.

**Verdict on Q3:** The dynamical route does not derive flatness. H = β|Φ|² constrains what sources the expansion rate; it says nothing about spatial curvature. The curvature contribution to the Friedmann equation is a separate geometric term. The e-fold dilution of curvature (Part 3's Ω_k → 0) is standard inflationary cosmology, not a derivation, and is already correctly stated in Part 3 without attributing it to this equation.

---

## Q4. Reconciliation

### Asymptotic Ω_k → 0 vs exact zero

Part 3 already holds the defensible position: the S³ is closed (Ω_k < 0 strictly), but after the e-fold run the radius is so large that curvature is undetectable at any accessible scale. This is:

- *Physically sensible:* standard inflationary dilution.
- *Consistent with data:* Planck Ω_k = 0.0007 ± 0.0019 (consistent with zero, consistent with tiny negative).
- *Not a derivation of flatness:* it is a consequence of sufficient expansion, true in any closed model with enough e-folds.
- *Not what Companion 5 claims:* §4 and §9 claim exact Ω_k = 0, not asymptotic approach.

There is a defensible statement available to NTE: "The boundary ontology requires a closed S³ (Ω_k < 0), and the expansion history drives |Ω_k| to undetectably small values." This is Part 3's position. It is honest and survives. It is not what Companion 5 says.

### Magnitude vs sign

Part 3 item 11 states explicitly: *"NTE predicts the sign, not the magnitude — the e-fold run drives |Ω_k| toward values plausibly far below any achievable sensitivity."*

I concur. The framework commits to:
- **Sign:** Ω_k < 0 (closed S³). This is structural — the boundary ontology requires closure.
- **Magnitude:** Not constrained. The e-fold count determines how small |Ω_k| is, but NTE does not derive the e-fold count from first principles (N_e is conditional, per the conditional register).

The directive's suspicion (from AC's P1–P4 round analysis) is confirmed: the crossing datum carries at most one real number (β_NTE), already committed. No spare content exists to fix a second parameter (|Ω_k|).

---

## Q5. Draft §9 replacement falsifier

### Current §9 text (to be withdrawn):

> *"Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)."*

This is wrong in both directions: it claims exact flatness (contradicting the required closure), and it says non-zero curvature falsifies (but the framework *requires* non-zero negative curvature).

### Replacement (drawn from Part 3 item 11, which is ratified):

> **Spatial curvature sign.** The boundary ontology requires a closed S³, so NTE requires Ω_k < 0 strictly: exact flatness is excluded by the geometry, and an open universe (Ω_k > 0) is excluded outright. A confirmed Ω_k > 0 at significance falsifies the framework at the level of the ontology. The magnitude |Ω_k| is not predicted — the e-fold run drives it toward values plausibly below achievable sensitivity — and a negative Ω_k would not confirm NTE uniquely, since every closed-universe cosmology predicts the same sign.

This is verbatim-compatible with Part 3 item 11. The replacement reverses the polarity of the falsifier: the old version said non-zero curvature kills the framework; the new version says non-zero curvature of the wrong *sign* kills it, while non-zero curvature of the right sign is *required*.

---

## Inventory of all Companion 5 instances claiming flatness / Ω_k = 0

| # | Location | Text | Status |
|---|----------|------|--------|
| 1 | Abstract | "Flatness (Ω_k = 0) is required by the Euler closure condition on S³" | **Withdraw**: conflation (Q1); Euler identity is decoration (Q2); exact Ω_k = 0 contradicts required closure |
| 2 | §4, sentence 1 | "The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and zero total energy requires zero spatial curvature, Ω_k = 0." | **Withdraw**: the core conflation; bilateral pair-sum ≠ FRW single-sector energy |
| 3 | §4, sentence 3 | "NTE derives flatness both dynamically (from H(N) = β_NTE\|Φ_NTE(N)\|²) and topologically (from Euler closure)" | **Withdraw**: both routes fail — topological (Q1–Q2) and dynamical (Q3) |
| 4 | §8, summary table | "flatness (Euler closure)" listed as a result of this paper | **Withdraw**: replace with "Ω_k < 0 (closure); Ω_k → 0 (e-fold dilution)" or similar |
| 5 | §9, falsifier | "Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)." | **Replace** with draft above (Q5), aligning with Part 3 item 11 |

**Total: 5 instances. All 5 must be corrected.** No instance of "derives flatness" survives as written.

---

## Fork chosen: Fork 2

**Two-quantity conflation confirmed; the flatness derivation fails; withdraw.**

### Reasoning

The constructive audit attempted to build the strongest honest reading of Companion 5's flatness claim. Every route was checked:

- **Topological / Euler route (Q1–Q2):** The bilateral CPN zero-energy sum (a symmetry conservation statement about the pair) is conflated with the FRW zero-energy condition (a single-sector energy balance that determines curvature). These are categorically different quantities. The Euler identity dresses a tautology (x + (−x) = 0) as a topological derivation. The strongest rescue — ADM mass = 0 for a closed universe — actually implies closure (Ω_k < 0), not flatness (Ω_k = 0), and is already the position in Part 3.

- **Dynamical route (Q3):** H = β|Φ|² identifies what sources H; it does not constrain the spatial curvature term in the Friedmann equation. The e-fold dilution of |Ω_k| is standard inflationary cosmology and is already correctly recorded in Part 3 without this equation.

- **Reconciliation (Q4):** The defensible position (Ω_k < 0 strictly, |Ω_k| → 0 by e-fold dilution, magnitude not predicted) already exists in Part 3 and item 11. It does not require anything from Companion 5 §4's derivation.

No rescue was found that the text supports. The constructive lane concurs with the expectation.

### Withdrawal / replacement list

**Withdraw from Companion 5 (pending Greg ratification; do not edit Core_Papers):**

1. Abstract: "Flatness (Ω_k = 0) is required by the Euler closure condition on S³" → replace with language consistent with Part 3 (Ω_k → 0 from e-fold dilution; Ω_k < 0 by closure).
2. §4 sentence 1: entire Euler-flatness paragraph → rewrite: the Euler/antipodal map encodes CPN bilateral cancellation (zero total charge, energy, baryon number for the pair); this is a statement about the pair, not about within-sector curvature; observed near-flatness follows from the e-fold run on a closed S³.
3. §4 sentence 3: "NTE derives flatness both dynamically…and topologically" → remove "derives flatness" claim; replace with "Observed near-flatness is a consequence of the e-fold expansion of the closed S³, not an independent derivation."
4. §8 table: "flatness (Euler closure)" → "Ω_k < 0 (S³ closure); |Ω_k| → 0 (e-fold dilution)" or equivalent.
5. §9 falsifier: replace with the draft in Q5 above, aligning with Part 3 item 11.

**Do not withdraw from Part 3:** Part 3's Ω_k → 0 entry and item 11 are correctly stated and ratified; they are the *target* alignment, not the problem.

### What survives

- The CPN bilateral zero-energy statement (§5) is valid: the pair has zero total quantum numbers by construction. This is the strongest content of the "zero-sum" claim. It simply does not imply flatness.
- The antipodal map reading of e^{iπ} = −1 (§5) is legitimate S³ geometry. It simply does not derive curvature.
- The Hubble relation H = β|Φ|² (§4) is a central NTE commitment. It simply does not derive flatness.
- The e-fold dilution of curvature is genuine cosmology, already in Part 3, and does not need Companion 5's derivation claim to stand.

### Note on withdrawal precedent

This withdrawal follows the pattern of four prior corpus withdrawals (the six-note chord, the β_NTE √6/π characterisation, the θ₁₃ formula, the Cabibbo formula): a conclusion is reached by a route that does not logically support it, dressed in notation that obscures the gap. The discipline applies.

---

**Filed by Scratch (constructive lane), 2026-09-24. Blind protocol observed: no Jammer output read.**
