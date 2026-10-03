#!/usr/bin/env python3
"""Rebuild Book/depreciated/Appendix_A Full Edition archive from Full Edition source."""
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")
FULL = Path(
    r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md"
)
OUT = BOOK / "depreciated" / "Appendix_A_NTE_Popular_Paper_v10_8_v6.md"

RETIRED = """# RETIRED — do not use as Appendix A

This file is an **archived book build** from Popular Paper **Full Edition (v10.8)**.
The live book uses **Reader Edition** only: `../Appendix_A_NTE_Popular_Paper_Reader_Edition.md`.

| Edition | Corpus file |
|---------|-------------|
| Full Edition | `NTE v10_6/Papers/Paper_Popular_v10_8_Full_Edition.md` |
| Reader Edition | `NTE v10_6/Papers/Paper_Popular_v10_8_Reader_Edition.md` |

---

"""

OLD_HEADER = """# The Shape of Time

# Appendix A — The Popular Paper (Full Edition) [RETIRED BUILD]

*Non-Temporal Emergence (NTE): the Null-Time Extension to the Standard Model*

G. White

---

**Superseded.** Book Appendix A is now Reader Edition only.

**Source (Full Edition):** `NTE v10_6/Papers/Paper_Popular_v10_8_Full_Edition.md`

---

"""


def strip_workshop_tail(text: str) -> str:
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("## Editorial") or s.startswith("### Pending Greg"):
            return "".join(lines[:i]).rstrip() + "\n"
        if s == "---" and i + 1 < len(lines):
            nxt = lines[i + 1].strip()
            if nxt.startswith("## Editorial") or nxt.startswith("### Pending Greg"):
                return "".join(lines[:i]).rstrip() + "\n"
    return text


def main():
    body = strip_workshop_tail(FULL.read_text(encoding="utf-8"))
    OUT.write_text(RETIRED + OLD_HEADER + body, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
