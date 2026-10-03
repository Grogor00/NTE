#!/usr/bin/env python3
"""Discover remaining mojibake byte patterns vs Reader Edition clean text."""
from pathlib import Path

corrupt = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md.mojibake_bak")
reader = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Reader_Edition.md")

cb = corrupt.read_bytes()
# patterns to find in corrupt
needles = [
    b"m_\xce\xbd",  # m_nu start
    b"H\xe2\x82",  # H0
    b"\xce\x9b",  # Lambda if fixed
    b"\xc3\x8e\xc2\xbb",  # bad Lambda
    b"\xc3\xa2\xe2\x80\x9a",  # subscript prefix
    b"\xc3\xa2\xcb\x86\x9a",  # sqrt
    b"\xc3\x8f\xe2\x80\xb0",  # pi bad
    b"\xc3\x82\xa7",  # section
]
for n in needles:
    i = cb.find(n)
    print(n, "->", cb[i:i+20] if i>=0 else "NOT FOUND")

# find m_ nu subscript corrupt
i = cb.find(b"m_{\xce\xbd")
print("m_nu block", cb[i:i+30])

i = cb.find(b"H\xe2\x82\x80")
print("H0 block", cb[i:i+12])

i = cb.find(b"\xc3\x8e\xc2\xbb")
print("Lambda block", cb[i:i+8])

i = cb.find(b"\xc3\xa2\xcb\x86\x9a")
print("sqrt block", cb[i:i+8])

# reader equivalents
rb = reader.read_bytes()
i = rb.find(b"m_{\xce\xbd")
print("clean m_nu", rb[i:i+20])
i = rb.find(b"H\xe2\x82\x82")
print("clean H0", rb[i:i+8])
i = rb.find(b"\xce\x9b")
print("clean Lambda", rb[i:i+4])
