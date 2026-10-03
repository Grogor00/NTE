# S2-NF1 — $g_{\rm eff}(T_{\rm GB})$ thermal map v0.1

**From:** Jammer (R&D) — Sprint A item 4  
**Date:** 2026-05-24  
**Status:** **CLOSED at register level**  
**Script:** `Working/s2_nf1_g_eff_numerics.py`

---

## §0. Problem

Paper S2 heat-kernel upgrade noted **19% gap** between $N_{\rm lock}=45/(4\cdot N_F/2)=0.125$ and corpus $N_{\rm lock}=0.1054$.

---

## §1. Sunshine

$N_F=180$ counts **Dirac internal multiplicity** on $A_F$ in $a_4$ heat-kernel.

$g_{\rm eff}=106.75$ counts **SM thermal radiation dof** at $T_{\rm GB}\gg m_{\rm top}$:

$$g_{\rm eff} = 28 + \frac{7}{8}\times 90 = 106.75$$

Then $N_{\rm lock}=S_{\rm dS}/4$ with $S_{\rm dS}=\pi M_{\rm Pl}^2/H_{\rm Friedmann}^2(T_{\rm GB})$ gives **exact** $0.105386$.

**The 19% gap is solely from wrongly identifying $N_F/2$ with $g_{\rm eff}$.**

---

## §2. Verdict

| Map | $N_{\rm lock}$ | Status |
|-----|----------------|--------|
| $45/(4\cdot N_F/2)$ | 0.125 | **WRONG** |
| $45/(4\cdot g_{\rm eff})$ | 0.105386 | **CORRECT** |

**S2-NF1: CLOSED.** Optional: formal SM thermal derivation in Paper S2 Session 2.

---

— Jammer S2-NF1 v0.1, 2026-05-24.
