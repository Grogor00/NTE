#!/usr/bin/env python3
"""AC grep gates — verifier contract (Handoff_AC_to_Cursor_Main_GrepGate_PassFail_Spec…)."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
PAPERS = ROOT / "Papers"
SPLITS = ROOT / "Working" / "AC_Readable_Splits"

# Live carriers per AC KPhi handoff + grep spec
KPHI_CARRIERS = [
    PAPERS / "Paper_S2_v1_0_Consolidation_20260525.md",
    PAPERS / "NTE_v10_17_Part1_Foundations.md",
    PAPERS / "NTE_v10_17_Part2_Structure.md",
    PAPERS / "NTE_v10_17_Part3_Accounting.md",
    SPLITS / "NTE_v10_17_Part3_Accounting__C_S22_App.md",
]

AUDIT_SKIP = re.compile(
    r"^\s*(?:>|\-|\#|\*)*\s*(?:\[Deprecated|Historical note \(superseded\)|\(deprecated\))",
    re.I,
)

KPHI_ALLOW = re.compile(
    r"open|assumed|conditional|routed|Route E|BREAK-1|retired|does not derive|"
    r"not derive|prior.*claim|undetermined|closure is open",
    re.I,
)
KPHI_BANNED = re.compile(
    r"K\s*\(\s*(?:\\Phi|Φ|Phi)\s*\)\s*=\s*1",
    re.I,
)
KPHI_DERIVED = re.compile(r"derived|closed|Derives|✓", re.I)

KAPPA_BANNED = re.compile(
    r"triply anchored|three-way confluence|two independent confirmations|"
    r"two independent derivations|two independent structural derivations|"
    r"two pathways(?=.*κ)|three Killing[- ]spinor",
    re.I,
)

A4_BANNED = re.compile(
    r"270\s*β_GB|270β_GB|a₄\s*=\s*270|a_4\s*=\s*270|a4\s*=\s*270|270\s*\\beta",
    re.I,
)

ETA_BANNED = re.compile(
    r"(?:η|\beta|baryon asymmetry).{0,120}(?:zero-parameter|zero parameter|0-parameter|parameter-free prediction)|"
    r"would make baryon asymmetry a zero-parameter",
    re.I,
)

MOJIBAKE_BANNED = re.compile(
    r"â€|\\ufffd|Â(?![a-z])|"
    r"Ãƒâ€šÃ‚Â§|Ã‚Â§|Ãƒâ€|â€šÃ‚Â§|"
    r"ð\u009d[\u0090-\u00bf][\u0080-\u00bf]|"
    r"ð\u009d\u0095\u0086|ð\u009d\u0092¦|"
    r"J₃\(ð|J_3\(ð"
)


def is_audit_line(line: str) -> bool:
    return bool(AUDIT_SKIP.search(line))


def gate_kphi(lines: list[str], path: Path) -> list[str]:
    hits: list[str] = []
    name = path.name
    for i, line in enumerate(lines, 1):
        if is_audit_line(line):
            continue
        if not KPHI_BANNED.search(line):
            continue
        if KPHI_ALLOW.search(line):
            continue
        if KPHI_DERIVED.search(line):
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
            continue
        # chord table / closed list without qualifier
        if "§6 ✓" in line or "| Derived" in line:
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
    return hits


def gate_kappa(lines: list[str], path: Path) -> list[str]:
    hits: list[str] = []
    name = path.name
    for i, line in enumerate(lines, 1):
        if is_audit_line(line):
            continue
        if KAPPA_BANNED.search(line):
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
    return hits


SKIP_FILES = {
    "NTE_Standalone_Papers_Register_v0_4.md",
    "NTE_Standalone_Papers_Register_v0_5.md",
    "NTE_Standalone_Papers_Register_v0_6_20260618.md",
    "NTE_Corpus_Papers_Index.md",
}


def gate_a4(lines: list[str], path: Path) -> list[str]:
    if path.name in SKIP_FILES:
        return []
    hits: list[str] = []
    name = path.name
    for i, line in enumerate(lines, 1):
        if is_audit_line(line):
            continue
        if A4_BANNED.search(line):
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
    return hits


def gate_eta(lines: list[str], path: Path) -> list[str]:
    if path.name in SKIP_FILES:
        return []
    negation = re.compile(
        r"not\s*(?:\*\*)?\s*(?:a\s+)?zero-parameter|NOT\s+zero-parameter|"
        r"\*\*not\*\*\s*['\"]zero-parameter|"
        r"structural consistency.{0,80}not.{0,40}zero-parameter|"
        r"not\s+['\"]zero-parameter|"
        r"no structural content changes.{0,80}eta.{0,40}zero-parameter status|"
        r"existence and sign|δ_J\s*=\s*π/2",
        re.I,
    )
    hits: list[str] = []
    name = path.name
    for i, line in enumerate(lines, 1):
        if is_audit_line(line):
            continue
        if negation.search(line):
            continue
        if ETA_BANNED.search(line):
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
    return hits


def gate_mojibake(lines: list[str], path: Path) -> list[str]:
    hits: list[str] = []
    name = path.name
    for i, line in enumerate(lines, 1):
        if MOJIBAKE_BANNED.search(line):
            hits.append(f"{name}:L{i}:{line.strip()[:120]}")
    return hits


GATES = {
    "kphi": gate_kphi,
    "kappa": gate_kappa,
    "a4": gate_a4,
    "eta": gate_eta,
    "mojibake": gate_mojibake,
}


def run_pdf_artifact_gate() -> tuple[bool, list[str]]:
    """Dual-channel PDF gate — text layer + raster sight pack (AC calibration)."""
    gate_py = ROOT / "Working" / "pdf_artifact_gate.py"
    if not gate_py.exists():
        return False, ["pdf_artifact_gate.py missing"]
    r = subprocess.run(
        [sys.executable, str(gate_py), "--report"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    hits: list[str] = []
    if r.returncode != 0:
        report = ROOT / "Working" / "PDF_Sight_Calibration" / "latest" / "report.txt"
        if report.exists():
            for ln in report.read_text(encoding="utf-8").splitlines():
                if ln.strip().startswith("[FAIL]") or "HIT:" in ln or "ERROR:" in ln:
                    hits.append(ln.strip()[:160])
        if not hits:
            hits.append("pdf-artifact gate FAIL (see PDF_Sight_Calibration/latest/report.txt)")
    return r.returncode == 0, hits[:30]


def targets_for_gate(gate: str) -> list[Path]:
    if gate == "kphi":
        return [p for p in KPHI_CARRIERS if p.exists()]
    if gate == "kappa":
        return [PAPERS / "Paper_S2_v1_0_Consolidation_20260525.md"]
    if gate == "mojibake":
        paths = [p for p in PAPERS.glob("*.md") if "depreciated" not in str(p)]
        paths += [p for p in SPLITS.glob("*.md")]
        book = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")
        if book.exists():
            paths += [p for p in book.glob("Chapter_*.md")]
            paths += [p for p in book.glob("Appendix_*.md")]
        return paths
    if gate in ("a4", "eta"):
        return [p for p in PAPERS.glob("*.md") if "depreciated" not in str(p)]
    return []


def run_gate(gate: str, files: list[Path] | None = None) -> tuple[bool, list[str]]:
    fn = GATES[gate]
    paths = files or targets_for_gate(gate)
    all_hits: list[str] = []
    for path in paths:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        all_hits.extend(fn(lines, path))
    return len(all_hits) == 0, all_hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", action="append", required=True)
    ap.add_argument("--file", action="append")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    files = [Path(f) for f in args.file] if args.file else None
    lines_out: list[str] = []
    any_fail = False
    for gate in args.gate:
        if gate == "pdf-mojibake":
            ok, hits = run_pdf_artifact_gate()
        else:
            ok, hits = run_gate(gate, files)
        status = "PASS" if ok else "FAIL"
        if not ok:
            any_fail = True
        lines_out.append(f"[{status}] {gate} ({len(hits)} hits)")
        lines_out.extend(f"  {h}" for h in hits[:20])
        if len(hits) > 20:
            lines_out.append(f"  ... +{len(hits)-20} more")
        lines_out.append("")

    report = "\n".join(lines_out)
    if args.report:
        (ROOT / "Working" / "_cursor_grep_report.txt").write_text(report, encoding="utf-8")
    print(report.encode("ascii", "replace").decode("ascii"))
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
