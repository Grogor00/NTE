#!/usr/bin/env python3
"""Seed/score Scratch+Jammer for single-kinetic ontology-cost programme."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUNDS = ROOT / "rounds"
STATE = ROOT / "state.json"
BOARD = ROOT.parent / "NU_SINGLE_KINETIC_STATUS_BOARD_Cursor_Main.md"
STOP = ROOT / "STOP"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state() -> dict:
    if STATE.exists():
        st = json.loads(STATE.read_text(encoding="utf-8"))
    else:
        st = {"status": "READY", "round": 0, "converged": False, "history": []}
    if STOP.exists():
        st["status"] = "STOPPED"
    return st


def save_state(st: dict) -> None:
    st["updated_utc"] = utc_now()
    STATE.write_text(json.dumps(st, indent=2) + "\n", encoding="utf-8")


def write_board(st: dict) -> None:
    hist = st.get("history") or []
    rows = "\n".join(
        f"| R{h.get('round')} | {h.get('K')} | agree={h.get('agree')} | {h.get('note','')} |"
        for h in hist[-10:]
    ) or "| — | — | — | — |"
    BOARD.write_text(
        f"""# Drop shared-ν second kinetic — status board

**Updated:** {st.get('updated_utc') or utc_now()}  
**Status:** **{st.get('status')}** · Round **{st.get('round', 0)}** · Converged: **{st.get('converged')}**  
**Directive:** `Handoffs/Directive_Cursor_Main_Drop_Shared_Nu_Second_Kinetic_Ontology_Cost_Scratch_Jammer_Clones_20261007.md`  
**Prior:** CPN+Gravity R01 → **G2**

## History

| Round | K forks | Agree | Note |
|---|---|---|---|
{rows}
""",
        encoding="utf-8",
    )


def seed_round(st: dict) -> dict:
    st["round"] = int(st.get("round") or 0) + 1
    rnd = st["round"]
    rd = ROUNDS / f"R{rnd:02d}"
    rd.mkdir(parents=True, exist_ok=True)
    scratch = f"""# Round R{rnd:02d} — Cursor Scratch brief (constructive, blind)

**Programme:** Drop shared-ν second kinetic — ontology cost.

1. Read `Handoffs/Directive_Cursor_Main_Drop_Shared_Nu_Second_Kinetic_Ontology_Cost_Scratch_Jammer_Clones_20261007.md`
2. Run `python Working/nu_single_kinetic_loop/run_all.py`
3. Read `Working/nu_single_kinetic_loop/results/KINETIC_COST_RESULTS.md`
4. Deposit check: Part 2 (both-EOM stress; bilateral action §IX), Companion 5/7 (bilateral support, κ₀), Part 1 §VI.
5. **Constructive:** Strongest honest case that single-kinetic still carries bilateral/bridge work (lean K1 or K3 if deposit allows).
6. File `Working/nu_single_kinetic_loop/rounds/R{rnd:02d}/Scratch_VERDICT.md` with `**Lands: K?**`
7. Sign **Cursor Scratch**. Do not read Jammer. No Core patches. No κ restore.
"""
    jammer = f"""# Round R{rnd:02d} — Cursor Jammer brief (adversarial, blind)

**Programme:** Drop shared-ν second kinetic — ontology cost.

1. Read `Handoffs/Directive_Cursor_Main_Drop_Shared_Nu_Second_Kinetic_Ontology_Cost_Scratch_Jammer_Clones_20261007.md`
2. Run `python Working/nu_single_kinetic_loop/run_all.py`
3. Read `Working/nu_single_kinetic_loop/results/KINETIC_COST_RESULTS.md`
4. Deposit check: Part 2 literal “stress-energy appears in both Einstein equations”; §IX shared ν sector.
5. **Adversarial:** Is K1 a smuggle? Press that both-EOM stress is load-bearing (K2) or that drop kills the backbone (K4).
6. File `Working/nu_single_kinetic_loop/rounds/R{rnd:02d}/Jammer_VERDICT.md` with `**Lands: K?**`
7. Sign **Cursor Jammer**. Do not read Scratch. No Core patches. No κ restore.
"""
    (rd / "BRIEF_Scratch.md").write_text(scratch, encoding="utf-8")
    (rd / "BRIEF_Jammer.md").write_text(jammer, encoding="utf-8")
    (rd / "META.json").write_text(
        json.dumps({"round": rnd, "seeded_utc": utc_now(), "prior": "G2"}, indent=2) + "\n",
        encoding="utf-8",
    )
    st["status"] = "RUNNING"
    save_state(st)
    write_board(st)
    print(f"Seeded {rd}")
    return st


def score_round(st: dict, rnd: int | None = None) -> dict:
    rnd = rnd or int(st.get("round") or 0)
    rd = ROUNDS / f"R{rnd:02d}"
    sp, jp = rd / "Scratch_VERDICT.md", rd / "Jammer_VERDICT.md"
    if not sp.exists() or not jp.exists():
        raise SystemExit(f"Missing verdicts in {rd}")

    def land(txt: str) -> str | None:
        m = re.search(r"Lands?:\s*\*?\*?(K[1-4])", txt, re.I)
        if m:
            return m.group(1).upper()
        m = re.search(r"\b(K[1-4])\b", txt)
        return m.group(1).upper() if m else None

    sk, jk = land(sp.read_text(encoding="utf-8")), land(jp.read_text(encoding="utf-8"))
    agree = bool(sk and jk and sk == jk)
    score = {
        "round": rnd,
        "Scratch": sk,
        "Jammer": jk,
        "agree": agree,
        "scored_utc": utc_now(),
        "note": f"Scratch {sk}; Jammer {jk}",
    }
    (rd / "SCORE.json").write_text(json.dumps(score, indent=2) + "\n", encoding="utf-8")
    st["history"] = (st.get("history") or []) + [
        {"round": rnd, "K": f"{sk}/{jk}", "agree": agree, "note": score["note"]}
    ]
    st["converged"] = agree
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
