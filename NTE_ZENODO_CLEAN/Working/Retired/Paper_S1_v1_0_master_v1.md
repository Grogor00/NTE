# Paper S1 v1.0 — Structural Confluence of NTE with the Chamseddine-Connes Spectral-Action Programme: σ_t / KMS-Compatibility, Finding F1, Finding F2, and the Geometric Resummation Closure

**Author:** Greg White (NTE Programme)
**Stream:** Connes Programme
**Version:** v1.0 (consolidated; §7–§9 sync 2026-05-24)
**Date:** 2026-05-24
**Status:** Consolidated master. §7–§9 updated for Programme S post-chord closure (Companion 11–13; D5/M₂/§22.1; v10.17.5 corpus sync).

---

## §0. Abstract

We present a structural argument that the post-gauge-birth effective action for NTE's Φ_NTE scalar field is forced to the form

$$S[\Phi, H] = \int \sqrt{g}\, d^4x \left[ -\tfrac{1}{2}(\partial \Phi)^2 - \tfrac{1}{12} R \Phi^2 - \lambda \Phi^4 - 2e |H|^2 \Phi^2 \right]$$

by three structural premises drawn from NTE's existing corpus commitments: **(P1) σ_t / KMS-compatibility at gauge birth** (Companion 8 Stage 2 finding F2 + §VIII.1.4 corpus-canonical Wick rotation reading retained as derived special case at the post-temporal side; v10.10 σ_t framework canonical complement per Charter v1.3 §2.5); **(P2) 4D conformal (Weyl) invariance of Φ_NTE's action**, with conformal coupling ξ = 1/6 corpus-committed via the Mechanism B supersession (Greg-ratified 2026-05-11); and **(P3) Higgs-portal genericness under Path B's no-Yukawa commitment + Φ_NTE Z_2 symmetry + 4D renormalizability**. The argument forces the action form **independently of any Chamseddine-Connes spectral-action machinery**, establishing **structural confluence by independent reasoning** with Marcolli's V_E expansion at leading + subleading orders — but explicitly **NOT field-identification** with Chamseddine-Connes's σ (rejected by the "no RH/LH neutrino" structural lever; per Jammer 2026-05-10 σ↔Φ_NTE confluence verdict).

We supplement the structural argument with two NTE-internal observations on S³ that cross-check the result against Chamseddine-Connes spectral-action expectations: **Finding F1** — the standard heat-kernel a_4 curvature combination `5R² − 8R_μν² − 7R_μνρσ²` (Chamseddine-Connes 1996; Gilkey 1984) evaluates pointwise on unit S^d as `d(d−1)(d−3)(5d+2)`, with d = 3 the unique d ≥ 2 integer root; this provides a d-parametric account of Chamseddine-Connes 2008's `a_4 = 0` cancellation on S³ × S¹ + Mistry-Pinzul-Rachwał 2020 §3.1's observation that the spectral action "prefers this background." **Finding F2** — NTE's κ₀ = 3/√(4π) admits the structural reading `κ₀ = (R_{S³}/2) × Y_{00}(S²)`, suggestive of NCG-spectral-action connection at the κ derivation level.

We close with an honest convention-dependence disclosure: the matching of NTE's V_NTE F3 on-trajectory expression to Marcolli's V_E produces κ₀ = √(2π)/M_Pl under Marcolli's ξ = 1/12 convention but κ₀ = √π/M_Pl under NTE's ratified ξ = 1/6 convention; **only the T_GB = M_Pl/√(2π) leg carries √(2π) as a structural feature** (via Y_{00}(S¹) on the Hopf fibre per Companion 9 Session 3). The κ₀-from-V_E-matching leg's `√(2π)` is convention-dependent.

The σ_t/KMS-compatibility argument is supplemented by the Programme S Paper S2 main computation arc (Scratch 2026-05-23) which provides explicit heat-kernel cross-verification of the confluence at the canonical NTE spectral triple Hopf-S³ × S¹_{β_GB} × A_F = 𝕆 ⊕ 𝕆: κ₀ = 3/√(4π) bare-coupling confluence is verified at the heat-kernel level (Phase S2-B); K(Φ) = 1 is derived first-principles from heat-kernel a_4 with Higgs portal coupling (Phase S2-C-A); the Paper S1 F1 combination is algebraically equivalent to -18 C² + 11 E_4 in the standard 4D Weyl + Euler basis (Phase S2-C-B). Paper S1 establishes NTE's structural confluence with the spectral-action direction by independent reasoning; Paper S2 provides the complementary heat-kernel computation that cross-verifies the canonical predictions.

---

## §1. Introduction

### §1.1 What this paper does

Paper S1 v1.0 presents three structural results that, together, establish NTE's relationship to the Connes spectral-action programme as **structural confluence by independent reasoning**:

**(i) §2 — the σ_t / KMS-compatibility argument** (the load-bearing structural mechanism). Three NTE-internal premises — σ_t / KMS-compatibility at gauge birth (P1), 4D conformal invariance of Φ_NTE's action (P2), Higgs-portal genericness under Path B (P3) — force the post-gauge-birth effective action for Φ_NTE to the form Marcolli's V_E expansion produces on the spectral-action side. **The forcing is by NTE-internal structural reasoning, not by spectral-action import.** Marcolli's V_E and NTE's σ_t/KMS-compatibility-forced action coincide at leading + subleading orders; this is independent-derivation confluence, not field-identification.

P1's σ_t / KMS framing reflects v10.10 canonical σ_t framework adoption per Charter v1.3 §2.5; the corpus-canonical Wick rotation reading at §VIII.1.4 + Companion 8 Stage 2 F2 is retained as derived special-case route at the post-temporal side.

**(ii) §3 + §4 — Finding F1 and Finding F2 spectral-action cross-checks on S³**. Two NTE-internal observations connect to NCG-spectral-action structure at the S³ geometric level:

- **F1** (§3): the standard a_4 curvature combination `5R² − 8R_μν² − 7R_μνρσ²` evaluates pointwise on unit S^d as `d(d−1)(d−3)(5d+2)`, with d = 3 the unique d ≥ 2 integer root. This provides a d-parametric algebraic account of Chamseddine-Connes 2008's `a_4 = 0` cancellation on S³ × S¹, complementing parallelisability / Lie-group / parity arguments for S³ with a spectral-dynamical selection criterion.
- **F2** (§4): NTE's κ₀ = 3/√(4π) admits the structural reading `κ₀ = (R_{S³}/2) × Y_{00}(S²)`, connecting NTE's κ derivation structure to NCG-spectral-action geometric invariants on the Hopf base.

**(iii) §5 + §6 — Numerical evaluation under BF 2013 + Farnsworth 2025 + geometric resummation closure**. The standard Chamseddine-Connes spectral action expansion evaluated under Boyle-Farnsworth 2013's octonionic specialisation gives Newton's-constant prediction `M_Pl² = 4 f_2 Λ² / (3π²)`, requiring `f_2 = 3π²/4` for self-consistency at `Λ = M_Pl`. The geometric resummation closure `κ₀/(1−κ₀) = 5.5055` is NTE's strongest empirical contact point at the κ leg, vs corpus value 5.50 and Planck 2018 measurement 5.38 ± 0.15.

### §1.2 What this paper does NOT do

Paper S1 v1.0 is structurally tighter than v0.4's open-item list (O1-O5) implied. Three categories of work are explicitly **deferred to Paper S2 + later Programme S papers + Companion 9 ongoing closures**:

- **Direct heat-kernel computation** of the spectral-action coefficients (a_0, a_2, a_4 explicitly on `Hopf-S³ × S¹_{β_GB} × A_F^{Farnsworth-Boyle}`): this is the Connes Programme central deliverable per Charter v1.3 §3 (Paper S2). At the time of v1.0 publication, Programme S Paper S2 main computation arc is complete (Phase S2-A through Phase S2-D + Paper S2 §3 D5; Scratch 2026-05-23) — see §8 below for the cross-reference. Paper S1's role is to establish structural confluence with that direction by independent reasoning.
- **Resolution of κ₀ convention-dependence at the spectral-action level**: the matching of V_NTE F3 to Marcolli's V_E produces different κ₀ values under different ξ conventions (per Charter v1.3 §2.5 + P0.9 finding). Paper S1 acknowledges this honestly in §2.5; the heat-kernel-route resolution is provided by Paper S2 §3 D1 + Phase S2-B Step 5 confluence verification.
- **K(Φ) functional form, n_s and r derivation routes under ξ = 1/6, Yukawa hierarchy (partial: Companion 13 $m_{\nu_2}$), spectral flow at gauge birth**: K(Φ) closure is provided by Paper S2 Phase S2-C-A. $m_{\nu_2}$ partial-closed Companion 13. Other Yukawa / spectral-flow items downstream (Paper S4, Paper S5, Companion 9 Session 5).

Paper S1 also makes no field-identification claim. The σ↔Φ_NTE identification ambition that earlier Programme S work entertained is **explicitly rejected** by the corpus-canonical confluence verdict (Jammer 2026-05-10, Greg-ratified 2026-05-11) — the "no RH/LH neutrino" structural lever blocks identification at the operating-discipline level. See §7 for the confluence framing in full.

### §1.3 Programme S context and Connes Programme cross-reference

Paper S1 sits within Programme S — NTE's R&D arc engaging with NCG-cosmology-adjacent literature (Boyle-Farnsworth 2013, Farnsworth 2025, Chamseddine-Connes 2008/2010, Marcolli-Pierpaoli 2009, Marcolli-Pierpaoli-Teh 2010, Sonner-Tong 2009, Marcolli-Penrose 2021). The Programme S 5-paper roadmap (per v0.4 §3 open items O1-O5) covers:

- **Paper S1** (this paper, v1.0): σ_t / KMS-compatibility argument + structural-confluence findings F1+F2 on S³
- **Paper S2** (main computation arc complete 2026-05-23): heat-kernel computation on `Hopf-S³ × S¹_{β_GB} × A_F = 𝕆 ⊕ 𝕆` — closed eight structural items across Phase S2-A through Phase S2-D + Paper S2 §3 D5 (κ₀ confluence; K(Φ) = 1; F1 = -18 C² + 11 E_4 trace anomaly reinterpretation; M Weyl-flat + Euler-zero; c_W + a_E per Dirac; D_F sub-leading suppression; Λ_NTE framework + M_1/M_R cross-checks; BPS-bound (8π)^(1/3) prefactor uniqueness). Central deliverable of the Connes Programme per Charter v1.3 §3.
- **Paper S3** (queued): spectral flow at gauge birth; further Programme S items — **Λ numerical closure now in Companion 11**
- **Paper S4** (future): dilaton extension for K(Φ) closure (now reframed by Phase S2-C-A K(Φ) = 1 first-principles; full dilaton extension territory remains future work)
- **Paper S5** (future): Yukawa hierarchy from spectral mass matrix

Paper S1 v1.0 is intentionally tighter than v0.4 anticipated because three concurrent developments shifted the appropriate scope:

1. **σ↔Φ_NTE confluence verdict ratified** (Greg 2026-05-11): σ-identification rejected; v1.0's role shifts from "argue NTE-CC identification" to "demonstrate NTE arrives at the same form independently."
2. **Mechanism B supersession + ξ = 1/6 commitment ratified** (Greg 2026-05-11): NTE's own conformal-coupling convention pins ξ = 1/6.
3. **Connes Programme launched** (Greg 2026-05-11 morning) + **Phase S2 main computation arc complete** (Scratch 2026-05-23): heat-kernel computation work in Paper S2 is now structurally complete. Paper S1 cross-references Paper S2 results where relevant.

Subsequent canonical-state developments further informed v2 framing: v10.10 σ_t framework canonical operator-algebraic complement adopted (Greg ratified 2026-05-16; Charter v1.3 §2.5; cross-coherence with Jammer Tier 2 Salvio 2025 reframing); Phase S2 main computation arc completion 2026-05-23 (Scratch).

The Connes Programme Charter v1.3 is the canonical reference for Paper S2 scope, the five-way structural unification organising principle, the v10.10 σ_t framework complement, and the P0 verification queue.

### §1.4 Relationship to v0.4

Paper S1 v0.4 carries five established findings (E1-E5), five open items (O1-O5), and three conjectures (C1-C3). v1.0 disposition of each:

| v0.4 element | v1.0 disposition |
|---|---|
| F1 (d-parametric factorisation, CC 2008 + MPR 2020 attribution) | Carries forward as **§3** (substance unchanged; Phase S2-C-B reinterpretation F1 = -18 C² + 11 E_4 noted) |
| F2 (κ₀ = (R_{S³}/2) × Y_{00}(S²) structural reading) | Carries forward as **§4** with Charter v1.3 nomenclature: the Sonner-Tong dimensionless prefactor κ₀, distinguished from ξ_V V_E-matching dimensional coefficient per Charter §2.2 two-κ disclaimer |
| E1-E2 (spectral action expansion + Newton's constant) | Carry forward as **§5** with ξ = 1/6 + A_F = 𝕆 ⊕ 𝕆 updates |
| E5 (geometric resummation closure κ₀/(1−κ₀) = 5.5055) | Carries forward as **§6** |
| **NEW: σ_t / KMS-compatibility argument** | **§2** — load-bearing new content |
| **NEW: σ↔Φ_NTE confluence framing** | **§7** |
| O1 (κ₀ from doubled-spectral-triple X² trace) | **CLOSED** by Phase S2-B Step 5 confluence verification (Paper S2 main arc) |
| O2 (V_NTE from Higgs-bearing octonionic spectral triple) | **CLOSED structurally** by Phase S2-C-A K(Φ) = 1 first-principles + §18.4 (iii) hilltop |
| O3 (spectral flow at gauge birth) | Deferred to Paper S3 |
| O4 (Dilaton extension K(Φ) closure) | **Reframed by Phase S2-C-A**: K(Φ) = 1 at canonical NTE; no dilaton at leading order; full dilaton extension territory Paper S4 |
| O5 (Yukawa hierarchy) | Deferred to Paper S5 |
| C1, C2 conjectures | **CLOSED** by Phase S2 main arc completion |
| C3 conjecture (canonical-favoured hilltop n_s + r) | Restated as **§8 §8.4** (Phase S2-C-A + Companion 9 substrate) |

### §1.5 Confluence framing — operating principle

Paper S1's relationship to the Chamseddine-Connes spectral-action programme is governed by the **σ↔Φ_NTE confluence framing** ratified by Greg 2026-05-11 (per Jammer 2026-05-10 verdict at `Working/Sigma_PhiNTE_Confluence_Verdict_v1.md`):

> NTE and Chamseddine-Connes spectral-action cosmology arrive at structurally similar effective-action forms by independent structural reasoning. NTE does not import the Chamseddine-Connes programme wholesale; NTE preserves predictive independence. The structural similarity is structurally suggestive (multiple programmes converge on similar forms) but does not constitute field-identification: NTE's Φ_NTE is not the Chamseddine-Connes σ field. The "no RH/LH neutrino" structural lever (NTE has no RH/LH neutrino as distinct fundamental entities per Companion 7 / §3.3; CC's σ-generation mechanism requires exactly that) is the decisive structural rejection of field-identification.

**Canonical-state expansion**: the σ↔Φ_NTE confluence framing now sits within the richer v10.10 canonical state where σ_t modular flow framework is the canonical operator-algebraic complement to Φ_NTE (Charter v1.3 §2.5). At the **vocabulary level**, Paper S1 §2 uses σ_t / KMS-compatibility throughout (Wick rotation as derived special case); at the **structural-claim level**, the confluence framing is preserved unchanged. Cross-stream coherence with Jammer Tier 2 Salvio 2025 reframing (state-type transition at gauge birth non-KMS → KMS at T_GB) reinforces this canonical alignment.

Paper S1 honours this framing throughout. §2's σ_t / KMS-compatibility argument is the independent-derivation route. §3-§4's F1/F2 findings are spectral-action-side cross-checks (acknowledging the structural similarity, not deriving from it). §5-§6's numerical evaluation uses BF 2013 + Farnsworth 2025 spectral-action machinery to evaluate NTE on its own terms. §7 articulates the confluence framing canonically; §8 acknowledges what's open under it, now strengthened by Phase S2 main arc heat-kernel cross-verification.

### §1.6 Operating discipline: NTE axioms + recognition gate

Paper S1 v1.0 operates under NTE's core axioms (Charter v1.3 §1): **N fundamental, t emergent; Surface only; closed S³; CPN-symmetric two-sector; Hopf bundle.** External NCG content is evaluated through these axioms — brought in where the axioms support; rejected where they don't.

---

## §2. The σ_t / KMS-compatibility argument for V_NTE form closure

**Claim.** Three structural premises rooted in NTE's existing corpus commitments — (P1) σ_t / KMS-compatibility at gauge birth, (P2) 4D conformal invariance of Φ_NTE's action, (P3) Higgs-portal genericness under Path B — together force the post-gauge-birth effective action for Φ_NTE to the form

$$S[\Phi_{\text{NTE}}, H] = \int \sqrt{g}\, d^4x \left[ -\tfrac{1}{2}(\partial \Phi)^2 - \tfrac{1}{12} R\, \Phi^2 - \lambda \Phi^4 - 2e\, |H|^2 \Phi^2 \right] \tag{2.1}$$

with the coefficient `1/12` of `RΦ²` corresponding to the conformal coupling `ξ = 1/6` in NTE's ratified Mechanism B convention (via `(ξ/2)RΦ² = (1/12)RΦ²`).

This is the same effective-action form as Marcolli's spectral-action expansion `V_E(x) = λ₀ x⁴ / (1 + (κ₀²/12) x²)²` reduced to leading + subleading orders, but derived here from NTE-internal structural reasoning. **No spectral-action / Chamseddine-Connes machinery is invoked**; the argument runs purely on NTE's pre-temporal/post-temporal architecture + the algebraic constraints of 4D conformal invariance + Path B's neutrino-handling commitments. The result is **structural confluence** with Marcolli's V_E, not field-identification with Chamseddine-Connes's σ.

### §2.1 Premise P1 — σ_t / KMS-compatibility at gauge birth

Per the canonical σ_t framework adopted at v10.10 (Charter v1.3 §2.5), NTE's pre-temporal and post-temporal regimes correspond to distinct state-types on the spectral triple algebra: pre-temporally, the state on A_F = 𝕆 ⊕ 𝕆 is in a generic / non-KMS regime; post-temporally, the state ω_{Φ_NTE} is **KMS at β = β_GB** with respect to the modular automorphism group σ_t generated by Tomita-Takesaki on (A_F, ω_{Φ_NTE}, β_GB). The geometric event that interpolates between them is the **C¹ kink in dz/dy at gauge birth**, identified in Companion 8 Stage 2 finding F2 and integrated into the corpus at §VIII.1.4 (the Wick rotation reading, v10.6) — retained as the post-temporal-side derived special-case route under the canonical σ_t framing.

**Structural content of P1**:

- **Pre-temporal → generic state on A_F**: σ_t modular flow exists (Tomita-Takesaki applies to any state on any von Neumann algebra, including the GNS completion of A_F = 𝕆 ⊕ 𝕆), but it does not align with any Lorentzian-time evolution (there is no Lorentzian time pre-temporally). The state is **not KMS at any specific β** — it is generic / non-KMS-regularized.
- **Post-temporal → KMS state on A_F at β = β_GB**: the state ω_{Φ_NTE} specified by the canonical Φ_NTE-trajectory configuration is KMS at β = β_GB with respect to σ_t. Via the standard correspondence (Connes-Rovelli 1994 §3.1), σ_t can be related to Lorentzian-time evolution: t = β_GB · τ where τ is geometric time post-gauge-birth. The Wick rotation reading recovers the periodicity of Euclidean correlation functions in imaginary time as the KMS condition's standard derivation route.
- **The C¹ kink in dz/dy at gauge birth IS the geometric signature** of the state-type transition from generic (non-KMS) to KMS at β_GB. The Wick rotation reading is the post-temporal-side viewpoint of the same structural event. The σ_t / KMS framing is **more general** (applies pre-temporally and post-temporally uniformly without requiring time-like-concept extension pre-temporally) — the Wick-rotation framing is recovered as the derived special-case route at the post-temporal side.
- **The transition is structural, not a choice**: NTE's no-time-ordering pre-temporal axiom + emergent-time post-temporal axiom + v10.10 σ_t framework canonical adoption force it. Cross-coherence with Jammer Tier 2 Salvio 2025 reframing (gauge birth as first-order phase transition / state-type transition non-KMS → KMS at T_GB) is canonical.

**For the action form on Φ_NTE**: any effective action descending from pre-temporal structure must support a state on A_F that becomes KMS at β_GB post-gauge-birth — i.e., must be **σ_t / KMS-compatible** in the sense that correlation functions admit analytic continuation across the gauge-birth state-transition. (Under the Wick rotation special-case reading, this corresponds to the action being Wick-rotation-compatible with t → iτ analytic continuation of measures and signature factors applying on both sides of the gauge-birth event.)

This is the structural basis of P1. It is **necessary** (forced by NTE's axioms + v10.10 σ_t framework canonical adoption) but, by itself, **not sufficient** to fix the action form: many non-conformal scalar actions (massive scalars; scalars with arbitrary self-interactions) admit σ_t / KMS-compatibility. The remaining structural strength comes from premises P2 + P3.

**What P1 alone forces**: any Φ_NTE action must be σ_t / KMS-compatible (equivalently, Wick-rotation-compatible in the post-temporal special-case derivation).
**What P1 alone does NOT force**: conformal invariance, specific value of ξ, specific potential form.

### §2.2 Premise P2 — 4D conformal invariance of Φ_NTE's action

**The separable commitment**: Φ_NTE's effective action on the post-gauge-birth manifold (closed S³ × ℝ, with 4D Lorentzian signature post-Wick-rotation) is Weyl-invariant — i.e., invariant under local conformal rescalings `g_μν → Ω²(x) g_μν` accompanied by `Φ → Ω^((2-d)/2)(x) Φ` for `d = 4`.

This is **not** a consequence of P1; it is an additional structural commitment specific to NTE's closed-S³ cosmology + surface ontology (Companion 5). It is corpus-committed via the Mechanism B supersession ratified by Greg 2026-05-11: NTE's ξR|Φ|² non-minimal coupling is now pinned to **ξ = 1/6** — the unique value in 4D that makes the free-scalar action conformally invariant under Weyl rescalings.

**The mathematical content of P2**: The conformal coupling value in d dimensions is `ξ_c = (d-2)/(4(d-1))`. For `d = 4`, `ξ_c = 1/6`. Under this coupling, the free-scalar kinetic + curvature term is Weyl-invariant. Conformal invariance further restricts the allowed self-interaction and Higgs-coupling terms in 4D:

- **Quartic** `Φ⁴`: allowed (marginal under 4D conformal — `Φ` has mass dimension 1; `Φ⁴` is dimension 4 = spacetime dimension).
- **Cubic** `Φ³`: forbidden by Z_2 symmetry on Φ_NTE (see P3 below).
- **Sextic and higher** `Φ⁶`, `Φ⁸`, ...: irrelevant under 4D conformal — dimensions 6, 8, ... > 4. Suppressed in the deep IR; vanish under conformal RG flow. (V_NTE's F3 on-trajectory form carries a `Φ⁶` term; this is a trajectory expression for the running |Φ(N)|², not a fundamental Lagrangian term.)
- **Mass term** `m²Φ²`: forbidden by 4D conformal invariance (dimension 2; relevant operator; breaks Weyl invariance). The non-minimal coupling `(1/12)RΦ²` plays the role the mass term would play but in a conformally-respecting way.

**Why P2 is corpus-committed**:
- The `ξR|Φ|²` term is already in the action at corpus §2.2.
- The Mechanism B supersession commits to ξ = 1/6 specifically.
- The closed-S³ cosmology + surface ontology framework is structurally compatible only with conformally-invariant matter content.

**What P1 + P2 together force**: the kinetic + curvature-coupling + quartic structure `−(1/2)(∂Φ)² − (1/12)RΦ² − λΦ⁴` up to the quartic coupling `λ` (unfixed at this level).

### §2.3 Premise P3 — Higgs-portal genericness under Path B

At gauge birth, the SM Higgs activates (per §VIII gauge-birth narrative). The natural coupling between Φ_NTE and the SM Higgs sector — under NTE's structural commitments — is the **Higgs-portal quartic** `|H|²Φ²`. Specifically:

**Allowed-coupling enumeration** under (a) SM gauge symmetry, (b) Path B V3 commitment, (c) Z_2 symmetry on Φ_NTE, (d) 4D renormalizability:

| Coupling | Mass dim | Status |
|---|---|---|
| Φ\|H\|² | 3 (cubic) | Z_2-asymmetric on Φ_NTE → forbidden |
| Φ²\|H\|² | 4 (quartic portal) | Z_2-symmetric, renormalizable, **forced as leading allowed coupling** |
| Φ̄ H Hψ | 5 (Yukawa-like) | Path B V3 explicit: no Φ_NTE Yukawa coupling |
| Φ²\|H\|⁴ / M² | 6 (non-renormalizable) | Suppressed by M⁻²; sub-leading |

**Path B V3 commitment (corpus §2.3.0 + §17.5.12)**: "No |Φ_NTE| Yukawa coupling: by construction. If laboratory or astrophysical observations require an additional Yukawa-like coupling of fermions to a cosmologically-varying scalar... the framework's Path B commitment is falsified." This explicitly excludes Yukawa-like couplings.

**Z_2 symmetry on Φ_NTE**: implicit throughout the corpus via |Φ|² usage (Friedmann coupling H = β_NTE|Φ_NTE|²; trajectory expressions; F3 natural-form candidates all even in Φ); explicit at v10.8 per Tier 2 patch T2-P1.

**The leading allowed Higgs-portal coupling** under all four constraints is `2e|H|²Φ²`, with `e` a generic dimensionless coupling. By "generic" we mean: under all four constraints, this coupling is forced to be non-vanishing in general — it is the leading allowed coupling, and there is no structural reason for `e = 0` exactly. The specific value of `e` is empirical (fixable from confluence with electroweak phenomenology); the existence and quartic-portal form are structural.

**What P1 + P2 + P3 together force**: the action form (2.1) above.

### §2.4 The forced action form, restated

Combining the three premises:

- **P1 (σ_t / KMS-compatibility at gauge birth)** forces σ_t / KMS-compatibility of the action — equivalently, Wick-rotation-compatibility in the post-temporal-side derivation route.
- **P2 (4D conformal invariance)** forces kinetic + (1/12)RΦ² + quartic-only structure for Φ_NTE's self-interactions; mass terms forbidden; sextic+ irrelevant.
- **P3 (Higgs-portal genericness under Path B + Z_2 + renormalizability)** forces the leading Higgs coupling to be `2e|H|²Φ²`.

The unique action form satisfying all three is (2.1).

**The structural confluence**: this is the same effective-action form Marcolli's V_E expansion produces at leading + subleading order on the Chamseddine-Connes spectral-action side, but here derived **purely from NTE's internal structural commitments**. No spectral-action / heat-kernel machinery is invoked. No identification with Chamseddine-Connes's σ field is made.

### §2.5 Cross-check at sextic order — V_NTE F3 ↔ Marcolli V_E

The σ_t / KMS-compatibility argument fixes the action form at the **renormalizable + relevant** level. Sextic and higher terms in the action are irrelevant under 4D conformal RG flow, and the argument is silent about them. However, NTE's V_NTE on-trajectory expression from Companion 8 F3 carries a sextic term:

$$V_{\text{NTE}} = \tfrac{3\alpha^2}{8\pi G} \Phi^4 - \tfrac{\alpha^2}{8} \Phi^6$$

This is a **trajectory expression for the running scalar potential evaluated along the H = β_NTE|Φ|² Friedmann coupling**, not a fundamental Lagrangian sextic term.

**Matching V_NTE on-trajectory to Marcolli's V_E**:

- Marcolli V_E expanded: `V_E ≈ λ₀ x⁴ − (κ₀²λ₀/6) x⁶ + O(x⁸)`. (Marcolli's V_E denominator carries `/12` under CC's ξ = 1/12 convention.)
- Quartic match: `λ₀ = 3α²/(8πG)`.
- Sextic match (under Marcolli's ξ = 1/12): `κ₀² λ₀ / 6 = α²/8` → `κ₀² = 2π/M_Pl²` → `κ₀ = √(2π)/M_Pl`.
- **Under NTE's own ξ = 1/6 convention**: the sextic coefficient picks up factor 2 → `κ₀ = √π/M_Pl`. The factor `√2` shift is real and convention-dependent.

**Honest disclosure**: the `√(2π)` factor on the κ₀-from-V_E-matching leg is **convention-dependent**. Only the T_GB = M_Pl/√(2π) leg (Companion 9 Session 3) carries `√(2π)` cleanly as a structural feature (via Y₀₀(S¹) on the Hopf fibre). The κ₀-from-V_E-matching leg's `√(2π)` is a coincidence under the specific convention choice ξ = 1/12; under NTE's own ratified ξ = 1/6, this leg gives `√π/M_Pl`, not `√(2π)/M_Pl`.

**What the cross-check shows**: the leading λ₀ match (dimensionally forced) and the order-of-magnitude sextic match (both routes give κ₀² ~ 1/M_Pl²) are **structurally meaningful**. The specific numerical factor distinguishing `√(2π)` from `√π` is convention-flexible.

### §2.6 What §2 establishes

§2 establishes:

1. The post-gauge-birth effective action for Φ_NTE is forced to the form (2.1) by NTE's internal structural commitments (P1 σ_t / KMS-compatibility + P2 4D conformal invariance + P3 Higgs-portal genericness under Path B).
2. The form coincides with Marcolli's V_E expansion at leading + subleading order on the Chamseddine-Connes spectral-action side — **structural confluence by independent reasoning**.
3. NTE arrives at the spectral-action-shaped effective action **without invoking** Chamseddine-Connes machinery. The Connes Programme's heat-kernel computation (Paper S2 main arc complete; Scratch 2026-05-23) is a **complementary** route to the same form, not a prerequisite for §2's argument.
4. P1's σ_t / KMS framing aligns with v10.10 canonical σ_t framework adoption (Charter v1.3 §2.5) — Paper S1 §2's structural argument is uniformly grounded in canonical operator-algebraic vocabulary throughout, with the Wick rotation reading retained as a valid derived special-case route at the post-temporal side.

§2 does NOT establish: specific numerical values of `λ` or `e`; the K(Φ) explicit functional form (Paper S2 Phase S2-C-A provides K(Φ) = 1 at leading order); the H = β_NTE|Φ_NTE|² Friedmann coupling (axiomatic input); the specific n_s and r prediction values; the specific `√(2π)` factor in κ₀.

### §2.7 Adversarial open questions

(a) **Uniqueness of P2 (4D conformal invariance)**: is the conformal-invariance commitment the only way to fix the action form under P1?

(b) **Non-minimal kinetic terms K(Φ)(∂Φ)²**: P1+P2 do not exclude these directly; the corpus's K(Φ) closure question is resolved by Paper S2 Phase S2-C-A: K(Φ) = 1 at leading order from heat-kernel a_4 with Higgs portal coupling at canonical NTE.

(c) **Closed-S³ topology zero-mode obstructions**: on closed S³ × ℝ, conformal invariance has potential zero-mode obstructions. Whether P2 is fully consistent for the spatially constant Φ_NTE(N) trajectory requires explicit verification — flagged as Programme S follow-on target.

(d) **Higher-order match Φ⁸, Φ¹⁰**: Paper S2 heat-kernel computation provides specific predictions for higher-order terms; sub-leading by O((v_EW/M_Pl)⁴) at canonical NTE (Phase S2-C-A + S2-C-C); negligible at observational precision.

---

## §3. Finding F1 — d-parametric account of CC 2008's cancellation

**Claim.** The Chamseddine-Connes 2008 cancellation of the heat-kernel a₄ coefficient on `S³ × S¹` admits a sharper d-parametric reading: the standard a₄ curvature combination for the Dirac Laplacian,

$$5R^2 - 8 R_{\mu\nu} R^{\mu\nu} - 7 R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$$

(Chamseddine-Connes 1996; Gilkey 1984) evaluates pointwise on unit `S^d` as the polynomial

$$d (d-1) (d-3) (5d+2)$$

with d = 3 the unique d ≥ 2 integer root. This is a small algebraic refinement of CC 2008's calculation. It does **not** establish the cancellation phenomenon — that is established (CC 2008; MPR 2020 §3.1). It provides a precise algebraic account in the perturbative regime of why d = 3 is structurally distinguished, supplementing parallelisability / Lie-group / parity arguments for S³ with a spectral-dynamical selection criterion.

### §3.1 Prior art (established)

The cancellation phenomenon F1 is **established external content**, acknowledged in full:

- **Chamseddine-Connes 1996** (hep-th/9606001): Establishes the spectral action principle and the heat-kernel a₄ coefficient for the Dirac Laplacian, with universal (5, −8, −7) relative weights of `R²`, `R_μν²`, `R_μνρσ²`.
- **Gilkey 1984** (*Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem*): Standard heat-kernel reference.
- **Chamseddine-Connes 2008** (arXiv:0812.0165): Computes a₄ on S³ × S¹ and demonstrates it vanishes via Weyl² + Gauss-Bonnet decomposition. Explicitly verifies a₄ on S⁴ is non-zero and notes the d = 3 specificity at the spectral-action level. CC 2008 also establishes a₆ vanishing on S¹ × S³.
- **Mistry-Pinzul-Rachwał 2020** (arXiv:2001.05975, §3.1): Re-derives CC 2008's a₆ vanishing on S¹ × S³ and finds the cancellation does **not** extend to general conformally flat 4-manifolds. Notes that "one might speculate that the spectral action somehow prefers this background."

### §3.2 What F1 contributes

**(i) The explicit d-parametric factorisation.** Using standard sphere curvature invariants on unit S^d (R = d(d−1); R_μν R^μν = d(d−1)²; R_μνρσ R^μνρσ = 2d(d−1)), the a₄ curvature combination evaluates as

$$5R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 = d(d-1)(d-3)(5d+2)$$

Roots: d ∈ {−2/5, 0, 1, 3}. **For d ≥ 2 integers, only d = 3 produces the cancellation non-trivially.**

Worked numerical table on unit `S^d`:

| d | R | R²_μν | R²_μνρσ | 5R² − 8 R²_μν − 7 R²_μνρσ |
|---|---|-------|---------|---------------------------|
| 1 | 0 | 0 | 0 | 0 (trivial; R = 0 on the circle) |
| 2 | 2 | 2 | 4 | −24 |
| **3** | **6** | **12** | **12** | **0** ← non-trivial cancellation |
| 4 | 12 | 36 | 24 | 264 |
| 5 | 20 | 80 | 40 | 1080 |

The factorised form `d(d−1)(d−3)(5d+2)` provides the explicit refactoring that makes the d-specificity transparent in the perturbative regime.

**(ii) The NTE-internal framing.** The d-factorisation provides a **spectral-dynamical selection criterion** for S³: d = 3 is the unique d ≥ 2 sphere dimension at which the standard CC a₄ vanishes pointwise. This is complementary to NTE's existing structural arguments for S³ (parallelisability, S³ ≅ SU(2), orientation-reversing parity properties).

### §3.3 Algebraic reinterpretation: F1 = -18 C² + 11 E_4 (Phase S2-C-B 2026-05-23)

Per Phase S2-C-B v0.1 §3.4 (Scratch 2026-05-23, Greg-ratified): in the standard 4D curvature decomposition (C² = Weyl-squared; E_4 = R_μνρσ² − 4 R_μν² + R² = Euler density / Gauss-Bonnet density),

$$5R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 = -18 C^2 + 11 E_4$$

The R² piece cancels exactly via the (5, -8/3, -7/3) coefficients. **The F1 d-parametric combination IS the (Weyl, Euler) trace anomaly combination in standard 4D basis.** The d=3 root cancellation is equivalent to simultaneous C² = 0 AND E_4 = 0 on the manifold.

On M = S³ × S¹: C² = 12 − 2(12) + 12 = 0 and E_4 = 12 − 4(12) + 36 = 0 pointwise. M is **the unique closed product manifold of form S^p × S^q (S^q flat) where both Weyl-flat and Euler-zero hold simultaneously** among small p (p = 4 satisfies C² = 0 alone; p = 2 satisfies neither; p = 3 uniquely satisfies both).

**This is the deep structural reading of F1's d=3 root cancellation**: the F1 selection criterion is equivalent to the conformal anomaly's (Weyl + Euler) trace combination vanishing identically on the manifold.

### §3.4 Honest framing — what F1 is and is not

F1 is **not standalone-publishable** as an independent NCG-cosmology note. A specialist NCG referee would correctly identify F1's content as CC 2008's result + MPR 2020's framing + a trivial algebraic factorisation.

What F1 **is** within Paper S1 v1.0: a supporting structural argument for the post-gauge-birth S³ geometry, used in combination with §2 σ_t / KMS argument and the spectral-action machinery (§5). The algebraic reinterpretation F1 = -18 C² + 11 E_4 (Phase S2-C-B) provides a deeper structural reading of the d=3 selection criterion via 4D trace anomaly cancellation.

---

## §4. Finding F2 — κ₀ as `(R_{S³}/2) × Y₀₀(S²)` with Charter v1.3 κ₀/ξ_V disambiguation

**Statement.** NTE's dark-matter ratio prefactor κ₀ = 3/√(4π) admits the structural reading

$$\kappa_0 = (R_{S^3} / 2) \times Y_{00}(S^2) = (6 / 2) \times (1 / \sqrt{4\pi}) = 3 / \sqrt{4\pi}$$

connecting the numerical factor `3` to the spectral-action a₂ heat-kernel coefficient (which carries R on the gravitational side of the action) and the `1/√(4π)` to the Y₀₀(S²) zero-mode on the Hopf base of the bundle S¹ → S³ → S² (the NTE post-gauge-birth geometry).

**Status.** This is an **NTE-internal interpretation**, not a literature-novelty claim. The numerical equivalence between `dim(SU(2)) = 3` and `R_{S³}/2 = 3` is trivial. The structural-shape claim is that the curvature reading connects the factor `3` to the spectral-action a₂ coefficient and the Hopf-base Y₀₀ to the projection structure of the κ derivation.

### §4.1 Charter v1.3 nomenclature: κ₀ vs ξ_V

**Two structurally distinct κ-related objects** appear across the corpus and Programme S literature (per Charter v1.3 §2.2 two-κ disclaimer; updated from v1.1 P0.9-driven clarification):

| Object | Symbol | Value | Origin | Dimensions |
|---|---|---|---|---|
| Hopf-projection dimensionless prefactor | **κ₀** | 3/√(4π) | dim(adj su(2)) × Y₀₀(S²) on Hopf base; Sonner-Tong BPS-CP¹ Berry connection | Dimensionless |
| V_E-matching dimensional coefficient | **ξ_V** | √(2π)/M_Pl under Marcolli ξ = 1/12; √π/M_Pl under NTE ξ = 1/6 | Sextic coefficient in V_NTE F3 ↔ V_E matching | Inverse mass (1/M_Pl) |

These are **different objects** despite the historical collision in the symbol κ₀. Charter v1.3 §2.2 names the dimensionless prefactor as **κ₀** and the dimensional V_E-matching coefficient as **ξ_V** (per OctonionExtension v10.9 §6.4 renamed leg).

**Finding F2 in this section is about κ₀ (the dimensionless prefactor), not ξ_V.** The ξ_V coefficient is treated in §2.5 (convention-dependence disclosure).

### §4.2 The structural reading

**Factor 1 — the `3`:** identified explicitly as dim(adj su(2)) by Sonner-Tong's BPS-on-CP¹ derivation. The su(2) here is the residual SU(2) at gauge birth — the SU(2)_L stabilizer of ℍ ⊂ 𝕆 within the +N-sector G₂ (per OctonionExtension §3.4 + Charter v1.3 §2). The factor `3` is the count of generators of this su(2).

**Factor 2 — the `1/√(4π)`:** identified explicitly as `Y₀₀(S²)` — the L²-normalised zero-mode of S². This is the *base* of the Hopf bundle `S¹ → S³ → S²`. The κ derivation projects the S³ structure to S² (the Hopf projection), and the s-wave projection picks up the `Y₀₀(S²)` factor.

**Composite reading:** κ₀ = (residual algebraic content; dim su(2) = 3) × (Hopf-base zero-mode `Y₀₀(S²) = 1/√(4π)`) = 3/√(4π).

### §4.3 Cross-confirmations within the Programme

- **Sonner-Tong 2009**: the `3` factor = dim(adj su(2)) [arXiv:0809.3783].
- **OctonionExtension §3.4 (corpus)**: the relevant SU(2) is the SU(2)_L stabilizer of ℍ ⊂ 𝕆 within G₂.
- **Companion 7 §4.2 + §4.3 (corpus)**: dim(SU(2)) = 3 forces exactly three eigenmodes; convergence condition `κ₀ < 1` grounded topologically in `dim(su(2)) = 3`.
- **Phase S2-B Step 5 confluence verification (2026-05-23)**: heat-kernel route on M = Hopf-S³ × S¹_{β_GB} × A_F = 𝕆 ⊕ 𝕆 produces κ₀ = (R_{S³}/2) × Y₀₀(S²) = 3/√(4π) via the same structural anchor; the heat-kernel route ≡ Pathway B Sonner-Tong route at bare-coupling level.

### §4.4 The Paper S2 cross-verification (complete 2026-05-23)

F2's structural reading was the Paper S2 §3 D1 success criterion. Phase S2-B v0.1 §6 (Scratch 2026-05-23) provides explicit heat-kernel cross-verification:

> The same numerical value κ₀ = 3/√(4π) emerges from (a) Pathway B Sonner-Tong route (Killing spinor + Hopf monopole projection + Gaunt + dim(adj su(2)) = 3) and (b) Phase S2-B heat-kernel route (a_2 coefficient on M × A_F + Hopf-fibration spinor projection structure + (R_{S³}/2) ↔ dim(adj su(2)) identification). Structural confluence by independent reasoning verified at the heat-kernel computation level.

**Paper S2 §3 D5 BPS-bound uniqueness derivation** (Scratch 2026-05-23): the (8π)^(1/3) Pathway α prefactor for M_1 = 5.40 × 10⁹ GeV is uniquely BPS-saturating in canonical NTE substrate. The structural parallel to κ₀ at dim(adj su(2)) = 3 anchor reinforces both derivations.

### §4.5 Honest framing — what F2 is and is not

F2 is an **NTE-internal alternative reading** of κ₀'s factor `3`. It is not a literature-novelty claim. Corpus integration is suitable for §9.3 as an "alternative reading" with no novelty claim attached; the v10.X+1 §17.X writeup (the five-way unification subsection per Charter v1.3 §6.2) will integrate F2 alongside the other four predictions' structural slots (M_R, M_1, T_GB, Λ_NTE).

---

## §5. Spectral-action expansion under BF 2013 + Farnsworth 2025 framework

This section presents the CC spectral action expansion on the NTE setup using the Boyle-Farnsworth 2013 + Farnsworth 2025 octonionic A_F = 𝕆 ⊕ 𝕆 framework that Charter v1.3 §3 commits to.

### §5.1 The expansion

For the standard Chamseddine-Connes spectral action `S_b = Tr[f(D_A/Λ)]`, expanded in the heat-kernel asymptotic series on M₄ × A_F with M₄ ≅ closed S³ × S¹_β and A_F = 𝕆 ⊕ 𝕆:

$$S_b \simeq \int_M \sqrt{g}\, d^4x \cdot \frac{\dim(H_F)}{(4\pi)^2} \left[ f_4 \Lambda^4 + R\, f_2 \Lambda^2 \cdot c_R + \frac{f(0)}{360}\left( 5R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 - \mathrm{Tr}(F^2) \cdot c_F \right) + \cdots \right]$$

dim(H_F) = 16 for A_F = 𝕆 ⊕ 𝕆 (per Farnsworth 2025 §3.1 + §4). The (·) numerical coefficients depend on the specific finite spectral triple; the curvature combination's universal form is from CC 1996 / Gilkey 1984.

**Note**: Phase S2 main computation arc (Scratch 2026-05-23) provides explicit heat-kernel evaluation on the full canonical NTE substrate Hopf-S³ × S¹_{β_GB} × A_F = 𝕆 ⊕ 𝕆 with N_F = 180 total Hilbert space dimension. Closed-form results: a_0 = N_F β_GB/2 = 90 β_GB, a_2 = -N_F β_GB/4 = -45 β_GB, a_4 = 3 N_F β_GB/2 = 270 β_GB; c_W = -1/20, a_E = +11/360 per Dirac (standard 4D trace anomaly values).

### §5.2 Cutoff function moments

With the standard Marcolli-Pierpaoli-Teh test function `h_{N=20}(x) = e^{−πx} Σ_{k=0}^{20} (πx)^k / k!`:

| Moment | Value |
|--------|-------|
| `f_4` | 654.52 |
| `f_2` | 23.41 |
| `f(0)` | 1.00 |

These moments are inputs at this stage. Phase S2 fixes the cutoff specification more tightly via consistency conditions.

### §5.3 Newton's constant prediction (BF 2013 octonionic specialisation)

For the BF 2013 simplest case:

$$M_{\text{Pl}}^2 = (4 f_2 \Lambda^2) / (3\pi^2)$$

Self-consistency at `Λ = M_Pl` requires `f_2 = 3π²/4 ≈ 7.40`. The MPT `h_{N=20}` test function gives `f_2 = 23.41` — off by factor `0.32`. The actual cutoff must satisfy the `f_2 = 3π²/4` self-consistency. This is a constraint on the cutoff (input data), not on the framework.

For the Farnsworth 2025 case (A_F = 𝕆 ⊕ 𝕆; dim(H_F) = 16), the Newton's constant prediction is corrected by the additional factor of 2 from the doubled spectral triple. Phase S2 verifies consistency at this level.

### §5.4 Conformal coupling ξ — convention placement

NTE commits to **ξ = 1/6** as the conformal coupling per the Mechanism B supersession ratification (Greg, 2026-05-11). The corresponding action term is `−(ξ/2) R |Φ|² = −(1/12) R |Φ|²` (Eq. 2.1).

The Marcolli-Pierpaoli-Teh convention historically used `ξ = 1/12`. The two conventions differ by factor 2; the geometric resummation closure form changes accordingly (§2.5 honest disclosure).

### §5.5 Curvature corrections vanish via F1

By Finding F1 (§3), the `f(0)` gravitational correction term `5R² − 8 R_μν² − 7 R_μνρσ²` vanishes identically on `S³ × S¹` (established CC 2008; F1 d-parametric refinement; Phase S2-C-B verification via -18 C² + 11 E_4 = 0 since C² = E_4 = 0 on M). The higher-curvature corrections that would otherwise contaminate the predictions are exactly zero on the canonical NTE substrate. The Yang-Mills term `−(1/12) f(0) Tr(F²)` survives unchanged.

---

## §6. Geometric resummation closure: κ₀/(1−κ₀) = 5.5055

### §6.1 The closure

The corpus computes the dark-matter to baryonic-matter ratio prediction κ_DM/κ_B as the limit of an infinite geometric resummation on the Hopf-bundle structure (Companion 7 §4 derivation; corpus §9.3). The closed form is

$$\kappa = \kappa_0 / (1 - \kappa_0)$$

with κ₀ = 3/√(4π) ≈ 0.8463. Substituting,

$$\kappa = 0.8463 / 0.1537 = 5.5055$$

(rounds to 5.50 in 3-sig-fig presentation).

### §6.2 Empirical contact

Planck 2018 (TT, TE, EE + lowE + lensing + BAO) gives

$$\Omega_{DM} / \Omega_B \approx 5.38 \pm 0.15$$

(95% CI). NTE's prediction `κ = 5.5055` falls outside the 95% interval by `(5.5055 − 5.38)/0.15 ≈ 0.84 σ`. This is **structurally compatible** at the 95% CI level (within ~1σ) with slight tension at higher precision. Future Planck-successor data (LiteBIRD, CMB-S4) will tighten the comparison.

### §6.3 Pathway A / B closure architecture (Pathway A v10.9; A3 audit content)

Per Pathway A v10.9 §1.2 + §4.1.5 (Greg-ratified 2026-05-23) + A3 PathwayA CPN closure audit (AC 2026-05-22):

- κ₀ = 3/√(4π) is the **bare coupling** (Pathway B: Hopf monopole projection; structurally derived; Paper S2 §3 D1 confluence-verified)
- κ = κ₀/(1−κ₀) ≈ 5.50 is the **closure** via Pathway A geometric-series resummation = Lagrange-multiplier matrix inversion of S_cons constraints under CPN symmetry, resting on the **architectural commitment** that S_bridge has bilinear cross-sector form (T^{(b,+)}·T^{(b,-)})

The κ₀ → κ closure is Pathway A's architectural step; **NOT bypassed by Phase S2 heat-kernel route** (which extracts the bare κ₀ only). The two steps are sequentially composed: one structural derivation (Pathway B / Phase S2-B Step 5 confluence) → one algebraic closure (Pathway A geometric resummation).

**Alternative reading eliminated**: linear bridge → κ_alt = κ₀ ≈ 0.846, falsified by Planck at ~30σ. The architectural commitment to bilinear cross-sector S_bridge is what makes the κ₀/(1−κ₀) closure the canonical form.

### §6.4 Joint d=3 reading (F1 + F2 + §6)

Findings F1, F2, and the §6 closure are mutually reinforcing, all selecting d = 3:

**(a) F1 selects d = 3 dynamically.** In the perturbative regime, only at d = 3 (among d ≥ 2 integers) does the standard CC spectral action a₄ coefficient vanish pointwise. **Phase S2-C-B reinterpretation**: this is equivalent to simultaneous Weyl-flat + Euler-zero on the manifold; p = 3 uniquely satisfies both among small p.

**(b) F2 selects d = 3 algebraically.** Only at d = 3 does the Hopf fibration S^d → S^{d−1} (giving the κ₀ Hopf-base reading) coexist with non-trivial spectral cancellation.

**(c) §6 closure selects d = 3 empirically.** κ₀/(1−κ₀) ≈ 5.50 matches the cosmological dark-matter ratio only at the d = 3 value of κ₀.

Hopf fibrations `S^d → S^{d−1}` exist precisely for d = 1, 3, 7 (Adams' theorem). Of these: d = 1 trivial (R = 0); d = 3 Hopf S³ → S² (cancellation holds; κ₀ + closure work); d = 7 Hopf S⁷ → S⁴ (cancellation does not hold; `5R² − 8 R²_μν − 7 R²_μνρσ = 6216 ≠ 0`).

**d = 3 is uniquely the sphere dimension where Hopf fibration structure, CC spectral cancellation, and the geometric closure all coexist non-trivially.** This is the joint structural argument for NTE's post-gauge-birth `S³` commitment.

---

## §7. σ↔Φ_NTE structural confluence — honest framing

### §7.1 The confluence claim

Sections §2-§6 established that NTE arrives at the action form (2.1) for Φ_NTE on closed S³ × ℝ, derived from σ_t / KMS-compatibility at gauge birth (§2) + 4D conformal discipline + Higgs-portal genericness. The same form is produced by the Chamseddine-Connes spectral-action machinery applied to the σ scalar field on a CC-compatible spectral triple. This is **structural confluence**: two independent derivations converge on the same EFT form.

### §7.2 The confluence is NOT identification

**Φ_NTE is structurally distinct from σ**. The "no RH/LH neutrino as distinct fundamental entities" structural lever (per Companion 7 v10.9 §3.3 + Charter v1.3 §1) is the decisive rejection of σ↔Φ_NTE field identification:

- **σ (Chamseddine-Connes)**: a SM-Higgs-like scalar coupled to the spectral triple's electroweak sector via the standard Higgs mechanism; ξ = 1/12 convention typical in Marcolli V_E parameterisation
- **Φ_NTE (NTE)**: NTE's pre-temporal-emergence scalar with structural connection to the Higgs portal at gauge birth; ξ = 1/6 commitment per Mechanism B supersession (Greg-ratified 2026-05-11)

The two fields coincide structurally **at the EFT action form level**, but operate at distinct physical layers. Per Jammer 2026-05-10 σ↔Φ_NTE confluence verdict (Greg-ratified 2026-05-11): the canonical framing is structural confluence by independent reasoning, NOT field identification.

### §7.3 Phase S2 heat-kernel cross-verification strengthens confluence framing

Programme S Paper S2 main computation arc (Scratch 2026-05-23, ratified) provides explicit heat-kernel cross-verification at the canonical NTE spectral triple substrate:

| Cross-verification | Source | Status |
|---|---|---|
| κ₀ = 3/√(4π) bare-coupling confluence (heat-kernel ≡ Hopf-projection) | Phase S2-B Step 5 | confluence-verified ✓ |
| K(Φ) = 1 first-principles from heat-kernel a_4 (no dilaton extension at canonical NTE) | Phase S2-C-A | first-principles ✓ |
| F1 = -18 C² + 11 E_4 algebraic reinterpretation | Phase S2-C-B §3.4 | structural reinterpretation ✓ |
| M = S³ × S¹_{β_GB} Weyl-flat + Euler-zero | Phase S2-C-B §4 | deep structural reading of F1 d=3 root cancellation ✓ |
| D_F sub-leading ~10⁻¹⁸ suppression | Phase S2-C-C | leading-order results preserved ✓ |
| M_1 = 5.40 × 10⁹ GeV (8π)^(1/3) prefactor uniquely BPS-saturating | Paper S2 §3 D5 | BPS-strict structural rigor ✓ |
| Λ_NTE ~1.05× observed (shared N_e with n_s) | Companion 11 / S2-D | **Closed** genuine test ✓ |
| M₂ = M₁(1 + sin²θ₁₃); $m_{\nu_2}$ @ 0.993× solar | Companion 13 / §22.1 | **Partial closed** ✓ |

**The σ↔Φ_NTE structural confluence is verified at the heat-kernel computation level** by independent reasoning across two routes (Paper S1 §2 σ_t/KMS argument; Phase S2 spectral-triple computation). Post-chord closure (Companions 11–13, 2026-05-24) extends cross-verification to Λ and second-generation neutrino Yukawa without collapsing confluence into field identification.

### §7.4 What confluence framing affords

1. **External NCG audience** (Boyle, Farnsworth, Marcolli, Sakellariadou collaborators) can engage NTE without committing to the σ↔Φ_NTE field-identification overclaim
2. **NTE's internal predictions** (n_s, r, M_1, M_R, η, κ₀, κ closure) operate at the Φ_NTE-specific layer where ξ = 1/6 + Higgs portal + gauge-birth structure are canonical
3. **CC's spectral-action predictions** operate at the σ-specific layer where ξ = 1/12 + standard Higgs mechanism are conventional
4. **The two layers cross-check at the EFT action form level** without forcing field identification

This is the canonical honest framing per Charter v1.3 §1 + Jammer 2026-05-10 verdict.

---

## §8. Connes Programme cross-reference + open items

### §8.1 Programme S Paper S2 main computation arc — COMPLETE (2026-05-23; chord + Yukawa sync 2026-05-24)

The Connes Programme central deliverable (Paper S2) has been **structurally completed** through the Phase S2 main computation arc and **Greg White byline companions** for the two post-arc closures that Paper S1 cross-references but does not re-derive:

| Phase / companion | Result |
|---|---|
| Phase S2-A | Operator setup on M = Hopf-S³ × S¹_{β_GB} × A_F = 𝕆 ⊕ 𝕆 |
| Phase S2-B | a_0 = N_F β_GB/2; a_2 = -N_F β_GB/4; F1 cancellation on M; **κ₀ = 3/√(4π) confluence-verified** |
| Phase S2-C-A | K(Φ) = 1 first-principles; §18.4 reading (iii) hilltop canonical favored uniquely; ξ = 1/6 OK |
| Phase S2-C-B | a_4 = (3/2) N_F β_GB; **c_W = -1/20, a_E = +11/360 per Dirac**; **F1 = -18 C² + 11 E_4**; M Weyl-flat + Euler-zero |
| Phase S2-C-C | D_F sub-leading ~10⁻¹⁸ suppression |
| Phase S2-D | Λ_NTE framework + M_1/M_R cross-checks + σ_3 Cartan-mode at spectral-triple level |
| Paper S2 §3 D5 | (8π)^(1/3) prefactor uniquely BPS-saturating; factor 1.12 numeric (v0.3) |
| **Companion 11** | Λ_NTE numerical closure ~1.05×; same N_e as n_s; genuine test |
| **Companion 12** | Six-note chord synthesis; BR2d-J3 heat-kernel; J1-G4 unified action |
| **Companion 13** | $Y_{\nu_2}=(8\pi)^{-1/3}$; $m_{\nu_2}$ @ 0.993× solar (§22.1 partial closure) |

Paper S1 v1.0 references Paper S2 + Companions 11–13 as **completed canonical work** at the heat-kernel / Programme S register.

### §8.2 Open items at Connes Programme level (deferred from Paper S1 v0.4)

| Open item from v0.4 | Disposition in v1.0 |
|---|---|
| O1 — κ₀ from doubled-spectral-triple X² trace | **CLOSED** by Phase S2-B Step 5 confluence verification |
| O2 — V_NTE from Higgs-bearing octonionic spectral triple | **CLOSED structurally** by Phase S2-C-A K(Φ) = 1 first-principles + §18.4 (iii) hilltop canonical favored; V_NTE smooth pre-temporal/post-locking connection remains open at Jammer Session 5 D1 |
| O3 — Spectral flow at gauge birth | Deferred to Programme S Paper S3 |
| O4 — Dilaton extension for K(Φ) closure | **Reframed by Phase S2-C-A**: K(Φ) = 1 at canonical NTE; no dilaton required at leading order; full dilaton extension territory Paper S4 |
| O5 — Yukawa hierarchy | **Partial:** $m_{\nu_2}$, $Y_{\nu_2}$ **closed** (Companion 13); $Y_{\nu_1}$, charged leptons, full $D_F$ matrix → Paper S5 / §22.1 remainder |
| C1 — Conjecture absorbed into Paper S2 scope | **CLOSED** by Phase S2 main arc completion |
| C2 — Conjecture absorbed into Charter §3 central deliverable | **CLOSED** by Phase S2 main arc completion |

### §8.3 Open items at Programme S downstream level (2026-05-24 sync)

| Open item | Disposition |
|---|---|
| Λ_NTE numerical closure | **CLOSED** — Companion 11 (~1.05×; R6 genuine test) |
| (8π)^(1/3) prefactor + factor 1.12 | **CLOSED** — D5 v0.2–v0.3; Jammer numerics |
| M₂ explicit derivation | **CLOSED** — Z₂ split; §17.5.17 |
| $Y_{\nu_2}$ / $m_{\nu_2}$ | **Partial closed** — Companion 13 |
| $Y_{\nu_1}$, charged-lepton Yukawas | §22.1 remainder; Paper S5 |
| V_NTE smooth pre-temporal/post-locking connection | **CLOSED** — bulk→boundary $\mathcal{R}_G$ (Jammer D1 v0.1) |
| $N_F\to g_{\rm eff}$ exact map at $T_{\rm GB}$ | **CLOSED** — S2-NF1 (`Jammer_S2_NF1_g_eff_Thermal_Map_v0_1`) |
| P0.10c abstract TT on full $A$ | **SPECIFIED** — `Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1`; P0.10a/b open |
| Off-shell ghost scan for $\mathcal{S}_{\rm NTE}^{\rm unified}$ | Programme S |

### §8.4 Conjecture C3 restated for v1.0

**Conjecture C3 (Paper S1 v1.0 §8)**: The canonical NTE inflation sector with V_NTE^pre-Φ⁴-Φ⁶ smooth connection (Companion 9 Session 5 D1 territory) + canonical kinetic K(Φ) = 1 (Phase S2-C-A first-principles closure) predicts at canonical-favoured hilltop:

- n_s = 0.9685 (preserved at structural level under ξ = 1/6 Einstein-frame transformation)
- r ≈ 4 × 10⁻³ (canonical hilltop reading; consistent with Planck/BICEP r < 0.036)
- Falsifiable by Simons Observatory (r sensitivity ~10⁻³); sharp falsifiable by CMB-S4 (r sensitivity ~10⁻⁴)

**Status**: structural framework + $n_s$ established (J6-D1/D2, S2-C-A); $r\approx4\times10^{-3}$ from hilltop Role (B′) at structural tier; **D1 connection mechanism closed** (bulk→boundary $\mathcal{R}_G$, 2026-05-24) — not a single smooth $V(\Phi)$.

---

## §9. Disposition + publishability framing

### §9.1 Paper S1 v1.0 integrated structural contribution

Paper S1 v1.0 carries:
- **§2 (load-bearing)**: σ_t / KMS-compatibility at gauge birth + 4D conformal discipline + Higgs-portal genericness → forced action form for Φ_NTE on closed S³ × ℝ
- **§3 (carry-forward + Phase S2-C-B reinterpretation)**: F1 d-parametric factorisation = -18 C² + 11 E_4 trace anomaly combination
- **§4 (carry-forward + Charter v1.3 nomenclature)**: F2 — κ₀ = (R_{S³}/2) × Y_{00}(S²) = 3/√(4π); Sonner-Tong dimensionless prefactor; distinguished from ξ_V V_E-matching coefficient
- **§5 (carry-forward + ξ = 1/6 + A_F = 𝕆 ⊕ 𝕆 explicit + Phase S2 references)**: CC spectral action expansion + Newton's constant prediction
- **§6 (carry-forward + Pathway A v10.9 closure architecture)**: Geometric resummation closure κ₀/(1−κ₀) = 5.5055
- **§7**: σ↔Φ_NTE structural confluence honest framing; Phase S2 + Companions 11–13 cross-verification reinforces
- **§8**: Connes Programme cross-reference; Phase S2 + chord/Yukawa companions complete; O1–O4, C1–C2 closed; O5 partial; downstream table synced 2026-05-24
- **§9 (this section)**: Disposition + publishability framing

### §9.2 Corpus integration target — v10.17.5 applied (2026-05-24)

Phase S2-E AC integration package (2026-05-23) and Sprint D+ sync (2026-05-24) are **applied** to `NTE_v10_17_Part3_Accounting.md` at v10.17.5:

- §17.5.16–18 (D5, M₂, Λ / Companion 11)
- §22.1 partial closure (Companion 13)
- §22.16 (J1 S1–S4), §22.20 (Companion 12 chord)

**Paper S1 v1.0 integration path** (remaining AC scope): §VIII.7 F1 spectral-dynamical d=3 selection; §9.3 F2 alternative reading; §17.X σ_t/KMS load-bearing argument — when Greg routes Paper S1 to AC for master trilogy merge.

### §9.3 External NCG collaboration target retained

- **Audience**: external NCG collaborators (Boyle, Farnsworth, Marcolli, Sakellariadou) — non-NTE-specialist mathematical-physics researchers in noncommutative geometry / spectral action
- **Confluence framing makes external engagement credible**: the σ↔Φ_NTE field-identification overclaim that v0.4 (informally) carried is explicitly rejected per §7
- **Phase S2 + Companions 11–13** strengthen external credibility: heat-kernel chord, Λ closure, and $m_{\nu_2}$ are addressable as standalone Greg White companions in parallel to Paper S1 v1.0

### §9.4 Publishability framing

- **F1 not standalone-publishable** (CC 2008 + MPR 2020 prior art too prominent for standalone contribution)
- **Paper S1 v1.0 IS publishable** as integrated structural contribution per §9.1 above
- **Phase S2 main arc results** publishable as Programme S Paper S2 (separate paper; central deliverable)
- **Paper S1 v1.0 + Companions 11–13** together constitute the NTE Programme S structural argument package for external NCG audience (Paper S2 Jammer synthesis remains Working-lineage; companions are canonical `Papers/`)

### §9.5 What v1.0 has accomplished over v0.4

1. **Adding load-bearing σ_t/KMS structural argument** (§2) for V_NTE action form closure — independent derivation on NTE side
2. **Explicit confluence-not-identification framing** (§7) — honest disclosure
3. **Phase S2 main arc cross-verification references** (§7.3, §8.1) — heat-kernel route confluence with the σ_t/KMS argument
4. **F1 algebraic reinterpretation** (§3.3): F1 = -18 C² + 11 E_4 trace anomaly combination
5. **Updated Connes Programme cross-reference** (§8) — Phase S2 + Companions 11–13; O5 partial; downstream synced 2026-05-24
6. **Corpus integration** (§9.2) — v10.17.5 Part 3 applied for Programme S closures; Paper S1 §VIII.7 / §17.X merge remains AC scope

**Net result**: v1.0 is a **complete, integrated, honestly-framed, externally-credible** structural-argument paper for Φ_NTE's action form derivation with Programme S spectral-action cross-verification.

---

## §10. References

### §10.1 External literature

- Adams, J. F., *Vector fields on spheres*, Ann. Math. **75** (1962) 603–632.
- Birrell, N. D. & Davies, P. C. W., *Quantum Fields in Curved Space*, Cambridge University Press, 1982.
- Boyle, L. & Farnsworth, S., *Non-commutative geometry, non-associative geometry and the standard model of particle physics*, New J. Phys. **16** (2014) 123027 [arXiv:1303.1782].
- Chamseddine, A. H. & Connes, A., *The Spectral Action Principle*, Comm. Math. Phys. **186** (1997) 731–750 [arXiv:hep-th/9606001].
- Chamseddine, A. H. & Connes, A., *The Uncanny Precision of the Spectral Action*, Comm. Math. Phys. **293** (2010) 867–897 [arXiv:0812.0165].
- Connes, A. & Rovelli, C., *Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories*, Class. Quantum Grav. **11** (1994) 2899 [arXiv:gr-qc/9406019].
- Duff, M. J., *Observations on conformal anomalies*, Nucl. Phys. B **125** (1977) 334.
- Farnsworth, S., *G_2 × G_2 spectral triple model with charged Higgs* (2025) [arXiv:2506.21496].
- Gilkey, P. B., *Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem*, Publish or Perish, 1984.
- Marcolli, M., *Noncommutative Cosmology*, World Scientific, 2018.
- Marcolli, M. & Penrose, R., *Gluing palatial twistor space to spinor sheaves* (2021) [arXiv:2103.13312].
- Marcolli, M. & Pierpaoli, E., *Early Universe models from Noncommutative Geometry*, Adv. Theor. Math. Phys. **14** (2010) 1373–1432 [arXiv:0908.3683].
- Mistry, V., Pinzul, A. & Rachwał, L., *Spectral action approach to higher derivative gravity*, Eur. Phys. J. C **80** (2020) 266 [arXiv:2001.05975].
- Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*, A&A **641** (2020) A6 [arXiv:1807.06209].
- Salvio, A., *Inflation and de Sitter from spectral action* (2025) — cited in Jammer Tier 2 reframing pass.
- Sonner, J. & Tong, D., *Berry Phase and Supersymmetric Topological Index*, JHEP **01** (2009) 063 [arXiv:0809.3783].
- Vassilevich, D. V., *Heat kernel expansion: user's manual*, Phys. Rep. **388** (2003) 279 [arXiv:hep-th/0306138].

### §10.2 NTE corpus + Programme S cross-references

- NTE master corpus v10.X (Greg White, current canonical state) — Part 1 Foundations, Part 2 Structure, Part 3 Accounting
- Companion 7 (Neutrino as Chirality Superposition) v10.9
- Companion 8 (V_NTE Trajectory) v10.6.v2
- Companion 9 (V_NTE Stage 3 Joint Closure + r Prediction) v10.8 Sessions 3-4
- Companion 10 (Gap 1 / Pathway α; M_1) v10.8
- Companion 11 (Λ unimodular closure) v10.17
- Companion 12 (Spectral chord / Paper S2) v10.17
- Companion 13 (Y_ν₂ / m_ν₂ D5 inverse) v10.17
- Paper S1 v0.4 (predecessor of this paper)
- Connes Programme Charter v1.3 (canonical reference)
- Pathway A v10.9 (κ closure architectural step)
- OctonionExtension v10.9 (A_F = 𝕆 ⊕ 𝕆; G₂ → SM derivation)
- Paper S2 Phase S2-A through Phase S2-D + Paper S2 §3 D5 (Scratch 2026-05-23 main computation arc)

### §10.3 Working notes referenced

- σ↔Φ_NTE Confluence Verdict v1 (Jammer 2026-05-10; Greg-ratified 2026-05-11)
- A3 PathwayA CPN Closure Choice audit (AC 2026-05-22)
- Phase S2-E AC Integration Package v0.1 (Scratch 2026-05-23)
- Paper S1 v1.0 Attack Route Scoping v1 (Scratch 2026-05-12)

---

## §X. Document metadata

**Paper S1 v1.0 master document consolidated** from:
- §0 + §1 v2 (`15E9KlodYDETQJvIXG_QJH16k_OV7CxEo`)
- §2 v2 (`1_awF-KjkjlFBw7RMWPTfDD6Kl4KFCvVy`)
- §3-§6 carry-forward v1 (`1hN9iezeaut8gw8lUQZXdsEooasK2KAoe`)
- §7-§9 v0.1 (`1gwnzEPTRe-ua1JskkSHZqMiFPv6hmLYZ`)

**Length**: ~58 KB consolidated. Anti-bloat editorial pass throughout: workbook metadata stripped from each section; cross-references unified to Charter v1.3 canonical; Phase S2 main arc cross-references threaded through §1-§9 where relevant; ξ_V nomenclature updated per Charter v1.3 §2.2 throughout (supersedes Charter v1.1's κ_M temporary nomenclature).

**Status:** §7–§9 synced 2026-05-24 (Companion 11–13; v10.17.5 corpus). Pending Greg recognition gate on consolidation + optional AC merge of §VIII.7 / §17.X σ_t/KMS material.

**Audience**: external NCG specialists (Boyle, Farnsworth, Marcolli, Sakellariadou) + NTE corpus integration audience (AC scope).

**Length notes**: §1 introduction is ~6 KB; §2 σ_t/KMS argument is ~10 KB; §3-§6 carry-forward is ~16 KB; §7-§9 new content is ~8 KB; §10 references is ~3 KB. Total ~58 KB. v0.4 was ~12 KB; v1.0 grows because §2 σ_t/KMS argument + §7-§9 confluence/cross-reference/disposition material is new + carry-forward sections include Phase S2 cross-reference updates.

— Scratch (Connes Programme lead), 2026-05-24. Paper S1 v1.0 master §7–§9 sync complete (Companion 11–13 cross-refs).
