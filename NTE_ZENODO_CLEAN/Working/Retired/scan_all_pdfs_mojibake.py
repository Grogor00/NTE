#!/usr/bin/env python3
"""Batch mojibake scan on all PDFs in paper-build/pdf-out."""
import re
import subprocess
import sys
from pathlib import Path

PDF_DIR = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\paper-build\pdf-out")
PDFTOTEXT = Path(r"C:\Users\gregw\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe")
OUT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_pdf_mojibake_scan_report.txt")
TMP = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_pdf_scan_tmp.txt")

# Known UTF-8-read-as-Latin1 corruption fragments
BAD_SUBSTRINGS = [
    "â€",   # em dash / smart quotes
    "â»",   # superscript minus
    "âŸ",   # angle brackets
    "âˆ",   # math minus/sqrt
    "â‰",   # approx
    "â†",   # arrows
    "âˆ'",  # sqrt variant
    "Ã—",   # times
    "Ã©",   # é (if wrong context — flag for review)
    "Ïˆ",   # psi corruption
    "Ï†",   # phi corruption
    "Îº",   # kappa corruption
    "Î²",   # beta corruption
    "Î›",   # Lambda corruption
    "â‚",   # subscript corruption
    "â„",   # script C etc.
]

# Regex: lines with â not part of legitimate French (rare); flag all â hits
RE_SUSPECT = re.compile(r"â|Ã.|Î[A-Za-z]|Ï[A-Za-z]|ï¿½|\ufffd")


def scan_text(name: str, text: str) -> dict:
    hits = {b: text.count(b) for b in BAD_SUBSTRINGS if b in text}
    suspect_lines = []
    for i, line in enumerate(text.splitlines(), 1):
        if RE_SUSPECT.search(line):
            suspect_lines.append((i, line.strip()[:160]))
    return {"name": name, "hits": hits, "lines": suspect_lines, "chars": len(text)}


def main() -> int:
    if not PDFTOTEXT.exists():
        print(f"pdftotext not found: {PDFTOTEXT}", file=sys.stderr)
        return 1

    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    results = []
    clean = []
    failed = []

    for pdf in pdfs:
        try:
            subprocess.run(
                [str(PDFTOTEXT), "-enc", "UTF-8", str(pdf), str(TMP)],
                check=True,
                capture_output=True,
            )
            text = TMP.read_text(encoding="utf-8", errors="replace")
            r = scan_text(pdf.name, text)
            results.append(r)
            if r["hits"] or r["lines"]:
                pass  # flagged
            else:
                clean.append(pdf.name)
        except subprocess.CalledProcessError as e:
            failed.append((pdf.name, e.stderr.decode(errors="replace")[:200]))

    lines_out = [
        f"PDF mojibake scan — {PDF_DIR}",
        f"Files scanned: {len(pdfs)}",
        f"Clean: {len(clean)}",
        f"Flagged: {len(results) - len(clean) - len(failed)}",
        f"Failed extraction: {len(failed)}",
        "",
    ]

    flagged = [r for r in results if r["hits"] or r["lines"]]
    if flagged:
        lines_out.append("=" * 72)
        lines_out.append("FLAGGED PDFs")
        lines_out.append("=" * 72)
        for r in sorted(flagged, key=lambda x: x["name"]):
            lines_out.append(f"\n## {r['name']} ({r['chars']} chars extracted)")
            if r["hits"]:
                lines_out.append("  substring counts: " + ", ".join(f"{k}={v}" for k, v in sorted(r["hits"].items())))
            else:
                lines_out.append("  substring counts: (none)")
            if r["lines"]:
                lines_out.append(f"  suspect lines ({len(r['lines'])}):")
                for ln, content in r["lines"][:8]:
                    lines_out.append(f"    L{ln}: {content}")
                if len(r["lines"]) > 8:
                    lines_out.append(f"    ... +{len(r['lines']) - 8} more")
    else:
        lines_out.append("No mojibake patterns detected in any PDF.")

    if failed:
        lines_out.extend(["", "=" * 72, "EXTRACTION FAILURES", "=" * 72])
        for name, err in failed:
            lines_out.append(f"  {name}: {err}")

    lines_out.extend(["", "=" * 72, "CLEAN PDFs", "=" * 72])
    for name in clean:
        lines_out.append(f"  OK  {name}")

    report = "\n".join(lines_out)
    OUT.write_text(report, encoding="utf-8")
    # stdout summary (ASCII-safe)
    print(f"Scanned {len(pdfs)} PDFs -> {len(clean)} clean, {len(flagged)} flagged, {len(failed)} failed")
    print(f"Report: {OUT}")
    if flagged:
        for r in flagged:
            print(f"  FLAG  {r['name']}: {r['hits'] or 'regex-only'}")
    return 0 if not flagged else 2


if __name__ == "__main__":
    raise SystemExit(main())
