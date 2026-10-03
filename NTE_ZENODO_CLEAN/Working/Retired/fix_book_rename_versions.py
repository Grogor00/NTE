#!/usr/bin/env python3
"""Fix version tokens in renamed Book files."""
import re
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")

# old_name -> correct version suffix (from Greg's canonical versions)
VERSION_FIX = {
    "Chapter_1_The_Photons_Journey_v7.md": "v7_3",
    "Chapter_4_Time_as_Expansion_v7.md": "v7_2",
    "Chapter_5_The_Eighth_Colour_v6.md": "v6_1",
    "Chapter_6_Why_Quantum_Mechanics_is_Geometry_v5.md": "v5_3",
    "Chapter_7_The_Gauge_Birth_v3.md": "v3_3",
    "Chapter_11_What_the_Universe_Sounds_Like_v3.md": "v3_1",
    "Chapter_12_The_Chord_v3.md": "v3_1",
    "Chapter_16_The_Working_Bet_v1 (1).md": "v1",
}

CH13_REORDER = {
    "Chapter_13_v3_The_Strange_Silence_of_the_Cosmological_Constant.md": (
        "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v3.md"
    ),
    "Chapter_13_v4_The_Strange_Silence_of_the_Cosmological_Constant.md": (
        "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v4.md"
    ),
}


def swap_version(path: Path, new_ver: str) -> Path:
    stem = path.stem
    # replace trailing _v...
    new_stem = re.sub(r"_v[\d_]+(?:\s*\(\d+\))?$", f"_{new_ver}", stem)
    if new_stem == stem:
        new_stem = stem + f"_{new_ver}"
    return path.parent / f"{new_stem}.md"


def main():
    for old, ver in VERSION_FIX.items():
        p = BOOK / old
        if not p.exists():
            print("missing:", old)
            continue
        new = swap_version(p, ver)
        if new.name != p.name:
            p.rename(new)
            print(f"{old} -> {new.name}")

    for old, new_name in CH13_REORDER.items():
        p = BOOK / old
        if p.exists():
            target = BOOK / new_name
            p.rename(target)
            print(f"{old} -> {new_name}")


if __name__ == "__main__":
    main()
