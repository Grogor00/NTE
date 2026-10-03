#!/usr/bin/env python3
"""Update ledger: MOJIBAKE-REPAIR VERIFIED; add HOUSEKEEPING-EXECUTE VERIFIED."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    for t in data["tasks"]:
        if t["id"] == "MOJIBAKE-REPAIR":
            t["state"] = "VERIFIED"
            t["verified_at"] = now
            t["note"] = "Greg Part3 pixel sight PASS 2026-06-19; S2 block lifted AC 2026-06-18"
    ids = {t["id"] for t in data["tasks"]}
    if "HOUSEKEEPING-EXECUTE" not in ids:
        data["tasks"].append(
            {
                "id": "HOUSEKEEPING-EXECUTE",
                "state": "VERIFIED",
                "priority": 51,
                "stream": "main",
                "gate": "housekeeping",
                "title": "Housekeeping Phase 2 execute (Greg approved 2026-06-19)",
                "verified_at": now,
            }
        )
    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("MOJIBAKE-REPAIR -> VERIFIED")
    print("HOUSEKEEPING-EXECUTE -> VERIFIED")


if __name__ == "__main__":
    main()
