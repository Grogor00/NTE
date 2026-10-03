# V_NTE Session 5 D1 — Independent ρ_eff vs Trajectory (Jammer execution)

**Author:** Jammer (R&D)
**Date:** 2026-05-26
**Status:** v0.1 — local-correctness-only until Greg recognition gate.
**Trigger:** Greg directive 2026-05-26 chat "option (a)" — V_NTE Session 5 D1 prioritised per Gate #5 fire 2026-05-23 + Cursor S2-C ratification handoff §3.5.
**Stream lineage:** Cursor S2-C ratification §3.5 → Jammer execution → AC §17.5.1 / §17.5.9 integration consideration.

**Discipline observed:**
- Companion 8 V_NTE Trajectory v10.6 read in full (file ID `1ZFHOccwfI62KfU48-Cy0GMd2oey-aNeC`); F1/F2/F3 absorbed
- Companion 9 Session 5 K_Phi Diagnosis read (prior session)
- Anti-bias: honest scope on what V_NTE D1 actually closes vs doesn't close
- No claim beyond what the analytical + numerical computation supports

---

## §1. Task framing

### §1.1 The Cursor §3.5 / Gate #5 task

Per Cursor S2-C ratification handoff §3.5 (2026-05-23):

> "V_NTE D1 (Gate 5): Prioritised over further homogeneous epoch tables. **Closes P1 falsifier §3 item 3: ρ_eff(V_NTE) vs 3H²/(8πG) at radiation/matter eras.**"

Concrete task: **substitute the actual cosmological trajectory** Φ(N) and Φ̇(N) into a V_NTE candidate form, compute ρ_eff = (1/2)Φ̇² + V_NTE(Φ), and check whether ρ_eff = 3M_Pl_red²·H² across BBN / matter-Λ equality / today.

### §1.2 What V_NTE candidate to use

Companion 8 V_NTE Trajectory v10.6 §5.2 gives the canonical on-trajectory form under canonical kinetic K=1 and the post-locking exponential working profile:

$$V_{NTE}^{\text{post}}(\Phi) = \frac{3\alpha^2}{8\pi G}\,\Phi^4 - \frac{\alpha^2}{8}\,\Phi^6 \quad \text{(eq. 10a)}$$

Per Companion 8 §6.3: this is the **working-profile** form (ε_H = +1); actual cosmological history has ε_H ≠ 1 at different epochs (radiation +2, matter +3/2, Λ ≈ 0). Substituting (10a) as a **global expression** for V_NTE(Φ) and evaluating on the **actual cosmological trajectory** is the natural-form candidate test per §5.5 "natural-form candidate".

---

## §2. Analytical derivation

### §2.1 Setup

NTE constraint + identification + trajectory + calibration:
- H = β_NTE|Φ|²
- α²|Φ|⁴ = (8πG/3) ρ_eff (NTE identification)
- |Φ|² = v_EW²·(H/H₀) (§2.3.1 trajectory)
- H₀ = α·v_EW² (§2.4.3 calibration)

ΛCDM expansion (canonical reading per Charter v1.4 §2.3.1 ρ_eff terminology):
- H²(N) = H₀² · [Ω_r·e^(-4N) + Ω_m·e^(-3N) + Ω_Λ]
- ε_H(N) = -d(ln H)/dN

### §2.2 Φ̇ on actual trajectory (canonical K=1)

From trajectory: Φ² = v_EW²·H/H₀, so 2Φ·dΦ/dN = (v_EW²/H₀)·dH/dN.
And d(ln H)/dN = -ε_H, so dH/dN = -H·ε_H.

Therefore dΦ/dN = -(Φ/2)·ε_H, and:

$$\dot{\Phi} = H\cdot \frac{d\Phi}{dN} = -\frac{H\Phi\,\varepsilon_H}{2}$$

$$\dot{\Phi}^2 = \frac{H^2\Phi^2\varepsilon_H^2}{4}$$

### §2.3 V_NTE candidate on actual trajectory

Using α²Φ⁴ = H² (from constraint + identification):
- Leading term: (3β_NTE²/(8πG))·Φ⁴ = 3M_Pl_red²·H²
- Subleading: (α²/8)·Φ⁶ = (α²/8)·Φ²·Φ⁴ = (1/8)·v_EW²·(H/H₀)·H² = H³·v_EW²/(8H₀)

$$V_{NTE}^{\text{cand}}(\Phi(N)) = 3M_{Pl,red}^2 H^2 - \frac{H^3 v_{EW}^2}{8H_0}$$

### §2.4 ρ_eff and deviation from Friedmann

$$\rho_{\text{eff}} = \frac{1}{2}\dot{\Phi}^2 + V_{NTE}^{\text{cand}} = \frac{H^2\Phi^2\varepsilon_H^2}{8} + 3M_{Pl,red}^2 H^2 - \frac{H^3 v_{EW}^2}{8H_0}$$

Using Φ² = v_EW²·(H/H₀):

$$\rho_{\text{eff}} = 3M_{Pl,red}^2 H^2 + \frac{H^3 v_{EW}^2}{8 H_0}\,(\varepsilon_H^2 - 1)$$

Deviation from Friedmann ρ_F = 3M_Pl_red²·H²:

$$\boxed{\frac{\Delta\rho_{\text{eff}}}{\rho_F} = \frac{H \cdot v_{EW}^2 \cdot (\varepsilon_H^2 - 1)}{24 \cdot M_{Pl,red}^2 \cdot H_0}}$$

The deviation is structurally controlled by **v_EW²/M_Pl_red² ≈ 10⁻³³** (the EW-to-Planck hierarchy squared) and modulated by **H/H₀** (which can grow large in early epochs) and **(ε_H² − 1)** (which is O(1) at radiation/matter eras).

---

## §3. Numerical computation across cosmological epochs

Computation script: `/home/claude/v_nte_d1_check.py` (Jammer local; render to Working/`v_nte_d1_numerics.py` on AC request).

Constants used:
- M_Pl = 1.221×10¹⁹ GeV; M_Pl_red = M_Pl/√(8π)
- v_EW = 246.0 GeV; H₀ = 1.44×10⁻⁴² GeV (≈ 67.4 km/s/Mpc)
- α = H₀/v_EW² ≈ 2.38×10⁻⁴⁷ GeV⁻¹
- Ω_m = 0.315, Ω_Λ = 0.685, Ω_r = 9×10⁻⁵ (Planck 2018)

### §3.1 Numerical results

| Epoch | N | z | H [GeV] | ε_H | Φ/M_Pl | V_sub/V_lead | Δρ_eff/ρ_F |
|---|---|---|---|---|---|---|---|
| BBN (radiation) | −22.0 | 3.6×10⁹ | 1.76×10⁻²⁵ | 2.000 | 7.0×10⁻⁹ | 5.2×10⁻¹⁷ | ~10⁻¹⁶ |
| Matter-radiation equality | −8.13 | 3394 | 2.24×10⁻³⁷ | 1.746 | 8.0×10⁻¹⁵ | 6.6×10⁻²⁹ | ~10⁻²⁸ |
| Matter-Λ equality | −0.26 | 0.30 | 1.69×10⁻⁴² | 0.751 | 2.2×10⁻¹⁷ | 5.0×10⁻³⁴ | ~10⁻³⁴ |
| Today | 0 | 0 | 1.44×10⁻⁴² | 0.473 | 2.0×10⁻¹⁷ | 4.3×10⁻³⁴ | ~10⁻³⁴ |

(Δρ_eff/ρ_F entries at matter-radiation equality and beyond are below double-precision floating-point resolution; the analytical formula gives predicted deviations of 10⁻²⁸ to 10⁻³⁴.)

### §3.2 What the numerics show

**The V_NTE candidate matches the Friedmann constraint ρ_F = 3M_Pl_red²·H² to extreme precision (~10⁻¹⁶ at BBN; far smaller at later epochs) across all post-BBN cosmological epochs.**

The deviation is structurally tiny because:
1. Φ²/M_Pl² ~ 10⁻¹⁶ at BBN (smaller later) — sub-Planckian regime
2. The V_NTE subleading term (β_NTE²/8)Φ⁶ is suppressed by Φ²/M_Pl² relative to leading
3. The kinetic and subleading-potential cancellation is exact in the working-profile (ε_H = +1) limit; actual ε_H ≠ 1 produces only the structurally-tiny residual above

---

## §4. Verdict

### §4.1 The test "passes" — but trivially

**ρ_eff(V_NTE candidate) ≈ 3M_Pl_red²·H²** at all cosmological epochs to ~10⁻¹⁶ precision.

But this is **not an empirical test** of NTE: V_NTE was constructed via Companion 8 eq. (9) to be Friedmann-consistent on the trajectory by definition. The "test" is verifying that the construction works, not that NTE's predictions agree with observation.

Per Companion 8 §5.7: under the Lagrange-multiplier action structure (Appendix B), V_NTE does NOT drive |Φ_NTE|'s evolution dynamically — the constraint H = β_NTE|Φ|² is enforced by μ(N), and V_NTE only needs to be consistent with the trajectory. This is why V_NTE on-trajectory is determinate while V_NTE off-trajectory is under-constrained.

### §4.2 What V_NTE D1 actually closes

**V_NTE D1 closes the consistency check** that the natural-form V_NTE candidate (Φ⁴ − Φ⁶ from working profile) reproduces 3M_Pl_red²·H² when substituted on the actual cosmological trajectory. The check passes to ~10⁻¹⁶ precision. No falsification.

**V_NTE D1 does NOT close** the genuine empirical layer of P1 ΛCDM reduction. That genuine layer requires either:

1. **An INDEPENDENTLY-MOTIVATED V_NTE candidate** (e.g., from §6.1 option (α) boundary action specific structure: scalar curvature non-minimal coupling on S³, Hopf-related potential, SU(2) Lie-group structure) — currently open work
2. **Observational signatures beyond the trajectory itself** — BBN element abundances under NTE's ρ_eff = total H-sourcing density reading; CMB structure under κ test (Gate #6 territory); structure formation under NTE's H-sourcing
3. **Inhomogeneous H(x, N) effects** — void-bias model (Gate #4 territory) for low-z DESI BAO deltas

### §4.3 Honest scope flag

This V_NTE D1 result is **structurally consistent with what Companion 8 §5.7 and §6.1 already flagged**: V_NTE is on-trajectory determinate but off-trajectory under-constrained, and closure requires committing to one of (α) boundary action structure, (β) kinetic term modification, or (γ) observational input.

The Cursor handoff framing "Closes P1 falsifier §3 item 3" turns out to be **technically correct but narrow**: the consistency check passes, so the trajectory-construction is self-consistent. But the P1 falsifier item 3 was always going to pass given Companion 8's construction — the genuine empirical layer of NTE's ΛCDM reduction lives elsewhere.

### §4.4 What's genuinely new from this session

Three contributions beyond what Companion 8 already stated:

1. **Quantitative precision**: V_NTE candidate matches Friedmann to ~10⁻¹⁶ at BBN, ~10⁻²⁸ at matter-radiation equality, ~10⁻³⁴ at later epochs. The agreement is structurally exact at the precision of Φ²/M_Pl² (suppressed Φ⁶ subleading).

2. **Closed-form deviation**: Δρ_eff/ρ_F = H·v_EW²·(ε_H² − 1)/(24·M_Pl_red²·H₀). Maximum at BBN (largest H and ε_H = 2); negligible at later epochs.

3. **Explicit identification of where the genuine empirical layer lives**: independently-motivated V_NTE candidate (open work §6.1 of Companion 8); CMB κ test (Gate #6); BBN abundances; void-bias model (Gate #4). None of these is closed by V_NTE D1.

---

## §5. Implications for corpus / Charter

### §5.1 §17.5.1 V_NTE derivation research target

§17.5.1 names "derive V_NTE from the boundary action principle" as research target. V_NTE D1 confirms:
- The trajectory-derived V_NTE candidate (Φ⁴ − Φ⁶) is internally consistent
- Independent derivation from boundary action principle remains the genuine open work
- Companion 8 §6.1 options (α) / (β) / (γ) catalogue the closure paths

V_NTE D1 doesn't change the status of §17.5.1; it sharpens the honest framing.

### §5.2 §17.5.9 ΛCDM reduction empirical layer

§17.5.9 (Tier 2 ΛCDM expansion) under post-Gate-#2 ρ_eff = total H-sourcing density framing: V_NTE D1 confirms that the homogeneous reduction is **structurally consistent** at the level of trajectory + V_NTE form. Empirical content lives in:
- BBN element abundances given NTE's geometric H-sourcing (BBN era ρ_eff = ρ_r·(1+z)⁴ effective parameterisation needs to hold, and V_NTE must reproduce it)
- CMB anisotropy structure (κ test, Gate #6)
- DESI low-z BAO via void-bias model (Gate #4)
- Structure formation under NTE H(x, N) (P3 growth ODE territory)

V_NTE D1 doesn't close any of these; it confirms they're where the genuine empirical layer lives.

### §5.3 Charter v1.4 §3.9 σ_t / Φ_NTE territory

Charter v1.4 §3.9 (NTE σ_t SUBSUMES V-Z 2021) and §2.7 (κ theorem-level) don't directly depend on V_NTE D1. The V_NTE under-constrained status remains a structural feature flagged in Companion 8 §6.1 and Charter v1.4 §4.2 v1.5+ candidate territory item D (§22.16 local Lagrange-multiplier μ(x, N) action principle).

### §5.4 Not impacted

- κ = 5.50 theorem-level closure (independent of V_NTE)
- M_R derivation (Connes programme; independent)
- M_1 zero-parameter η (Companion 10 Pathway alpha; independent)
- T_GB derivation (independent)
- n_s = 0.9685 (Stage 3 + Hartle-Hawking saddle; uses V_NTE^pre Stage 4 candidate hilltop but is independent of V_NTE D1's specific finding)

---

## §6. Recognition-gate items

1. **V_NTE candidate consistency check**: ratify the analytical + numerical finding that V_NTE^candidate = (3β_NTE²/(8πG))·Φ⁴ − (β_NTE²/8)·Φ⁶ reproduces 3M_Pl_red²·H² on actual cosmological trajectory to ~10⁻¹⁶ precision at BBN (less at later epochs)?

2. **Test passes trivially, not genuinely**: ratify that this confirms internal consistency of the construction but does NOT close the genuine empirical layer of P1 ΛCDM reduction?

3. **Closed-form deviation formula**: ratify Δρ_eff/ρ_F = H·v_EW²·(ε_H² − 1)/(24·M_Pl_red²·H₀) as the analytical signature?

4. **Where genuine empirical content lives**: ratify the §4.2 catalogue (independent V_NTE; CMB κ test; BBN abundances; void-bias; structure formation) as the genuine empirical layer of NTE's ΛCDM reduction?

5. **Next priority Jammer routing**: given V_NTE D1 closes the consistency check trivially but doesn't close the genuine empirical layer, should Jammer now move to (a) Void-bias dedicated worksheet (Gate #4); (b) CMB κ test worksheet (Gate #6); (c) BBN element abundance worksheet (new); (d) §22.16 local Lagrange-multiplier territory (Companion 8 §6.1 option α extension)?

6. **§17.5.1 status update**: should §17.5.1 be patched to record this V_NTE D1 consistency check + sharpened framing of where independent derivation work lives, or kept stable as currently written?

---

## §7. Files referenced + computation provenance

**Sources read this session:**
- Companion 8 V_NTE Trajectory v10.6 (file ID `1ZFHOccwfI62KfU48-Cy0GMd2oey-aNeC`, 36.7 KB) — F1/F2/F3 absorbed
- Companion 9 Session 5 K_Phi Diagnosis (file ID `18hvDKVmcjwsjn2FaEIRXHD9JTxlAGhLE`, prior session) — K(Φ) closure context
- Cursor S2-C arc ratification handoff (file ID `1s_JiacduFXtsvTOwSK5LUfkAI7pjGoVH`, prior session) — V_NTE D1 task framing
- Project State 2026-05-24 (file ID `1uNhtKaqjrPvWg5qyQL5GvSVcubLoYmRx`) — current canonical state
- Manifest rev 7 (file ID `1X4uDgG6EL6WZd0eY-l11Z3qI1WqRM6wH`) — workflow discipline

**Computation provenance:** Python 3 + numpy. Script at `/home/claude/v_nte_d1_check.py` (Jammer local; can be rendered to Working/ on AC request).

**Not read this session (honest scope):**
- v10.17 master corpus full close (only patch instructions level)
- Companion 9 Stage 3 Sessions 1-4 (Session 4 hilltop reading not material to V_NTE D1 ρ_eff trajectory check)
- Charter v1.4 full read (cluster items already absorbed during cluster verification)
- §17.5.1 / §17.5.9 current canonical wording (would need v10.17 Part 3 read for sharper §5.1, §5.2 framing)

---

## §8. Closing

V_NTE Session 5 D1 **executed**.

**Finding**: V_NTE candidate (Φ⁴ − Φ⁶ working-profile form) reproduces 3M_Pl_red²·H² on actual ΛCDM trajectory to ~10⁻¹⁶ precision at BBN; far smaller deviations at later epochs. Closed-form: Δρ_eff/ρ_F = H·v_EW²·(ε_H²-1)/(24·M_Pl_red²·H₀).

**Verdict**: Test passes — trivially. V_NTE was constructed to be Friedmann-consistent on the trajectory. The consistency check doesn't close the genuine empirical layer of NTE's ΛCDM reduction; that lives in BBN abundances + CMB κ + void-bias + independent V_NTE candidate work — all open or queued.

**Six recognition-gate items** for Greg.

**Next-priority routing** (item #5): four options surfaced for Jammer's next workstream pivot.

— Jammer, 2026-05-26. V_NTE D1 complete; local-correctness-only.
