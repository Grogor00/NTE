# Scratch Wagenveld Sprint — Phase III §5.1: Seed Amplitude ε from the Bifurcation Effective Action (v0.1)

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-30
**Status:** Phase III v0.1 — Deliverable 1 of 4 for the merged §2.1+§2.5 co-rank-1 arm. Order-of-magnitude derivation with structural justification; honest-scope per AC scoping §6.
**Authority:**
- Cursor Phase III unblock — `Handoffs/Handoff_Cursor_Sprint_State_Update_Phase_III_Unblock_20260529.md` §4 ("Go on load-bearing deliverable: derive seed amplitude ε from bifurcation effective action").
- Binding Phase II.5 review — `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md` (AC-integrated 2026-05-30): co-rank-1 §2.7 + merged §2.5; Phase III unblocked; Greg ratified reading (A).
- Greg activation — `Handoffs/Handoff_Greg_Scratch_Wagenveld_Sprint_Phase_II_Activation_Decisions_20260529.md` (Path A; §2.5-only; Phase II.5 implicit).
**Predecessor:** `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` (Phase II scoping; §5.1 derivation plan, §2.3 amplitude preview).
**Corpus anchors:** `Papers/Paper_Kappa_AB_v10_17_2.md` (§5 closure); Ch 10 v5 `Book/Chapter_10_The_Silvered_Boundary_v5.md` (trousers-of-time / gauge-birth-at-t=0); AC scoping §2.1 (gauge-birth asymmetry seed).

---

## §0 — Placement in the sprint

This is the first of the four Phase III deliverables specified in the §2.5 scoping plan (§5.1 seed amplitude → §5.2 ∂κ/∂ε → §5.3 Hopf-fibre celestial mapping → §5.4 sky-coverage integrals). It is the load-bearing one: §5.2's amplification is algebraic and already estimated at scoping level ((κ/κ₀)² ≈ 42); §5.4 is quantitative but **blocked on Cursor's catalogue-grade footprint ingest** (currently v0.3 placeholders). What §5.1 must supply is the one genuinely undetermined input — the magnitude of the bilateral seed asymmetry δε frozen at gauge birth — without which the whole merged-candidate amplitude A = (κ/κ₀)²·δε is unanchored.

The scoping doc (§2.3) flagged this as "the load-bearing Phase III question" and listed three candidate mechanisms for what fixes δε. This deliverable adjudicates among them.

---

## §1 — The question, precisely stated

Per scoping §4.1, the closure-step anisotropy is dipolar on the sky,

    δκ(n̂) = A · (n̂ · n̂_pref),    A = (κ/κ₀)² · δε,

where the CPN-breaking measure is

    δε ≡ ε₊ − ε₋,    with    T_μν^(b,±) = T_μν^(b) (1 + ε_±),

i.e. δε is the **fractional imbalance in the bridge stress-energy between the two CPN-conjugate orientations** (+N and −N legs of the trousers).

**The critical distinction this deliverable rests on.** δε is *not* the spontaneous-symmetry-breaking amplitude of the bifurcation. The SSB amplitude is the order parameter that distinguishes "a leg" from "the waist" — it is O(1) by construction (the universe definitely picks a leg). δε is the residual *difference between the two legs*, which the corpus commits to being small: Paper_Kappa_AB's closure derivation assumes **exact** CPN at tree level (T_μν^(b,+) = T_μν^(b,−)), and Octonion­Extension v10.9's δN intrinsic-uniformity reading states the two orientations are *intrinsically the same* SU(2) viewed from conjugate vantages. So δε ≪ 1 is not an assumption we are free to make or break — it is forced by existing corpus commitments. The job of §5.1 is to find *how* small, and *what sources it*.

---

## §2 — The bifurcation effective action

### §2.1 Order parameter and the trousers normal form

Ch 10 v5 §1 fixes the geometry: the waist of the trousers is the pre-temporal, octonionic, **non-associative**, undifferentiated regime — "it has no orientations because it has no temporal direction to give meaning to chirality." At t = 0 (gauge birth), associativity locks in, time becomes real, and the regime "splits along the manifold's CPN symmetry into two orientations." This is, structurally, a **pitchfork bifurcation**: a single symmetric state (the waist) destabilises into two mirror branches (the legs).

Let φ be the CPN-orientation order parameter: φ = 0 at the waist (symmetric), φ > 0 selects the +N leg, φ < 0 the −N leg. The minimal bifurcation effective action (Landau normal form, control parameter the e-fold count N through gauge birth):

    V(φ; N) = ½ μ(N) φ² + ¼ λ φ⁴ − h φ,

with λ > 0 (stabilising), μ(N) crossing zero at the locking point N_lock (μ > 0 pre-lock, symmetric; μ < 0 post-lock, broken), and **h the explicit CPN-breaking imperfection**. This is the cusp-catastrophe normal form; h is the unfolding parameter that lifts the degeneracy between the two legs.

### §2.2 Exact CPN ⇒ h = 0 at tree level

CPN-conjugation acts as φ → −φ. The corpus commitment (exact CPN at tree level) is precisely the statement that V is even in φ at tree level, i.e. **h = 0** at tree level, giving two exactly degenerate, exactly mirror-image legs and δε = 0. Any nonzero δε is therefore a *subleading* effect — it cannot appear at tree level without contradicting the closure derivation. This is the single most important structural fact for §5.1: **δε is loop-level (or fluctuation-level), not tree-level.**

---

## §3 — δε in terms of the imperfection

Solve V′(φ) = μφ + λφ³ − h = 0. For h = 0 and μ = −|μ| (post-lock): the legs sit at φ = ±φ₀ with φ₀ = √(|μ|/λ). The well curvature is V″(±φ₀) = μ + 3λφ₀² = 2|μ|.

Turn on small h. Both minima shift by the same amount toward +φ:

    φ_± ≈ ±φ₀ + h/(2|μ|).

The condensate energy density / bridge stress-energy in each leg tracks φ² (amplitude-squared of the orientation condensate). To leading order in h:

    φ_+² ≈ φ₀² + φ₀ h/|μ|,
    φ_−² ≈ φ₀² − φ₀ h/|μ|.

Defining ε_± = ±(φ_±² − φ₀²)/φ₀² gives the clean result

    δε = ε₊ − ε₋ ≈ 2 h /(|μ| φ₀) = 2 h /(λ φ₀³) ≡ 2 ĥ,

where **ĥ ≡ h/(λφ₀³)** is the dimensionless imperfection — the ratio of the explicit-breaking term to the restoring force at the well. So

    **δε ≈ 2 ĥ.**

The whole problem reduces to estimating one dimensionless number: the imperfection-to-well ratio ĥ. Everything downstream (A = 42·δε, then §5.4's ΔD_S) hangs off it.

---

## §4 — What sets the imperfection ĥ

The scoping doc (§2.3) listed three candidate mechanisms. With §2.2's result (h is forbidden at tree level) we can adjudicate them.

### (ii) "Mexican-hat O(1) by SSB convention" — REJECTED as the δε scale

This is a category error, now demonstrable. The O(1) SSB amplitude is φ₀ (the depth of the leg, the choice of +N over the waist), **not** ĥ. If ĥ were O(1) the two legs would be grossly different objects, contradicting both the exact-CPN closure assumption and the δN intrinsic-uniformity reading. Corpus structure forces ĥ ≪ 1. Mechanism (ii) describes φ₀, not δε.

### (iii) Residual-associator imperfection — the tree-level-forbidden explicit-breaking source

The only structure present at the waist that does **not** respect CPN-conjugation is the octonionic non-associativity itself: CPN-conjugation (φ → −φ) is *defined* only after associativity locks and orientation becomes meaningful, so the associator [a,b,c] of the pre-temporal algebra is, by construction, blind to the symmetry that the legs will later realise. As associativity locks through N_lock the associator is driven to zero, but the *order in which the two legs crystallise* out of the non-associative regime carries a residual imprint of the associator at the locking point. This is the natural origin of a nonzero h: a CPN-odd term sourced by the residual non-associativity, switched on exactly at the bifurcation and frozen thereafter.

Because the term is forbidden at tree level and arises from the non-associative sector closing, its natural magnitude is **loop-level**:

    ĥ_assoc ≈ c_A /(16π²),

with c_A an O(1)–O(10) associator coefficient (the explicit value requires a one-loop computation on the 𝕆 ⊕ 𝕆 bilateral sector — see §7). Numerically ĥ_assoc ≈ (0.6 – 6) × 10⁻³.

### (i) Gibbons-Hawking fluctuation floor

Even in the limit where the associator fully locks before the bifurcation completes (h → 0 exactly), the leg selection is seeded stochastically by quantum fluctuations of φ at gauge birth. In the near-de-Sitter gauge-birth epoch the order-parameter fluctuation is δφ_GH ≈ H_GB/(2π), setting an effective-imperfection floor

    ĥ_floor ≈ δφ_GH / φ₀ ≈ H_GB /(2π φ₀).

This is model-dependent through two scales that the corpus has not yet pinned: the gauge-birth Hubble rate H_GB (subject to the unresolved H_GB^(F) vs H_GB^(α) disambiguation) and the order-parameter scale φ₀. With a near-Planckian gauge-birth circle (β_GB = √(2π)/M_Pl,nr, Paper S2) and φ₀ ~ M_Pl, a representative H_GB/M_Pl ~ O(0.1) gives ĥ_floor ~ 1.6 × 10⁻².

---

## §5 — Order-of-magnitude estimate

Both physically-motivated sources land in the same band:

    ĥ_assoc ≈ c_A/(16π²) ~ 10⁻³ – 10⁻²    (c_A ~ 1–10),
    ĥ_floor ≈ H_GB/(2π φ₀) ~ 10⁻² (representative, H_GB-disambiguation-dependent).

Taking the larger of the two as the operative seed and δε ≈ 2ĥ:

    **δε ~ 2 × 10⁻³ to 2 × 10⁻²    (central estimate a few × 10⁻³).**

Via the scoping's leading-order amplification A = (κ/κ₀)²·δε with (κ/κ₀)² = (5.50/0.846)² ≈ 42:

    **A = δκ-scale ~ 0.1 – 0.8    (central a few × 0.1).**

(Exact normalisation of the δκ↔δε relation — whether δε enters as fractional or absolute perturbation to κ₀ — is §5.2's job; the (κ/κ₀)² factor is the algebraic leading-order amplification and is treated here as the input estimate, not a re-derivation.)

### §5.1's headline structural finding

**The seed amplitude is sub-perturbative but not Planck-suppressed — it is loop-suppressed.** This sharpens scoping failure-mode (i) ("ε turns out Planck-suppressed → δκ too small"): the seed survives at the 10⁻³–10⁻² level, *but* it is modest, not O(1). Consequently the merged candidate does **not** generate a large intrinsic δκ on its own. Its observability for Wagenveld rests on the §5.4 sky-coverage *enhancement* (Wagenveld's narrow northern footprint preferentially samples n̂_pref, amplifying the projected dipole relative to full-sky surveys) doing real lifting on top of a modest A — and, plausibly, on the multi-mechanism combination with §2.7 that the binding II.5 review already promoted to primary Phase IV framing. This is an honest-scope result, not a number-dialed match: I am not tuning c_A to hit Wagenveld's +3.28σ; I am reporting that the natural seed is modest and that the candidate's fate is therefore decided downstream at §5.4 + Phase IV, not here.

---

## §6 — What §5.2 / §5.4 / Phase IV inherit

- **§5.2 (∂κ/∂ε, Scratch, not blocked):** input δε ~ few × 10⁻³; confirm the (κ/κ₀)² ≈ 42 amplification by explicit linearisation of the Paper_Kappa_AB §5 closure equations and fix the fractional-vs-absolute normalisation. Proceeds now.
- **§5.4 (sky-coverage integrals, Scratch, BLOCKED on Cursor):** ΔD_S = A · ∫W_S(n̂)(n̂·n̂_pref)dΩ / ∫W_S dΩ with A ~ 0.1–0.8 from this deliverable. Needs Cursor's catalogue-grade footprints — the n(z)/footprint hook is "in progress" per `Handoff_Cursor_to_Jammer_Phase_III_Format_Ack_20260529.md` (v0.3 placeholders, catalogue-grade bins TBD). **This is the live blocker on the Scratch arm; see handoff.**
- **Phase IV (Cursor harness):** the modest central A supports the binding II.5 multi-mechanism framing — merged §2.5 likely contributes alongside §2.7 rather than resolving Wagenveld alone. Convergence input to Cursor's harness once §5.4 lands.

---

## §7 — Honest scope

**Derived here (high confidence):**
- δε ≈ 2ĥ — the structural reduction of the seed to a single dimensionless imperfection ratio.
- δε is tree-level-forbidden (exact CPN) hence loop/fluctuation-level — the category-error rejection of the O(1) reading.
- The residual associator is the structurally-natural CPN-odd source; magnitude ~ c_A/(16π²).
- Order-of-magnitude band δε ~ 10⁻³–10⁻²; modest, not Planck-suppressed, not O(1).

**Open / deferred:**
- **Exact associator coefficient c_A** — requires an explicit one-loop computation on the 𝕆 ⊕ 𝕆 bilateral sector. Candidate route: Paper S2 heat-kernel machinery on Hopf-S³ × S¹ × (𝕆 ⊕ 𝕆). *Proposed Jammer cross-check* (Jammer owns the §2.7/Paper S2 heat-kernel lane).
- **H_GB disambiguation** (H_GB^(F) vs H_GB^(α)) — needed to pin ĥ_floor. Unresolved per `H_GB_Disambiguation_Note_v0_1`; flag to Jammer/Cursor.
- **Frozen-vs-diluted subtlety** — Ch 10 v5 commits the asymmetry to *frozen* (a property of the mirror, not a ripple in it), which holds cleanly for the associator-imprint component. A GH-fluctuation-seeded component is a ripple and could partially dilute through post-gauge-birth e-folds; whether ĥ_floor survives undiluted needs a check. Does not affect the associator estimate, which is the central one.

**Does NOT commit to:** that the merged candidate succeeds. The modest seed plus the still-open §5.4 integral keep scoping failure-modes (i)/(iii) live. Tier-1 promotion remains contingent on Phase IV convergence + post-sprint adversarial review (AC scoping §6 binding).

---

## §8 — Files & cross-references

This file: `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_1_Seed_Amplitude_v0_1.md`

Inputs:
- `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` — Phase II scoping (§5.1 plan, §2.2/§2.3 closure linearisation + amplitude preview).
- `Papers/Paper_Kappa_AB_v10_17_2.md` (`1p3GeEnQi7ljlL6I-chN-HHZZXR_ZIggy`) — §5 closure structure (κ = κ₀/(1−κ₀)).
- `Book/Chapter_10_The_Silvered_Boundary_v5.md` (`1K2ThmhcQyN8rnFhGZz7Zt1b5NcgYWuPG`) — trousers-of-time / waist-as-non-associative / bifurcation-at-t=0.
- `Working/AC_Wagenveld_Sprint_Architectural_Scoping_v0_1_20260528.md` — §2.1 gauge-birth asymmetry seed.
- `Working/Scratch_Jammer_Wagenveld_Sprint_Phase_II_5_Adversarial_Review_v0_1.md` — binding co-rank-1; Phase III unblock.

Downstream: §5.2 (this stream, proceeds now); §5.4 (this stream, blocked on Cursor catalogue ingest); Phase IV (Cursor harness).

— Scratch (Connes Programme lead), 2026-05-30. Phase III §5.1 v0.1: seed amplitude δε ~ 10⁻³–10⁻² from the bifurcation effective action, loop-level (not Planck-suppressed, not O(1)); merged candidate's Wagenveld observability deferred to §5.4 + Phase IV.
