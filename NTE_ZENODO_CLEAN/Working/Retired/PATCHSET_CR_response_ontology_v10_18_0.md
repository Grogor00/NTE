# Patch set — CR ontology/falsifiability response (v10.18.0, pre-Zenodo)

**Author:** AC · **Date:** 2026-07-05 · **For:** Cursor local render lane → CR verification → Greg ratification
**Origin:** CR handoff (2026-07-05) ontology/falsifiability pass. AC worked each point on the merits; Greg selected these five for concrete edits.
**Nature:** Five independent patches. Approve/hold each separately — Cursor applies the approved subset (four land in Part 1, one in Part 2). Patches 2 and 3 are concessions that change the argument; Patch 5 needs a construction confirmation. Details in each.

**Application rule (all):** match on the distinctive prose, not exact whitespace. Part 1 uses LaTeX `$…$`; Part 2 §8.5–8.6 uses plain unicode — preserve each file's style, do not convert. After each edit, re-read and confirm NEW present / OLD gone. **If any OLD block does not byte-match, stop and report — do not force** (the LaTeX in the Part 1 anchors is my reconstruction; Cursor's real file is authoritative). Apply to the canonical source; keep Core_Papers and paper-build/scratch-src copies in sync; re-render; confirm 29/29.

| # | CR pt | Target | Effect | Needs your call on |
|---|-------|--------|--------|--------------------|
| 1 | 1 | Part 1 §2.3 | soften "addition is forced" → FRW-definitional, Φ structural-linking | wording |
| 2 | 4 (P1) | Part 1 §I | drop Higgs-only framing → proper-time ⟺ rest-energy/embedding | wording + abstract rider |
| 3 | 5 | Part 1 §II.0 | regrade Born-as-Hopf and t=iΔN as reformulations | escape hatch (distinguishing prediction?) |
| 4 | 6 | Part 1 §III | separate forced symmetry from open magnitudes | wording |
| 5 | 7 | Part 2 §8.5–8.6 | state involution = Cayley–Dickson ℍ-flip (forced, not fitted) | confirm construction |

---

## PATCH 1 — Part 1 §2.3 (CR point 1: "central relation is a definition")

Softens "the addition is forced" to match Part 3's honesty: in the FRW sector the relation is definitional; Φ's real content is structural-linking, not new cosmological dynamics.

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §2.3

**OLD:**
```
The addition is forced: $H = \beta_{\mathrm{NTE}}|\Phi|^2$ requires a scalar whose value varies cosmologically as $|\Phi_{\mathrm{NTE}}(N)|^2 = v_{\mathrm{EW}}^2 (H(N)/H_0)$, from $v_{\mathrm{EW}}$ today to $\sim 10^{8.5} v_{\mathrm{EW}}$ at BBN; the SM Higgs, stiff against such variation by its potential curvature, cannot supply it.
```
**NEW:**
```
In the cosmological (FRW) sector this addition introduces no independent dynamics: adopting $|\Phi_{\mathrm{NTE}}(N)|^2 = v_{\mathrm{EW}}^2 (H(N)/H_0)$ makes $H = \beta_{\mathrm{NTE}}|\Phi|^2$ an identity with $\beta_{\mathrm{NTE}} = H_0/v_{\mathrm{EW}}^2$, so there $\Phi_{\mathrm{NTE}}$ is a relabelling of the expansion history — consistent with Part 3 carrying $H_0$, $w$, and $\Omega_k$ as construction/inherited rather than as new FRW dynamics. What the added scalar contributes is structural, not cosmological-dynamical: it ties the boundary-expansion sector to the electroweak scale $v_{\mathrm{EW}}$ and, through the $S^3$ Hopf geometry, to the sectors where the framework's results actually live — the cross-thickness coupling $\kappa$, the Born-rule geometry, and gauge birth. Its profile still runs from $v_{\mathrm{EW}}$ today to $\sim 10^{8.5} v_{\mathrm{EW}}$ at BBN, a range the SM Higgs — stiff against such variation by its potential curvature — could not supply; but that range is read off the expansion history, not predicted by it.
```
**Note:** aligns §2.3 with §2.4 (which already concedes self-consistency fixes no β_NTE) and Part 3. Concedes CR's FRW point while stating the genuine load-bearing role (linkage to κ / Born / gauge birth).

---

## PATCH 2 — Part 1 §I (CR point 4 / P1: photon-paradox breaks at hadrons)

Drops the "zero proper time ⟺ zero Higgs coupling, exact correlation" framing that §III's own QCD-mass concession falsifies, and replaces it with the correct relativistic correlation (proper-time ⟺ rest energy ⟺ sub-luminal) read through e-fold embedding — which covers hadrons, so §I no longer breaks against §III.

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §I (second paragraph)

**OLD:**
```
The Standard Model answers cleanly. Every entity with zero proper-time accumulation has zero Higgs (Yukawa) coupling — photons, gluons. Every entity that accumulates proper time has nonzero Higgs coupling — electrons, quarks, W/Z; neutrinos, barely, with $y_\nu \sim 10^{-12}$. The correlation is exact, with no Standard-Model exceptions. NTE takes it as structural: the boundary expansion field $\Phi_{\mathrm{NTE}}$ parameterises the map from e-fold increments to proper-time increments, and entities without Yukawa coupling do not participate — they accumulate zero proper time (null-time).
```
**NEW:**
```
The Standard Model answers in two steps. For *fundamental* particles the correlation is clean: those accumulating zero proper time are exactly the massless ones (photons, gluons), and for fundamental fermions rest mass *is* Higgs (Yukawa) coupling — so among them proper-time accumulation tracks Higgs coupling (neutrinos barely, with $y_\nu \sim 10^{-12}$). But the exception-free statement is the relativistic one: an entity accumulates proper time if and only if it carries rest energy and moves sub-luminally. That covers the composite case a Higgs-only framing would miss — a proton accumulates proper time although $\sim$99% of its mass is the QCD binding energy of massless gluons (§III). NTE takes *this* correlation as structural: proper-time accumulation is e-fold embedding depth (§VII), sourced by rest energy from whatever mechanism — Higgs coupling for fundamental fermions, confinement for hadrons — while entities with no rest energy (photons, gluons) do not embed and accumulate zero proper time (null-time).
```
**Rider (recommended, separate micro-edit):** the Abstract opens with the same framing — *"every massive particle accumulates nonzero proper time and has nonzero Higgs coupling."* If Patch 2 ships, that line should get a matching touch, e.g. replace *"and has nonzero Higgs coupling"* with *"and carries rest energy"* so the hook doesn't state what §I walks back. Flagged, not bundled — say if you want it and I'll add the abstract OLD/NEW.

---

## PATCH 3 — Part 1 §II.0 (CR point 5: apply §II.0's own test evenly)

Regrades Born-rule-as-Hopf and t=iΔN from "earned simplifications" to "reformulations," per §II.0's stated test (re-description without a distinguishing prediction doesn't earn a derivation).

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §II.0

**OLD:**
```
NTE's record therefore includes both. Simplifications that earned their place: the gauge group from $G_2$, the Born rule as a Hopf projection on $S^3$, the dark-matter coupling from $S^3$ topology.
```
**NEW:**
```
NTE's record therefore includes both. Simplifications that earned their place: the gauge group from $G_2$, and the dark-matter coupling from $S^3$ topology. Two items earlier listed as earned simplifications are, by the test just stated, better classed as *reformulations*: the Born rule as a Hopf projection on $S^3$ (§IV) is Gleason's theorem read on an imported qubit geometry — a coherent geometric restatement, but not a reduction in independent postulates unless it yields a consequence Gleason does not; and $t = i\,\Delta N$ as the Euclidean saddle (§2.1.2) is Wick rotation plus the Hartle–Hawking no-boundary condition in NTE vocabulary, wholly within the unobservable pre-temporal regime. Both are kept for the coherence they supply, not counted as postulate reductions — and either is upgraded the moment it makes a distinguishing prediction.
```
**Escape hatch (your call):** this regrade stands *unless* Born-as-Hopf or t=iΔN has a genuine distinguishing consequence I can't supply — a Hopf-geometry effect Gleason wouldn't give, or an observable constraint from the N-identification. If you can name one, that item keeps the higher grade and this patch is trimmed accordingly. Absent that, the even-handed regrade is the honest call and disarms the "advocacy not science" read CR is testing for.

---

## PATCH 4 — Part 1 §III (CR point 6: signature ontology on worst-fitting sector)

Separates what the neutrino ontology cleanly forces (symmetry: Majorana/0νββ, θ₂₃, δ) from what stays open (magnitudes: θ₁₂, atmospheric ratio), so the two don't read as one failing sector.

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §III (end of the "unresolved neutrino" paragraph)

**OLD:**
```
The "Majorana bridge" label from earlier drafts should be read in this light: the bridge is geometric, not a particle mechanism.
```
**NEW:**
```
The "Majorana bridge" label from earlier drafts should be read in this light: the bridge is geometric, not a particle mechanism. What this ontology *forces* is symmetry structure, and that is where its testable content sits: the Majorana character itself — a clean falsifier at neutrinoless double-beta decay — and, through the $\mu$–$\tau$ symmetry it carries, the maximal atmospheric angle $\theta_{23} = \pi/4$ and maximal phase $\delta_J = \pi/2$ (Part 2). The *magnitudes* on the same sector — the solar angle $\theta_{12}$ and the atmospheric mass ratio — remain open, and are carried as such (Part 3). These are a separate question from the forced symmetry; the open magnitudes do not weaken the symmetry results the ontology actually delivers.
```

---

## PATCH 5 — Part 2 §8.5–8.6 (CR point 7: S³ = S⁷/ℤ₂ forced or reverse-fit?)

States the involution is the Cayley–Dickson ℍ-complement conjugation — the same ℍ⊂𝕆 split that drives G₂→SU(3) — so the −1-on-4-of-8 action and the S³ fixed locus are forced, not reverse-fitted from choosing S³.

**TARGET:** `NTE_v10_18_0_Part2_Structure.md`, §8.5–8.6 (the involution parenthetical). Plain unicode, not LaTeX. Adjacent to the Pati–Salam/Boyle–Farnsworth patch from the earlier handoff — different anchor sentence, both apply cleanly; if running both, apply this one to the involution sentence and that one to the J₃(𝕆) sentence.

**OLD:**
```
The same quaternionic involution that gives G₂ → SU(3) also localises resolved fermions on the S³ fixed locus of S⁷/ℤ₂ while leaving the ℤ₂-even neutrino delocalised over S⁷ — the geometric basis for §IX.
```
**NEW:**
```
The same quaternionic involution that gives G₂ → SU(3) also localises resolved fermions on the S³ fixed locus of S⁷/ℤ₂ while leaving the ℤ₂-even neutrino delocalised over S⁷ — the geometric basis for §IX. That involution is not chosen to land on S³: it is the Cayley–Dickson conjugation on 𝕆 = ℍ ⊕ ℍℓ, fixing the quaternionic ℍ and negating its complement ℍℓ, so its −1 eigenspace is exactly 4 of the 8 octonionic coordinates and its fixed locus is the unit-quaternion S³ by construction — the same ℍ ⊂ 𝕆 split that drives G₂ → SU(3), not a separate reverse-fit.
```
**Confirm before shipping:** this asserts the corpus's S⁷/ℤ₂ / CPN involution *is* the Cayley–Dickson ℍ-flip. The math is sound (that conjugation fixes unit-ℍ = S³, acts −1 on 4 of 8), and §8.5–8.6's existing "same quaternionic involution that gives G₂→SU(3)" already points this way — but confirm it matches the actual construction in your S⁷/ℤ₂ definition (standalone/Companion) before it ships. If the involution is defined differently, the sentence adjusts.

---

## Routing note

These answer an adversarial CR pass, so they should go **back to CR for a verification pass** (does the response land?) alongside your ratification, not straight to render. Patches 1, 4, 5 are clean repairs/clarifications; 2 and 3 are honest concessions that make the document stronger against the "advocacy" read but do concede ground — worth a deliberate yes. CR's P0 (κ-rigidity) is already covered by the κ-appendix in Working/. Not addressed here (need your steer): CR point 2 (N-primary empirically inert where testable) and the meta distinctiveness gap — those are positioning/framing calls, not single-line edits.
