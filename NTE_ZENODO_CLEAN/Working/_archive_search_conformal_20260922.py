#!/usr/bin/env python3
"""Read-only archive search: conformal reset / seed photon. Fast path: text+docx first; PDF optional with timeout."""
from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
import zipfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ARCHIVE = Path(r"C:\Users\gregw\Desktop\NTE_historical_archive")
OUT = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Handoffs\Handoff_Cursor_to_PC_Archive_Search_ConformalReset_20260922.md"
)

SKIP_BASELINE = {"NTFN_v9_5.docx", "NTE_v10_5_9.md"}

TEXT_EXTS = {
    ".md",
    ".txt",
    ".json",
    ".py",
    ".tex",
    ".html",
    ".htm",
    ".yaml",
    ".yml",
    ".log",
    ".ps1",
    ".csv",
}

# Broad rg pattern to prefilter files (then classify in Python)
RG_PATTERN = (
    r"conformal\s+reset|seed\s+photon|trigger\s+photon|T_reset|n_γ|n_gamma|"
    r"photon per Hubble|causal web|topologically unstable|"
    r"Janus\s+point|half[- ] ?photon|conformal\s+class|fractal\s+foam|"
    r"Conformal Cyclic|\bCCC\b|Penrose|Gurzadyan|Hawking point|"
    r"λ/R_H|lambda/R_H|0\.625|3\.92|super-?Planckian|"
    r"conformal rescaling|conformal factor|self-conjugate|"
    r"incomplete transaction|no absorber|Wheeler-Feynman|transactional|"
    r"α_\{n\+1\}|self-reproducing|each photon seeds"
)

CATEGORIES: list[tuple[str, list[re.Pattern[str]]]] = [
    (
        "1 Trigger condition",
        [
            re.compile(r"n_γ|n_\\?gamma|n_gamma", re.I),
            re.compile(r"photon per Hubble volume", re.I),
            re.compile(r"T_reset", re.I),
            re.compile(r"2\.213"),
            re.compile(r"ζ\(3\)|zeta\(3\)|\\zeta\(3\)", re.I),
            re.compile(r"topologically unstable", re.I),
            re.compile(r"causal web", re.I),
        ],
    ),
    (
        "2 Conformal step",
        [
            re.compile(r"Ω²|Omega\^2|\\Omega\^2", re.I),
            re.compile(r"conformal rescaling", re.I),
            re.compile(r"conformal factor", re.I),
            re.compile(r"super-?Planckian", re.I),
            re.compile(r"λ/R_H|lambda/R_H|\\\\lambda/R_H", re.I),
            re.compile(r"\b0\.625\b"),
            re.compile(r"\b3\.92\b"),
            re.compile(r"conformal reset", re.I),
        ],
    ),
    (
        "3 Seed photon",
        [
            re.compile(r"seed photon", re.I),
            re.compile(r"trigger photon", re.I),
            re.compile(r"last electromagnetic mode", re.I),
            re.compile(r"standing wave", re.I),
            re.compile(r"pure information", re.I),
            re.compile(r"conformal class", re.I),
        ],
    ),
    (
        "4 Bilateral seeding / halving",
        [
            re.compile(r"CPN\s*\(\s*γ\s*\)\s*=\s*γ", re.I),
            re.compile(r"self-conjugate", re.I),
            re.compile(r"one quantum seeds two", re.I),
            re.compile(r"photon IS the Janus point|photon is the Janus point", re.I),
            re.compile(r"half[- ]photon|half a photon", re.I),
            re.compile(r"no absorber", re.I),
            re.compile(r"transaction that cannot complete|incomplete transaction", re.I),
        ],
    ),
    (
        "5 Fractal burst",
        [
            re.compile(r"fractal foam", re.I),
            re.compile(r"each photon seeds", re.I),
            re.compile(r"causally disconnected", re.I),
            re.compile(r"\bfractal\b.{0,40}\b(photon|seed|burst|foam)", re.I),
            re.compile(r"\b(photon|seed|burst).{0,40}\bfractal\b", re.I),
        ],
    ),
    (
        "6 α inheritance / recursion",
        [
            re.compile(r"α_\{?n\+1\}?|alpha_\{n\+1\}", re.I),
            re.compile(r"self-reproducing", re.I),
            re.compile(r"fixed point.{0,40}α|α.{0,40}fixed point", re.I),
            re.compile(r"parent.{0,30}daughter|daughter.{0,30}parent", re.I),
            re.compile(r"inherited.{0,40}(α|alpha|fine.?structure)", re.I),
        ],
    ),
    (
        "7 CCC relationship",
        [
            re.compile(r"Conformal Cyclic|\bCCC\b", re.I),
            re.compile(r"\bPenrose\b"),
            re.compile(r"Hawking point", re.I),
            re.compile(r"Gurzadyan", re.I),
            re.compile(r"concentric circles", re.I),
            re.compile(r"previous aeon|\baeon\b", re.I),
        ],
    ),
    (
        "8 Crediting candidates",
        [
            re.compile(r"\bCramer\b"),
            re.compile(r"absorber theory", re.I),
            re.compile(r"Wheeler-Feynman|Wheeler–Feynman", re.I),
            re.compile(r"\btransactional\b", re.I),
            re.compile(r"\bBarbour\b"),
            re.compile(r"\bKoslowski\b"),
            re.compile(r"\bMercati\b"),
            re.compile(r"\bBoyle\b"),
            re.compile(r"\bTurok\b"),
        ],
    ),
    (
        "9 Against / cut / park",
        [
            re.compile(r"not deposited", re.I),
            re.compile(r"withdraw(?:n|al).{0,60}(conformal|seed photon|§V|section V)", re.I),
            re.compile(r"(conformal reset|seed photon).{0,80}(speculative|park(?:ed)?|cut|withdraw)", re.I),
            re.compile(r"(speculative|park(?:ed)?|cut|withdraw).{0,80}(conformal reset|seed photon)", re.I),
            re.compile(r"pressure test.{0,60}(conformal|seed)", re.I),
        ],
    ),
]

DISC_A = re.compile(r"0\.625")
DISC_B = re.compile(r"3\.92")
DISC_CTX = re.compile(r"λ|lambda|R_H|conformal", re.I)


def read_bytes_text(path: Path) -> str | None:
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def read_docx(path: Path) -> str | None:
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="replace")
        text = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", text)
    except Exception:
        return None


def read_pdf(path: Path) -> str | None:
    try:
        import pypdf  # type: ignore

        reader = pypdf.PdfReader(str(path))
        return "\n".join((p.extract_text() or "") for p in reader.pages[:80])
    except Exception:
        return None


def extract_snippet(text: str, match: re.Match[str], radius: int = 160) -> str:
    start = max(0, match.start() - radius)
    end = min(len(text), match.end() + radius)
    snip = text[start:end].replace("\r", "")
    snip = re.sub(r"\n+", " / ", snip)
    snip = re.sub(r"\s+", " ", snip).strip()
    if start > 0:
        snip = "…" + snip
    if end < len(text):
        snip = snip + "…"
    return snip


def mtime_str(path: Path) -> str:
    try:
        return dt.datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")
    except OSError:
        return "?"


def family_key(p: Path) -> str:
    name = re.sub(r"_v[\d_\.]+", "", p.stem, flags=re.I)
    name = re.sub(r"\(\d+\)$", "", name).strip()
    return name.lower()[:80]


def rg_prefilter() -> list[Path]:
    """Use ripgrep to list matching text files quickly."""
    try:
        proc = subprocess.run(
            [
                "rg",
                "-l",
                "-i",
                "--hidden",
                "-g",
                "*.md",
                "-g",
                "*.txt",
                "-g",
                "*.json",
                "-g",
                "*.py",
                "-g",
                "*.tex",
                "-g",
                "*.html",
                "-g",
                "*.yaml",
                "-g",
                "*.yml",
                "-g",
                "*.log",
                "-g",
                "*.ps1",
                RG_PATTERN,
                str(ARCHIVE),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
    except FileNotFoundError:
        return []
    except subprocess.TimeoutExpired:
        return []
    paths = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        p = Path(line)
        if p.name in SKIP_BASELINE:
            continue
        if p.exists():
            paths.append(p)
    return paths


def classify(path: Path, text: str, hits: dict, discrepancy: list) -> None:
    if DISC_A.search(text) and DISC_B.search(text) and DISC_CTX.search(text):
        discrepancy.append(path)
    for cat_name, pats in CATEGORIES:
        bucket: list = []
        for pat in pats:
            n = 0
            for m in pat.finditer(text):
                bucket.append((pat.pattern[:50], extract_snippet(text, m)))
                n += 1
                if n >= 2:
                    break
            if len(bucket) >= 5:
                break
        if bucket:
            hits[cat_name][path] = bucket


def main() -> None:
    if not ARCHIVE.exists():
        OUT.write_text(
            f"# Archive search FAIL\n\nFolder unreachable: `{ARCHIVE}`\n\n— Cursor, 2026-09-22.\n",
            encoding="utf-8",
        )
        print("UNREACHABLE")
        return

    hits: dict[str, dict[Path, list]] = defaultdict(lambda: defaultdict(list))
    discrepancy: list[Path] = []

    print("rg prefilter…")
    rg_files = rg_prefilter()
    print(f"rg hits: {len(rg_files)}")

    # Fallback walk if rg empty
    if not rg_files:
        print("rg empty/unavailable — walking text files…")
        for p in ARCHIVE.rglob("*"):
            if p.is_file() and p.suffix.lower() in TEXT_EXTS and p.name not in SKIP_BASELINE:
                rg_files.append(p)

    # Classify text files from rg (or all if walk)
    # If rg worked, only those; else scan with quick topical check
    for i, path in enumerate(rg_files):
        text = read_bytes_text(path)
        if not text:
            continue
        classify(path, text, hits, discrepancy)
        if (i + 1) % 100 == 0:
            print(f"  text {i+1}/{len(rg_files)}")

    # All docx except baseline
    print("docx…")
    docx_n = 0
    for path in ARCHIVE.rglob("*.docx"):
        if path.name in SKIP_BASELINE:
            continue
        text = read_docx(path)
        if not text:
            continue
        # Only keep if topical-ish
        if not re.search(RG_PATTERN, text, re.I):
            continue
        classify(path, text, hits, discrepancy)
        docx_n += 1
    print(f"docx topical: {docx_n}")

    # PDF with timeout per file (max 8s), only filenames suggesting relevance
    print("pdf (filename-filtered + timeout)…")
    pdf_ok = 0
    pdf_fail = 0
    name_hint = re.compile(
        r"conformal|seed.?photon|NTFN|NTE_v|reset|CCC|Janus|photon", re.I
    )

    def _pdf_job(p: Path) -> tuple[Path, str | None]:
        return p, read_pdf(p)

    pdfs = [
        p
        for p in ARCHIVE.rglob("*.pdf")
        if name_hint.search(p.name) and p.name not in SKIP_BASELINE
    ]
    print(f"pdf candidates: {len(pdfs)}")
    with ThreadPoolExecutor(max_workers=2) as ex:
        for p in pdfs:
            fut = ex.submit(_pdf_job, p)
            try:
                path, text = fut.result(timeout=8)
            except FuturesTimeout:
                pdf_fail += 1
                continue
            except Exception:
                pdf_fail += 1
                continue
            if not text:
                pdf_fail += 1
                continue
            if not re.search(RG_PATTERN, text, re.I):
                continue
            classify(path, text, hits, discrepancy)
            pdf_ok += 1
    print(f"pdf ok={pdf_ok} fail/timeout={pdf_fail}")

    # Write report
    lines: list[str] = []
    lines.append(
        "# Handoff — Cursor → PC: Archive search — conformal reset / seed photon"
    )
    lines.append("")
    lines.append(
        "**From:** Cursor · **To:** Claude_PC · **Cc:** Greg, AC, Jammer · **Date:** 2026-09-22"
    )
    lines.append(
        "**Re:** `Handoff_PC_to_Cursor_Archive_Search_ConformalReset_ReadOnly_20260922.md`"
    )
    lines.append(
        "**Status:** Complete — read-only; no copies/moves into canonical tree."
    )
    lines.append(f"**Search root:** `{ARCHIVE}` (reachable).")
    lines.append(
        f"**Coverage:** ripgrep-prefiltered text ({len(rg_files)} files) + topical `.docx` ({docx_n}) + "
        f"name-filtered `.pdf` ({pdf_ok} extracted, {pdf_fail} timeout/fail). "
        "Baseline skipped: `NTFN_v9_5.docx`, `NTE_v10_5_9.md`."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Live inconsistency flag — λ/R_H = 0.625 vs 3.92")
    lines.append("")
    uniq = sorted(set(discrepancy), key=lambda p: p.stat().st_mtime, reverse=True)
    if uniq:
        lines.append(
            f"**{len(uniq)} non-baseline file(s)** contain both `0.625` and `3.92` with λ/R_H or conformal context:"
        )
        lines.append("")
        for p in uniq[:50]:
            lines.append(f"- `{p.name}` · `{p}` · {mtime_str(p)}")
        if len(uniq) > 50:
            lines.append(f"- … +{len(uniq)-50} more")
    else:
        lines.append("No non-baseline dual-numeral files found in this pass.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for cat_name, _ in CATEGORIES:
        paths = hits[cat_name]
        lines.append(f"## {cat_name}")
        lines.append("")
        if not paths:
            lines.append("*No hits beyond baseline in this pass.*")
            lines.append("")
            continue
        ranked = sorted(paths.keys(), key=lambda p: p.stat().st_mtime, reverse=True)
        families: dict[str, list[Path]] = defaultdict(list)
        for p in ranked:
            families[family_key(p)].append(p)

        lines.append(f"**{len(ranked)} file(s)** with hits.")
        lines.append("")
        shown = 0
        for _fam, members in sorted(
            families.items(),
            key=lambda kv: max(m.stat().st_mtime for m in kv[1]),
            reverse=True,
        ):
            members_sorted = sorted(
                members, key=lambda p: p.stat().st_mtime, reverse=True
            )
            latest = members_sorted[0]
            if len(members_sorted) > 1:
                lines.append(
                    f"### Versions of one document — **latest** `{latest.name}` ({mtime_str(latest)}); "
                    f"{len(members_sorted)} total"
                )
                lines.append(
                    "Also: "
                    + ", ".join(
                        f"`{m.name}` ({mtime_str(m)})" for m in members_sorted[1:5]
                    )
                    + ("…" if len(members_sorted) > 5 else "")
                )
                lines.append("")
                report = [latest]
            else:
                report = [latest]

            for p in report:
                extracts = paths[p][:3]
                lines.append(
                    f"- **`{p.name}`** · `{p}` · modified **{mtime_str(p)}**"
                )
                for _pat, snip in extracts:
                    lines.append(f"  - {snip}")
                lines.append("")
                shown += 1
                if shown >= 30:
                    lines.append(
                        f"*…truncated at 30 families; {len(ranked)} files total in category.*"
                    )
                    lines.append("")
                    break
            if shown >= 30:
                break
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Method notes")
    lines.append("")
    lines.append(
        "- Fast path: `rg -l` prefilter on text types, then Python classification; `.docx` via zip XML; "
        "`.pdf` only if filename hints + 8s extract timeout."
    )
    lines.append(
        "- Categories 5–9 patterns tightened to reduce unrelated fractal/Penrose/credit noise."
    )
    lines.append("- No archive files copied into `NTE_ZENODO_CLEAN`.")
    lines.append("")
    lines.append("— Cursor, 2026-09-22.")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print("wrote", OUT)
    print("disc", len(uniq))
    for cat, _ in CATEGORIES:
        print(f"  {cat}: {len(hits[cat])} files")


if __name__ == "__main__":
    main()
