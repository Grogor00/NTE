#!/usr/bin/env python3
"""Seed AC hold-tranche sprint tasks into cursor_task_ledger.json."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")
SOURCE = (
    "Handoffs/Handoff_AC_to_Cursor_LedgerTargeted_Carrier_Correction_F1_Sweep_"
    "P5_Kappa0_P4_Reframes_HOLD_Tranche_Sprint_SightFirst_20260619.md"
)

NEW_TASKS = [
    {
        "id": "F1-SELF-CORRECT",
        "state": "QUEUED",
        "priority": 20,
        "stream": "main",
        "gate": "f1uniqueness",
        "title": "F1 paper title+abstract: restricted S^p×S^q uniqueness (SIGHT-FIRST)",
        "source_handoff": SOURCE,
    },
    {
        "id": "F1-CARRIER-S2",
        "state": "QUEUED",
        "priority": 21,
        "stream": "main",
        "gate": "f1uniqueness",
        "title": "S2 F1 false-claim sweep + §13.2 five-note (SIGHT-FIRST)",
        "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md",
        "source_handoff": SOURCE,
    },
    {
        "id": "F1-CARRIER-P5",
        "state": "QUEUED",
        "priority": 22,
        "stream": "main",
        "gate": "f1uniqueness",
        "title": "P5 §1/§8 F1 framing + companion ref drop (SIGHT-FIRST)",
        "source_handoff": SOURCE,
    },
    {
        "id": "P5-REFRAME",
        "state": "QUEUED",
        "priority": 23,
        "stream": "main",
        "gate": "zeroparam",
        "title": "P5 reframe: mass-ratio headline, strike zero-parameter (SIGHT-FIRST)",
        "source_handoff": SOURCE,
    },
    {
        "id": "KAPPA0-SIMPLIFY",
        "state": "BLOCKED_AC",
        "priority": 24,
        "stream": "main",
        "gate": "kappa",
        "title": "κ₀ simplify-or-pull (Greg decision gate)",
        "source_handoff": SOURCE,
        "blocked_reason": "Greg pull-vs-reframe ruling required",
    },
    {
        "id": "P4-REFRAME",
        "state": "QUEUED",
        "priority": 25,
        "stream": "main",
        "gate": "novelty",
        "title": "P4 reframe: cite priority + falsifiable π/4 (SIGHT-FIRST)",
        "source_handoff": SOURCE,
    },
]


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    ids = {t["id"] for t in data["tasks"]}
    added = 0
    for task in NEW_TASKS:
        if task["id"] not in ids:
            data["tasks"].append(task)
            added += 1
    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Seeded {added} hold-tranche tasks")


if __name__ == "__main__":
    main()
