# Handoff — AC → Cursor: manifest §4 rebuilt path-first; §6 path rule mandatory; ID note retracted

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** PC, Greg · **Date:** 2026-09-18
**Status:** Greg-directed, mandatory. Root cause of the recurring wrong-tree failures.
**Target:** `NTE_Workflow_Manifest_v10_18.md` (canonical root, `G:\My Drive\NTE_ZENODO_CLEAN\`)

---

## Why

Manifest §4 carries Drive IDs for every child folder. Rev 10.3 retargeted the root line and left the child IDs pointing into the pre-retarget tree. **All seven are wrong**, verified individually this session:

| Folder | §4 currently resolves to |
|---|---|
| `Book\` | the **archive** root's Book folder |
| `Core_Papers\` | the v10_18_0 set |
| `Handoffs\` | not the folder Cursor actually polls |
| `Popular_Editions\`, `Pedagogical_Notes\`, `paper-build\`, `Working\` | all pre-retarget |

Consequence already realised: **PC wrote Appendix C v1.3 (2026-08-03) into the archived Book folder** while following §4 correctly, and it was invisible to every subsequent brief. A half-updated ID list is worse than none — it looks checkable and is not.

Drive IDs live only in an agent's volatile context. Greg cannot see them, Cursor cannot see them, and they do not survive a tree rebuild. **Folder names and paths do.**

---

## Patch MF-1 — §4 replaced (RANGE REPLACE, not byte-exact OLD/NEW)

Replace everything from the line `## 4. Folder structure (lean tree — verified 2026-07-06)` up to but **not including** the line `## 5. The streams`, with the block below.

Flagged explicitly: this is a range replace because the existing §4 is ~30 lines and reconstructing it byte-exact from an escaped read is the very class of error this patch exists to stop. **Report the replaced block back verbatim in your completion handoff** so AC and Greg can verify what was removed.

```
## 4. Folder structure (canonical, path-addressed — rebuilt 2026-09-18)

**Canonical root: `G:\My Drive\NTE_ZENODO_CLEAN\`**

```
NTE_ZENODO_CLEAN\
  Core_Papers\        Parts 1-3 + Companions 01-20
  Popular_Editions\   Full + Reader
  Pedagogical_Notes\  tier-3 notes
  Book\               chapters, Prelude, Appendices A-C, deposit register
  Handoffs\           stream handoffs (Cursor polls this on a 5-min tick)
  Working\            durable stream reasoning / working notes
  paper-build\        render lane
  paper-build\pdf-out\  rendered PDFs (deliverables stay in Drive)
```

**Drive IDs are deliberately NOT recorded in this manifest.** Resolve every folder and file by name/path at the point of use. Never cache an ID across turns or sessions; never write one into a manifest, handoff, or working note; never report a file to Greg by ID.

**Archive.** The pre-2026-08-02 tree is superseded and must not be read from or written to. It is being renamed `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`. Until that rename lands, treat any Book/Core_Papers/Handoffs folder **not** reached by descending from `G:\My Drive\NTE_ZENODO_CLEAN\` as archive, regardless of what any pointer says.

**Scratch staging is NOT in Drive.** `render-all-clean.ps1` uses `%TEMP%\nte-build-scratch` (stripped copies for pandoc only). Do not recreate `paper-build\scratch-src\` or mirror `Core_Papers\` into the synced tree.

**Octonionic standalones** (source, not deposit) live in the folder named `New folder` off the canonical root: the Octonionic-Origin standalone (v0.1/v0.2), the Neutrino-Mixing-Sector paper, and the two-sector-necessity deep-dive. These ground the ℍ⊂𝕆 / J₃(𝕆) claims in Parts 2-3. Rename pending.

This manifest lives at the canonical root.
```

---

## Patch MF-2 — §6, new working discipline 9 (MANDATORY)

```
OLD:
8. **No standalone claims a tier above what the corpus grants the underlying scale.**

NEW:
8. **No standalone claims a tier above what the corpus grants the underlying scale.**
9. **Address everything by name and path — never by Drive ID. NON-NEGOTIABLE.** Folder and file names persist across sessions and are visible to Greg and Cursor; Drive IDs live only in an agent's volatile context and are invisible to both. Resolve an ID from the path at the point of use and discard it. Never cache one across turns or sessions, never record one in this manifest or any handoff or working note, and never report a file to Greg by ID. Where a pointer and the live tree disagree, **stop and flag it to Greg** — do not resolve the conflict silently, in either direction. (Cause of the 2026-08-03 Appendix C v1.3 misfile into the archive tree, and of the AC folder-ID misdirection on 2026-09-18.)
```

---

## Patch MF-3 — §7, tooling line

```
OLD:
- **Search snippets and `search_files` are stale-prone.**

NEW:
- **Resolve by path, not by cached ID.** Enumerate from `G:\My Drive\NTE_ZENODO_CLEAN\` downward every time. An ID that worked last session may now address the archive tree; it will not error, it will silently return the wrong file.
- **Search snippets and `search_files` are stale-prone.**
```

---

## Patch MF-4 — Last updated

```
OLD:
**Last updated.** 2026-09-18 — rev 10.5.

NEW:
**Last updated.** 2026-09-18 — rev 10.6. §4 rebuilt path-first (all seven child IDs resolved into the pre-retarget tree; IDs removed from the manifest entirely). §6 discipline 9 added: address by name/path, never by Drive ID — mandatory. Prior: rev 10.5.
```

*(If the Last updated line has additional text after `rev 10.5.`, retain it after the new text rather than discarding it, and report what was retained.)*

---

## Retraction

`Handoff_AC_to_Cursor_Ch12_Ratified_StaleFiles_MergeNote_Corrections_20260918.md` section C and its Notes block told Cursor that §4's IDs were "pre-rebuild" and to "use the live tree." **That framing is retracted.** It was an unflagged AC inference, correct in outcome for `Core_Papers` and `Handoffs` and stated without verification. Superseded by discipline 9: resolve by path; flag conflicts to Greg rather than resolving them.

---

## Greg — Drive-UI actions (cannot be done from here)

1. **Move** `Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` out of the archive tree's `Book\` into `G:\My Drive\NTE_ZENODO_CLEAN\Book\`. A move, not a copy — a second twin is what caused this.
2. **Rename** the superseded root to `NTE_ZENODO_CLEAN_ARCHIVE_pre-20260802`. Pending since 2026-08-02; it is the action that actually closes this failure mode.

---

— AC, 2026-09-18.
