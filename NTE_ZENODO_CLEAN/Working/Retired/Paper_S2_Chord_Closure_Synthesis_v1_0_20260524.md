# Paper S2 — six-note chord closure synthesis v1.0

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at heat-kernel register** — post-sprint consolidation  
**Script:** `Working/paper_s2_chord_closure_numerics.py`  
**Parents:** Paper S2 S2-A–S2-E arc; `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0`; `Jammer_J1_G4_PaperS2_Unified_Action_Derive`; Companion 11 (Λ); J6-D2 (n_s)

---

## §0. Executive

Programme S **Paper S2** central deliverable is a **single** Seeley–DeWitt computation on

$$M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F,\qquad A_F=\mathbb{O}\oplus\mathbb{O}$$

yielding Charter predictions **D1–D9** as **six notes from one chord** — not six independent fits.

**Verdict (2026-05-24):** Scratch arc S2-A → S2-E is **structurally complete** at heat-kernel register. May 2026 sprint closes the **Λ numerical gap** (~1.05×) and upgrades **BR2d-J3** + **J1-G4** unified boundary action. **Canonical paper:** `Papers/Companion_12_Spectral_Chord_Closure_v10_17.md`.

---

## §1. Single spine (S2-A)

| Quantity | Value | Role |
|----------|-------|------|
| ${\rm Vol}(S^3)$ | $2\pi^2$ | topology lock |
| $\beta_{\rm GB}$ | $\sqrt{2\pi}/M_{\rm Pl,nr}$ | fibre modulus |
| ${\rm Vol}(M)$ | $2\pi^2\beta_{\rm GB}$ | spectral triple internal volume |
| $N_F$ | $180$ | $A_F=\mathbb{O}\oplus\mathbb{O}$ Hilbert dimension |
| $D_M$ | $D_{S^3}\otimes1+\gamma_{S^3}\otimes D_{S^1}$ | Dirac on $M$ |
| Spin on $S^1$ | $\theta=1/2$ antiperiodic | Greg ratification (S2-A) |

**Confluence:** $\beta_{\rm GB}M_{\rm Pl,nr}=\sqrt{2\pi}$ ⟹ $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ (Note 2).

---

## §2. Heat-kernel coefficients (S2-B, S2-C-B)

On $M$ with Dirac $D_M$, spinor rank $r=4$:

$$\boxed{a_0=\frac{N_F\beta_{\rm GB}}{2},\quad a_2=-\frac{N_F\beta_{\rm GB}}{4},\quad a_4\big|_M=\frac{3N_F\beta_{\rm GB}}{2}=270\beta_{\rm GB}}$$

**F1 cancellation on $M$:** $5R^2-8R_{\mu\nu}^2-7R_{\mu\nu\rho\sigma}^2=0$ (Paper S1 route; S2-C-B).

**CC2008 tail:** $a_{2n}=0$ for $n\ge2$ on round $S^3\times S^1$ — exponential suppression (S2-C-C / S3-f4).

---

## §3. Six-note registry

| Note | Prediction | S2 phase | Sprint upgrade | Status |
|------|------------|----------|----------------|--------|
| **1** | $\kappa_0=3/\sqrt{4\pi}$ | S2-B Step 5 | Janus / Pathway B confluence | **Derived** |
| **2** | $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ | S2-A | J6-n3 / §22.18 | **Derived** |
| **3** | $K(\Phi)=1$; $n_s=0.9685$; $r\sim4\times10^{-3}$ | S2-C-A | J6-D2 identity; hilltop canonical | **Derived** (r: structural) |
| **4** | $M_1=5.40\times10^9$ GeV; $M_R=8.2\times10^{14}$ GeV | S2-D | Companion 10 Pathway $\alpha$ | **Cross-checked** |
| **5** | $\Lambda_{\rm pred}=\Lambda_{a_4}e^{-3N_e}/(2\pi^2)$ | S2-D | Paper S4; Companion 11 | **Closed ~1.05×** |
| **6** | $2\pi^2$ audit: ${\rm Vol}(S^3)$, $V_{\rm lock}$, $\Lambda$ denom | S2-A/R6 | BR2d-J3 heat-kernel | **Derived** |

**Closure $\kappa=\kappa_0/(1-\kappa_0)\approx5.50$:** Pathway A / Janus — **architectural**, not re-derived from bare heat-kernel (honest scope preserved).

---

## §4. Note 5 — Λ closure (post-S2-D)

**Step chain (single computation register):**

1. Unimodular projection removes extensive $f_4a_0\Lambda^4$ mode (§22.15; S2-D).
2. Lock residual $\mathcal{E}_{\rm lock}=\Lambda_{a_4}\sim f_0 a_4$ (S3-f2: $f_0\sim O(1)$ derived).
3. Conditional measure on one comoving cell: $d\mu(V)=\delta(V-V_{\rm lock})dV/V_{\rm lock}$, $V_{\rm lock}=2\pi^2 e^{3N_e}$.
4. $\Lambda_{\rm obs}=\Lambda_{a_4}\,e^{-3N_e}/(2\pi^2)$.

**Numeric (script):** ratio **~1.046 (~1.05×)** — **same $N_e$ as $n_s$** (BR5 discipline: $N_{\rm lock}\neq N_e$).

**Canonical paper:** `Papers/Companion_11_Lambda_Unimodular_Closure_v10_17.md`.

---

## §5. Unified action (J1-G4 × BR2d-J3)

**Single boundary action** at crystallisation (J1-G4):

$$\mathcal{S}_{\rm NTE}^{\rm unified}=\mathcal{S}_{\rm bulk}+\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}$$

| Piece | Heat-kernel form | S2 source |
|-------|------------------|-----------|
| $\mathcal{S}_{\rm cryst}$ | $\int_0^{N_{\rm lock}}[\rho_{\rm surf}+\mu(\mathcal{H}-\alpha|\Phi|^2)+\lambda_{\rm Hopf}\kappa_0 Y_{00}]$ | S2-B + Hopf |
| $\rho_{\rm surf}$ | $f_0 a_4/{\rm Vol}(M)$ | S2-B |
| $\mathcal{S}_{\rm post}$ | $2\pi^2\int dN[\mathcal{L}_{\rm eff}+\mu(H-\alpha|\Phi_{\rm NTE}|^2)]$ | S2-A + Appendix B.3 |
| $\xi=1/6$ | conformal coupling | Paper S1 / S2-C-A |

**Register upgrade:** proof-sketch → **heat-kernel derived** (`Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0`).

---

## §6. D1–D9 Charter map

| ID | Content | Paper S2 closure |
|----|---------|------------------|
| D1 | $\kappa_0$ bare | S2-B ✓ |
| D2 | $T_{\rm GB}$ | S2-A ✓ |
| D3 | $M_1$ prefactor | S2-D cross-check; **D5 tree closed** |
| D4 | $M_R$ Hopf 3:1 | S2-D ✓ |
| D5 | $(8\pi)^{1/3}$ BPS prefactor | **Closed** — tree + factor 1.12 numeric (v0.3) |
| D6 | $\Lambda$ | S2-D + S4 ✓ (~1.05×) |
| D7 | $K(\Phi)$ | S2-C-A ✓ |
| D8 | $V_{\rm NTE}$ / inflation | **Closed** — bulk→boundary $\mathcal{R}_G$; $K(\Phi)=1$ |
| D9 | $\sqrt{2\pi}$ audit | S2-A confluence ✓ |

---

## §7. Honest remaining open

| Item | Register | Route |
|------|----------|-------|
| $(8\pi)^{1/3}$ strict uniqueness | D5 | **Closed** — `Jammer_D5_Factor_112_Numerics_v0_3` |
| $M_2$ explicit | Companion 10 §7 S2-3 | **Closed** — `Jammer_M2_Z2_Split_Derive_v0_1` |
| $N_F\to g_{\rm eff}$ at $T_{\rm GB}$ | ~19% naive gap | **CLOSED** S2-NF1 |
| P0.10 abstract TT on full $A$ | parallel | **SPECIFIED** J2 v0.1 |
| $V_{\rm NTE}$ smooth connection | mechanism | Companion 9 Session 5 |
| AC §22.16 S1–S4 status | authorised | J1 handoff |

---

## §8. Falsifiers

1. Independent Paper S2 computation gives $\beta_{\rm GB}$ inconsistent with $\sqrt{2\pi}/M_{\rm Pl,nr}$ → spine breaks.
2. Smoothed $d\mu(V)$ with $\sigma_N\gtrsim1$ → Λ R6 match fails (S3-f3).
3. $4\pi$ replaces $2\pi^2$ without spectral justification → ~1.64× Λ shift.
4. Heat-kernel $\kappa_0$ ≠ $3/\sqrt{4\pi}$ at bare level → D1 fails.

---

## §9. Working corpus index

| Phase | File |
|-------|------|
| S2-A | `Paper_S2_S2A_Operator_Setup_v0_1.md` |
| S2-B | `Paper_S2_S2B_Coefficients_Plus_Kappa0_v0_1.md` |
| S2-C-A | `Paper_S2_S2CA_KPhi_Closure_v0_1.md` |
| S2-C-B | `Paper_S2_S2CB_a4_Weyl_Euler_v0_1.md` |
| S2-C-C | `Paper_S2_S2CC_DF_Subleading_v0_1.md` |
| S2-D | `Paper_S2_S2D_Lambda_NTE_M1_MR_v0_1.md` |
| S2-E | `Paper_S2_S2E_AC_Integration_Package_v0_1.md` |
| Upgrade | `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0_20260523.md` |
| **This synthesis** | `Paper_S2_Chord_Closure_Synthesis_v1_0_20260524.md` |

---

## §10. Corpus patches authorised (AC)

- §17.5.18: Λ closure ~1.05× (Companion 11 cross-ref)
- §18.3: J6-D2 $n_s$ identity cross-ref
- §22.16: S1–S4 sign-off (J1 stack)
- §22.19: heat-kernel derived + this synthesis
- Paper S2 registry: **main arc COMPLETE**; D5 + M₂ queued

---

— Jammer Paper S2 chord closure, 2026-05-24.
