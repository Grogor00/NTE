#!/usr/bin/env python3
"""Apply Tier 0 v10.10 patches from instruction file."""
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
INST = Path(
    r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\Master_v10_9_to_v10_10_Patch_Instructions_Tier0_Integration_20260523.md"
)

PARTS = [
    ("NTE_v10_9_Part1_Foundations.md", "NTE_v10_10_Part1_Foundations.md", ["T0-3b"]),
    ("NTE_v10_9_Part2_Structure.md", "NTE_v10_10_Part2_Structure.md", ["T0-3c"]),
    (
        "NTE_v10_9_Part3_Accounting.md",
        "NTE_v10_10_Part3_Accounting.md",
        ["T0-1a", "T0-1b", "T0-1c", "T0-1d", "T0-2a", "T0-2b", "T0-2c", "T0-3"],
    ),
]


def parse_patches(md: str) -> dict[str, tuple[str, str]]:
    patches = {}
    blocks = re.split(r"## Patch (T0-\S+):", md)
    for i in range(1, len(blocks), 2):
        pid = blocks[i].strip().split()[0] if blocks[i].strip() else ""
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
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
                print(f"MISSING PATCH ID {pid}")
                continue
            old, new = all_patches[pid]
            if old not in text:
                print(f"{out_name}: MISMATCH {pid}")
            else:
                text = text.replace(old, new, 1)
                print(f"{out_name}: OK {pid}")
        (BASE / out_name).write_text(text, encoding="utf-8", newline="\n")
    print("Done.")


if __name__ == "__main__":
    main()
