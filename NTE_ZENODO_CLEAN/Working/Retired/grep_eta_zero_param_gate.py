#!/usr/bin/env python3
"""Grep gate: live deposit carriers must not claim η magnitude zero-parameter."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
CARRIERS = [
    "Companion_10_Gap1_M1_Pathways_v10_17_2.md",
    "NTE_v10_17_Part3_Accounting.md",
    "Paper_Popular_v10_8_Full_Edition.md",
    "Paper_Popular_v10_8_Reader_Edition.md",
    "NTE_Standalone_Papers_Register_v0_5.md",
]

BAD_PATTERNS = [
    re.compile(r"would make baryon asymmetry a zero-parameter"),
    re.compile(r"η\s*=\s*6\.1[^.\n]{0,40}zero-parameter prediction"),
    re.compile(r"η_B[^.\n]{0,60}zero-parameter prediction(?!\s*\()"),
    re.compile(r"complete zero-parameter prediction[^.\n]{0,40}η"),
    re.compile(r"η[^.\n]{0,40}complete zero-parameter prediction"),
    re.compile(r"zero-parameter at S1 precision"),
]

NEGATION = re.compile(r"not zero-parameter|not a zero-parameter|not clean Tier A zero-parameter|Do not claim η zero-parameter|Strike")


def scan_file(path: Path) -> list[tuple[int, str]]:
    hits = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if NEGATION.search(line):
            continue
        for pat in BAD_PATTERNS:
            if pat.search(line):
                hits.append((i, line.strip()[:200]))
                break
    return hits


def main() -> None:
    any_bad = False
    for name in CARRIERS:
        p = ROOT / name
        hits = scan_file(p)
        status = "CLEAN" if not hits else "FLAG"
        print(f"{status}  {name}")
        for ln, text in hits:
            any_bad = True
            print(f"  L{ln}: {text}")
    # A.4 #5 spot check
    p3 = (ROOT / "NTE_v10_17_Part3_Accounting.md").read_text(encoding="utf-8")
    a45 = [ln for ln in p3.splitlines() if ln.strip().startswith("5. M₁")]
    print("\nA.4 #5:", a45[0][:160] if a45 else "MISSING")
    raise SystemExit(1 if any_bad else 0)


if __name__ == "__main__":
    main()
