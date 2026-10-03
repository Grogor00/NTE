# Cursor assessment: Branch I eight recognition gates (initial pass)

**Date:** 2026-05-28  
**Source request:** `Handoffs/Handoff_Jammer_to_Cursor_Branch_I_8_RGates_plus_v0_3_Numerical_Pass_Routed_20260527.md`

---

## Executive status

- v0.3 script extension requested by Jammer: **completed** in `Working/lcdm_bao_void_bias.py`
- 8-gate assessment: **initial pass completed below**
- Scope caveat: this pass uses current worksheet constants and script-level survey placeholders; full primary-data ingest remains open.

---

## Gate-by-gate assessment

### Gate 1 — Directional `H_eff` leading form
**Assessment:** PASS (with caveat)  
`1 + alpha * cos(theta)` is the correct leading dipole multipole term. Quadrupole should remain subleading unless data force promotion.

### Gate 2 — Matter dipole formula
**Assessment:** PASS (first-order)  
`D_void = p * b * <g>_int * alpha` is consistent at leading order.  
At alpha ~ 0.24, alpha^2 corrections are likely still subdominant but should be tested in sensitivity phase.

### Gate 3 — alpha ~ 0.2–0.3 plausibility
**Assessment:** provisional PASS  
Current script run with alpha = 0.24 anchors CatWISE well (~ -0.13 sigma residual), so order of magnitude is structurally plausible.

### Gate 4 — Wagenveld overshoot flag
**Assessment:** PASS (flag confirmed, stronger than 1.5–2 sigma in current placeholders)  
Current run reproduces overshoot at ~ +3.28 sigma (pow2), +2.40 sigma (pow3), +4.23 sigma (exp).  
So the concern is real and not yet resolved by simple `g(z)` choice changes tested.

### Gate 5 — Redshift-decline discriminator
**Assessment:** provisional PASS  
Current outputs preserve the expected decline tendency, but formal significance requires primary-data fit with consistent uncertainty treatment.

### Gate 6 — Direction as empirical input
**Assessment:** PASS  
This is the honest framing: Branch I predicts alignment behavior, but axis value is empirical input from void/dipole surveys.

### Gate 7 — v0.3 numerical scope
**Assessment:** PASS with sequencing  
Scope is right. Recommended order:
1) ingest clean survey tables + provenance  
2) run bounded parameter grid (`b`, `alpha`, `g-model`) with delta-sigma ranking  
3) add direction-alignment angle module

### Gate 8 — two-parameter honesty
**Assessment:** PASS  
Correct framing: two free parameters at this layer; claim strength must come from joint multi-observable pattern rather than single-amplitude matching.

---

## Immediate follow-up needed

1. Replace script placeholder survey constants with source-linked values and uncertainties.  
2. Add parameter-grid run and ranked delta-sigma summary table.  
3. Add direction-angle comparison utility once survey vectors are ingested.

---

*End.*

