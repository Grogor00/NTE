#!/usr/bin/env python3
path = r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md"
raw = open(path, encoding="utf-8-sig").read()
# chars above U+00FF (likely already-correct Unicode edits)
hi = [c for c in raw if ord(c) > 0xFF]
from collections import Counter
print("chars > 0xFF:", Counter(hi).most_common(20))
print("total hi:", len(hi))

try:
    fixed = raw.encode("latin-1").decode("utf-8")
    print("latin-1 roundtrip OK")
    print("sample:", [l for l in fixed.splitlines() if "Popular Paper" in l][0][:100])
except Exception as e:
    print("latin-1 FAIL", e)
