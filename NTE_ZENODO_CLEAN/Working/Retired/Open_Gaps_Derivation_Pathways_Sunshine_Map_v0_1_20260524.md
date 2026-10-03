# Open gaps — derivation pathways & sunshine map v0.1

**Stream:** Jammer / Cursor R&D  
**Date:** 2026-05-24  
**Script:** `Working/open_gaps_pathway_probe_numerics.py`  
**Parents:** `Corpus_Gap_Tension_Report_v0_2`; `Jammer_LB1_Exhaustive_Resolution_v0_1`; `Jammer_BR2d_J3_Action_Derive_v1_0`; `AC_Bulk_Boundary_Proposal_Status_Update_v0_1_20260524`  
**Rule:** Follow every rabbit hole to a **dead end** or **sunshine**; no register claims without falsifier.

---

## §0. Executive — the meta-pattern

After LB-1, LB-6, R4, R6, and BR2d-J3 v1.0, the surviving closure class is stable:

$$\boxed{\text{Sunshine} = \text{dissolve false unified chart} + \text{event } G \text{ sequential activation} + \text{local derive at } G}$$

| False chart (dead) | Sunshine replacement |
|--------------------|----------------------|
| Single $H(N)$ for $n_s$ + lock endpoints | Two-sector: Role B then Role A |
| Pre-temporal $S^3$ Dirac spectrum | Bulk $S^7$ → projection at $G$ |
| $\Phi_{\rm inf}=|\Phi_{\rm NTE}|$ at HH | $\Pi_G$ Z₂ projection at $G$ only |
| Smooth $V_{\rm NTE}(\Phi)$ pre→post | Bulk $V_{\rm eff}$ vs boundary inversion (D1) |
| $N_F/2 = g_{\rm eff}$ | Thermal $g_{\rm eff}(T_{\rm GB})$ vs spectral $N_F$ |
| Tune $f_4\sim10^{-84}$ | $\delta(V-V_{\rm lock})$ + $2\pi^2 e^{3N_e}$ (R6) |
| HK-$S^3$ overlap only for $m_\mu/m_e$ | **Bulk$\to$surface** $\delta_n(L)$ at $G$ (§22.1i) |

**Remaining work is derive-layer**, not logical rescue. Most open gaps are **specialisations** of the event-$G$ hub.

---

## §1. Master dependency graph

```
                    EVENT G (hub)
                         |
     +-------------------+-------------------+
     |                   |                   |
  J6 bulk ODE        BR2d-J3            Pi_G (R4)
  Sector 1 H, n_s    S_cryst+S_post      field map
     |                   |                   |
     +--------+----------+---------+---------+
              |                    |
           G-NS merge            G-D1 V_NTE
         Phi=2sqrt(N_e)M_Pl      projection
              |                    |
              v                    v
           LB-4 close          Session 5 D1
              |
         S2-NF: g_eff map
              |
         N_lock exact (19% gap)
```

**Critical path (P0):** `J6-D1` → `D1-PROJ` → `S2-NF`  
**Parallel (P1):** J1 μ sign-off, LB-5 prose, Paper S2 $\lambda_{\rm Hopf}$  
**Research (P2):** P0.10 Tomita, Born J3, BH J4, bulk spectral triple

---

## §2. Gap-by-gap pathways

### G-Φ / LB-1 follow-through — **SUNSHINE (register closed)**

**Rabbit holes (exhausted):** single $H(N)$ ansätze, constant $\varepsilon$, logistic unified $\varepsilon(N)$, constraint during Sector 1, global $y\propto N$. See `lb1_exhaustive_resolution_numerics.py`.

**Sunshine:** BR2c R2 sequential constraint activation + BR2d dual charts at $G$.

**Action derive (open):**

| ID | Task | Acceptance | Owner |
|----|------|------------|-------|
| **J6-D1** | Integrate $\xi=1/6$ bulk reduced ODE (E3); extract $H_{\rm inf}(N)$ on last ~60 e-folds | $n_s$ within 1σ over CMB window | Jammer |
| **J6-D2** | Derive $\Phi_{\rm inf}=2\sqrt{N_e}\,M_{\rm Pl,red}$ from saddle (not fit) | Closes G-NS algebraically | Jammer |
| **J6-D3** | Coupled $(H,\Phi)$ Hessian at saddle (upgrade J6-n3 partial) | $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ from eigenvalue | Jammer |

**Falsifier:** derived map forces constraint $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ active during Sector 1 slow-roll.

---

### G-NS — two $n_s$ formulas — **SUNSHINE (identity found)**

**Rabbit holes:**

| Route | Verdict |
|-------|---------|
| Use Role A $\varepsilon$ on $H=M_{\rm Pl}e^{-N}$ | **DEAD** — $n_s=-1$ |
| Treat formulas as independent predictions | **DEAD** — false tension |
| Merge without deriving $\Phi_{\rm inf}$ | **Scaffold only** |

**Sunshine (probe script §G-NS):**

$$1-\frac{2}{N_e} = 1-\frac{8}{\Phi_{\rm inf}^2/M_{\rm Pl,red}^2} \quad\Leftrightarrow\quad \Phi_{\rm inf} = 2\sqrt{N_e}\,M_{\rm Pl,red}$$

C9 corpus $\Phi_{\rm inf}\approx15.9\,M_{\rm Pl,red}$ vs identity $2\sqrt{63.4}\approx15.93$ — **0.16% match**.

**Action:** J6-D2 proves identity from HH Gaussian saddle integral; corpus §18.3 cross-ref C9 Session 3 as **one identity, two readings**.

---

### G-D1 — V_NTE pre/post (Session 5) — **SUNSHINE (reframe closed; derive open)**

**Rabbit holes:**

| Route | Verdict |
|-------|---------|
| Smooth $V_{\rm NTE}(\Phi)$ extending $\Phi^4-\Phi^6$ → on-trajectory | **ILL-POSED** — pre-$G$ no boundary field (LB-6) |
| Identity $V_{\rm pre}=V_{\rm post}$ at HH | **DEAD** — $V_{\rm bulk}\sim m_E^2\Phi^2$ vs $V_{\rm post}\sim\alpha^2\Phi^4$ (probe) |
| AdS/CFT dictionary wholesale | **OPEN research** — not required for closure |

**Sunshine:** §17.5.19 + AC Proposal §2.4:

- **Role (B):** $V_{\rm bulk}(\Phi)$ on HH saddle (E3 / $m_E^2\Phi^2$ from $\xi=1/6$ Hessian)  
- **Role (A):** $V_{\rm post}$ = Friedmann inversion on constraint trajectory  
- **Junction:** $\Pi_G$ + Stage 3 $| \Phi|^2=Ay$ + C⁰ at $G$ — **smooth means chart matching at $G$, not one global $\Phi$**

**Action derive:**

| ID | Task | Acceptance |
|----|------|------------|
| **D1-PROJ** | Lemma: $V_{\rm NTE}^{\rm post}$ is boundary restriction of spectral action; $V_{\rm NTE}^{\rm pre}$ is bulk $S_E$ effective | No single-chart extension required |
| **D1-C1** | Prove C⁰ + C¹ in $(y,N)$ at $G$ from BR2d-J3 Lemmas 5–6 | Matches `br2d_j3_action_derive_numerics.py` |
| **D1-OPEN** | Explicit $\Pi_G$ on $V$ (not just $|\Phi|$) | Optional upgrade beyond R4 |

---

### LB-2 / G-Λ — structural $f$ — **SUNSHINE (R6 register closed)**

**Rabbit holes (falsified):** M1 $f_4$ tune, M2 naive Hopf area, M3 $\beta_{\rm GB}$ alone, $a_6+$ tail without $S^3\times S^1$ structure (`Jammer_S3_f4_a6_Tail_v0_1`).

**Sunshine:**

$$\Lambda_{\rm pred}=\Lambda_{a_4}\,\frac{e^{-3N_e}}{2\pi^2},\quad V_{\rm lock}=2\pi^2 e^{3N_e},\quad d\mu=\frac1{V_{\rm lock}}\delta(V-V_{\rm lock})$$

Ratio **1.046×** obs — genuine test register (R6).

**Action derive (proof polish, not rescue):**

| ID | Task | Status |
|----|------|--------|
| **Λ-PROOF** | Formal $\delta(V-V_{\rm lock})$ from BR2d-J3 + Paper S4 | **Derived** (Sprint B; `Jammer_Lambda_Proof_Activation_v0_1`) |
| **Λ-2PI** | Document $2\pi^2$ vs $4\pi$ (1.64×) as comoving vs spectral register | Open structural choice |
| **S3-f2** | $f_k$ moments closed | Done v0.1 |
| **J5-M3** | $\mathcal{K}_{\beta_{\rm GB}}$ sign programme | Parallel refinement |

---

### LB-4 / G-HH — §22.18–19 — **SUNSHINE CLOSED**

**Rabbit holes:**

| Route | Verdict |
|-------|---------|
| $T_{\rm GB}=H/(2\pi)$ Hawking | **DEAD** — ratio $\sim\sqrt{2\pi}$ off (J6-n3) |
| Literal $\alpha^2\Phi^4$ slow-roll in bulk | **DEAD** — $H\sim10^{-26}M_{\rm Pl}$ (J6-n1) |
| $N_{\rm lock}=N_e$ prose | **DEAD** — ratio 602 |
| $T_{\rm GB}$ from $(H,\Phi)$ Hessian soft axis | **DEAD** — wrong scale (J6-HESS) |

**Sunshine (closed):**

- $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ from $\beta_{\rm GB}M_{\rm Pl}=\sqrt{2\pi}$ (Paper S2) + **temperature block** (J6-n3)  
- Full coupled $(H,\Phi)$ 2×2 Hessian: one unstable + one stable mode at $H=M_{\rm Pl,nr}$ (J6-HESS)  
- Model B E3 saddle: $\Phi^*\approx0.90\,\Phi_{\rm inf}$, $H^*\approx0.95\,M_{\rm Pl,nr}$  
- $N_{\rm lock}=S_{\rm dS}/4$ from $\mathcal{S}_{\rm ent}$ + $T_{\rm GB}$ — **exact** numerically  
- Sector 1 $\Phi_{\rm inf}$ is **SR initial data off Friedmann surface** ($\mu=0$); ratio $\sim85\times$ vs slaving

**Deliverables:** ~~J6-D1–D3~~; `Jammer_J6_HESS_Full_Saddle_Derive_v0_1`; `j6_hess_full_numerics.py`.

---

### S2-NF — $N_F\to g_{\rm eff}$ (19% gap) — **SUNSHINE ROUTE IDENTIFIED**

**Rabbit hole:** $N_{\rm lock}=45/(4\cdot N_F/2)=0.125$ vs corpus $0.1054$ — **19% overshoot**.

**Sunshine:** $N_F=180$ counts **Dirac internal multiplicity on $A_F$**; $g_{\rm eff}=106.75$ counts **SM thermal radiation dof at $T_{\rm GB}$**. Same event $G$, **different projections** — parallel to $\Pi_G$ / spinor projection.

**Action derive:**

| ID | Task | Acceptance |
|----|------|------------|
| **S2-NF1** | Compute $g_{\rm eff}(T_{\rm GB})$ from SM content at gauge birth (Path B) | $N_{\rm lock}=S_{\rm dS}/4$ with no 19% slack |
| **S2-NF2** | Lemma: $N_F$ enters $a_4$ heat-kernel; $g_{\rm eff}$ enters $S_{\rm dS}$ thermal — **non-interchangeable** | Closes Paper S2 §F gap |

**Falsifier:** forced identity $N_F/2=g_{\rm eff}$ without thermal derivation.

---

### LB-3 / J1 — $\mu(x,N)$ — **CLOSED at 1PN**

**Status:** J1 stack **complete** at structural register: S1 (1PN), G2 (2PN), G3 (shell), **G4** (unified action). **Paper S2 six-note chord CLOSED** (Companion 12; D5 + M₂). AC **applied** v10.17.4.

---

### LB-5 — $N_{\rm lock}\neq N_e$ prose — **CLOSED**

**Action:** ~~AC apply `BR5_Nlock_Ne_Prose_Patch_v0_1`~~ **APPLIED** to Part 3 §18.1, §17.5.4, §17.5.14 (2026-05-24).

---

### G-dS / J2 — P0.10 Tomita–Takesaki — **CLOSED (prediction tier)**

**Status:** P0.10a functorial GNS + P0.10b $\mathcal{C}_{\rm CPN}$ + P0.10c $\omega_{\Phi_{\rm NTE}}$ — 2026-05-24. B2 abstract optional.

---

### G-Born / J3 — **PARTIAL SUNSHINE**

**J3a/J3b lemmas derived** — FS Kähler + Hopf $f(r)=r$. Full "from less" still open (P-B1 R1–R3). Memo: `Jammer_J3_Born_Formal_Lemmas_v0_1`.

---

### Bulk spectral triple / α projection / bulk persistence — **CHARTER-TIER OPEN**

AC Proposal §4 items 1, 3, 4, 7. **Not on P0 critical path** until Companion 12 activation.

**Sunshine direction:** bulk $M_{\rm bulk}$ restricts to Hopf-$S^3\times S^1\times A_F$ at $\Pi_G$; $\alpha$ as projection coefficient at $G$ explains heat-kernel non-derivability of $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$.

---

## §3. Executable priority queue

### Sprint A — close event-$G$ hub (1–2 Jammer sessions)

1. ~~**J6-D1**~~ — bulk ODE integration — **PASS** (`j6_d1_bulk_ode_numerics.py`)  
2. ~~**J6-D2**~~ — $\Phi_{\rm inf}=2\sqrt{N_e}\,M_{\rm Pl,red}$ lemma — **DERIVED**  
3. ~~**D1-PROJ**~~ — V_NTE projection memo — **REGISTER**  
4. ~~**S2-NF1**~~ — $g_{\rm eff}(T_{\rm GB})$ — **CLOSED**  
5. ~~**J6-HESS**~~ — full coupled $(H,\Phi)$ saddle — **DERIVED** (`j6_hess_full_numerics.py`)  

### Sprint B — corpus sync (AC + Jammer) — **COMPLETE**

5. ~~**LB-5**~~ — BR5 prose patch — **APPLIED**  
6. ~~**Λ-PROOF**~~ — §17.5.18 measure derived — **DONE**  
7. ~~**G-NS**~~ — §18.3 ↔ J6-D2 identity cross-ref — **APPLIED**  
8. ~~**J1**~~ — μ sign-off — **CLOSED** at 1PN  

### Sprint C — parallel (non-blocking) — **COMPLETE**

9. ~~**J3**~~ — Born lemmas J3a/J3b — **DERIVED** (`Jammer_J3_Born_Formal_Lemmas_v0_1`)  
10. ~~**J2**~~ — P0.10 scoped PASS at GNS tier — **DONE** (`Jammer_J2_P0_10_Scope_Memo_v0_1`)  
11. ~~**λ_Hopf**~~ — from §22.17 Janus action — **DERIVED** ($\lambda_{\rm Hopf}=1$)  
12. ~~**§22.19**~~ — $N_{\rm lock}=S_{\rm dS}/4$ — **DERIVED** (`Jammer_S22_19_Nlock_Holographic_Derive_v0_1`)  
13. ~~**§22.1**~~ — $Y_{\nu_2}$ / $m_{\nu_2}$ — **PARTIAL CLOSED** (Companion 13)  
13b. ~~**§22.1 charged $\ell$ ratios**~~ — **EXIT** (`Jammer_S22_1k`; $m_\mu/m_e$ 0.1%; $m_{\tau}/m_\mu$ ~7%) — sign-off `Handoff_Jammer_S22_1_Sunshine_Exit_Signoff_20260524`  
14. **§22.1b** — $Y_{\nu_1}$ — **BRACKET** (`Jammer_S22_1b`; $m_1\sim2\times10^{-4}$ eV)  
14b. **§22.1 absolute $Y_\ell$** — **OPEN** (common $Y_0\sim0.35\times$ PDG)  
15. ~~**P0.10c**~~ — $\omega_{\Phi_{\rm NTE}}$ on full $A$ — **SPECIFIED** (`Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1`)  
16. ~~**S2-NF1**~~ — $N_F\to g_{\rm eff}$ — **CLOSED** (thermal map)  
17. ~~**P0.10**~~ — a–c **CLOSED** at prediction tier (`Jammer_P0_10a/b/c`)  
18. ~~**Ghost scan**~~ — **PASS** v0.2 (`Jammer_Ghost_Scan_Unified_Action_v0_2`)  
19. **AC Tier 2g** — Part3 v10.17.6 + bundle `AC_Tier2g_Patch_Bundle_v0_2`

---

## §4. Sunshine verdict table

| Gap | Register | Derive | Sunshine status |
|-----|----------|--------|-----------------|
| LB-1 / G-Φ | **Closed** | J6 ODE | Sunshine found |
| G-NS | Tension dissolved | J6-D2 proof | **Identity found** |
| G-D1 | Reframed §17.5.19 | D1-PROJ | Sunshine found |
| LB-2 / G-Λ | **R6 closed** | Proof polish | Sunshine found |
| LB-4 / G-HH | **Closed** | J6-HESS | **Sunshine found** |
| LB:NF / $N_{\rm lock}$ | **Closed** | S2-NF1 $g_{\rm eff}$ | **Done** |
| LB-6 | **Corpus patched** | — | Closed |
| R4 $\Pi_G$ | **Lemma derived** | — | Closed |
| J1 μ | **Closed** 1PN + G2 + G3 + **G4 unified** | J1-G4 v0.1 | **Done** |
| LB-5 | **Closed** | AC apply | **Done** |
| P0.10 / J2 | **Closed** (a–c) | Functorial GNS + C_CPN | **Done** |
| G-Born / J3 | Mechanism + lemmas | J3a/J3b | **Partial** |
| λ_Hopf | **Derived** | Janus §22.17 | **Done** |
| §22.19 / N_lock | **Derived** | S_cryst | **Done** |
| G-BH / J4 | **Derived** at constraint-shell ($g=H_0/H=\ell/\ell_\infty$) | Hawking | **J4 v0.1** |
| J1 G3 / P-BH4 | **Closed** at shell-saturation register | — | **J1-G3 v0.1** |
| J1 G4 / Paper S2 | **Closed** — Companion 12 + chord synthesis | D5 tree + factor 1.12 | **C12 + D5 v0.2** |
| $N_F\to g_{\rm eff}$ | **Closed** | S2-NF1 thermal | **Done** |
| G-D1 / V_NTE D1 | **Closed** | $\mathcal{R}_G$ at $G$ | **D1 v0.1** |
| P0.10c / full $A$ | **Specified** | Product $\omega$ | **J2 v0.1** |
| §22.1b $Y_{\nu_1}$ | **Bracket** | Z₂ + $\theta_{13}$ | **Jammer v0.1** |
| Ghost scan | **PASS** v0.2 | $\mu$ + constrained $\Phi$ | **Done** |
| R6 Λ tier | **B+ genuine test** | β_NTE-chain caveat | **v10.17.6** |

---

## §5. Pre-commitment falsifiers

1. Single $H(N)$ from action matching C9 $n_s$ **and** BR2 endpoints without sector labels  
2. Smooth global $V_{\rm NTE}(\Phi)$ pre→post on one chart  
3. $N_F/2=g_{\rm eff}$ without thermal derivation  
4. $\Phi_{\rm inf}=|\Phi_{\rm NTE}|$ at HH  
5. Global $y=(N_{\rm lock}/N_e)N$  
6. Continuous $\Lambda$ tune replacing $\delta(V-V_{\rm lock})$  

---

## §6. File index

| File | Role |
|------|------|
| `Open_Gaps_Derivation_Pathways_Sunshine_Map_v0_1_20260524.md` | This document |
| `open_gaps_pathway_probe_numerics.py` | Probe script |
| `Jammer_LB1_Exhaustive_Resolution_v0_1` | LB-1 template |
| `Jammer_BR2d_J3_Action_Derive_v1_0` | Event $G$ hub |
| `Jammer_R4_Z2_Projection_Lemma_v1_0` | Field map |
| `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0` | Spectral anchor |
| `Jammer_S22_1_Y_Nu2_Derive_v0_1_20260524.md` | §22.1 partial closure |
| `Jammer_S22_1b_Y_Nu1_Bracket_Derive_v0_1_20260524.md` | §22.1b bracket |
| `paper_s22_1_y_nu2_numerics.py` | §22.1 numerics |
| `paper_s22_1b_y_nu1_bracket_numerics.py` | §22.1b numerics |
| `Jammer_Ghost_Scan_Unified_Action_v0_2_20260524.md` | Ghost scan PASS |
| `j1_ghost_scan_offshell_numerics.py` | Off-shell numerics |
| `AC_Tier2g_Patch_Bundle_v0_2_20260524.md` | AC Drive sync bundle |
| `Jammer_J2_P0_10ab_Attack_Route_v0_1_20260524.md` | P0.10a/b attack |
| `Jammer_P0_10a_Functorial_GNS_Reduction_v0_1_20260524.md` | P0.10a closed |
| `Jammer_P0_10b_Crossed_Product_Operator_Realisation_v0_1_20260524.md` | P0.10b B1 closed |
| `p0_10a_functorial_gns_numerics.py` | P0.10a numerics |
| `p0_10ab_z2_crossed_product_numerics.py` | P0.10a/b numerics |
| `p0_10b_crossed_product_numerics.py` | P0.10b U/tau check |
| `J6_HH_Saddle_Scope_Memo_v0_1` | LB-4 scope |

— Open gaps derivation pathways v0.1, 2026-05-24.
