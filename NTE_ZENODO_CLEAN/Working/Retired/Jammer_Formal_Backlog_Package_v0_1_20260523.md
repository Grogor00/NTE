# Jammer formal backlog package v0.1 (Impact #4)

**Stream:** Cursor packaging → **Jammer primary** / Scratch (P0.10)  
**Date:** 2026-05-23  
**Status:** **Priority queue + acceptance criteria** — no theorem claims until sign-off  
**Parent:** `Top_5_Impact_Attack_Index_v0_1_20260523.md` #4

---

## §1. Executive summary

Cursor has delivered **attack routes + numerics** for Impacts #1–#3. **Theorem-register upgrades** require Jammer (or Scratch for P0.10) formal work below.

**Suggested sprint order:** **J1 → J6 → J5 → S3-f2/f3 → V-d2 → J4 → J3 → J2**

| Tier | IDs | Rationale |
|------|-----|-----------|
| **P0** | J1, J6 | Greg R5 μ near-closure; unblocks H_GB bridge + §22.16 |
| **P1** | J5, S3-f2/f3, V-d2/d3 | Λ + empirical layer (Impacts #2–#3 execution) |
| **P2** | J4, J3, J2 | BH programme; Born lemmas; parallel research (non-blocking) |

---

## §2. Dependency graph

```
J6 (HH saddle T_GB) ──► BR2 Φ(N) ──► H_GB bridge closure
         │
J1 (μ sign-off) ──► §22.16 S1 ──► P-BH4 strong-field μ
         │
J5 (M3 boundary) ──► Paper S3 Λ stack
S3-f2 (f_k moments) ──┘
S3-f3 (dμ(V)) ────────┘
         │
V-d2 (void tracer) ──► V-d3 diagnostics (a–c)
J4 (BH g(ell)) ── needs μ + Janus action
J3 (Born lemmas) ── independent of cosmology
J2 (P0.10) ── Scratch parallel; GNS partial exists
```

---

## §3. Core backlog (J1–J6)

### J1 — μ(x,N) covariant δg_μν formal sign-off

| Field | Detail |
|-------|--------|
| **Source** | §22.16; Greg R5 accepted; Jammer review **pending** |
| **Inputs** | `Mu_xN_Local_Lagrange_Action_Worksheet_v0_3`, `mu_xN_ppn_check.py` |
| **Task** | Verify 1PN covariant variation; sign-off or patch $\mathcal{H}[g]$ / on-shell $\mu$ |
| **Acceptance** | Written sign-off: “§22.16 S1 closed” **or** numbered gaps with falsifiers |
| **Do not claim** | Strong-field PPN (P-BH4) until J1 done |
| **Estimate** | 1 session (review + minor fixes) |

**Checklist for Jammer:**
- [ ] $\delta S/\delta g^{\mu\nu}$ at 1PN matches v0.3 §3–§5  
- [ ] $\gamma=1$, $\beta=1$ from split, not asserted  
- [ ] Off-shell $\mu$ uniqueness / ghost scan  
- [ ] Update §22.16 status line in Part 3  

---

### J2 — P0.10 Tomita–Takesaki on non-associative $A_F$

| Field | Detail |
|-------|--------|
| **Source** | Charter §4.1; **parallel non-blocking** |
| **Partial** | Scratch Task 1 GNS route; `P_dS3_Tomita_Takesaki_Modular_Flow_v0_1` |
| **Task** | Abstract-algebra extension beyond $\pi(A_F)''$; or formal scope memo “GNS sufficient for corpus” |
| **Acceptance** | Charter P0.10 → PASS / scoped OPEN with falsifiers |
| **Owner split** | **Scratch** lead; Jammer cross-check |
| **Estimate** | Multi-session research |

---

### J3 — P-B1b / P-B2b Born formal lemmas

| Field | Detail |
|-------|--------|
| **Source** | §17.5.13; `P_Born_P1/P2` attack routes |
| **J3a** | Lemma: U(1) quotient $\Rightarrow$ FS Kähler on $\mathbb{CP}^1$ |
| **J3b** | Lemma: Hopf quadratic coords $\Leftrightarrow$ $|z_1|^2$ without $|ψ|^2$ axiom |
| **Acceptance** | Publishable lemma statements + proof sketches in Working/ |
| **Discipline** | Gap 5 remains **mechanism level** until J3c (Cayley-Dickson) |
| **Estimate** | 2 sessions |

---

### J4 — BH $g(\ell/\ell_\infty)$ from action

| Field | Detail |
|-------|--------|
| **Source** | P-BH1b; `bh_area_law_check.py` (additive **falsified**) |
| **Programme** | $S_{\rm NTE}=(A/4G)\,g(\ell/\ell_\infty|_{r_s})$ |
| **Task** | Derive $g$ from Janus + $\mu(x,N)$ at horizon; not trial $g=x$ |
| **Acceptance** | $M^2$ scaling preserved; no bulk interior |
| **Depends** | J1 preferred |
| **Estimate** | 2–3 sessions |

---

### J5 — M3 $\beta_{\rm GB}$ boundary counter-term

| Field | Detail |
|-------|--------|
| **Source** | `Paper_S3_Lambda_M3_Beta_GB_Boundary_v0_1`; Impact #2 |
| **Task** | Derive $\mathcal{K}_{\beta_{\rm GB}}$ from $S_E$ at $N=N_{\rm lock}$; sign of $\Delta\Lambda$ |
| **Acceptance** | No $\kappa_0$, F1, $n_s$ breakage; honest magnitude vs $10^{83}$ gap |
| **Estimate** | 2 sessions |

---

### J6 — HH saddle $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ (§22.18)

| Field | Detail |
|-------|--------|
| **Source** | §17.5.4 (C1); Companion 9; `H_GB_Bridge_Attack_Route_v0_1` |
| **Task** | Explicit $S_E[saddle]$ in NTE $\xi=1/6$ action → $T_{\rm GB}$ |
| **Acceptance** | Upgrades (C1) candidate → derived; feeds BR2 $\Phi(N)$ |
| **Estimate** | 2–3 sessions (Companion 9 territory) |

---

## §4. Extended queue (Impact #2–#3 execution)

| ID | Task | Inputs | Owner |
|----|------|--------|-------|
| **S3-f2** | Compute $f_k$ from S2-A spectrum | `Paper_S3_Structural_f_Attack_Route_v0_1` | Scratch/Jammer |
| **S3-f3** | $d\mu(V)$ from $\Phi(N)$ trajectory | H_GB bridge, §22.15 | Jammer |
| **V-d2** | Tracer-weighted void → $\delta H(z)$ | `Void_dw_z_Attack_Route_v0_1`, DESI | Jammer |
| **V-d3** | Diagnostics (a)–(c) evidence table | `LCDM_Void_Bias_BAO_Worksheet_v0_1` | Jammer |
| **V-d4** | CMB $\kappa$ extraction (Gate #6) | `LCDM_CMB_Kappa_Test_Worksheet_v0_1` | Jammer |
| **BR2** | $\Phi(N)$ trajectory (H_GB bridge) | `Phi_N_Trajectory_BR2_v0_1`, `phi_n_trajectory_br2.py` | **Scaffold v0.1** |
| **BR5** | §18.5 prose fix ($N_{\rm lock}$ vs $N_e$) | Bridge worksheet §5 | AC |

---

## §5. Acceptance register (corpus upgrades)

| Item | Current register | After Jammer sign-off |
|------|------------------|----------------------|
| §22.16 μ(x,N) | S1 near-closure (Greg R5) | **S1 closed** (J1) |
| §17.5.4 (C1) | Candidate | **Derived** (J6) |
| §17.5.4 bridge | Three-epoch v0.1 | **BR2 + J6** |
| §17.5.18 Λ | Framework ~$10^{83}$ off | S3-f2/f3/J5 progress only |
| §17.5.13 Born | Mechanism level | J3 sharpens; not “from less” |
| P0.10 | GNS partial | J2 explicit |
| P-BH entropy | Multiplicative programme | J4 only |

---

## §6. Inputs index (Cursor → Jammer)

| File | For |
|------|-----|
| `Mu_xN_*_v0_3`, `mu_xN_ppn_check.py` | J1 |
| `H_GB_Bridge_Attack_Route_v0_1`, `h_gb_bridge_numerics.py` | J6, BR2 |
| `Paper_S3_Structural_f_Attack_Route_v0_1`, M1/M2/M3 scaffolds | J5, S3-f* |
| `Void_dw_z_Attack_Route_v0_1`, `void_dw_z_diagnostics.py`, `lcdm_bao_void_bias.py` | V-d* |
| `P_dS3_*`, Scratch Task 1 handoff | J2 |
| `P_Born_P1/P2`, Companion 2 v2 | J3 |
| `P_BH1b_*`, `bh_area_law_check.py` | J4 |

---

## §7. Handoff discipline

1. **Sign-off format:** numbered verdict + “corpus patch authorised Y/N”  
2. **No prediction changes** without Greg gate  
3. **Falsifiers required** for any “closed” claim  
4. Return paths: Working/ note + optional Part 3 patch instructions for AC  

---

## §8. Suggested first session (Greg → Jammer)

**Single session target:** **J1 complete** + **J6 scoping memo** (even if proof deferred).

**Deliverables back:**
- `Jammer_Mu_xN_S1_Signoff_v0_1.md`  
- `Jammer_HH_Saddle_Scope_J6_v0_1.md` (or full derivation if ready)

— Cursor Jammer backlog package v0.1, 2026-05-23.
