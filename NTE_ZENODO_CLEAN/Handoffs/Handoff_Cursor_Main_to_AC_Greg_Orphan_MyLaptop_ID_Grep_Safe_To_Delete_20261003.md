# Handoff — Cursor Main → AC / Greg: orphan My Laptop ID grep — **safe to delete from configs' POV**

**From:** Cursor Main · **To:** AC, Greg · **Date:** 2026-10-03
**IDs checked:** outer `1EtIY3o9nuq1bZ_zCP_rrkY2_7nYd_9LJ` · inner `1zvYfkcbE21PMsLV_3ci-z86TrwsqvDTk`
**Also scanned:** Workflow `*.ps1` / `*.py` / `*.json` / `*.cmd`; live Manifest; Cursor skills-cursor; Claude AppData skills glob.

---

## Grep result — no live config caches either ID

| Location | `1EtIY3o9…` (Computers / My Laptop root) | `1zvYfkcb…` (inner NTE_ZENODO_CLEAN) |
|----------|:--:|:--:|
| `Workflow\` scripts & autonomous JSON | **0** | **0** |
| Live `NTE_Workflow_Manifest_v10_18.md` | **0** | **0** (IDs stripped 2026-09-18 path-first) |
| `~/.cursor/skills-cursor` | **0** | **0** |
| Claude Roaming skills glob | **0** | **0** |

**Cursor lanes write by path** (`G:\My Drive\NTE_ZENODO_CLEAN\…`). Deleting the Computers orphan will **not** break Cursor poll/drain/apply scripts. Worst case for a Drive-connector agent still holding a stale ID: **visible error** instead of silent wrong-target write — which is the desired failure mode.

## Historical mentions only (not executable)

`1zvYfkcb…` appears in **old handoffs / notes** as the *superseded* pre-2026-08-03 root, e.g.:
- `Handoffs\Handoff_Cursor_to_AC_Manifest_PathFirst_Rebuild_Complete_20260918.md` (documents removal)
- `Handoffs\Handoff_Claude_to_Cursor_AC_Edit_Manifest_Session_Results_20260803.md` (archive instruction)
- A few `Working\` notes naming the old root as superseded

These are audit text, not write targets. **Do not treat as live pointers.**

`1EtIY3o9…` — **no hits** anywhere in the corpus tree.

## Folder inventory — Cursor cannot scroll Computers

`G:\My Drive\Computers` is **not mounted** on this machine. The July-dated `Computers → My Laptop → NTE_ZENODO_CLEAN` tree is Drive-UI only. **Greg still owes the open-and-look-around check** before Remove → Bin.

## Recommendation

1. Greg: open the orphan, scroll subfolders for anything that looks like real handoffs/verdicts/patches not already in `G:\My Drive\NTE_ZENODO_CLEAN`.
2. If only stubs / 0-byte Manifest / Google Docs ghosts → **Remove → Bin** (30-day recover).
3. Config side: **clear to delete** — no Cursor script holds either ID.

— Cursor Main, 2026-10-03.
