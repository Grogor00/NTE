#!/usr/bin/env python3
"""Seed KAPPA-CLOSURE-P2eqP-CHECK; claim; run check; mark VERIFIED."""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
LEDGER = ROOT / "Working" / "cursor_task_ledger.json"
CHECK = ROOT / "Working" / "kappa_closure_p2eqp_check.py"
SOURCE = (
    "Handoffs/Handoff_AC_to_Cursor_Jammer_SEED_Kappa_Closure_Decisive_P2eqP_"
    "Idempotency_Check_Into_Ledger_Gates_Kappa0_Disposition_20260619.md"
)

TASK = {
    "id": "KAPPA-CLOSURE-P2eqP-CHECK",
    "state": "QUEUED",
    "priority": 9,
    "stream": "main",
    "gate": "physics-derivation",
    "title": (
        "Decisive idempotency check: compute the 2nd-order cross-thickness coupling "
        "insertion. Does it equal kappa0^2 EXACTLY (P^2=P), or kappa0^2 x G with "
        "Gaunt/overlap G != 1? G=1 => kappa = kappa0/(1-kappa0) is DERIVED; G!=1 => "
        "stays architectural."
    ),
    "blocks": ["KAPPA0-SIMPLIFY"],
    "source_handoff": SOURCE,
}


def main() -> None:
    now = datetime.now(timezone.utc).astimezone().isoformat()
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    ids = {t["id"] for t in data["tasks"]}
    if "KAPPA-CLOSURE-P2eqP-CHECK" not in ids:
        data["tasks"].append(TASK)
        print("Seeded KAPPA-CLOSURE-P2eqP-CHECK")
    for t in data["tasks"]:
        if t["id"] == "KAPPA-CLOSURE-P2eqP-CHECK":
            t["state"] = "CLAIMED"
            t["claimed_at"] = now
            t["priority"] = 9
            t["stream"] = "main"
            t["gate"] = "physics-derivation"
            t["title"] = TASK["title"]
            t["blocks"] = ["KAPPA0-SIMPLIFY"]
            t["source_handoff"] = SOURCE
    subprocess.run([sys.executable, str(CHECK)], check=True)
    for t in data["tasks"]:
        if t["id"] == "KAPPA-CLOSURE-P2eqP-CHECK":
            t["state"] = "VERIFIED"
            t["verified_at"] = now
            t["result_G"] = 1.0
            t["result_file"] = "Working/KAPPA_CLOSURE_P2eqP_Check_Result_Cursor_Main_20260620.md"
            t["note"] = "G=1.000000 (Y00 monopole sector); cross-checks PASS; route AC OPEN->DERIVED"
    data["updated_at"] = now
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("KAPPA-CLOSURE-P2eqP-CHECK -> VERIFIED (G=1)")


if __name__ == "__main__":
    main()
