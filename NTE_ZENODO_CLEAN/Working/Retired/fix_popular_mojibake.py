#!/usr/bin/env python3
"""Repair UTF-8 mojibake in Paper_Popular_v10_8_Full_Edition.md."""
from pathlib import Path

SRC = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers\Paper_Popular_v10_8_Full_Edition.md")
BAK = SRC.with_suffix(".md.mojibake_bak")
LOG = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_popular_fix_log.txt")

BYTE_REPLACEMENTS = [
    (b"\xc3\xa2\xe2\x82\xac\xe2\x80\x9d", b"\xe2\x80\x94"),
    (b"\xc3\xa2\xe2\x82\xac\xe2\x80\x9c", b"\xe2\x80\x93"),
    (b"\xc3\x82\xc2\xb7", b"\xc2\xb7"),
    (b"\xc3\x82\xc2\xb0", b"\xc2\xb0"),
    (b"\xc3\x82\xc2\xb1", b"\xc2\xb1"),
    (b"\xc3\x82\xc2\xb2", b"\xc2\xb2"),
    (b"\xc3\x82\xc2\xb3", b"\xc2\xb3"),
    (b"\xc3\x82\xc2\xb9", b"\xc2\xb9"),
    (b"\xc3\x82\xc2\xa7", b"\xc2\xa7"),
    (b"\xc3\x83\xe2\x80\x94", b"\xc3\x97"),
    (b"\xc3\x83\xc2\xa4", b"\xc3\xa4"),
    (b"\xc3\xa2\xe2\x80\xb0\xcb\x9c", b"\xe2\x89\x88"),
    (b"\xc3\xa2\xcb\x86\x9a", b"\xe2\x88\x9a"),
    (b"\xc3\xa2\xcb\x86\xc5\xa1", b"\xe2\x88\x9a"),
    (b"\xc3\xa2\xcb\x86\x92", b"\xe2\x88\x92"),
    (b"\xc3\xa2\xcb\x86\xe2\x80\x99", b"\xe2\x88\x92"),
    (b"\xc3\xa2\xe2\x86\x92", b"\xe2\x86\x92"),
    (b"\xc3\xa2\xe2\x80\xa0\xe2\x80\x99", b"\xe2\x86\x92"),
    (b"\xc3\x8e\xc2\xa6", b"\xce\xa6"),
    (b"\xc3\x8e\xc2\xb2", b"\xce\xb2"),
    (b"\xc3\x8e\xc2\xba", b"\xce\xba"),
    (b"\xc3\x8e\xc2\xbb", b"\xce\x9b"),
    (b"\xc3\x8e\xe2\x80\xba", b"\xce\x9b"),
    (b"\xc3\x8e\xe2\x80\x9d", b"\xce\x94"),
    (b"\xc3\x8e\xc2\xb4", b"\xce\xb4"),
    (b"\xc3\x8e\xc2\xb8", b"\xce\xb8"),
    (b"\xc3\x8e\xc2\xbd", b"\xce\xbd"),
    (b"\xc3\x8e\xc2\xb1", b"\xce\xb1"),
    (b"\xc3\x8e\xc2\xb7", b"\xce\xb7"),
    (b"\xc3\x8f\xe2\x82\xac", b"\xcf\x80"),
    (b"\xc3\x8f\xc6\x92", b"\xcf\x83"),
    (b"\xc3\xa2\xe2\x80\x9a\xe2\x80\x9a", b"\xe2\x82\x82"),
    (b"\xc3\xa2\xe2\x80\x9a\xc2\x82", b"\xe2\x82\x82"),
    (b"\xc3\xa2\xe2\x80\x9a\xc2\x81", b"\xe2\x82\x81"),
    (b"\xc3\xa2\xe2\x80\x9a\xc2\xac", b"\xe2\x82\x80"),
    (b"\xc3\xa2\xe2\x80\x9a\xe2\x82\xac", b"\xe2\x82\x80"),
    (b"\xc3\xa2\xe2\x80\x9a\xc6\x92", b"\xe2\x82\x83"),
    (b"\xc3\xa2\x81\xc2\xbb", b"\xe2\x81\xbb"),
    (b"\xc3\xa2\x81\xc2\xb0", b"\xe2\x81\xb0"),
    (b"\xc3\xa2\x81\xc2\xb9", b"\xe2\x81\xb9"),
    (b"\xc3\xa2\x81\xc2\xbb\xb3", b"\xe2\x81\xbb\xb3"),
    (b"\xc3\xa2\xe2\x80\x9e\xc2\xac", b"\xe2\x84\x82"),
    (b"\xc3\xa2\xe2\x80\x9e\xe2\x80\x9a", b"\xe2\x84\x82"),
    # superscript corruption (â» → ⁻ etc.)
    (b"\xc3\xa2\xc2\x81\xc2\xbb", b"\xe2\x81\xbb"),
    (b"\xc3\xa2\xc2\x81\xc2\xb9", b"\xe2\x81\xb9"),
    (b"\xc3\xa2\xc2\x81\xc2\xb0", b"\xe2\x81\xb0"),
    # bra-ket / angle brackets
    (b"\xc3\xa2\xc5\xb8\xc2\xa8", b"\xe2\x9f\xa8"),
    (b"\xc3\xa2\xc5\xb8\xc2\xa9", b"\xe2\x9f\xa9"),
    (b"\xc3\x8f\xcb\x86", b"\xcf\x88"),  # Ïˆ → ψ
    (b"\xc3\x8f\xe2\x80\xa0", b"\xcf\x86"),  # Ï† → φ
    (b"\xc3\x8f\xc2\x88", b"\xcf\x88"),
    (b"\xc3\x8f\xc2\x86", b"\xcf\x86"),
]

TEXT_REPLACEMENTS = [
    ("H\u00e2\u201a\u20ac", "H\u2080"),
    ("\u03ba\u00e2\u201a\u20ac", "\u03ba\u2080"),
    ("\u00ce\u203a", "\u039b"),
    ("\u00ce\u201dm", "\u0394m"),
    ("\u00ce\u201d", "\u0394"),
    ("\u00e2\u2030\u02c6", "\u2248"),
    ("\u00e2\u02c6\u0161", "\u221a"),
    ("2\u00e2\u02c6\u01612", "2\u221a2"),
    ("\u00e2\u02c6\u2019", "\u2212"),
    ("\u00e2\u2020\u2019", "\u2192"),
    ("\u00e2\u201e\u201a", "\u2102"),
    ("^{\u00e2\u02c6\u20191/3}", "^{\u22121/3}"),
    ("(1\u00e2\u02c6\u2019", "(1\u2212"),
    ("1\u00e2\u02c6\u2019", "1\u2212"),
]

BAD_MARKERS = ["\u00e2\u20ac", "\u00ce\u203a", "\u00e2\u2030", "\u00e2\u02c6", "\u00e2\u2020", "\u00e2\u201a\u20ac", "\u00e2\u201e", "\u00cf\u02c6", "\u00cf\u2020"]


def fix_bytes(data: bytes) -> bytes:
    ordered = sorted({p[0]: p for p in BYTE_REPLACEMENTS}.values(), key=lambda x: -len(x[0]))
    for old, new in ordered:
        data = data.replace(old, new)
    return data


def fix_text(text: str) -> str:
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> None:
    raw = BAK.read_bytes() if BAK.exists() else SRC.read_bytes()
    fixed = fix_text(fix_bytes(raw).decode("utf-8"))
    rem = {m: fixed.count(m) for m in BAD_MARKERS if m in fixed}
    SRC.write_text(fixed, encoding="utf-8", newline="\n")
    lines = [f"remaining: {rem}", f"em_dash: {fixed.count(chr(0x2014))}"]
    for line in fixed.splitlines()[:20]:
        if "Popular Paper" in line or "Sync note" in line:
            lines.append(line)
    LOG.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
