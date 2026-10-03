# BR5 — $N_{\rm lock}$ vs $N_e$ prose patch v0.1 (LB-5)

**Stream:** Cursor draft → **AC** master integration  
**Date:** 2026-05-23  
**Target:** `NTE_v10_17_Part3_Accounting.md` §XVIII / §17.5.14 pointer  
**Status:** Patch instructions only — ~~not applied to master locally~~ **APPLIED** (Sprint B, 2026-05-24; log `LB5_Part3_Prose_Patch_Applied_v0_1`)

---

## Problem

§18.2 and §17.5.14 still blur **holographic locking width** ($N_{\rm lock}\approx0.1$ on Stage 3 coordinate $y$) with **inflation e-fold depth** ($N_e\approx63.4$ on cosmological $N$). BR2/BR2c require explicit separation.

---

## Patch BR5-1: §18.2 after first paragraph (insert coordinate note)

**After** the sentence ending "...gauge birth is reheating, not the inflationary phase."

**Insert:**

> **Coordinate discipline (v10.17.1+).** $N_e=-\ln(\alpha M_{\rm Pl})\approx63.4$ counts **cosmological e-folds** $N$ over the pre-temporal inflation sector (Role B / constraint terminal roll — see `Working/Phi_N_Trajectory_BR2c_Attack_Route_v0_1`). It is **not** the Stage 3 surface-ontology width $N_{\rm lock}=S_{\rm dS}/4\approx0.105$ (§17.5.4, audit §2). Do not substitute one for the other in formulas or prose.

---

## Patch BR5-2: §17.5.14 status bullet (add pointer)

**After** the Companion 9 Session 3 closure bullet (n_s = 1 − 8M_Pl²/Φ²):

**Insert:**

> *BR2c (2026-05-23): Role (B) slow-roll closes $n_s$; Role (A) constraint trajectory closes lock endpoints — two-sector resolution per §17.5.19; single exponential $H(N)$ matches $N_e$ only (`Working/Phi_N_Trajectory_BR2_v0_1`).*

---

## Patch BR5-3: §17.5.4 (add one line)

**After** bridge pointer to `H_GB_Bridge_Attack_Route_v0_1`:

**Insert:**

> **BR5:** $N_{\rm lock}$ (holographic) and $N_e$ (inflation depth) are **different coordinates**; see `Working/BR5_Nlock_Ne_Prose_Patch_v0_1`.

---

## Verification

- [ ] No prose equates $N_{\rm lock}$ with $N_e$
- [ ] §18.2 spectral-tilt paragraph references Role (B) for $n_s$, not lock width
- [ ] Cross-ref BR2c in §17.5.21 register optional row

— Cursor BR5 patch v0.1, 2026-05-23.
