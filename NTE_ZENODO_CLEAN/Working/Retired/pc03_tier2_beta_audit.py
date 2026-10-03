#!/usr/bin/env python3
"""PC-03 Tier 2: Working/ Handoffs/ MB beta audit apply + resolution summary."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# import audit module
sys.path.insert(0, str(Path(__file__).resolve().parent))
import alpha_to_beta_nte_audit as audit

SKIP_HANDOFFS = {
    "Handoff_PC_to_Cursor_AlphaToBeta_Corpus_Audit_20260604.md",
    "Handoff_Cursor_PC_to_PC_AlphaToBeta_Audit_Verification_20260604.md",
    "Handoff_Cursor_PC_to_PC_AlphaToBeta_Ambiguity_Resolution_20260605.md",
}

LEAVE_PATTERNS = [
    re.compile(r"Pathway\s+\u03b1", re.I),
    re.compile(r"Path\s+\u03b1", re.I),
    re.compile(r"\u03b1_em", re.I),
    re.compile(r"\u03b1_s\b"),
    re.compile(r"a_\{?0\}?\^?\u03b1"),
    re.compile(r"\u03b1_\d\(M_Pl\)"),
    re.compile(r"\u03b1_i\b"),
    re.compile(r"g_\{?\+\}?\^\{\u03b1\u03b2\}"),
    re.compile(r"option\s+\u03b1\)", re.I),
    re.compile(r"\u03b1_NTE\s*→\s*\u03b2"),  # rename docs
    re.compile(r"α_NTE\s*→\s*β"),
]


def tier2_files(nte_root: Path) -> list[Path]:
    out: list[Path] = []
    for sub in ("Working", "Handoffs", "MB"):
        d = nte_root / sub
        if not d.exists():
            continue
        for p in sorted(d.rglob("*.md")):
            if "depreciated" in str(p):
                continue
            if sub == "Handoffs" and p.name in SKIP_HANDOFFS:
                continue
            out.append(p)
    return out


def categorize_flag(ctx: str) -> str:
    for i, rx in enumerate(LEAVE_PATTERNS):
        if rx.search(ctx):
            return f"R{i+1}_LEAVE"
    if re.search(r"H\s*=\s*\u03b1|2\.38|10\^-47|GeV\^-1|M_Pl|characterisation|β_NTE|expansion coefficient", ctx, re.I):
        return "R5_APPLY_BETA"
    if re.search(r"Handoff|audit|rename|β_NTE", ctx, re.I):
        return "R6_HISTORICAL"
    return "R7_PC_REVIEW"


def main():
    apply = "--apply" in sys.argv
    root = Path(__file__).resolve().parent
    nte = root.parent
    files = tier2_files(nte)
    reports = []
    for fp in files:
        r = audit.process_file(fp, apply=apply)
        reports.append(r)

    log_path = root / "alpha_to_beta_audit_log.json"
    prior = []
    if log_path.exists():
        prior = json.loads(log_path.read_text(encoding="utf-8"))

    # resolution summary from prior tier1 ambiguities
    buckets: dict[str, int] = {}
    samples: dict[str, list] = {}
    for entry in prior:
        for a in entry.get("ambiguous", []):
            cat = categorize_flag(a.get("context", ""))
            buckets[cat] = buckets.get(cat, 0) + 1
            if cat not in samples:
                samples[cat] = []
            if len(samples[cat]) < 3:
                samples[cat].append(
                    {
                        "file": Path(entry["path"]).name,
                        "line": a.get("line"),
                        "context": a.get("context", "")[:120],
                    }
                )

    tier2_log = root / "alpha_to_beta_tier2_log.json"
    tier2_log.write_text(
        json.dumps([r.__dict__ for r in reports], indent=2), encoding="utf-8"
    )
    summary = {
        "tier2_files": len(files),
        "tier2_modified": sum(1 for r in reports if r.modified),
        "tier2_subs": sum(r.subs_made for r in reports),
        "tier1_ambiguity_buckets": buckets,
        "tier1_ambiguity_samples": samples,
        "tier1_ambiguity_total": sum(buckets.values()),
    }
    (root / "pc03_ambiguity_resolution_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
