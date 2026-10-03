# Master v10.9 → v10.10 Patch Instructions

## Tier 0 — Corpus integration housekeeping (Cursor draft for AC ratification)

**Date:** 2026-05-23.  
**Author lane:** Cursor (Greg local render) → **AC** canonicalises after Greg ratification.  
**Scope:** Reconcile master §XXI / §XVII with Companion 10 Gap 1 S1 closure; align r listing with §18.4; v10.10 headers. No new physics.

**Greg ratification required:** Adopt Companion 10 v10.8 Pathway α as master-canonical Gap 1 closure at **S1 (M_R-comparable) precision**. S2 (Paper S2 spectral-triple uniqueness) remains open.

**Render target:** Local `NTE_v10_9_Part*.md` → output `NTE_v10_10_Part*.md` (or in-place version bump per Greg).

---

## Patch T0-1a: §XXI opening paragraph — Gap 1 status

**Location:** Part 3 §XXI, first paragraph after heading.

**Find:**

```
Five original gaps. Gap 2 analytically closed (v10.3). Gap 3 partially closed (v10.3). Gap 4a closed (v10.2). Gap 5 closed (v10.2). Gap 1 remains open. Additional gaps identified and tracked below.
```

**Replace with:**

```
Five original gaps. Gap 2 analytically closed (v10.3). Gap 3 partially closed (v10.3). Gap 4a closed (v10.2). Gap 5 closed (v10.2). Gap 1: M₁ leptogenesis scale closed at S1 precision v10.10 (Companion 10 Pathway α); y_eff(N) Planck-era form factor f remains open (§22.5). Additional gaps identified and tracked below.
```

---

## Patch T0-1b: §XXI Tier 1 — Gap 1 bullet

**Find:**

```
Gap 1: UV physics at the Planck epoch. The effective Yukawa coupling function y_eff(N) requires the form factor f from first principles. Also: M₁ from Janus geometry would make baryon asymmetry a zero-parameter prediction.
```

**Replace with:**

```
Gap 1 (partial closure v10.10): M₁ from Janus geometry — closed at S1 (M_R-comparable precision) per Companion 10 v10.8 Pathway α: M₁ = (8π)^(1/3) × (M_Pl² × H_GB)^(1/3) ≈ 5.4 × 10⁹ GeV (M₁,obs ≈ 6.06 × 10⁹ GeV; ratio 0.89). Baryon asymmetry η = 6.1 × 10⁻¹⁰ is a complete zero-parameter prediction at S1 rigor. **Still open:** y_eff(N) form factor f at Planck epoch (§22.5); M₁ prefactor uniqueness at S2 (Programme S Paper S2).
```

---

## Patch T0-1c: §XXI Tier 1 — remove duplicate M₁ line

**Find:**

```
M₁ from geometry: The leptogenesis scale M₁ = 6 × 10⁹ GeV is constrained, not derived. Should follow from S³ curvature radius and gauge birth temperature.
```

**Replace with:**

```
M₁ cross-reference: §22.2; Companion 10 v10.8. S2 prefactor programme: Programme S Paper S2 (Charter §3).
```

---

## Patch T0-1d: §XXI Closed Gaps — add Gap 1

**Find:**

```
Gap 5: Born rule from S³ — closed at the level of physical mechanism. Gauge birth + Hopf fibration supplies the U(1)-fibre activation story (Companion 6); the two-layer gauge symmetry argument closes Step 1 of Paper 2's derivation under its complex-Hilbert-space + global-U(1)-phase inputs. The complementary scope question — whether the rule's specific quadratic form derives from less than those inputs (bilinearity in amplitude; complex Hilbert space structure) — is the framework's standing open research target at §17.5.13.
κ y_ν correction: Exactly zero — topological protection of Y₀₀(S²) proven.
```

**Replace with:**

```
Gap 5: Born rule from S³ — closed at the level of physical mechanism. Gauge birth + Hopf fibration supplies the U(1)-fibre activation story (Companion 6); the two-layer gauge symmetry argument closes Step 1 of Paper 2's derivation under its complex-Hilbert-space + global-U(1)-phase inputs. The complementary scope question — whether the rule's specific quadratic form derives from less than those inputs (bilinearity in amplitude; complex Hilbert space structure) — is the framework's standing open research target at §17.5.13.
Gap 1 (M₁, S1, v10.10): Leptogenesis scale from S³ + Hopf + Killing-spinor cube-root quantization (Companion 10 Pathway α). η zero-parameter at S1; S2 uniqueness via Paper S2 queued.
κ y_ν correction: Exactly zero — topological protection of Y₀₀(S²) proven.
```

---

## Patch T0-2a: §XVII Derived list — r line

**Find:**

```
- r = 0.0030 from N_e (v10.4)
```

**Replace with:**

```
- r ≈ 4×10⁻³ (hilltop reading (iii), §18.4 v10.8; K(Φ) closure via Paper S2 pending); legacy Mechanism-B r = 0.0030 route superseded
```

---

## Patch T0-2b: §XVII category (A) — r line

**Find:**

```
- r = 0.0030 (forward-looking; testable by CMB-S4 / LiteBIRD)
```

**Replace with:**

```
- r ≈ 4×10⁻³ hilltop (reading (iii), §18.4); falsification commitments per §17.5.12 Category A
```

---

## Patch T0-2c: §XVII Constrained by Observation

**Find:**

```
Constrained by Observation (Not Yet Derived): M₁ (leptogenesis scale), M_R (Majorana mass scale, pathway identified).
```

**Replace with:**

```
Constrained by Observation (Not Yet Derived): M_R (Majorana mass scale, pathway identified). M₁ closed at S1 v10.10 — see §XXI Closed Gaps; Companion 10.
```

---

## Patch T0-3: Part 3 header (v10.10)

**Find:**

```
> **NTE v10.9 — Part 3 of 3: Accounting + Open Work + Appendices**
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.9 (ship date: 2026-05-23). v10.9 patches: §17.5.10 closed-by-enumeration v10.9; §XVII Parameter Accounting framing upgrade; §17.5.12 falsifiability catalogue consolidation; §XXI Gap 5 + §20.5 Born rule scope alignment (A5).
```

**Replace with:**

```
> **NTE v10.10 — Part 3 of 3: Accounting + Open Work + Appendices**
> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.10 (ship date: 2026-05-23). v10.10 patches: §XXI Gap 1 / M₁ S1 integration (Companion 10); §XVII r alignment with §18.4 three-readings; carries forward v10.9 A5+A6 (§17.5.10, §17.5.12, §XXI Gap 5, §20.5).
```

---

## Patch T0-3b: Part 1 header (v10.10, minimal)

**Find:**

```
> **NTE v10.9 — Part 1 of 3: Foundations + Method**  
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.9 (ship date: 2026-05-23). No A5/A6 content patches (carried from v10.8).
```

**Replace with:**

```
> **NTE v10.10 — Part 1 of 3: Foundations + Method**  
> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. Master canonical at v10.10 (ship date: 2026-05-23). Tier 0 integration ship; content carried from v10.9 / v10.8.
```

---

## Patch T0-3c: Part 2 header (v10.10, minimal)

**Find:**

```
> **NTE v10.9 — Part 2 of 3: Structure + Dynamics**  
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.9 (ship date: 2026-05-23). v10.9 patches: §8.7.7 helicity bookkeeping clarification (A6).
```

**Replace with:**

```
> **NTE v10.10 — Part 2 of 3: Structure + Dynamics**  
> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). Master canonical at v10.10 (ship date: 2026-05-23). Carries forward v10.9 §8.7.7 helicity clarification (A6).
```

---

## What is NOT in Tier 0

- Programme S / Paper S2 content (Tier 1)
- ΛCDM appendix (Tier 2)
- Abstract Part 1 η zero-parameter claim (requires broader AC edit)
- N_lock calibration disclosure (separate patch)

---

— Cursor draft for AC ratification (2026-05-23)
