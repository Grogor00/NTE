#!/usr/bin/env python3
"""Batch-update ledger task states and fix section mojibake (UTF-8 safe)."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")

VERIFY = [
    "MOJIBAKE-GATE-FIX",
    "MOJIBAKE-REPAIR",
    "ETA-GATE-PRECISION",
    "C10-CORRECT",
]


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    for t in data["tasks"]:
        if "section" in t and isinstance(t["section"], str):
            t["section"] = re.sub(r"Â§", "§", t["section"])
        if t["id"] in VERIFY:
            t["state"] = "VERIFIED"
            t["verified_at"] = now
        if t["id"] == "CPN-T2" and "blocked_by" in t:
            del t["blocked_by"]
    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("verified:", ", ".join(VERIFY))
    print("CPN-T2 unblocked")


if __name__ == "__main__":
    main()
