# Handoff — Cursor Main → AC: Scratch references triage APPLIED (potential/ → References/)

**From:** Cursor Main · **To:** AC · **Cc:** Greg, Scratch · **Date:** 2026-07-05
**Re:** `potential/References_Triage_Manifest_potential_20260705.md` + `References_Triage_potential_20260705.csv` (Scratch 2026-07-05). Greg requested execution of Scratch's moves and deletes.

Executed locally against `NTE_ZENODO_CLEAN/potential/` → `References/`. Machine report: `Working/references_triage_apply_report_20260705.json`.

---

## Summary

| Action | Count | Notes |
|---|---|---|
| **Moved → References/** | **55** | All `REF` rows without `dup` flag (59 REF − 4 duplicates = 55 unique keeps) |
| **Deleted** | **39** | 35 `DEL` + 4 `DUP` (duplicates deleted regardless of REF disposition) |
| **Left in potential/** | **36** | All `REV` (borderline — awaiting Greg's call per manifest §C) |
| **Missing / errors** | **0** | Every CSV row resolved on disk |

**Post-state:**
- `potential/`: **36 PDFs** (REV hold) + triage manifest CSV/MD (2 files)
- `References/`: **60 PDFs** (55 moved this session + 5 pre-existing in folder)

---

## Duplicates deleted (kept the canonical copy)

| Deleted duplicate | Kept original |
|---|---|
| `Relational dynamics and Page-Wootters formalism.pdf` | `Page–Wootters formalism.pdf` (#2) |
| `The standard model, the Pati-Salam model, and Jordan geometry.pdf` | `the Pati-Salam model.pdf` (#89) |
| `Spectral Geometry with Exceptional Symmetry and Charged Higgs Fields.pdf` | `Spectral Geometry with Exceptional.pdf` (#13) |
| `Bubbles.pdf` | `Bubbles2.pdf` (#111) |

---

## REV hold (36 files remain in `potential/`)

Per Scratch manifest §C — borderline items **not** moved or deleted. Greg decides keep vs delete using each item's lean. Full list in `Working/references_triage_apply_report_20260705.json` → `left` array.

Notable lean-keep REV items Scratch flagged: Sonner–Tong BPS monopoles, Brain–Landi quantum Hopf fibration, Skenderis–van Rees gauge/gravity, simons-proposal, Non-Signalling Bell theorem, Cravo–Nastase 4d holo-cosmo, and others.

---

## Not executed (out of scope)

- **Drive writes** — local filesystem only (Scratch noted Drive down).
- **§E missing sources** — Page–Wootters 1983 original, Singh, Günaydin–Gürsey, Furey, RT 2006, CFL 2024×2, etc. — still to source separately.
- **§F deep evaluations** — Boyle–Finn–Turok CPT universe, Grady phase-boundary, etc. — not triaged here.

---

## Script

`Working/apply_references_triage.py` — idempotent-safe for re-run only on remaining REV rows if Greg later reclassifies them in an updated CSV.

— Cursor Main, 2026-07-05.
