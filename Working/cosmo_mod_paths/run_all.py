#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from path_catalog import HARD_LOCKS, catalog, summary

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md(data: dict) -> str:
    lines = [
        "# Cosmology mod-path catalogue",
        "",
        f"**Generated:** {utc_now()}",
        f"**Chase set:** {data['recommended_chase_set']}",
        f"**Live:** {data['live_ids']}",
        f"**Costly:** {data['costly_ids']}",
        f"**Kill-likely:** {data['kill_likely_ids']}",
        f"**Presentation:** {data['presentation_ids']}",
        "",
        f"Hard locks: {', '.join(HARD_LOCKS)}",
        "",
        "| ID | Name | locksOK | hint | ghost | particle risk |",
        "|---|---|---|---|---|---|",
    ]
    for p in catalog():
        lines.append(
            f"| {p.id} | {p.name[:48]} | {p.keeps_hard_locks} | {p.status_hint} | "
            f"{p.ghost_outlook} | {p.particle_risk} |"
        )
    lines += ["", "## Detail", ""]
    for p in catalog():
        lines.append(f"### {p.id} — {p.name}")
        lines.append("")
        lines.append(f"- **Axiom changes:** {'; '.join(p.axiom_changes)}")
        lines.append(f"- **Soft-lock cost:** {p.soft_lock_cost}")
        lines.append(f"- **Cosmology targets:** {', '.join(p.cosmology_targets)}")
        lines.append(f"- **Blockers addressed:** {', '.join(p.prior_blockers_addressed)}")
        lines.append(f"- **Notes:** {p.notes}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = summary()
    (OUT / "probe_results.json").write_text(
        json.dumps({"generated_utc": utc_now(), **data}, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "PATH_CATALOG_RESULTS.md").write_text(md(data), encoding="utf-8")
    # copy lock into results for clone convenience
    lock = ROOT / "PARTICLE_LOCK.md"
    if lock.exists():
        (OUT / "PARTICLE_LOCK.md").write_text(lock.read_text(encoding="utf-8"), encoding="utf-8")
    print(json.dumps({"chase": data["recommended_chase_set"], "live": data["live_ids"]}, indent=2))


if __name__ == "__main__":
    main()
