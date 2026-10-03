#!/usr/bin/env python3
"""Scan prepared scratch markdown for author-only leakage before PDF export."""
from __future__ import annotations

import re
import sys
from pathlib import Path

BANNED = (
    "NTE Popular Paper",
    "Edition discipline",
    "do not treat Full Edition",
    "interchangeable filenames",
    "Publication programme:",
    "**Version:**",
    "**Stream:**",
    "**Ratification lineage**",
    "Appendix_A_NTE_Popular",
    "Paper_Popular_v10_8_Full_Edition.md",
    "Working/",
    "Handoffs/",
    "Jammer_",
    "Greg-ratified",
    "ship note (2026",
)


def scan_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    head = text[:4000]
    issues = []
    for needle in BANNED:
        if needle in head:
            issues.append(f"{path.name}: contains '{needle}' in head")
    if re.search(r"^>\s*\*\*NTE", head, re.M):
        issues.append(f"{path.name}: edition blockquote remains")
    return issues


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "paper-build" / "scratch-src"
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    all_issues: list[str] = []
    for path in sorted(root.glob("*.md")):
        all_issues.extend(scan_file(path))
    if all_issues:
        print("\n".join(all_issues))
        return 1
    print(f"OK: {len(list(root.glob('*.md')))} files clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
