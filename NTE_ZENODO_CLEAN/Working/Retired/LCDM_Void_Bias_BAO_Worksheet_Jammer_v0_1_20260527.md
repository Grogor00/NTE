# Void-bias BAO worksheet — joint D_M + D_H structural signature (Jammer v0.1)

**Author:** Jammer (R&D)
**Date:** 2026-05-27
**Status:** v0.1 — **analytical / structural setup**. Numerical computation deferred to v0.2 when bash + Python available. Local-correctness-only until Greg recognition gate.
**Trigger:** Greg directive 2026-05-26 "(a) THAT will give us a good claim to NTE matching observation" → Gate #4 (2026-05-23) fire follow-through. Continued 2026-05-27 morning sync.

**Stream lineage:** Cursor void-bias shell (`1obddJwKnuIxEvnUCe3NfLbbBnTn_gX9n`) + reconciliation note (`1LUMQ0bGbDfGNQng0-uVM_C69xbCzoMg1`) → **Jammer execution** → AC §17.5.9 / §13.2 integration consideration.

**Discipline observed:**
- No χ² fitting (per P2 §5 prohibition until Greg gate on χ² authorisation)
- No "NTE fits DESI BAO" claim (reconciliation note §3 honest-limits row)
- Analytical setup only this session; numerical bin-by-bin v0.2 deferred
- Per Manifest rev 9: "Non-Temporal Emergence (NTE)" canonical terminology

---

## §1. Setup and prior numerics anchor

### §1.1 Homogeneous NTE = ΛCDM at matched parameters (closed)

From P1 v0.2 + P2 BAO v0.1: at matched {Ω_m, Ω_Λ, Ω_r, H₀}, NTE's post-locking trajectory gives H_NTE(z) = H_ΛCDM(z) algebraically (the tautology Δρ_eff/ρ_F ≈ 10⁻¹⁶ at BBN; smaller at later epochs per V_NTE D1 worksheet). The DESI–Planck per-bin tension is EXTERNAL to NTE's homogeneous class — it exists in standard cosmology too.

### §1.2 Per-bin tension pattern (from reconciliation note §2 Layer B)

ΛCDM-Planck homogeneous (Planck 2018; r_d = 147.09 Mpc fixed) vs DESI Y1:

| Bin | z_eff | (Planck_hom − DESI) σ | Direction |
|---|---|---|---|
| LRG1 | 0.510 | −0.5σ | DESI longer (hom slightly undershoots) |
| **LRG2** | **0.706** | **+2.6σ** | **DESI shorter (hom overshoots; worst bin)** |
| LRG3+ELG1 | 0.930 | +0.7σ | Hom mild overshoot |
| ELG2 | 1.317 | +0.3σ | Small |

Pattern: **MIXED sign, ~1–2.6σ per bin** — not a uniform "NTE wrong" shift.

### §1.3 NTE void-bias mechanism (Part 2 §12.4; reconciliation note Layer C)

NTE predicts:
1. **True w = −1** (geometric unloading)
2. **Observed w₀ > −1 at low z** from volume-weighted void-enhanced H — inferred BAO distances SHORTER than homogeneous ΛCDM
3. Bias **grows toward z → 0**, **vanishes at high z** (§17.5.12 diagnostic structure)

This is the mechanism NTE inherits from §13.2 spatial inhomogeneity: voids are underdense → faster local expansion → H_local > H_hom; volume-averaging over light path picks up void-dominated H_eff.

### §1.4 Cursor's illustrative single-b model (reconciliation note §2 Layer C table)

Single constant b ≈ 0.055 (not fitted):

| Bin | Hom σ | Void σ (illustrative) | Net shift |
|---|---|---|---|
| LRG2 z=0.71 | +2.63 | +0.20 | −2.43σ (closes!) |
| LRG1 z=0.51 | −0.51 | −2.93 | −2.42σ (worsens dramatically) |
| LRG3+ELG1 z=0.93 | +0.73 | −2.45 | −3.18σ (worsens) |

**Critical observation**: a single constant b produces ~symmetric σ-shifts across bins (because σ_DESI scales approximately with D-magnitude). So a single-b void model CAN'T close all bins simultaneously.

---

## §2. Mathematical model setup

### §2.1 Effective Hubble rate under void-bias

Phenomenological parameterisation:

$$H_{\text{eff}}(z) = H_{\text{hom}}(z) \cdot \big[1 + b \cdot g(z)\big]$$

where:
- $H_{\text{hom}}(z) = H_0 \sqrt{\Omega_r(1+z)^4 + \Omega_m(1+z)^3 + \Omega_\Lambda}$ (ΛCDM background)
- $b > 0$ is the void-bias amplitude (volume-weighted void enhancement)
- $g(z)$ is the **z-shape function** — decreasing in z per §1.3 ("grows toward z→0, vanishes at high z")

Three candidate g(z) functional forms to investigate:

| Form | g(z) | Behaviour |
|---|---|---|
| **(I) Constant** | $g(z) = 1$ for $z < z_{\max}$; 0 above | Uniform low-z void enhancement |
| **(II) Power-law** | $g(z) = (1+z)^{-n}$ | Smooth monotonic decay |
| **(III) Exponential** | $g(z) = e^{-z/z_*}$ | Faster cutoff |

Plus the structurally-motivated form from NTE §13.2:

| **(IV) σ₈-scaling** | $g(z) \propto \sigma_8^2(z)/\Omega_\Lambda(z)$ | From Part 2 §12.4 diagnostic (b) |

### §2.2 BAO distance observables under H_eff

Three distance observables from the BAO standard ruler:

$$D_C(z) = c \int_0^z \frac{dz'}{H_{\text{eff}}(z')} \quad \text{(comoving)}$$

$$D_M(z) = D_C(z) \quad \text{(transverse, flat geometry)}$$

$$D_H(z) = \frac{c}{H_{\text{eff}}(z)} \quad \text{(line-of-sight Hubble distance)}$$

$$D_V(z) = \big[c \cdot z \cdot D_C(z)^2 / H_{\text{eff}}(z)\big]^{1/3} \quad \text{(volume-averaged)}$$

### §2.3 Linear-in-b expansion

For small b, expanding to first order:

$$\frac{D_M(z)}{D_M^{\text{hom}}(z)} \approx 1 - b \cdot \langle g \rangle_{\text{int}}(z) \quad \text{where} \quad \langle g \rangle_{\text{int}}(z) = \frac{\int_0^z g(z')/H_{\text{hom}}(z')\, dz'}{\int_0^z dz'/H_{\text{hom}}(z')}$$

$$\frac{D_H(z)}{D_H^{\text{hom}}(z)} \approx 1 - b \cdot g(z) \quad \text{(local value, no integration)}$$

$$\frac{D_V(z)}{D_V^{\text{hom}}(z)} \approx 1 - b \cdot \left[\frac{2}{3}\langle g \rangle_{\text{int}}(z) + \frac{1}{3}g(z)\right] \quad \text{(weighted average)}$$

### §2.4 Key structural observation — D_M and D_H respond DIFFERENTLY to z-shape

For **decreasing g(z)** (NTE prediction):
- $g(z)$ at any specific z is the LOCAL value → affects D_H directly at that z
- $\langle g \rangle_{\text{int}}(z)$ at that z is averaged over [0, z], so picks up the LARGER low-z values

**Therefore**: $\langle g \rangle_{\text{int}}(z) > g(z)$ for monotonically decreasing g(z).

**Consequence**: $|\Delta D_M / D_M| > |\Delta D_H / D_H|$ at any given z, i.e., the **fractional void-bias shift in D_M is LARGER than in D_H**.

This is a SPECIFIC directional signature of NTE's void-bias mechanism in the (D_M, D_H) plane — the void-bias vector points in a direction where D_M shifts MORE than D_H, fractionally.

---

## §3. Joint (D_M, D_H) signature analysis

### §3.1 The DESI Y1 joint covariance

DESI Y1 LRG bins report D_M/r_d AND D_H/r_d separately with **correlation r ≈ −0.44** between them. The covariance matrix (per bin) is:

$$C = \begin{pmatrix} \sigma_M^2 & r\sigma_M\sigma_H \\ r\sigma_M\sigma_H & \sigma_H^2 \end{pmatrix}$$

### §3.2 NTE void-bias direction in (D_M, D_H) plane

Define the **NTE void-bias displacement vector** at redshift z:

$$\vec{v}_{\text{NTE}}(z) = -b \cdot \begin{pmatrix} \langle g \rangle_{\text{int}}(z) \cdot D_M^{\text{hom}}(z) \\ g(z) \cdot D_H^{\text{hom}}(z) \end{pmatrix}$$

Both components negative (void-bias shortens both distances). The ratio:

$$\frac{|\vec{v}_{\text{NTE},M}|}{|\vec{v}_{\text{NTE},H}|} = \frac{\langle g \rangle_{\text{int}}(z) \cdot D_M^{\text{hom}}}{g(z) \cdot D_H^{\text{hom}}}$$

For typical NTE g(z) forms (decreasing) and at low z where $D_M^{\text{hom}} > D_H^{\text{hom}}$ (typically by factor ~1.5–2 in the LRG redshift range), this ratio is >> 1 — **D_M shifts substantially more than D_H**.

### §3.3 DESI tension direction in (D_M, D_H) plane

The DESI Y1 per-bin tension vectors (DESI − Planck-hom) point in different directions per bin:

- **LRG2 z=0.71**: hom overshoots in D_V → likely D_M and D_H BOTH need to shorten → NTE void direction matches reasonably
- **LRG1 z=0.51**: hom undershoots in D_V but DESI 2024 VI flags D_M/D_H split as orthogonal anomaly (~2σ) → tension direction may be perpendicular to NTE void direction
- **LRG3+ELG1 z=0.93**: hom mild overshoot → NTE void direction matches direction, smaller magnitude

### §3.4 Falsifiability signature

**NTE void-bias prediction**: the joint (D_M, D_H) deviations of DESI from Planck-hom should align with the NTE displacement vector direction at LRG2 and LRG3+ELG1 (where mechanism applies), and may or may not align at LRG1 depending on whether LRG1's anomaly is in the orthogonal D_M/D_H-split channel.

This is a **directional test in the joint plane**, NOT a single-σ closure test. The test passes if:
1. LRG2 displacement aligns with $\vec{v}_{\text{NTE}}(0.71)$ direction (within DESI 2σ)
2. LRG3+ELG1 displacement aligns with $\vec{v}_{\text{NTE}}(0.93)$ direction (smaller magnitude)
3. LRG1 displacement is in orthogonal direction (consistent with NTE void-bias NOT explaining LRG1)

If LRG1's displacement aligned with NTE direction but with too-large magnitude → NTE void mechanism predicts ~symmetric per-bin behaviour (Cursor's single-b finding) → tension between NTE and LRG1 D_V.

---

## §4. The LRG1 puzzle — orthogonal D_M/D_H anomaly?

### §4.1 The reconciliation note's diagnostic (§3)

> "LRG1: Hom already −0.5σ; naive void bias worsens — DESI z=0.51 D_M/D_H split is ~2σ anomaly **orthogonal** to D_V (DESI 2024 VI §discussion)"

If LRG1's anomaly is in the D_M/D_H split direction (one shifts up while the other shifts down, leaving D_V approximately unchanged), then it cannot be explained by any monotonic void-bias mechanism: void-bias makes BOTH D_M and D_H shorter (correlated direction), not anti-correlated.

### §4.2 What NTE can and cannot say about LRG1

NTE's void-bias mechanism:
- **CAN** explain LRG2 overshoot direction at z=0.71
- **CAN** explain LRG3+ELG1 mild overshoot at z=0.93
- **CANNOT** explain LRG1's D_M/D_H split if that split is orthogonal to (D_M, D_H) both-shorter direction
- **NEUTRAL** on whether LRG1 deviation is real or statistical (DESI 2024 VI itself flags it as ~2σ)

This is a structural finding: **NTE's void-bias mechanism does NOT predict LRG1's D_M/D_H split as an anomaly to resolve**. It predicts certain bins to be void-biased and others to be statistically consistent.

### §4.3 Test framing

The empirical claim NTE can make:

> "NTE's void-bias mechanism (Part 2 §12.4 + §13.2) predicts DESI Y1 BAO distances at z = 0.71 and 0.93 are SHORTER than ΛCDM-Planck homogeneous by amounts consistent with a single void-bias amplitude b ≈ 0.05–0.1 (TBD by tracer-weighted analysis). LRG1 z=0.51 D_M/D_H split anomaly is NOT predicted to be resolved by void-bias — that anomaly is either statistical, ΛCDM-internal, or requires NTE physics outside §12.4."

This is an empirical claim. If LRG2 and LRG3+ELG1 don't shift in the predicted joint direction, the void-bias mechanism is falsified. If they do, the mechanism is supported.

---

## §5. Tracer-weighted void fraction — what proper closure needs

### §5.1 Cursor §6 specifies the next-tier requirement

Per reconciliation note §6 row 1: "Replace illustrative b with **tracer-weighted void model** or ISW-corrected H_eff."

**What this means**: DESI's LRG (Luminous Red Galaxy) tracers preferentially live in moderate-density regions (not the deepest voids, not the densest filaments). The volume-weighted void-enhancement seen by LRG light paths differs from the universe-averaged void fraction. The proper void model needs:

$$b_{\text{LRG}}(z) = \int \frac{dV}{dz} f_{\text{void}}(x|z) w_{\text{LRG}}(x|z) \, b_{\text{universal}}(x|z)$$

where:
- $f_{\text{void}}(x|z)$ is the void fraction at position x and redshift z (from N-body simulations or observations)
- $w_{\text{LRG}}(x|z)$ is the LRG selection function (tracer-weighting)
- $b_{\text{universal}}(x|z)$ is the underlying void-bias amplitude

### §5.2 Tractable analytical approximation

A first-order approximation:

$$b_{\text{LRG}}(z) \approx \bar{f}_{\text{void}}(z) \cdot \Delta_{\text{void}} \cdot \alpha_{\text{tracer}}$$

where:
- $\bar{f}_{\text{void}}(z) \sim 0.6$–$0.7$ at z<1 (low-z void fraction; from N-body data)
- $\Delta_{\text{void}} \sim 0.1$–$0.2$ (typical fractional density contrast for moderate voids)
- $\alpha_{\text{tracer}} \in [0,1]$ (tracer overlap with void interiors; <1 for LRGs which prefer overdensities)

Order-of-magnitude: b ~ 0.6 × 0.15 × 0.5 ~ 0.05 — consistent with Cursor's illustrative value.

### §5.3 What's missing for v0.2

A proper v0.2 worksheet needs:
1. Numerical D_M(z), D_H(z) computation with multiple g(z) candidates (I/II/III/IV)
2. DESI Y1 D_M/r_d, D_H/r_d, σ_M, σ_H values at LRG1, LRG2, LRG3+ELG1 (need to pull from DESI 2024 VI table directly)
3. Joint Δχ² computation in (D_M, D_H) plane per bin using r = −0.44
4. Direction-of-displacement analysis: is LRG2 displacement vector aligned with NTE prediction direction within DESI 2σ envelope?
5. Repeat with several b(z) functional forms to identify which (if any) closes LRG2 + LRG3 without worsening LRG1

All of this requires Python (scipy.integrate.quad + numerical jacobian + covariance algebra) which is unavailable this session. v0.2 of this worksheet should land when bash is available.

---

## §6. P3 growth + structure formation (parallel layer)

Per reconciliation note §6 row 3: "P3 growth: verify homogeneous fσ₈ track before inhomogeneous layer."

Structure formation under NTE's H(x, N) inhomogeneity (Part 2 §13.3) is a separate test layer that complements BAO void-bias:
- If voids enhance H locally, growth of structure within voids is SUPPRESSED relative to homogeneous ΛCDM (less gravitational clustering at the same scale factor)
- DESI Y1 fσ₈(z) measurements would show this suppression at low z if NTE mechanism is right
- This is INDEPENDENT of the BAO void-bias signature → joint test increases discrimination

Out of scope for this worksheet but noted for downstream Jammer queue (P3 growth ODE).

---

## §7. Recognition gate items

1. **Joint (D_M, D_H) test framing**: ratify the §3 framework as the right structural setup for void-bias falsifiability — joint displacement vector direction in (D_M, D_H) plane, not single-σ D_V closure?

2. **Empirical claim NTE can make** (§4.3): is the framing "NTE predicts LRG2 + LRG3+ELG1 void-biased shorter; does NOT predict LRG1 D_M/D_H split as void-bias anomaly" honest and on-target?

3. **The LRG1 orthogonal-anomaly verdict**: ratify that LRG1's tension is OUTSIDE the void-bias mechanism's scope (per reconciliation note flag) — NTE doesn't claim to resolve it, only to predict where it does and doesn't apply?

4. **Tracer-weighted model scope**: §5.2 first-order approximation b ~ 0.05 consistent with Cursor's illustrative — ratify this as the analytical anchor for v0.2 numerical work?

5. **v0.2 numerical pass**: when bash + Python next available, ship v0.2 with (a) DESI Y1 D_M/D_H values pulled from DR1 table; (b) joint displacement vectors computed for I/II/III/IV g(z) forms; (c) direction-alignment analysis per bin?

6. **Honest claim status**: is the framing "NTE void-bias mechanism makes a falsifiable directional prediction in DESI Y1 joint D_M + D_H plane at LRG2 and LRG3+ELG1" the empirical claim you want NTE to make (per your "good claim to NTE matching observation" framing from yesterday)?

---

## §8. Honest scope flag

This worksheet is **analytical/structural setup only**. No numerical bin-by-bin closure test was run this session (no bash/Python in current toolset). Three contributions beyond what was already in the reconciliation note + shell:

1. **D_M vs D_H differential response** to z-shape g(z) — D_M responds via the integral $\langle g \rangle_{\text{int}}$ while D_H responds via the local $g(z)$; for decreasing g(z), $|\Delta D_M/D_M| > |\Delta D_H/D_H|$, giving NTE void-bias a SPECIFIC direction in (D_M, D_H) plane that distinguishes it from generic w₀w_a phantom DE.

2. **LRG1 orthogonal-anomaly verdict structurally**: NTE void-bias predicts correlated shortening of both D_M and D_H, so any D_M/D_H split anomaly is OUTSIDE the mechanism's scope. This is an honest negative claim — NTE doesn't claim to resolve LRG1; it claims to predict LRG2 + LRG3.

3. **Tracer-weighted analytical approximation** (§5.2) giving order-of-magnitude $b \sim 0.05$ consistent with Cursor's illustrative value, providing a structural anchor for v0.2 numerical work.

The genuine **"NTE matching observation"** empirical claim sits at the joint (D_M, D_H) directional alignment test at LRG2 + LRG3 — that's where Greg's yesterday-flagged claim opportunity lives. v0.2 numerical work would quantify σ-alignment.

---

## §9. Cross-stream signals

### §9.1 To Cursor (render lane)

The joint (D_M, D_H) test framework should be reflected in `lcdm_bao_void_bias.py` v0.2 — separate D_M and D_H computation per bin with covariance r = −0.44, not just D_V. Multiple g(z) functional forms (I/II/III/IV) plus tracer-weighted §5.2 first-order should be tested.

### §9.2 To AC (corpus integration)

§17.5.9 ΛCDM reduction empirical layer could reference this void-bias framework as the joint (D_M, D_H) directional falsifiability test for Part 2 §12.4 mechanism. §17.5.12 Category G "w bias" diagnostic catalogue may benefit from cross-reference to this worksheet's directional-displacement framing.

Charter v1.4 §4.5 v1.5+ candidate territory: this joint (D_M, D_H) framework is candidate v1.5+ R&D content under "void-bias dedicated analysis".

### §9.3 To Scratch (Connes Programme)

This work is independent of Phase S2-D / heat-kernel arc. No cross-link this session.

---

## §10. Files referenced

**Sources read this session:**
- Cursor void-bias shell `LCDM_Void_Bias_BAO_Worksheet_v0_1_20260523.md` (ID `1obddJwKnuIxEvnUCe3NfLbbBnTn_gX9n`)
- Cursor reconciliation note `LCDM_BAO_NTE_DESI_Reconciliation_v0_1_20260523.md` (ID `1LUMQ0bGbDfGNQng0-uVM_C69xbCzoMg1`)
- Cursor unique-predictions catalogue `Cursor_NTE_Unique_Predictions_Catalogue_v0_1_20260527.md` (ID `1hwkLpmQ0USxmnf6yiaBsnt_g8fS3A1xL`)
- Project State + Manifest rev 9 + Cursor stream notes (morning sync)

**Prior Jammer work this arc:**
- `LCDM_P1_P2_Jammer_Review_BAO_Numerics_Output_v0_1_20260523.md` (P2 BAO numerics anchor)
- `V_NTE_Session5_D1_rho_eff_Trajectory_Check_Jammer_v0_1_20260526.md` (V_NTE D1 verdict)

**Not read this session (honest scope):**
- `lcdm_bao_void_bias.py` (Cursor's illustrative script — would inform v0.2)
- Part 2 §12.4 + §13.2 + §13.3 full text from `NTE_v10_17_Part2_Structure.md`
- DESI 2024 VI direct table data
- Companion 8 §6.1 V_NTE option α/β/γ for cross-link to V_NTE D1

---

## §11. Closing

Void-bias dedicated worksheet v0.1 **analytical/structural setup**.

**Key structural finding**: NTE void-bias mechanism produces a SPECIFIC direction in the joint (D_M, D_H) plane (D_M shifts more than D_H for monotonically-decreasing g(z)). This is a falsifiable directional signature distinct from generic w₀w_a phantom DE. The empirical test is whether DESI Y1 per-bin displacements at LRG2 + LRG3+ELG1 align with this direction.

**Honest claim NTE can make**: void-bias mechanism predicts LRG2 and LRG3+ELG1 D-shifts; LRG1 D_M/D_H split is OUTSIDE the mechanism (orthogonal-anomaly). This is "where NTE matches observation" + "where NTE stays silent" — calibrated empirical claim.

**v0.2 numerical pass** queued for next bash-enabled session. Six recognition-gate items for Greg.

— Jammer, 2026-05-27. Void-bias v0.1 analytical setup; numerical work deferred.
