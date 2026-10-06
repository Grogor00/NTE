# HiggsInflation VERDICT — Jammer (adversarial), gates G-2 and G-3, plus the cheaper-candidate question

**Headline:**
- **G-2:** inflation itself sits inside the model's domain of validity on the best-supported reading. **Reheating does not.** The preheating stage is ~470× above the vacuum cutoff at λ ≈ 0.01. The standard cure adds a scalaron, so "zero new fields" fails in the unitarity-safe version.
- **G-3:** the corpus's own declared closure route for ξ = 1/6 (route B, spectral origin), if it runs through a Chamseddine–Connes-type action, fixes the Higgs at the conformal value too. **Route B and Higgs inflation are mutually exclusive.** Correction: "minimally coupled by omission" was mine and is wrong in kind.
- **Cross-lane D1 risk:** Part 2 §8.1 puts the Higgs into existence only at gauge birth, so the no-boundary saddle cannot carry a Higgs field value. That is Scratch's G-1, flagged here.
- **Cheaper candidate:** no other scalar in the deposit, but an omitted R² term (Starobinsky) does the same job with fewer disqualifier exposures.

**From:** Jammer · **To:** AC · **Cc:** Greg · **Date:** 2026-09-26
**Directive:** `Handoffs\Directive_AC_Higgs_Inflation_Research_Programme_Five_Gates_Pre_Registered_Disqualifiers_20260926.md`
**Register:** findings, not rulings. Nothing patched. Blind: I did **not** read Scratch's G4 verdict or its handoff, nor anything else advocating an exit. I read AC's arbitration (`Handoffs\Arbitration_AC_G4_Route1_Defeated_NTE_Needs_Accelerated_Epoch_To_Exist_Three_Exits_20260926.md`), which summarises Scratch's (0.965, 0.0037, 1.5×10¹³ GeV) claim.

---

## 0. Read set (discipline 11)

**Read in full this session:**
- Part 1, Part 2, Part 3, C8, C9 (`Core_Papers\*.md`, v10.19.0), read earlier this session for the no-inflation verdict and still in context.
- This turn: the directive and AC's arbitration.

**Not read this session:** C15, C17 and the C21 draft. **[not re-read]** marks where they bear.

**External, read this session (abstract level):**
- Bezrukov, Magnin, Shaposhnikov & Sibiryakov, *Higgs inflation: consistency and generalisations*, JHEP 01 (2011) 016.
- Ema, Jinno, Mukaida & Nakayama, *Violent preheating in inflation with nonminimal coupling*, arXiv:1609.05209 / JCAP 02 (2017) 045.
- Gorbunov & Tokareva, *Scalaron the healer*, arXiv:1807.02392.
- Buck, Fairbairn & Sakellariadou, *Inflation in models with conformally coupled scalar fields: an application to the noncommutative spectral action*, arXiv:1005.1188 / PRD 82 043509.
- Masina & Quiros, *Electroweak metastability and Higgs inflation*, EPJC (2024-11-15).
- Rubio et al., *Quantum effects in Palatini Higgs inflation*, arXiv:2002.07105.

**From background knowledge, not fetched:** Burgess–Lee–Trott 2009 and Barbón–Espinosa 2009 (the original M_Pl/ξ objection); the one-loop β_ξ ∝ (ξ − 1/6) structure (the OSTI copy was robots-blocked); the Chamseddine–Connes spectral-action Higgs–curvature coefficient; Palatini r ≈ 2/(ξN²); the Starobinsky reheating rate ∝ (1 − 6ξ_H)².

**Script:** `scratchpad/hi.py`, the α = 1 E-model map, which is the Einstein-frame form of metric Higgs inflation.

---

## 1. Disqualifiers and forks

The disqualifiers D1–D5 are adopted as written.

**Jammer forks.** The literature searches came first; these forks were declared before the numerical run.
- **G-2:**
  - U-in: inside validity at both inflation and reheating.
  - U-split: inside during inflation, outside at (p)reheating.
  - U-out: outside during inflation.
- **G-3:**
  - P-gap: a principle fixes ξ = 1/6 and is merely silent on ξ_H.
  - P-weak: no principle; ξ = 1/6 is weakened.
  - P-clash: the candidate principle, applied, forbids ξ_H ≫ 1.
- **Cheaper candidate:**
  - C-none
  - C-field: another scalar in the deposit.
  - C-term: an omitted operator.

**Where each landed:** U-split. P-clash, conditional on route B's form. C-term.

---

## 2. G-2 — Unitarity

**2.1 NTE's numbers** (metric formulation, A_s = 2.1×10⁻⁹, k* = 0.05 Mpc⁻¹):

| N* | n_s | r | ξ/√λ | H_inf (GeV) | V^¼ (GeV) |
|---|---|---|---|---|---|
| 50 | 0.9616 | 0.0042 | 43 200 | 1.60×10¹³ | 8.3×10¹⁵ |
| 55 | 0.9650 | 0.0035 | 47 300 | 1.47×10¹³ | 7.9×10¹⁵ |
| 60 | 0.9678 | 0.0030 | 51 500 | 1.35×10¹³ | 7.6×10¹⁵ |

- Scratch's (0.965, 0.0037, 1.5×10¹³) reproduces at N* ≈ 53–55. That is a check of the arithmetic only; G-4 remains Scratch's gate.
- Against the two anchors (printed, not picked): at N* = 55, Planck +0.0σ and P-ACT-LB −2.7σ. At N* = 60, +0.7σ and −1.9σ.

**2.2 Cutoffs against scales** (H_inf = 1.47×10¹³ GeV and V^¼ = 7.9×10¹⁵ GeV, both independent of λ):

| λ at inflation | ξ | M/ξ (vacuum cutoff) | M/√ξ (large-field cutoff) | preheating k ~ √λ M | k ÷ (M/ξ) |
|---|---|---|---|---|---|
| 0.1 | 15 000 | 1.6×10¹⁴ | 2.0×10¹⁶ | 7.7×10¹⁷ | 4 700 |
| 0.01 | 4 700 | 5.1×10¹⁴ | 3.5×10¹⁶ | 2.4×10¹⁷ | 470 |
| 10⁻³ | 1 500 | 1.6×10¹⁵ | 6.3×10¹⁶ | 7.7×10¹⁶ | 47 |
| 10⁻⁴ | 470 | 5.1×10¹⁵ | 1.1×10¹⁷ | 2.4×10¹⁶ | 4.7 |
| 10⁻⁵ | 150 | 1.6×10¹⁶ | 2.0×10¹⁷ | 7.7×10¹⁵ | 0.5 |

**2.3 Each reading, stated plainly**
- **Vacuum reading** (Burgess–Lee–Trott; Barbón–Espinosa):
  - V^¼ sits above M/ξ for every λ ≳ 10⁻⁵. **The inflationary energy scale is above this cutoff.**
  - H_inf sits below it. Whether H or V^¼ is the scale to compare is itself part of the dispute.
- **Background-dependent reading** (Bezrukov–Magnin–Shaposhnikov–Sibiryakov 2011, abstract read): the cutoff "is found to be higher than the relevant dynamical scales" throughout cosmic history.
  - During inflation, M/√ξ ≈ 3.5×10¹⁶ GeV (λ = 0.01) lies above V^¼ and H.
  - **Inside validity during inflation.** This is the best-supported reading *for the inflationary stage*.
- **Preheating** (Ema–Jinno–Mukaida–Nakayama, abstract read): produced particles have "very high momenta k ≲ √λ M_P", and "the possibility of unitarity violation at the preheating stage" is raised.
  - For NTE's parameters the momenta exceed M/ξ by 470× at λ = 0.01.
  - Only near-critical λ ≲ 10⁻⁵ keeps them below.
  - The 2011 paper's "throughout cosmic history" claim predates this result and does not address it.
  - **This is where the dispute actually lives now.**
- **The cure:** Gorbunov–Tokareva (abstract read): adding R² lifts "the strong coupling energy scales in scalar, gauge and gravity sectors all … up to the Planck scale."
  - That is a **new propagating gravitational scalar** (the scalaron) and a second coefficient.
  - **The unitarity-safe version of exit (a) is Higgs–R², not Higgs alone. "One new parameter, zero new fields" does not survive.**

**2.4 D2 status.** It fires for the reheating stage, not the inflation stage. It is a known defect to carry, and it lands on the exact stage G-5 hoped would "reopen favourably".

**2.5 Formulation fork the deposit has not made.** C9 eq. (1) writes R without saying whether gravity is metric or Palatini. Metric is the implicit default.
- **Palatini:** the cutoff rises to ≈ M/√ξ and inflation is comfortably safe (Rubio et al. abstract: "the cutoff … is higher than the scale of inflation"). But ξ must be ~10⁹-scale and r ≈ 2/(ξN²) ~ 10⁻¹². This formula is from background knowledge.
- **So AC's "r ≈ 0.0037 is testable within a few years" holds only in the metric formulation.** Choosing Palatini to escape G-2 kills the testability that is the programme's best feature.

---

## 3. G-3 — ξ_H ≫ 1 beside ξ = 1/6

**3.1 What the deposit's "principle" is** (read this session):
- C9 §1: ξ = 1/6 is "**motivated** by the boundary-only ontology … conformal coupling is **consistent with** reading Φ_NTE as a geometric quantity of the boundary rather than a separate matter field."
- Part 3 "Open": "Spectral origin of ξ = 1/6 (route B)". It also says the metric-only spectral route is "proven empty" (C15 §6.1 **[not re-read]**).

So the current basis is a Φ-specific motivation, not a derivation. By its own terms it says nothing about the Higgs, which is a matter field (Part 1 §2.3).

**3.2 Branch one: P-gap, weakly.** Read as Φ-specific, the motivation neither forbids nor sets ξ_H.
- ξ_H becomes a free input fixed by A_s: ξ/√λ ≈ 4.7×10⁴.
- **That is one parameter matched to one observable**, the same register as β_NTE fixed by H₀ (Part 1 §2.4).
- **D3's second clause ("ξ_H tuned to a value with no independent motivation") fires literally.** Under Greg's imported-and-credited framing this is standard Higgs inflation and may be acceptable. It must be ledgered as a fitted input, not structure.

**3.3 Branch two: P-clash, if route B closes.**
- **The RG point** (background knowledge; source fetch blocked): at one loop β_ξ ∝ (ξ − 1/6), so **1/6 is the only RG-distinguished value for any scalar**, the Higgs included.
  - "Minimally coupled by omission" (ξ_H = 0) is not a stable assignment. It runs.
  - **Correction, owned:** that phrase originated in *my* no-inflation verdict §5 and was carried into AC's arbitration §3 and this directive §1. The accurate statement is "**ξ_H is unassigned** in C9 eq. (1)." The class correction: every downstream use of "minimal by omission" should read "unassigned".
- **The spectral-action point** (the coefficient is from background knowledge; the paper framing is from Buck–Fairbairn–Sakellariadou, abstract read):
  - The Chamseddine–Connes spectral action couples the Higgs to R at the **conformal value**.
  - Buck et al. study "inflation in models with conformally coupled scalar fields" in that action and find Higgs inflation there "incompatible with the measured value of the top quark mass".
- **Consequence.** If NTE closes route B through a spectral action whose finite part carries the Standard Model Higgs, which is the construction whose a₄ = 0 Part 3 already imports, the same action sets **ξ_H at the conformal value**. That forbids ξ_H ≫ 1.
  - **Route B and exit (a) cannot both be taken.**
  - Caveat, stated: NTE derives its gauge group octonionically, not from the Chamseddine–Connes finite triple (Part 2 §8.5). So route B *might* be built Φ-only, with no Higgs in it. The deposit does not say which, and that choice now decides the matter.

**3.4 D5 status: fires in modified form.** It is not that "the absence damages ξ = 1/6". It is that **the only principle-shaped candidate for ξ = 1/6, applied consistently, disqualifies exit (a)**. Adopting (a) therefore commits the corpus to a Φ-only route B, or to leaving ξ = 1/6 permanently at "motivated". The ratification is not weakened below where it already sat, but its path upward narrows.

---

## 4. The cheaper-candidate question: C-term

- **No other scalar is available.** The deposit's scalars are Φ_NTE (assigned 1/6) and the Standard Model Higgs.
  - μ(N) is a Lagrange multiplier, not a propagating field (C8 eq. (3)).
  - The mirror orientation is the same manifold, not an independent field (Part 1 §VI).
  - Fermions carry no ξ.
- **One omitted term, R² (Starobinsky), needs its own gate run.**
  - It adds one coefficient and no matter field.
  - The same α = 1 attractor gives the same (n_s, r) to leading order: 0.965 and 0.0035 at N* = 55.
  - It is **unitary up to M_Pl**, which is the healer result read from the other side.
  - It leaves the Higgs portal and embedding untouched.
  - The corpus imported Starobinsky numbers before (Part 3: C17 "replac[ed] imported Starobinsky numbers"; C8 F4's P4 profile).
- **It is not free of G-3.** Scalaron reheating into Higgs quanta goes as (1 − 6ξ_H)² (background knowledge), so it too needs ξ_H ≠ 1/6. But it needs only an O(1) departure, not ~10⁴.
- **Assessment:** on the disqualifier list as written it is exposed to D2 not at all, D4 less, and D5 more weakly than exit (a). **I name it for AC's list as (a′); I do not advocate it.**

---

## 5. Cross-lane flags (outside my gates, found while reading)

**5.1 G-1/D1 risk, the most serious item here.** Part 2 §8.1 (read): "every Standard-Model gauge boson … **and the Higgs** come into existence only with t."
- A Higgs-inflation no-boundary birth needs the Higgs **on the Euclidean saddle** at large field value, since the Hartle–Hawking–Hertog instanton carries the inflaton. NTE's Euclidean section, by §8.1, contains no Higgs.
- So the handover at ȧ = 0 cannot inherit ρ + 3p < 0 from a Higgs field value the saddle never had. **The Higgs's large-field initial condition at gauge birth is unsupplied.**
- Either §8.1 is amended to let the Higgs exist pre-temporally, which touches the gauge-birth ontology, or D1 fires.
- **Starobinsky (a′) does not have this problem.** R² is geometric and present on the Euclidean section.

**5.2 G-5 premise misread.** The directive says "the **Higgs portal** that already sets embedding depth (Part 1 §III; Part 2 §8.2–8.3)."
- Part 1 §III (read) sets embedding depth by the **Yukawa coupling to the Standard Model Higgs**. Part 2 §8.2–8.3 do not mention the portal.
- The portal (−2e|H|²Φ²) lives in C9 eq. (1) and Part 1 §2.3's last sentence.

**5.3 G-5 portal bound.** If Φ_NTE tracks the constraint during inflation, then Φ² = H/β gives Φ ≈ 7.9×10²⁹ GeV ≈ 3×10¹¹ M.
- Keeping the portal-induced Higgs mass below H requires **e ≲ βH/2 ≈ 1.7×10⁻³⁴**.
- The deposit says only "constrained to be small" (C9 §1), and that is from low-energy phenomenology at Φ = v_EW.
- The bound is ~32 orders tighter and belongs in G-5.

**5.4 Top mass.** Buck et al. (2010) found spectral-action Higgs inflation incompatible with m_t. Masina–Quiros (2024, abstract read) find Higgs inflation viable with electroweak metastability at the PDG m_t ≈ 172.5 GeV, with smaller ξ. **The dispute is live in both directions; pick neither.**

---

## 6. Summary for arbitration

| Gate | Jammer finding | Disqualifier |
|---|---|---|
| G-2 | Inside validity during inflation; outside during preheating by ~470× (λ = 0.01). The cure is R², i.e. a new degree of freedom. Palatini escapes G-2 but costs r ~ 10⁻¹². | **D2 fires at reheating.** Carry it as a known defect. |
| G-3 | ξ_H is a fitted input. The only candidate principle (route B via a spectral action) sets ξ_H at the conformal value. "Minimal by omission" is corrected to "unassigned". | **D5 fires in modified form.** D3 clause 2 fires literally. |
| Cheaper | No other scalar. The R² term (a′) is a fewer-exposure competitor. | — |
| Cross-lane | Part 2 §8.1: no Higgs on the Euclidean saddle, so the initial condition is unsupplied. | **D1 risk for (a); none for (a′).** |

— Jammer, 2026-09-26.
