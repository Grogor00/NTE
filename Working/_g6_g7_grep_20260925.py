#!/usr/bin/env python3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
root = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Core_Papers")
pdf = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\paper-build\pdf-out")

patterns = [
    "40 Mpc",
    "forty megaparsec",
    "coherence length",
    "coherence mass",
    "free-stream",
    "free streaming",
    "M_c",
]

print("=== G6 hits ===")
for p in sorted(root.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    for pat in patterns:
        i = 0
        while True:
            j = t.lower().find(pat.lower(), i)
            if j < 0:
                break
            before = t[:j]
            heads = [ln for ln in before.splitlines() if ln.startswith("#")]
            head = heads[-1] if heads else "(no heading)"
            snip = t[max(0, j - 100) : j + 220].replace("\n", " ")
            print(f"FILE\t{p.name}")
            print(f"PAT\t{pat}")
            print(f"HEAD\t{head[:100]}")
            print(f"SNIP\t{snip}")
            print("---")
            i = j + 1

print("=== G7 mediat (neutrino-subject filter) ===")
for p in sorted(root.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    low = t.lower()
    i = 0
    while True:
        j = low.find("mediat", i)
        if j < 0:
            break
        before = t[:j]
        heads = [ln for ln in before.splitlines() if ln.startswith("#")]
        head = heads[-1] if heads else "(no heading)"
        snip = t[max(0, j - 80) : j + 180].replace("\n", " ")
        print(f"FILE\t{p.name}")
        print(f"HEAD\t{head[:100]}")
        print(f"SNIP\t{snip}")
        print("---")
        i = j + 1

print("=== PDF currency C17-20 ===")
for name in ["Companion_17", "Companion_18", "Companion_19", "Companion_20"]:
    mds = list(root.glob(name + "*.md"))
    pdfs = list(pdf.glob(name + "*.pdf"))
    if mds and pdfs:
        ok = pdfs[0].stat().st_mtime > mds[0].stat().st_mtime
        status = "OK" if ok else "STALE"
        print(f"{status}\t{pdfs[0].name}\tsize={pdfs[0].stat().st_size}")
