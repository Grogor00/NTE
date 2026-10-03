#!/usr/bin/env python3
"""Build AC file-reference index (local paths + known Drive IDs).

Regenerate after corpus changes or on autonomous sustain tick.
Output: Workflow/INDEX_NTE_FileReference_AC.md + .json
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT.parent / "Book"
OUT_MD = ROOT / "Workflow" / "INDEX_NTE_FileReference_AC.md"
OUT_JSON = ROOT / "Workflow" / "INDEX_NTE_FileReference_AC.json"

# Known Drive IDs extracted from corpus cross-refs and PC/AC handoffs (extend on refresh)
KNOWN_DRIVE_IDS: dict[str, str] = {
    "Papers/Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md": "1OsA7PSa3cfbzEIvH2Rn-wrFXVQ8R6BJQ",
    "Papers/Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md": "1B515jCCc3Czau6CGoReGK0YicKSSVOHc",
    "Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md": "19iX9jPZKaZyB1hRKAiuTGORvOXkrMV3N",
    "Papers/Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md": "1cN9WWDLrQjjtRz2oNfn-lezwAxJk0nnW",  # Greg Drive link 2026-06-14
    "Papers/Paper_S1_v0_4.md": "13vbn5u4KZbwdoU-cof4SpWaSRYI6GCjV",
    "Papers/Paper_Kappa_AB_v10_17_2.md": "1p3GeEnQi7ljlL6I-chN-HHZZXR_ZIggy",
    "Papers/Paper_OctonionExtension_v10_9.md": "1uSoJeIwnsa7luWvHHHFDz_SxhjdSBhn6",
    "Papers/Paper_Popular_v10_8_Full_Edition.md": "115aOQInM0s7WFA4GPRtVs5ljUh72ONJH",
    "Papers/Paper_S2_v1_0_Consolidation_20260525.md": "",
    "Papers/Paper_S2_Pedagogical_Pivot_v1_0_20260530.md": "1COPAku3QGT4uSwzNsNHO4R6GDLONaEDV",
    "Papers/Paper_Kappa_AB_Pedagogical_Pivot_v1_0_20260530.md": "1i10lETyZVDBuBD_2m35F8-6dlYd3HrAC",
    "Papers/Paper_External_Empirical_Surface_Clean_Gates_Pedagogical_Pivot_v1_0_20260530.md": "1FdsM83L2z9faCg0epy8GR7MDFpVZX6XB",
    "Papers/Companion_7_Neutrino_v10_17_2.md": "1rrBbRgY-QUcJz4bIi4QF38ODRQyPyF2J",
    "Papers/Companion_11_Lambda_Unimodular_Closure_v10_17_2.md": "1vpmoYs6AMEMSPEHbMfHY4IMnBNRBIR_f",
    "Papers/Companion_12_Spectral_Chord_Closure_v10_17_2.md": "1mogZdQI5npkfrD2WRqnWYzqvfzgFav7d",
    "Papers/Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md": "1E_Flis1APeYDXefOl_YTp57mIEsm0Uza",
    "Papers/NTE_v10_17_Part1_Foundations.md": "1OoHqvk2B7yAiL9Lm3UkELdPmUvtiKXLi",
    "Papers/NTE_v10_17_Part2_Structure.md": "1FAH18ssZbv8iNTlnhjeNOfRYsk0Qvq-E",
    "Papers/NTE_v10_17_Part3_Accounting.md": "",
    "Working/NTE_Pedagogical_Pivot_Companions_Register.md": "1R7Wo4oY7wb17Z5me8RS8VsyudYD2bnss",
    "Book/Chapter_12_The_Chord_v3_1.md": "1SFEhBwkMQ06aBN2vX5aboO817RpDAMs7",
    "Book/Chapter_10_The_Silvered_Boundary_v6.md": "1Y7xe8kyV3AeHuGbuoQb4q2XTKuuxA2PT",
    "Book/Chapter_15_The_Score_v2.md": "1BInbM4if7eesRQtyZqIDefEfniMybspC",
    "Book/Prelude_The_Forty_Million_Year_Instant_v5.md": "1o74wLHzsHnHKT3MlEFlSf_vdVag-IQB-",
    "Book/Appendix_A_NTE_Popular_Paper_Reader_Edition.md": "1YcsIinXxfQGJkaofbpGAlqwnMGD2OBmC",
}

DRIVE_ID_RE = re.compile(r"\b(1[A-Za-z0-9_-]{20,})\b")
VERSION_RE = re.compile(r"v\d+(?:_\d+)*(?:\.\d+)?", re.I)

SCAN_DIRS = [
    (ROOT / "Papers", "Papers"),
    (ROOT / "Working", "Working"),
    (ROOT / "Handoffs", "Handoffs"),
    (ROOT / "Workflow", "Workflow"),
    (BOOK, "Book"),
]


def one_line_description(path: Path, rel: str) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")[:4000]
    except OSError:
        return ""
    for line in text.splitlines()[:40]:
        line = line.strip()
        if line.startswith("title:"):
            return line.split("title:", 1)[1].strip().strip('"')
        if line.startswith("# ") and "INDEX" not in line.upper():
            return line[2:].strip()[:120]
        if line.startswith("**") and len(line) < 120:
            return line.strip("* ")[:120]
    return path.stem.replace("_", " ")[:80]


def status_flag(rel: str) -> str:
    if "depreciated" in rel or "depreciated" in rel:
        return "superseded"
    if rel.startswith("Working/AC_Readable_Splits/"):
        return "split-mirror"
    if rel.startswith("Handoffs/"):
        return "handoff"
    if rel.endswith(".py"):
        return "worksheet"
    return "canonical"


def scan_file(path: Path, folder: str) -> dict:
    rel = f"{folder}/{path.name}" if folder else path.name
    rel_posix = rel.replace("\\", "/")
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")
    ext = path.suffix.lstrip(".") or "unknown"
    versions = VERSION_RE.findall(path.name)
    version = versions[-1] if versions else ""
    drive_id = KNOWN_DRIVE_IDS.get(rel_posix, "")
    return {
        "drive_id": drive_id,
        "filename": path.name,
        "path": rel_posix,
        "type": ext,
        "description": one_line_description(path, rel_posix),
        "last_modified": mtime,
        "version": version,
        "status": status_flag(rel_posix),
    }


def collect_entries() -> list[dict]:
    entries: list[dict] = []
    for base, label in SCAN_DIRS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if "depreciated" in path.parts:
                continue
            if path.suffix.lower() not in {".md", ".json", ".py", ".pdf"}:
                continue
            if path.name in {"desktop.ini", ".DS_Store"}:
                continue
            entries.append(scan_file(path, label))
    return entries


def render_md(entries: list[dict], generated: str) -> str:
    lines = [
        "---",
        'title: "NTE File Reference Index (AC)"',
        'author: "Cursor Main"',
        f'date: "{generated}"',
        "---",
        "",
        f"**Generated/refreshed at:** {generated} UTC",
        "",
        "**Purpose:** Drive ID + metadata pointer index for AC gatekeeping reach. Regenerate via `Working/build_ac_file_reference_index.py`.",
        "",
        "**Corpus roots:** NTE `1n6RXMzYYZO6tnSCJOMB14DVCKikEPxNs` · Book `1bZkfhlTwx96ApLn3y9tWGr8YyVp5RMSb`",
        "",
        "**Companion indexes:** `Papers/NTE_Corpus_Papers_Index.md` (reader abstracts) · `Working/AC_Readable_Splits/INDEX_AC_Readable_Splits.json`",
        "",
    ]
    by_section: dict[str, list[dict]] = {}
    for e in entries:
        section = e["path"].split("/")[0]
        by_section.setdefault(section, []).append(e)

    order = ["Papers", "Book", "Working", "Workflow", "Handoffs"]
    for section in order:
        group = by_section.get(section, [])
        if not group:
            continue
        lines.append(f"## {section}/ ({len(group)} files)")
        lines.append("")
        lines.append("| Drive ID | File | Description | Modified | Status |")
        lines.append("|----------|------|-------------|----------|--------|")
        for e in group[:200]:  # cap per section for usability
            did = e["drive_id"] or "*(local — ID TBD)*"
            desc = e["description"].replace("|", "/")[:60]
            lines.append(f"| `{did}` | `{e['filename']}` | {desc} | {e['last_modified']} | {e['status']} |")
        if len(group) > 200:
            lines.append(f"| … | *{len(group)-200} more* | see JSON | | |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("— Cursor Main. Mechanical index; extend `KNOWN_DRIVE_IDS` as Drive IDs are confirmed.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    entries = collect_entries()
    payload = {
        "generated_at": generated,
        "author": "Cursor Main",
        "corpus_root_drive_id": "1n6RXMzYYZO6tnSCJOMB14DVCKikEPxNs",
        "book_root_drive_id": "1bZkfhlTwx96ApLn3y9tWGr8YyVp5RMSb",
        "maintenance": "Run Working/build_ac_file_reference_index.py after renames/supersedes; extend KNOWN_DRIVE_IDS",
        "entry_count": len(entries),
        "entries": entries,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_md(entries, generated), encoding="utf-8")
    print(f"Wrote {len(entries)} entries -> {OUT_MD.name}, {OUT_JSON.name}")


if __name__ == "__main__":
    main()
