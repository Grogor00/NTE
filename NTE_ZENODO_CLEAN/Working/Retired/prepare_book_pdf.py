#!/usr/bin/env python3
"""Prepare Book chapter markdown for publication PDF export."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

INNER_FM_RE = re.compile(
    r"^(---\s*\n(?:title:|author:|date:).*?\n---\s*\n)(.*)",
    re.S | re.M,
)
SUBTITLE_LINE = re.compile(
    r"^\*(The Null-Time Extension to the Standard Model[^\n*]+)\*\s*$",
    re.M,
)


def inject_yaml_subtitle(fm: str, subtitle: str) -> str:
    if "subtitle:" in fm:
        return fm
    esc = subtitle.replace('"', '\\"')
    lines = fm.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        out.append(line)
        if line.startswith("date:"):
            out.append(f'subtitle: "{esc}"\n')
    return "".join(out)


def prepare_appendix_a(text: str) -> str:
    """Appendix A embeds Popular Reader Edition with a workshop header — strip for PDF."""
    from prepare_paper_pdf import strip_author_head
    from strip_corpus_metadata import strip_corpus_metadata
    from strip_publication_tail import strip_publication_tail

    m = INNER_FM_RE.search(text)
    if not m:
        return text

    fm, body = m.group(1), m.group(2)

    yaml_title = None
    tm = re.search(r'^title:\s*"(.*)"', fm, re.M)
    if tm:
        yaml_title = tm.group(1).replace('\\"', '"')

    sm = SUBTITLE_LINE.search(body)
    if sm:
        fm = inject_yaml_subtitle(fm, sm.group(1))
        body = body[: sm.start()] + body[sm.end() :]

    body = strip_author_head(body, yaml_title)
    body, _ = strip_publication_tail(body)
    body = strip_corpus_metadata(body)

    return fm.rstrip() + "\n\n" + body.lstrip("\n")


def prepare_appendix_b(text: str) -> str:
    """Strip workshop-only tails from Appendix B for PDF."""
    from strip_corpus_metadata import strip_corpus_metadata
    from strip_publication_tail import strip_publication_tail

    lines = text.splitlines(keepends=True)
    # Drop book wrapper through first ---; keep from intro paragraph onward.
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            start = i + 1
            break
    body = "".join(lines[start:]).lstrip("\n")
    body, _ = strip_publication_tail(body)
    body = strip_corpus_metadata(body)
    return body


def prepare_book(text: str, path: Path) -> str:
    if path.name.startswith("Appendix_A_"):
        return prepare_appendix_a(text)
    if path.name.startswith("Appendix_B_"):
        return prepare_appendix_b(text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare Book chapter markdown for PDF export."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    out = prepare_book(text, args.path)
    out_path = args.output or args.path
    out_path.write_text(out, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
