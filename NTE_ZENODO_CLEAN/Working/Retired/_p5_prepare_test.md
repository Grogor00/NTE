---
title: "A structural prediction for the neutrino mass-ratio m(ν₃)/m(ν₂) on the Hopf flux line: the (flux)^(2/3) form and its two flux branches"
author: "Gregory Lyndon White"
date: "2026-06-21"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID 0009-0003-3680-2363*

**Abstract**

The seesaw mechanism for Majorana light neutrinos links observed sub-eV masses to a heavy right-handed Majorana scale $M_R$ through $m_\nu = Y^2 v^2 / M_R$, with $Y$ the Dirac Yukawa coupling and $v = 246$ GeV the electroweak vacuum expectation value. In most extensions of the Standard Model the values of $\{Y_i\}$ and $M_R$ are independent inputs constrained by observation. We present a structural prediction for the *form* of the second-generation neutrino Yukawa on a Hopf-bundle three-sphere geometry: $Y_{\nu_2} = (\mathrm{flux})^{-1/3}$, the inverse cube-root of a characteristic Hopf flux. The flux prefactor admits **two branches** distinguished by a real-structure question — whether the Dirac coupling inherits the Majorana doubling of the heavy sector. The heaviest Majorana mass scale $M_1$ carries $(8\pi)^{1/3}$ unambiguously (the doubling is structural). The Dirac Yukawa carries either the same normalisation, $Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341$ (the **8π / Majorana-dual** branch), or the single un-doubled Hopf flux, $Y_{\nu_2} = (4\pi)^{-1/3} \approx 0.430$ (the **4π / single-flux** branch). An operator-theoretic analysis of the Connes real structure favours the 4π branch for the Dirac coupling, because the Dirac entry connects left- and right-handed neutrinos *within* the particle sector and does not pass through the antiparticle (J) block that produces the Majorana doubling. We do not, however, claim the magnitude is fixed by a Lagrangian term; it remains a structural confluence-tier input, and both branches are presented.

The branch-independent commitment is the **shape** of the mass-ratio:
$$\frac{m_{\nu_3}}{m_{\nu_2}} = (\mathrm{flux})^{2/3}.$$
With the right-handed Cartan mass scale $M_R = 8.2 \times 10^{14}$ GeV (set independently by the heaviest light-neutrino mass), the two branches give:

| Branch | $Y_{\nu_2}$ | $m_{\nu_2}$ (solar) | solar fit | $m_{\nu_3}/m_{\nu_2}$ | ratio fit |
|---|---|---|---|---|---|
| **8π** | $(8\pi)^{-1/3}=0.341$ | $0.00860$ eV | $0.993\times$ | $(8\pi)^{2/3}=8.57$ | $1.47\times$ |
| **4π** | $(4\pi)^{-1/3}=0.430$ | $0.01365$ eV | $1.58\times$ | $(4\pi)^{2/3}=5.40$ | $0.93\times$ |

No single $M_R$ fits both the solar level and the atmospheric ratio at once: the 8π branch fits the solar level tightly while the ratio overshoots by $\approx 1.5\times$; the 4π branch fits the ratio tightly while the solar level overshoots by $\approx 1.5\times$. **This is not a zero-parameter prediction**, and neither branch is dialled to the data. The genuine, fallible content is the $(\mathrm{flux})^{2/3}$ form and the trade-off it forces. No observational input from the cosmological-constant sector enters the derivation. The first-generation Yukawa $Y_{\nu_1}$, the charged-lepton Yukawas, the full Dirac mass matrix from the finite algebra, and a first-principles fixing of the flux branch all remain open. We give the geometric derivation, the seesaw arithmetic for both branches, the cross-check with its honest tension, and five falsifiers.

**Keywords:** neutrino masssaw mechanism; Yukawa couplings; Hopf bundle; spectral geometry; real structure; precision neutrino physics

---

## 1. Introduction

The seesaw mechanism remains the most economical explanation of the observed sub-eV neutrino mass scale: a Standard Model singlet right-handed neutrino with Majorana mass $M_R$ at high scale, coupled to the left-handed neutrino through a Dirac Yukawa $Y$, generates light-neutrino mass
$$m_\nu = \frac{Y^2 v_{\mathrm{EW}}^2}{M_R}, \qquad v_{\mathrm{EW}} = 246~\mathrm{GeV},$$
through the standard type-I integration of the heavy right-handed mode [1–4]. The mechanism is structurally elegant; the values $\{Y_i, M_R\}$ are not. In the Standard Model with right-handed neutrinos added, both the Yukawa entries and the Majorana scale are free parameters, fit to the observed mass splittings $\Delta m^2_{21}$ and $\Delta m^2_{31}$ [5,6].

This paper reports a structural prediction for the *form* of the second-generation neutrino Yukawa $Y_{\nu_2}$ from a framework in which the universe's three-dimensional spatial topology is a closed three-sphere $S^3$ carrying a Hopf-bundle structure, and in which the Standard Model gauge group emerges at a "gauge birth" transition from an algebraic reduction at the geometric scale of the $S^3$ boundary. The framework's heaviest Majorana mass scale $M_1$ is fixed structurally by a BPS-saturating tree-level closure with a characteristic cube-root prefactor $(8\pi)^{1/3}$, derived from the geometry of the $S^3$ Hopf fibration and a spectral-action computation on the product manifold $M = \mathrm{Hopf}\text{-}S^3 \times S^1 \times A_F$, where $A_F$ is the finite (algebraic) sector.

The new content of this paper is twofold. First, the Yukawa coupling on the same Hopf flux line carries the *inverse* cube-root exponent of the Majorana scale: $Y_{\nu_2} = (\mathrm{flux})^{-1/3}$. The Majorana mass scales as $(\mathrm{flux}/V)^{1/3}$ (volumetric cube root on the flux line); the dimensionless Dirac Yukawa scales as $(\mathrm{flux}/V)^{-1/3}$, the dual exponent, with the Higgs vacuum expectation value supplying the mass dimension downstream. Second, and the focus of this revision, the flux prefactor itself is **not** unambiguous for the Dirac coupling: it depends on whether the Dirac Yukawa inherits the factor-of-2 Majorana doubling that the heavy sector carries. This produces two branches, set out in §3, with distinct observational signatures.

**Scope, stated plainly at the outset.** This is *not* a zero-parameter prediction and we do not present it as one. $M_R$ is a structural confluence-tier input, not a derived output. The magnitude of $Y_{\nu_2}$ is not fixed by a Lagrangian term in either branch; what the geometry fixes is the *form* $(\mathrm{flux})^{-1/3}$ and the $(\mathrm{flux})^{2/3}$ mass-ratio shape. The *test* this paper offers — the thing a reader should try to break — is that ratio shape, and the trade-off that no single $M_R$ fits both the solar level and the atmospheric ratio simultaneously. No observational input from the cosmological-constant sector enters at any step.

A companion paper [14] establishes that on closed product-of-spheres 4-manifolds $S^p \times F^q$ with a flat factor ($p \in \{2,3,4\}$), the Weyl–Euler trace-anomaly combination $F_1 = -18 C^2 + 11 E_4$ vanishes identically **only at $p = 3$** — i.e. on $M = S^3 \times S^1$ within that family (Lafontaine 1988; Chang–Gursky–Yang 2003). Uniqueness is *not* claimed among all closed 4-manifolds: flat $T^4$ and closed-hyperbolic $N^3 \times S^1$ lie outside this family. The companion establishes the possibility space within the product-of-spheres family; the present paper establishes the empirical signature on that geometry.

Section 2 defines the neutrino mass-eigenmode ontology. Section 3 reviews the cube-root Majorana prefactor, presents its Dirac dual, and sets out the two flux branches with the real-structure argument that favours 4π. Section 4 gives the seesaw arithmetic and the solar mass scale for both branches. Section 5 cross-checks $m_{\nu_3}$ and states the atmospheric tension honestly. Section 6 places the result in a tier register and lists five falsifiers. Section 7 lays out the remaining open programme, including the first-principles fixing of the flux branch.

## 2. The neutrino mass-eigenmode ontology

The framework treats the three light neutrinos as eigenmodes of the *unresolved* $\mathrm{su}(2)$ Cartan decomposition of the right-handed neutrino sector relative to the direction set by the Higgs vacuum expectation value. In the generator basis $\{\sigma_1, \sigma_2, \sigma_3\}$ with $\sigma_3$ aligned to the Higgs VEV direction, the three eigenmodes carry distinct geometric structure on the $S^3$ Hopf bundle. The restricted product-of-spheres trace-anomaly result for $M = S^3 \times S^1$ ($p = 3$; companion [14]) is the substrate selection this paper builds on.

- The $\sigma_1$ and $\sigma_2$ modes carry the Hopf flux quantisation, lying transverse to the Cartan direction and sourcing the heaviest and second-heaviest Majorana masses through the BPS-saturating geometric closure.
- The $\sigma_3$ mode is the Cartan direction itself, decoupled from the Hopf flux line, carrying the right-handed Cartan mass scale $M_R$ that anchors the heaviest light-neutrino seesaw.

The assignment of light-neutrino mass eigenstates to these structural modes is:

| Eigenmode | Pauli direction | Right-handed scale | Light-neutrino mass route |
|---|---|---|---|
| $\nu_1$ | $\sigma_1$ | $M_1$ from Hopf-flux BPS closure | First-generation Yukawa bracket (open) |
| $\nu_2$ | $\sigma_2$ | $M_2 = M_1(1+\sin^2\theta_{13})$ from $Z_2$ split | **This paper** |
| $\nu_3$ | $\sigma_3$ (Cartan) | $M_3 = M_R$ from heaviest light-neutrino consistency | $m_{\nu_3} = v_{\mathrm{EW}}^2/M_R$ (cross-check) |

The $Z_2$ split between $M_1$ and $M_2$ is the same $\sigma_1 \leftrightarrow \sigma_2$ exchange that underwrites the framework's prediction of maximal atmospheric mixing $\theta_{23} = \pi/4$ at leading order. Both predictions share the same $Z_2$ generator at the Cartan structure level.

The seesaw reading is non-standard in one respect: the *coupling* line for the second-generation light neutrino is on $\sigma_1/\sigma_2$ (carrying the inverse Hopf-flux normalisation), but the *seesaw denominator* is the Cartan-sector scale $M_R$, not the Majorana scale $M_2$. This distinction is load-bearing; we address it in §4.2.

## 3. The cube-root prefactor, its dual, and the two flux branches

### 3.1 The Majorana scale (8π, unambiguous)

The heaviest Majorana mass scale is set by a BPS-saturating tree-level closure on the Hopf-bundle flux line at the gauge-birth temperature:
$$M_1 = (8\pi)^{1/3} \left( M_{\mathrm{Pl}}^2\, H_{\mathrm{GB}} \right)^{1/3} \cdot (1 + c\,(\mu/M)^2), \qquad c \approx 0.97,$$
with $M_{\mathrm{Pl}}$ the reduced Planck mass and $H_{\mathrm{GB}}$ the Hubble parameter at gauge birth. The closure gives $M_1 \approx 5.42 \times 10^9$ GeV at central values. The $(8\pi)$ structure combines **Majorana doubling** (a factor of 2 from the Weyl-pair-to-Majorana identification) with a three-dimensional volumetric prefactor (a factor of $4\pi$ from the unit-three-sphere volume), giving $8\pi$ as the tree-level combination. The factor of 2 is structural: it is the operator-theoretic content that makes a Majorana mass term possible at all, and it cannot be removed without removing the lepton-number violation that defines the Majorana sector. **$M_1$ carries $(8\pi)^{1/3}$ in all branches considered below.**

### 3.2 The Dirac dual and the branch question

On the *same* Hopf flux line that gives the Majorana mass, the Dirac Yukawa coupling scales with the *inverse* cube-root exponent. The reason is dimensional: the Majorana mass has mass dimension 1, requiring a flux-cube-root normalisation; the Yukawa coupling is dimensionless, with the Higgs vacuum expectation value $v_{\mathrm{EW}}$ supplying the mass dimension downstream. The Hopf-Killing-spinor flux supports a Majorana–Dirac relation at the cube-root level:
$$Y_{\nu_2} = (\mathrm{flux})^{-1/3}.$$

The open question is **which flux** the Dirac coupling sees — the doubled $8\pi$ of the Majorana sector, or the single un-doubled $4\pi$ Hopf flux:

- **8π / Majorana-dual branch:** the Dirac Yukawa inherits the same $8\pi$ normalisation as the Majorana scale, as its exact cube-root inverse:
 $$Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341.$$
 This is the reading in which the Dirac prefactor is the dual of the Majorana prefactor on a shared normalisation.

- **4π / single-flux branch:** the Dirac Yukawa sees only the single Hopf flux $4\pi$, *without* the Majorana factor-of-2 doubling:
 $$Y_{\nu_2} = (4\pi)^{-1/3} \approx 0.430.$$

### 3.3 The real-structure argument (favours 4π)

The distinction between the branches is decided, in principle, by where the two couplings sit in the Connes real structure $(A, H, D, J)$ with antilinear $J$. The Hilbert space decomposes as $H_{\mathrm{particle}} \oplus H_{\mathrm{antiparticle}}$, with $J$ exchanging the two summands.

- The **Majorana mass** $M_R$ connects $\nu_R$ to its charge conjugate $J\nu_R$ — it lives in the particle↔antiparticle (J) block, violates fermion number by two, and inherits the reality doubling. This is the structural source of the factor of 2 → $8\pi$.
- The **Dirac Yukawa** $Y_{\nu_2}$ connects $\nu_L$ to $\nu_R$ *within* the particle sector via the Higgs scalar — no $J$, conserves fermion number, and does **not** pass through the antiparticle block. It therefore does not inherit the doubling, and sees the single Hopf flux → $4\pi$.

This assignment is not a basis choice: it follows from the standard identification of charge conjugation with the $J$ operation and from fermion-number conservation, which is structural rather than conventional. An operator-theoretic analysis of the octonionic bimodule, including the non-associative associator on the relevant Killing-spinor overlap, finds that the off-diagonal Dirac overlap activates a single sector (the antiparticle-block sector is inactive for the Dirac coupling) and that the associator does not relabel the particle/antiparticle sectors at this vertex. **On this analysis the 4π / single-flux branch is favoured for the Dirac coupling.**

### 3.4 Honest scope on the branch

We nonetheless present both branches, for two reasons. First, the *magnitude* of $Y_{\nu_2}$ is not fixed by a first-principles Lagrangian term in either branch; whether a Lagrangian derivation on the Hopf flux line ultimately fixes the flux prefactor, or leaves it as a confluence-tier structural input, is an explicit open item (§7). Second, the two branches make sharply different and individually falsifiable predictions (§4–§5), so naming both — rather than committing prematurely — is the honest presentation while the first-principles question is open. Neither branch is dialled to the data; each is reported with the leg it fits and the leg it misses.

## 4. The seesaw formula and the solar mass scale

### 4.1 Canonical seesaw formula (confluence-tier $M_R$)

Combining the dual Yukawa from §3 with the right-handed Cartan mass scale $M_R$ from the heaviest light-neutrino consistency (§5), the canonical seesaw expression for the second-generation light-neutrino mass is
$$m_{\nu_2} = \frac{(\mathrm{flux})^{-2/3}\, v_{\mathrm{EW}}^2}{M_R}$$
with $M_R = 8.2 \times 10^{14}$ GeV and $v_{\mathrm{EW}} = 246$ GeV. Evaluating both branches:

| Branch | $m_{\nu_2}$ | Observed $\sqrt{\Delta m^2_{21}}$ | Ratio |
|---|---|---|---|
| **8π** | $(8\pi)^{-2/3} v^2/M_R = 0.00860$ eV | $0.00866$ eV | $0.993\times$ |
| **4π** | $(4\pi)^{-2/3} v^2/M_R = 0.01365$ eV | $0.00866$ eV | $1.58\times$ |

The mass-value comparison is the directly meaningful figure (the prediction is a mass scale, not a squared splitting). In the **8π** branch the solar level is reproduced tightly ($0.993\times$, within current $1\sigma$). In the **4π** branch the solar level overshoots by $1.58\times$ (and, in squared-splitting terms, $\Delta m^2_{21}$ overshoots by $\approx 2.5\times$ — the solar leg is *not* fit in this branch). In neither branch is the mass scale fitted to the solar splitting: $v_{\mathrm{EW}}$ is the electroweak scale, $M_R$ is anchored by the heaviest light-neutrino mass (§5), and the cube-root prefactor is structural.

### 4.2 Critical seesaw denominator discipline (branch-independent)

A naive misreading — applying the dual Yukawa in the seesaw formula with the second-generation Majorana scale $M_2 \approx 6.18 \times 10^{9}$ GeV in the denominator — would give, in the 8π branch,
$$m_{\nu_2}^{\mathrm{naive}} = \frac{(8\pi)^{-2/3}\, v_{\mathrm{EW}}^2}{M_2} \approx 1142~\mathrm{eV},$$
approximately $1.3 \times 10^{5}$ times the observed solar mass scale and ruled out at $\sim 10^5\sigma$. The discipline-preserving formula requires the right-handed Cartan-sector denominator $M_R$, not the Majorana-sector denominator $M_2$, for the light second-generation neutrino, in both branches. The Hopf-Killing-spinor coupling supports the *Yukawa* on the $\sigma_1/\sigma_2$ sector with inverse normalisation, but the seesaw integration runs through the Cartan-sector right-handed scale $M_R$. The mechanism by which $M_R$ enters the denominator for both $\nu_2$ and $\nu_3$ is PMNS mixing through the $\sigma_3$ Cartan — an open item we discuss in §7.

## 5. Cross-check: the atmospheric mass scale and the ratio (honest scope)

The assignment of $M_R$ is anchored by the heaviest light-neutrino mass through the Cartan-sector Yukawa $Y_3 = 1$ (no Hopf-flux normalisation; the $\sigma_3$ mode is Cartan-aligned, so the flux branch does **not** affect it):
$$m_{\nu_3} = \frac{Y_3^2\, v_{\mathrm{EW}}^2}{M_R} = \frac{v_{\mathrm{EW}}^2}{M_R}.$$
With $M_R = 8.2 \times 10^{14}$ GeV this gives $m_{\nu_3} = 0.0738$ eV in **both branches**. The comparison uses the normal-ordering atmospheric scale $\sqrt{\Delta m^2_{31}} \approx 0.0495$ eV, giving $m_{\nu_3} \approx 1.49\times \sqrt{\Delta m^2_{31}}$ — also branch-independent.

**The branch-dependent quantity is the mass-ratio.** The framework predicts $m_{\nu_3}/m_{\nu_2} = (\mathrm{flux})^{2/3}$; the observed ratio is $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.82$:

| Branch | $m_{\nu_2}$ | $m_{\nu_3}$ | $m_{\nu_3}/m_{\nu_2}$ | Observed $5.82$ |
|---|---|---|---|---|
| **8π** | $0.00860$ eV ($0.993\times$ solar) | $0.0738$ eV ($1.49\times$ atm) | $(8\pi)^{2/3}=8.57$ | $1.47\times$ |
| **4π** | $0.01365$ eV ($1.58\times$ solar) | $0.0738$ eV ($1.49\times$ atm) | $(4\pi)^{2/3}=5.40$ | $0.93\times$ |

Two structural readings follow, and we state both without dialling either:

- **8π branch:** the *solar level* is the tight leg ($0.993\times$); the *mass-ratio* overshoots by $\approx 1.47\times$. A single $M_R$ cannot anchor both at sub-1%.
- **4π branch:** the *mass-ratio* is the tight leg ($0.93\times$); the *solar level* overshoots by $\approx 1.58\times$. Note that in this branch **both** absolute scales sit $\approx 1.5\times$ high ($m_{\nu_2}$ at $1.58\times$, $m_{\nu_3}$ at $1.49\times$), so the overshoot is largely common and **cancels in the ratio** — pointing at a single $\approx 1.5\times$ normalisation offset in $M_R$, with the $(4\pi)^{2/3}$ ratio shape surviving as the clean structural prediction.

In neither branch is this a simultaneous sub-1% fit of both legs. The branch-independent commitment is the $(\mathrm{flux})^{2/3}$ *shape*; the specific value ($8.57$ or $5.40$) and which leg is tight are the flux-branch outputs.

## 6. Tier register and falsifiers

### 6.1 Tier register

We distinguish tiers of prediction by the degree of upstream observational anchoring in the derivation chain:

- **Structural consistency (confluence-tier $M_R$):** the derivation uses the electroweak vacuum expectation value $v_{\mathrm{EW}}$ and the geometric Hopf sector; $M_R$ is a structural confluence input, not a zero-parameter output; no observational input from the cosmological-constant sector enters.
- **Framework-dependent identification:** the prediction is structural but the identification with the observable requires a framework-specific reading.

The present result sits in **structural consistency on a confluence-tier $M_R$**. We are explicit that this is **not a zero-parameter prediction.** The genuine, fallible content of the paper is the forced $(\mathrm{flux})^{2/3}$ mass-ratio and the trade-off it carries; the magnitude of $Y_{\nu_2}$ and the choice of flux branch are not claimed as derived.

### 6.2 Falsifiers

1. **Solar mass splitting precision (8π branch).** In the 8π branch the prediction $\Delta m^2_{21} = 7.40 \times 10^{-5}$ eV$^2$ sits at $\sim 0.5\sigma$ from current central values. If future precision data (JUNO, KamLAND-Zen, Hyper-K) shift $\Delta m^2_{21}$ outside $7.40 \pm 0.55 \times 10^{-5}$ eV$^2$, the 8π Dirac branch fails at $>3\sigma$ with $M_R$ fixed.

2. **Mass-ratio coherence (the primary test, both branches).** The framework predicts $m_{\nu_3}/m_{\nu_2} = (\mathrm{flux})^{2/3}$ — $8.57$ (8π) or $5.40$ (4π). The observed ratio is $\approx 5.82$. The 4π branch fits this at $0.93\times$; the 8π branch is in $\approx 1.47\times$ tension. If future precision drives $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}}$ away from *both* $8.57$ and $5.40$ at $>3\sigma$, the single-$M_R$ $\sigma_3$-Cartan assignment fails outright. This is the strongest test the paper offers.

3. **Inverted hierarchy resolution.** The mode assignment requires *normal* ordering ($m_{\nu_1} < m_{\nu_2} < m_{\nu_3}$). If JUNO confirms inverted ordering at $>3\sigma$, the $\sigma_3 \to M_R$ assignment for the heaviest light neutrino fails, and the present derivation fails with it.

4. **$M_2$-only seesaw.** Any reading that places the dual Yukawa against $M_2$ alone (without the canonical $M_R$ denominator) gives $\sim 1142$ eV and is dead at $\sim 10^5\sigma$. The $M_R$ denominator is load-bearing discipline, not interpretive choice — branch-independent.

5. **Direct $Y_{\nu_2}$ measurement / branch discrimination.** Any measurement of the leading-order Dirac neutrino Yukawa away from *both* $(8\pi)^{-1/3}=0.341$ and $(4\pi)^{-1/3}=0.430$ at $>3\sigma$, absent higher-loop corrections, falsifies the construction; a measurement consistent with one and not the other discriminates the branch. Direct measurement at this precision is not currently accessible; the falsifier is included for completeness, with indirect testability via the mass splittings and the ratio.

## 7. The remaining programme

This paper closes the *form* of the second-generation entry in the neutrino Yukawa programme and isolates the flux-branch question. What remains open:

- **First-principles fixing of the flux branch.** Whether a Lagrangian term on the Hopf flux line fixes the Dirac prefactor to $4\pi$ (favoured by the real-structure analysis of §3.3) or $8\pi$, or leaves the magnitude as a confluence-tier structural input, is an explicit open item — not assumed closed here. The real-structure analysis favours 4π; a complete Lagrangian derivation is the natural next step.
- **First-generation Yukawa $Y_{\nu_1}$:** an illustrative bracket using the $Z_2$ split and the observed $\sin\theta_{13}$ gives $Y_{\nu_1} \sim 1.4 \times 10^{-4}$, consistent with the cosmological sum bound $m_{\nu_1} \lesssim 0.037$ eV. The bracket is not zero-parameter; full closure requires the embedding-depth structure on the finite algebra $A_F$.
- **Charged-lepton Yukawas $Y_e, Y_\mu, Y_\tau$:** mass-ratio closure is at high precision; the absolute charged-lepton scale is at working closure with a partial flag on the Dirac prefactor. Full closure remains open.
- **Full neutrino Dirac mass matrix from the finite algebra $D_F$:** closing the full $\{Y_{\nu_i}\}$ from the Dirac operator on $A_F$ at the gauge-birth boundary ab initio is open — the natural extension of the present second-generation result.
- **PMNS mixing and the $M_R$ denominator mechanism:** the load-bearing discipline of §4.2 requires the $M_R$ Cartan-sector denominator for the light $\nu_2$, mechanistically through PMNS mixing on the $\sigma_3$ Cartan. Ab initio derivation of that mechanism is open.

The present prediction stands or falls collectively with the cube-root Majorana prefactor it dualises and with the flux branch eventually fixed. If the tree-level $M_1$ closure holds and the 4π branch is confirmed, the $(4\pi)^{2/3}$ mass-ratio becomes the live, fallible prediction, fit at $0.93\times$, with both absolute scales sharing a common $M_R$ normalisation offset. If the 8π branch is instead fixed, the solar level becomes the tight leg at $0.993\times$ and the ratio carries the tension. Either way the $(\mathrm{flux})^{2/3}$ shape is the structural commitment.

## 8. Conclusion

The second-generation neutrino Yukawa coupling takes the structural form $Y_{\nu_2} = (\mathrm{flux})^{-1/3}$ on the Hopf-Killing-spinor flux line of the $S^3$ Hopf-bundle geometry, dual to the cube-root prefactor $(8\pi)^{1/3}$ that fixes the heaviest right-handed Majorana mass scale. The Majorana scale carries $(8\pi)^{1/3}$ unambiguously; the Dirac coupling carries either the same normalisation ($Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341$, the Majorana-dual branch) or the single un-doubled Hopf flux ($Y_{\nu_2} = (4\pi)^{-1/3} \approx 0.430$, the single-flux branch), with the real-structure analysis favouring the latter because the Dirac coupling does not pass through the antiparticle block that doubles the Majorana sector.

Combined with the right-handed Cartan mass scale $M_R = 8.2 \times 10^{14}$ GeV — independently anchored by the heaviest light-neutrino mass $m_{\nu_3} = v_{\mathrm{EW}}^2/M_R = 0.0738$ eV — the seesaw formula gives $m_{\nu_2} = 0.00860$ eV ($0.993\times$ the solar scale) in the 8π branch and $m_{\nu_2} = 0.01365$ eV ($1.58\times$) in the 4π branch. The mass-ratio is $m_{\nu_3}/m_{\nu_2} = (\mathrm{flux})^{2/3}$: $8.57$ (8π) or $5.40$ (4π) against the observed $\approx 5.82$. No single $M_R$ fits both the solar level and the atmospheric ratio simultaneously in either branch; the flux choice selects which leg is tight. This is not a zero-parameter result, and neither branch is dialled to the data. In the 4π branch both absolute scales sit $\approx 1.5\times$ high, so the offset largely cancels in the ratio, leaving the $(4\pi)^{2/3}$ shape as the clean prediction. No cosmological-constant-sector dependency enters the derivation. Five falsifiers tighten the test; the strongest is mass-ratio coherence. The first-generation Yukawa, the charged-lepton Yukawas, the full Dirac mass matrix from the finite algebra, and the first-principles fixing of the flux branch remain open.

A companion paper [14] establishes the restricted product-of-spheres trace-anomaly result for $M = S^3 \times S^1$ ($p = 3$ in $S^p \times F^q$; not a general closed-4-manifold uniqueness theorem). The pair points at one structural substrate from two directions: the selected geometry within that family under the Weyl–Euler trace-anomaly constraint (companion), and the empirical signature of a structural neutrino mass-ratio on that geometry (this paper).

---

## Acknowledgements

The author thanks adversarial-review collaborators for scrutiny at the Majorana–Dirac duality identification, the real-structure branch analysis, and the seesaw denominator discipline.

## Data availability

This work uses publicly available observational data from the Particle Data Group [5], the NuFIT global analysis [6], and Planck 2018 + BAO [19]. No new experimental data is reported.

---

## References

[1] P. Minkowski, *μ → eγ at a rate of one out of 10⁹ muon decays?*, Phys. Lett. B **67** (1977) 421.

[2] M. Gell-Mann, P. Ramond, R. Slansky, in *Supergravity*, eds. P. van Nieuwenhuizen and D. Z. Freedman, North Holland (1979).

[3] T. Yanagida, in *Workshop on the Unified Theory of Baryon Number in the Universe*, eds. A. Sawada and A. Sugamoto, KEK (1979).

[4] R. N. Mohapatra and G. Senjanović, *Neutrino mass and spontaneous parity nonconservation*, Phys. Rev. Lett. **44** (1980) 912.

[5] S. Navas et al. (Particle Data Group), *Review of Particle Physics*, Phys. Rev. D **110** (2024) 030001.

[6] I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, T. Schwetz, A. Zhou, *The fate of hints: updated global analysis of three-flavor neutrino oscillations*, JHEP **09** (2020) 178; NuFIT global analysis, www.nu-fit.org.

[7] C. Bär, *Real Killing spinors and holonomy*, Commun. Math. Phys. **154** (1993) 509.

[8] A. H. Chamseddine and A. Connes, *The Spectral Action Principle*, Commun. Math. Phys. **186** (1997) 731.

[9] J. Lafontaine, *Sur la géométrie d'une généralisation de l'équation différentielle d'Obata*, J. Math. Pures Appl. **62** (1983) 63; and conformal trace-anomaly results on product manifolds (1988).

[10] S.-Y. A. Chang, M. J. Gursky, P. C. Yang, *A conformally invariant sphere theorem in four dimensions*, Publ. Math. IHÉS **98** (2003) 105.

[11] D. V. Vassilevich, *Heat kernel expansion: user's manual*, Phys. Rep. **388** (2003) 279.

[14] G. White, *F₁ = −18 C² + 11 E₄ and the vanishing of the trace-anomaly combination on S³ × S¹ among product-of-spheres 4-manifolds*, companion preprint (2026).

[16] F. P. An et al. (JUNO Collaboration), *Neutrino Physics with JUNO*, J. Phys. G **43** (2016) 030401.

[17] S. Abe et al. (KamLAND-Zen Collaboration), *Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset*, Phys. Rev. Lett. **130** (2023) 051801.

[18] K. Abe et al. (Hyper-Kamiokande Collaboration), *Hyper-Kamiokande Design Report*, arXiv:1805.04163 (2018).

[19] N. Aghanim et al. (Planck Collaboration), *Planck 2018 results. VI. Cosmological parameters*, Astron. Astrophys. **641** (2020) A6.

---

*Corresponding author: Gregory Lyndon White, gregwhite00@gmail.com, ORCID 0009-0003-3680-2363.*
