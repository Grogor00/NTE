#!/usr/bin/env python3
"""Remove corpus/process stamps and internal paths from publication PDF scratch copies."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CORPUS_STAMP_LINE = re.compile(
    r"^\s*(?:"
    r"\*?\[?Working [Dd]raft\b[^\n]*"
    r"|\*Corpus version:[^*]*\*"
    r"|\*Part of NTE Corpus[^*]*\*"
    r"|\*Pedagogical / explanatory note\.[^*]*\*"
    r")\s*$",
    re.I | re.M,
)

PROCESS_FOOTER_LINE = re.compile(
    r"^\s*(?:"
    r"—\s*G\.\s*White,[^\n]*(?:tier-3|light-currency|explanatory note)[^\n]*"
    r"|\*[^*]*(?:decontaminated Zenodo|aligned 2026-)[^*]*\*"
    r")\s*$",
    re.I | re.M,
)

CLEAN_REBUILD_SUFFIX = re.compile(
    r"(\*End of Part[^*]*?)\s*[—\-]\s*Clean rebuild[^*]*(\*)",
    re.I,
)

BLANK_RUN = re.compile(r"\n{3,}")

BACKTICK_DESKTOP = re.compile(
    r"`(?:Paper_[^`\n]+|Desktop[^`\n]*)`",
    re.I,
)

# Backtick-enclosed internal artefacts (order: specific before generic)
BACKTICK_PATH = re.compile(
    r"`(?:Working|Handoffs|Papers|Master|Core_Papers|Pedagogical_Notes|Popular_Editions|New folder|Scratch|Book)/[^`\n]+`",
    re.I,
)
BACKTICK_JAMMER = re.compile(r"`Jammer_[^`\n]+`", re.I)
BACKTICK_ATTACK = re.compile(r"`(?:P_|Sigma_)[^`\n]+`", re.I)
BACKTICK_SCRIPT = re.compile(r"`[^`\n]+\.py`", re.I)
BACKTICK_MASTER = re.compile(r"`Master_[^`\n]+`", re.I)
# Any remaining internal markdown note in backticks
BACKTICK_MD = re.compile(
    r"`[^`\n]+\.md`",
    re.I,
)

# Parenthetical blocks dominated by internal file references
INTERNAL_PAREN = re.compile(
    r"\(\s*(?:"
    r"see\s+)?(?:"
    r"Jammer_[^)]*"
    r"|Working/[^)]*"
    r"|Papers/[^)]*"
    r"|Master_[^)]*"
    r"|Handoffs/[^)]*"
    r"|New folder/[^)]*"
    r"|Scratch/[^)]*"
    r"|P_[^)]*"
    r")\s*\)",
    re.I,
)

# Any parenthetical Jammer attribution (audit, version, sprint)
JAMMER_PAREN = re.compile(r"\(\s*Jammer[^)]*\)", re.I)

# Trailing semicolon + internal backtick path
TRAILING_PATH = re.compile(
    r";\s*`[^`]*(?:Working|Papers|Jammer|Master|Handoffs|New folder|Scratch)[^`]*`",
    re.I,
)

# "per Jammer audit ..." with optional path / empty parens
JAMMER_AUDIT = re.compile(r"\s*per Jammer audit[^.\n]*\.?", re.I)

# Workshop tails pointing at internal files.
# Require line-start or "; " so mid-sentence "…not a derivation: …" is not eaten.
WORKSHOP_TAIL = re.compile(
    r"(?:^|[;\n]\s*)(?:Cross-ref(?:erences?)?|Derivation|numerics|Parents|"
    r"Working corpus|Canonical paper|attack route):\s*[^.\n]*\.?",
    re.I | re.M,
)

# Italic single-line workshop notes (e.g. *BR2c ... Working/...*)
ITALIC_WORKSHOP_LINE = re.compile(
    r"^\*[^*\n]*(?:Working/|Jammer_|Handoffs/|Master/|Papers/|"
    r"New folder/|Scratch/|Core_Papers/|Pedagogical_Notes/|"
    r"Rewritten from|Desktop draft|Greg-endorsed|Item[- ]?1|"
    r"Scratch/Jammer)[^*\n]*\*?\s*$",
    re.I | re.M,
)

# Orphans left after backtick removal
ORPHAN_SEE = re.compile(r"(?:;\s*)?\b[Ss]ee\b(?=\s*[);])", re.I)
EMDASH_SEMI = re.compile(r"—\s*;\s*", re.I)
EMPTY_PARENS = re.compile(r"\(\s*\)\.?")
ORPHAN_SEMI = re.compile(r";\s*;+")
LABEL_COLON_SPACE = re.compile(r":\s*:")

CLEANUP = [
    (re.compile(r"  +"), " "),
    (re.compile(r" +\."), "."),
    (re.compile(r" +,"), ","),
    (re.compile(r" ;"), ";"),
    (re.compile(r";\s+\."), "."),
    (re.compile(r"\.\s*\.+"), "."),
    (re.compile(r"\s+—\s+—\s+"), " — "),
]


def fix_unicode_outside_math(text: str) -> str:
    parts = re.split(r"(\$[^$]+\$)", text)
    replacements = [
        ("J₃(𝕆)", r"$J_3(\mathbb{O})$"),
        ("J₃(\\mathbb{O})", r"$J_3(\mathbb{O})$"),
        ("A_F = 𝕆 ⊕ 𝕆", r"$A_F = \mathbb{O} \oplus \mathbb{O}$"),
        ("𝕆 ⊕ 𝕆", r"$\mathbb{O} \oplus \mathbb{O}$"),
        ("𝕆 → ℍ → ℂ → ℝ", r"$\mathbb{O} \to \mathbb{H} \to \mathbb{C} \to \mathbb{R}$"),
        ("𝕆 → ℍ", r"$\mathbb{O} \to \mathbb{H}$"),
        ("ℍ → ℂ", r"$\mathbb{H} \to \mathbb{C}$"),
        ("ℂ → ℝ", r"$\mathbb{C} \to \mathbb{R}$"),
        ("ℂ ⊗ 𝕆", r"$\mathbb{C} \otimes \mathbb{O}$"),
        ("unit 𝕆", r"unit $\mathbb{O}$"),
        ("unit S⁷ = unit 𝕆", r"unit $S^7$ = unit $\mathbb{O}$"),
        ("Im(𝕆)", r"Im($\mathbb{O}$)"),
        ("J₃", r"$J_3$"),
        ("𝕆", r"$\mathbb{O}$"),
        ("ℍ", r"$\mathbb{H}$"),
        ("ℂ", r"$\mathbb{C}$"),
        ("ℝ", r"$\mathbb{R}$"),
        ("≲", r"$\lesssim$"),
        ("↪", r"$\hookrightarrow$"),
        ("✗", "FAIL"),
        ("𝒜", r"$\mathcal{A}$"),
        ("𝒦", r"$\mathcal{K}$"),
        ("ᴺ", r"$N$"),
        ("ᴄ", r"$c$"),
        ("ᴨ", r"$p$"),
    ]
    for i in range(0, len(parts), 2):
        chunk = parts[i]
        for old, new in replacements:
            chunk = chunk.replace(old, new)
        parts[i] = chunk
    return "".join(parts)


def strip_corpus_metadata(text: str) -> str:
    text = CORPUS_STAMP_LINE.sub("", text)
    text = PROCESS_FOOTER_LINE.sub("", text)
    text = CLEAN_REBUILD_SUFFIX.sub(r"\1\2", text)
    text = ITALIC_WORKSHOP_LINE.sub("", text)
    text = BACKTICK_PATH.sub("", text)
    text = BACKTICK_JAMMER.sub("", text)
    text = BACKTICK_ATTACK.sub("", text)
    text = BACKTICK_SCRIPT.sub("", text)
    text = BACKTICK_MASTER.sub("", text)
    text = BACKTICK_DESKTOP.sub("", text)
    text = BACKTICK_MD.sub("", text)
    text = TRAILING_PATH.sub("", text)
    text = JAMMER_AUDIT.sub("", text)
    text = WORKSHOP_TAIL.sub("", text)
    text = INTERNAL_PAREN.sub("", text)
    text = JAMMER_PAREN.sub("", text)
    text = ORPHAN_SEE.sub("", text)
    text = EMDASH_SEMI.sub(" — ", text)
    text = EMPTY_PARENS.sub("", text)
    text = ORPHAN_SEMI.sub(";", text)
    text = LABEL_COLON_SPACE.sub(":", text)
    for pattern, repl in CLEANUP:
        text = pattern.sub(repl, text)
    text = fix_unicode_outside_math(text)
    text = re.sub(r"\bGreg-endorsed\s+", "", text, flags=re.I)
    text = re.sub(r",\s*Greg-endorsed", "", text, flags=re.I)
    text = re.sub(r"\(\s*Greg-endorsed\s*\)", "", text, flags=re.I)
    text = re.sub(r"\s*\(Scratch/Jammer\)", "", text, flags=re.I)
    text = re.sub(r"\bScratch/Jammer\b", "open work", text, flags=re.I)
    text = BLANK_RUN.sub("\n\n", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Strip corpus/process metadata from a PDF scratch markdown copy."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    text = args.path.read_text(encoding="utf-8")
    out = strip_corpus_metadata(text).rstrip() + "\n"
    (args.output or args.path).write_text(out, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
