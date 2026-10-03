#!/usr/bin/env python3
"""Generate AC-readable splits of oversized NTE corpus markdown files.

Read-mirrors only — canonical masters remain authoritative.
Verifies concatenation equality before writing index.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPLIT_DIR = ROOT / "Working" / "AC_Readable_Splits"
THRESHOLD_BYTES = 122_880  # ~120 KB
TARGET_MAX_BYTES = 100_000  # ~100 KB per part

# Manual section-boundary plans for known oversized canon files
SPLIT_PLANS: dict[str, list[tuple[str, int]]] = {
    "Papers/NTE_v10_17_Part3_Accounting.md": [
        ("A_S17_5", 1),      # header through §17.5.21
        ("B_S18_20", 369),   # §18–§20
        ("C_S22_App", 622),  # §22 through end
    ],
}


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def scan_oversized() -> list[tuple[int, Path]]:
    hits: list[tuple[int, Path]] = []
    for base in (ROOT / "Papers", ROOT / "Working", ROOT / "Book"):
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            if "depreciated" in p.parts or "AC_Readable_Splits" in p.parts:
                continue
            sz = p.stat().st_size
            if sz > THRESHOLD_BYTES:
                hits.append((sz, p))
    return sorted(hits, reverse=True)


def split_file(rel: str, parts: list[tuple[str, int]]) -> dict:
    src = ROOT / rel
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out_parts: list[dict] = []

    for i, (label, start_line) in enumerate(parts):
        start_idx = start_line - 1
        end_idx = (parts[i + 1][1] - 1) if i + 1 < len(parts) else len(lines)
        chunk = "".join(lines[start_idx:end_idx])
        out_name = f"{src.stem}__{label}.md"
        out_path = SPLIT_DIR / out_name
        out_path.write_text(chunk, encoding="utf-8", newline="\n")
        out_parts.append(
            {
                "file": out_name,
                "relative_path": str(out_path.relative_to(ROOT)).replace("\\", "/"),
                "source": rel.replace("\\", "/"),
                "lines": f"{start_line}-{end_idx}",
                "bytes": len(chunk.encode("utf-8")),
                "sha256": sha256(chunk),
            }
        )

    recon = "".join(
        (SPLIT_DIR / p["file"]).read_text(encoding="utf-8") for p in out_parts
    )
    if recon != text:
        raise SystemExit(f"Concatenation mismatch for {rel}")

    return {
        "source": rel.replace("\\", "/"),
        "source_bytes": len(text.encode("utf-8")),
        "source_sha256": sha256(text),
        "parts": out_parts,
        "integrity": "concatenation-equality verified",
    }


def main() -> None:
    SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    oversized = scan_oversized()
    entries: list[dict] = []

    for sz, path in oversized:
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if rel in SPLIT_PLANS:
            entries.append(split_file(rel, SPLIT_PLANS[rel]))
        else:
            entries.append(
                {
                    "source": rel,
                    "source_bytes": sz,
                    "status": "NEEDS_MANUAL_PLAN",
                    "note": "No section split plan defined yet",
                }
            )

    index = {
        "generated": date.today().isoformat(),
        "author": "Cursor Main",
        "discipline": "Read-mirrors of canonical masters only; regenerate after master edits.",
        "threshold_bytes": THRESHOLD_BYTES,
        "target_max_bytes": TARGET_MAX_BYTES,
        "method": "Section-boundary split + SHA-256 per part + full concatenation equality check",
        "drive_ids": "N/A — local Desktop canonical workspace; AC reads relative paths below",
        "oversized_scan": [
            {"source": rel, "bytes": sz}
            for sz, p in oversized
            for rel in [str(p.relative_to(ROOT)).replace("\\", "/")]
        ],
        "splits": entries,
        "maintenance": "Re-run this script after any edit to a split source file.",
    }

    index_path = SPLIT_DIR / "INDEX_AC_Readable_Splits.json"
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")

    md_lines = [
        "# AC-readable corpus splits — index",
        "",
        f"**Generated:** {index['generated']} — **Cursor Main**",
        "",
        "Canonical masters remain authoritative. These parts are byte-faithful read-mirrors for AC gatekeeping sessions that cannot load whole files >~120 KB.",
        "",
        "## Integrity",
        "",
        "- Method: section-boundary split only (never mid-section)",
        "- Check: concatenation of all parts equals canonical source exactly",
        "- Per-part SHA-256 in `INDEX_AC_Readable_Splits.json`",
        "",
        "## Oversized canon files (>120 KB)",
        "",
    ]
    for item in index["oversized_scan"]:
        md_lines.append(f"- `{item['source']}` — {item['bytes'] / 1024:.1f} KB")

    md_lines.extend(["", "## Split parts", ""])
    for entry in entries:
        if entry.get("status") == "NEEDS_MANUAL_PLAN":
            md_lines.append(f"### `{entry['source']}` — **needs manual plan**")
            continue
        md_lines.append(f"### `{entry['source']}` ({entry['source_bytes'] / 1024:.1f} KB)")
        for p in entry["parts"]:
            md_lines.append(
                f"- `{p['relative_path']}` — lines {p['lines']}, {p['bytes'] / 1024:.1f} KB"
            )
        md_lines.append("")

    md_lines.extend(
        [
            "## Maintenance",
            "",
            "After any master edit: `python Working/ac_readable_split_corpus.py`",
            "",
            "— Cursor Main.",
        ]
    )
    (SPLIT_DIR / "INDEX_AC_Readable_Splits.md").write_text(
        "\n".join(md_lines) + "\n", encoding="utf-8"
    )

    print(json.dumps({"ok": True, "splits": len(entries), "index": str(index_path)}, indent=2))


if __name__ == "__main__":
    main()
