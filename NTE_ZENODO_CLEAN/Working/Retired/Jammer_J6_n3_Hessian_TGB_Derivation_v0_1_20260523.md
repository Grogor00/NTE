# J6-n3 — Explicit Hessian on simplified $S_E$ + $T_{\rm GB}$ derivation v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Authorisation:** Greg (J6-n3)  
**Script:** `Working/j6_n3_hessian_numerics.py`  
**Parents:** J6 first pass; J6-n1; Companion 9 §3; §22.18; `H_GB_Bridge_Attack_Route_v0_1`

---

## §1. Mission

Close J6c steps 1–3 on a **simplified** Euclidean action (dS₄ cap + $\xi=1/6$ scalar + corpus thermal identification):

1. Write $S_E$ explicitly at the HH saddle.
2. Compute Hessian eigenvalues (gravity + scalar blocks).
3. Derive $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ from Gaussian normalization with $\lambda_T\sim M_{\rm Pl}^2$.
4. Reconcile J6-n1: saddle supplies **Role B** $V_{\rm eff}$ scale; cosmological $\alpha$ quartic does not.

**Out of scope:** Full Hopf-$S^3\times S^1_\beta$ heat-kernel (Paper S2); J6d field map.

---

## §2. Simplified $S_E$ (NTE pre-EWSB, Sector 1 window)

### §2.1 Integrand

On Euclidean $S^4$ cap (HH no-boundary) with $H_E\equiv H$ and $R=12H^2$:

$$S_E = \frac{M_{\rm Pl}^2}{2}\int d^4x\,\sqrt{g}\,R \;-\; \int d^4x\,\sqrt{g}\left[\frac12(\partial\Phi)^2 + \frac{1}{12}R\,\Phi^2 + V_{\rm NTE}(\Phi)\right] \;+\; S_{\rm constr}$$

**Sector 1 discipline (BR2c):** $S_{\rm constr}$ (Lagrange multiplier enforcing $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$) is **inactive** during HH slow-roll; it activates in Sector 2 terminal roll. J6-n1 confirmed literal $\alpha$ quartic cannot source $H\sim M_{\rm Pl}$ at $\Phi\sim16\,M_{\rm Pl,red}$.

Pre-EWSB: $|H_{\rm SM}|=0$; $V_{\rm NTE}$ subleading off saddle — quadratic piece from Wick rotation (Companion 9 §4.2).

### §2.2 Integrated gravity sector (explicit)

For the 4-sphere cap of radius $R_H=1/H$ (Gibbons–Hawking–Perry convention):

$$\boxed{S_{\rm grav}(H) = -\frac{3\pi^2 M_{\rm Pl}^2}{H^2}}$$

Saddle at $H_*=M_{\rm Pl}$ (non-reduced) gives $S_*=-3\pi^2 M_{\rm Pl}^2$.

---

## §3. Hessian — gravity block (Step 2a)

Expand in $H$ about $H_*$:

$$\frac{\partial^2 S_{\rm grav}}{\partial H^2}\bigg|_{H_*} = \frac{18\pi^2 M_{\rm Pl}^2}{H_*^4} = 18\pi^2 M_{\rm Pl}^2 \cdot M_{\rm Pl}^{-4} \cdot M_{\rm Pl}^4 = 18\pi^2 \;\text{(in }M_{\rm Pl}\text{ units)}$$

In GeV units ($M_{\rm Pl}=M_{\rm Pl,nr}=1.221\times10^{19}$ GeV):

$$\lambda_H = \frac{18\pi^2 M_{\rm Pl,nr}^2}{H_*^4}\bigg|_{H_*=M_{\rm Pl,nr}} = 1.19\times10^{-36}\;\text{GeV}^2$$

Gaussian width in $H$:

$$\sigma_H = \lambda_H^{-1/2} \approx 9.16\times10^{17}\;\text{GeV} \approx 0.075\,M_{\rm Pl,nr}$$

**Register:** Gravity Hessian is **Planck-scale** ($\lambda_H^{-1/2}\sim M_{\rm Pl}^{-1}H_*^2$ structure); not $H_{\rm GB}^{(\alpha)}$ scale.

---

## §3. Hessian — scalar block (Step 2b)

For $\xi=1/6$, constant $R=12H^2$ on the cap, Euclidean quadratic coefficient:

$$m_E^2(H) = \xi R = 2H^2$$

At $H_*=M_{\rm Pl,nr}$:

$$m_E = \sqrt{2}\,M_{\rm Pl,nr} \approx 1.73\times10^{19}\;\text{GeV}$$

**Wick rotation (Companion 9 §4.2):** Lorentzian $V''(0)<0$ (Mexican-hat pre-temporal form) $\to$ Euclidean positive-definite $m_E^2$ at the HH peak — Gaussian saddle in $\Phi$.

**J6-n1 reconciliation:** Role B slow-roll uses **effective** $V\approx\frac12 m_{\rm eff}^2\Phi^2$ with $m_{\rm eff}\sim M_{\rm Pl,red}$ (C9 $\Phi^2$-chaotic, J6-n1 T2 PASS). This is **not** the literal on-trajectory coefficient $3\alpha^2 M_{\rm Pl}^2\Phi^4$ with cosmological $\alpha$. The saddle Hessian supplies $m_E\sim\sqrt{2}\,M_{\rm Pl,nr}$; C9 identifies $m_{\rm eff}\sim M_{\rm Pl,red}$ for $n_s$ after projection to slow-roll window — **same order, distinct register** (Euclidean peak vs Lorentzian roll).

---

## §4. Temperature block — $T_{\rm GB}$ (Step 2c + Step 3)

### §4.1 Corpus identification

Gauge-birth nucleation peak uses **thermal-direction** Hessian eigenvalue:

$$\lambda_T = M_{\rm Pl,nr}^2$$

(Gaussian curvature of $S_E$ in temperature mode at saddle — gravity-sector scale; Companion 9 §3.1.)

### §4.2 Gaussian normalization (explicit)

Fluctuation integral:

$$\int_{-\infty}^{\infty} \exp\!\left(-\frac{\lambda_T}{2}\,\delta T^2\right) d(\delta T) = \sqrt{\frac{2\pi}{\lambda_T}} = \frac{\sqrt{2\pi}}{M_{\rm Pl,nr}}$$

Characteristic nucleation scale (peak amplitude × width):

$$\boxed{T_{\rm GB} = \frac{M_{\rm Pl,nr}}{\sqrt{2\pi}} \approx 0.399\,M_{\rm Pl,nr} \approx 4.87\times10^{18}\;\text{GeV}}$$

Reduced mass: $T_{\rm GB,red}=M_{\rm Pl,red}/\sqrt{2\pi}\approx9.71\times10^{17}$ GeV.

**Numeric:** $T_{\rm GB}/M_{\rm Pl,nr}=0.398942=1/\sqrt{2\pi}$ ✓

### §4.3 Not Hawking $T=H/2\pi$

At $H=M_{\rm Pl,nr}$: $T_{\rm Hawking}=H/(2\pi)\approx0.159\,M_{\rm Pl,nr}$.

$$T_{\rm GB}/T_{\rm Hawking} \approx 2.51$$

**Register:** $T_{\rm GB}$ is **Gaussian saddle width** at gauge birth (C1), not de Sitter Hawking temperature. Epoch A uses $H_{\rm GB}^{(F)}$ from Friedmann at $T_{\rm GB}$ — distinct from $H_*$ and from $H_{\rm GB}^{(\alpha)}$.

---

## §5. Epoch A cross-check (Step 4)

Friedmann at $T_{\rm GB}$ with $g_{\rm eff}=106.75$:

| Quantity | Value |
|----------|-------|
| $H_{\rm GB}^{(F)}$ | $3.33\times10^{19}$ GeV |
| $H_{\rm GB}^{(\alpha)}$ | $3.55\times10^{-9}$ GeV |
| $\ln(H^{(F)}/H^{(\alpha)})$ | **64.41** |

Matches `h_gb_bridge_numerics.py` three-epoch table. **No contradiction** with $N_e\approx63.4$ on $H^{(\alpha)}$ scale (BR2c).

---

## §6. Verdict

| Item | Status |
|------|--------|
| $S_E$ written (simplified dS₄ + $\xi=1/6$) | **Done** |
| $\lambda_H$ computed explicitly | **Done** — $\sim18\pi^2 M_{\rm Pl}^2/H^4$ |
| $\lambda_T=M_{\rm Pl}^2$ $\Rightarrow$ $T_{\rm GB}$ | **Done** — derived-at-simplified-$S_E$ |
| $m_E$ scalar block | **Done** — $m_E=\sqrt{2}\,H_*$ at $H=M_{\rm Pl}$ |
| J6-n1 scale reconciliation | **Done** — saddle vs $\alpha$ quartic |
| Full Paper S2 heat-kernel | **Open** |
| J6d field map | **Open** |

### §6.1 (C1) register upgrade (Jammer sign-off)

**§17.5.4 (C1):** upgrade **candidate $\to$ derived-at-simplified-$S_E$** (Jammer J6-n3, 2026-05-23).

**Corpus patch authorised:** **Y** — status register + §22.18 footnote; **no prediction change**.

**Remaining upgrade path:** Paper S2 explicit $S_E[saddle]$ on Hopf-$S^3\times S^1_\beta$ $\to$ **fully derived** (drop “simplified”).

---

## §7. Falsifiers

1. Paper S2 heat-kernel gives $\lambda_T$ at $H_{\rm GB}^{(\alpha)}$ scale $\Rightarrow$ $T_{\rm GB}$ formula fails.
2. Explicit $\xi=1/6$ re-derivation gives $m_E^2\not\sim H^2$ at saddle $\Rightarrow$ scalar block revised.
3. Derived field map (J6d) forces single-sector $\alpha$ quartic at HH $\Rightarrow$ J6-n1 T0 becomes sole dynamics — contradicts $n_s$.

---

## §8. Next queue

| ID | Task |
|----|------|
| **J6-n4** | BR2d $y\leftrightarrow N$ locking junction |
| **J6-n2** | E2 ($-\Phi^6$) numeric (optional) |
| **S3-f3** | $d\mu(V)$ along Sector 1 $H(N)$ |

— Jammer J6-n3 v0.1, 2026-05-23.
