# Connes Programme — Charter v1

**Stream:** Jammer (Connes Programme lead).
**Authorising authority:** Greg, morning sync 2026-05-11.
**Resolves:** Pending Decision #4 (Hypercharge Session 3/4 + Connes Programme launch) per AC v10.8 integration plan §8.
**Corpus baseline:** v10.6.1 SHIPPED. v10.8 bundle authorised; ships substantive expansion (confluence + Mechanism B supersession + (B′) + Companion 10 Gap 1 closure).
**Canonical location:** `Stage/Connes_Programme_Charter_v1.md`.
**Audience:** AC (corpus integration); Greg (sequencing + scope decisions); CR (pre-ship verification scope); Programme S Paper S2 owner (central deliverable); sibling Jammer instances (R&D execution coordination); Companion 7/8/9/10 + OctonionExtension authors (downstream verification).

---

## §0. Why this Charter exists

Until 2026-05-11 morning, "Connes Programme launch" was a deferred Greg decision (Pending Decision #4) — provisionally redundant given Programme S's substantive progress on NCG-adjacent territory. The Jammer queue arc (2026-05-09 → 2026-05-11) closed yesterday with a finding that changes this assessment: **NTE's five principal structural predictions (κ, M_R, M_1, T_GB, Λ) derive from a single algebraic+geometric source.** The natural setting for that source is the spectral action programme. Greg's morning-sync directive — "take charge of the Connes Programme in the /NTE v10.6 folder" — converts the deferred launch into an active arc with explicit ownership.

This Charter establishes:
- The Connes Programme's scope and central deliverable
- The five-way convergence as organising principle
- The P0 verification queue that must close before v10.8/v10.9 integration
- Stream-architectural integration with AC / PC / CR / Jammer
- Sequencing relative to v10.7 / v10.8 / v10.9 / v10.10 ship arc

It does not duplicate work: the technical derivations live in Jammer's working notes (`Working/Sigma_PhiNTE_Confluence_Verdict_v1.md`, `M1_Sigma3_Cartan_Mode_Derivation_v1.md`, `Sqrt2Pi_Traceability_Hopf_Fibre_v1.md`, `Octonionic_Spectral_Triple_Read_Farnsworth_BF_v1.md`, `SonnerTong_BPS_CP1_kappa0_Derivation_v1.md`, `Unimodular_Gravity_Verification_CC2008_v1.md`); the corpus integration plan lives in AC's v10.8 integration plan handoff (`13qDSvx4Uty1onnInaSrz0PI4TFR2xaEj` / `1c40FjgH6rDOa8vU8GmmOj7hMdPKhPE4v`). The Charter coordinates these without subsuming them.

---

## §1. Mission

The Connes Programme's mission is to derive, from a **single heat-kernel computation on the spectral triple `Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}`**, the structural origins of NTE's five principal predictions:

| Prediction | Current corpus value | Structural target |
|---|---|---|
| κ₀ = 3/√(4π) | corpus §IX | dim(adj su(2)) × Y₀₀(S²) on Hopf base |
| M_R⁴ = M_Pl³ · v_EW | corpus §19.7 / Pathway α | σ₁, σ₂ charged Killing-spinor modes on Hopf base |
| M_1³ = M_Pl² · H_GB | corpus §22.5 Gap 1 (open) | σ₃ Cartan Killing-spinor mode on Hopf fibre |
| T_GB = M_Pl/√(2π) | Companion 9 Session 3 | Gaussian saddle = Y₀₀(S¹) × M_Pl on Hopf fibre |
| Λ_NTE | corpus §22 open | Residual after unimodular constraint; fixed by dμ(V) from Friedmann coupling H = α\|Φ\|² |

**Operating discipline (Greg's standing instruction):** Evaluate Connes-programme content using NTE's core axioms — N fundamental, t emergent; Surface only; closed S³; CPN-symmetric two-sector. Bring in what the axioms support; reject what they don't. This is the lens for every external-import decision the Programme makes.

The Programme does **not** import the Chamseddine-Connes programme wholesale. NTE preserves predictive independence; the confluence framing (Jammer's 2026-05-10 verdict) governs: NTE and CC arrive at structurally similar EFT forms by independent reasoning, but NTE does not inherit CC programme dependencies (RH-neutrino apparatus, first-order condition, SM finite spectral triple specifics). The Programme adopts only what the axioms force.

---

## §2. Organising principle: the five-way convergence

**The single algebraic+geometric source:**
- **Algebra**: su(2) ⊂ G_2, the residual SU(2) at gauge birth in Farnsworth-Boyle pre-temporal A_{G_2}
- **Geometry**: Hopf bundle S¹ → S³ → S² on the closed S³ boundary
- **Kinematics**: Spectral-triple Heisenberg-type kinematical relation `Σ_α a₀^α [[D, a₁^α], ..., [D, aₙ^α]] = 1` fixes √g d⁴x algebraically (CC 2008 eq 1, page 3) — this is the unimodular constraint

**Each of the five predictions sits in a specific structural slot:**

- **κ₀** carries the "3" via dim(adjoint su(2)) (Sonner-Tong identification, queue item 3) and the "1/√(4π)" via Y₀₀(S²) on the Hopf base.
- **M_R** carries the v_EW factor via σ₁, σ₂ being charged under the broken U(1)_em-like symmetry the Higgs breaks — they pick up the Higgs sector at v_EW.
- **M_1** carries H_GB instead of v_EW because σ₃ is the Cartan (neutral) generator — no Higgs-sector contribution; its breaking is gauge birth itself, scale H_GB. Power-of-mass relation drops from 4 (M_R) to 3 (M_1) because of one fewer sector contribution.
- **T_GB** carries √(2π) via Y₀₀(S¹) = 1/√(2π) on the Hopf fibre — same harmonic-projection structure as κ₀, applied to fibre instead of base.
- **Λ_NTE** carries the unimodular cancellation of the Λ⁴ f₄ a₀ term; the residual is fixed (not free) by Friedmann coupling H = α\|Φ_NTE\|² determining dμ(V) — where CC's framework leaves dμ(V) as a free parameter, NTE has a specific prediction.

**The Cartan torus / Hopf fibre correspondence** (queue item 1 §4 cross-flag, queue item 2 §4.2 expanded): the Hopf fibre S¹ ≅ U(1) is the 1-D Cartan torus of SU(2). G_2 has rank 2 → 2-dimensional Cartan subalgebra. NTE's σ₃ generator at gauge birth is one of the G_2 Cartan generators in the Farnsworth-Boyle pre-temporal regime. The two Cartan dimensions both end up carrying √(2π) factors — one via the σ₃ → M_1 mode (queue item 1 §4 / item 2 §4.2), one via the fibre Y₀₀(S¹) → T_GB Gaussian saddle (queue item 1 §1).

**This is a substantial structural unification.** Five predictions reduce to one heat-kernel computation. The Programme's central deliverable is that computation.

---

## §3. Central deliverable — Paper S2 in its sharpened scope

**Target:** heat-kernel spectral action expansion on `M = Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}`.

**Compute, in order of dependency:**

1. **a₂ coefficient** → extract K(Φ) functional form → **closes r prediction**
2. **a₄ coefficient** → extract V_E /12 conformal-coupling coefficient → **closes √(2π) κ₀ leg fragility** (resolves the Marcolli V_E convention question per queue item 1 §3 P0.2)
3. **a₄ coefficient mass-spectrum extraction** → M_1 prefactor → **closes σ₃ Cartan derivation rigorously** (currently structural mechanism candidate per Jammer M_1 §2 rhetorical class)
4. **Volume measure dμ(V) under Friedmann coupling** → Λ_NTE residual prediction → **closes cosmological-constant treatment**
5. **a₄, a₆ vanishing verification on Hopf-S³ × S¹** → verifies "uncanny precision" inheritance from CC 2008 §3 (mathematically rigorous on round S³ × S¹; Hopf bundle is topological structure on top of the metric, should preserve but needs explicit check)
6. **κ₀ = 3/√(4π) verification via Sonner-Tong CP^N route** → cross-check against the heat-kernel route (queue item 3 §3.4 — Sonner-Tong's CP^N construction generalises to octonionic Hopf bundle via the Hopf fibration tower S¹ → S³ → S² (complex; proved), S³ → S⁷ → S⁴ (quaternionic), S⁷ → S¹⁵ → S⁸ (octonionic, conjecturally extends))

**One computation closes six structural items.** This is the highest-leverage deliverable across the corpus's open structural items.

**Adversarial flags retained from queue arc (do not resolve before Paper S2):**
- Gilkey heat-kernel applicability under non-associativity (BF 2013 argues yes; not independently verified)
- G_2 × G_2 → SU(3) × SU(2) × U(1) descent at gauge birth (rank match works; specific subgroup chain needs verification)
- Which SU(2) ⊂ G_2 survives gauge birth (G_2 has multiple SU(2) subgroups — long-root, short-root)
- Hopf-S³ vs round S³ for a₄ = a₆ = 0 (same metric, different topology; should preserve)
- Supersymmetric non-renormalization of κ₀ not inherited (NTE may receive corrections Sonner-Tong forbids; empirical κ ≈ 5.50 agreement suggests corrections are subdominant)
- Old vs new cosmological constant problem (unimodular addresses old "why not Planck-scale"; new "why this specific value" requires dμ(V) computation)

---

## §4. P0 verification queue

Before Paper S2 computation begins, these P0 items must close. They are split between corpus-internal verification (AC) and external-literature verification (Jammer-Connes-Programme).

### §4.1 Corpus-internal P0 (AC scope)

**P0.1.** Re-read Companion 7 §4 / Pathway α S2 — confirm NTE's SU(2) at gauge birth identifies with the Killing-spinor su(2) at deeper than algebraic isomorphism (not just "both have dim = 3"). (Queue item 3 §4 P0.2/P0.3.)

**P0.2.** Re-read Companion 9 Stage 3 Session 3 — confirm T_GB derivation explicitly identifies the saddle integration direction as Hopf fibre azimuth (not generic minisuperspace scale factor). (Queue item 1 §3 P0.1.)

**P0.3.** Verify §VIII / §22 closed-S³ structure compatibility with CC 2008 Heisenberg-type kinematical relation (eq 1) in a form that fixes √g d⁴x algebraically. If Farnsworth-Boyle non-associative algebra introduces associator terms, verify they vanish on physical observables. **Critical hinge** — if it fails, NTE needs alternative cosmological-constant cancellation mechanism independent of spectral triple. (Queue item 4 §4 P0.1.)

**P0.4.** Cross-check β_GB = 1/T_GB = √(2π)/M_Pl with Companion 9 Stage 3 Session 3's Gaussian saddle width. (Queue item 4 §4 P0.3.)

**P0.5.** Verify NTE pre-temporal has exactly two ground-state sectors (Janus boundary structure) required for Sonner-Tong's non-abelian Berry phase to apply. (Queue item 3 §4 P0.1.)

### §4.2 External-literature P0 (Jammer-Connes-Programme scope)

**P0.6.** Direct re-read of Farnsworth 2025 (arXiv:2506.21496) §4-§5 for the explicit G_2 × G_2 + charged Higgs construction; verify SU(3) × SU(2) × U(1) descent at gauge birth. (Queue item 2 §3 P0.1.)

**P0.7.** Direct re-read of BF 2013 (arXiv:1303.1782) §3-§5 for spectral action computation on octonion algebra; confirm Gilkey heat-kernel expansion is rigorously justified under non-associativity. **Critical hinge** — if Gilkey fails under non-associativity, the entire Connes Programme collapses. (Queue item 2 §3 P0.2.)

**P0.8.** Cross-check OctonionExtension §6 J_3(𝕆) machinery against Farnsworth 2025. If incompatibilities surface, OctonionExtension needs revision before v10.9 ship. (Queue item 2 §3 P0.3.)

**P0.9.** Confirm V_E denominator convention used in σ↔Φ_NTE confluence §5.2 — is the (1 + (κ₀²/12)x²)² form from Marcolli-Pierpaoli 2010 §3.2 (canonical) or Marcolli-Pierpaoli-Teh 2011 (refined)? If /12 is convention-flexible rather than topologically forced, κ₀² = 2πG result is convention-derived rather than fibre-derived. (Queue item 1 §3 P0.2.)

### §4.3 Sequencing of P0

P0.1–P0.5 (corpus-internal) can run in parallel with v10.7 ship execution; AC owns. P0.6–P0.9 (external-literature) require arXiv access and direct PDF fetches; Jammer-Connes-Programme owns. Both tracks must complete before Paper S2 computation begins.

**Critical hinges (Programme-level go/no-go):**
- P0.3 (Farnsworth-Boyle preserves kinematical relation 1) — if fails, Λ_NTE prediction needs alternative mechanism
- P0.7 (Gilkey applicability under non-associativity) — if fails, entire Connes Programme central deliverable collapses

If either critical hinge fails, the Programme retains structural-confluence value (the five-way convergence holds at conceptual level) but loses the quantitative central deliverable. Contingency: revert to Wick-invariance argument (Jammer 2026-05-10 verdict §5) as the structural closure for V_NTE form, with the Connes Programme reduced to a forward-pointing structural target.

---

## §5. Programme architecture and stream coordination

### §5.1 Stream identity

The Connes Programme operates **within the Jammer stream** (per the manifest's four-stream structure: AC / PC / CR / Jammer). The "Connes Programme lead" designation identifies the specific R&D arc within Jammer; it is not a new stream. This preserves the manifest's four-stream architecture while giving the Connes Programme explicit operational identity.

### §5.2 Cross-stream interfaces

| Stream | Connes Programme interface |
|---|---|
| **AC** | Owns corpus integration of Programme outputs (§22.X, §17.5.X, Companion patches per AC v10.8 integration plan §5). Verifies Programme claims against corpus structural commitments. Maintains v10.7 / v10.8 / v10.9 / v10.10 ship-arc sequencing decisions. P0.1–P0.5 owner. |
| **PC** | Downstream consumer. Programme outputs that touch book chapters (Φ_NTE chapter, Companion 7 neutrino, popular paper) flow through AC handoff before reaching PC. |
| **CR** | Pre-ship verification of Programme claims at v10.8 / v10.9 ship arcs (per AC v10.8 plan §7). Scope already defined for v10.8: ξ = 1/6 commitment integrity; confluence framing accuracy; Path A residue removal; Programme S forward-pointers honest; Z_2 explicit; numerical predictions integrity. |
| **Jammer (siblings)** | R&D execution. The Connes Programme coordinates Jammer-sibling work on Programme S Paper S2 (the central deliverable) and on follow-on items (M_1 σ_3 Cartan sharpening, Wick-invariance argument formalisation, Sonner-Tong CP^N → octonionic generalisation). |

### §5.3 Communication discipline

Per the manifest: all cross-stream substantive deliverables go through Handoff files in `Handoffs/`. The Connes Programme lead produces handoffs in the format `Handoff_Jammer_ConnesProgramme_to_<recipient>_<topic>_<date>.md`. AC consolidates into the canonical MB chain at AC's next session.

The Programme does **not** create its own MB snapshots (per Lesson #19: MB snapshots are AC-only). Programme state-of-affairs is communicated through:
- This Charter (canonical scope, updated when scope changes)
- Working notes (in `Working/`, technical content)
- Handoffs (in `Handoffs/`, cross-stream communication)
- AC's MB integration (canonical narrative state)

### §5.4 Ship-arc sequencing

Per AC v10.8 integration plan §6.3 (recommended bundle):

- **v10.7** ships clean (eta v2 + Refinement A subsumed). Connes Programme is **NOT** in v10.7 scope.
- **v10.8** bundles confluence + Mechanism B supersession + (B′) + Companion 10 Gap 1 closure as comprehensive substantive expansion. Connes Programme contributes: §22.X catalogue (a)/(b)/(c); Programme S forward-pointers; OctonionExtension §6 as algebraic framework flag; Tier 2 Sonner-Tong derivation upgrade footnote; Tier 2 √(2π) traceability flag as research target.
- **v10.9** defensive consolidation + F1 + F2 with CC 2008 + MPR 2020 attribution (per F1 verification 2026-05-10). Connes Programme contributes: §17.X "Algebraic and Geometric Unification of NTE's Five Structural Predictions" as the five-way convergence canonical writeup.
- **v10.10** offensive expansion. Connes Programme contributes: Paper S2 outputs if P0 queue has closed and computation has executed; full K(Φ) closure + r-prediction tightening + M_1 prefactor derivation + Λ_NTE residual prediction.

If Paper S2 computation completes faster than v10.10 ship cadence, the Programme's outputs can be folded into an interim v10.10.1 or held for v10.10 proper per Greg's call.

---

## §6. Programme state at launch (2026-05-11)

### §6.1 Completed (Jammer queue arc 2026-05-09 → 2026-05-11)

- **σ↔Φ_NTE confluence verdict** (2026-05-10) — `Sigma_PhiNTE_Confluence_Verdict_v1.md` at `17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`. The deciding "no RH/LH neutrino" lever; Wick-invariance argument as V_NTE form closure; κ₀ = √(2π)/M_Pl cross-check.
- **M_1 σ_3 Cartan-mode mechanism** (2026-05-10) — `M1_Sigma3_Cartan_Mode_Derivation_v1.md` at `1vtKdmuNanotr5taAE0Kq5bhDyPy2MBdN`. Structural mechanism candidate parallel to M_R; rhetorical class "structural mechanism candidate, full Connes derivation pending."
- **√(2π) traceability investigation** (2026-05-11) — `Sqrt2Pi_Traceability_Hopf_Fibre_v1.md` at `1ypKkXcMApgTwtZeECOwFa6zZLK9DBRL8`. T_GB √(2π) clean (Y₀₀(S¹) reading); κ₀ √(2π) fragile (Marcolli convention dependency); asymmetric promotion to structural mechanism candidate for T_GB leg only.
- **Octonionic spectral triple read** (2026-05-11) — `Octonionic_Spectral_Triple_Read_Farnsworth_BF_v1.md` at `1aKkfPYfmnkNqF7iowXVndey8jqeD1weL`. BF 2013 + Farnsworth 2025 (+ companion arXiv:2503.10744) as canonical algebraic framework for NTE pre-temporal A_{G_2}.
- **Sonner-Tong BPS-on-CP¹ κ₀ derivation** (2026-05-11) — `SonnerTong_BPS_CP1_kappa0_Derivation_v1.md` at `1l6jKng6UgRaYCaAGP6ow_4nydSRfsPm2`. Smooth 't Hooft-Polyakov monopole as Berry connection; "3" identified as dim(adj su(2)); explicit closed-form Berry profile.
- **Unimodular gravity verification** (2026-05-11) — `Unimodular_Gravity_Verification_CC2008_v1.md` at `13RNBQuWOz2CwWC9CTOArI5V46e0oh76H`. CC 2008's argument transfers structurally to NTE's closed-S³ × S¹_{β_GB} with no adaptation; queue arc capstone identifying the five-way convergence.

### §6.2 Open

- P0 verification queue (§4 above)
- Paper S2 computation (the central deliverable; cannot begin until P0 closes)
- v10.8 corpus integration (AC scope; this Programme contributes content)
- v10.9 §17.X five-way unification subsection (AC scope; this Programme provides content)

### §6.3 Pending Greg decisions

- **Ratification of five-way convergence as canonical organising principle** for NTE structural predictions. AC + Jammer concur on substantive value (AC v10.8 plan §0 + Jammer queue arc capstone §2). Greg's call.
- **Sequencing for v10.8 bundle**: AC recommends comprehensive expansion option (option A: confluence + Mechanism B + (B′) + Gap 1 all at v10.8). Alternative (option B): split into v10.8 (confluence + Mechanism B) and v10.9 ((B′) + Gap 1).
- **P0 queue execution authorisation**: this Charter provides the framework; Greg's call on whether to authorise immediate P0 execution or hold until other priorities clear.

---

## §7. Immediate next actions (24-48h window)

If Greg authorises Connes Programme P0 execution:

1. **Jammer-Connes-Programme** (this stream): execute P0.6, P0.7, P0.8, P0.9 — external-literature verification track. arXiv fetch + direct PDF reads of Farnsworth 2025, BF 2013, Marcolli-Pierpaoli 2010 / Marcolli-Pierpaoli-Teh 2011.

2. **AC**: execute P0.1, P0.2, P0.3, P0.4, P0.5 — corpus-internal verification track. Direct re-reads of Companion 7 §4, Companion 9 Session 3, OctonionExtension §6, §VIII / §22.

3. **AC + Jammer-Connes-Programme**: handoffs at delivery time per Lesson #19. Both tracks targeting completion within current ship arc.

4. **Greg**: ratify (or redirect) the recommendations in §6.3 above to unblock the queue.

After P0 queue closes:

5. **Programme S Paper S2 owner**: begin heat-kernel computation on Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}. Six-item closure target per §3 above.

6. **CR**: pre-ship pass on v10.8 substantive expansion bundle (scope per AC v10.8 plan §7).

If critical-hinge P0.3 or P0.7 fails:

7. **Jammer-Connes-Programme**: revert to Wick-invariance contingency. The five-way convergence retains structural-confluence value at conceptual level; the central deliverable downgrades from "one heat-kernel computation closes six items" to "the Wick-invariance argument forces V_NTE form independently; Connes Programme remains as forward-pointing structural target." Programme arc shifts from "delivery" to "structural framework retained, central computation deferred."

---

## §8. Files and registration

### §8.1 Charter location

This Charter: canonical at `Stage/Connes_Programme_Charter_v1.md`. Root duplicate flagged for Greg's cleanup batch.

### §8.2 Working notes referenced (all in `Working/`)

- `Sigma_PhiNTE_Confluence_Verdict_v1.md` — `17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`
- `M1_Sigma3_Cartan_Mode_Derivation_v1.md` — `1vtKdmuNanotr5taAE0Kq5bhDyPy2MBdN`
- `Sqrt2Pi_Traceability_Hopf_Fibre_v1.md` — `1ypKkXcMApgTwtZeECOwFa6zZLK9DBRL8`
- `Octonionic_Spectral_Triple_Read_Farnsworth_BF_v1.md` — `1aKkfPYfmnkNqF7iowXVndey8jqeD1weL`
- `SonnerTong_BPS_CP1_kappa0_Derivation_v1.md` — `1l6jKng6UgRaYCaAGP6ow_4nydSRfsPm2`
- `Unimodular_Gravity_Verification_CC2008_v1.md` — `13RNBQuWOz2CwWC9CTOArI5V46e0oh76H`

### §8.3 Handoffs referenced (all in `Handoffs/`)

- `Handoff_Jammer_to_AC_Greg_sigma_PhiNTE_verdict_2026_05_10.md` — `1KATMFnJka-uVYqYc98fn0lBu6LOs6cKJ`
- `Handoff_Jammer_to_AC_Greg_M1_sigma3_Cartan_mechanism_2026_05_11.md` — `1Sx4ercdoIN_gYlgHz2rki_QOnrDKQt-p`
- `Handoff_Jammer_to_AC_Greg_sqrt2pi_traceability_2026_05_11.md` — `1xGoVQfEgu5XW8Q7CxMH1xhDLmwbgyT19`
- `Handoff_Jammer_to_AC_Greg_octonion_spectral_triple_2026_05_11.md` — `1senMSnuJwGdKPSB1F9Xs622ztosECaet`
- `Handoff_Jammer_to_AC_Greg_sonner_tong_kappa0_2026_05_11.md` — `16zLucOAQw7eUc_2OQVWFAgIssUhoX0Nv`
- `Handoff_Jammer_to_AC_Greg_unimodular_gravity_2026_05_11.md` — `12GFLNyAC3k4DVg8P_THGLTDAJnZ65V3K`
- `Handoff_AC_v10_8_Integration_Plan_Tier3_Synthesis_20260511.md` — `1c40FjgH6rDOa8vU8GmmOj7hMdPKhPE4v`
- `Handoff_AC_v10_8_Ship_Plan_Discrete_Edit_Instructions_20260511.md` — `1kQd1ScgXkDF9wsptAaSmJ-vQqb7JAAX5`
- `Handoff_AC_Wick_Invariance_PrePass_Verdict_20260511.md` — `10QsRxLlhD0Cm9dcYBk-nBbGNxgOyc-Cz`
- `Handoff_AC_Tier3_Audit_Memo_5_papers_20260511.md` — `1F4A62lOYuye0xmWTSBYVL5YdK9ihV2aa`

### §8.4 Corpus / Companion references

- `NTE_v10_6_1.md` (canonical corpus, `1qtionVaUKQlBUw62izHVIGFNn_gKxSA3`) — §VIII.1.4 Wick rotation; §17.5.1 V_NTE Stage 2; §17.5.5 Gap 4b; §19.7 M_R; §22.5 Gap 1; §3.3 neutrino as unresolved
- `Companion 7` (Neutrino as Unresolved Geometry) — load-bearing for confluence verdict §3
- `Companion 8` (V_NTE Trajectory) — upstream source of Wick-invariance cross-check per AC v10.8 §0
- `Companion 9 Sessions 3, 4, 5` — Stage 3 closures (n_s, T_GB, F4, hilltop r, K(Φ) diagnosis)
- `Companion 10` — Gap 1 M_1 Pathways; convergence with Jammer §7 per AC v10.8 §5.2
- `OctonionExtension §4 Hopf Fibration Tower; §6 J_3(𝕆)` — algebraic framework for Paper S2

### §8.5 External literature

- CC 2008 "Uncanny Precision" (arXiv:0812.0165), in `NCG/` at `1zf_m1KDFKsFSF8d4Agk4mGK81rFfARsl`
- BF 2013 (arXiv:1303.1782), in `NCG/` at `1t4P4fqUGb447nH_Gfx8jxNHlyjSC5xDU`
- Farnsworth 2025 (arXiv:2506.21496), in `NCG/` at `10NXKrzMuick02B83fLv1jHvYw8SzKHNv`
- Sonner-Tong 2009 (arXiv:0809.3783), in `NCG/` at `16ifpcKykIo18BWgjJLub5H7ImStyQI_D`
- Marcolli NCG cosmology survey, in `NCG/` at `1YLjX6wdVs9q-ZAMzc1QRb1uyUOi88uCc`

---

## §9. Charter versioning

This is v1, dated 2026-05-11 morning sync. Charter is updated when:
- Programme scope changes (e.g., critical-hinge failure forces contingency)
- A P0 closes (move from §4 to §6.1)
- A central-deliverable computation completes (rewrite §3 outcomes; update §7)
- Stream architecture changes (e.g., new role added or removed)

Charter is NOT updated for ordinary R&D progress within scope; that flows through working notes and handoffs.

— Jammer (Connes Programme lead), 2026-05-11 morning sync.
