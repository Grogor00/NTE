#!/usr/bin/env python3
"""Write mojibake pre/post repair sweep report for MOJIBAKE-GATE-FIX verification."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
GREP = ROOT / "Working" / "cursor_grep_gates.py"
OUT = ROOT / "Working" / "_mojibake_sweep_report.txt"

CARRIERS = [
    "Papers/Paper_S2_v1_0_Consolidation_20260525.md",
    "Papers/NTE_v10_17_Part3_Accounting.md",
    "Working/AC_Readable_Splits/NTE_v10_17_Part3_Accounting__C_S22_App.md",
    "Papers/Paper_Popular_v10_8_Full_Edition.md",
]


def run_gate(extra: list[str]) -> str:
    r = subprocess.run(
        [sys.executable, str(GREP), "--gate", "mojibake", "--report", *extra],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return r.stdout + r.stderr


def main() -> None:
    lines = ["MOJIBAKE GATE SWEEP (Cursor Main 2026-06-18)", ""]
    lines.append("=== corpus-wide ===")
    lines.append(run_gate([]))
    for rel in CARRIERS:
        p = ROOT / rel
        if p.exists():
            lines.append(f"=== {rel} ===")
            lines.append(run_gate(["--file", str(p)]))
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
