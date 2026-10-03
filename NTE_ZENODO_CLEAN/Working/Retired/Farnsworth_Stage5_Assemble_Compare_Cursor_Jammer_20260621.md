# Farnsworth Stage 5 — Assemble + Compare

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** JAMMER-FARNWORTH-S5 → **VERIFIED (scaffold)**

---

## BUILD SPEC outcome: **(ii)**

Yukawa **magnitude not derived** — M_IJ remains free input (Stage 0). Stage 5 reports geometry branch comparison only.

## Assembly (scaffold)

| Quantity | Value |
|----------|-------|
| Raw ν_L^(2)–ν_R^(2) block (free M_IJ) | 0.7000 |
| × (8π)^(-1/3) branch | **0.238974** |
| × (4π)^(-1/3) branch | **0.301089** |
| Corpus target (8π)^(-1/3) alone | 0.341392 |
| Corpus target (4π)^(-1/3) alone | 0.430127 |

## Geometric prefactor-only (raw = 1)

| Branch | Prefactor | vs target |
|--------|-----------|-----------|
| (8π)^(-1/3) | 0.341392 | exact match (scaffold) |
| (4π)^(-1/3) | 0.430127 | **≠** 8π target (ratio 0.7937) |

## Verdict

- **Outcome (ii):** magnitude **Ansatz-scaled**, not derived — **STOP claiming derived Y_ν2** from Farnsworth alone.
- **4π vs 8π:** still **OPEN** until Stage 2.2 envelope ordering (Scratch lane).
- **Power (-1/3):** present only via volumetric flux scaffold; L2 overlap (-1/2) not computed.

**Recommendation:** Route Stage 2.2 envelope decision to Scratch; do not propagate (8π)^(-1/3) as derived Yukawa without CPN/σ₂ fixation.

---

```text
python Working/farnsworth_stage5_assemble.py
```

— Cursor Jammer, 2026-06-21.
