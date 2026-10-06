# Handoff — Claude (chat) → Cursor Main: rename edited files to v10_19_0

**From:** Claude (chat)
**To:** Cursor Main
**Date:** 2026-08-04
**Authorization:** Greg, 2026-08-04 ("Do it").
**MO:** match-or-report, never force. Return a completion handoff listing renames by filename.

## Task
Rename the deposit files that now carry **v10.19 content** but still have **`v10_18_0`** in their filename → **`v10_19_0`**. For each file, rename the `.md` source, the matching `.pdf` in `paper-build/pdf-out/`, and the `paper-build/scratch-src/` copy together, keeping all locations in sync.

## Selection criterion (byte-exact verifiable)
A deposit file qualifies iff its **in-file version/date header reads `v10.19.0`** (the 2026-08-03 Section A edit batch) **while its filename still contains `v10_18_0`**.

Confirmed member:
- `Companion_09_VNTE_Stage3_v10_18_0` — content header reads "2026-08-03 (v10.19.0 draft — eq.(1) sign + saddle addendum)". Rename.

Check each of these from the Section A batch; rename **only if** the file's content shows its v10.19 Section A edit, else report:
- `Companion_08_VNTE_Trajectory_v10_18_0` (§8 frame-identity update)
- `Companion_15_EPhi_Farnsworth_Spectral_Data_v10_18_0` (§6.3 saddle parking)
- the **Part 2 / Structure** master (§XII/§XIII dark-energy corrections)
- the **Part 3 / Accounting** master (prediction register, anchors, θ₁₂ withdrawal, falsifiability rewrite)
- `Paper_OctonionExtension_Pedagogical_Note_v10_18_0` (gauge-group crediting alignment)

Already correctly named — **no action**: Companions 16, 17, 18, 19, 20 (`v10_19_0`).

## Do NOT
- Do not rename files whose content was not touched in the Section A batch (they still legitimately read v10_18_0 until a corpus-wide bump).
- Do not force a rename where the content header doesn't confirm v10.19 — report it instead.

## Note for Greg (version-policy call — not Cursor's)
This renames only the **edited** files, leaving the corpus in a mixed 18/19 state. If you'd rather bump the **entire** deposit set to `v10_19_0` at once (the "one canonical version at a time" convention in the Manifest), say so and I'll extend this instruction to the unedited files.

— Claude (chat), 2026-08-04
