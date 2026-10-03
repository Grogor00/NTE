#!/usr/bin/env python3
"""Apply Scratch references triage: REF->References/, DEL+DUP->delete, REV->leave."""
from __future__ import annotations

import csv
import shutil
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\Desktop\NTE_ZENODO_CLEAN")
POTENTIAL = ROOT / "potential"
REFERENCES = ROOT / "References"
CSV_PATH = POTENTIAL / "References_Triage_potential_20260705.csv"
REPORT = ROOT / "Working" / "references_triage_apply_report_20260705.json"

REFERENCES.mkdir(exist_ok=True)

moved: list[str] = []
deleted: list[dict] = []
left: list[str] = []
missing: list[dict] = []
errors: list[dict] = []

with CSV_PATH.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    title = row["title"].strip()
    disp = row["disp"].strip()
    dup = (row.get("dup") or "").strip()
    src = POTENTIAL / title
    if not src.exists():
        missing.append({"disp": disp, "title": title, "reason": "not found"})
        continue
    try:
        if disp == "REF" and not dup:
            dst = REFERENCES / title
            if dst.exists():
                errors.append({"title": title, "error": "already in References"})
            else:
                shutil.move(str(src), str(dst))
                moved.append(title)
        elif disp == "DEL" or dup:
            src.unlink()
            deleted.append({"title": title, "reason": "DEL" if disp == "DEL" else dup})
        elif disp == "REV":
            left.append(title)
        else:
            errors.append({"title": title, "error": f"unknown disp={disp}"})
    except OSError as e:
        errors.append({"title": title, "error": str(e)})

remaining_pdfs = sorted(p.name for p in POTENTIAL.iterdir() if p.is_file() and p.suffix.lower() == ".pdf")
ref_pdfs = sorted(p.name for p in REFERENCES.iterdir() if p.is_file() and p.suffix.lower() == ".pdf")

report = {
    "moved_to_References": len(moved),
    "deleted": len(deleted),
    "left_REV_in_potential": len(left),
    "missing": len(missing),
    "errors": len(errors),
    "remaining_pdfs_in_potential": len(remaining_pdfs),
    "pdfs_in_References": len(ref_pdfs),
    "moved": moved,
    "deleted": deleted,
    "left": left,
    "missing": missing,
    "errors": errors,
    "remaining_pdfs": remaining_pdfs,
}
import json
REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({k: report[k] for k in ("moved_to_References", "deleted", "left_REV_in_potential", "missing", "errors", "remaining_pdfs_in_potential", "pdfs_in_References")}, indent=2))
