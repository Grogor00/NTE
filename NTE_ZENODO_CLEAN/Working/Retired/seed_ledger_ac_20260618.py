#!/usr/bin/env python3
"""Rewrite cursor_task_ledger.json with UTF-8 and seed AC 2026-06-18 P1 tasks."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
LEDGER = ROOT / "Working" / "cursor_task_ledger.json"

ledger = {
    "version": 2,
    "updated_at": datetime.now(timezone.utc).astimezone().isoformat(),
    "rules": {
        "seen_is_not_done": True,
        "verified_requires_gate_pass": True,
        "max_strikes_before_blocked": 3,
        "handoff_to_ledger_required": True,
    },
    "tasks": [
        # --- grep infra (done) ---
        {"id": "GREP-SPEC-IMPLEMENT", "state": "VERIFIED", "priority": 1, "stream": "main", "gate": "all",
         "title": "AC grep-gate verifier strings", "verified_at": "2026-06-17T19:45:00+12:00"},
        # --- K(Φ) deposit gate (content ratified; publish held on mojibake) ---
        {"id": "KPHI-S2-1.2", "state": "VERIFIED", "priority": 10, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§1.2",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-S2-6.3", "state": "VERIFIED", "priority": 11, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§6.3",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-S2-10.1", "state": "VERIFIED", "priority": 12, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§10.1",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-S2-10.2", "state": "VERIFIED", "priority": 13, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§10.2",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-S2-11.1", "state": "VERIFIED", "priority": 14, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§11.1",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-S2-12.2", "state": "VERIFIED", "priority": 15, "stream": "main", "gate": "kphi",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§12.2",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-P3-22.14b", "state": "VERIFIED", "priority": 16, "stream": "main", "gate": "kphi",
         "file": "Papers/NTE_v10_17_Part3_Accounting.md", "section": "§22.14(b)",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-P3-22.22", "state": "VERIFIED", "priority": 17, "stream": "main", "gate": "kphi",
         "file": "Papers/NTE_v10_17_Part3_Accounting.md", "section": "§22.22",
         "split_file": "Working/AC_Readable_Splits/NTE_v10_17_Part3_Accounting__C_S22_App.md",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KAPPA-S2-4.4", "state": "VERIFIED", "priority": 18, "stream": "main", "gate": "kappa",
         "file": "Papers/Paper_S2_v1_0_Consolidation_20260525.md", "section": "§4.4",
         "verified_at": "2026-06-17T19:45:00+12:00"},
        {"id": "KPHI-DEPOSIT-GATE", "state": "VERIFIED", "priority": 19, "stream": "main", "gate": "kphi",
         "title": "K(Φ) content sync + PDFs (publish held on mojibake per AC 2026-06-18)",
         "handoff": "Handoffs/Handoff_Cursor_Main_to_AC_KPhi_Sync_VERIFIED_20260617.md",
         "verified_at": "2026-06-17T19:50:00+12:00"},
        # --- AC 2026-06-18 P1/P2 (hand-carried; supersedes CPN until VERIFIED) ---
        {"id": "MOJIBAKE-GATE-FIX", "state": "QUEUED", "priority": 5, "stream": "main", "gate": "mojibake",
         "title": "Extend mojibake gate: astral-plane 𝕆/𝒦 + BMP double-encode; prove FAIL pre-repair",
         "source_handoff": "Handoffs/AC_SIGHT_KPhi_Sync_RATIFIED_Both_Carriers_PublishBlock_Cleared_HELD_on_Mojibake_FalseGreen_Astral_Plane_Plus_EtaGate_Precision_20260618.md",
         "file": "Working/cursor_grep_gates.py"},
        {"id": "MOJIBAKE-REPAIR", "state": "QUEUED", "priority": 6, "stream": "main", "gate": "mojibake",
         "title": "Silent font-repair: restore 𝕆 U+1D546 + 𝒦 U+1D4A6; S2+Part3 monolith+split; rebuild PDFs; fix .ps1 UTF-8 writers",
         "depends_on": ["MOJIBAKE-GATE-FIX"],
         "source_handoff": "Handoffs/AC_ADDENDUM_Greg_Dispositions_C10_Correct_Not_Archive_Mojibake_Silent_FontRepair_No_Changelog_20260618.md",
         "carriers": ["Papers/Paper_S2_v1_0_Consolidation_20260525.md", "Papers/NTE_v10_17_Part3_Accounting.md",
                      "Working/AC_Readable_Splits/NTE_v10_17_Part3_Accounting__C_S22_App.md"]},
        {"id": "ETA-GATE-PRECISION", "state": "QUEUED", "priority": 7, "stream": "main", "gate": "eta",
         "title": "Eta gate negation carve-out (not zero-parameter / structural consistency lines)",
         "source_handoff": "Handoffs/AC_SIGHT_KPhi_Sync_RATIFIED_Both_Carriers_PublishBlock_Cleared_HELD_on_Mojibake_FalseGreen_Astral_Plane_Plus_EtaGate_Precision_20260618.md",
         "file": "Working/cursor_grep_gates.py"},
        {"id": "C10-CORRECT", "state": "QUEUED", "priority": 8, "stream": "main", "gate": "eta",
         "title": "Correct stale C10 finalisation pass η zero-parameter lines (Greg: correct not archive)",
         "source_handoff": "Handoffs/AC_ADDENDUM_Greg_Dispositions_C10_Correct_Not_Archive_Mojibake_Silent_FontRepair_No_Changelog_20260618.md",
         "file": "Papers/Companion_10_v10_8_to_v10_17_2_Finalisation_Pass_20260524.md",
         "lines": ["L133", "L136", "L203"]},
        # --- CPN + housekeeping (after P1/P2) ---
        {"id": "CPN-T1", "state": "VERIFIED", "priority": 30, "stream": "main", "gate": None,
         "title": "CPN symbolic parity check",
         "file": "Working/CPN_Universe_Pair_T1_Symbolic_Parity_Cursor_20260617.md",
         "verified_at": "2026-06-17T19:30:00+12:00"},
        {"id": "CPN-T2", "state": "QUEUED", "priority": 31, "stream": "main", "gate": None,
         "title": "CPN toy junction model", "blocked_by": ["MOJIBAKE-REPAIR"]},
        {"id": "CPN-T3", "state": "QUEUED", "priority": 32, "stream": "main", "gate": None,
         "title": "CPN literature rabbit-hole"},
        {"id": "HOUSEKEEPING-DRYRUN", "state": "QUEUED", "priority": 50, "stream": "main", "gate": "housekeeping",
         "title": "Housekeeping dry-run manifest (no moves)",
         "source_handoff": "Handoff_AC_to_Cursor_Main_Housekeeping_Cleanup_ArchiveFirst_IndexAnchored_DryRunThenACGate_20260616.md"},
    ],
}

LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {LEDGER} tasks={len(ledger['tasks'])}")
