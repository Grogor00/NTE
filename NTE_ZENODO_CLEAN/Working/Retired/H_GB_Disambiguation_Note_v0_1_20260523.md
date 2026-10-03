# H_GB disambiguation note v0.1 (P-dS1 cross-check follow-up)

**Date:** 2026-05-23  
**Trigger:** `p_ds1_gh_entropy_check.py` — Route A/C PASS, Route B FAIL  
**Status:** **Corpus notation fix** — not a prediction change  
**Master patches:** §17.5.4, §18.2 (v10.17 Part 3)

---

## §1. Problem

Corpus uses **H_GB** for two quantities that differ by **~10²⁸**:

| Symbol (v0.1) | Definition | Typical value | Used in |
|---------------|------------|---------------|---------|
| **H_GB^(F)** | Friedmann H at $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$, $g_{\rm eff}=106.75$ | $\sim 3\times10^{19}$ GeV | §17.5.4 (C1)+(C2); $S_{\rm dS}=45/g_{\rm eff}$; $N_{\rm lock}$ |
| **H_GB^(α)** | Constraint H at locking: $H=\alpha M_{\rm Pl}^2$ (§2.3.1 anchor) | $\sim 3.5\times10^{-9}$ GeV | §18.2 $N_e$; M₁ Pathway α; CMB pivot |

**Algebra (audit chain):** $H_{\rm GB}^{(F)\,2} = (\pi g_{\rm eff}/45)\,M_{\rm Pl}^2$ → $S_{\rm dS}=\pi M_{\rm Pl}^2/H^2=45/g_{\rm eff}$ → $N_{\rm lock}=0.1054$.

**Not an identity:** $H_{\rm GB}^{(\alpha)} \neq H_{\rm GB}^{(F)}$ with corpus $\alpha=2.38\times10^{-47}$ GeV$^{-1}$.

---

## §2. Resolution (corpus default v0.1)

1. **Retain both** — they label **different physical readings** at the gauge-birth transition, not a single Hubble parameter.

2. **H_GB^(α)** — **locking constraint H** when temporal ordering crystallises; set by ratified $\alpha$ calibration ($H_0=\alpha v_{\rm EW}^2$). Drives $N_e$, $|Φ|$ trajectory endpoint, M₁ scale.

3. **H_GB^(F)** — **thermal Friedmann H** at $T_{\rm GB}$ when the SM plasma is relativistic at $g_{\rm eff}$; enters **horizon entropy** and audit (C2). Does **not** replace $H_{\rm GB}^{(\alpha)}$ in §18.2.

4. **Bridge (open):** three-epoch timeline — thermal **(F)**, inflation **N_e**, locking **(α)**; see `H_GB_Bridge_Attack_Route_v0_1`. **Do not force equality** without derivation.

---

## §3. What does NOT change

- $N_{\rm lock}=45/(4g_{\rm eff})\approx 0.105$ (candidate derivation)
- $N_e=-\ln(\alpha M_{\rm Pl})\approx 63.4$; $n_s=0.9685$
- $H_{\rm GB}^{(\alpha)}=\alpha M_{\rm Pl}^2$ numerics in §18.1

---

## §4. Cross-references

- `P_dS1_Dirac_Spectrum_S3_Worksheet_v0_2_20260523.md`
- `17.5.4_Audit_NLock_Derivation.md` §3.4

— Cursor, 2026-05-23.
