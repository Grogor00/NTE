#!/usr/bin/env python3
"""Seed Scratch/Jammer briefs and score agreement for CPN+Gravity programme."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUNDS = ROOT / "rounds"
STATE = ROOT / "state.json"
BOARD = ROOT.parent / "CPN_GRAVITY_STATUS_BOARD_Cursor_Main.md"
STOP = ROOT / "STOP"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state() -> dict:
    if STATE.exists():
        st = json.loads(STATE.read_text(encoding="utf-8"))
    else:
        st = {
            "status": "READY",
            "round": 0,
            "converged": False,
            "history": [],
        }
    if STOP.exists():
        st["status"] = "STOPPED"
    return st


def save_state(st: dict) -> None:
    st["updated_utc"] = utc_now()
    STATE.write_text(json.dumps(st, indent=2) + "\n", encoding="utf-8")


def write_board(st: dict) -> None:
    hist = st.get("history") or []
    rows = "\n".join(
        f"| R{h.get('round')} | P={h.get('P')} G={h.get('G')} | agree={h.get('agree')} | {h.get('note','')} |"
        for h in hist[-10:]
    ) or "| — | — | — | — |"
    md = f"""# CPN relation + gravity completion — status board

**Updated:** {st.get('updated_utc') or utc_now()}  
**Status:** **{st.get('status')}** · Round **{st.get('round', 0)}** · Converged: **{st.get('converged')}**  
**Directive:** `Handoffs/Directive_Cursor_Main_CPN_Relation_And_Gravity_Completion_Programme_Scratch_Jammer_Clones_20261007.md`

## Gates

| Gate | Meaning |
|---|---|
| P-fork | Scratch + Jammer land same Track-P fork (or reasoned dissent filed) |
| G-fork | Scratch + Jammer land same Track-G fork |
| Probes | `results/probe_results.json` present |
| No-restore | No κ=Ω_DM / Planck538 revive |

## History

| Round | Forks | Agree | Note |
|---|---|---|---|
{rows}

## Stop

Create `Working/cpn_gravity_loop/STOP` or tell Main to stop.
"""
    BOARD.write_text(md, encoding="utf-8")


def seed_round(st: dict) -> dict:
    st["round"] = int(st.get("round") or 0) + 1
    rnd = st["round"]
    rd = ROUNDS / f"R{rnd:02d}"
    rd.mkdir(parents=True, exist_ok=True)

    scratch = f"""# Round R{rnd:02d} — Cursor Scratch brief (constructive, blind)

**Track primary: P — CPN relation.** Secondary: run gravity probe numbers only.

1. Read directive: `Handoffs/Directive_Cursor_Main_CPN_Relation_And_Gravity_Completion_Programme_Scratch_Jammer_Clones_20261007.md`
2. Run (or re-run): `python Working/cpn_gravity_loop/run_all.py`
3. Read `Working/cpn_gravity_loop/results/CPN_MAP_RESULTS.md` and `GRAVITY_COMPLETION_RESULTS.md`
4. **Constructive job:** Can any map (esp. M5 composite, M1+M2+M4 package) honestly advance past O2 C-3? Stress-test probe flags against deposit. Land **P1–P4**.
5. Cross-check gravity mechanical hint; land **G1–G4** briefly (adversarial depth is Jammer's).
6. File: `Working/cpn_gravity_loop/rounds/R{rnd:02d}/Scratch_VERDICT.md`
7. Sign **Cursor Scratch**. Do **not** read Jammer's verdict before filing.
8. No Core patches. No κ restore.
"""
    jammer = f"""# Round R{rnd:02d} — Cursor Jammer brief (adversarial, blind)

**Track primary: G — Gravity completion.** Secondary: attack CPN probe optimism.

1. Read directive: `Handoffs/Directive_Cursor_Main_CPN_Relation_And_Gravity_Completion_Programme_Scratch_Jammer_Clones_20261007.md`
2. Run (or re-run): `python Working/cpn_gravity_loop/run_all.py`
3. Read `Working/cpn_gravity_loop/results/GRAVITY_COMPLETION_RESULTS.md` and `CPN_MAP_RESULTS.md`
4. **Adversarial job:** Press H0–H3 / N0 against 1408.0487 and constraint gaps. Does any path give G1 without ontology cost? Land **G1–G4**.
5. Attack M5 "full_work" flags — is P2 smuggling a Core patch? Land **P1–P4**.
6. File: `Working/cpn_gravity_loop/rounds/R{rnd:02d}/Jammer_VERDICT.md`
7. Sign **Cursor Jammer**. Do **not** read Scratch's verdict before filing.
8. No Core patches. No κ restore.
"""
    (rd / "BRIEF_Scratch.md").write_text(scratch, encoding="utf-8")
    (rd / "BRIEF_Jammer.md").write_text(jammer, encoding="utf-8")
    (rd / "META.json").write_text(
        json.dumps({"round": rnd, "seeded_utc": utc_now()}, indent=2) + "\n",
        encoding="utf-8",
    )
    st["status"] = "RUNNING"
    save_state(st)
    write_board(st)
    print(f"Seeded {rd}")
    return st


def _fork(text: str, letter: str) -> str | None:
    # match **P3** or Lands: P3 or Track P: **P3**
    m = re.search(rf"\b{letter}([1-4])\b", text)
    return f"{letter}{m.group(1)}" if m else None


def score_round(st: dict, rnd: int | None = None) -> dict:
    rnd = rnd or int(st.get("round") or 0)
    rd = ROUNDS / f"R{rnd:02d}"
    sp = rd / "Scratch_VERDICT.md"
    jp = rd / "Jammer_VERDICT.md"
    if not sp.exists() or not jp.exists():
        raise SystemExit(f"Missing verdicts in {rd}")
    stxt = sp.read_text(encoding="utf-8")
    jtxt = jp.read_text(encoding="utf-8")
    # Prefer explicit "Lands:" lines
    def land(txt: str, letter: str) -> str | None:
        m = re.search(rf"Lands?:\s*\*?\*?({letter}[1-4])", txt, re.I)
        if m:
            return m.group(1).upper()
        return _fork(txt, letter)

    sp_p, sp_g = land(stxt, "P"), land(stxt, "G")
    jp_p, jp_g = land(jtxt, "P"), land(jtxt, "G")
    agree = bool(sp_p and jp_p and sp_g and jp_g and sp_p == jp_p and sp_g == jp_g)
    note = f"Scratch P={sp_p} G={sp_g}; Jammer P={jp_p} G={jp_g}"
    score = {
        "round": rnd,
        "Scratch": {"P": sp_p, "G": sp_g},
        "Jammer": {"P": jp_p, "G": jp_g},
        "agree": agree,
        "scored_utc": utc_now(),
        "note": note,
    }
    (rd / "SCORE.json").write_text(json.dumps(score, indent=2) + "\n", encoding="utf-8")
    st["history"] = (st.get("history") or []) + [
        {"round": rnd, "P": f"{sp_p}/{jp_p}", "G": f"{sp_g}/{jp_g}", "agree": agree, "note": note}
    ]
    st["converged"] = bool(agree)
    st["status"] = "CONVERGED" if agree else "DIVERGED"
    save_state(st)
    write_board(st)
    print(json.dumps(score, indent=2))
    return st


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["status", "seed-round", "score", "board", "request-stop"])
    ap.add_argument("--round", type=int, default=None)
    args = ap.parse_args()
    st = load_state()
    if args.cmd == "status":
        print(json.dumps({k: st.get(k) for k in ("status", "round", "converged")}, indent=2))
        write_board(st)
    elif args.cmd == "board":
        write_board(st)
    elif args.cmd == "seed-round":
        seed_round(st)
    elif args.cmd == "score":
        score_round(st, args.round)
    elif args.cmd == "request-stop":
        STOP.write_text("stop\n", encoding="utf-8")
        st["status"] = "STOPPED"
        save_state(st)
        write_board(st)


if __name__ == "__main__":
    main()
