#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
PDFTOTEXT = Path(r"C:\Users\gregw\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe")
OUT = ROOT / "Working" / "_codepoint_probe.txt"

def probe(name, pdf):
    tmp = ROOT / "Working" / f"_probe_{name}.txt"
    subprocess.run([str(PDFTOTEXT), "-enc", "UTF-8", "-layout", str(pdf), str(tmp)], check=True)
    t = tmp.read_text(encoding="utf-8")
    lines = [f"=== {name} {pdf.name} ==="]
    for label, ch in [
        ("U+1D546 O", "\U0001d546"),
        ("U+1D4A6 K", "\U0001d4a6"),
        ("eth", "\u00f0"),
        ("beta", "\u03b2"),
        ("kappa", "\u03ba"),
        ("sect", "\u00a7"),
    ]:
        lines.append(f"  {label}: {t.count(ch)}")
    lines.append("  AC bad literal count: " + str(t.count("\u00f0\u009d")))
    for i, ln in enumerate(t.splitlines()[:8], 1):
        lines.append(f"  L{i}: {ln.strip()[:120]}")
    for i, ln in enumerate(t.splitlines(), 1):
        if "S_bridge" in ln or ("bridge" in ln.lower() and "K(" in ln):
            lines.append(f"  S_bridge L{i}: {ln.strip()[:200]}")
    for i, ln in enumerate(t.splitlines(), 1):
        if "K(Φ)" in ln or "K(\\Phi)" in ln or "6.2" in ln and "K" in ln:
            if "open" in ln.lower() or "BREAK" in ln:
                lines.append(f"  Kphi L{i}: {ln.strip()[:200]}")
                break
    for i, ln in enumerate(t.splitlines(), 1):
        if "appears only" in ln and "trace" in ln:
            lines.append(f"  REFLOW? L{i}: {ln.strip()[:200]}")
    return lines

pdfs = {
    "S2": ROOT / "paper-build/pdf-out/Paper_S2_v1_0_Consolidation_20260525.pdf",
    "Part3": ROOT / "paper-build/pdf-out/NTE_v10_17_Part3_Accounting.pdf",
    "Popular": ROOT / "paper-build/pdf-out/Paper_Popular_v10_8_Full_Edition.pdf",
}
report = []
for k, p in pdfs.items():
    report.extend(probe(k, p))
    report.append("")
OUT.write_text("\n".join(report), encoding="utf-8")
