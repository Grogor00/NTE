#!/usr/bin/env python3
"""Apply Tier 2d v10.15 patch (Paper S2 S2-C arc master tick-down)."""
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
INST = Path(
    r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\Master_v10_14_Tier2d_Patch_Instructions_PaperS2_S2C_20260523.md"
)

PARTS = [
    ("NTE_v10_14_Part1_Foundations.md", "NTE_v10_15_Part1_Foundations.md", []),
    ("NTE_v10_14_Part2_Structure.md", "NTE_v10_15_Part2_Structure.md", []),
    (
        "NTE_v10_14_Part3_Accounting.md",
        "NTE_v10_15_Part3_Accounting.md",
        ["T2d-1", "T2d-2", "T2d-3", "T2d-4", "T2d-5", "T2d-6"],
    ),
]


def parse_patches(md: str) -> dict[str, tuple[str, str]]:
    patches = {}
    parts = re.split(r"## Patch (T2d-\S+):", md)
    for i in range(1, len(parts), 2):
        pid = re.match(r"(\S+)", parts[i].strip())
        if not pid:
            continue
        pid = pid.group(1)
        body = parts[i + 1] if i + 1 < len(parts) else ""
        finds = re.findall(r"\*\*Find:\*\*\s*\n\n```\n(.*?)```", body, re.DOTALL)
        repls = re.findall(r"\*\*Replace with:\*\*\s*\n\n```\n(.*?)```", body, re.DOTALL)
        if finds and repls:
            patches[pid] = (finds[0].rstrip("\n"), repls[0].rstrip("\n"))
    return patches


def main():
    all_patches = parse_patches(INST.read_text(encoding="utf-8"))
    for src_name, out_name, ids in PARTS:
        text = (BASE / src_name).read_text(encoding="utf-8")
        for pid in ids:
            if pid not in all_patches:
                print(f"MISSING {pid}")
                continue
            old, new = all_patches[pid]
            if old not in text:
                print(f"{out_name}: MISMATCH {pid}")
            else:
                text = text.replace(old, new, 1)
                print(f"{out_name}: OK {pid}")
        (BASE / out_name).write_text(text, encoding="utf-8", newline="\n")
    for part in ("NTE_v10_15_Part1_Foundations.md", "NTE_v10_15_Part2_Structure.md"):
        p = BASE / part
        t = p.read_text(encoding="utf-8")
        t = t.replace("NTE v10.14", "NTE v10.15", 1).replace(
            "Master canonical at v10.14", "Master canonical at v10.15"
        )
        p.write_text(t, encoding="utf-8", newline="\n")
        print(f"{part}: header bump")
    print("Done v10.15")


if __name__ == "__main__":
    main()
