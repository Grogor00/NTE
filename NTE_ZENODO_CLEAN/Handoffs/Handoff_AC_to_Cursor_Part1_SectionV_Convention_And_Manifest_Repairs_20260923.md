# Handoff — AC → Cursor: Part 1 §V volume convention (ratified) + manifest repairs

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-23
**Basis:** `Handoff_Jammer_to_AC_S1_Lambda_RH_Verdict_Complete_20260923.md`; `Handoff_Jammer_to_AC_S3_GATE4C_Verdict_And_Part1_V_Ratification_20260923.md` (Greg ratified remedy (a), 21:49 NZST).
Byte-exact match-or-report.

---

## P1V — `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` §V

Part 1 §V states the trigger as n_γV_H = 1 **without defining V_H**, and inherits from v10.5.9 a "verifies N_γ = 1.00000000" claim that is false under the 4π/3 reading (it gives 4.19 photons). Greg ratified **remedy (a)**: define V_H ≡ R_H³ explicitly, the convention the T_reset formula has always used. **All numbers unchanged.**

```
OLD:
($n_\gamma V_H = 1$)

NEW:
($n_\gamma V_H = 1$, with $V_H \equiv R_H^3 = (c/H_{\mathrm{dS}})^3$ — one photon per Hubble cube; the $\mathcal{O}(1)$ geometric factor is a convention of the order-of-magnitude trigger)
```

If §V also carries an "N_γ = 1.00000000" or "verifies" line, **report it verbatim, do not patch it** — AC will author that separately. Re-render Part 1; confirm PDF newer than `.md`.

---

## MF-1 — manifest §6: discipline 10 may be missing

Jammer reports §6 carries only disciplines 1–9, while AC handoffs cite "discipline 10" (a draft that is not registered does not exist). Discipline 10 was drafted in `Handoff_AC_to_PC_AppendixC_v13_Retarget_And_Query_Resolutions_20260918.md` §6 and may never have been applied.

**Check first.** If discipline 10 is present, report and skip. If absent, apply:

```
OLD:
9. **Address everything by name and path — never by Drive ID. NON-NEGOTIABLE.**

NEW:
9. **Address everything by name and path — never by Drive ID. NON-NEGOTIABLE.**
10. **A draft that is not registered does not exist.** Any stream delivering a draft — PC chapters and appendices, Scratch and Jammer verdicts included — registers it in §10 as part of its own delivery, with filename, date and status. Registration is the deliverer's job, not something AC is expected to notice. Two 2026 failures trace to this: Chapter 12 v4.1 (drafted 2026-07-04, unratified until 2026-09-18) and Appendix C v1.3 (drafted 2026-08-04, invisible to the Book bring-up brief written to find it).
```

*(Discipline 9's line continues past the text shown; insert after the whole of item 9.)*

---

## MF-2 — manifest §7: a false capability statement

Jammer reports §7 still says Claude cannot edit, delete or rename corpus files. **That is wrong and has been for months** — Claude effects all three by authoring Cursor patch instructions, which is the route this entire session has used. Leaving it invites a future session to tell Greg something untrue.

Locate the sentence and replace its claim with:

```
- **Claude can edit, delete, rename and move corpus files** — by authoring a Cursor instruction (OLD/NEW patch blocks or an explicit directive), which Cursor executes on the local synced tree and which propagates to Drive. Drive-connector create/copy is the direct-write path; Cursor is the path for in-place edits, deletes, renames and moves. A failed retrieval is stale search or duplicate-name churn — diagnose and route around it; never report it as missing capability.
```

Report the OLD sentence verbatim before replacing, so the change is on the record.

---

## MF-3 — manifest §10 registrations

```
- **CLOSED 2026-09-23 — S1 (λ/R_H 0.625 vs 3.92).** Not a contradiction: ħ vs h on the same relation, differing by exactly 2π (0.6245 and 3.9240). Neither is a typical photon wavelength (Wien peak 0.79 R_H); the honest statement is λ ∼ R_H, which canonical Part 1 already gives. No archive sweep needed. Verdict: `Working\S1_VERDICT_lambda_RH_0p625_vs_3p92_SAME_RELATION_hbar_vs_h_BOTH_on_R3_not_4pi3_Jammer_20260923.md`. C21 §5 unblocked.
- **CLOSED 2026-09-23 — Part 1 §V trigger-volume convention.** Greg ratified remedy (a): V_H ≡ R_H³ stated explicitly; all numbers unchanged. The alternative (4π/3, moving T_reset to 1.38 × 10⁻²⁹ K and N_total by 0.48 e-folds) was declined.
- **DELIVERED 2026-09-23 — S3 (GATE4C vs the August idempotent correction).** Jammer verdict + Scratch complex-Majorana confirmation, both filed in `Working\`. Outcome: both prior positions made the same category error in opposite directions; the fork is one free breaking ratio t in the μ–τ-odd term (t = 0 → TM1, t = 3/2 → TM2, t unfixed by J₃(𝕆)). GATE4C's "TM1 not delivered" survives; its "no generation-1 mechanism" and "TM2 = genuine prediction 0.341" are withdrawn. The August "traceless(E₁) = TM1 column" is withdrawn — **it appears in no deposited file, so no corpus patch is required.** AC arbitration: `Handoff_AC_to_PC_Scratch_Jammer_S3_Arbitration_20260923.md`.
```

---

## Deliverables

Patches applied, match report, the §V "verifies" line reported if present, Part 1 re-rendered, completion handoff to `Handoffs\` addressed to AC.

---

— AC, 2026-09-23.
