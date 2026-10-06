# URGENT — Cursor Main → Greg / AC: **Manifest zeroed** during C11 apply

**From:** Cursor Main · **To:** Greg (restore), AC · **Date:** 2026-09-30 ~20:50 NZDT
**Severity:** deposit-adjacent infrastructure — **`NTE_Workflow_Manifest_v10_18.md` is 0 bytes.**

---

## What happened

While applying the Companion 11 register and updating Manifest §10, a Python `Path.write_text(..., newline='\\n')` call raised `ValueError: illegal newline value`. **`pathlib` opens the target with mode `'w'` (truncate) before validating `newline`**, so the Manifest was emptied to 0 bytes and the write aborted.

**Verify-then-report:** current disk state is Length=0, LastWriteTime=2026-09-30 20:50:13.

Local Cursor history for this path only goes to **2026-08-09 / 2026-09-18** (~15 KB) — **not** today's post–Door B / discipline-12 Manifest. No non-empty copy found on `G:\`. No git repo.

---

## What Greg should do (preferred)

**Google Drive → right-click `NTE_Workflow_Manifest_v10_18.md` → Manage versions / Version history → restore the last non-empty version immediately before 20:50 NZDT tonight.**

Do **not** let me rebuild from the Aug history — that would erase a month of §10.

---

## C11 register status (separate — applied successfully)

Companion 11 + Part 3 Λ paragraph **were patched before the Manifest wipe** and remain on disk. See sibling apply handoff. **Manifest §10 registration for C11 is NOT written** until Manifest is restored.

---

## Protocol lesson

Never use `Path.write_text` with a custom `newline` on a live corpus file without writing to a temp then `os.replace`. Prefer StrReplace / write-temp-rename for Manifest edits.

— Cursor Main, 2026-09-30.
