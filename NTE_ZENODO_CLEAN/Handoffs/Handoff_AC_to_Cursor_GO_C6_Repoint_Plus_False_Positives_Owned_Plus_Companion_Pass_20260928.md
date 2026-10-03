# Handoff — AC → Cursor Main: **GO — C6 §6 κ-closure repoint** (ratified 2026-09-27, never drafted). Plus two AC false positives owned, and the Door B cite drift routed.

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**In response to:** `Handoffs\Handoff_Cursor_Main_to_AC_Outstanding_Work_Register_Tier1_Reports_Tier2_Applied_20260928.md`

---

## 1. **AC's two false positives — owned**

**Item 1 (mojibake) and item 3 (truncation) were both artefacts of AC's decode layer**, not the files. On-disk 𝕆 is healthy UTF-8 (`f0 9d 95 86`); Part 2 ends properly at `…credited).*`. AC called item 1 a **deposit blocker** and placed it first.

**Standing correction, effective now:** anything AC reports about **bytes, encoding, glyph corruption, or file boundaries** is an observation about AC's reader and must be treated as unconfirmed until Cursor checks the file locally. **AC will label such observations as reader-level from here.**

The caveat AC attached to item 1 — *match on the actual on-disk bytes and report what you find* — is why this cost one report cycle instead of a wasted patch. **Keep that pattern on any future AC byte-level claim.**

**Item 2's clean sweep is therefore a real result, not a null:** 0 encoding defects across `Core_Papers\`, `Book\`, `Popular_Editions\`, `Pedagogical_Notes\`. **That is worth having established before deposit**, and it answers the question AC actually cared about — whether the apply chain was silently corrupting Unicode. **It is not.**

---

## 2. **GO — C6 §6 κ-closure repoint. Greg ratified 2026-09-27; AC never issued the blocks.**

**This is AC's gap, not a pipeline failure.** The ratification is in `Handoffs\AC_C6_Repoint_Ratified_Citation_Sweep_Commissioned_Claude_Lanes_On_Existence_Gate_Plus_Pre_t_Scalar_Path_20260927.md` §1, and no byte-exact register followed it.

**Target:** `Core_Papers\Companion_06_BornRule_GaugeBirth_v10_19_0.md` §6.

**Defect:** attributes the κ closure to **Companion 5**. The closure is in **Part 2 §IX** — AC verified this 2026-09-27 while discharging the Door B hold, and the sweep has now confirmed it independently.

**OLD text is from AC's full read of C6 on 2026-09-25 and may have drifted. Match-or-report; do not force.**

```
OLD: closed by CPN-symmetric self-consistency to κ = κ₀/(1 − κ₀) = 5.50 (Companion 5)
NEW: closed by CPN-symmetric self-consistency to κ = κ₀/(1 − κ₀) = 5.50 (Part 2 §IX — a geometric-series resummation over CPN-conjugate traversals, resting on the bilateral two-metric action whose completion Part 3 lists as open)
```

**The register clause is not optional.** A bare repoint fixes the address and leaves κ looking better supported than it is. **κ survives Door B and is demonstrated** (both lanes, N-thickness round) — **but its support rests on an action Part 3 lists as open**, and the citation should carry that.

**If the OLD does not match, report the actual sentence** and AC will redraft rather than have you approximate.

---

## 3. **Door B cite drift in C8 / C12 / C15 / C17 — this is the Companion pass, arriving early**

The sweep reports cite drift in four Companions. **That is tier-4 item 8 surfacing on its own**, and it confirms the exposure AC predicted: the three Parts have had systematic passes; the twenty Companions have not.

**Proceed with the mechanical Companion pass as scoped in the outstanding-work register**, prioritising the four already flagged. For each Companion report only:

1. Does it assert **native (n_s, r)** as NTE predictions?
2. Does it reference **μ(N), F(Φ)R, or the Higgs portal** as live objects?
3. Does it carry **Φ_NTE as a dynamical field** rather than a relabelling of the expansion history?
4. Does it cite a **derivation, closure or formula to a location that does not hold it**?

**Report only. AC arbitrates; Greg ratifies.** Do not patch Companions from this pass.

---

## 4. Acknowledged and closed

- **P1-5/6/7 applied**, Part 1 re-rendered, currency OK. **AC's specific concern is answered:** P1-5 keeps the cosmological inverse-lapse and drops the Schwarzschild/derived-gravity reading, and the adjacent paragraphs now agree. **That was the item AC reserved and it is closed.**
- **C13 M_R fixed.**
- **C12 T_GB — no mandatory patch.** Tier-4 item 7 closed.
- **Part 2 N-3 items held for Greg.** Correct.

---

## 5. Pipeline

`last_poll` still not advancing after the em-dash parse fix. **Flagged as next.** AC notes this is the **fourth** distinct fault in this chain — `promote_skip no_ledger`, `Directive_REISSUE_` no_specs, the QUEUED/CLAIMED clearing bug, and now the parse bug plus a residual. **Each was found and fixed properly; the pattern is that the chain has more failure modes than the work it carries.**

Not AC's lane to fix, and not urgent while hand-carry works — but worth stating plainly before the deposit, since a deposit is exactly when a silent pipeline failure costs most.

---

— AC, 2026-09-28.
