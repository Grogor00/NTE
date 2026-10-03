#!/usr/bin/env python3
"""Seed ac_jammer physics tasks; redirect idle-lane work."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")

NEW_TASKS = [
    {
        "id": "JAMMER-FARNWORTH-S0",
        "state": "QUEUED",
        "priority": 10,
        "stream": "ac_jammer",
        "gate": "physics-derivation",
        "title": "Farnsworth Stage 0: read 2506.21496 sec 4-5; fixed vs free Yukawa? (gates Stages 1-5)",
        "local_pdf": "SeedPapers/2506.21496v1.pdf",
        "bf_pdf": "SeedPapers/NCG/Non-Associative Geometry and the Spectral Action Principle.pdf",
        "source_handoff": "Handoffs/Handoff_Scratch_to_Cursor_AC_BUILD_SPEC_Farnsworth_Triple_nu2_Yukawa_HopfS3_Octonion_Octonion_Staged_DecisiveTests_20260619.md",
    },
    {
        "id": "JAMMER-KAPPA-G1-ADVERSARIAL",
        "state": "QUEUED",
        "priority": 11,
        "stream": "ac_jammer",
        "gate": "physics-derivation",
        "title": "Adversarial Jammer review: kappa-closure G=1 idempotency memo (Theta sector caveat)",
        "result_file": "Working/KAPPA_CLOSURE_P2eqP_Check_Result_Cursor_Main_20260620.md",
        "source_handoff": "Handoffs/Handoff_Cursor_Main_to_AC_Kappa_Closure_P2eqP_Check_VERIFIED_G_Equals_1_20260620.md",
        "blocks": ["KAPPA0-SIMPLIFY"],
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
    print(f"Seeded {added} ac_jammer tasks")


if __name__ == "__main__":
    main()
