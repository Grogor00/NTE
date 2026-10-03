# J6-n4 / BR2d — $y\leftrightarrow N$ locking junction memo v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Authorisation:** Greg (J6-n4)  
**Script:** `Working/j6_n4_yN_junction_numerics.py`  
**Parents:** BR2c; BR2 v0.1; H_GB bridge v0.1; J6-n1; J6-n3; Stage 3 audit (`17.5.4_Audit_NLock_Derivation.md`); BR5 prose patch

---

## §1. Mission

Specify how **Stage 3 surface-ontology coordinate** $y$ and **cosmological e-fold coordinate** $N$ meet at gauge birth without conflating $N_{\rm lock}\approx0.1$ with $N_e\approx63.4$.

**Deliverables:**

| ID | Output | Status |
|----|--------|--------|
| **BR2d-J1** | Junction event $G$ — dual-chart specification | **Done** |
| **BR2d-J2** | Sector handoff (Role B $\to$ Role A) at $G$ | **Proposed** |
| **BR2d-J3** | Derived map from Appendix B.3 / Paper S2 | **Done v1.0** — `Jammer_BR2d_J3_Action_Derive_v1_0` |
| **R4** | Field magnitude map $\Phi_{\rm inf}\to|\Phi_{\rm NTE}|$ | **Still open** |

---

## §2. Three charts (do not conflate)

| Chart | Symbol | Range | Physical content | Corpus |
|-------|--------|-------|------------------|--------|
| **Surface ontology** | $y$ | $0\to N_{\rm lock}$ | Linear pre-temporal profile; holographic locking **width** | Stage 3 audit §2 |
| **Inflation depth** | $N$ | Sector 1 window + Sector 2 roll | CMB slow-roll + constraint terminal roll | §18.2; BR2c |
| **Emergent time** | $t$ | post-$G$ | $dt = dN/(\alpha|\Phi|^2)$ | §2.3.1 |

**Theorem (register):** $N_{\rm lock}=S_{\rm dS}/4\approx0.105$ and $N_e=-\ln(\alpha M_{\rm Pl})\approx63.4$ are **different coordinates** on the same transition. Ratio $N_e/N_{\rm lock}\approx602$ is **not** a global conversion factor (numerics script §A).

**Falsifier (BR2c §5.4):** Using $N_{\rm lock}$ in place of $N_e$ in §18.2 spectral-tilt counting — **excluded**.

---

## §3. Three sectors at gauge birth (BR2c + bridge)

```
Sector 1 (Role B)     HH slow-roll, unconstrained V_eff
        |   N : last ~60 e-folds (n_s sector)
        v
Sector 2 (Role A)     H = alpha |Phi|^2 terminal roll
        |   N : 0 -> N_e (~63 e-folds)
        v
Event G               gauge birth (simultaneous readings)
        ||  Epoch A: T_GB, H^(F) thermal
        ||  Sector 0: y -> N_lock (Stage 3 profile closes)
        v
Post-G                Lorentzian + SM + Wick-rotated cosmos
```

**J6-n1 / J6-n3 inputs:**

- Sector 1: $n_s$ from saddle-scale $V_{\rm eff}$ (not literal $\alpha^2\Phi^4$).
- Epoch A: $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ (J6-n3 derived-at-simplified-$S_E$).
- $\ln(H^{(F)}/H^{(\alpha)})\approx N_e+1\approx64.4$ at $G$ (bridge numerics).

---

## §4. Junction event $G$ (BR2d-J1)

**Definition.** Gauge birth is a **single physical event** described by **two chart endpoints simultaneously**:

| Reading | $y$-chart | $N$-chart |
|---------|-----------|-----------|
| Coordinate | $y=N_{\rm lock}$ | $N=N_e$ (Role A lock end) |
| $|\Phi|$ | $|\Phi|_y=\Phi_0 e^{-N_{\rm lock}/2}$ (linear profile) | $|\Phi|_N=M_{\rm Pl,nr}$ (constraint) |
| $H$ (Role A) | — | $H^{(\alpha)}=\alpha M_{\rm Pl}^2$ |
| Thermal | $T_{\rm GB}$ | $H^{(F)}=\mathrm{Friedmann}(T_{\rm GB})$ |
| Topology | Wick kink (C¹ in $y$) | Lorentzian continuation |

**No global map** $y=f(N)$ with constant $f'(N)=N_{\rm lock}/N_e$ is asserted. Charts are **orthogonal projections** of $G$ until BR2d-J3 derives $f$ from boundary action.

### §4.1 Local C⁰ matching (Stage 3 $\to$ Sector 2)

Stage 3 linear profile (audit §2):

$$|\Phi|^2(y)=\frac{\Phi_0^2 e^{-N_{\rm lock}}}{N_{\rm lock}}\,y$$

At $y=N_{\rm lock}$: $|\Phi|_y=\Phi_0 e^{-N_{\rm lock}/2}$.

Sector 2 at $N=N_e$: $|\Phi|_N=M_{\rm Pl,nr}$ (BR2 exponential endpoints).

**Numeric (script §C):** With $\Phi_0=M_{\rm Pl,nr}$, relative mismatch $|\Phi|_y/|\Phi|_N-1|\approx5\%$. **C⁰ match** achievable with $\Phi_0\approx1.05\,M_{\rm Pl,nr}$ — **calibration**, not yet derived from $S_E$.

**Register:** C⁰ continuity of $|\Phi|^2$ at $G$ is **plausible**; **derived** only after BR2d-J3.

### §4.2 C¹ / Wick structure (unchanged corpus)

At $y=N_{\rm lock}$: Stage 3 audit — $dz/dy$ finite $\to$ post-locking jump (F2 Wick rotation). This is **not** a condition on cosmological $N$; it lives on the $y$-chart only.

---

## §5. Sector handoff BR2d-J2 (Role B $\to$ Role A)

**Proposal (default register):**

1. **Sector 1 ends** when slow-roll inflaton (Role B) exits observation window — **before** constraint slaving dominates $n_s$.
2. **Sector 2 begins** when $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ is **enforced** as holonomic constraint for terminal roll to $H^{(\alpha)}$.
3. **At $G$:** constraint sector reaches $|\Phi|=M_{\rm Pl,nr}$; thermal bath (Epoch A) is **simultaneous** reading on $H^{(F)}$ axis; Stage 3 profile reaches $y=N_{\rm lock}$.

**Not claimed:** Role B inflaton field **equals** Role A $|\Phi_{\rm NTE}|$ in magnitude. J6-n1 / numerics §E: $\Phi_{\rm inf}/|\Phi_{\rm NTE}(0)|\sim10^{-13}$.

**R4 routes (still open):**

| Route | Mechanism | Verdict |
|-------|-----------|---------|
| **R4a — Z₂ portal** | Same underlying d.o.f., two **readings** at $G$ | **Preferred programme** |
| **R4b — Sequential activation** | Constraint switches on; Sector 1 decouples | **Default for BR2c** |
| **R4c — Magnitude identity** | $\Phi_{\rm inf}=|\Phi_{\rm NTE}|$ | **Excluded** (BR2c numerics) |

---

## §6. BR2d-J3 — derived map (programme)

**Target:** Derive $f$ in $y=f(N)$ (or junction relation) from Appendix B.3 Lagrange-multiplier boundary action + Paper S2 geometry (Hopf-$S^3\times S^1_\beta$).

**Success criteria:**

1. C⁰ $|\Phi|^2$ match at $G$ **without** ad hoc $\Phi_0$ tuning.
2. $N_{\rm lock}=S_{\rm dS}/4$ from $H^{(F)}$ only; $N_e$ from $H^{(\alpha)}$ only — **same event**, different projections (§22.19 parallel).
3. Sector 1 $H(N)$ from J6 action **continuous** with Stage 3 endpoint in appropriate chart.

**Owner:** Jammer + Paper S2 / Scratch heat-kernel lane.

---

## §7. Timeline diagram (ASCII)

```
Janus          Stage 3 (y)         HH peak        Sector 1 (N)      Sector 2 (N)         G
y=0            y in (0,N_lock)     N=0            N slow-roll       N: 0 -> N_e        y=N_lock
|Phi|=0        linear profile      H~M_Pl         Role B n_s        Role A roll        N=N_e
               z(y) linear         |Phi|_A huge   Phi_inf~16 M_Pl   |Phi|-> M_Pl        T_GB, H^(F)
                                                                                      Wick kink
```

---

## §8. Verdict

| Claim | Status |
|-------|--------|
| $N_{\rm lock}\neq N_e$ as coordinates | **Theorem** (register) |
| Junction $G$ dual-chart specification | **Done** (BR2d-J1) |
| Global $y\leftrightarrow N$ linear map | **Rejected** |
| Local C⁰ $|\Phi|$ match at $G$ | **Candidate** ($\Phi_0\sim1.05 M_{\rm Pl,nr}$) |
| Sector handoff sequential activation | **Proposed** (BR2d-J2) |
| R4 field map | **Open** |
| Derived map BR2d-J3 | **Programme** |

**Corpus patch authorised:** **Y** — pointer block for §17.5.4 / §22.19 / BR5 (coordinate discipline); **no prediction change**.

**Suggested AC insert (after BR5 patch):**

> **BR2d (Jammer J6-n4, 2026-05-23):** Gauge birth is event $G$ with **dual charts** $y=N_{\rm lock}$ and $N=N_e$; no global identification $y\propto N$. Stage 3 C⁰ matching and Sector 2 constraint endpoints align at $G$ with $\Phi_0\sim M_{\rm Pl,nr}$. See `Working/Jammer_J6_n4_BR2d_Locking_Junction_Memo_v0_1_20260523.md`.

---

## §9. Cross-references

- `Phi_N_Trajectory_BR2c_Attack_Route_v0_1`; `BR5_Nlock_Ne_Prose_Patch_v0_1`
- `Jammer_J6_n1_*`; `Jammer_J6_n3_*`
- §17.5.19 (three-role / two-sector); §22.18–§22.19

— Jammer J6-n4 / BR2d v0.1, 2026-05-23.
