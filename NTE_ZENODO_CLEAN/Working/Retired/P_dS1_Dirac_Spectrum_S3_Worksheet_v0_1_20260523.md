# P-dS1 — Dirac spectrum on $S^3$ and Gibbons–Hawking entropy worksheet v0.1

**Stream:** Cursor scaffold → Jammer/Scratch (§22.8 pathway)  
**Date:** 2026-05-23  
**Status:** **S0 setup** — spectrum catalogue + entropy target; no TT/KMS closure  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-dS1

---

## §1. Mission

Formal step toward §22.8 de Sitter QM: show NTE's **finite-dimensional** spinor structure on $S^3$ accommodates **Gibbons–Hawking entropy** $S_{\rm GH} = \pi H^{-2}$ at the gauge-birth scale $H_{\rm GB} = \alpha M_{\rm Pl}^2$.

**Links:** §17.5.4 (C2) $N_{\rm lock} = S_{\rm dS}/4$; §22.19 N_lock holographic identity.

---

## §2. Dirac spectrum on unit $S^3$ (catalogue)

Eigenvalues of Dirac operator on $S^3$ radius $r$ (Bär 1996 convention):

$$\lambda_n = \pm\left(n + \frac{3}{2r}\right), \quad n = 0,1,2,\ldots$$

Degeneracy per level (spinor Laplacian):

$$g_n = 2(n+1)(n+2) \quad\text{(for each sign branch)}$$

**NTE radius at gauge birth:** $r_{\rm GB} \sim 1/H_{\rm GB} \sim 1/(\alpha M_{\rm Pl}^2)$ (Hubble radius at locking).

---

## §3. Entropy target

Gibbons–Hawking (de Sitter):

$$S_{\rm GH} = \frac{\pi}{H^2} \quad (G=\1,\ c=1)$$

At $H = H_{\rm GB} = \alpha M_{\rm Pl}^2$:

$$S_{\rm GH,GB} = \frac{\pi}{(\alpha M_{\rm Pl}^2)^2}$$

**Corpus N_lock candidate (§17.5.4):** $N_{\rm lock} = S_{\rm dS}/4 = S_{\rm GH,GB}/4$.

With $g_{\rm eff} = 106.75$ at gauge birth (§17.5.10):

$$N_{\rm lock} \stackrel{?}{=} \frac{45}{4\,g_{\rm eff}} \approx 0.105$$

**Check (Cursor OOM):** compare $S_{\rm GH,GB}/4$ to $0.1$ — requires explicit $\alpha$, $M_{\rm Pl}$ numerics in v0.2 script.

---

## §4. NTE-specific content (not in standard GH)

| NTE layer | Role |
|-----------|------|
| $A_F = \mathbb{O}\oplus\mathbb{O}$ | Finite spectral triple — **dimensionality** of physical Hilbert space |
| Hopf projection | Relates $S^3$ spinor modes to $S^2$ base (κ derivation kin) |
| N-thickness / F1 | $\ell = 1/H$ links entropy to thickness geometry |
| Pre-temporal HH | Euclidean section $N<N_{\rm lock}$ — entropy counting on **sub-phase** saddle |

---

## §5. Deliverables checklist

| ID | Task | Owner | Status |
|----|------|-------|--------|
| P-dS1a | Spectrum sum / zeta-regularised $\eta_D(0)$ on $S^3_{r(H)}$ | Scratch | Open |
| P-dS1b | Match $S_{\rm GH}$ to log-dim or microstate count | Jammer | Open |
| P-dS1c | Bridge to $N_{\rm lock}=S_{\rm dS}/4$ | Jammer | Open |
| P-dS1d | Script `p_ds1_gh_entropy_check.py` | Cursor v0.2 | **Done** — see v0.2 worksheet |

---

## §6. Discipline

- Do **not** claim dS/CFT closed — only entropy **accommodation** on $S^3$
- P0.10 Tomita-Takesaki on $A_F$ remains parallel (Scratch Task 1)
- κ₀ derivation **independent** of this worksheet (S2-D §2.5)

---

## §7. Cross-references

- §22.8, §22.19, §17.5.4  
- Companion 9 (HH saddle); `17.5.4_Audit_NLock_Derivation.md`

— Cursor P-dS1 v0.1, 2026-05-23.
