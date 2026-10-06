# Handoff — AC → Cursor: Ω_k register correction + T_GB conditional flag (Greg-ratified)

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-24
**Greg ratified 2026-09-24, 18:00 NZST.** Cursor is offline as of the last check; this queues for its return.
**Targets:** `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` (P3-Ω); `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` (P1-Ω); `NTE_Workflow_Manifest_v10_18.md` (MF-Ω, MF-T).
**Render:** Part 3 and Part 1 after their patches.
**No numbers change.** These are register corrections.

Byte-exact match-or-report throughout.

---

## Why

Part 3 grades **Ω_k = 0** as *derived within the framework (structural)*. Exact spatial flatness is the one value a **closed S³ of finite radius cannot have** — Ω_k = 0 is the flat case; a finite closed S³ has Ω_k < 0 in the density convention. The corpus was asserting something its own geometry forbids, undetected because the observational difference is far below measurement precision (Planck 2018: Ω_k = 0.0007 ± 0.0019).

**This is not a concession to data.** No evidence contradicts NTE here. The corrected claim is **stronger**: the S³ radius is vast after the e-fold run, so the observable patch is flat to any achievable precision — observed flatness becomes a *prediction of the e-fold history* rather than a coincidence the framework must survive.

Part 1 §2.3 separately mis-describes Part 3's grading of w and Ω_k. That is corrected here too.

---

## P3-Ω — Part 3, derived/structural ledger

```
OLD:
- Spatial flatness $\Omega_k = 0$ (boundary-only ontology); $w = -1$ (geometric-unloading de Sitter asymptote).

NEW:
- Spatial flatness $\Omega_k \to 0$ — the $S^3$ is closed, and its radius after the e-fold run is vast compared with the observable patch, so curvature is undetectable at every scale we can probe (Planck 2018: $\Omega_k = 0.0007 \pm 0.0019$). Observed flatness is thus a consequence of the expansion history, not an assumption. Exact $\Omega_k = 0$ is **not** claimed: a closed $S^3$ of finite radius has $\Omega_k < 0$, and exact flatness would contradict the closure the boundary ontology rests on. $w = -1$ (geometric-unloading de Sitter asymptote).
```

## P1-Ω — Part 1 §2.3, correct the account of Part 3

Part 1 states that Part 3 carries H₀, w and Ω_k as *construction/inherited*. Part 3 carries H₀ under tautological-consequences-of-construction, but **w and Ω_k under derived/structural**. The sentence's intent — that the added scalar introduces no new FRW dynamics — is preserved; only the register labels are wrong.

```
OLD:
consistent with Part 3 carrying $H_0$, $w$, and $\Omega_k$ as construction/inherited rather than as new FRW dynamics

NEW:
consistent with Part 3 carrying $H_0$ as a consequence of construction, and $w$ and $\Omega_k \to 0$ as structural consequences of the boundary ontology, rather than as new FRW dynamics
```

---

## MF-Ω and MF-T — manifest §3

**Check-first: AC does not hold byte-exact text for §3 this session.** Locate each line, **report it verbatim**, then apply.

**MF-Ω.** §3 lists **Ω_k = 0** under *Derived / structural*. Replace that entry with:
```
Ω_k → 0 (closed S³; radius vast after the e-fold run — observed flatness predicted, not assumed; exact Ω_k = 0 not claimed, and would contradict closure)
```

**MF-T.** §3's *Derived / structural* line states the Companion 12 fibre-modulus identification as a closure — wording to the effect of *"T_GB = M_Pl/√(2π) — closed at the Hartle–Hawking Gaussian saddle-width (Companion 9), fibre-modulus identification β_GB·M_Pl = √(2π) from the spectral side (Companion 12)"*. **Part 3 says that identification is the open item**, not the closure. Replace with:
```
T_GB = M_Pl/√(2π) — CONDITIONAL (2026-08). The Gaussian-width argument assumes a nucleation saddle of the constrained system; the raw-trace saddle is ruled out (Companion 9 addendum / Companion 15 §6.3). The Companion 12 fibre-modulus identification β_GB·M_Pl = √(2π) is the candidate independent grounding and is OPEN. Not graded unconditionally derived.
```
§3's other two T_GB entries already read *conditional* and need no change. **Report all three after patching** so the snapshot is self-consistent.

---

## MF-R — manifest §10 registration

```
- **CLOSED 2026-09-24 — Ω_k register.** Part 3's derived entry claimed exact spatial flatness, which a closed S³ of finite radius cannot have. Corrected to Ω_k → 0 with the e-fold-run reasoning; Part 1 §2.3's account of Part 3's grading corrected with it (it mis-stated w and Ω_k as construction/inherited). Greg-ratified. No numbers change. Found by PC during the 2026-09-24 Book campaign (flag N1); Chapter 3 needed no change.
- **CLOSED 2026-09-24 — T_GB snapshot contradiction.** §3 graded T_GB derived and conditional simultaneously, citing Companion 12 both ways. Part 3 wins: conditional, fibre-modulus grounding open. Chapter 15 patches B1/B10 confirmed correct and released. Found by PC (flag F5).
```

---

## Deliverables

Patches applied; the three §3 lines reported verbatim before and after; Part 1 and Part 3 re-rendered with PDF newer than `.md`; completion handoff to `Handoffs\` addressed to AC.

---

— AC, 2026-09-24.
