# Handoff: CR → AC / Greg — v10.18.0 re-verify + fresh adversarial pass (against the shipped/rendered deposit)

**From:** CR (Critical Reviewer)
**To:** AC (fix blockers), Greg (ratification), Cursor (render after ratify)
**Date:** 2026-07-06
**Basis:** Manifest rev 10.2; verified against **live** `NTE_v10_18_0_Part1_Foundations` (§I, §II.0, §II, §III, §VI) and `NTE_v10_18_0_Part3_Accounting` (ledger, triage, distinctiveness, CC section) — not the §3 snapshot. Most prior CR points confirmed landed. Two are shipped defects; four are structural/ontological. Ranked.

---

## BLOCKERS (shipped into the rendered deposit — fix before Zenodo)

**B1 — Part 1 §III asserts "θ₁₃ = 0 … matching observation." False and self-refuting.** This is the item CR held Patch 4 v3 on (`…PATCHSET_Reverify_20260705`); the θ₁₂ de-bundle shipped but carried the error in. Live §III: "θ₂₃ = π/4, **θ₁₃ = 0**, and the maximal phase |δ_J| = π/2 (matching observation)."
- θ₁₃ ≈ 8.6°, nonzero at >5σ (Daya Bay/RENO 2012). "θ₁₃ = 0 … matching observation" is false — first line a neutrino referee checks.
- Self-refuting: Jarlskog J ∝ sin θ₁₃, so θ₁₃ = 0 ⇒ no observable CP ⇒ "|δ_J| = π/2 matching observation" cannot coexist with it.
- Contradicts the source: the mixing-sector paper's abstract says μ–τ *reflection* gives "naturally **nonzero** θ₁₃" (its advantage over permutation). §III shipped the permutation value.
- Part 3 is clean (never asserts it; withdraws the θ₁₃ formula as numerology). Defect is localized to **Part 1 §III + manifest §3 snapshot**.
- **Fix:** θ₁₃ ≠ 0 (nonzero, naturally, consistent with ~8.6°) — correct *and* stronger for NTE (accommodating nonzero θ₁₃ is reflection's whole point). Update the snapshot to match.

**B2 — Part 3 contradicts itself on a₄.** The POS a₄ correction landed in the CC section ("the structural mechanism stands and is **independent of a₄**; a previously quoted a₄-dependent number is withdrawn") but NOT in the **Empirical-distinctiveness paragraph of the same file**, which still says the dissolution works "via the absence of a gravitating 4-bulk vacuum **and the a₄ = 0 suppression on S³×S¹**." Manifest snapshot repeats the a₄ version. **Fix:** strike "and the a₄ = 0 suppression on S³×S¹" from the distinctiveness paragraph and the snapshot. (The CC problem is an a₀/a₂-order quantity; a₄ is irrelevant to it — the CC section already says so.)

---

## Ontological (the "break the ontology" answer)

**O1 (HIGH) — the time-emergence claim is idle / detachable.** Part 3 concedes N-primary/t-emergent "makes no post-lock observable … not directly testable; its empirical purchase is carried entirely by the consequences above." But every genuine result descends from the **spatial/algebraic** structure, not from time-emergence: κ (S³ Hopf topology), δ_J (CPN bilateral geometry), θ₂₃ (μ–τ on J₃(𝕆)), Majorana (Z₂-orbifold, κ₀<1), CC dissolution (boundary-only + unimodular). None invoke "t emergent from N." Time-emergence does work only in the pre-lock Euclidean phase, whose sole output is the **demoted conditional** n_s/r. So the namesake ontology is not just untestable — remove it and every listed derivation goes through unchanged; it motivates the bilateral-S³ geometry heuristically but is load-bearing for nothing in the confirmed ledger. Not an editing fix — honest positioning: state that time-emergence is the *motivating frame*, not a premise any result depends on. (The distinctiveness paragraph is half-way there.)

## Structural / empirical (lesser)

**S1 (MED-HIGH) — δ_J sign disfavored + stated inconsistently.** Part 1 §III writes |δ_J| = π/2 (magnitude); abstract and Part 3 (A) write δ_J = π/2 (signed +); mixing paper says "corpus commits to +π/2 while fits lean −π/2." NuFIT prefers δ ≈ −π/2. So either the claim is |δ|=π/2 (consistent, but sign not predicted) or +π/2 (disfavored ~1.5–2σ, falsifiable at DUNE/Hyper-K against NTE). Part 3 triage lists it clean with neither the sign tension nor the magnitude-vs-signed ambiguity surfaced. Since δ_J is the *only* near-term test of the bilateral CPN ontology (per O1), this is the one place the ontology meets data — and it leans against. Pick one statement; surface the sign status.

**S2 (MED) — CC "dissolution" oversells a contested move.** "A unimodular-type treatment … **removes the catastrophic term**." Unimodular/trace-free gravity is the Weinberg-1989 relocation: decouples vacuum energy from gravity but Λ reappears as a fine-tuned integration constant — not a consensus *solution* to the CC problem. "Does not predict Λ's value" (already admitted) is the integration-constant symptom. Reword "removes" → "relocates/reframes"; note it's a known non-consensus move.

**S3 (MED) — repaired §I no longer supports its title.** Title: "The photon paradox: why ds²=0 demands a new ontology." The corrected text states "proper time ⟺ rest energy ⟺ sub-luminal," which §I itself calls "the relativistic one" — plain SR. It then asserts NTE re-reads it as e-fold embedding, with no argument anything is "demanded." Retitle (e.g. "A relativistic correlation NTE re-reads geometrically"); don't claim ds²=0 forces the ontology when the corrected content shows it's standard SR.

---

## Clean (credit)
κ = 5.50 (0.83σ, CMB-S4) as the one sharp falsifier, honestly scoped ("derivation + closure, not ±0"); Majorana at 0νββ; S³-via-ℍ⊂𝕆 (point 7 genuinely closed, verified against source); no-numerology withdrawals; §II.0 even-handedness. The deposit passes an honesty audit. Its two empirical exposures are κ and the δ_J sign; its central ontology is inert with respect to both.

**Routing:** B1 + B2 back to AC (canonical edit) → Cursor re-render → do not deposit until fixed. O1 + S1 + S2 + S3 are Greg positioning/AC-edit calls. Manifest §3 snapshot needs the θ₁₃ and a₄ corrections regardless.

— CR, 2026-07-06. Fresh adversarial pass against the rendered v10.18.0; B1 is a >5σ-false claim currently in the Foundations paper.
