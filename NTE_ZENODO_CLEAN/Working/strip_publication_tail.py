#!/usr/bin/env python3
"""Strip author-only editorial tails and workflow footers for publication PDF builds."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Cut everything from the first matching marker onward.
HEAD_MARKERS = (
    "## Editorial notes for revision",
    "## Editorial notes on",
    "## Editorial notes —",
    "## Editorial notes",
    "## Note on extraction provenance",
    "### Pending Greg",
    "## Accuracy audit",
    "## Desktop draft",
    "## Session notes",
)

AUTHOR_NOTE = "*Notes for the author, not part of"

WORKING_DRAFT_RE = re.compile(
    r"^\s*(?:\*)?\[?Working [Dd]raft\s*[—\-].*$",
    re.MULTILINE,
)


def strip_publication_tail(text: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    cut = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if any(stripped.startswith(m) for m in HEAD_MARKERS):
            cut = i
            break
        if AUTHOR_NOTE in stripped:
            cut = i
            break
        if stripped == "---" and i + 1 < len(lines):
            look = "".join(lines[i + 1 : min(i + 6, len(lines))])
            if any(m in look for m in HEAD_MARKERS) or AUTHOR_NOTE in look:
                cut = i
                break

    changed = cut is not None
    if changed:
        text = "".join(lines[:cut]).rstrip() + "\n"

    cleaned = WORKING_DRAFT_RE.sub("", text).rstrip() + "\n"
    if cleaned != text:
        changed = True
        text = cleaned

    return text, changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Remove editorial/workshop tails before PDF export."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="Markdown file to strip (default: stdin)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output file (default: overwrite input or stdout)",
    )
    args = parser.parse_args()

    if args.path:
        text = args.path.read_text(encoding="utf-8")
        out_path = args.output or args.path
    else:
        text = sys.stdin.read()
        out_path = args.output

    new_text, _ = strip_publication_tail(text)

    if out_path:
        out_path.write_text(new_text, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(new_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
