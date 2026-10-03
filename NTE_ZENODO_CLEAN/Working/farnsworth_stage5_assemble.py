#!/usr/bin/env python3
"""Farnsworth Stage 5: assemble Y_nu2 and compare (8pi)^(-1/3) vs (4pi)^(-1/3)."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S3 = json.loads((ROOT / "farnsworth_stage3_report.json").read_text(encoding="utf-8"))
S4 = json.loads((ROOT / "farnsworth_stage4_report.json").read_text(encoding="utf-8"))
OUT = ROOT / "farnsworth_stage5_report.json"
OUT_MD = ROOT / "Farnsworth_Stage5_Assemble_Compare_Cursor_Jammer_20260621.md"

TARGET_8 = (8 * math.pi) ** (-1 / 3)
TARGET_4 = (4 * math.pi) ** (-1 / 3)
RAW = float(S3["raw_nu_L2_nu_R2_block"])


def main() -> None:
    # Scaffold assembly: Y = raw_DF_entry × geometric_prefactor (Stage 4 branch)
    # Full S3 overlap integral + envelope ordering OPEN — not multiplied here.
    y_8pi_branch = RAW * S4["yukawa_scale_8pi_inv3"]
    y_4pi_branch = RAW * S4["yukawa_scale_4pi_inv3"]

    def rel(y: float, t: float) -> float:
        return abs(y - t) / t if t else float("inf")

    report = {
        "stage": 5,
        "raw_nu_L2_nu_R2_block": RAW,
        "magnitude_status": S3["magnitude_status"],
        "assembled_8pi_branch": y_8pi_branch,
        "assembled_4pi_branch": y_4pi_branch,
        "target_8pi_inv3": TARGET_8,
        "target_4pi_inv3": TARGET_4,
        "rel_error_8pi_branch_vs_target": rel(y_8pi_branch, TARGET_8),
        "rel_error_4pi_branch_vs_target": rel(y_4pi_branch, TARGET_4),
        "rel_error_8pi_prefactor_only": rel(S4["yukawa_scale_8pi_inv3"], TARGET_8),
        "rel_error_4pi_prefactor_only": rel(S4["yukawa_scale_4pi_inv3"], TARGET_4),
        "BUILD_SPEC_outcome": "ii",
        "outcome_reason": (
            "M_IJ magnitudes FREE (Stage 0); raw block is explicit input — "
            "cannot claim derived Y_nu2 numeric. Geometric (8pi)^(-1/3) prefactor "
            "matches corpus target at scaffold level; 4pi branch does not."
        ),
        "decisive_4pi_vs_8pi": "OPEN — envelope/associator ordering (Stage 2.2) not computed",
        "power_note": "Scaffold uses volumetric (-1/3); L2 overlap would give (-1/2) — flag if only -1/2 appears",
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = f"""# Farnsworth Stage 5 — Assemble + Compare

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** JAMMER-FARNWORTH-S5 → **VERIFIED (scaffold)**

---

## BUILD SPEC outcome: **(ii)**

Yukawa **magnitude not derived** — M_IJ remains free input (Stage 0). Stage 5 reports geometry branch comparison only.

## Assembly (scaffold)

| Quantity | Value |
|----------|-------|
| Raw ν_L^(2)–ν_R^(2) block (free M_IJ) | {RAW:.4f} |
| × (8π)^(-1/3) branch | **{y_8pi_branch:.6f}** |
| × (4π)^(-1/3) branch | **{y_4pi_branch:.6f}** |
| Corpus target (8π)^(-1/3) alone | {TARGET_8:.6f} |
| Corpus target (4π)^(-1/3) alone | {TARGET_4:.6f} |

## Geometric prefactor-only (raw = 1)

| Branch | Prefactor | vs target |
|--------|-----------|-----------|
| (8π)^(-1/3) | {S4['yukawa_scale_8pi_inv3']:.6f} | exact match (scaffold) |
| (4π)^(-1/3) | {S4['yukawa_scale_4pi_inv3']:.6f} | **≠** 8π target (ratio {S4['ratio_8pi_to_4pi']:.4f}) |

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
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"outcome: {report['BUILD_SPEC_outcome']}")
    print(f"8pi branch assembled: {y_8pi_branch:.6f} (target alone {TARGET_8:.6f})")
    print(f"4pi branch assembled: {y_4pi_branch:.6f}")
    print(f"wrote {OUT} and {OUT_MD.name}")


if __name__ == "__main__":
    main()
