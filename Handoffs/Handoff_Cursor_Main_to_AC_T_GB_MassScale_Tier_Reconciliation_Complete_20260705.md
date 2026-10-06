# Handoff — Cursor Main → AC: T_GB / mass-scale tier reconciliation COMPLETE (v10.18.0)

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC · **Date:** 2026-07-05
**Re:** `Patch instructions — T_GB / mass-scale tier reconciliation (v10.18.0)` (AC 2026-07-04). Split resolution applied: **upgrade T_GB in Part 3**; **downgrade Majorana/Dirac mass scales in Companion 12**.

All five edits applied to the canonical deposit sources. Every OLD block matched cleanly — no near-misses, no forced substitutions. Re-rendered Part 3 and Companion 12; deposit PDF set remains **29/29**.

---

## Files edited (canonical)

| File | Path |
|---|---|
| Part 3 | `Core_Papers/NTE_v10_18_0_Part3_Accounting.md` |
| Companion 12 | `Core_Papers/Companion_12_Chord_v10_18_0.md` |

**Duplicate sync:** `paper-build/scratch-src/` copies of both files updated from Core_Papers before render (no divergence).

---

## Part 3 — `NTE_v10_18_0_Part3_Accounting.md`

### Edit 1A — T_GB added to "Derived within the framework (structural)"
Inserted after the Standard BBN line:
- `$T_{\mathrm{GB}} = M_{\mathrm{Pl}}/\sqrt{2\pi}$` (gauge-birth temperature)
- Closed at Hartle–Hawking Gaussian saddle-width (Companion 9)
- Fibre-modulus identification `$\beta_{\mathrm{GB}}M_{\mathrm{Pl}}=\sqrt{2\pi}$` cross-checked from spectral side (Companion 12)
- `$\sqrt{2\pi}$` is Gaussian normalisation, not a fitted constant

### Edit 1B — T_GB removed from "Cross-checks / candidate derivations"
Cross-checks tier now reads:
- `$M_1$` (geometric, O(1) residue ~1.1); `$M_R$` (pathway identified, not derived); `$N_{\mathrm{lock}}$` (candidate, pending closure); two-branch solar mass
- **T_GB no longer listed here**

---

## Companion 12 — `Companion_12_Chord_v10_18_0.md`

### Edit 2A — Abstract: four → three clean-spine results
- Clean-spine set: **κ₀, T_GB, 2π² audit**
- Majorana/Dirac mass scales moved to cross-checked register (Companions 10, 13); O(1) residual + unresolved 8π/4π branch; not counted among clean-spine results

### Edit 2B — §4 register table
- **Cleanly derived on the spine (three results):** κ₀, T_GB, 2π² audit — with T_GB closure note (Companion 9 + fibre-modulus cross-check; master accounting grades derived/structural)
- **New paragraph — Cross-checked on the spine, at their own register:** M₁, M_R, Y_{ν₂} with explicit caveats (O(1) ~1.1 residual; M_R pathway not closed; solar 0.993× branch-contingent; atmospheric ≈1.5× overshoot open)

### Edit 2C — §4 closing sentence
- Coherence claim now attaches to **three** cleanly-derived results, **cross-checked mass scales**, and structural Λ

---

## Post-edit verification (source)

| Check | Result |
|---|---|
| Part 3: T_GB in structural tier | **1** occurrence (L28) |
| Part 3: T_GB in cross-checks tier | **0** |
| Part 3: N_lock still candidate | **yes** (cross-checks line) |
| Companion 12: "four cleanly-derived" | **0** |
| Companion 12: "three cleanly-derived" | **2** (abstract + §4 closing) |
| Companion 12: "Cross-checked on the spine" | **present** (§4) |

**Cross-document consistency:** T_GB reads clean/derived in both Part 3 and Companion 12. M₁/M_R/Y_{ν₂} read cross-check/open in both. No quantity graded "cleanly derived" in one document and "candidate/open" in the other.

---

## Render results

| PDF | Size | Status |
|---|---|---|
| `paper-build/pdf-out/NTE_v10_18_0_Part3_Accounting.pdf` | 55.4 KB | PASS (re-rendered 2026-07-05) |
| `paper-build/pdf-out/Companion_12_Chord_v10_18_0.pdf` | 43.6 KB | PASS (re-rendered 2026-07-05) |

**Deposit set:** 29/29 PDFs present in `paper-build/pdf-out/` (Book excluded).

### PDF spot-check (pdftotext)
- **Part 3:** "gauge-birth temperature" + "Hartle" present in structural context; cross-checks line shows `N_lock (candidate, pending closure)` only — **no T_GB candidate**
- **Companion 12:** "three cleanly-derived" + "Cross-checked on the spine" present; **no** "four cleanly-derived"

---

## Ready for CR

Expected post-edit state per AC patch spec is met. Requesting CR pass on Part 3 §XVII and Companion 12 abstract + §4, then Greg ratification.

No other quantities moved. §3 (Companion 12 caveats), §1/§5 (generic usage), and all other deposit files unchanged.

— Cursor Main, 2026-07-05.
