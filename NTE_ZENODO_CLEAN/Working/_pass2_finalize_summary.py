#!/usr/bin/env python3
"""Rewrite Pass2 summary compactly; update handoff + manifest."""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NZ = timezone(timedelta(hours=12))
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
W = ROOT / "Working"
WC = ROOT / "Working candidates"
SUMMARY = W / "Working_Candidates_Triage_Pass2_Summary_20260922.md"
MOVES = W / "Working_Candidates_Triage_Pass2_Moves_20260922.csv"
HANDOFF = ROOT / "Handoffs" / "Handoff_Cursor_to_AC_Working_Candidates_Triage_Pass2_Complete_20260922.md"
MANIFEST = ROOT / "NTE_Workflow_Manifest_v10_18.md"

P1 = [
    "prepare_paper_pdf.py",
    "prepare_master_pdf.py",
    "strip_publication_tail.py",
    "strip_corpus_metadata.py",
]

rows = list(csv.DictReader(MOVES.open(encoding="utf-8")))
to_ret = sum(1 for r in rows if "Retired" in r["destination"])
to_w = sum(1 for r in rows if r["destination"] == "Working\\")
rule_c = Counter(r["rule"].split(" (")[0] for r in rows)

keep_files = sorted([p for p in W.iterdir() if p.is_file()], key=lambda p: p.name.lower())
cand_left = len([p for p in WC.rglob("*") if p.is_file()]) if WC.exists() else 0

MR = re.compile(
    r"8\.2.{0,30}(?:10\^\{?14\}?|10¹⁴|×10\^14|e14)|(?:10\^\{?14\}?|10¹⁴|×10\^14|e14).{0,30}8\.2",
    re.I | re.S,
)
mr_hits = []
for p in keep_files:
    if p.suffix.lower() not in {".md", ".txt", ".py"} or p.stat().st_size > 2_000_000:
        continue
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    if not MR.search(t):
        continue
    for i, ln in enumerate(t.splitlines(), 1):
        if "8.2" in ln and re.search(r"10\^|10¹|e14|×10", ln):
            mr_hits.append((p.name, i, ln.strip()[:200]))
            break

tilde = [r for r in rows if "~" in r["filename"]]
now = datetime.now(NZ).strftime("%Y-%m-%d %H:%M %Z")
aug = datetime(2026, 8, 1, tzinfo=NZ).timestamp()

L = []
L += [
    "# Working Candidates Triage — Pass 2 Summary (2026-09-22)",
    "",
    f"**Agent:** Cursor Main · **Generated:** {now}",
    "**Handoff:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_Pass2_20260922.md`",
    "",
    "## Correction acknowledged",
    "",
    "Pass-1 \"render-blocking / restore to paper-build\" finding is **withdrawn** (AC error). "
    "Live strip/prepare scripts live in `Working\\`. `__pycache__` left alone. No restore to `paper-build\\`.",
    "",
    "## P1 — derived render-pipeline protect list",
    "",
    "From `paper-build\\render-all-clean.ps1` + imports of `prepare_paper_pdf.py` / `prepare_master_pdf.py`:",
]
for n in P1:
    L.append(f"- `Working\\{n}`")
L += [
    "",
    "## Counts",
    "",
    f"**moved to Working (from candidates):** {to_w} · **moved to Retired:** {to_ret} · **held:** 0",
    f"`Working candidates\\` files remaining: **{cand_left}** (folder left in place).",
    f"`Working\\` top-level files now: **{len(keep_files)}**.",
    "",
    "### Counts per rule (moves)",
    "",
]
for rule, c in rule_c.most_common(40):
    L.append(f"- {rule}: {c}")
L += [
    "",
    "## KEEP — `Working\\` top-level after Pass 2",
    "",
]
for p in keep_files:
    tag = ""
    if p.name in P1:
        tag = " [P1]"
    elif p.stat().st_mtime >= aug:
        tag = " [P3/post-Aug]"
    L.append(f"- `{p.name}`{tag}")
L += ["", "## K2 — M_R trace (8.2 × 10¹⁴)", ""]
if not mr_hits:
    L.append("**no occurrence of 8.2 × 10¹⁴ found in Working top-level after Pass 2**")
else:
    L.append(f"Found **{len(mr_hits)}** file(s) with an 8.2↔10¹⁴ adjacency (first matching line each):")
    for fn, i, t in mr_hits[:25]:
        L.append(f"- `{fn}`:{i}: `{t}`")
    if len(mr_hits) > 25:
        L.append(f"- … +{len(mr_hits) - 25} more")
L += [
    "",
    "## K6 — cursor_task_ledger.json",
    "",
    "Monitoring lane reads `Working\\.cursor_handoff_watch_state.json`, **not** `cursor_task_ledger.json`. Ledger retired (D7).",
    "",
    "**Greg flag — corrupt.bak:** At Pass-1 inventory, `Working candidates\\cursor_task_ledger.json.corrupt.bak` was ~1.93 GB. "
    "At Pass-2 apply time the file was **already gone** from the tree (not in candidates, Working, or Retired). "
    "Not moved by Cursor. Please check Drive trash / version history and delete if it reappears.",
    "",
    "## Tilde / short-name identification (all retired)",
    "",
    f"Tilde/`~` files moved: **{len(tilde)}**. Sample:",
    "",
    "| short name | rule |",
    "|---|---|",
]
for r in tilde[:25]:
    L.append(f"| `{r['filename']}` | {r['rule']} |")
if len(tilde) > 25:
    L.append(f"| … | +{len(tilde) - 25} more in CSV |")
L += [
    "",
    "## HOLD list",
    "",
    "**(none)** — Pass-2 cleanup retracted the over-broad D2 Part-3 full-text guard. "
    "Re-checked against Part 3 §Open work + manifest §10 In-progress/Open only; no K/D conflicts remained. "
    "Candidate twins of live P1 scripts (different SHA) retired — Working copies win.",
    "",
    "## K4 stale register",
    "",
    "Kept in Working (currency pass needed before use): `NTE_Reader_Glossary_Companion_v1_0.md`; "
    "`NTE_FAQ_Supplement_DRAFT_v0_2_*` (see manifest §10).",
    "",
    "## Pass 1 report",
    "",
    "Retired to `Working\\Retired\\Working_Candidates_Triage_Report_20260922.md`.",
    "",
]
SUMMARY.write_text("\n".join(L), encoding="utf-8")
print("summary_bytes", SUMMARY.stat().st_size)

p1_joined = ", ".join(f"`Working\\{n}`" for n in P1)
hand = f"""# Handoff — Cursor → AC: Working-candidates triage Pass 2 complete

**From:** Cursor Main · **To:** AC · **Cc:** Greg · **Date:** 2026-09-22
**In response to:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_Pass2_20260922.md`
**Status:** Complete. Held = 0 (≤25).

## Correction

Pass-1 restore-to-`paper-build` finding withdrawn. No restore. `__pycache__` left alone.

## Deliverables

- `Working\\Working_Candidates_Triage_Pass2_Summary_20260922.md` ({SUMMARY.stat().st_size} bytes)
- `Working\\Working_Candidates_Triage_Pass2_Moves_20260922.csv` ({len(rows)} move rows)
- Pass 1 report → `Working\\Retired\\`

## Totals

**moved to Working:** {to_w} · **moved to Retired:** {to_ret} · **held:** 0
`Working candidates\\` file count now **{cand_left}** (folder not removed).

## P1 pipeline list

{p1_joined}

## Notes

- Candidate copies of `prepare_*.py` / `strip_publication_tail.py` differed from live Working copies → retired (Working wins).
- D2 guard cleaned up: initial full-Part-3 scan over-held 56 files; re-check against Open work + §10 open/in-progress → all retired.
- **Greg:** `cursor_task_ledger.json.corrupt.bak` (~1.93 GB) seen at Pass-1 inventory but absent at Pass-2 apply — check Drive trash; delete if present.

— Cursor Main, 2026-09-22.
"""
HANDOFF.write_text(hand, encoding="utf-8")

man = MANIFEST.read_text(encoding="utf-8")
man = re.sub(
    r"- Working-candidates triage 2026-09-22[^\n]*",
    "- Working-candidates triage 2026-09-22 Pass 2 — 0 held; summary at `Working\\Working_Candidates_Triage_Pass2_Summary_20260922.md`.",
    man,
    count=1,
)
man = re.sub(
    r"(\*\*Last updated\.\*\*\s*)([^\n]+)",
    r"\g<1>2026-09-22 — §10: Working-candidates Pass 2 complete (0 held; candidates emptied). Prior: \2",
    man,
    count=1,
)
MANIFEST.write_text(man, encoding="utf-8")
print("done")
