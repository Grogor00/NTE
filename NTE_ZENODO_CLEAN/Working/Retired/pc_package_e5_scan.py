#!/usr/bin/env python3
"""E5 spot-fix grep scan (Cursor PC)."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop")
CARRIERS = list((ROOT / "Book").glob("Chapter_*.md"))
CARRIERS += list((ROOT / "Book").glob("Appendix_A_*.md"))
CARRIERS += [
    ROOT / "NTE v10_6/Papers/Paper_Popular_v10_8_Full_Edition.md",
    ROOT / "NTE v10_6/Papers/Paper_Popular_v10_8_Reader_Edition.md",
]
CARRIERS = [p for p in CARRIERS if "depreciated" not in str(p) and "Book_with_TP" not in str(p)]

E5_1 = [
    "Experimental Confirmations", "experimental confirmations", "experimental confirmation",
    "experimentally confirmed", "experimentally verifies", "experimental verification of NTE",
    "confirms NTE", "confirmed NTE",
]
E5_2 = [r"harmonic oscillator", r"quantisation is compactness", r"Hopf projection of the oscillator"]
E5_3 = [r"a_4\s*=\s*270", r"a₄\s*=\s*270", r"the coefficient 270"]

out = []
for p in CARRIERS:
    t = p.read_text(encoding="utf-8")
    out.append(f"\n## {p.relative_to(ROOT)}")
    for pat in E5_1:
        if pat.lower() in t.lower() if pat != "Experimental Confirmations" else pat in t:
            for m in re.finditer(re.escape(pat), t, re.I):
                line = t[:m.start()].count("\n") + 1
                ctx = t.splitlines()[line - 1].strip()[:120]
                out.append(f"  E5-1 {pat!r} L{line}: {ctx}")
    for pat in E5_2:
        if re.search(pat, t, re.I):
            out.append(f"  E5-2 match: {pat}")
    for pat in E5_3:
        if re.search(pat, t):
            out.append(f"  E5-3 match: {pat}")
    if "geometric constraint" in t:
        out.append("  E6 anchor present: geometric constraint")

report = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_pc_e5_scan_report.txt")
report.write_text("\n".join(out) if len(out) > 1 else "CLEAN — no E5 pattern hits", encoding="utf-8")
print(report.read_text(encoding="utf-8")[:4000])
