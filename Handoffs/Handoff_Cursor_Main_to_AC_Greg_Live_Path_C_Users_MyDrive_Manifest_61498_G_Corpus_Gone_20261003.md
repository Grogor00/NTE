# Handoff — Cursor Main → AC / Greg: **live path is C:\Users\gregw\My Drive\…**

**From:** Cursor Main · **To:** AC, Greg · **Date:** 2026-10-03
**Lanes:** still OFF (not restarted).

---

## Live path report

| Check | Result |
|--------|--------|
| `G:\My Drive\NTE_ZENODO_CLEAN` | **MISSING** |
| `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN` | **EXISTS** (corpus tree present) |
| Drive `G:\` itself | Still present, but corpus folder not under it |
| Manifest at C: path | **61 498 bytes** — matches AC target |
| Manifest SHA256 | `EADC1BD8D416A9D0C9C10CA13E004E6885711A2AB745098892A9E3D2FC14A60C` |
| Manifest readable | Yes — RESTORED banner / disciplines 12–13 intact |

**Canonical root for all Cursor work now:**

`C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\`

## Implication

Every Workflow script and patch that hardcodes `G:\My Drive\NTE_ZENODO_CLEAN` will fail or write nowhere useful until retargeted to `C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN`.

**Not done this turn (await Greg GO):** path rewrite in `Workflow\`, Manifest §4 if it still mentions G:, agent workspace root move, then `auto on all`.

— Cursor Main, 2026-10-03.
