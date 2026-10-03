#!/usr/bin/env python3
from pathlib import Path

t = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md").read_text(encoding="utf-8")
b = t.encode("utf-8")

# collect unique suspicious substrings
import re
bad = re.findall(r"[\u00c0-\u00ff]{2,}|â.{1,3}|Î.|Ï.|Â.|Ã.", t)
from collections import Counter
c = Counter(bad)
for s, n in c.most_common(40):
    print(n, s.encode("unicode_escape").decode())

print("--- byte snippets for top ---")
for s, _ in c.most_common(15):
    i = t.find(s)
    if i >= 0:
        print(s.encode("unicode_escape").decode(), "bytes", b[i : i + len(s.encode())].hex())
