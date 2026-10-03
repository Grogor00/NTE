#!/usr/bin/env python3
"""Restructure NTE master trilogy markdown for publication PDF export."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PART1_TITLE = (
    "Boundary-Only Extension to the Standard Model from CPN-Symmetric "
    "Nucleation on S³, with Zero-Parameter Dark Matter Prediction, "
    "Geometric Neutrino Oscillation, Octonionic Gauge Group Derivation, "
    "and Spectral Index from α"
)
PART1_SUBTITLE = (
    "Non-Temporal Emergence (NTE): The Null-Time Extension to the "
    "Standard Model — with E-Fold–Proportional Temporal Coordinate"
)

HEAD_DROP_PATTERNS = (
    re.compile(r"^\*\*Naming discipline \(Greg-ratified", re.I),
    re.compile(r"^Programme S Paper S2", re.I),
    re.compile(r"^\*\*Language note \(v10", re.I),
    re.compile(r"^New in v10\.", re.I),
    re.compile(r"^Table of Contents\s*$", re.I),
)

LANGUAGE_NOTE_SENTENCE = re.compile(
    r"\s*See the language note at the end of this abstract\.?\s*",
    re.I,
)

PART_HEADER_RE = re.compile(
    r"^\s*>\s*\*\*NTE[^—]*—\s*(Part\s+\d+\s+of\s+3[^\*]*)\*\*\s*$",
    re.I,
)


def yaml_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def yaml_block(text: str, indent: str = "  ") -> str:
    lines = text.strip().splitlines()
    if not lines:
        return indent + '""'
    out = []
    for line in lines:
        out.append(f'{indent}{line}')
    return "\n".join(out)


def parse_part_header(lines: list[str]) -> tuple[str | None, int]:
    """Return (part label for running header, index after blockquote)."""
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines):
        return None, 0

    m = PART_HEADER_RE.match(lines[i])
    if not m:
        return None, i

    part_label = m.group(1).strip()
    i += 1
    while i < len(lines) and (lines[i].startswith(">") or not lines[i].strip()):
        i += 1
    return part_label, i


def collect_abstract(lines: list[str], start: int, end: int) -> str:
    chunks: list[str] = []
    for line in lines[start:end]:
        stripped = line.strip()
        if not stripped:
            if chunks and chunks[-1] != "":
                chunks.append("")
            continue
        if any(p.match(stripped) for p in HEAD_DROP_PATTERNS):
            break
        if stripped.startswith("**Language note"):
            break
        if stripped.startswith("Programme S Paper"):
            break
        chunks.append(stripped)

    while chunks and chunks[-1] == "":
        chunks.pop()
    text = "\n".join(chunks)
    text = LANGUAGE_NOTE_SENTENCE.sub(" ", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"  +", " ", text)
    text = re.sub(r"\n +", "\n", text)
    return text.strip()


def find_body_start(lines: list[str], start: int) -> int:
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        if re.match(r"^[IVX]+\.\s+[A-Z]", stripped):
            return i
        if re.match(r"^XVII\.\s+", stripped):
            return i
    return start


def build_frontmatter(
    *,
    title: str,
    subtitle: str | None,
    part_header: str,
    abstract: str | None = None,
    titlepage: bool = True,
) -> str:
    lines = [
        "---",
        f'title: "{yaml_escape(title)}"',
    ]
    if subtitle:
        lines.append(f'subtitle: "{yaml_escape(subtitle)}"')
    lines.extend(
        [
            'author: "G. White"',
            'date: "April 2026"',
        ]
    )
    if not titlepage:
        lines.append("titlepage: false")
    if abstract:
        lines.append("abstract: |")
        lines.append(yaml_block(abstract, indent="  "))
    lines.append("header-includes:")
    lines.append(f"  - '\\renewcommand{{\\masterpartheader}}{{{part_header}}}'")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def prepare_part1(text: str) -> str:
    lines = text.splitlines()
    part_label, idx = parse_part_header(lines)
    part_header = (part_label or "Part 1 of 3 · Foundations + Method").replace(
        ": ", " · ", 1
    )

    abstract_idx = next(
        (i for i, line in enumerate(lines) if line.strip().upper() == "ABSTRACT"),
        None,
    )
    if abstract_idx is None:
        raise ValueError("Part 1: ABSTRACT marker not found")

    body_start = find_body_start(lines, abstract_idx + 1)
    abstract = collect_abstract(lines, abstract_idx + 1, body_start)
    body = "\n".join(lines[body_start:]).lstrip() + "\n"

    front = build_frontmatter(
        title=PART1_TITLE,
        subtitle=PART1_SUBTITLE,
        part_header=part_header,
        abstract=abstract,
        titlepage=True,
    )
    return front + body


def prepare_part_other(text: str, default_title: str, default_header: str) -> str:
    lines = text.splitlines()
    part_label, idx = parse_part_header(lines)
    part_header = (part_label or default_header).replace(": ", " · ", 1)
    title = part_header if part_label else default_title
    body = "\n".join(lines[idx:]).lstrip() + "\n"

    front = build_frontmatter(
        title=title,
        subtitle="Non-Temporal Emergence (NTE) — Master Corpus",
        part_header=part_header,
        abstract=None,
        titlepage=False,
    )
    return front + body


def prepare_master(text: str, path: Path) -> str:
    from strip_corpus_metadata import strip_corpus_metadata

    name = path.name.lower()
    if "part1" in name:
        out = prepare_part1(text)
    elif "part2" in name:
        out = prepare_part_other(
            text,
            "Part 2 of 3: Structure + Dynamics",
            "Part 2 of 3 · Structure + Dynamics",
        )
    elif "part3" in name:
        out = prepare_part_other(
            text,
            "Part 3 of 3: Accounting + Appendices",
            "Part 3 of 3 · Accounting + Appendices",
        )
    else:
        return text
    return strip_corpus_metadata(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare NTE master trilogy markdown for PDF export."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    if not args.path.name.startswith("NTE_v10_17_Part"):
        out = text
    else:
        out = prepare_master(text, args.path)

    out_path = args.output or args.path
    out_path.write_text(out, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
