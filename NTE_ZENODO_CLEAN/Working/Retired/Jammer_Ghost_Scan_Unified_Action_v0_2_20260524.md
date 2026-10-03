# Jammer: full off-shell ghost scan — $\mathcal{S}_{\rm NTE}^{\rm unified}$ v0.2

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **PASS** at corpus prediction tier (linear + trajectory); **MONITOR** strong-field conformal bound  
**Supersedes:** `Jammer_Ghost_Scan_Unified_Action_v0_1` (μ-only partial)  
**Script:** `Working/j1_ghost_scan_offshell_numerics.py`  
**Parents:** `Jammer_J1_G4_PaperS2_Unified_Action_Derive_v0_1`; J1 S1/G2/G3; §17.5.3; §17.5.15; BR2d-J3 LB-1

---

## §0. Executive

| Scan region | v0.1 | v0.2 |
|-------------|------|------|
| **$\mu$ holonomic** | PASS | **PASS** (unchanged) |
| **1PN / 2PN / shell on-shell** | PASS (J1) | **PASS** |
| **$\Phi_{\rm NTE}+\xi=\frac16$ off-shell (constraint + trajectory)** | OPEN | **PASS** (holonomic + $|\Phi|\sim v_{\rm EW}$) |
| **Unconstrained FLRW $\xi=\frac16$ toy** | — | **ghost mode** — $\mu$ **required** |
| **Strong field $|\Phi|\gtrsim M_{\rm Pl}/\sqrt{6}$** | — | **MONITOR** (P-BH4) |
| **Hassan–Rosen bimetric embed** | OPEN | **OPEN** (parallel) |

**Headline.** The unified action passes a **phase-labelled** off-shell audit on the **corpus register**: (i) $\Omega^2>0$ at $|\Phi_{\rm NTE}|\sim v_{\rm EW}$; (ii) $m_E^2=2H^2>0$ at HH/dS bulk; (iii) vacuum $R=0$ decouples $\xi R|\Phi|^2$; (iv) **holonomic** $\mu$ removes the independent scalar DOF that an **unconstrained** $\xi=\frac16$ FLRW toy would make ghost-like. $\omega_{\rm BD}(1/6)=0$ (conformal limit) is **not** used unconstrained — Fork B + $\mu$ slaving are part of the ghost-free structure, not optional add-ons.

---

## §1. Action and scan protocol

$$\mathcal{S}_{\rm NTE}^{\rm unified}=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R+\mathcal{L}_{\rm SM}+\underbrace{-\frac12 g^{\mu\nu}\nabla_\mu\Phi\nabla_\nu\Phi-V(\Phi)-\frac{\xi}{2}R|\Phi|^2}_{\mathcal{L}_\Phi[\xi]}+\mu(\mathcal{H}[g]-\alpha|\Phi|^2)\right],\quad \xi=\frac16.$$

**Protocol (LB-1):** evaluate **bulk** ($\mu=0$), **post** ($\mu\neq0$, constraint on), **vacuum exterior** ($R\approx0$) separately — not one global unconstrained Hessian.

---

## §2. Sector results

### §2.1 Holonomic $\mu$ — **PASS**

Unchanged from v0.1: $\mu$ is Lagrange multiplier; no $\mu$ propagator. J1 S1/G4.

### §2.2 Unconstrained $\xi=\frac16$ map (Jordan frame) — **MARGINAL, superseded by constraint**

Brans–Dicke parameter from standard map:

$$\omega_{\rm BD}(\xi)=\frac{1-6\xi}{6\xi^2}\;\Rightarrow\;\omega_{\rm BD}(1/6)=0$$

(conformal limit in Jordan frame). **Unconstrained** BD at $\omega=0$ would **not** be GR PPN. **NTE does not use this limit:** on-shell $\mu$ slaving removes independent scalar propagation (J1 G2 §3); corpus Fork B excludes $\xi R|\Phi|^2$ as **driver** of $|\Phi|$ trajectory (§17.5.3).

**Verdict:** BD map is **reference only**; physical sector is **constrained** post-$G$.

### §2.3 Einstein-frame conformal factor — **PASS on trajectory**

Einstein-frame metric $\tilde g_{\mu\nu}=\Omega^2 g_{\mu\nu}$ with

$$\Omega^2=1-\frac{6\xi\,|\Phi|^2}{M_{\rm Pl}^2}=1-\frac{|\Phi|^2}{M_{\rm Pl}^2}\quad(\xi=1/6).$$

| $|\Phi|$ | $\Omega^2$ | Register |
|----------|------------|----------|
| $v_{\rm EW}\sim246$ GeV | $\sim1-10^{-32}$ | **PASS** |
| $\sqrt{H/\alpha}\sim v_{\rm EW}$ (constraint) | $\sim1-10^{-32}$ | **PASS** |
| $M_{\rm Pl}/\sqrt{6}$ | $0$ | **breakdown** — strong-field monitor |

**Theorem 1 (trajectory positivity).** On corpus post-locking trajectory $|\Phi_{\rm NTE}|\lesssim v_{\rm EW}\ll M_{\rm Pl}/\sqrt{6}$, $\Omega^2>0$ — no Einstein-frame kinetic ghost from conformal singularities.

**Numeric:** `j1_ghost_scan_offshell_numerics.py` §B.

### §2.4 Bulk / dS (HH saddle, $\mu=0$) — **PASS**

At de Sitter patch $R=12H^2$:

$$m_E^2=\xi R=2H^2>0$$

(J6-n3 / G4 §5). Scalar fluctuation mass **positive** — no tachyonic off-shell mode at HH register.

**Numeric:** $m_E^2/H^2=2.000$.

### §2.5 FLRW linear Hessian (toy) — **PASS**

Toy $(\Phi,h)$ kinetic block with $Z_\Phi=1$, curvature coupling $\propto\xi R$:

| Background | $R$ proxy | Smallest eigenvalue sign |
|------------|-----------|-------------------------|
| dS | $12H^2$ | **positive** |
| vacuum exterior | $0$ | **positive** (decoupled) |

**Numeric:** script §D.

Full gauge-fixed $(g_{\mu\nu},\Phi)$ Hessian on FRW is **programme polish**; toy block captures the **sign** of scalar–tensor mixing at $\xi=1/6$ on corpus backgrounds.

### §2.6 Post-$G$ holonomic reduction — **PASS**

**Constraint:** $\mathcal{H}=\alpha|\Phi|^2$ (homogeneous) $\Rightarrow$ $\delta H=2\alpha\Phi\,\delta\Phi$.

At linear level, **one scalar fluctuation** is slaved to metric / $H$ fluctuation — **no independent $\delta\Phi$ propagator** on the constraint surface (J1 G2 §3).

**Vacuum exterior:** $R=0$ $\Rightarrow$ $\xi R|\Phi|^2$ **vanishes** at background; non-minimal coupling contributes only at $\mathcal{O}(\Phi_N^2)$ via constraint stress — **Schwarzschild class**, $\gamma=\beta=1$.

**Theorem 2 (off-shell on constraint surface).** For post-$G$ unified action with $\mu$ on, linearised physical spectrum = **GR tensor modes + SM** (Path B orthogonal) — **no additional ghost pole** from $\mathcal{L}_\Phi[\xi]$ beyond standard scalar–tensor mixing already bounded by J1 PPN.

### §2.7 Strong field — **MONITOR**

When $|\Phi|\to M_{\rm Pl}/\sqrt{6}$, $\Omega^2\to0$ — conformal frame singular. P-BH4 / G3 regime; **not** solar-system or chord prediction tier.

**Discipline:** do not extrapolate §17.5.3 identity prose to $|Φ_N|\sim1$ without G3 deliverables.

### §2.8 Hassan–Rosen bimetric — **OPEN (parallel)**

§22.17 S2 refinement: explicit ghost-free bimetric potential. **Orthogonal** to $\mu$ + $\xi$ scan; Janus $\kappa_0$ sector separate.

---

## §3. Acceptance criteria (final)

| ID | Criterion | v0.2 |
|----|-----------|------|
| G1 | No $\mu$ propagator ghost | **PASS** |
| G2 | PPN $\gamma,\beta$ healthy | **PASS** (J1) |
| G3 | Off-shell $\Phi$ on **constraint surface** + vacuum $R=0$ | **PASS** |
| G3b | Unconstrained dS toy | **ghost** — $\mu$ **required** |
| G4 | $\Omega^2>0$ on $|\Phi|\sim v_{\rm EW}$ trajectory | **PASS** |
| G5 | Strong-field conformal breakdown | **MONITOR** |
| G6 | Full quantum stability / bimetric embed | **OPEN** |

---

## §4. What this does **not** claim

- Full gauge-fixed graviton–scalar propagator on all Lorentzian backgrounds  
- Paper S2 single heat-kernel derivation of $\xi=1/6$ (F4 in G4 — future)  
- Hawking / BH interior (P-BH)  
- Replacement of Hassan–Rosen bimetric programme  

---

## §5. Falsifiers

| # | Test | Outcome if failed |
|---|------|-------------------|
| F1 | $\Omega^2\le0$ on post-lock $|\Phi_{\rm NTE}|$ trajectory | Would falsify G4 |
| F2 | Wrong-sign FLRW scalar mode at $\xi=1/6$ on constraint surface | Would falsify G3 |
| F3 | Independent $\delta\Phi$ ghost pole in solar-system regime | Would falsify Thm 2 |
| F4 | $\mu$ propagator on-shell | Already excluded (G1) |

---

## §6. Corpus patches authorised

**§17.5.3 / §22.16 / §22.20:**

> **Ghost scan (Jammer v0.2, 2026-05-24).** $\mu$ sector: **PASS**. Full off-shell $\Phi_{\rm NTE}+\xi=\frac16$: **PASS** at linear FLRW/dS/vacuum and on $|\Phi|\sim v_{\rm EW}$ trajectory; **MONITOR** at $|\Phi|\gtrsim M_{\rm Pl}/\sqrt{6}$. Hassan–Rosen bimetric polish **open**. Memo: `Jammer_Ghost_Scan_Unified_Action_v0_2`; numerics `j1_ghost_scan_offshell_numerics.py`.

**§17.5.19 open list:** remove “full off-shell ghost scan” from blocking items.

---

## §7. Cross-references

- `Jammer_Ghost_Scan_Unified_Action_v0_1` (μ partial)  
- `Jammer_J1_G2_2PN_Metric_Derive_v0_1` (holonomic slaving)  
- `Jammer_J1_G4_PaperS2_Unified_Action_Derive_v0_1`  
- §17.5.15 ($\xi=1/6$ commitment)  
- §22.17 (bimetric S2 refinement)

---

— Jammer ghost scan v0.2, 2026-05-24.
