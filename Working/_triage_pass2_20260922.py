#!/usr/bin/env python3
"""Pass 2 Working-candidates triage — decisive P/K/D disposition. Target ≤25 held."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NZ = timezone(timedelta(hours=12))
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
WC = ROOT / "Working candidates"
W = ROOT / "Working"
RETIRED = W / "Retired"
SUMMARY = W / "Working_Candidates_Triage_Pass2_Summary_20260922.md"
MOVES_CSV = W / "Working_Candidates_Triage_Pass2_Moves_20260922.csv"
HANDOFF = ROOT / "Handoffs" / "Handoff_Cursor_to_AC_Working_Candidates_Triage_Pass2_Complete_20260922.md"
MANIFEST = ROOT / "NTE_Workflow_Manifest_v10_18.md"
PASS1_REPORT = W / "Working_Candidates_Triage_Report_20260922.md"
PART3 = ROOT / "Core_Papers" / "NTE_v10_19_0_Part3_Accounting.md"

P3_CUTOFF = datetime(2026, 8, 1, tzinfo=NZ).timestamp()

P1_PIPELINE = [
    "prepare_paper_pdf.py",
    "prepare_master_pdf.py",
    "strip_publication_tail.py",
    "strip_corpus_metadata.py",
]

K2_PREFIXES = (
    "CHARTER_GATE1_", "GATE2_", "GATE3_", "GATE4", "GATE5_", "GATE6",
    "CHARTER_P4D_", "Investigation_P4D_", "FS_Geometry_Finding_Theta23_",
    "CR2_Programme_S_Sigma3_",
)
K2_EXACT = {"M1_Sigma3_Cartan_Mode_Derivation_v1.md"}
K2_FARN = re.compile(r"^farnsworth_stage.*\.py$", re.I)
K2_MR_KEEP = (
    "Cursor_Heat_Kernel_M_R_Critical_Review_",
    "CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_",
)
MR_PAT = re.compile(
    r"8\.2.{0,40}(?:10\^\{?14\}?|10¹⁴|×10\^14|x10\^14|e14)|"
    r"(?:10\^\{?14\}?|10¹⁴|×10\^14|x10\^14|e14).{0,40}8\.2",
    re.I | re.S,
)
FIBRE_PAT = re.compile(
    r"(?:fibre|fiber)\s+modulus|β_GB.{0,60}(?:√\(?2π\)?|sqrt\s*\(\s*2\s*\*\s*pi\s*\))|"
    r"(?:√\(?2π\)?|sqrt\s*\(\s*2\s*\*\s*pi\s*\)).{0,60}β_GB",
    re.I | re.S,
)

K3_NAMES = {
    "clfv_cartan_ratio_numerical.py",
    "clfv_cartan_ratio_numerical_results.json",
    "CLFV_Cartan_Ratio_Numerical_Results_20260613.md",
    "kappa_closure_g1_adversarial_jammer.py",
    "kappa_closure_p2eqp_check.py",
}
K3_PREFIX = "KAPPA_CLOSURE_"

K4_PREFIXES = (
    "NTE_Book_Title_and_Pratchett_Discipline_",
    "NTE_Book_DeAI_Voice_Pass_",
    "NTE_Book_Appendix_and_Corpus_Links_Discipline_",
    "NTE_Acronym_Naming_Discipline_",
    "Publication_Title_Block_Standard_",
    "Standalone_Papers_Accessibility_Tiering_Framework_",
    "NTE_FAQ_Supplement_DRAFT_v0_2_",
)
K4_EXACT = {
    "NTE_Book_Popular_Voice_Register.md",
    "NTE_Reader_Glossary_Companion_v1_0.md",
}
K4_STALE_REGISTER = {
    "NTE_Reader_Glossary_Companion_v1_0.md",
    "NTE_FAQ_Supplement_DRAFT_v0_2_",  # prefix match
}

K5_PREFIX = "NTE_Octonionic_Spine_Neutrino_Mixing_Sector_"

# D1–D7 prefix/exact lists (substring startswith for most)
D1_PREFIXES = (
    "CR2_", "CR4_", "CR_Question_", "Jammer_", "AC_Patch_", "AC_Tier2g_",
    "AC_Bulk_Boundary_", "AC_Lambda_Pathways_", "AC_Full_Corpus_Reading_Register_",
    "AC_Wagenveld_", "Master_v10_", "Master_Part_3_", "MASTER_REBUILD_",
    "Companion_v10_8_", "LB5_", "LB6_", "BR5_", "LCDM_", "Load_Bearing_Blocks_",
    "Mu_xN_", "H_GB_", "J6_", "NTE_PP_Audit_", "NTE_Pedagogical_Pivot_",
    "PC_", "Chapter_NEW_", "NTE_Session_Writeup_", "NTE_Corpus_Sitrep_",
    "Comprehensive_Status_Update_", "CRITICAL_UPDATE_", "DRAFT_CatchUp_",
    "NTE_Recording_Gap_Audit_", "Drive_Sync_Manifest_", "Corpus_Gap_",
    "Corpus_Sunshine_", "NTE_CR2_Sunshine_", "Paper_Scope_Alignment_",
    "NTE_Corpus_Critical_Review_", "NTE_Extension_Scorecard_",
    "NTE_Unified_Corpus_Network_Map_", "NTE_Ontological_Bridge_",
    "NTE_Book_Open_Future_", "Greg_Tier1_Standalone_Upload_",
    "NTE_Standalone_Claims_Inventory_", "Compatibility_Catalogue_",
    "II_0_Graded_Criteria_",
)
D1_SPECIAL = (
    "Companion_11_v10_17_2_Scratch_CR_Verification_",
    "Companion_12_v10_17_2_Scratch_CR_Verification_",
    "Companion_13_v10_17_2_Scratch_CR_Verification_",
)

D2_PREFIXES = (
    "Connes_Programme_", "NTE_Connes_Programme_", "BF2020_", "Filter_Report_",
    "Cross_Fertilization_", "Wagenveld_", "Jammer_Wagenveld_", "C3_Anisotropic_",
    "CPN_Universe_Pair_", "CRUNCH_", "Gate0_Worksheet_", "Investigation_FS_",
    "CHARTER_FS_", "AC_Assessment_Scratch_FS_", "NTE_Note_CPN_", "Assessment_",
    "BMV_", "Cosmic_Dipole_", "Connes_Rovelli_", "External_", "KSIP_",
    "Draft_Outreach_", "NTE_Time_Dimension_Count_", "NTE_vs_Singh_", "NTE_x_Singh_",
    "NTE_Provenance_Audit_", "NTE_External_Positioning_", "NTE_Governance_Note_",
    "NTE_Investigation_Note_", "NTE_Visualisation_", "Exploration_",
    "compass_artifact_", "CLFV_2A_Extension_", "BH_Nthickness_",
    "AC_Foundations_Probe_", "EXTERNAL_ColdReferee_", "Programme_S_",
    "Paper_PhiNTE_", "Paper_A1_", "Paper_A2_", "P1_", "P5_v0_3_", "Cursor_BranchI_",
)
D2_EXACT = {"Kletetschka_2025_extracted.txt"}

D3_SUBSTR = (
    "Candidate_Pathway_Neutrino_",
    "Companion_Paper_7a_Neutrino_as_Chirality_Superposition_",
    "n_s_Wick_Rotation_",
    "Derivation_Y3_",
    "lcdm_bao_void_bias.py",
    "Void_Bias",
)
D3_ETA = re.compile(r"^(Eta_|eta_)", re.I)

D4_PREFIXES = (
    "j1_", "j4_", "j6_", "lcdm_", "lambda_", "lb1_", "m1_", "br2d_", "bh_",
    "mu_xn_", "gap1_", "h_gb_", "cr2_", "alpha_", "pc03_", "paper_s22_", "p5_",
)
D4_EXACT = {"healpix_ring.py"}
D4_CALC = re.compile(r"_Calculation\.txt$", re.I)

D6_PREFIX = "INDEX_NTE_Canonical_Drive_IDs_"
D7_EXACT = {
    "NTE_CR2_Execution_Queue.json",
    "NTE_CR2_Open_Work_Registry.json",
    "NTE_CR2_Registry_Waves.json",
    "cursor_task_ledger.json",
    "cursor_task_ledger.json.corrupt.bak",
}
D7_PREFIXES = ("alpha_to_beta_", "consolidated_")

CITE_DIRS = [
    ROOT / "Core_Papers",
    ROOT / "Pedagogical_Notes",
    ROOT / "Book",
    ROOT / "Popular_Editions",
]


def sha_full(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def first_heading(path: Path) -> str:
    try:
        for ln in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if ln.strip():
                return ln.strip()[:160]
    except Exception as e:
        return f"<unreadable: {e}>"
    return "(empty)"


def starts_any(name: str, prefixes: tuple[str, ...]) -> bool:
    return any(name.startswith(p) for p in prefixes)


def load_open_guard_text() -> str:
    parts = []
    if PART3.exists():
        t = PART3.read_text(encoding="utf-8", errors="replace")
        # open-list heuristic: sections mentioning open / watch / unresolved
        parts.append(t)
    if MANIFEST.exists():
        man = MANIFEST.read_text(encoding="utf-8", errors="replace")
        # §10 region
        m = re.search(r"## 10\..*", man, re.S)
        parts.append(m.group(0) if m else man[-8000:])
    return "\n".join(parts).lower()


def distinctive_tokens(name: str) -> list[str]:
    stem = Path(name).stem
    # drop common noise
    toks = re.split(r"[_\-\s]+", stem)
    out = []
    for t in toks:
        if len(t) < 5:
            continue
        if t.lower() in {
            "draft", "scratch", "working", "note", "paper", "nte", "cursor",
            "handoff", "companion", "assessment", "investigation", "v0", "v1",
            "v2", "md", "ac", "pc", "greg",
        }:
            continue
        if re.fullmatch(r"v?\d+", t, re.I):
            continue
        out.append(t.lower())
    # also long contiguous chunks
    if len(stem) >= 24:
        out.append(stem.lower()[:40])
    return out[:8]


def d2_guard_hit(name: str, guard_text: str) -> str | None:
    toks = distinctive_tokens(name)
    hits = [t for t in toks if t in guard_text and len(t) >= 6]
    if hits:
        return hits[0]
    return None


def successor_in_ped_book_pop(name: str) -> bool:
    stem = Path(name).stem.lower()
    # strip version tokens for fuzzy
    base = re.sub(r"_?v\d+(?:_\d+)*", "", stem)
    base = re.sub(r"_+", "_", base).strip("_")
    for d in (ROOT / "Pedagogical_Notes", ROOT / "Book", ROOT / "Popular_Editions"):
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if not p.is_file():
                continue
            n = p.stem.lower()
            if base and base[:30] in n:
                return True
            if stem[:30] in n:
                return True
    return False


def build_citation_index(names: list[str]) -> dict[str, list[str]]:
    """Map filename -> list of citing relative paths."""
    # Prefer full filename match; also stem if stem length >= 28
    needles = {}
    for n in names:
        needles[n] = n
        stem = Path(n).stem
        if len(stem) >= 28:
            needles[stem] = n
    cites = defaultdict(list)
    for d in CITE_DIRS:
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in {".md", ".tex", ".txt"}:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            rel = str(p.relative_to(ROOT))
            for needle, orig in needles.items():
                if needle in text:
                    if rel not in cites[orig]:
                        cites[orig].append(rel)
    return cites


def match_k2_name(name: str) -> str | None:
    if name in K2_EXACT:
        return "K2 open-item (exact)"
    if starts_any(name, K2_PREFIXES):
        return "K2 open-item (GATE/P4D/FS/CR2_Programme_S)"
    if K2_FARN.match(name):
        return "K2 Route-B farnsworth_stage*.py"
    if starts_any(name, K2_MR_KEEP):
        return "K2 M_R figure / seesaw convention"
    return None


def match_d_name(name: str) -> str | None:
    if name in D7_EXACT or starts_any(name, D7_PREFIXES):
        return "D7 registries/queues/ledgers"
    if name.startswith(D6_PREFIX):
        return "D6 ID caches"
    if starts_any(name, D1_PREFIXES) or starts_any(name, D1_SPECIAL):
        # H_GB_ unless K2 — K2 checked first
        return "D1 closed May–June process"
    if name.startswith("Cursor_") and any(
        x in name for x in ("Audit", "Review", "Critical", "Heat_Kernel")
    ):
        # Heat_Kernel may be K2 — checked earlier
        if not starts_any(name, K2_MR_KEEP):
            return "D1 Cursor_* audits/reviews"
    if name in D2_EXACT or starts_any(name, D2_PREFIXES):
        return "D2 concluded/dormant research"
    if any(s in name for s in D3_SUBSTR) or D3_ETA.match(name):
        return "D3 withdrawn/retired content carriers"
    low = name.lower()
    if name in D4_EXACT or D4_CALC.search(name) or starts_any(low, D4_PREFIXES):
        return "D4 spent numerics"
    return None


def collect_targets() -> list[tuple[str, Path]]:
    out = []
    if WC.exists():
        for p in WC.rglob("*"):
            if p.is_file():
                out.append(("candidates", p))
    for p in W.iterdir():
        if p.is_file():
            out.append(("working", p))
    return out


def safe_retire(src: Path) -> tuple[bool, str]:
    RETIRED.mkdir(parents=True, exist_ok=True)
    dest = RETIRED / src.name
    if dest.exists():
        try:
            if sha_full(dest) == sha_full(src):
                src.unlink()
                return True, "already in Retired identical; unlinked twin"
        except Exception as e:
            return False, f"collision hash error: {e}"
        # different — try disambiguate with source tag
        dest = RETIRED / f"{src.stem}__from_candidates{src.suffix}"
        if dest.exists():
            return False, "NAME COLLISION different SHA"
    try:
        shutil.move(str(src), str(dest))
        return True, str(dest.relative_to(ROOT))
    except Exception as e:
        return False, f"move failed: {e}"


def safe_keep_to_working(src: Path) -> tuple[bool, str]:
    """Move from candidates into Working\\."""
    dest = W / src.name
    if dest.exists():
        try:
            if sha_full(dest) == sha_full(src):
                src.unlink()
                return True, "already in Working identical; unlinked twin"
        except Exception as e:
            return False, f"collision hash error: {e}"
        return False, "NAME COLLISION different SHA — HOLD"
    try:
        shutil.move(str(src), str(dest))
        return True, str(dest.relative_to(ROOT))
    except Exception as e:
        return False, f"move failed: {e}"


def main():
    print("=== Pass 2 start ===", flush=True)
    targets = collect_targets()
    print(f"targets: {len(targets)}", flush=True)

    # P1 derived
    p1_list = list(P1_PIPELINE)
    print("P1:", p1_list)

    # Citation index (K1)
    names = [p.name for _, p in targets]
    print("=== Building citation index ===", flush=True)
    cites = build_citation_index(names)
    print(f"  cited names: {len(cites)}", flush=True)

    # M_R and fibre content scans
    print("=== Content scans (M_R / fibre) ===", flush=True)
    mr_hits = []  # (filename, line)
    fibre_keep = set()
    for src, p in targets:
        if p.suffix.lower() not in {".md", ".txt", ".py", ".tex", ".json"}:
            continue
        # skip huge bak
        if p.stat().st_size > 50_000_000:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if MR_PAT.search(text):
            for i, ln in enumerate(text.splitlines(), 1):
                if MR_PAT.search(ln) or (
                    "8.2" in ln and re.search(r"10\^|10¹|e14|×10", ln, re.I)
                ):
                    mr_hits.append((p.name, i, ln.strip()[:240]))
        if FIBRE_PAT.search(text):
            fibre_keep.add(p.name)

    print(f"  M_R hits: {len(mr_hits)}; fibre files: {len(fibre_keep)}", flush=True)

    guard_text = load_open_guard_text()

    # Identify tilde files
    tilde_ids = {}
    for src, p in targets:
        if "~" in p.name:
            tilde_ids[p.name] = first_heading(p)

    # New-folder check for K5
    new_folder = ROOT / "New folder"
    new_folder_files = {}
    if new_folder.exists():
        for p in new_folder.rglob("*"):
            if p.is_file():
                new_folder_files[p.name.lower()] = p

    # Copy/(1) twins
    by_base = defaultdict(list)
    for src, p in targets:
        base = re.sub(r" \(\d+\)| - Copy", "", p.name, flags=re.I)
        by_base[base].append((src, p))

    decisions = []  # dicts
    rule_counts = Counter()

    def decide(src, path, rule, action, note=""):
        decisions.append({
            "source": src,
            "path": path,
            "name": path.name,
            "rule": rule,
            "action": action,  # KEEP_WORKING / KEEP_STAY / RETIRE / HOLD
            "note": note,
        })
        rule_counts[rule] += 1

    print("=== Classifying ===", flush=True)
    for src, p in targets:
        name = p.name
        try:
            st = p.stat()
        except OSError as e:
            decide(src, p, "HOLD unreadable", "HOLD", str(e))
            continue

        # --- P rules ---
        if name in P1_PIPELINE or name in p1_list:
            decide(src, p, "P1 pipeline", "KEEP_STAY" if src == "working" else "KEEP_WORKING")
            continue
        if src == "working" and name == PASS1_REPORT.name:
            # will retire after summary exists — mark RETIRE_PASS1 for later
            decide(src, p, "P4 then retire Pass1 after summary", "RETIRE_PASS1")
            continue
        if name.startswith("Working_Candidates_Triage_Pass2_"):
            decide(src, p, "P4 pass2 outputs", "KEEP_STAY")
            continue
        if name == "_triage_pass2_20260922.py":
            decide(src, p, "P4 pass2 runner (self)", "KEEP_STAY")
            continue
        if name == "_triage_working_candidates_20260922.py":
            decide(src, p, "D5 spent tooling (pass1 triage)", "RETIRE")
            continue
        if src == "working" and st.st_mtime >= P3_CUTOFF:
            # P3 protect unless byte-identical duplicate elsewhere handled at move
            decide(src, p, "P3 post-2026-08-01 Working", "KEEP_STAY")
            continue

        # --- K rules ---
        if name in cites:
            decide(src, p, "K1 cited", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY",
                   f"cited in {cites[name][0]}")
            continue
        k2 = match_k2_name(name)
        if k2:
            decide(src, p, k2, "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            continue
        if name in fibre_keep or any(h[0] == name for h in mr_hits):
            # content-based K2
            if any(h[0] == name for h in mr_hits):
                decide(src, p, "K2 M_R numeric trace content", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            else:
                decide(src, p, "K2 fibre-modulus / β_GB content", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            continue
        if name in K3_NAMES or name.startswith(K3_PREFIX):
            decide(src, p, "K3 reproducibility", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            continue
        # K4
        k4 = name in K4_EXACT or starts_any(name, K4_PREFIXES)
        if k4:
            if successor_in_ped_book_pop(name):
                decide(src, p, "D (K4 has successor in Ped/Book/Pop)", "RETIRE", "successor exists")
            else:
                decide(src, p, "K4 standing guidance", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            continue
        # K5
        if name.startswith(K5_PREFIX) or (
            "Octonionic_Spine_Neutrino_Mixing" in name
        ):
            nf = new_folder_files.get(name.lower())
            if nf:
                try:
                    if sha_full(nf) == sha_full(p) or nf.stat().st_mtime >= st.st_mtime:
                        decide(src, p, "K5/R1 New folder has same/later", "RETIRE")
                    else:
                        decide(src, p, "K5 octonionic standalone keep", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
                except Exception:
                    decide(src, p, "HOLD K5 compare failed", "HOLD")
            else:
                decide(src, p, "K5 octonionic standalone keep", "KEEP_WORKING" if src == "candidates" else "KEEP_STAY")
            continue
        # K6 — monitoring lane does NOT read cursor_task_ledger.json
        if name == "cursor_task_ledger.json":
            decide(src, p, "D7 (K6 no — lane uses watch_state)", "RETIRE",
                   "monitoring uses Working\\.cursor_handoff_watch_state.json")
            continue

        # Copy/(1) twins
        base = re.sub(r" \(\d+\)| - Copy", "", name, flags=re.I)
        if base != name and base in {x[1].name for x in by_base.get(base, [])}:
            # has unsuffixed twin
            twins = by_base.get(base, [])
            unsuf = [t for t in twins if t[1].name == base]
            if unsuf:
                try:
                    if sha_full(unsuf[0][1]) == sha_full(p):
                        decide(src, p, "Copy twin identical", "RETIRE")
                        continue
                    # keep later-modified; retire earlier — decide per file
                    if st.st_mtime < unsuf[0][1].stat().st_mtime:
                        decide(src, p, "Copy twin older", "RETIRE")
                        continue
                    # this is newer — fall through to D on the identified base? keep via fallthrough K none → D
                except Exception:
                    decide(src, p, "HOLD copy-compare failed", "HOLD")
                    continue

        # --- D rules ---
        d = match_d_name(name)
        if d == "D2 concluded/dormant research":
            hit = d2_guard_hit(name, guard_text)
            if hit:
                decide(src, p, "HOLD D2 guard", "HOLD", f"topic token '{hit}' in Part3/§10")
                continue
            decide(src, p, d, "RETIRE")
            continue
        if d:
            decide(src, p, d, "RETIRE")
            continue

        # D5 — every remaining candidates script
        if src == "candidates" and p.suffix.lower() in {".py", ".ps1", ".lua"}:
            if name in P1_PIPELINE:
                decide(src, p, "HOLD D5 pipeline gap", "HOLD", "invoked by pipeline but only in candidates")
            else:
                decide(src, p, "D5 spent tooling", "RETIRE")
            continue

        # Default: not P/K → retire
        if "~" in name:
            decide(src, p, "D tilde-identified default retire", "RETIRE",
                   f"header: {tilde_ids.get(name, '')[:80]}")
            continue

        # remaining working or candidates prose/other
        decide(src, p, "D default (not P/K)", "RETIRE")

    # Apply moves
    print("=== Applying moves ===", flush=True)
    moved_rows = []
    kept = []
    held = []
    for dec in decisions:
        p = dec["path"]
        act = dec["action"]
        if act == "KEEP_STAY":
            kept.append(dec)
            continue
        if act == "RETIRE_PASS1":
            # defer
            continue
        if act == "HOLD":
            held.append(dec)
            continue
        if act == "KEEP_WORKING":
            if dec["source"] == "candidates":
                ok, msg = safe_keep_to_working(p)
                if ok:
                    moved_rows.append((dec["name"], dec["rule"], "Working\\"))
                    kept.append(dec)
                else:
                    dec["action"] = "HOLD"
                    dec["note"] = msg
                    held.append(dec)
            else:
                kept.append(dec)
            continue
        if act == "RETIRE":
            ok, msg = safe_retire(p)
            if ok:
                moved_rows.append((dec["name"], dec["rule"], "Working\\Retired\\"))
            else:
                dec["action"] = "HOLD"
                dec["note"] = msg
                held.append(dec)

    # Write summary BEFORE retiring pass1
    print("=== Writing summary/CSV ===", flush=True)
    now = datetime.now(NZ).strftime("%Y-%m-%d %H:%M %Z")
    lines = []
    lines.append("# Working Candidates Triage — Pass 2 Summary (2026-09-22)")
    lines.append("")
    lines.append(f"**Agent:** Cursor Main · **Generated:** {now}")
    lines.append("**Handoff:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_Pass2_20260922.md`")
    lines.append("")
    lines.append("## Correction acknowledged")
    lines.append("")
    lines.append(
        "Pass-1 \"render-blocking / restore to paper-build\" finding is **withdrawn** (AC error). "
        "Live strip/prepare scripts live in `Working\\`. `__pycache__` left alone."
    )
    lines.append("")
    lines.append("## P1 — derived render-pipeline protect list")
    lines.append("")
    lines.append("From `paper-build\\render-all-clean.ps1` + imports of `prepare_paper_pdf.py` / `prepare_master_pdf.py`:")
    for n in p1_list:
        lines.append(f"- `Working\\{n}`")
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    n_retire = sum(1 for r in moved_rows if r[2].endswith("Retired\\"))
    n_keep_moved = sum(1 for r in moved_rows if r[2] == "Working\\")
    lines.append(
        f"**seen:** {len(decisions)} · **kept:** {len(kept)} · "
        f"**moved to Working:** {n_keep_moved} · **moved to Retired:** {n_retire} · "
        f"**held:** {len(held)}"
    )
    lines.append("")
    lines.append("### Counts per rule")
    lines.append("")
    for rule, c in rule_counts.most_common():
        lines.append(f"- {rule}: {c}")
    lines.append("")
    lines.append("## KEEP list (filename → rule)")
    lines.append("")
    for dec in sorted(kept, key=lambda d: d["name"].lower()):
        note = f" — {dec['note']}" if dec.get("note") else ""
        lines.append(f"- `{dec['name']}` → {dec['rule']}{note}")
    lines.append("")
    lines.append("## K2 — M_R trace (8.2 × 10¹⁴)")
    lines.append("")
    if not mr_hits:
        lines.append("**no occurrence of 8.2 × 10¹⁴ found in either folder**")
    else:
        for fn, ln, text in mr_hits[:40]:
            lines.append(f"- `{fn}`:{ln}: `{text}`")
        if len(mr_hits) > 40:
            lines.append(f"- … +{len(mr_hits)-40} more")
    lines.append("")
    lines.append("## K6 — cursor_task_ledger.json")
    lines.append("")
    lines.append(
        "Monitoring lane reads `Working\\.cursor_handoff_watch_state.json`, **not** "
        "`cursor_task_ledger.json`. Ledger retired under D7. "
        "**`cursor_task_ledger.json.corrupt.bak` (~1.93 GB) → Retired; Greg: delete from Drive.**"
    )
    lines.append("")
    lines.append("## Tilde / short-name identification")
    lines.append("")
    lines.append("| short name | header / title | disposition rule |")
    lines.append("|---|---|---|")
    tilde_decs = {d["name"]: d for d in decisions if "~" in d["name"]}
    for n, hdr in sorted(tilde_ids.items()):
        d = tilde_decs.get(n)
        rule = d["rule"] if d else "?"
        lines.append(f"| `{n}` | {hdr.replace('|','/')} | {rule} |")
    lines.append("")
    lines.append("## HOLD list (≤25 target)")
    lines.append("")
    if not held:
        lines.append("(none)")
    for dec in held:
        lines.append(f"### `{dec['name']}`")
        lines.append(f"- **What:** {first_heading(dec['path']) if dec['path'].exists() else '(moved/missing)'}")
        lines.append(f"- **Rules conflict / reason:** {dec['rule']} — {dec.get('note','')}")
        lines.append("- **Decision needed:** AC/Greg choose keep-in-Working vs Retired.")
        lines.append("")

    # K4 stale register note
    lines.append("## K4 stale register (manifest §10)")
    lines.append("")
    lines.append(
        "Kept and flagged for PC currency pass before use: "
        "`NTE_Reader_Glossary_Companion_v1_0.md`, any `NTE_FAQ_Supplement_DRAFT_v0_2_*`."
    )
    lines.append("")

    text = "\n".join(lines) + "\n"
    SUMMARY.write_text(text, encoding="utf-8")
    sz = SUMMARY.stat().st_size
    print(f"Summary size: {sz} bytes", flush=True)
    if sz > 40_000:
        print("WARNING: summary over 40KB", flush=True)

    with MOVES_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["filename", "rule", "destination"])
        for row in moved_rows:
            w.writerow(row)
        # also note pass1 retirement
        w.writerow([PASS1_REPORT.name, "Pass2: retire Pass1 report", "Working\\Retired\\"])

    # Retire Pass1 report now that summary exists
    if PASS1_REPORT.exists():
        ok, msg = safe_retire(PASS1_REPORT)
        print("Pass1 report retire:", ok, msg, flush=True)

    # Handoff
    hand = f"""# Handoff — Cursor → AC: Working-candidates triage Pass 2 complete

**From:** Cursor Main · **To:** AC · **Cc:** Greg · **Date:** 2026-09-22
**In response to:** `Handoffs\\Handoff_AC_to_Cursor_Working_Candidates_Triage_Pass2_20260922.md`
**Status:** Complete.

## Correction

Pass-1 restore-to-`paper-build` finding withdrawn per AC. No restore performed. `__pycache__` left alone.

## Deliverables

- `Working\\Working_Candidates_Triage_Pass2_Summary_20260922.md` ({sz} bytes)
- `Working\\Working_Candidates_Triage_Pass2_Moves_20260922.csv`
- Pass 1 report retired to `Working\\Retired\\`

## Totals

**seen:** {len(decisions)} · **kept:** {len(kept)} · **moved to Working:** {n_keep_moved} · **moved to Retired:** {n_retire} · **held:** {len(held)}

## P1 pipeline list

{", ".join("`Working\\\\"+n+"`" for n in p1_list)}

## Greg flag

`Working\\Retired\\cursor_task_ledger.json.corrupt.bak` (~1.93 GB) — delete from Drive when convenient.

## K6

Lane uses `.cursor_handoff_watch_state.json`; `cursor_task_ledger.json` retired (D7).

— Cursor Main, 2026-09-22.
"""
    HANDOFF.write_text(hand, encoding="utf-8")

    # Manifest §10
    man = MANIFEST.read_text(encoding="utf-8")
    old = re.search(r"- Working-candidates triage 2026-09-22[^\n]*", man)
    new_line = (
        f"- Working-candidates triage 2026-09-22 Pass 2 — {len(held)} held for AC verification; "
        f"summary at `Working\\Working_Candidates_Triage_Pass2_Summary_20260922.md`."
    )
    if old:
        man = man[: old.start()] + new_line + man[old.end() :]
    elif "**In progress:**" in man:
        man = man.replace("**In progress:**", "**In progress:**\n" + new_line, 1)
    # K4 stale
    stale_lines = []
    for pref in ("NTE_Reader_Glossary_Companion_v1_0.md",):
        if pref in {d["name"] for d in kept} or (W / pref).exists() or any(
            d["name"] == pref for d in kept
        ):
            stale_lines.append(
                f"- kept, stale vs v10.19, needs PC currency pass before any use: `{pref}`"
            )
    # FAQ
    for d in kept:
        if d["name"].startswith("NTE_FAQ_Supplement_DRAFT_v0_2_"):
            stale_lines.append(
                f"- kept, stale vs v10.19, needs PC currency pass before any use: `{d['name']}`"
            )
    for sl in stale_lines:
        if sl not in man:
            man = man.replace("**In progress:**", "**In progress:**\n" + sl, 1)
    man = re.sub(
        r"(\*\*Last updated\.\*\*\s*)([^\n]+)",
        rf"\g<1>2026-09-22 — §10: Working-candidates Pass 2 complete "
        rf"({n_retire} retired, {len(held)} held). Prior: \2",
        man,
        count=1,
    )
    MANIFEST.write_text(man, encoding="utf-8")

    summary = {
        "seen": len(decisions),
        "kept": len(kept),
        "moved_working": n_keep_moved,
        "moved_retired": n_retire,
        "held": len(held),
        "summary_bytes": sz,
        "mr_hits": len(mr_hits),
        "held_names": [h["name"] for h in held],
    }
    print("SUMMARY", json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
