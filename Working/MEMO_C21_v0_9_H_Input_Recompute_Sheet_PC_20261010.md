# MEMO — C21 v0.9: H input correction sheet (PC)

**Status:** Working prep — **not a Core patch.**  
**Date:** 2026-10-10  
**Trigger:** PC used H = 2.141 × 10⁻¹⁸ s⁻¹; deposit T_reset implies **H_dS ≈ 1.81 × 10⁻¹⁸ s⁻¹** (Jammer + AC adopted 2026-10-07).

---

## What changes vs what does not

| Quantity | H-dependent? | Action at v0.9 |
|---|---|---|
| E-fold count from T\_today / T\_reset | **No** (ln ratio) | **67** nominal; **~65** first-occurrence estimate **unchanged** |
| Ht at crossing | **Yes** (Ht = N in dS) | Should read **67** at nominal if H from paper — **already corrected in v0.8 text** |
| **Years** to N e-folds (if computed as N/H) | **Yes** | Scale × **(2.141/1.81) ≈ 1.18** (~18% longer) |
| No-hair residue e^(−3Ht) | **Yes** | Exponent uses Ht; at fixed **N**, residue scales with **same H correction** — **qualitative §10 argument (causal severance) unchanged** |
| 10⁻⁹⁰ / anchor-independent claims | Per prior ruling | **Unaffected** |

---

## Inputs (single source)

- T_reset = 2.213 × 10⁻²⁹ K (paper)  
- T_CMB ≈ 2.725 K → ln(T_CMB/T_reset) ≈ **67** e-folds  
- H from T_reset on dS plateau: **1.81 × 10⁻¹⁸ s⁻¹** (not H₀ = 2.19 × 10⁻¹⁸ unless explicitly labelled observational contrast)

**Wrong input:** H = 2.141 × 10⁻¹⁸ s⁻¹ (PC plateau, pre-correction).

---

## v0.9 checklist (PC + AC mappability rulings)

1. Sweep C21 for any **year** figure still implicitly using 2.141/H.  
2. Confirm §2 / §10 **Ht** and residue prose consistent with **N = 67** and **H = 1.81 × 10⁻¹⁸**.  
3. Fold AC five mappability rulings (2026-10-08 arbitration) — **not duplicated here**.  
4. No §7 κ cross-dependency (firewall — broad withdrawal standing).

---

## Order-of-magnitude year check (nominal 67 e-folds)

t ≈ N/H:

- At H = 1.81 × 10⁻¹⁸ s⁻¹: t ≈ 3.7 × 10¹⁹ s ≈ **1.2 × 10¹² yr**  
- At H = 2.141 × 10⁻¹⁸ s⁻¹: t ≈ 3.1 × 10¹⁹ s ≈ **1.0 × 10¹² yr**

v0.8 already states **≈ 1 × 10¹² years** at corrected physics — **consistent with 1.81 × 10⁻¹⁸**.

— Cursor Main, 2026-10-10
