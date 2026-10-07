#!/usr/bin/env python3
"""Run CPN + gravity probes; write JSON + markdown tables for clone lanes."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from cpn_map_probes import REQUIREMENTS, catalog as cpn_catalog, summary as cpn_summary
from gravity_completion_probes import CRITERIA, catalog as grav_catalog, summary as grav_summary

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cpn_md(data: dict) -> str:
    lines = [
        "# CPN map probe results",
        "",
        f"**Generated:** {utc_now()}",
        "",
        f"**Fork hint (mechanical):** `{data['suggested_fork_hint']}`",
        f"**M0 fails deposit-work:** {data['m0_fails_work']}",
        f"**Full-work IDs:** {data['full_work_ids'] or '(none)'}",
        f"**Deposited ∩ full-work:** {data['deposited_full_work_ids'] or '(none)'}",
        f"**Partial survivors:** {data['partial_survivor_ids']}",
        "",
        "## Requirement key",
        "",
    ]
    for k, v in REQUIREMENTS.items():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Scores", "", "| ID | Name | full | dep | baryon | ¬gauge | SU2R | MA=MB | acts N | free |", "|---|---|---|---|---|---|---|---|---|---|"]
    for m in cpn_catalog():
        s = m.scores
        lines.append(
            f"| {m.id} | {m.name[:40]} | {m.full_work} | {m.deposited} | "
            f"{s['R_baryon_sort']} | {s['R_not_gauge']} | {s['R_su2r']} | "
            f"{s['R_MA_MB']} | {s['R_acts_on_N']} | {s['R_free_symmetry']} |"
        )
    lines += ["", "## Notes", ""]
    for m in cpn_catalog():
        lines.append(f"- **{m.id}:** {m.notes}")
    lines.append("")
    return "\n".join(lines)


def grav_md(data: dict) -> str:
    lines = [
        "# Gravity completion probe results",
        "",
        f"**Generated:** {utc_now()}",
        "",
        f"**Fork hint (mechanical):** `{data['suggested_fork_hint']}`",
        f"**Healthy ∩ full ontology:** {data['healthy_full_ontology_ids'] or '(none)'}",
        f"**Healthy two-metric:** {data['healthy_two_metric_ids']}",
        f"**NTE (N0) ghost_status:** {data['nte_ghost_status']}",
        f"**1408 blocks kinetic shared ν:** {data['shared_nu_kinetic_blocked_by_1408']}",
        "",
        "## Criteria key",
        "",
    ]
    for k, v in CRITERIA.items():
        lines.append(f"- `{k}`: {v}")
    lines += [
        "",
        "## Scores",
        "",
        "| ID | Name | ghost | ontology | 2-met | 1-man | ν both | kinOK | constr | NTE |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for c in grav_catalog():
        s = c.scores
        lines.append(
            f"| {c.id} | {c.name[:36]} | {c.ghost_status} | {c.ontology_fit} | "
            f"{s['C_two_orientation_metrics']} | {s['C_one_manifold']} | "
            f"{s['C_shared_nu_both_EOM']} | {s['C_kinetic_double_ok']} | "
            f"{s['C_constraint_complete']} | {s['C_deposited_nte']} |"
        )
    lines += ["", "## Notes", ""]
    for c in grav_catalog():
        lines.append(f"- **{c.id}:** {c.notes}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    cpn = cpn_summary()
    grav = grav_summary()
    bundle = {
        "generated_utc": utc_now(),
        "programme": "CPN relation + gravity completion",
        "cpn": cpn,
        "gravity": grav,
        "mechanical_fork_hints": {
            "P": cpn["suggested_fork_hint"],
            "G": grav["suggested_fork_hint"],
        },
    }
    (OUT / "probe_results.json").write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    (OUT / "CPN_MAP_RESULTS.md").write_text(cpn_md(cpn), encoding="utf-8")
    (OUT / "GRAVITY_COMPLETION_RESULTS.md").write_text(grav_md(grav), encoding="utf-8")
    print(json.dumps(bundle["mechanical_fork_hints"], indent=2))
    print(f"Wrote {OUT / 'probe_results.json'}")


if __name__ == "__main__":
    main()
