#!/usr/bin/env python3
from pathlib import Path
import re

t = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md").read_text(encoding="utf-8")

anchors = ["H\u2080", "Hâ‚€", "Î›", "â‰ˆ", "âˆ’", "â†’", "κâ‚€", "â„‚", "Pin⁻", "Pinâ", "2âˆš2", "Î”"]
for a in anchors:
    i = t.find(a)
    if i >= 0:
        seg = t[i : i + len(a) + 3]
        print(a.encode("unicode_escape").decode(), "->", seg.encode("unicode_escape").decode())

# unique bad 3-char sequences starting with special
bad = re.findall(r"[\u00e2\u00c3\u00ce\u00cf][\u0080-\u00ff]{1,3}", t)
from collections import Counter
for s, n in Counter(bad).most_common(20):
    print(n, s.encode("unicode_escape").decode())
