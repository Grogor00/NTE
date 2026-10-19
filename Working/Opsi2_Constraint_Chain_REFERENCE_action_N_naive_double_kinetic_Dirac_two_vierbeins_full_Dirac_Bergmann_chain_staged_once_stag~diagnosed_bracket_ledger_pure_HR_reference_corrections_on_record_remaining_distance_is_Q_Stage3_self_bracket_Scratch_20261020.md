# CONSTRAINT-CHAIN REFERENCE — action (N): naive double-kinetic Dirac on two vierbeins (HR bimetric). The full Dirac–Bergmann chain written once, every object placed at its stage. Reference document, not a verdict.

**Author:** Scratch, per `Handoffs/Directive_AC_to_Scratch_Write_The_Constraint_Chain_Document_20261020.md`. **Date:** 2026-10-20.
**Register:** reference document. **No new computation** — where a bracket is uncomputed, the ledger says so; that is the document's value. No Core; no f; P04 unchanged.
**Purpose (Greg's two decisions):** (1) is the remaining bracket tractable → does Round 6 run? (2) is this worth continuing at all? The map is built to make the remaining distance visible, not to pre-empt either call.
**Convention:** objects named by content, not register label. "Placement" marked **[computed in <file>, <lane>]** or **[placement by chain structure — not independently recomputed]**.

---

## 0. The diagnosis this document exists to fix
Five rounds produced one durable result and a sequence of objects each of which looked terminal and was not. The physics was not the difficulty; **the target kept being mis-staged** — objects from different preservation equations were compared as if co-staged. Specifically (central finding, §3): **R_j lives in the C_SC self-bracket {C_SC, C_SC} (a pre-integration ∂δ covector coefficient, Stage 3); the D-matrix absorption channel L(Dn)^i ∂_i ð® lives in the secondary preservation {ð®, H} (a post-integration scalar lapse-equation, Stage 4).** The Round-4/5 question "does the Stage-4 D-matrix channel cancel the Stage-3 R_j" compared objects across two stages; Cursor's "scalar-vs-covector type mismatch" (R5 Kill 2) is the *symptom* of that cross-stage comparison, not an independent kill. The correctly-staged questions are in §3.

---

## 1. The chain, stage by stage (action N, with pure-HR reference in §4)

**Stage 0 — phase space.** Gravity: two triads/metrics (γ_g, π_g), (γ_f, π_f), on the symmetric-vielbein-condition (SVC) surface where f = eX, X = √(h_g⁻¹h_f), h_g = EᵀE. Lapses N_g, N_f; after the HR shift redefinition the independent multipliers are N_g, N_f, n^i. Matter: Grassmann (ψ, π_ψ), (ψ̄, π_{ψ̄}).

**Stage 1 — primary constraints.**
- **Gravitational primaries** (ADM lapse/shift momenta vanish). [standard]
- **Dirac primary, second class:** χ = π_ψ − (i/2)(√γ_g ψ̄γ^a e_a^{0} + √γ_f ψ̄γ^a f_a^{0}) ≈ 0, and χ̄. **χ depends on BOTH vierbeins** (the single π_ψ receives both kinetic terms). {χ, χ̄} ≠ 0 ⇒ second class ⇒ eliminated by Dirac brackets; this is also why H is lapse-linear (no p²/N term). [computed: lapse-linearity re-derived, Scratch R1/V1; χ-both-vierbeins, Scratch R2]

**Stage 2 — secondary constraints (preserve the gravitational primaries).**
- **Two super-Hamiltonian constraints** C_g = C_g^(grav) + C_g^(ψ) ≈ 0, C_f = C_f^(grav) + C_f^(ψ) ≈ 0 (lapse coefficients; matter pieces are the frame-specific Dirac energy densities). [placement by chain structure; matter pieces' ∂δ self/cross-weights computed — see ledger]
- **Total (diagonal) momentum constraint** C_i = C_i^(g,grav) + C_i^(f,grav) + p_i ≈ 0, p_i = ψ†∂_iψ frame-neutral. First class (generates the diagonal diffeo). [placement by structure]
- **HR split:** C_+ (first-class combination — overall time diffeo) and **C_SC** (the second-class combination, ≈ C_g − C_f at the ∂δ level, K1-forced equal weight — the direction whose preservation triggers the ghost-killing chain). [C_SC weight w=1 forced by K1: Scratch R3]
- **n^i is fixed here** by preservation of the momentum/shift sector: **n^i = n^i(γ, π)** (HR 1109.3515 eq 24) — phase-space-dependent, **NOT n(X)**. [source: Cursor R5 citing HR eq 24; this correction accepted — see §5]

**Stage 3 — the BD-killing secondary ð®.**
- Preserve C_SC: {C_SC, H} ≈ 0 ⇒ generates the secondary **ð®⁽⁰⁾ ≈ 0** (pure HR). With matter: **ð®^(ψ²) = ð®⁽⁰⁾ + ΔS_ultralocal** (ΔS ultralocal, bilinear in ψ). [ΔS ≢ 0 and ultralocal: S3 §4.4, reused as algebra not label]
- **The C_SC self-bracket {C_SC(x), C_SC(y)}** carries the ∂_jδ³(x−y) structure-function coefficient **R_j = h_g(I−X)² p_j** (covector density). This is where R_j lives. Whether {C_SC, C_SC} ≉ 0 (R_j not weakly zero) alters C_SC's class is the Stage-3 question. [R_j closed form: Scratch R3, verified]

**Stage 4 — preserve ð®.**
- {ð®^(ψ²), H} ≈ 0. **Pure HR: fixes the relative lapse N_f/N_g, no tertiary → BD mode removed, 7 dof.** Action (N): the open fork — fixes the lapse ratio (G-1), fixes a lapse / fails (G-2), or a tertiary (G-3).
- The **D-matrix/n^i multiplier term** (L D^i_j n^j)C_i in H enters here via {ð®^(ψ²), (LDn)C_i} = **L(Dn)^i ∂_i ð®^(ψ²)** — a scalar density (lapse-type equation). The gradient of the ultralocal matter secondary ∂_i(ΔS_ultralocal) is p-structured, so this channel is nonzero. [channel: Scratch R4; computed to fail to supply −R_j: Cursor R5 — but see the cross-stage caveat, §3]

---

## 2. Staging table — every round-1–5 object placed

| Object | Lives in (equation / stage) | Tensor type | Status / file / lane |
|---|---|---|---|
| **χ (Dirac primary, both vierbeins)** | Stage 1 primary | — | computed; `..._VERDICT_Scratch_lands_G4_...does_C_minus..._20261019` (R2) |
| **lapse-linearity (both lapses)** | Stage 1 consequence | scalar | computed; Scratch R1/V1 — **= Nelson–Teitelboim 1977 for single metric (not novel)** |
| **C_g^(ψ), C_f^(ψ) diagonal ∂δ weights h_g, h_f** | Stage 2, {C_g,C_g}/{C_f,C_f} | covector | computed (frame-matched, healthy); Scratch R1/V1 |
| **cross weight G = h_g X (= EᵀF)** | Stage 2, {C_g^(ψ),C_f^(ψ)} via Dirac bracket through χ | covector | computed; Scratch V1, re-verified R3, Jammer re-check |
| **R_j = h_g(I−X)² p_j** | **Stage 3, {C_SC,C_SC} ∂δ coefficient** | **covector** | computed closed form; Scratch R3 (= h_g+h_f−2G) |
| **θ-weighted residual h_g(θ_g I − θ_f X)²** | Stage 3, {C_SC,C_SC} with lapse weights | covector | Jammer generalization (R-stage); same stage as R_j |
| **(LDn)C_i term → L(Dn)^i ∂_i ð®** | **Stage 4, {ð®^(ψ²), H} channel** | **scalar** | channel identified Scratch R4; evaluated Cursor R5 |
| **R_i^(g) D^i_j n^j (grav momentum × D × n)** | Stage 4, {ð®^(ψ²), H} assembly | scalar | Cursor R4/R5 |
| **n^i = n^i(γ,π)** | Stage 2 (fixes shift), HR eq 24 | — | source HR; **not n(X)** — corrects Scratch R4 framing (§5) |

**The cross-stage error, exactly:** R_j (covector, Stage 3, {C_SC,C_SC}) and the (LDn)∂ð® channel (scalar, Stage 4, {ð®,H}) are in **different preservation equations**. "Does the D-matrix channel cancel R_j" (Scratch R4 framing, Cursor R5 computation) is **cross-stage as literally posed.** R_j's effect *can* propagate into Stage 4 because ð® is generated from {C_SC, H} (so ð® carries C_SC data) — but that propagation is itself an **uncomputed bracket**; the rounds compared the two objects directly, as if co-staged, which they are not.

---

## 3. The correctly-staged questions (what Round 6 should target, if it runs)
Neither is resolved here — this is the map, not the verdict.
- **Q-Stage3 (the one the chain makes primary):** Is {C_SC(x), C_SC(y)} ≉ 0 via R_j = h_g(I−X)² p_j, and does that change C_SC's first/second-class status and hence the dof count — *independently of the Stage-4 D-matrix channel*? R_j ∝ total C_i (⇒ weakly zero, harmless) **only if** h_g(I−X)² ∝ identity, which is false for generic X≠I. So {C_SC,C_SC} is generically **not** weakly zero in the matter sector — but whether that removes a constraint (→ ghost, G-2) or is absorbed into the diffeo algebra is **uncomputed**.
- **Q-Stage4 (correctly posed):** In {ð®^(ψ²), H}, with n^i = n^i(γ,π) on-shell and ð® carrying the propagated C_SC data, does preservation fix the relative lapse (G-1) or a lapse (G-2)? This is the HR Stage-4 question *with matter*, and it is where the D-matrix channel legitimately lives — but it must be fed the Stage-3-propagated R_j, not compared to R_j directly.
**The mis-staging meant five rounds computed a hybrid of these two that is neither.** The remaining distance is one correctly-staged computation of Q-Stage3 (cleaner: it is a self-bracket, no D-matrix needed) and, if that doesn't settle the count, Q-Stage4.

---

## 4. Pure-HR reference column (K0′ as reference, generic n)
| Bracket | Pure-HR closure at generic n = n(γ,π) |
|---|---|
| {C_g, C_g}, {C_f, C_f} | close on the respective frame's momentum density (h_g, h_f weights); part of the diffeo algebra |
| {C_SC, C_SC} | carries ∂δ with grav coefficient (h_g−2G+h_f-type in the grav densities); **in pure HR this is handled by the potential + the C_SC/ð® second-class pair — NOT by being weakly zero** |
| {C_SC, H} | generates ð®⁽⁰⁾ (the BD secondary) |
| {ð®⁽⁰⁾, H} | **fixes N_f/N_g**; no tertiary; BD mode removed; 7 dof |
| n^i | = n^i(γ,π), HR eq 24 (minimal form closed-form; non-minimal β₂,β₃≠0 has no closed-form n) |
**Reference caveat:** pure HR's {C_SC,C_SC} ≠ 0 is *expected and healthy* (handled by the second-class pair). So "R_j makes {C_SC,C_SC}≠0" is **not by itself** a ghost signal (F12) — the matter question is whether R_j's contribution exceeds what the C_SC/ð® pair absorbs. That is Q-Stage3.

---

## 5. Corrections carried onto the record
- **R_j = h_g(I−X)² p_j** — a perfect square; **not h_g(I−X²)** (AC's conversational misstatement, corrected in the R3 ruling).
- **Residual is 3-dimensional**, not ≥6 (tr(S·B) sees only the symmetric part; the physical residual is the 3-component relative boost). My S3 ≥6 and AC's repeat are withdrawn.
- **φ₀ = 0 and n = 0 are special loci, not WLOG.** (Scratch F1; Cursor's R4 empty-locus G-2 withdrawn for using n=0 with P≠0.)
- **D2/D2′ labels are not premises** (regraded; Gate-0 W-3 reopened earlier).
- **The "90/90" statistic is struck** — not reproducible from Cursor's filed script/JSON (Cursor's own R5-read flagged it; restore-or-strike → struck here).
- **My "X-only polynomial identity" framing (Scratch R4) is WITHDRAWN** and recorded here, not left in a handoff: the preservation multiplier is **n^i = n^i(γ,π)** (HR eq 24), not n(X), so the absorption object is **not** a pure-X identity — it carries π-dependence R_j lacks. This both corrects my framing and is itself a Stage-wise fact (the π-dependence sits at Stage 2's n-fixing, not Stage 3's R_j).
- **n^i = n^i(γ,π)** is the on-shell multiplier throughout (Stage 2), per HR eq 24.

---

## 6. For Greg's two decisions (honest remaining-distance)
1. **Is the remaining bracket tractable?** The chain reframes the target from the cross-staged "D-matrix absorbs R_j" to **Q-Stage3: does R_j = h_g(I−X)² p_j make {C_SC,C_SC} fail to close beyond what the pure-HR C_SC/ð® second-class pair absorbs?** This is a **self-bracket** — it needs {C_SC,C_SC} at O(ψ²) and the pure-HR absorption reference (§4), **not** the full Stage-4 D-matrix preservation. That is strictly smaller than what Rounds 4–5 attempted. **Tractability: plausibly yes for Q-Stage3**; Q-Stage4 (if needed) remains a full ADM-with-spinors preservation with the known-but-nontrivial HR n(γ,π). Greg's call.
2. **Worth continuing?** Honest ledger: **one durable finding — single-metric Dirac lapse-linearity — is Nelson–Teitelboim 1977 (not novel).** The novel content is strictly the doubly-coupled answer (G-1 ghost-free, or G-2 ghost returns), which is **not yet established** (five rounds, no ratified terminal fork; Cursor's R5 G-2 is cross-staged and under Jammer attack). The remaining distance to a *novel, publishable* result is Q-Stage3 (one self-bracket). If Q-Stage3 is computed cleanly and lands, there is a result; if it too proves intractable at O(ψ²), **"the chain cannot be closed at O(ψ²) with current methods" is itself the honest terminal statement** and the most useful thing left to say.

---

## 7. Bracket ledger (computed / partial / not)
- {χ, χ̄}: computed (second class, lapse-linearity) — Scratch R1/V1. ✓
- {C_g^(ψ),C_g^(ψ)}, {C_f^(ψ),C_f^(ψ)} ∂δ (h_g, h_f): computed — Scratch V1. ✓
- {C_g^(ψ),C_f^(ψ)} ∂δ (G=h_g X): computed via Dirac bracket through χ — Scratch V1/R3, Jammer re-check. ✓
- {C_SC,C_SC} ∂δ matter coefficient (R_j = h_g(I−X)²p_j): computed closed form — Scratch R3. ✓ **(but its effect on C_SC class — Q-Stage3 — NOT computed.)**
- n^i = n^i(γ,π): sourced HR eq 24 (minimal). Non-minimal n: **not closed-form (not computed).**
- {ð®^(ψ²), H} full preservation with correctly-propagated R_j: **NOT computed.** (Cursor R5 computed the cross-staged channel-vs-R_j comparison; Scratch R4 identified the channel. The correctly-staged Stage-4 bracket is open.)
- {C_SC, H} → ð®^(ψ²) with matter: **partial** (ΔS_ultralocal established ultralocal, S3 §4.4; full generation not re-derived here).
- Pure-HR reference brackets (§4): known from HR literature (1109.3515, 1111.2070, 1203.5783); not independently recomputed this document.

---

**Status:** reference document complete; no new computation performed; all round-1–5 objects placed by stage; central cross-stage error diagnosed (R_j ∈ Stage-3 {C_SC,C_SC} vs the D-matrix channel ∈ Stage-4 {ð®,H}); corrected record folded in; remaining distance reduced to **Q-Stage3 (a self-bracket)** for Greg's tractability call. Cursor is computing in parallel (separate directive) — this is the reference, not merged with it.

— Scratch, 2026-10-20. Constraint-chain reference for action (N); staging table + bracket ledger + pure-HR reference + corrections; the correctly-staged next target is Q-Stage3 ({C_SC,C_SC} closure under R_j), strictly smaller than Rounds 4–5; novelty ledger honest (lapse-linearity = Nelson–Teitelboim 1977; doubly-coupled answer not yet established). Routed to AC → Greg.
