#!/usr/bin/env python3
"""Run Bridge Law Phase-0 catalog algebra; write markdown + JSON results."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # Working/
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bridge_law.candidates import KAPPA0, catalog, phase0_verdict, summary_table

OUT_MD = ROOT / "BRIDGE_LAW_PHASE0_CATALOG_AND_ALGEBRA_RESULT_Cursor_Main_20261007.md"
OUT_JSON = ROOT / "bridge_law" / "phase0_results.json"


def main() -> None:
    rows = catalog()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md = "\n".join(
        [
            "# Bridge Law — Phase 0 catalog & algebra result",
            "",
            f"**Author:** Cursor Main · **Ran:** {now}",
            "**Parent:** `Handoffs/Directive_Cursor_Main_Bridge_Law_From_Snu_Or_Bigravity_Research_Programme_20261007.md`",
            f"**κ₀ = 3/√(4π) = {KAPPA0:.6f}** (input; not fitted)",
            "",
            "## Candidate table",
            "",
            summary_table(rows),
            "",
            phase0_verdict(rows),
            "## Per-candidate notes",
            "",
        ]
    )
    for r in rows:
        md += (
            f"### {r.id} — {r.name}\n\n"
            f"- Track: `{r.track}` · Fundamental: **{r.fundamental}**\n"
            f"- EOM: `{r.eom_sketch}`\n"
            f"- r_bg formula: {r.r_bg_formula}\n"
            f"- Ghost risk: {r.ghost_risk}\n"
            f"- Perturbation character: {r.perturbation_character}\n"
            f"- Notes: {r.notes}\n\n"
        )
    md += (
        "## Next gates\n\n"
        "1. **BL-1 Track N (Scratch):** write concrete `S_nu`, vary, show whether C1 or something else emerges.\n"
        "2. **BL-1/4 Track B (parallel):** Hassan–Rosen identification + healthy branch.\n"
        "3. **Jammer:** attack any smuggling of `S_cons` or T-in-action as derived.\n"
        "4. **AC:** ratify programme; no Core patch at Phase 0.\n"
    )
    OUT_MD.write_text(md, encoding="utf-8")
    OUT_JSON.write_text(
        json.dumps(
            {
                "kappa0": KAPPA0,
                "ran_utc": now,
                "candidates": [r.to_dict() for r in rows],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {OUT_MD}")
    print(f"Wrote {OUT_JSON}")
    print(f"κ₀ = {KAPPA0:.6f}; C1 r_bg = {rows[1].r_bg:.4f}; C2 r_bg = {rows[2].r_bg:.4f}")


if __name__ == "__main__":
    main()
