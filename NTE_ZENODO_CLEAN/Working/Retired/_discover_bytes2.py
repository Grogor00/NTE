#!/usr/bin/env python3
from pathlib import Path

b = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md").read_bytes()

def show(label, start: bytes, ctx=20):
    i = b.find(start)
    print(label, i, b[i:i+ctx].hex() if i>=0 else "NF")

show("approx", b"follows")
# search text anchors
for anchor in [b"m_{\xce\xbd", b"H\xe2\x80\x9a", b"\xce\xba and m_", b"\xce\xbb", b"2\xc3\xa2", b"(8\xc3\x8f", b"\xc3\x8e\xbb", b"\xc3\x82\xa7"]:
    i = b.find(anchor)
    if i >= 0:
        print(anchor, "at", i, b[max(0,i-5):i+25].hex())

# find m_ nu pattern in text
t = b.decode("utf-8")
idx = t.find("m_")
while idx >= 0 and idx < 2000:
    if "nu" in t[idx:idx+8] or "\u03bd" in t[idx:idx+8]:
        seg = t[idx:idx+12]
        print("m_seg", seg.encode("unicode_escape").decode(), b[idx:idx+20].hex())
    idx = t.find("m_", idx+1)
