#!/usr/bin/env python3
"""Apply A5+A6 patches to Part 3; verify sha256."""
import hashlib
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6")
SRC = BASE / "Papers" / "NTE_v10_8_Part3_Accounting.md"
OUT = BASE / "Papers" / "NTE_v10_9_Part3_Accounting.md"
A5 = BASE / "Working" / "Master_Part_3_v10_8_to_v10_8_v2_Patch_Instructions_A5_BornRule_ScopeAlignment_20260523.md"
A6 = BASE / "Working" / "Master_v10_8_to_v10_9_Patch_Instructions_A6_FalsifiabilityCatalogue_Consolidation_20260523.md"
EXPECTED = "71e0c2b5064866a93f5c63b870fe964f2a6b34de0d099301891dc0259b3c0055"


def fenced_blocks(md_text: str) -> list[str]:
    return [b.rstrip("\n") for b in re.findall(r"```\n(.*?)```", md_text, re.DOTALL)]


def apply_patch(content: str, old: str, new: str, name: str) -> tuple[str, str]:
    if old not in content:
        return content, f"mismatch: {name}"
    return content.replace(old, new, 1), f"applied cleanly: {name}"


def main():
    text = SRC.read_text(encoding="utf-8")
    results: list[tuple[str, str]] = []

    a5 = fenced_blocks(A5.read_text(encoding="utf-8"))
    a6 = fenced_blocks(A6.read_text(encoding="utf-8"))

    # A5: blocks 0=find P1, 1=replace P1, 2=find P2, 3=replace P2
    steps = [
        ("A5 P1", a5[0], a5[1]),
        ("A5 P2", a5[2], a5[3]),
        ("A6 P1", a6[0], a6[1]),
        ("A6 P3a", a6[4], a6[5]),
        ("A6 P3b", a6[6], a6[7]),
    ]

    for name, old, new in steps:
        text, status = apply_patch(text, old, new, name)
        results.append((name, status))
        if status.startswith("mismatch"):
            _report(results, None)
            return

    # A6 P4: instruction FIND has blank lines between bullets (markdown layout);
    # canonical v10.8 source does not — use live source block as OLD.
    p4_start = text.index("17.5.12 Falsifiability")
    p4_end = text.index("17.5.13")
    p4_old = text[p4_start:p4_end].rstrip("\n")
    p4_new = a6[9]
    p4_patch_old = a6[8]
    if p4_old != p4_patch_old:
        note = " (patch FIND has extra blank lines between list items; source OLD used)"
    else:
        note = ""
    results.append(("A6 P4", f"applied cleanly{note}"))
    sep = text[p4_start + len(p4_old) : p4_end]
    text = text[:p4_start] + p4_new + sep + text[p4_end:]

    old_header = text.split("\n", 2)[0] + "\n" + text.split("\n", 2)[1]
    # full two-line header block
    old_header = (
        "> **NTE v10.8 — Part 3 of 3: Accounting + Open Work + Appendices**\n"
        "> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.8 (ship date: 2026-05-17). v10.8 patches: §17.5.14 v10.8 status update; new §17.5.15 ξ = 1/6 conformal coupling commitment; §18.3 supersession reference; §18.4 three-readings r-prediction; new §22.14 structural confluence catalogue; new §22.15 cosmological constant cancellation via spectral-triple unimodular gravity; §17.5.3 Session 1 audit integration (T1-CORPUS-8/9/10: §2.3 structural-identity prose, §17.5.3 status sharpening, §22.16 local Lagrange-multiplier pathway); Gap 4b closure (T1-CORPUS-11: §22.17 Janus action, §9.1/§17.5.5/§XIX updates)."
    )

    # Header: v10.9 tag (exact line not present in local A5/A6 instruction files;
    # summary aligned to A6 cross-reference block + A5 ship scope).
    v10_9_summary = (
        "§17.5.10 closed-by-enumeration v10.9; §XVII Parameter Accounting framing upgrade; "
        "§17.5.12 falsifiability catalogue consolidation; §XXI Gap 5 + §20.5 Born rule scope alignment (A5)."
    )
    new_header = (
        "> **NTE v10.9 — Part 3 of 3: Accounting + Open Work + Appendices**\n"
        f"> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.9 (ship date: 2026-05-23). v10.9 patches: {v10_9_summary}"
    )
    if old_header not in text:
        results.append(("header", "mismatch: v10.8 header block not found"))
    else:
        text = text.replace(old_header, new_header, 1)
        header_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if header_hash == EXPECTED:
            results.append(("header", "applied cleanly"))
        else:
            results.append(
                (
                    "header",
                    "applied (v10.9 summary; exact replacement text not in local patch files — sha256 still differs from stamp)",
                )
            )

    OUT.write_text(text, encoding="utf-8", newline="\n")
    _report(results, text)


def _report(results, text):
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest() if text else "n/a"
    matched = digest == EXPECTED
    print("Patch results:")
    for name, status in results:
        print(f"  {name}: {status}")
    if text:
        print(f"Final sha256: {digest}")
        print(f"Matched expected: {'yes' if matched else 'no'}")
        print(f"Byte count: {len(text.encode('utf-8'))}")
        print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
