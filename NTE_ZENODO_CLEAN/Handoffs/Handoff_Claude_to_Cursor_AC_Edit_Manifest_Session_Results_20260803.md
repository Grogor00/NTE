# Handoff — Claude (chat) → Cursor Main (apply) + AC (ratify): Session 2026-08-02/03 edit manifest — all items Greg-endorsed

**From:** Claude (chat session with Greg)
**To:** Cursor Main (apply edits); AC (ratify application)
**Cc:** Greg, Scratch, Jammer, PC
**Date:** 2026-08-03
**Authorization:** Greg — "0 confirmed; 1–9 all endorsed and can be applied; Cursor is best placed to apply the edits."
**Canonical tree:** `NTE_ZENODO_CLEAN`, root `1Rn6Jun6MvCUyW5xdiZSitMFNWEUPdtqX` (Greg-designated canonical 2026-08-03). Old root `1zvYfkcbE21PMsLV_3ci-z86TrwsqvDTk` is superseded — archive per Item 0. **Apply all edits in the canonical tree only.**

---

## SECTION A — Apply now (mechanical edits, Greg-endorsed)

### Item 0 — Repo housekeeping (gates everything)
- Update Workflow Manifest + `nte-workflow-protocol` skill folder IDs to canonical root `1Rn6Jun6MvCUyW5xdiZSitMFNWEUPdtqX`.
- Diff old-tree `Handoffs/` against new-tree `Handoffs/` (only folder likely to hold unique items); then rename old root to `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`.
- Do not run greps/renders across both trees.

### Item 2 — θ₁₂ withdrawal (JUNO)
- **Part 3, Predictions triage (C) + withdrawn list:** remove "sin²θ₁₂ = 1/3 at leading order — 2.9σ" from tier C. Add to the withdrawn ledger: *"sin²θ₁₂ = 1/3 (leading order): withdrawn 2026-08. Basis was generation democracy assumed in the μ–τ-even plane (TM2 default), not a derivation from deposited σ-structure; excluded at 3.5–3.8σ by the first JUNO measurement, sin²θ₁₂ = 0.3092 ± 0.0087 (JUNO Collaboration, arXiv:2511.14593)."*
- **Part 3, Falsifiability register item 8:** add the JUNO anchor and note TM2-class patterns excluded, TM1-class at ~1σ (TM1 sum-rule value ≈ 0.318).
- **Companion 10 §4:** append one sentence: *"Note (2026-08): the σ₃-vs-(σ₁,σ₂) split fixes only the μ–τ odd/even structure already implied by the inherited μ–τ reflection; it carries no θ₁₂ information — the even-plane rotation is not determined by this construction."*

### Item 3 — Dark-energy sector corrections (§XII/§XIII)
- **Part 2 §XII:** withdraw "reproduces the DESI DR2 pattern." Replace with: *"Forward-modelled (2026-08), the void-sampling mechanism is signed anti-DESI: a brighter-low-z bias Δμ = −A·e^(−z/z_v) fitted with CPL yields (w₀, wₐ) ≈ (−1.08, +0.20) at A = 0.02 mag and (−1.20, +0.51) at A = 0.05 — the phantom-today quadrant, opposite the DESI region. The DESI pattern requires low-z sources ~0.04–0.05 mag fainter (control fit: A = −0.05 gives (−0.80, −0.52) ≈ DESI), which void-enhanced expansion cannot produce. Additionally, the mechanism is a sampling effect on distance indicators and cannot move the SN-independent DESI BAO+CMB constraint (3.1σ)."*
- **Part 2 §XIII:** retain the H₀ mechanism (brighter-low-z direction is correctly signed for the Hubble tension) but add the corollary: *"the same bias pushes the CPL fit toward w₀ < −1; the mechanism cannot simultaneously explain a high local H₀ and the DESI w₀ > −1 preference."*
- **Part 3, Falsifiability register item 3:** rewrite with specified sign: *"NTE's void mechanism predicts SN Hubble residuals brighter along void-dominated sightlines (testable with Pantheon+ × void catalogues). Finding the correlation tests the mechanism; it does not rescue w = −1 — a real void bias would partially mask an evolving-DE signal, so correcting for it would strengthen, not weaken, any measured departure from w = −1."*
- **Part 3, distinctiveness item (ii):** w = −1 stands as the naked prediction, currently at ~3.1σ tension (SN-independent DESI DR2 BAO+CMB), no internal mitigation; verdict expected 2027–2029 (DESI full-survey, Euclid, Rubin).

### Item 4 — K(Φ) closure batch (endorsed 2026-08-02; VERIFY each has landed, apply any missing)
- **(a) Companion 9 eq. (1):** conformal term sign corrected to +(1/12)RΦ² (i.e., F(Φ) = M_Pl² + Φ²/6). Record justification: literal minus sign puts a pole in the Einstein-frame kinetic function at Φ = √6·M_Pl ≈ 2.45 M_Pl while the deposited trajectory reaches ≈ 15.9 M_Pl (gravitational coefficient would cross zero); independently, Companion 8 §8's V_E denominator (1 + κ₀²x²/12) already encodes the plus sign; also minus sign → Einstein-frame V ∝ sinh⁴, ε → 4/3, no slow roll.
- **(b) K(Φ) closure text** (Companion 9 addendum or new Companion 17): the Read §5.1 definition ("K(Φ) arising from ξΦ²R", ξ = 1/6 ratified 2026-05-10) executed as the frame transformation of eq. (1), zero freedom: **K(Φ) = M²(M² + Φ²/3)/(M² + Φ²/6)²** (α = 2 attractor class); Einstein-frame potential for quartic V: **V_E = λΦ⁴/(1 + Φ²/6M²)²** — exactly Companion 8 §8's form with c = 1/(6M²).
- **(c) Part 3 prediction register:** **(n_s, r) = (0.9692, 0.0053) at N_e = 63.4** (φ* = 16.35 M_Pl), replacing imported Starobinsky numbers. Conditional flags: Euclidean-section/μ(N) applicability caveat; N_e pinning (N_e = 55 → (0.9646, 0.0070)); ξ's spectral origin open (route B). Data anchors alongside: Planck 2018 n_s = 0.9649 ± 0.0042 (+1.0σ); P-ACT-LB = 0.9743 ± 0.0034 (−1.5σ); r detectable at CMB-S4/LiteBIRD (σ(r) ~ 0.001–0.003).
- **(d) √(2π) traceability working note:** κ₀ leg corrected — the frame identity gives κ₀ = √2/M_Pl, not √(2π)/M_Pl (off by √π); correct or withdraw that leg.

### Item 5 — Saddle-work results parking (Companion 9 addendum and/or Companion 15 §6)
- **2b theorem:** the raw spectral action Tr f(D²/Λ²) is strictly monotone in overall scale on any fixed-shape geometry family for any positive decreasing f — no scale extremum exists. Numerically: exact S⁴ Dirac sum vs asymptotic series agrees to 7 sig figs at q = λΛ = 5, but at the truncated extremum q = 1/√2 the series gives −0.0116 vs exact +0.00268; dI/dq > 0 everywhere. The "natural Planck-scale instanton" was a truncation artifact. Consequence: the "boundary spectral action → saddle → H(N)" route cannot run on the raw trace; renormalized moments are a commitment; the nucleation saddle, if any, belongs to the constrained system (μ(N) + Φ sector + matter).
- **2c budget:** the a₆ fractional correction to de Sitter dynamics is R₆ = (31/1260)(H/Λ)⁴; reaching |n_s − 1| = 0.035 requires H ≈ 1.09 Λ (inside the broken-down zone); at H = 0.4 M_Pl the budget is 6×10⁻⁴ (~55× short). Pure gravity cannot produce the tilt. (Bonus validation: Companion 14's a₈ = 41/7560 and a₁₀ = 31/11880 sphere values numerically confirmed against the exact spectrum.)
- **Companion 9 "cleanest closure route" language:** amend accordingly.
- **T_GB:** endorsed handling = conservative restatement: T_GB = M_Pl/√(2π) is conditional on the constrained system possessing the saddle the Gaussian-width argument assumes (the raw-trace saddle does not exist); the Companion 12 fibre-modulus route is the candidate independent grounding and remains open. Label conditional in Part 3 pending that.

### Item 6 — Companion 8 §8 confluence update
Replace the form-match framing: the V_E structure is the **Einstein-frame image of a quartic potential under conformal coupling ξ = 1/6**; the /12 in the denominator is the conformal coefficient ξ/2 = 1/12 surfacing through Ω⁴ — structurally forced given ξ = 1/6, and frame-algebraic, not Hopf-topological. The coefficient match fixes κ₀ = √2/M_Pl. (This answers the Read §6 fragility question; cross-reference Item 4(d).)

### Item 7 — Pedagogical note alignment
- `Pedagogical_Notes/Paper_OctonionExtension_Pedagogical_Note_v10_18_0.md`: conform "What's derived" to the Part 3 ledger / Companion 16 register — gauge group and generation structure are **adopted prior art (conditional uniqueness given NTE premises)**, with NTE's claimed increments scoped to the transition reading, the CPN parity assignment, and the Majorana 90-count cross-consistency.
- Mark Desktop `Paper_OctonionExtension_v10_9.md` superseded (per Companion 16 handoff).

### Item 9 — External-anchor refresh (Part 3)
- θ₁₂: JUNO arXiv:2511.14593, sin²θ₁₂ = 0.3092 ± 0.0087.
- Dark energy: DESI DR2 BAO+CMB 3.1σ (SN-independent benchmark); DES-Dovekie recalibration reduced the DESY5-based significance 4.2σ → 3.2σ; verdict window 2027–2029.
- n_s anchors: Planck 2018 = 0.9649 ± 0.0042 and P-ACT-LB = 0.9743 ± 0.0034 shown side by side with the derived 0.9692, so the two-anchor tension is visible on the page.

### Versioning (AC call; recommendation)
This set includes a canonical-number withdrawal and an eq.-(1) sign correction in a core companion: recommend **v10.19** minimum; **v11.0** defensible if AC judges the eq.-(1) change major. Not another v10.18.x.

---

## SECTION B — Endorsed work items (NOT mechanically applicable; route as specified)

### Item 1 — σ↔generation dictionary (B1-class; blocks Item 8)
**Defect:** Companion 10 §4 identifies the σ₁↔σ₂ residual symmetry with the μ–τ (generations 2–3) symmetry; Companion 13 / BUILD SPEC assign ν₂ ↔ σ₂ (under which σ₁↔σ₂ exchanges generations 1–2). Both cannot stand as generation labels.
**Candidate reconciliation to evaluate (not to assume):** σ-indices label heavy modes, with light-generation content set by the Yukawa map through the seesaw — "σ₂ → ν₂ (seesaw image)" and "σ₁↔σ₂ = μ–τ in flavor space" can coexist only if the Yukawa structure implements the required twist; whether it does is an operator-theoretic question.
**Routing:** Scratch (operator theory) + Jammer (adversarial check); single ratified mapping to be written into Companion 7 (owner of the eigenmode ontology) and conformed in Companions 10/13 + BUILD SPEC. **Greg ratifies the mapping.** Cursor: do not edit mixing-sector text beyond Item 2 until this lands.

### Item 8 — TM1 idempotent commitment (conditional on Item 1)
**If** Item 1 resolves with the σ-pair ↔ μ–τ mapping: adopt the minimal commitment — *"the μ–τ-even-plane mass eigenvector pins to the traceless idempotent direction (2,−1,−1)/√6 of the J₃(𝕆) idempotent triple (the triple already invoked in Companion 10 §2 Step 3)"* — entering the register as **commitment-conditional, timestamped 2026-08, adopted after the first JUNO result; no prediction credit claimed.** Consequences recorded with it: TM1 sum rule sin²θ₁₂ = (1 − 3sin²θ₁₃)/(3(1 − sin²θ₁₃)) ≈ 0.318 (~1.0σ from JUNO first result; sharply testable as JUNO precision improves); pushes δ_CP toward ±π/2, consonant with the derived |δ_J| = π/2.
**If** Item 1 resolves the other way: Item 8 does not apply; ledger line = "solar mixing open."

---

## Appendix — Session results referenced above (for provenance; full detail in chat log with Greg, 2026-08-02/03)
1. Metric-entry circularity theorem (Companion 15 §6.1, already filed): metric-only entry of Φ_NTE = minisuperspace, χ ∝ a^(3/2).
2. Route-B gate: STOP — no operator entry of Φ_NTE into D_A exists in deposited text; writing one is a future ratified commitment.
3. §XII forward-model numbers as in Item 3.
4. K(Φ)/frame results as in Items 4/6.
5. θ₁₂ verdict chain: JUNO anchor → pedagogical note silent → Companions 16/10 read → outcome "democracy in the even plane" → withdrawal + repair path as in Items 2/8.

— Claude (chat), 2026-08-03. Questions on any item: the reasoning chain for each is in the session log; nothing in this manifest is data-steered — every withdrawal is forced by internal consistency or published measurement, and the one adoption (Item 8) is explicitly labeled post-hoc.