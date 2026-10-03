#!/usr/bin/env python3
"""Remove internal corpus paths and workshop references from publication PDF text."""
from __future__ import annotations

import re

# Backtick-enclosed internal artefacts (order: specific before generic)
BACKTICK_PATH = re.compile(
    r"`(?:Working|Handoffs|Papers|Master)/[^`\n]+`",
    re.I,
)
BACKTICK_JAMMER = re.compile(r"`Jammer_[^`\n]+`", re.I)
BACKTICK_HANDOFF = re.compile(r"`Handoff_[^`\n]+`", re.I)
BACKTICK_ATTACK = re.compile(r"`(?:P_|Sigma_|Paper_S|Void_|Gap_)[^`\n]+`", re.I)
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
    r"|P_[^)]*"
    r")\s*\)",
    re.I,
)

# Any parenthetical Jammer attribution (audit, version, sprint)
JAMMER_PAREN = re.compile(r"\(\s*Jammer[^)]*\)", re.I)

# Workshop attribution blocks: (LB-6; Greg …; AC Proposal …; Jammer …) — not bare (LB-6)
WORKSHOP_ATTRIBUTION_PAREN = re.compile(
    r"\(\s*[^)]*(?:"
    r"Greg\s+\d{4}-\d{2}-\d{2}|"
    r"Jammer(?:\s+v[\d.]+|_|\s+§|\s+\d{4})|"
    r"AC Proposal\s+\d{4}-\d{2}-\d{2}|"
    r"Scratch\s+\d{4}-\d{2}-\d{2}|"
    r"Scratch\s+P\d+|Scratch\s+v[\d.]+|Scratch\s+next|"
    r"Sprint\s+[A-Z]"
    r")[^)]*\)\s*",
    re.I,
)

# ratified by Greg … (abstract / status prose)
RATIFIED_BY_GREG = re.compile(
    r"\*\*ratified by Greg \d{4}-\d{2}-\d{2}\*\*\s*",
    re.I,
)
JAMMER_WORKING_NOTE = re.compile(
    r"(?:\s*\+\s*)?Jammer(?:'s|\s+)[^.;]*(?:working note|numerics open)[^.)]*|"
    r"(?:;\s*|—\s*)?Jammer numerics open\.?",
    re.I,
)
JAMMER_NUMERICS_OPEN = re.compile(r"(?:;\s*|—\s*)?Jammer numerics open\.?", re.I)
JAMMER_POSSESSIVE = re.compile(r"\bJammer's\s+", re.I)
JAMMER_AND_SETUP = re.compile(
    r"\s+and Jammer V_NTE Stage 1 setup \(against v[\d.]+\)",
    re.I,
)
JAMMER_INLINE = re.compile(
    r",\s*Jammer (?:J1 sign-off \d{4}-\d{2}-\d{2}|S3-f3[^;)]+|J6-n1b[^;)]+)",
    re.I,
)
JAMMER_SEMI_CLAUSE = re.compile(
    r";\s*Jammer (?:S3-f3[^;]+|J6-n1b[^;)]+|unimodular gravity working note)",
    re.I,
)
JAMMER_DERIVED_HEADER = re.compile(r"\(\s*derived,\s*Jammer[^)]*\)", re.I)
JAMMER_UNDER = re.compile(r"\bunder Jammer J6-n1b\s+", re.I)
PLUS_JAMMER = re.compile(r"\s*\+\s*Jammer\b", re.I)
EMDASH_DOT = re.compile(r"—\s*\.")
ORPHAN_COMMA_PAREN = re.compile(r"\(\s*,\s*\)\.?\s*")
ORPHAN_VERSION_PAREN = re.compile(r"\(\s*v[\d.]+\s*\)")
NUMERICS_ORPHAN = re.compile(r"\s*Numerics:\s*,+\.?", re.I)
SCOPE_EM_DASH = re.compile(r"scopes —\.")
TRAILING_EMDASH = re.compile(r"\s+—\s*$", re.M)
TRAILING_COMMA_DOT = re.compile(r",\s*,+\.|,\s*\.\s*$", re.M)
SCRATCH_PAREN = re.compile(
    r"\(\s*Scratch(?:\s+P\d+|\s+v[\d.]+|\s+next)\s*\)",
    re.I,
)
EMPTY_BOLD_BLOCK = re.compile(r"\*\*\*\*;?\s*(?:numerics\.?)?", re.I)
DOUBLE_COLON_DOT = re.compile(r"\.:\.")
ORPHAN_PLUS_PAREN = re.compile(r"\(\s*([^()]+?)\s*\+\s*\)")
BOLD_LABEL_SPACE = re.compile(r"(\S)\s+:\*\*")

# Trailing semicolon + internal backtick path
TRAILING_PATH = re.compile(
    r";\s*`[^`]*(?:Working|Papers|Jammer|Master|Handoffs)[^`]*`",
    re.I,
)

# "per Jammer audit ..." with optional path / empty parens
JAMMER_AUDIT = re.compile(r"\s*per Jammer audit[^.\n]*\.?\s*", re.I)

# Workshop tails pointing at internal files (only when tail names an internal artefact)
WORKSHOP_TAIL = re.compile(
    r"(?:;\s*)?(?:Cross-ref(?:erences?)?|Derivation|numerics|Parents|"
    r"Working corpus|Canonical paper|attack route):\s*"
    r"(?=[^.\n]*(?:Working/|Papers/|Jammer|Master/|Handoffs/|Handoff_|\.py))[^.\n]*\.?",
    re.I,
)

# Italic single-line workshop notes (e.g. *BR2c ... Working/...*)
ITALIC_WORKSHOP_LINE = re.compile(
    r"^\*[^*\n]*(?:Working/|Jammer_|Handoffs/|Master/|Papers/)[^*\n]*\*?\s*$",
    re.I | re.M,
)

# Standalone handoff / ratification sync metadata (publication strip)
HANDOFF_SYNC_LINE = re.compile(
    r"^Handoff:[^\n]*(?:AC sync|R6):[^\n]*\n?",
    re.I | re.M,
)
HANDOFF_ORPHAN_LINE = re.compile(
    r"^Handoff:;(?:\s*(?:AC sync|R6):;?)+\.?\s*\n?",
    re.I | re.M,
)

# Orphans left after backtick removal (do not consume paragraph breaks)
ORPHAN_SEE = re.compile(r";\s*See\b\s*\.?(?:[ \t]*)", re.I)
TRAILING_SEE = re.compile(r"(?<=[.!?])[ \t]+See\s*\.?(?:[ \t]*)$", re.I | re.M)
EMDASH_SEMI = re.compile(r"—\s*;\s*", re.I)
EMPTY_PARENS = re.compile(r"\(\s*\)\.?")
EMPTY_EMDASH = re.compile(r"—\s*\)\.?")
EMPTY_PARENS_SEMI = re.compile(r"\(\s*;\s*\)\.?")
ORPHAN_SEMI = re.compile(r";\s*;+")
LABEL_COLON_SPACE = re.compile(r":\s*:")
GHOST_SCAN_LABEL = re.compile(r"(\*\*Ghost scan)\s+:\s*\*\*", re.I)
LEVEL_RUNON = re.compile(r"level\*\*The\b", re.I)
SEE_EMPTY = re.compile(r" — see \)\.?")
REQUIRED_MONITOR = re.compile(r"required\*\*\s+\*\*MONITOR", re.I)
CLOSED_ORPHAN = re.compile(r"\*\*Closed [^*]+\*\*:\.?\s*")
LABEL_TRAIL_DOT = re.compile(r"(\*\*[^*]+:\*\*)\.(?=\s)")
ORPHAN_LABEL = re.compile(
    r"(?:Cross-ref|Canonical paper|Derivation|Consolidation|numerics|audit|Full audit):\s*[;\.]+\s*",
    re.I,
)
PAREN_LEAD_SEMI = re.compile(r"\(\s*;\s*")
PAREN_SEMI_TAIL = re.compile(r"\(([^();]+);\s*\)")
T2G_TAG = re.compile(r"\(\s*T2g-1\s*\)\.?")
DOUBLE_SEMI = re.compile(r";\s*;+")

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
    text = HANDOFF_SYNC_LINE.sub("", text)
    text = ITALIC_WORKSHOP_LINE.sub("", text)
    text = BACKTICK_PATH.sub("", text)
    text = BACKTICK_HANDOFF.sub("", text)
    text = BACKTICK_JAMMER.sub("", text)
    text = BACKTICK_ATTACK.sub("", text)
    text = BACKTICK_SCRIPT.sub("", text)
    text = BACKTICK_MASTER.sub("", text)
    text = BACKTICK_MD.sub("", text)
    text = TRAILING_PATH.sub("", text)
    text = JAMMER_AUDIT.sub(". ", text)
    text = WORKSHOP_TAIL.sub("", text)
    text = INTERNAL_PAREN.sub("", text)
    text = WORKSHOP_ATTRIBUTION_PAREN.sub("", text)
    text = SCRATCH_PAREN.sub("", text)
    text = JAMMER_PAREN.sub("", text)
    text = RATIFIED_BY_GREG.sub("", text)
    text = JAMMER_WORKING_NOTE.sub("", text)
    text = JAMMER_NUMERICS_OPEN.sub("", text)
    text = JAMMER_POSSESSIVE.sub("", text)
    text = JAMMER_AND_SETUP.sub("", text)
    text = JAMMER_INLINE.sub("", text)
    text = JAMMER_SEMI_CLAUSE.sub("", text)
    text = JAMMER_DERIVED_HEADER.sub("(derived)", text)
    text = JAMMER_UNDER.sub("under ", text)
    text = PLUS_JAMMER.sub("", text)
    text = ORPHAN_PLUS_PAREN.sub(r"(\1)", text)
    text = ORPHAN_SEE.sub("", text)
    text = TRAILING_SEE.sub("", text)
    text = EMDASH_SEMI.sub(" — ", text)
    text = EMPTY_PARENS.sub("", text)
    text = EMPTY_EMDASH.sub("", text)
    text = EMPTY_PARENS_SEMI.sub("", text)
    text = ORPHAN_SEMI.sub(";", text)
    text = LABEL_COLON_SPACE.sub(":", text)
    text = GHOST_SCAN_LABEL.sub(r"\1:**", text)
    text = BOLD_LABEL_SPACE.sub(r"\1:**", text)
    text = LEVEL_RUNON.sub("level**. The", text)
    text = SEE_EMPTY.sub(").", text)
    text = REQUIRED_MONITOR.sub("required.** **MONITOR", text)
    text = LABEL_TRAIL_DOT.sub(r"\1", text)
    text = CLOSED_ORPHAN.sub("", text)
    text = HANDOFF_ORPHAN_LINE.sub("", text)
    text = ORPHAN_LABEL.sub("", text)
    text = PAREN_LEAD_SEMI.sub("(", text)
    text = PAREN_SEMI_TAIL.sub(r"(\1)", text)
    text = T2G_TAG.sub("", text)
    text = DOUBLE_SEMI.sub(";", text)
    text = EMDASH_DOT.sub(".", text)
    text = ORPHAN_COMMA_PAREN.sub(". ", text)
    text = ORPHAN_VERSION_PAREN.sub("", text)
    text = NUMERICS_ORPHAN.sub("", text)
    text = SCOPE_EM_DASH.sub("scopes.", text)
    text = TRAILING_EMDASH.sub("", text)
    text = TRAILING_COMMA_DOT.sub(".", text)
    text = EMPTY_BOLD_BLOCK.sub("", text)
    text = DOUBLE_COLON_DOT.sub(".", text)
    for pattern, repl in CLEANUP:
        text = pattern.sub(repl, text)
    text = fix_unicode_outside_math(text)
    return text
