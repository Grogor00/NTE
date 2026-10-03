# V_NTE D1 — ρ_eff from candidate V_NTE vs Friedmann (P1 genuine test)

**Stream:** Cursor execution (Jammer D1 handoff)  
**Date:** 2026-05-23 (v0.1)  
**Status:** **Numerics complete** — magnitude tautology confirmed; **w-scaling mismatch** is the genuine diagnostic  
**Script:** `Working/lcdm_vnte_rho_eff_numerics.py`  
**Lineage:** Jammer P1 review §1.3–§1.5; Companion 9 Session 5; Gate #2 canonical ρ_eff reading

---

## §1. Setup (Session 5 / Companion 8 F3)

Total H-sourcing density:

$$\rho_{\rm eff} = \tfrac{1}{2} K(\Phi)\,\dot\Phi^2 + V_{\rm NTE}(\Phi)$$

Constraint + Friedmann:

$$H = \\beta_{\\mathrm{NTE}}|\Phi|^2,\qquad H^2 = \frac{8\pi G}{3}\,\rho_{\rm eff}$$

Inverting (with $8\pi G = 1/M_{\rm Pl}^2$):

$$V_{\rm NTE}(\Phi,\dot\Phi) = 3\alpha^2 M_{\rm Pl}^2 \Phi^4 - \tfrac{1}{2} K(\Phi)\,\dot\Phi^2$$

**Trajectory (canonical ΛCDM, not working-profile $e^{-N}$):**

$$|\Phi|^2 = v_{\rm EW}^2 \cdot \frac{H(N)}{H_0},\qquad
\frac{H(N)}{H_0} = \sqrt{\Omega_r e^{-4N}+\Omega_m e^{-3N}+\Omega_\Lambda}$$

**Constants:** $\alpha = 2.38\times10^{-47}\,\mathrm{GeV}^{-1}$, $v_{\rm EW}=246\,\mathrm{GeV}$, $M_{\rm Pl}=2.435\times10^{18}\,\mathrm{GeV}$, Planck 2018 $\Omega$'s, $K(\Phi)=1$ (S2-E canonical).

**Friedmann target:** $\rho_{\rm FRI} = 3H^2/(8\pi G) = 3H^2 M_{\rm Pl}^2$.

---

## §2. Candidate V_NTE forms tested

| ID | Form | Motivation |
|----|------|------------|
| **C0** | $3\alpha^2 M_{\rm Pl}^2\Phi^4 - \tfrac{1}{2}K\dot\Phi^2$ | Friedmann inversion (control) |
| **E1** | $3\alpha^2 M_{\rm Pl}^2\Phi^4$ | Companion 9 extension E1; F3 leading term |
| **E2** | E1 $-\ (\alpha^2/8)\Phi^6$ | F3 post-locking on-trajectory (10a) |
| **E3** | E1 $-\ (\alpha^2 A^2/8)\Phi^2$ | F3 pre-temporal on-trajectory (10b); $A=\|\Phi\|^2/N_{\rm lock}$ at lock |
| **Hilltop** | = E2 globally | Session 4 smooth $\Phi^4-\Phi^6$ connection |
| **Anchor** | E2 + $\lambda(\Phi^2-v_{\rm EW}^2)^2$ | F3 (V1'-min) illustrative |

---

## §3. Magnitude test — ρ_VNTE vs ρ_FRI

| Epoch | N | $\Phi/v_{\rm EW}$ | $\rho_{\rm VNTE}/\rho_{\rm FRI}$ (E1) | kin/$\rho_{\rm FRI}$ |
|-------|---|-------------------|--------------------------------------|----------------------|
| Today ($\Lambda$) | 0 | 1.00 | **1.000** | $9.5\times10^{-35}$ |
| Matter–$\Lambda$ equality | −0.26 | 1.08 | **1.000** | $2.8\times10^{-34}$ |
| DESI BAO ($z\sim0.5$) | −0.41 | 1.15 | **1.000** | $4.7\times10^{-34}$ |
| Matter-dom ($z\sim19$) | −3.0 | 7.12 | **1.000** | $4.9\times10^{-32}$ |
| BBN (radiation) | −20.7 | $9.7\times10^7$ | **1.000** | $1.6\times10^{-17}$ |

**All candidates (E1–E3, hilltop, anchor): ratio = 1.000 to machine precision** — subleading E2/E3 terms $<10^{-20}\,\rho$ on post-locking trajectory ($\Phi \ll M_{\rm Pl}$).

### §3.1 Reading (magnitude)

**Confirms Jammer P1 §1.3:** On the §2.3.1 trajectory + §2.4.3 calibration, **E1 quartic equals $\rho_{\rm FRI}$ identically** because $V_{\rm leading} = 3\alpha^2 M_{\rm Pl}^2\Phi^4 = 3H^2 M_{\rm Pl}^2$ under $H=\alpha\Phi^2$. Kinetic fraction is negligible ($\lesssim10^{-17}$ even at BBN). **This is the tautological relabelling layer — not an independent empirical pass.**

---

## §4. Genuine test — equation-of-state / thermal scaling

If $\rho_{\rm eff}=\rho_{\rm total}$ is carried by a single $V_{\rm NTE}(\Phi)$ scalar, **scalar thermodynamics** must reproduce the **thermal-history split**:

| Epoch | Dominant component | $w_{\rm LCDM}$ (Ω-weighted) | $w_{\rm scalar}$ (E1) | Mismatch |
|-------|-------------------|----------------------------|----------------------|----------|
| Today | mixed | −0.685 | **−1.000** | −0.315 |
| Matter–$\Lambda$ eq. | mixed | −0.500 | **−1.000** | −0.500 |
| DESI BAO | mixed | −0.391 | **−1.000** | −0.609 |
| Matter-dom | matter | **0.000** | **−1.000** | **−1.000** |
| BBN | radiation | **+0.333** | **−1.000** | **−1.333** |

Scalar pressure: $p = \tfrac{1}{2}\dot\Phi^2 - V$; with $V \gg \tfrac{1}{2}\dot\Phi^2$ everywhere post-locking, **$w_{\rm scalar} \approx -1$ at all epochs**.

### §4.1 Reading (genuine test)

1. **Magnitude scaling across eras passes** only because $|\Phi|$ is **slaved to $H(N)$** — not because $V_{\rm NTE}=\Phi^4$ dynamically sources radiation/matter/Λ fractions.

2. **Thermal split fails:** At BBN the universe is radiation-dominated ($w=1/3$); E1 gives $w=-1$. At matter-domination ($w=0$); E1 gives $w=-1$. **No independently-motivated global $V(\Phi)$ in the corpus reproduces the Ω_r / Ω_m / Ω_Λ pressure hierarchy.**

3. **Gate #2 canonical reading preserved:** Ω_m, Ω_r, Ω_Λ are **ΛCDM bookkeeping chart** for the same $H(N)$; SM radiation/matter + geometric Λ unloading carry the **thermal content**. $V_{\rm NTE}$ is **consistency layer** (Appendix B Lagrange multiplier), not a single-fluid replacement for SM+Λ.

4. **Session 5 D1 still open for:** (α) boundary-action-derived $V(\Phi)$ off-trajectory; (β) $K(\Phi)\neq1$ from Connes programme; (γ) smooth pre/post connection that changes **inflation** sector without fixing post-locking $w$ mismatch above.

---

## §5. What would falsify / close

| Outcome | Implication |
|---------|-------------|
| $|\rho_{\rm VNTE}-\rho_{\rm FRI}|/\rho > 1\%$ at fixed trajectory | Trajectory or $V$ candidate inconsistent with §2.3.1 |
| $w_{\rm scalar}$ matches $w_{\rm LCDM}$ at BBN/matter without SM content | Would require non-quartic $V$ + large kinetic fraction — **not seen** for E1–E3 |
| Independent $V(\Phi)$ from CPN/Connes matches **both** $\rho(N)$ **and** $w(N)$ | Would close D1; **not achieved** by current candidates |

**Inverted $V(\Phi,\dot\Phi)$ always matches $\rho$ by construction** — confirms V_NTE is **under-determined** off-trajectory (Companion 8 F3, Session 5).

---

## §6. Cross-references

- `LCDM_Epoch_Friedmann_Check_Worksheet_v0_2_20260523.md` (P1 tautology)  
- `LCDM_P1_P2_Jammer_Review_BAO_Numerics_Output_v0_1_20260523.md` (§1.3 genuine test routing)  
- `Handoff_Greg_Cursor_Ratification_LCDM_Tier2c_Six_Gates_20260523.md` (Gate #2 ρ_eff)  
- Companion 8 F3; Companion 9 E1–E3; Session 5 K(Φ) diagnosis  
- Part 1 §2.3.1; §17.5.1; §17.5.9

---

## §7. Verdict (Cursor execution, Jammer D1 scope)

**P1 genuine test executed.**  
- **ρ magnitude:** E1 (and corpus candidates E2/E3/hilltop) **match** $3H^2/(8\pi G)$ at all tested epochs — **expected tautology** on constraint trajectory.  
- **ρ scaling / thermal physics:** **Fail** for single-field $V(\Phi)$ — $w_{\rm scalar}\approx -1$ vs $w=1/3$ (BBN), $0$ (matter).  
- **Corpus discipline:** Do not claim "V_NTE fits cosmological energy budget"; claim **ρ_eff = total H-sourcing density** with Ω's as bookkeeping; V_NTE closure remains **structural**, not empirical at this layer.

— Cursor V_NTE D1 v0.1, 2026-05-23.
