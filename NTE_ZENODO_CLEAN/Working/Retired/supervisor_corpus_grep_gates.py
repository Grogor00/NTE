#!/usr/bin/env python3
"""Supervisor corpus consistency grep gates — delegates to cursor_grep_gates.py."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
GATES = ROOT / "Working" / "cursor_grep_gates.py"


def main() -> int:
    if not GATES.exists():
        print("cursor_grep_gates.py missing")
        return 2
    cmd = [sys.executable, str(GATES), "--gate", "mojibake", "--gate", "a4", "--gate", "eta",
           "--gate", "kphi", "--gate", "kappa", "--report"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    (ROOT / "Working" / "_supervisor_grep_report.txt").write_text(out, encoding="utf-8")
    print(out.encode("ascii", "replace").decode("ascii"))
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
