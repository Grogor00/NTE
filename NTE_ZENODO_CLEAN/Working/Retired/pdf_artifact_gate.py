#!/usr/bin/env python3
"""
Dual-channel PDF artifact gate — text layer + raster sight pack.

Channel A (text): pdftotext full doc + per-locus page extract — mojibake + anchors + reflow.
Channel B (raster): pdftoppm PNG per locus page — shared files for AC human sight + Cursor Read.

Output: Working/PDF_Sight_Calibration/latest/{manifest.json, report.txt, <carrier>/*.png, *.txt}

See Workflow/NTE_PDF_Artifact_Sight_Calibration_v0_1_20260618.md
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
CONFIG_PATH = ROOT / "Working" / "pdf_sight_config.json"

# Shared with cursor_grep_gates.py — PDF text-layer mojibake signatures
MOJIBAKE_RE = re.compile(
    r"â€|\\ufffd|Â(?![a-z])|"
    r"Ãƒâ€šÃ‚Â§|Ã‚Â§|Ãƒâ€|â€šÃ‚Â§|"
    r"ð\u009d[\u0090-\u00bf][\u0080-\u00bf]|"
    r"ð\u009d\u0095\u0086|ð\u009d\u0092¦|"
    r"J₃\(ð|J_3\(ð"
)


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def poppler(cfg: dict, name: str) -> Path:
    base = Path(cfg.get("poppler_bin", ""))
    exe = base / f"{name}.exe"
    if exe.exists():
        return exe
    return Path(name)  # hope on PATH


def page_count(pdfinfo: Path, pdf: Path) -> int:
    r = subprocess.run(
        [str(pdfinfo), str(pdf)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    for line in r.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    return 0


def extract_page(pdftotext: Path, pdf: Path, page: int, out: Path) -> str:
    subprocess.run(
        [str(pdftotext), "-enc", "UTF-8", "-layout", "-f", str(page), "-l", str(page), str(pdf), str(out)],
        check=True,
        capture_output=True,
    )
    return out.read_text(encoding="utf-8", errors="replace")


def extract_full(pdftotext: Path, pdf: Path, out: Path) -> str:
    subprocess.run(
        [str(pdftotext), "-enc", "UTF-8", "-layout", str(pdf), str(out)],
        check=True,
        capture_output=True,
    )
    return out.read_text(encoding="utf-8", errors="replace")


def render_page(pdftoppm: Path, pdf: Path, page: int, prefix: Path) -> Path | None:
    # pdftoppm -png -f N -l N -r 150 input.pdf outprefix  -> outprefix-N.png
    subprocess.run(
        [str(pdftoppm), "-png", "-r", "150", "-f", str(page), "-l", str(page), str(pdf), str(prefix)],
        check=True,
        capture_output=True,
    )
    # poppler names: prefix-01.png (zero-padded)
    candidates = sorted(prefix.parent.glob(f"{prefix.name}-*.png"))
    return candidates[-1] if candidates else None


def find_page_for_locus(
    pdftotext: Path,
    pdf: Path,
    n_pages: int,
    locus: dict,
    tmp_dir: Path,
    full_text: str,
) -> tuple[int | None, str]:
    """Return (page_num, page_text) where locus anchors first match."""
    must_any = locus.get("must_contain_any", [])
    if must_any and not any(a in full_text for a in must_any):
        return None, ""

    hint = locus.get("page_hint")
    page_range = locus.get("page_range")
    if page_range and len(page_range) == 2:
        lo, hi = max(1, page_range[0]), min(n_pages, page_range[1])
        order = list(range(lo, hi + 1))
    elif hint and 1 <= hint <= n_pages:
        order = [hint] + [p for p in range(1, n_pages + 1) if p != hint]
    elif must_any:
        # Estimate page from anchor position in full extract (avoid full-doc scan)
        pos = min(full_text.find(a) for a in must_any if a in full_text)
        est = max(1, min(n_pages, int(pos / max(len(full_text), 1) * n_pages) + 1))
        order = list(range(max(1, est - 2), min(n_pages, est + 2) + 1))
        order += [p for p in range(1, n_pages + 1) if p not in order]
    else:
        order = list(range(1, n_pages + 1))

    for page in order:
        tmp = tmp_dir / f"_scan_p{page:03d}.txt"
        text = extract_page(pdftotext, pdf, page, tmp)
        if must_any:
            if any(a in text for a in must_any):
                return page, text
        else:
            return page, text
    return None, ""


def check_text(text: str, must_any: list[str], must_not: list[str]) -> list[str]:
    hits: list[str] = []
    if MOJIBAKE_RE.search(text):
        hits.append("bad_pattern:mojibake_signature")
    for pat in must_not:
        if not pat:
            continue
        try:
            if re.search(pat, text):
                hits.append(f"must_not:{pat[:40]}")
        except re.error:
            if pat in text:
                hits.append(f"must_not_literal:{pat[:40]}")
    if must_any and not any(a in text for a in must_any):
        hits.append(f"missing_anchor:any_of_{len(must_any)}")
    return hits


def run_carrier(
    key: str,
    spec: dict,
    cfg: dict,
    out_root: Path,
    pdftotext: Path,
    pdftoppm: Path,
    pdfinfo: Path,
) -> dict:
    pdf = ROOT / spec["pdf"]
    md = ROOT / spec.get("md", "")
    carrier_dir = out_root / key
    carrier_dir.mkdir(parents=True, exist_ok=True)

    result: dict = {
        "carrier": key,
        "pdf": str(pdf.relative_to(ROOT)),
        "md": str(md.relative_to(ROOT)) if md.exists() else None,
        "pdf_exists": pdf.exists(),
        "pdf_mtime": pdf.stat().st_mtime if pdf.exists() else None,
        "pdf_size": pdf.stat().st_size if pdf.exists() else None,
        "channels": {"text_full": None, "text_page": None, "raster": None},
        "loci": [],
        "pass": False,
    }

    if not pdf.exists():
        result["error"] = "PDF_MISSING"
        return result

    bad_global = cfg.get("global_bad_patterns", [])  # legacy; MOJIBAKE_RE is authoritative
    reflow = [re.compile(p, re.I) for p in cfg.get("reflow_patterns", [])]
    n_pages = page_count(pdfinfo, pdf)
    result["page_count"] = n_pages

    full_txt_path = carrier_dir / "full_extract.txt"
    full_text = extract_full(pdftotext, pdf, full_txt_path)
    full_hits = check_text(full_text, [], [])
    for rx in reflow:
        for i, ln in enumerate(full_text.splitlines(), 1):
            if rx.search(ln):
                full_hits.append(f"reflow:L{i}:{ln.strip()[:80]}")
    result["channels"]["text_full"] = "PASS" if not full_hits else "FAIL"
    result["text_full_hits"] = full_hits

    all_loci_pass = True
    for locus in spec.get("loci", []):
        lid = locus["id"]
        page, page_text = find_page_for_locus(pdftotext, pdf, n_pages, locus, carrier_dir, full_text)
        locus_hits = []
        if page is None:
            locus_hits.append("page_not_found")
        else:
            locus_hits = check_text(
                page_text,
                locus.get("must_contain_any", []),
                locus.get("must_not_match", []),
            )

        png_path = None
        if page is not None:
            prefix = carrier_dir / lid
            try:
                png_path = render_page(pdftoppm, pdf, page, prefix)
            except subprocess.CalledProcessError as e:
                locus_hits.append(f"raster_fail:{e.stderr.decode(errors='replace')[:80]}")

        page_txt_path = carrier_dir / f"{lid}_p{page or 0:03d}.txt"
        if page_text:
            page_txt_path.write_text(page_text, encoding="utf-8")

        loc_pass = len(locus_hits) == 0 and png_path is not None
        if not loc_pass:
            all_loci_pass = False

        entry = {
            "id": lid,
            "label": locus.get("label", lid),
            "md_snippet": locus.get("md_snippet"),
            "page": page,
            "pass": loc_pass,
            "hits": locus_hits,
            "sight_files": {
                "png": str(png_path.relative_to(ROOT)) if png_path else None,
                "page_text": str(page_txt_path.relative_to(ROOT)) if page_txt_path.exists() else None,
            },
            "ac_visual_checklist": [
                f"Open PNG: {png_path.name if png_path else 'MISSING'}",
                f"Confirm: {locus.get('md_snippet', locus.get('label'))}",
                "Reject if glyphs show ð… byte-soup, missing ⊕, or scrambled table/math order",
            ],
        }
        result["loci"].append(entry)

    text_page_fail = any(not loc["pass"] for loc in result["loci"])
    result["channels"]["text_page"] = "PASS" if not text_page_fail else "FAIL"
    raster_fail = any(loc["sight_files"]["png"] is None for loc in result["loci"])
    result["channels"]["raster"] = "PASS" if not raster_fail else "FAIL"

    result["pass"] = (
        result["channels"]["text_full"] == "PASS"
        and result["channels"]["text_page"] == "PASS"
        and result["channels"]["raster"] == "PASS"
        and all_loci_pass
    )
    return result


def format_report(manifest: dict) -> str:
    lines = [
        "PDF ARTIFACT GATE REPORT",
        f"generated_at: {manifest['generated_at']}",
        f"verdict: {'PASS' if manifest['pass'] else 'FAIL'}",
        "",
        "Channels: text_full + text_page (pdftotext) | raster (pdftoppm PNG sight pack)",
        "AC human sight: open each locus PNG listed below — same files Cursor uses.",
        "",
    ]
    for c in manifest["carriers"]:
        lines.append("=" * 72)
        lines.append(f"## {c['carrier']}  pass={c['pass']}")
        if c.get("error"):
            lines.append(f"  ERROR: {c['error']}")
            continue
        lines.append(f"  pdf: {c['pdf']}  pages={c.get('page_count')}")
        lines.append(f"  text_full: {c['channels']['text_full']}  hits={len(c.get('text_full_hits', []))}")
        for h in c.get("text_full_hits", [])[:8]:
            lines.append(f"    {h}")
        lines.append(f"  text_page: {c['channels']['text_page']}  raster: {c['channels']['raster']}")
        for loc in c["loci"]:
            status = "PASS" if loc["pass"] else "FAIL"
            sf = loc["sight_files"]
            lines.append(f"  [{status}] {loc['id']} p{loc['page']} — {loc['label']}")
            lines.append(f"         PNG: {sf['png']}")
            lines.append(f"         TXT: {sf['page_text']}")
            for h in loc["hits"]:
                lines.append(f"         HIT: {h}")
            lines.append(f"         AC: {loc['ac_visual_checklist'][1]}")
        lines.append("")
    lines.append("=" * 72)
    lines.append(
        "Machine PASS is necessary; AC visual sight on PNGs is still required for publish-block lift."
    )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Dual-channel PDF artifact gate")
    ap.add_argument("--carrier", action="append", help="S2|Part3|Popular (default: all)")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", action="store_true", help="Print manifest JSON to stdout")
    args = ap.parse_args()

    cfg = load_config()
    out_rel = cfg.get("output_dir", "Working/PDF_Sight_Calibration/latest")
    out_root = ROOT / out_rel
    out_root.mkdir(parents=True, exist_ok=True)

    pdftotext = poppler(cfg, "pdftotext")
    pdftoppm = poppler(cfg, "pdftoppm")
    pdfinfo = poppler(cfg, "pdfinfo")

    keys = args.carrier or list(cfg["carriers"].keys())
    carriers_out = []
    for key in keys:
        if key not in cfg["carriers"]:
            print(f"unknown carrier: {key}", file=sys.stderr)
            continue
        carriers_out.append(run_carrier(key, cfg["carriers"][key], cfg, out_root, pdftotext, pdftoppm, pdfinfo))

    manifest = {
        "version": cfg.get("version", 1),
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "config": str(CONFIG_PATH.relative_to(ROOT)),
        "calibration_doc": "Workflow/NTE_PDF_Artifact_Sight_Calibration_v0_1_20260618.md",
        "pass": all(c["pass"] for c in carriers_out),
        "carriers": carriers_out,
    }

    manifest_path = out_root / "manifest.json"
    report_path = out_root / "report.txt"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = format_report(manifest)
    report_path.write_text(report, encoding="utf-8")

    if args.json:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
    elif args.report:
        print(report.encode("ascii", errors="replace").decode("ascii"))
    else:
        v = "PASS" if manifest["pass"] else "FAIL"
        print(f"[{v}] pdf-artifact ({len(carriers_out)} carriers) -> {manifest_path.relative_to(ROOT)}")

    return 0 if manifest["pass"] else 2


if __name__ == "__main__":
    sys.exit(main())
