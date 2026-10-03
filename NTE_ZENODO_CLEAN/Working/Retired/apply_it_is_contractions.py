#!/usr/bin/env python3
"""
Selective it is -> it's for NTE book + Popular Papers.

REGISTER: pedagogical pivot (non-formal). Do not use government/academic
contraction avoidance. Contract when read-aloud sounds natural; target ~55–65%
of eligible 'it is' per pass (cumulative across passes).

Keeps full form only for: short punch sentences, 'it is,' comma-bridge, and
a short list of sentence-initial emphasis (still / structurally forced).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop")

CANONICAL = [
    ROOT / "Book" / "Prelude_The_Forty_Million_Year_Instant_v5.md",
    ROOT / "Book" / "Chapter_1_The_Photons_Journey_v7_3.md",
    ROOT / "Book" / "Chapter_2_Entanglement_as_Geometry_v6.md",
    ROOT / "Book" / "Chapter_3_A_Closed_Universe_v5.md",
    ROOT / "Book" / "Chapter_4_Time_as_Expansion_v7_2.md",
    ROOT / "Book" / "Chapter_5_The_Eighth_Colour_v6_1.md",
    ROOT / "Book" / "Chapter_6_Why_Quantum_Mechanics_is_Geometry_v5_3.md",
    ROOT / "Book" / "Chapter_7_The_Gauge_Birth_v3_3.md",
    ROOT / "Book" / "Chapter_8_The_Unresolved_Particle_v4.md",
    ROOT / "Book" / "Chapter_9_The_Number_That_Could_Have_Failed_v3.md",
    ROOT / "Book" / "Chapter_10_The_Other_Trouser_v2.md",
    ROOT / "Book" / "Chapter_11_What_the_Universe_Sounds_Like_v3_1.md",
    ROOT / "Book" / "Chapter_12_The_Chord_v3_1.md",
    ROOT / "Book" / "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v4.md",
    ROOT / "Book" / "Chapter_14_Strange_Geometries_and_Structural_Rhymes_v1.md",
    ROOT / "Book" / "Chapter_15_The_Score_v2.md",
    ROOT / "Book" / "Chapter_16_The_Working_Bet_v1.md",
    ROOT / "NTE v10_6" / "Papers" / "Paper_Popular_v10_8_Full_Edition.md",
    ROOT / "NTE v10_6" / "Papers" / "Paper_Popular_v10_8_Reader_Edition.md",
]

# Rare keeps — emphasis / rhythm only
KEEP_INITIAL_RE = re.compile(
    r"^It is\b\s+(?:still\b|structurally forced)",
    re.IGNORECASE,
)

KEEP_SHORT_PUNCH = re.compile(
    r"^It is\s+(?:real|invisible|octarine|meaningful|forced|novel|clear|correct|true|false)\.\s",
    re.IGNORECASE,
)

IT_IS = re.compile(r"\b([Ii])t is\b")


def should_contract(match: re.Match[str], text: str) -> bool:
    start = match.start()
    before = text[max(0, start - 100) : start]
    if re.search(r"\bit's\b|\bIt's\b", before[-25:]):
        return False

    rest = text[start : start + 80]
    if KEEP_SHORT_PUNCH.match(rest) or KEEP_INITIAL_RE.match(rest):
        return False

    after = text[match.end() : match.end() + 8]
    # "although it is, but …" — predicate continues after comma
    if re.match(r",\s", after):
        return False

    return True


def process_text(text: str) -> tuple[str, int, int]:
    total = len(IT_IS.findall(text))
    contracted = 0
    parts: list[str] = []
    last = 0
    for m in IT_IS.finditer(text):
        parts.append(text[last : m.start()])
        if should_contract(m, text):
            parts.append(f"{m.group(1)}t's")
            contracted += 1
        else:
            parts.append(m.group(0))
        last = m.end()
    parts.append(text[last:])
    return "".join(parts), total, contracted


def main() -> int:
    dry = "--dry-run" in sys.argv
    grand_total = grand_contracted = 0
    reports: list[str] = []

    for path in CANONICAL:
        if not path.exists():
            reports.append(f"MISSING: {path}")
            continue
        raw = path.read_text(encoding="utf-8")
        new, total, contracted = process_text(raw)
        pct = (100.0 * contracted / total) if total else 0.0
        reports.append(f"{path.name}: {contracted}/{total} ({pct:.0f}%)")
        grand_total += total
        grand_contracted += contracted
        if not dry and new != raw:
            path.write_text(new, encoding="utf-8", newline="\n")

    gpct = (100.0 * grand_contracted / grand_total) if grand_total else 0.0
    print("=== it is -> it's (pedagogical pivot / non-formal) ===")
    print("\n".join(reports))
    print(f"\nTOTAL this pass: {grand_contracted}/{grand_total} ({gpct:.1f}%)")
    if dry:
        print("(dry run — no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
