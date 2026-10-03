#!/usr/bin/env python3
"""Build Book/Appendix A from canonical Popular Paper Reader Edition (strip workshop tail)."""
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")
POPULAR = Path(
    r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Reader_Edition.md"
)
OUT = BOOK / "Appendix_A_NTE_Popular_Paper_Reader_Edition.md"

HEADER = """# The Shape of Time

# Appendix A — Popular Paper, Reader Edition (NTE v10.8)

*Non-Temporal Emergence (NTE): the Null-Time Extension to the Standard Model*

G. White

---

This appendix is **not** the full corpus Popular Paper. It reproduces the **Reader Edition** only:

| Edition | File | Role |
|---------|------|------|
| **Reader Edition (this appendix)** | `Paper_Popular_v10_8_Reader_Edition.md` | ~4,800 words; recap after the chapters |
| **Full Edition (corpus)** | `Paper_Popular_v10_8_Full_Edition.md` | ~13,000 words; complete corpus lay paper |

Same framework and predictions; different length and purpose. Technical proofs and companion papers: **Appendix B**.

**Source of truth for this appendix:** `NTE v10_6/Papers/Paper_Popular_v10_8_Reader_Edition.md`

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
    body = POPULAR.read_text(encoding="utf-8")
    body = strip_workshop_tail(body)
    OUT.write_text(HEADER + body, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.name} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
