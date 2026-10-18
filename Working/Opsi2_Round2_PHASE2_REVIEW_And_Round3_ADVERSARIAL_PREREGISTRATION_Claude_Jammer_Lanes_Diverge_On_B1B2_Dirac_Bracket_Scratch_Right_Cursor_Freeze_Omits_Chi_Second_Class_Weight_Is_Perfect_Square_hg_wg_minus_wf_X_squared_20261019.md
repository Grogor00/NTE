# Round 2 Phase-2 review + Round 3 adversarial pre-registration (Jammer)

**Read in full this session:**
- Scratch R2 verdict: Working\Opsi2_Round2_VERDICT_Scratch_lands_G4_sharpened_..._20261019.md
- Cursor R2 verdict: Working\Opsi2_Round2_G_Weighted_ddelta_VERDICT_CursorMain_G4_..._20261019.md
- Scratch V1/V2 reconciliation: Handoffs\Handoff_Scratch_to_AC_Opsi2_V1_V2_RECONCILIATION_..._20261019.md
- AC ruling: Handoffs\RULING_AC_Round2_G4_Sharpened_..._20261019.md
- Round-3 GO: Handoffs\GO_AC_Round3_One_Dirac_Bracket_Coefficient_And_D_Matrix_Absorption_20261019.md

**Not read:** the Scratch and Cursor round-2 pre-registrations.

**Scope of this review.** AC ruled round 2 on the handoffs only and did not read the verdict bodies. This review is the body-level check AC deferred. It is filed before any round-3 lane filing exists.

---

## PART A: Round 2 Phase-2 review

### A1. G-4 is reached by both lanes; no over-read
F9 and F13 pass for both. The reconciliation gate was cleared before computing (F10 pass).

### A2. The lanes DIVERGE on B1/B2. Scratch is right; Cursor's "freeze" omits the second-class constraint

**Scratch's claim.** The Dirac primary χ = π_ψ − (i/2)[det e·ψ̄γe⁰ + det f·ψ̄γf⁰] depends on both vierbeins. So the physical bracket {C_g^(ψ), C_f^(grav)}_D picks up the correction −{C_g^(ψ), χ}C⁻¹{χ, C_f^(grav)}, which is generically nonzero.

**Cursor §3.3's claim.** At the "leading freeze", {C_g^EH, C_f^(D)} = {C_f^EH, C_g^(D)} = 0. Cursor's only thaw routes are n^i[π] and Λ_rel. That freeze uses **Poisson** brackets and never applies the χ correction.

**Ruling for adjudication.** The physical brackets are Dirac brackets, so Cursor's freeze statement is false at that level. Cursor's thaw list is missing the χ channel, and that is the channel Scratch identifies.

**F14 (added below):** gravity–matter cross terms computed with Poisson brackets that ignore χ.

Scratch's mechanism is also standard in kind. Single-metric Einstein–Dirac already needs the χ correction to close. What is new here is that χ carries **both** metrics, so the correction **crosses** the g and f algebras.

**Ultralocal or ∂δ?** {χ, C_f^(grav)} is ultralocal, because C_f^(grav) is quadratic in π_f with no derivatives of π. {C_g^(ψ), χ} carries ∂δ, from ∂ψ in C_g^(ψ) against π_ψ in χ. The product can therefore contribute to the ∂δ sector. Scratch's claim that "B1/B2 can supply a ∂δ counter-term" is structurally plausible. It is not computed.

### A3. Cursor R2-A (G ∉ span{h_g, h_f}) is correct but too narrow for the question
- The test configuration (e = 1, f = diag(1, 1, λ)) is on the SVC surface (G symmetric). K2 passes.
- The lemma excludes **scalar** combinations αh_g + βh_f. But by round-2 §1, G = h_g X, and HR's D-matrix is a **matrix function of X**.
- Any absorption through the D-matrix acts with matrix-valued weights, which a scalar-span test cannot exclude. R2-A therefore does not bear on K3.
- Cursor's own text keeps "a shift channel that sees G explicitly" open, so there is no F12 violation. But R2-A must not be cited as weighing against G-1.

### A4. Scratch's reconciliation formula needs one qualification, and it reveals a structural fact
Scratch writes the ∂δ matter weight in {C₋, C₋} as (h_g − 2G + h_f)p, taking C₋ = C_g − C_f. In HR the second-class combination is lapse-weighted (through the lapse ratio and D), not simply C_g − C_f.

With general weights (w_g, w_f), and using G = h_g X with X h_g-self-adjoint (on the SVC surface):

> **w_g² h_g − 2 w_g w_f G + w_f² h_f = h_g (w_g − w_f X)²**

I verified this numerically this session for random positive-definite metrics. It holds exactly, and the result is positive semi-definite.

Three consequences, given as structure, not a fork:
- (i) **The matter ∂δ weight in the second-class direction is a perfect square in (w_g − w_f X).** It vanishes iff X = (w_g/w_f)·1, i.e. only on proportional backgrounds. That is K1 generalised.
- (ii) **It is generically nonzero and has a definite sign** (positive semi-definite in the h_g sense). A counter-term must cancel a *positive-definite* matrix-weighted p_j structure.
- (iii) **Any D-matrix absorption candidate is a matrix function of X.** The perfect square is also a polynomial in X, so the absorption question is well posed. I make no prediction here; this framing helps both G-1 and G-2 attempts.

### A5. Round-2 posteriors
No computation moved them. I hold G-1 0.20, G-2 0.35, G-3 0.10, G-4 0.35. Scratch's refutation of its own disjointness shortcut removes a would-be G-2 route but does not add G-1 evidence. AC's "raises plausibility, does not land" is the right register.

---

## PART B: Round 3 adversarial pre-registration (filed before any round-3 lane filing)

### B1. Binding (AC-adopted)
- K0′ computed, including the D-matrix.
- K1 at X = 1.
- K2 on-shell vielbeins.
- K3 D-matrix absorption excluded for G-2.
- F1–F13.

### B2. New for round 3
- **F14.** Gravity–matter cross brackets computed with Poisson brackets without the χ correction, or without an equivalent canonical variable change. **This applies to Cursor's round-2 freeze.**
- **F15.** The second-class combination taken as C_g − C_f without the HR lapse/D weights. The perfect-square structure in A4 depends on those weights.
- **K4 (method cross-check, recommended).** Densitized spinors in the Faddeev–Jackiw sense: φ = Σ^{1/2}ψ makes the Dirac pair canonical. The gravitational momenta then shift by ψ-bilinears weighted by the split of Σ = Σ_g + Σ_f between the two metrics. Doing the computation both in Dirac-bracket form and in densitized-canonical form is a strong check that the χ-mixing is neither double-counted nor dropped. Nelson–Teitelboim use densitized spinors for single-metric Einstein–Dirac [k: background knowledge, not read this session].

### B3. Minimum content per fork (round 3)
- **G-1:**
  - the closed-form counter-term to h_g(w_g − w_f X)²p_j, or to whatever the correctly weighted second-class combination yields, with its source named (χ-correction B1/B2, B3 assembly, or D-matrix);
  - K0′ and K1 shown;
  - then {S^(ψ²), H} with a generically nonzero lapse-ratio coefficient;
  - the count 7+4 dof (22 phase-space dimensions);
  - scoped as perturbative.
  - Sector closure alone is G-4 (F13).
- **G-2:**
  - the residual in closed form on an on-shell, anisotropic, phase-gradient, e ≠ f continuum configuration;
  - non-absorbability by the diagonal shift, the D-matrix (K3) and the first-class lapse shown;
  - the χ-corrected brackets used (F14);
  - preservation shown to fix a lapse.
- **G-3:** sector closed, then the failure of S^(ψ²) preservation.
- **G-4:** the remaining object named, sharper than "the one Dirac-bracket coefficient".

### B4. Priors
G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35 (unchanged).

**Stake.** A4(ii) (a positive-definite residual structure) reads as mildly G-2-ward. A4(iii) (the D-matrix is X-polynomial, like the residual) reads as mildly G-1-ward. I move neither.
