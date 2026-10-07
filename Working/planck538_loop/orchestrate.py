#!/usr/bin/env python3
"""Planck-comparable recovery loop orchestrator.

Commands:
  python orchestrate.py status
  python orchestrate.py seed-round          # advance queue → write briefs
  python orchestrate.py score --round N     # score filed lane results
  python orchestrate.py append-path --id Pxx --title "..." 
  python orchestrate.py request-stop
  python orchestrate.py tick                # seed if needed + print agent prompt JSON

Stop: create Working/planck538_loop/STOP or `request-stop`.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_PATH = ROOT / "state.json"
STOP_PATH = ROOT / "STOP"
ROUNDS = ROOT / "rounds"
BOARD = ROOT.parent / "PLANCK538_STATUS_BOARD_Cursor_Main.md"

BAND = (5.23, 5.53)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state() -> dict:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if STOP_PATH.exists():
        state["stop_requested"] = True
        if state.get("status") == "RUNNING":
            state["status"] = "STOPPED"
    return state


def save_state(state: dict) -> None:
    state["updated_utc"] = utc_now()
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def pending_paths(state: dict) -> list[dict]:
    return [p for p in state["path_queue"] if p.get("status") == "pending"]


def write_board(state: dict) -> None:
    pending = ", ".join(p["id"] for p in pending_paths(state)) or "(none)"
    active = ", ".join(state.get("active_path_ids") or []) or "(none)"
    hist = state.get("history") or []
    hist_lines = "\n".join(
        f"| R{h.get('round')} | {h.get('paths')} | V={h.get('V')} C={h.get('C')} A={h.get('A')} L={h.get('L')} | {h.get('note','')} |"
        for h in hist[-12:]
    ) or "| — | — | — | — |"
    md = (
        f"# Planck-comparable recovery — status board\n\n"
        f"**Updated:** {state.get('updated_utc') or utc_now()}  \n"
        f"**Status:** **{state.get('status')}** · Round **{state.get('round', 0)}** · "
        f"Converged: **{state.get('converged')}**  \n"
        f"**Directive:** `Handoffs/Directive_Cursor_Main_Planck538_Comparable_Recovery_Loop_20261007.md`  \n"
        f"**Stop:** create `Working/planck538_loop/STOP` or tell Greg/Main to stop.\n\n"
        f"## Success gates (all required)\n\n"
        f"| Gate | Meaning |\n|---|---|\n"
        f"| V | r_bg in [{BAND[0]}, {BAND[1]}] structurally (no-f) |\n"
        f"| C | Cold + collisionless + co-located at CMB epoch |\n"
        f"| A | Legitimate action / ghost-free (no smuggled S_cons) |\n"
        f"| L | Scratch + Jammer agree |\n\n"
        f"**Note:** kappa~5.50 already satisfies V. Withdrawal failed on C (and A).\n\n"
        f"## Live\n\n"
        f"| Item | Value |\n|---|---|\n"
        f"| Active paths | {active} |\n"
        f"| Pending queue | {pending} |\n"
        f"| Stop requested | {state.get('stop_requested')} |\n\n"
        f"## History (recent)\n\n"
        f"| Round | Paths | Gates | Note |\n|---|---|---|---|\n"
        f"{hist_lines}\n\n"
        f"## Closed negative\n\n"
    )
    for c in state.get("closed_negative") or []:
        md += f"- `{c.get('id')}`: {c.get('reason')}\n"
    BOARD.write_text(md, encoding="utf-8")


def seed_round(state: dict, n_paths: int = 2) -> dict:
    if state.get("stop_requested") or STOP_PATH.exists():
        state["status"] = "STOPPED"
        state["stop_requested"] = True
        save_state(state)
        write_board(state)
        return state
    if state.get("converged"):
        state["status"] = "CONVERGED"
        save_state(state)
        write_board(state)
        return state

    pend = pending_paths(state)
    if not pend:
        state["status"] = "EXHAUSTED"
        save_state(state)
        write_board(state)
        return state

    chosen = pend[:n_paths]
    state["round"] = int(state.get("round") or 0) + 1
    rnd = state["round"]
    state["active_path_ids"] = [p["id"] for p in chosen]
    state["status"] = "RUNNING"
    for p in state["path_queue"]:
        if p["id"] in state["active_path_ids"]:
            p["status"] = "in_progress"

    ROUNDS.mkdir(parents=True, exist_ok=True)
    round_dir = ROUNDS / f"R{rnd:02d}"
    round_dir.mkdir(exist_ok=True)

    path_block = "\n".join(
        f"- **{p['id']}** — {p['title']}\n  - V hope: {p.get('v_hope')}\n  - C risk: {p.get('c_risk')}"
        for p in chosen
    )

    scratch = (
        f"# Round R{rnd:02d} — Cursor Scratch brief (constructive, blind)\n\n"
        f"**Programme:** Planck-comparable recovery (V+C+A+L). No Core patches. No-f.\n"
        f"**Paths this round:**\n{path_block}\n\n"
        f"## Your job\n"
        f"For each path: propose concrete mechanism/action; estimate r_bg; "
        f"argue gates **V, C, A** PASS/FAIL with evidence.\n"
        f"Land: which paths survive; propose at most two *new structural* paths if all fail (no dials).\n\n"
        f"## Deliverable\n"
        f"`Working/planck538_loop/rounds/R{rnd:02d}/Scratch_VERDICT.md`\n"
        f"Also optional handoff under Handoffs/.\n\n"
        f"Sign as **Cursor Scratch**. Do not read Jammer's round file.\n"
    )
    jammer = (
        f"# Round R{rnd:02d} — Cursor Jammer brief (adversarial, blind)\n\n"
        f"**Programme:** Planck-comparable recovery (V+C+A+L). No Core patches. No-f.\n"
        f"**Paths this round:**\n{path_block}\n\n"
        f"## Your job\n"
        f"Kill: number-without-character; no-f dials; smuggled S_cons / T-in-action; "
        f"ghostly C6; re-litigation of closed N1 bilkinetic as CDM.\n"
        f"Only allow a path if V+C+A could survive. Prefer fail-closed.\n\n"
        f"## Deliverable\n"
        f"`Working/planck538_loop/rounds/R{rnd:02d}/Jammer_VERDICT.md`\n"
        f"Also optional handoff under Handoffs/.\n\n"
        f"Sign as **Cursor Jammer**. Do not read Scratch's round file.\n"
    )
    (round_dir / "BRIEF_Scratch.md").write_text(scratch, encoding="utf-8")
    (round_dir / "BRIEF_Jammer.md").write_text(jammer, encoding="utf-8")
    (round_dir / "META.json").write_text(
        json.dumps(
            {"round": rnd, "paths": state["active_path_ids"], "seeded_utc": utc_now()},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    # inbox pointers
    inbox = ROOT.parent.parent / "Workflow" / ".cursor_autonomous_agent_inbox"
    if inbox.is_dir():
        (inbox / "pc_scratch.md").write_text(
            f"CR-P538 Scratch: execute `Working/planck538_loop/rounds/R{rnd:02d}/BRIEF_Scratch.md` now. Blind. File Scratch_VERDICT.md in that round folder.\n",
            encoding="utf-8",
        )
        (inbox / "ac_jammer.md").write_text(
            f"CR-P538 Jammer: execute `Working/planck538_loop/rounds/R{rnd:02d}/BRIEF_Jammer.md` now. Blind. File Jammer_VERDICT.md in that round folder.\n",
            encoding="utf-8",
        )

    save_state(state)
    write_board(state)
    print(f"Seeded round R{rnd:02d} paths={state['active_path_ids']}")
    return state


def _gate_from_text(text: str, gate: str) -> str:
    """Heuristic extract PASS/FAIL for gate letter."""
    patterns = [
        rf"\b{gate}\s*[=:]\s*(PASS|FAIL|OPEN|UNKNOWN)",
        rf"\bGate\s*{gate}\b[^\n]*(PASS|FAIL)",
        rf"\b{gate}\b[^\n]{{0,40}}\b(PASS|FAIL)\b",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            return m.group(1).upper() if m.lastgroup is None else m.group(m.lastindex).upper()
    # fallback group
    m = re.search(rf"\b{gate}\b[^\n]*(PASS|FAIL)", text, re.I)
    if m:
        return m.group(1).upper()
    return "UNKNOWN"


def score_round(state: dict, round_no: int | None = None) -> dict:
    rnd = round_no or int(state.get("round") or 0)
    round_dir = ROUNDS / f"R{rnd:02d}"
    scratch_p = round_dir / "Scratch_VERDICT.md"
    jammer_p = round_dir / "Jammer_VERDICT.md"
    if not scratch_p.exists() or not jammer_p.exists():
        print(f"Missing verdicts in {round_dir} (need Scratch_VERDICT.md and Jammer_VERDICT.md)")
        return state

    s_txt = scratch_p.read_text(encoding="utf-8")
    j_txt = jammer_p.read_text(encoding="utf-8")
    combined = s_txt + "\n" + j_txt

    gates = {g: _gate_from_text(combined, g) for g in ("V", "C", "A", "L")}
    # L requires both lanes; if either says FAIL on C, C fails
    if re.search(r"\bC\b[^\n]*(FAIL|fail)", j_txt) or re.search(
        r"character\s+FAIL|BL-3\s+FAIL|not\s+Planck\s+CDM", j_txt, re.I
    ):
        gates["C"] = "FAIL"
    if "FAIL" in (gates["V"], gates["C"], gates["A"]):
        gates["L"] = "FAIL"
    elif gates["V"] == "PASS" and gates["C"] == "PASS" and gates["A"] == "PASS":
        if re.search(r"\bL\s*[=:]\s*PASS|dual-lane\s+agree|converged", combined, re.I):
            gates["L"] = "PASS"

    note = "scored"
    if all(gates[g] == "PASS" for g in ("V", "C", "A", "L")):
        state["converged"] = True
        state["status"] = "CONVERGED"
        note = "CONVERGED"
    else:
        # mark active paths failed unless explicitly kept
        for p in state["path_queue"]:
            if p["id"] in (state.get("active_path_ids") or []):
                if re.search(rf"{p['id']}[^\n]{{0,80}}(PASS|survive|KEEP)", combined, re.I):
                    p["status"] = "keep_open"
                else:
                    p["status"] = "failed"
                    state.setdefault("closed_negative", []).append(
                        {
                            "id": f"R{rnd:02d}_{p['id']}",
                            "reason": f"failed or not sustained in round R{rnd:02d} score",
                        }
                    )
        note = f"gates {gates}"

    state.setdefault("history", []).append(
        {
            "round": rnd,
            "paths": list(state.get("active_path_ids") or []),
            **gates,
            "note": note,
            "scored_utc": utc_now(),
        }
    )
    state["active_path_ids"] = []
    save_state(state)
    write_board(state)
    (round_dir / "SCORE.json").write_text(json.dumps(gates | {"note": note}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"round": rnd, **gates, "note": note}, indent=2))
    return state


def append_path(state: dict, pid: str, title: str, v_hope: str = "", c_risk: str = "") -> dict:
    state["path_queue"].append(
        {
            "id": pid,
            "title": title,
            "status": "pending",
            "v_hope": v_hope or "unspecified",
            "c_risk": c_risk or "unspecified",
        }
    )
    if state.get("status") == "EXHAUSTED":
        state["status"] = "RUNNING"
    save_state(state)
    write_board(state)
    print(f"Appended {pid}")
    return state


def tick(state: dict) -> None:
    """Called on loop wake: score prior round if both filed; else seed; print prompt."""
    if STOP_PATH.exists() or state.get("stop_requested"):
        state["status"] = "STOPPED"
        state["stop_requested"] = True
        save_state(state)
        write_board(state)
        print("STOPPED")
        return

    rnd = int(state.get("round") or 0)
    if rnd > 0:
        round_dir = ROUNDS / f"R{rnd:02d}"
        if (round_dir / "Scratch_VERDICT.md").exists() and (
            round_dir / "Jammer_VERDICT.md"
        ).exists() and not (round_dir / "SCORE.json").exists():
            state = score_round(state, rnd)

    if state.get("converged"):
        print("CONVERGED — loop should halt")
        write_board(state)
        return

    if state.get("status") in ("STOPPED", "EXHAUSTED", "CONVERGED"):
        print(state.get("status"))
        return

    # If no active in-progress, seed next
    if not state.get("active_path_ids") or all(
        p.get("status") != "in_progress" for p in state["path_queue"]
    ):
        # only seed if previous scored or round 0
        if rnd == 0 or (ROUNDS / f"R{rnd:02d}" / "SCORE.json").exists() or not list(
            (ROUNDS / f"R{rnd:02d}").glob("*_VERDICT.md")
        ):
            if rnd == 0 or (ROUNDS / f"R{rnd:02d}" / "SCORE.json").exists():
                state = seed_round(state)

    prompt = (
        "Planck538 loop tick: (1) Read Working/PLANCK538_STATUS_BOARD_Cursor_Main.md and "
        "Working/planck538_loop/state.json. (2) If STOP file exists, halt. "
        "(3) If round briefs exist without verdicts, launch/resume Scratch+Jammer Task clones "
        "on those briefs. (4) If both verdicts exist unscored, run orchestrate.py score. "
        "(5) If scored and not converged, seed-round and launch next clones. "
        "(6) Update board. Continue until CONVERGED or STOP."
    )
    print(f'AGENT_LOOP_TICK_planck538 {json.dumps({"prompt": prompt})}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "cmd",
        choices=["status", "seed-round", "score", "append-path", "request-stop", "tick", "board"],
    )
    ap.add_argument("--round", type=int, default=None)
    ap.add_argument("--id", default=None)
    ap.add_argument("--title", default=None)
    ap.add_argument("--v-hope", default="")
    ap.add_argument("--c-risk", default="")
    args = ap.parse_args()
    state = load_state()

    if args.cmd == "status":
        print(json.dumps({k: state.get(k) for k in ("status", "round", "active_path_ids", "converged", "stop_requested")}, indent=2))
        write_board(state)
    elif args.cmd == "board":
        write_board(state)
        print(f"Wrote {BOARD}")
    elif args.cmd == "seed-round":
        seed_round(state)
    elif args.cmd == "score":
        score_round(state, args.round)
    elif args.cmd == "append-path":
        if not args.id or not args.title:
            raise SystemExit("--id and --title required")
        append_path(state, args.id, args.title, args.v_hope, args.c_risk)
    elif args.cmd == "request-stop":
        STOP_PATH.write_text("stop\n", encoding="utf-8")
        state["stop_requested"] = True
        state["status"] = "STOPPED"
        save_state(state)
        write_board(state)
        print("STOP requested")
    elif args.cmd == "tick":
        tick(state)


if __name__ == "__main__":
    main()
