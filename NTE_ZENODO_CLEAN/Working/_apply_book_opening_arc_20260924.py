#!/usr/bin/env python3
"""
Apply Greg-ratified Book opening-arc patches 2026-09-24.
Byte-exact match-or-report. Predecessors left in place; new versioned files written.
Master order from Handoff_PC_to_Cursor_Book_Opening_Arc_Four_Sets_RATIFIED_20260924.md
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
BOOK = ROOT / "Book"
HANDOFFS = ROOT / "Handoffs"
MANIFEST = ROOT / "NTE_Workflow_Manifest_v10_18.md"
REPORT_PATH = ROOT / "Working" / "_apply_book_opening_arc_20260924_REPORT.md"

report: list[tuple[str, str, str]] = []  # (id, status, detail)


def log(pid: str, status: str, detail: str = "") -> None:
    report.append((pid, status, detail))
    line = f"{pid}: {status}" + (f" — {detail}" if detail else "")
    print(line)


def nearby(text: str, needle: str, radius: int = 80) -> str:
    """Find a distinctive substring of needle and show context on FAIL."""
    words = needle.split()
    probe = " ".join(words[:6]) if words else needle[:40]
    i = text.find(probe)
    if i < 0 and words:
        probe = words[0]
        i = text.find(probe)
    if i < 0:
        return f"(no nearby match for probe {probe!r})"
    start = max(0, i - radius)
    end = min(len(text), i + min(len(needle), 120) + radius)
    return repr(text[start:end])


def apply_once(text: str, old: str, new: str, pid: str) -> tuple[str, bool]:
    n = text.count(old)
    if n != 1:
        log(pid, "FAIL", f"expected 1 occurrence, got {n}; nearby={nearby(text, old)}")
        return text, False
    log(pid, "OK", "1→1")
    return text.replace(old, new, 1), True


def extract_fenced_blocks(section: str) -> list[str]:
    """Return contents of ``` ... ``` fences in section (no language tags expected)."""
    return re.findall(r"```\n(.*?)```", section, flags=re.S)


def extract_old_new_pairs(section: str) -> list[tuple[str, str]]:
    """
    Extract (OLD, NEW) pairs from a patch section.
    Prefer fenced blocks after **OLD** / **NEW**.
    Fall back to unfenced single-line/paragraph form (Appendix C A1–A4).
    """
    pairs: list[tuple[str, str]] = []
    # Split on **OLD** keeping structure
    parts = re.split(r"\*\*OLD\*\*\s*", section)
    for part in parts[1:]:
        # part starts with OLD content, then **NEW**, then NEW content
        if "**NEW**" not in part:
            continue
        old_part, new_part = part.split("**NEW**", 1)
        old_fences = extract_fenced_blocks(old_part)
        new_fences = extract_fenced_blocks(new_part)
        if old_fences and new_fences:
            old = old_fences[0].rstrip("\n")
            new = new_fences[0].rstrip("\n")
            pairs.append((old, new))
            continue
        # Unfenced: take text until blank line or --- or next heading marker
        old = old_part.strip()
        # strip trailing --- if present before NEW was split (already split)
        if old.startswith("```"):
            # malformed; skip
            continue
        # NEW may be fenced or unfenced
        if new_fences:
            new = new_fences[0].rstrip("\n")
        else:
            new = new_part.strip()
            # cut at --- horizontal rule or next ## heading
            new = re.split(r"\n---\n|\n## ", new, maxsplit=1)[0].strip()
            if new.startswith("```"):
                inner = extract_fenced_blocks(new_part)
                if inner:
                    new = inner[0].rstrip("\n")
        # Unfenced OLD: single paragraph, no fences
        if "```" in old:
            continue
        old = re.split(r"\n---\n|\n## ", old, maxsplit=1)[0].strip()
        if old and new:
            pairs.append((old, new))
    return pairs


def section_for_heading(text: str, heading_re: str) -> str | None:
    """Return text from a matching heading to the next same-level-or-higher heading."""
    m = re.search(heading_re, text, flags=re.M)
    if not m:
        return None
    start = m.start()
    # next ### or ## after start (not including the match itself)
    rest = text[m.end() :]
    nxt = re.search(r"\n(?=### |\n## )", rest)
    if nxt:
        return text[start : m.end() + nxt.start()]
    return text[start:]


def copy_base(src: Path, dst: Path) -> str:
    if dst.exists():
        print(f"NOTE: {dst.name} already exists; overwriting from {src.name}")
    shutil.copy2(src, dst)
    return dst.read_text(encoding="utf-8")


def write_out(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# 1. Appendix C: A1–A4 + A5
# ---------------------------------------------------------------------------
def apply_appendix_c() -> None:
    src = BOOK / "Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md"
    dst = BOOK / "Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_AppendixC_v1_4_Patch_Set_20260924.md"
    a5 = HANDOFFS / "Handoff_PC_to_Cursor_AppendixC_v1_4_Patch_A5_CLFV_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")

    for pid in ("A1", "A2", "A4"):
        sec = section_for_heading(h, rf"^## {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found in handoff")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 OLD/NEW pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    # A3 insert
    sec = section_for_heading(h, r"^## A3 —")
    if not sec:
        log("A3", "FAIL", "section not found")
    else:
        anchor = (
            "...Progress and constraints in their programme bear directly on this one, "
            "in both directions."
        )
        # The insert instruction quotes the ending ellipsis-style; find the real paragraph end
        before_marker = "**The exceptional-Jordan and octonionic algebra programme.**"
        pairs = extract_old_new_pairs(sec)
        # A3 has only NEW; extract NEW fence or unfenced
        new_fences = extract_fenced_blocks(sec.split("**NEW**", 1)[-1]) if "**NEW**" in sec else []
        if new_fences:
            insert_body = new_fences[0].rstrip("\n")
        else:
            # unfenced NEW after **NEW**
            raw = sec.split("**NEW**", 1)[1].strip()
            insert_body = re.split(r"\n---\n|\n## ", raw, maxsplit=1)[0].strip()

        # Locate insertion point: after CPT paragraph ending, before exceptional-Jordan
        if before_marker not in text:
            log("A3", "FAIL", f"before-marker not found; nearby={nearby(text, 'exceptional-Jordan')}")
        elif "Ciambelli" in text and "Null-hypersurface quantisation" in text:
            log("A3", "SKIP", "already inserted")
        else:
            # Find the paragraph ending that matches the handoff instruction
            # Real text ends without leading ellipsis
            end_snip = (
                "Progress and constraints in their programme bear directly on this one, "
                "in both directions."
            )
            idx = text.find(end_snip)
            if idx < 0:
                log("A3", "FAIL", f"anchor end not found; nearby={nearby(text, 'Progress and constraints')}")
            else:
                # insert after this sentence/paragraph, before exceptional-Jordan
                insert_at = idx + len(end_snip)
                # consume trailing newlines then re-emit with blank line + insert + blank
                after = text[insert_at:]
                # expect whitespace then before_marker
                m = re.match(r"(\s*)", after)
                ws = m.group(1) if m else "\n\n"
                # Prefer: keep one blank line, insert paragraph, blank line, then marker
                marker_pos = text.find(before_marker, insert_at)
                if marker_pos < 0:
                    log("A3", "FAIL", "before_marker after anchor not found")
                else:
                    between = text[insert_at:marker_pos]
                    if between.strip():
                        log(
                            "A3",
                            "FAIL",
                            f"non-empty content between anchor and marker: {between!r}",
                        )
                    else:
                        text = (
                            text[:insert_at]
                            + "\n\n"
                            + insert_body
                            + "\n\n"
                            + text[marker_pos:]
                        )
                        log("A3", "OK", "inserted before exceptional-Jordan")
                        _ = anchor  # silence lint

    # A5
    a5t = a5.read_text(encoding="utf-8")
    pairs = extract_old_new_pairs(a5t)
    if len(pairs) != 1:
        log("A5", "FAIL", f"expected 1 pair, got {len(pairs)}")
    else:
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, "A5")

    write_out(dst, text)


# ---------------------------------------------------------------------------
# 2. Chapter 15: B1–B11 with B3′ B10′
# ---------------------------------------------------------------------------
def apply_ch15() -> None:
    src = BOOK / "Chapter_15_The_Score_v3.md"
    dst = BOOK / "Chapter_15_The_Score_v4.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter15_v4_Patch_Set_20260924.md"
    rev = HANDOFFS / "Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")
    r = rev.read_text(encoding="utf-8")

    # B3′ NEW and B10′ NEW from revisions; OLD from B3/B10 sections
    b3_sec = section_for_heading(h, r"^### B3 —")
    b10_sec = section_for_heading(h, r"^### B10 —")
    b3p_sec = section_for_heading(r, r"^## 1\. B3′")
    b10p_sec = section_for_heading(r, r"^## 2\. B10′")

    b3_pairs = extract_old_new_pairs(b3_sec or "")
    b3p_pairs = extract_old_new_pairs(b3p_sec or "")
    # B10′ has only NEW in a fence after **NEW**
    b10_old = extract_fenced_blocks((b10_sec or "").split("**OLD**", 1)[-1].split("**NEW**", 1)[0])
    b10p_new_fences = extract_fenced_blocks(
        (b10p_sec or "").split("**NEW**", 1)[-1] if b10p_sec else ""
    )

    for pid in ("B1", "B2", "B4", "B5", "B6", "B7", "B8", "B9", "B11"):
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    # B3′
    if len(b3_pairs) != 1:
        log("B3′", "FAIL", f"B3 OLD extract failed, pairs={len(b3_pairs)}")
    elif len(b3p_pairs) != 1:
        # B3′ section has OLD+NEW; if extract worked use its NEW; OLD from B3
        log("B3′", "FAIL", f"B3′ pair extract failed, pairs={len(b3p_pairs)}")
    else:
        old = b3_pairs[0][0]
        # Prefer NEW from B3′ section (same OLD)
        new = b3p_pairs[0][1]
        # Sanity: OLDs should match
        if b3p_pairs[0][0] != old:
            log(
                "B3′",
                "FAIL",
                f"OLD mismatch between B3 and B3′ (len {len(old)} vs {len(b3p_pairs[0][0])})",
            )
        else:
            text, _ = apply_once(text, old, new, "B3′")
            log("B3", "SKIP", "superseded by B3′")

    # B10′
    if not b10_old:
        log("B10′", "FAIL", "B10 OLD fence not found")
    elif not b10p_new_fences:
        log("B10′", "FAIL", "B10′ NEW fence not found")
    else:
        old = b10_old[0].rstrip("\n")
        new = b10p_new_fences[0].rstrip("\n")
        text, _ = apply_once(text, old, new, "B10′")
        log("B10", "SKIP", "superseded by B10′")

    write_out(dst, text)


# ---------------------------------------------------------------------------
# 3. Chapter 4: C1–C16, rename file
# ---------------------------------------------------------------------------
def apply_ch04() -> None:
    src = BOOK / "Chapter_04_Time_as_Expansion_v8.md"
    dst = BOOK / "Chapter_04_Time_and_Expansion_v9.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter04_v9_Patch_Set_20260924.md"
    rev = HANDOFFS / "Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")
    r = rev.read_text(encoding="utf-8")

    for n in range(1, 16):
        pid = f"C{n}"
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    # C16
    sec = section_for_heading(r, r"^## 3\. C16")
    if not sec:
        log("C16", "FAIL", "section not found")
    else:
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log("C16", "FAIL", f"expected 1 pair, got {len(pairs)}")
        else:
            old, new = pairs[0]
            text, _ = apply_once(text, old, new, "C16")

    write_out(dst, text)


# ---------------------------------------------------------------------------
# 4. Chapter 5: D1–D11
# ---------------------------------------------------------------------------
def apply_ch05() -> None:
    src = BOOK / "Chapter_05_The_Eighth_Colour_v7.md"
    dst = BOOK / "Chapter_05_The_Eighth_Colour_v8.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter05_v8_Patch_Set_20260924.md"
    rev = HANDOFFS / "Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")
    r = rev.read_text(encoding="utf-8")

    for n in range(1, 10):
        pid = f"D{n}"
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    for pid, heading in (("D10", r"^## 4\. D10"), ("D11", r"^## 5\. D11")):
        sec = section_for_heading(r, heading)
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    write_out(dst, text)


# ---------------------------------------------------------------------------
# 5. Chapter 2: E1–E6 (E3 has two pairs)
# ---------------------------------------------------------------------------
def apply_ch02() -> None:
    src = BOOK / "Chapter_02_Entanglement_as_Geometry_v7.md"
    dst = BOOK / "Chapter_02_Entanglement_as_Geometry_v8.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter02_v8_Patch_Set_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")

    for n in range(1, 7):
        pid = f"E{n}"
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if pid == "E3":
            if len(pairs) != 2:
                log(pid, "FAIL", f"expected 2 pairs, got {len(pairs)}")
                continue
            for i, (old, new) in enumerate(pairs, 1):
                text, ok = apply_once(text, old, new, f"E3.{i}")
            # Also mark parent E3 as OK if both children OK
            if all(r[0] in ("E3.1", "E3.2") and r[1] == "OK" for r in report if r[0].startswith("E3.")):
                pass
        else:
            if len(pairs) != 1:
                log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
                continue
            old, new = pairs[0]
            text, _ = apply_once(text, old, new, pid)

    write_out(dst, text)


# ---------------------------------------------------------------------------
# 6–7. Chapter 1 + Prelude
# ---------------------------------------------------------------------------
def apply_ch01_prelude() -> None:
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter01_v11_and_Prelude_v8_Patch_Set_20260924.md"
    h = handoff.read_text(encoding="utf-8")

    # Ch 1
    src = BOOK / "Chapter_01_The_Photons_Journey_v10.md"
    dst = BOOK / "Chapter_01_The_Photons_Journey_v11.md"
    text = copy_base(src, dst)
    for n in range(1, 10):
        pid = f"F{n}"
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)
    write_out(dst, text)

    # Prelude
    src = BOOK / "Prelude_The_Forty_Million_Year_Instant_v7.md"
    dst = BOOK / "Prelude_The_Forty_Million_Year_Instant_v8.md"
    text = copy_base(src, dst)
    for pid in ("P1", "P2"):
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)
    write_out(dst, text)


# ---------------------------------------------------------------------------
# 8. Chapter 3: M1–M9 + M10
# ---------------------------------------------------------------------------
def apply_ch03() -> None:
    src = BOOK / "Chapter_03_A_Closed_Universe_v6_1.md"
    dst = BOOK / "Chapter_03_A_Closed_Universe_v7.md"
    handoff = HANDOFFS / "Handoff_PC_to_Greg_Cursor_Chapter03_v7_Patch_Set_20260924.md"
    master = HANDOFFS / "Handoff_PC_to_Cursor_Book_Opening_Arc_Four_Sets_RATIFIED_20260924.md"
    text = copy_base(src, dst)
    h = handoff.read_text(encoding="utf-8")
    m = master.read_text(encoding="utf-8")

    for n in range(1, 10):
        pid = f"M{n}"
        sec = section_for_heading(h, rf"^### {pid} —")
        if not sec:
            log(pid, "FAIL", "section not found")
            continue
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log(pid, "FAIL", f"expected 1 pair, got {len(pairs)}")
            continue
        old, new = pairs[0]
        text, _ = apply_once(text, old, new, pid)

    # M10 from master handoff
    sec = section_for_heading(m, r"^### Patch M10")
    if not sec:
        log("M10", "FAIL", "section not found in master handoff")
    else:
        pairs = extract_old_new_pairs(sec)
        if len(pairs) != 1:
            log("M10", "FAIL", f"expected 1 pair, got {len(pairs)}")
        else:
            old, new = pairs[0]
            text, _ = apply_once(text, old, new, "M10")

    write_out(dst, text)


# ---------------------------------------------------------------------------
# Manifest §10 registrations
# ---------------------------------------------------------------------------
REGS = [
    (
        "MF-OPENING",
        "Book/ opening arc — four sets ratified 2026-09-24",
        """- **Book/ opening arc — four sets ratified 2026-09-24, 18:21 NZST** (`Handoff_PC_to_Cursor_Book_Opening_Arc_Four_Sets_RATIFIED_20260924.md`, PC). Clears Ch 1 v11 (F1–F9), Prelude v8 (P1–P2), Ch 2 v8 (E1–E6), Ch 5 v8 (D1–D11) and Ch 3 v7 (M1–M10) for Cursor, alongside the already-ratified Appendix C v1.4 (A1–A5), Ch 15 v4 (B1–B11 with B3′/B10′) and Ch 4 v9 (C1–C16, renamed to `Chapter_04_Time_and_Expansion_v9.md`). **K1 settled: "Time and Expansion" stays as both Ch 1's section heading and Ch 4's chapter title.** **M10 added to Ch 3** — carries the ratified Ω_k → 0 reading and falsifiability item 11 into the Book at AC's warned register, and removes a Book overclaim the corpus correction exposed (v6.1 said a detected closed curvature "would be dramatic support"; item 11 is one-sided and not NTE-distinguishing). Ch 4's rename and Ch 3's M7 forward pointer must be applied together or not at all.
""",
    ),
    (
        "MF-ACREV",
        "Book/ AC-response revisions to three patch sets",
        """- **Book/ AC-response revisions to three patch sets** (`Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md`, PC, 2026-09-24, Greg-ratified 18:15 NZST). **B3′ and B10′ supersede B3 and B10 in the Ch 15 v4 set** — σ figures removed on AC's instruction (the Companion 17 N_e item would move both anchors within the week); P-ACT-LB 0.9743 ± 0.0034 printed alongside Planck 2018. **C16** added to the Ch 4 v9 set — N_lock demoted to candidate register and reframed as staged completion (quarks ~10⁻³, leptons ~10⁻², completion ~10⁻¹) per Part 1 §VII and Part 3. **D10, D11** added to the Ch 5 v8 set — the forced-addition argument rebuilt on the SM Higgs potential's curvature rather than on a named V_NTE whose form is unverified (H1), and the 10^8.5 BBN ratio regraded as read-off cross-check rather than prediction (H2). Closed with no Book change: N2, F5, N1, F2. Falsifiability item 11 deliberately not carried into Ch 15 — exposure, not handle.
""",
    ),
    (
        "MF-A5",
        "Book/ Appendix C v1.4 patch set",
        """- **Book/ Appendix C v1.4 patch set** — A1–A4 (2026-09-24) plus **A5 (CLFV tan²θ₂₃ = 1 stated plainly)**, Greg-ratified 2026-09-24. The originally proposed A5 on the (n_s, r) row was withdrawn as redundant; flag F1 retired as raised in error (v1.3 already current). F2 closed by A5.
""",
    ),
]


def apply_manifest() -> None:
    man = MANIFEST.read_text(encoding="utf-8")
    if "**In progress:**" not in man:
        log("MF", "FAIL", "**In progress:** marker not found")
        return
    block = ""
    for pid, needle, entry in REGS:
        if needle in man:
            log(pid, "SKIP", "already present")
        else:
            block += entry if entry.endswith("\n") else entry + "\n"
            log(pid, "OK", "queued for insert")
    if block:
        man = man.replace("**In progress:**", "**In progress:**\n" + block, 1)
        MANIFEST.write_text(man, encoding="utf-8", newline="\n")
        log("MF-WRITE", "OK", "manifest updated")
    else:
        log("MF-WRITE", "SKIP", "nothing to add")


def write_report() -> None:
    ok = sum(1 for _, s, _ in report if s == "OK")
    fail = sum(1 for _, s, _ in report if s == "FAIL")
    skip = sum(1 for _, s, _ in report if s == "SKIP")
    lines = [
        "# Book opening-arc apply report — 2026-09-24",
        "",
        f"Totals: **OK={ok}** · **FAIL={fail}** · **SKIP={skip}** · rows={len(report)}",
        "",
        "| Patch ID | Status | Detail |",
        "|---|---|---|",
    ]
    for pid, status, detail in report:
        detail_esc = detail.replace("|", "\\|")
        lines.append(f"| {pid} | {status} | {detail_esc} |")
    lines.append("")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"\nReport written: {REPORT_PATH}")
    print(f"Totals: OK={ok} FAIL={fail} SKIP={skip}")


def main() -> int:
    print("=== 1. Appendix C ===")
    apply_appendix_c()
    print("=== 2. Chapter 15 ===")
    apply_ch15()
    print("=== 3. Chapter 4 ===")
    apply_ch04()
    print("=== 4. Chapter 5 ===")
    apply_ch05()
    print("=== 5. Chapter 2 ===")
    apply_ch02()
    print("=== 6–7. Chapter 1 + Prelude ===")
    apply_ch01_prelude()
    print("=== 8. Chapter 3 ===")
    apply_ch03()
    print("=== Manifest §10 ===")
    apply_manifest()
    write_report()
    fails = sum(1 for _, s, _ in report if s == "FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
