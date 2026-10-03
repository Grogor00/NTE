# Connes Programme — P0.6.5 Full Closure (Boyle-Farnsworth 2020 Direct Read)

**Stream:** Scratch (Jammer's twin), Connes Programme lead.
**Date:** 2026-05-12 morning sync continuation.
**Trigger:** Greg's "Work towards full closure (C)" directive (this morning) + arXiv:1910.11888 addition to NCG/ at `1ITO7HlOWU8v8zYqwLB0VOmez9IJ-ZyZ_` (added Greg 2026-05-12 morning, acknowledged by Jammer in P0.7 handoff §4).
**Status:** **P0.6.5 verdict UNCHANGED at PASS** (held via OctonionExtension §3.3-§3.4 per P0.8 §6.4 uplift). **Original Charter v1.1 §4.2 EXPECTATION about what arXiv:1910.11888 contributes has been REVISED** — the paper is a different programme than what Charter v1.1 implied. Substantive new findings (a)-(d) below merit Charter v1.2 framing update.
**Recognition-gate aware**: this working note reframes a structurally-mistaken expectation honestly per Manifest Lesson #28; flags the misframing for the canonical record.
**Source read:** Boyle & Farnsworth, "The standard model, the Pati-Salam model, and 'Jordan geometry'" (arXiv:1910.11888v3), at NCG/ `1ITO7HlOWU8v8zYqwLB0VOmez9IJ-ZyZ_`. Full read this session.

---

## §0. Headline

**P0.6.5 verdict: PASS — UNCHANGED from Charter v1.1 disposition.** The verdict was already PASS via OctonionExtension §3.3-§3.4 providing the G_2 → SU(3) × SU(2) × U(1) descent mechanism (per P0.8 §6.4 uplift); arXiv:1910.11888 was supposed to add spectral-action-level rigour to that disposition per Charter v1.1 §4.2.

**Substantive surprise:** arXiv:1910.11888 does NOT provide spectral-action-level rigour for G_2 × G_2 → SM descent. It is a fundamentally different NCG programme (the authors propose **"Jordan geometry"** — commutative complex Jordan algebras like J_3(C) ⊕ J_2(C) ⊕ S_2 ⊕ R — as an alternative to noncommutative geometry, NOT an extension of Farnsworth 2025's non-associative octonion approach).

**Honest disclosure required**: Charter v1.1 §4.2 framed arXiv:1910.11888 as "would close P0.6.5 with spectral-action-level rigor." This was a structurally-mistaken expectation. The actual paper does something different: it provides a separate framework (Jordan geometry → SM gauge group directly, plus Pati-Salam extension). **P0.6.5 closure does not depend on arXiv:1910.11888**; the OctonionExtension-§3.3-§3.4-based PASS stands.

**However:** arXiv:1910.11888 contains four substantive findings that warrant Charter v1.2 framing update (§4 below).

---

## §1. What arXiv:1910.11888 actually does

### §1.1 The Jordan geometry framework

Boyle-Farnsworth 2020 proposes "Jordan geometry" as an **alternative** to noncommutative geometry — explicitly NOT an extension of the non-associative octonion programme. The core move:

- Standard NCG: A is a noncommutative associative algebra (e.g., M_3(C) ⊕ H ⊕ C for SM)
- Jordan geometry: A is a **commutative non-associative Jordan algebra** of Hermitian matrices, with product given by anti-commutator `{a, b}`

**Motivation** (per §1 of arXiv:1910.11888): in quantum mechanics, observables are Hermitian operators; Hermitian operators do not close under associative operator composition but DO close under the Jordan anti-commutator product. So replacing noncommutative algebras with Jordan algebras is "more natural for quantum mechanics" than the NCG approach.

### §1.2 The SM in Jordan geometry

`A_F = J_3(C) ⊕ J_2(C) ⊕ S_2 ⊕ R`

where:
- **J_3(C)** = 3×3 Hermitian complex matrices (replaces M_3(C) of NCG SM)
- **J_2(C)** = 2×2 Hermitian complex matrices (replaces H of NCG SM)
- **S_2** = spin factor (Clifford algebra of 2 Euclidean Dirac γ matrices)
- **R** = real numbers

**Automorphism group** = SU(3) × SU(2) × U(1) — the SM gauge group directly.

**Plus one outer automorphism** = U(1)_{B-L} (anomaly-free), predicting the extended SM with sterile neutrinos + a complex scalar φ Higgsing U(1)_{B-L}.

**Crucially: this is the gauge group as automorphism, not as descent.** No G_2 → SM symmetry-breaking machinery is invoked.

### §1.3 The Pati-Salam extension in Jordan geometry

`A_F^{Pati-Salam} = J_2^L(C) ⊕ J_2^R(C) ⊕ J_4(C)`

with automorphism group SU(2)_L × SU(2)_R × SU(4).

**The Pati-Salam group SU(4) × SU(2)_L × SU(2)_R contains the SM as a subgroup.** Boyle-Farnsworth 2020 argues this Pati-Salam extension is "experimentally viable and naturally arises" within Jordan geometry.

### §1.4 What's explicitly NOT in the paper

- **G_2 × G_2 → SM descent** — Boyle-Farnsworth 2020 does not develop this. Their gauge group emerges directly as Jordan-algebra automorphism, not from G_2 × G_2 breaking.
- **Heat-kernel computations / spectral action machinery** — The paper is structural/algebraic. Spectral action is critically discussed in §2: "We suspect this expression [Tr f(D/Λ)] is incorrect, for both experimental and theoretical reasons... another motivation for Jordan geometry is that it seems to have better properties in this regard."
- **Connection to octonionic / exceptional Jordan J_3(𝕆)** — explicitly flagged in §5 Discussion bullet 1 as appealing-but-unexplored direction.

---

## §2. Why my Charter v1.1 expectation was structurally mistaken

Charter v1.1 §4.2 P0.6.5 status said: "arXiv:1910.11888 read would add spectral-action-level rigor [to the G_2 × G_2 → SM descent]." This was based on the misframing that arXiv:1910.11888 is the natural extension of Farnsworth 2025's non-associative octonion programme to SM gauge group descent.

**The actual relationship**: Boyle-Farnsworth 2020 is a **different research direction** within the broader Boyle-Farnsworth programme:
- Farnsworth 2025 = non-associative octonionic spectral geometry, G_2 × G_2 + charged Higgs framework
- Boyle-Farnsworth 2020 = Jordan geometry (commutative non-associative), J_3(C) ⊕ J_2(C) ⊕ S_2 ⊕ R + Pati-Salam extension

These are PARALLEL programmes by the same authors, not sequential elaborations.

**The misframing source**: Charter v1.1 generated the expectation from Farnsworth 2025 ref [5] citing arXiv:1910.11888 as "Pati-Salam route to SM descent." But the actual paper develops Pati-Salam in **Jordan geometry**, not in non-associative octonion geometry. The "Pati-Salam descent" Charter v1.1 hoped to verify in arXiv:1910.11888 is conceptually different from the G_2 × G_2 → SM descent the Connes Programme central deliverable presumes.

**Recognition-gate trigger**: this is exactly the kind of structural misexpectation Manifest Lesson #28 is designed to catch. Honest disclosure: my Charter v1.1 expectation was wrong; the recognition gate (Greg's morning addition of the paper signaling "go check what it actually does") + the actual read produce the correction.

---

## §3. P0.6.5 verdict status

**PASS — UNCHANGED.**

The verdict was already established at PASS via OctonionExtension §3.3-§3.4 providing the explicit G_2 → SU(3) × SU(2) × U(1) descent mechanism (per P0.8 §6.4 uplift):
- Higgs VEV picks direction e_1 ∈ Im(𝕆) ≅ R^7
- Stabilizer of e_1 in G_2 is SU(3)
- ℍ ⊂ 𝕆 quaternionic embedding gives SU(2)_L
- CPN parity selects handedness (per OctonionExtension §3.6)
- Combined with Farnsworth 2025's (7,1) charged Higgs framework, this is a **concrete G_2 × G_2 → SM descent route**

The Charter v1.1 §4.2 status note that "arXiv:1910.11888 read would add spectral-action-level rigor" was a **mistaken expectation** about what arXiv:1910.11888 provides. The paper provides different content (Jordan geometry framework + Pati-Salam in Jordan geometry); not spectral-action-level rigour for G_2 × G_2 descent.

**P0.6.5 FULL CLOSURE STATUS**: PASS via OctonionExtension §3.3-§3.4 mechanism + Farnsworth 2025 (7,1) charged Higgs framework. **Independent of arXiv:1910.11888.** The closure is structural-mechanism-level, not spectral-action-level. Charter §3 Paper S2 will compute heat-kernel spectral action on `Hopf-S³ × S¹_{β_GB} × A_F^{Farnsworth-Boyle}` directly; that IS the spectral-action-level work, and it's the Connes Programme central deliverable, not a P0.6.5 prerequisite.

---

## §4. Substantive findings from arXiv:1910.11888 (Charter v1.2 candidates)

Notwithstanding the framing correction, arXiv:1910.11888 contains four substantive findings relevant to the Connes Programme that warrant Charter v1.2 framing updates:

### §4.1 Finding (a) — Pati-Salam SU(2)_L × SU(2)_R structurally matches NTE's two-sector CPN encoding

Boyle-Farnsworth 2020 §4: Pati-Salam in Jordan geometry has `A_F = J_2^L(C) ⊕ J_2^R(C) ⊕ J_4(C)`, with automorphism group **SU(2)_L × SU(2)_R × SU(4)**. The SU(2)_L and SU(2)_R factors are independent.

**This matches NTE OctonionExtension §3.6 exactly**: SU(2)_L modes commit to +N sector; SU(2)_R modes commit to −N sector (CPN-symmetric two-sector structure).

**Implication for Charter v1.2**: §2 organising principle could note that NTE's CPN-symmetric two-sector structure has an NCG-side analog in Pati-Salam-in-Jordan-geometry's SU(2)_L × SU(2)_R structure. This is independent structural support — two different NCG programmes (Farnsworth 2025 non-associative octonions; Boyle-Farnsworth 2020 Jordan geometry) both yield SU(2)_L × SU(2)_R as natural structure when applied to SM-extending algebras. The convergence is suggestive.

### §4.2 Finding (b) — J_3(𝕆) flagged by Boyle-Farnsworth 2020 as appealing-but-unexplored

Boyle-Farnsworth 2020 §5 Discussion bullet 1: "the most interesting Jordan algebra of all: the exceptional Jordan algebra J_3(𝕆). This is obviously a very appealing possibility, and we are curious to understand how it may relate to our construction."

**This is exactly NTE OctonionExtension §6's territory.** OctonionExtension §6 develops J_3(𝕆) UV completion programme via the alternative-law `[A, A, B] = 0`. Boyle-Farnsworth 2020 acknowledges J_3(𝕆) is appealing but explicitly does not develop it.

**Implication for Charter v1.2**: NTE OctonionExtension §6's J_3(𝕆) UV completion programme is potentially a **bridge between Farnsworth 2025's non-associative octonion programme and Boyle-Farnsworth 2020's Jordan geometry programme**. J_3(𝕆) is exceptional Jordan algebra (appears in Jordan geometry context) AND is built from octonions (appears in non-associative octonion context). NTE's J_3(𝕆) programme could be cited as exploring the unexplored direction Boyle-Farnsworth 2020 flags.

Per Lesson #28 recognition-gate caveat: this is a structurally suggestive cross-link, not a derived result. Greg's recognition should weigh whether this cross-link warrants foregrounding in Charter v1.2 or is too speculative for the canonical Charter record.

### §4.3 Finding (c) — Boyle-Farnsworth 2020 questions standard spectral action formula

Boyle-Farnsworth 2020 §2: "The traditional proposal [for S_bosonic] has been to obtain the remaining terms from the so called 'spectral action' Tr[f(D/Λ)], where Λ is some energy scale, and f(x) is some real function. **But we suspect this expression is incorrect, for both experimental and theoretical reasons:** from the experimental standpoint, it predicts relationships between standard model couplings (including gravitational couplings) which disagree with observations, and from the theoretical standpoint, these relations are also not preserved by the known RG flow of the standard model (regarded as an effective field theory)."

**This is important context for the Connes Programme central deliverable.** Boyle-Farnsworth 2020 (one of the authors of the non-associative octonion programme Charter §3 invokes) explicitly questions the standard spectral action formula Tr[f(D/Λ)] on both experimental and theoretical grounds.

**Implication for Charter v1.2**: §3 central deliverable (Paper S2 heat-kernel computation) should acknowledge this skepticism honestly. Two possible dispositions:

1. **NTE-specific defense**: argue that NTE's closed-S³ + Wick-rotation + ξ = 1/6 structure stabilizes the spectral action formula in ways the standard CC programme doesn't (because NTE's specific commitments fix the cutoff structure differently). This needs explicit argument, not just assertion.

2. **Honest skepticism**: acknowledge that Boyle-Farnsworth 2020's concerns about the spectral action formula could affect NTE's Paper S2 results, and that Paper S2 should be cross-checked against alternative bosonic-action formulations if available.

Recognition-gate consideration: this is a real structural concern that affects how confident NTE should be in spectral-action-level outputs. Greg's recognition should weigh how to frame Paper S2's dependence on the spectral action formula given Boyle-Farnsworth's own skepticism.

### §4.4 Finding (d) — Pati-Salam-in-Jordan-geometry as alternative NCG programme

Boyle-Farnsworth 2020 §4 + §5: Pati-Salam in Jordan geometry is a viable alternative NCG programme, distinct from Chamseddine-Connes-van Suijlekom 2013 (arXiv:1304.8050) "Beyond the SM with NCG" Pati-Salam-in-NCG and from Farnsworth 2025's G_2 × G_2 structure.

**Implication for Charter v1.2**: NTE has at least THREE NCG-side reference programmes that align with NTE's pre-temporal structure to various degrees:
- **Farnsworth 2025**: G_2 × G_2 + charged Higgs (non-associative octonionic; main reference for Charter §2-§3)
- **Boyle-Farnsworth 2020**: Jordan geometry SM + Pati-Salam extension
- **Chamseddine-Connes-van Suijlekom 2013**: Pati-Salam-in-NCG (different from Boyle-Farnsworth 2020 Jordan geometry route)

Each programme produces SM-compatible spectral data via a different route. **Convergence across multiple NCG approaches is structural evidence that the SM is somehow naturally encoded in the spectral-data framework**, but the specific route NTE adopts (Farnsworth 2025 G_2 × G_2) is a structural commitment, not a forced choice.

---

## §5. Recognition-gate consideration on this working note

Per Manifest Lesson #28, this working note's findings need to pass Greg's recognition before being treated as load-bearing for Charter v1.2 updates. Specifically:

- **The "framing was structurally mistaken" claim (§2 above)** — I'm characterising my Charter v1.1 expectation as wrong. This is honest disclosure of an error. Greg's recognition: does the error characterisation match his view, or is there a different reading?

- **The SU(2)_L × SU(2)_R cross-link to NTE OctonionExtension §3.6 (§4.1 above)** — structurally suggestive convergence. Greg's recognition: does this convergence warrant foregrounding, or is it too coincidental for canonical incorporation?

- **The J_3(𝕆) bridge claim (§4.2 above)** — speculative cross-link between Farnsworth 2025 and Boyle-Farnsworth 2020 via OctonionExtension §6. Greg's recognition: structural insight or over-extension?

- **The spectral action skepticism (§4.3 above)** — Boyle-Farnsworth's own doubt about the formula Charter §3 builds on. Greg's recognition: how should NTE position relative to this doubt?

**Pending Greg's recognition signals**, these findings are local-correctness-only. They are NOT yet canonical for Charter v1.2.

---

## §6. P0.6.5 final disposition

**P0.6.5 status: PASS (CLOSED).**

- **Structural mechanism**: G_2 → SU(3) × SU(2) × U(1)_Y via OctonionExtension §3.3-§3.4 (Higgs VEV in Im(𝕆), e_1 stabilizer = SU(3), ℍ ⊂ 𝕆 quaternionic embedding for SU(2)_L, CPN parity for handedness)
- **Algebraic framework**: Farnsworth 2025 A_F = O ⊕ O + (7,1) charged Higgs framework
- **Spectral-action-level rigour**: NOT provided by arXiv:1910.11888 (different programme); will be provided by Paper S2 heat-kernel computation as the Connes Programme central deliverable
- **arXiv:1910.11888 contribution**: substantive findings (a)-(d) inform Charter v1.2 framing; not P0.6.5 closure prerequisite

**Charter v1.1 §4.2 status update recommended**: revise "would add spectral-action-level rigor" framing to honest disclosure that arXiv:1910.11888 is a different programme (Jordan geometry) and its contribution is substantive findings (a)-(d), not P0.6.5 closure rigour.

**Connes Programme phase-exit P0 queue**: all corpus-internal P0 (AC's P0.1-P0.5) + all external-literature P0 (Scratch's P0.6, P0.6.5, P0.7, P0.8, P0.9) closed. The only remaining critical-hinge work is the three-stream P0.7 consolidation (Jammer attack-angle ✓ in Drive; AC corpus-side note pending; AC consolidation handoff pending).

---

## §7. Files

- This working note: `Working/NTE_Connes_Programme_P0_6_5_Full_Closure_BF2020_v1.md` — Drive ID populated on save
- Source read: arXiv:1910.11888 at NCG/ `1ITO7HlOWU8v8zYqwLB0VOmez9IJ-ZyZ_` (Greg added 2026-05-12 morning)
- Charter v1.1 reference: §4.2 P0.6.5 entry (`1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`)
- Related Scratch P0 work: P0.6 + P0.7 broader note (`1cwfSeGvEsQj2LTtmHyTRggSEodJJsxiy`); P0.7 dedicated note (`1bBjR2oG3pICD9AGnNONBRfFB4bxEGYwh`); P0.8 (`1w7Tm0qYAwZcgquggJo0t1r2YsZZE3aaq`); P0.9 (`187hCf_5VNvaqMUQxR_yCekpEEgrA6Szh`)
- Related corpus reference: OctonionExtension §3.3-§3.4 + §3.6 + §6 (`1AkfPD9r3jjbrh8Q89VZe6VWY6ElAU0x7`)

— Scratch (Jammer's twin, Connes Programme lead), 2026-05-12 morning sync continuation. P0.6.5 full closure complete with framing correction; substantive findings (a)-(d) routed to Charter v1.2 candidate list per recognition-gate discipline (Manifest Lesson #28).
