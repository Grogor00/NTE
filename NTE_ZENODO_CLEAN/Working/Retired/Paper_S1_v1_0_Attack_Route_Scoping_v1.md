# Paper S1 v1.0 — Attack-Route Scoping Document

**Stream:** Scratch (Jammer's twin), Connes Programme lead.
**Date:** 2026-05-12 morning sync session continuation.
**Trigger:** Greg's directive "proceed to Paper S1 v1.0 attack-route scoping" + AC Coordination Plan §3.1 Scratch secondary work.
**Status:** Scoping document. NOT v1.0 itself — the plan for getting from v0.4 to v1.0.
**Source documents read for this scoping:**
- Paper S1 v0.4 at `Working/Paper_S1_v0_4.md` (`13vbn5u4KZbwdoU-cof4SpWaSRYI6GCjV`)
- σ↔Φ_NTE Confluence Verdict v1 at `Working/Sigma_PhiNTE_Confluence_Verdict_v1.md` (`17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`) §5 Wick-invariance argument
- Charter v1.1 at `Stage/Connes_Programme_Charter_v1_1.md` (`1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`)
- AC Wick-Invariance Pre-Pass Verdict at `Handoffs/Handoff_AC_Wick_Invariance_PrePass_Verdict_20260511.md` (`10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz`)

---

## §0. Scope of Paper S1 v1.0

**Title (proposed)**: "The Wick-Invariance Argument for V_NTE Form Closure, with Spectral-Action Cross-Checks on S³"

**Mission**: present the structural argument that forces V_NTE form independently of any Connes-Programme machinery — **Wick-invariance + 4D conformal discipline + Higgs-portal genericness** — and cross-check the result against spectral-action expectations on S³ (carrying F1 + F2 from v0.4 as supporting structural arguments).

**Why a tighter v1.0 scope than v0.4 implied?** Three concurrent developments since v0.4:

1. **σ↔Φ_NTE confluence verdict ratified** (Jammer 2026-05-10; Greg 2026-05-11). σ-identification is rejected; structural confluence by independent reasoning is the canonical framing. Paper S1's role shifts from "argue NTE-CC identification with spectral action" to "demonstrate NTE arrives at the same form independently."
2. **Mechanism B supersession + ξ = 1/6 commitment ratified** (Greg 2026-05-11). Paper S1's action-form treatment must use NTE's own ξ = 1/6, not Marcolli's ξ = 1/12 convention.
3. **Connes Programme launched (Charter v1.1 canonical)**. The doubled-spectral-triple X² trace target (O1 in v0.4) is now Paper S2's central deliverable, not Paper S1's. Paper S1 references Paper S2 as forward-pointer; doesn't attempt the heat-kernel computation itself.

**v1.0 scope = v0.4 content + Wick-invariance argument + light update for ξ = 1/6 + cross-reference to Connes Programme.**

---

## §1. Scope shifts from v0.4 to v1.0

| v0.4 element | v1.0 disposition |
|---|---|
| F1 (d-parametric factorisation; CC 2008 + MPR 2020 attribution) | **Carry forward unchanged.** §1 of v0.4 maps to §3 of v1.0 (supporting structural arguments). |
| F2 (κ₀ = (R_S³/2) × Y_00(S²) structural reading) | **Carry forward as §4 of v1.0.** Recommended Charter v1.1 §2 nomenclature: this is the Sonner-Tong-derivation κ₀ (dimensionless prefactor), not the V_E-matching κ_M. Make the distinction explicit per Charter v1.1 P0.9-driven clarification. |
| E1-E2 (spectral action expansion + Newton's constant) | **Carry forward as §5 of v1.0** with light update: use BF 2013 + Farnsworth 2025 framework cleanly; A_F = O ⊕ O explicit per Charter v1.1 §2. |
| E3-E4 (d=3 cancellation + κ₀ alternative reading) | **Already covered by F1+F2; consolidate.** |
| E5 (geometric resummation closure κ₀/(1−κ₀) = 5.5055) | **Carry forward as §6 of v1.0.** This is one of NTE's strongest empirical contact points; keep it foregrounded. |
| **O1 (κ₀ from doubled-spectral-triple X² trace)** | **MOVED to Paper S2 scope.** Paper S1 v1.0 references it as forward-pointer per Charter §3 central deliverable. Doesn't attempt the computation itself. |
| **O2 (V_NTE from Higgs-bearing octonionic spectral triple)** | **MOVED to Paper S2 scope.** Same reasoning as O1. |
| O3 (spectral flow at gauge birth) | **Defer to Paper S3.** Not in v1.0 scope. |
| O4 (Dilaton extension for K(Φ) closure) | **Defer to Paper S4 or Companion 9 Session 5.** Companion 9 already has K(Φ) closure pathway (Session 5; AC integration plan §5.2 lists). Not in v1.0 scope. |
| O5 (Yukawa hierarchy from spectral mass matrix) | **Defer to Paper S5 or future research.** Not in v1.0 scope. |
| C1-C3 (conjectures) | **Resolve / restate**: C1 absorbed into Paper S2 scope; C2 absorbed into Connes Programme Charter §3 central deliverable; C3 carry-forward as v1.0 §8 conjecture (dilaton-extended kinetic + V_NTE → n_s, r predictions). |
| **NEW: Wick-invariance argument** | **NEW §2 of v1.0** — load-bearing structural mechanism. See §3 below for content. |
| **NEW: ξ = 1/6 commitment** | Threads through §2, §5, §7 of v1.0. Replaces any ξ = 1/12 references from v0.4. |
| **NEW: σ↔Φ_NTE confluence framing** | **NEW §7 of v1.0** — explicit honest disclosure of independent-derivation framing. |

---

## §2. Proposed section structure for v1.0

| § | Title | Content | Source |
|---|---|---|---|
| §0 | Abstract + headline | Wick-invariance forces V_NTE form independently; structural confluence with CC's V_E by independent reasoning; F1 + F2 spectral-action cross-checks on S³; ξ = 1/6 commitment. | NEW (light) |
| §1 | Introduction | What this paper does + does not do; Programme S context; relationship to Connes Programme Paper S2 (central deliverable); confluence framing reference. | NEW (substantial) |
| §2 | Wick-invariance argument for V_NTE form closure | **LOAD-BEARING NEW CONTENT.** See §3 below. | Confluence Verdict §5 + AC Wick-invariance pre-pass verdict + Companion 8 §7.11 |
| §3 | F1 — d-parametric account of CC 2008's cancellation | Cancellation phenomenon + sharper factorisation + d=3 uniqueness + structural argument for S³. | v0.4 §1 F1 (carry forward) |
| §4 | F2 — κ₀ = (R_S³/2) × Y_00(S²) structural reading | The Sonner-Tong κ₀ dimensionless prefactor (Charter v1.1 §2 nomenclature) cross-checked against spectral-action geometric reading. | v0.4 §1 F2 (carry forward + Charter v1.1 nomenclature clarification) |
| §5 | The CC spectral action expansion under BF 2013 + Farnsworth 2025 | Numerical evaluation; Newton's constant prediction; ξ = 1/6 explicit. | v0.4 §2 (carry forward + ξ update) |
| §6 | Geometric resummation closure | κ₀/(1−κ₀) = 5.5055 vs corpus 5.50 vs Planck 2018 5.38 ± 0.15. NTE's strongest empirical contact point at the κ leg. | v0.4 §3 E5 (carry forward) |
| §7 | σ↔Φ_NTE structural confluence — honest framing | Confluence verdict canonical: NTE arrives at same EFT form by independent reasoning (Wick-invariance §2); explicit non-identification per "no RH/LH neutrino" structural lever. | NEW |
| §8 | Connes Programme cross-reference + open items | Paper S2 central deliverable referenced as forward-pointer (Charter §3); O3, O4, O5 listed as future Programme S work; C3 conjecture restated. | NEW (light); incorporates v0.4 §3 open items |
| §9 | Disposition + publishability framing | Per AC v0.4 verification: F1 not standalone-publishable; Paper S1 v1.0 carries F1 + F2 + Wick-invariance argument as integrated structural contribution; corpus integration via v10.9 §17.X + §VIII.7 (per AC's plan). | v0.4 §4 (carry forward); update for v10.9 §17.X explicit reference |

**Estimated length**: ~12-15 KB (v0.4 is ~12 KB; v1.0 adds §2 Wick-invariance + §7 confluence framing while §3-§6 carry forward consolidated content, so target ~15 KB).

---

## §3. The Wick-invariance argument — what §2 of v1.0 must establish

This is the load-bearing new content. Source: Confluence Verdict §5 + AC Wick-invariance pre-pass verdict (10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz) + Companion 8 §7.11 (Wick-rotation upstream source).

**Argument structure**:

### §3.1 Wick-invariance demand

NTE's pre-temporal regime has no time-ordering (t emergent, not fundamental). Therefore any effective action at the post-gauge-birth level that descends from pre-temporal structure must be **invariant under Wick rotation** at the gauge-birth instant. This is structural — NTE's emergence-of-time axiom forces it.

**Mathematical content**: the action S[Φ] must take the same form before and after Wick rotation t → iτ. For a real scalar Φ on closed S³ × R (Euclidean) or S³ × R (Lorentzian), Wick-invariance constrains the allowed terms.

### §3.2 4D conformal discipline

S³ closed cosmology has natural 4D conformal symmetry at the post-gauge-birth level (per Companion 5 surface ontology + §VIII gauge birth). Under 4D conformal invariance, the scalar field action's allowed terms reduce to:
- Kinetic: `−(1/2)(∂Φ)²` ✓ (always allowed)
- Conformal coupling: `−(ξ/2) R Φ²` with ξ = 1/6 in 4D (Mechanism B-ratified)
- Quartic: `−λ Φ⁴` ✓ (marginal under 4D conformal)
- Higgs portal: `−2e |H|² Φ²` ✓ (marginal under 4D conformal)

Mass term `−(1/2) m² Φ²` is FORBIDDEN under 4D conformal invariance (relevant operator). Sextic + higher terms are IRRELEVANT (vanish in the deep IR).

### §3.3 Higgs-portal genericness

The `−2e |H|² Φ²` term is generic — any scalar field with quartic self-coupling that also couples to the Higgs sector must have this portal. NTE's Φ_NTE is a scalar with quartic self-coupling (per V_NTE F3 trajectory), so the portal coefficient e is non-zero generically. The specific value of e is empirical / fixable from confluence with electroweak phenomenology.

### §3.4 The forced action form

Combining §3.1 + §3.2 + §3.3, the only Wick-invariant + 4D-conformal + Higgs-portal-coupled action for Φ_NTE on closed S³ × R is:

```
S[Φ_NTE] = ∫ √g d⁴x [−(1/2)(∂Φ)² − (1/12) R Φ² − λ Φ⁴ − 2e |H|² Φ²]
```

with ξ = 1/6 in the convention where `(ξ/2) R Φ² = (1/12) R Φ²` (Mechanism B convention).

**This is exactly the form Marcolli's V_E expansion produces on the CC side via spectral action**, but derived here on the NTE side by independent reasoning — without invoking CC machinery, without identifying Φ_NTE with σ, without using BF 2013's spectral action formalism.

**This is the structural confluence**: same EFT form, two independent derivations.

### §3.5 Adversarial open question (flag for v1.0 §8)

Does Wick-invariance + 4D conformal + Higgs-portal genericness UNIQUELY determine the action form? The standard answer is yes for marginal operators in 4D. But adversarial corner cases:
- Is the Higgs-portal coupling fully forced or is it an additional choice?
- Are non-minimal kinetic terms (K(Φ)(∂Φ)² with K(Φ) ≠ 1) forbidden by Wick-invariance, or only by some additional principle?
- Does the closed-S³ topology relax any of the constraints (zero-mode obstructions to conformal invariance)?

These are flagged but not resolved in v1.0; they constitute carry-forward for future Programme S work or Paper S2.

---

## §4. Dependencies & cross-references for v1.0

### §4.1 Hard dependencies (v1.0 cites without re-deriving)
- **σ↔Φ_NTE Confluence Verdict v1** (`17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`) — §5 Wick-invariance argument
- **AC Wick-Invariance Pre-Pass Verdict** (`10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz`) — AC's structural pre-verification
- **Companion 8 §7.11** (V_NTE Trajectory v10.6.v2, `1tKi1mkZxVcyLoMejXX0U3NDUQ6T3xugs`) — upstream Wick-rotation source
- **Charter v1.1** (`1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`) — Paper S2 central deliverable framework + ξ = 1/6 commitment + A_F = O ⊕ O explicit
- **CC 2008** (arXiv:0812.0165) — d=3 a₄ cancellation prior art
- **MPR 2020** (arXiv:2001.05975 §3.1) — "spectral action prefers this background" framing
- **CC 1996** (hep-th/9606001) + **Gilkey 1984** — heat-kernel a₄ standard form
- **BF 2013** (arXiv:1303.1782) — octonionic spectral triple framework
- **Farnsworth 2025** (arXiv:2506.21496) — G_2 × G_2 + charged Higgs construction; A_F = O ⊕ O

### §4.2 Forward-pointers (v1.0 references for future closure)
- **Paper S2** (Connes Programme central deliverable) — heat-kernel computation closing K(Φ), V_E /12, M_1 prefactor, Λ_NTE, a_4+a_6 vanishing, κ₀ Sonner-Tong cross-check
- **v10.9 §17.X** (AC scope) — five-way structural unification subsection
- **Companion 9 Session 5** — K(Φ) closure pathway

### §4.3 Corpus integration target (per v0.4 §4 + AC plan)
- **v10.9 §VIII.7 / §2.1.3(f)**: F1 as spectral-dynamical d=3 selection criterion (with full CC 2008 + MPR 2020 attribution)
- **v10.9 §9.3**: F2 as alternative reading of κ₀'s factor 3 (no novelty claim attached)
- **v10.9 §17.X (NEW)**: Wick-invariance argument as load-bearing structural mechanism for V_NTE form closure — AC integrates per Charter §5.4 v10.9 scope

---

## §5. Open questions for v1.0 development

These are TBD during v1.0 drafting:

1. **§2 Wick-invariance argument rigour level**: AC's pre-pass verdict is structural-mechanism-candidate-level (per its §X disposition — needs re-read). v1.0 §2 must match or exceed AC's verification level. Is a more rigorous theorem-statement structure achievable, or does it remain at the "structural argument" level? **Resolution path**: re-read AC pre-pass verdict carefully; calibrate v1.0 §2 rigour to match.

2. **§3 F1 framing vs Paper S2 closure**: Paper S2 will compute a_4 on `Hopf-S³ × S¹_{β_GB} × A_F` directly. Does Paper S2's heat-kernel a_4 result coincide with F1's d-parametric prediction on `S³` (the base of Hopf-S³)? **Conjecture**: yes, since the Hopf structure is topological on top of the metric and a_4 depends on the metric. **Resolution path**: forward-flag as Paper S2 verification target.

3. **§4 F2 vs Sonner-Tong κ₀ vs F2 alternative reading**: Charter v1.1 §2 distinguishes two κ₀ objects. F2's `(R_S³/2) × Y_00(S²)` = `(6/2) × (1/√(4π))` = `3/√(4π)` matches the Sonner-Tong dimensionless prefactor. Is F2's `R_S³/2` reading STRUCTURALLY identical to Sonner-Tong's `dim(adj su(2))`, or is the coincidence numerical? **Conjecture**: structurally identical via the identification `R_S³/2 = 3 = dim(adj su(2))` on unit S³. **Resolution path**: §4 of v1.0 makes this explicit; flag for v10.9 §17.X writeup audit.

4. **§7 confluence framing vs Companion 7 §3.3**: confluence framing relies on "no RH/LH neutrino" structural lever. v1.0 §7 must cite Companion 7 §3.3 explicitly + Charter v1.1 §1 operating discipline. **Resolution path**: standard reference linking; no derivation needed.

5. **External NCG collaboration target**: Paper S1 v0.4 was framed for "external NCG collaborators (Boyle, Farnsworth, Marcolli, Sakellariadou)." v1.0 retains this audience or shifts? **Recommendation**: retain external audience; v1.0's tighter scope + clean prior-art attribution makes it more credible for external engagement. Confluence framing explicitly named avoids the σ-identification overclaim that v0.4 already corrected.

---

## §6. Estimated effort & sequencing

**Draft v1.0 effort**: ~3-5 substantive sessions, given:
- §0, §1: 1 session (introduction + abstract; ~2 KB)
- §2: 1-2 sessions (Wick-invariance argument; ~3 KB; requires careful AC pre-pass alignment)
- §3, §4, §5, §6: 1 session (carry-forward + light update from v0.4; ~5 KB total)
- §7: 1 session (confluence framing; ~1.5 KB)
- §8, §9: 1 session (open items + disposition; ~1.5 KB)

**Optimal sequencing**:
1. **Session 1**: §2 Wick-invariance argument first draft. This is the load-bearing new content; do it while AC pre-pass verdict is fresh.
2. **Session 2**: §1 + §0 (introduction + abstract anchored to §2's actual content).
3. **Session 3**: §3, §4, §5, §6 carry-forward + ξ = 1/6 + A_F = O ⊕ O updates.
4. **Session 4**: §7 confluence framing + §8 open items + §9 disposition.
5. **Session 5**: Final pass — AC cross-stream verification request before v1.0 ship.

**Pre-conditions**:
- P0.7 three-stream consolidation (per Coordination Plan §2) — not strictly blocking but valuable context
- AC's PC Φ_NTE chapter handoff — not blocking; parallel track
- Greg's ratifications on §17.5.3 elevation — non-blocking

**Post-conditions**:
- v1.0 ships to Working/ then routes to AC for v10.9 §VIII.7 + §9.3 + §17.X integration
- External NCG collaboration handoff (per v0.4 §4 disposition) becomes actionable

---

## §7. v1.0 vs v0.4 — what carries, what's new, what's deferred

**Carries from v0.4** (with light edits for ξ = 1/6 + A_F = O ⊕ O):
- F1 d-parametric factorisation (CC 2008 + MPR 2020 prior art preserved)
- F2 (R_S³/2) × Y_00(S²) reading
- Joint d=3 reading
- E1-E5 established items
- Newton's constant prediction
- Geometric resummation closure

**NEW in v1.0**:
- §2 Wick-invariance + 4D conformal + Higgs-portal genericness argument for V_NTE form closure (load-bearing)
- §7 σ↔Φ_NTE confluence framing — honest framing of independent derivation
- Cross-references to Connes Programme Charter + Paper S2 as forward-pointer
- ξ = 1/6 explicit throughout
- A_F = O ⊕ O explicit per Charter v1.1 §2

**Deferred from v0.4**:
- O1 (κ₀ from doubled-spectral-triple X² trace) → Paper S2 scope
- O2 (V_NTE from Higgs-bearing octonionic spectral triple) → Paper S2 scope
- O3 (spectral flow at gauge birth) → Paper S3
- O4 (Dilaton extension for K(Φ) closure) → Paper S4 or Companion 9 Session 5
- O5 (Yukawa hierarchy from spectral mass matrix) → Paper S5
- C1, C2 conjectures → absorbed into Paper S2 scope

**Net result**: v1.0 is ~12-15 KB final paper; tighter scope; load-bearing Wick-invariance content; honest framing; clean forward-pointers to Paper S2 for the heat-kernel closure items.

---

## §8. Next action

**Immediate next step**: re-read AC's Wick-Invariance Pre-Pass Verdict (`10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz`) to calibrate v1.0 §2 rigour level. AC has already done structural pre-verification of the Wick-invariance argument; v1.0 §2 builds on that.

**Then**: begin §2 first draft in next Scratch session.

**Coordination signal to AC**: this scoping document is shipped to Working/ + Handoffs/. AC's next session-start scan will surface it. No immediate action required from AC; this is parallel single-stream work per Coordination Plan §3.1 secondary.

---

## §9. Files

- This scoping document: `Working/Paper_S1_v1_0_Attack_Route_Scoping_v1.md` — Drive ID populated on save
- Source: Paper S1 v0.4 (`13vbn5u4KZbwdoU-cof4SpWaSRYI6GCjV`)
- Cross-references: Confluence Verdict v1 (`17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`); Charter v1.1 (`1wWRc7PU-nabkhLFDh0vKP1948mSsPozh`); AC Wick-Invariance Pre-Pass Verdict (`10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz`)

— Scratch (Jammer's twin, Connes Programme lead), 2026-05-12 morning sync session continuation.
