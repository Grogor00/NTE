#!/usr/bin/env python3
"""Update cursor_task_ledger.json task states (UTF-8 safe)."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: update_ledger_task.py TASK_ID VERIFIED|QUEUED|CLAIMED")
        return 1
    task_id, state = sys.argv[1], sys.argv[2]
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    for t in data["tasks"]:
        if t["id"] == task_id:
            t["state"] = state
            if state == "VERIFIED":
                t["verified_at"] = datetime.now(timezone.utc).astimezone().isoformat()
            break
    else:
        print(f"task not found: {task_id}")
        return 1
    data["updated_at"] = datetime.now(timezone.utc).astimezone().isoformat()
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{task_id} -> {state}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
