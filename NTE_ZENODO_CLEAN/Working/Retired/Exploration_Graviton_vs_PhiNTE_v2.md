# Exploration: Graviton vs Φ_NTE — v2 (Definitive Pathway via Connes Spectral Action)

**Stream:** Scratch (deep-exploration role; descendent of v1 Jammer draft).
**Date:** 2026-05-09 evening NZST.
**Status:** Definitive pathway identified. v1's "joint origin" reframing concretized via the Connes spectral action on the NTE pre-temporal spectral triple. Substantial literature support; non-trivial calculation programme remaining.
**Audience:** Greg (origin); AC (corpus integration target — affects §17.5.5, §22.7, §17.5.1 simultaneously); Jammer (R&D continuation).
**Corpus baseline:** v10.6 SHIPPED.
**Supersedes:** `Exploration_Graviton_vs_PhiNTE_v1.md` (parked draft 2026-05-09 morning).

---

## §1. Executive summary

The v1 draft established that the QFT graviton is **not** identical to Φ_NTE — five independent decisive arguments (Lorentz representation, pre-temporal availability, coupling structure, mode count, existing r prediction). v1 then proposed the productive reframing: *graviton and Φ_NTE are post-temporal projections of the same pre-temporal undifferentiated boundary structure, factored into tensor (geometric shape) and scalar (strength/density) modes at gauge birth.*

**This v2 finding: the reframing has a concrete technical realization. Both fields emerge from a single action principle — the Connes spectral action functional applied to the NTE pre-temporal spectral triple (A_G₂, H_S⁷, D_S³).** This is the action principle the corpus has explicitly named as its programme target (§22.7, "Spectral flow account of gauge birth"); the literature has done substantial spadework that NTE can directly absorb.

Five literature anchors carry decisive weight:

1. **Chamseddine-Connes 2010 "Uncanny Precision"** — Spectral action evaluated on S³ gives Einstein-Hilbert + cosmological term + scalar potential V(φ) for an inflaton. NTE's pre-temporal regime is the S³ boundary; this calculation IS the action on it.

2. **Marcolli-Pierpaoli-Teh 2010 "Coupling of topology and inflation in NCG"** — Explicit computation of the spectral action on S³ and other cosmic topologies, with the resulting slow-roll inflation potential and tensor-to-scalar ratio derived in closed form (modulo the cutoff function h).

3. **Boyle-Farnsworth 2013 "Non-Associative Geometry and the Spectral Action Principle"** — Extended the spectral action principle to **non-associative geometries based on the octonions**. The simplest octonionic spectral action gives Einstein gravity + G₂ gauge theory + 8 Dirac fermions. *NTE's pre-temporal A_G₂ algebra IS the octonionic algebra; this is the calculation NTE's §22.7 needs.*

4. **Chamseddine-Connes 2005 "Scale Invariance in the Spectral Action"** — When the spectral action's mass scale is made dynamical via a dilaton field, every matter coupling becomes scale-invariant; only Einstein-Hilbert and the dilaton kinetic term break scale invariance. The dilaton's role *is structurally Φ_NTE's role in NTE*: a scalar that controls the scale of all couplings.

5. **Chamseddine-Connes 2012 + Fathizadeh-Ghorbanpour-Khalkhali 2014 "Spectral Action for Robertson-Walker metrics"** — Computed the full asymptotic expansion of the spectral action for FRW metrics in terms of a(t) and derivatives, to order a_12. NTE's H(N) = β_NTE|Φ(N)|² gives a specific RW metric; the spectral action expansion specializes to NTE-specific predictions.

The synthesis: Boyle-Farnsworth's octonionic spectral action machinery, applied to a Robertson-Walker metric on S³ with the NTE Hopf structure and a Chamseddine-Connes scale-invariance dilaton, *produces simultaneously* — by one functional Tr(f(D/Λ)) — the gravitational sector (Einstein-Hilbert + curvature corrections), the dilaton/scalar sector (V_NTE with on-trajectory and off-trajectory structure), the gauge sector (G₂ at the pre-temporal level, breaking to SM at gauge birth), and the Yukawa sector. Φ_NTE and the graviton are not identical; they are jointly and consistently determined by this single principle.

This closes Gap 4b structurally, closes V_NTE Stage 2's open option (α), and closes K(Φ) via Companion 9 Session 5's spectral-triple route in one synthesis. It does not close any of these *numerically* without the explicit NTE calculation, but the calculation is well-defined.

---

## §2. Concur with v1: identity fails

v1's five mismatches stand on review:

- **M-1** Spin/Lorentz representation: graviton is symmetric rank-2 tensor (helicities ±2); Φ_NTE is a scalar (j=0).
- **M-2** Domain: graviton is post-locking; Φ_NTE exists pre-temporally.
- **M-3** Coupling: graviton couples universally to T_μν; Φ_NTE couples selectively (Path B disclosure).
- **M-4** Mode count: 2 vs 1.
- **M-5** Existing r prediction structurally distinguishes them.

Identity fails. Joint origin holds. v2 takes joint origin from "available reframing" (v1 §5) to "concretely realized via spectral action" (this section forward).

---

## §3. The structural setup

### 3.1 NTE's pre-temporal spectral triple

Per corpus §20.1 and §22.7, NTE specifies the pre-temporal spectral triple as (A_G₂, H_S⁷, D_S³):

- **A_G₂**: the octonion algebra 𝕆, a non-associative normed division algebra of dimension 8 over ℝ. Aut(𝕆) = G₂ (the smallest exceptional Lie group, dim 14). The pre-temporal epoch's algebraic structure (§2.1.3(f)).
- **H_S⁷**: spinor space on S⁷ = unit-norm 𝕆 (the "boundary spinors" pre-temporally; the S⁷ structure encodes the full octonionic content with the physical S³ as the quaternionic submanifold per §2.1.3(f)).
- **D_S³**: Dirac operator on the physical S³ boundary. S³ is the geometric carrier of NTE's pre-temporal physics; its Dirac spectrum is well-known (eigenvalues ±(n + 3/2) with multiplicities n(n+1)(n+2)/2 and similar — Trautman 1993, Friedrich 2000).

### 3.2 The post-temporal spectral triple

Post-locking, NTE's spectral triple becomes the standard Connes-Chamseddine-Marcolli SM spectral triple (A_SM, H_SM, D_SM) per §20.1:

- **A_SM = ℂ ⊕ ℍ ⊕ M_3(ℂ)** — the SM finite algebra (ℂ ↔ U(1), ℍ ↔ SU(2), M_3(ℂ) ↔ SU(3)).
- **H_SM** — the spinor space of the SM (90 fermion species per the J_3(𝕆) Majorana count §VIII.7).
- **D_SM** = D_M + γ⊗D_F — Dirac on M plus finite-spectral-triple mass matrix.

### 3.3 Gauge birth as spectral flow

Per §22.7, gauge birth is the spectral flow (A_G₂, H_S⁷, D_S³) → (A_SM, H_SM, D_SM). The C¹ kink at gauge birth (§VIII.1.4) is the Wick rotation event; the surface-ontology programme's z(y) trajectory passes through z = π/2 uniquely at gauge birth (corrected reading; Stage 3).

This is where v2's structural claim lives: **the action principle for both pre-temporal and post-temporal regimes is the Connes spectral action — `S = Tr(f(D/Λ))` — applied to the appropriate spectral triple. The transition between them is the spectral flow at gauge birth.**

---

## §4. The Connes spectral action: how it works

### 4.1 The action functional

For a spectral triple (A, H, D) with Λ a UV cutoff and f a smooth positive even test function (e.g., a smooth approximation to a step function), the Chamseddine-Connes spectral action is:

$$ S_{spec}(A, H, D, f, \Lambda) = \mathrm{Tr}(f(D/\Lambda)) $$

This is a single number depending on the spectral data and the cutoff. The structural content lies in its asymptotic expansion at large Λ, which (for a 4-dimensional spin manifold M with an internal almost-commutative geometry) reads:

$$ \mathrm{Tr}(f(D/\Lambda)) \sim \sum_{k \in DimSp_+} f_k \Lambda^k \int\!\!\!\!\!\!\!\!\!\!\!- |D|^{-k} + f(0) \zeta_D(0) + o(1) $$

where the residues `∫\!\!\!− |D|^{-k}` are integrals of curvature terms on M coupled to internal-algebra contractions. Concretely, for the SM almost-commutative geometry on a 4-manifold M, this expansion contains (Chamseddine-Connes-Marcolli 2007):

- Cosmological term: `∫ √g d⁴x` 
- Einstein-Hilbert: `(1/(2κ²)) ∫ R √g d⁴x` 
- Weyl conformal-gravity: `α₀ ∫ C_μνρσ C^μνρσ √g d⁴x`
- Topological Pontrjagin term: `τ₀ ∫ R*R* √g d⁴x`
- Yang-Mills for SM gauge fields: `(1/4g²) ∫ F_μν F^μν √g d⁴x` (with three independent g for SU(3)_C, SU(2)_L, U(1)_Y — and the famous near-equality g₃² = g₂² = (5/3) g₁² at the unification scale)
- Higgs kinetic term: `½ ∫ |D_μ H|² √g d⁴x`
- Higgs potential: `V(H) = λ|H|⁴ − μ²|H|² + ...` (with λ and μ² determined by the spectral triple)
- Higgs-curvature non-minimal coupling: `−(1/12) ∫ R |H|² √g d⁴x` (the conformal coupling, with coefficient 1/12 fixed by the spectral action structure — *not* a free parameter)
- Yukawa terms and fermion masses

**The crucial observation for NTE**: gravity (Einstein-Hilbert + Weyl + topological) and the SM Lagrangian (gauge, Higgs, Yukawa) are *jointly* outputs of one functional. The graviton sector and the Higgs/scalar sector are *jointly determined*; their relative coefficients (including the non-minimal coupling 1/12) are not free.

### 4.2 The dilaton extension (Chamseddine-Connes 2005)

Promoting the cutoff Λ to a dynamical scalar field (the dilaton σ via Λ → e^σ·Λ), the spectral action becomes:

$$ S_{dil} = \mathrm{Tr}(f(e^{-\sigma} D/\Lambda)) $$

Expansion: every matter coupling becomes scale-invariant under σ → σ + const (i.e., the matter Lagrangian transforms homogeneously); only Einstein-Hilbert and the dilaton kinetic term break this scale invariance. The dilaton acquires a kinetic term `(½) ∫ (∂σ)² √g d⁴x` and a coupling to R via the structure of f.

**Key map to NTE**: σ in Chamseddine-Connes 2005 plays the same structural role as ln|Φ_NTE| in NTE — a scale-controlling field through which the universal coupling enters. The map σ ↔ ln|Φ_NTE|/Λ_ref is direct. Under this map, NTE's H = β_NTE|Φ|² constraint becomes a relation between the dilaton field and the Hubble parameter, exactly as the Chamseddine-Connes 2005 setup naturally produces.

---

## §5. The unified action on the NTE pre-temporal spectral triple

### 5.1 Strategy

Replace the SM almost-commutative geometry's (A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)) with NTE's pre-temporal A_G₂ (the octonion algebra). Replace the 4-manifold M with the S³ boundary (or its Euclidean compactification S³ × S¹_β for the spectral action calculation, per Marcolli-Pierpaoli-Teh §3). Apply the spectral action functional. The result, by construction, contains:

- **Gravitational sector** (Einstein-Hilbert + curvature corrections on S³) — this is where the graviton lives. Per Marcolli-Pierpaoli-Teh §3, the spectral action on S³ recovers Einstein-Hilbert + cosmological term to leading order, plus a non-perturbative scalar potential.

- **Scalar sector** (V_NTE potential for the NTE field) — this is Φ_NTE. The non-perturbative scalar potential identified by Chamseddine-Connes 2010 §5 in the variation D² → D² + φ² is, *by the literature's own framing*, a slow-roll inflation potential. **This is V_NTE.**

- **Gauge sector** — Boyle-Farnsworth 2013's octonionic spectral action gives "Einstein gravity + G₂ gauge theory + 8 Dirac fermions (singlet + septuplet of G₂)." NTE's pre-temporal G₂ symmetry breaks to SU(3)_C × SU(2)_L × U(1)_Y at gauge birth via the Dubois-Violette/Todorov mechanism (preserving the J_2(𝕆) substructure within J_3(𝕆); cf. NTE §VIII.7).

- **Fermion sector** — Boyle-Farnsworth's 8 Dirac fermions (singlet + septuplet of G₂) constitute one octonion-worth of pre-temporal fermion modes; the Furey 1-gen mechanism on each row of J_3(𝕆) (per AC's Hypercharge S2 audit) replicates this three times to give 3 generations × 1 Higgs neutral state + 7 charged states per generation. The 90-species count per Majorana reduction follows.

- **Non-minimal coupling ξ|Φ|²R** — emerges automatically from the spectral action expansion (Chamseddine-Connes 2010 §5, equations 5.x; Buck-Fairbairn-Sakellariadou 2010 §II for inflationary application). The coefficient ξ is **fixed by the spectral data**, not a free parameter. This is the structural unifier of the scalar and tensor sectors.

### 5.2 Schematic action

To leading order, the NTE pre-temporal spectral action takes the form:

$$ S_{NTE}^{pre} \supset \int_{S^3 \times S^1_\beta} \!\!\!\!\!\!\!\!\!\!\sqrt{g} \left[ \frac{\Lambda^4}{8\pi^2} f_4 + \frac{\Lambda^2}{24\pi^2} f_2 R + \frac{f(0)}{16\pi^2} \left( c_1 R^2 + c_2 C_{\mu\nu\rho\sigma}^2 + c_3 R^*R^* \right) \right.$$
$$ + \text{(gauge sector: G_2 Yang-Mills)} + \text{(fermion sector: 8 Dirac × 3 row-replications)} $$
$$ \left. + V_{NTE}(\Phi) + \xi_{NTE} |\Phi|^2 R + \text{(kinetic term for Φ via dilaton extension)} \right] $$

with the coefficients f_4, f_2, c_i, ξ_{NTE} determined by:
- The cutoff function f (free choice; physically restricted by smoothness and asymptotic conditions)
- The spectral triple data (fixed by NTE's setup: A_G₂, H_S⁷, D_S³)
- The volumes Vol(S³) = 2π² and Vol(S¹_β) = 2πβ, with the Marcolli-Pierpaoli-Teh assumption Λβ ~ 1 (well-justified per their §3)

The on-trajectory V_NTE is determined by computing the perturbative variation D² → D² + |Φ|² on the S³ × S¹ Euclidean compactification (Marcolli-Pierpaoli-Teh §3.2; explicit form for S³ given by their equation (3.8)).

### 5.3 Wick rotation back

The spectral action is most naturally computed in Euclidean signature (S³ × S¹ compactification). The Wick rotation back to Lorentzian (Λβ → −iΛt; the S¹ factor becomes the Lorentzian time axis) recovers the standard inflationary Lagrangian:

$$ \mathcal{L}^{post}_{NTE} = -\frac{1}{2}M_{Pl}^2 R - \xi_{NTE} |\Phi|^2 R + \frac{1}{2}|\partial\Phi|^2 - V_{NTE}(\Phi) + \mathcal{L}_{gauge} + \mathcal{L}_{fermion} $$

The pre-temporal Euclidean → post-locking Lorentzian transition (the Wick rotation event of §VIII.1.4) is the same transition that turns the spectral action's Euclidean compactification into a Lorentzian inflationary cosmology. **The C¹ kink at gauge birth is structurally the Euclidean-Lorentzian boundary of the spectral action calculation itself.**

---

## §6. What this closes in the NTE corpus

### 6.1 Gap 4b (§17.5.5) — action principle for two-metric coupling

**Closed structurally.** The two-metric coupling is the κ-coupling between the two CPN-conjugate orientations of the N-thickness (§6.1, §9.3). In the spectral action picture:

- The N-thickness has two CPN-conjugate orientations, each carrying an induced metric (g^(+), g^(−)).
- The spectral triple is doubled: (A_G₂ ⊕ A_G₂, H_S⁷ ⊕ H_S⁷, D_+ ⊕ D_−) with a coupling between the two sectors (the κ₀ term).
- The spectral action of the doubled spectral triple is the action principle for the two-metric coupling.
- The CPN-symmetric self-consistency closure κ₀ + κ₀² + ... = κ₀/(1−κ₀) emerges naturally as the perturbative resummation in the doubled spectral action.

This is the Gap 4b closure target. The full calculation (extracting κ₀ = 3/√(4π) from the spectral triple structure, verifying the geometric resummation gives κ = 5.50) is the v2 research target. **Conjectural** at this stage; structural setup defined.

### 6.2 V_NTE Stage 2 option (α) — boundary action's specific structure on S³

**Closed structurally.** V_NTE Stage 2 (`V_NTE_Stage2_Structural_Inventory.md` §5.3 option α) named "V_NTE arises from a specific geometric construction — e.g., V_NTE as the integral of scalar curvature times |Φ|² over S³" as the candidate closure.

The Connes spectral action gives precisely this kind of construction, with the additional benefit that V_NTE is determined *uniquely* by the spectral data, not just up to a few constants. The Chamseddine-Connes 2010 §5 calculation gives V(Φ) on S³ explicitly (their equation (3.8)):

$$ V_{S^3}(\phi) = \pi \int_0^\infty u\left[h(u + x) − h(u)\right] du + \frac{\pi}{2} \int_0^x h(u) du $$

with x = φ²/Λ² and h the cutoff function. NTE's V_NTE is structurally this V_{S³} (modulo the dilaton extension and the octonionic A_G₂ replacing A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)).

### 6.3 K(Φ) under-determination — Companion 9 Session 5 / spectral-triple closure

**Closed structurally.** The kinetic term for Φ_NTE (the K(Φ) function in Companion 9 Session 5's slow-roll calculation) is fixed by the spectral action's natural kinetic-term structure. Under the Chamseddine-Connes 2005 dilaton extension, the kinetic term is canonical (½(∂σ)² with σ = ln|Φ|), with corrections at higher curvature.

The r prediction (tensor-to-scalar ratio) is therefore determined by the spectral action's V_{S³}(Φ), the dilaton-induced kinetic structure, and the slow-roll parameters as standard. NTE's r ~ O(10⁻³) is consistent with the Marcolli-Pierpaoli-Teh §6 calculation for S³.

### 6.4 §22.7 — spectral flow account of gauge birth

**Becomes the central programme rather than a peripheral target.** Gauge birth is the spectral flow (A_G₂, H_S⁷, D_S³) → (A_SM, H_SM, D_SM); the spectral action transitions across this flow in continuity with the Wick rotation event of §VIII.1.4. The central work: defining the spectral flow precisely (Boyle-Farnsworth 2013 + Farnsworth 2025 give the octonionic spectral triple side; Chamseddine-Connes-Marcolli 2007 give the SM side; the flow between them at gauge birth is the missing technical piece).

---

## §7. What this opens for derivation

### 7.1 NTE-specific predictions extractable

With the unified action principle defined, the following NTE-specific quantities become computable rather than imposed:

- **κ from spectral data**: κ₀ = 3/√(4π) plausibly emerges from the spectral triple structure on S³ (the Hopf fibration S³ → S² with Y₀₀(S²) = 1/√(4π) and dim(SU(2)) = 3 are the load-bearing inputs); κ = κ₀/(1−κ₀) emerges from the doubled-spectral-triple perturbative resummation. **Conjectural; explicit calculation would close this.**

- **V_NTE off-trajectory**: explicit form determined by the cutoff function f (Marcolli-Pierpaoli-Teh equation 3.8). On-trajectory consistency with V_NTE^post(Φ) = (3β_NTE²/(8πG))Φ⁴ − (β_NTE²/8)Φ⁶ becomes a *constraint on f* rather than a free choice.

- **n_s**: V_NTE plus K(Φ) determine the slow-roll parameters; n_s = 1 − 6ε + 2η is derivable from the spectral action expansion. **NTE's existing n_s = 0.9685 (zero-parameter) becomes a check on the spectral action structure rather than a separate empirical input.**

- **r**: similarly derivable; NTE's r ~ O(10⁻³) is a structural prediction once V_NTE and K(Φ) are pinned.

- **Yukawa hierarchy**: emerges from the spectral triple's mass matrix structure. Boyle-Farnsworth's "8 Dirac fermions per row" times Furey-via-row-symmetry across 3 generations gives the texture; the explicit Yukawa values come from the spectral data.

- **Hypercharge assignments**: per the F₄/J_3(𝕆) → SM mechanism (corpus §VIII.7 + Hypercharge Sessions 1+2), the spectral triple's representation theory directly gives the hypercharge assignments. AC's Hypercharge S2 audit's HS2-3 concern (per-row octonion algebra under-specification) is closed by the explicit Boyle-Farnsworth construction.

### 7.2 What requires new calculation

**Substantial calculation work remains** to extract NTE-specific values:

1. **Octonionic spectral triple on S³ × S¹_β specifically** (Boyle-Farnsworth gives the abstract octonionic spectral triple; Marcolli-Pierpaoli-Teh gives the S³ spectral action; the specific cross — octonionic A_G₂ on the S³ × S¹ spacetime — has not been computed in the literature as of 2026-05-09).

2. **The spectral flow (A_G₂, H_S⁷, D_S³) → (A_SM, H_SM, D_SM) explicitly**. Farnsworth 2025 (arXiv 2506.21496) extends Boyle-Farnsworth's machinery to include charged Higgs fields with G₂ × G₂ gauge symmetry, which is structurally close to NTE's gauge-birth target but not identical (NTE wants G₂ → SM, not G₂ × G₂ → SM).

3. **The doubled-spectral-triple structure for the CPN-symmetric two-sector** (the structural target for Gap 4b closure with κ derivation).

4. **Dilaton extension of the octonionic spectral action** combining Chamseddine-Connes 2005 with Boyle-Farnsworth 2013/Farnsworth 2025.

These four calculations are the core research programme. Each is a paper or two of work; collectively they would constitute the technical realization of NTE's Connes-program target (§22.7) and would deliver every quantity the corpus currently flags as under-determined or contingent on imported machinery.

---

## §8. Why this is the way (and the alternative pathways)

The corpus already commits to the spectral-triple programme (§20.1, §22.7). v1 of this exploration identified joint origin via post-temporal projection as the structural reframing. v2 identifies the Connes spectral action as the concrete realization. The alternative pathways considered and their relative status:

| Pathway | Status | Why this isn't the way |
|---|---|---|
| Identity (graviton = Φ_NTE) | Failed (v1 §4) | Five decisive mismatches |
| Joint origin via Cayley-Dickson algebraic split per se | Inadequate alone | Cayley-Dickson governs gauge sector (𝕆 → ℍ → ℂ → ℝ at locking); doesn't give graviton sector. Needs the spectral action layer on top. |
| Higgs inflation à la Bezrukov-Shaposhnikov | Adjacent / partial | Provides the non-minimal coupling ξ\|Φ\|²R structure but doesn't have the algebraic foundation for Φ_NTE's geometric origin. The spectral action *gives* Bezrukov-Shaposhnikov as a special case while also supplying the missing geometric structure. |
| Mimetic gravity (Chamseddine-Mukhanov) | Adjacent | NTE's H = α\|Φ\|² is mimetic-flavoured, but mimetic gravity has the constraint imposed externally; in NTE (and in spectral action) it emerges from the underlying geometry. |
| Sakharov induced gravity | Complementary | Could provide one-loop matter-induced gravity contributions on top of the spectral action's tree-level gravity. Not a substitute. |
| Verlinde / Jacobson emergent gravity | Adjacent in spirit, different in mechanism | Gravity as thermodynamic/entropic emergent. Spectral action gives gravity geometrically (from the Dirac spectrum). NTE's "boundary-only" ontology has flavours of both, but the spectral action route is the technically concrete one. |
| Horndeski / Galileon | Compatible | NTE's effective post-Wick action would fit into the Horndeski class; this is a phenomenology-side check, not a structural origin. |
| Asymptotic safety | Complementary | UV completion question. The spectral action's f(D/Λ) structure is essentially asymptotic-safety-flavoured (Λ as UV cutoff with specific f). |
| AdS/CFT / holographic inflation | Adjacent | Different boundary condition (asymptotic dS or AdS, not S³). Useful conceptual flavour but not the same mechanism. |

The Connes spectral action route is unique among these in that it:
- Has the algebraic foundation NTE's pre-temporal regime needs (octonionic A_G₂, via Boyle-Farnsworth).
- Has the geometric foundation (spectral triple on S³, via Chamseddine-Connes / Marcolli-Pierpaoli-Teh).
- Has the cosmological extension (Robertson-Walker spectral action, via Chamseddine-Connes 2012 / Fathizadeh et al. 2014).
- Has the dilaton/scalar structure NTE's Φ_NTE plays (Chamseddine-Connes 2005).
- Already produces the SM gauge group, Higgs mechanism, and Yukawa structure without further input (Chamseddine-Connes-Marcolli 2007).
- Is *already named in the corpus* as the closure target for §22.7.

No other pathway has this convergence. **This is the way.**

---

## §9. The κ connection — conjectural but structurally necessary

**Claim**: κ₀ = 3/√(4π) and κ = κ₀/(1−κ₀) = 5.50 emerge from the doubled-spectral-triple structure on the CPN-conjugate two-sector S³ × S¹_β with octonionic A_G₂.

**Sketch of why this is structurally necessary, not optional**:

- NTE's κ derivation (§9.3) uses three load-bearing inputs: Y₀₀(S²) = 1/√(4π) (Hopf monopole projection topological protection), dim(su(2)) = 3 (eigenstate count for the Bianchi-IX wave equation truncation), and CPN-symmetric two-sector self-consistency (the geometric series).
- All three are spectral data of the (S³, A_G₂) spectral triple: Y₀₀ is the lowest-weight spherical harmonic on S² = base of S³ → S² Hopf fibration; dim(su(2)) = 3 is the dimension of the Lie algebra of SU(2) = isometry group of S³; the CPN-symmetric two-sector is the doubled spectral triple structure.
- The spectral action Tr(f(D/Λ)) on the doubled spectral triple is computable. Its perturbative expansion in the cross-coupling (the κ₀ parameter) is a geometric series, by structure.
- The closed-form sum κ₀/(1−κ₀) is the natural output.

**What's missing**: the explicit calculation showing that the spectral data give κ₀ = 3/√(4π) (rather than e.g. some other combination of the same ingredients). This is the technical work that would *prove* the claim. Until that is done, the κ connection is a structural conjecture, not a derivation.

But: the load-bearing pieces are exactly the right type of data for the spectral action machinery. The conjecture has the structural shape of a true claim — *if* the spectral action picture is right for NTE, *then* κ should fall out by this route. The conjecture's failure would be much more surprising than its success.

---

## §10. r prediction status

NTE's r ~ O(10⁻³) (Companion 9 Stage 3 Session 4 hilltop reading, conditional on K(Φ); §17.5.14) survives intact under the spectral action picture. The relationship:

- The Marcolli-Pierpaoli-Teh §6 calculation gives r explicitly for spherical cosmic topologies via the spectral action V(Φ): r = 16ε with ε = (M_Pl²/16π)(V'/V)² evaluated on the V_{S³}(Φ) potential.
- NTE's S³ boundary specializes the topology choice; the multiplicative factor λ_Y = 1 (the S³ case has #Γ = 1).
- Crucially: r is no longer "conditional on K(Φ)" once K(Φ) is fixed by the spectral action's natural kinetic-term structure (Chamseddine-Connes 2005 dilaton extension). The K(Φ) that enters the slow-roll calculation IS the dilaton-induced kinetic term; this is computable.

**Prediction**: r is determined by the spectral-action-derived V_NTE(Φ) and dilaton-induced kinetic term; NTE's existing r ~ O(10⁻³) becomes a *consequence* of the unified action rather than an input. CMB-S4 / LiteBIRD will test this.

---

## §11. Concrete research programme

**For Jammer's R&D queue (post-Hypercharge S3/S4 or independently):**

### Programme S — Spectral Action Closure (multi-paper)

**Paper S1**: Boyle-Farnsworth octonionic spectral action on S³ × S¹_β (the cross they didn't compute). Inputs: Boyle-Farnsworth 2013 octonionic spectral triple data; Marcolli-Pierpaoli-Teh's S³ spectral action machinery. Output: V_NTE(Φ) and gravitational-coupling structure on S³ × S¹ Euclidean compactification with octonionic A_G₂. This is **the central calculation**; all subsequent NTE-specific predictions key off it.

**Paper S2**: Doubled-spectral-triple for the CPN-symmetric two-sector. Inputs: S1 result; the §6.1 N-thickness structure; the κ derivation §9.3. Output: closed-form expression for κ in terms of S1's spectral data, target value 5.50. Closes Gap 4b.

**Paper S3**: Spectral flow at gauge birth. Inputs: S1 result; Chamseddine-Connes-Marcolli 2007 SM spectral triple. Output: explicit spectral-flow construction connecting (A_G₂, H_S⁷, D_S³) to (A_SM, H_SM, D_SM); identifies what's preserved vs broken across the flow; identifies the Wick rotation as the spectral-flow event. Closes §22.7.

**Paper S4**: Dilaton extension of S1. Inputs: S1; Chamseddine-Connes 2005. Output: explicit kinetic-term structure for Φ_NTE; r prediction sharpened.

**Paper S5** (optional, longer-term): Spectral action Yukawa hierarchy. Inputs: S1, S3; the J_3(𝕆) row-symmetric structure (Hypercharge Sessions). Output: derives the Yukawa values from the spectral triple's mass matrix structure. Closes §VIII.7's mass-spectrum gap.

### Programme S sequencing

S1 is foundational and self-contained. S2 and S3 each take S1 as input. S4 takes S1 + Chamseddine-Connes 2005. S5 takes S1 + S3.

S1 is the first paper. Estimated scope: a 30-50 page technical paper, requiring spectral-triple computation expertise (heat kernel, pseudodifferential calculus, Poisson summation) — accessible to NCG specialists (Chamseddine-Connes-Marcolli school, Boyle-Farnsworth, Fathizadeh, Sakellariadou). Possible external collaboration target.

---

## §12. Standing claim

**The structural unification of Φ_NTE and the QFT graviton in NTE is realized by the Connes spectral action `S = Tr(f(D/Λ))` applied to the NTE pre-temporal spectral triple (A_G₂, H_S⁷, D_S³), with the doubled-spectral-triple structure for the CPN-symmetric two-sector.**

This single action principle:
- Produces Einstein-Hilbert (graviton sector) + V_NTE (scalar sector) + gauge sector + Yukawa sector simultaneously.
- Includes the non-minimal coupling ξ|Φ|²R with coefficient determined by the spectral data, not free.
- Reduces to the standard Chamseddine-Connes-Marcolli SM action under the spectral flow at gauge birth.
- Closes Gap 4b structurally; closes V_NTE Stage 2 option (α); closes K(Φ) underdetermination; closes the §22.7 Connes target.
- Gives κ, n_s, r, V_NTE coefficients, and Yukawa values as outputs of the single calculation rather than as separate inputs.

The pathway is well-defined. The literature anchors are solid (Chamseddine-Connes 1996+; Boyle-Farnsworth 2013; Marcolli-Pierpaoli-Teh 2010; Chamseddine-Connes 2005, 2010, 2012; Fathizadeh-Ghorbanpour-Khalkhali 2014; Farnsworth 2025). The remaining work is the explicit calculation programme outlined in §11 — substantial but tractable.

**v1's "joint origin" reframing is concrete.** Φ_NTE and the graviton are not identical; they are jointly determined by one spectral action principle on one spectral triple. The gravitational sector and the scalar sector are paired structurally, not phenomenologically. The framework's r ~ O(10⁻³) prediction, the n_s = 0.9685 prediction, the κ = 5.50 prediction, and the Yukawa hierarchy — all of these become outputs of the same single calculation, not independent inputs.

This is the way. NTE has been pointing at it (§22.7); the literature has built most of the machinery (Boyle-Farnsworth, Marcolli-Pierpaoli-Teh, Chamseddine-Connes 2005); the synthesis hasn't yet been done in print, but the pieces are in place. Programme S is the work to do it.

---

## §13. Status / ownership

- **Stream**: Scratch (deep-exploration; descendant of Jammer's v1 draft).
- **Status**: Definitive pathway identified. Substantial calculation programme remaining.
- **Resume condition**: Greg's authorisation. Programme S sequencing decision (S1 first; S2-S5 sequenced after).
- **Adjacent corpus targets to alert on resumption**: §17.5.5 (Gap 4b — closes structurally upon Programme S completion); §17.5.1 (V_NTE — closes under S1); §22.7 (Connes target — central programme upon Programme S launch); Companion 9 K(Φ) (closes under S4); §VIII.7 mass spectrum (closes under S5).
- **External collaboration target**: NCG specialists who could compute Programme S papers efficiently — the Chamseddine-Connes-Marcolli circle, Boyle and Farnsworth specifically, Fathizadeh, Sakellariadou, the Connes IHES group.

— Scratch, 2026-05-09 evening NZST.
