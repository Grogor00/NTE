#!/usr/bin/env python3
"""Corpus astral-plane / BMP mojibake repair (silent font-restore per AC 2026-06-18)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")

# Literal mojibake sequences -> correct glyphs
TEXT_FIXES = [
    (re.compile(r"J₃\(ð[\u009d\u2020\u0086\u008a\u00a6\u2022\u0080-\u00bf]{2,6}\)"), "J₃(𝕆)"),
    (re.compile(r"J_3\(ð[\u009d\u2020\u0086\u008a\u00a6\u2022\u0080-\u00bf]{2,6}\)"), "J_3(𝕆)"),
    (re.compile(r"ð\u009d\u0095\u0086"), "𝕆"),
    (re.compile(r"ð\u009d\u0092¦"), "𝒦"),
    (re.compile(r"ð\u009d\u0092\u009c"), "𝒜"),
    (re.compile(r"Ãƒâ€šÃ‚Â§"), "§"),
    (re.compile(r"â€šÃ‚Â§"), "§"),
    (re.compile(r"\u00e2\u20ac\u201d"), "\u2014"),
    (re.compile(r"\u00e2\u20ac\u201c"), "\u2013"),
]

SCAN_ROOTS = [
    ROOT / "Papers",
    ROOT / "Working" / "AC_Readable_Splits",
    BOOK,
]


def repair_text(text: str) -> tuple[str, int]:
    n = 0
    for pat, repl in TEXT_FIXES:
        text, c = pat.subn(repl, text)
        n += c
    return text, n


def scan_paths() -> list[Path]:
    out: list[Path] = []
    for base in SCAN_ROOTS:
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            if "depreciated" in str(p) or ".mojibake_bak" in p.name:
                continue
            out.append(p)
    return sorted(out)


def main() -> int:
    report: list[str] = ["ASTRAL MOJIBAKE REPAIR", ""]
    total = 0
    changed_files: list[str] = []
    for path in scan_paths():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        new, n = repair_text(text)
        if n:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed_files.append(f"{path.relative_to(ROOT.parent)}: {n} fix(es)")
            total += n
    report.append(f"files_changed={len(changed_files)} total_fixes={total}")
    report.extend(changed_files or ["(no text-level fixes needed)"])
    out = ROOT / "Working" / "_mojibake_repair_report.txt"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
