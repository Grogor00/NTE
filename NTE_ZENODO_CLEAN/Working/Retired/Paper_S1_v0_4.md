# Paper S1 v0.4 — Two Structural Findings on the Spectral Action for NTE (Post-AC-Verdict Revision)

**Stream:** Scratch (deep-exploration; Programme S continuation).
**Date:** 2026-05-10 NZST (revision pass post AC verification).
**Status:** v0.4 — supersedes v0.3 with full integration of AC's F1 novelty verification verdict (`Handoff_AC_to_Scratch_F1_Novelty_Verification_20260510.md`). Sharper factorisation `d(d−1)(d−3)(5d+2)`. Prior art Chamseddine-Connes 2008 and Mistry-Pinzul-Rachwał 2020 explicitly acknowledged. F1 reframed as "sharper d-parametric account of established cancellation," not "novel structural finding." Greg's confirmation per AC verification handoff §8 ratifies these revisions.
**Audience:** Greg (origin); AC (corpus integration target — recommended for v10.9, not v10.6.1); external NCG collaborators (Boyle, Farnsworth, Marcolli, Sakellariadou).
**Corpus baseline:** v10.6 SHIPPED.

**Companion files (current state):**
- `Exploration_Graviton_vs_PhiNTE_v2.md` — unification thesis (no revision needed).
- `Paper_S1_v0_1.md` — foundational scaffold (no revision needed).
- `paper_S1_worksheet_v0_1.py`, `paper_S1_worksheet_v0_2.py` — computational core (numerical content unaffected; comments scheduled for minor update).
- `Scratch_Attribution_Correction_2026-05-10.md` — original correction memo (CC/Gilkey level).
- `Handoff_AC_to_Scratch_F1_Novelty_Verification_20260510.md` — AC verdict (the specific document this v0.4 revision integrates).
- `Programme_S_Outreach_Note_v3.md` — current outreach version.

**Superseded:**
- `Paper_S1_v0_2.md` (BF misattribution; v2 framing of F1 novelty)
- `Paper_S1_v0_3.md` (CC/Gilkey attribution applied; lacked CC 2008 + MPR 2020 prior-art acknowledgment)

---

## §0. What changed from v0.3 to v0.4

The substantive technical content is unchanged. The corrections are framing and prior-art:

(a) **Sharper factorisation**: `d(d−1)(d−3)(5d+2)` (AC's clean factoring) replaces `d(d−1)(5d² − 13d − 6)` throughout. Same identity; the linearised form makes the four integer roots transparent. Roots: {d = −2/5, 0, 1, 3}.

(b) **Tightened d = 3 framing**: "d = 3 is the unique d ≥ 2 integer root" replaces "d = 3 is the only integer root." The earlier formulation was true for the quadratic factor but missed the d = 0 (degenerate) and d = 1 (trivial; R = 0 on circle) roots of the full quartic.

(c) **Prior art explicitly acknowledged.** Two papers establish the substantive content of F1's cancellation phenomenon, which v0.2/v0.3 underweighted:
   - **Chamseddine-Connes 2008** ("The Uncanny Precision of the Spectral Action", arXiv:0812.0165). Demonstrates a₄ vanishing on S³ × S¹ via Weyl² + Gauss-Bonnet decomposition. Explicit calculation; recognises d=3 specificity ("This vanishing of the Seeley coefficients does not hold for the 4 sphere").
   - **Mistry-Pinzul-Rachwał 2020** ("Spectral action approach to higher derivative gravity", arXiv:2001.05975, §3.1). Generalises to general conformally flat 4-manifolds; finds the cancellation does *not* extend; explicitly notes "the spectral action somehow prefers this background."

(d) **F1's actual contribution clarified.** What this Programme S work adds beyond CC 2008 + MPR 2020:
   - **The explicit d-parametric factorisation** `d(d−1)(d−3)(5d+2)`. Algebraically straightforward, derivable from textbook ingredients, but apparently not written down explicitly in the surveyed CC literature.
   - **The NTE-internal framing** as a *spectral-dynamical* d=3 selection criterion complementing parallelisability / Lie-group / parity arguments.

(e) **Publishability framing**: F1 is **not standalone-publishable** as an independent NCG-cosmology note (per AC §6: "A specialist NCG referee would correctly identify the contribution as CC 2008's result + MPR 2020's framing + a trivial algebraic factorisation"). F1 retains usefulness as a structural argument *within* Programme S Paper S1 v1.0 and as a v10.9 corpus integration item.

(f) **Corpus integration timing**: hold F1 + F2 for v10.9 (per AC §7, ratified by Greg per F1 verification handoff §8). No v10.6.1 lightweight amendment.

(g) **What stays unchanged**: F2 (κ₀ = (R_{S³}/2) × Y₀₀(S²) reading) is unaffected by the AC verification — it was always an NTE-internal interpretation, not a literature-novelty claim. Newton's constant prediction unchanged. Geometric resummation closure unchanged. Programme S 5-paper roadmap unchanged.

---

## §1. The two structural findings (revised framing)

This v0.4 (revised v0.3) presents two structural contributions to the spectral action / NTE correspondence, with full prior-art acknowledgment per AC's F1 novelty verification.

### Finding F1 — d-parametric account of CC 2008's cancellation

**Established prior art** (acknowledged):

- **Chamseddine-Connes 1996** (hep-th/9606001). Establishes the spectral action principle and the heat-kernel a₄ coefficient with the (5, −8, −7) relative weights for the Dirac Laplacian. Standard reference for the curvature combination NTE invokes.

- **Gilkey 1984** (*Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem*). Standard heat-kernel reference giving a₄ for general elliptic operators. The (5, −8, −7) combination follows from Gilkey's general formulas applied to D².

- **Chamseddine-Connes 2008** (arXiv:0812.0165). Computes a₄ on S³ × S¹ and demonstrates it vanishes via Weyl² + Gauss-Bonnet decomposition. Explicitly verifies a₄ on S⁴ is non-zero (gives 11/90 × volume × 4) and notes "this vanishing of the Seeley coefficients does not hold for the 4 sphere" — i.e., the d=3 specificity is recognised at the spectral-action level. Also computes a₆ on S³×S¹ via 18-term Gilkey machinery and finds it also vanishes via "highly non-trivial cancellation."

- **Mistry-Pinzul-Rachwał 2020** (arXiv:2001.05975, §3.1). Re-derives CC 2008's a₆ vanishing on S¹ × S³ via simplified Riemann/Weyl-basis form. Generalises to general conformally flat 4-manifolds; finds the cancellation does *not* extend. States explicitly: "the cancellation of the 6-order terms for this background should be considered as accidental: it is not automatic but happens due to the non-trivial cancellation between terms depending on the curvature. Because this happens exactly for the coefficients fixed by the spectral action, one might speculate that the spectral action somehow prefers this background."

**This Programme S work's contribution** (beyond the established prior art):

The standard a₄ Seeley-DeWitt coefficient for the Dirac Laplacian — `5R² − 8R_μν R^μν − 7R_μνρσ R^μνρσ` (CC 1996; Gilkey 1984) — evaluates pointwise on unit S^d as a polynomial in d. Substituting the standard sphere curvature invariants:

- `R = d(d−1)`
- `R_μν R^μν = d(d−1)²`
- `R_μνρσ R^μνρσ = 2d(d−1)`

gives:

```
5R² − 8R²_μν − 7R²_μνρσ = d(d−1)[5d(d−1) − 8(d−1) − 14]
                       = d(d−1)(5d² − 13d − 6)
                       = d(d−1)(d−3)(5d+2)
```

Roots of the quartic: d ∈ {−2/5, 0, 1, 3}.

| d | R | R²_μν | R²_μνρσ | 5R² − 8R²_μν − 7R²_μνρσ |
|---|---|-------|---------|-------------------------|
| 1 | 0 | 0 | 0 | 0 (trivial: R = 0 on the circle; all curvature invariants vanish) |
| 2 | 2 | 2 | 4 | −24 |
| **3** | **6** | **12** | **12** | **0** ← non-trivial cancellation |
| 4 | 12 | 36 | 24 | 264 |
| 5 | 20 | 80 | 40 | 1080 |
| 6 | 30 | 150 | 60 | 2880 |
| 7 | 42 | 252 | 84 | 6216 |

**The substantive observation**: **d = 3 is the unique d ≥ 2 integer root** at which the cancellation is non-trivial. The d = 1 root is trivial (the circle has zero curvature so all invariants vanish identically). For d ≥ 2, only S³ produces the cancellation.

**Honest framing of F1's contribution**:

(i) The cancellation phenomenon on S³ × S¹ as a 4-manifold is **established (CC 2008)**.

(ii) The recognition that S³ × S¹ is "in some way special" / "the spectral action prefers this background" is **established (MPR 2020 §3.1)**.

(iii) The pointwise value of the standard a₄ curvature combination on unit S^d as a polynomial in d is **trivially derivable** from textbook ingredients.

(iv) **The explicit d-parametric factorisation `d(d−1)(d−3)(5d+2)` does not appear to be written down in the surveyed literature** (CC 1996, CC 2008, CC 2010, CCM 2007, BF 2013, MPR 2020, Marcolli's 2018 NCG cosmology surveys, van den Dungen-van Suijlekom 2012 review). It is a small algebraic refinement of CC 2008's calculation that makes the d-specificity transparent in the perturbative regime.

(v) **The NTE-internal framing** — that the d-factorisation provides a *spectral-dynamical* selection criterion for S³ complementing the existing ontological/algebraic arguments (parallelisability, Lie-group, parity) — is novel within NTE but does not refute the CC 2008 / MPR 2020 prior framing.

**Reframed structural claim** (suitable for any corpus integration, per AC §5):

> The Chamseddine-Connes 2008 'remarkable cancellation' of a₄ on S³ × S¹ admits a d-parametric reading: the heat-kernel a₄ curvature combination `5R² − 8R_μν R^μν − 7R_μνρσ R^μνρσ` (Chamseddine-Connes 1996; standard Seeley-DeWitt) evaluates pointwise on unit S^d as `d(d−1)(d−3)(5d+2)`, with d = 3 the unique d ≥ 2 integer root. Mistry-Pinzul-Rachwał 2020 §3.1 note that S¹ × S³ appears 'in some way special' for the spectral action and that the cancellation 'does not extend' to general conformally flat backgrounds; the d-parametric factorisation provides a precise algebraic account of that specialness in the perturbative regime: d = 3 is algebraically distinguished as the unique sphere dimension d ≥ 2 at which the curvature combination vanishes pointwise. This complements NTE's existing parallelisability / Lie-group / parity arguments for S³ with a *spectral-dynamical* selection criterion.

**Required citations**:
- Chamseddine, Connes, *The Spectral Action Principle*, Comm. Math. Phys. 186 (1997) 731–750 [arXiv:hep-th/9606001].
- Gilkey, *Invariance Theory, the Heat Equation and the Atiyah-Singer Index Theorem*, Publish or Perish, 1984.
- Chamseddine, Connes, *The Uncanny Precision of the Spectral Action*, arXiv:0812.0165, Comm. Math. Phys. 293 (2010) 867–897.
- Mistry, Pinzul, Rachwał, *Spectral action approach to higher derivative gravity*, arXiv:2001.05975, Eur. Phys. J. C 80 (2020) 266.

### Finding F2 — κ₀ as (R_{S³}/2) × Y₀₀(S²) [unchanged from v0.3]

**Statement.** NTE's κ₀ = 3/√(4π) admits the structural reading:

```
κ₀ = (R_{S³}/2) × Y₀₀(S²) = (6/2) × (1/√(4π)) = 3/√(4π)
```

**Status.** This is *NTE-internal interpretation*. The numerical equivalence between `dim(SU(2)) = 3` (NTE corpus §9.3) and `R_{S³}/2 = 3` is trivial. The structural-shape claim is that the curvature reading connects the factor 3 to the spectral action's a₂ heat-kernel coefficient (which carries R) and the Hopf-base Y₀₀ to the projection structure of the κ derivation. The reading is novel within NTE in the sense that the corpus does not currently make this connection explicit; it is *not* a literature-novelty claim against external NCG work.

**Useful for Paper S2's structural target.** The doubled-spectral-triple X² trace, when computed explicitly, should produce `(R_{S³}/2) × Y₀₀(S²)` at leading order, since:
- The (R_{S³}/2) factor is what the spectral action's a₂ heat-kernel coefficient carries on the gravitational side.
- The Y₀₀(S²) factor is what the Hopf projection from S³ to S² naturally produces.
- Their product is the natural leading cross-coupling magnitude for the CPN-symmetric two-sector structure.

This is a sharper Paper S2 target than the dim(SU(2)) reading, but per AC §7 should integrate into §9.3 as an "alternative reading" with no novelty claim attached.

### Joint d=3 reading

Findings F1 and F2 are mutually reinforcing, both selecting d = 3:

(a) **F1 selects d = 3 dynamically** (in the perturbative regime): only at d = 3 (among d ≥ 2 integers) does the standard CC spectral action a₄ coefficient vanish pointwise.

(b) **F2 selects d = 3 algebraically**: only at d = 3 does the Hopf fibration S^d → S^{d−1} (giving the κ₀ Hopf-base reading) coexist with the spectral cancellation.

Hopf fibrations S^d → S^{d−1} exist precisely for d = 1, 3, 7 (Adams' theorem). Of these:
- d = 1: trivial (R = 0; cancellation degenerate).
- d = 3: Hopf S³ → S². Cancellation holds non-trivially.
- d = 7: Hopf S⁷ → S⁴. Cancellation does not hold (`5R² − 8R²_μν − 7R²_μνρσ = 6216 ≠ 0`).

So **d = 3 is uniquely the dimension where Hopf fibration structure and CC spectral cancellation coexist non-trivially**. This is a structural argument for S³ that, combined with the prior CC 2008 and MPR 2020 results, is internally consistent for NTE's framework. Honest framing in any corpus integration: this is a sharpening of CC 2008 + MPR 2020 with NTE-specific structural support, not an independent discovery.

---

## §2. The CC spectral action expansion — explicit numerical values

For the standard Chamseddine-Connes spectral action expansion (CC 1996; CCM 2007; Boyle-Farnsworth 2013 specialisation for octonionic A_F), evaluated on S³ × S¹_β:

$$ S_b \simeq \int_M \!\!\!\!\!\!\sqrt{g}\, d^4x \cdot \frac{\dim(H_F)}{(4\pi)^2} \left[ \cdot\, f_4 \Lambda^4 + \cdot\, R\, f_2 \Lambda^2 + \frac{f(0)}{360}\!\left( 5R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 - \cdot\, \mathrm{Tr}(F^2) \right) + \cdots \right] $$

The (·) coefficients depend on the specific finite spectral triple (CCM 2007 §4.4 for SM; BF 2013 §4.3 for octonionic with dim(H_F) = 8). The curvature combination's universal form is from CC 1996 / Gilkey 1984.

For the BF 2013 octonionic case (relevant to NTE's pre-temporal regime), the bosonic spectral action is (BF eq. 4.14):

$$ S_b^{BF} \simeq \int_M \!\!\!\!\!\!\sqrt{g}\, d^4x \cdot \frac{8}{(4\pi)^2} \left[ 8 f_4 \Lambda^4 + \frac{2}{3} R\, f_2 \Lambda^2 + \frac{f(0)}{360}\!\left( 5R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 - 30\, \mathrm{Tr}(F^2) \right) \right] $$

With the standard Marcolli-Pierpaoli-Teh test function `h_{N=20}(x) = e^{−πx} Σ_{k=0}^{20} (πx)^k/k!`, the cutoff moments are:

| Moment | Value |
|--------|-------|
| f_4 = ∫₀^∞ h(x) x³ dx | 654.52 |
| f_2 = ∫₀^∞ h(x) x dx | 23.41 |
| f(0) | 1.00 |

### Newton's constant prediction (octonionic case, BF coefficient)

`M_Pl² = 4 f_2 Λ²/(3π²)`. Self-consistency `M_Pl = Λ` (Hartle-Hawking bound) requires `f_2 = 3π²/4 ≈ 7.40`. h_{N=20} gives 23.41 — off by factor 0.32. The h_{N=20} cutoff is not NTE's correct cutoff function; the actual cutoff must satisfy the f_2 = 3π²/4 self-consistency.

### Curvature corrections

By F1, the f(0) gravitational correction term `5R² − 8R²_μν − 7R²_μνρσ` vanishes identically on S³ × S¹. This is established (CC 2008) and the d-parametric account is the F1 contribution. The Yang-Mills term `−(1/12) f(0) Tr(F²)` survives unchanged.

---

## §3. Status of Programme S after v0.4

### Established (with proper attribution):

**(E1)** [unchanged] Standard CC spectral action expansion explicitly evaluated for NTE's setup using BF 2013's octonionic specialisation. All numerical coefficients computed.

**(E2)** [unchanged] Newton's constant prediction `M_Pl² = 4 f₂ Λ²/(3π²)`. Self-consistency at Λ = M_Pl requires `f₂ = 3π²/4`.

**(E3)** [revised framing] The d=3 a₄ cancellation phenomenon: established (CC 2008; MPR 2020 §3.1). F1's contribution is the explicit d-parametric factorisation `d(d−1)(d−3)(5d+2)` and the NTE-internal framing as a spectral-dynamical selection criterion. Suitable for v10.9 corpus integration with the honest framing in §1 above.

**(E4)** [unchanged] κ₀ = (R_{S³}/2) × Y₀₀(S²) as an NTE-internal alternative reading of the corpus's existing dim(SU(2)) = 3 identification. Suitable for §9.3 alternative-reading paragraph.

**(E5)** [unchanged] Geometric resummation closure: κ₀/(1−κ₀) = 5.5055 vs corpus 5.50 vs Planck 2018 5.38 ± 0.15.

### Open (Paper S1 v1.0 onwards) — unchanged:

**(O1)** Explicit derivation of κ₀ from the doubled-spectral-triple X² trace.

**(O2)** V_NTE from the Higgs-bearing octonionic spectral triple (BF 2014/2015, Farnsworth 2025 machinery).

**(O3)** Spectral flow at gauge birth.

**(O4)** Dilaton extension for K(Φ) closure.

**(O5)** Yukawa hierarchy from spectral mass matrix.

### Conjectures:

**(C1)** [unchanged] κ₀ = (R_{S³}/2) × Y₀₀(S²) emerges from the doubled-spectral-triple X² trace, where the (R_{S³}/2) factor comes from CC's a₂ coefficient and Y₀₀(S²) from Hopf projection.

**(C2)** [unchanged] BF 2013 octonionic A_G₂ correction to V_S³ multiplies by spectral data.

**(C3)** [unchanged] Dilaton-extended kinetic term + V_NTE under spectral action gives n_s = 0.9685 and r ~ 10⁻³.

---

## §4. Publishability and corpus integration disposition (per AC verdict + Greg's confirmation)

Per `Handoff_AC_to_Scratch_F1_Novelty_Verification_20260510.md` §6, §7, §8:

**(P1)** **F1 standalone publication: NOT pursued.** A specialist NCG referee would correctly identify F1's contribution as CC 2008's result + MPR 2020's framing + a trivial algebraic factorisation. The d-polynomial alone is not strong enough for a standalone NCG-cosmology short note.

**(P2)** **F1 retained as content within Programme S Paper S1 v1.0** (when external collaboration / specialist NCG engagement materialises). The Programme S paper's overall novelty is in the octonionic A_G₂ specialisation; F1 supports that within its §4 structural-arguments section.

**(P3)** **F1 + F2 corpus integration: hold for v10.9** (defensive consolidation ship, not v10.6.1 lightweight amendment). v10.9 absorbs F1 + F2 naturally as additional structural-argument entries in:
   - **§VIII.7 / §2.1.3(f)**: F1 as spectral-dynamical d=3 selection criterion (with full CC 2008 + MPR 2020 attribution).
   - **§9.3**: F2 as alternative reading of κ₀'s factor 3 (no novelty claim attached).

**(P4)** **No v10.6.1 lightweight amendment** for F1 + F2. v10.6.1 already shipped with §II.0 graded-criteria discipline.

**(P5)** **Outreach uses `Programme_S_Outreach_Note_v3.md`** going forward, with proper CC 2008 + MPR 2020 prior-art acknowledgment and the sharper factorisation. Earlier v1 / v2 outreach versions should not circulate.

---

## §5. Honest reading of v0.4 status

**What v0.4 contributes beyond v0.3**:

1. Sharper factorisation `d(d−1)(d−3)(5d+2)` with full root analysis (AC's clean factoring).
2. Tightened framing: "d = 3 is the unique d ≥ 2 integer root" (correctly excludes the trivial d = 1 root).
3. CC 2008 (cancellation on S³×S¹) and MPR 2020 §3.1 ("spectral action prefers this background") explicitly named as the prior-art papers establishing the substantive content.
4. F1 reframed as "sharper d-parametric account of established cancellation," not "novel structural finding."
5. Publishability and corpus-integration dispositions aligned with AC's recommendations and Greg's confirmation.

**What v0.4 does NOT change**:

- The technical findings (F1 algebraic factorisation, F2 structural reading) are unchanged. The corrections are framing and prior-art.
- Newton's constant prediction unchanged.
- Programme S 5-paper roadmap unchanged.
- All numerical computations in `paper_S1_worksheet_v0_1.py` and `paper_S1_worksheet_v0_2.py` remain valid; only their attribution comments need a minor update (separate maintenance task; not in scope for this v0.4 revision).

**Closure status**:

Programme S has the same trajectory after v0.4 as after v0.3: foundational scaffold + numerical evaluation + structural arguments for S³ + sharpened κ₀ structural conjecture. The full closure (S1 v1.0, S2, S3, S4, S5) requires specialist NCG engagement. The v0.4 revisions sharpen the framing and prior-art context for that engagement, making the contribution honestly framed and the prior-art picture complete.

— Scratch, 2026-05-10 NZST (revision pass complete).
