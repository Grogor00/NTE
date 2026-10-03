# S3-f4 — $a_6+$ exponential tail on NTE $M$ v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Script:** `Working/s3_f4_a6_tail_numerics.py`  
**Parents:** Paper S3 §R3; CC2008 §3 Theorem 3; S2-C-B/C-C; S3-f2/f3

---

## §1. Mission

Evaluate **R3** — CC2008 exponential tail $a_6+$ on $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$:

1. Do heat-kernel coefficients $a_6,a_8$ vanish (CC2008 inheritance)?
2. Does Theorem 3 tail $|\varepsilon(\Lambda)|\lesssim e^{-\pi(\mu\Lambda)^2/2}$ supply **~83 OOM** suppression at canonical NTE parameters?

**Honest register:** Paper S3/S4 must not claim $\Lambda_{\rm obs}$ closure unless derived chain passes falsifiers.

---

## §2. Coefficient level — $a_6,a_8$ on $M$

### §2.1 CC2008 (round $S^3\times S^1$)

- **$a_4=0$:** Weyl $C^2=0$ and Gauss–Bonnet $R^*R^*=0$ on product geometry.
- **$a_6=0$:** 18 Gilkey terms split $(+2/3,-2/3)a^{-6}$ — exact cancellation (CC2008 §3 pp. 27–31).
- **Higher $a_{2n}$:** same mechanism → expansion terminates after $a_0,a_2$ + exponential remainder.

### §2.2 NTE substrate

| Item | Register |
|------|----------|
| Hopf $S^3$ | **Same round metric** as CC2008 — bundle is topological; **does not break** $a_6=0$ |
| $A_F=N_F=180$ | Enters **multiplicatively** at leading order (S2-B); no known $a_6$ lift |
| NTE **non-zero $a_4$** | S2-C-B: $a_4|_M=\tfrac32 N_F\beta_{\rm GB}$ from **$R^2$-only** piece — **distinct** from CC2008 geometric $a_4=0$ |
| D_F subleading (S2-C-C) | $\mathcal{O}(10^{-18})$ on $a_4$ — $a_6$ from Yukawa insertions **negligible** |

**S3-f4 coefficient verdict:** $a_6=a_8=0$ **inherited** at geometric level; NTE gravitating residual sits in **$f_0 a_4$** (S3-f2), not in $a_6$ coefficient.

---

## §3. Tail level — CC2008 Theorem 3

For $h\in\mathcal{S}(\mathbb{R})$, on $S^3_a\times S^1_\beta$:

$$\mathrm{Tr}(h(D^2/\Lambda^2)) = 2\pi\Lambda^4\beta a^3\!\int\! h(\rho^2)\rho^3 d\rho - \pi\Lambda^2\beta a\!\int\! h(\rho^2)\rho d\rho + \varepsilon(\Lambda)$$

$$|\varepsilon(\Lambda)| \le C\, e^{-\pi(\mu\Lambda)^2/2}, \qquad \mu=\inf(a,\beta)$$

### §3.1 NTE canonical geometry

| Parameter | Value |
|-----------|-------|
| $a$ | 1 (unit $S^3$, S2-A) |
| $\beta$ | $\beta_{\rm GB} M_{\rm Pl}=\sqrt{2\pi}\approx 2.51$ (Planck lengths) |
| $\mu=\inf(a,\beta)$ | **1** |
| $\Lambda_{\rm cut}$ | $M_{\rm Pl}$ |
| $\mu\Lambda$ (Planck) | **$\sim 1$** |

### §3.2 Numeric tail (script)

| Quantity | Value |
|----------|-------|
| $|\varepsilon|$ upper bound | $\lesssim e^{-\pi/2}\approx 0.21$ |
| $\log_{10}$ suppression | **$\sim -0.7$ dex** |
| Required for $\Lambda_{\rm obs}$ | **$\sim -84$ dex** |
| $\mu\Lambda$ needed for 83 OOM | **$\sim 11$** |

**At canonical NTE:** tail is **O(1)**, not $10^{-83}$.

### §3.3 Spectral-gap cross-check (S2-A)

Lowest $|λ_D|$ modes $\sim M_{\rm Pl}$ → $e^{-\pi(\lambda/M_{\rm Pl})^2/2}\sim 0.01$–$0.2$ — still **not** 83 OOM.

---

## §4. Combined stack (R1 + R2 + R3)

From S3-f2/f3 + this memo:

$$\Lambda_{\rm eff} \sim \underbrace{f_0 a_4}_{\sim 10^{37}\,{\rm GeV}^4} \times \underbrace{\mathcal{W}_{d\mu}}_{\sim 1} \times \underbrace{|\varepsilon(\Lambda)|}_{\sim 0.2} \sim 5\times 10^{36}\,{\rm GeV}^4$$

Still **$\sim 83$ dex** above $\Lambda_{\rm obs}$.

| Scenario | $|\varepsilon|$ | $\Lambda_{\rm eff}$ vs obs |
|----------|-----------------|---------------------------|
| **Canonical** ($\mu\Lambda\sim 1$) | $\sim 0.21$ | **83.2 dex high** |
| $\mu\Lambda=11$ (tail-only target) | $\sim 10^{-83}$ | **$\sim 1.4$ dex high** — *not derived* |
| $\Lambda=10 M_{\rm Pl}$ | $\sim 10^{-69}$ | **15.7 dex high** — *non-canonical* |

---

## §5. Verdict table

| Claim | Status |
|-------|--------|
| $a_6=a_8=0$ on round $M$ (Hopf inherited) | **Done** — CC2008 + S2 metric |
| NTE $a_4$ non-zero from $R^2/N_F$ | **Confirmed** (S2-C-B) — separate from CC2008 $a_4=0$ |
| CC2008 tail closes 83 OOM at canonical params | **Excluded** |
| Tail *could* close gap if $\mu\Lambda\sim 11$ | **Illustrative only** — no derived NTE geometry |
| Paper S3 $\Lambda_{\rm obs}$ ship claim | **Still forbidden** |

---

## §6. What remains open (Paper S4 programme)

1. **R4** — RT / de Sitter horizon area law on $S^3$ (P-dS1).
2. **R5** — M3 $\beta_{\rm GB}$ boundary counter-term (sign programme).
3. **Non-perturbative** spectral action beyond heat-kernel truncation (if any).
4. **Honest combined chain** landing within $10\times\Lambda_{\rm obs}$ with falsifiers — **not yet achieved**.

**Discipline:** $\mu\Lambda\sim 11$ is **not** to be imported as fit parameter; would require **derived** enlargement of effective spectral gap from boundary/gauge-birth physics.

---

## §7. AC pointer

> **S3-f4 (Jammer, 2026-05-23):** $a_6=a_8=0$ inherited on round $S^3\times S^1_{\beta_{\rm GB}}$; CC2008 Theorem 3 tail at canonical $\mu\Lambda\sim 1$ gives $|\varepsilon|\sim 0.2$ — **does not** supply ~83 OOM. Combined R1+R2+R3 still ~83 dex high. See `Working/Jammer_S3_f4_a6_Tail_v0_1_20260523.md`.

---

## §8. Cross-references

- `Unimodular_Gravity_Verification_CC2008_v1.md` §2  
- `Jammer_S3_f2_fk_Moments_v0_1`; `Jammer_S3_f3_dmu_V_from_PhiN_v0_1`  
- `Paper_S2_S2CB_a4_Weyl_Euler_v0_1`; S2-C-C  
- `Paper_S3_Structural_f_Attack_Route_v0_1`

— Jammer S3-f4 v0.1, 2026-05-23.
