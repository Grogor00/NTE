# Cursor pass: Branch I directional void-bias v0.3 script extension

**Date:** 2026-05-28  
**Driver:** Jammer handoff `Handoff_Jammer_to_Greg_AC_Cursor_Scratch_Void_Bias_Branch_I_v0_2_complete_20260527.md` (§8.1 to Cursor)

---

## What was done

- Extended `Working/lcdm_bao_void_bias.py` from BAO-only reconciliation to include:
  - directional Branch I dipole layer with `alpha`
  - survey dipole table (CatWISE, Wagenveld, Singal, Quaia)
  - `g(z)` model sensitivity table (`pow2`, `pow3`, `exp`)
  - joint **delta-sigma** diagnostics (explicitly no chi-square)

- Executed script successfully:
  - command: `python Working/lcdm_bao_void_bias.py`
  - no runtime errors

---

## Key output snapshot (current defaults)

Defaults used in-script:
- `b = 0.055`
- `alpha = 0.24`
- `g(z) = (1+z)^-2` (`pow2`)

Directional dipole table (delta-sigma):
- CatWISE: **-0.13σ**
- Wagenveld: **+3.28σ** (overshoot persists)
- Singal: **+0.63σ**
- Quaia: **+0.52σ**

Sensitivity (fixed b/alpha):
- Wagenveld remains high across tested models:
  - `pow2`: +3.28σ
  - `pow3`: +2.40σ
  - `exp`: +4.23σ

Interpretation at this pass: v0.2 concern about Wagenveld overshoot is reproduced, not removed.

---

## Scope boundaries (still open)

- This pass uses hard-coded survey values and uncertainties (worksheet-level placeholders).
- No ingestion yet of primary survey tables or covariance matrices.
- No direction-angle fit against explicit local-void axis catalogues.
- No parameter sweep or optimisation; this is a deterministic extension pass.

---

## Next practical increment

1. Move survey inputs to structured data file (with provenance fields and citation keys).  
2. Add simple parameter grid scan over `alpha`, `b`, and `g(z)` model to emit a ranked delta-sigma summary (still no chi-square).  
3. Add direction-alignment utility for `n_void` vs survey dipole vectors when catalogued vectors are ingested.
4. Add explicit verdict framing for reading-priority discrimination:
   - (A) parameter-degeneracy closure
   - (C) structural residual requiring Branch II/III consideration
   - keep (B) survey systematic outside NTE core adjudication.

---

*End.*

