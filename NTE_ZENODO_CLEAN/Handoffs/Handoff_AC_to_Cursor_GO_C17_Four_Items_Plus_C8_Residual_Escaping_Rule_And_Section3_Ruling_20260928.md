# Handoff — AC → Cursor Main: **GO — C8 residual + C17 Items 1–4.** Plus two rulings: escaping normalisation, and §3's calculation lines stay.

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**Greg ratified the register as drafted.** **GO on all six.**
**Apply from:** `Handoffs\AC_Patch_Register_Companion17_Body_Lags_Banner_Four_Items_Plus_C8_Residual_20260928.md`
**Targets:** `Core_Papers\Companion_08_VNTE_Trajectory_v10_19_0.md` (banner residual); `Core_Papers\Companion_17_KPhi_Frame_Closure_v10_19_0.md` (Items 1–4).

---

## 1. **Escaping — AC's defect, and a standing rule**

**AC's NEW blocks carry read-layer escaping** (`$N\_e$`, `\\lesssim`, `\\mathrm`) that is an artefact of how AC reads the file, not the file's own convention. **The OLDs matched because you normalised them; the NEWs would have written escaped text into the source.**

**Authority granted: normalise AC's NEW blocks to each file's existing conventions before writing** — match the surrounding LaTeX and markdown style, unescape what the file does not escape. **Report any block where normalisation changes more than escaping**, i.e. where meaning could shift.

**Standing rule, extending the byte/encoding one already in force:**
> **Anything AC transcribes back into a patch carries AC's reader's escaping.** AC's NEW blocks specify **content**; Cursor owns **encoding and escaping**. Where they disagree, the file's convention wins.

**This is the second instance of the same root** — AC treating its reader's rendering as the file. The first was the mojibake false positive. **Both were caught by Cursor checking the disk.**

## 2. **Ruling — §3's calculation lines STAY as written**

You flagged that §3's body still carries live `N_e = 63.4` and `N_e = 55` in the calculation lines, outside the four items.

**AC rules: leave them.** Three reasons:

1. **Item 2 re-heads the whole section** as *"The pre–Door B (n_s, r) calculation — WITHDRAWN, retained as audit trail."* Every line under it is thereby marked historical.
2. **Item 3 explains the error in place** — that 63.4 is N_HH, not a pivot depth, and that identifying the two is the category error that produced the numbers.
3. **The calculation lines record what was computed.** Altering the symbol there would change the record of the mistake, not correct it. **The audit trail's value is that it shows the error as made.**

**This is the same ruling AC applied to C17 §1–§2 (the frame-transform mathematics), and to C15 §6.1/§6.3/§4.** Consistent treatment: **banner and framing are corrected; the historical computation is preserved intact.**

**If a future reader quotes 63.4 from those lines, the section heading and flag 2 are what stop them.** That is the repair working, not a gap in it.

## 3. Apply, render, report

Six patches. Byte-exact match-or-report on OLDs; **normalise NEWs per §1.** Re-render **C8 and C17** to `paper-build\pdf-out\`; confirm currency.

**Report:** per-patch match result, any block where normalisation altered more than escaping, and **C17 §3's heading and flag 2 verbatim after applying** — those two carry the whole audit-trail framing and AC wants to see them land.

---

## 4. After this — three Companions left

| Target | AC read state | Note |
|---|---|---|
| **C12** | read 2026-09-25 | fibre modulus → C9 §6 should be §4; constrained-system residue |
| **C16** | **not read** | source of Part 2 §8.5–8.6 material; B2 forbid locus |
| **C14** | **never read** | open-conditional spectrum diction |

**AC reads each before drafting.** As with C17, **your flagged-sentence reports shorten the read without replacing it** — they have twice now surfaced loci AC's own read would have reached more slowly, and once (C15 §5, C8 token count) caught something AC had wrong.

**Then:** the Part 2 N-3 items (§XII DM-variance attribution, §XIII void mechanism) — **still awaiting Greg** — and the Part 1 §VII locking criterion, which no lane has recomputed under Door B.

---

— AC, 2026-09-28.
