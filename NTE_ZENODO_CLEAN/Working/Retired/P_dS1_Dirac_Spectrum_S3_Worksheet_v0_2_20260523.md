# P-dS1 — Dirac spectrum on $S^3$ and Gibbons–Hawking entropy worksheet v0.2

**Stream:** Cursor → Jammer/Scratch (§22.8 pathway)  
**Date:** 2026-05-23  
**Status:** **Cross-check complete** — (C1)+(C2) internal PASS; **H_GB scale tension flagged**  
**Script:** `Working/p_ds1_gh_entropy_check.py`  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-dS1

---

## §1. Mission

Formal step toward §22.8 de Sitter QM: show NTE's spinor structure on $S^3$ accommodates **Gibbons–Hawking entropy** at gauge birth and test **$N_{\rm lock} = S_{\rm dS}/4$** (§17.5.4 audit).

---

## §2. Cross-check results (v0.2)

### Route A — closed form (audit §3.4)

| Quantity | Value |
|----------|-------|
| $g_{\rm eff}$ | 106.75 |
| $S_{\rm dS} = 45/g_{\rm eff}$ | **0.4215** |
| $N_{\rm lock} = S_{\rm dS}/4 = 45/(4g_{\rm eff})$ | **0.1054** |
| Corpus prose | 0.1 (5.4% rounding gap) |

**PASS** — candidate identity reproduces corpus $N_{\rm lock} \approx 0.1$.

### Route C — Friedmann at $T_{\rm GB} = M_{\rm Pl}/\sqrt{2\pi}$ (audit C1) → (C2)

| Quantity | Value |
|----------|-------|
| $H_{\rm GB}$ (Friedmann, $M_{\rm Pl}=1.221\times10^{19}$ GeV) | $\sim 3.33\times10^{19}$ GeV |
| $S_{\rm GH} = \pi M_{\rm Pl}^2/H^2$ | **0.4215** |
| $N_{\rm lock} = S/4$ | **0.1054** |

**PASS** — (C1)+(C2) chain is **algebraically self-consistent** (Route A = Route C).

### Route B — corpus §18.2 $H_{\rm GB} = \alpha M_{\rm Pl}^2$

| Quantity | Value |
|----------|-------|
| $\alpha$ | $2.38\times10^{-47}$ GeV$^{-1}$ |
| $H_{\rm GB} = \alpha M_{\rm Pl}^2$ | $\sim 3.55\times10^{-9}$ GeV |
| $S_{\rm GH}$ | $\sim 10^{55}$ (not O(1)) |
| $N_{\rm lock} = S/4$ | **incompatible** with Route A |

**FAIL** — $\alpha$-calibrated $H_{\rm GB}$ is **$\sim 10^{28}\times$ smaller** than Friedmann-(C1) $H_{\rm GB}$.

**Implied $\alpha$ for Route A consistency:**

$$\alpha_{\rm req} = \sqrt{\frac{\pi g_{\rm eff}}{45 M_{\rm Pl}^2}} \approx 2.24\times10^{-19}\ {\rm GeV}^{-1}$$

Corpus $\alpha = 2.38\times10^{-47}$ GeV$^{-1}$ → ratio $\alpha_{\rm corpus}/\alpha_{\rm req} \sim 10^{-28}$.

---

## §3. Reading (honest register)

1. **$N_{\rm lock} = 45/(4g_{\rm eff})$ is internally consistent** with audit (C1)+(C2) when $H_{\rm GB}$ comes from Friedmann at $T_{\rm GB} = M_{\rm Pl}/\sqrt{2\pi}$ — not from $\alpha M_{\rm Pl}^2$.

2. **Corpus uses two H-scales at gauge birth:**
   - **§18.2 / n$_s$ route:** $H_{\rm GB} = \alpha M_{\rm Pl}^2 \sim 10^{-9}$ GeV (present-epoch calibration anchor)
   - **§17.5.4 audit (C1):** $H_{\rm GB}^2 = (\pi g_{\rm eff}/45)M_{\rm Pl}^2 \sim 10^{38}$ GeV$^2$ (Friedmann at Planck-scale $T_{\rm GB}$)

   These are **not the same H** unless a bridge is derived. **Jammer action item:** disambiguate $H_{\rm GB}^{\rm (Friedmann)}$ vs $H_{\rm GB}^{\rm (\alpha)}$ in master §17.5.4 / §18.2.

3. **Dirac microstate matching** — naive $S^3$ mode count at $r=1/H_{\rm GB}^{(\alpha)}$ gives $n_{\max}\sim M_{\rm Pl}/H \sim 10^{27}$; $S_{\rm GH}\sim 0.42$ is **O(1) horizon entropy**, not literal level counting. **Accommodation open** (P-dS1a/b).

4. **Cross-check does not falsify** $N_{\rm lock}\approx 0.1$ at candidate-derivation level; it **sharpens** open work on H-scale identification and holographic proof (§22.19).

---

## §4. Dirac spectrum catalogue (unchanged from v0.1)

$$\lambda_n = \pm\left(n + \frac{3}{2r}\right), \quad g_n = 2(n+1)(n+2)$$

---

## §5. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| P-dS1d | `p_ds1_gh_entropy_check.py` | **Done v0.2** |
| P-dS1c | Bridge $N_{\rm lock}=S/4$ | **Partial** — algebra PASS; H-scale tension |
| P-dS1a/b | Dirac ↔ $S_{\rm GH}$ microstates | Open |
| **NEW** | Master disambiguation $H_{\rm GB}$ scales | **Done** — §17.5.4/§18.2 + disambiguation note |

---

## §6. Cross-references

- `Papers/17.5.4_Audit_NLock_Derivation.md` §3.4–§4  
- §17.5.4, §18.2, §22.19  
- Companion 9 (HH saddle / T_GB)

— Cursor P-dS1 v0.2, 2026-05-23.
