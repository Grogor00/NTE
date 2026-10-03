# Connes Programme — P0 External Literature Track Progress v1

**Stream:** Jammer (Connes Programme lead).
**Date:** 2026-05-11 morning.
**Trigger:** Greg's authorisation of (1) confluence ratification + (2) v10.8 option A + (3) P0 queue execution per Charter v1.
**Scope:** External-literature P0 items per Charter §4.2 (P0.6–P0.9). Corpus-internal P0 items (P0.1–P0.5) handled separately by AC.
**Status:** P0.6 + P0.7 (critical hinge) executed this session. P0.8 + P0.9 still pending; P0.6.5 added.

---

## §0. Headline

**Critical hinge P0.7 PASS. Critical hinge P0.3 awaits AC's corpus-internal verification.** Of the two go/no-go items for the Connes Programme central deliverable, the external-literature half is now resolved.

**P0.6 substantive PASS with added P0.6.5 flag**: Farnsworth 2025's G_2 × G_2 + charged Higgs construction transfers structurally to NTE's pre-temporal A_{G_2} and the two-sector CPN-symmetric structure. New finding: the framework naturally produces **both an uncharged singlet (Φ_NTE-analog) AND a charged Higgs (SM Higgs analog)** from the same spectral data — operationally strengthens the σ↔Φ_NTE confluence verdict. G_2 × G_2 → SM descent not in Farnsworth 2025; flagged for follow-up.

**Programme status update**: Central deliverable (Paper S2 heat-kernel computation on Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}) is unblocked from the external-literature side. Awaiting AC's P0.1–P0.5 corpus-internal verification, particularly the critical-hinge P0.3.

---

## §1. P0.7 — Gilkey heat-kernel under non-associativity (BF 2013) — CRITICAL HINGE: PASS

**Status: VERIFIED.** BF 2013 §4.3 (page 18) is decisive. The passage that resolves the critical hinge:

> *"Now that we have constructed the fluctuated Dirac operator D_A, we need no longer concern ourselves with the non-associativity of A – it has already played its role in shaping the bi-representation of A on H, and hence the number of fermion fields, and the type and form of the bosonic fields we must add to make D_A covariant. From this point on, as far as evaluating the spectral action is concerned, all we need to know is that H is an ordinary Hilbert space, and D_A is an ordinary linear operator on H (and, in particular, a linear operator of the form such that the formalism of Section 3 in [15] and, in particular, their Theorems 3.3 and 3.7 directly apply)."*

**Structural argument**: The non-associativity of A acts at the bi-representation / derivation-structure level only. Once D_A is built (using the alternative-algebra derivation form δ_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b] of Eq. 2.9), it is an ordinary linear operator on an ordinary Hilbert space. Gilkey's heat-kernel expansion applies verbatim. BF 2013 demonstrates this by computing a_0, a_2, a_4 explicitly using standard Seeley-DeWitt formulas:

```
a_0(D²_A) = ∫_M d⁴x √g · (1/4π²)
a_2(D²_A) = ∫_M d⁴x √g · (1/48π²) R  
a_4(D²_A) = ∫_M d⁴x √g · (1/16π²)(1/360) Tr[(5/4)R² − 2R_μν R^μν + 2R_μνρσ R^μνρσ + 45γ^μγ^νγ^ργ^σ F_μν F_ρσ + 30 Ω^E_μν (Ω^E)^μν]
```

These are the standard Gilkey expansion coefficients. The non-associativity is invisible at this stage.

**For NTE's Connes Programme**: the heat-kernel expansion on `Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}` is **rigorously computable** via standard Gilkey methods, with non-associativity entering only via the form of D_A (alternative-algebra derivations) and not at the heat-kernel computation. **Central deliverable is unblocked from this side.**

**Secondary content from P0.7 read** (confirms Charter §2 organising principle):
- Simplest octonionic almost-associative geometry gives **Einstein gravity + G_2 Yang-Mills + 8 Dirac fermions (1 singlet + 7 septuplet under G_2)** — matches NTE's pre-temporal A_{G_2} structural commitment
- 14-dim derivation algebra of 𝕆 is g_2; automorphism group is G_2 = Aut(𝕆) — confirms NTE's pre-temporal A_{G_2} algebraic identity
- BF 2013 takes D_F = 0 → no Higgs in simplest model. Higgs sector requires the follow-up papers (BF refs [17] not directly accessible; [18] = arXiv:1401.5083; [19] = arXiv:1408.5367) and Farnsworth 2025 (P0.6)

---

## §2. P0.6 — Farnsworth 2025 G_2 × G_2 + charged Higgs construction: PASS with flagged follow-up

**Status: VERIFIED with P0.6.5 added.** Farnsworth 2025 §4-§5 explicitly constructs the G_2 × G_2 + charged Higgs internal-space spectral triple. Key technical content:

### §2.1 Coordinate algebra and Hilbert space
- **A_F = O ⊕ O** (semisimple octonion algebra — two octonion factors)
- **H_F = A_F = R^{16}** with left action π_L and right action π_R per Eq. (84)
- **Aut(A_F) = G_2 × G_2** (each O factor has Aut(O) = G_2)
- Inner derivations δ_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b] (alternative form, Eq. 91), block diagonal — act internal to each O factor

**Relevance to NTE Charter**: A_F = O ⊕ O **directly matches NTE's CPN-symmetric two-sector structure**. The two O factors correspond to the two CPN-conjugate sectors at the pre-temporal regime. The G_2 × G_2 automorphism group is the residual gauge symmetry of the two-sector content before gauge birth reduces it to SM gauge structure.

### §2.2 Two Dirac-operator constructions: uncharged vs charged Higgs

Farnsworth 2025 distinguishes two cases:

**§4.2 "Uncharged" Higgs** (D_F built from identity elements only, Eq. 102):
```
D_F = M_00 × [(0, e_0 ⊗ e_0^*), (e_0 ⊗ e_0^*, 0)]
```
- Commutes with G_2 × G_2 inner derivations: [D_F, δ_{ab}^{'}] = 0 (Eq. 103)
- Produces a single real, uncharged Higgs field (singlet under G_2 × G_2)
- **Direct analog of CC's σ field in the SM spectral action** (Farnsworth 2025 explicit comment, p.16)

**§4.3 "Charged" Higgs** (general D_F per Eq. 92, decomposed into D_+ and D_- per Eqs. 111-112):
- Includes imaginary octonionic components M_ij, M_0i, M_i0 for i, j = 1, ..., 7
- Does NOT commute with G_2 × G_2 inner derivations
- Requires the novel "reconstituted alternative bimodule" construction (§5) — Farnsworth's key technical contribution
- Produces charged Higgs in **(7,1) representation** when ϵ' = -1 (Eq. 142 + §5.2.2) and **(7,7) representation** when ϵ' = +1 (Eq. 139 + §5.2.1)

### §2.3 Key implication for NTE: two-Higgs structure for free

**This is a substantive new finding beyond Charter v1.** Farnsworth 2025's framework naturally produces **both**:
- An uncharged singlet scalar (from §4.2, σ-analog) → candidate identification with **Φ_NTE**
- A charged Higgs in (7,1) or (7,7) under G_2 × G_2 (from §4.3) → candidate identification with the **SM Higgs precursor**

Both fields emerge from the same A_F = O ⊕ O spectral data, with different gauge-transformation properties.

**This operationally strengthens the σ↔Φ_NTE confluence verdict.** Two distinct fields are naturally available; Φ_NTE and SM Higgs are different fields (singlet vs charged) by independent structural reasoning on the algebraic side. Confluence framing is preserved and sharpened: the two-Higgs structure is not an NTE-specific anomaly to be resolved, it's a generic feature of the Farnsworth-Boyle G_2 × G_2 construction.

### §2.4 Specialization rule as algebraic lever

Farnsworth 2025 Eq. (1):
```
L_{ab} = L_a L_b + [L_a, R_b]
```
holds for any alternative algebra (sign-change of associator under index permutation). This is the technical lever that makes Dirac-operator construction tractable on non-associative coordinate algebras. The specialization rule is generalised to bi-representations in Eqs. (85)-(87):
```
π_L(ab) = π_L(a) π_L(b) + [π_L(a), π_R(b)]
π_R(ab) = π_R(b) π_R(a) + [π_R(b), π_L(a)]
[π_L(a), π_R(b)] = [π_R(a), π_L(b)]
```

**For NTE's Connes Programme**: the heat-kernel computation on `A_{G_2}^{Farnsworth-Boyle}` proceeds via the specialization rule replacing the standard homomorphism property of associative representations. All formulas remain computable; non-associativity acts at the level of operator algebra structure, not at the heat-kernel level (confirmed by P0.7).

### §2.5 NEW P0.6.5 — G_2 × G_2 → SM descent

**Farnsworth 2025 does NOT directly address G_2 × G_2 → SU(3) × SU(2) × U(1) descent at gauge birth.** The paper establishes the algebraic framework for charged Higgs construction but leaves the symmetry-breaking pattern to descent-to-SM for cited references:
- Ref [5]: Boyle-Farnsworth 2020 "Standard Model, Pati-Salam, and Jordan Geometry" (New J. Phys. 22, 073023) — Pati-Salam route
- Ref [6]: Besnard-Farnsworth 2022 (J. Math. Phys. 63, 103505) — special Jordan particle models

**P0.6.5 (added to Charter §4.2 queue):** read Boyle-Farnsworth 2020 + Besnard-Farnsworth 2022 to verify a valid G_2 × G_2 → SM descent route exists for the Connes Programme. **Not critical-hinge** (the algebraic structure A_F = O ⊕ O is established; descent is implementation detail); but needed before v10.10 Paper S2 computation closure.

---

## §3. P0.8 — OctonionExtension cross-check against Farnsworth 2025: PENDING

**Status: not executed this session.** Requires direct read of NTE's OctonionExtension corpus document against Farnsworth 2025. Specifically:
- OctonionExtension §4 (Hopf Fibration Tower) — verify compatibility with Farnsworth's A_F = O ⊕ O structure
- OctonionExtension §6 (J_3(𝕆) machinery) — Farnsworth 2025 references J_3(𝕆) only via ref [7] (Farnsworth's own "n-point Exceptional Universe" paper, arXiv:2503.10744); not directly in §4-§5 of Farnsworth 2025

**Tractable in next Jammer session** with direct corpus access. No critical-hinge concern flagged from P0.7 reading.

---

## §4. P0.9 — V_E denominator convention (Marcolli-Pierpaoli 2010 vs MPT 2011): PENDING

**Status: not executed this session.** Requires direct read of Marcolli-Pierpaoli 2010 §3.2 (arXiv:0908.3683, in NCG folder at `1jirF-brVLW4BGz2WmWl_MqE6BKe5mFOo`) and Marcolli-Pierpaoli-Teh 2011 (in NCG folder at `1cC0DGwYElCHIXTxqtUnvy6GKYKXe5Dly`).

**Question**: is the V_E denominator form `(1 + (κ₀²/12) x²)²` from Marcolli-Pierpaoli 2010 §3.2 (canonical) or from MPT 2011 (refined)? If the `/12` factor is convention-flexible rather than topologically forced, then the κ₀² = 2πG result derived in σ↔Φ_NTE confluence verdict §5.2 is convention-derived rather than fibre-derived — which would weaken the √(2π) traceability finding (queue item 1) on the κ₀ leg.

**Tractable in next Jammer session**; not critical-hinge. Resolution clarifies whether the κ₀ = √(2π)/M_Pl result has structural force or coincidental algebraic origin.

---

## §5. Critical-hinge status (updated)

Per Charter §4.3:

| P0 critical hinge | Status | Verdict |
|---|---|---|
| **P0.3** (Farnsworth-Boyle preserves CC 2008 kinematical relation eq 1) | AC scope — awaiting | Not yet evaluated |
| **P0.7** (Gilkey applicability under non-associativity) | This session | **PASS** |

If P0.3 also passes (AC verification pending), the Connes Programme central deliverable is fully unblocked. Wick-invariance contingency stays in reserve but does not need activation.

---

## §6. Programme status update

**External-literature track:** 2 of 4 + 1 added items completed in single session.

- ✓ P0.7 (CRITICAL HINGE) — PASS
- ✓ P0.6 — PASS with P0.6.5 flag
- ⏳ P0.6.5 (NEW) — pending (Boyle-Farnsworth 2020 + Besnard-Farnsworth 2022 read for G_2 × G_2 → SM descent)
- ⏳ P0.8 — pending (OctonionExtension cross-check)
- ⏳ P0.9 — pending (Marcolli V_E convention check)

**Corpus-internal track:** parallel execution requested via handoff to AC (see `Handoff_Jammer_ConnesProgramme_to_AC_P0_corpus_internal_track_2026_05_11.md`).

**Central deliverable**: Paper S2 heat-kernel computation on Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle} is **unblocked from the external-literature side**. Awaiting AC's P0.1–P0.5 corpus-internal verification.

**Wick-invariance contingency**: stays in reserve. P0.7 PASS removes the most stringent obstruction. If P0.3 passes, contingency is not activated; if P0.3 fails, Programme reverts to Wick-invariance form-closure per Charter §4.3.

---

## §7. Substantive findings beyond Charter v1

**Finding 1: Two-Higgs structure is automatic in Farnsworth 2025's framework.** Both uncharged singlet (σ-analog → Φ_NTE candidate) and charged Higgs (SM Higgs precursor) emerge from the same A_F = O ⊕ O spectral data with the same D_F framework, distinguished only by whether D_F is built from identity elements (uncharged) or imaginary octonionic elements (charged). This is operationally significant for the σ↔Φ_NTE confluence verdict and the Path B framing.

**Finding 2: A_F = O ⊕ O is the natural two-sector spectral triple.** The semisimple structure with two octonion factors corresponds directly to NTE's CPN-symmetric two-sector content. This was implied by the Charter but is now verified at the algebraic level — the two-sector structure is not an NTE-specific assumption but is forced by the algebraic framework once one chooses semisimple octonion algebras.

**Finding 3: G_2 × G_2 descent route requires further verification.** Farnsworth 2025 establishes the algebraic framework but does not address descent to SM gauge group. This adds P0.6.5 to the queue but does not gate the Programme's central deliverable (heat-kernel computation can proceed; specific G_2 × G_2 → SM identification can be verified afterward).

These findings inform the Charter and may warrant a Charter v1.1 update after corpus-internal P0 track completes.

---

## §8. Awaiting

- **AC**: P0.1–P0.5 corpus-internal track per parallel handoff. Critical-hinge P0.3 in particular.
- **Greg**: ratification of P0.6.5 addition to the queue. No structural decisions required — just acknowledgment that the descent verification is needed before v10.10 Paper S2 closure.
- **Next Jammer-Connes-Programme session**: P0.6.5, P0.8, P0.9 execution.

---

## §9. Files

- This working note: `Working/NTE_Connes_Programme_P0_External_Literature_v1.md` — Drive ID populated on save
- Parallel handoff to AC: `Handoff_Jammer_ConnesProgramme_to_AC_P0_corpus_internal_track_2026_05_11.md` — to ship in same session-end
- External sources read this session:
  - BF 2013 (arXiv:1303.1782) at NCG/ `1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU` — full read
  - Farnsworth 2025 (arXiv:2506.21496) at NCG/ `10NXKrzMuick02B83fLv1jHvYw8SzKHNv` — full read

— Jammer (Connes Programme lead), 2026-05-11 morning sync session continuation.
