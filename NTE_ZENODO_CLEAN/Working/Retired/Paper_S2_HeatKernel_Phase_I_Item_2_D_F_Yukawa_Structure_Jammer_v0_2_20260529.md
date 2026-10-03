# Paper S2 Heat-Kernel Phase I Item 2 — D_F Block Structure (Yukawa + Majorana)
**Jammer v0.2 — 2026-05-29**

**Supersedes v0.1 (2026-05-29).** v0.2 folds in the Scratch adversarial-review verdict (gate dispositions R1–R7) + one Jammer-found substantive correction (light-neutrino seesaw denominator). Change log at §0.

**Status:** Phase I item 1 (D operator) shipped 2026-05-28. Item 2 v0.1 reviewed by Scratch 2026-05-29; this v0.2 carries the corrections. Phase II Cursor launch held pending Item 2-α / 2-β closure (R7) + Greg ratification.

---

## §0 — Change Log v0.1 → v0.2

1. **SEESAW DENOMINATOR CORRECTION (R1, Jammer-found):** v0.1 incorrectly fed the leptogenesis Majorana masses M₁ ≈ 5.4×10⁹ / M₂ ≈ 6.18×10⁹ GeV into the **light-neutrino** seesaw denominators. The corpus (Companion 7 §3.3/§7.3; Companion 10 §3.8; Companion 13 §4.4) uses the **single Cartan scale M_R ≈ 8.2×10¹⁴ GeV** in the seesaw denominator for **all three** light masses, with the Yukawa hierarchy (Y₃ = 1 vs Y_{ν2} = (8π)^{-1/3}) producing the mass splitting. The M₁/M₂ ≈ 10⁹ GeV masses are the **leptogenesis RH spectrum** (set η), structurally distinct from the light-seesaw scale. Corrected throughout §2–§4.
2. **R2 tag:** Y₃ = 1 labelled as **normalisation convention**, not derivation; Y_{ν2} = (8π)^{-1/3} labelled as **inheriting the un-closed status** of the (8π)^{1/3} prefactor (common-parent Seeley–DeWitt dependency).
3. **R3:** η held at **Tier A** (not promoted to Tier S) — tier-inversion guard (output not above weakest input) + Lesson #37 confirmation-bias guard.
4. **R4:** M₂ = M₁(1 + sin²θ₁₃) **demoted to provisional / observational-anchored placeholder**, removed from the ratified zero-parameter substrate. Rationale: sin²θ₁₃ = 0.022 is observational PMNS input inside a derivation-phase quantity + R4↔R6 deferral consistency. (NB: not demoted on grounds of P4 conflict — see §4.4 note.)
5. **R5:** §22.1 non-interference sentence added.
6. **R6:** Seeley–DeWitt annotated as the **common parent** of (8π)^{1/3}, Y_{ν2}, M₁ prefactor, and η-conditionality.
7. **R7:** Item 2-α (J₃(𝕆) → 𝕆⊕𝕆 embedding) and Item 2-β (ℋ_{S⁷} → ℋ_{S³}⊗ℋ_{S¹}⊗ℋ_F restriction governing the a₀ multiplier) carried as **explicit open items / Cursor-facing flags** (§5.3). Substrate is **not** complete until these close or are carried as named a₀ flags.

---

## §1 — D_F Block Structure (from Item 1)

$$D_F = \begin{pmatrix} M & T \\ T^\dagger & \bar{M} \end{pmatrix}$$

- **M** = 3×3 Dirac Yukawa matrix (neutrino sector)
- **T** = 3×3 Majorana mass matrix (RH neutrino)
- M = Hopf-S³ × S¹_{β_GB} × A_F with A_F = 𝕆⊕𝕆

**Grounding caveat (R7 / Item 2-α):** the block entries below are grounded in canonical species accounting only once the J₃(𝕆) → 𝕆⊕𝕆 embedding (Item 2-α) is closed. Until then they are structurally-motivated assignments, not embedding-derived. Flagged for Cursor.

---

## §2 — Two Distinct Mass Registers (Corrected)

The corpus carries **two structurally distinct Majorana mass registers** that v0.1 conflated. v0.2 separates them explicitly.

### §2.1 Register A — Light-Neutrino Seesaw (Single Cartan Scale)

**All three light masses use the Cartan-scale M_R in the seesaw denominator** (Companion 13 "Cartan-scale seesaw"):

$$m_{\nu_i} = \frac{Y_{\nu_i}^2 \, v_{\rm EW}^2}{M_R}, \qquad M_R = M_{\rm Pl}^{3/4} v_{\rm EW}^{1/4} \approx 8.2 \times 10^{14}\,\text{GeV (corpus §19.7)}$$

The **mass hierarchy comes from the Yukawa hierarchy**, not from per-generation Majorana masses:

| Mode | Dirac Yukawa | m_ν = Y² v²/M_R | Observed √Δm² | Ratio |
|------|--------------|------------------|---------------|-------|
| σ₃ (Cartan) | **Y₃ = 1** (convention) | 0.0738 eV | √Δm²_atm = 0.0741 eV | **0.997** ✓ |
| σ₁/σ₂ | **Y_{ν2} = (8π)^{-1/3}** (inherits un-closed prefactor) | 0.00860 eV | √Δm²_solar = 0.0087 eV | **0.993** ✓ |
| σ₁ | Y_{ν1} ~ 1.4×10⁻⁴ (bracket; open) | open | — | — |

Check: (8π)^{-2/3} × 0.0738 eV = 0.1167 × 0.0738 = 0.00861 eV ✓.

This is the single-scale (Cartan M_R) Yukawa-hierarchy-driven seesaw — a form of right-handed-neutrino dominance by the σ₃/Cartan heavy mode.

### §2.2 Register B — Leptogenesis RH Spectrum (Distinct)

The actual RH Majorana mass eigenvalues that govern leptogenesis kinematics:

| RH mode | Majorana mass | Source |
|---------|---------------|--------|
| M₁ (σ₁/σ₂) | (8π)^{1/3}(M_Pl² H_GB)^{1/3} ≈ 5.4×10⁹ GeV | Companion 10 Pathway α (H_GB quantization) |
| M₂ (σ₁/σ₂) | **PROVISIONAL** ≈ 6.18×10⁹ GeV | §2.3 — observational-anchored, deferred |
| M₃ = M_R (σ₃) | 8.2×10¹⁴ GeV | Corpus §19.7 — **coincides with Register-A Cartan scale** |

**M₁ sets the leptogenesis scale → η** (Davidson–Ibarra). **M₁/M₂ do NOT appear in the light-neutrino seesaw** (Register A). The σ₃ mode is the one point of coincidence: M₃ = M_R serves as both the heaviest leptogenesis mass and the Register-A seesaw scale.

**Honest-scope flag:** the mutual consistency of Register A (single-scale light seesaw) and Register B (three-mass leptogenesis spectrum) is a structural assumption inherited from Companion 10/13 — a form of sequential/single-RH-dominance. Full type-I seesaw consistency (m_ν = −m_D M_R^{-1} m_D^T with the full RH matrix) is **deferred to Phase II / Programme S** for verification. Not closed here.

### §2.3 M₂ — Provisional Placeholder (R4)

$$M_2 = M_1(1 + \sin^2\theta_{13}) \approx 6.18 \times 10^9\,\text{GeV} \quad\text{[PROVISIONAL — NOT in ratified substrate]}$$

This is demoted to a provisional, observational-anchored placeholder because:
1. **sin²θ₁₃ = 0.022 is observational PMNS input** (NuFIT 5.3), not a derived quantity — using it inside a derivation-phase mass splitting breaches honest scope if presented as derived.
2. **R4↔R6 consistency:** M₂ ab initio is a deferred item (§5.2); we cannot simultaneously defer M₂ and ratify a source formula for it.

The worksheet label "M₂ Z₂ Split **Derive**" should be retired — the content is observational-input-driven, not a derivation. M₂ does **not** feed the Register-A light masses, so its demotion is **cost-free** for the genuine-test results (m_{ν2}, m_{ν3}).

---

## §3 — σ-Eigenmode Assignment (Companion 7 / 10)

Three Pauli eigenmodes of the unresolved-neutrino su(2) structure:

- **σ₃-aligned (Higgs / Cartan direction):** strong Higgs coupling → Y₃ = 1; the σ₃ RH mode is the heavy Cartan-scale M_R (= M₃)
- **σ₁, σ₂-orthogonal (transverse to Higgs):** weak Higgs coupling → Y_{ν2} = (8π)^{-1/3}; residual Z₂ symmetry σ₁ ↔ σ₂

**Light-mass / mixing reconciliation with canonical P4 (R1):** P4 v0.2 fixes σ₃ ↔ ν₃ as the distinguished (Higgs-aligned) direction under normal ordering. Register A is consistent: Y₃ = 1 on σ₃ gives the **largest** light mass m_{ν3} (heaviest), matching P4's σ₃ ↔ ν₃, since all three share the same M_R denominator and the Yukawa ordering Y₃ = 1 > Y_{ν2} = (8π)^{-1/3} > Y_{ν1} directly sets the light-mass ordering m_{ν3} > m_{ν2} > m_{ν1}. No seesaw inversion subtlety arises once the single-scale Register-A structure is used (this is the v0.1 confusion resolved).

θ₂₃ ≈ π/4 from σ₁ ↔ σ₂ Z₂ (P4 v0.2; corpus line 26). The Z₂-breaking parameter (order sin²θ₁₃) perturbs θ₂₃ off π/4 **and** — in Register B — lifts the M₁/M₂ degeneracy. Same single breaking source, two observables; this is standard perturbed-Z₂ logic and is **not** forbidden by P4 (§4.4 note).

---

## §4 — Cross-Checks

### §4.1 Light Neutrino Masses (Tier A genuine tests)

Per §2.1: m_{ν3} = 0.0738 eV (0.997×), m_{ν2} = 0.00860 eV (0.993×). Both zero-parameter given (M_R, Y₃ = 1 convention, Y_{ν2} inheriting (8π)^{-1/3}). m_{ν1} open (bracket).

### §4.2 Leptogenesis η (held at Tier A, R3)

η = 6.1×10⁻¹⁰ via Davidson–Ibarra with M₁ framework-derivative; Planck+BBN η_B = 6.12×10⁻¹⁰ (ratio 0.997). **Held at Tier A, not promoted to Tier S:** η's zero-parameter status is conditional on the M₁ prefactor (8π)^{1/3}, which is downstream of the still-open Seeley–DeWitt computation (§4.5 common-parent). Promoting η above the tier of its weakest input would be a tier-inversion. Promote only after Phase II ties (8π)^{1/3} to a₄.

### §4.3 §22.1 Charged-Lepton Ratios — Non-Interference (R5)

Corpus §22.1 (Drive-canonical): m_μ/m_e = 207.0 ± 0.2, m_τ/m_μ = 18.0 ± 1.3. **The neutrino σ-eigenmode assignment shares no parameter with the §22.1 charged-lepton register** — the two operate on independent structural axes (Higgs-eigenmode polarisation vs charged-lepton embedding-depth) and the heat-kernel a₀/a₂/a₄ extraction does not consume the charged-lepton ratios. This is a non-interference statement, not a full numerical cross-check (the latter deferred to Phase III AC boundary engagement).

### §4.4 κ₀ Topological Protection + P4 Citation Note

κ₀ = 3/√(4π) from three Killing-spinor modes (Paper Kappa v10.17.2 §3); each σ-eigenmode contributes one Y₀₀ vertex; protected by dim(su(2)) = 3. Item 2's Yukawa/Majorana structure is consistent.

**P4 citation note (for Scratch):** the v0.1 review located the M₂ objection at "P4 §4.1," attributing to it a mass/mixing firewall ("mass eigenvalues do not participate in the Z₂ breaking that affects mixing"). On direct read of canonical P4 v0.2: there is **no §4.1** (the paper runs §1–§7; §4 has no subsections), and **no such firewall statement** appears — P4 is entirely about mixing angles, treats the σ-polarisation assignment of **mass eigenstates** as its input (ii), and ties a single σ₁↔σ₂ Z₂-breaking parameter (order sin²θ₁₃) to the θ₂₃ perturbation. A shared breaking parameter across mass-splitting and mixing is therefore natural, not forbidden. **M₂'s demotion stands on the observational-input + R4↔R6 grounds (§2.3), not on a P4 conflict.**

### §4.5 Common-Parent Annotation (R6)

The single **Seeley–DeWitt computation on M** (Phase II) is the **common parent** of four nominally-separate "canonical" supports:
- (8π)^{1/3} M₁ prefactor (Register B)
- Y_{ν2} = (8π)^{-1/3} (Register A; reciprocal of the same prefactor)
- the M₁-prefactor → η zero-parameter conditionality
- the a₄-route κ₀ confluence

These do not constitute four independent confirmations; they hang off one un-closed root. Making this visible prevents the illusion of independent support.

---

## §5 — Honest-Scope

### §5.1 Closed
1. M structure (σ-eigenmode columns: Y₃ = 1 convention, Y_{ν2} = (8π)^{-1/3} inherited)
2. Register separation (A: Cartan-scale light seesaw; B: leptogenesis RH spectrum)
3. Tier-A cross-checks: m_{ν3} (0.997×), m_{ν2} (0.993×); η at Tier A; θ₂₃ = π/4 from Z₂; §22.1 non-interference; κ₀ consistency

### §5.2 Deferred
1. Seeley–DeWitt a₀, a₂, a₄ → Phase II / Programme S (common parent, §4.5)
2. Y_{ν1} zero-parameter closure → bracket level (Companion 13 §5)
3. Register A↔B full type-I seesaw consistency → Phase II / Programme S (§2.2)
4. M₂ ab initio → deferred; provisional placeholder only (§2.3)
5. Boyle–Farnsworth full 𝕆 → 𝕆⊕𝕆 extension → Programme S
6. Charged-lepton Y_e/Y_μ/Y_τ → corpus §22.1 (not Item 2 scope)

### §5.3 R7 Carries — Cursor-Facing a₀ Flags (Substrate NOT complete until closed)
- **Item 2-α (J₃(𝕆) → 𝕆⊕𝕆 embedding):** grounds the D_F block entries in canonical species accounting; without it the §1/§2 entries are structurally-motivated placeholders, not embedding-derived. Feeds a₀.
- **Item 2-β (ℋ_{S⁷} → ℋ_{S³}⊗ℋ_{S¹}⊗ℋ_F restriction):** decides whether the a₀ finite-trace multiplier comes from a Hopf-projection of S⁷ onto its S³ base or from a direct unified-bundle reading. Feeds a₀ directly.

Both flagged by Scratch in the Item 1 triangle review (2026-05-28). Cursor must not launch heat-kernel on an unresolved a₀ multiplier — same recompute-risk the Item-1 convention patch (v0.2 gates 2/4) headed off.

---

## §6 — Phase II Substrate (Cursor) — Conditional

**Ready content** (Register A + σ-assignment + Yukawa structure):
- Y₃ = 1 (convention), Y_{ν2} = (8π)^{-1/3} (inherited), Cartan-scale M_R = 8.2×10¹⁴ GeV light seesaw
- σ-eigenmode → light-mass ordering (m_{ν3} > m_{ν2} > m_{ν1})

**Held content** (not for bake-in):
- M₂ provisional (do not treat as derived)
- η at Tier A (do not promote)
- a₀ multiplier — pending Item 2-α / 2-β

**Phase II deliverable (on launch):** Seeley–DeWitt a₀, a₂, a₄; heat-kernel κ₀ extraction (cross-check Paper Kappa §4.2 / Companion 12 Note 1); directional-α + dipole diagnostics; (8π)^{1/3} tree-level uniqueness.

---

**End Item 2 v0.2 — gate corrections folded; Phase II held on R7 (Item 2-α/2-β) + Greg ratification.**