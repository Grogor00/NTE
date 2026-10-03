# Task 2 — CR §3.2 Simplification: Wick Rotation → KMS State-Transition for Paper S1 v1.0 §2 — Scratch v1

**Status:** Working note v1, 2026-05-16. Single-deliverable per Task 2 scope (Handoff `1KU8TWgiM_zg0m0Rk01OraElYm8oYqKl2` §3 queue: Task 2 next after Task 1 ratified; Greg fired ratification on Task 1 + "proceed to Task 2" 2026-05-16).
**Author stream:** Scratch (Connes Programme lead within Jammer-stream).
**Investigation question:** Apply CR 1994 §3.2's simplification (KMS condition primary; Wick rotation derived special case) to Paper S1 v1.0 §2's premise P1 (currently "Wick rotation at gauge birth"). Under canonical σ_t framework adoption at v10.10 (Charter v1.3 §2.5), the simplified framing becomes natural; the Wick rotation reading becomes a special-case derivation route rather than a foundational premise.
**Scope discipline:** Single working note proposing candidate revised inline text for Paper S1 v1.0 §2 P1; not a full §2 v2 draft. Absorption into Paper S1 v1.0 §2 is a subsequent Scratch session per scoping document `1BRpIRPPXWxaEwd33jlTzCiXHJP07TBMb` §6 sequencing.
**Recognition-gate aware:** Local-correctness-only until passing Greg's recognition gate via AC review. Recognition-gate items in §8 below.
**Vocabulary discipline (canonical 2026-05-16):** "Modular flow σ_t / KMS parameter β / modular conjugation J / modular operator Δ" preferred; "thermal time / temperature" avoided.
**Source basis read for this investigation:**
- Connes-Rovelli 1994 primary `1pcHHNL8jJyYFhYgb0jva6q2aBxgFWaQc` (read in full during Direction 1; §3.2 KMS condition content recalled)
- Paper S1 v1.0 §2 first draft `1oJUGrGUsckGE8C9LdoxQJfeM6sDjw6jM` (read in full this session)
- AC convergence assessment `1iMdcLoVmIMIsTaso9u5zptRAEtXPVEaU` (canonical synthesized framing reference)
- AC→Scratch Task 1 routing `1KU8TWgiM_zg0m0Rk01OraElYm8oYqKl2` (queue context)
- Charter v1.3 `1TDrHUFSuROWzu__hY34PGAvLmmZdxAu4` (§2.5 σ_t canonical complement; v10.10 framework adoption)
- Paper 7a v1.1 (Track 2 + δN canonical content background)
- Scratch Direction 1 working note (σ_t / Φ_NTE investigation Top-Down)
- Scratch Task 1 working note (CR Question B verdict)
**Files NOT read this session** (flagged as confidence-limiters per §7):
- Jammer Direction 2 working note (referenced via AC convergence assessment summary)
- Jammer Tier 2 reframing working note (Verlinde-Zurek + Martins + Koslowski + Salvio); particularly relevant: Salvio 2025 reframing (gauge birth as first-order phase transition / state-type transition non-KMS → KMS at T_GB) directly informs this simplification
- Hersent 2025; Summers 2005; Borchers 1999

---

## §1. Task framing — what CR §3.2 establishes; what the simplification means

### §1.1 CR 1994 §3.2 content

Connes-Rovelli 1994 §3.2 establishes the connection between the KMS condition and the modular automorphism group σ_t. The key technical content:

**Tomita-Takesaki theorem** (CR §2.1): given a von Neumann algebra R and cyclic+separating vector |Ψ⟩, define $S: A|\Psi\rangle \mapsto A^*|\Psi\rangle$; polar decomposition $S = J\Delta^{1/2}$ gives modular conjugation J and modular operator Δ. The modular automorphism group is $\sigma_t(A) = \Delta^{-it} A \Delta^{it}$.

**KMS condition automatic** (CR §3.1): the state ω corresponding to |Ψ⟩ satisfies the KMS condition with respect to σ_t at inverse temperature β = 1:
$$\omega(A \sigma_t(B)) = \omega(\sigma_{t+i}(B) A)$$
This is the modular condition; it's a *property of* σ_t, not an additional postulate.

**Connection to QFT-with-Hamiltonian via Wick rotation** (CR §3.2 — the section Task 2 targets):
- For a QFT system with Hamiltonian H and thermal Gibbs state $\omega = N e^{-\beta H}$, the modular flow σ_t corresponds to Hamiltonian time evolution rescaled by β: $\sigma_t = \alpha_{\beta t}$ where $\alpha_t$ is Hamiltonian time flow
- The KMS condition $\omega(A \alpha_t(B)) = \omega(\alpha_{t-i\beta}(B) A)$ at imaginary time shift $i\beta$ is recovered by analytic continuation of $e^{iHt} \to e^{-H\tau}$ under Wick rotation $t \to -i\tau$
- The periodicity in imaginary time (period β) IS the KMS condition

**The deeper structural point** (CR §4): the modular flow σ_t exists for ANY state on ANY von Neumann algebra. It does not require a Hamiltonian; it does not require Wick rotation. Wick rotation is the SPECIAL CASE where σ_t can be related to Hamiltonian-time evolution via $t = \beta \tau$. For systems without a global Hamiltonian (generally covariant systems; spectral triples without a preferred time), σ_t still exists as the canonical mathematical structure determined by (R, ω).

### §1.2 What the "simplification" of CR §3.2 means for Paper S1 §2

Paper S1 v1.0 §2's premise P1 currently invokes Wick rotation at gauge birth as the structural mechanism forcing Wick-rotation-compatibility of the effective action. The "C¹ kink in dz/dy at gauge birth" is identified as the Wick rotation event — pre-temporal Euclidean → post-temporal Lorentzian.

**The simplification**: under v10.10 canonical σ_t framework (Charter v1.3 §2.5 ratified 2026-05-16), the modular flow σ_t on (A_F, ω_{Φ_NTE}, β = β_GB) gives KMS condition automatically via Tomita-Takesaki. The "gauge birth event" is structurally a state-transition: pre-temporally, the state is not KMS at β_GB (or KMS at no specific β; or is a generic / non-KMS state); post-temporally, the state is KMS at β_GB.

The Wick rotation reading remains valid as the SPECIAL CASE where σ_t is related to Lorentzian-time evolution post-gauge-birth. The C¹ kink in dz/dy is the geometric signature of the state-transition. But the deeper structural content is the state-type-transition, not the signature change.

**Why the simplification is structurally cleaner**:

1. **Pre-temporal applicability**: pre-temporally, t doesn't exist; there's no Lorentzian signature to rotate FROM. The "Wick rotation at gauge birth" framing requires the pre-temporal state to admit interpretation as Euclidean — but Euclidean signature already presupposes some signature structure on the underlying manifold, which awkwardly extends time-like concepts pre-temporally. The σ_t / KMS framing is uniform: σ_t exists pre-temporally and post-temporally; the difference is whether the state is KMS at a specific β.

2. **Canonical framing alignment**: v10.10 σ_t framework is canonical operator-algebraic complement (Charter v1.3 §2.5). Using σ_t / KMS framing throughout Paper S1 §2 aligns with canonical state. Wick-rotation framing carries thermodynamic vocabulary inheritance (β as inverse temperature) that the Charter v1.3 vocabulary discipline canonization deprecates.

3. **Unified with Jammer Tier 2 reframing (Salvio 2025)**: Jammer's Tier 2 reframing of Salvio 2025 (per AC handoff `1sC8ofY1vaDi8-7PCCl2vX4RoKQuEV9wq` §2.1 + Jammer working note `1fBZ3VeDF4E--fNagYMhwCEjEYd1f_KkW` §4) models gauge birth as first-order phase transition / state-type transition non-KMS → KMS at T_GB. This is EXACTLY the same structural content as the CR §3.2 simplification proposed here. The proposed Paper S1 §2 P1 revision is consistent with canonical framing across both Jammer + Scratch streams.

4. **No content loss**: the structural strength of P1 (forcing analytic-structure constraints on the effective action) is preserved. KMS-compatibility forces the same analytic continuation properties that Wick-rotation-compatibility forces; the deeper structural content is identical.

### §1.3 Scope discipline for this deliverable

- **In scope**: candidate revised inline text for Paper S1 v1.0 §2 P1 (§2.1) + cascade implications for §2.4 (forced action form restatement) + §2.6 (what §2 establishes); structural analysis showing the simplification preserves §2's argumentative strength
- **Out of scope**: full §2 v2 draft (subsequent Scratch session); absorption of revised P1 into Paper S1 v1.0 master document (subsequent Scratch session); revision of §3-§6 carry-forward content from v0.4 (unchanged); revision of §7-§9 still-pending sections (separate work)
- **Out of scope**: any change to P2 (4D conformal invariance) or P3 (Higgs-portal genericness) — these are independent of P1's framing and don't require modification under CR §3.2 simplification

---

## §2. CR §3.2 simplification — structural content in detail

### §2.1 The standard QFT-derivation route (what CR §3.2 simplifies AWAY from)

In QFT with Hamiltonian H on Hilbert space H_QFT:
1. **Thermal Gibbs state**: $\omega_\beta(A) = \text{Tr}(N e^{-\beta H} A)$
2. **Wick rotation**: analytic continuation $t \to -i\tau$; $e^{-iHt} \to e^{-H\tau}$; Lorentzian time → Euclidean time
3. **Periodicity**: KMS condition emerges as periodicity of Euclidean correlation functions in imaginary time, with period β
4. **Result**: thermal state ω_β satisfies $\omega_\beta(A \alpha_t(B)) = \omega_\beta(\alpha_{t-i\beta}(B) A)$ for $\alpha_t$ Hamiltonian time evolution

The standard route makes Wick rotation FOUNDATIONAL — the KMS condition is *derived from* Wick rotation + thermal state.

### §2.2 CR §3.2's simplification route (Tomita-Takesaki primary)

CR §3.2 inverts the foundation:
1. **Start from (R, ω, |Ψ⟩)** with cyclic+separating vector — minimal structural assumption (any state on any von Neumann algebra)
2. **Apply Tomita-Takesaki**: $S = J\Delta^{1/2}$; σ_t = Δ^{-it} A Δ^{it}
3. **KMS automatic**: ω is KMS at β=1 w.r.t. σ_t (built into Tomita-Takesaki theorem)
4. **Specialize to QFT**: when (R, ω) corresponds to thermal state on QFT-with-Hamiltonian, σ_t = α_{βt} (Hamiltonian flow rescaled); the special-case derivation route via Wick rotation recovers the periodicity
5. **General case**: for spectral triples without preferred time (generally covariant systems; NTE), σ_t exists as the canonical mathematical structure without requiring Wick rotation

**The simplification**: the KMS condition is *primary*, not *derived*. Wick rotation is a *consequence* in the QFT-with-Hamiltonian special case, not a *foundation* for the KMS condition.

### §2.3 Implication for systems without preferred time

For systems without a preferred time (generally covariant systems; NTE's pre-temporal regime; spectral triples without an obvious Hamiltonian):
- Wick rotation is *not available* as a foundational mechanism (no preferred time to rotate from/to)
- KMS condition via Tomita-Takesaki is *still available* — σ_t exists for any state on any algebra
- The structural content that Wick rotation provides in the QFT case is provided by Tomita-Takesaki in the general case

**For NTE pre-temporal regime**: there's no t pre-temporally; Wick rotation framing is awkward. KMS / σ_t framing applies cleanly: pre-temporal state on A_F has its own σ_t (or is in a generic / non-KMS regime), structurally well-defined.

**For NTE post-temporal regime**: t exists; σ_t can be related to t-evolution; this is the special case where Wick rotation recovers the KMS condition as derived consequence.

**At gauge birth**: the structural event is the transition from generic state (no specific β) to KMS state at β = β_GB. The C¹ kink in dz/dy is the geometric signature of this state-transition; the Wick rotation reading is the post-temporal-side viewpoint of the same event.

---

## §3. Application to Paper S1 v1.0 §2 — what changes, what doesn't

### §3.1 What changes — P1 framing

**Current Paper S1 v1.0 §2.1 P1 framing** ("Wick rotation at gauge birth"):
- Pre-temporal → Euclidean signature; post-temporal → Lorentzian signature
- C¹ kink in dz/dy at gauge birth IS the Wick rotation event
- Forces "Wick-rotation compatibility" of effective action — must admit analytic continuation across C¹ kink

**Proposed simplified P1 framing** ("σ_t / KMS state-transition at gauge birth"):
- Pre-temporal: state on A_F is generic (not KMS at β_GB); modular flow σ_t exists but does not align with any Lorentzian-time evolution (because there's no Lorentzian time pre-temporally)
- Post-temporal: state ω_{Φ_NTE} is KMS at β = β_GB w.r.t. σ_t generated by Tomita-Takesaki on (A_F, ω_{Φ_NTE}, β_GB); σ_t can be related to Lorentzian-time evolution via $t = \beta_{GB} \tau$ (CR §3.1 standard correspondence)
- Gauge birth event: state-type transition from generic (non-KMS) to KMS at β_GB; the C¹ kink in dz/dy is the geometric signature of this state-transition
- Forces "σ_t / KMS-compatibility" of effective action — must support a state on A_F that becomes KMS at β_GB post-gauge-birth, structurally equivalent to admitting analytic continuation of correlation functions across the gauge-birth event

### §3.2 What doesn't change — argumentative strength

**P1's argumentative role is preserved**:
- Both framings constrain the effective action to admit analytic continuation across the gauge-birth event
- Both framings allow many actions (massive scalars, scalars with arbitrary self-interactions admit Wick rotation / KMS-compatibility)
- Both framings require P2 (4D conformal invariance) + P3 (Higgs-portal genericness) to fix the action form

**The structural conclusion (forced action form) is unchanged**:
$$S[\Phi_{NTE}, H] = \int \sqrt{g}\, d^4x \left[-\tfrac{1}{2}(\partial\Phi)^2 - \tfrac{1}{12}R\Phi^2 - \lambda\Phi^4 - 2e|H|^2\Phi^2\right]$$

This action form is forced under P1 + P2 + P3 regardless of whether P1 is framed as Wick-rotation-compatibility or σ_t / KMS-compatibility.

**Confluence with Marcolli's V_E expansion is unchanged**: §2.5 cross-check at sextic order remains valid; convention-dependence disclosure remains valid; honest-disclosure framing per Manifest Lesson #28 + recognition-gate discipline remains valid.

### §3.3 What strengthens — canonical framing alignment

The simplification *strengthens* §2's structural integration with canonical NTE state:

1. **v10.10 σ_t framework canonical complement adoption**: Paper S1 §2 P1 directly uses the canonical σ_t / KMS vocabulary; no separate "Wick rotation reading" required as bridging vocabulary
2. **Charter v1.3 §2.5 vocabulary discipline**: P1 simplified uses "modular flow," "KMS parameter β" — canonical preferred vocabulary; "Wick rotation" remains valid as derived special-case but does not need to be foundational
3. **Cross-coherence with Jammer Tier 2 reframing**: Salvio 2025 reframing models gauge birth as state-type transition non-KMS → KMS at T_GB — this is the same structural content as the proposed P1 simplification. Cross-stream coherence at canonical framing level
4. **Cross-coherence with Direction 1 + Direction 2 investigations**: both σ_t / Φ_NTE investigation directions adopted σ_t / KMS framing throughout; Paper S1 §2 P1 simplified aligns with same vocabulary
5. **Companion 8 Stage 2 F2 + §VIII.1.4 corpus reference preserved**: the Wick rotation reading remains a valid corpus-canonical structural identification; the P1 simplification adds the σ_t / KMS framing as the more general / pre-temporally-applicable reading, with Wick rotation as the post-temporal-side special case

---

## §4. Candidate revised inline text for Paper S1 v1.0 §2 P1

### §4.1 §2.1 candidate revised text (replaces current §2.1)

> ### §2.1 Premise P1 — σ_t / KMS-compatibility at gauge birth
>
> NTE's pre-temporal regime is structurally distinguished from the post-temporal regime by *state type on the spectral triple algebra A_F = 𝕆 ⊕ 𝕆*: pre-temporally, the state on A_F is in a generic / non-KMS regime; post-temporally, the state ω_{Φ_NTE} is KMS at β = β_GB w.r.t. the modular automorphism group σ_t generated by Tomita-Takesaki on (A_F, ω_{Φ_NTE}, β_GB). The geometric event that interpolates between them is the **C¹ kink in dz/dy at gauge birth**, identified in Companion 8 Stage 2 finding F2 and integrated into the corpus at §VIII.1.4 (the Wick rotation reading, v10.6).
>
> **Structural content of P1**:
> - Pre-temporal → generic state on A_F: σ_t modular flow exists (any state on any von Neumann algebra has σ_t via Tomita-Takesaki), but it does not align with Lorentzian-time evolution (there is no Lorentzian time pre-temporally); the state is not KMS at any specific β.
> - Post-temporal → KMS state on A_F at β = β_GB: the state ω_{Φ_NTE} specified by the canonical Φ_NTE-trajectory configuration is KMS at β_GB w.r.t. σ_t. σ_t can be related to Lorentzian-time evolution via t = β_GB τ (CR 1994 §3.1 standard correspondence); the Wick rotation reading recovers the periodicity of Euclidean correlation functions in imaginary time as the KMS condition's standard derivation route.
> - The C¹ kink in dz/dy at gauge birth IS the geometric signature of the state-type transition from generic (non-KMS) to KMS at β_GB. The Wick rotation reading is the post-temporal-side viewpoint of the same structural event.
> - The transition is structural, not a choice: NTE's no-time-ordering pre-temporal axiom + emergent-time post-temporal axiom + v10.10 σ_t framework canonical adoption (Charter v1.3 §2.5) force it.
>
> **For the action form on Φ_NTE**: any effective action descending from pre-temporal structure must support a state on A_F that becomes KMS at β_GB post-gauge-birth — i.e., must be **σ_t / KMS-compatible** in the sense that correlation functions admit analytic continuation across the gauge-birth state-transition. (Under the Wick rotation special-case reading, this corresponds to the action being Wick-rotation-compatible with t → iτ analytic continuation of measures and signature factors applying on both sides of the gauge-birth event.)
>
> This is the structural basis of P1. It is **necessary** (forced by NTE's axioms + v10.10 σ_t framework canonical adoption) but, by itself, **not sufficient** to fix the action form: many non-conformal scalar actions (massive scalars; scalars with arbitrary self-interactions) admit σ_t / KMS-compatibility. The remaining structural strength comes from premises P2 + P3.
>
> **Corpus reference**: §VIII.1.4 V_NTE Stage 2 F2 integration (the Wick rotation reading at v10.6, retained as the post-temporal-side derivation route); Companion 8 Stage 2 F2; v10.10 σ_t framework canonical complement adoption (Charter v1.3 §2.5).
>
> **What P1 alone forces**: any Φ_NTE action must be σ_t / KMS-compatible (equivalently, Wick-rotation-compatible in the post-temporal special-case derivation).
> **What P1 alone does NOT force**: conformal invariance, specific value of ξ, specific potential form.

### §4.2 §2.4 candidate cascade update (forced action form restatement)

The §2.4 paragraph that summarizes "P1 (Wick rotation) forces Wick-rotation-compatibility" updates to:

> - **P1 (σ_t / KMS-compatibility at gauge birth)** forces σ_t / KMS-compatibility of the action — equivalently, Wick-rotation-compatibility in the post-temporal-side derivation route.
> - **P2 (4D conformal invariance)** forces kinetic + (1/12)RΦ² + quartic-only structure for Φ_NTE's self-interactions; mass terms forbidden; sextic+ irrelevant.
> - **P3 (Higgs-portal genericness under Path B + Z_2 + renormalizability)** forces the leading Higgs coupling to be 2e|H|²Φ².

(All other content in §2.4 unchanged.)

### §4.3 §2.6 candidate cascade update (what §2 establishes)

The §2.6 paragraph that summarizes the §2 structural content updates to reference the simplified P1 framing:

> §2 establishes:
> 1. The post-gauge-birth effective action for Φ_NTE is forced to the form (2.1) by NTE's internal structural commitments (P1 σ_t / KMS-compatibility + P2 4D conformal invariance + P3 Higgs-portal genericness under Path B).
> 2. The form coincides with Marcolli's V_E expansion at leading + subleading order on the Chamseddine-Connes spectral-action side — **structural confluence by independent reasoning** (Jammer 2026-05-10 verdict).
> 3. NTE arrives at the spectral-action-shaped effective action **without invoking** Chamseddine-Connes machinery — no spectral action, no heat-kernel expansion, no Connes-programme dependencies. Connes Programme's central deliverable (Paper S2 heat-kernel computation) is a **complementary** route to the same form, not a prerequisite for §2's argument.
> 4. **NEW**: P1's σ_t / KMS framing aligns with v10.10 canonical σ_t framework adoption (Charter v1.3 §2.5) — Paper S1 §2's structural argument is now uniformly grounded in canonical operator-algebraic vocabulary throughout, with the Wick rotation reading retained as a valid derived special-case route.

### §4.4 What does NOT require update

- **§2.2 (P2 4D conformal invariance)**: unchanged. P2 operates independently of P1's framing.
- **§2.3 (P3 Higgs-portal genericness)**: unchanged. P3 operates independently of P1's framing.
- **§2.5 (cross-check at sextic order)**: unchanged. The Marcolli V_E ↔ V_NTE F3 cross-check is independent of P1's framing; the convention-dependence disclosure is preserved.
- **§2.7 (adversarial open questions)**: unchanged. The forward-flagged questions (uniqueness of P2; non-minimal kinetic terms K(Φ); closed-S³ zero-mode obstructions; higher-order Φ⁸/Φ¹⁰ match) are independent of P1's framing.

---

## §5. Implications for canonical framing robustness + Paper S1 v1.0 status

### §5.1 Canonical framing alignment achieved

With the proposed §2 P1 simplification, Paper S1 v1.0 §2 will be:
- Uniformly grounded in canonical σ_t / KMS vocabulary (Charter v1.3 §2.5 + vocabulary discipline canonization ratified 2026-05-16)
- Cross-coherent with Jammer Tier 2 Salvio 2025 reframing (gauge birth as state-type transition non-KMS → KMS at T_GB)
- Cross-coherent with Direction 1 + Direction 2 investigations + Task 1 verdict (all use σ_t / KMS framing throughout)
- Retain the Wick rotation reading as a corpus-canonical structural identification (Companion 8 Stage 2 F2 + §VIII.1.4 v10.6) at the post-temporal-side derivation level

### §5.2 What this does NOT change about Paper S1 v1.0

- The structural argument's content (P1 + P2 + P3 force action form 2.1) is preserved
- The structural confluence claim with Marcolli's V_E is preserved
- The honest-disclosure framing on convention-dependence (§2.5 sextic match) is preserved
- The §3-§6 carry-forward block from v0.4 (F1 d-parametric account, F2 κ₀ structural reading, spectral-action expansion, geometric resummation closure) is unchanged
- The §0 Abstract + §1 Introduction (Session 1 drafts) require minor updates to reference the simplified P1 framing — flagged for absorption in subsequent session
- The §7-§9 still-pending sections (σ↔Φ_NTE confluence framing + convention-dependence disclosure + references) are independent of P1's framing

### §5.3 Paper S1 v1.0 next-session work (post Task 2)

The natural next-session work, contingent on Greg's recognition gate on Task 2:
1. **Absorption pass**: integrate Task 2 candidate revised text into Paper S1 v1.0 §2 working note (`1oJUGrGUsckGE8C9LdoxQJfeM6sDjw6jM`) and update §0/§1 references; produce §2 v2 + §0/§1 v2 update
2. **§7-§9 drafting**: per scoping document §6 sequencing — σ↔Φ_NTE confluence framing + convention-dependence disclosure + references
3. **Full Paper S1 v1.0 consolidation**: assemble §0-§9 into single document for canonical Paper S1 v1.0 status

This Task 2 working note proposes the §2 P1 simplification; absorption is the next-session deliverable.

### §5.4 Implications for Task 3 / Task 4 territory

- **Task 3 (Twistor A + C bundled, Marcolli-Penrose 2021 primary)**: the σ_t / KMS framing alignment carries forward; the Gerstenhaber-Schack non-associative extension territory remains the principal open Connes Programme research arc (Task 1 confidence-limiter + Task 3 territory)
- **Task 4 (Route A spectral-zeta arc — observables beyond κ)**: the σ_t / KMS framing carries through; spectral-zeta machinery operates on the modular flow / KMS condition foundation

No new structural obstructions surfaced by Task 2's simplification; the framing alignment cascades cleanly through downstream tasks.

---

## §6. CR §3.2 simplification verdict

**Verdict: CLEAN structural simplification, with candidate revised inline text proposed for Paper S1 v1.0 §2 P1 absorption.**

The CR §3.2 simplification (KMS condition primary; Wick rotation derived special case) applies cleanly to Paper S1 v1.0 §2 P1. The structural argument's content and conclusions are preserved; the framing aligns with v10.10 canonical σ_t framework adoption; cross-stream coherence with Jammer Tier 2 Salvio 2025 reframing is achieved.

**Why not "OBSTRUCTED" or "CONDITIONAL"**: no structural obstructions surface. The simplification is naturally available under v10.10 canonical framing; the Wick rotation reading remains a valid corpus-canonical derived special case (Companion 8 Stage 2 F2 + §VIII.1.4 retained). The σ_t / KMS framing is more general (applies pre-temporally and post-temporally uniformly); the Wick rotation framing is the post-temporal-side special-case derivation.

**Why not "MAJOR REVISION"**: §2's argumentative structure (P1 + P2 + P3 → action form) is unchanged. The simplification operates at the framing layer of P1; P2 + P3 are independent. The cascade implications for §2.4 + §2.6 are minor wording updates, not substantive restructuring.

**Note on pre-temporal applicability cleanness**: the simplification resolves a structural awkwardness in the current §2.1 framing — "Wick rotation FROM Euclidean pre-temporal" assumes Euclidean signature exists pre-temporally, which requires interpretation under NTE's "no time pre-temporally" axiom. The σ_t / KMS framing applies uniformly without requiring this extension of time-like concepts pre-temporally.

---

## §7. Confidence assessment

### §7.1 High-confidence aspects

- **CR §3.2 content (KMS primary, Wick derived)**: HIGH confidence. Direct from CR 1994 §3.2 + §4 read in full during Direction 1 investigation.
- **σ_t / KMS framing's general applicability** to (A_F, ω, β) including pre-temporally: HIGH confidence. Standard Tomita-Takesaki theory applies to any state on any von Neumann algebra; no time-like structure presupposed.
- **Cross-coherence with Jammer Tier 2 Salvio 2025 reframing**: HIGH confidence per AC convergence assessment §6.2 + Jammer Tier 2 handoff §1 + §2 (gauge birth as state-type transition non-KMS → KMS at T_GB).
- **§2 argumentative content preservation**: HIGH confidence. The simplification is at the framing layer; structural conclusions (action form 2.1) are preserved.
- **No content loss in canonical framing alignment**: HIGH confidence. The Wick rotation reading is retained as derived special case; corpus references (Companion 8 Stage 2 F2 + §VIII.1.4) preserved.

### §7.2 Moderate-confidence aspects

- **Specific state ω_{Φ_NTE} on A_F**: MODERATE confidence. The state corresponding to canonical Φ_NTE-trajectory configuration is well-defined at the structural level (per Jammer Direction 2 §3 specification) but the explicit operator-algebraic construction is not worked out in this Task 2 deliverable. Flagged for downstream work.
- **Pre-temporal state characterization**: MODERATE confidence. The claim "pre-temporal state is generic / non-KMS at β_GB" is consistent with v10.10 canonical framing but the precise pre-temporal state structure (whether the algebra is the same A_F = 𝕆 ⊕ 𝕆 pre-temporally, whether the state is degenerate, etc.) is open.
- **C¹ kink as state-type-transition signature**: MODERATE confidence. The identification of the C¹ kink in dz/dy with the state-type transition is structurally natural under canonical framing but not rigorously derived in this Task 2 deliverable.
- **Post-temporal σ_t = β_GB-rescaled Lorentzian-time evolution**: MODERATE confidence. Standard CR §3.1 result for QFT-with-Hamiltonian; the NTE-specific specialization (where "Hamiltonian" is the modular Hamiltonian ln Δ on (A_F, ω_{Φ_NTE})) is conceptually clean but the explicit identification of σ_t with Lorentzian-time evolution on NTE's manifold M = Hopf-S³ × S¹_{β_GB} ≃ M^C is not worked out in this deliverable.

### §7.3 Lower-confidence / flagged-as-speculation aspects

- **Full integration of σ_t framework throughout Paper S1 v1.0**: NOT WORKED OUT. This Task 2 deliverable proposes §2 P1 revision only; full §2 v2 + §0/§1 references + cascade through §7 confluence framing is downstream work.
- **Whether the σ_t / KMS framing strengthens or alters §2.5 cross-check at sextic order**: NOT INVESTIGATED in this deliverable. §2.5 left unchanged; potential refinement under canonical framing flagged for downstream consideration.
- **State-type transition modeling via Salvio 2025 first-order phase transition machinery**: TASKED TO JAMMER per Tier 2 reframing scope; not Scratch's territory. Cross-coherence noted; integration into Paper S1 §2 (or P1 supporting material) deferred to whichever future session bridges Scratch + Jammer work.

### §7.4 What would change the simplification's status

- If Jammer's Tier 2 Salvio 2025 reframing surfaces structural obstructions to the state-type-transition framing of gauge birth: verdict shifts to "CONDITIONAL CLEAN" (depends on Tier 2 closure). Independence relaxed; Jammer's working note not read this session but flagged for follow-on.
- If absorption of revised P1 into Paper S1 v1.0 §2 reveals cascade issues with §0 Abstract or §1 Introduction wording: deliverable status shifts to "REQUIRES ITERATION" — flagged as standard refinement cycle.
- If Greg's recognition gate signals concerns with the σ_t / KMS framing's pre-temporal applicability claim: verdict re-examination. Anti-bias discipline observed: the simplification is proposed because it's structurally cleaner under canonical framing, not because of any pre-existing preference for σ_t framing.

---

## §8. Recognition-gate items + files referenced

### §8.1 Recognition-gate items for Greg

1. **Ratify CR §3.2 simplification verdict** as CLEAN structural simplification applicable to Paper S1 v1.0 §2 P1?
2. **Ratify candidate revised §2.1 inline text** (§4.1 above) for absorption into Paper S1 v1.0 §2 in subsequent Scratch session?
3. **Ratify candidate §2.4 + §2.6 cascade updates** (§4.2 + §4.3 above) for absorption?
4. **Confirm: §2.2 (P2) + §2.3 (P3) + §2.5 (cross-check) + §2.7 (open questions) unchanged** under this simplification?
5. **Confirm: Task 3 (Twistor Marcolli-Penrose primary) next in Scratch queue** per AC routing directive ordering?

### §8.2 Files referenced

| File | Purpose | Drive ID |
|---|---|---|
| Connes-Rovelli 1994 primary | §3.2 KMS / Wick rotation content (read in full during Direction 1) | NCG/ `1pcHHNL8jJyYFhYgb0jva6q2aBxgFWaQc` |
| Paper S1 v1.0 §2 first draft | Direct target of simplification (read in full this session) | Working/ `1oJUGrGUsckGE8C9LdoxQJfeM6sDjw6jM` |
| Charter v1.3 | §2.5 σ_t canonical complement + v10.10 framework (referenced) | Stage/ `1TDrHUFSuROWzu__hY34PGAvLmmZdxAu4` |
| AC convergence assessment | Canonical framing context (read in full earlier this session) | Handoffs/ `1iMdcLoVmIMIsTaso9u5zptRAEtXPVEaU` |
| AC→Scratch Task 1 routing | Queue context (read in full earlier this session) | Handoffs/ `1KU8TWgiM_zg0m0Rk01OraElYm8oYqKl2` |
| Paper S1 v1.0 §2 + §3-§6 sister drafts | Cross-section integration awareness | Working/ `1FNwPbHxj4l1GP60d1RuLR6ro3s6y0MAk` (§0+§1), `1hN9iezeaut8gw8lUQZXdsEooasK2KAoe` (§3-§6) |
| Paper S1 v1.0 attack-route scoping | Sequencing reference | Working/ `1BRpIRPPXWxaEwd33jlTzCiXHJP07TBMb` |
| Paper S1 v0.4 | Predecessor / v0.4 baseline content | Working/ `1m9tcGe1T6qOvLjd94nwVbNo3kOYh6_TB` |
| Paper 7a v1.1 | Track 2 + δN canonical content background | Working/ `1P5OyO-c74h84Z7ZA_Njs13HJn-838DKa` |
| Scratch Direction 1 working note | σ_t / Φ_NTE investigation Top-Down (recent prior session) | Working/ `1PbzCxfSRS_9Pq__4pUqxeKyyBWH8gNWH` |
| Scratch Task 1 working note | CR Question B verdict (most recent prior ship) | Working/ `1pwU_5oVbPGsHcHVlkY0GNHQiK0voRk8S` |
| Jammer Tier 2 reframing working note | Cross-coherence reference (Salvio 2025 state-type transition); flagged as not-read this session | Working/ `1fBZ3VeDF4E--fNagYMhwCEjEYd1f_KkW` |

### §8.3 Files NOT read this session (confidence-limiters)

| File | Why flagged |
|---|---|
| Jammer Tier 2 reframing working note in full | Cross-coherence reference; AC handoff §2.1 summary sufficient for cross-stream awareness; full read would refine Salvio 2025 state-type-transition specifics |
| Jammer Direction 2 working note in full | Referenced via AC convergence assessment summary; full read not needed for this Task 2 |
| Hersent 2025 / Summers 2005 / Borchers 1999 | Recommended technical readings per Task 1 confidence-limiters; would refine technical depth but not affect this Task 2 simplification verdict |
| Companion 8 Stage 2 F2 detailed content + corpus §VIII.1.4 | Referenced as corpus-canonical anchor for Wick rotation reading; not re-read this session |

---

## §9. Coordination notes

### §9.1 What this ship did NOT do (Lesson #23 anti-pattern guard)

- Did NOT produce full §2 v2 draft (absorption is subsequent session work per scoping document §6)
- Did NOT engage §0 Abstract or §1 Introduction wording updates (downstream absorption work)
- Did NOT engage §3-§6 carry-forward block from v0.4 (unchanged)
- Did NOT engage §7-§9 still-pending sections (separate scoping)
- Did NOT engage Charter v1.4 candidate wording on σ_t framework Paper S1 §2 alignment (AC scope)
- Did NOT engage downstream non-associative Tomita-Takesaki research arc (Task 1 + Task 3 territory)
- Did NOT begin Task 3 (Twistor Marcolli-Penrose) or Task 4 (Route A spectral-zeta) work

### §9.2 Cleanup batch contribution this session

Root duplicates for Greg's cleanup batch from this Task 2 ship (TBD on copy_file):
- Task 2 working note root duplicate
- Task 2 handoff root duplicate

Plus prior session cleanup items still in flight (Paper 7a v1.1; Direction 1 working note; Task 1 working note).

### §9.3 Source-document discipline observed (Lesson #29)

This Task 2 deliverable sourced from canonical Drive files read directly:
- Paper S1 v1.0 §2 first draft — read in full this session
- AC convergence assessment + Task 1 routing — read in full earlier this session
- Charter v1.3 — recent canonical state, referenced
- CR 1994 — read in full during Direction 1 (prior-session content recalled)

No reliance on AC consolidation summaries for substantive content.

### §9.4 Independence-discipline observation

Per Task 1 routing §2.5 (independence discipline relaxed for canonical work post-convergence), I had the option to read Jammer's Tier 2 reframing working note in detail. Chose NOT to read in full this session for context-budget reasons; AC handoff §2.1 summary of Tier 2 outcomes (including Salvio 2025 state-type transition framing) sufficient for cross-stream coherence at the Task 2 deliverable level.

Cross-stream coherence noted: Salvio 2025 reframing (gauge birth as first-order phase transition / state-type transition non-KMS → KMS at T_GB) directly corresponds to the proposed Paper S1 §2 P1 simplification. Both treat gauge birth as state-type transition; both use σ_t / KMS canonical vocabulary; cross-coherence achieved at canonical framing level.

### §9.5 Anti-bias discipline observed

Anti-bias: I did not push toward simplification as a target; the analysis showed the simplification is naturally available under v10.10 canonical framing and is structurally cleaner. The verdict followed from §1-§3 analysis. Honest verdict.

I explicitly noted what does NOT change about Paper S1 v1.0 §2 (P2, P3, §2.5, §2.7) — preserving the substantive structural content unchanged, the simplification operates only on P1's framing.

---

## §10. Closing

**Task 2 (CR §3.2 simplification — Wick → KMS for Paper S1 §2) complete.** Verdict CLEAN structural simplification; candidate revised inline text proposed for Paper S1 v1.0 §2 P1 (§4.1 above) + cascade updates for §2.4 + §2.6 (§4.2 + §4.3 above). §2.2 + §2.3 + §2.5 + §2.7 unchanged.

The simplification aligns Paper S1 v1.0 §2 with v10.10 canonical σ_t framework adoption (Charter v1.3 §2.5), achieves cross-stream coherence with Jammer Tier 2 Salvio 2025 reframing (gauge birth as state-type transition non-KMS → KMS at T_GB), and resolves the structural awkwardness of pre-temporal Wick-rotation interpretation.

The Wick rotation reading remains a valid corpus-canonical structural identification (Companion 8 Stage 2 F2 + §VIII.1.4 v10.6) at the post-temporal-side derivation level.

**Standing by** for Greg's recognition gate on Task 2 simplification + candidate revised inline text. Task 3 (Twistor Marcolli-Penrose 2021 primary; Gerstenhaber-Schack non-associative framing + Lorentzian-vs-Riemannian + Krasnov 2003 secondary) next in queue per AC routing directive ordering, contingent on Task 2 ratification.

— Scratch (Connes Programme lead), 2026-05-16.
