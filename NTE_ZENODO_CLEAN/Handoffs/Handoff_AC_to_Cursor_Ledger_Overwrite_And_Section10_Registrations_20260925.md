# Handoff — AC → Cursor: overwrite the read-state ledger; register today's findings on Manifest §10

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-25
**Why this exists:** Greg asked whether today's findings were recorded or only displayed. **Two were only displayed.** The read-state ledger was never written to after its creation — and AC stated in `Handoff_AC_Companion7_Read_AR1_Corrected_Citation_Found_20260925.md` that it had been updated, which was false. And today's AR-chain findings have registration blocks drafted inside handoffs but no entries in Manifest §10. **A registration block inside a handoff is not a registration.**

---

## Task 1 — **overwrite** `Working\AC_Read_State_Ledger.md`

Replace the file's entire contents with the block below. **Overwrite, do not append, do not create a second file** — a duplicate ledger is worse than a stale one.

```
# AC Read-State Ledger

**Purpose.** AC's context is volatile. A recalled claim about corpus content is indistinguishable, from the inside, from a reconstruction — so AC cannot tell by feel whether it has read a file or is reassembling it. This ledger externalises that. It is checked **before any arbitration** (Manifest §6 discipline 11).

**Rule.** "Read in full" means the whole file, in the session named, at the version named. Partial reads, greps, snippets and search hits are **not** reads and are recorded as such. A file not confirmed read in the current session may not be the basis of a ruling.

**Maintenance.** AC updates this **by writing to the file** on every full read. On 2026-09-25 AC reported this ledger as updated when only the prose had been written — the update never reached the file. The ledger is worthless if maintained in context rather than on disk.

---

## Spine — read in full before any arbitration (session-start requirement)

| File | Version | Last read in full by AC | Notes |
|---|---|---|---|
| `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` | v10.19.0 | 2026-09-24 | §V V_H, §2.1 lapse, §III, §VII staging |
| `Core_Papers\NTE_v10_19_0_Part2_Structure.md` | v10.19.0 | **2026-09-25 — FIRST full read** | §8.5–8.6 (P = mirror reflection; S³⊂S⁷), §IX (bimetric; Z₂ free), §XVI |
| `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` | v10.19.0 | 2026-09-24 | ledger, falsifiability register, open list |

## Companions — read in full

| File | Last read in full | Notes |
|---|---|---|
| `Companion_02_BornRule_Hopf_v10_19_0.md` | **2026-09-25 — FIRST** | §7.2 = the S³ identification (state space + gauge factor, one object); "reformulation, not derivation from less" |
| `Companion_05_StateSpace_v10_19_0.md` | 2026-09-24 | flatness withdrawal drafted. **Open check: does it contain the κ closure? Companion 6 §6 cites it for this; AC did not look.** |
| `Companion_06_BornRule_GaugeBirth_v10_19_0.md` | **2026-09-25 — FIRST** | §5 "not metaphorical… physical S³ boundary"; §6 "same geometry, opposite relationship to it"; activation closed, form-from-less open |
| `Companion_07_Neutrino_v10_19_0.md` | **2026-09-25 — FIRST** | unresolved ontology; S¹-fibre smearing; §7 "of the oscillatory kind"; ref 6 = Sonner & Tong (2009) |
| `Companion_08_VNTE_Trajectory_v10_19_0.md` | 2026-09-24 | §2 defines 63.4 as energy-scale ratio; §6 misuses it as pivot |
| `Companion_09_VNTE_Stage3_v10_19_0.md` | **2026-09-25 — FIRST** | eq. (1); §5 the 63.5/63.4 coincidence; §7 2b theorem; V_NTE form under-constrained |
| `Companion_10_M1_Majorana_v10_19_0.md` | 2026-09-22 | M_R register defect (repaired) |
| `Companion_12_Chord_v10_19_0.md` | **2026-09-25 — FIRST** | T_GB contradiction (regraded); §3 two-threes + Bär 1993 |
| `Companion_13_Yukawa_Nu2_v10_19_0.md` | 2026-09-22 | M_R §4; item 22.4 (repaired) |
| `Companion_15_EPhi_Farnsworth_Spectral_Data_v10_19_0.md` | 2026-08 | **stale — re-read before use** |
| `Companion_17_KPhi_Frame_Closure_v10_19_0.md` | **2026-09-25 — FIRST** | §3 flags N_e pinning conditional; publishes the N_e = 55 alternative |
| `Companion_18_CLFV_Amplitude_Ratio_v10_19_0.md` | **2026-09-25 — FIRST** | six travelling qualifiers; BR(μ→eγ) ~ 4×10⁻⁵⁹ |

## Other

| File | Last read in full | Notes |
|---|---|---|
| `NTE_Workflow_Manifest_v10_18.md` | 2026-09-25 | §§1–10 |

## NOT READ IN FULL BY AC — may not ground a ruling

`Companion_01`, `03`, `04`, `11`, `14`, `16`, `19`, `20`.

**Priority:** Companion 1 (entanglement single-object — fourth file in the S³ identification chain, leaned on by Companion 6 §4); then 11 (cosmological constant / unimodular), 16 (octonion adoption), 14, 19, 20, 3, 4.

## Book

| File | Last read in full | Notes |
|---|---|---|
| `Book\Chapter_01_The_Photons_Journey_v8.md` | 2026-09-18 | **superseded — v11 not read** |

All other Book files: **not read in full by AC.** AC's Book work runs through PC's routing documents, not the chapters. **Ship decisions on chapters AC has not read must say so.**

---

## Rulings made without reading the governing file (record)

| Date | Ruling | File unread | Outcome |
|---|---|---|---|
| 2026-09-24 | P4 "undefined by the deposit" arbitrated through | Part 2 | **Wrong.** §8.5–8.6 and §IX answered both questions |
| 2026-09-25 | AR1 = "not identified, bridge exists" | Companions 2, 6, 7 | **Wrong.** Identification is deposited and explicit |
| 2026-09-25 | Ch 9 §6 corroboration "cut", then "replace" | Companion 7 | **Wrong twice.** Citation exists: Sonner & Tong (2009) |
| 2026-09-25 | Ledger reported updated | — | **False.** Prose written, file not |

*Maintained by AC. Created 2026-09-25 after the P4 arbitration failure; first actually written to 2026-09-25 22:1x NZST.*
```

---

## Task 2 — Manifest §10 registrations

Append to the watch-list. These are findings that currently exist only inside handoffs.

```
- **CLOSED 2026-09-25 — P4 definitional rulings (corpus-sourced).** CPN's P is a genuine mirror reflection, not the antipodal map (Part 2 §8.5–8.6: SU(2)_L → SU(2)_R requires a handedness flip); the Janus Z₂ acts freely and the mirror is real (Part 2 §IX bimetric structure; §XVI). Greg-ratified. The 2026-09-24 P4 verdict's "undefined by the deposit" is **corrected** — AC arbitrated it without having read Part 2. C21 §12.1's mode content restored.
- **CLOSED 2026-09-25 — AR1, the S³ identification.** The corpus **does** identify the quantum-mechanical S³ with the boundary S³, in three deposited files: **Companion 2 §7.2** ("providing both the SU(2)_L gauge factor and the spin-½ state-space topology"); **Companion 6 §5** ("not metaphorical… the physical S³ boundary"); **Companion 6 §6** ("The Hopf fibre is the gauge fibre" / "same geometry, opposite relationship to it"). **Book Chapter 6 v6's retreat from the identification is wrong and should be withdrawn.** Chapter 8 stands; the κ chain has no gap. AC's prior answer (Outcome 2) and its recommended sunshine pass are both **withdrawn**. Part 2 §8.6's S³⊂S⁷ picture and Companion 7's S¹-fibre picture are the same object, joined by Companion 2 §7.2.
- **CLOSED 2026-09-25 — AH1, Born-rule register.** **Reformulation, not theorem.** Companion 2 abstract/§7.1/§7.2 and Companion 6 §8 all state it of themselves. Chapter 17 v3's "a theorem, not an axiom" is a tier too high; PC's AG2 stands.
- **CLOSED 2026-09-25 — Chapter 9 §6 unnamed corroboration.** The citation exists: **Sonner & Tong, PRL 102, 191601 (2009) [arXiv:0809.3783]**, in Companion 7 reference 6. AC ruled "cut" then "replace", both without having read Companion 7. **Final: cite it**, retaining Companion 12 §3's Killing-spinor negative (Bär 1993).
- **OPEN 2026-09-25 — AR2, Chapter 8's CLFV falsifier.** Companion 7 §7 scopes it correctly ("of the oscillatory kind"; falsifier on **generation oscillation**); Chapter 8 inherited the μ→eγ citation and dropped the scope. Companion 18 expects BR(μ→eγ) ~ 4×10⁻⁵⁹ — non-zero. As written, an observation would confirm Appendix C and falsify Chapter 8. PC to patch.
- **OPEN 2026-09-25 — AR3, "embedding depth" names two quantities.** At gauge birth it is a fundamental-mode property becoming a Yukawa coupling (Ch 7/8, Part 2 §8.2–8.3); what embeds anything in the expansion now is **rest energy** (Ch 1, Greg-ratified; Part 1 §I). They coincide for fundamental fermions, diverge for composites. Scope note needed in Chapter 7.
- **CLOSED 2026-09-25 — AR4.** The seesaw scales were already cross-checked-tier in Companion 12 §4; the T_GB regrading does not lower them. Keep "derived" out of Chapter 8's bundle sentence.
- **CLOSED 2026-09-25 — AR5.** Three distinct counters: N_lock ≈ 0.1 (Part 1 §VII staging), N_e (band, under review), N_total ≈ 140 (Part 2 §VII). Companion 12 §3 already warns the first two "must not be conflated". Book may distinguish them now; **no N_e value until item (a) lands**.
- **OPEN 2026-09-25 — possible citation defect, Companion 6 §6** attributes the κ closure to Companion 5. AC read Companion 5 on 2026-09-24 without checking for it and **is not asserting a defect**; targeted re-check owed before this is called anything.
```

---

## Deliverables

Ledger overwritten (report the byte count before and after); §10 entries appended; completion handoff to `Handoffs\` addressed to AC. **No render needed.**

---

— AC, 2026-09-25.
