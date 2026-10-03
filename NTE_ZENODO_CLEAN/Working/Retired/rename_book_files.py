#!/usr/bin/env python3
"""Rename Book/*.md to include chapter title slugs."""
import re
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")


def slugify(title: str) -> str:
    title = title.strip().strip("*")
    title = title.replace("'", "").replace("'", "")
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"[-\s]+", "_", title.strip())
    return title


def parse_title(text: str, filename: str) -> tuple[str, str] | None:
    for line in text.splitlines()[:12]:
        s = line.strip()
        m = re.match(r"^# Chapter (\d+) — (.+)$", s)
        if m:
            return m.group(1), m.group(2)
        m = re.match(r"^# Prelude — (.+)$", s)
        if m:
            return "Prelude", m.group(1)
    return None


def version_suffix(name: str) -> str:
    """Extract v... from filename after chapter number."""
    base = name.removesuffix(".md")
    if base.startswith("Prelude_"):
        m = re.search(r"_v(\d+(?:_\d+)?)$", base)
        return f"v{m.group(1)}" if m else "v5"
    m = re.search(r"Chapter_\d+_(.+)$", base)
    if not m:
        return ""
    rest = m.group(1)
    # already has title slug: Chapter_13_v4_The_Strange...
    if rest.startswith("v"):
        return rest.split("_")[0] if "_" in rest else rest
    # Chapter_1_v7_3
    vm = re.match(r"(v[\d_]+(?:\s*\(\d+\))?)", rest)
    if vm:
        v = vm.group(1).replace(" ", "").replace("(1)", "_1")
        return v
    return ""


def target_name(path: Path, num: str, title: str) -> str:
    slug = slugify(title)
    ver = version_suffix(path.name)

    if num == "Prelude":
        return f"Prelude_{slug}_{ver}.md"

    # Ch 13 may already include slug
    if slug.lower().replace("_", "") in path.stem.lower().replace("_", ""):
        # normalize version only if needed
        if f"_{slug}_" in path.stem or path.stem.endswith(f"_{slug}"):
            return path.name
        pass

    base = f"Chapter_{num}_{slug}_{ver}"
    return base.replace("__", "_") + ".md"


def main():
    renames = []
    for path in sorted(BOOK.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        parsed = parse_title(text, path.name)
        if not parsed:
            print("SKIP (no title):", path.name)
            continue
        num, title = parsed
        new_name = target_name(path, num, title)
        new_path = path.parent / new_name
        if new_path.name == path.name:
            print("OK:", path.name)
            continue
        if new_path.exists() and new_path != path:
            print("CONFLICT:", path.name, "->", new_name)
            continue
        renames.append((path, new_path))

    for old, new in renames:
        old.rename(new)
        print(f"{old.name} -> {new.name}")

    print(f"\nRenamed {len(renames)} files.")


if __name__ == "__main__":
    main()
