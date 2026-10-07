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
BOARD = ROOT.parent / "ANOMALY_FIRST_STATUS_BOARD_Cursor_Main.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"status": "READY", "round": 0, "history": []}


def save_state(st: dict) -> None:
    st["updated_utc"] = utc_now()
    STATE.write_text(json.dumps(st, indent=2) + "\n", encoding="utf-8")


def write_board(st: dict) -> None:
    BOARD.write_text(
        f"""# Anomaly-first search — status board

**Updated:** {st.get('updated_utc') or utc_now()}  
**Status:** **{st.get('status')}** · Round **{st.get('round', 0)}**  
**Guard:** independently strange → then NTE contact. No predict-then-hunt. No 4th-sterile CONTACT.  
**Directive:** `Handoffs/Directive_Cursor_Main_Anomaly_First_Search_Elliptic_dS_Lead_No_Sterile_Scratch_Jammer_Clones_20261007.md`
""",
        encoding="utf-8",
    )


def seed_round(st: dict) -> dict:
    st["round"] = int(st.get("round") or 0) + 1
    rnd = st["round"]
    rd = ROUNDS / f"R{rnd:02d}"
    rd.mkdir(parents=True, exist_ok=True)
    guard = "`Working/anomaly_first_search/ANOMALY_FIRST_GUARD.md`"
    directive = "`Handoffs/Directive_Cursor_Main_Anomaly_First_Search_Elliptic_dS_Lead_No_Sterile_Scratch_Jammer_Clones_20261007.md`"
    (rd / "BRIEF_Scratch.md").write_text(
        f"""# R{rnd:02d} — Cursor Scratch (constructive, blind)

1. Read {directive} and {guard}
2. Run `python Working/anomaly_first_search/run_inventory.py`
3. **Tier 1 first:** sourced elliptic dS literature; land **E1–E4** with baryogenesis/free-vs-quotient cost named
4. **Tier 2:** anomaly-first table for N1–N4, G1, C1–C3 — IND/WEAK/NONE then STERILE/CONTACT/NOCONTACT
5. **Tier 3:** L1/L2 brief only
6. Global **A1–A4**. No Core patches. No sterile CONTACT. No predict-then-hunt.
7. File `Working/anomaly_first_search/rounds/R{rnd:02d}/Scratch_VERDICT.md` with `**Lands: E? and A?**`
Sign **Cursor Scratch**. Do not read Jammer.
""",
        encoding="utf-8",
    )
    (rd / "BRIEF_Jammer.md").write_text(
        f"""# R{rnd:02d} — Cursor Jammer (adversarial, blind)

1. Read {directive} and {guard}
2. Run `python Working/anomaly_first_search/run_inventory.py`
3. **Enforce the guard** — reject any predict-then-hunt framing
4. Press elliptic dS **E3** / mod-paths P12 cost (quotient vs free antipodal / §8.4 sorting)
5. Kill sterile-smuggle CONTACT on N1–N4; Companion 7 forbids 4th light Majorana
6. Global **A1–A4**. File `Working/anomaly_first_search/rounds/R{rnd:02d}/Jammer_VERDICT.md` with `**Lands: E? and A?**`
Sign **Cursor Jammer**. Do not read Scratch.
""",
        encoding="utf-8",
    )
    (rd / "META.json").write_text(
        json.dumps({"round": rnd, "seeded_utc": utc_now(), "guard": "anomaly-first"}, indent=2)
        + "\n",
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
        raise SystemExit("missing verdicts")

    def land(txt: str, letter: str) -> str | None:
        m = re.search(rf"Lands?:\s*\*?\*?({letter}[1-4])", txt, re.I)
        if m:
            return m.group(1).upper()
        m = re.search(rf"\b({letter}[1-4])\b", txt)
        return m.group(1).upper() if m else None

    stxt, jtxt = sp.read_text(encoding="utf-8"), jp.read_text(encoding="utf-8")
    se, sa = land(stxt, "E"), land(stxt, "A")
    je, ja = land(jtxt, "E"), land(jtxt, "A")
    agree = bool(se and je and sa and ja and se == je and sa == ja)
    score = {
        "round": rnd,
        "Scratch": {"E": se, "A": sa},
        "Jammer": {"E": je, "A": ja},
        "agree": agree,
        "scored_utc": utc_now(),
    }
    (rd / "SCORE.json").write_text(json.dumps(score, indent=2) + "\n", encoding="utf-8")
    st["history"] = (st.get("history") or []) + [score]
    st["status"] = "CONVERGED" if agree else "DIVERGED"
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
        print(json.dumps({k: st.get(k) for k in ("status", "round")}, indent=2))
        write_board(st)
    else:
        write_board(st)


if __name__ == "__main__":
    main()
