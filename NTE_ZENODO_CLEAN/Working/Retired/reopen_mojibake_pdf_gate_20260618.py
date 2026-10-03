#!/usr/bin/env python3
"""Re-open MOJIBAKE-REPAIR; add PDF-SIGHT-CALIBRATION; fix ledger UTF-8."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\cursor_task_ledger.json")


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    tasks = {t["id"]: t for t in data["tasks"]}

    # Fix mojibake in section fields
    for t in data["tasks"]:
        if "section" in t and isinstance(t["section"], str):
            t["section"] = re.sub(r"Â§|Ã‚Â§|Ãƒâ€šÃ‚Â§", "§", t["section"])

    if "MOJIBAKE-REPAIR" in tasks:
        t = tasks["MOJIBAKE-REPAIR"]
        t["state"] = "QUEUED"
        t["gate"] = "pdf-mojibake"
        t["title"] = (
            "PDF-BUILD-FIX + dual-channel artifact gate (md clean; fix render pipeline; "
            "pdf-mojibake PASS + AC PNG sight before publish-block lift)"
        )
        t.pop("verified_at", None)
        for k in ("blocked_by",):
            t.pop(k, None)

    if "PDF-SIGHT-CALIBRATION" not in tasks:
        data["tasks"].append(
            {
                "id": "PDF-SIGHT-CALIBRATION",
                "state": "VERIFIED",
                "priority": 4,
                "stream": "main",
                "gate": "pdf-mojibake",
                "title": "Dual-channel PDF sight calibration reference + pdf_artifact_gate.py",
                "file": "Workflow/NTE_PDF_Artifact_Sight_Calibration_v0_1_20260618.md",
                "verified_at": now,
            }
        )
    else:
        tasks["PDF-SIGHT-CALIBRATION"]["state"] = "VERIFIED"
        tasks["PDF-SIGHT-CALIBRATION"]["verified_at"] = now

    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("MOJIBAKE-REPAIR -> QUEUED (pdf-mojibake gate)")
    print("PDF-SIGHT-CALIBRATION -> VERIFIED")


if __name__ == "__main__":
    main()
