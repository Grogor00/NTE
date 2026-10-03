# J1-G4 — Paper S2 unified boundary action v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **G4 closed at structural-unification register** — full heat-kernel single computation **open polish**  
**Script:** `Working/j1_g4_unified_action_numerics.py`  
**Parents:** J1 S1/G2/G3; BR2d-J3; §17.5.15; §22.16; Appendix B.3; Paper S2 scope

---

## §0. Executive

| Gap | Verdict |
|-----|---------|
| **G4** — μ + $\xi=1/6$ bare sector in **one action** | **Closed at structural register** |
| Paper S2 single Seeley–DeWitt computation (D1–D9) | **Open polish** — coefficients not all from one heat trace yet |
| Off-shell ghost scan | **PASS** v0.2 (`Jammer_Ghost_Scan_Unified_Action_v0_2`) |

**Headline.** Local $\mu(x,N)$ (§22.16) and conformal coupling $\xi=1/6$ (§17.5.15) are **not independent bolt-ons**. They are sectors of one **post-gauge-birth boundary action** $\mathcal{S}_{\rm NTE}^{\rm unified}$, whose phase limits reproduce BR2d-J3 ($\mathcal{S}_{\rm bulk}+\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm post}$), Mu worksheet v0.3, and Appendix B.3.

---

## §1. Problem (G4 from J1 sign-off)

J1 closed S1 (1PN), G2 (2PN), G3 (shell). **G4** asked:

> Single boundary action unifying $\mu(x,N)$ with bare-action conformal coupling at Paper S2 level.

Corpus §22.16 / §17.5.3 listed this as open. BR2d-J3 gave **three-phase** split but not the **single Lorentzian functional** for post-$G$ physics.

---

## §2. Unified post-$G$ action (primary deliverable)

**Manifold:** post-crystallisation Lorentzian $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$ (Path B; $\Phi_{\rm NTE}\neq$ SM Higgs).

$$\boxed{
\mathcal{S}_{\rm NTE}^{\rm unified}=\int d^4x\sqrt{-g}\,\Big[
\frac{M_{\rm Pl}^2}{2}R+\mathcal{L}_{\rm SM}+\mathcal{L}_\Phi[\xi]+\mu(x)\,\big(\mathcal{H}[g]-\alpha|\Phi_{\rm NTE}|^2\big)
\Big]
}$$

**Scalar sector (§17.5.15):**

$$\mathcal{L}_\Phi[\xi]=-\frac12 g^{\mu\nu}\nabla_\mu\Phi_{\rm NTE}\nabla_\nu\Phi_{\rm NTE}-V_{\rm NTE}(\Phi_{\rm NTE})-\frac{\xi}{2}\,R\,|\Phi_{\rm NTE}|^2, \qquad \xi=\frac16$$

**Constraint sector (§22.16; Mu v0.3):**

$$\mathcal{H}[g]=H_0\sqrt{\frac{-g_{00}}{(-g_{00})_\infty}}, \qquad \delta_\mu:\;\mathcal{H}=\alpha|\Phi_{\rm NTE}|^2$$

**Discipline.**

- $\mu$ is **holonomic** Lagrange multiplier — not an independent propagating DOF (J1).  
- $\xi R|\Phi|^2$ is **bare** non-minimal coupling — **not** the driver of cosmological $|\Phi|$ trajectory (Appendix B Fork B closed; $\mu$ enforces $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$).  
- SM Higgs sector **orthogonal** (Path B §2.3.0).

---

## §3. Phase limits → BR2d-J3 (unification theorem)

| Phase | Limit of $\mathcal{S}_{\rm NTE}^{\rm unified}$ | BR2d-J3 piece |
|-------|-----------------------------------------------|---------------|
| **Bulk** (pre-$G$, Euclidean) | $\mu\to0$; Wick rotate; $V_{\rm bulk}(\Phi)$ from HH sector | $\mathcal{S}_{\rm bulk}$ |
| **Cryst** ($y\in[0,N_{\rm lock}]$) | Thin shell: surface $\rho_{\rm surf}$ + $\mu(y)$ activation + $\mathcal{S}_{\rm ent}$ | $\mathcal{S}_{\rm cryst}+\mathcal{S}_{\rm ent}$ |
| **Post** ($N$ chart, $V_3=2\pi^2$) | Homogeneous $H(N),\Phi(N)$; $\mu(N)\neq0$ | $\mathcal{S}_{\rm post}$ |

**Theorem 1 (BR2d-J3 recovery).** BR2d-J3 three-phase action is the **gauge-birth factorisation** of $\mathcal{S}_{\rm NTE}^{\rm unified}$ — not a second action principle.

**Proof sketch.** Lemma 1 BR2d-J3: bulk variation with $\mu=0$ is $\mathcal{S}_{\rm bulk}$ integrand. Lemma 2: $\delta\mu=0$ on post support is $\mathcal{S}_{\rm post}$ constraint. Cryst is the **activation locus** where $\mu$ switches from $0$ to on-shell values (sequential constraint, LB-1).

---

## §4. Reduction theorems (J1 stack)

| Limit | Result | Source |
|-------|--------|--------|
| Static weak field, on-shell $\mu$ | Mu v0.3; $\gamma=\beta=1$ | **J1 S1** |
| $\mathcal{O}(\Phi_N^2)$ vacuum exterior | Shapiro / perihelion = GR | **J1-G2** |
| Shell $r\approx r_s$ | Saturation + J4 $x=2$ | **J1-G3** |
| Homogeneous FRW | Appendix B.3 $\mu(N)$ | **Corpus B.3** |

**Theorem 2 (no double constraint).** One $\mu$ enforces **one** holonomic constraint; $\xi R|\Phi|^2$ modifies **bare** EH variation but does **not** add a second $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ (Fork B excluded — Part 3 §17.5.3).

---

## §5. $\xi=1/6$ ↔ bulk saddle (Paper S2 / J6-n3 link)

At HH saddle with $R=12H^2$ (de Sitter patch):

$$m_E^2=\xi R=\frac{1}{6}\cdot 12 H^2=2H^2$$

Matches J6-n3 / Companion 9 scalar block — **same** $\Phi$ and **same** $\xi$ as $\mathcal{L}_\Phi[\xi]$ in $\mathcal{S}_{\rm NTE}^{\rm unified}$.

**Numeric (script):** $m_E^2/H^2=2.000$ at $\xi=1/6$, $R=12H^2$.

---

## §6. Relation to Paper S2 scope

| Paper S2 deliverable | G4 status |
|---------------------|-----------|
| Single heat-kernel on Hopf-$S^3\times S^1\times A_F$ | **Action identified** — coefficients partially derived (S2-A–D arc) |
| D1–D9 numerical closure from **one** trace | **Open polish** |
| $\mu$ vs $\xi$ separate | **Closed** — one functional |

**Honest scope.** G4 closes **structural unification** (one action, correct phase limits). It does **not** claim Paper S2's full single-computation deliverable is complete.

---

## §7. Falsifiers

| ID | Test |
|----|------|
| F1 | Bulk requires $\mu\neq0$ for HH saddle | **Pass** (J6-n1 Track A) |
| F2 | Fork B: $\xi R|\Phi|^2$ drives cosmological $|\Phi|$ trajectory | **Pass** — $\mu$ enforces constraint |
| F3 | Two independent $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ mechanisms | **Pass** — one $\mu$ |
| F4 | Paper S2 heat trace yields $\xi\neq1/6$ at leading order | **Future** — would falsify §17.5.15 |

---

## §8. Corpus patches authorised

**§22.16 status (AC):**

> **S1 @ 1PN; S2 @ 2PN; S3 @ shell; S4 @ structural unification (Jammer J1-G4 v0.1, 2026-05-24).** Unified action $\mathcal{S}_{\rm NTE}^{\rm unified}$; Paper S2 single heat-kernel polish **open**.

**§17.5.3 / §17.5.15 cross-pointer:** add unified action reference.

**Corpus patch authorised:** **Y**

---

## §9. Cross-references

- `Jammer_BR2d_J3_Action_Derive_v1_0_20260523.md`  
- `Mu_xN_Local_Lagrange_Action_Worksheet_v0_3_20260523.md`  
- `Jammer_J1_G2_2PN_Metric_Derive_v0_1_20260524.md`  
- `Jammer_J1_G3_P_BH4_StrongField_Derive_v0_1_20260524.md`  
- `Paper_S2_Scope_and_Attack_Route_v0_1_20260523.md`  
- `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0_20260523.md`

---

— Jammer J1-G4 v0.1, 2026-05-24.
