#!/usr/bin/env python3
"""Apply The Shape of Time front matter to Book chapters in place."""
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")

NTE_BLOCK = (
    "*Non-Temporal Emergence (NTE): the Null-Time Extension to the Standard Model*\n\n"
    "G. White\n\n"
)


def has_book_title(text: str) -> bool:
    for line in text.splitlines()[:6]:
        s = line.strip()
        if s in ("# The Shape of Time", "# **THE SHAPE OF TIME**"):
            return True
    return False


def has_nte_block(text: str) -> bool:
    return "Non-Temporal Emergence (NTE)" in text[:1500]


def find_chapter_h1_index(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("# Chapter ") or s.startswith("# Prelude"):
            return i
    return None


def insert_nte_after_h1(lines: list[str]) -> list[str]:
    idx = find_chapter_h1_index(lines)
    if idx is None:
        return lines
    out = lines[: idx + 1]
    j = idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    out.append("\n")
    out.append(NTE_BLOCK)
    out.append("---\n\n")
    out.extend(lines[j:])
    return out


def process_prelude(text: str) -> str:
    if has_book_title(text) and has_nte_block(text):
        return text

    lines = text.splitlines(keepends=True)
    while lines and lines[0].strip() == "":
        lines = lines[1:]

    idx = find_chapter_h1_index(lines)
    if idx is None:
        return text

    prelude_h1 = lines[idx]
    body = lines[idx + 1 :]

    new_lines = [
        "# The Shape of Time\n\n",
        "G. White\n\n",
        NTE_BLOCK,
        "---\n\n",
        prelude_h1 if prelude_h1.endswith("\n") else prelude_h1 + "\n",
    ]
    new_lines.extend(body)
    return "".join(new_lines)


def process_chapter(text: str) -> str:
    lines = text.splitlines(keepends=True)
    while lines and lines[0].strip() == "":
        lines = lines[1:]

    if has_book_title(text):
        if has_nte_block(text):
            return text
        return "".join(insert_nte_after_h1(lines))

    idx = find_chapter_h1_index(lines)
    if idx is None:
        return text

    chapter_h1 = lines[idx]
    rest = lines[idx + 1 :]
    new_lines = [
        "# The Shape of Time\n\n",
        chapter_h1 if chapter_h1.endswith("\n") else chapter_h1 + "\n",
        "\n",
        NTE_BLOCK,
        "---\n\n",
    ]
    new_lines.extend(rest)
    return "".join(new_lines)


def main():
    updated = []
    for path in sorted(BOOK.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        original = text
        if path.name.lower().startswith("prelude"):
            text = process_prelude(text)
        else:
            text = process_chapter(text)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            updated.append(path.name)

    print("Updated:", len(updated))
    for n in updated:
        print(" ", n)


if __name__ == "__main__":
    main()
