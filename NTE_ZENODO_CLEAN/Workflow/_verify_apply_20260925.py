# -*- coding: utf-8 -*-
from pathlib import Path

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
checks = [
    ("Ch10v9", "Chapter_10_The_Silvered_Boundary_v9.md", [
        "Three caveats", "four hundred trillion suns", "science-fiction sense", "cluster-scale, and moving",
        "above roughly 4",  # should be gone
    ]),
    ("Ch12", "Chapter_12_The_Chord_v4_2a.md", [
        "moved twice", "conditional register", "sales figure", "not yet earned",
        "earned its promotion",  # should be gone if AJ1 applied
    ]),
    ("Ch3", "Chapter_03_A_Closed_Universe_v8.md", [
        "cosmological event horizon", "not carrying the coupling", "not a bookkeeping device",
        "Hubble horizon",  # should be gone
    ]),
    ("Ch6", "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6_1.md", [
        "well-defined cosmic time", "well-defined proper time",
    ]),
    ("AppC", "Appendix_C_The_Open_Ledger_v1_5_DRAFT_PC_20260925.md", [
        "not fixed", "order 10", "~40 Mpc",
    ]),
    ("Ch15", "Chapter_15_The_Score_v6.md", [
        "not a fixed threshold", "order 10", "coherence mass of around 4",
    ]),
]
lines = []
for label, fn, needles in checks:
    p = book / fn
    if not p.exists():
        lines.append(f"{label}: MISSING FILE {fn}")
        continue
    t = p.read_text(encoding="utf-8")
    tl = t.lower()
    for n in needles:
        hit = n.lower() in tl
        lines.append(f"{label}: {'HIT' if hit else 'MISS'}  {n}")

out = Path(r"C:\Users\gregw\Desktop\NTE v10_6\Workflow\_cursor_apply_report_20260925.txt")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
