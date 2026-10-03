#!/usr/bin/env python3
"""PC pass-two: apply Handoff_PC_to_Cursor_AC_AlphaToBeta_Ambiguity_Resolutions §2-§4."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import alpha_to_beta_nte_audit as audit

A = "\u03b1"
B = "\u03b2_NTE"

PASS_TWO_FILES = [
    "NTE_v10_17_Part3_Accounting.md",
    "Companion_8_VNTE_Trajectory_v10_8.md",
    "Companion_9_VNTE_Stage3_v10_8.md",
    "NTE_v10_17_Part1_Foundations.md",
    "Paper_PhiNTE_Necessity_and_Irreducibility_v0_1_Scratch_20260603.md",
    "Companion_11_Lambda_Unimodular_Closure_v10_17_2.md",
    "NTE_v10_17_Part2_Structure.md",
    "Paper_PhiNTE_Necessity_PedagogicalPivot_v0_1_PC_20260604.md",
    "Paper_Popular_v10_8_Full_Edition.md",
    "17.5.4_Audit_NLock_Derivation.md",
    "Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md",
    "Companion_5_StateSpace_Surface_v10_8.md",
    "Companion_7_Neutrino_v10_17_2.md",
    "Companion_7_v10_9_to_v10_17_2_Finalisation_Pass_20260524.md",
    "NTE_Standalone_Papers_Register_v0_4.md",
    "Paper_Popular_v10_8_Reader_Edition.md",
]

# §3 recursion (Part 1) — before generic protect
RECURSION = [
    (re.compile(r"\u03b1_\{n\+1\}"), "β_NTE,{n+1}"),
    (re.compile(r"\u03b1_\{daughter\}"), "β_NTE,daughter"),
    (re.compile(r"\u03b1_\{parent\}"), "β_NTE,parent"),
    (re.compile(r"\u03b1_n\b"), "β_NTE,n"),
    (re.compile(r"\u03b1_\{n\}"), "β_NTE,n"),
]

EXTRA_PROTECT = [
    (re.compile(r"\u03b1_s\b"), "__P_AS__"),
    (re.compile(r"\u03bd_\u03b1"), "__P_NUA__"),
    (re.compile(r"U_\u03b1i"), "__P_UAI__"),
    (re.compile(r"V_\u03b1\u03b2"), "__P_VAB__"),
    (re.compile(r"P\(\u03bd_\u03b1"), "__P_PNUA__"),
    (re.compile(r"\u03b1\|\\\u03bd_L"), "__P_AMP__"),  # |ν⟩ = α|ν_L
    (re.compile(r"=\s*\u03b1\\\|\\\u03bd_L"), "__P_AMP2__"),
    (re.compile(r"g_\{?\+?\}?\^\{\u03b1\u03b2\}"), "__P_GAB__"),
    (re.compile(r"T_\{\u03b1\u03b2\}"), "__P_TAB__"),
    (re.compile(r"\u03b1\u03b2"), "__P_AB__"),
    (re.compile(r"\u03b1_i\b"), "__P_AI__"),
    (re.compile(r"\u03b1_\d\(M_Pl\)"), "__P_RUN__"),
    (re.compile(r"\u03a3\u03b1_i"), "__P_SAI__"),
    (re.compile(r"\u03b1_char"), f"{B}_char"),
    (re.compile(r"\u03b1-chain"), f"{B}-chain"),
    (re.compile(r"Pathway\s+\u03b1", re.I), "__P_PATH__"),
    (re.compile(r"option\s+\u03b1\)", re.I), "__P_OPT__"),
    (re.compile(r"a_\{?0\}?\^?\u03b1"), "__P_HEAT__"),
    (re.compile(r"\u03b1_em", re.I), "__P_EM__"),
]

RESTORE = {
    "__P_AS__": None,  # restored from maps
}


def protect_extra(text: str) -> tuple[str, list[tuple[str, str]]]:
    maps: list[tuple[str, str]] = []
    for rx, tok in EXTRA_PROTECT:
        if tok.startswith("__P_") and tok not in ("__P_AB__",):

            def repl(m, t=tok):
                maps.append((t, m.group(0)))
                return t

            text = rx.sub(repl, text)
        else:
            text = rx.sub(tok, text)
    return text, maps


def restore_maps(text: str, maps: list[tuple[str, str]]) -> str:
    for tok, orig in reversed(maps):
        text = text.replace(tok, orig, 1)
    return text


def blanket_beta(text: str) -> str:
    """Replace remaining bare α with β_NTE."""
    return text.replace(A, B)


def process(path: Path, apply: bool) -> dict:
    before = path.read_text(encoding="utf-8")
    if A not in before:
        return {"path": str(path), "before": 0, "after": 0, "modified": False}

    n_before = before.count(A)
    t = before
    for rx, repl in RECURSION:
        t = rx.sub(repl, t)
    t, maps = protect_extra(t)
    t, maps2 = audit.protect_with_map(t)
    maps.extend(maps2)
    t, _ = audit.apply_replacements(t)
    t = blanket_beta(t)
    t = audit.unprotect_maps(t, [m for m in maps if m[0].startswith("__PROT")])
    t = restore_maps(t, [m for m in maps if m[0].startswith("__P_")])
    n_after = t.count(A)
    modified = t != before
    if apply and modified:
        path.write_text(t, encoding="utf-8")
    return {
        "path": path.name,
        "before": n_before,
        "after": n_after,
        "subs_est": n_before - n_after,
        "modified": modified,
    }


def main():
    apply = "--apply" in sys.argv
    root = Path(__file__).resolve().parent.parent
    papers = root / "Papers"
    working = root / "Working"
    results = []
    for name in PASS_TWO_FILES:
        fp = papers / name
        if not fp.exists():
            fp = working / name
        if not fp.exists():
            results.append({"path": name, "error": "not found"})
            continue
        results.append(process(fp, apply))

    out = working / "pc_pass_two_verification.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
