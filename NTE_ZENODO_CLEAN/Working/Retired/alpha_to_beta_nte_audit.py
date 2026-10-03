#!/usr/bin/env python3
"""PC handoff: α_NTE → β_NTE corpus audit (conservative). Greg 2026-06-04."""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ALPHA = "\u03b1"  # α
BETA = "\u03b2_NTE"

PROTECT = [
    (re.compile(r"fine-structure constant\s+\u03b1_em", re.I), "__PROT_FS_AEM__"),
    (re.compile(r"fine-structure constant\s+\$\\alpha_\{em\}\$", re.I), "__PROT_FS_AEM_MATH__"),
    (re.compile(r"fine-structure constant\s+\u03b1\b", re.I), "__PROT_FS_ALPHA__"),
    (re.compile(r"fine-structure constant\s+\$\\alpha\$", re.I), "__PROT_FS_ALPHA_MATH__"),
    (re.compile(r"fine-structure constant\s+\$\\alpha_\{\\mathrm\{em\}\}\$", re.I), "__PROT_FS_AEM_MATH2__"),
    (re.compile(r"\u03b1_em", re.I), "__PROT_EM__"),
    (re.compile(r"\u03b1_EM"), "__PROT_EM__"),
    (re.compile(r"\u03b1_s\b"), "__PROT_AS__"),
    (re.compile(r"g_eff\s*\u00b7\s*\u03b1_em", re.I), "__PROT_GEFF__"),
    (re.compile(r"Pathway\s+\u03b1\b", re.I), "__PROT_PATH__"),
    (re.compile(r"Path\s+\u03b1\b", re.I), "__PROT_PATH__"),
    (re.compile(r"Pathway\s+Alpha\b", re.I), "__PROT_PATHA__"),
    (re.compile(r"\u03b1-particle", re.I), "__PROT_AP__"),
    (re.compile(r"\u03b1-decay", re.I), "__PROT_AD__"),
    (re.compile(r"\u03b1_helix", re.I), "__PROT_AH__"),
    (re.compile(r"\u03b1_i\b"), "__PROT_IDX__"),
    (re.compile(r"\u03b1_j\b"), "__PROT_IDX__"),
    (re.compile(r"\u03b1_\d"), "__PROT_IDX__"),
    (re.compile(r"\u03b1_\*"), "__PROT_IDX__"),
    (re.compile(r"a_\{?0\}?\^?\u03b1"), "__PROT_HEAT__"),  # heat-kernel a_0^α style
]

UNPROTECT = {v: k.pattern for k, v in PROTECT}

# Confident NTE replacements (order matters)
REPLACEMENTS = [
    (re.compile(r"H\(N\)\s*=\s*\u03b1\|"), r"H(N) = " + BETA + "|"),
    (re.compile(r"H\(x,N\)\s*=\s*\u03b1\|"), r"H(x,N) = " + BETA + "|"),
    (re.compile(r"H\s*=\s*\u03b1\|"), r"H = " + BETA + "|"),
    (re.compile(r"1/\(\u03b1\|"), r"1/(" + BETA + "|"),
    (re.compile(r"dN/\(\u03b1\|"), r"dN/(" + BETA + "|"),
    (re.compile(r"/\(\u03b1\|"), r"/(" + BETA + "|"),
    (re.compile(r"\u03b1\|Φ_NTE"), BETA + "|Φ_NTE"),
    (re.compile(r"\u03b1\|Φ"), BETA + "|Φ"),
    (re.compile(r"\u03b1\s*=\s*2\.38\s*\u00d7\s*10"), BETA + " = 2.38 × 10"),
    (re.compile(r"\u03b1\s*=\s*2\.38\u00d710"), BETA + " = 2.38×10"),
    (re.compile(r"\u03b1\s*=\s*\(1/M_P\)"), BETA + " = (1/M_P)"),
    (re.compile(r"cosmological coupling constant\s+\u03b1\b"), "cosmological coupling constant " + BETA),
    (re.compile(r"coupling constant\s+\u03b1\b"), "coupling constant " + BETA),
    (re.compile(r"constant\s+\u03b1\s+whose"), "constant " + BETA + " whose"),
    (re.compile(r"constant\s+\u03b1\b"), "constant " + BETA),
    (re.compile(r"\u03b1\s+characterisation"), BETA + " characterisation"),
    (re.compile(r"\u03b1-chain"), BETA + "-chain"),
    (re.compile(r"\u03b1M_Pl"), BETA + "·M_Pl"),
    (re.compile(r"\u03b1\s*·\s*M_Pl"), BETA + "·M_Pl"),
    (re.compile(r"−ln\(\u03b1M_Pl\)"), "−ln(" + BETA + "·M_Pl)"),
    (re.compile(r"-ln\(\u03b1M_Pl\)"), "-ln(" + BETA + "·M_Pl)"),
    (re.compile(r"H₀\s*=\s*\u03b1\s"), r"H₀ = " + BETA + " "),
    (re.compile(r"\u03b1\s+v_EW"), BETA + " v_EW"),
    (re.compile(r"\u03b1\s+encodes\s+both"), BETA + " encodes both"),
    (re.compile(r"expressing\s+\u03b1\s+in\s+terms"), "expressing " + BETA + " in terms"),
    (re.compile(r"\u03b1\s+is\s+the\s+cosmological"), BETA + " is the cosmological"),
    (re.compile(r"\u03b1\s+is\s+a\s+fundamental"), BETA + " is a fundamental"),
    (re.compile(r"\u03b1\s+is\s+potentially"), BETA + " is potentially"),
    (re.compile(r"\u03b1\s+is\s+the\s+friedmann", re.I), BETA + " is the Friedmann"),
    (re.compile(r"so\s+\u03b1\s+has\s+dimensions"), "so " + BETA + " has dimensions"),
    (re.compile(r"where\s+\u03b1\s+is\s+the\s+cosmological"), "where " + BETA + " is the cosmological"),
    (re.compile(r"where\s+\u03b1\s+is\s+"), "where " + BETA + " is "),
    (re.compile(r"via\s+the\s+substitution\s+d/dt\s*→\s*\u03b1\|"), "via the substitution d/dt → " + BETA + "|"),
    (re.compile(r"da/dt\s*=\s*\u03b1\|"), r"da/dt = " + BETA + "|"),
    (re.compile(r"Characterisation\s+\u03b1\b"), "Characterisation " + BETA),
    (re.compile(r"Appendix\s+B\.\d+.*?\u03b1\s+adjusts"), lambda m: m.group(0).replace(ALPHA, BETA)),
    (re.compile(r"framework's\s+\u03b1\b"), "framework's " + BETA),
    (re.compile(r"foundational constant\s+\u03b1\b"), "foundational constant " + BETA),
    (re.compile(r"\u03b1\s+adjusts\s+to\s+accommodate"), BETA + " adjusts to accommodate"),
    (re.compile(r"value\s+of\s+\u03b1\b"), "value of " + BETA),
    (re.compile(r"any\s+value\s+of\s+\u03b1\b"), "any value of " + BETA),
    (re.compile(r"tested\s+values\s+of\s+\u03b1\b"), "tested values of " + BETA),
    (re.compile(r"\u03b1\s+is\s+not\s+derivable"), BETA + " is not derivable"),
    (re.compile(r"\u03b1\s+←\s+"), BETA + " ← "),
    (re.compile(r"←\s+\u03b1\b"), "← " + BETA),
    (re.compile(r"\(\u03b1\s+←"), "(" + BETA + " ←"),
    (re.compile(r"one\s+new\s+constant[^.]*\u03b1\b"), lambda m: m.group(0).replace(ALPHA, BETA)),
    (re.compile(r"multiplied\s+by\s+a\s+constant\s+\u03b1\b"), "multiplied by a constant " + BETA),
    (re.compile(r"multiplied\s+by\s+\u03b1\b"), "multiplied by " + BETA),
    (re.compile(r"with\s+H\s*=\s*\u03b1\|"), "with H = " + BETA + "|"),
    (re.compile(r"equation\s+H\s*=\s*\u03b1\|"), "equation H = " + BETA + "|"),
    (re.compile(r"central\s+equation\s+and\s+dt\s*=\s*dN/\(\u03b1\|"), "central equation and dt = dN/(" + BETA + "|"),
    (re.compile(r"dt\s*=\s*dN/\(\u03b1\|"), "dt = dN/(" + BETA + "|"),
    (re.compile(r"dt/dN\s*=\s*1/\(\u03b1\|"), "dt/dN = 1/(" + BETA + "|"),
    (re.compile(r"ratified\s+proportionality\s+constraint\*\*\s+H\(N\)\s*=\s*\u03b1\|"), "ratified proportionality constraint** H(N) = " + BETA + "|"),
    (re.compile(r"constraint\s+H\s*=\s*\u03b1\|"), "constraint H = " + BETA + "|"),
    (re.compile(r"constraint\s+relation\s+—\s+not.*?\u03b1\|"), lambda m: m.group(0).replace(ALPHA, BETA)),
    (re.compile(r"via\s+dt\s*=\s*dN/\(\u03b1\|"), "via dt = dN/(" + BETA + "|"),
    (re.compile(r"map\s+from\s+e-fold[^.]*\u03b1\|"), lambda m: m.group(0).replace(ALPHA, BETA)),
    (re.compile(r"only\s+on\s+the\s+proportionality\s+constraint\s+and[^.]*\u03b1\b"), lambda m: m.group(0).replace(ALPHA, BETA)),
]

EM_CONTEXT = re.compile(
    r"fine-structure|1/137|0\.007297|Sommerfeld|electromagnetic coupling|QED coupling|α_em|__PROT_EM__",
    re.I,
)


@dataclass
class FileReport:
    path: str
    modified: bool = False
    nte_confident: int = 0
    em_confident: int = 0
    leave_unchanged: int = 0
    ambiguous: list = field(default_factory=list)
    subs_made: int = 0


def protect(text: str) -> str:
    for rx, tok in PROTECT:
        text = rx.sub(tok, text)
    return text


def protect_with_map(text: str) -> tuple[str, list[tuple[str, str]]]:
    maps: list[tuple[str, str]] = []
    for rx, tok in PROTECT:
        def repl(m, t=tok):
            maps.append((t, m.group(0)))
            return t

        text = rx.sub(repl, text)
    return text, maps


def unprotect_maps(text: str, maps: list[tuple[str, str]]) -> str:
    for tok, orig in reversed(maps):
        text = text.replace(tok, orig, 1)
    return text


def apply_replacements(text: str) -> tuple[str, int]:
    n = 0
    for rx, repl in REPLACEMENTS:
        if callable(repl):

            def _cb(m):
                nonlocal n
                n += 1
                return repl(m)

            text, c = rx.subn(_cb, text)
            n += c
        else:
            text, c = rx.subn(repl, text)
            n += c
    return text, n


def classify_remaining(text: str, path: str) -> list[dict]:
    flags = []
    for i, line in enumerate(text.splitlines(), 1):
        if ALPHA not in line and "alpha" not in line.lower():
            continue
        for m in re.finditer(r"\u03b1", line):
            start = max(0, m.start() - 80)
            end = min(len(line), m.end() + 80)
            ctx = line[start:end]
            if "__PROT_" in ctx:
                continue
            if EM_CONTEXT.search(ctx):
                continue
            if re.search(r"Pathway|Path\s+\u03b1|alpha-numeric", ctx, re.I):
                continue
            flags.append(
                {
                    "line": i,
                    "context": ctx.strip(),
                    "reason": "α present after replacements; needs PC/AC review",
                }
            )
    return flags


def process_file(path: Path, apply: bool) -> FileReport:
    rep = FileReport(path=str(path))
    raw = path.read_text(encoding="utf-8")
    if ALPHA not in raw:
        return rep

    protected, maps = protect_with_map(raw)
    before_alpha = protected.count(ALPHA)
    new_text, subs = apply_replacements(protected)
    rep.subs_made = subs
    new_text = unprotect_maps(new_text, maps)

    # count em (protected tokens restored)
    rep.em_confident = len(re.findall(r"\u03b1_em", raw, re.I))

    amb = classify_remaining(new_text, str(path))
    rep.ambiguous = amb
    rep.nte_confident = subs
    if amb:
        rep.leave_unchanged = len(amb)
    else:
        remaining = new_text.count(ALPHA) - raw.count(r"\u03b1_em")  # approximate
        rep.leave_unchanged = max(0, new_text.count(ALPHA) - rep.em_confident)

    if apply and new_text != raw:
        path.write_text(new_text, encoding="utf-8")
        rep.modified = True

    return rep


def tier1_files(root: Path) -> list[Path]:
    files = []
    desktop = root.parent.parent  # NTE v10_6 -> Desktop
    book = desktop / "Book"
    for p in sorted(book.glob("*.md")):
        if p.name.startswith("Zenodo"):
            continue
        files.append(p)
    papers = root.parent / "Papers"
    for p in sorted(papers.glob("*.md")):
        if "depreciated" in str(p):
            continue
        files.append(p)
    for name in (
        "NTE_v10_17_Part1_Foundations.md",
        "NTE_v10_17_Part2_Structure.md",
        "NTE_v10_17_Part3_Accounting.md",
    ):
        fp = papers / name
        if fp.exists():
            files.append(fp)
    working = root
    for name in (
        "Paper_PhiNTE_Necessity_and_Irreducibility_v0_1_Scratch_20260603.md",
        "Paper_PhiNTE_Necessity_PedagogicalPivot_v0_1_PC_20260604.md",
    ):
        fp = working / name
        if fp.exists():
            files.append(fp)
    return files


def add_footnote_pc(text: str) -> str:
    note = (
        "\n\n[^beta-nte]: **β_NTE** denotes the framework's cosmological coupling in "
        "**H = β_NTE |Φ_NTE|²** (≈ 2.38×10⁻⁴⁷ GeV⁻¹). It is **not** the fine-structure "
        "constant **α_em** ≈ 1/137.\n"
    )
    if "[^beta-nte]" in text:
        return text
    # after first β_NTE introduction
    idx = text.find(BETA)
    if idx < 0:
        return text
    line_end = text.find("\n", idx)
    if line_end < 0:
        return text
    return text[: line_end + 1] + note + text[line_end + 1 :]


def main():
    apply = "--apply" in sys.argv
    root = Path(__file__).resolve().parent
    files = tier1_files(root)
    reports = []
    total_subs = 0
    total_amb = 0
    for fp in files:
        r = process_file(fp, apply=apply)
        if apply and "PedagogicalPivot" in fp.name:
            t = fp.read_text(encoding="utf-8")
            t2 = add_footnote_pc(t)
            if t2 != t:
                fp.write_text(t2, encoding="utf-8")
                r.modified = True
        reports.append(r)
        total_subs += r.subs_made
        total_amb += len(r.ambiguous)

    out = root / "alpha_to_beta_audit_log.json"
    out.write_text(
        json.dumps([r.__dict__ for r in reports], indent=2), encoding="utf-8"
    )
    print(f"Scanned {len(files)} files, apply={apply}, log={out}")
    if apply:
        print(f"Substitutions: {total_subs}, ambiguity flags: {total_amb}")


if __name__ == "__main__":
    main()
