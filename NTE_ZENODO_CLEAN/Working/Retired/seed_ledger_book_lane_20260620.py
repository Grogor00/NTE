#!/usr/bin/env python3
"""Seed 2026-06-18 book-side / Popular PC handoffs into cursor_task_ledger.json."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")

NEW_TASKS = [
    {
        "id": "BOOK-PRELUDE-GALACTIC",
        "state": "QUEUED",
        "priority": 50,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Prelude factual fix: galactic → extragalactic distance (PR-FX-1)",
        "file": "Book/Prelude_The_Forty_Million_Year_Instant_v5.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Prelude_Factual_Fix_Galactic_Distance_20260616.md",
    },
    {
        "id": "BOOK-PRELUDE-OPTIONB",
        "state": "QUEUED",
        "priority": 51,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Prelude Option B: delete corpus-meta-data scorecard paragraph (PR-DEL-1)",
        "file": "Book/Prelude_The_Forty_Million_Year_Instant_v5.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Prelude_Paragraph_Deletion_OptionB_20260618.md",
        "blocks": ["BOOK-PRELUDE-GALACTIC"],
    },
    {
        "id": "BOOK-TELLS-EXCISE",
        "state": "QUEUED",
        "priority": 52,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Tells-Excise Sweep: 14 patches Ch 9/10/12/15 + Appendix A (TE-1..TE-14)",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Tells_Excise_Sweep_Book_Corpus_Meta_Data_Excision_20260618.md",
        "blocks": ["BOOK-PRELUDE-OPTIONB"],
    },
    {
        "id": "BOOK-READER-SYNC",
        "state": "QUEUED",
        "priority": 53,
        "stream": "pc_scratch",
        "gate": None,
        "title": "Reader Edition sync: book Appendix A ← corpus Reader Edition",
        "file": "Book/Appendix_A_NTE_Popular_Paper_Reader_Edition.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Reader_Edition_Sync_Book_To_Corpus_20260618.md",
        "blocks": ["BOOK-TELLS-EXCISE"],
    },
    {
        "id": "BOOK-E6-POPULAR-L53",
        "state": "QUEUED",
        "priority": 54,
        "stream": "pc_scratch",
        "gate": None,
        "title": "E6 hotfix: Popular Full §opening L53 constraint marker + PDF rebuild",
        "file": "Papers/Paper_Popular_v10_8_Full_Edition.md",
        "source_handoff": "Handoffs/Handoff_PC_to_Cursor_PC_Popular_Full_L53_Marker_E6_Hotfix_20260618.md",
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
    print(f"Seeded {added} book-lane task(s). Ledger now has {len(data['tasks'])} tasks.")


if __name__ == "__main__":
    main()
