# Master v10.12 → v10.13 Patch Instructions

## Tier 2b — §17.5.4 N_lock candidate derivation (Jammer audit integration)

**Date:** 2026-05-23.  
**Source:** `Papers/depreciated/17.5.4_Audit_NLock_Derivation.md` (Jammer 2026-05-07); Companion 9 Session 3 (C1) for T_GB.  
**Greg ratification:** Candidate-derivation status (not full first-principles closure).

---

## Patch T2b-1: §17.5.4 body

**Find:**

```
17.5.4 The N_lock Value (Connects to §2.1.2 and §VII)

The temporal locking e-fold N_lock ≈ 0.1 is used throughout the corpus, particularly in §VII (gauge birth) and §XVIII (n_s prediction via N_e = -ln(α M_Pl)). Whether this specific value is derived from boundary tension dynamics or fitted to give the correct gauge-birth temperature T_GB is not made explicit. If derived, the derivation should be visible. If fitted, N_lock should be acknowledged as a calibration parameter and the framework's parameter accounting (§17) should reflect this. Research target: trace N_lock to either a derivation from boundary action dynamics or an explicit calibration target; revise §17 parameter accounting accordingly.
```

**Replace with:**

```
17.5.4 The N_lock Value (Connects to §2.1.2 and §VII)

**Status (v10.13, Tier 2b): closed at candidate-derivation level** per Jammer audit 2026-05-07 (`Papers/17.5.4_Audit_NLock_Derivation.md`). The temporal locking e-fold N_lock ≈ 0.105 (rounded N_lock ≈ 0.1 in prose) is used throughout the corpus — §VII (gauge birth), §XVIII (n_s via N_e = −ln(α M_Pl)), surface-ontology programme (Appendix E).

**Candidate structural derivation.** Under two structural commitments (both open to upgrade via Programme S / holographic work):

> N_lock = S_dS/4 = π M_Pl²/(4 H_GB²) = 45/(4 g_eff)

where S_dS is de Sitter horizon entropy at gauge birth (Bekenstein–Hawking units). For g_eff = 106.75 (§17.5.10): **N_lock = 45/427 ≈ 0.1054**, matching corpus N_lock ≈ 0.1.

**(C1) T_GB = M_Pl/√(2π).** Hartle-Hawking Gaussian saddle temperature; corpus "T_GB ~ 0.4 M_Pl" is 1/√(2π) ≈ 0.399 M_Pl_red. Verified at structural level in Companion 9 Session 3 (§17.5.4 (C1) cross-ref); full first-principles closure: Programme S Paper S2 / explicit S_E[saddle] in boundary action.

**(C2) N_lock = S_dS/4.** Pre-temporal e-fold count equals one-quarter of horizon entropy at gauge birth — holographic identity tying locking transition to thermodynamic horizon formation. Open: derive from Appendix B.3 Lagrange-multiplier boundary action (§22.19).

**Parameter accounting.** Under (C1)+(C2), N_lock is **not an independent calibration**; it is fixed by g_eff (SM relativistic d.o.f. count, §17.5.10). T_GB moves from opaque calibration to candidate structural derivation alongside N_lock. No empirical predictions change.

**Still open for rigorous closure:** (i) explicit HH saddle calculation in NTE's ξ = 1/6 action; (ii) holographic proof of N_lock = S_dS/4. See §22.18–§22.19.
```

---

## Patch T2b-2: §17.5.9 — remove stale N_lock deferral

**Find:**

```
**Open work (research programme).** Full Planck + DESI + BAO χ² fits not in corpus. Priority: (i) epoch-by-epoch ρ_Φ ↔ α²|Φ|⁴ through radiation/matter/Λ; (ii) explicit homogeneous BAO distance comparison; (iii) structure growth / σ_8 under H(x,N). Working scaffold: `Working/LCDM_Reduction_Appendix_Scaffold_v0_1_20260523.md`. **N_lock** derivation remains separate (§17.5.4; `17.5.4_Audit_NLock_Derivation.md` in depreciated/).
```

**Replace with:**

```
**Open work (research programme).** Full Planck + DESI + BAO χ² fits not in corpus. Priority: (i) epoch-by-epoch ρ_Φ ↔ α²|Φ|⁴ through radiation/matter/Λ; (ii) explicit homogeneous BAO distance comparison; (iii) structure growth / σ_8 under H(x,N). Working scaffold: `Working/LCDM_Reduction_Appendix_Scaffold_v0_1_20260523.md`. N_lock candidate derivation: §17.5.4 (audit `Papers/17.5.4_Audit_NLock_Derivation.md`).
```

---

## Patch T2b-3: §XVII parameter accounting — N_lock / T_GB

**Find:**

```
Constrained by Observation (Not Yet Derived): M_R (Majorana mass scale, pathway identified). M₁ closed at S1 v10.10 — see §XXI Closed Gaps; Companion 10.
```

**Replace with:**

```
Candidate structural derivation (pending rigorous closure): N_lock = 45/(4 g_eff) ≈ 0.105; T_GB = M_Pl/√(2π) ≈ 0.399 M_Pl_red — see §17.5.4, Companion 9 Session 3.

Constrained by Observation (Not Yet Derived): M_R (Majorana mass scale, pathway identified). M₁ closed at S1 v10.10 — see §XXI Closed Gaps; Companion 10.
```

---

## Patch T2b-4: §22.18–§22.19 (new) — after §22.17, before Closing remark

**Find:**

```
**Cross-references:** §6.3; §9.1–9.3; §17.5.5; §22.6 (superseded); §22.16 (local μ(x,N) programme — parallel, still open).

Closing remark: these pathways are open because NTE's structure makes them precisely formulable
```

**Replace with:**

```
**Cross-references:** §6.3; §9.1–9.3; §17.5.5; §22.6 (superseded); §22.16 (local μ(x,N) programme — parallel, still open).

22.18 Hartle-Hawking saddle temperature in NTE's regime (Pathway for Exploration, v10.13)

Verify that the Hartle-Hawking instanton calculation in NTE's pre-temporal regime (ξ = 1/6 action per §17.5.15; Companion 9 v10.8 §3.1) produces T_HH = M_Pl/√(2π) as the saddle's dominant exit temperature. If so, T_GB ≈ 0.4 M_Pl in corpus prose is structurally derived as rounded 1/√(2π). Tied to Companion 9 / Programme S Paper S2. Cross-ref: §17.5.4 (C1); §22.14 T_GB leg.

22.19 Holographic identity N_lock = S_dS/4 (Pathway for Exploration, v10.13)

Verify that the boundary action's Appendix B.3 Lagrange-multiplier structure produces a holographic identity N_lock = S_dS/4 between the pre-temporal phase's e-fold count and de Sitter horizon entropy at gauge birth. If so, N_lock ≈ 0.1 is structurally derived as 45/(4 g_eff) given g_eff from §17.5.10. Parallel to Gap 4b closure (§22.17). Cross-ref: §17.5.4 (C2); Jammer audit `17.5.4_Audit_NLock_Derivation.md`.

Closing remark: these pathways are open because NTE's structure makes them precisely formulable
```

---

## Patch T2b-5a: Part 1 header v10.13

**Find:**
```
> **NTE v10.10 — Part 1 of 3: Foundations + Method**  
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.12 (ship date: 2026-05-23). Tier 2 §17.5.9 ΛCDM reduction expansion; carries v10.11 Programme S + Tier 0 + v10.9 A5+A6.
```

**Replace with:**
```
> **NTE v10.13 — Part 1 of 3: Foundations + Method**  
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.13 (ship date: 2026-05-23). Tier 2b §17.5.4 N_lock candidate derivation; carries v10.12 ΛCDM + prior tiers.
```

## Patch T2b-5b: Part 2 header v10.13

**Find:**
```
> **NTE v10.10 — Part 2 of 3: Structure + Dynamics**  
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.12 (ship date: 2026-05-23). Carries v10.11 Programme S spine + prior tiers.
```

**Replace with:**
```
> **NTE v10.13 — Part 2 of 3: Structure + Dynamics**  
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.13 (ship date: 2026-05-23). Carries v10.12+ prior tiers.
```

## Patch T2b-5c: Part 3 header v10.13

**Find:**
```
> **NTE v10.10 — Part 3 of 3: Accounting + Open Work + Appendices**
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.12 (ship date: 2026-05-23). v10.12: §17.5.9 ΛCDM reduction expansion (Tier 2); v10.11: Programme S spine; v10.10: Gap 1 S1, r, A5+A6.
```

**Replace with:**
```
> **NTE v10.13 — Part 3 of 3: Accounting + Open Work + Appendices**
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.13 (ship date: 2026-05-23). v10.13: §17.5.4 N_lock candidate derivation (Tier 2b); v10.12: §17.5.9 ΛCDM; v10.11: Programme S; v10.10: Gap 1, r, A5+A6.
```
