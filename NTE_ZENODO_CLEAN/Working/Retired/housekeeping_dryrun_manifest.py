#!/usr/bin/env python3
"""Phase 1 housekeeping dry-run manifest — no moves (AC gate)."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
WORK = ROOT / "Working"
OUT = ROOT / "Handoffs" / "Handoff_Cursor_Main_to_AC_Housekeeping_Manifest_DRYRUN_20260618.md"

PRESERVE = {
    "cursor_task_ledger.json",
    "pdf_sight_config.json",
    "pdf_artifact_gate.py",
    "cursor_grep_gates.py",
}
PRESERVE_PREFIXES = ("supervisor_", "cursor_autonomous_", "CPN_", "PDF_Sight_")
SUPERSEDED_MARKERS = ("SUPERSEDED", "superseded", "_draft_v1", "DRAFT_AC_HELD", "Package_E")


def file_hash(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()[:16]


def main() -> None:
    candidates: list[dict] = []
    # Superseded Working notes
    for p in WORK.glob("*.md"):
        if p.name in PRESERVE:
            continue
        if any(m in p.name for m in SUPERSEDED_MARKERS):
            candidates.append(
                {
                    "path": str(p.relative_to(ROOT)),
                    "size": p.stat().st_size,
                    "action": "ARCHIVE",
                    "reason": "superseded/draft marker in filename; canonical in Papers/ or later note",
                }
            )
    # Tiny stub files in Working
    for p in WORK.rglob("*"):
        if not p.is_file():
            continue
        if p.stat().st_size <= 64 and p.suffix.lower() in {".pdf", ".txt", ".md"}:
            candidates.append(
                {
                    "path": str(p.relative_to(ROOT)),
                    "size": p.stat().st_size,
                    "action": "DELETE",
                    "reason": "≤64B stub (AC whitelist — verify dup exists before execute)",
                }
            )
    # Byte-identical dupes in Working/*.md (simple pairwise)
    md_files = [p for p in WORK.glob("*.md") if p.stat().st_size > 64]
    hashes: dict[str, list[Path]] = {}
    for p in md_files:
        try:
            hashes.setdefault(file_hash(p), []).append(p)
        except OSError:
            pass
    for h, group in hashes.items():
        if len(group) > 1:
            keep = min(group, key=lambda x: len(str(x)))
            for p in group:
                if p != keep:
                    candidates.append(
                        {
                            "path": str(p.relative_to(ROOT)),
                            "size": p.stat().st_size,
                            "action": "DELETE",
                            "reason": f"byte-identical dupe of {keep.relative_to(ROOT)} hash={h}",
                        }
                    )

    archive_n = sum(1 for c in candidates if c["action"] == "ARCHIVE")
    delete_n = sum(1 for c in candidates if c["action"] == "DELETE")
    flag_n = 0

    lines = [
        "# Handoff: Cursor Main → AC — Housekeeping manifest DRY RUN (Phase 1)",
        "",
        "**From:** Cursor Main",
        "**To:** AC",
        "**Date:** 2026-06-18",
        "**Task:** HOUSEKEEPING-DRYRUN",
        "**Phase:** 1 — **NO MOVES OR DELETES**",
        "",
        f"Generated: {datetime.now(timezone.utc).astimezone().isoformat()}",
        "",
        "## Counts",
        f"- ARCHIVE candidates: {archive_n}",
        f"- DELETE candidates (whitelist): {delete_n}",
        f"- FLAG: {flag_n}",
        f"- **Total candidates:** {len(candidates)}",
        "",
        "## Candidates",
        "",
    ]
    for c in sorted(candidates, key=lambda x: (x["action"], x["path"])):
        lines.append(f"- **{c['action']}** `{c['path']}` ({c['size']} B) — {c['reason']}")

    lines.extend(
        [
            "",
            "## AC disposition",
            "Reply ARCHIVE / DELETE / LEAVE per line. Phase 2 executes only after AC sight.",
            "",
            "— Cursor Main, 2026-06-18.",
        ]
    )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (WORK / "_housekeeping_dryrun_manifest.json").write_text(
        json.dumps({"candidates": candidates, "counts": {"archive": archive_n, "delete": delete_n}}, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {OUT} ({len(candidates)} candidates)")


if __name__ == "__main__":
    main()
