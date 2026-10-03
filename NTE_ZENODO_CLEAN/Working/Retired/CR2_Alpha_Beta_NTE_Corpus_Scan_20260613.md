# α ↔ β_NTE corpus scan — multi-pass repair log

**Author:** Cursor Main  
**Date:** 2026-06-13  
**Trigger:** Greg — Hopf pedagogical pivot line *"fine-structure constant β_NTE ≈ 1/137"* (value collision; obvious mis-rename).

## Symbol discipline (Greg 2026-06-04)

| Symbol | Object | Typical value |
|--------|--------|---------------|
| **α_em** | Fine-structure / QED coupling | ≈ 1/137 |
| **α₁, α₂, α₃** | SM gauge couplings at M_Pl | ~0.017, 0.034, 0.065 |
| **β_NTE** | H-coefficient in **H = β_NTE\|Φ_NTE\|²** | ≈ 2.38×10⁻⁴⁷ GeV⁻¹ |

## Root cause

June 2026 `α → β_NTE` rename used over-broad rule **`constant α` → `constant β_NTE`**, which caught *"fine-structure constant α"* when **α_em** was intended. Value context (1/137) should have been an automatic block.

## Pass 1 — pattern grep (Papers + Book + Working + Outreach)

Subagents + parent grep. **Canonical Papers:** 8 files with HIGH-confidence collisions (pre-fix).

## Pass 2 — automated repair

Script: `Working/alpha_beta_nte_corpus_fix_pass.py`  
**631 files scanned; 100 files patched.**

### Canonical Papers fixed

- `Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md` — α_em ≈ 1/137 (manual + script)
- `Companion_5_StateSpace_Surface_v10_8.md` — §8.1 header → cosmological coupling β_NTE
- `NTE_v10_17_Part2_Structure.md` — β_NTE₁/₂/₃ → **α₁/₂/₃** (gauge couplings)
- `Companion_11_Lambda_Unimodular_Closure_v10_17_2.md` — α_char → β_NTE,char
- `Companion_11_Lambda_Unimodular_Closure_v10_17.md` — partial β_NTE pass (superseded; v10.17_2 canonical)
- `Paper_Solar_*_v0_2/v0_3` — α-chain / α-coupling → β_NTE-chain / β_NTE-coupling
- `Paper_S2_*`, `Paper_S6_*` — tier-register α → β_NTE
- `NTE_Standalone_Papers_Register_v0_5.md` — α-decoupled → β_NTE-decoupled

### Other lanes

- `Outreach/Distribution_Campaign_v1_20260530.md` — H = β_NTE|Φ|²; β_NTE-chain
- `Working/NTE_Reader_Glossary_Companion_v1_0.md` — split **α_em** vs **β_NTE** rows
- `Book/Book_with_TP/*` — stale parallel copy synced (11 chapters + Appendix A)
- ~60 Working memos — H-coefficient α → β_NTE; V_NTE α² → β_NTE²

### Pass 2 residual (false positives — correct disambiguation)

Lines mentioning **both** β_NTE and 1/137 in *disambiguation* prose (Part 1 §2.4.2, C7 footnote, Necessity pivot footnotes) — **no fix**.

### Not scanned (archive)

`Papers/depreciated/` excluded from automated pass — pre-rename snapshots; not in PDF pipeline.

## Pass 3 — audit script hardening

`Working/alpha_to_beta_nte_audit.py` — added PROTECT for `fine-structure constant α` / `α_em` before `constant α` replacement.

## Re-run

```text
python Working/alpha_beta_nte_corpus_fix_pass.py          # dry-run
python Working/alpha_beta_nte_corpus_fix_pass.py --apply  # patch
```

Report: `Working/alpha_beta_nte_corpus_fix_report.json`

---

— Cursor Main, 2026-06-13.
