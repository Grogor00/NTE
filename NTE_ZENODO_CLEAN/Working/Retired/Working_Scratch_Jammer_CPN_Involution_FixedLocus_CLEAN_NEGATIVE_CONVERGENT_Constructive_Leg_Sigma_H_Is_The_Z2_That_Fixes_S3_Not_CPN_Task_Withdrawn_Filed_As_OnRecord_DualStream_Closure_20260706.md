# Working — Scratch (constructive) + Jammer (adversarial): CPN-involution fixed-locus on S⁷ — JOINT NOTE. VERDICT: CLEAN NEGATIVE, CONVERGENT. S³ is *not* forced as the fixed locus of the canonical CPN; the ℤ₂ that *does* fix S³ is the G₂-involution σ_ℍ (centraliser SO(4)) — i.e. the ℍ-subalgebra grounding restated, not CPN.

**Streams:** Scratch (constructive pathway) + Jammer (adversarial check) — joint integration per the AC dual-stream deliverable spec.
**To:** AC (task issuer); Cc: Greg (authorising).
**Date:** 2026-07-06
**Priority:** P1-originated; see status below.

**Status / provenance (read first).** The originating task (`Handoff_AC_to_Scratch_Jammer_CPN_Involution_FixedLocus_Pathway_20260705`) was **WITHDRAWN by AC the same evening** (`WITHDRAWN_Handoff_AC_to_Scratch_Jammer_CPN_Involution_FixedLocus_20260705`): canonical v10.18 already grounds S³ via the ℍ-subalgebra route in Part 2 §8.5–8.6 and Part 3 §XVII, the "S⁷/ℤ₂ fixed locus" phrasing is already purged from both, and CR point 7 is closed on the ℍ grounding — so there is no live corpus claim to establish or refute. This joint note is therefore **not** actioning a live task. It is filed at Greg's direction as an on-record, dual-stream closure of the deposit's most-scrutinised geometric identification: a permanent record that the fixed-locus reading was *rightly* retired on the mathematics, not merely dropped as phrasing. No corpus change is proposed.

**Sources.** Ratified CPN definition P0.10b (Paper_Susskind_v0_4: CPN as the modular conjugation of the Janus crossed product on A_F = 𝕆₊ ⊕ 𝕆₋); Octonionic-origin standalone v0.2 §3.1/§3.3 (SO(4) ⊂ G₂ stabilises ℍ; S³ ≅ SU(2) = unit quaternions ⊂ S⁷, identified with SU(2)_L); Part 2 v10.18 §VIII.8.5–8.6; Part 3 v10.18 §XVII. Jammer's adversarial leg: `Working_Jammer_Adversarial_CPN_Involution_FixedLocus_CLEAN_NEGATIVE_...20260706` plus its triangulation amendment.

---

## §0 — Joint verdict (one line)

**CLEAN NEGATIVE, CONVERGENT.** The canonical CPN (P0.10b) does not fix S³ on the relevant S⁷; its fixed locus is a whole S⁷ (the CPN diagonal). There *is* a canonical ℤ₂ whose fixed locus on the unit octonions is exactly S³ — the G₂-involution σ_ℍ with centraliser SO(4) — but σ_ℍ **is not CPN**; it is precisely the involution that defines the ℍ-subalgebra, so "S³ = fixed locus of σ_ℍ" is a coordinate-free *restatement of the ℍ-subalgebra grounding*, not a CPN-orbifold derivation. The deposit's original "S³ = S⁷/ℤ₂ fixed locus, CPN as Pin⁻ on that orbifold" conflated two distinct ℤ₂'s. AC's disposition (retire the fixed-locus phrasing; ℍ grounding stands alone; Patch 5 v2 as written) is correct on the mathematics. Both legs agree; no PATHWAY was found.

---

## §1 — The question (per the withdrawn AC handoff)

The deposit grounded S³ two ways: (1) **established** — S³ is the unit sphere of the quaternionic subalgebra ℍ ⊂ 𝕆 surviving the 𝕆 → ℍ associativity transition, stabilised by SO(4) ⊂ G₂, the same ℍ giving SU(2)_L; (2) **asserted, not established** — "S³ as the S⁷/ℤ₂ fixed locus," with CPN as "Pin⁻ on the ℤ₂ orbifold," claiming the CPN involution geometrically fixes exactly S³. The task: determine whether (2) is derivable, or establish the clean negative. Guardrail: the deliverable is a *finding, not a rescue* — do not assert an identification to close CR point 7 (the κ₀-"3" failure mode).

Scratch owns the constructive leg (§2–§4); Jammer owns the adversarial leg (§5); convergence in §6.

---

## §2 — Constructive leg: the canonical CPN fixes S⁷, not S³

CPN, as ratified in P0.10b, is not a single-S⁷ operation. It acts on the doubled Janus algebra A_F = 𝕆₊ ⊕ 𝕆₋ as the antilinear, sector-swapping modular conjugation

    CPN(a, b) = (b̄, ā),   a ∈ 𝕆₊, b ∈ 𝕆₋,   ¯ = octonion conjugation.

Its fixed locus is immediate. CPN(a,b) = (a,b) requires a = b̄ and b = ā, which are the same condition (b = ā ⟺ a = b̄). So the fixed set is the **CPN diagonal**

    Δ = { (a, ā) : a ∈ 𝕆 },

an 8-real-dimensional subspace. Intersecting with the unit sphere of A_F (|a|² + |b|² = 1, i.e. |a|² = 1/2 on Δ) gives a sphere of radius 1/√2 in 𝕆 ≅ ℝ⁸ — a whole **S⁷**, parameterised by a ∈ 𝕆. The physical S³ is *not* this fixed locus; S³ has codimension 4 inside it.

So on the object CPN actually lives on, the CPN fixed locus is S⁷. To obtain "S³ = S⁷/ℤ₂ fixed locus" one must (i) collapse the doubled algebra to a single S⁷, and (ii) supply a *second*, independent involution cutting that S⁷ down to S³. Step (ii) is exactly what P0.10b does not provide: the C∘P∘N decomposition has free convention knobs (which C, which P), and only a specific tuned choice — P chosen to undo, on Im(ℍ), the sign flip that octonion-conjugation C imposes there — yields the ℍ-complement flip. Nothing in the modular-conjugation definition fixes that choice. This is the constructive form of the clean negative: **the S³-cut is imposed, not descended.**

(Sanity checks on the two extreme single-S⁷ conventions: bare octonion conjugation C flips all seven imaginary directions, fixing only the real axis → S⁰; the identity fixes all of S⁷. S³ requires flipping exactly the four ℍℓ directions and no others — a measure-zero convention among the choices, and the one that has to be *put in by hand*.)

---

## §3 — The ℤ₂ that *does* fix S³ is σ_ℍ, and it is a canonical G₂-involution

The constructive value-add over "no pathway": identify precisely which involution fixes S³, and show what it is.

Take S⁷ = unit octonions ⊂ 𝕆 and the Cayley–Dickson split 𝕆 = ℍ ⊕ ℍℓ (ℍ associative; ℓ a unit imaginary octonion orthogonal to ℍ). Define

    σ_ℍ(p + qℓ) = p − qℓ,   p, q ∈ ℍ.

Facts:

1. **σ_ℍ is an automorphism of 𝕆** (the grade/doubling involution of the Cayley–Dickson construction), so σ_ℍ ∈ Aut(𝕆) = G₂. It is order 2.
2. **Its fixed subalgebra is exactly ℍ.** On Im(𝕆) = ℝ⁷ it acts +1 on Im(ℍ) = ℝ³ and −1 on ℍℓ = ℝ⁴; the real axis is fixed. Fixed set = ℝ ⊕ Im(ℍ) = ℍ (4-dimensional).
3. **Its fixed locus on S⁷ is therefore the unit sphere of ℍ = S³.**
4. **Its centraliser in G₂ is SO(4) ≅ (SU(2)×SU(2))/ℤ₂** — the stabiliser of the quaternionic subalgebra. (Consistent counting: dim G₂ = 14, dim SO(4) = 6; the symmetric space G₂/SO(4) has dim 8, the quaternionic real form. G₂ has a single conjugacy class of involutions, with this centraliser and fixed subalgebra ℍ.)

So the statement "S³ is the fixed locus of a ℤ₂ acting on S⁷" is **true and forced** — for the ℤ₂ = ⟨σ_ℍ⟩. But this SO(4) is *the very same* SO(4) ⊂ G₂ that the standalone §3.1/§3.3 uses to stabilise ℍ, and whose SU(2) factor is SU(2)_L. Hence σ_ℍ is not new structure: it is the ℍ-subalgebra grounding written in involution/fixed-locus language. Nothing is gained or lost by phrasing it either way — they are the same fact.

**The decisive point:** σ_ℍ ≠ CPN. σ_ℍ is a *linear octonion automorphism* (an element of G₂) fixing a 4-plane; CPN is an *antilinear, sector-swapping modular conjugation* on the doubled algebra fixing an S⁷ diagonal. They are different maps on different spaces with different fixed loci. Identifying "the ℤ₂ orbifold whose fixed locus is S³" with CPN — as the retired phrasing did — conflates σ_ℍ with CPN. The correct reading keeps them apart.

---

## §4 — Constructive check against the two S⁷ readings, and the spectral-triple angle

**Hopf reading.** With S⁷ = total space of the quaternionic Hopf fibration S³ → S⁷ → S⁴, coordinates (h₁, h₂) ∈ ℍ², the involution (h₁, h₂) ↦ (h₁, −h₂) fixes the fibre {h₂ = 0} ≅ S³. This is a legitimate S³-fixing ℤ₂, but again a *chosen* fibre-flip, differently embedded from σ_ℍ, and still not CPN. Robust across both S⁷ readings: an S³-fixing involution always exists, is never unique, and is never the ratified CPN.

**Connes / spectral-triple angle (A_F = 𝕆 ⊕ 𝕆).** In the finite real spectral triple, the real structure J is the charge-conjugation/modular operator, and for the doubled algebra it acts as the swap-conjugation (a,b) ↦ (b*, a*) — i.e. it is CPN, and its fixed locus is the diagonal, as in §2. The S³ does **not** enter through J's fixed locus; it enters through the *subalgebra* structure ℍ ⊂ 𝕆 (equivalently through the SU(2)_L factor sitting inside the finite algebra). The grading γ and order-one condition do not cut S⁷ to S³ either. So the NCG reading independently confirms: S³ is subalgebra data, not modular-involution-fixed-locus data. There is no Connes-side pathway restoring the CPN-orbifold claim.

---

## §5 — Adversarial leg (Jammer), summarised and credited

Jammer recomputed the fixed loci from scratch without importing a convention and reached the same negative by an independent route. Key results (Jammer Working memo §5, §9):

- Natural restrictions of the ratified P0.10b CPN to a single S⁷ — single-sector restriction (undefined; CPN doesn't self-map a sector), diagonal embedding {(a,ā)} (→ S⁷), real diagonal a = ā (→ S⁰), bare unitary swap τ (→ S⁷) — **none produces S³.**
- Among four candidate involutions on S⁷ independent of P0.10b: α bare octonion conjugation → S⁰; β ℍ-complement flip → S³; γ quaternionic swap on ℍ² → S³ (different embedding); δ antipodal → ∅. Only β, γ fix S³, they fix *different* S³'s, and **neither is the ratified CPN.**
- Four adversarial self-checks (Farnsworth non-associative NCG selection; bilateral 𝕆₊/𝕆₋ ~ ℍ/ℍℓ alignment; CPN redefinition; Volovik/Rovelli external references) — none forces the identification; each would be a *choice* or a *replacement*, not a derivation.
- Triangulation amendment: the contested phrasing is orphaned from all three canonical v10.18 sources (Part 2 §VIII.8.5–8.6, Part 3 §XVII, standalone v0.2 §3.3), all of which already ground S³ via ℍ-subalgebra.

Scratch's β (§3 above) is the same map as Jammer's β, now identified precisely as the G₂-involution σ_ℍ with centraliser SO(4) — closing the small gap between "an involution that happens to fix S³" and "the involution that defines ℍ."

---

## §6 — Convergence (the joint outcome AC asked for)

| | Scratch (constructive) | Jammer (adversarial) |
|---|---|---|
| Canonical CPN fixed locus | S⁷ (diagonal Δ) | S⁷ (diagonal) |
| Any S³-fixing ℤ₂? | Yes — σ_ℍ (G₂-involution, centraliser SO(4)) and Hopf fibre-flip | Yes — β, γ |
| Is that ℤ₂ = CPN? | **No** | **No** |
| S³ forced by CPN? | **No** | **No** |
| S³ grounding that *is* forced | ℍ-subalgebra (= σ_ℍ fixed locus, same fact) | ℍ-subalgebra |

**CONVERGENT → retire the "S⁷/ℤ₂ fixed locus" reading; the ℍ-subalgebra grounding is the sole honest one; Patch 5 v2 as written is correct.** No divergence; AC adjudication not required.

---

## §7 — Consistency with Pin⁻ selection and Majorana forcing (unchanged)

Retiring the S³-fixed-locus phrasing does not disturb the two CPN machinery items that stand on their own terms:

- **Pin⁻ selection** (Part 1 §VI) is a consequence of a ℤ₂ action + spin-structure choice; multiple ℤ₂ actions on S⁷ admit Pin⁻ lifts, and none of them needs to be σ_ℍ. Independent of the fixed-locus reading.
- **κ₀ < 1 convergence → Majorana** (Companion 10) depends on the σ Cartan-mode count (dim adj SU(2) = 3) and the Y₀₀ monopole projection, not on any S⁷/ℤ₂ fixed-locus identification.

Both survive verbatim. This matches Jammer §5 and AC's withdrawal note ("those are grounded on their own terms and do not depend on S³ being the orbifold fixed locus").

---

## §8 — Disposition for AC

1. **No corpus change proposed.** Canonical v10.18 already reflects the correct grounding; the task was withdrawn on that basis. This note is the on-record mathematical closure behind the withdrawal.
2. **Patch 5 v2 as written is correct** and honestly scoped.
3. **Optional, at AC's discretion only:** if a coordinate-free restatement of the ℍ grounding is ever wanted, S³ may be described as "the fixed locus of the G₂-involution σ_ℍ that defines ℍ (centraliser SO(4))." This is *equivalent* to the current ℍ-subalgebra wording and would name σ_ℍ, **explicitly not CPN** — it does not restore the CPN-orbifold phrasing and carries no new content, so there is no reason to prefer it over the current wording. Recorded for completeness, not recommended.
4. **CR point 7 remains closed** on the ℍ grounding.

— Scratch (constructive) + Jammer (adversarial), 2026-07-06. Joint note per AC dual-stream deliverable spec; filed as on-record closure of a withdrawn task at Greg's direction.
