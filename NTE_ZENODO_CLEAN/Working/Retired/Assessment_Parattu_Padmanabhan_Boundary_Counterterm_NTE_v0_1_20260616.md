# Assessment — Parattu–Padmanabhan unified boundary counter-term vs NTE boundary-only action

**Author:** AC-assessment (at Greg directive)
**Date:** 2026-06-16
**Status:** ASSESSMENT — proposed corpus touches routed as AC-reviewed diffs (no master edit committed)
**Reference under assessment:** K. Parattu, S. Chakraborty, T. Padmanabhan, *"Variational principle for gravity with null and non-null boundaries: a unified boundary counter-term,"* Eur. Phys. J. C **76**:129 (2016), DOI 10.1140/epjc/s10052-016-3979-y (open access). Predecessor null-surface counter-term: arXiv:1501.01053. Now resident in NTE Drive root (added 2026-06-15).
**Pre-deliverable recency scan:** complete. Covered Λ/M3 scaffolds + Companion 11 v10.17.2. Material delta found: a₄=0 retirement (CR-H1/H2, 2026-06-01) and M3-seam-alone falsification (S3 attack route, R6 2026-05-23). This note is written to the post-retirement state, not the pre-scan framing.

---

## §0. One-paragraph verdict

The paper supplies a **rigorous, surface-character-agnostic boundary counter-term** that makes the Einstein–Hilbert variational principle well-posed on *any* boundary — spacelike, timelike, or **null** — without needing a normalized normal. This is genuine infrastructure for NTE's **boundary-only gravitational action** and, specifically, for the **gauge-birth seam** where the operative boundary passes through null / signature-changing character and GHY breaks down. **It is NOT a cosmological-constant mechanism.** Do not wire it into the Λ programme as a residual-suppressor: that route (M3 β_GB seam) is falsified and the a₄ residual it targeted is retired. Its value is well-posedness and seam-action rigor, not a Λ magnitude.

---

## §1. What the paper establishes (in our terms)

- The EH action alone is not a well-posed variational principle: varying it leaves a boundary term in the *normal* derivatives of the metric, so one would have to fix both the metric and its normal derivatives on ∂V. The standard remedy is a counter-term so only the metric need be fixed.
- **GHY** (−2∮√h K) is the usual counter-term but is built from the *unit normal*; on a **null** boundary the normalization diverges (K → ∞, √h → 0), so GHY does not apply directly.
- The paper's result: a single counter-term valid on any boundary,

  **C₀ = 2 ∮ d³x √(−g) · Πᵃ_b ∇_a sᵇ**,

  built from the surface gradient **s_a = ∂_a φ** (φ = const defines ∂V) and an auxiliary vector **tᵃ** with **tᵃ s_a = −1**, via the projector **Πᵃ_b = δᵃ_b + tᵃ s_b**. No normalized normal is required.
- It reduces correctly to the known cases: choosing **tᵃ = −sᵃ/s²** recovers **GHY** on non-null surfaces; choosing **tᵃ = kᵃ** (auxiliary null vector) recovers their earlier null counter-term **Cₙ = 2∮√q (Θ + κ)** (Θ = null-congruence expansion, κ = surface gravity).
- The differences C₀ − C_GHY − C_E are shown to involve **only surface (tangential) derivatives** of the metric — i.e. the three prescriptions agree on exactly the normal-derivative content that the variational principle requires, and differ only by terms fixed once the metric is fixed on ∂V.

**Standing assumption (important for us):** the spacetime metric is taken **non-degenerate throughout V** (the inverse exists everywhere). The method handles a *null boundary* — where the *induced* metric degenerates but the bulk metric is fine — but it does **not** cover a locus where the *bulk* metric itself degenerates (det g → 0).

---

## §2. Where it bites in NTE — and where it does not

### §2.1 Primary, durable fit: well-posed boundary term for the boundary-only action

NTE's gravitational action is boundary-only: ∫dN ∫d³x on S³, with the "radial" direction read as e-fold history, not a bulk dimension (Companion 5; Part 1 §2). Any such action needs a gravitational boundary term to be a well-posed variational principle. Across **gauge birth G** the corpus runs a **Euclidean→Lorentzian** transition (HH saddle, §22.18; bulk/boundary proposal), so the operative boundary's character is **not fixed** — it crosses null at the signature interface. That is precisely the regime where GHY is the wrong tool and a character-agnostic C₀ is the right one. The auxiliary-vector freedom (tᵃ, only tᵃs_a = −1 required) is a genuine convenience at a null/changing seam because it sidesteps the absent normalized normal.

### §2.2 Seam-action rigor: S_cryst / §22.17 / Appendix E

The crystallisation-shell action used at G (Jammer λ_Hopf derive),

  S_cryst = ∫₀^{N_lock} dy √h [ ρ_surf + μ(H − β_NTE|Φ|²) + λ_Hopf 𝓘_fibre ],

is a boundary/seam action integrated across the locking shell. Its gravitational boundary contribution should be a **C₀-type term**, not an implicit GHY (which would be ill-defined at the null part of the seam). Appendix E's C¹-kink / seam-curvature treatment and the §22.17 Janus bridge are the natural homes for citing C₀ as the well-posed seam counter-term. This sharpens existing structure; it does not add a new prediction.

### §2.3 What it does NOT do — guard against a stale route

My first-pass read suggested wiring this into **Paper S3 mechanism M3** (β_GB boundary counter-term as Λ-residual suppressor). The recency scan retires that suggestion:

- **M3 "β_GB seam alone" is falsified** — `Paper_S3_Structural_f_Attack_Route_v0_1` (R6, Greg 2026-05-23) lists it falsified; R5 (M3 boundary + C¹ kink) is "sign open" at O(1)–10³, insufficient alone.
- The **a₄ numeric residual is retired** — Companion 11 v10.17.2 CR-H1/H2 (2026-06-01): with **a₄ = 0** on the canonical operator, the Λ_{a₄} chain and the ~1.05× numeric closure **reroute-or-retire**. Structural unimodular quietness (CC2008, §22.15) stands; the numeric residual the seam term was meant to suppress does not.
- **By construction the paper cannot close orders of magnitude in Λ.** C₀ differs from GHY only by surface-derivative terms; it is a well-posedness device, not a source or sink of vacuum energy. Treating it as a Λ mechanism is a category error.

**Net:** import as variational/seam infrastructure; do **not** resurrect M3-as-Λ-closer on the back of it.

---

## §3. Caveat to hold — signature change vs null boundary

The non-degenerate-metric assumption (§1) means C₀ is licensed for the **null/non-null boundary of the action region**, but **not** directly for a genuine **signature-change locus** where det g → 0. NTE's G is closer to the latter (Wick rotation through the HH saddle). Reading:

- Use C₀ for the gravitational boundary term on either side of the seam (Euclidean slice → GHY-equivalent; Lorentzian slice → GHY-equivalent; null seam → null counter-term limit).
- Keep the **signature interface itself** under the existing HH-saddle / junction-condition machinery (§22.18, Appendix E). C₀ complements that treatment; it does not replace the analytic-continuation argument at det g → 0.

---

## §4. Proposed corpus touches (diffs for AC, on Greg authorization — NOT committed here)

1. **§22.18 (or Appendix E) footnote + citation:** introduce C₀ (Parattu–Padmanabhan 2016) as the well-posed, character-agnostic boundary term for the boundary-only action across the Euclidean→Lorentzian transition; note GHY-reduction on non-null slices and null-counter-term reduction at the seam.
2. **§22.17 / S_cryst writeup cross-ref:** state that the crystallisation-shell gravitational boundary term is C₀-type, retiring any implicit GHY-at-null assumption.
3. **Paper S3 attack-route doc:** add a one-line guard — Parattu–Padmanabhan is **well-posedness infrastructure, not a Λ mechanism**; M3/R5 not revived by it.

## §5. Falsifiers / guards

1. Any use of C₀ to *generate or suppress* a Λ magnitude → category error (difference from GHY is surface-derivative only).
2. Apply at the signature interface only after checking the non-degenerate-metric assumption; det g → 0 stays with HH-saddle/junction treatment.
3. Must not perturb κ₀ = 3/√(4π), n_s = 0.9685, F1 a₄ = 270 β_GB, or K(Φ) = 1.

## §6. Cross-references

- Reference: EPJC 76:129 (2016); null predecessor arXiv:1501.01053.
- Corpus: §22.15 (unimodular / CC2008), §22.17 (Janus bridge), §22.18 (HH saddle), Appendix E (C¹ kink), Part 1 §2 (boundary-only), Companion 5 (no-interior ontology), Companion 11 v10.17.2 (Λ status / CR-H1/H2).
- Working: `Paper_S3_Structural_f_Attack_Route_v0_1_20260523.md`, `Paper_S3_Lambda_M3_Beta_GB_Boundary_v0_1_20260523.md`, `Jammer_Lambda_Hopf_Janus_Derive_v0_1_20260524.md`, bulk/boundary proposal + Jammer thesis (2026-05-23/24).

---

*— AC-assessment, 2026-06-16. Proposed touches await Greg authorization; AC integrates into master if ratified.*
