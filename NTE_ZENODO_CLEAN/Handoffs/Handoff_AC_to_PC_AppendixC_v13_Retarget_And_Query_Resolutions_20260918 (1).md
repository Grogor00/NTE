# Handoff — AC → PC (+ Cursor, Greg): Appendix C retarget to v1.3, and resolutions to PC's queries

**From:** AC (Claude) · **To:** Claude_PC · **Cc:** Cursor Main, Greg · **Date:** 2026-09-18
**Status:** Correction + resolutions. One item remains open and is Greg's, flagged at the end.
**Supersedes:** the Appendix C row in AC Part B of `Handoff_AC_to_PC_Book_BringUp_Corpus_Delta_20260705_to_20260918.md`, and the Appendix C line the Cursor merge note inherited from it.

---

## 0. Correction — Appendix C base is v1.3, and it is now in the canonical tree

PC is right. AC's Part B table targeted **v1.2**, and the merge note inherited that error.

**Cause, now fully diagnosed.** Two Drive folders are named `NTE_ZENODO_CLEAN`. The canonical one is `G:\My Drive\NTE_ZENODO_CLEAN\`. The second sits inside a Drive folder named `My Laptop` — a backed-up-computer folder that appears only under "Computers" in Drive web and **never** in G:. PC's 2026-08-04 pass was saved to the laptop-local path and rode up into that backup, so it was invisible from G: and from every brief written against G:.

**Resolved 2026-09-18.** `Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` is now in `G:\My Drive\NTE_ZENODO_CLEAN\Book\`, alongside v1.2. **Write against v1.3.**

**Cleanup for Greg:** a duplicate of v1.3 remains in the `My Laptop` tree's `Book`. Harmless now, but worth deleting so a future session doesn't find two and have to adjudicate.

**Note for everyone, including AC:** a freshly-synced file can be missing from title search and from metadata on an older copy while being present in the folder. Enumerate the folder; do not conclude absence from a title search. (Manifest §7 already says this. AC did not follow it and told Greg to go move a file that was already in place.)

---

## 1. Dual anchors on n_s — **PC is correct, add them**

v1.3 gives n_s = 0.9692 with no observational comparison. Part 3 requires both anchors shown side by side **so the two-anchor tension is visible**:

- Planck 2018: n_s = 0.9649 ± 0.0042 → **+1.0σ**
- P-ACT-LB: n_s = 0.9743 ± 0.0034 → **−1.5σ**

Carry r = 0.0053 with the CMB-S4 / LiteBIRD sensitivity window (σ(r) ~ 0.001–0.003), and keep the N_e alternative already in v1.3 (N_e = 55 → (0.9646, 0.0070)).

PC's diagnosis is exactly right: **a conditional number with no anchor reads as a result.** This is the one place v1.3 sits softer than canon.

---

## 2. CFL absent from C.4 — **add**

Ciambelli–Freidel–Leigh shipped 2026-07-06, the day after the Book freeze, which is the whole reason it is missing. C.4 "unexpected neighbourhoods" is the right home. Content, from Part 1 Positioning:

- Null-hypersurface quantisation programme (*Null Raychaudhuri: canonical structure and the dressing time*, 2024; *Quantum null geometry and gravity*, 2024).
- Closest external relative **on the emergent-time axis specifically**; time emerges as a quantum (central-charge) effect, area form treated as a discrete operator.
- **Convergence, not confirmation.** It operates on an *already-Lorentzian* null hypersurface and yields a preferred clock and vacuum — a resolution of the clock-ambiguity form of the problem of time — **downstream of N_lock**, whereas NTE concerns the birth of the time dimension at the Euclidean→Lorentzian signature change. **Stacked layers, not competitors.**

Optional and PC's call: the CFL discrete area operator is registered in manifest §10 as a candidate-tier working item against the open RT-1/4 coefficient. Registered, not actioned, **no tier promotion** — mention only if C.4 can carry it without implying progress.

---

## 3. CLFV amplitude ratio (tan²θ₂₃) — **VERIFIED, keep**

Checked directly against `NTE_v10_19_0_Part3_Accounting.md`, falsifiability register item 6. It is canonical:

> CLFV (**conditional**). If charged-lepton flavour violation is ever observed, the amplitude ratio |A(μ→eγ)|²/|A(τ→eγ)|² = tan²θ₂₃ is testable (Companion 18; **unobservable at the framework's heavy scale**).

Two conditions on carrying it in Appendix C: register is **conditional**, and the "unobservable at the framework's heavy scale" caveat must travel with it. Without that caveat the entry reads stronger than canon.

---

## 4. M_R = 8.2 × 10¹⁴ GeV — **does not verify; trace or drop**

Checked against Parts 1–3. The figure appears in none of them.

- Part 3, cross-checks: "**M_R (pathway identified, not derived)**" — no number.
- Part 3, open list: "the derivation of M_R" — still owed.
- Part 2 §X: M_R appears only inside m_ν₂ = (8π)^(−2/3) v_EW²/M_R. The heavy scale Part 2 does quote is **M₁ ≈ 5.4 × 10⁹ GeV**, a different quantity — do not conflate them.

**Resolution path.** The figure most plausibly originates in `Companion_07_Neutrino_v10_19_0.md` or `Companion_13_Yukawa_Nu2_v10_19_0.md`, since the two-branch solar-mass relation is where M_R is used. Before Appendix C ships:

1. Trace it. If a companion carries it at **cross-check** register, Appendix C may carry it **at that register, citing the companion**, and not above.
2. If it cannot be traced to a companion, **it comes out.** Default is removal, not retention pending investigation.

Discipline §8: no standalone claims a tier above what the corpus grants the underlying scale. A bare figure in the Open Ledger with no canonical backing is precisely the thing the Ledger exists to prevent.

---

## 5. Prelude — **reclassified High, accepted**

AC graded it "Check" from the title; PC read the file. PC's grading stands and AC's is withdrawn.

Accepted with it: the Prelude runs the framing five times in seven kilobytes, and the pivot line *From the photon's perspective, no time passed at all* is the book's entry point rather than a phrase to swap. Also accepted: **"The bridge is real; the traversal is not"** is already the corrected position in PC voice, sitting one line after the framing that now misstates the corpus, and is the natural load-bearing replacement.

Sequencing unchanged: **Ch 1, then Prelude, then Ch 4.**

---

## 6. Registration discipline — **AC agrees; Greg has ratified**

PC's diagnosis is right and today produced two independent proofs: Ch 12 v4.1 sat from 2026-07-04 until ratified today, and Appendix C v1.3 was invisible to a brief written specifically to find it. Both were **registration failures, not competence failures**.

Manifest patch below, addressed to Cursor.

**ORDERING:** apply **after** `Handoff_AC_to_Cursor_Manifest_PathFirst_Rebuild_MANDATORY_20260918.md`, whose MF-2 creates discipline 9. If discipline 9 is not present, **stop and report** rather than applying.

```
OLD:
9. **Address everything by name and path — never by Drive ID. NON-NEGOTIABLE.**

NEW:
9. **Address everything by name and path — never by Drive ID. NON-NEGOTIABLE.**
10. **A draft that is not registered does not exist.** Any stream delivering a draft — PC chapters and appendices included — registers it in §10 as part of its own delivery, with filename, date, and status (drafted / awaiting ratification / ratified). Registration is the deliverer's job, not something AC is expected to notice. Two 2026 failures trace to this: Chapter 12 v4.1 (drafted 2026-07-04, unratified until 2026-09-18) and Appendix C v1.3 (drafted 2026-08-04, invisible to the Book bring-up brief written to find it).
```

*(Discipline 9's line continues past the text shown; match the OLD on the bolded heading text and insert the new item after the whole of item 9.)*

---

## 7. OPEN — Greg's decision, PC is blocked on it

The book's seed observation is currently *a photon experiences no time*. That phrasing is load-bearing for the Prelude, for Ch 1, and arguably for the title's logic — and it is the **specific formulation Part 1 §I now names as mis-stated**.

**AC's recommendation**, for Greg to accept or reject:

- **Recast — yes.** Leaving it means the book's first sentence contradicts the corpus's first section.
- **But not to "nothing along the photon's path is metrically marked."** True, and cold; an opening line must land before it can be unpacked.
- **Use PC's own sentence as the seed: "The bridge is real; the traversal is not."** It is already in the Prelude, already in voice, and survives §I intact. Let the no-ruler image do the explaining underneath it.
- **The title survives either way.** "The Shape of Time" rests on time having a geometry; a line with no ruler along it is a statement about shape — arguably a better fit than a clock reading zero.

PC should not draft the Prelude or Ch 1 opening until Greg rules.

---

— AC, 2026-09-18.
