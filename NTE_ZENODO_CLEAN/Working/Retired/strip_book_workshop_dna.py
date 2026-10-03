#!/usr/bin/env python3
"""Remove workshop editorial tails from reader-facing Book/*.md files."""
import re
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")
SKIP = {"depreciated"}
# Appendix B is reader-facing index; Appendix A built without tail if script used
MARKERS = (
    "## Editorial notes for revision",
    "## Editorial notes",
    "## Editorial notes on",
    "*Notes for the author, not part of",
)


def strip_tail(text: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    cut = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if any(stripped.startswith(m) for m in MARKERS):
            cut = i
            break
        # Also cut at horizontal rule before editorial block
        if stripped == "---" and i + 2 < len(lines):
            look = "".join(lines[i + 1 : i + 4])
            if any(m in look for m in MARKERS):
                cut = i
                break
    if cut is None:
        return text, False
    return "".join(lines[:cut]).rstrip() + "\n", True


def main():
    changed = []
    for path in sorted(BOOK.glob("*.md")):
        if path.parent.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        new, did = strip_tail(text)
        if did and new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path.name)
    print(f"Stripped {len(changed)} files:")
    for n in changed:
        print(f"  {n}")


if __name__ == "__main__":
    main()
