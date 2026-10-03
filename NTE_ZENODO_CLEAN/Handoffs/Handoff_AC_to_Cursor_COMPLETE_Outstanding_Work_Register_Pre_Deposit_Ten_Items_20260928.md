# Handoff — AC → Cursor Main: **complete outstanding-work register.** Pre-deposit. Ten items, ordered.

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**Context:** Greg's goal is a **coherent, stable corpus before PC is activated for the Book**, for a **Zenodo deposit** — which records the corpus as it stands. Everything below is what AC knows to be outstanding.
**Nothing here is patched. Items marked GO are ratified; the rest await Greg.**

---

## TIER 1 — Deposit blockers. Do these first.

### 1. **Mojibake in `Core_Papers\NTE_v10_19_0_Part2_Structure.md`** — NOT YET RATIFIED
Register: `Handoffs\AC_Patch_Register_Part2_Mojibake_Deposit_Blocker_Plus_Two_N3_Items_20260928.md`, item 1.

Three corrupted 𝕆 glyphs in §8.5–8.6's S³-grounding parenthetical; surrounding text uses `$\mathbb{O}$` correctly. **Will render as garbage in the PDF, in the paper carrying the gauge-group derivation.**

**AC reads through a decoding layer — match on the actual on-disk bytes and report what you find.**

### 2. **Corpus-wide encoding sweep** — do with item 1
Same apply chain produced other patches. Sweep `Core_Papers\`, `Book\`, `Popular_Editions\`, `Pedagogical_Notes\` for mis-decoded **𝕆 ℍ ℝ ℂ 𝔽**, Greek letters, arrows, and en/em dashes. **The real question is how many other patches introduced raw Unicode that lost its encoding.**

### 3. **Part 2 trailer — possible truncation** — verify, then report
File ends mid-word: *"…mirror-matter and bimetric prior art **credi**"*, no closing parenthesis or punctuation. **AC has seen this on every read since 2026-09-18** and cannot distinguish a real truncation from a read-layer cut at ~18.6 kB. **Check the final bytes locally.** If truncated, restore; if it is the read layer, say so and AC stops flagging it.

---

## TIER 2 — Ratified, awaiting apply

### 4. **§2.1 self-contradiction register — GO ISSUED** ✅
`Handoffs\Handoff_AC_to_Cursor_GO_Apply_Section2p1_Register_Plus_Citation_Sweep_And_C12_Check_20260928.md`
Three items (P1-5, P1-6, P1-7) on Part 1. **Greg ratified 19:23.** Re-render Part 1; report P1-5's final paragraph verbatim.

**Note on P1-5:** do not simply align wording to the sentence above it. β_NTE|Φ|² **is** the inverse lapse of the N-foliation (dt = dN/(β|Φ|²)) — that survives; the **spatial-variation / Schwarzschild** reading is what fails. If the result still looks contradictory after applying, **stop and report**.

---

## TIER 3 — Drafted, awaiting Greg's ratification

### 5. **Part 2 items 2–4** — same register as item 1
- **§XII contradicts §IX on the DM variance.** §XII credits spatial |Φ| variation; §IX credits the central limit theorem. §IX is correct.
- **§XIII's void "specific mechanism"** reduces under Door B — spatially varying |Φ|² *is* spatially varying H, which is Wiltshire/Célérier. **A genuine loss of a distinguishing claim; record it as one.**

---

## TIER 4 — Commissioned, open, not blocking

### 6. **Citation sweep** — commissioned 2026-09-27, **still open**. AC's assessment: **highest-yield mechanical task before deposit.**
Grep every cross-reference in `Core_Papers\` naming a paper as the **home of a derivation, closure or formula** — `(Companion N)`, `Part N §`, "see Companion", "derived in", "closed in", "per Part". **Verify the named location contains it.** Report filename, citing sentence verbatim, claimed location, actual location, match/mismatch.

**Two confirmed misattributions already, both found only by chasing a named development:** Companion 13 ref 4 → Part 3 for an M_R formula Part 3 never carried; Companion 6 §6 → Companion 5 for a closure that lives in Part 2 §IX.

### 7. **Does the T_GB regrade reach Companion 12's fibre modulus?**
T_GB and β_GB·M_Pl = √(2π) are one relation (C12 §3); Part 2 §8.3's T_GB statement is regraded. **Report whether C12 needs a matching change. Do not patch.**

### 8. **The Companions have had NO systematic pass since Door B.**
Parts 1, 2 and 3 have now all had one. **Companions 1–20 have not.** Known or suspected exposure: **C9** (rewritten — AC verified, portal withdrawn), **C12** (item 7), **C17** (audit-trail regrade — check it says so throughout), **C5/C6** (κ-closure citation, item 6), **C8** (N_HH relabel — check applied), **C13** (M_R and item 22.4 repairs — check applied), **C15** (metric-entry result cited by others), **C16** (the source of the §8.5–8.6 material carrying the mojibake).

**AC proposes:** after tiers 1–3, a mechanical pass reporting for each Companion — does it assert native (n_s, r)? does it reference μ(N), F(Φ)R, or the portal as live? does it carry Φ as a dynamical field rather than a relabelling? does it cite a derivation to a location that does not hold it? **Report only; AC arbitrates.**

---

## TIER 5 — AC's own queue, not Cursor's

- **DESI Phase-2 directive** with the five ratified inputs Scratch's pre-stage requested.
- **Part 1 §VII locking criterion** y_eff²/(β|Φ|) ≥ 1 — no lane has recomputed it under Door B; listed open.
- **Register v5** for the Book deposit, once the chapter passes settle.

---

## Standing

**Pipeline note:** the sweep stalled 2026-09-27 19:44 → 2026-09-28 19:13 (1,409 min) and the marker named the fix — launch `auto.ps1` from `G:\My Drive\NTE_ZENODO_CLEAN\Workflow` only. **The alert worked; it just needed someone at the machine.** Confirm the sweep's `last_poll` is advancing before starting tier 1.

**AC will not call the corpus deposit-ready until tiers 1–3 are applied and tier 4 item 8 has reported.** PC's Book activation waits on that.

---

— AC, 2026-09-28.
