#!/usr/bin/env python3
"""Post-apply smoke checks for Book opening-arc 20260924."""
from __future__ import annotations
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
BOOK = ROOT / "Book"

files = [
    "Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md",
    "Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md",
    "Chapter_15_The_Score_v3.md",
    "Chapter_15_The_Score_v4.md",
    "Chapter_04_Time_as_Expansion_v8.md",
    "Chapter_04_Time_and_Expansion_v9.md",
    "Chapter_05_The_Eighth_Colour_v7.md",
    "Chapter_05_The_Eighth_Colour_v8.md",
    "Chapter_02_Entanglement_as_Geometry_v7.md",
    "Chapter_02_Entanglement_as_Geometry_v8.md",
    "Chapter_01_The_Photons_Journey_v10.md",
    "Chapter_01_The_Photons_Journey_v11.md",
    "Prelude_The_Forty_Million_Year_Instant_v7.md",
    "Prelude_The_Forty_Million_Year_Instant_v8.md",
    "Chapter_03_A_Closed_Universe_v6_1.md",
    "Chapter_03_A_Closed_Universe_v7.md",
]
print("=== File presence ===")
for f in files:
    p = BOOK / f
    status = "OK" if p.exists() else "MISSING"
    size = p.stat().st_size if p.exists() else 0
    print(f"{status:8} {f}  ({size} bytes)")

print("\n=== Appendix C v1.4 ===")
ac = (BOOK / "Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md").read_text(encoding="utf-8")
for needle, expect in [
    ("Ciambelli", 1),
    ("necessary but not sufficient", 1),
    ("does not determine the solar angle", 1),
    ("exactly 1", 1),
    ("equal* amplitude".replace("*", ""), 0),  # placeholder
]:
    pass
checks = [
    ("Ciambelli", "Ciambelli", 1),
    ("necessary but not sufficient", "necessary but not sufficient", 1),
    ("does not determine the solar angle", "does not determine the solar angle", 1),
    ("tan exactly 1", "tan²θ₂₃ is exactly 1", 1),
    ("equal amplitude", "equal* amplitude".replace("*", ""), 1),
]
# fix equal amplitude needle
checks[-1] = ("equal amplitude", "equal amplitude", 1)
for label, needle, expect in checks:
    n = ac.count(needle)
    print(f"{'PASS' if n == expect else 'FAIL':4} {label}: count={n} expect={expect}")
print(f"     0.9692={ac.count('0.9692')} 0.0053={ac.count('0.0053')}")
print(f"     TM1={ac.count('TM1')} TM2={ac.count('TM2')} trimaximal={ac.count('trimaximal')}")

print("\n=== Ch 4 / Ch 3 retitle alignment ===")
c4 = (BOOK / "Chapter_04_Time_and_Expansion_v9.md").read_text(encoding="utf-8")
c3 = (BOOK / "Chapter_03_A_Closed_Universe_v7.md").read_text(encoding="utf-8")
print("Ch4 H1:", [ln for ln in c4.splitlines() if ln.startswith("# ")][:1])
print("Time as Expansion in Ch4 v9:", c4.count("Time as Expansion"))
print("Time and Expansion in Ch4 v9:", c4.count("Time and Expansion"))
print("Towards Time and Expansion in Ch3:", c3.count("Towards Time and Expansion"))
print("Towards Time as Expansion in Ch3:", c3.count("Towards Time as Expansion"))
print("dramatic support in Ch3 v7:", c3.count("dramatic support"))
print("one-sided present:", "one-sided" in c3)
print("may never get to find out:", "may never get to find out" in c3)
print("N_lock candidate:", "candidate" in c4 and "N_lock" in c4)

print("\n=== Ch 15 ===")
c15 = (BOOK / "Chapter_15_The_Score_v4.md").read_text(encoding="utf-8")
print("0.9692", c15.count("0.9692"), "0.9743", c15.count("0.9743"))
print("1.0σ", c15.count("1.0σ"), "0.85σ", c15.count("0.85σ"))
print("Withdrawn", c15.count("Withdrawn"))
print("sitting between anchors:", "n_s sitting between the two CMB anchors" in c15)

print("\n=== Ch 5 D10/D11 ===")
c5 = (BOOK / "Chapter_05_The_Eighth_Colour_v8.md").read_text(encoding="utf-8")
print("V_NTE count:", c5.count("V_NTE"))
print("curvature of its potential:", "curvature of its potential" in c5)
print("read off:", "read off" in c5)

print("\n=== Ch 1 F2 heading ===")
c1 = (BOOK / "Chapter_01_The_Photons_Journey_v11.md").read_text(encoding="utf-8")
print("## Time and Expansion:", c1.count("## Time and Expansion"))
print("## Time is Emergent from Expansion:", c1.count("## Time is Emergent from Expansion"))

print("\n=== Manifest ===")
man = (ROOT / "NTE_Workflow_Manifest_v10_18.md").read_text(encoding="utf-8")
for s in [
    "Book/ opening arc — four sets ratified",
    "Book/ AC-response revisions",
    "Appendix C v1.4 patch set",
]:
    print(("YES" if s in man else "NO "), s)

print("\n=== Size deltas (pred → new) ===")
pairs = [
    ("Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md", "Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md"),
    ("Chapter_15_The_Score_v3.md", "Chapter_15_The_Score_v4.md"),
    ("Chapter_04_Time_as_Expansion_v8.md", "Chapter_04_Time_and_Expansion_v9.md"),
    ("Chapter_05_The_Eighth_Colour_v7.md", "Chapter_05_The_Eighth_Colour_v8.md"),
    ("Chapter_02_Entanglement_as_Geometry_v7.md", "Chapter_02_Entanglement_as_Geometry_v8.md"),
    ("Chapter_01_The_Photons_Journey_v10.md", "Chapter_01_The_Photons_Journey_v11.md"),
    ("Prelude_The_Forty_Million_Year_Instant_v7.md", "Prelude_The_Forty_Million_Year_Instant_v8.md"),
    ("Chapter_03_A_Closed_Universe_v6_1.md", "Chapter_03_A_Closed_Universe_v7.md"),
]
for a, b in pairs:
    print(f"  {(BOOK/a).stat().st_size:6} → {(BOOK/b).stat().st_size:6}  {b}")
