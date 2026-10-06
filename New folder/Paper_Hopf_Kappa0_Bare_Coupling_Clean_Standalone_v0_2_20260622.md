---
title: "A structural derivation of the bare dimensionless coupling 3/√(4π) from monopole projection on the unit Hopf bundle"
author: "Greg White (Gregory Lyndon White)"
date: "2026-06-22 (v0.2 pre-submission draft)"
---

*Part of NTE Corpus v10.18.0 (deposited 2026-06).*

*Independent researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID: 0009-0003-3680-2363*

## Abstract

We derive the bare dimensionless coupling

$$\kappa_0 \;=\; \frac{3}{\sqrt{4\pi}} \;=\; \frac{3}{2\sqrt{\pi}} \;\approx\; 0.8463$$

as a structural identity in Hopf-bundle geometry on the unit 3-sphere. The numerator 3 is the dimension of the adjoint representation of SU(2), corresponding to the three SU(2)-gauge-field components (a = 1, 2, 3) on the S² Hopf base, each independently sourcing an s-wave monopole projection of a Killing spinor on the unit S³. The fixed-sign Killing-spinor solution space on S³ is 2-dimensional (the fundamental of SU(2); Bär 1993), and the "three channels" refers to the action of the three SU(2) gauge components on a single Killing-spinor amplitude, not three independent spinor polarisations. The denominator √(4π) is the L²-normalisation of the monopole harmonic Y_{00} on the unit 2-sphere — the s-wave spherical harmonic obtained by Hopf-fibre integration of a constant Killing spinor on S³ to the S² base. The combination 3 × Y_{00} = 3/√(4π) is therefore the bare structural coupling between three SU(2)-adjoint gauge components on the S² Hopf base and a monopole-projected gauge sector sourced from Killing-spinor projection on S³.

We establish three properties of this coupling: (i) the Hopf-fibre projection (§3) is canonical for the unit Hopf bundle; (ii) the SU(2)-adjoint counting (§4) of three gauge-field components is convention-independent and matches the Sonner–Tong (2009) identification of the same factor in SU(2) gauge physics; (iii) the s-wave channel is **topologically protected** (§5): for the monopole vertex V = Y_{00} = 1/√(4π) (constant on S²), the matrix element ⟨ψ|Y_{00}|ψ⟩ = (1/√(4π)) ∫|ψ|² dΩ = Y_{00} for any normalised ψ on S² (Gaunt-coefficient triviality), so higher-mode corrections do not perturb κ₀. The result is a clean math-physics identity verifiable in a few lines of spin-geometry and spherical-harmonic arithmetic.

---

## 1. Introduction

The unit 3-sphere S³, identified canonically with the Lie group SU(2), carries the Hopf bundle structure (Hopf 1931; Trautman 1985)

$$\pi: \quad S^3 \;\to\; S^2, \qquad \text{fibre} \;=\; S^1 \;=\; U(1).$$

Both S³ and the base S² are taken to carry their canonical round metrics (unit radius). The Hopf fibration has rank-one U(1) structure group, with the canonical principal connection ω whose curvature 2-form Ω descends to the S² base. The integral ∫_{S²} Ω = 2π is the Hopf invariant (one quantum of magnetic flux, in Dirac monopole conventions).

On the round unit S³, parallel spinors — the **Killing spinors** of Bär (1993) — admit a complete classification. The Killing equation

$$\nabla_a \epsilon \;=\; \pm \frac{i}{2}\, \gamma_a \, \epsilon$$

has, on the round S³, **two linearly independent solutions for each sign choice**, giving four Killing spinors total. The two sign choices correspond to the two chirality projections; for either fixed sign, the two solutions span an irreducible representation of the holonomy group SU(2) = Spin(3) acting on the Killing-spinor space (Friedrich 2000 §1.5; Bär 1993 Theorem 1).

We are interested in the bare dimensionless coupling between such Killing-spinor channels on S³ and a U(1)-monopole gauge sector on the S² Hopf base. The motivation: such couplings appear in heat-kernel calculations on closed Riemannian product backgrounds (Vassilevich 2003) and in the bosonic spectral-action computation on Hopf-S³ × ⋯ product spectral triples (Chamseddine–Connes 2010 [arXiv:0812.0165]). At leading order — before sector-specific Wilson-coefficient corrections, propagator self-energies, or self-consistency closures — the coupling is fixed by the bare structural counting: (number of gauge channels) × (s-wave monopole amplitude on S²).

We compute this bare coupling and verify that it is **topologically protected**: higher-mode corrections do not shift the leading value. The result, 3/√(4π) ≈ 0.846, is a clean structural identity in Hopf-bundle geometry.

---

## 2. Geometric setup

### 2.1 The unit Hopf bundle

The unit 3-sphere S³ ⊂ ℝ⁴ carries the round metric of unit radius. As a Lie group, S³ ≅ SU(2), with Lie algebra su(2) of dimension 3. The Hopf fibration realises S² = S³ / U(1), where U(1) acts by the right-multiplication of an internal phase on the SU(2) group manifold. The volumes are:

$$\text{vol}(S^3) \;=\; 2\pi^2, \qquad \text{vol}(S^2) \;=\; 4\pi, \qquad \text{vol}(S^1_{\rm fibre}) \;=\; \frac{2\pi^2}{4\pi} \;=\; \frac{\pi}{2},$$

with the Hopf fibre carrying half the circumference of a great circle on S³ (a consequence of the U(1) action on SU(2)).

### 2.2 The monopole harmonic on S²

The spherical harmonics Y_{ℓm} on the unit S² are the eigenfunctions of the round Laplacian ∇² with eigenvalues −ℓ(ℓ+1). The s-wave harmonic Y_{00} is the constant function with unit L² norm on S²:

$$Y_{00}(\theta, \phi) \;=\; \frac{1}{\sqrt{4\pi}}, \qquad \int_{S^2} |Y_{00}|^2 \, d\Omega \;=\; 1.$$

In the language of Dirac monopole physics, Y_{00} is the **monopole harmonic** at the s-wave (ℓ = 0) level — the constant gauge potential on S² corresponding to vanishing monopole quantum number. It is the most symmetric harmonic on S², invariant under all SO(3) rotations of the sphere.

### 2.3 Killing spinors on the round S³

On the round unit S³ = SU(2), Killing spinors satisfy ∇_a ε = ±(i/2) γ_a ε (Bär 1993). For each sign choice, the solution space is 2-dimensional (the spin representation of SO(4) restricted to SO(3)). The 2-dim fixed-sign Killing-spinor solution space carries the **fundamental (spin-1/2)** representation of SU(2). It is acted upon by the three left-invariant Killing vector fields {ξ_1, ξ_2, ξ_3} generating su(2) ≅ Lie(SU(2)), which transform under the **adjoint** representation of SU(2). The "three" that enters the bare coupling counts the three SU(2)-adjoint Killing **vectors** (and correspondingly the three components of an SU(2) gauge field in the adjoint), not three Killing **spinors**. The dim-3 adjoint count is convention-independent (Lawson–Michelsohn 1989; Friedrich 2000) and follows from dim(adj SU(2)) = 3.

---

## 3. Hopf-fibre projection of Killing spinors to the S² base

Let ψ_K be a Killing spinor on S³ of unit L² norm in some convention. Constant Killing spinors (those satisfying the Killing equation with constant amplitude in a suitable trivialisation, e.g. the left-invariant trivialisation on SU(2)) have $|\psi_K|^2$ constant on S³.

The Hopf-fibre integration produces a function on the S² base:

$$\psi_K^{(S^2)}(p) \;\equiv\; \frac{1}{\sqrt{\text{vol}(S^1_{\rm fibre})}} \int_{\pi^{-1}(p)} \psi_K \,d\theta, \qquad p \in S^2,$$

where ∫_{π^{-1}(p)} denotes the Hopf-fibre integral over the U(1) orbit above the point p. For a constant Killing spinor, this integration yields a **constant function on S²** (since the Hopf fibres are isometric and the integrand is constant).

Imposing the standard L²-normalisation ∫_{S²} |ψ_K^{(S²)}|² dΩ = 1 gives

$$|\psi_K^{(S^2)}|^2 \;=\; \frac{1}{\text{vol}(S^2)} \;=\; \frac{1}{4\pi}, \qquad \psi_K^{(S^2)} \;=\; \frac{1}{\sqrt{4\pi}} \;=\; Y_{00}(S^2).$$

**The constant Killing spinor on S³ projects to the monopole harmonic Y_{00} on S² via Hopf-fibre integration**, with amplitude 1/√(4π). This is the structural fact that underwrites §4.

---

## 4. The bare structural coupling: 3 × Y_{00} = 3/√(4π)

Take a bare coupling χ between a Killing-spinor projection on S³ and a U(1)-monopole gauge sector on the S² Hopf base. At the s-wave (Y_{00}) level, the coupling matrix element per gauge component is

$$\chi_1 \;=\; Y_{00}(S^2) \;=\; \frac{1}{\sqrt{4\pi}}.$$

Each of the three SU(2)-adjoint gauge components (A^a, a = 1, 2, 3) contributes one s-wave amplitude per Killing-spinor projection. Summing over the three gauge components gives

$$\boxed{\;\kappa_0 \;=\; 3 \;\times\; \chi_1 \;=\; 3 \;\times\; Y_{00}(S^2) \;=\; \frac{3}{\sqrt{4\pi}} \;=\; \frac{3}{2\sqrt{\pi}} \;\approx\; 0.8463.\;}$$

This is the bare dimensionless structural coupling. The factor 3 = dim(adj SU(2)) counts independent gauge-field components (convention-independent; Sonner–Tong 2009); the factor 1/√(4π) is the L²-normalisation of the s-wave monopole harmonic on the unit S². Topological protection of the per-component amplitude (§5) is independent of this gauge-component sum.

### 4.1 Convention-independence: Sonner–Tong (2009) anchor

Sonner and Tong (Phys. Rev. D 79, 084009 (2009) [arXiv:0809.3783]) identify the same factor 3 as dim(adj SU(2)) in the coupling structure of SU(2) Yang–Mills connections to Killing-spinor matter on related backgrounds. The agreement provides an **independent, convention-free anchor** for the factor 3 in (4): it is the dimension of the adjoint representation of SU(2), and the same numerical factor appears in unrelated SU(2)-gauge computations.

---

## 5. Topological protection: Gaunt-coefficient triviality of the s-wave channel

A potential concern: does the bare coupling κ₀ receive corrections from higher Dirac modes (ℓ ≥ 1) on S², or from non-constant Killing-spinor solutions on S³?

For the monopole vertex V = Y_{00} = 1/√(4π) (constant on S²), and any normalised mode ψ on S² (i.e. ∫|ψ|² dΩ = 1):

$$\langle \psi | Y_{00} | \psi \rangle \;=\; \int_{S^2} \psi^* \, Y_{00} \, \psi \, d\Omega \;=\; \frac{1}{\sqrt{4\pi}} \int_{S^2} |\psi|^2 \, d\Omega \;=\; \frac{1}{\sqrt{4\pi}} \;=\; Y_{00}.$$

The matrix element of the s-wave vertex Y_{00} on **any** normalised state ψ equals Y_{00} itself — the coupling is **independent of the mode content of ψ** beyond its normalisation. This is the Gaunt-coefficient triviality of the s-wave channel: the Gaunt integral

$$G(\ell_1, \ell_2; 0) \;=\; \int Y_{\ell_1 m_1}^* \, Y_{00} \, Y_{\ell_2 m_2} \, d\Omega \;=\; \frac{1}{\sqrt{4\pi}} \delta_{\ell_1 \ell_2} \delta_{m_1 m_2}$$

is diagonal in ℓ and proportional to the s-wave amplitude. Higher Dirac modes (ℓ ≥ 1) on S² therefore do not couple to the s-wave monopole vertex through Y_{00}; only the ℓ = 0 channel contributes.

**Consequence:** the bare coupling κ₀ = 3/√(4π) is **topologically protected** at the s-wave level. Corrections from higher Dirac modes change the occupied modes of the matter sector but do not shift the s-wave monopole matrix element. Any deviation of an observed coupling from 3/√(4π) — in contexts where the structural derivation of §3–§4 applies — must originate from (i) a different multiplet structure (not the SU(2)-adjoint count of 3), (ii) self-consistency or non-linear closure mechanisms beyond the bare coupling, or (iii) measurement systematics in the specific physical realisation. It cannot originate from perturbative correction of the s-wave monopole vertex itself.

---

## 6. Connection to spectral-action computations

The spectral action principle of Chamseddine and Connes (Commun. Math. Phys. 186, 731–750 (1997); J. Geom. Phys. 58, 38–47 (2008) [arXiv:0706.3688]; Fortsch. Phys. 58, 553–600 (2010) [arXiv:0812.0165]) computes the bosonic action of a noncommutative geometry as a heat-kernel expansion of the Dirac operator on a spectral triple. The $a_4$ Seeley–DeWitt coefficient of this expansion (Vassilevich 2003) contains the standard 4D trace-anomaly combination on the underlying Riemannian manifold; on product spectral triples whose underlying 4-manifold is Hopf-S³ × S¹ (or higher-dimensional Hopf-product backgrounds), the SU(2)-adjoint gauge sector couples to monopole-projected content on the S² Hopf base via the structural coupling derived above.

The identity (4) is therefore the **leading bare coupling** in such spectral-action computations, before sector-specific Wilson-coefficient corrections, propagator self-energies, or self-consistency closures. Whether the bare value 3/√(4π) is preserved or modified at next-to-leading order depends on the specific computation; the §5 topological-protection argument constrains the type of correction possible (no higher-Dirac-mode perturbation of the s-wave channel itself).

A heat-kernel computation on a Hopf-S³ × S¹ product background reaches the same factor 3 via the SU(2)-adjoint structure in the Seeley–DeWitt coefficient analysis. Because it shares the analytic structure of §3–§4, it is **not** an independent confirmation — it is the same identity computed by a second route.

---

## 7. Discussion

The structural identity κ₀ = 3/√(4π) ≈ 0.846 is a clean math-physics result on the unit Hopf bundle. It expresses the bare leading dimensionless coupling between **three SU(2)-adjoint gauge-field components** on S³ = SU(2) and a U(1)-monopole gauge sector on the S² Hopf base. The numerator 3 is dim(adj SU(2)) (convention-independent; anchored independently by Sonner–Tong 2009); the denominator √(4π) is the L²-normalisation of the s-wave monopole harmonic on the unit S². The fixed-sign Killing-spinor solution space on round S³ is **2-dimensional** (Bär 1993) — not three independent spinor polarisations.

The result has three structural features:

(i) **Hopf-projection canonical** — the construction uses only the canonical Hopf bundle structure on the unit 3-sphere; no additional choices are required beyond unit-radius normalisation of S³ and the standard round metric on S².

(ii) **Topologically protected at the s-wave level** — higher Dirac modes on S² do not perturb the matrix element of the s-wave monopole vertex (Gaunt-coefficient diagonality). Deviations of an observed coupling from 3/√(4π), in contexts where the structural derivation applies, must originate from non-perturbative or non-s-wave physics.

(iii) **One derivation + one independent anchor** — the Hopf projection (§3–§4) is the **primary derivation**; the Sonner–Tong SU(2)-adjoint count (§4.1) is the **convention-independent anchor**. The heat-kernel route (§6) reaches the same value via shared 3×Y₀₀ structure and is **not** an independent confirmation.

The identity is structural and falsifiable. Any heat-kernel or spectral-action calculation on a Hopf-bundle background that yields a bare leading dimensionless coupling **differing from 3/√(4π)** at the SU(2)-adjoint s-wave level would falsify the construction. Such a deviation would indicate either (a) a different multiplet count (not the SU(2)-adjoint dimension 3), (b) a non-canonical normalisation of either factor S³ or S², or (c) a coupling structure not at the s-wave Y_{00} level.

The note presents the result framework-independently: no cosmological commitments enter the bare identity itself. A companion note [9] derives a fixed-point closure κ = κ₀/(1−κ₀) from idempotent Y₀₀-sector insertion (second-order insertion ratio G = 1.000000); that closure is **derived**, not assumed, and is not load-bearing for the Hopf identity established here. Any downstream physical identification of κ₀ or of the closure value is a separate, framework-dependent question and is not claimed in this note.

---

## References

1. H. Hopf, "Über die Abbildungen der dreidimensionalen Sphäre auf die Kugelfläche," Math. Ann. **104**, 637–665 (1931).
2. A. Trautman, "Optical structures in relativistic theories," Astérisque, hors série, 401–420 (1985).
3. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry* (Princeton Math. Series 38, 1989), §III.6.
4. T. Friedrich, *Dirac Operators in Riemannian Geometry* (AMS Graduate Studies in Math. 25, 2000), §1.5.
5. C. Bär, "Real Killing spinors and holonomy," Commun. Math. Phys. **154**, 509–521 (1993).
6. J. Sonner and D. Tong, "Berry phase and supersymmetric quantum mechanics," Phys. Rev. D **79**, 084009 (2009) [arXiv:0809.3783].
7. D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279–360 (2003).
8. A. H. Chamseddine and A. Connes, "The Spectral Action Principle," Commun. Math. Phys. **186**, 731–750 (1997); "Why the Standard Model," J. Geom. Phys. **58**, 38–47 (2008) [arXiv:0706.3688]; "Noncommutative Geometry as a Framework for Unification," Fortsch. Phys. **58**, 553–600 (2010) [arXiv:0812.0165].
9. G. White, "A derived fixed-point closure for the bare Hopf coupling: κ = κ₀/(1−κ₀) from idempotent monopole projection," companion note (2026).

---

*v0.2 pre-submission draft. Self-contained: the bare identity κ₀ = 3/√(4π) is established here on the Hopf bundle alone; the closure and any physical identification are separate companion results.*
