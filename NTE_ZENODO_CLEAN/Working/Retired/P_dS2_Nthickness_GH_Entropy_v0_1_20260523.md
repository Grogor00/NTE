# P-dS2 — N-thickness ↔ Gibbons–Hawking horizon entropy v0.1 (§22.8)

**Stream:** Cursor → Jammer/Scratch  
**Date:** 2026-05-23  
**Script:** `Working/p_ds2_nthickness_gh_link.py`  
**Status:** **F1 + GH + audit chain linked** at $H_{\rm GB}^{(F)}$ — not full dS QM closure

---

## §1. Mission

Connect **F1** ($\ell = 1/H$) to **Gibbons–Hawking entropy** at the gauge-birth de Sitter horizon, extending P-dS1 cross-check into thickness language (§22.8 P-dS2).

---

## §2. Identities (corpus stack)

| Layer | Relation |
|-------|----------|
| **F1** | $\ell = 1/(\alpha|\Phi|^2) = 1/H$ — proper-length thickness = Hubble radius |
| **GH** | $S_{\rm GH} = \pi M_{\rm Pl}^2/H^2 = A/(4G)$ with $A=4\pi/H^2$ |
| **Horizon radius** | $r_H = 1/H = \ell$ at same $H$ |
| **Audit (C2)** | $N_{\rm lock} = S_{\rm dS}/4 = 45/(4g_{\rm eff})$ |

**Programme reading:** pre-temporal e-fold depth to locking ($N_{\rm lock}$) is **one quarter** of horizon entropy counted in GH units at **$H_{\rm GB}^{(F)}$** — not at $H_{\rm GB}^{(\alpha)}$.

---

## §3. Numerics (script)

At $H_{\rm GB}^{(F)} \sim 3.3\times10^{19}$ GeV:

| Quantity | Value |
|----------|-------|
| $\ell = 1/H$ | $\sim 3\times10^{-20}$ GeV$^{-1}$ |
| $S_{\rm GH}$ | **0.4215** |
| $N_{\rm lock}$ | **0.1054** |
| $N_{\rm lock}/S_{\rm GH}$ | **0.25** exactly (C2 form) |

At $H_{\rm GB}^{(\alpha)}$: $\ell$ huge, $S_{\rm GH}\sim10^{55}$ — **inconsistent** with $N_{\rm lock}\sim0.1$ (P-dS1 Route B FAIL).

---

## §4. What P-dS2 does NOT claim

- Dirac mode count = $S_{\rm GH}$ (P-dS1: microstates open)  
- dS/CFT or Tomita-Takesaki (P-dS3)  
- Bridge $H_{\rm GB}^{(\alpha)}$ ↔ $H_{\rm GB}^{(F)}$ (§22.18–§22.19)

---

## §5. Cross-references

- `P_dS1_Dirac_Spectrum_S3_Worksheet_v0_2_20260523.md`  
- `H_GB_Disambiguation_Note_v0_1_20260523.md`  
- §17.5.4, §22.8, Appendix E (N-thickness)

— Cursor P-dS2 v0.1, 2026-05-23.
