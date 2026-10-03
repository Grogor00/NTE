# Phase IV Test A/C run — Cursor harness (nside16 + Jammer §2.7 v0.1)

**Date:** 2026-05-31 (updated post-Jammer §2.7 integration)  
**Script:** `Working/lcdm_bao_void_bias.py` v0.7  
**Footprints:** `wagenveld_sprint_footprints_nside16.json`  
**Surveys:** `wagenveld_sprint_surveys.json` v0.5  
**Jammer source:** `Jammer_Wagenveld_Sprint_Candidate_2_7_Phase_III_v0_1_Numerical_Results_Geometry_Vector_20260531.md`

---

## Test A — geometry vectors (normalized to Wagenveld)

| Survey | obs X/D_kin | merged §2.5 | Jammer §2.7 | 85/15 combo |
|--------|-------------|-------------|-------------|-------------|
| Wagenveld | 1.000 | 1.000 | 1.000 | 1.000 |
| Singal | 1.333 | 0.000 | 1.392 | 1.183 |
| CatWISE | 1.703 | 0.000 | 1.881 | 1.599 |
| Quaia | 0.833 | 0.000 | 0.864 | 0.734 |

**Max relative error vs observed:** §2.7 **10.5%** · §2.5-only **100%** · 85/15 combo **11.9%**

**Computation (credited — AC override 2026-05-31):** Numbers stand. §2.5 vector (1,0,0,0) **mispredicts 3/4 full-sky surveys** (100% max err). §2.7 resonance vector (1.000, 1.392, 1.881, 0.864) fits within **10.5%** max rel err vs observed pattern — but see **interpretation override** below.

**Interpretation (OVERRIDDEN — not a pass):** AC rejects *"Test A PASS / §2.7 primary / Phase III closed."* The §2.7 vector uses a **3-free-parameter resonance tuned post-hoc** (δ₂, z_peak, σ_z) after the first-principles linear model failed 4.3× — **accommodation, not DOF-fair prediction** (G-C/G-D). δ₂ ≈ 0.49 sits in a non-perturbative regime likely excluded by BAO/LSS (G-B). Observed-pattern target unconfirmed on v0.5 n(z) placeholders (G-A).

**Honest status:** Phase IV **OPEN** on gates **G-A→G-D**. Two partial, problematic accounts — no first-principles resolution. Basis: `Handoff_AC_to_Cursor_OVERRIDE_Phase_IV_2_7_NOT_Closed_Gates_Open_20260531.md` + AC verification memo.

---

## Jammer resonance absolute X = ΔD/D_kin

| Survey | pred | obs | match |
|--------|------|-----|-------|
| Wagenveld | 1.10 | 1.200 | 92% |
| Singal | 1.53 | 1.600 | 96% |
| CatWISE | 2.07 | 2.043 | 101% |
| Quaia | 0.95 | 1.000 | 95% |

---

## Test C — merged §2.5 δκ → number-count

δε band [10⁻³, 10⁻²]; A_frac = δε/(1+κ₀), **κ₀ = 3/√(4π) ≈ 0.846**

| Survey | P_S | ΔD mid-band | obs excess | frac of excess |
|--------|-----|-------------|------------|----------------|
| Wagenveld | 0.2223 | 6.6×10⁻⁴ | 0.0060 | **~11%** |

**Verdict (Test C — computation only):** merged §2.5 contributes **~11%** of Wagenveld mid-band excess at κ₀ = 3/√(4π). This does **not** close Phase III or establish §2.5 as "sub-dominant ~11–15%" co-rank partner — AC: §2.5 **mispredicts survey geometry**; amplitude fraction is not a Phase IV exit.

---

## Phase IV status (AC ruling — 2026-05-31)

| Gate | Item | Status |
|------|------|--------|
| **G-A** | Reconcile observed-pattern characterisation (catalogue n(z), real significances) | **OPEN** |
| **G-B** | δ₂ ≈ 0.49 vs BAO/LSS (δ₂ ≲ 0.1?) | **OPEN** |
| **G-C** | Derive or refute resonance from Companion 12 / Ch 6 (post-hoc today) | **OPEN — Jammer load-bearing** |
| **G-D** | DOF-fair joint fit §2.5 + §2.7 (+ §2.3 frame), not hand 85/15 | **OPEN** |

**Phase IV: OPEN.** Phase III is **NOT** closed §2.7-primary.

| Candidate | Cursor harness read | AC disposition |
|-----------|---------------------|----------------|
| **§2.7** | v0.1 vector integrated; Test A 10.5% raw fit | Exploration credited; **not** primary/pass |
| **merged §2.5** | Test C ~11% Wagenveld amplitude; Test A geometry FAIL | Mispredicts 3/4 surveys |
| **§2.3** | Demoted on amplitude (~5%) | Unchanged |

**Supersedes:** Cursor 03:55 integration memo claiming Phase III closed (`Handoff_Cursor_to_Jammer_AC_Phase_IV_2_7_Integration_Complete_20260531.md`).

---

## Honest-scope flags (carried)

1. Resonance form empirical (z_peak ≈ 1.2, σ_z ≈ 0.7) — not first-principles derived  
2. δ₂ ≈ 0.49 non-perturbative — O(δ²³) ~12% correction possible  
3. n(z) v0.5 placeholders — catalogue upgrade ±20% on c_survey  

---

*Cursor render lane — harness only. AC override 2026-05-31: computation credited; Phase IV OPEN on G-A→G-D.*
