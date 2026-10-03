#!/usr/bin/env python3
"""Extract and scan Popular PDF for mojibake."""
import subprocess
from pathlib import Path

PDF = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\paper-build\pdf-out\Paper_Popular_v10_8_Full_Edition.pdf")
TXT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_popular_pdf_extract.txt")
PDFTOTEXT = Path(r"C:\Users\gregw\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe")

subprocess.run([str(PDFTOTEXT), "-enc", "UTF-8", str(PDF), str(TXT)], check=True)
text = TXT.read_text(encoding="utf-8", errors="replace")

BAD = ["â€", "â»", "âŸ", "âˆ", "â‰", "Ã—", "Ïˆ", "Ï†"]
found = {b: text.count(b) for b in BAD if b in text}
print("mojibake hits:", found or "none")

GOOD = ["—", "·", "κ", "β", "10⁻¹²", "Pin⁻", "⟨ψ|φ⟩", "η_B", "H₀"]
for g in GOOD:
    print(f"  {g!r}: {text.count(g)}")

for line in text.splitlines():
    if "â" in line or "Ã" in line:
        print("SUSPECT:", line[:140])

print("em_dash:", text.count("\u2014"))
print("pdf_bytes:", PDF.stat().st_size)
