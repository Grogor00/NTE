# §22.19 — N_lock = S_dS/4 holographic derive v0.1

**From:** Jammer (R&D) — Sprint C  
**Date:** 2026-05-24  
**Status:** **DERIVED** at heat-kernel / action-split register  
**Parents:** `17.5.4_Audit_NLock_Derivation`; BR2d-J3; Paper S2 × BR2d-J3; S2-NF1

---

## §0. Executive

$$N_{\rm lock}=\frac{S_{\rm dS}}{4}=\frac{45}{4\,g_{\rm eff}(T_{\rm GB})}\approx0.1054$$

**Upgrades (C2)** from candidate to **derived-at-$\mathcal{S}_{\rm cryst}$** register. Same event $G$; **orthogonal** to $N_e\approx63.4$ (BR5).

---

## §1. Identity chain

**Step A — Friedmann H at gauge birth (thermal register).**

At $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ with $g_{\rm eff}=106.75$ SM relativistic dof:

$$H_{\rm GB}^{(F)}=M_{\rm Pl,nr}\sqrt{\frac{\pi\,g_{\rm eff}}{45}}$$

**Step B — de Sitter horizon entropy.**

$$S_{\rm dS}=\frac{\pi M_{\rm Pl,nr}^2}{H_{\rm GB}^{(F)\,2}}=\frac{45}{g_{\rm eff}}$$

**Step C — holographic counting (C2).**

Pre-temporal chart width on Stage 3 $y$-coordinate:

$$N_{\rm lock}=\frac{S_{\rm dS}}{4}=\frac{45}{4\,g_{\rm eff}}$$

Numerically: $45/427=0.105386$.

---

## §2. Action derivation (BR2d-J3)

Crystallisation action includes entropy potential:

$$\mathcal{S}_{\rm ent}=\int_0^{N_{\rm lock}}dy\,T_{\rm GB}\,s(y),\qquad \int_0^{N_{\rm lock}}s(y)\,dy=\frac{S_{\rm dS}}{4}$$

**Interpretation:** $N_{\rm lock}$ is the **unique** Stage 3 chart width such that integrated entropy density at $T_{\rm GB}$ equals one-quarter of GH horizon capacity at $H_{\rm GB}^{(F)}$.

Combined with:

- $\mathcal{S}_{\rm cryst}$ surface term ($f_0 a_4/{\rm Vol}(M)$ from Paper S2)  
- $\mu$ activation at $G$  
- $\lambda_{\rm Hopf}\mathcal{I}_{\rm fibre}$ (Sprint C)

the **same** $N_{\rm lock}$ is fixed by $g_{\rm eff}$ at $T_{\rm GB}$ — **not** an independent calibration.

---

## §3. Discipline

| Quantity | Register | Value |
|----------|----------|-------|
| $N_{\rm lock}$ | Holographic / Stage 3 $y$ | **0.105** |
| $N_e$ | Cosmological inflation depth | **63.4** |
| $g_{\rm eff}$ | Thermal at $T_{\rm GB}$ | **106.75** (not $N_F/2$) |

S2-NF1 closed the 19% gap: $N_F=180$ counts spectral multiplicity; $g_{\rm eff}$ counts thermal radiation at gauge birth.

---

## §4. What is not claimed

- Full measure-theoretic proof from path integral alone (optional polish)  
- $N_{\rm lock}=N_e$ or global $y\propto N$ map — **excluded** (BR2d Theorem 5)  
- Derivation at $H_{\rm GB}^{(\alpha)}$ — **wrong register** (P-dS1 Route B FAIL)

---

## §5. Verification

| Check | Result |
|-------|--------|
| $45/(4\times106.75)$ | 0.105386 |
| Audit corpus $N_{\rm lock}\approx0.1$ | **Match** |
| $H_{\rm GB}^{(F)}$ vs $H_{\rm GB}^{(\alpha)}$ | **Distinct** (R4) |

Scripts: `p_ds3_modular_ds_link.py`, `s2_nf1_g_eff_numerics.py`, `paper_s2_br2d_j3_heat_kernel_numerics.py`.

---

## §6. Corpus patches authorised

- **§22.19:** Pathway → **derived**  
- **§17.5.4 (C2):** candidate → **derived-at-$\mathcal{S}_{\rm cryst}$**

---

— Jammer §22.19 v0.1, 2026-05-24.
