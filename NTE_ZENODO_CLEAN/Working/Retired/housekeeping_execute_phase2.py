#!/usr/bin/env python3
"""Execute housekeeping Phase 2 — archive moves per Greg approval 2026-06-19."""
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
MANIFEST = ROOT / "Working" / "_housekeeping_dryrun_manifest.json"
ARCHIVE = ROOT / "Working" / "Archive" / "2026-06-18_cleanup"
EXECUTED = ROOT / "Handoffs" / "Handoff_Cursor_Main_to_AC_Housekeeping_Manifest_EXECUTED_20260619.md"


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    log: list[str] = []
    for c in data["candidates"]:
        src = ROOT / c["path"].replace("\\", "/")
        if not src.exists():
            log.append(f"SKIP missing: {c['path']}")
            continue
        if c["action"] != "ARCHIVE":
            log.append(f"SKIP non-archive: {c['path']}")
            continue
        dst = ARCHIVE / src.name
        shutil.move(str(src), str(dst))
        log.append(f"ARCHIVED {c['path']} -> {dst.relative_to(ROOT)}")

    EXECUTED.write_text(
        "\n".join(
            [
                "# Handoff: Cursor Main → AC — Housekeeping manifest EXECUTED (Phase 2)",
                "",
                "**From:** Cursor Main",
                "**To:** AC",
                "**Cc:** Greg",
                f"**Date:** 2026-06-19",
                "**Authorization:** Greg approved Phase 2 (2026-06-19); dry-run manifest 2026-06-18",
                "",
                "## Executed moves",
                "",
                *[f"- {line}" for line in log],
                "",
                f"**Total archived:** {sum(1 for l in log if l.startswith('ARCHIVED'))}",
                "",
                "— Cursor Main, 2026-06-19.",
            ]
        ),
        encoding="utf-8",
    )
    print("\n".join(log))
    print(f"Wrote {EXECUTED}")


if __name__ == "__main__":
    main()
