# Bulk / no-boundary pre-temporal thesis v0.1

**Stream:** Jammer (R&D) — Greg insight + post-LB-1 derive queue  
**Date:** 2026-05-23  
**Status:** **Structural resolution proposed** — sharpens BR2c, BR2d-J3, R4a  
**Scripts:** `j6_n1b_bulk_boundary_numerics.py`; `j6_e3_saddle_numerics.py`  
**Parents:** `Jammer_LB1_Exhaustive_Resolution_v0_1`; `Jammer_J6_n4_BR2d_*`; Part 1 §2.1.4; Companion 9 §5.1

---

## §0. Greg thesis (one paragraph)

> *Just because the temporal epoch **is** $S^3$ does not mean the pre-temporal epoch **was** $S^3$. Perhaps it was **all bulk and no boundary** — and the $S^3$ cosmological slice **crystallises at gauge birth**.*

**Jammer reading:** This is not a rejection of NTE axioms; it **completes** them. The temporal manifold is $S^3$ (§2.2). The pre-temporal regime is **Euclidean bulk** (HH $S^4$ / octonionic $S^7$) with **no sharp 3-boundary** as the operative cosmological slice. **Gauge birth $G$** is the event where the **boundary comes into existence** and the **holonomic constraint** $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ **turns on**. LB-1 two-sector resolution is the **operational form** of this ontology.

---

## §1. Three geometric regimes (not two)

| Regime | Geometry | Constraint $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ | Primary coordinate | Role |
|--------|----------|--------------------------------|--------------------|------|
| **Bulk pre-temporal** | Euclidean 4D saddle ($S^4$ HH) / $S^7$ octonion bulk | **OFF** — no boundary slice | $N$ (bulk e-folds) | Sector 1 / Role B |
| **Boundary birth** | $S^3$ **nucleates** | **Switches ON** | $y\in[0,N_{\rm lock}]$ | Sector 0 / Stage 3 |
| **Temporal post-$G$** | Lorentzian $S^3$ cosmology | **ON** (boundary field) | $t$ emergent; $N$ terminal | Sector 2 / Role A |

**Numeric separation (script):**

$$N_e = 63.4 \quad\text{(bulk depth)} \qquad N_{\rm lock} = 0.105 \quad\text{(boundary width)} \qquad \frac{N_e}{N_{\rm lock}} \approx 602$$

The ratio is **not** a conversion factor — it is the ratio of **bulk inflation depth** to **boundary-formation thickness**.

---

## §2. Why this dissolves the remaining LB-1 puzzles

| Puzzle | Old framing | Bulk/no-boundary reading |
|--------|-------------|--------------------------|
| $n_s$ vs lock endpoints | One $H(N)$ must do both | Bulk slow-roll sets $n_s$; boundary roll sets lock |
| $|\Phi_{\rm inf}| \ll |\Phi_{\rm NTE}|$ at HH | “Two fields?” | **Bulk inflaton** vs **premature boundary projection** of constraint |
| BR2 exponential $n_s=-1$ | Exponential “wrong” | Constraint **mis-applied in bulk** — category error |
| $N_{\rm lock}\neq N_e$ | Prose conflation | **Different objects:** boundary width vs bulk depth |
| Stage 3 linear $y$-profile | Mysterious thin chart | **Boundary nucleation profile** |
| HH no-boundary vs $S^3$ modes | Tension in §2.1.3 | **No $S^3$ boundary at Janus** — bulk closes at $\tau=0$; $S^3$ at $G$ |

---

## §3. Corpus alignment (what already says this)

| Source | Content |
|--------|---------|
| Part 1 §2.1.4 | HH table: Euclidean pre-temporal; “No-boundary ($S^4$) ↔ Janus (no boundary at $N=0$)” |
| Companion 9 §5.1 | HH **no-boundary** at $\tau=0$: $a\to0$ regularly — **bulk** closing |
| Part 1 §2.1.3(f) | Octonion $S^7$ bulk; $S^3$ as **quaternionic fibre** — fibre **not** yet physical boundary |
| §17.5.19 | Role (B) pre-temporal; Role (A) post-locking |
| BR2d-J1 | Dual charts at $G$ — now interpreted as **bulk chart** vs **boundary chart** |
| Audit §17.5.4 | $N_{\rm lock}=S_{\rm dS}/4$ uses $H^{(F)}$ — **boundary entropy** at birth |

**Corpus tension to patch (LB-6):** §2.1.3(a) “$S^3$ boundary supports spinor modes pre-temporally” → rephrase: **bulk spinor modes on $S^7$/HH geometry** that **project to $S^3$ Dirac spectrum at $G$** (spectral triple flow §17.5.x).

---

## §4. Crystallisation event $G$ (BR2d-J3 target)

### §4.1 Physical sequence

```
BULK (Euclidean)                    BOUNDARY BIRTH              TEMPORAL S^3
  V_eff(Phi) slow-roll                  y: 0 -> N_lock              H = alpha |Phi_NTE|^2
  Phi_inf ~ 16 M_Pl,red                 S^3 nucleates               terminal roll
  N: 0 -> ~63 (CMB modes)               constraint ON               dt = dN/(alpha|Phi|^2)
  NO H = alpha|Phi|^2                   Wick / gauge birth          SM + Born + Hopf
        |                                     |                            |
        +------------- event G ---------------+----------------------------+
```

### §4.2 What switches on at $G$

| Structure | Pre-$G$ (bulk) | Post-$G$ (boundary/temporal) |
|-----------|----------------|------------------------------|
| $S^3$ cosmological slice | absent as operative manifold | **present** |
| $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ | inactive | **active** |
| U(1) / Hopf / Born | absent | **activated** (Gap 5) |
| SM gauge groups | octonionic pre-structure | **crystallised** (G₂→SM) |
| Real time $t$ | $t=i\Delta N$ only | **Lorentzian** $dt=dN/(\alpha|\Phi|^2)$ |
| Thermal $H^{(F)}$ | — | Friedmann($T_{\rm GB}$) reading |

### §4.3 R4 field map (bulk → boundary projection)

**Not** magnitude identity. **Projection:**

$$\Phi_{\rm bulk}(N) \xrightarrow{\text{at }G} \text{boundary data } \big(|\Phi_{\rm NTE}|, H^{(\alpha)}, H^{(F)}\big)$$

**Z₂ / Janus:** bilateral bulk reads as **two orientations**; boundary birth selects **one** Lorentzian sheet + CPN partner structure.

**Numeric (script):** $\Phi_{\rm bulk}/\sqrt{M_{\rm Pl}/\alpha} \sim 10^{-13}$ at HH scale if constraint were wrongly applied — confirms **constraint is post-crystallisation**.

---

## §5. J6-n1b numerics (bulk Sector 1 + boundary Sector 2)

| Test | Result |
|------|--------|
| Bulk E3 / scaled saddle | $H\sim M_{\rm Pl}$ achievable **without** $\alpha$ in potential scale (J6-n1 T1) |
| $\Phi^2$-chaotic (bulk) | $n_s=0.9669$ numeric; $0.9684$ analytic (J6-n1 T2) **PASS** |
| Literal E3 + corpus $\alpha$ | $H/M_{\rm Pl}\sim10^{-26}$ **FAIL** — bulk saddle scale $\neq$ cosmological $\alpha$ |
| Constraint eq.(7) in bulk | $n_s\to1$ or $-1$ **FAIL** — proves constraint **off** in bulk |
| Boundary Sector 2 roll | $N_e=63.4$, $H^{(\alpha)}$, $|\Phi|=M_{\rm Pl}$ **PASS** (BR2) |

**Register:** Bulk dynamics **must not** use Appendix B constraint as equation of motion pre-$G$. Post-$G$, constraint is **holonomic** (J1 sign-off).

---

## §6. BR2d-J3 derive programme (revised)

**Target:** Derive crystallisation map from Appendix B.3 + Paper S2 Hopf-$S^3\times S^1_\beta$ geometry.

**Lemma candidates:**

1. **Bulk phase:** path integral dominated by $S^4$ HH saddle; **no** Lagrange multiplier $\mu(H-\alpha\Phi^2)$ in bulk measure.
2. **Birth phase:** boundary term $\propto \delta(\text{Hopf fibre})$ + $\mu$ activates → $S^3$ unit cell ${\rm Vol}(S^3)=2\pi^2$ (links to R6 $\Lambda$).
3. **Matching:** $N_{\rm lock}=S_{\rm dS}/4$ from **boundary** entropy; $N_e=-\ln(\alpha M_{\rm Pl})$ from **bulk-to-lock** depth.

**Success criteria (unchanged + sharpened):**

- C⁰ $|\Phi|^2$ at $G$ without ad hoc $\Phi_0$ tuning  
- Derive **why** $N_{\rm lock}\ll N_e$ from bulk/boundary dimension count  
- Sector 1 $H(N)$ from bulk E3 ODE **continuous** with Stage 3 endpoint in **boundary** chart only  

---

## §7. Dead ends (bulk lens)

| Route | Verdict |
|-------|---------|
| Pre-temporal **was** full $S^3$ cosmology with $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ | **Excluded** — creates LB-1 false contradiction |
| $S^3$ modes exist at Janus with U(1)/Born | **Excluded** — gauge birth **creates** Hopf |
| Single geometry for bulk and boundary | **Excluded** — HH $S^4$ vs temporal $S^3$ |
| $\alpha$ sets bulk inflaton scale | **Excluded** — J6-n1 $10^{-26}$ H deficit |
| Global $y\propto N$ | **Excluded** — ratio $\sim602$ |

---

## §8. Proposed corpus language (AC patch LB-6)

> **Pre-temporal bulk / temporal boundary (Greg 2026-05-23; Jammer v0.1):** The Hartle–Hawking epoch is **bulk-dominated** (Euclidean saddle; no operative $S^3$ cosmological slice). The **temporal** epoch is **$S^3$** (§2.2). **Gauge birth** is **boundary crystallisation**: the $S^3$ slice, the constraint $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$, gauge/Hopf structure, and Lorentzian continuation **switch on** at event $G$. Pre-temporal CMB physics samples **bulk** $V_{\rm eff}$ (Role B); post-$G$ cosmology samples **boundary** constraint roll (Role A). $N_{\rm lock}$ is **boundary-formation width**; $N_e$ is **bulk inflation depth**.

---

## §9. Queue status after this lift

| ID | Status |
|----|--------|
| LB-1 | **CLOSED** (two-sector) |
| **LB-6** | **NEW** — bulk/no-boundary ontology + §2.1.3 patch |
| J6-n1b | **PARTIAL** — bulk/boundary numerics v0.1 |
| BR2d-J3 | **SHARPENED** — crystallisation derive |
| R4a | **SHARPENED** — bulk→boundary Z₂ projection |
| R6 Λ | Unchanged — $2\pi^2$ is **boundary** unit cell post-$G$ |

---

## §10. Falsifiers

1. Derived pre-$G$ dynamics **requires** $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ in bulk → contradicts J6-n1 constraint track  
2. $N_{\rm lock}\approx N_e$ from first principles → contradicts $S_{\rm dS}/4$ vs $-\ln(\alpha M_{\rm Pl})$  
3. $\Phi_{\rm bulk}=\Phi_{\rm NTE}$ at HH without projection map  
4. U(1)/Born structure in bulk without gauge birth  

---

## §11. Sunshine (one sentence)

*The pre-temporal epoch was not a smaller $S^3$ — it was **bulk without boundary**; the temporal epoch **is** $S^3$ because **the boundary was born at $G$**.*

— Jammer bulk/no-boundary v0.1, 2026-05-23.
