#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUNDS = ROOT / "rounds"
STATE = ROOT / "state.json"
BOARD = ROOT.parent / "COSMO_MOD_PATHS_STATUS_BOARD_Cursor_Main.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"status": "READY", "round": 0, "converged": False, "history": []}


def save_state(st: dict) -> None:
    st["updated_utc"] = utc_now()
    STATE.write_text(json.dumps(st, indent=2) + "\n", encoding="utf-8")


def write_board(st: dict) -> None:
    hist = st.get("history") or []
    rows = "\n".join(
        f"| R{h.get('round')} | agree={h.get('agree')} | {h.get('note','')} |"
        for h in hist[-8:]
    ) or "| — | — | — |"
    BOARD.write_text(
        f"""# Cosmology mod-paths — status board

**Updated:** {st.get('updated_utc') or utc_now()}  
**Status:** **{st.get('status')}** · Round **{st.get('round', 0)}**  
**Directive:** `Handoffs/Directive_Cursor_Main_Cosmology_Mod_Paths_Keep_Particle_Locks_Scratch_Jammer_Clones_20261007.md`

| Round | Agree | Note |
|---|---|---|
{rows}
""",
        encoding="utf-8",
    )


def seed_round(st: dict) -> dict:
    st["round"] = int(st.get("round") or 0) + 1
    rnd = st["round"]
    rd = ROUNDS / f"R{rnd:02d}"
    rd.mkdir(parents=True, exist_ok=True)
    common = f"""
Read:
- `Handoffs/Directive_Cursor_Main_Cosmology_Mod_Paths_Keep_Particle_Locks_Scratch_Jammer_Clones_20261007.md`
- `Working/cosmo_mod_paths/PARTICLE_LOCK.md`
- Run `python Working/cosmo_mod_paths/run_all.py`
- Read `Working/cosmo_mod_paths/results/PATH_CATALOG_RESULTS.md`
Priors: P3/G2/K2∩K3; κ amplifier withdrawn; CDM/origin open; AC honest-path two-register.
"""
    (rd / "BRIEF_Scratch.md").write_text(
        f"""# R{rnd:02d} — Cursor Scratch (constructive, blind)
{common}
**Job:** Maximal honest KEEP set. Build a **recommended stack** (ordered combo) that could describe cosmology while preserving L1–L10.
Tag every path P01–P12 as KEEP / COST / KILL / PRES.
File `Working/cosmo_mod_paths/rounds/R{rnd:02d}/Scratch_VERDICT.md`
Sign **Cursor Scratch**. Do not read Jammer. No silent Core patches. No-f.
""",
        encoding="utf-8",
    )
    (rd / "BRIEF_Jammer.md").write_text(
        f"""# R{rnd:02d} — Cursor Jammer (adversarial, blind)
{common}
**Job:** Kill restore-shaped paths (esp. P11), unproven 1408 exceptions (P10), and any KEEP that breaks L1–L10 or smuggles κ=Ω_DM. Attack soft KEEP on P05/P06/P12.
Tag every path P01–P12 as KEEP / COST / KILL / PRES. Recommended stack = safest surviving combo (may be thinner than Scratch).
File `Working/cosmo_mod_paths/rounds/R{rnd:02d}/Jammer_VERDICT.md`
Sign **Cursor Jammer**. Do not read Scratch. No silent Core patches. No-f.
""",
        encoding="utf-8",
    )
    (rd / "META.json").write_text(
        json.dumps({"round": rnd, "seeded_utc": utc_now()}, indent=2) + "\n", encoding="utf-8"
    )
    st["status"] = "RUNNING"
    save_state(st)
    write_board(st)
    print(f"Seeded {rd}")
    return st


def _tags(text: str) -> dict[str, str]:
    out = {}
    for pid in [f"P{i:02d}" for i in range(1, 13)]:
        # allow **P01** bold, pipes, etc.
        m = re.search(
            rf"\|?\s*\*?\*?{pid}\*?\*?\s*\|?\s*\*?\*?(KEEP|COST|KILL|PRES)\*?\*?",
            text,
            re.I,
        )
        if m:
            out[pid] = m.group(1).upper()
    return out


def score_round(st: dict, rnd: int | None = None) -> dict:
    rnd = rnd or int(st.get("round") or 0)
    rd = ROUNDS / f"R{rnd:02d}"
    sp, jp = rd / "Scratch_VERDICT.md", rd / "Jammer_VERDICT.md"
    if not sp.exists() or not jp.exists():
        raise SystemExit("missing verdicts")
    stags, jtags = _tags(sp.read_text(encoding="utf-8")), _tags(jp.read_text(encoding="utf-8"))
    keys = sorted(set(stags) | set(jtags))
    agree_n = sum(1 for k in keys if stags.get(k) == jtags.get(k))
    score = {
        "round": rnd,
        "Scratch": stags,
        "Jammer": jtags,
        "n_compared": len(keys),
        "n_agree": agree_n,
        "agree_all": bool(keys) and agree_n == len(keys) and len(stags) == 12 and len(jtags) == 12,
        "scored_utc": utc_now(),
    }
    (rd / "SCORE.json").write_text(json.dumps(score, indent=2) + "\n", encoding="utf-8")
    st["history"] = (st.get("history") or []) + [
        {
            "round": rnd,
            "agree": score["agree_all"],
            "note": f"tag-agree {agree_n}/{len(keys)}",
        }
    ]
    st["converged"] = score["agree_all"]
    st["status"] = "CONVERGED" if score["agree_all"] else "DIVERGED"
    save_state(st)
    write_board(st)
    print(json.dumps(score, indent=2))
    return st


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["seed-round", "score", "status", "board"])
    ap.add_argument("--round", type=int, default=None)
    args = ap.parse_args()
    st = load_state()
    if args.cmd == "seed-round":
        seed_round(st)
    elif args.cmd == "score":
        score_round(st, args.round)
    elif args.cmd == "status":
        print(json.dumps({k: st.get(k) for k in ("status", "round", "converged")}, indent=2))
        write_board(st)
    else:
        write_board(st)


if __name__ == "__main__":
    main()
