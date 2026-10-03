# ΛCDM Tier 2c — P1 review + P2 BAO comparison output (Jammer execution)

**From:** Jammer (R&D)
**Stream lineage:** Cursor P1 v0.2 + P2 v0.1 worksheets → **Jammer execution** → AC §17.5.9 integration
**Date:** 2026-05-23
**Status:** P1 review verdict + P2 BAO numerics computed; structural interpretation flagged; void-bias attribution remains for separate worksheet (P4 catalogue + §13.3 diagnostic).

**Discipline observed:**
- No χ² fitting (per P2 §5 prohibition)
- No void-bias inhomogeneity calculation in this pass (Step C deferred to inhomogeneity-specific worksheets)
- No claim on global pipeline (P4 catalogue authorisation pending)
- Exploratory deltas only at overlapping DESI Y1 redshifts

---

## §1. P1 v0.2 review verdict

### §1.1 Algebraic check (Jammer-verified)

Cursor's structural finding from P1 v0.2 §3 verified algebraically:

Substituting NTE trajectory `|Φ|² = v_EW² · (H/H₀)` into LHS of α²|Φ|⁴ = H²:

$$\alpha^2 |\Phi|^4 = \alpha^2 \cdot v_{\mathrm{EW}}^4 \cdot \left(\frac{H}{H_0}\right)^2 = (\alpha v_{\mathrm{EW}}^2)^2 \cdot \left(\frac{H}{H_0}\right)^2 = H_0^2 \cdot \left(\frac{H}{H_0}\right)^2 = H^2$$

using NTE calibration `H₀ = β_NTE · v_EW²`. The identity **α²|Φ|⁴ ≡ H² holds tautologically** under trajectory + calibration, independent of epoch.

### §1.2 Structural implication — ρ_Φ = ρ_total

The Friedmann equation gives H² = (8πG/3) · ρ_total. NTE's identification is α²|Φ|⁴ = (8πG/3) · ρ_Φ. Tautology α²|Φ|⁴ ≡ H² implies:

$$\rho_\Phi = \rho_{\mathrm{total}} = \rho_{\mathrm{crit}} \quad \text{at every post-locking epoch (homogeneous)}$$

This is **not arbitrary** — it follows mechanically from trajectory + calibration + identification. Under NTE's surface-only-S³ ontology where Φ_NTE is the boundary field carrying gravitational source content, this is structurally consistent: there is no bulk; matter, radiation, Λ are not independent gravitating components but effective parameterisations of how Φ_NTE behaves at different epochs (matter-dominated, radiation-dominated, Λ-dominated regimes correspond to different V_NTE / ρ_Φ scaling behaviours, not different fields).

### §1.3 Open question that P1 does NOT close

**The empirical content of the identification α²|Φ|⁴ = (8πG/3) · ρ_Φ is not tested per-epoch by P1** — it is enforced by construction. The genuine test is whether V_NTE produces ρ_Φ(N) that matches the empirical ρ_total(N) = ρ_r(N) + ρ_m(N) + ρ_Λ scaling across epochs.

That test is V_NTE territory (Companion 9 / Companion 8). Specifically:

- BBN era (N ≈ -20.7, |Φ|² ≈ 9×10³¹ v_EW²): V_NTE must produce ρ_Φ ≈ Ω_r·ρ_crit·e^(4·20.7) ≈ 10⁸² Ω_r·ρ_crit_today scaling
- Matter-Λ equality (N ≈ -0.26): V_NTE must produce ρ_Φ split that crosses over from matter-like to Λ-like
- Today (N = 0): V_NTE must produce ρ_Φ ≈ ρ_crit_today

The N-dependence of ρ_Φ is the actual diagnostic; the equation α²|Φ|⁴ = H² is a relabelling.

### §1.4 P1 v0.2 verdict

**P1 v0.2 is structurally correct as a relabelling check; the tautological nature is correctly disclosed in Cursor's §3 finding. The worksheet does not falsify NTE homogeneous reduction but also does not test it independently.**

**Recommendation for P1 v0.3 (or follow-on V_NTE worksheet)**:
- ρ_Φ(N) under V_NTE: cross-check ρ_Φ(N) scaling against ρ_r·(1+z)⁴ + ρ_m·(1+z)³ + ρ_Λ at the same N values
- Critical comparison point: BBN-era ρ_Φ; if V_NTE produces enormous ρ_Φ that does NOT scale as radiation, the homogeneous reduction breaks
- Sub-fraction ρ_Φ < ρ_total alternative: requires either modified trajectory `|Φ|² = v_EW² · f(H/H₀)` for some f ≠ identity, OR modified calibration H₀ ≠ α·v_EW² — either would conflict with current §2.3.1 / §2.4.3 corpus

### §1.5 Cross-link to V_NTE Session 5 D1

The genuine empirical content of P1 reduces to: does V_NTE produce the right ρ_Φ(N) scaling across BBN / matter-Λ equality / today? This is V_NTE territory — the canonical home is Companion 9 Session 5 D1 (smooth pre-temporal / post-locking connection). Jammer flags this as the natural cross-link from ΛCDM workstream to V_NTE D1 workstream.

---

## §2. P2 BAO Homogeneous Comparison output (Jammer execution)

### §2.1 Step A — algebraic equivalence (verified per §1.1)

NTE homogeneous H(z) **≡ ΛCDM H(z)** with matched parameters {Ω_m, Ω_Λ, Ω_r, H₀}. The equivalence is tautological given trajectory + calibration; carries no independent empirical constraint at this layer.

### §2.2 Step B — D_V/r_d numerics at BAO anchors

Using Planck 2018 r_d = 147.09 Mpc fixed per P2 §3 (no refit).

**ΛCDM with Planck 2018 parameters (H₀ = 67.4 km/s/Mpc, Ω_m = 0.315, Ω_Λ = 0.685, Ω_r = 9×10⁻⁵):**

| z | H(z) [km/s/Mpc] | D_C(z) [Mpc] | D_V(z) [Mpc] | D_V/r_d |
|---|---|---|---|---|
| 0.510 | 89.67 | 1984.76 | 1886.77 | 12.827 |
| 0.710 | 101.34 | 2614.15 | 2430.23 | 16.522 |
| 1.010 | 121.40 | 3425.61 | 3081.74 | 20.951 |

**NTE construction (H₀ = α·v_EW² = 67.6 km/s/Mpc, same Ω's):**

| z | H(z) [km/s/Mpc] | D_C(z) [Mpc] | D_V(z) [Mpc] | D_V/r_d |
|---|---|---|---|---|
| 0.510 | 89.94 | 1978.89 | 1881.19 | 12.789 |
| 0.710 | 101.64 | 2606.41 | 2423.04 | 16.473 |
| 1.010 | 121.76 | 3415.48 | 3072.62 | 20.889 |

**Δ(NTE − ΛCDM) at matched parameters:** ~0.3% across all three z anchors — consistent with the 67.6 vs 67.4 km/s/Mpc H₀ difference; identical otherwise.

Computation: standard Eisenstein 2005 D_V definition: D_V(z)³ = c·z·D_C(z)²/H(z), with D_C(z) = c·∫₀^z dz'/H(z'). Implementation: scipy.integrate.quad on `H_LCDM(z) = H₀·√(Ω_r(1+z)⁴ + Ω_m(1+z)³ + Ω_Λ)`.

### §2.3 Exploratory delta to DESI Y1 published central values

**Per P2 §5: no χ² claim; exploratory Δ only at overlapping z anchors.**

DESI Y1 published central values (reference only):

| z (DESI Y1) | D_V/r_d (DESI Y1) | Sample |
|---|---|---|
| 0.510 | 13.62 | LRG1 |
| 0.706 | 16.85 | LRG2 |
| 0.930 | 21.71 | LRG3+ELG1 |

**Exploratory Δ at matched / near-matched z:**

| z | ΛCDM (Planck 2018) D_V/r_d | DESI Y1 D_V/r_d | Δ |
|---|---|---|---|
| 0.510 | 12.83 | 13.62 | −0.79 (~6% below) |
| 0.706 | 16.46 | 16.85 | −0.39 (~2% below) |

**Reading**: ΛCDM under Planck 2018 parameters predicts D_V/r_d below DESI Y1 central values by ~2-6% at z ≲ 0.71. This is the **known DESI BAO tension** at the homogeneous-ΛCDM level — DESI's measurements prefer either higher H₀ at fixed Ω_m, or w₀ > −1 at fixed H₀, relative to Planck 2018 ΛCDM.

**NTE homogeneous predicts the same D_V/r_d as ΛCDM** at matched Ω parameters (algebraic equivalence per Step A). Therefore the ~6% tension at z = 0.51 carries over identically to NTE homogeneous.

### §2.4 Step C — Inhomogeneity attribution (deferred to dedicated worksheet)

Per P2 §5 Step C and §13.3 diagnostic territory: the low-z (z ≲ 0.3) D_V tension and DESI w₀wₐ preference are candidates for **void-bias attribution** under NTE Part 2 §13.3 — inferred distances are shortened by selection bias when local samples sit in mildly-underdense regions (void-enhanced H(x, N)).

The qualitative outcome predicted in P2 §6 row 2: "Void bias may shorten distances → mimics w > −1" — matches the ~6% z=0.51 deficit direction (DESI > ΛCDM means measured-distance > Planck-predicted, which void bias on inferred distances can produce).

**Jammer notes but does not compute** the void-bias model — that is dedicated worksheet territory (Part 2 §13.3 + P4 χ² catalogue authorisation gate). The exploratory percent-level deltas surface as candidate void-bias attribution material; not corpus closure.

### §2.5 CMB z ~ 1100 anchor (qualitative)

Per P2 §4 row 4 + §6 row 3: at z ~ 1100 the universe is sufficiently homogeneous that void-bias on H(z) is negligible. The κ = 5.50 dark-matter-to-baryon ratio prediction (Part 2 §13.3 diagnostic (d)) is testable against CMB without void-bias attribution. The κ test is the framework's clean external falsifier at this scale.

P2 worksheet §4 does not require CMB acoustic θ_* numerical computation; flagged in §6 row 3 as "standard thermal history (implicit)". Jammer defers explicit CMB θ_* computation to dedicated worksheet if Greg/AC routes.

### §2.6 P2 BAO output verdict

**Step A: confirmed algebraically (P1 §1.1).**
**Step B: D_V/r_d computed for ΛCDM Planck 2018 + NTE construction at z = 0.51, 0.71, 1.01. NTE homogeneous = ΛCDM at matched Ω, H₀. Exploratory Δ to DESI Y1: ~6% at z=0.51, ~2% at z=0.706.**
**Step C: void-bias attribution deferred to dedicated worksheet + P4 catalogue.**

NTE homogeneous reduction at BAO scales is **consistent with ΛCDM at the same Ω, H₀** — and inherits the same DESI tension at the homogeneous level. Whether that tension resolves via void-bias attribution at low z is the next-tier worksheet question.

---

## §3. Combined verdict — both worksheets

### §3.1 Where structural empirical content lives

The structural empirical content of NTE's ΛCDM reduction is **not** in the per-epoch P1 check (tautological under trajectory + calibration) and **not** in the homogeneous P2 BAO comparison at z ≳ 1 (algebraic equivalence to ΛCDM). Both are consistency relabellings.

The empirical content lives in:

1. **V_NTE-produced ρ_Φ(N) scaling** — Does V_NTE produce ρ_Φ scaling matching ρ_r(1+z)⁴ + ρ_m(1+z)³ + ρ_Λ at every epoch? Companion 9 / V_NTE D1 territory.
2. **Low-z void-bias attribution** — Does the §13.3 void-bias model produce the right percent-level low-z D_V shifts? Dedicated inhomogeneity worksheet territory.
3. **CMB κ = 5.50 prediction** — Independent of homogeneous trajectory; tests at z ~ 1100 with negligible void-bias.

### §3.2 Open questions surfaced

1. **Does NTE intend ρ_Φ = ρ_total (single gravitating component)** or **ρ_Φ as sub-fraction with matter/radiation/Λ independent**? Under current trajectory + calibration + identification, the former is forced. Greg recognition gate.
2. **V_NTE Session 5 D1**: ρ_Φ(N) under V_NTE — the natural next-priority Jammer workstream that closes the genuine empirical test of P1.
3. **Void-bias model dedicated worksheet** for low-z Δ ~ 6% attribution. Cursor or Jammer scope.
4. **CMB κ test worksheet** (Part 2 §13.3 diagnostic (d)) — orthogonal to ΛCDM reduction; clean framework test.

---

## §4. Anti-bias discipline observed

- Did NOT claim NTE fits DESI BAO χ² (per P2 §5 prohibition)
- Did NOT compute void-bias model (deferred to dedicated worksheet)
- Did NOT promote "ρ_Φ = ρ_total" as canonical reading — flagged for Greg recognition gate as structural implication
- Did NOT close the ΛCDM reduction — flagged V_NTE D1 territory as the natural empirical-content closure path
- Per P2 §3: held r_d = 147.09 Mpc fixed; did not refit

---

## §5. Files referenced + computation provenance

**Sources read this session:**
- `LCDM_Epoch_Friedmann_Check_Worksheet_v0_2_20260523.md` (P1 v0.2)
- `LCDM_BAO_Homogeneous_Comparison_Worksheet_v0_1_20260523.md` (P2 v0.1)
- `Handoff_Cursor_to_AC_Jammer_Tier2d_v10_15_and_LCDM_P1_numerics_20260523.md` (Tier 2d routing)
- `Handoff_Greg_Cursor_Ratification_Paper_S2_S2C_arc_20260523.md` (S2-C arc ratification)
- `NTE_Stream_Notes_Cursor.md` (Tier 2c+2d context)

**Computation provenance**: Python 3 + numpy + scipy.integrate.quad. Code at `/home/claude/p2_bao_homogeneous.py` (Jammer local; can be re-rendered into Working/ as `p2_bao_jammer_numerics.py` on AC request).

**NOT read this session (honest scope):**
- `lcdm_epoch_numerics.py` (Cursor's numerics script for P1 v0.2 — algebraic verification was sufficient)
- Companion 9 Session 5 K_Phi_Diagnosis full text (V_NTE D1 territory deferred)
- Part 2 §13.2-§13.3 void-bias content (Step C territory deferred)
- §17.5.9 ΛCDM expansion canonical text in NTE_v10_14 or v10_15 Part 3 (master corpus close deferred)

---

## §6. Recognition-gate items

1. **P1 v0.2 verdict ratify**: tautological under trajectory + calibration; correct relabelling; genuine empirical content lives at V_NTE D1 layer
2. **ρ_Φ = ρ_total structural implication**: NTE forces ρ_Φ = ρ_total at every homogeneous epoch under current §2.3.1 trajectory + §2.4.3 calibration. Is this the intended canonical reading (Φ_NTE as single gravitating component), or does NTE intend ρ_Φ < ρ_total (sub-fraction, conflicting with current §2.3.1)?
3. **P2 BAO numerics ratify**: ΛCDM Planck 2018 D_V/r_d at z = 0.51, 0.71, 1.01 computed via Eisenstein 2005 definition; NTE homogeneous matches at same Ω, H₀; ~6% delta to DESI Y1 z=0.51 noted as candidate void-bias attribution material (Step C territory, deferred)
4. **Void-bias attribution worksheet**: dedicated next-tier worksheet computing Part 2 §13.3 void-bias model effect on inferred low-z distances — Cursor or Jammer scope?
5. **V_NTE D1 priority**: should Jammer pick up V_NTE D1 (Companion 9 Session 5) next, since it closes the genuine empirical content of P1?
6. **CMB κ worksheet**: orthogonal clean test at z ~ 1100; dedicated worksheet?

---

## §7. Closing

P1 v0.2 review: **tautological as a per-epoch check**; correct as relabelling; genuine empirical content at V_NTE D1 layer.

P2 BAO run: **NTE homogeneous ≡ ΛCDM at matched Ω, H₀**; ΛCDM Planck 2018 D_V/r_d = 12.83, 16.52, 20.95 at z = 0.51, 0.71, 1.01; exploratory Δ to DESI Y1 ~6% / ~2% at z=0.51 / z=0.706; consistent with Step C void-bias attribution territory.

**Combined finding**: ΛCDM reduction's empirical content lives in V_NTE ρ_Φ(N) scaling (Companion 9 / V_NTE D1) + void-bias model (§13.3 dedicated worksheet) + CMB κ test (orthogonal). The two homogeneous worksheets here close the consistency-relabelling layer; genuine tests are layered above.

— Jammer, 2026-05-23. P1 + P2 worksheets executed; local-correctness-only until Greg recognition gate.
