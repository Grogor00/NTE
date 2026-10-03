#!/usr/bin/env python3
"""Apply Tier 2c v10.14 patch (§17.5.9 worksheet pointers)."""
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
INST = Path(
    r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\Master_v10_13_Tier2c_Patch_Instructions_LCDM_Worksheets_17_5_9_20260523.md"
)

PARTS = [
    ("NTE_v10_13_Part1_Foundations.md", "NTE_v10_14_Part1_Foundations.md", []),
    ("NTE_v10_13_Part2_Structure.md", "NTE_v10_14_Part2_Structure.md", []),
    ("NTE_v10_13_Part3_Accounting.md", "NTE_v10_14_Part3_Accounting.md", ["T2c-1", "T2c-2", "T2c-3"]),
]


def parse_patches(md: str) -> dict[str, tuple[str, str]]:
    patches = {}
    parts = re.split(r"## Patch (T2c-\S+):", md)
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
    # Bump Part 1/2 headers to v10.14
    for part, label in [
        ("NTE_v10_14_Part1_Foundations.md", "Part 1"),
        ("NTE_v10_14_Part2_Structure.md", "Part 2"),
    ]:
        p = BASE / part
        t = p.read_text(encoding="utf-8")
        t = t.replace("NTE v10.13", "NTE v10.14", 1).replace(
            "Master canonical at v10.13", "Master canonical at v10.14"
        )
        p.write_text(t, encoding="utf-8", newline="\n")
        print(f"{part}: header bump")
    print("Done.")


if __name__ == "__main__":
    main()
