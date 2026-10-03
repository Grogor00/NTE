#!/usr/bin/env python3
"""Seed pc_scratch E8a-d pivot tasks into cursor_task_ledger.json."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")

NEW_TASKS = [
    {
        "id": "PC-E8a-S2-PIVOT",
        "state": "QUEUED",
        "priority": 40,
        "stream": "pc_scratch",
        "gate": "kphi",
        "title": "Package E8a: S2 pedagogical pivot sync (K(Phi), Root A, tells-excise)",
        "file": "Papers/Paper_S2_Pedagogical_Pivot_v1_0_20260530.md",
        "draft": "Working/Package_E8a_S2_Pivot_KPhi_RootA_TellsExcise_Replacement_Prose_Draft_PC_20260618.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_S2_Pivot_Sync_KPhi_RootA_TellsExcise_PackageE8a_20260618.md",
    },
    {
        "id": "PC-E8b-P4-PIVOT",
        "state": "QUEUED",
        "priority": 41,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Package E8b: P4 pivot CLFV sister-prediction cross-reference",
        "file": "Papers/Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_Pedagogical_Pivot_v1_0_20260530.md",
        "draft": "Working/Package_E8b_P4_Pivot_CLFV_Sister_Prediction_Replacement_Prose_Draft_PC_20260618.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_P4_Pivot_Sync_CLFV_PackageE8b_20260618.md",
    },
    {
        "id": "PC-E8c-OCTONION-PIVOT",
        "state": "QUEUED",
        "priority": 42,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Package E8c: Octonion pivot tells-excise + Root D preventive clarification",
        "file": "Papers/Paper_OctonionExtension_Pedagogical_Pivot_v1_0_20260530.md",
        "draft": "Working/Package_E8c_Octonion_Pivot_TellsExcise_RootD_Replacement_Prose_Draft_PC_20260618.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Octonion_Pivot_Sync_TellsExcise_RootD_PackageE8c_20260618.md",
    },
    {
        "id": "PC-E8d-HOPF-PIVOT",
        "state": "QUEUED",
        "priority": 43,
        "stream": "pc_scratch",
        "gate": "kappa",
        "title": "Package E8d: Hopf pivot Root A + a4-to-a2 correction",
        "file": "Papers/Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md",
        "draft": "Working/Package_E8d_Hopf_Pivot_RootA_a4_to_a2_Replacement_Prose_Draft_PC_20260618.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Hopf_Pivot_Sync_RootA_a4toa2_PackageE8d_20260618.md",
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
    print(f"Seeded {added} pc_scratch tasks (E8a-d)")


if __name__ == "__main__":
    main()
