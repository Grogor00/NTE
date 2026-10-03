#!/usr/bin/env python3
"""Find non-latin-1 chars blocking mojibake fix."""
path = r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md"
text = open(path, encoding="utf-8-sig").read()
for i, c in enumerate(text):
    if ord(c) > 255:
        start = max(0, i - 30)
        end = min(len(text), i + 30)
        snippet = text[start:end].replace("\n", "\\n")
        print(f"U+{ord(c):04X} at {i}: ...{snippet}...")
