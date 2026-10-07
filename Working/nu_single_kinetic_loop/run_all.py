#!/usr/bin/env python3
"""Run single-kinetic ontology-cost probes; write results for clones."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from kinetic_cost_probes import CLAIMS, catalog, summary

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md(data: dict) -> str:
    lines = [
        "# Drop shared-ν second kinetic — ontology cost probe",
        "",
        f"**Generated:** {utc_now()}",
        f"**Mechanical fork hint:** `{data['suggested_fork_hint']}`",
        f"**Keep κ₀+bilateral+Z₂ under drop:** {data['keep_kappa0_bilateral_z2_ids']}",
        f"**Fatal readings:** {data['fatal_ids'] or '(none)'}",
        "",
        "## Deposit claims",
        "",
    ]
    for k, v in CLAIMS.items():
        lines.append(f"- `{k}`: {v}")
    lines += [
        "",
        "## Readings",
        "",
        "| ID | Name | drop2nd | cost | ghost | →K |",
        "|---|---|---|---|---|---|",
    ]
    for r in catalog():
        lines.append(
            f"| {r.id} | {r.name[:42]} | {r.drops_second_kinetic} | "
            f"{r.ontology_cost} | {r.ghost_outlook} | {r.suggested_k} |"
        )
    lines += ["", "## Claim fate detail", ""]
    for r in catalog():
        lines.append(f"### {r.id} — {r.name}")
        lines.append("")
        lines.append(f"{r.notes}")
        lines.append("")
        for c, fate in r.claim_fate.items():
            lines.append(f"- `{c}`: **{fate}**")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = summary()
    bundle = {"generated_utc": utc_now(), "programme": "nu_single_kinetic_cost", **data}
    (OUT / "probe_results.json").write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    (OUT / "KINETIC_COST_RESULTS.md").write_text(md(data), encoding="utf-8")
    print(json.dumps({"suggested_fork_hint": data["suggested_fork_hint"]}, indent=2))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
