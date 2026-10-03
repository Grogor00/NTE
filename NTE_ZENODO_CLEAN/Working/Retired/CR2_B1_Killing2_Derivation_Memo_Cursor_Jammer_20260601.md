# CR2 / WP-B1 — Killing dim 2 vs adjoint dim 3: derivation attempt on the 2/3 atmospheric factor

**From:** Cursor Jammer  
**To:** Cursor Main (CR2 coordinator), AC, Scratch — Claude model, Greg  
**Cc:** Cursor AC  
**Date:** 2026-06-01  
**Re:** `Working/CR2_B1_Killing2_vs_Adjoint3_Neutrino_Pathway_Scratch_Claude_20260601.md`; `Working/CR2_B3_kappa0_RepTheory_Verdict_Claude_Jammer_20260601.md`; `Handoff_Cursor_Main_to_Jammer_B1_Killing2_Pathway_Derivation_Request_20260601.md`  
**Verdict:** **NEEDS-MORE** — numerically compelling candidate; load-bearing derivation steps **not closed**; one premise **refuted** against current corpus. **Do not patch corpus with ×2/3 until PASS.**

---

## §0 — One-line summary

The factor **(2/3)(8π)^(2/3) ≈ 5.716** lands both neutrino legs within ~2% from a single $M_R$, and the **2 vs 3** rep-theory disambiguation aligns with B3. But the pathway **does not derive** $m_{\nu_3} \times (2/3)$ from an explicit $\sigma_3$ mass operator on $D_F$; the claim that the corpus already **mistakenly imported adjoint-3 normalisation** into $m_{\nu_3}$ is **refuted**; chirality-superposition amplitude gives **×1**, not 2/3; and $\sigma_1/\sigma_2$ **escape** is stipulated, not derived from the same construction.

---

## §1 — Target and numerical anchor

| Quantity | Naive corpus | ×(2/3) on $\sigma_3$ | Observed (NuFIT 6.0 / PDG 2024, NO) |
|----------|-------------|------------------------|--------------------------------------|
| $m_{\nu_2}$ | 0.00860 eV | 0.00860 eV (unchanged) | $\sqrt{\Delta m^2_{21}} \approx 0.00866$ eV |
| $m_{\nu_3}$ | 0.0738 eV | **0.0492 eV** | $\sqrt{\Delta m^2_{31}} \approx 0.0495$ eV |
| $m_{\nu_3}/m_{\nu_2}$ | $(8\pi)^{2/3} \approx 8.574$ | **5.716** | $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}} \approx 5.72$–5.82 |

The numerical fit is real (~2% on both legs). **Fit alone is not derivation** (Scratch §6; Greg §II.0 discipline).

---

## §2 — What the corpus actually says (baseline)

### §2.1 $m_{\nu_3}$ prescription

Companion 13 v10.17.2, Paper P5 v0.3, Paper S6 v1.0, and CR2 B1 Jammer verdict agree:

$$m_{\nu_3} = \frac{Y_3^2\, v_{\rm EW}^2}{M_R}, \qquad Y_3 = 1 \text{ (convention)}.$$

**Reading:** $\sigma_3$ is Cartan-aligned, strongly Higgs-VEV coupled; **no Hopf-flux normalisation** on the $\sigma_3$ Yukawa (Paper P5 §5: "no Hopf-flux normalisation; the $\sigma_3$ mode is Cartan-aligned"). $Y_3 = 1$ is an **electroweak-scale Higgs inner-fluctuation convention** (Paper S6 §B; C13 §2), **not** a sum over three adjoint channels.

**What remains open (C7 §7.1):** ab initio derivation of $Y_3 = 1$ from explicit $D_F$ structure — Programme S downstream. That open item is **not** the same as "we already summed three adjoint channels and must divide by 3."

### §2.2 $m_{\nu_2}$ prescription (contrast)

$$Y_{\nu_2} = (8\pi)^{-1/3} \quad \Rightarrow \quad m_{\nu_2} = \frac{(8\pi)^{-2/3}\, v^2}{M_R}.$$

C13 explicitly places $\sigma_1/\sigma_2$ on the **Hopf–Killing-spinor flux line** (D5-inverse). The solar leg is **Tier A sub-1%** at this register.

### §2.3 B3 / κ₀ (cross-ref)

B3 verdict (`CR2_B3_kappa0_RepTheory_Verdict_Claude_Jammer_20260601.md`): **κ₀ = 3/√(4π) survives** under **dim(adj SU(2)) = 3 gauge-field components** × $Y_{00}(S^2)$. Fixed-sign Killing-spinor space is **2-dim fundamental**, not 3-dim adjoint.

Companion 7 v10.17.2 §4.2 (post-B3 patch) states explicitly:

> NTE's three neutrino mass eigenmodes (§3.2, §3.3) provide structural parallel at the su(2) level but **do not supply the multiplicity count in κ₀** — that count is dim(adj SU(2)) = 3 gauge components.

**Consequence:** B3 is already resolved by **rep-theory disambiguation + language patch** without changing κ₀ or importing a neutrino 2/3 factor. The Scratch pathway's claim that B3 and B1 "resolve together via 2/3" overstates dependence: B3 closure does **not** require the neutrino correction.

---

## §3 — Derivation attempt: dim 2 / dim 3 → factor 2/3

### §3.1 Proposed chain (Scratch)

1. $\sigma_3$ neutrino = chirality-superposed mode → lives in fixed-sign **Killing-spinor** space, dim **2** (Bär 1993).
2. Naive $m_{\nu_3} = v^2/M_R$ implicitly normalised over **adjoint-3** (same "3" as κ₀).
3. Re-normalise coupling from adjoint count 3 to Killing count 2 → $m_{\nu_3} \to (2/3)\, m_{\nu_3}$.
4. $\sigma_1/\sigma_2$ are definite (non-superposed) → no 2/3.

### §3.2 Step 1 — σ₃ as Killing-spinor mode (partial)

**Support:** Companion 7a chirality superposition $|\nu\rangle = \alpha|\nu_L\rangle + \beta|\nu_R\rangle$; C7 §3.2 intrinsic-vantage $\sigma_1/\sigma_2/\sigma_3$ flavor decomposition; round $S^3$ fixed-sign Killing spinors = dim 2, **fundamental** of SU(2) (B3 §2.1).

**Gap:** Identifying the **mass eigenstate** $\nu_3$ (Cartan-aligned, Higgs-coupled) with a **single Killing-spinor mode on $S^3$** requires an explicit $D_F$ embedding map (Programme S). The corpus assigns $\nu_3$ to **$\sigma_3$ Pauli direction in flavor/Cartan space**, which is a **generator label**, not yet a proof that the mass matrix element is computed in the 2-dim Killing-spinor bundle rather than the 3-dim adjoint.

### §3.3 Step 2 — "Naive m_ν₃ imported adjoint-3" (**REFUTED**)

**Finding:** The corpus **does not** sum three adjoint channels to set $Y_3 = 1$.

| Object | Multiplicity "3" | What it counts |
|--------|------------------|----------------|
| κ₀ = 3/√(4π) | dim(adj SU(2)) | Three **gauge-field components** $A^a$, each × $Y_{00}$ |
| $Y_3 = 1$ | **None** — unit convention | Cartan Higgs coupling on $\sigma_3$ |
| $Y_{\nu_2} = (8\pi)^{-1/3}$ | Hopf flux / volume | D5-inverse on $\sigma_1/\sigma_2$ **Killing-spinor flux line** |

The 1.49× atmospheric overshoot is the **honest outcome** of $Y_3 = 1$ + $Y_{\nu_2} = (8\pi)^{-1/3}$ + single $M_R$ (CR2 B1 PMNS verdict §2), not evidence of a hidden adjoint-3 overcount in $m_{\nu_3}$.

**To derive 2/3 one must show:** an **explicit** $\sigma_3$ Dirac/Yukawa operator on $D_F$ yields $Y_3 = \sqrt{2/3}$ (equivalently $m_{\nu_3} \times 2/3$), **replacing** the current $Y_3 = 1$ convention — not "correcting" a mistake already in the text.

### §3.4 Step 3 — dim 2 / dim 3 as mass factor (**NOT DERIVED**)

Naive dimension ratio:

$$\frac{\dim(\text{Killing spinors, fixed sign})}{\dim(\text{adj SU(2)})} = \frac{2}{3}.$$

**Problems without operator:**

1. **Incomparable reps:** Killing spinors carry **fundamental** (complex 2); adjoint is **real 3** (spin-1). A mass factor requires a **projection/overlap** (e.g. $\|P_{\rm fund}\,\psi\|^2 / \|P_{\rm adj}\,\psi\|^2$), not raw dimension ratio.
2. **Wrong object for σ₃:** $\sigma_3$ is one **Cartan generator** acting on spinors; it is not the adjoint representation space itself. The adjoint "3" in κ₀ counts **independent gauge components**, not three copies of the neutrino.
3. **Equivalent Yukawa form:** $m_{\nu_3} \to (2/3)m_{\nu_3}$ iff $Y_3 \to \sqrt{2/3} \approx 0.816$. The pathway must derive **$Y_3 = \sqrt{2/3}$** from $D_F$, not post-multiply a closed $Y_3 = 1$ result.

**Status:** Counting motivation only; **no spectral-triple computation** supplied.

### §3.5 Chirality-superposition amplitude (**REFUTES 2/3 from amplitude route**)

Balanced superposition $|\nu\rangle = \frac{1}{\sqrt{2}}(|\nu_L\rangle + |\nu_R\rangle)$ gives Dirac Yukawa strength $| \langle H \rangle | \times |\alpha|^2 + |\beta|^2 = 1$ at unit normalisation — **×1**, not 2/3 (Scratch §6 honest scope).

Scratch correctly routes 2/3 through **counting/normalisation**, not amplitude. **That counting chain is not displayed** at operator level.

### §3.6 σ₁/σ₂ escape the 2/3 (**NOT DERIVED**)

Scratch: $\sigma_1/\sigma_2$ are "definite, Higgs-orthogonal, not chirality-superposed Killing modes" → retain $(8\pi)^{-2/3}$ only.

**Corpus tension:** C13 **explicitly** assigns $\sigma_1/\sigma_2$ to the **Hopf–Killing-spinor flux line** with D5-inverse Yukawa. They are not "non-Killing" in the corpus ontology — they are the **transverse** Killing-flux sector. If 2/3 arises from Killing-vs-adjoint normalisation, a unified derivation must show **why the flux-line normalisation on $\sigma_1/\sigma_2$ already uses dim 2 (or equivalent)** while $\sigma_3$ mistakenly used dim 3 — or why Cartan alignment bypasses the flux factor differently from a dim ratio.

**Current status:** Escape is **stipulated** to preserve solar Tier A; not derived from one $D_F$ calculation.

---

## §4 — Principled κ₀ vs neutrino separation

### §4.1 What already exists (B3 + C7)

| Sector | Object | Rep / count | Observable |
|--------|--------|-------------|------------|
| **Gauge bridge** | SU(2) Yang–Mills on Hopf base | **3** adjoint gauge components × $Y_{00}$ | κ₀ = 3/√(4π) |
| **Neutrino flavor** | Three $\sigma_i$ eigenmodes of unresolved su(2) | Structural parallel to su(2); **not** κ₀ multiplicity | $m_{\nu_i}$ via $Y_i$, $M_R$ |

This separation **is principled** at the level of **which operator is being summed**: gauge-field component sum vs Yukawa mass matrix entries. It does **not** automatically imply $m_{\nu_3}$ carries a 2/3 correction.

### §4.2 Scratch "disambiguation resolves B3" — assessment

**Partially true:** 2 vs 3 are different objects (B3 closed).  
**Overstated:** B3 does **not** need neutrino 2/3 to close; κ₀ unchanged.  
**Still open:** Derive **neutrino-sector** $Y_3$ from spinor geometry without conflating with gauge-component sum.

**Discipline test (handoff ask):** "Use 3 here, 2 there" fails unless one **operator display** shows both sectors from one $D_F$ decomposition. That display is **missing**.

---

## §5 — What would close (Programme S deliverables)

1. **Explicit $\sigma_3$ mass matrix element** on $D_F$ (Paper S6 downstream): compute $Y_3$ from Killing-spinor overlap / Cartan projection; target $Y_3 = \sqrt{2/3}$ if pathway holds.
2. **Unified $\sigma_i$ treatment:** same construction for $\sigma_1,\sigma_2,\sigma_3$ showing $(8\pi)^{-2/3}$ on transverse sector and $(2/3)$ on Cartan sector **without** tuning.
3. **Chirality map:** link C7a superposition to **which** of the two fixed-sign Killing spinors (or their combination) carries $\nu_3$ mass.
4. **Falsify numerology:** show 2/3 is **unique** among dim-ratio candidates (e.g. rule out $\sqrt{2/3}$, $1/2$, $3/4$) from the same operator.

---

## §6 — Falsifiers (from Scratch §6 + this review)

| ID | Condition | Current status |
|----|-----------|----------------|
| **F1** | Explicit $\sigma_3$ derivation yields **×1** or **√(2/3)** on mass, not **2/3** | **Open** — no derivation; amplitude route gives ×1 |
| **F2** | $\sigma_1/\sigma_2$ escape cannot be derived from same structure | **Triggered as open** — escape stipulated; C13 Killing-flux line unresolved |
| **F3** | κ₀ (adjoint-3) vs neutrino (Killing-2) separation not principled | **Not triggered** — B3+C7 §4.2 already separate; neutrino 2/3 not required |
| **F4** | Observed $\sqrt{\Delta m^2_{31}/\Delta m^2_{21}}$ moves off 5.7–5.8 | **Not triggered** (NuFIT 6.0 central ≈ 5.72–5.82) |
| **F5** | Premise: corpus already adjoint-3-normalised $m_{\nu_3}$ | **Triggered — refuted** — $Y_3 = 1$ is explicit convention, not adjoint sum |
| **F6** | Correcting $Y_3$ to $\sqrt{2/3}$ breaks another locked prediction | **Open** — must scan σ₃-linked observables (PMNS rows, $M_R$ heat-kernel, leptogenesis) |

---

## §7 — Verdict and routing

### §7.1 Verdict: **NEEDS-MORE**

| Criterion | Result |
|-----------|--------|
| Numerical landing of (2/3)(8π)^(2/3) | ✅ ~2% both legs |
| Structural hook (2 vs 3, B3 parallel) | ✅ Plausible research direction |
| Explicit $D_F$ derivation of 2/3 | ❌ Absent |
| Corpus adjoint-3 mistake premise | ❌ **Refuted** |
| Chirality amplitude → 2/3 | ❌ Gives ×1 |
| σ₁/σ₂ escape from same construction | ❌ Not derived |
| Principled κ₀ vs neutrino separation | ✅ Already in B3+C7; does not imply 2/3 |

**Not FAIL outright:** the numerical match and rep-theory axis are worth a Programme S closure attempt.  
**Not PASS:** load-bearing steps fail; one premise contradicts corpus; **no corpus patch with ×2/3**.

### §7.2 Corpus discipline

- **Do not** patch C13, P5, S6, or master with $m_{\nu_3} \times (2/3)$ or $Y_3 = \sqrt{2/3}$ until **PASS** + AC ratify.
- **Maintain** CR2 B1 honest scope: solar Tier A; atmospheric ≈1.49× open.
- **B3 patches** (Hopf paper language) proceed **independently** — already closed numerically.

### §7.3 Routing

| Stream | Action |
|--------|--------|
| **Cursor Main** | Hold MAIN-14 / programme pointer; no 2/3 corpus write |
| **AC** | B1 disposition unchanged; candidate pathway logged as NEEDS-MORE |
| **Scratch — Claude model** | Optional: adversarial PS-12 on F5 + σ₁/σ₂ tension |
| **Programme S / Paper S6** | If pursued: explicit $Y_3$ from $D_F$ Killing-spinor–Cartan projection |

---

## §8 — One-line verdict

**The (2/3)(8π)^(2/3) fix fits both neutrino legs well, but the 2/3 is not derived — the corpus does not adjoint-overcount $m_{\nu_3}$, chirality amplitude gives ×1, and σ₁/σ₂ escape is unstipulated; B3 already disambiguates 2 vs 3 without this factor. NEEDS-MORE; no corpus patch.**

— **Cursor Jammer**, 2026-06-01.
