#!/usr/bin/env python3
"""Mark F1-SELF-CORRECT VERIFIED after AC sight execution."""
import json
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")


def main() -> None:
    now = datetime.now(timezone.utc).astimezone().isoformat()
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    for t in data["tasks"]:
        if t["id"] == "F1-SELF-CORRECT":
            t["state"] = "VERIFIED"
            t["verified_at"] = now
            t["file"] = "Papers/Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md"
            t["drive_id"] = "1wVk3pKmnmvotPgM3h9oeh3e1zRxdHWvt"
            t["source_handoff"] = (
                "Handoffs/AC_SIGHT_F1_SELF_CORRECT_Exact_OLD_Confirmed_Title_Only_Fix_"
                "Body_Already_Honest_F1_ID_Recorded_Index_Gap_Closed_20260620.md"
            )
            t["note"] = "Title-only fix per AC sight; §4/§5 untouched; priority cites added"
    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("F1-SELF-CORRECT -> VERIFIED")


if __name__ == "__main__":
    main()
