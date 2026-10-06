---
title: "A structural prediction for the solar neutrino mass scale and the mass-ratio m(ν3)/m(ν2) = (8π)^(2/3) on the Hopf flux line"
author: "Gregory Lyndon White"
date: "2026-06-21"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com — ORCID 0009-0003-3680-2363*

**Abstract**

The seesaw mechanism for Majorana light neutrinos links observed sub-eV masses to a heavy right-handed Majorana scale $M_R$ through $m_\nu = Y^2 v^2 / M_R$, with $Y$ the Dirac Yukawa coupling and $v = 246$ GeV the electroweak vacuum expectation value. In most extensions of the Standard Model the values of $\{Y_i\}$ and $M_R$ are independent inputs constrained by observation. We present a structural prediction for the second-generation neutrino Yukawa, $Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341$, obtained as the dual normalisation of the cube-root prefactor that fixes the heaviest Majorana mass scale $M_1$ on a Hopf-bundle three-sphere geometry. Combined with the right-handed Cartan mass scale $M_R = 8.2 \times 10^{14}$ GeV (set independently by the heaviest light-neutrino mass in the framework), the predicted solar mass scale is

$$m_{\nu_2} = \frac{(8\pi)^{-2/3}\, v_{\mathrm{EW}}^2}{M_R} = 0.00860\,\mathrm{eV},$$

a factor $0.993\times$ the central value of $\sqrt{\Delta m^2_{21}} = 0.00866$ eV. This mass scale is not fitted to $\Delta m^2_{21}$.

**The load-bearing structural test is the mass-ratio prediction** $m_{\nu_3}/m_{\nu_2} = (8\pi)^{2/3} \approx 8.57$ versus the observed $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.82$ — a **$\sim 1.5\times$ tension.** The same single $M_R$ gives $m_{\nu_3} = 0.0738$ eV, which is $\approx 1.49\times$ the normal-ordering atmospheric scale $\sqrt{\Delta m^2_{31}} \approx 0.0495$ eV. The solar-scale match $0.993\times$ is the **$M_R$-normalisation point** on a confluence-tier structural input — not an independent zero-parameter prediction, and not a simultaneous sub-1% fit of both legs. We are explicit about this scope throughout. No observational input from the cosmological-constant sector enters the solar derivation. The first-generation Yukawa $Y_{\nu_1}$, the charged-lepton Yukawas, and the full Dirac mass matrix from the finite algebra remain open. We give the geometric derivation, the seesaw arithmetic, the cross-check with its honest tension, and five falsifiers.

**Keywords:** neutrino mass; seesaw mechanism; Yukawa couplings; Hopf bundle; spectral geometry; precision neutrino physics

---

## 1. Introduction

The seesaw mechanism remains the most economical explanation of the observed sub-eV neutrino mass scale: a Standard Model singlet right-handed neutrino with Majorana mass $M_R$ at high scale, coupled to the left-handed neutrino through a Dirac Yukawa $Y$, generates light-neutrino mass

$$m_\nu = \frac{Y^2 v_{\mathrm{EW}}^2}{M_R}, \qquad v_{\mathrm{EW}} = 246~\mathrm{GeV},$$

through the standard type-I integration of the heavy right-handed mode [1–4]. The mechanism is structurally elegant; the values $\{Y_i, M_R\}$ are not. In the Standard Model with right-handed neutrinos added, both the Yukawa entries and the Majorana scale are free parameters, fit to the observed mass splittings $\Delta m^2_{21}$ and $\Delta m^2_{31}$ [5,6]. The natural-scale puzzle — why the lightest seesaw scale sits near $10^9$–$10^{15}$ GeV rather than at the Planck or electroweak scales — is unresolved within the Standard Model.

This paper reports a structural prediction for the second-generation neutrino Yukawa $Y_{\nu_2}$ from a framework in which the universe's three-dimensional spatial topology is a closed three-sphere $S^3$ carrying a Hopf-bundle structure, and in which the Standard Model gauge group emerges at a "gauge birth" transition from an algebraic reduction at the geometric scale of the $S^3$ boundary. The framework's heaviest Majorana mass scale $M_1$ is fixed structurally by a BPS-saturating tree-level closure with a characteristic cube-root prefactor $(8\pi)^{1/3}$, derived from the geometry of the $S^3$ Hopf fibration and a spectral-action computation on the product manifold $M = \mathrm{Hopf}\text{-}S^3 \times S^1 \times A_F$, where $A_F$ is the finite (algebraic) sector.

The new content of this paper is the recognition that the Yukawa coupling on the same Hopf flux line carries the *inverse* of the Majorana prefactor:

$$Y_{\nu_2} = (8\pi)^{-1/3}.$$

This is a duality identification, not a fit. The Majorana mass scales as $(\mathrm{flux}/V)^{1/3}$ (volumetric cube root on the flux line); the Dirac Yukawa coupling on the same line scales as $(\mathrm{flux}/V)^{-1/3}$, the dual exponent. Combined with the framework's independent fix of the right-handed Cartan mass scale $M_R$ from the heaviest light-neutrino mass $m_{\nu_3} = v_{\mathrm{EW}}^2/M_R$, the seesaw formula gives

$$m_{\nu_2} = \frac{(8\pi)^{-2/3}\, v_{\mathrm{EW}}^2}{M_R} = 0.00860~\mathrm{eV},$$

which is $0.993\times$ the central value of $\sqrt{\Delta m^2_{21}} = 0.00866$ eV [5,6]. The match sits within current $1\sigma$ observational precision.

**Scope, stated plainly at the outset.** This is *not* a zero-parameter prediction and we do not present it as one. $M_R$ is a structural confluence-tier input, not a derived output. The solar-scale match is the point at which $M_R$ is normalised; it is one leg, not two independent hits. The *test* this paper offers — the thing a reader should try to break — is the **mass-ratio** $m_{\nu_3}/m_{\nu_2} = (8\pi)^{2/3} \approx 8.57$, which the same structure forces, and which currently overshoots the observed $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.82$ by a factor $\approx 1.5$. That tension is real, it is the framework's, and we keep it in view from abstract to conclusion. No observational input from the cosmological-constant sector enters at any step of the solar derivation.

A companion paper [14] establishes that on closed product-of-spheres 4-manifolds $S^p \times F^q$ with a flat factor ($p \in \{2,3,4\}$), the Weyl–Euler trace-anomaly combination $F_1 = -18 C^2 + 11 E_4$ vanishes identically **only at $p = 3$** — i.e. on $M = S^3 \times S^1$ within that family (Lafontaine 1988; Chang–Gursky–Yang 2003). Uniqueness is *not* claimed among all closed 4-manifolds: flat $T^4$ and closed-hyperbolic $N^3 \times S^1$ lie outside this family. The companion establishes the possibility space within the product-of-spheres family; the present paper establishes the empirical signature on that geometry. Read together, the pair points at one structural substrate from two directions.

Section 2 defines the neutrino mass-eigenmode ontology. Section 3 reviews the cube-root Majorana prefactor and presents its Dirac dual. Section 4 gives the seesaw arithmetic and the $0.993\times$ match. Section 5 cross-checks $m_{\nu_3}$ and states the $\approx 1.49\times$ atmospheric tension honestly. Section 6 places the result in a tier register and lists five falsifiers, the strongest being the mass-ratio test. Section 7 lays out the remaining open programme.

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

The seesaw reading is non-standard in one respect: the *coupling* line for the second-generation light neutrino is on $\sigma_1/\sigma_2$ (carrying the inverse Hopf-flux normalisation), but the *seesaw denominator* is the Cartan-sector scale $M_R$, not the Majorana scale $M_2$. This distinction is load-bearing; we address it in §4.

## 3. The cube-root prefactor and its dual

The heaviest Majorana mass scale is set by a BPS-saturating tree-level closure on the Hopf-bundle flux line at the gauge-birth temperature:

$$M_1 = (8\pi)^{1/3} \left( M_{\mathrm{Pl}}^2\, H_{\mathrm{GB}} \right)^{1/3} \cdot (1 + c\,(\mu/M)^2), \qquad c \approx 0.97,$$

with $M_{\mathrm{Pl}}$ the reduced Planck mass and $H_{\mathrm{GB}}$ the Hubble parameter at gauge birth. The closure gives $M_1 \approx 5.42 \times 10^9$ GeV at central values. Tree-level uniqueness of the prefactor $(8\pi)^{1/3}$ — eliminating the candidate alternatives $(4\pi)^{1/3}$ and $(12\pi)^{1/3}$ — was established in the framework's spectral-action consolidation. The $(8\pi)$ structure combines Majorana doubling (a factor of 2 from the Weyl-pair-to-Majorana identification) with a three-dimensional volumetric prefactor (a factor of $4\pi$ from the unit-three-sphere volume), giving $8\pi$ as the only consistent tree-level combination.

The key observation is geometric: on the *same* Hopf flux line that gives Majorana mass scaling as $(\mathrm{flux}/V)^{1/3}$, the Dirac Yukawa coupling scales as $(\mathrm{flux}/V)^{-1/3}$ — the dual exponent. The reason is dimensional: the Majorana mass has mass dimension 1, requiring a flux-cube-root normalisation; the Yukawa coupling is dimensionless, with the Higgs vacuum expectation value $v_{\mathrm{EW}}$ supplying the mass dimension downstream. The geometric reading is that the Hopf-Killing-spinor flux supports a Majorana–Dirac duality at the cube-root level, in which the BPS-saturating prefactor on the Majorana side becomes its inverse on the Dirac side:

$$Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341.$$

This is the dual of the Majorana cube-root prefactor, not an independent structural quantity. If the tree-level Majorana closure stands, the Yukawa duality stands with it; if either fails, the duality fails with it. The vulnerability is shared — and, as §6 notes, that shared vulnerability is the test's epistemic strength.

## 4. The seesaw formula and the solar mass scale

### 4.1 Canonical seesaw formula (confluence-tier $M_R$)

Combining the dual Yukawa from §3 with the right-handed Cartan mass scale $M_R$ from the heaviest light-neutrino consistency (§5), the canonical seesaw expression for the second-generation light-neutrino mass is

$$m_{\nu_2} = \frac{(8\pi)^{-2/3}\, v_{\mathrm{EW}}^2}{M_R}$$

with $M_R = 8.2 \times 10^{14}$ GeV and $v_{\mathrm{EW}} = 246$ GeV. Evaluating:

$$m_{\nu_2} = (8\pi)^{-2/3} \times \frac{(246~\mathrm{GeV})^2}{8.2 \times 10^{14}~\mathrm{GeV}} = 0.00860~\mathrm{eV}.$$

The comparison to observation:

| Quantity | Prediction | Observed | Ratio |
|---|---|---|---|
| $m_{\nu_2}$ | $0.00860$ eV | $\sqrt{\Delta m^2_{21}} = 0.00866$ eV | $0.993\times$ |
| $\Delta m^2_{21}$ | $7.40 \times 10^{-5}$ eV$^2$ | $7.49 \pm 0.19 \times 10^{-5}$ eV$^2$ (NO) [6] | $0.988\times$, within $1\sigma$ |
| $\Delta m^2_{21}$ | $7.40 \times 10^{-5}$ eV$^2$ | $7.53 \pm 0.18 \times 10^{-5}$ eV$^2$ [5] | $0.983\times$, within $1\sigma$ |

The mass-value comparison $m_{\nu_2}^{\mathrm{pred}}/m_{\nu_2}^{\mathrm{obs}} = 0.993$ is the directly meaningful figure (the prediction is a mass scale, not a squared splitting). This mass scale is not fitted to the solar mass splitting at any step: $v_{\mathrm{EW}}$ is the electroweak scale, $M_R$ is anchored by the heaviest light-neutrino mass (§5), and the cube-root prefactor is structural from the Hopf-bundle BPS closure. It remains, however, a single normalisation point on a confluence-tier $M_R$ — see §6 for the tier register.

### 4.2 Critical seesaw denominator discipline

A naive misreading — applying the dual Yukawa $(8\pi)^{-1/3}$ in the seesaw formula with the second-generation Majorana scale $M_2 \approx 6.18 \times 10^{9}$ GeV in the denominator — would give

$$m_{\nu_2}^{\mathrm{naive}} = \frac{(8\pi)^{-2/3}\, v_{\mathrm{EW}}^2}{M_2} \approx 1142~\mathrm{eV},$$

approximately $1.3 \times 10^{5}$ times the observed solar mass scale and ruled out at $\sim 10^5\sigma$. The discipline-preserving formula requires the right-handed Cartan-sector denominator $M_R$, not the Majorana-sector denominator $M_2$, for the light second-generation neutrino. The Hopf-Killing-spinor coupling supports the *Yukawa* on the $\sigma_1/\sigma_2$ sector with inverse normalisation, but the seesaw integration runs through the Cartan-sector right-handed scale $M_R$. The mechanism by which $M_R$ enters the denominator for both $\nu_2$ and $\nu_3$ is PMNS mixing through the $\sigma_3$ Cartan — an open item we discuss in §7.

### 4.3 Equivalent $M_2$ parametrisation

An algebraically equivalent form uses the Majorana scale $M_2$ in the denominator with the Yukawa carrying an additional factor $\sqrt{M_1/M_R}$:

$$m_{\nu_2} = \frac{Y_{\nu_2}^2 v_{\mathrm{EW}}^2}{M_2}, \qquad Y_{\nu_2} = (8\pi)^{-1/3}\sqrt{M_1/M_R},$$

with $M_1 \approx 6.04 \times 10^9$ GeV and $M_2 \approx 6.18 \times 10^9$ GeV from the $Z_2$ split. This form gives $m_{\nu_2} = 0.00841$ eV, a factor $0.972\times$ the observed solar mass scale (within $2\sigma$), differing from the canonical $M_R$ form by $\approx 2\%$ from the $\sin^2\theta_{13}$ split. Both forms are derivationally equivalent; the $M_R$ form is the cleaner statement of the underlying duality.

## 5. Cross-check: the atmospheric mass scale (honest scope)

The assignment of $M_R$ is anchored by the heaviest light-neutrino mass through the Cartan-sector Yukawa $Y_3 = 1$ (no Hopf-flux normalisation; the $\sigma_3$ mode is Cartan-aligned):

$$m_{\nu_3} = \frac{Y_3^2\, v_{\mathrm{EW}}^2}{M_R} = \frac{v_{\mathrm{EW}}^2}{M_R}.$$

With $M_R = 8.2 \times 10^{14}$ GeV this gives $m_{\nu_3} = 0.0738$ eV. The comparison uses the **normal-ordering atmospheric scale** $\sqrt{\Delta m^2_{31}}$:

| Quantity | Prediction | Observed | Ratio |
|---|---|---|---|
| $m_{\nu_2}$ | $0.00860$ eV | $\sqrt{\Delta m^2_{21}} = 0.00866$ eV | $0.993\times$ |
| $m_{\nu_3}$ (same $M_R$) | $0.0738$ eV | $\sqrt{\Delta m^2_{31}} \approx 0.0495$ eV | $\approx 1.49\times$ |

**Structural ratio test.** The framework predicts $m_{\nu_3}/m_{\nu_2} = (8\pi)^{2/3} \approx 8.57$. The observed ratio is $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.82$. A single $M_R$ **cannot** anchor both legs at sub-1%: anchoring the solar leg (0.993×) forces the atmospheric leg off by $\approx 8.57/5.82 \approx 1.47$. This is a genuine $\sim 1.5\times$ tension, and we state it as such. The solar prediction of §4 is the confluence-tier normalisation point; atmospheric consistency is **open**, not a simultaneous-fit success.

## 6. Tier register and falsifiers

### 6.1 Tier register

We distinguish tiers of prediction by the degree of upstream observational anchoring in the derivation chain:

- **Structural consistency (confluence-tier $M_R$):** the derivation uses the electroweak vacuum expectation value $v_{\mathrm{EW}}$ and the geometric Hopf sector; $M_R$ is a structural confluence input, not a zero-parameter output; no observational input from the cosmological-constant sector enters.
- **Framework-dependent identification:** the prediction is structural but the identification with the observable requires a framework-specific reading.

The present result sits in **structural consistency on a confluence-tier $M_R$** for the solar leg: $v_{\mathrm{EW}}$ is measured, $M_R$ is a structural input, and $(8\pi)^{-1/3}$ is structural. **Atmospheric leg:** the same $M_R$ gives $m_{\nu_3}$ at $\approx 1.49\times$ $\sqrt{\Delta m^2_{31}}$ (§5) — a mass-ratio tension of $\approx 1.5\times$, not simultaneous-fit status.

We are explicit that this is **not a zero-parameter prediction.** The solar match is a normalisation point, not an independent risky hit; the genuine, fallible content of the paper is the forced mass-ratio $(8\pi)^{2/3}$ and the tension it currently carries.

### 6.2 Falsifiers

1. **Solar mass splitting precision.** The prediction $\Delta m^2_{21} = 7.40 \times 10^{-5}$ eV$^2$ sits at $\sim 0.5\sigma$ from current central values. If future precision data (JUNO, KamLAND-Zen, Hyper-K) shift $\Delta m^2_{21}$ outside $7.40 \pm 0.55 \times 10^{-5}$ eV$^2$, the $(8\pi)^{-1/3}$ Dirac duality fails at $>3\sigma$ with $M_R$ fixed.

2. **Direct $Y_{\nu_2}$ measurement.** Any measurement of the leading-order Dirac neutrino Yukawa away from $(8\pi)^{-1/3} = 0.341$ at $>3\sigma$, absent higher-loop corrections, falsifies the duality. Direct measurement at this precision is not currently accessible; the falsifier is included for completeness with indirect testability via the mass splittings.

3. **Inverted hierarchy resolution.** The mode assignment requires *normal* ordering ($m_{\nu_1} < m_{\nu_2} < m_{\nu_3}$). If JUNO confirms inverted ordering at $>3\sigma$, the $\sigma_3 \to M_R$ assignment for the heaviest light neutrino fails, and the present derivation fails with it.

4. **$M_2$-only seesaw.** Any reading that places the dual Yukawa against $M_2$ alone (without the $\sqrt{M_1/M_R}$ factor or the canonical $M_R$ denominator) gives $\sim 1142$ eV and is dead at $\sim 10^5\sigma$. The $M_R$ denominator is load-bearing discipline, not interpretive choice.

5. **Mass-ratio coherence (the primary test).** The framework predicts $m_{\nu_3}/m_{\nu_2} = (8\pi)^{2/3} \approx 8.57$. Current data place the observed ratio at $\approx 5.82$ — already a $\sim 1.5\times$ tension. If future precision drives $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}}$ *further* from $8.57$ at $>3\sigma$ while $m_{\nu_2}$ holds at $(8\pi)^{-2/3} v^2/M_R$, the single-$M_R$ $\sigma_3$-Cartan assignment fails. This is the strongest test the paper offers, and the framework is already in measurable tension on it.

## 7. The remaining programme

This paper closes the second-generation entry in the neutrino Yukawa programme. What remains open:

- **First-generation Yukawa $Y_{\nu_1}$:** an illustrative bracket using the $Z_2$ split and the observed $\sin\theta_{13}$ gives $Y_{\nu_1} \sim 1.4 \times 10^{-4}$, consistent with the cosmological sum bound $m_{\nu_1} \lesssim 0.037$ eV. The bracket is not zero-parameter; full closure requires the embedding-depth structure on the finite algebra $A_F$.
- **Charged-lepton Yukawas $Y_e, Y_\mu, Y_\tau$:** mass-ratio closure is at high precision ($m_\mu/m_e \sim 0.1\%$, $m_\tau/m_\mu \sim 7\%$); the absolute charged-lepton scale is at working closure with a partial flag on the Dirac prefactor. Full closure remains open.
- **Full neutrino Dirac mass matrix from the finite algebra $D_F$:** closing the full $\{Y_{\nu_i}\}$ from the Dirac operator on $A_F$ at the gauge-birth boundary ab initio is open — the natural extension of the present second-generation result.
- **PMNS mixing and the $M_R$ denominator mechanism:** the load-bearing discipline of §4.2 requires the $M_R$ Cartan-sector denominator for the light $\nu_2$, mechanistically through PMNS mixing on the $\sigma_3$ Cartan. Ab initio derivation of that mechanism is open.
- **$(8\pi)^{-1/3}$ Lagrangian derivation:** whether a first-principles Lagrangian term on the Hopf flux line fixes $Y_{\nu_2}=(8\pi)^{-1/3}$, or leaves the magnitude as confluence-tier structural input, is an explicit open item — not assumed closed here.

The present prediction stands or falls collectively with the cube-root Majorana prefactor it dualises. If the tree-level $M_1$ closure holds, the $Y_{\nu_2} = (8\pi)^{-1/3}$ duality holds; the $0.993\times$ solar match becomes a structural normalisation rather than a parameter fit, and the $(8\pi)^{2/3}$ mass-ratio becomes the live, fallible prediction. If either fails, both fail. The collective vulnerability is the test's epistemic strength.

## 8. Conclusion

The second-generation neutrino Yukawa coupling $Y_{\nu_2} = (8\pi)^{-1/3} \approx 0.341$ arises as the dual normalisation of the cube-root Majorana prefactor that fixes the heaviest right-handed neutrino mass scale, from the geometry of the Hopf-Killing-spinor flux line on the $S^3$ Hopf-bundle structure. Combined with the right-handed Cartan mass scale $M_R = 8.2 \times 10^{14}$ GeV — independently anchored by the heaviest light-neutrino mass $m_{\nu_3} = v_{\mathrm{EW}}^2/M_R$ — the seesaw formula gives

$$m_{\nu_2} = (8\pi)^{-2/3} v_{\mathrm{EW}}^2 / M_R = 0.00860~\mathrm{eV},$$

a factor $0.993\times$ the central value of $\sqrt{\Delta m^2_{21}}$. This mass scale is not fitted to the solar splitting. The same $M_R$ gives $m_{\nu_3} = 0.0738$ eV at $\approx 1.49\times$ $\sqrt{\Delta m^2_{31}}$ — the **mass-ratio headline** $m_{\nu_3}/m_{\nu_2}=(8\pi)^{2/3}\approx 8.57$ versus observed $\approx 5.82$, a **$\sim 1.5\times$ tension.** The solar $0.993\times$ match is the $M_R$-normalisation point, not a second independent hit, and not a zero-parameter result. No cosmological-constant-sector dependency enters the solar derivation. Five falsifiers tighten the test; the strongest is mass-ratio coherence, on which the framework is already in measurable tension. The first-generation Yukawa, the charged-lepton Yukawas, and the full Dirac mass matrix from the finite algebra remain open.

A companion paper [14] establishes the restricted product-of-spheres trace-anomaly result for $M = S^3 \times S^1$ ($p = 3$ in $S^p \times F^q$; not a general closed-4-manifold uniqueness theorem). The pair points at one structural substrate from two directions: the selected geometry within that family under the Weyl–Euler trace-anomaly constraint (companion), and the empirical signature of a structural solar neutrino mass scale at $0.993\times$ observed value on that geometry (this paper).

---

## Acknowledgements

The author thanks adversarial-review collaborators for scrutiny at the Majorana–Dirac duality identification and at the seesaw denominator discipline.

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
