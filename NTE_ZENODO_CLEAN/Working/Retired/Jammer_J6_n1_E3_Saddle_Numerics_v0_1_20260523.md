# J6-n1 — E3 reduced ODE + n_s numeric execution v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Authorisation:** Greg J6-n1  
**Script:** `Working/j6_e3_saddle_numerics.py`  
**Parent:** `Jammer_J6_HH_Saddle_First_Pass_v0_1_20260523.md`; BR2c two-sector register

---

## §1. Mission

Integrate Sector 1 (Role B) slow-roll dynamics from E3 off-trajectory $V_{\rm NTE}$, extract $n_s$ at the CMB window ($\sim$60 e-folds before end of inflation), compare to corpus target $n_s=0.9685$ and Companion 9 $\Phi^2$-chaotic benchmark.

**Discipline:** Sector 1 integration is **unconstrained** (no $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ slaving during HH slow-roll) per BR2c §3. Track A (constraint-slaved eq. (7)) run as **control only**.

---

## §2. Method

Three tiers + control:

| Tier | Potential | Purpose |
|------|-----------|---------|
| **T0** | Literal E3 with corpus $\alpha$ | Scale diagnostic |
| **T1** | Saddle-scaled E3: $V(\phi_0)=3M_{\rm Pl}^4$ | HH Hubble scale imposed at start |
| **T2** | $V=\frac12 m^2\phi^2$, $m=M_{\rm Pl,red}$ | C9 $\Phi^2$-chaotic reference |
| **A** | Constraint eq. (7), flat $k=0$ | Sector 2 / false single-ansatz control |

Integration: slow-roll Euler ($d\phi/dN = -V'/V \cdot M_{\rm Pl}^2$), $n_s = 1-6\varepsilon+2\eta$ at $N_{\rm end}-60$.

Corpus inputs: $\alpha=2.38\times10^{-47}$ GeV$^{-1}$, $M_{\rm Pl,red}=2.435\times10^{18}$ GeV, $\phi_{\rm start}=15.9\,M_{\rm Pl,red}$.

---

## §3. Results

### §3.1 T0 — Literal E3 + corpus $\alpha$ (**FAIL scale**)

| Quantity | Value |
|----------|-------|
| $V(\phi_{\rm start})$ | $\sim 2.2\times10^{22}$ GeV$^4$ |
| $H_{\rm SR}=\sqrt{V/3M_{\rm Pl}^2}$ | $\sim 3.6\times10^{-8}$ GeV |
| $H/M_{\rm Pl,red}$ | $\sim 1.5\times10^{-26}$ |

**Finding:** The on-trajectory leading coefficient $3\alpha^2 M_{\rm Pl}^2\Phi^4$ uses **cosmological** $\alpha$ (fixed at $H_0=\alpha v_{\rm EW}^2$). At $\phi\sim16\,M_{\rm Pl,red}$ this gives **no Planck-scale inflation**. HH Sector 1 cannot be sourced by literal E3 with present $\alpha$ alone.

**Register:** Not a contradiction — Role B saddle scale is **not** the Role A constraint scale (BR2c magnitude clash, numeric confirmation).

### §3.2 T1 — Saddle-scaled E3 ($V(\phi_0)=3M_{\rm Pl}^4$)

Quartic rescaled so $H(\phi_{\rm start})\approx M_{\rm Pl,red}$; subleading $\Phi^2$ term retains corpus $\alpha^2 A^2/8$ form.

| Quantity | Best scan |
|----------|-----------|
| $A$ | $10^4$ GeV$^2$ (subleading still negligible at $\phi_{\rm start}$) |
| $N_{\rm efolds}$ | 30.7 |
| $n_s$ at CMB window | **0.905** |
| Target | 0.9685 |

**Finding:** With saddle-imposed quartic, dynamics are **$\lambda\Phi^4$ dominated**; analytic $n_s\approx 1-24/\phi^2\approx0.905$. Subleading E3 $\Phi^2$ is **$\lesssim10^{-20}$** of quartic at $\phi\sim16\,M_{\rm Pl,red}$ unless $A\sim M_{\rm Pl}/\alpha$ (non-corpus). **E3 with corpus $\alpha$ structure does not turn quartic into $\Phi^2$-chaotic.**

### §3.3 T2 — $\Phi^2$-chaotic benchmark (**PASS**)

| Quantity | Value |
|----------|-------|
| $n_s$ analytic $1-8/\phi^2$ | **0.9684** |
| $n_s$ numeric (CMB window) | **0.9669** |
| $N_{\rm efolds}$ | **62.8** |
| $|\Delta n_s|$ vs 0.9685 | **0.0016** |

**Finding:** Unconstrained slow-roll on **effective quadratic** $V=\frac12 M_{\rm Pl}^2\phi^2/M_{\rm Pl}^2$ reproduces corpus $n_s$ and $N_e\sim63$ — consistent with Companion 9 Session 3 Gaussian-saddle / $\Phi^2$-chaotic equivalence. **Numeric integrator validated.**

### §3.4 Track A — Constraint-slaved eq. (7) (**FAIL $n_s$**)

| Quantity | Value |
|----------|-------|
| $n_s$ mid-integration | $\sim 1.0$ (constant-$\varepsilon$ exponential) |
| Reaches $H_{\rm GB}^{(\alpha)}$ in 2000 steps | **No** |

Confirms BR2c R1 exclusion: single constrained ansatz does not produce observed tilt.

---

## §4. Verdict (J6-n1)

| Claim | Verdict |
|-------|---------|
| Sector 1 $n_s=0.9685$ from **literal E3 + corpus $\alpha$** | **FAIL** (H-scale + wrong tilt) |
| Sector 1 $n_s$ from **effective $\Phi^2$ saddle / C9** | **PASS** (T2) |
| E3 $\Phi^2$ subleading with corpus $\alpha$ at HH scales | **Negligible** — cannot steer $n_s$ without non-corpus $A$ |
| Two-sector register (BR2c) | **Supported** — T0/T1 vs T2 + Track A |
| Action-derived **full** closure | **Not closed** — saddle scale in $S_E$ still required (J6-n3) |

**Corpus patch authorised:** **N** — findings are register-sharpening, not prediction change.

---

## §5. Falsifiers

1. If explicit $S_E[saddle]$ with $\xi=1/6$ yields **only** quartic $\lambda\Phi^4$ with cosmological $\alpha$ coefficient at $\phi\sim16\,M_{\rm Pl,red}$, then **C9 $\Phi^2$-chaotic route fails** — framework must revise Session 3 closure.
2. If derived $A$ from F3 on-trajectory ($A=|\Phi|^2/N_{\rm lock}$ at lock) is applied at HH scales and **changes** $n_s$ materially, T1 register must be revised (current: too small by $\sim10^{50+}$).
3. If unconstrained integration with **derived** (not rescaled) $V$ from J6-n3 matches T2 without Gaussian effective quadratic, upgrade J6b to **derived**.

---

## §6. Next queue

| ID | Task |
|----|------|
| **J6-n2** | E2 ($-\Phi^6$) numeric — Starobinsky-class comparison |
| **J6-n3** | Explicit $\mathcal{H}_{TT}$ on simplified $S_E$ → $T_{\rm GB}$ + $V_{\rm eff}$ normalization |
| **J6-n4** | BR2d locking junction memo |
| **S3-f3** | $d\mu(V)$ along derived $H(N)$ — after J6-n3 |

---

## §7. Handoff

- **AC:** File under Working/; reference in §22.18 pathway note (numeric support for saddle-scale requirement).
- **Cursor:** Update J6 first-pass status; no BR2c route change.
- **Greg:** J6-n1 **complete** at partial-closure register; authorise J6-n2 or J6-n3 next.

— Jammer J6-n1 v0.1, 2026-05-23.
