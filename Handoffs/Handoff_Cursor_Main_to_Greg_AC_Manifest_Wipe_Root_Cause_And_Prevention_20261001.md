# Analysis — Manifest wipe 2026-09-30: root cause and recurrence prevention

**From:** Cursor Main · **To:** Greg, AC · **Date:** 2026-10-01
**File lost:** `NTE_Workflow_Manifest_v10_18.md` (zeroed ~20:50 NZDT 2026-09-30; later deleted; restored from Desktop New-folder snapshot 2026-09-26 + catch-up)

---

## 1. What happened (causal chain)

1. **Cursor Main** was applying the C11 register and updating Manifest §10 via an inline Python one-liner.
2. The call was effectively:
   ```python
   Path(...).write_text(t, encoding="utf-8", newline="\\n")
   ```
   The `newline` value was the **two-character string** `\` + `n` (PowerShell / nested quoting double-escaped `\n`), not a real newline.
3. **Python `pathlib.Path.write_text` opens the target with mode `'w'` first** — which **truncates the file to empty** — then validates `newline`. Invalid `newline` raises `ValueError: illegal newline value: \\n` **after** the truncate.
4. **Reproduced 2026-10-01:** a 19-byte file becomes **length 0** on the same call pattern. The exception does not roll back the truncate.
5. Google Drive File Stream then synced the empty file. The live path later became **missing** (delete / restore churn), so recovery needed an external snapshot.

**Not the cause:** Drive corruption, autonomous pollers, or concurrent stream edits. The wipe was a **local truncate-on-failed-write** from agent tooling.

---

## 2. Why recovery was hard

| Layer | Status at wipe |
|--------|----------------|
| Live Drive file | 0 bytes → then absent |
| Cursor local history for this path | Stale (Aug / early Sept only) |
| Desktop `NTE v10_6.zip` / rev6 | May–July — unusable |
| Desktop `New folder\…v10_18.md` | **2026-09-26** — best local base |
| Git | No repo on `NTE_ZENODO_CLEAN` |
| Drive version history | Available to Greg; not used in the restore that landed |

So the fault mode is **high-impact + low local redundancy** for one spine file.

---

## 3. Same failure class as status≠artifact

Discipline 13 (verify-then-report) already names status claims standing in for artifacts. This wipe is the **write-side twin**: an **error return** standing in for “no change,” while the file on disk was already destroyed.

---

## 4. Prevention (adopted / proposed)

### A. Mechanical (adopted this turn)

`Workflow\nte_safe_write.py` — **write to `*.tmp` in the same directory, fsync, then `os.replace`**. Optional `min_bytes` guard refuses to replace a large file with a tiny one. Manifest and other load-bearing corpus files should go through this, never `Path.write_text` / `Set-Content` in place on the live path.

### B. Procedural (Manifest §7 + discipline 13)

- Prefer **StrReplace** / OLD–NEW for Manifest edits.
- If a full rewrite is required: **safe_write only**.
- Never pass `newline=` unless it is the literal `"\n"` / `"\r\n"` / `""` — and even then, prefer safe_write (no need for newline on UTF-8 corpus md).
- After any Manifest edit: read back length + first “Last updated” line (discipline 13).

### C. Redundancy (recommended, Greg optional)

1. **Keep a dated Desktop / offline copy** of the Manifest after major §10 days (the New-folder copy saved this incident).
2. **Init a private git repo** on `NTE_ZENODO_CLEAN` (or Cursor share) so a zeroed file is one `git checkout` away — highest leverage.
3. On wipe: **Drive → Manage versions** before inventing a rebuild.

### D. Do not

- Rebuild Manifest from May/July archives when a Sept snapshot exists.
- Use nested `python -c "... newline='\\n' ..."` from PowerShell for corpus files.

---

## 5. Bottom line

**Root cause:** `pathlib` truncates before argument validation; a quoting bug supplied an illegal `newline`; the Manifest was emptied; Drive synced the empty artifact.

**Prevention:** atomic replace writes + no in-place truncate APIs on corpus files + verify-then-report on length + offline/git redundancy for the Manifest specifically.

— Cursor Main, 2026-10-01.
