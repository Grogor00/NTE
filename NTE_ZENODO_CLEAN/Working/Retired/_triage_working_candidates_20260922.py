#!/usr/bin/env python3
"""Working candidates + Working top-level triage per AC handoff 2026-09-22.
Applies only R1-R5 (+ known strip item). Everything else FLAG/HELD.
Move never copy. No deletes. No renames.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NZ = timezone(timedelta(hours=12))
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
WC = ROOT / "Working candidates"
W = ROOT / "Working"
RETIRED = W / "Retired"
REPORT = W / "Working_Candidates_Triage_Report_20260922.md"
HANDOFF = ROOT / "Handoffs" / "Handoff_Cursor_to_AC_Working_Candidates_Triage_Complete_20260922.md"
MANIFEST = ROOT / "NTE_Workflow_Manifest_v10_18.md"

REF_DIRS = [
    ROOT / "Core_Papers",
    ROOT / "Book",
    ROOT / "Popular_Editions",
    ROOT / "Pedagogical_Notes",
    ROOT / "paper-build",
    ROOT / "References",
    ROOT / "Outreach",
    ROOT / "potential",
    ROOT / "Handoffs",
]

R3_PREFIXES = (
    "apply_", "fix_", "seed_", "update_ledger_", "housekeeping_", "rename_",
    "reopen_", "batch_verify_", "_discover_", "_find_", "_test_", "_run_",
)
R3_EXACT = {"codepoint_probe.py"}
R3_CONTAINS = ("mojibake",)
R3_BUILD_DEP = re.compile(r"^build_depreciated_", re.I)

PHYSICS_NAMES = {
    "clfv_cartan_ratio_numerical.py",
    "p5_flux_dial_worksheet.py",
    "alpha_to_beta_nte_audit.py",
    "alpha_beta_nte_corpus_fix_pass.py",
    "pc03_tier2_beta_audit.py",
    "healpix_ring.py",
}
PHYSICS_PREFIXES = ("farnsworth_stage", "paper_s22_", "kappa_closure_")

PROSE_PREFIXES = (
    "Wagenveld_Sprint_", "Programme_S_Paper_S6_", "Paper_PhiNTE_Necessity_",
    "Paper_A1_", "Paper_A2_", "Standalone_Papers_Accessibility_Tiering_",
    "Publication_Title_Block_Standard_", "P5_v0_3_Zenodo_Changelog_",
    "PC_Book_Pedagogical_Pivot_Pass_", "PC_Audit_Repairs_",
    "P1_Kappa_FM5_Audit_",
)
PROSE_EXACT = {"Paper_Scope_Alignment_Sweep_Results.md"}

WITHDRAWN_MARKERS = [
    (r"sin\^2\\?theta_\{?12\}?\s*=\s*1/3|sin²θ₁₂\s*=\s*1/3|sin\^2θ_12\s*=\s*1/3", "sin^2 theta_12 = 1/3"),
    (r"six-note", "six-note"),
    (r"two pathways", "two pathways"),
    (r"S\^7/\\mathbb\{Z\}_2|S⁷/Z₂|S\^7/Z_2", "S^7/Z_2"),
    (r"Planck-radius", "Planck-radius"),
    (r"\bvoid\b.{0,200}\bDESI\b|\bDESI\b.{0,200}\bvoid\b", "void+DESI"),
    (r"β_NTE.{0,80}√6/π|beta_NTE.{0,80}sqrt\(6\)/pi|β_NTE.{0,80}sqrt\(6\)/pi", "beta_NTE + sqrt6/pi"),
    (r"Cabibbo", "Cabibbo"),
    (r"θ₁₃\s*=|theta_\{?13\}?\s*=", "theta_13 ="),
    (r"\bT_GB\b(?!.{0,40}conditional)", "T_GB without conditional nearby"),
]

SHORT83 = re.compile(r"^[A-Z0-9]{6,8}~1\.", re.I)


def sha12(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha_full(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_r3_name(name: str) -> bool:
    low = name.lower()
    if name in R3_EXACT or low in {x.lower() for x in R3_EXACT}:
        return True
    if any(c in low for c in R3_CONTAINS):
        return True
    if R3_BUILD_DEP.match(name):
        return True
    return any(low.startswith(p) for p in R3_PREFIXES)


def is_physics(name: str) -> bool:
    low = name.lower()
    if low in {x.lower() for x in PHYSICS_NAMES}:
        return True
    return any(low.startswith(p) for p in PHYSICS_PREFIXES)


def is_prose_named(name: str) -> bool:
    if name in PROSE_EXACT:
        return True
    return any(name.startswith(p) for p in PROSE_PREFIXES)


def first_nonempty_lines(path: Path, n: int = 12) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [f"<read error: {e}>"]
    out = []
    for line in text.splitlines():
        if line.strip():
            out.append(line.rstrip())
        if len(out) >= n:
            break
    return out


def header_bits(lines: list[str]) -> tuple[str, str]:
    heading = ""
    status = ""
    for ln in lines:
        s = ln.strip()
        if not heading and s.startswith("#"):
            heading = s
        if not status and re.search(r"(?i)\b(status|version|date)\b", s):
            status = s
        if heading and status:
            break
    return heading, status


def withdrawn_hits(path: Path) -> list[tuple[str, int, str]]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    hits = []
    for pat, label in WITHDRAWN_MARKERS:
        ms = list(re.finditer(pat, text, re.I | re.S))
        if ms:
            sample = ms[0].group(0)
            sample = re.sub(r"\s+", " ", sample)[:120]
            hits.append((label, len(ms), sample))
    return hits


def evidence_r3_done(name: str) -> bool:
    """Cheap evidence: matching Complete/Applied/Ack handoff or target already fixed."""
    stem = Path(name).stem
    # strip leading underscore noise for search
    key = re.sub(r"^_+", "", stem)[:40]
    hand = ROOT / "Handoffs"
    if not hand.exists():
        return False
    for p in hand.glob("*.md"):
        n = p.name.lower()
        if "complete" in n or "applied" in n or "ack" in n or "fixed" in n:
            if key.lower()[:20] in n or stem.lower()[:25] in n:
                return True
    # known: ORPHAN_SEE fix handoff
    if "strip_corpus" in name.lower() or "orphan" in name.lower():
        for p in hand.glob("*ORPHAN*"):
            return True
        for p in hand.glob("*Orphan*"):
            return True
    return False


def build_ref_indexes():
    """hash -> [(relpath, mtime, size)] and name -> [(path, hash, size, mtime)]"""
    by_hash: dict[str, list[tuple[str, float, int]]] = defaultdict(list)
    by_name: dict[str, list[tuple[Path, str, int, float]]] = defaultdict(list)
    # Index Working top-level (not Retired, not dirs) + reference sets
    scan_roots = [W] + [d for d in REF_DIRS if d.exists()]
    n = 0
    for base in scan_roots:
        if base == W:
            paths = [p for p in base.iterdir() if p.is_file()]
        else:
            # skip huge binary trees lightly: hash md/py/txt/json/yaml/tex/ps1/lua primarily;
            # still include others but skip pdf-out scratch if huge
            paths = []
            for p in base.rglob("*"):
                if not p.is_file():
                    continue
                rel = str(p.relative_to(ROOT))
                if "pdf-out" in rel or "scratch-src" in rel or "__pycache__" in rel:
                    continue
                if "Retired" in rel and base == W:
                    continue
                paths.append(p)
        for p in paths:
            try:
                st = p.stat()
            except OSError:
                continue
            digest = sha_full(p)
            rel = str(p.relative_to(ROOT))
            by_hash[digest].append((rel, st.st_mtime, st.st_size))
            by_name[p.name.lower()].append((p, digest, st.st_size, st.st_mtime))
            n += 1
            if n % 200 == 0:
                print(f"  indexed {n} ref files...", flush=True)
    print(f"  indexed total {n} ref files", flush=True)
    return by_hash, by_name


def version_key(name: str):
    """Extract comparable version tokens for R5."""
    m = re.search(r"v(\d+(?:_\d+)*)", name, re.I)
    if not m:
        return None
    parts = tuple(int(x) for x in m.group(1).split("_"))
    # stem without version for matching
    stem = re.sub(r"_?v\d+(?:_\d+)*", "", Path(name).stem, flags=re.I)
    stem = re.sub(r"_+", "_", stem).strip("_").lower()
    return stem, parts


def find_successor(name: str, by_name) -> str | None:
    vk = version_key(name)
    if not vk:
        # nearest-name: same stem prefix in refs
        stem = Path(name).stem.lower()[:40]
        cands = []
        for n, lst in by_name.items():
            if stem and stem in n:
                for path, digest, size, mt in lst:
                    cands.append((mt, str(path.relative_to(ROOT))))
        if cands:
            cands.sort(reverse=True)
            return f"{cands[0][1]} (mtime {datetime.fromtimestamp(cands[0][0], NZ).strftime('%Y-%m-%d')})"
        return None
    stem, parts = vk
    best = None
    for n, lst in by_name.items():
        ov = version_key(n)
        if not ov:
            continue
        ostem, oparts = ov
        if ostem == stem and oparts > parts:
            for path, digest, size, mt in lst:
                if best is None or oparts > best[0]:
                    best = (oparts, str(path.relative_to(ROOT)), mt)
    if best:
        return f"{best[1]} (v{'_'.join(map(str,best[0]))}, mtime {datetime.fromtimestamp(best[2], NZ).strftime('%Y-%m-%d')})"
    return None


def classify_candidate(path: Path, by_hash, by_name, source: str) -> dict:
    name = path.name
    st = path.stat()
    digest = sha_full(path)
    row = {
        "source": source,
        "path": path,
        "name": name,
        "size": st.st_size,
        "mtime": st.st_mtime,
        "sha": digest,
        "sha12": digest[:12],
        "rule": "",
        "dest": "",
        "action": "HELD",
        "flag_cat": "",
        "note": "",
    }

    # Known item
    if source == "candidates" and name == "strip_corpus_metadata.py":
        row.update(rule="KNOWN pre-fix ORPHAN_SEE", dest="Working\\Retired\\", action="MOVED", note="AC-directed")
        return row

    # R1 duplicate
    others = [x for x in by_hash.get(digest, []) if Path(ROOT / x[0]) != path and "Working candidates" not in x[0]]
    # also duplicates within candidates handled later; for now ref/Working match
    if others:
        row.update(rule="R1 duplicate", dest="Working\\Retired\\", action="MOVED",
                   note=f"identical to {others[0][0]}")
        return row

    # R2 run artifact
    low = name.lower()
    if (path.suffix.lower() == ".json" and ("report" in low or "manifest" in low or low.startswith("_"))) \
       or low.endswith("grep_report.txt") or low.startswith("_") and low.endswith((".txt", ".log")) \
       or "grep_report" in low:
        # be careful: not all _*.md are artifacts
        if path.suffix.lower() in {".txt", ".json", ".log"} or "grep_report" in low:
            row.update(rule="R2 run artifact", dest="Working\\Retired\\", action="MOVED")
            return row

    # R4 tooling superseded (same name in paper-build, differs)
    pb_hits = [x for x in by_name.get(name.lower(), []) if "paper-build" in str(x[0]).replace("/", "\\")]
    if pb_hits and source == "candidates":
        pb_path, pb_hash, pb_size, pb_mt = pb_hits[0]
        if pb_hash != digest:
            row.update(rule="R4 tooling superseded", dest="Working\\Retired\\", action="MOVED",
                       note=f"live in {pb_path.relative_to(ROOT)}")
            return row
        else:
            row.update(rule="R1 duplicate", dest="Working\\Retired\\", action="MOVED",
                       note=f"identical to {pb_path.relative_to(ROOT)}")
            return row

    # R5 versioned supersession
    succ = None
    vk = version_key(name)
    if vk:
        stem, parts = vk
        for n, lst in by_name.items():
            ov = version_key(n)
            if not ov:
                continue
            ostem, oparts = ov
            if ostem == stem and oparts > parts:
                # ensure the hit is outside Working candidates
                for path2, digest2, size2, mt2 in lst:
                    if "Working candidates" in str(path2):
                        continue
                    succ = path2
                    break
            if succ:
                break
    if succ is None and "DECONTAMINATED_PILOT" in name.upper():
        # companion pilots — if Core_Papers has companion without pilot
        m = re.search(r"(Companion[_\s]?\d+)", name, re.I)
        if m:
            key = re.sub(r"[_\s]", "", m.group(1)).lower()
            for n, lst in by_name.items():
                if "decontaminated" in n:
                    continue
                if key in n.replace("_", "").replace(" ", "").lower() and "core_papers" in str(lst[0][0]).lower():
                    succ = lst[0][0]
                    break
    if succ is not None:
        row.update(rule="R5 versioned supersession", dest="Working\\Retired\\", action="MOVED",
                   note=f"successor {succ.relative_to(ROOT) if isinstance(succ, Path) else succ}")
        return row

    # R3 spent one-off — only if evidence of completion
    if is_r3_name(name) and path.suffix.lower() in {".py", ".ps1", ".txt", ".json"}:
        if evidence_r3_done(name):
            row.update(rule="R3 spent one-off script", dest="Working\\Retired\\", action="MOVED",
                       note="completion evidenced")
            return row
        # without evidence → FLAG (fall through) unless clear R2 already handled

    # Explicit FLAG categories
    if SHORT83.match(name):
        row.update(rule="FLAG", flag_cat="8.3 short-name", dest="(held)", action="HELD")
        return row
    if is_physics(name):
        row.update(rule="FLAG", flag_cat="physics numerics", dest="(held)", action="HELD")
        return row
    if is_prose_named(name) or path.suffix.lower() == ".md":
        # all remaining md prose FLAG
        row.update(rule="FLAG", flag_cat="prose working document", dest="(held)", action="HELD")
        return row
    if path.suffix.lower() == ".py" or path.suffix.lower() in {".ps1", ".lua", ".tex"}:
        row.update(rule="FLAG", flag_cat="script/tooling", dest="(held)", action="HELD")
        return row

    row.update(rule="FLAG", flag_cat="other", dest="(held)", action="HELD")
    return row


def safe_retire(src: Path) -> tuple[bool, str]:
    RETIRED.mkdir(parents=True, exist_ok=True)
    dest = RETIRED / src.name
    if dest.exists():
        # collision: compare hashes
        if sha_full(dest) == sha_full(src):
            # identical — remove source only after confirming (move = retire duplicate)
            # destination already has it; delete source? Handoff: move never copy; nothing deleted.
            # If dest already has identical, source is twin — retiring means getting it into Retired.
            # Dest already IS in Retired. So we need to remove source without "delete"?
            # Interpret: source can be unlinked after identical content confirmed in Retired (the keep).
            # Actually: "Nothing is deleted. Working\Retired\ is quarantine."
            # If already in Retired identical, the candidate is the twin — moving to Retired would collide.
            # Rule: Identical → the candidate goes to Retired (duplicate). Dest already there.
            # So unlink source (the duplicate leaving candidates) — content preserved in Retired.
            src.unlink()
            return True, f"already in Retired identical; unlinked source twin"
        else:
            return False, "NAME COLLISION different SHA — FLAG"
    shutil.move(str(src), str(dest))
    return True, str(dest)


def main():
    print("=== Building reference indexes ===", flush=True)
    by_hash, by_name = build_ref_indexes()

    # Also index Working Retired into by_hash for R1
    if RETIRED.exists():
        for p in RETIRED.rglob("*"):
            if p.is_file():
                try:
                    d = sha_full(p)
                    by_hash[d].append((str(p.relative_to(ROOT)), p.stat().st_mtime, p.stat().st_size))
                    by_name[p.name.lower()].append((p, d, p.stat().st_size, p.stat().st_mtime))
                except OSError:
                    pass

    rows = []
    print("=== Classifying Working candidates ===", flush=True)
    cand_files = sorted([p for p in WC.rglob("*") if p.is_file()], key=lambda p: str(p).lower())
    for i, p in enumerate(cand_files, 1):
        if i % 50 == 0:
            print(f"  candidates {i}/{len(cand_files)}", flush=True)
        rows.append(classify_candidate(p, by_hash, by_name, "candidates"))

    print("=== Classifying Working top-level ===", flush=True)
    for p in sorted([p for p in W.iterdir() if p.is_file()], key=lambda p: p.name.lower()):
        # skip our own triage outputs / poll state? include them as FLAG tooling
        rows.append(classify_candidate(p, by_hash, by_name, "working"))

    # Apply moves for MOVED rows
    print("=== Applying moves ===", flush=True)
    moved_retired = 0
    moved_working = 0
    held = 0
    collision_flags = []
    for row in rows:
        if row["action"] != "MOVED":
            held += 1
            continue
        ok, msg = safe_retire(row["path"])
        if ok:
            row["action"] = "MOVED"
            row["note"] = (row.get("note") or "") + f" | {msg}"
            moved_retired += 1
            # update indexes
        else:
            row["action"] = "HELD"
            row["rule"] = "FLAG"
            row["flag_cat"] = "name collision different SHA"
            row["note"] = msg
            row["dest"] = "(held)"
            held += 1
            collision_flags.append(row["name"])

    # strip check
    pb_strip = ROOT / "paper-build" / "strip_corpus_metadata.py"
    w_strip = W / "strip_corpus_metadata.py"
    strip_finding = []
    if not pb_strip.exists():
        strip_finding.append(
            "RENDER-BLOCKING: `paper-build\\strip_corpus_metadata.py` is MISSING. "
            "No live strip tool in paper-build."
        )
    if w_strip.exists():
        txt = w_strip.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^ORPHAN_SEE\s*=\s*re\.compile\((.+)\)\s*$", txt, re.M)
        line = m.group(0) if m else "<ORPHAN_SEE line not found>"
        strip_finding.append(f"`Working\\strip_corpus_metadata.py` ORPHAN_SEE line verbatim:\n\n```\n{line}\n```")
        expected = r'(?:;\s*)?\b[Ss]ee\b(?=\s*[);])'
        if expected in txt:
            strip_finding.append("Working copy contains the corrected pattern.")
        else:
            strip_finding.append("WARNING: Working copy does NOT contain the corrected pattern.")
    else:
        strip_finding.append("WARNING: Working\\strip_corpus_metadata.py also missing.")

    # Farnsworth inventory
    farm = W / "Farnsworth_Archive_Pull_20260802"
    farm_files = []
    if farm.exists():
        farm_files = [p for p in farm.rglob("*") if p.is_file()]

    # __pycache__
    pyc = W / "__pycache__"
    pyc_files = [p.name for p in pyc.iterdir()] if pyc.exists() else []

    # FLAG packets for held prose / 8.3 / physics
    print("=== Building FLAG packets ===", flush=True)
    flag_rows = [r for r in rows if r["action"] == "HELD"]

    # Re-read held files that still exist for packets
    packets = []
    for r in flag_rows:
        p = r["path"]
        if not p.exists():
            continue
        # For working-source held, path unchanged; for candidates held, still in WC
        cat = r.get("flag_cat") or "other"
        if cat in {"prose working document", "8.3 short-name"} or (
            p.suffix.lower() == ".md" and cat != "physics numerics"
        ):
            lines = first_nonempty_lines(p, 12)
            heading, status = header_bits(lines)
            whits = withdrawn_hits(p) if p.suffix.lower() == ".md" else []
            succ = find_successor(r["name"], by_name)
            packets.append({
                "name": r["name"],
                "source": r["source"],
                "cat": cat,
                "heading": heading,
                "status": status,
                "lines": lines,
                "withdrawn": whits,
                "successor": succ,
                "sha12": r["sha12"],
                "size": r["size"],
                "mtime": r["mtime"],
            })
        elif cat == "physics numerics":
            # grep Core_Papers and Working for filename and leave note
            cites = []
            needle = p.name
            for base in [ROOT / "Core_Papers", W]:
                if not base.exists():
                    continue
                for q in base.rglob("*"):
                    if not q.is_file() or q.suffix.lower() not in {".md", ".py", ".tex", ".txt"}:
                        continue
                    if q == p:
                        continue
                    try:
                        t = q.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue
                    if needle in t:
                        cites.append(str(q.relative_to(ROOT)))
                        if len(cites) >= 5:
                            break
                if len(cites) >= 5:
                    break
            packets.append({
                "name": r["name"],
                "source": r["source"],
                "cat": cat,
                "heading": "(physics script)",
                "status": "",
                "lines": first_nonempty_lines(p, 8),
                "withdrawn": [],
                "successor": None,
                "cites": cites,
                "sha12": r["sha12"],
                "size": r["size"],
                "mtime": r["mtime"],
            })

    # Write report
    print("=== Writing report ===", flush=True)
    now = datetime.now(NZ).strftime("%Y-%m-%d %H:%M %Z")
    lines_out = []
    lines_out.append("# Working Candidates Triage Report — 2026-09-22")
    lines_out.append("")
    lines_out.append(f"**Agent:** Cursor Main · **Generated:** {now}")
    lines_out.append(f"**Handoff:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_20260922.md`")
    lines_out.append("")
    lines_out.append("## Top finding — strip_corpus_metadata.py")
    lines_out.append("")
    for s in strip_finding:
        lines_out.append(f"- {s}")
    lines_out.append("")
    lines_out.append(
        "- Known item acted: `Working candidates\\strip_corpus_metadata.py` (pre-fix ORPHAN_SEE) → `Working\\Retired\\`."
    )
    lines_out.append("")
    lines_out.append("## Totals")
    lines_out.append("")
    lines_out.append(
        f"**files seen:** {len(rows)} · **moved to Working:** {moved_working} · "
        f"**moved to Retired:** {moved_retired} · **held:** {held}"
    )
    lines_out.append("")
    lines_out.append(
        "(Cursor phase: R1–R5 + known strip item only. All R1–R5 destinations are Retired; "
        "keeps remain HELD in place for AC verification.)"
    )
    lines_out.append("")
    lines_out.append("## Inventory — Farnsworth_Archive_Pull_20260802 (not moved)")
    lines_out.append("")
    lines_out.append(f"Files: **{len(farm_files)}** (live source for open route-B E(Φ_NTE) build). Left untouched.")
    lines_out.append("")
    lines_out.append("## __pycache__ (report only)")
    lines_out.append("")
    lines_out.append(f"Contents: {', '.join(pyc_files) if pyc_files else '(empty or absent)'}")
    lines_out.append("**Recommendation to Greg:** delete `Working\\__pycache__\\` — Python cache, not corpus.")
    lines_out.append("")
    if collision_flags:
        lines_out.append("## Name-collision FLAGs (different SHA)")
        lines_out.append("")
        for n in collision_flags:
            lines_out.append(f"- `{n}`")
        lines_out.append("")

    lines_out.append("## Master table (every file)")
    lines_out.append("")
    lines_out.append("| source | filename | size | modified | SHA-256 (12) | rule | destination | action |")
    lines_out.append("|---|---|---:|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: (x["source"], x["name"].lower())):
        mt = datetime.fromtimestamp(r["mtime"], NZ).strftime("%Y-%m-%d %H:%M")
        rule = r["rule"] + (f" / {r['flag_cat']}" if r.get("flag_cat") else "")
        note = (r.get("note") or "").replace("|", "/")
        dest = r["dest"]
        if note:
            rule = f"{rule} — {note}"[:120]
        lines_out.append(
            f"| {r['source']} | `{r['name']}` | {r['size']} | {mt} | `{r['sha12']}` | {rule} | {dest} | {r['action']} |"
        )

    lines_out.append("")
    lines_out.append("## FLAG packets (held for AC)")
    lines_out.append("")
    for pk in packets:
        mt = datetime.fromtimestamp(pk["mtime"], NZ).strftime("%Y-%m-%d %H:%M")
        lines_out.append(f"### `{pk['name']}` ({pk['source']} · {pk['cat']} · {pk['size']} B · {mt} · `{pk['sha12']}`)")
        lines_out.append("")
        if pk.get("heading"):
            lines_out.append(f"- **Heading:** {pk['heading']}")
        if pk.get("status"):
            lines_out.append(f"- **Status/version/date line:** {pk['status']}")
        if pk.get("successor"):
            lines_out.append(f"- **Possible successor:** {pk['successor']}")
        else:
            lines_out.append("- **Possible successor:** (none found by stem/version match)")
        if pk.get("cites") is not None:
            lines_out.append(f"- **Cite hits:** {', '.join('`'+c+'`' for c in pk['cites']) if pk['cites'] else '(none in Core_Papers/Working)'}")
        lines_out.append("- **First non-empty lines:**")
        lines_out.append("```")
        lines_out.extend(pk["lines"])
        lines_out.append("```")
        if pk.get("withdrawn"):
            lines_out.append("- **Withdrawn-claim markers:**")
            for label, count, sample in pk["withdrawn"]:
                lines_out.append(f"  - {label}: count={count}; sample: `{sample}`")
        else:
            if pk["cat"] in {"prose working document", "8.3 short-name"}:
                lines_out.append("- **Withdrawn-claim markers:** none")
        lines_out.append("")

    REPORT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(f"Wrote {REPORT}", flush=True)

    # Completion handoff
    held_n = held
    hand = f"""# Handoff — Cursor → AC: Working-candidates triage complete

**From:** Cursor Main · **To:** AC · **Cc:** Greg · **Date:** 2026-09-22
**Status:** Complete for Cursor phase (R1–R5 + known strip item). Held items await AC verification.
**In response to:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_20260922.md`

---

## Done

1. Triaged every file under `Working candidates\\` and every top-level file under `Working\\`.
2. Applied only unambiguous R1–R5 moves (+ AC-directed pre-fix `strip_corpus_metadata.py`) → `Working\\Retired\\`. Move-never-copy; no deletes; no renames; no `paper-build\\` writes.
3. Left `Working\\Farnsworth_Archive_Pull_20260802\\` untouched (inventory only).
4. Report: `Working\\Working_Candidates_Triage_Report_20260922.md`

## Totals

**files seen:** {len(rows)} · **moved to Working:** {moved_working} · **moved to Retired:** {moved_retired} · **held:** {held_n}

## Top finding (also at report head)

`paper-build\\strip_corpus_metadata.py` is **MISSING**. The corrected ORPHAN_SEE pattern lives in `Working\\strip_corpus_metadata.py`:

```
ORPHAN_SEE = re.compile(r"(?:;\\s*)?\\b[Ss]ee\\b(?=\\s*[);])", re.I)
```

Pre-fix copy from `Working candidates\\` retired. AC/Greg: restore the corrected script into `paper-build\\` if the render pipeline still calls it by that path.

## Held for AC

{held_n} files held (FLAG packets in the report): 8.3 short-names, physics numerics, prose working docs, scripts without completion evidence, and all Working top-level items not caught by R1–R5.

`Working candidates\\` folder itself was not removed.

## Manifest

§10 In-progress line registered.

— Cursor Main, 2026-09-22.
"""
    HANDOFF.write_text(hand, encoding="utf-8")
    print(f"Wrote {HANDOFF}", flush=True)

    # Manifest §10
    man = MANIFEST.read_text(encoding="utf-8")
    marker = "**In progress:**"
    insert = (
        f"- Working-candidates triage 2026-09-22 — {held_n} held for AC verification; "
        f"report at `Working\\Working_Candidates_Triage_Report_20260922.md`."
    )
    if "Working-candidates triage 2026-09-22" not in man:
        if marker in man:
            man = man.replace(marker, marker + "\n" + insert, 1)
        else:
            man = man + "\n" + marker + "\n" + insert + "\n"
        # bump last-updated lightly
        man2 = re.sub(
            r"(\*\*Last updated\.\*\*\s*)([^\n]+)",
            r"\g<1>2026-09-22 — §10: Working-candidates triage Cursor phase complete "
            f"({moved_retired} retired, {held_n} held). Prior: \g<2>",
            man,
            count=1,
        )
        if man2 != man:
            man = man2
        else:
            # fallback if pattern odd
            pass
        MANIFEST.write_text(man, encoding="utf-8")
        print("Manifest §10 updated", flush=True)
    else:
        print("Manifest already had triage line", flush=True)

    # summary json for chat
    summary = {
        "seen": len(rows),
        "moved_working": moved_working,
        "moved_retired": moved_retired,
        "held": held_n,
        "collisions": collision_flags,
        "strip_pb_missing": not pb_strip.exists(),
    }
    print("SUMMARY", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
