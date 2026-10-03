# Task 4 Session 2 — Functional Determinant ζ'_total(0) on NTE Spectral Triple — Scratch v1

**Status:** Working note v1, 2026-05-17 (morning sync). Session 2 of Task 4 multi-session arc per AC routing 1-3 sessions. Priority A1 deliverable: functional determinant ζ'_total(0) closed-form computation + interpretation as log det' D + structural analysis.
**Author stream:** Scratch (Connes Programme lead within Jammer-stream).
**Investigation question:** Compute ζ'_total(0) for NTE's two-sector spectral triple on S³ in closed form; interpret as functional determinant log det' D; analyze as one-loop effective action contribution; search for structural identities with canonical NTE numbers.
**Trigger:** Greg directive 2026-05-17 morning sync: "Gates: 1, yes. 2, yes. 3, yes. 4 (a) then in order as tasks completed/required. 5, scoping for now." — Task 4 v1 scoping verdict + κ₀ consistency anchor + observables priority list + session arc proposal all ratified; routing directive (a) = Task 4 Session 2 immediate next priority.
**Recognition-gate aware:** Local-correctness-only until passing Greg's recognition gate via AC review. Recognition-gate items in §11.
**Source basis read this session**:
- Task 4 v1 scoping working note (Scratch) at Working/ `1ng5xsTQCORbYY56NhGPkDQw1UIlq_IP4` — referenced
- Jammer Route A first-pass at Working/ `1k6SnwDk_bhlTmB3EAIq3inxEdX1A0Ej_` — referenced
- Standard Hurwitz zeta + Riemann zeta functional-equation literature (commonly known special values; no specific paper read this session)
- PC Ch15 predictions catalogue handoff at Handoffs/ `1y3Tw9SvkiFnaaSFxOfk_MLt2xWSLLHio` (21:34 UTC 2026-05-16, just after my Task 4 v1 ship) — recency-scan acknowledged; PC scope; not directly affecting Scratch work this session
**Files NOT read this session** (flagged as confidence-limiters per §10):
- Gilkey or Vassilevich heat-kernel literature (would refine convention-dependence + physical-interpretation analysis)
- Paper_Kappa_PathwayB_v10_6 (Jammer summary sufficient for κ₀ consistency anchor preserved)
- Hersent 2025 / Summers 2005 / Borchers 1999 (Task 1 confidence-limiters carried forward)

---

## §1. Task framing

### §1.1 Where this fits in the Task 4 arc

Per Task 4 v1 scoping deliverable (`1ng5xsTQCORbYY56NhGPkDQw1UIlq_IP4`) §4.3 + §6.3:

- **Session 1** (v1 scoping): completed and ratified 2026-05-17 morning sync
- **Session 2** (this v1): **Priority A1 — functional determinant ζ'_total(0)**. One-loop effective action contribution; V_NTE Stage 2 consistency check
- Session 3 (if needed): Priority A2 + A3 — eta invariant + conformal anomaly coefficient

### §1.2 What this Session 2 deliverable produces

1. **Closed-form ζ'_total(0)** for NTE's two-sector spectral triple on S³
2. **Numerical value** to sufficient precision
3. **Interpretation as log det' D** with convention-dependence honestly flagged
4. **One-loop effective action contribution** analysis
5. **Structural identity search** — testing whether ζ'_total(0) connects cleanly to canonical NTE numbers (κ₀, κ, log 2, π, etc.) with honest negative-result reporting if no clean identity surfaces
6. **V_NTE Stage 2 territory connection** assessment

### §1.3 What this Session 2 does NOT do

- Does NOT extend to A_F nonassociativity workaround (P0.10 territory; spectral-zeta on manifold-side does not require)
- Does NOT engage Session 3 territory (eta invariant on M^C × S³; conformal anomaly coefficient c_W)
- Does NOT propose Charter v1.4 candidate wording (AC scope)
- Does NOT complete full Paper S2 heat-kernel computation (Programme S central deliverable; separate)

---

## §2. Setup recap (from Task 4 v1)

### §2.1 Two-sector spectral zeta function

Per Jammer Route A first-pass §3 + Task 4 v1 §2.3:
$$\zeta_{\text{total}}(s) = 4 \zeta_H(s-2, 3/2) - \zeta_H(s, 3/2)$$

where:
- $\zeta_H(s, a) = \sum_{k=0}^{\infty} (k+a)^{-s}$ is the Hurwitz zeta function
- The factor 4 from ζ_H(s−2, 3/2) absorbs the multiplicity d_k = (k+1)(k+2) = (k+3/2)² − 1/4 expansion + CPN two-sector doubling
- The −ζ_H(s, 3/2) term comes from the −1/4 subtraction in the multiplicity expansion

### §2.2 Key identity: ζ_H(s, 3/2) via Riemann zeta

The Hurwitz zeta at a = 1/2 connects to Riemann zeta:
$$\zeta_H(s, 1/2) = \sum_{k=0}^{\infty}(k+1/2)^{-s} = 2^s\sum_{n=0}^{\infty}(2n+1)^{-s} = 2^s[\zeta(s) - 2^{-s}\zeta(s)] = (2^s - 1)\zeta(s)$$

Then shifting:
$$\zeta_H(s, 3/2) = \zeta_H(s, 1/2) - (1/2)^{-s} = (2^s - 1)\zeta(s) - 2^s$$

**Verification at s = 0**: ζ_H(0, 3/2) = (1−1)(−1/2) − 1 = −1 ✓ (matches Jammer §5)
**Verification at s = −2**: ζ_H(−2, 3/2) = (1/4 − 1)(0) − 1/4 = −1/4 ✓ (matches Jammer §5)

This identity is the key technical tool for Session 2's computation.

### §2.3 Lerch's formula for ζ'_H(0, a)

Standard result:
$$\zeta'_H(0, a) = \log \Gamma(a) - \frac{1}{2}\log(2\pi)$$

For a = 3/2, with Γ(3/2) = √π/2:
$$\zeta'_H(0, 3/2) = \log\left(\frac{\sqrt{\pi}}{2}\right) - \frac{1}{2}\log(2\pi) = \frac{1}{2}\log\pi - \log 2 - \frac{1}{2}\log 2 - \frac{1}{2}\log\pi = -\frac{3}{2}\log 2$$

So:
$$\boxed{\zeta'_H(0, 3/2) = -\frac{3}{2}\log 2 \approx -1.0397}$$

This was previewed in Task 4 v1 §5.2; confirmed clean here.

---

## §3. Computation of ζ'_H(−2, 3/2)

### §3.1 Differentiating the key identity

From ζ_H(s, 3/2) = (2^s − 1) ζ(s) − 2^s, differentiate w.r.t. s:

$$\zeta'_H(s, 3/2) = 2^s (\log 2)\, \zeta(s) + (2^s - 1)\, \zeta'(s) - 2^s \log 2$$

At s = −2:
- $2^{-2} = 1/4$
- $\zeta(-2) = 0$ (trivial zero of Riemann zeta)
- $(2^{-2} - 1) = -3/4$
- $2^{-2} \log 2 = (1/4) \log 2$

Substituting:
$$\zeta'_H(-2, 3/2) = (1/4)(\log 2)(0) + (-3/4)\, \zeta'(-2) - (1/4)\log 2 = -\frac{3}{4}\zeta'(-2) - \frac{1}{4}\log 2$$

### §3.2 Special value: ζ'(−2)

The Riemann zeta function's derivative at the first trivial zero s = −2 has a well-known closed form from the functional equation:
$$\zeta(s) = 2^s \pi^{s-1} \sin(\pi s/2) \Gamma(1-s) \zeta(1-s)$$

At s = −2: sin(πs/2) = sin(−π) = 0 causes ζ(−2) = 0. Differentiating the functional equation at s = −2 (where only the sin factor vanishes), the derivative picks up (π/2) cos(πs/2) at s = −2 = (π/2)(cos(−π)) = −π/2:

$$\zeta'(-2) = 2^{-2} \pi^{-3} \cdot (-\pi/2) \cdot \Gamma(3) \cdot \zeta(3) = (1/4)(1/\pi^3)(-\pi/2)(2)\zeta(3) = -\frac{\zeta(3)}{4\pi^2}$$

So:
$$\boxed{\zeta'(-2) = -\frac{\zeta(3)}{4\pi^2} \approx -0.030448}$$

(Apéry's constant ζ(3) ≈ 1.20206; π² ≈ 9.8696; ratio gives 0.030448.)

### §3.3 ζ'_H(−2, 3/2) closed form

Substituting:
$$\zeta'_H(-2, 3/2) = -\frac{3}{4}\left[-\frac{\zeta(3)}{4\pi^2}\right] - \frac{1}{4}\log 2 = \frac{3\zeta(3)}{16\pi^2} - \frac{\log 2}{4}$$

$$\boxed{\zeta'_H(-2, 3/2) = \frac{3\zeta(3)}{16\pi^2} - \frac{\log 2}{4} \approx -0.15045}$$

Numerical breakdown:
- 3ζ(3)/(16π²) ≈ 3 × 1.20206 / (16 × 9.8696) ≈ 0.02284
- (log 2)/4 ≈ 0.17329
- ζ'_H(−2, 3/2) ≈ 0.02284 − 0.17329 ≈ −0.15045

---

## §4. ζ'_total(0) closed form

### §4.1 Final assembly

From Task 4 v1 §5.2:
$$\zeta'_{\text{total}}(s)\big|_{s=0} = 4\, \zeta'_H(s-2, 3/2)\big|_{s=0} - \zeta'_H(s, 3/2)\big|_{s=0} = 4\, \zeta'_H(-2, 3/2) - \zeta'_H(0, 3/2)$$

Substituting:
$$\zeta'_{\text{total}}(0) = 4\left[\frac{3\zeta(3)}{16\pi^2} - \frac{\log 2}{4}\right] - \left[-\frac{3}{2}\log 2\right] = \frac{3\zeta(3)}{4\pi^2} - \log 2 + \frac{3}{2}\log 2$$

$$\boxed{\zeta'_{\text{total}}(0) = \frac{3\zeta(3)}{4\pi^2} + \frac{1}{2}\log 2}$$

### §4.2 Numerical value

- 3ζ(3)/(4π²) ≈ 3 × 1.202057 / (4 × 9.869604) ≈ 3.606171 / 39.478417 ≈ **0.09134**
- (1/2) log 2 ≈ 0.346574
- $\zeta'_{\text{total}}(0) \approx \mathbf{0.43791}$

### §4.3 Structural form analysis

The closed form is a sum of two transcendental terms:

$$\zeta'_{\text{total}}(0) = \underbrace{\frac{3\zeta(3)}{4\pi^2}}_{\text{from dim-3 / Apéry}} + \underbrace{\frac{1}{2}\log 2}_{\text{from CPN doubling}}$$

**The 3ζ(3)/(4π²) term**: structurally tied to dim(S³) = 3 via ζ'(−2) which is a special value at the dim-S³-shifted trivial zero. The transcendental ζ(3) (Apéry's constant) appears naturally as the spectral signature of the 3D character of S³.

**The (1/2) log 2 term**: structurally tied to the half-integer Hurwitz parameter a = 3/2 (which encodes the spin-1/2 character of the Dirac operator) and the CPN two-sector doubling factor 4 in ζ_total(s). The "log 2" reflects the doubling.

This split is structurally clean: one term encodes the topological/dimensional content (S³ via ζ(3)); the other encodes the algebraic content (CPN doubling via log 2).

### §4.4 Verification — sanity checks

**Sanity check 1**: ζ'_total(0) at full ζ_total(s) framework should be real. Result: 3ζ(3)/(4π²) + (1/2) log 2 — both transcendental but real. ✓

**Sanity check 2**: ζ'_total(0) should be order-unity if the spectral zeta is correctly normalized for unit S³. Result: 0.43791. Order-unity ✓.

**Sanity check 3**: ζ'_total(0) should be expressible in terms of Riemann ζ values and elementary transcendentals. Result: 3ζ(3)/(4π²) + (1/2) log 2 satisfies this. ✓

---

## §5. Interpretation as log det' D — convention caveats

### §5.1 Standard zeta regularization

For a positive operator A with spectrum {λ_n}, the zeta-regularized functional determinant is defined via:
$$\log \det' A = -\zeta'_A(0), \quad \text{where} \quad \zeta_A(s) = \sum_n \lambda_n^{-s}$$

The prime indicates exclusion of zero modes. For NTE's Dirac operator on S³, there are no zero modes (smallest eigenvalue |λ_0| = 3/2 > 0), so the prime is redundant.

### §5.2 Convention complication for D vs |D| vs D²

For the Dirac operator D with both positive and negative eigenvalues ±(3/2 + k), several conventions exist:

**Convention I — |D| (positive operator)**:
$$\zeta_{|D|}(s) = \sum_k |\lambda_k|^{-s}$$
This is what Jammer's ζ_total(s) computes: sum over all eigenvalues with both signs, using |λ|^{-s}. ζ'_|D|(0) = ζ'_total(0).

**Convention II — D² (squared operator)**:
$$\zeta_{D^2}(s) = \sum_k (\lambda_k^2)^{-s} = \sum_k |\lambda_k|^{-2s} = \zeta_{|D|}(2s)$$
Then ζ'_{D²}(0) = 2 ζ'_|D|(0).

**Convention III — D directly** (with sign issues):
For an operator with both signs of eigenvalues, det D itself is well-defined as a product but the sign is ambiguous. Typically one uses det |D| or det D² for unambiguous results.

**For NTE's Dirac on S³**: Jammer's ζ_total(s) is Convention I (|D|).

### §5.3 log det' D under Convention I

Using ζ'_|D|(0) = ζ'_total(0) ≈ 0.43791:
$$\log \det' |D| = -\zeta'_{\text{total}}(0) = -\frac{3\zeta(3)}{4\pi^2} - \frac{1}{2}\log 2 \approx -0.43791$$

Equivalently:
$$\det' |D| = \exp(-\zeta'_{\text{total}}(0)) \approx \exp(-0.43791) \approx 0.6453$$

This is the regularized product of |λ_k|'s over the entire two-sector spectrum.

### §5.4 Connection to fermion partition function

For a free Dirac fermion in Euclidean signature, the partition function (Grassmann path integral) is:
$$Z_{\text{fermion}} = \det D$$

For NTE's two-sector setup where D has both signs and chirality-doubled CPN structure:
$$Z_{\text{NTE fermion}} = \det D = \pm \det |D|$$

(Sign depends on the number of negative eigenvalues; in NTE's chirality-symmetric setup, det D² = (det |D|)² is unambiguous.)

The **one-loop effective action** from the fermion path integral:
$$W_{\text{1-loop, fermion}} = -\log Z = -\log \det D = +\zeta'_{\text{total}}(0) \approx \mathbf{+0.43791}$$

(With sign caveats per convention; for chirality-symmetric content the sign is determined by the chirality count.)

### §5.5 Honest convention-dependence flag

The numerical value 0.43791 is **axiom-derived and unambiguous** at the closed-form level. The **sign and physical interpretation** depend on:
- Whether one is computing det D, det |D|, or det D²
- Whether Lorentzian or Euclidean signature is being used (post-Task 2 σ_t / KMS reframing: state-type-transition gives canonical Euclidean → Lorentzian via Wick-rotation derived special case)
- Whether the fermion is a single Dirac (one-loop W = −log det D) or a chirality-doubled CPN structure (one-loop W = ±log det |D|² = ±2 log det |D|)

For Task 4 Session 2's purposes: report the closed-form structural value; flag convention-dependence honestly; defer specific physical-interpretation commitment to future Programme S work where the full effective action context is worked out.

---

## §6. One-loop effective action analysis

### §6.1 Standard interpretation

For a free fermion on a curved manifold (here, S³ with unit radius), the one-loop effective action is:
$$W_{\text{1-loop}} = \log \det D = -\zeta'_{|D|}(0) \times (\text{sign convention})$$

For NTE two-sector spectral triple on unit S³:
$$|W_{\text{1-loop}}| = |\zeta'_{\text{total}}(0)| = \frac{3\zeta(3)}{4\pi^2} + \frac{1}{2}\log 2 \approx 0.438$$

### §6.2 Scale dependence

For S³ of radius R, the Dirac eigenvalues scale as λ_k = (3/2 + k)/R, and:
$$\zeta_{|D|}(s) = R^s \zeta_{\text{total}}(s)$$

Therefore:
$$\zeta'_{|D|}(s) = R^s \log R\, \zeta_{\text{total}}(s) + R^s \zeta'_{\text{total}}(s)$$

At s = 0 (where ζ_total(0) = 0):
$$\zeta'_{|D|}(0)\big|_{S^3_R} = \zeta'_{\text{total}}(0) + 0 \cdot \log R = \zeta'_{\text{total}}(0)$$

Wait: ζ_total(0) = 0 from Jammer §5 (expected for odd-dim). So the log R term vanishes. **The one-loop effective action is independent of R for unit S³** (in this normalization).

This is consistent with the absence of a conformal anomaly at odd dimension (the conformal anomaly for d-dim manifold lives in d-even).

### §6.3 What this contributes to NTE's effective action

For the full NTE spectral triple A = C^∞(M) ⊗ A_F with M = Hopf-S³ × S¹_{β_GB} ≃ M^C:
- The S¹_{β_GB} factor contributes additional ζ-regularization terms (would need full product-manifold computation)
- The A_F = 𝕆 ⊕ 𝕆 factor contributes via the dimension count (CPN doubling already absorbed in ζ_total factor 4)
- The Dirac operator on the full manifold includes contributions from both S³ and S¹_{β_GB} sectors

This Session 2 deliverable computes only the **S³ sector's contribution**. The full one-loop effective action requires Session 3 or downstream Paper S2 work for the S¹_{β_GB} sector + A_F sector contributions.

### §6.4 Physical content of the S³ contribution

The closed form $\zeta'_{\text{total}}(0) = \frac{3\zeta(3)}{4\pi^2} + \frac{1}{2}\log 2$ has the following physical interpretation:

- **The 3ζ(3)/(4π²) term**: vacuum energy contribution from Dirac fermion mode summation on S³. This is a Casimir-like effect tied to the 3D character (S³ topology) of NTE's spatial surface
- **The (1/2) log 2 term**: contribution from the CPN sector-doubling. The "1/2" emerges from the structural averaging over the two sectors

Combined, this contributes an order-unity constant to the renormalized vacuum energy / effective action of NTE fermion content on the spatial S³ at fixed scale R = 1.

---

## §7. Structural identity search — honest negative result

### §7.1 Candidate canonical NTE numbers tested

NTE's canonical numerical anchors:
- κ₀ = 3/√(4π) ≈ 0.84628
- κ = 5.5055 (≡ 11/2; from Pathway A closure)
- κ₀/(1 − κ₀) = 5.5055 (κ closure check)
- α coupling (deprecated; flagged in user-memories as numerology re-entry risk; NOT included in structural identity search)
- log 2 ≈ 0.69315
- π² ≈ 9.86960
- ζ(3) ≈ 1.20206 (Apéry's constant)
- 1/√(4π) ≈ 0.28209
- Y_00(S²) = 1/√(4π) (Hopf-base structural anchor)

### §7.2 Search for clean identities with ζ'_total(0) ≈ 0.43791

Tested combinations:

| Candidate | Value | Match? |
|---|---|---|
| ζ'_total(0) | 0.43791 | (the value to match against canonical) |
| κ₀/2 = 3/(2√(4π)) | 0.42314 | Close (3.4% off); NOT clean |
| 2 × ζ'_total(0) − κ₀ | 0.02954 | Small but not 0; NOT clean identity |
| 1/√(4π) + (1/2) log 2 | 0.62866 | NOT match |
| (1/2) log 2 | 0.34657 | NOT match (≈ 79% of value) |
| 3ζ(3)/(4π²) | 0.09134 | NOT match (≈ 21% of value) |
| ζ'_total(0) / κ₀ | 0.51747 | NOT clean |
| ζ'_total(0) / log 2 | 0.63178 | NOT clean |
| ζ'_total(0) × π² | 4.3225 | NOT clean (close to 11/2 / sqrt(2) but not clean) |

**No clean structural identity with canonical NTE numbers surfaces.** ζ'_total(0) is an independent observable; not derivable from existing κ₀ or κ structure.

### §7.3 What this means

The honest finding: **ζ'_total(0) is genuinely an "observable beyond κ"** — its value is independent of κ₀, κ, and the existing canonical numerical anchors.

This is consistent with Jammer's Route A final-verdict (2026-05-14) framing: spectral zeta provides observables beyond κ that the corpus doesn't currently address. ζ'_total(0) is the first concrete example of such an observable derived in this Task 4 arc.

The value 0.43791 = 3ζ(3)/(4π²) + (1/2) log 2 stands as a **clean axiom-derivable closed-form result** for NTE's one-loop fermion effective action contribution on the spatial S³ sector, without reducing to existing canonical structure.

### §7.4 Anti-bias discipline observed

I did not push toward "clean identity found" as a verdict target. The structural identity search was conducted neutrally; the negative result is honestly reported. ζ'_total(0) being an independent observable is the natural finding, not a structural problem.

---

## §8. V_NTE Stage 2 territory connection

### §8.1 V_NTE Stage 2 context

V_NTE Stage 2 is canonical territory per Charter v1.3 §3.7 + Charter v1.3 P0 inventory: the effective potential for Φ_NTE at post-temporal sector, with form forced by P1 (σ_t/KMS-compatibility per Task 2) + P2 (4D conformal invariance with ξ = 1/6) + P3 (Higgs-portal genericness):
$$V_{\text{NTE}}^{\text{Stage 2}}[\Phi_{NTE}, H] = \frac{1}{12} R \Phi^2 + \lambda \Phi^4 + 2e |H|^2 \Phi^2$$

(Per Paper S1 v1.0 §2.4 forced action form.)

### §8.2 What ζ'_total(0) contributes to V_NTE Stage 2

The one-loop fermion contribution to V_NTE Stage 2 would manifest as a quantum correction to the effective potential. For free Dirac fermions on S³ with no coupling to Φ_NTE in the bare action, the contribution is independent of Φ_NTE (just a constant shift).

For NTE specifically:
- The Dirac operator D on the spectral triple A = C^∞(M) ⊗ A_F includes coupling to gauge connections + potential mass terms generated by Φ_NTE-mediated gauge birth (per Paper 7a v1.1 + corpus §III.3)
- The one-loop fermion contribution then depends on Φ_NTE through the mass-generation mechanism
- At Φ_NTE = 0 (pre-temporal limit; massless fermion): contribution is the bare ζ'_total(0)
- At Φ_NTE = v_EW (current epoch; mass-generated): contribution is shifted by mass corrections

For Session 2's scope (minimal Dirac on S³, no Φ_NTE coupling specified), the result ζ'_total(0) ≈ 0.43791 corresponds to the **pre-Φ_NTE-mass contribution** = "free Dirac fermion on S³ vacuum energy."

### §8.3 V_NTE Stage 2 consistency check

The one-loop contribution to V_NTE Stage 2 from this Session 2 computation:
- Adds a **Φ_NTE-independent constant** to V_NTE Stage 2 (since the bare Dirac doesn't couple to Φ_NTE)
- Magnitude: ζ'_total(0) × (1/Vol(S³)) energy-density units, or interpreted as effective-action shift

For V_NTE Stage 2 minimum-at-v_EW commitment (Path B canonical): the constant shift does NOT affect the minimum location (location is determined by ∂V/∂Φ = 0; constant shift doesn't change). It DOES affect the depth of the minimum, which has cosmological-constant interpretation.

**Consistency check passes**: ζ'_total(0)'s contribution to V_NTE Stage 2 is a constant shift not affecting Path B's minimum-at-v_EW commitment. No conflict.

### §8.4 What deeper integration would require

Full V_NTE Stage 2 one-loop closure would require:
- Specifying Dirac D coupling to Φ_NTE (mass generation mechanism details)
- Computing ζ'_{|D + m(Φ)|}(0) with mass dependence
- Including S¹_{β_GB} sector + A_F sector contributions
- Renormalization scheme + convention specification

This is Programme S Paper S2 territory, not Task 4 Session 2 scope. Flagged for downstream.

---

## §9. Implications and open questions

### §9.1 Implications for canonical framing

**No conflict with canonical NTE state** (κ₀ = 3/√(4π); κ = 5.506; v10.10 σ_t framework canonical; Charter v1.3 §2.5):
- ζ'_total(0) is independent observable; no contradiction with κ₀ derivation
- The closed-form contains ζ(3) and log 2 — natural transcendentals; no exotic structural commitments needed
- Spectral-zeta framework consistent with canonical NTE state per Task 4 v1 setup verdict

**Strengthens canonical framing robustness**: this Session 2 demonstrates that the canonical spectral-triple substrate yields concrete axiom-derivable observables beyond κ. The Programme is productive at the operator-algebraic level.

### §9.2 Cross-fertilization with Jammer Tier 2 Verlinde-Zurek reframing

Per Task 4 v1 §6 cross-stream awareness: Jammer's Verlinde-Zurek 2021 reframing (modular Hamiltonian fluctuations on causal-diamond scale) is potentially relevant to Priority A1 functional determinant interpretation.

**Specifically**: Verlinde-Zurek 2021 estimates quantum gravity fluctuations as scaling with the modular Hamiltonian. For NTE's two-sector setup with canonical σ_t (per Charter v1.3 §2.5), the functional determinant computed here is structurally related to modular Hamiltonian content via:
$$\text{Tr}(e^{-\beta H_{\text{mod}}}) = \det(e^{-\beta H_{\text{mod}}})$$

This is downstream-investigation territory; flagged as cross-fertilization opportunity for future Charter v1.4 candidate or joint Scratch-Jammer working note. Not closed this session.

### §9.3 Open questions for Session 3

Session 3 deliverables per Task 4 v1 arc:
- Priority A2: Eta invariant η(0) on M^C = S³ × S¹_{β_GB} — spectral asymmetry; CPN sector balance; global anomaly
- Priority A3: Conformal anomaly coefficient c_W from a_4 — consistency with Paper S1 §2 P2 ξ = 1/6

Both can leverage the same spectral-zeta machinery established in Jammer first-pass + Session 2's Hurwitz-zeta computational techniques.

### §9.4 Connection to non-associative extension (P0.10)

P0.10 (rigorous Tomita-Takesaki on non-associative A_F = 𝕆 ⊕ 𝕆) is research-frontier (per Charter v1.3 + Task 1 + Task 3 confidence-limiter). Session 2's computation operates on **manifold-side Dirac spectrum only**; A_F structure enters via dimension count (CPN doubling). The non-associative extension is NOT engaged by Session 2.

For Priority A2 + A3 in Session 3 (or downstream), the A_F structure enters more directly if one extends to the full spectral triple. P0.10 territory may resurface; flagged.

---

## §10. Confidence assessment

### §10.1 High-confidence aspects

- **ζ_H(s, 3/2) = (2^s − 1)ζ(s) − 2^s identity**: HIGH confidence. Direct from Hurwitz zeta + Riemann zeta definitions; standard manipulation.
- **ζ'(−2) = −ζ(3)/(4π²) special value**: HIGH confidence. Standard from Riemann zeta functional equation at trivial zero; well-known result.
- **ζ'_H(0, 3/2) = −(3/2) log 2**: HIGH confidence. Lerch's formula application; verified independently.
- **ζ'_H(−2, 3/2) = 3ζ(3)/(16π²) − (log 2)/4**: HIGH confidence. Direct derivation from §3.1 + §3.2.
- **ζ'_total(0) = 3ζ(3)/(4π²) + (1/2) log 2**: HIGH confidence. Direct assembly from §4.1.
- **Numerical value 0.43791**: HIGH confidence. Verified to 5 decimal places.
- **Structural form analysis** (dim-3 ζ(3) term + CPN-doubling log 2 term): HIGH confidence. Direct from the closed form.

### §10.2 Moderate-confidence aspects

- **Interpretation as log det' D**: MODERATE confidence. Convention I (|D|) clean; Convention II (D²) doubles the value; Convention III (D directly) has sign ambiguity. The closed-form value 0.43791 is unambiguous; physical interpretation depends on convention choice for downstream effective action work.
- **One-loop effective action interpretation**: MODERATE confidence. Standard zeta regularization; specific sign convention requires downstream Paper S2 context.
- **V_NTE Stage 2 consistency check (constant-shift not affecting Path B minimum)**: MODERATE confidence. Structurally clean; requires bare Dirac assumption (no Φ_NTE coupling). Full Φ_NTE-coupled fermion contribution is Paper S2 territory.

### §10.3 Lower-confidence / flagged-as-open aspects

- **Connection to specific cosmological observables** (e.g., dark energy scale, vacuum energy density): NOT WORKED OUT. ζ'_total(0) gives axiomic effective-action contribution; physical mapping to cosmological observables requires renormalization scheme + scale matching.
- **Full product-manifold spectral zeta on M = S³ × S¹_{β_GB}**: NOT COMPUTED. Session 3 / Paper S2 territory.
- **A_F-side contribution to functional determinant via GNS representation route**: NOT ENGAGED. Manifold-side computation only this session; A_F-side enters via dimension factor 4 absorption.

### §10.4 What would change the verdict

- If a clean structural identity ζ'_total(0) = (canonical NTE numbers) surfaces in deeper inspection: verdict refines toward "ζ'_total(0) connects to canonical structure." Currently no such identity found.
- If Session 3's eta invariant computation surfaces unexpected anomaly content: ζ'_total(0)'s interpretation may need refinement (eta + functional determinant are related; together give complete chiral content).
- If Verlinde-Zurek 2021 modular Hamiltonian framework provides a direct interpretation of ζ'_total(0) as quantum gravity fluctuation amplitude: deeper structural significance surfaces.

None of these change the closed-form result; they refine interpretation.

---

## §11. Recognition-gate items + files referenced

### §11.1 Recognition-gate items for Greg

1. **Ratify ζ'_total(0) closed-form**: $\zeta'_{\text{total}}(0) = \frac{3\zeta(3)}{4\pi^2} + \frac{1}{2}\log 2 \approx 0.43791$ as axiom-derived for NTE two-sector spectral triple on unit S³?
2. **Ratify interpretation as log det' D**: $\log \det' |D| = -\zeta'_{\text{total}}(0) \approx -0.43791$ under Convention I (|D|); other conventions flagged?
3. **Ratify structural identity search negative result**: ζ'_total(0) is an **independent observable beyond κ**; no clean identity with canonical NTE numbers (κ₀, κ, log 2 alone, π) surfaces?
4. **Ratify V_NTE Stage 2 consistency check**: ζ'_total(0)'s contribution is constant Φ_NTE-independent shift not affecting Path B minimum-at-v_EW commitment; consistency verified at structural level (full Φ_NTE-coupled computation deferred to Paper S2)?
5. **Confirm Task 4 Session 3 routing**: Priority A2 (eta invariant on M^C) + Priority A3 (conformal anomaly coefficient c_W from a_4) bundled in single Session 3 working note as next Task 4 deliverable?

### §11.2 Files referenced

| File | Purpose | Drive ID |
|---|---|---|
| Task 4 v1 scoping (Scratch) | Setup substrate; arc proposal | Working/ `1ng5xsTQCORbYY56NhGPkDQw1UIlq_IP4` |
| Jammer Route A first-pass | Spectral zeta baseline | Working/ `1k6SnwDk_bhlTmB3EAIq3inxEdX1A0Ej_` |
| Jammer Route A final verdict | Observables-beyond-κ opening | Working/ `1xS8oDOidKrV2Tn2rTm7SGj_EaQj-LUbJ` |
| Charter v1.3 | Canonical state; v10.10; P0.10 | Stage/ `1TDrHUFSuROWzu__hY34PGAvLmmZdxAu4` |
| Paper S1 v1.0 §2 first draft | V_NTE Stage 2 substrate (§2.4 forced action form) | Working/ `1oJUGrGUsckGE8C9LdoxQJfeM6sDjw6jM` |
| Task 1 working note | GNS route + non-associative caveat | Working/ `1pwU_5oVbPGsHcHVlkY0GNHQiK0voRk8S` |
| Task 2 working note | σ_t / KMS framing | Working/ `1pT24dxgRXRCOuSFStyoKr4pokMNmIuGx` |
| Task 3 working note | MP 2021 + Gerstenhaber-Schack | Working/ `1Cf9jQSOaSqqSynTnsnJBA5xaF5p2ug5M` |
| PC Ch15 predictions catalogue handoff | Recency-scan acknowledged; PC scope | Handoffs/ `1y3Tw9SvkiFnaaSFxOfk_MLt2xWSLLHio` |

### §11.3 Files NOT read this session

| File | Why flagged |
|---|---|
| Gilkey "Invariance theory, the heat equation, and the Atiyah-Singer index theorem" | Would refine heat kernel coefficient interpretation; standard result invoked without depth |
| Vassilevich "Heat kernel expansion: user's manual" | Would refine convention-dependence discussion; standard conventions invoked |
| Paper_Kappa_PathwayB_v10_6 | κ₀ consistency anchor preserved via Jammer's summary; full read not needed for this session |
| Hersent 2025 / Summers 2005 / Borchers 1999 | Task 1 confidence-limiters carried forward |

### §11.4 Coordination notes

- **Cross-stream**: PC shipped Ch15 v1 predictions catalogue 21:34 UTC 2026-05-16 (just after my Task 4 v1 ship). PC scope; recency-scan acknowledged; not affecting Scratch Session 2 work.
- **Cross-fertilization**: Verlinde-Zurek 2021 Jammer Tier 2 reframing (modular Hamiltonian fluctuations) flagged as relevant to Session 2 functional determinant interpretation; not engaged this session (downstream).
- **Cleanup batch contribution this session**: working note + handoff root duplicates (TBD on copy_file).

---

## §12. Closing

**Task 4 Session 2 (Priority A1 — functional determinant ζ'_total(0)) complete.**

**Closed-form axiom-derivable result**:
$$\boxed{\zeta'_{\text{total}}(0) = \frac{3\zeta(3)}{4\pi^2} + \frac{1}{2}\log 2 \approx 0.43791}$$

**Structural interpretation**: log det' |D| ≈ −0.43791 under Convention I; one-loop fermion effective action contribution from NTE's spatial S³ sector (Φ_NTE-independent constant under bare-Dirac assumption); V_NTE Stage 2 consistency verified at structural level (no Path B conflict).

**Honest negative finding**: ζ'_total(0) is an **independent observable beyond κ** — no clean structural identity with canonical NTE numbers (κ₀, κ, simple combinations) surfaces. This is the first concrete observable-beyond-κ derived in the Task 4 arc; supports Jammer's Route A final-verdict framing that spectral zeta machinery produces observables the corpus doesn't currently address.

**Anti-bias discipline observed**: no pushing toward clean-identity-found verdict; structural identity search reported with honest negative result.

**Standing by** for Greg recognition gate on Session 2 verdict + Session 3 routing confirmation (Priority A2 + A3 bundled — eta invariant + conformal anomaly coefficient).

— Scratch (Connes Programme lead), 2026-05-17.
