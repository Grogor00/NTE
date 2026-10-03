#!/usr/bin/env python3
"""Prepare standalone NTE paper markdown for publication PDF export."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)

METADATA_PREFIXES = (
    "**Publication programme:**",
    "**Version:**",
    "**Stream:**",
    "**Programme:**",
    "**Master corpus",
    "**Companion papers:**",
    "**Predecessor:**",
    "**Ratification lineage**",
    "**Status:**",
    "**Author:**",
    "**Date:**",
    "**Bidirectional pattern",
    "**Edition discipline:**",
    "**NTE v10",
    "**v10.",
    "**Companion to the NTE",
)

EDITION_BLOCKQUOTE = re.compile(
    r"^>\s*\*\*(?:NTE Popular Paper|Edition discipline|This is not the)",
    re.I,
)
INTERNAL_BLOCKQUOTE = re.compile(
    r"^>\s.*(?:Paper_Popular|Appendix_A_|do not treat|interchangeable filenames)",
    re.I,
)
SHIP_NOTE = re.compile(r"^\*v[\d.]+\s+ship note", re.I)
KAPPA_MERGE = re.compile(r"^\*\*NTE v10\.\d+ Technical Paper\*\*", re.I)
WORKING_DRAFT = re.compile(r"^\s*Working Draft\s+[—\-]", re.I)
DUPLICATE_H1 = re.compile(r"^#\s+")
RATIFICATION_BULLET = re.compile(r"^-\s+(?:Scoping|v0\.|v1\.|\*\*v)", re.I)
PROGRAMME_TITLE_RE = re.compile(
    r"^(Paper S\d+(?: v[\d.]+)?)\s*[—–-]\s*(.+)$",
    re.S,
)


def split_programme_label_frontmatter(fm: str, scratch_path: Path) -> str:
    """Put 'Paper S2' (etc.) in \\doclabel above the descriptive title for PDF."""
    m = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    if not m:
        return fm
    title = m.group(1).replace('\\"', '"')
    pm = PROGRAMME_TITLE_RE.match(title)
    if not pm:
        return fm

    label = pm.group(1)
    rest = pm.group(2).replace('"', '\\"')
    sidecar = scratch_path.with_suffix(".doclabel.tex")
    sidecar.write_text(f"\\doclabel{{{label}}}\n", encoding="utf-8", newline="\n")

    lines = fm.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        if line.startswith("title:"):
            out.append(f'title: "{rest}"\n')
            continue
        if line.startswith("header-includes:"):
            continue
        if line.strip().startswith("- '\\doclabel") or line.strip().startswith('- "\\doclabel'):
            continue
        out.append(line)
    return "".join(out)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    m = FM_RE.match(text)
    if not m:
        return None, text
    return m.group(0), text[m.end() :]


def is_affiliation_line(line: str) -> bool:
    s = line.strip()
    return bool(
        re.match(r"^\*Independent Researcher", s, re.I)
        or re.match(r"^\*Email:", s, re.I)
        or re.match(r"^\*Full title:\*", s, re.I)
    )


def is_subtitle_line(line: str) -> bool:
    s = line.strip()
    if not s.startswith("*") or not s.endswith("*"):
        return False
    if is_affiliation_line(line):
        return False
    if SHIP_NOTE.match(s) or KAPPA_MERGE.match(s):
        return False
    return len(s) < 220


def is_metadata_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if EDITION_BLOCKQUOTE.match(s) or INTERNAL_BLOCKQUOTE.match(s):
        return True
    if s.startswith(">") and (
        "NTE Popular" in s
        or "Full Edition" in s
        or "Reader Edition" in s
        or "Appendix_A" in s
        or "Paper_Popular" in s
    ):
        return True
    if any(s.startswith(p) for p in METADATA_PREFIXES):
        return True
    if SHIP_NOTE.match(s) or KAPPA_MERGE.match(s):
        return True
    if WORKING_DRAFT.match(s):
        return True
    if RATIFICATION_BULLET.match(s):
        return True
    if s.startswith("*Bare Coupling") and "Pathway" in s:
        return True
    return False


def body_start_index(lines: list[str], start: int) -> int:
    i = start
    while i < len(lines):
        s = lines[i].strip()
        if not s or s == "---":
            i += 1
            continue
        if is_metadata_line(lines[i]) or s.startswith(">"):
            i += 1
            continue
        if s.startswith("## ") or (s.startswith("# ") and i > start):
            return i
        if len(s) > 40 and not s.startswith("**"):
            return i
        i += 1
    return start


def strip_author_head(body: str, yaml_title: str | None) -> str:
    lines = body.splitlines(keepends=True)
    i = 0
    kept: list[str] = []

    while i < len(lines) and not lines[i].strip():
        i += 1

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            if kept and i + 1 < len(lines) and (
                is_affiliation_line(lines[i + 1])
                or is_subtitle_line(lines[i + 1])
            ):
                kept.append(lines[i])
                i += 1
                continue
            break
        if s == "---":
            break
        if is_affiliation_line(lines[i]) or is_subtitle_line(lines[i]):
            kept.append(lines[i])
            i += 1
            continue
        break

    start = body_start_index(lines, i)
    if yaml_title and start < len(lines):
        h1 = lines[start].strip()
        if DUPLICATE_H1.match(h1):
            title_norm = re.sub(r"\s+", " ", yaml_title).strip().lower()
            h1_norm = re.sub(r"^#\s+", "", h1).strip().lower()
            if title_norm == h1_norm or h1_norm in title_norm or title_norm in h1_norm:
                start += 1
                while start < len(lines) and lines[start].strip() in ("", "---"):
                    start += 1

    tail = lines[start:]
    while tail and tail[0].strip() in ("", "---"):
        tail = tail[1:]

    head = "".join(kept).rstrip()
    body_text = "".join(tail).lstrip("\n")
    if head and body_text:
        out = head + "\n\n" + body_text
    else:
        out = head + body_text
    out = re.sub(r"\n---\n---\n", "\n---\n", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.lstrip("\n")


def legacy_to_yaml(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("# "):
        return text

    title = lines[0].strip()[2:].strip()
    abstract_idx = next(
        (i for i, line in enumerate(lines) if line.strip().startswith("## Abstract")),
        None,
    )
    if abstract_idx is None:
        return text

    author = "G. White"
    date = "2026"
    for line in lines[1:abstract_idx]:
        s = line.strip()
        if s.startswith("**Author:**"):
            author = s.split(":", 1)[1].strip()
        if s.startswith("**Date:**"):
            date = s.split(":", 1)[1].strip()

    body = "".join(lines[abstract_idx:])
    esc = title.replace('"', '\\"')
    front = (
        "---\n"
        f'title: "{esc}"\n'
        f'author: "{author}"\n'
        f'date: "{date}"\n'
        "---\n\n"
    )
    return front + body


def prepare_paper(text: str, path: Path) -> str:
    from strip_corpus_metadata import strip_corpus_metadata
    from strip_publication_tail import strip_publication_tail

    name = path.name
    if name.startswith("NTE_v10_17_Part"):
        return text

    if not text.lstrip().startswith("---"):
        text = legacy_to_yaml(text)

    fm, body = split_frontmatter(text)
    if fm:
        fm = split_programme_label_frontmatter(fm, path)
    yaml_title = None
    if fm:
        m = re.search(r'^title:\s*"(.*)"', fm, re.M)
        if m:
            yaml_title = m.group(1).replace('\\"', '"')

    body = strip_author_head(body, yaml_title)
    body, _ = strip_publication_tail(body)
    body = strip_corpus_metadata(body)
    text = (fm or "") + body
    return text.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare NTE standalone paper markdown for PDF export."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    out = prepare_paper(text, args.path)
    out_path = args.output or args.path
    out_path.write_text(out, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
