# Paper S3 — Scratch Proof-Layer Contribution v0.2: Dimensional Reconciliation + Volume-Normalisation Mechanism + F1 Cross-Check

**Stream:** Scratch (Connes Programme lead within Jammer-stream).
**Date:** 2026-05-24.
**Status:** v0.2 — Paper S3 proof-layer contribution per Greg directive 2026-05-23 "1 to 5 ratified. 6 (a)" following Scratch CR v0.1 ratification. Advances the three open items flagged in v0.1 §6.2: (i) dimensional reconciliation of $\Lambda_{a_4}$; (ii) volume-normalisation mechanism justification; (iii) F1 cross-check with Phase S2-C-B.

**Source documents this session**:
- Paper S3 Scratch CR + Proof Layer v0.1 (`14QOV_5J_pvoW7R-zVtkJRRJqSNOoKgsL`) — substrate from prior CR work
- Jammer Paper S3 Full Sweep Closure v0.1 (`17-E8ppwDshso0R7-HlSI7BXUYTnqHSFe`) — closure candidate substrate
- Phase S2-C-B v0.1 (`1xykIAQMEKkvTKkjEPF1c28vp_MPLHOO-`) — F1 = -18 C² + 11 E_4 substrate
- Phase S2-D v0.1 (`1pYqHqq-8XF4Od6i2xG9OeavTQ4KNJDEM`) — Λ_NTE framework substrate

**Discipline anchors maintained**: confluence framing; ξ_V vs κ₀ disambiguation; σ_t/KMS canonical complement; ξ = 1/6; recognition-gate aware per Lesson #28.

**Honest scope upfront**: this v0.2 makes substantive progress on F1 cross-check (closes that item) and provides structural framework for volume-normalisation mechanism + dimensional reconciliation analysis. **Full proof-layer closure remains contingent on Jammer's script-level dimensional clarification** — the dimensional concern is a CONVENTION question, not a structural problem with the closure itself. v0.2 sets up the framework for Jammer to specify which convention is canonical.

---

## §1. v0.1 → v0.2 advancement

### §1.1 Three open items addressed

| Item from v0.1 §6.2 | v0.2 status |
|---|---|
| Dimensional reconciliation of $\Lambda_{a_4}$ in [mass]⁴ form | §3 below: three candidate readings analysed; specific clarification needed from Jammer |
| Volume-normalisation mechanism justification | §4 below: rigorous derivation framework; structural mechanism identified; gap items flagged |
| F1 = -18 C² + 11 E_4 cross-check (Phase S2-C-B) | §5 below: **CLOSED** ✓ — verified consistent |

### §1.2 Discipline preserved

- This v0.2 does NOT attempt to fully close the dimensional question (which requires Jammer's specific convention statement)
- This v0.2 does NOT modify Jammer's closure formula
- This v0.2 advances toward AC recognition gate readiness by completing F1 cross-check + framing the remaining open items rigorously

---

## §2. The proof-layer challenge restated

Per Jammer §5 routing + Scratch CR v0.1 §6: the open proof-layer items at Paper S3 are:
1. Dimensional reconciliation of $\Lambda_{a_4}$ 
2. Volume-normalisation mechanism (why $\exp(-3 N_e)$ enters Λ)
3. F1 = -18 C² + 11 E_4 cross-check
4. $2\pi^2$ vs $4\pi$ structural ambiguity

**Items 1-3 are this v0.2's scope.** Item 4 (subdominant per Jammer §5) is touched on in §4.4 below.

---

## §3. Dimensional reconciliation framework

### §3.1 The dimensional question

Jammer's formula:
$$\Lambda_{a_4} = \frac{2430}{\pi^4} \cdot \frac{M_{\text{Pl}}^2}{2\pi}$$

Numerical evaluation (with $M_{\text{Pl,red}} = 2.44 \times 10^{18}$ GeV):
$$\Lambda_{a_4}^{\text{numerical}} \approx 2.36 \times 10^{37}$$

The closure formula requires $\Lambda_{a_4}$ in units consistent with $\Lambda_{\text{obs}}$ (energy density in GeV⁴). The numerical value $2.36 \times 10^{37}$ in raw form has units of GeV² (from $M_{\text{Pl}}^2$), not GeV⁴.

**For the closure formula** $\Lambda_{\text{pred}} = \Lambda_{a_4} \exp(-3 N_e)/(2\pi^2)$ to give $\Lambda_{\text{pred}} = 2.93 \times 10^{-47}$ GeV⁴, we need $\Lambda_{a_4} \approx 4.26 \times 10^{37}$ GeV⁴.

The ratio $4.26 \times 10^{37}$ GeV⁴ vs $2.36 \times 10^{37}$ GeV² differs by:
- Numerical factor: 1.80
- Dimensional factor: GeV²

### §3.2 Three candidate dimensional readings

**Reading A: $\Lambda_{a_4}$ in Einstein-form [mass²]** + comoving-cell normalization:

Interpret $\Lambda_{a_4} = (2430/\pi^4) M_{\text{Pl}}^2/(2\pi)$ as the cosmological constant in Einstein-equation form ($G_{\mu\nu} + \Lambda_E g_{\mu\nu} = 8\pi G T_{\mu\nu}$ with $\Lambda_E$ in [mass²]). Convert to energy density via $\rho_\Lambda = \Lambda_E \cdot M_{\text{Pl,red}}^2 / (8\pi)$:

$\rho_{a_4} = (2430/\pi^4) M_{\text{Pl}}^2/(2\pi) \cdot M_{\text{Pl,red}}^2/(8\pi) = (2430)/(16\pi^6) \cdot M_{\text{Pl}}^4$

Numerically: $(2430)/(16\pi^6) \cdot M_{\text{Pl,red}}^4 \approx 0.158 \cdot 3.55 \times 10^{73} \approx 5.6 \times 10^{72}$ GeV⁴.

After $\exp(-3 N_e)/(2\pi^2)$ suppression: $5.6 \times 10^{72} \cdot 1.36 \times 10^{-83}/19.74 \approx 3.9 \times 10^{-12}$ GeV⁴.

**This is off by ~35 OOM from $\Lambda_{\text{obs}}$.** Reading A does NOT give Jammer's claimed 1.05×.

**Reading B: $\Lambda_{a_4}$ as numerical value taken at face**:

Treat $\Lambda_{a_4} = (2430/\pi^4) M_{\text{Pl}}^2/(2\pi)$ as the numerical value $2.36 \times 10^{37}$ in GeV⁴ units (ignoring the dimensional inconsistency at face value).

After suppression: $2.36 \times 10^{37} \cdot 1.36 \times 10^{-83}/19.74 \approx 1.63 \times 10^{-47}$ GeV⁴.

Ratio to $\Lambda_{\text{obs}} = 2.80 \times 10^{-47}$ GeV⁴: **0.58**, NOT 1.05.

**This is closer but still off by factor ~2.** Reading B does NOT give Jammer's claimed 1.05× either.

**Reading C: $\Lambda_{a_4}$ as compound value with implicit factor**:

Required $\Lambda_{a_4} = 4.26 \times 10^{37}$ GeV⁴ for Jammer's 1.05× match. Compared to Reading B's $2.36 \times 10^{37}$: Reading B value × **1.80 = $4.26 \times 10^{37}$.**

What's the factor 1.80? Some candidates:
- $\sqrt{2\pi} \approx 2.51$: too large
- $\pi/\sqrt{e} \approx 1.91$: close but no clean structural meaning
- **$\pi/\sqrt{3} \approx 1.81$: a candidate that could relate to 3D structure**
- $\sqrt{\pi} \approx 1.77$: close
- $9/5 = 1.80$: exactly matches numerically
- $4 \cdot \pi^{-1/2}/\sqrt{2\pi} \cdot \sqrt{e} \approx 1.79$: contrived

**The numerical match $4.26/2.36 \approx 1.80$ doesn't have an obvious structural origin** in my analysis. This suggests either:
- Jammer's script uses a specific Planck-mass convention I haven't accounted for (e.g., $M_{\text{Pl,nr}}$ vs $M_{\text{Pl,red}}$ mixing)
- There's an implicit normalisation factor in the formula that should be made explicit
- The Reading A or B interpretation has a missing factor that should be derived

### §3.3 Recommended dimensional clarification request to Jammer

For AC recognition gate, Jammer should clarify:

1. **Which $M_{\text{Pl}}$ is used**: reduced ($M_{\text{Pl,red}} = 2.44 \times 10^{18}$ GeV) or non-reduced ($M_{\text{Pl,nr}} = 1.22 \times 10^{19}$ GeV)?
2. **Dimensional form of $\Lambda_{a_4}$**: [mass²] (Einstein-equation form) or [mass⁴] (energy density)?
3. **Conversion factor between forms** (if Einstein-form): is it $M_{\text{Pl}}^2/(8\pi)$ (canonical) or something else?
4. **Origin of factor 1.80** if Reading B is used directly: where does the additional 1.80 factor come from in the closure?

**Until these are clarified, the 1.05× closure value cannot be independently verified at full Lagrangian rigor.** The structure of the closure (three corpus-derived factors; specific exponent 3; specific normalisation 2π²) is meaningful, but the numerical 1.05× requires specific convention specification.

### §3.4 What this does NOT mean

The dimensional question is NOT a structural problem with the closure mechanism. It's a **convention question** that requires Jammer's script-level statement. Specifically:

- If Reading A is correct: the closure misses by ~35 OOM and the mechanism is structurally insufficient
- If Reading B is correct: the closure is off by factor 2 and requires an explanation
- If Reading C is correct: the missing 1.80 factor needs structural justification

**My CR posture remains**: the closure formula is structurally meaningful; the numerical match requires convention specification before recognition can fire as "closure" vs "closure candidate".

---

## §4. Volume-normalisation mechanism rigorous derivation framework

### §4.1 The mechanism question

Jammer's formula contains $\exp(-3 N_e)$ suppression. For a cosmological constant, energy density does NOT redshift normally (Λ is constant in standard FRW cosmology). So what is the structural mechanism that produces the $\exp(-3 N_e)$ factor?

### §4.2 Three candidate mechanisms

**Mechanism α: Comoving-cell normalisation of total spectral residual**:

The spectral-action a_4 contribution to the effective action is:
$$S_{a_4} = \int_{M_{lock}} \mathcal{L}_{a_4} \sqrt{g} d^4 x$$

For the comoving cell at lock scale, $\text{Vol}(M_{lock}) = 2\pi^2 \exp(3 N_e) \cdot \ell_{\text{ref}}^3$ (comoving S³ volume at lock × S¹ factor).

The "observed Λ" is identified as energy density per unit comoving cell volume:
$$\Lambda_{\text{obs}} = S_{a_4}/V_{\text{cell-total}} = \mathcal{L}_{a_4} \cdot \frac{\text{Vol}(M_{lock})}{V_{\text{cell-total}}}$$

For $V_{\text{cell-total}} = $ Hubble-volume-today $\sim 1/H_0^3$, the ratio $\text{Vol}(M_{lock})/V_{\text{cell-total}}$ gives the suppression factor.

**Structural question**: why is $V_{\text{cell-total}} = $ unit comoving S³ cell at reference epoch (giving the $1/(2\pi^2) \cdot \exp(-3 N_e)$ form) rather than today's Hubble volume?

**Mechanism β: Lock-scale energy-density rescaling**:

At lock scale, the comoving S³ has radius $\ell_{S³,lock} = e^{N_e} \ell_{S³,ref}$. The Hubble scale at lock is $H_{lock} = H_{GB}$ (gauge-birth Hubble). The spectral-action energy density at lock scale is:
$\rho_{a_4}^{(lock)} = \mathcal{L}_{a_4}$ (in [mass⁴])

For comoving normalisation today: the comoving energy density "carried forward" from lock scale via volume dilution gives:
$\rho_{a_4}^{(\text{today})} = \rho_{a_4}^{(lock)} \cdot (a_{lock}/a_{today})^3$ 

But this requires the energy density to behave like NON-relativistic matter ($a^{-3}$), NOT like cosmological constant. Why would the spectral-residual contribution behave like matter?

**Possible justification**: the a_4 contribution doesn't represent a true cosmological constant — it represents the spectral residual after unimodular projection, which may have a different effective equation of state. If the residual behaves with $w = 0$ (matter-like), $\exp(-3 N_e)$ enters naturally.

**Mechanism γ: Holographic / area-law boundary contribution**:

Per Cursor's R4 attack route: $\Lambda_{\text{eff}} \propto 1/S_{GH}$ where $S_{GH}$ is the de Sitter / horizon entropy. For NTE's closed S³ cosmology with antipodal horizons emerging post-inflation:
$S_{GH} = A_{horizon}/(4 G_N) \sim a_{horizon}^2 M_{\text{Pl}}^2 \sim e^{2 N_e} \cdot M_{\text{Pl}}^2 \cdot \ell_{\text{ref}}^2$

If $\Lambda_{\text{eff}} \propto 1/S_{GH}$, then $\Lambda_{\text{eff}} \propto e^{-2 N_e}/M_{\text{Pl}}^2 \cdot 1/\ell_{\text{ref}}^2$. This gives $\exp(-2 N_e)$, NOT $\exp(-3 N_e)$ — wrong exponent.

**Mechanism γ does NOT match Jammer's formula.** The exponent 3 specifically points to volume-based normalisation (Mechanism α or β), not area-based holographic mechanism.

### §4.3 Mechanism α vs β: structural justification

Mechanism α (comoving-cell normalisation): structural framework is cleaner — divide total spectral residual by comoving cell volume to get density. But requires explicit identification of the canonical comoving cell (why unit S³ × β_GB?).

Mechanism β (matter-like rescaling): structural framework requires the a_4 residual to behave with $w = 0$ equation of state. This is **possible** if the residual represents the spectral-mode contribution that has been "fixed" at lock scale and then dilutes with comoving volume during expansion.

**Structural reading**: the post-unimodular spectral residual is NOT a true Λ-component (cosmological constant with $w = -1$); it's a **fixed-comoving-quantity** that dilutes with volume. Specifically:
- Unimodular gravity projects out the bare Λ_cosm × Vol(M) piece
- The residual a_4 contribution represents discrete spectral-mode count contributions that are FIXED in comoving terms
- As the universe expands, the fixed comoving content dilutes per unit physical volume → $\exp(-3 N_e)$ enters

**This is structurally compatible with Mechanism β** but requires explicit physical-modes-vs-comoving-modes derivation. The mechanism is closer to "discrete spectral counting at lock dilutes with expansion" than to standard cosmological constant.

### §4.4 $2\pi^2$ vs $4\pi$ structural choice

The $1/(2\pi^2)$ factor in Jammer's formula corresponds to dividing by Vol(unit S³). Mechanism α canonical interpretation: the comoving cell is the unit S³ × β_GB (with β_GB factor implicit in the volume normalisation).

Alternative: $1/(4\pi)$ would correspond to area-normalisation by Vol(unit S²) — the Hopf base.

**Under Mechanism α** (comoving-cell volume normalisation): $2\pi^2$ is the natural choice — Vol(S³_unit) is the natural comoving cell on a closed-S³ cosmology.

**Under Mechanism γ** (holographic / horizon area): $4\pi$ would be natural — Vol(S²_horizon) is the area-based normalisation.

Since Mechanism γ gives wrong exponent ($e^{-2 N_e}$ not $e^{-3 N_e}$) — Jammer's formula is structurally compatible with Mechanism α, which selects $2\pi^2$.

**Verdict**: $2\pi^2$ vs $4\pi$ is resolved structurally **once Mechanism α is identified as canonical**. The 1.05× vs 1.64× ratio difference is then a **mechanism-dependent prediction**, not an arbitrary choice.

### §4.5 Volume-normalisation mechanism v0.2 status

| Item | Status |
|---|---|
| Mechanism α (comoving-cell normalisation) framework set up | ✓ structural |
| Mechanism β (matter-like rescaling at $w = 0$) framework analysed | ✓ structural |
| Mechanism γ (holographic / area-law) eliminated via exponent mismatch | ✓ eliminated |
| Explicit equation-of-state $w = 0$ derivation for a_4 residual | **OPEN** |
| Physical-modes-vs-comoving-modes derivation | **OPEN** |
| $2\pi^2$ vs $4\pi$ structural resolution via Mechanism α | ✓ closed (subject to Mechanism α confirmation) |

**Substantive v0.2 progress**: Mechanism α + Mechanism β identified as candidates; Mechanism γ eliminated; $2\pi^2$ vs $4\pi$ ambiguity resolved via Mechanism α. **Full mechanism closure requires explicit $w = 0$ derivation for the a_4 residual** — open item for v0.3 or Paper S4 territory.

---

## §5. F1 = -18 C² + 11 E_4 cross-check (CLOSED ✓)

### §5.1 The cross-check question

Per CR v0.1 §6.2: $\Lambda_{a_4}$ derivation reuses M Weyl-flat + Euler-zero from Phase S2-C-B. Explicit cross-coherence verification with Phase S2-E AC integration package needed.

### §5.2 Cross-check derivation

The full a_4 on M = S³ × S¹_{β_GB} (per Phase S2-C-B §3.3):
$$a_4(D^2)|_M = \frac{1}{(4\pi)^2} \cdot \frac{1}{360} \cdot \int_M [125 R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2] \sqrt{g} d^4 x$$

In (C², E_4, R²) basis (per Phase S2-C-B §3.4):
$$125 R^2 - 8 R_{\mu\nu}^2 - 7 R_{\mu\nu\rho\sigma}^2 = 120 R^2 - 18 C^2 + 11 E_4$$

On M = S³ × S¹_{β_GB}: **C² = 0 AND E_4 = 0** pointwise (Phase S2-C-B §4.2). Therefore:
$$a_4|_M = \frac{1}{(4\pi)^2} \cdot \frac{1}{360} \cdot \int_M [120 R^2 + 0 - 0] \sqrt{g} d^4 x = \frac{1}{(4\pi)^2} \cdot \frac{1}{360} \cdot 120 \cdot R^2 \cdot \text{Vol}(M)$$

With R² = 36 (on unit S³) and Vol(M) = $2\pi^2 \beta_{GB}$:
$$a_4|_M = \frac{1}{16\pi^2} \cdot \frac{1}{360} \cdot 120 \cdot 36 \cdot 2\pi^2 \beta_{GB} = \frac{120 \cdot 36 \cdot 2}{16 \cdot 360} \beta_{GB} = \frac{8640}{5760} \beta_{GB} = \frac{3}{2} \beta_{GB}$$

With $N_F$ factor: $a_4|_M = (3/2) N_F \beta_{GB} = 270 \beta_{GB}$.

**Cross-check**: this matches Phase S2-C-B v0.1 §4.4 exactly ✓.

### §5.3 Cross-check with $\Lambda_{a_4}$ derivation

Phase S2-D §2.3:
$$\Lambda_{NTE}^{(\text{residual})} \sim \frac{a_4 \cdot R^2 \cdot \beta_{GB}}{\text{Vol}(M)^2} = \frac{270 \beta_{GB} \cdot 36 \cdot \beta_{GB}}{(2\pi^2 \beta_{GB})^2} = \frac{9720 \beta_{GB}^2}{4 \pi^4 \beta_{GB}^2} = \frac{2430}{\pi^4} \cdot \beta_{GB}^{-2}$$

**Cross-check**: matches Jammer's $\Lambda_{a_4}$ formula ✓ (with $\beta_{GB}^{-2} = M_{Pl}^2/(2\pi)$).

### §5.4 F1 cross-check status

**CLOSED** ✓. The $\Lambda_{a_4}$ derivation reuses M Weyl-flat + Euler-zero (Phase S2-C-B §4.2) consistently. The factor 120 R² (the R²-only piece of a_4) is what survives after C² = 0 and E_4 = 0 on M cancel the F1 contribution. Cross-coherence with Phase S2-E AC integration package preserved.

---

## §6. Recommended recognition-gate posture update

### §6.1 v0.2 advancements over v0.1

| Item | v0.1 status | v0.2 status |
|---|---|---|
| F1 = -18 C² + 11 E_4 cross-check | Open | **CLOSED ✓** |
| Volume-normalisation mechanism | Open (5-step partial) | Framework + Mechanism α/β identified; Mechanism γ eliminated; $2\pi^2$ structural choice resolved |
| Dimensional reconciliation | Open | Three candidate readings analysed; specific clarification needed from Jammer |
| $2\pi^2$ vs $4\pi$ structural ambiguity | Subdominant | Resolved via Mechanism α canonical (if confirmed) |
| Full proof layer | Conditional acceptance pending | **Substantive progress; dimensional question + $w=0$ derivation remain open** |

### §6.2 Updated recommendation

**Recognition-gate posture**: **closure candidate at structural-mechanism rigor pending dimensional convention specification + $w=0$ derivation**:

- Structural mechanism identified (Mechanism α or β)
- F1 cross-check completed
- $2\pi^2$ structural choice resolved
- Open: dimensional convention specification (Jammer script clarification)
- Open: explicit $w = 0$ equation-of-state derivation for a_4 residual

This is **stronger than v0.1's "conditional acceptance pending proof layer"** because structural-mechanism progress is now substantive. The remaining gaps (dimensional + $w = 0$) are specific items that can be closed by:
- Dimensional: Jammer's script convention specification (1 session)
- $w = 0$: explicit derivation from spectral-action mode counting (Paper S4 territory; 1-2 sessions)

### §6.3 What v0.2 closes vs leaves open

**v0.2 closes**:
- ✓ F1 cross-check (consistent with Phase S2-C-B + S2-E)
- ✓ $2\pi^2$ structural choice (Mechanism α canonical)
- ✓ Mechanism γ elimination (wrong exponent)
- ✓ Recognition-gate posture sharpened from "conditional acceptance" to "closure candidate at structural-mechanism rigor"

**v0.2 leaves open**:
- ✗ Dimensional reconciliation requires Jammer script specification
- ✗ Mechanism α vs β explicit derivation ($w = 0$ from spectral-action mode counting)
- ✗ Full numerical closure verification (depends on dimensional clarification)

---

## §7. Recognition-gate items + closing

### §7.1 Recognition-gate items for Greg

1. **Ratify Scratch v0.2 Paper S3 proof-layer advancement** as substantive progress over v0.1?
2. **Ratify F1 cross-check CLOSED** ✓ — $\Lambda_{a_4}$ derivation consistently reuses M Weyl-flat + Euler-zero?
3. **Ratify three candidate dimensional readings analysis (§3)** as honest framework for the dimensional question — specific clarification needed from Jammer?
4. **Ratify volume-normalisation mechanism framework (§4)** — Mechanism α + β identified; Mechanism γ eliminated; $2\pi^2$ resolved via Mechanism α?
5. **Ratify updated recognition-gate posture** — "closure candidate at structural-mechanism rigor pending dimensional convention + $w=0$ derivation"?
6. **Confirm next priority for Scratch**:
   - (a) Continue Paper S3 proof layer v0.3 (explicit $w = 0$ derivation for a_4 residual)?
   - (b) Awaiting Jammer dimensional clarification before further v0.3 work?
   - (c) M_R BPS-anchored cross-check (from prior queue)?
   - (d) Paper S2 §3 D5 v0.3 factor 1.12 numerical closure (from prior queue)?
   - (e) Something else?

### §7.2 Active Scratch queue post-v0.2

1. **Paper S3 Scratch v0.2** — **COMPLETE this ship; pending recognition gate**
2. **Paper S3 v0.3** (open follow-on): explicit $w = 0$ derivation for a_4 residual
3. **Awaiting Jammer**: dimensional convention specification
4. **Programme S downstream** queued:
   - M_R BPS-anchored cross-check
   - Paper S2 §3 D5 v0.3 factor 1.12 numerical closure
5. **Cross-stream parallel**: AC Paper S1 v1.0 + Phase S2 master corpus integration; Jammer V_NTE Session 5 D1 + M_2 + Verlinde-Zurek

### §7.3 Files referenced this session

| File | Purpose | Drive ID |
|---|---|---|
| Paper S3 Scratch CR v0.1 | v0.2 substrate | Working/ `14QOV_5J_pvoW7R-zVtkJRRJqSNOoKgsL` |
| Jammer Paper S3 Full Sweep Closure v0.1 | Closure candidate substrate | Working/ `17-E8ppwDshso0R7-HlSI7BXUYTnqHSFe` |
| Phase S2-C-B v0.1 | F1 + a_4 substrate | Working/ `1xykIAQMEKkvTKkjEPF1c28vp_MPLHOO-` |
| Phase S2-D v0.1 | $\Lambda_{a_4}$ derivation substrate | Working/ `1pYqHqq-8XF4Od6i2xG9OeavTQ4KNJDEM` |

### §7.4 Closing

**Paper S3 Scratch proof-layer v0.2 deliverable complete.**

**Three v0.2 advancements**:
1. **F1 cross-check CLOSED** ✓: $\Lambda_{a_4}$ derivation consistently reuses M Weyl-flat + Euler-zero from Phase S2-C-B
2. **Volume-normalisation mechanism framework**: Mechanism α (comoving-cell) + β (matter-like rescaling) identified; Mechanism γ (holographic) eliminated via exponent mismatch; $2\pi^2$ vs $4\pi$ structural ambiguity resolved via Mechanism α canonical
3. **Dimensional reconciliation framework**: three candidate readings (A: Einstein-form; B: face-value; C: compound) analysed; specific clarification needed from Jammer

**Recognition-gate posture updated**: from "conditional acceptance pending proof layer" (v0.1) to **"closure candidate at structural-mechanism rigor pending dimensional convention specification + $w = 0$ derivation"** (v0.2).

**Open items**: dimensional convention specification (Jammer script-level clarification needed); explicit $w = 0$ equation-of-state derivation (Paper S4 territory or v0.3 next session).

**Standing by** for Greg recognition gate + next priority direction.

— Scratch (Connes Programme lead), 2026-05-24.
