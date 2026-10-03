#!/usr/bin/env python3
"""Apply local A5 + A6 patch instructions to all three master corpus parts."""
import hashlib
import re
from pathlib import Path

BASE = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Papers")
WORKING = Path(r"c:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working")
A5 = WORKING / "Master_Part_3_v10_8_to_v10_8_v2_Patch_Instructions_A5_BornRule_ScopeAlignment_20260523.md"
A6 = WORKING / "Master_v10_8_to_v10_9_Patch_Instructions_A6_FalsifiabilityCatalogue_Consolidation_20260523.md"


def fenced_blocks(md_text: str) -> list[str]:
    return [b.rstrip("\n") for b in re.findall(r"```\n(.*?)```", md_text, re.DOTALL)]


def apply_replace(text: str, old: str, new: str, name: str) -> tuple[str, str]:
    if old not in text:
        return text, f"mismatch: {name}"
    return text.replace(old, new, 1), f"applied cleanly: {name}"


def write_out(path: Path, text: str) -> str:
    path.write_text(text, encoding="utf-8", newline="\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def patch_part1(a5: list[str], a6: list[str]) -> dict:
    src = BASE / "NTE_v10_8_Part1_Foundations.md"
    out = BASE / "NTE_v10_9_Part1_Foundations.md"
    text = src.read_text(encoding="utf-8")
    results = []

    old_h = (
        "> **NTE v10.8 — Part 1 of 3: Foundations + Method**  \n"
        "> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII."
    )
    new_h = (
        "> **NTE v10.9 — Part 1 of 3: Foundations + Method**  \n"
        "> Abstract through §VII (Temporal Locking). Continues in Part 2 at §VIII. "
        "Master canonical at v10.9 (ship date: 2026-05-23). No A5/A6 content patches (carried from v10.8)."
    )
    if old_h not in text:
        results.append(("header", "mismatch: Part 1 header not found"))
    else:
        text = text.replace(old_h, new_h, 1)
        results.append(("header", "applied cleanly: v10.9 tag (no content patches per A6)"))

    digest = write_out(out, text)
    return {"part": 1, "results": results, "sha256": digest, "bytes": len(text.encode()), "out": out}


def patch_part2(a5: list[str], a6: list[str]) -> dict:
    src = BASE / "NTE_v10_8_Part2_Structure.md"
    out = BASE / "NTE_v10_9_Part2_Structure.md"
    text = src.read_text(encoding="utf-8")
    results = []

    text, status = apply_replace(text, a6[2], a6[3], "A6 P2 §8.7.7")
    results.append(("A6 P2", status))
    if status.startswith("mismatch"):
        return {"part": 2, "results": results, "error": True}

    old_h = (
        "> **NTE v10.8 — Part 2 of 3: Structure + Dynamics**  \n"
        "> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII)."
    )
    new_h = (
        "> **NTE v10.9 — Part 2 of 3: Structure + Dynamics**  \n"
        "> §VIII (Gauge Birth) through §XVI (Holographic). Continued from Part 1 (§VII). "
        "Master canonical at v10.9 (ship date: 2026-05-23). v10.9 patches: §8.7.7 helicity bookkeeping clarification (A6)."
    )
    if old_h not in text:
        results.append(("header", "mismatch: Part 2 header not found"))
    else:
        text = text.replace(old_h, new_h, 1)
        results.append(("header", "applied cleanly"))

    digest = write_out(out, text)
    return {"part": 2, "results": results, "sha256": digest, "bytes": len(text.encode()), "out": out}


def patch_part3(a5: list[str], a6: list[str]) -> dict:
    src = BASE / "NTE_v10_8_Part3_Accounting.md"
    out = BASE / "NTE_v10_9_Part3_Accounting.md"
    text = src.read_text(encoding="utf-8")
    results = []

    for name, old, new in [
        ("A5 P1", a5[0], a5[1]),
        ("A5 P2", a5[2], a5[3]),
        ("A6 P1", a6[0], a6[1]),
        ("A6 P3a", a6[4], a6[5]),
        ("A6 P3b", a6[6], a6[7]),
    ]:
        text, status = apply_replace(text, old, new, name)
        results.append((name, status))
        if status.startswith("mismatch"):
            return {"part": 3, "results": results, "error": True}

    p4_start = text.index("17.5.12 Falsifiability")
    p4_end = text.index("17.5.13")
    p4_old = text[p4_start:p4_end].rstrip("\n")
    p4_new = a6[9]
    note = ""
    if p4_old != a6[8]:
        note = " (source OLD; patch FIND has markdown-only blank lines between bullets)"
    sep = text[p4_start + len(p4_old) : p4_end]
    text = text[:p4_start] + p4_new + sep + text[p4_end:]
    results.append(("A6 P4", f"applied cleanly{note}"))

    old_h = (
        "> **NTE v10.8 — Part 3 of 3: Accounting + Open Work + Appendices**\n"
        "> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). Master canonical at v10.8 (ship date: 2026-05-17). v10.8 patches: §17.5.14 v10.8 status update; new §17.5.15 ξ = 1/6 conformal coupling commitment; §18.3 supersession reference; §18.4 three-readings r-prediction; new §22.14 structural confluence catalogue; new §22.15 cosmological constant cancellation via spectral-triple unimodular gravity; §17.5.3 Session 1 audit integration (T1-CORPUS-8/9/10: §2.3 structural-identity prose, §17.5.3 status sharpening, §22.16 local Lagrange-multiplier pathway); Gap 4b closure (T1-CORPUS-11: §22.17 Janus action, §9.1/§17.5.5/§XIX updates)."
    )
    new_h = (
        "> **NTE v10.9 — Part 3 of 3: Accounting + Open Work + Appendices**\n"
        "> §XVII (Parameter Accounting) through Appendix E and References. Continued from Part 2 (§XVI). "
        "Master canonical at v10.9 (ship date: 2026-05-23). v10.9 patches: §17.5.10 closed-by-enumeration v10.9; "
        "§XVII Parameter Accounting framing upgrade; §17.5.12 falsifiability catalogue consolidation; "
        "§XXI Gap 5 + §20.5 Born rule scope alignment (A5)."
    )
    if old_h not in text:
        results.append(("header", "mismatch: Part 3 header not found"))
    else:
        text = text.replace(old_h, new_h, 1)
        results.append(("header", "applied cleanly"))

    digest = write_out(out, text)
    return {"part": 3, "results": results, "sha256": digest, "bytes": len(text.encode()), "out": out}


def main():
    a5 = fenced_blocks(A5.read_text(encoding="utf-8"))
    a6 = fenced_blocks(A6.read_text(encoding="utf-8"))
    reports = [patch_part1(a5, a6), patch_part2(a5, a6), patch_part3(a5, a6)]

    print("NTE master corpus v10.9 render (A5 + A6 local instructions)\n")
    for r in reports:
        print(f"=== Part {r['part']} -> {r.get('out', 'FAILED').name} ===")
        if r.get("error"):
            print("  STOPPED on mismatch")
        for name, status in r["results"]:
            print(f"  {name}: {status}")
        if "sha256" in r:
            print(f"  sha256: {r['sha256']}")
            print(f"  bytes:  {r['bytes']}")
        print()


if __name__ == "__main__":
    main()
