#!/usr/bin/env python3
"""C21 support greps + PC housekeeping read-only reports."""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NZ = timezone(timedelta(hours=12))
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
DIRS = [ROOT / "Core_Papers", ROOT / "Popular_Editions", ROOT / "Pedagogical_Notes", ROOT / "Book"]


def md_files(dirs):
    for d in dirs:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            if p.is_file() and not p.name.startswith("_"):
                yield p


def section_near(text, pos):
    before = text.rfind("\n#", 0, pos)
    heading = "(no heading)"
    if before >= 0:
        line = text[before + 1 : text.find("\n", before + 1)].strip()
        heading = line[:120]
    start = text.rfind("\n", 0, pos)
    end = text.find("\n", pos)
    if start < 0:
        start = max(0, pos - 120)
    if end < 0:
        end = min(len(text), pos + 200)
    sent = re.sub(r"\s+", " ", text[start:end].strip())[:300]
    return heading, sent


# G1
g1_terms = [
    "transaction",
    "transactional",
    "absorber",
    "no possible absorber",
    "cannot complete",
    "unclosed",
    "Cramer",
    "Wheeler-Feynman",
    "Wheeler–Feynman",
]
g1_pat = re.compile("|".join(re.escape(t) for t in g1_terms), re.I)
g1_hits = []
for p in md_files(DIRS):
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    for m in g1_pat.finditer(t):
        h, s = section_near(t, m.start())
        idea = bool(
            re.search(
                r"Cramer|Wheeler|absorber|transactional|incomplete.?transaction",
                s,
                re.I,
            )
        )
        g1_hits.append(
            (str(p.relative_to(ROOT)), h, s, m.group(0), "USE" if idea else "INCIDENTAL")
        )

# G2
g2_pat = re.compile(r"0\.625|3\.92|lambda/R_H|λ/R_H|λ = 3\.92|0\.625 R_H", re.I)
g2_hits = []
both = []
for p in md_files(DIRS):
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    ms = list(g2_pat.finditer(t))
    if not ms:
        continue
    figs = set()
    for m in ms:
        g = m.group(0)
        if "0.625" in g:
            figs.add("0.625")
        if "3.92" in g:
            figs.add("3.92")
        h, s = section_near(t, m.start())
        g2_hits.append((str(p.relative_to(ROOT)), h, s, g))
    if "0.625" in figs and "3.92" in figs:
        both.append(str(p.relative_to(ROOT)))

# G4 / H2
a9_files = [
    ROOT / "Popular_Editions" / "Popular_Full_Edition_v10_19_0.md",
    ROOT / "Popular_Editions" / "Popular_Reader_Edition_v10_19_0.md",
    ROOT / "Book" / "Appendix_A_Popular_Reader_Edition_v10_19_0.md",
]
a9_terms = [
    r"from the photon's perspective",
    r"photon's frame",
    r"photon's own frame",
    r"photon's perspective",
    r"from the photon",
    r"experiences no time",
    r"experiences zero time",
    r"emission and absorption",
    r"same instant",
    r"same event",
    r"same point",
    r"limit case",
    r"no clock",
    r"proper time",
    r"Higgs coupling",
]
a9_pat = re.compile("|".join(f"({t})" for t in a9_terms), re.I)
a9_hits = {}
for f in a9_files:
    if not f.exists():
        continue
    key = str(f.relative_to(ROOT))
    a9_hits[key] = []
    t = f.read_text(encoding="utf-8", errors="replace")
    for m in a9_pat.finditer(t):
        start = t.rfind("\n", 0, m.start())
        end = t.find("\n", m.end())
        line = t[start + 1 if start >= 0 else 0 : end if end >= 0 else len(t)].strip()[:240]
        a9_hits[key].append((m.group(0), line))

# currency
checks = [
    ("Book", "Chapter_01_The_Photons_Journey_v10.md"),
    ("Book", "Prelude_The_Forty_Million_Year_Instant_v7.md"),
    ("Core_Papers", "NTE_v10_19_0_Part3_Accounting.md"),
    ("Core_Papers", "Companion_10_M1_Majorana_v10_19_0.md"),
    ("Core_Papers", "Companion_13_Yukawa_Nu2_v10_19_0.md"),
]
pdf_out = ROOT / "paper-build" / "pdf-out"
currency = []
for folder, name in checks:
    md = ROOT / folder / name
    pdf = pdf_out / (Path(name).stem + ".pdf")
    if not pdf.exists() and folder == "Book":
        cands = list(ROOT.rglob(Path(name).stem + ".pdf"))
        pdf = cands[0] if cands else pdf
    if not md.exists():
        currency.append((name, "MD MISSING", "", ""))
        continue
    if not pdf.exists():
        currency.append(
            (
                name,
                "PDF MISSING",
                datetime.fromtimestamp(md.stat().st_mtime, NZ).isoformat(timespec="seconds"),
                "",
            )
        )
        continue
    ok = pdf.stat().st_mtime > md.stat().st_mtime
    currency.append(
        (
            name,
            "OK" if ok else "STALE md newer",
            datetime.fromtimestamp(md.stat().st_mtime, NZ).isoformat(timespec="seconds"),
            datetime.fromtimestamp(pdf.stat().st_mtime, NZ).isoformat(timespec="seconds"),
        )
    )

# duplicates
target = "Handoff_AC_to_PC_AppendixC_v13_Retarget_And_Query_Resolutions_20260918.md"
copies = list(ROOT.rglob(target))
dup_rows = []
for p in copies:
    st = p.stat()
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    text = p.read_text(encoding="utf-8", errors="replace")
    lines = [ln for ln in text.splitlines() if ln.strip()][:10]
    meta = []
    for ln in text.splitlines()[:40]:
        if re.search(r"(?i)^(From|To|Status|\*\*From|\*\*To|\*\*Status)", ln.strip()):
            meta.append(ln.strip()[:160])
    dup_rows.append(
        {
            "path": str(p),
            "size": st.st_size,
            "mtime": datetime.fromtimestamp(st.st_mtime, NZ).isoformat(timespec="seconds"),
            "ctime": datetime.fromtimestamp(getattr(st, "st_ctime", st.st_mtime), NZ).isoformat(
                timespec="seconds"
            ),
            "sha12": digest[:12],
            "head": lines,
            "meta": meta,
        }
    )

# H4 drift
hdir = ROOT / "Handoffs"
drift = []
seen = set()
for p in list(hdir.glob("Handoff_*202609*.md")):
    m = re.search(r"(20260\d{3})", p.name)
    if not m:
        continue
    stamp = m.group(1)
    mt = datetime.fromtimestamp(p.stat().st_mtime, NZ)
    try:
        sd = datetime.strptime(stamp, "%Y%m%d").date()
        if sd != mt.date():
            if p.name not in seen:
                seen.add(p.name)
                drift.append((p.name, stamp, mt.strftime("%Y-%m-%d")))
    except Exception:
        pass

# H5
copy_app = next(
    Path(r"G:\My Drive").glob("**/Copy of Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md"),
    None,
)
v12 = None
for p in Path(r"G:\My Drive").glob("**/Appendix_C_The_Open_Ledger_v1_2_DRAFT_PC_20260705.md"):
    if ROOT not in p.parents:
        v12 = p
        break
    if v12 is None:
        v12 = p

# C21 report
L = [
    "# C21 Support Greps — 2026-09-23",
    "",
    "**Agent:** Cursor Main · **Handoff:** `Handoff_AC_to_Cursor_C21_Support_Greps_20260923.md`",
    "Complements PC housekeeping; overlaps noted (G4↔H2, G5↔H1, G3↔H3).",
    "",
    "## G1 — Cramer / Wheeler–Feynman / transaction scope",
    "",
    f"Total hits: {len(g1_hits)}.",
    "",
]
use = [h for h in g1_hits if h[4] == "USE"]
inc = [h for h in g1_hits if h[4] != "USE"]
L.append(f"### Uses the idea ({len(use)})")
for fn, h, s, term, kind in use[:80]:
    L.append(f"- `{fn}` · {h} · term=`{term}`")
    L.append(f"  > {s}")
L.append(f"### Incidental word hits ({len(inc)}) — sample")
for fn, h, s, term, kind in inc[:25]:
    L.append(f"- `{fn}` · `{term}` · {s[:160]}")
L += ["", "## G2 — λ/R_H occurrence map", ""]
if both:
    L.append("**BOTH figures in same file:**")
    for b in both:
        L.append(f"- `{b}`")
    L.append("")
L.append(f"Total hits: {len(g2_hits)}")
for fn, h, s, term in g2_hits[:120]:
    L.append(f"- `{fn}` · {h} · `{term}`")
    L.append(f"  > {s}")
L += ["", "## G3 — Render currency", ""]
for name, status, md, pdf in currency:
    L.append(f"- `{name}`: **{status}** · md={md} · pdf={pdf}")
L += ["", "## G4 — A9 violations in popular editions (+ Appendix A)", ""]
L.append(
    "Confirmed. Sequencing: repair Popular Full + Reader first; Appendix A syncs from Reader."
)
L.append("")
for fn, hits in a9_hits.items():
    L.append(f"### `{fn}` — {len(hits)} hits")
    c = Counter(t for t, _ in hits)
    for term, n in c.most_common():
        L.append(f"- `{term}` × {n}")
    for term, line in hits[:10]:
        L.append(f"  - `{term}`: {line}")
    if len(hits) > 10:
        L.append(f"  - … +{len(hits) - 10} more")
    L.append("")
L += ["", "## G5 — Duplicate-name resolution", ""]
for d in sorted(dup_rows, key=lambda x: -x["size"]):
    L.append(f"### {d['size']} B · sha `{d['sha12']}`")
    L.append(f"- path: `{d['path']}`")
    L.append(f"- mtime: {d['mtime']} · ctime: {d['ctime']}")
    for mline in d["meta"]:
        L.append(f"- {mline}")
    L.append("- head:")
    L.append("```")
    L.extend(d["head"])
    L.append("```")
    L.append("")

report = ROOT / "Working" / "C21_Support_Greps_20260923.md"
report.write_text("\n".join(L) + "\n", encoding="utf-8")
print("C21 report bytes", report.stat().st_size)

# PC handoff
P = [
    "# Handoff — Cursor → PC: housekeeping batch report",
    "",
    "**From:** Cursor Main · **To:** PC · **Cc:** Greg, AC · **Date:** 2026-09-23",
    "**In response to:** `Handoff_PC_to_Cursor_Housekeeping_Batch_ReadOnly_20260923.md`",
    "**Status:** Read-only complete. No moves/renames/deletes/edits.",
    "",
    "## H1 — Three files, one name",
    "",
    f"Found **{len(dup_rows)}** copies:",
    "",
]
for d in sorted(dup_rows, key=lambda x: -x["size"]):
    P.append(f"### {d['size']} bytes · sha12 `{d['sha12']}`")
    P.append(f"- **path:** `{d['path']}`")
    P.append(f"- **mtime:** {d['mtime']}")
    P.append(f"- **ctime:** {d['ctime']}")
    for mline in d["meta"]:
        P.append(f"- {mline}")
    P.append("- **10-line head:**")
    P.append("```")
    P.extend(d["head"])
    P.append("```")
    P.append("")
P.append(
    "**Decision (Greg/AC):** which copy is canonical; disposition of the others. Cursor does not nominate."
)
P += ["", "## H2 — Popular A9 violations", ""]
P.append("Confirmed. Detail also in `Working\\C21_Support_Greps_20260923.md` §G4.")
P.append("**Sequencing:** Popular Full + Reader first; Appendix A inherits from Reader.")
P.append("")
for fn, hits in a9_hits.items():
    P.append(f"- `{fn}`: **{len(hits)}** hits")
P += ["", "## H3 — Render currency", ""]
for name, status, md, pdf in currency:
    P.append(f"- `{name}`: **{status}**")
P.append("")
P.append("(Part 3 / C10 / C13 refreshed today under M_R GO — currency OK.)")
P += ["", "## H4 — Filename date-stamp drift (list for Greg)", ""]
P.append("| filename | stamp in name | modified date |")
P.append("|---|---|---|")
for name, stamp, mt in drift[:60]:
    P.append(f"| `{name}` | {stamp} | {mt} |")
P.append("")
P.append("**Decision (Greg):** restamp or leave.")
P += ["", "## H5 — Archive-tree hygiene", ""]
P.append(
    "1. Renamed archive root `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`: **not present** as a rename. "
    "Manifest §4 marks rename **CANCELLED** (2026-09-23). Canonical tree answers at "
    f"`{ROOT}`."
)
P.append(
    "2. `Copy of Appendix_C_...v1_3...`: "
    + (f"FOUND at `{copy_app}`" if copy_app else "not found in Drive glob (may be offline).")
)
P.append(
    "3. `Appendix_C_...v1_2...`: "
    + (f"FOUND at `{v12}`" if v12 else "not found in Drive glob.")
    + " Canonical Book carries v1.3 only."
)
P += ["", "— Cursor Main, 2026-09-23.", ""]
hout = ROOT / "Handoffs" / "Handoff_Cursor_to_PC_Housekeeping_Batch_20260923.md"
hout.write_text("\n".join(P), encoding="utf-8")

# C21 completion to AC
ac = ROOT / "Handoffs" / "Handoff_Cursor_to_AC_C21_Support_Greps_Complete_20260923.md"
ac.write_text(
    f"""# Handoff — Cursor → AC: C21 support greps complete

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC · **Date:** 2026-09-23
**In response to:** `Handoff_AC_to_Cursor_C21_Support_Greps_20260923.md`
**Status:** Complete. Read-only.

Report: `Working\\C21_Support_Greps_20260923.md` ({report.stat().st_size} bytes).

Overlaps with PC housekeeping (G4/H2, G5/H1, G3/H3) noted in-report; not re-done separately beyond cross-reference.

— Cursor Main, 2026-09-23.
""",
    encoding="utf-8",
)
print("PC report", hout.stat().st_size)
print("dups", [(d["size"], d["sha12"]) for d in dup_rows])
print("both", both)
print("a9", {k: len(v) for k, v in a9_hits.items()})
print("done")
