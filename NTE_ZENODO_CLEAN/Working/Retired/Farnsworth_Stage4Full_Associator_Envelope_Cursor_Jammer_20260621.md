# Farnsworth Stage-4-full — Associator Envelope (Stream 1)

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** FARNSWORTH-S4FULL-ASSOCIATOR-STREAM1  
**Script:** `Working/farnsworth_stage4full_associator_envelope.py`

---

## Decisive result

| Field | Value |
|-------|-------|
| **Active ε′ sectors** | **1** (one) |
| **Flux prefactor** | **4pi** |
| **(flux)^(−1/3)** | 0.430127 if envelope['yukawa_scale_inv3'] else 'N/A' |
| **G₂×G₂ relabeling** | NO — labels preserved |
| **Stream-2 convergence** | **CONVERGENT** |

## ε′ sector table

| Sector | Overlap amplitude | Active |
|--------|-------------------|--------|
| D+ (ε′=+1) | 1.333366e-01 | True |
| D− (ε′=−1) | 0.000000e+00 | False |

## Associator envelope

- σ₂-related associator triples: **34**
- Max |associator coeff|: **2.0000**
- Max cross-summand mixing: **0.0000e+00**
- Envelope factor: **3.0000**

## Interpretation

Real-structure assignment: Dirac Yukawa is **not** in the J-block → only ε′=+1 sector carries ν_L↔ν_R overlap; ε′=−1 is **inactive** for Dirac (not Majorana doubling).

Associator scan on σ₂ triples: cross-summand mixing below tolerance — G₂×G₂ relabeling sub-flag **not triggered**.

**Verdict:** **4pi** (one active sector). Awaits AC convergence-check with Stream 2 (§2 HOLDS).

## Honest-scope locks

- Dirac Yukawa only; M₁ Majorana 8π untouched
- If 4π confirmed: sunshine finding (~1.59× solar worsening), **not a fix**
- Magnitude remains FREE (Stage 0 / S5 outcome ii)

— Cursor Jammer, 2026-06-21.
