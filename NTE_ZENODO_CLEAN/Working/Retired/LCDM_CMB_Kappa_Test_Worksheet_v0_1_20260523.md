# ΛCDM Tier 2c — CMB κ amplitude test worksheet scaffold (P5)

**Stream:** Cursor scaffold → **Jammer** execution  
**Date:** 2026-05-23 (v0.1)  
**Status:** Scaffold only — **no Planck likelihood run**

**Gate #6 routing:** Jammer numerics primary; this file is the worksheet shell.

---

## §1. Test (from §17.5.12 diagnostic (d))

At z ~ 1100 (recombination), δρ/ρ ~ 10⁻⁵ — **nearly homogeneous**. Void-bias that affects low-z BAO/w₀ should **not** affect CMB-inferred κ the same way.

**NTE prediction:** κ ≈ 5.50 ± 0 (zero theoretical uncertainty in corpus framing).  
**Planck 2018:** κ_obs ≈ 5.38 ± 0.15 (0.83σ).

**Falsifier F3 (P4 catalogue):** CMB κ converges to value ≠ 5.50 at z~1100 with void bias ruled out.

---

## §2. Jammer tasks

| # | Task | Notes |
|---|------|-------|
| 1 | Define κ extraction from Planck 2018 (Ω_m h², Ω_b h², or peak-height ratio — cite method) | Hold r_d / H₀ convention explicit |
| 2 | Propagate uncertainty to κ | Compare to 5.50 band [5.27, 5.73] at CMB-S4 milestone |
| 3 | Document why void bias is negligible at z~1100 | Cross-ref Part 2 §13.3 diagnostic (d) |
| 4 | Separate κ from Ω_m degeneracy | Honest: partial degeneracy remains |

---

## §3. Cross-references

- §9.3, §17.5.12 (κ falsifier)  
- `LCDM_Chi2_Falsifier_Catalogue_v0_1_20260523.md` (F3)  
- P2 reconciliation (low-z bias must **not** replicate here)

— Cursor scaffold, 2026-05-23.
