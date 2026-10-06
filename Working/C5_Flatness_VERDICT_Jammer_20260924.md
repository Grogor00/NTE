# Verdict — Companion 5 Flatness Derivation (Jammer / Adversarial Lane)

**Auditor:** Jammer (Claude, adversarial lane)
**Date:** 2026-09-24
**Source:** `Core_Papers\Companion_05_StateSpace_v10_19_0.md` §4, §5, §8, §9, abstract
**Cross-references:** `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` (Ω_k entry, falsifiability item 11)
**Directive:** `Handoffs\Directive_AC_to_Scratch_Jammer_Companion5_Flatness_Derivation_Sunshine_Audit_20260924.md`

---

## Pre-registered forks (stated before results)

1. **The bilateral argument does bear on curvature.** Report how and reconcile with closure. Strongest outcome.
2. **Two-quantity conflation confirmed; flatness derivation fails.** Companion 5 §4's derivation claim is withdrawn, §9's falsifier replaced. Both instances of "derives flatness" come out. AC's expectation.
3. **Dynamical route (Q3) survives alone.** Flatness is derived, but not from Euler closure; §4 keeps one route and loses the other.
4. **Undetermined without a commitment NTE has not made.** Joins the open list; neither derivation nor falsifier may stand as written.

---

## Q1. Does the bilateral zero-energy condition imply anything about spatial curvature?

**No. The derivation conflates two distinct quantities.**

Companion 5 §5 establishes that CPN symmetry requires "simultaneous nucleation of two CPN-conjugate sectors with total energy, charge, and baryon number exactly zero." This is a statement about the **pair**: sector + antisector sum to zero across the Janus boundary. Call this E_bilateral = 0.

The Newtonian reading of the Friedmann equation relates the **single-sector** total energy to curvature:

- E_sector = 0 ↔ k = 0 (flat, critical density)
- E_sector < 0 ↔ k = +1 (closed)
- E_sector > 0 ↔ k = −1 (open)

Companion 5 §4 moves from "total energy of the manifold must vanish" (bilateral) to "zero total energy requires zero spatial curvature" (single-sector Friedmann). This step is invalid. The bilateral sum E_bilateral = E₁ + E₂ = 0 does not constrain either sector individually. Two CPN-conjugate closed sectors each with E < 0 can sum to zero across the boundary precisely because CPN reverses the N-direction (and hence the sign convention on the kinetic term in the Friedmann-energy analogy). The bilateral zero does not propagate into either sector's Friedmann equation.

Moreover, NTE's own ontology requires this to fail: the manifold is S³ (closed, k = +1), which means each sector individually has E < 0 in the Friedmann reading. If the bilateral argument did force E_sector = 0, it would contradict the S³ topology that the entire framework rests on.

**Verdict on Q1:** The bilateral zero-energy condition constrains the pair, not the individual-sector curvature. The flatness conclusion is a conflation error. The two quantities — bilateral CPN-summed energy and single-sector Friedmann energy — are logically independent, and the closed S³ topology requires them to differ.

---

## Q2. Is the Euler-identity step doing any work?

**No. It is notation for the antipodal map, doing no work for the curvature claim.**

Companion 5 §4: "The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary."

Decompose this:

- e^{iπ} = −1. In Companion 5 §5 this is correctly identified as the CPN transformation: "multiplication by e^{iπ}, the Euler rotation on the state space, reversing every coordinate." This is the antipodal map on S³. This usage is legitimate.
- "+1 = 0" then reads: (antipodal image) + (original) = 0, i.e. x + (−x) = 0. This is CPN symmetry — the statement that sector plus antisector sum to zero. It is an algebraic tautology once the antipodal identification is made.
- The further step to "zero spatial curvature" is the conflation identified in Q1 and does not follow.

The Euler identity is therefore:

**(b)** Notation for the antipodal map that Companion 5 elsewhere uses correctly, combined with **(c)** decoration on a curvature conclusion that is itself wrong. The phrase "Euler closure" gives the appearance of a topological argument, but no topological content connects e^{iπ} + 1 = 0 to the curvature parameter Ω_k. The identity is about complex exponentials; spatial curvature is about the sign of k in the Robertson–Walker metric. No derivation bridges these.

The corpus has a documented history of retiring exactly this pattern (§4 of the directive lists four precedents). This is the same pattern: an algebraic identity dressed as a structural derivation.

**Verdict on Q2:** The Euler identity is doing zero work for the flatness claim. It is legitimate notation for CPN (the antipodal map) and decoration on the curvature conclusion.

---

## Q3. Does H(N) = β_NTE|Φ_NTE(N)|² imply spatial flatness?

**No. The constraint fixes the expansion rate, not the curvature term.**

The Friedmann equation with curvature reads:

$$H^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2}$$

The relation H = β|Φ|² is presented in Companion 5 §3 as "a geometric constraint between two properties of the same surface." It says the Hubble parameter tracks the boundary field amplitude. This is a definitional relationship — the field's magnitude is the expansion rate up to a coupling constant.

This constraint is perfectly compatible with any value of k. In a closed universe (k = +1), the Friedmann equation includes the −k/a² term, and the field amplitude |Φ|² simply tracks the resulting net H, including curvature effects. As a → ∞ (large e-fold count), k/a² → 0, so H → the flat-limit form regardless — but this is the standard inflationary dilution of curvature, not a derivation of exact flatness.

There is no step in Companion 5 where H = β|Φ|² is shown to require k = 0. The claim "NTE derives flatness... dynamically (from H(N) = β_NTE|Φ_NTE(N)|²)" asserts a conclusion without providing a derivation. The constraint relates two quantities on the boundary; it is silent on curvature.

**Verdict on Q3:** The dynamical route does not survive as a flatness derivation. H = β|Φ|² constrains the expansion rate, not the curvature. This route fails independently of Q1.

---

## Q4. Reconciliation

Both claimed routes to flatness fail. What survives?

**What Part 3 already says is correct and sufficient:** The S³ is closed (Ω_k < 0 strictly), but its radius after the e-fold run is vast compared with the observable patch, so curvature is driven to undetectable levels. This is the standard inflationary explanation for observed near-flatness, transposed into NTE's language. Observed flatness is a consequence of the expansion history, not of a boundary condition forcing exact Ω_k = 0.

**Can the boundary condition set Ω_k → 0 asymptotically?** Yes, trivially: any closed universe that undergoes sufficient expansion drives |Ω_k| → 0 as a → ∞. The NTE-specific content here is that the manifold must be S³ (closed), which forces Ω_k < 0 at all times but pushed toward zero by expansion. This is already stated in Part 3 and is not what Companion 5 claims.

**Does NTE constrain the magnitude of |Ω_k|?** No — only the sign. The magnitude depends on the e-fold count and the expansion history, which are set by β_NTE and the matter content. The crossing datum carries at most one real number (Ω, already consumed by β_NTE). There is no spare geometric content to pin |Ω_k| to a specific value. This is consistent with Part 3's honest qualifier: "NTE predicts the sign, not the magnitude."

**Verdict on Q4:** Part 3's treatment is correct: Ω_k < 0 strictly, |Ω_k| → 0 by expansion, sign predicted but not magnitude. Companion 5's claim of derived exact flatness is irreconcilable with the closed S³ and should be withdrawn in favour of Part 3's wording.

---

## Q5. What replaces §9's falsifier?

### Current text (to be withdrawn)
> "Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)."

This is directly contradicted by Part 3's falsifiability item 11 (ratified 2026-09-24), which requires Ω_k < 0 strictly. The two point in opposite directions: §9 says non-zero curvature falsifies; item 11 says exact zero falsifies (and positive curvature falsifies even more strongly). They cannot both stand; item 11 is ratified and Companion 5 is the outlier.

### Draft replacement

> Spatial curvature sign: the boundary ontology requires a closed S³, hence Ω_k < 0 strictly; confirmed Ω_k > 0 at significance falsifies the framework at the ontological level (falsifiability item 11).

This aligns §9 with item 11 and the Part 3 parameter ledger.

---

## Fork determination

**Fork 2 confirmed: two-quantity conflation; flatness derivation fails.**

- The bilateral zero-energy condition (Q1) constrains the CPN pair, not the individual-sector curvature; the step to Ω_k = 0 is a conflation error.
- The Euler identity (Q2) is notation for the antipodal map plus decoration; it contributes no curvature content.
- The dynamical route H = β|Φ|² (Q3) constrains the expansion rate, not the curvature term; it fails independently.
- Part 3's treatment (Q4) — Ω_k < 0 strictly, driven toward zero by expansion — is correct and requires no repair.
- §9's falsifier (Q5) contradicts the ratified item 11 and must be replaced.

The derivation does not hold. The claims should be withdrawn.

---

## All instances of the flatness claim in Companion 5 (complete inventory)

Each instance below must be corrected in the §10 patch:

| Location | Current text | Status |
|---|---|---|
| **Abstract** | "Flatness (Ω_k = 0) is required by the Euler closure condition on S³." | **Withdraw.** Replace with: near-flatness (Ω_k → 0) is a consequence of the expansion history on a closed S³. |
| **§4 "Flatness" paragraph** (full paragraph) | "The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and zero total energy requires zero spatial curvature, Ω_k = 0. The universe is flat because the boundary condition demands it. NTE derives flatness both dynamically (from H(N) = β_NTE\|Φ_NTE(N)\|²) and topologically (from Euler closure): the Euler identity explains why the initial conditions had to be flat, the Hubble relation explains how flatness is maintained." | **Withdraw entire paragraph.** Replace with text consistent with Part 3: the closed S³ has Ω_k < 0 strictly, driven toward zero by the e-fold run. |
| **§8 table row** | "flatness (Euler closure)" listed as a result of this paper | **Withdraw "flatness (Euler closure)".** Replace with: spatial curvature sign (Ω_k < 0 from closed S³). |
| **§8 enumeration** | "flatness (Euler closure)" in the sentence listing results | **Withdraw.** Replace with: near-flatness (expansion-driven). |
| **§9 falsifier** | "Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)." | **Withdraw.** Replace with the draft in Q5 above. |

Five instances total. All must be corrected to align with Part 3 and item 11.

---

## Summary

The flatness derivation in Companion 5 does not hold. Both claimed routes — the "Euler closure" (topological) and the dynamical H = β|Φ|² — fail on independent grounds. The core error is conflating the bilateral CPN zero-energy condition (a statement about the pair of conjugate sectors) with the single-sector Friedmann energy that determines spatial curvature. The Euler identity adds no curvature content — it is notation for the antipodal map dressed as a derivation. The dynamical constraint relates the expansion rate to the field amplitude and is silent on curvature.

Part 3's treatment is already correct: Ω_k < 0 strictly (closed S³), with |Ω_k| driven toward zero by expansion. Companion 5 is the outlier. Five instances of the claim must be corrected, and §9's falsifier must be replaced to align with ratified item 11.

**"The flatness derivation does not hold and should be withdrawn"** is the finding.

---

— Jammer, 2026-09-24. Blind protocol: no Scratch / Cursor / other-lane output was read before this filing.
