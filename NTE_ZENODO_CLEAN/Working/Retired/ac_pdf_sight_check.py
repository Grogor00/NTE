#!/usr/bin/env python3
"""AC sight check: extract PDF text layer and probe known-risk loci."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
PDFTOTEXT = Path(r"C:\Users\gregw\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe")
OUT = ROOT / "Working" / "_ac_pdf_sight_report.txt"

CARRIERS = {
    "S2": ROOT / "paper-build/pdf-out/Paper_S2_v1_0_Consolidation_20260525.pdf",
    "Part3": ROOT / "paper-build/pdf-out/NTE_v10_17_Part3_Accounting.pdf",
    "Popular": ROOT / "paper-build/pdf-out/Paper_Popular_v10_8_Full_Edition.pdf",
}

# AC corruption signatures (rendered artifact)
BAD_RE = re.compile(
    r"ð\u009d|â€|\\ufffd|Ãƒ|Ã‚Â§|J₃\(ð|J_3\(ð|"
    r"ð\u009d\u0095\u0086|ð\u009d\u0092¦"
)
GOOD_GLYPHS = ["𝕆", "𝒦", "β", "κ", "§", "Φ"]

AC_LOCI = {
    "S2": [
        ("title CPN octonion", re.compile(r"Hopf.*S.*×.*S.*×", re.I)),
        ("§2.3 octonion", re.compile(r"2\.3|octonion", re.I)),
        ("κ₀ 4.3", re.compile(r"3/\\sqrt\{4\\pi\}|3/\u221a\(4\u03c0\)|kappa", re.I)),
        ("K(Φ) 6.2", re.compile(r"K\s*\(\s*\\?Phi|K\(Φ\)", re.I)),
    ],
    "Part3": [
        ("§22.17 S_bridge", re.compile(r"S_bridge|22\.17", re.I)),
        ("Conclusion octonion", re.compile(r"Conclusion|octonion", re.I)),
    ],
    "Popular": [
        ("J3 Jordan", re.compile(r"Jordan|J₃|J3", re.I)),
    ],
}


def extract(pdf: Path) -> str:
    tmp = ROOT / "Working" / "_pdf_sight_tmp.txt"
    subprocess.run(
        [str(PDFTOTEXT), "-enc", "UTF-8", "-layout", str(pdf), str(tmp)],
        check=True,
        capture_output=True,
    )
    return tmp.read_text(encoding="utf-8", errors="replace")


def scan(name: str, text: str) -> list[str]:
    lines: list[str] = []
    bad_hits = [(i + 1, ln) for i, ln in enumerate(text.splitlines()) if BAD_RE.search(ln)]
    lines.append(f"bad_pattern_lines={len(bad_hits)}")
    for i, ln in bad_hits[:15]:
        lines.append(f"  BAD L{i}: {ln.strip()[:200]}")
    if len(bad_hits) > 15:
        lines.append(f"  ... +{len(bad_hits) - 15} more BAD lines")

    for g in GOOD_GLYPHS:
        c = text.count(g)
        if c:
            lines.append(f"good_glyph {g!r} count={c}")

    for label, pat in AC_LOCI.get(name, []):
        ctx = []
        for i, ln in enumerate(text.splitlines(), 1):
            if pat.search(ln):
                ctx.append((i, ln.strip()[:220]))
                if len(ctx) >= 3:
                    break
        lines.append(f"locus {label}: {len(ctx)} matching line(s)")
        for i, ln in ctx:
            lines.append(f"  L{i}: {ln}")

  # reflow heuristics per AC
    reflow_flags = []
    for i, ln in enumerate(text.splitlines(), 1):
        if re.search(r"appears only\s*/\s*through trace", ln, re.I):
            reflow_flags.append((i, "dirac splice?", ln.strip()[:180]))
        if re.search(r"therefore not available.*from an", ln, re.I):
            reflow_flags.append((i, "kphi reorder?", ln.strip()[:180]))
    if reflow_flags:
        lines.append(f"reflow_suspects={len(reflow_flags)}")
        for i, tag, ln in reflow_flags[:5]:
            lines.append(f"  L{i} [{tag}]: {ln}")

    lines.append("--- first 15 nonblank lines ---")
    n = 0
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.strip():
            lines.append(f"  L{i}: {ln.strip()[:200]}")
            n += 1
            if n >= 15:
                break
    return lines


def main() -> int:
    report = ["AC PDF SIGHT REPORT (Cursor Main)", "method: pdftotext -enc UTF-8 -layout", ""]
    any_bad = False
    for key, pdf in CARRIERS.items():
        report.append("=" * 72)
        report.append(f"## {key}: {pdf}")
        if not pdf.exists():
            report.append("MISSING")
            any_bad = True
            continue
        st = pdf.stat()
        report.append(f"mtime={st.st_mtime} size={st.st_size}")
        try:
            text = extract(pdf)
            report.append(f"extracted_chars={len(text)}")
            sub = scan(key, text)
            report.extend(sub)
            if any(l.startswith("  BAD") for l in sub) or sub[0].startswith("bad_pattern_lines=") and not sub[0].endswith("=0"):
                cnt = int(sub[0].split("=")[1])
                if cnt > 0:
                    any_bad = True
        except subprocess.CalledProcessError as e:
            report.append(f"pdftotext FAILED: {e.stderr.decode(errors='replace')[:300]}")
            any_bad = True
        report.append("")

    report.append("VERDICT: " + ("FAIL — PDF text layer still shows corruption" if any_bad else "PROVISIONAL PASS — no BAD patterns in text layer; AC human sight still required"))
    OUT.write_text("\n".join(report), encoding="utf-8")
    print(OUT.read_text(encoding="utf-8").encode("ascii", errors="replace").decode("ascii"))
    return 2 if any_bad else 0


if __name__ == "__main__":
    sys.exit(main())
