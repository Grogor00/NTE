#!/usr/bin/env python3
"""Apply Tier 2e v10.16 patch (Paper S2 S2-E AC integration)."""
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
INST = Path(
    r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\Master_v10_15_Tier2e_Patch_Instructions_PaperS2_S2E_20260523.md"
)

PARTS = [
    ("NTE_v10_15_Part1_Foundations.md", "NTE_v10_16_Part1_Foundations.md", ["T2e-6", "T2e-9"]),
    ("NTE_v10_15_Part2_Structure.md", "NTE_v10_16_Part2_Structure.md", []),
    (
        "NTE_v10_15_Part3_Accounting.md",
        "NTE_v10_16_Part3_Accounting.md",
        ["T2e-1", "T2e-2", "T2e-3", "T2e-4", "T2e-5", "T2e-8"],
    ),
]
PAPER_S1 = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_S1_v0_4.md")


def parse_patches(md: str) -> dict[str, tuple[str, str]]:
    patches = {}
    parts = re.split(r"## Patch (T2e-\S+):", md)
    for i in range(1, len(parts), 2):
        pid = re.match(r"(\S+)", parts[i].strip())
        if not pid:
            continue
        pid = pid.group(1)
        body = parts[i + 1] if i + 1 < len(parts) else ""
        finds = re.findall(r"\*\*Find:\*\*\s*\n\n```\n(.*?)```", body, re.DOTALL)
        repls = re.findall(r"\*\*Replace with:\*\*\s*\n\n```\n(.*?)```", body, re.DOTALL)
        if finds and repls:
            for j, (old, new) in enumerate(zip(finds, repls)):
                key = pid if j == 0 else f"{pid}-{j+1}"
                patches[key] = (old.rstrip("\n"), new.rstrip("\n"))
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
    p2 = BASE / "NTE_v10_16_Part2_Structure.md"
    t = p2.read_text(encoding="utf-8")
    t = t.replace("NTE v10.15", "NTE v10.16", 1).replace(
        "Master canonical at v10.15", "Master canonical at v10.16"
    )
    p2.write_text(t, encoding="utf-8", newline="\n")
    print("NTE_v10_16_Part2_Structure.md: header bump")
    if "T2e-7" in all_patches:
        old, new = all_patches["T2e-7"]
        s1 = PAPER_S1.read_text(encoding="utf-8")
        if old in s1:
            PAPER_S1.write_text(s1.replace(old, new, 1), encoding="utf-8", newline="\n")
            print("Paper_S1_v0_4.md: OK T2e-7")
        else:
            print("Paper_S1_v0_4.md: MISMATCH T2e-7")
    print("Done v10.16")


if __name__ == "__main__":
    main()
