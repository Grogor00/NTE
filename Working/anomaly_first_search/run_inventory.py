#!/usr/bin/env python3
"""Scaffold inventory slots for anomaly-first search (tags filled by clones)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"

SLOTS = [
    {"id": "E0", "tier": 1, "name": "Elliptic de Sitter (antipodal dS/Z2)", "fork_field": "E1-E4"},
    {"id": "N1", "tier": 2, "name": "Reactor antineutrino anomaly"},
    {"id": "N2", "tier": 2, "name": "Gallium anomaly (SAGE/GALLEX/BEST)"},
    {"id": "N3", "tier": 2, "name": "LSND / MiniBooNE appearance excess"},
    {"id": "N4", "tier": 2, "name": "SBL vs LBL appearance tension"},
    {"id": "G1", "tier": 2, "name": "NANOGrav / PTA stochastic background"},
    {"id": "C1", "tier": 2, "name": "CMB low-ℓ alignments"},
    {"id": "C2", "tier": 2, "name": "CMB hemispherical power asymmetry"},
    {"id": "C3", "tier": 2, "name": "Parity-odd / mirror-odd CMB claims"},
    {"id": "L1", "tier": 3, "name": "Barbour–Koslowski–Mercati shape dynamics"},
    {"id": "L2", "tier": 3, "name": "ABL two-state / two-vector formalism"},
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "guard": "anomaly-first; no predict-then-hunt; no 4th light sterile CONTACT",
        "slots": [
            {**s, "tag": "PENDING", "notes": "Clone fills after sourced read"} for s in SLOTS
        ],
    }
    (OUT / "inventory_template.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    md = [
        "# Anomaly-first inventory template",
        "",
        "**Guard:** independently strange → then NTE contact. No sterile CONTACT.",
        "",
        "| ID | Tier | Name | Tag |",
        "|---|---|---|---|",
    ]
    for s in SLOTS:
        md.append(f"| {s['id']} | {s['tier']} | {s['name']} | PENDING |")
    (OUT / "INVENTORY_TEMPLATE.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"n_slots": len(SLOTS)}, indent=2))


if __name__ == "__main__":
    main()
