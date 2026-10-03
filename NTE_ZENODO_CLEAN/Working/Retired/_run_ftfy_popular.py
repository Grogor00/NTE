#!/usr/bin/env python3
import ftfy

path = r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md"
out_path = path
preview = r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_popular_fixed_preview.md"

t = open(path, encoding="utf-8-sig").read()
f = ftfy.fix_text(t)

print("emdash", t.count("\u2014"), "->", f.count("\u2014"))
print("bad ae", t.count("\u00e2"), "->", f.count("\u00e2"))
print("bad times", t.count("Ã"), "->", f.count("Ã"))
print("bad phi", t.count("Î"), "->", f.count("Î"))

for line in f.splitlines():
    if "Popular Paper" in line:
        print("LINE:", line[:110])
        break
for line in f.splitlines():
    if "photon of light" in line:
        print("PHOTON:", line[:95])
        break

open(preview, "w", encoding="utf-8", newline="\n").write(f)
print("preview bytes", len(f.encode("utf-8")))

# sanity: no mojibake markers
bad_markers = ["â€", "Ã—", "Î¦", "â‰ˆ", "âˆš", "Â·"]
for m in bad_markers:
    if m in f:
        print("STILL HAS", repr(m), f.count(m))
