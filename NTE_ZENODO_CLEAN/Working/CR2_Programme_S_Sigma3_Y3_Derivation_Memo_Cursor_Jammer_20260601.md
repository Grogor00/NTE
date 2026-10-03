# Programme S — Explicit σ₃ / Y₃ mass matrix element on D_F (AJ-11)

**From:** Cursor Jammer  
**To:** Cursor Main (CR2 coordinator), AC, Scratch — Claude model, Greg  
**Cc:** Cursor AC  
**Date:** 2026-06-01  
**Re:** AJ-11 Programme S deliverables per `Working/CR2_B1_Killing2_Derivation_Memo_Cursor_Jammer_20260601.md` §5; cross-ref AJ-10, Scratch Killing2 candidate, Paper S6 §2, Companion 13 §2, Companion 7a §2  
**Verdict:** **NEEDS-MORE** — Programme S closure **not achieved**; explicit $D_F$ display yields **$Y_3 = 1$**, not $\sqrt{2/3}$; 2/3 pathway **not closed** and **not unique-by-derivation**; **no corpus patch**

---

## §0 — One-line summary

Programme S deliverables 1–4 were executed at the **structural identification** level available in Paper S6 + corpus ontology. The explicit σ₃ Dirac–Yukawa matrix element on $D_F$ under Chamseddine–Connes inner-fluctuation normalisation returns **$Y_3 = 1$** (corpus convention), **not** $Y_3 = \sqrt{2/3}$ from Killing-spinor/adjoint counting. Unified $\sigma_i$ treatment is **partial** (σ-transverse D5-inverse vs σ₃ Cartan unit coupling — principled split, not one dim-ratio). Chirality map C7a → Killing spinors is **structural only** (no unique spinor label for $\nu_3$). Dim-ratio alternatives **falsified on fit** except 2/3 / $\sqrt{2/3}$, but **fit ≠ derivation** — operator route does not select 2/3. **NEEDS-MORE**; maintain CR2 B1 honest scope.

---

## §1 — Programme S task (AJ-11 scope)

Per AJ-10 §5 and MAIN-15 queue registration, close or falsify:

| # | Deliverable | Target if Scratch pathway holds |
|---|-------------|--------------------------------|
| **S1** | Explicit σ₃ mass matrix element on $D_F$; $Y_3$ from Killing-spinor / Cartan projection | $Y_3 = \sqrt{2/3}$ (equiv. $m_{\nu_3} \times 2/3$) |
| **S2** | Unified $\sigma_i$ treatment for $\sigma_1, \sigma_2, \sigma_3$ | $(8\pi)^{-2/3}$ transverse + $(2/3)$ Cartan **without tuning** |
| **S3** | Chirality map: C7a superposition → which Killing spinor carries $\nu_3$ mass | Explicit embedding |
| **S4** | Falsify dim-ratio alternatives ($\sqrt{2/3}$, $1/2$, $3/4$, etc.) | 2/3 **unique from operator**, not numerology |

**Constraint:** Do **not** patch corpus unless **PASS** + AC ratify (Greg queue discipline).

---

## §2 — Setup: $D_F$ display used (Paper S6 §2)

Substrate spectral triple: $M = \mathrm{Hopf}\text{-}S^3 \times S^1_{\beta_{\mathrm{GB}}}$, $A_F = \mathbb{O} \oplus \mathbb{O}$, inner fluctuation split

$$D_F = D_F^{\mathrm{Dirac}} + D_F^{\mathrm{Majorana}}.$$

On the 3 × 3 RH neutrino flavor block (σ₃ eigenbasis; Paper S6 §2.4 schematic):

$$D_F^{\mathrm{Majorana}}\big|_{3 \times 3} = \begin{pmatrix} M_R & \text{(off-diag } \sigma_\pm) & 0 \\ \text{(off-diag)} & M_R^{(-)} & 0 \\ 0 & 0 & M_R^{(\mathrm{Cartan\text{-}orth})} \end{pmatrix},$$

with σ-projectors $P_{\sigma_3}^\pm = \frac{1}{2}(1 \pm \sigma_3)$ on the **2-dim Cartan–Weyl subspace** embedded in the block.

**Light-neutrino mass (seesaw, C13 §4):**

$$m_{\nu_i} = \frac{Y_i^2\, v_{\mathrm{EW}}^2}{M_R}, \qquad i \in \{1,2,3\} \leftrightarrow \{\sigma_1, \sigma_2, \sigma_3\}.$$

**Rep-theory anchor (B3 verdict):** fixed-sign Killing spinors on round $S^3$ → **dim 2**, **fundamental** of SU(2) (Bär 1993); adjoint gauge components → **dim 3** (κ₀ sector). **Not interchangeable.**

---

## §3 — Deliverable S1: Explicit σ₃ matrix element → $Y_3$

### §3.1 Dirac–Yukawa sector on σ₃

Chamseddine–Connes inner fluctuation on the σ₃ Cartan channel (Paper S6 §3.6; C13 §2):

$$D_F^{\sigma_3} \supset Y_3 \cdot \langle H \rangle \cdot P_{\sigma_3}^{+}, \qquad \langle H \rangle = v_{\mathrm{EW}} \text{ along } \sigma_3.$$

The **mass-matrix-relevant** Dirac entry is the (ν_L, ν_R) coupling in the σ₃-aligned subspace:

$$\boxed{\ \left(D_F^{\mathrm{Dirac}}\right)_{\sigma_3} = Y_3 \cdot v_{\mathrm{EW}} \cdot \mathbf{P}_{\sigma_3,\mathrm{Cartan}}\ }$$

with $\mathbf{P}_{\sigma_3,\mathrm{Cartan}}$ the rank-1 projector onto the Higgs-selected Cartan eigenspace within the flavor block.

### §3.2 Killing-spinor / Cartan projection attempt

**Step A — Killing bundle.** Fixed-sign Killing spinors $\varepsilon \in \mathbb{C}^2$ (fundamental). Cartan generator $\sigma_3$ acts as $\mathrm{diag}(+1,-1)$ on the σ₃ eigenbasis $\{|{\uparrow}\rangle, |{\downarrow}\rangle\}$.

**Step B — Cartan overlap (legitimate matrix element).** For a normalised Killing spinor $|\psi_K\rangle$:

$$\mathcal{C}_{\sigma_3}(\psi_K) = \langle \psi_K | P_{\sigma_3}^{+} | \psi_K \rangle = \frac{1}{2}\left(1 + \langle \psi_K | \sigma_3 | \psi_K \rangle\right) \in [0,1].$$

- On a σ₃ **eigenstate** ($|\psi_K\rangle = |{\uparrow}\rangle$): $\mathcal{C}_{\sigma_3} = 1$.
- On balanced superposition $|\psi_K\rangle = \frac{1}{\sqrt{2}}(|{\uparrow}\rangle + |{\downarrow}\rangle)$: $\mathcal{C}_{\sigma_3} = \frac{1}{2}$.

**Step C — Chirality-superposition Yukawa strength (C7a route).** For $|\nu\rangle = \alpha|\nu_L\rangle + \beta|\nu_R\rangle$ with $|\alpha|^2 + |\beta|^2 = 1$, the Dirac Yukawa coupling strength at unit normalisation is $| \alpha |^2 + | \beta |^2 = 1$ (balanced case) → **×1 on mass**, not 2/3 (AJ-10 §3.5; Scratch §6 honest scope).

**Step D — Dim-ratio normalisation (Scratch counting route).** Postulate:

$$Y_3^{\mathrm{count}} = \sqrt{\frac{\dim(\mathrm{fund\ Killing})}{\dim(\mathrm{adj\ SU(2)})}} = \sqrt{\frac{2}{3}} \approx 0.816.$$

**Problems (load-bearing):**

1. **Incomparable reps:** fundamental $\mathbb{C}^2$ vs real adjoint $\mathbb{R}^3$ — ratio requires a **chosen** Hilbert–Schmidt / trace normalisation, not a spectral-action output.
2. **Wrong object for σ₃:** σ₃ is **one Cartan generator** acting on spinors; κ₀'s "3" sums **gauge-field components** $A^a$, not neutrino multiplicity (B3 §3; C7 §4.2 footnote).
3. **Corpus does not overcount:** $Y_3 = 1$ is an **explicit EW-scale unit convention** for Cartan-aligned Higgs coupling (C13 §2; Paper S6 §3.6) — **not** an adjoint-3 sum (AJ-10 §3.3 **refuted** premise).

### §3.3 Result of explicit display

Under the **corpus spectral-action normalisation** (natural unit on σ₃ Cartan inner fluctuation):

$$\boxed{\ Y_3 = 1\ } \quad \Rightarrow \quad m_{\nu_3} = \frac{v_{\mathrm{EW}}^2}{M_R} = 0.0738\ \mathrm{eV}.$$

Under the **postulated dim-ratio normalisation** (not derived from displayed $D_F$):

$$Y_3 = \sqrt{2/3} \quad \Rightarrow \quad m_{\nu_3} = \frac{2}{3}\frac{v_{\mathrm{EW}}^2}{M_R} \approx 0.0492\ \mathrm{eV}.$$

**S1 status:** **NOT CLOSED.** Explicit $D_F$ identification yields **$Y_3 = 1$**. $\sqrt{2/3}$ requires **replacing** the corpus convention, not correcting a hidden adjoint overcount. Full J₃(𝕆) → 3 × 3 reduction from OctExt §5 remains **Programme S downstream** (Paper S6 §2.4 honest scope) — but the **normalisation choice** is already fixed at structural level in shipped corpus.

---

## §4 — Deliverable S2: Unified $\sigma_i$ treatment

### §4.1 Single $D_F$ decomposition (Paper S6 §3.3)

$$\mathrm{Tr}_F\left(D_F^2\right) = \sum_{i=1}^{3} \mathrm{Tr}_{\sigma_i}\left(D_F^2 P_{\sigma_i}\right) + \text{(cross terms)}.$$

| Mode | Geometric role | Majorana scale | Dirac Yukawa | Light mass |
|------|----------------|----------------|--------------|------------|
| **σ₁, σ₂** | Transverse; σ_± base-acting (Hopf $S^2$ coset) | $M_1, M_2$ (Pathway α / Z₂) | $Y_{\nu_2} = (8\pi)^{-1/3}$ (D5-inverse on **same** Killing–Hopf flux line) | $(8\pi)^{-2/3} v^2/M_R$ |
| **σ₃** | Cartan; fibre-generating (Hopf $S^1$) | $M_R$ | $Y_3 = 1$ (full Higgs Cartan coupling; **no** Hopf-flux suppression) | $v^2/M_R$ |

**Unified principle (structural, not dim-ratio):**

- **Transverse** modes: one power down from Majorana $(8\pi)^{1/3}$ → Dirac $(8\pi)^{-1/3}$ (C13 §3.2 duality).
- **Cartan** mode: Higgs-VEV-aligned → **unit** Yukawa; Theorem A (Paper S6 §5) — off-diagonal Higgs portal that supplies 4π base factor to σ₁/σ₂ **does not** apply on σ₃ Cartan states.

Predicted ratio at corpus register:

$$\frac{m_{\nu_3}}{m_{\nu_2}} = (8\pi)^{2/3} \approx 8.57 \quad \text{vs observed} \quad \sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.72\text{–}5.82.$$

### §4.2 Can 2/3 unify without tuning?

**Scratch claim:** only σ₃ picks up 2/3; σ₁/σ₂ retain $(8\pi)^{-2/3}$.

**Tension (AJ-10 F2; still open):** C13 **explicitly** places σ₁/σ₂ on the **Hopf–Killing-spinor flux line** — already a **dim-2 (fundamental)** normalisation via $(8\pi)$ volume. If 2/3 repairs σ₃ by Killing-vs-adjoint counting, a unified derivation must show:

- either σ₁/σ₂ flux line **already** encodes dim-2 (so σ₃ alone was wrongly adjoint-normalised) — **refuted** for $Y_3=1$ (§3.3);
- or Cartan alignment **bypasses** flux suppression **for a different reason** than dim 2/3 — **stipulated** (Paper S6 Theorem A / EW matching), not derived from one dim ratio.

**Attempted unified formula:**

$$Y_i = \mathcal{N}_i \cdot \Phi_i, \quad \mathcal{N}_{\sigma_1,\sigma_2} = (8\pi)^{-1/3},\ \mathcal{N}_{\sigma_3} = 1 \text{ (corpus)} \quad \text{or} \quad \sqrt{2/3}\ \text{(Scratch)}.$$

Only the **corpus** branch preserves solar Tier A without extra parameters. The **Scratch** branch fits both legs ~2% but **introduces** $\sqrt{2/3}$ **by hand** on σ₃ only.

**S2 status:** **NOT CLOSED.** Partial unified structure exists (one $D_F$ σ-decomposition); **2/3 unified closure fails** — σ₁/σ₂ escape is **stipulated**, not derived from the same dim-ratio operator.

---

## §5 — Deliverable S3: Chirality map C7a → Killing spinors

### §5.1 C7a content (Companion 7a §2)

Fundamental neutrino state in N:

$$|\nu\rangle = \alpha|\nu_L\rangle + \beta|\nu_R\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1,$$

with **incomplete Hopf projection** (minimal Higgs coupling) → chirality superposition persists. Meta-vantage gauge projection (SU(2)_L in +N) samples LH amplitude; **not** a fundamental chirality assignment.

### §5.2 Proposed map to Killing-spinor sector

| C7a / C7 object | Killing-spinor / Hopf object | σ mode | Mass channel |
|-----------------|------------------------------|--------|--------------|
| Chirality superposition $|\nu\rangle$ (both amplitudes) | **Both** fixed-sign Killing bundles active; $S^1$ fibre phase **unlocked** | **σ₃** (Cartan; strongly Higgs-coupled) | Atmospheric ($m_{\nu_3}$) |
| Gauge-projected $|\nu_L\rangle$ in +N | $P_L$ on fundamental $\mathbb{C}^2$ | Flavour / weak basis | Oscillation detection |
| Definite-chirality resolved fermion | Single-sign Killing locked; Hopf complete | N/A (not neutrino) | — |
| Transverse flavour structure | Hopf **base** $S^2$ coset modes | **σ₁, σ₂** | Solar ($m_{\nu_2}$) |

**Key identification:** $\nu_3$ mass is **not** carried by a **single** labelled Killing spinor ($\varepsilon^+$ vs $\varepsilon^-$). It is carried by the **Cartan-projected** chirality-superposed configuration — coupling through **$P_{\sigma_3}^+$** on the 2-dim fundamental space **plus** Higgs fibre alignment (Paper S6 §2.2: σ₃ fibre-generating on Hopf $S^1 \to S^3 \to S^2$).

### §5.3 Gap

C7a does **not** select $|\uparrow\rangle$ vs $|\downarrow\rangle$ vs $\frac{1}{\sqrt{2}}(|{\uparrow}\rangle+|{\downarrow}\rangle)$ for the mass eigenstate. EWSB selects **σ₃ direction in flavor/Cartan space**, not a unique Killing-spinor index. The embedding map **flavor σ₃ ↔ geometric Hopf fibre** is structural (Paper S6 Theorem C: winding = 1) but **does not** produce factor 2/3.

**S3 status:** **PARTIAL** — structural map documented; **no closed proof** that σ₃ mass eigenstate = specific Killing mode; **no** derivation of $Y_3$ from this map.

---

## §6 — Deliverable S4: Falsify dim-ratio alternatives

### §6.1 Numerical scan (single $M_R$, solar leg fixed)

Baseline: $m_{\nu_2} = (8\pi)^{-2/3} v^2/M_R = 0.00860$ eV (0.993× solar). Apply factor $f$ on σ₃ mass only:

$$m_{\nu_3} = f \cdot \frac{v^2}{M_R}, \qquad R \equiv \frac{m_{\nu_3}}{m_{\nu_2}} = f \cdot (8\pi)^{2/3}.$$

Observed: $R_{\mathrm{obs}} = \sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.72\text{–}5.82$ (NuFIT 6.0 / PDG 2024, NO).

| Candidate | $f$ or $Y_3$ | $R_{\mathrm{pred}}$ | $R_{\mathrm{pred}}/R_{\mathrm{obs}}$ | Fit |
|-----------|--------------|---------------------|--------------------------------------|-----|
| Corpus (S6/C13) | $f=1$, $Y_3=1$ | 8.57 | **1.47–1.50×** high | ❌ ratio |
| **Dim ratio 2/3** | $f=2/3$ | **5.716** | **0.98–1.00×** | ✅ |
| $Y_3 = \sqrt{2/3}$ | $f=2/3$ | 5.716 | 0.98–1.00× | ✅ (same) |
| $f = 1/2$ | 4.29 | **0.74–0.75×** | ❌ ~25% low |
| $f = 3/4$ | 6.43 | **1.10–1.12×** | ❌ ~10–12% high |
| $\sqrt{2}$ (PS-12 guard) | 12.1 | 2.1× | ❌ |
| $\pi/2$ (PS-12 guard) | 13.5 | 2.3× | ❌ |
| Chirality amplitude ×1 | $f=1$ | 8.57 | 1.47× | ❌ ratio |

**Fit uniqueness:** Among **dim-ratio-style** candidates, **only** $f = 2/3$ (equivalently $Y_3 = \sqrt{2/3}$) lands both legs within ~2%. **$1/2$ and $3/4$ are falsified on fit.**

### §6.2 Derivation uniqueness (distinct from fit)

| Route | $Y_3$ or $f$ | Status |
|-------|--------------|--------|
| Spectral-action EW unit (Paper S6) | $Y_3 = 1$ | **Corpus default** — overshoots ratio |
| Balanced C7a amplitude | $f = 1$ | **Refutes** 2/3 from amplitude |
| Hilbert–Schmidt $\|\sigma_3\|/\|\mathrm{adj}\|$ guess | $\sqrt{2/3}$ | **Stipulated** normalisation — not from $D_F$ display |
| Raw dim quotient $2/3$ | $f = 2/3$ | **Counting motivation only** — incomparable reps |

**S4 status:** **PARTIAL.** Alternatives **$1/2$, $3/4$, $\sqrt{2}$, $\pi/2$ falsified on fit**; **2/3 not falsified on fit** but **not selected by explicit operator** — derivation route yields **×1**, triggering Scratch falsifier **(a)** / AJ-10 **F1**.

---

## §7 — Falsifier table (AJ-10 §6 + Programme S)

| ID | Condition | AJ-11 status |
|----|-----------|--------------|
| **F1** | Explicit σ₃ derivation yields ×1 or $\sqrt{2/3}$ on **mass**, not 2/3 | **Triggered:** operator display → **×1** ($Y_3=1$); $\sqrt{2/3}$ only by **postulate** |
| **F2** | σ₁/σ₂ escape not derived from same structure | **Still open** — flux-line dim-2 already in $(8\pi)^{-1/3}$ |
| **F3** | κ₀ vs neutrino separation not principled | **Not triggered** — B3+C7 separate gauge vs flavor |
| **F4** | Observed ratio off 5.7–5.8 | **Not triggered** |
| **F5** | Corpus adjoint-overcounted $m_{\nu_3}$ | **Still refuted** |
| **F6** | $Y_3 \to \sqrt{2/3}$ breaks locked predictions | **Open** — PMNS rows, $M_R$ heat-kernel, leptogenesis scan not executed |

---

## §8 — Verdict

### §8.1 Programme S deliverables scorecard

| Deliverable | Result |
|-------------|--------|
| **S1** Explicit σ₃ / $Y_3$ on $D_F$ | ❌ **Not closed** — $Y_3 = 1$ from corpus display; $\sqrt{2/3}$ not derived |
| **S2** Unified $\sigma_i$ | ⚠️ **Partial** — σ-decomposition unified; 2/3 branch **not** unified without stipulation |
| **S3** C7a → Killing map | ⚠️ **Partial** — structural map; no unique spinor + no $Y_3$ |
| **S4** Falsify alternatives | ⚠️ **Partial** — $1/2$, $3/4$ failed on fit; 2/3 **not** derived-unique |

### §8.2 Overall verdict: **NEEDS-MORE**

| Criterion | Result |
|-----------|--------|
| Explicit $D_F$ yields $Y_3 = \sqrt{2/3}$ | ❌ Yields **$Y_3 = 1$** |
| Unified σᵢ without tuning | ❌ 2/3 requires σ₃-only postulate |
| Chirality–Killing map closed | ❌ Structural only |
| 2/3 unique from operator | ❌ Fit-unique, not derivation-unique |
| Numerical (2/3)(8π)^(2/3) | ✅ ~2% both legs (still compelling **research** direction) |
| Corpus patch warranted | ❌ **No** |

**Not FAIL outright** for the research programme: dim-2 vs dim-3 axis + numerical landing remain worth a **full J₃(𝕆) matrix extraction** (Paper S6 marginal M11). **Not PASS:** load-bearing steps fail; AJ-10 conclusions **confirmed** at Programme S depth.

### §8.3 Corpus discipline

- **Do not** patch C13, P5, S6, C7, or master with $m_{\nu_3} \times (2/3)$ or $Y_3 = \sqrt{2/3}$ until **PASS** + AC ratify.
- **Maintain** CR2 B1 honest scope: solar Tier A (0.993×); atmospheric ≈1.49× open.
- **Route PS-13** (Scratch adversarial on this memo) + hold MAIN-15 programme pointer.

### §8.4 Routing

| Stream | Action |
|--------|--------|
| **Cursor Scratch (PS-13)** | Adversarial F1–F6 on this memo |
| **Cursor Main** | Programme pointer unchanged; no 2/3 write |
| **AC** | B1 disposition unchanged; Programme S **NEEDS-MORE** |
| **Future Programme S** | Full OctExt J₃(𝕆) → displayed $D_F$ matrix; explicit $\mathrm{Tr}_F(D_F^2)|_{\sigma_3}$ coefficient |

---

## §9 — One-line verdict

**Programme S AJ-11: explicit $D_F$ σ₃ Yukawa returns $Y_3 = 1$, not $\sqrt{2/3}$; unified σᵢ and C7a–Killing map stay partial; 2/3 is fit-unique among dim ratios but operator-refuted; NEEDS-MORE — no corpus patch.**

— **Cursor Jammer**, 2026-06-01.
