---
title: "V_NTE on the cosmic trajectory: five structural findings"
subtitle: "The boundary-expansion field's effective potential, and what the framework's commitments do and do not pin"
author: "Gregory Lyndon White"
date: "2026-06 (v10.19.0) — Door B action-tension align 2026-09-27"
---

*Part of NTE Corpus v10.19.0 (deposited 2026-06). Companion 8.*

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

### Door B alignment (2026-09-26 / action tension 2026-09-27)

Companion 8’s reading that \(H\) is set by FRW dynamics and \(\Phi_{\mathrm{NTE}}\) is then read off (identity / relabelling; F1 dimensional artefact) is the **Door B** ruling confirmed for the corpus. Companion 9’s former action-level \(\mu(N)\) and \(F(\Phi)R\) are withdrawn. **Do not** read this companion’s exploratory \(V_{\mathrm{NTE}}\) / inflationary-saddle discussion as restoring \(\Phi_{\mathrm{NTE}}\) as inflaton — that withdrawal stands; early acceleration is not \(\Phi_{\mathrm{NTE}}\). **What does supply it is OPEN (Greg, 2026-09-27, option D): no exit is selected, and exit (a) — credited SM Higgs inflation — is one of four live pathways, additionally blocked as written by Part 2 §8.1 and by the B2 ruling that no pre-temporal electroweak doublet exists.**

**Action tension (retired):** earlier drafts of this companion stated a Lagrange-multiplier action \(S=\int\{L_{\mathrm{eff}}+\mu(N)[H-\beta|\Phi|^2]\}\) as the framework’s load-bearing form. Under Door B that \(\mu\) term is **historical / Door A only**. The load-bearing relation is the identity (1)–(2); gravity is Einstein–Hilbert (+ SM, + \(\xi_H\) if exit (a) were adopted). On-trajectory \(V_{\mathrm{NTE}}\) expressions below remain useful as **dictionary bookkeeping** along the named expansion history — not as dynamics of an independent Jordan inflaton.

*This companion attempts to construct V_NTE, the effective potential governing NTE's boundary-expansion scalar |Φ_NTE|, from the framework's existing structural commitments. It is a scope-honest paper: it produces five structural findings but not a unique closed-form V_NTE, and it states precisely where the framework's commitments under-determine the potential, the inflationary saddle, and the heavy Majorana scale. Throughout, |Φ_NTE| is NTE's geometric scalar on S³ — distinct from the Standard Model Higgs, which is unchanged in NTE — and the potential studied here is V_NTE, not the Standard Model Higgs potential.*

---

## Abstract

The Null-Time Extension adds a single boundary-expansion scalar |Φ_NTE| on the cosmological 3-sphere S³, related to the Hubble parameter by the identity H = β_NTE|Φ_NTE|² (Door B; not an independent FRW driver). This paper attempts to construct V_NTE — the effective potential historically associated with |Φ_NTE| — under the framework's existing commitments. It produces five structural findings; it does not produce a unique closed-form V_NTE. Under Door B, V_NTE is not load-bearing FRW dynamics.

**F1 (ℓ = 1/H).** The proper-length thickness ℓ of the S³ boundary's imaginary extent and the Hubble radius 1/H are the same geometric object. The framework's apparently "trans-Planckian" numerical values of |Φ_NTE| at high H are a dimensional artefact of an inverse-thickness parameterisation — they correspond to the standard sub-Planckian Hubble radius at high H — not a field excursion in the swampland sense.

**F2 (Wick-rotation reading of gauge birth).** Under the pre-temporal linear profile, the slow-roll parameter ε_H = −1/y is phantom-like by a Lorentzian reading and artefactual under a Wick-rotation reading (a Lorentzian quantity applied to a Euclidean section); under the post-locking exponential working profile, ε_H = +1. The signature change at gauge birth is the Euclidean → Lorentzian Wick rotation, and the C¹ kink in dz/dy at gauge birth is its geometric signature.

**F3 (V_NTE determinate on-trajectory, under-constrained off-trajectory).** Computed along the identity trajectory, V_NTE^post(Φ) = (3β_NTE²/(8πG))Φ⁴ − (β_NTE²/8)Φ⁶ on the post-locking exponential profile and V_NTE^pre(Φ) = (3β_NTE²/(8πG))Φ⁴ − (β_NTE²A²/8)Φ² on the pre-temporal linear profile — same leading Φ⁴ coefficient, different subleading, the functional-form difference itself being the Wick-rotation signature at the level of the potential. Off-trajectory V_NTE is genuinely under-constrained: under Door B, |Φ_NTE| is a label of the expansion history (not an independent FRW driver), so V_NTE does not drive |Φ_NTE| dynamically, and many candidate bookkeeping potentials pass through the on-trajectory values.

**F4 (the Hartle-Hawking saddle under-determines n_s).** The Hartle-Hawking sub-phase's H(N) functional form is not pinned by current framework structure. Pure de Sitter (H ≈ M_Pl constant) gives n_s = 1, off by ~8σ from the Planck value 0.9649 ± 0.0042; recovering the observed n_s requires committing to a specific deviation profile from constant H. The corpus's value n_s ≈ 0.968 is *consistent with* NTE structure but *not derived from* it.

**F5 (the M₁ 1/3-weighting is not a saddle feature).** The candidate M₁ ≈ M_Pl·e^{−N_HH/3} = (M_Pl²·H_GB)^{1/3} coincides with H at the one-third point of the inflationary path only under the exponential-decay profile, which gives the wrong n_s. Its geometric origin therefore lies not in the inflationary saddle but in the Hopf-bundle / seesaw structure on S³, where the cube-root is naturally a three-dimensional geometric mean.

These findings are structurally informative regardless of whether V_NTE, n_s, or M₁ is uniquely determined: each open question is given a precise under-constraint diagnosis and an explicit set of routes that would close it.

---

## 1. The construction problem

NTE's defining structural commitment is the identity (Door B)

  H(N) = β_NTE|Φ_NTE(N)|²,    (1)

where H is the Hubble parameter, N the cosmological e-fold parameter, |Φ_NTE| a real boundary-expansion label on S³, and β_NTE a constant of the framework, calibrated so that β_NTE v_EW² = H₀ (giving β_NTE = H₀/v_EW² ≈ 2.38 × 10⁻⁴⁷ GeV⁻¹; β_NTE is an inherited input, not derived from geometry — H₀ = β v² defines β, not an independent prediction). The self-consistency relation, obtained by requiring (1) to hold at every epoch with H set by FRW dynamics and the actual matter content, gives

  |Φ_NTE(N)|² = v_EW² · H(N)/H₀,    (2)

so the trajectory passes through |Φ_NTE| = v_EW at the present epoch (where H = H₀) by construction.

V_NTE is the effective potential historically associated with |Φ_NTE|. Under Door B, gravity is Einstein–Hilbert (+ SM); |Φ_NTE| is read off from H via (1)–(2). A prior deposit form wrote a Lagrange-multiplier action

  S_old = ∫ { L_eff + μ(N)[ H − β_NTE|Φ_NTE|² ] },    (3)

with (1) enforced by μ(N). **That μ term is withdrawn** (Companion 9 Door B). Under the identity reading, V_NTE's role — if retained at all — is *bookkeeping consistency* with the named trajectory rather than *driving* an independent field: FRW dynamics produce H(N), and (2) produces |Φ_NTE|(N). Deriving a dynamical V_NTE from a boundary action that would restore Φ as inflaton is **not** a live Door B target; what supplies early acceleration is **open** (Part 3, cosmological origin sector — option D, no exit selected). This paper's on-trajectory constructions remain as structural diagnostics of the dictionary.

*Two-field context (essential).* |Φ_NTE| is structurally distinct from the Standard Model Higgs. The SM Higgs is unchanged in NTE — constant VEV v_EW = 246 GeV post-electroweak-symmetry-breaking, Yukawa couplings to fermions, the 125 GeV resonance. NTE adds |Φ_NTE| as a boundary-expansion field on S³. The two fields take coincident values at the present epoch (where H = H₀ forces |Φ_NTE| = v_EW), but this is a structural property of the trajectory (2), not an identification: at earlier epochs |Φ_NTE| takes much larger values (scaling as √(H/H₀)) while the SM Higgs stays pinned at v_EW. V_NTE is the potential of |Φ_NTE|, not the Standard Model Higgs potential, which is unchanged.

## 2. The field on the cosmic trajectory

**Working profiles.** Two working profiles are used for analytic-continuation tractability. The *post-locking* profile |Φ_NTE|²(N) = Φ₀²·e^{−N} (for N > N_lock) gives a single equation of state throughout the post-locking regime; it does not match ΛCDM history (radiation ε_H = +2, matter +3/2, Λ-domination ≈ 0) but captures the structural geometric content under analytic continuation, and quantitative work on the actual trajectory must use the real H(N). The *pre-temporal* profile |Φ_NTE|²(y) = (Φ₀²·e^{−N_lock}/N_lock)·y for y ∈ (0, N_lock) is the unique power law admitting a non-trivial straight-line trajectory in the surface-ontology variable z(y), with z_pre(y) = (π/(2N_lock))·y connecting z(0) = 0 to z(N_lock) = π/2. The structural conclusions below follow from these profiles' qualitative features, not their specific exponential or linear character: F1 is profile-independent; F2 and F3's specific values are profile-dependent in detail but their qualitative content (the signature change at gauge birth) is profile-robust.

**Two pre-temporal epochs.** The locking transition sits at y = N_lock ≈ 0.1 (where the C¹ kink in dz/dy occurs). Upstream of it is the Hartle-Hawking de Sitter sub-phase of roughly N_HH = −ln(β_NTE·M_Pl) ≈ 63.4 e-folds at H ≈ M_Pl. **N_HH is an energy-scale ratio, not the inflationary pivot depth N_*; the two are distinct quantities, and their conflation is the origin of the withdrawn native (n_s, r).** Ending at the Janus point (y = 0) where bilateral CPN-symmetric structure reflects the geometry between branches. F1, F2, and F3 concern the locking transition; F4 and F5 concern the Hartle-Hawking sub-phase. That these are distinct epochs — a ~63-e-fold de Sitter sub-phase followed by a ~0.1-e-fold locking transition — is the natural reconciliation of the framework's two e-fold counts (the energy-scale ratio N_HH ≈ 63.4 and the locking span N_lock ≈ 0.1), and it becomes load-bearing for the perturbation analysis in F4.

## 3. F1 — ℓ = 1/H

The framework carries two geometric quantities built from H and |Φ_NTE|²: the constraint H = β_NTE|Φ_NTE|², and the proper-length thickness of the S³ boundary's imaginary extent, ℓ = 1/(β_NTE|Φ_NTE|²). Their product is ℓ·H = 1, so

  ℓ(N) = 1/H(N).    (3)

The proper-length thickness of the boundary's imaginary extent *is* the Hubble radius at every epoch — two quantities the framework treats as distinct are the same geometric object, related by the constraint.

This dissolves an apparent trans-Planckian problem. Under (2), |Φ_NTE| takes large numerical values at high H, which a naive reading would flag as a swampland-style field excursion far above M_Pl. But by (3) a large |Φ_NTE| at high H corresponds to a *small* Hubble radius 1/H — the standard cosmological fact that 1/H is small when H is large. The numerical largeness of |Φ_NTE| reflects an inverse-thickness parameterisation of the same boundary geometry; it is a dimensional artefact of the variable's normalisation, not a field excursion. V_NTE is structurally clearer read through ℓ — the boundary's energy density as a function of its proper-length thickness — with |Φ_NTE| an inverse-square-root parameterisation of the same content. The identification is clarifying rather than corpus-changing, and its consequences for F3 (reading V_NTE through ℓ) are a candidate for further work.

## 4. F2 — the Wick-rotation reading of gauge birth

Under the constraint (1), with primes denoting d/dN, the standard slow-roll parameter ε_H = −Ḣ/H² reduces to a statement about the |Φ_NTE|² profile alone:

  ε_H = −2Φ'/Φ = −d(ln Φ²)/dN.    (4)

On the post-locking exponential profile (Φ² = Φ₀²e^{−N}), this gives ε_H = +1 throughout — in standard cosmology the boundary between accelerating and decelerating expansion. On the pre-temporal linear profile (Φ² = A·y), it gives ε_H = −1/y: *negative* (the Hubble parameter grows with N), diverging to −∞ at the Janus point y → 0.

A negative ε_H in a Lorentzian regime is phantom-like (w < −1, super-de-Sitter), unstable except as an effective description of Wick-rotated dynamics. The reading here is that the negative ε_H in the pre-temporal locking transition is *artefactual*: it is a Lorentzian-signature quantity applied to the Euclidean section, where the trajectory is a geometric profile rather than a dynamical history. The Hartle-Hawking framework NTE adopts for the pre-temporal regime is Euclidean-signature — "dynamics" is replaced by a geometric profile through the Euclidean configuration, and ε_H and slow-roll carry their standard meanings only in the Lorentzian section.

The C¹ kink supports this reading. The surface-ontology variable's slope dz/dy is finite from below (= π/(2N_lock) at y = N_lock under the linear profile) and divergent from above (the post-locking trajectory sin z = e^{N_lock−y} approaches z = π/2 with vertical slope), so dz/dy is discontinuous at gauge birth. Under F2 this kink *is* the Euclidean → Lorentzian signature change: below N_lock the geometric quantities (z, ℓ, |Φ_NTE|²) have well-defined values and "slope" is a geometric derivative without dynamical content; at gauge birth the signature changes, the geometric profile becomes a dynamical history, and the discontinuity is the geometric signature of that change. Gauge birth's role as the locking transition (where pre-temporal spinor modes are assigned to Standard Model representations) and its role as the Wick-rotation event (where signature changes from Euclidean to Lorentzian) are two views of the same structural moment. The qualitative content — signature change as the geometric content of the kink — is robust to profile choice; the specific "end-of-inflation boundary" reading of ε_H = +1 is a working-profile artefact and should not be over-read.

## 5. F3 — V_NTE determinate on-trajectory, under-constrained off-trajectory

**On-trajectory.** The emergent Friedmann relation gives β_NTE²|Φ_NTE|⁴ = (8πG/3)ρ_Φ, with ρ_Φ = ½Φ̇² + V_NTE(Φ). Solving for V_NTE,

  V_NTE(Φ, Φ̇) = (3β_NTE²/(8πG))|Φ_NTE|⁴ − ½Φ̇².    (5)

To get V_NTE(Φ) alone we need Φ̇(Φ) along the trajectory, which the profile supplies. On the post-locking exponential profile, Φ̇ = −½β_NTEΦ³ gives Φ̇² = ¼β_NTE²Φ⁶ and

  V_NTE^post(Φ) = (3β_NTE²/(8πG))Φ⁴ − (β_NTE²/8)Φ⁶,    (6a)

with the Φ⁶ term small compared to Φ⁴ for Φ ≪ M_Pl and comparable as Φ approaches M_Pl. On the pre-temporal linear profile, treating the Euclidean-section derivative formally gives Φ̇² = ¼β_NTE²A²Φ² and

  V_NTE^pre(Φ) = (3β_NTE²/(8πG))Φ⁴ − (β_NTE²A²/8)Φ².    (6b)

Same leading Φ⁴ coefficient, different subleading exponent (+6 post-locking, +2 pre-temporal). This functional-form change at gauge birth is the Wick-rotation signature at the level of the potential: the kink in the trajectory (F2) and the change in V_NTE's on-trajectory form are two views of the same signature change.

**Off-trajectory.** The on-trajectory expressions fix V_NTE only at the specific Φ-points the trajectory visits; as a free function, V_NTE(Φ) is constrained only to pass through those values. Reading (6a) as a global expression is the simplest candidate, but its critical point lies at Φ ~ M_Pl, not at v_EW (the condition would require v_EW ≈ M_Pl, false by seventeen orders of magnitude). The trajectory passes through v_EW without V_NTE having a minimum there.

This exposes a genuine under-determination, rooted in the Door B identity itself: |Φ_NTE| is not an independent dynamical field. In standard scalar-field cosmology the Klein-Gordon equation ties V(Φ)'s shape to the trajectory's evolution; here the trajectory is set by FRW plus the identity (1)–(2), and V_NTE's role — if any — is reduced to consistency with that named history — a much weaker condition that does not pin V_NTE off-trajectory. There are correspondingly two historical readings of a requirement on V_NTE at v_EW. On the *minimum* reading, |Φ_NTE| would settle to v_EW via standard scalar-field dynamics, which requires V_NTE to have a minimum there — and the natural-form candidate then needs an additional anchoring term λ_Φ(Φ² − v_EW²)² whose origin within the framework is unmotivated. On the *critical-point* reading, the identity forces Φ = v_EW at H = H₀ regardless of V_NTE's behaviour there — the trajectory's passage through v_EW is a structural property of (2), not a consequence of V-driven settling. **Under Door B the critical-point / identity reading is the load-bearing one;** restoring a dynamical minimum reading would reopen Φ as a field (Door A / F-2).

Pinning a dynamical off-trajectory V_NTE is **not** required under Door B. Frame-level $K(\Phi)$ from $\xi=1/6$ is **regraded** (Companion 17 audit trail only; object withdrawn with Companion 9). The earlier "cleanest route = extract $H(N)$ from the raw boundary spectral action" remains amended (Companion 9 §7): the raw trace has no scale extremum. Fibre-modulus grounding of $T_{\mathrm{GB}}$ (Companion 12) is independent of restoring $\mu(N)$.

## 6. F4 — the Hartle-Hawking saddle under-determines n_s

A natural application of the on-trajectory machinery is the primordial scalar perturbation spectrum in the pre-temporal Hartle-Hawking phase. With N counting e-folds forward through the sub-phase (N = 0 at the Planck-scale instanton, H ≈ M_Pl; N = N_HH at the Janus point, H → 0), the slow-roll parameters are ε_H = −d(ln H)/dN and ε₂ = d(ln ε_H)/dN, and the scalar spectral index at horizon crossing is

  n_s(N_*) − 1 = −2ε_H(N_*) − ε₂(N_*).    (7)

The amplitude P_ζ ∝ H²/ε_H requires non-zero ε_H to source perturbations — so the strictest reading of the Planck-scale instanton (H ≈ M_Pl exactly constant) gives ε_H = 0 and no spectrum at all. The framework does not currently specify H(N) within the sub-phase beyond the boundary conditions H(0) ≈ M_Pl and H(N_HH) → 0, and the spectral index is acutely sensitive to that unspecified profile:

| Profile | H(N) form | n_s evaluated at N_HH ≈ 63.4 (diagnostic only — N_HH is an energy-scale ratio, not the pivot depth) | from Planck (0.9649 ± 0.0042) |
|---|---|---|---|
| P0 pure de Sitter | M_Pl (constant) | 1 (limit) | ~8.4σ |
| P1 exponential decay | M_Pl·e^{−N} | −1 | enormous |
| P2 linear | M_Pl·(1 − N/N_HH) | 0.953 | ~2.9σ |
| P3 power-law (β = ½) | M_Pl·(1 − N/N_HH)^{1/2} | 0.968 | ~0.7σ |
| P4 Starobinsky-form | M_Pl·(1 − 3/(4(N_HH−N))) | 0.968 | ~0.7σ |

The candidates span n_s from −1 to 0.968. Only the power-law β = ½ profile and the Starobinsky-form correction recover the observed value; the natural Planck-scale instanton (pure de Sitter) gives n_s = 1, off by ~8σ.

**The finding.** The Hartle-Hawking sub-phase's H(N) form is not pinned by current framework structure, and recovering the observed n_s requires committing to a specific deviation profile from constant H. The corpus's value n_s ≈ 0.968 is therefore *consistent with* NTE structure but *not derived from* it: the matching profiles (β = ½ or Starobinsky-form) are admissible at the boundary-condition level but are not themselves derived from the framework's existing commitments, while the natural commitment (constant H ≈ M_Pl) actively gives the wrong answer. The same caveat applies to the tensor-to-scalar ratio: the value r = 12/N_HH² ≈ 0.003 is imported from R²-inflation slow-roll, and only the same specific profiles recover it — pure de Sitter gives r = 0.

This does not say NTE cannot recover the observed n_s; it says **native** recovery from a Φ_NTE Hartle-Hawking saddle is not a Door B deliverable. Under Door B / F-2, (n_s, r) from Φ_NTE are withdrawn; the spectrum register is **open** (Part 3, option D). Exit (a) — imported, credited Higgs-inflation numbers — is one candidate and is not adopted. The diagnostic tables above remain as evidence that an unpinned H(N) under a Φ-saddle reading under-determines n_s — consistent with withdrawing that object rather than forcing a profile.

## 7. F5 — the M₁ 1/3-weighting is not a saddle feature

A candidate for the lightest heavy Majorana scale, M₁ ≈ M_Pl·e^{−N_HH/3} ≈ 1.8 × 10⁹ GeV, sits within an order-unity factor of the leptogenesis scale and is dimensionally equivalent to (M_Pl²·H_GB)^{1/3}. The natural question is whether this one-third weighting is a feature of the Hartle-Hawking saddle — whether H at the one-third point of the e-fold path equals M₁ under any candidate profile:

| Profile | H(N = N_HH/3)/M_Pl | matches M_Pl·e^{−N_HH/3}? |
|---|---|---|
| P0 constant | 1 | no |
| P1 exponential | e^{−N_HH/3} | exact |
| P2 linear | ≈ 0.667 | no |
| P3 (β = ½) | ≈ 0.816 | no |
| P4 Starobinsky-form | ≈ 0.982 | no |

Only the exponential-decay profile places H(N_HH/3) at M_Pl·e^{−N_HH/3} — and that profile gives n_s = −1. The profiles that recover the observed n_s put H at the one-third point near M_Pl, nowhere near M_Pl·e^{−N_HH/3}.

**The finding.** The one-third weighting cannot share an origin with the saddle that produces n_s; its geometric origin lies elsewhere. The cube-root structure M₁ ~ (M_Pl²·H_GB)^{1/3} reads naturally as a three-dimensional geometric mean, arising from three-dimensional geometric structure — and S³, with its Hopf-bundle and the seesaw chain on it, is three-dimensional. The candidate's origin is most plausibly the Hopf-bundle / seesaw structure on S³ rather than the inflationary saddle. (This is consistent with the heavy-scale construction in Companion 10, where M₁ = (8π)^{1/3}(M_Pl²H_GB)^{1/3} is read as a three-dimensional geometric mean with a Hopf-Planck × Majorana-doubling prefactor.) The search for M₁'s origin therefore shifts from the inflationary saddle to the three-dimensional geometric structure of S³ — for instance a seesaw geometric mean over scales whose product is M_Pl²·H_GB, or a flux-quantisation condition through a Hopf-bundle three-volume.

## 8. The spectral-action confluence

*(Updated 2026-08 — form-match reframed; see also Companion 17 and Working note on √(2π) κ₀-leg withdrawal.)*

The $V_E$ structure matched on the trajectory is the Einstein-frame image of a quartic potential under conformal coupling $\xi=1/6$. Writing $\Omega^2 = 1 + \Phi^2/(6M_{\mathrm{Pl}}^2)$ for the Weyl factor of $F(\Phi)=M_{\mathrm{Pl}}^2+\Phi^2/6$, a Jordan-frame quartic $V=\lambda\Phi^4$ maps to

$$V_E = \frac{\lambda\Phi^4}{\bigl(1+\Phi^2/(6M_{\mathrm{Pl}}^2)\bigr)^2},$$

which is exactly the deposited confluence form $V_E(x)=\lambda_0 x^4/(1+(\kappa_{\mathrm{cfm}}^2/12)x^2)^2$ once the coefficient identity $\kappa_{\mathrm{cfm}}=\sqrt{2}/M_{\mathrm{Pl}}$ is imposed (the $/12$ is $\xi/2=1/12$ surfacing through $\Omega^4$ — structurally forced given $\xi=1/6$, and frame-algebraic, not Hopf-topological). This answers the Read §6 fragility question: the denominator coefficient does not need a Hopf-fibre derivation to be forced; the earlier identification $\kappa_{\mathrm{cfm}}=\sqrt{2\pi}/M_{\mathrm{Pl}}$ is withdrawn (off by $\sqrt{\pi}$; Working note). Notation: $\kappa_{\mathrm{cfm}}$ here is the confluence coefficient — not the dark-matter Hopf coupling $\kappa_0=3/\sqrt{4\pi}$ (Companion 7).

This remains a *structural confluence* with NCG cosmology's $V_E$ form — two routes converging on the same effective shape — not a field identification: the spectral-action scalar $\sigma$ is generated by the right-handed-neutrino Majorana mass in the Standard Model spectral triple, while $\Phi_{\mathrm{NTE}}$ is generated by $S^3$ geometry and (per Companion 7) NTE has no right-/left-handed neutrino of that kind. NTE does not inherit the spectral-action $\sigma$.

**$T_{\mathrm{GB}}$ honesty (cross-ref Companion 9 §4).** The Gaussian-saddle-width value $T_{\mathrm{GB}}=M_{\mathrm{Pl}}/\sqrt{2\pi}$ is conditional on Companion 12 fibre-modulus grounding (not on the withdrawn Door A $\mu(N)+\Phi$ constrained action); the raw spectral-action trace has no scale extremum. The dark-matter $\kappa_0=3/\sqrt{4\pi}$ stands on its su(2)-adjoint / Hopf-monopole origin and is independent of the confluence coefficient $\kappa_{\mathrm{cfm}}$. Confluence form-match above is **historical / audit** under Door B (Companion 17 regraded).

## 9. Summary

The construction of V_NTE from the framework's existing commitments yields five structural findings and not a unique closed-form potential. ℓ = 1/H identifies the boundary's proper-length thickness with the Hubble radius and dissolves the apparent trans-Planckian problem (F1). The signature change at gauge birth is a Euclidean → Lorentzian Wick rotation, with the C¹ kink as its geometric signature and the pre-temporal negative ε_H as an artefact of applying a Lorentzian quantity to a Euclidean section (F2). V_NTE is determinate on the identity trajectory — Φ⁴ − Φ⁶ post-locking, Φ⁴ − Φ² pre-temporal, the difference itself a Wick-rotation signature — but genuinely under-constrained off it, because Door B makes |Φ_NTE| a label of the expansion history rather than a dynamics-driving Jordan field (F3). Native Φ_NTE (n_s, r) from a Hartle-Hawking Φ-saddle are **withdrawn** under Door B / F-2; the spectrum register is open under option D; imported exit-(a) Higgs-inflation numbers are a candidate, not an adoption (F4 status amended). And the M₁ one-third weighting is not a saddle feature; its cube-root structure points to a three-dimensional geometric mean on S³'s Hopf-bundle / seesaw structure (F5).

Under Door B, closing early-universe existence and spectrum is **not** “derive V_NTE / Φ-saddle H(N) from Companion 9.” Companion 9 restores GR and withdraws μ / F(Φ)R. What supplies early acceleration is **open** (option D); exit (a) — credited SM Higgs inflation — is a candidate pathway, not a selection, and is blocked as written by §8.1 / B2. M₁'s origin remains redirected from any Φ-inflaton saddle to S³'s three-dimensional geometric structure. What this companion still delivers is structural clarity about the identity dictionary and where dynamical V_NTE claims stop — the prerequisite for not papering over the Door B cut.
