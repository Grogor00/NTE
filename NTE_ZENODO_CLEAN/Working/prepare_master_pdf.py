#!/usr/bin/env python3
"""Prepare NTE master trilogy markdown for publication PDF export (v10.18+ YAML form)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from strip_corpus_metadata import strip_corpus_metadata
from strip_publication_tail import strip_publication_tail

FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)

# Drop standalone process/stamp lines in the head, keep affiliation.
DROP_HEAD_LINE = re.compile(
    r"^\s*(?:"
    r"\*?\[?Working [Dd]raft\b"
    r"|\*Corpus version:"
    r"|\*Part of NTE Corpus"
    r")",
    re.I,
)


def prepare_master(text: str, path: Path) -> str:
    """v10.18+ Parts already carry YAML; strip process stamps only."""
    m = FM_RE.match(text)
    if m:
        fm = m.group(0)
        body = text[m.end() :]
    else:
        fm = ""
        body = text

    lines = body.splitlines(keepends=True)
    kept: list[str] = []
    for line in lines:
        if DROP_HEAD_LINE.match(line.strip()):
            continue
        kept.append(line)
    body = "".join(kept)

    text = fm + body
    text, _ = strip_publication_tail(text)
    text = strip_corpus_metadata(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare NTE master trilogy markdown for PDF export."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    name = args.path.name
    if re.search(r"Part\d", name, re.I) or "Part" in name:
        out = prepare_master(text, args.path)
    else:
        out = text

    out_path = args.output or args.path
    out_path.write_text(out, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
