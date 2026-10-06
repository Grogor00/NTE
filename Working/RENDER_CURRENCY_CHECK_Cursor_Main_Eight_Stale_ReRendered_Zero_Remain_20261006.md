# Whole-set render currency check — Cursor Main

**From:** Cursor Main · **To:** AC, Greg · **Date:** 2026-10-06  
**Mechanical #5.**

---

## Method

Compare `Core_Papers\*.md` LastWriteTimeUtc to `paper-build\pdf-out\*.pdf`. Stale = PDF older than MD.

## Initial state (before re-render)

**8 / 23 stale:**

| File | MD ahead (hours, approx) |
|---|---|
| Part 2 | 148 |
| Part 3 | 75 |
| C5 | 485 |
| C9 | 0.5 |
| C11 | 604 |
| C12 | 191 |
| C14 | 676 |
| C16 | 676 |

## Action

Re-rendered all eight via pandoc pipeline (`prepare_*` + strip + defaults). **All eight PASS.**

## Final state

**0 / 23 stale** among Core Parts + Companions 1–20 present in pdf-out.

---

## Note

Book PDFs / C21 Working draft were **not** in this Core whole-set check. C21 remains a Working paper pending PC/AC deposit path.

— Cursor Main, 2026-10-06.
