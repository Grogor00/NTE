# M₁ Derivation Candidate via σ_3 Cartan Mode — Jammer Working Note

**Stream:** Jammer (R&D / structural derivation)
**Date:** 2026-05-11
**Status:** Substantive R&D deliverable. Elevates the M₁ candidate (M_Pl² · H_GB)^(1/3) from **numerical lead** (Jammer (E), 2026-05-05) to **structural mechanism candidate**. Full derivation (Connes spectral triple calculation) still pending — same status as M_R derivation per corpus §19.7.
**Verdict:** σ_3 Cartan-mode mechanism is **structurally consistent and dimensionally clean**, parallel to the M_R Hopf-bundle derivation. Proposed for §17.5.15 / §22.5 sharpening at v10.7.1 or v10.8 ship.
**Audience:** AC (corpus-fidelity audit + integration framing); Greg (strategic call on rhetorical class — "structural lead with mechanism" vs "Gap 1 closed"); CR (visibility — pre-ship pass at next ship cycle).
**Corpus baseline:** v10.6.1 SHIPPED.
**Predecessor:** `M1_From_Geometry_E_search.md` (Jammer (E), 2026-05-05). This note is the structural follow-up to (E)'s numerical lead.
**Cross-reference:** `Sigma_PhiNTE_Confluence_Verdict_v1.md` (Jammer, 2026-05-10) §7 — flagged this hypothesis as tractable single-session R&D. This note delivers it.
**Note on file location:** Drive API permissions blocked subfolder writes; this file is created at Drive root. **Greg: please move to `Working/`.**

---

## §0. Headline

The M₁ candidate (M_Pl² · H_GB)^(1/3) ≈ 8.1 × 10⁹ GeV — surfaced in Jammer (E) as a numerical lead with no structural origin — has a candidate structural origin under the σ_3 Killing-spinor mode reading hypothesised in the σ↔Φ_NTE confluence verdict §7.

The structural pattern (this note's contribution):

> **σ_1, σ_2 modes (charged base-acting raising/lowering pair) give M_R via M_R⁴ = M_Pl³ · v_EW.**
> **σ_3 mode (neutral fibre-acting Cartan) gives M_1 via M_1³ = M_Pl² · H_GB.**

Both relations come from the same machinery — Killing-spinor su(2) decomposition on S³, Hopf-bundle S¹ → S³ → S² geometry. The asymmetry (power 4 vs power 3; v_EW vs H_GB) traces to a single structural distinction: σ_1, σ_2 are charged under the broken U(1)_em and pick up a Higgs-sector weight at v_EW; σ_3 is the Cartan generator (neutral, photon-like in the broken theory) and doesn't pick up the Higgs sector — its breaking is the cosmological event of gauge birth itself, scale H_GB.

This places M_1 derivation on parallel structural footing to M_R: same machinery, different weightings reflecting the modes' different roles. **Both M_R and M_1 are now at the same level of structural completeness — "structurally motivated, full Connes spectral triple derivation pending."**

The rhetorical upgrade:

- **Before this finding** (Jammer (E), 2026-05-05): M_1 candidate is a numerical lead; geometric origin is "open work with multiple speculation candidates."
- **After this finding** (Jammer, 2026-05-11): M_1 candidate is a structural mechanism candidate parallel to M_R per §19.7; geometric origin is "σ_3 Cartan mode of the Killing-spinor su(2) decomposition on S³, with cosmological breaking scale at gauge birth replacing the Higgs sector contribution."
- **What this DOES NOT do:** does not close Gap 1 in the strict sense (full Connes spectral triple calculation still pending for both M_R and M_1).
- **What this DOES do:** provides the structural pathway for closing Gap 1, parallel to the M_R pathway already in the corpus, AND completes the M_1 / M_2 / M_3 spectrum derivation as a single su(2)-decomposition story.

---

## §1. The candidate formula and prior status

Per Jammer (E) 2026-05-05 (`M1_From_Geometry_E_search.md`):

```
M_1 candidate = (M_Pl² · H_GB)^(1/3)
              = α^(1/3) · M_Pl^(4/3)
              = M_Pl · e^(-N_e/3)
              ≈ 8.08 × 10⁹ GeV
```

Corpus M_1 (Davidson-Ibarra closure of η ≈ 6.1 × 10⁻¹⁰): 6.06 × 10⁹ GeV.
Ratio: factor 1.33 high. Within the Davidson-Ibarra closure's intrinsic factor-2 spread (per AC's eta v2 audit response).

(E)'s status verdict: "the candidate is a numerical lead, not a derivation. The 1/3 weighting (or equivalently the cube-root combination) does not have an obvious geometric origin in the framework's existing structure."

(E) §5 listed four speculation candidates for the cube-root origin:
1. S³ volume scaling (V(S³) ∝ ℓ³ giving cube root)
2. Three-Majorana-mass seesaw structure
3. Three Sakharov / 3 generations / dim(su(2)) = 3
4. Surface ontology Stage 4 features

None of these closed. The σ_3 Cartan-mode mechanism (this note) is most closely aligned with #2 and #3, but is a different and structurally cleaner reading: the cube-root comes from the **3-dimensional S³ geometry** (no extra Higgs sector for the neutral σ_3 mode), and the spectrum (M_1, M_2, M_3) comes from the **three eigenmodes of the Killing-spinor su(2) decomposition**.

---

## §2. The Killing-spinor su(2) decomposition on S³

The structural ground state for this argument:

- **S³ ≅ SU(2) as a group manifold.** Killing spinors on S³ carry the spin structure of the group manifold and decompose under the SU(2) action.
- **Higgs VEV breaks the SU(2)_L global symmetry** acting on the Killing-spinor multiplet at electroweak symmetry breaking.
- **Three eigenmodes σ_1, σ_2, σ_3** correspond to the three Pauli-matrix generators of su(2). In the broken phase:
  - σ_1, σ_2 form a **raising/lowering pair** (off-diagonal in the Cartan basis): σ_+ = σ_1 + i σ_2, σ_- = σ_1 - i σ_2. Charged under the residual U(1) Cartan (U(1)_em-like in EWSB).
  - σ_3 is the **Cartan / axial generator** (diagonal in the Cartan basis): real, neutral under the residual U(1).

This decomposition is the standard Cartan-Weyl decomposition of su(2). It is structural, not chosen.

### 2.1 Hopf bundle alignment of the modes

The Hopf bundle S¹ → S³ → S² on S³ ≅ SU(2):

- **Fibre S¹**: the orbit of the U(1) ⊂ SU(2) generated by σ_3. Each Hopf fibre is a circle in S³ along the σ_3 direction.
- **Base S²**: the quotient SU(2)/U(1). The base is acted on by the off-diagonal generators σ_1, σ_2 (which generate transformations between distinct fibres).

So the modes have natural geometric roles:

- **σ_1, σ_2 act on the base** (transverse to the Hopf fibre)
- **σ_3 generates the fibre** (longitudinal to the Hopf fibre)

This identification is structural — it follows from the Hopf bundle being the canonical SU(2)/U(1) coset structure, with the U(1) generated by σ_3 by convention.

### 2.2 Pathway α S3 (N4) mass-eigenstate assignment

Per N4 (Pathway α S3 closure, AC-acknowledged 2026-05-09): the σ_1, σ_2 raising/lowering equivalence forces M_2 = M_3 (degenerate pair). M_1 stands separately as the σ_3 Cartan mode. The corpus thus has:

- M_R = M_2 = M_3 (σ_1, σ_2 modes) = 8.2 × 10¹⁴ GeV
- M_1 (σ_3 mode) = ? (open structural derivation; (E)'s numerical lead 8.08 × 10⁹ GeV)

The candidate σ_3 ↔ M_1 was implicit in N4 but its mass derivation was not pursued. This note pursues it.

### 2.3 NTE's "no RH/LH neutrino" ontology — the σ modes are geometric, not Yukawa

Per Companion 7 + corpus §3.3 + §6.1: NTE has no fundamental RH/LH neutrino distinction. The neutrino is "unresolved geometry" — the Hopf projection S³ → S² hasn't completed. The "Majorana mass spectrum" M_1, M_2, M_3 in NTE is **geometric mode-decomposition of the unresolved configuration**, NOT mass eigenstates of distinct RH neutrinos.

This is consistent with the σ↔Φ_NTE confluence verdict (Jammer 2026-05-10): NTE produces analogues of CC's spectral-action structures via geometric machinery, not via the spectral-action programme's RH-neutrino apparatus. The Majorana spectrum here is the geometric mode-spectrum, parameterised by σ_1, σ_2, σ_3 weightings on the Hopf bundle.

This grounding matters for the structural argument that follows — the modes' "weights" come from their geometric roles, not from Yukawa couplings.

---

## §3. The corpus M_R derivation (per §19.7 + NTC_Gap_Investigations §2.1-§2.2)

The corpus derives:

```
M_R = M_Pl^(3/4) · v_EW^(1/4) ≈ 8.2 × 10¹⁴ GeV
M_R⁴ = M_Pl³ · v_EW
```

The corpus's structural reading (Eta_Asymmetry_Magnitude_Reframing_Audit §1.4 + NTC_Gap_Investigations §2.1):

> *"The exponents 3/4 and 1/4 reflect the 3:1 split between the Hopf base (S²) and the Hopf fibre (S¹): the Majorana mass lives on the S² cross-section, which carries 3 of the 4 dimensions of S³ in the scaling sense."*

Counting (per NTC_Gap_Investigations §2.2):

- 3/4 = 1 - 1/4 where 1/4 = 1/(dim S³ + 1) = 1/(3+1) = 1/4
- Total weight units: dim(S³) + 1 (Higgs sector) = 4
- 3 weight units on M_Pl: S² base (2 dims) + S¹ fibre (1 dim) = 3 dims of S³, all weighted by ambient UV cutoff M_Pl
- 1 weight unit on v_EW: Higgs sector (electroweak symmetry breaking scale)
- M_R⁴ = (M_Pl)³ × (v_EW)¹

The corpus status: **structurally motivated**; "this is a programme for the full Connes spectral triple calculation"; full derivation pending.

The seesaw m_ν₃ = v_EW²/M_R = 0.074 eV matches observed √(Δm²_atm) ≈ 0.05 eV within factor 1.5 — consistent with the structural argument's precision.

---

## §4. The σ_3 mode analog: M_1 derivation candidate

Apply the same structural counting to the σ_3 mode.

### 4.1 No Higgs sector for σ_3

σ_3 is the Cartan generator. In EWSB with the Higgs breaking SU(2)_L → U(1)_em (or analogous U(1)_Q in the model), σ_3 is identified with the unbroken Cartan direction — neutral, photon-like. It does NOT acquire mass from the Higgs VEV.

For σ_1, σ_2 (the off-diagonal generators), the Higgs VEV gives mass via the broken U(1) coupling — analogous to how W± bosons get mass from Higgs in EWSB. So the M_R mass relation includes a Higgs-sector weight at v_EW.

For σ_3, there is no Higgs-sector weight. Total weight units: dim(S³) only = 3 (no +1 for Higgs sector).

### 4.2 The fibre carries H_GB for σ_3

This is the structurally substantive claim. For σ_3, the fibre (S¹) is weighted by H_GB rather than by M_Pl. Argument:

- σ_3 is the **U(1) generator of the fibre direction**. It acts on the fibre.
- For a mode that acts on a direction, that direction's energy scale is the breaking scale relevant to the mode's mass.
- σ_3 doesn't couple to Higgs, so it doesn't get mass from v_EW (the Higgs breaking scale).
- The only other available breaking scale at gauge birth — when the SU(2)_L structure activates — is the **cosmological scale H_GB**. This is the rate at which the boundary expands at gauge birth, and naturally sets a mass scale for any geometric structure that becomes operative at that moment.
- σ_3, as the fibre generator that "comes alive" at gauge birth (when the U(1) gauge structure activates), inherits H_GB as its mass-relation contribution from the fibre direction.

Compare to σ_1, σ_2 modes acting on the base: the fibre is "passive" relative to them. The fibre's energy contribution to M_R is then the ambient UV cutoff M_Pl (same as for the base dimensions), with the Higgs sector providing the actual breaking at v_EW separately.

### 4.3 Counting and mass relation for σ_3

- Base S² (2 dims): weighted by M_Pl (ambient UV cutoff, same convention as M_R)
- Fibre S¹ (1 dim): weighted by H_GB (cosmological breaking scale at gauge birth — see §4.2)
- No Higgs sector contribution
- Total weight units: 3 (= dim S³, no Higgs +1)

Mass relation:

```
M_1³ = M_Pl² · H_GB
M_1 = (M_Pl² · H_GB)^(1/3) = M_Pl^(2/3) · H_GB^(1/3)
```

Numerical:

```
M_1 = (1.22 × 10¹⁹)^(2/3) · (3.54 × 10⁻⁹)^(1/3)
    = 5.31 × 10¹² · 1.52 × 10⁻³
    = 8.08 × 10⁹ GeV
```

vs corpus M_1 = 6.06 × 10⁹ GeV: factor 1.33 high. Within Davidson-Ibarra factor-2 precision.

---

## §5. Numerical verification and structural ratios

### 5.1 The mode-mass spectrum at structural-argument level

```
M_R (σ_1, σ_2) = M_Pl^(3/4) · v_EW^(1/4) = 8.20 × 10¹⁴ GeV
M_1 (σ_3)      = M_Pl^(2/3) · H_GB^(1/3) = 8.08 × 10⁹  GeV
M_R / M_1      = M_Pl^(1/12) · v_EW^(1/4) · H_GB^(-1/3)
              ≈ 38.9 × 3.96 × 654
              ≈ 1.01 × 10⁵
```

vs corpus ratio M_R/M_1 = 8.2 × 10¹⁴ / 6.06 × 10⁹ = 1.35 × 10⁵.

Predicted structural ratio matches corpus ratio within factor 1.33. The same factor 1.33 spread that affects M_1 directly — i.e., M_R is exact to corpus per its own derivation; M_1 is factor 1.33 high; the ratio inherits the M_1 spread.

### 5.2 Davidson-Ibarra precision context

Per AC's eta v2 audit response: the M_1 = 6.06 × 10⁹ GeV corpus value is constrained to factor-2 precision by the Davidson-Ibarra leptogenesis closure: "factor-of-2 spread real and adequately explained by (i) the factor-1.5 neutrino mass spread, (ii) DI convention details."

The σ_3 candidate at factor 1.33 high is **consistent with the corpus's M_1 value within Davidson-Ibarra precision**. It is not in tension; it is the right ballpark with structural origin identified.

### 5.3 Equivalent forms (for cross-reference)

```
M_1 = (M_Pl² · H_GB)^(1/3)               [physical-scale form]
    = α^(1/3) · M_Pl^(4/3)               [in α and M_Pl]
    = M_Pl · (β_NTE·M_Pl)^(1/3)            [factoring out M_Pl]
    = M_Pl · e^(-N_e/3)                  [using β_NTE·M_Pl = e^(-N_e)]
    = M_Pl × (H_GB / M_Pl)^(1/3)         [Hartle-Hawking → gauge-birth ratio]
```

Geometric reading: M_1 is the energy scale obtained by descending from M_Pl by N_e/3 ≈ 21.1 e-folds, in a 63.41-e-fold pre-temporal regime. Geometrically: the cube-root-weighted geometric mean of M_Pl² and H_GB.

---

## §6. Comparison to (E)'s prior speculation candidates

(E) §5 listed four speculation candidates for the cube-root weighting:

| (E) candidate | This note's reading |
|---|---|
| #1: S³ volume V(S³) ∝ ℓ³ giving cube root | Partial. The cube root in M_1³ = M_Pl² · H_GB does reflect dim(S³) = 3. But the scale weighting (2 base dims × M_Pl + 1 fibre dim × H_GB) is more specific than "S³ volume scaling." |
| #2: Three-Majorana-mass seesaw structure | Closer to right reading. The three Majorana masses come from the three Killing-spinor su(2) modes. M_2 = M_3 (σ_1, σ_2 raising/lowering pair) and M_1 (σ_3 Cartan) form the spectrum from a single su(2) decomposition. |
| #3: Three Sakharov / 3 generations / dim(su(2)) = 3 | dim(su(2)) = 3 is the operative count — the three Killing-spinor modes σ_1, σ_2, σ_3. Three generations is independent (J₃(𝕆) structure). Three Sakharov is a separate counting. |
| #4: Surface ontology Stage 4 features | Different attack route; not the mechanism this note proposes. May still be productive for refining the precision factor. |

The σ_3 Cartan-mode mechanism is most closely a refined version of (E) #2 + #3, with the structural cause for the cube-root weighting identified.

---

## §7. What this DOES and DOES NOT close

### 7.1 What it does

- Provides a structural mechanism candidate for M_1 parallel to M_R's mechanism per §19.7.
- Connects M_1 to the same Killing-spinor su(2) machinery that gives M_R via N4 / Pathway α S3.
- Explains why M_1 ≠ M_R structurally — different mode (Cartan vs raising/lowering pair) with different geometric roles (fibre vs base) and different breaking scales (cosmological vs Higgs).
- Explains the cube-root structure of (E)'s candidate naturally — three dimensions of S³ (no Higgs sector).
- Promotes M_1 derivation status from "no structural lead, four open speculation candidates" to "structural mechanism candidate parallel to M_R."
- Completes the M_1, M_2, M_3 spectrum derivation as a single su(2)-decomposition story.

### 7.2 What it does NOT do

- Does NOT close Gap 1 in the strict sense (full Connes spectral triple calculation still pending — same status as M_R per §19.7).
- Does NOT pin down the exact precision-factor between candidate (8.08 × 10⁹ GeV) and corpus (6.06 × 10⁹ GeV); factor 1.33 is within Davidson-Ibarra precision but not "exact."
- Does NOT rigorously justify the specific weighting (2 base dims × M_Pl + 1 fibre dim × H_GB) from first principles. The structural argument in §4 is qualitative — it identifies the mechanism structure but doesn't prove uniqueness. Full Connes spectral triple calculation needed for the rigorous derivation.
- Does NOT replace M_R's pending full derivation; rather, places M_1 on the same structural footing.

The honest rhetorical class: **"structural mechanism candidate parallel to M_R, full derivation pending."** Same level of completion as M_R per the corpus's existing presentation.

---

## §8. Implication for leptogenesis: complete spectrum from one source

If σ_3 ↔ M_1 + σ_1, σ_2 ↔ (M_2, M_3) holds at structural level, then:

- **All three Majorana masses derive from the Killing-spinor su(2) decomposition on S³.**
- The asymmetry M_2 = M_3 ≠ M_1 reflects su(2)'s root-vs-Cartan structure — a single algebraic fact.
- Davidson-Ibarra η ≈ 6.1 × 10⁻¹⁰ is then derivable purely from S³ geometry via this complete spectrum, with no Yukawa-tunable input.

This is the **fully-geometric leptogenesis chain** the framework has been working toward. It is now within reach if both M_R and M_1 derivations close at the Connes spectral triple level.

The specific structure:

```
S³ ≅ SU(2) Killing-spinor multiplet under SU(2)_L
        ↓ Higgs VEV breaks SU(2)_L → U(1)_em
Three eigenmodes σ_1, σ_2, σ_3
        ↓ Hopf bundle S¹ → S³ → S² geometry
σ_1, σ_2 modes (charged, base-acting)    σ_3 mode (neutral, fibre-acting)
        ↓ + Higgs sector at v_EW           ↓ + cosmological scale at H_GB
M_R⁴ = M_Pl³ · v_EW                       M_1³ = M_Pl² · H_GB
M_R = 8.2 × 10¹⁴ GeV                      M_1 = 8.1 × 10⁹ GeV
        ↓ Davidson-Ibarra leptogenesis (M_1 dominant CP-violating decay)
η ≈ 6 × 10⁻¹⁰
```

Status: complete chain at structural-argument level. Full closure requires Connes spectral triple work on both M_R and M_1.

---

## §9. Verdict and integration recommendation

**Verdict.** The σ_3 Cartan-mode mechanism is **structurally consistent and dimensionally clean.** It elevates (E)'s candidate from "numerical lead" to "structural mechanism candidate parallel to M_R per §19.7."

**Rhetorical class.** "Structural mechanism candidate, full Connes spectral triple derivation pending." NOT "Gap 1 closed." Same status as M_R's existing corpus presentation.

**Integration recommendation:**

- **§17.5.15 sharpening** (proposed at v10.7.1 or v10.8 ship): replace "(E) numerical candidate, no structural origin" with: *"M_1 candidate from σ_3 Cartan-mode mechanism on the S³ Hopf bundle structure, parallel to M_R derivation per §19.7. Mass relation M_1³ = M_Pl² · H_GB derives from σ_3 being neutral under the broken U(1)_em (no Higgs sector contribution) with the fibre direction weighted by the cosmological scale at gauge birth (H_GB). Numerical: M_1 ≈ 8.08 × 10⁹ GeV vs corpus M_1 = 6.06 × 10⁹ GeV (factor 1.33 within Davidson-Ibarra closure precision). Full Connes spectral triple derivation pending — same status as M_R. Together the σ_1, σ_2 raising/lowering pair (M_R) and the σ_3 Cartan (M_1) close the M_1, M_2, M_3 Majorana spectrum from a single su(2) decomposition, completing the structural pathway for fully-geometric leptogenesis."*

- **§22.5 sharpening** (Gap 1 catalogue): Gap 1 status updated from *"open question with no leads"* to *"structural mechanism candidate identified (Jammer 2026-05-11): σ_3 Cartan mode of the Killing-spinor su(2) decomposition on S³, with cosmological scale at gauge birth replacing the Higgs sector contribution that gives M_R for σ_1, σ_2. Full Connes spectral triple derivation pending, parallel to M_R."*

- **§19.7 cross-reference**: add note that the M_R derivation per §19.7 has a parallel M_1 derivation per σ_3 mode mechanism; both are at the same structural completeness level.

**Sequencing:**

- v10.7 (eta v2): ships clean. This finding does NOT need to be in v10.7.
- **v10.7.1 or v10.8**: integrate alongside σ↔Φ_NTE confluence finding. Both are R&D-stream substantive structural advances since v10.6.1; both share the underlying "geometric mechanism replaces RH-neutrino-Yukawa apparatus" theme.
- v10.10 (offensive expansion): unaffected.

**Pre-ship CR pass scope addition:** verify the σ_3 ↔ M_1 mechanism structural argument (§4) is sound and not overclaiming. Specifically:

- Is the Higgs-sector +1 power asymmetry between σ_1, σ_2 and σ_3 structurally clean, or is it a heuristic that needs first-principles derivation?
- Is the H_GB weighting of the fibre for σ_3 justified beyond the qualitative argument in §4.2?
- Is the cube-root from "3 dims of S³" without Higgs sector consistent with the Connes spectral action's actual computation (when done) for a Cartan-mode-equivalent on S³?

---

## §10. Open follow-on items

If Greg authorises further σ_3 ↔ M_1 structural work after housekeeping closure:

1. **Pin down the σ_3 fibre-weight = H_GB structural derivation rigorously.** §4.2's qualitative argument (mode acting on a direction inherits that direction's relevant breaking scale) needs first-principles formalisation. Likely route: spectral-action-style integration of the σ_3 Cartan generator's energy contribution at gauge birth.

2. **Verify analog calculation for M_R.** Derive the σ_1, σ_2 modes' "S³ ambient at M_Pl + Higgs sector at v_EW" rigorously. This is the parallel programme for M_R's full closure.

3. **Connes spectral triple framework for the unified M_R + M_1 derivation.** Both derivations should close at the same level. The Connes machinery on S³ × F (where F is the relevant finite spectral triple — likely octonionic/G_2 per the σ↔Φ_NTE confluence framing) is the natural setting.

4. **Cross-check against Companion 7's three-mode picture.** Companion 7 §2-§3 develops the three-eigenmode picture for neutrino oscillation; verify the σ_1, σ_2, σ_3 mode-mass spectrum proposed here is consistent with the oscillation picture's mass-eigenstate ordering (m_3 > m_2 ~ m_1 normal ordering).

5. **Octonionic spectral triple read** (Farnsworth 2025 + Boyle-Farnsworth 2013, /NCG folder). If NTE's pre-temporal A_{G₂} structure has a Farnsworth-style spectral triple, the σ_3 ↔ M_1 mechanism may have a sharper derivation in that framework.

---

## §11. Files referenced

- Jammer (E) prior numerical investigation: `Working/M1_From_Geometry_E_search.md` (file ID `1vgruCSbzQQEt4NOw26W1_ANnfkFL9V9m`)
- Jammer σ↔Φ_NTE confluence verdict (parent of this hypothesis): `Working/Sigma_PhiNTE_Confluence_Verdict_v1.md` (file ID `17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`)
- Eta reframing audit (M_R Hopf-bundle derivation): `Working/Eta_Asymmetry_Magnitude_Reframing_Audit_v2.md`
- Companion 7 (neutrino as unresolved geometry): `Papers/7_Neutrino_As_Unresolved_Geometry.md`
- Corpus master: `NTE_v10_6_1.md` §3.3 (no RH/LH neutrino), §6.1 (Hopf projection), §17.5.15 (M_1 status), §19.7 (M_R derivation), §22.5 (Gap 1)
- Pathway α S3 (M_2 = M_3 = M_R from σ_1, σ_2 equivalence): `Handoffs/Handoff_Jammer_to_AC_M2_closure_N4.md`

---

## §12. END-OF-WORKING-NOTE status

```
CARRY-FORWARD (next session):
  - This working note + accompanying Handoff to AC (next item)
  - Greg's strategic call on rhetorical class (structural mechanism vs Gap 1 closed) and integration sequencing (v10.7.1 vs v10.8)
  - Pre-ship CR pass scope addition (per §9 above)
  - Open follow-on items §10 if authorized
  - Cross-listed with σ↔Φ_NTE confluence integration — both findings share the geometric-mechanism theme

DRIVE UI ACTIONS NEEDED (this turn):
  - File created at Drive root due to subfolder permission block. Greg: please move to Working/.

NO OTHER FILE OPERATIONS this turn.
```

— Jammer, 2026-05-11.
