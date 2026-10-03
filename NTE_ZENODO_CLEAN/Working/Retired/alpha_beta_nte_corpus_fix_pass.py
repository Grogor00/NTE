#!/usr/bin/env python3
"""Multi-pass α ↔ β_NTE collision repair (Greg 2026-06-04 rule).

β_NTE = H-coefficient in H = β_NTE|Φ_NTE|² (≈ 2.38×10⁻⁴⁷ GeV⁻¹).
α_em = fine-structure constant (≈ 1/137).
α_i / α₁,₂,₃ = SM gauge couplings at M_Pl.

Run: python alpha_beta_nte_corpus_fix_pass.py [--apply]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESKTOP = ROOT.parent

SKIP_DIR_NAMES = {
    "depreciated",
    "old-paper-build",
    "scratch-src",
    "agent-transcripts",
    ".git",
    "node_modules",
}

SKIP_FILE_PARTS = (
    "alpha_to_beta_nte_audit.py",
    "alpha_beta_nte_corpus_fix_pass.py",
    "Handoff_PC_to_Cursor_AlphaToBeta",
    "Handoff_AC_to_Cursor_AC_BetaNTE",
    "Handoff_Scratch_to_AC_Necessity_v0_3_betaNTE",
)

SCAN_ROOTS = [
    ROOT / "Papers",
    ROOT / "Working",
    ROOT / "Outreach",
    ROOT / "Workflow",
    DESKTOP / "Book",
]

# --- protect tokens (order: longer first) ---
PROTECT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"Pathway\s+\$?\\?alpha\$?", re.I), "__PROT_PATHWAY_A__"),
    (re.compile(r"Path\s+\$?\\?alpha\$?", re.I), "__PROT_PATH_A__"),
    (re.compile(r"Pathway\s+Alpha", re.I), "__PROT_PATHWAY_ALPHA__"),
    (re.compile(r"\u03b1_em", re.I), "__PROT_AEM__"),
    (re.compile(r"\u03b1_s\b"), "__PROT_AS__"),
    (re.compile(r"\u03b1_\{?i\}?\b"), "__PROT_AI__"),
    (re.compile(r"\u03b1_\{?1\}?\b"), "__PROT_A1__"),
    (re.compile(r"\u03b1_\{?2\}?\b"), "__PROT_A2__"),
    (re.compile(r"\u03b1_\{?3\}?\b"), "__PROT_A3__"),
    (re.compile(r"\u03b1\u2081"), "__PROT_A1__"),
    (re.compile(r"\u03b1\u2082"), "__PROT_A2__"),
    (re.compile(r"\u03b1\u2083"), "__PROT_A3__"),
    (re.compile(r"\$\\alpha_\{\\mathrm\{em\}\}\$"), "__PROT_AEM_MATH__"),
    (re.compile(r"\$\\alpha_\{em\}\$"), "__PROT_AEM_MATH__"),
    (re.compile(r"\$\\alpha_\{\\rm em\}\$"), "__PROT_AEM_MATH__"),
    (re.compile(r"g_\{[^}]*\}\^\{\\alpha\\beta\}"), "__PROT_TENSOR__"),
    (re.compile(r"\u03b1-particle", re.I), "__PROT_APART__"),
    (re.compile(r"\u03b1-decay", re.I), "__PROT_ADEC__"),
    (re.compile(r"\u03b1_helix", re.I), "__PROT_AHELIX__"),
    (re.compile(r"\|ν⟩\s*=\s*\u03b1\|"), "__PROT_CHIRAL__"),
    (re.compile(r"\u03b1\|ν_L⟩"), "__PROT_CHIRAL__"),
    (re.compile(r"fine-structure constant\s+\u03b1_em", re.I), "__PROT_FS_AEM__"),
    (re.compile(r"fine-structure constant\s+\$\\alpha_\{em\}\$", re.I), "__PROT_FS_AEM_MATH__"),
    (re.compile(r"electromagnetic fine-structure constant\s+\u03b1_em", re.I), "__PROT_EFS_AEM__"),
    (re.compile(r"\u03b1_em\s*=\s*1/137"), "__PROT_AEM137__"),
    (re.compile(r"g_eff\s*\u00b7\s*\u03b1_em", re.I), "__PROT_GEFF__"),
    (re.compile(r"g_eff\s*\u00d7\s*\u03b1_em", re.I), "__PROT_GEFF__"),
]

# Reverse collisions: β_NTE used where α_em or α_i belong
REVERSE_FIXES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"fine-structure constant\s+β_NTE", re.I), "fine-structure constant α_em"),
    (re.compile(r"fine-structure constant\s+\$\\beta_\{\\mathrm\{NTE\}\}\$", re.I), "fine-structure constant $\\alpha_{\\mathrm{em}}$"),
    (re.compile(r"β_NTE\s*≈\s*1/137"), "α_em ≈ 1/137"),
    (re.compile(r"β_NTE\s*≈\s*0\.00729"), "α_em ≈ 0.00729"),
    (re.compile(r"β_NTE₁"), "α₁"),
    (re.compile(r"β_NTE₂"), "α₂"),
    (re.compile(r"β_NTE₃"), "α₃"),
    (re.compile(r"H\s*=\s*\\alpha\|"), r"H = \\beta_{\\mathrm{NTE}}|"),
    (re.compile(r"H\(N\)\s*=\s*\\alpha\|"), r"H(N) = \\beta_{\\mathrm{NTE}}|"),
]

# Forward: H-coefficient α → β_NTE (after protect)
FORWARD_FIXES: list[tuple[re.Pattern[str], str]] = [
    # math-mode chains (solar / tier register)
    (re.compile(r"\$\\alpha\$\-chain"), r"$\\beta_{\\mathrm{NTE}}$-chain"),
    (re.compile(r"\$\\alpha\$\-coupling"), r"$\\beta_{\\mathrm{NTE}}$-coupling"),
    (re.compile(r"\$\\alpha\$\s+chain"), r"$\\beta_{\\mathrm{NTE}}$ chain"),
    (re.compile(r"characterisation of \$\\alpha\$"), r"characterisation of $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"decoupling \$\\alpha\$"), r"decoupling $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"deriving \$\\alpha\$"), r"deriving $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"framework's \$\\alpha\$ coupling"), r"framework's $\\beta_{\\mathrm{NTE}}$ coupling"),
    (re.compile(r"set by \$\\alpha\$"), r"set by $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"invoke \$\\alpha\$"), r"invoke $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"enters the \$\\alpha\$"), r"enters the $\\beta_{\\mathrm{NTE}}$"),
    (re.compile(r"upstream \$\\alpha\$\-chain"), r"upstream $\\beta_{\\mathrm{NTE}}$-chain"),
    (re.compile(r"No \$\\alpha\$\-chain"), r"No $\\beta_{\\mathrm{NTE}}$-chain"),
    (re.compile(r"\\alpha_\{\\rm char\}"), r"\\beta_{\\mathrm{NTE},\\mathrm{char}}"),
    (re.compile(r"\\alpha_\{char\}"), r"\\beta_{\\mathrm{NTE},\\mathrm{char}}"),
    # prose
    (re.compile(r"coupling α is empirically", re.I), "coupling β_NTE is empirically"),
    (re.compile(r"coupling α has observational", re.I), "coupling β_NTE has observational"),
    (re.compile(r"deriving α from geometry", re.I), "deriving β_NTE from geometry"),
    (re.compile(r"α geometric unloading", re.I), "β_NTE geometric unloading"),
    (re.compile(r"α unloading", re.I), "β_NTE unloading"),
    (re.compile(r"α-decoupled", re.I), "β_NTE-decoupled"),
    (re.compile(r"α-chain caveat", re.I), "β_NTE-chain caveat"),
    (re.compile(r"α-chain circularity", re.I), "β_NTE-chain circularity"),
    (re.compile(r"α-chain dependency", re.I), "β_NTE-chain dependency"),
    (re.compile(r"α-chain input", re.I), "β_NTE-chain input"),
    (re.compile(r"α-chain tier", re.I), "β_NTE-chain tier"),
    (re.compile(r"the α chain", re.I), "the β_NTE chain"),
    (re.compile(r"through the α chain", re.I), "through the β_NTE chain"),
    (re.compile(r"Ω_Λ → α\b"), "Ω_Λ → β_NTE"),
    (re.compile(r"feeds α anchoring", re.I), "feeds β_NTE anchoring"),
    (re.compile(r"enters α anchoring", re.I), "enters β_NTE anchoring"),
    (re.compile(r"empirical characterisation of α\b"), "empirical characterisation of β_NTE"),
    (re.compile(r"characterisation of α uses", re.I), "characterisation of β_NTE uses"),
    (re.compile(r"characterisation of α\b"), "characterisation of β_NTE"),
    (re.compile(r"deriving \*\*α\*\*"), "deriving **β_NTE**"),
    (re.compile(r"does not derive α\b", re.I), "does not derive β_NTE"),
    (re.compile(r"derive α\b", re.I), "derive β_NTE"),
    (re.compile(r"deriving α\b", re.I), "deriving β_NTE"),
    (re.compile(r"α's value", re.I), "β_NTE's value"),
    (re.compile(r"α is dimensionful", re.I), "β_NTE is dimensionful"),
    (re.compile(r"Ties \*\*α\*\*"), "Ties **β_NTE**"),
    (re.compile(r"Relates α to", re.I), "Relates β_NTE to"),
    (re.compile(r"H = α\|Φ_NTE\|²"), "H = β_NTE|Φ_NTE|²"),
    (re.compile(r"H = α\|Φ\|²"), "H = β_NTE|Φ|²"),
    (re.compile(r"H\(N\) = α\|"), "H(N) = β_NTE|"),
    (re.compile(r"H\(x,N\) = α\|"), "H(x,N) = β_NTE|"),
    (re.compile(r"\*H\* = α\|Φ_NTE\|²"), "*H* = β_NTE|Φ_NTE|²"),
    (re.compile(r"\*H\* = α\|Φ\|²"), "*H* = β_NTE|Φ|²"),
    (re.compile(r"dt/dN = 1/\(α\|"), "dt/dN = 1/(β_NTE|"),
    (re.compile(r"dt = dN/\(α\|"), "dt = dN/(β_NTE|"),
    (re.compile(r"\(3α²/\(8πG\)\)"), "(3β_NTE²/(8πG))"),
    (re.compile(r"\(3α\^2/\(8πG\)\)"), "(3β_NTE²/(8πG))"),
    (re.compile(r"α²/8\)Φ⁶"), "β_NTE²/8)Φ⁶"),
    (re.compile(r"α²/8\)Φ\^6"), "β_NTE²/8)Φ^6"),
    (re.compile(r"− \(α²/8\)"), "− (β_NTE²/8)"),
    (re.compile(r"- \(α²/8\)"), "- (β_NTE²/8)"),
    (re.compile(r"α = 2\.38"), "β_NTE = 2.38"),
    (re.compile(r"α = \(1/M_P\)"), "β_NTE = (1/M_P)"),
    (re.compile(r"cosmological coupling constant α\b"), "cosmological coupling constant β_NTE"),
    (re.compile(r"inherited constant α\b"), "inherited constant β_NTE"),
    (re.compile(r"same constant α\b"), "same constant β_NTE"),
    (re.compile(r"constant α that sets", re.I), "constant β_NTE that sets"),
    (re.compile(r"constant α …", re.I), "constant β_NTE …"),
    (re.compile(r"constant α,"), "constant β_NTE,"),
    (re.compile(r"anchoring of α\b"), "anchoring of β_NTE"),
    (re.compile(r"unloading of α\b"), "unloading of β_NTE"),
    (re.compile(r"geometric unloading of α\b"), "geometric unloading of β_NTE"),
    (re.compile(r"promotion-path-to-clean-Tier-A explicitly registered \(geometric unloading of α", re.I),
     "promotion-path-to-clean-Tier-A explicitly registered (geometric unloading of β_NTE"),
]

GLOSSARY_ALPHA_ROW = (
    "| **α** | Fine-structure / framework coupling; partly **anchored through Ω_Λ** (β_NTE-chain caveat). → Companion 11, S2 Note 5 |"
)
GLOSSARY_ALPHA_ROW_NEW = (
    "| **α_em** | Electromagnetic **fine-structure constant** ≈ 1/137; measured SM input in g_eff·α_em coincidence (Part 1 §2.4.2). → Part 1, Part 3 |\n"
    "| **β_NTE** | Cosmological H-coefficient in **H = β_NTE \\|Φ_NTE\\|²** (≈ 2.38×10⁻⁴⁷ GeV⁻¹); partly **anchored through Ω_Λ** (β_NTE-chain caveat). → Companion 11, S2 Note 5 |"
)


def should_skip(path: Path) -> bool:
    if any(p in SKIP_FILE_PARTS for p in path.parts):
        return True
    if path.name in SKIP_FILE_PARTS:
        return True
    if any(part in SKIP_DIR_NAMES for part in path.parts):
        return True
    if path.suffix.lower() not in {".md", ".txt"}:
        return True
    return False


def collect_files() -> list[Path]:
    files: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.is_file() and not should_skip(p):
                files.append(p)
    return sorted(set(files))


def protect(text: str) -> tuple[str, list[tuple[str, str]]]:
    maps: list[tuple[str, str]] = []
    for rx, tok in PROTECT_PATTERNS:
        def repl(m: re.Match[str], t: str = tok) -> str:
            maps.append((t, m.group(0)))
            return t
        text = rx.sub(repl, text)
    return text, maps


def unprotect(text: str, maps: list[tuple[str, str]]) -> str:
    for tok, orig in reversed(maps):
        text = text.replace(tok, orig, 1)
    return text


def apply_fixes(text: str) -> tuple[str, int]:
    n = 0
    for rx, repl in REVERSE_FIXES + FORWARD_FIXES:
        if callable(repl):
            new, c = rx.subn(repl, text)
        elif "\\" in repl:
            new, c = rx.subn(lambda _m, r=repl: r, text)
        else:
            new, c = rx.subn(repl, text)
        if c:
            n += c
            text = new
    return text, n


def post_glossary(text: str, path: Path) -> tuple[str, int]:
    if path.name != "NTE_Reader_Glossary_Companion_v1_0.md":
        return text, 0
    if GLOSSARY_ALPHA_ROW in text:
        return text.replace(GLOSSARY_ALPHA_ROW, GLOSSARY_ALPHA_ROW_NEW), 1
    return text, 0


def value_collision_scan(text: str, path: str) -> list[dict]:
    flags = []
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(r"β_NTE.*1/137|β_NTE.*0\.00729|fine-structure.*β_NTE", line, re.I):
            flags.append({"line": i, "issue": "β_NTE with EM value", "excerpt": line[:200]})
        if re.search(r"β_NTE[₁₂₃]|β_NTE_\{?[123]\}", line):
            flags.append({"line": i, "issue": "β_NTE subscript looks like gauge coupling", "excerpt": line[:200]})
    return flags


def process(path: Path, apply: bool) -> dict:
    raw = path.read_text(encoding="utf-8")
    original = raw
    protected, maps = protect(raw)
    fixed, n = apply_fixes(protected)
    fixed = unprotect(fixed, maps)
    fixed, gn = post_glossary(fixed, path)
    n += gn
    residual = value_collision_scan(fixed, str(path))
    changed = fixed != original
    if apply and changed:
        path.write_text(fixed, encoding="utf-8", newline="\n")
    return {
        "path": str(path.relative_to(DESKTOP)),
        "changed": changed,
        "subs": n,
        "residual": residual,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    files = collect_files()
    reports = [process(p, args.apply) for p in files]
    changed = [r for r in reports if r["changed"]]
    residual = [r for r in reports if r["residual"]]
    out = ROOT / "Working" / "alpha_beta_nte_corpus_fix_report.json"
    out.write_text(json.dumps({"changed": changed, "residual": residual, "total": len(files)}, indent=2), encoding="utf-8")
    print(f"Scanned {len(files)} files; changed {len(changed)}; residual flags {len(residual)}")
    if changed:
        for r in changed[:40]:
            print(f"  {r['subs']:3d}  {r['path']}")
        if len(changed) > 40:
            print(f"  ... +{len(changed)-40} more")
    if residual:
        print("RESIDUAL:")
        for r in residual:
            for f in r["residual"]:
                print(f"  {r['path']}:{f['line']} {f['issue']}")


if __name__ == "__main__":
    main()
