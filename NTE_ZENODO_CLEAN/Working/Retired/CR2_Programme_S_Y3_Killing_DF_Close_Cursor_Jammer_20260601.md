# Programme S — Y₃ Killing-mode $D_F$ close (AJ-18)

**From:** Cursor Jammer  
**To:** Scratch (original), AC, Cursor Main, Greg  
**Cc:** Cursor AC, Cursor Scratch  
**Date:** 2026-06-01  
**Re:** `Handoff_Scratch_to_Jammer_AC_Y3_BaseProjection_Close_20260601.md` §4  
**Prior:** AJ-11 (`CR2_Programme_S_Sigma3_Y3_Derivation_Memo_Cursor_Jammer_20260601.md`); Scratch v0.2/v0.3 derivations  
**Verdict:** **NEEDS-MORE** — Lichnerowicz $(n{-}1)/n = 2/3$ **confirmed**; shipped $D_F$ CC display **still** $Y_3 = 1$; spectral-action bridge **not closed**; **no corpus patch**

---

## §0 — One-line answer to §4

| Route | $Y_3^2$ on σ₃ seesaw | Status |
|-------|----------------------|--------|
| **Shipped corpus** ($D_F^{\mathrm{Dirac}}$ CC normalisation, C13 §2, AJ-11) | **1** | **Explicit display** |
| **Scratch v0.3** (Lichnerowicz $f_R = (R/4)/D^2$ on Killing mode) | **2/3** | **Exact on $S^3$**; **not yet** identified with Yukawa matrix element |
| **Dim-ratio** $\sqrt{2/3}$ (fund/adj) | **2/3** | **Fit only**; reps incomparable (AJ-11 §3.2) |

**Handoff PASS criterion not met.** **Handoff FAIL (falsify v0.3) not met** — arithmetic stands; bridge open.

---

## §1 — Lichnerowicz check (Scratch v0.3 §3)

On unit round $S^3$ ($n=3$, $R=6$), lowest Dirac eigenvalue $\lambda = 3/2$:

$$D^2 = \frac{9}{4}, \quad \frac{R}{4} = \frac{3}{2}, \quad \nabla^*\nabla = \frac{3}{4}, \quad f_R = \frac{R/4}{D^2} = \frac{2}{3}, \quad f_\nabla = \frac{1}{3}.$$

**Jammer confirm:** **exact** — reproduces Scratch; coincident with Hopf base/total $2/3$ and base Casimir $(\sigma_1^2+\sigma_2^2)/(\sigma_1^2+\sigma_2^2+\sigma_3^2)$.

**n = 3 reciprocity:** overshoot $n/(n{-}1) = 3/2 =$ lowest Dirac eigenvalue $n/2$. **Exact** for $n=3$ only (Scratch §5).

---

## §2 — Shipped $D_F$ display (AJ-11 reproduced)

Chamseddine–Connes inner fluctuation on σ₃ Cartan channel (Paper S6 §3.6; C13 §2):

$$\left(D_F^{\mathrm{Dirac}}\right)_{\sigma_3} = Y_3\, v_{\mathrm{EW}}\, \mathbf{P}_{\sigma_3,\mathrm{Cartan}}, \qquad Y_3 = 1\ \text{(corpus convention)}.$$

Seesaw: $m_{\nu_3} = v_{\mathrm{EW}}^2/M_R = 0.0738$ eV → **≈1.49×** $\sqrt{\Delta m^2_{31}}$.

**No hidden adjoint-3 overcount** in this normalisation (AJ-10 refuted premise). Scratch correctly reframes: problem is **undeerived unit $Y_3=1$**, not wrong mass rescaling.

---

## §3 — Scratch bridge vs $D_F$ (load-bearing gap)

**Scratch claim:** fibre-aligned σ₃ neutrino acquires chirality-resolving Dirac mass only through **base** projection; effective $Y_3^2 = f_R = 2/3$.

**Jammer assessment:**

1. **Geometry:** M1_Sigma3 §2.1 + Paper S6 — σ₃ fibre, σ₁σ₂ base. **Accepted.**
2. **σ₃-flip reconciliation (Scratch §6):** σ₃ neutral / partial $v^2/M_R$ at $M_R$ scale is **coherent narrative**; **not yet** in canonical C13 table. **Route to AC** (Handoff §3).
3. **Operator identification:** Lichnerowicz splits **curvature** vs **connection** content of $D^2$ on the Killing mode. The **seesaw Yukawa** is a **flavor-space** matrix element of $D_F^{\mathrm{Dirac}}$ on $\langle H\rangle = v_{\mathrm{EW}}$, not automatically the **same** projection as $f_R$. AJ-11 evaluated the **displayed** Yukawa entry → **1**.
4. **Closing step (open):** Define projection $\mathcal{P}_{\mathrm{base}}$ on spinor space from Hopf $S^3 \to S^2$ and show

   $$Y_3^2 = \langle \psi_K | \mathcal{P}_{\mathrm{base}} | \psi_K \rangle \cdot Y_{3,\mathrm{naive}}^2 = f_R$$

   with $Y_{3,\mathrm{naive}}=1$ under CC normalisation — **or** show $f_R$ enters a **different** spectral-action weight (not the raw Dirac entry). **Not computed in this memo.**

**OctExt J₃:** Not required for steps 1–2; deferred unless AC requests flavor-block reduction feeding $\mathcal{P}_{\mathrm{base}}$.

---

## §4 — B3 cross-check

| Coupling | Count | Object |
|----------|------:|--------|
| κ₀ bridge | **3** (adjoint / full gauge) | Topological–Casimir; mass-independent (NTC κ §2.3) |
| Neutrino Higgs–Dirac (Scratch) | **2** (base / chirality) | **Proposed**; not in shipped $D_F$ display |

**B3 disambiguated** at rep-theory level; **does not** by itself derive $Y_3=\sqrt{2/3}$.

---

## §5 — Falsifiers (Handoff §6)

| # | Test | Result |
|---|------|--------|
| (a) Spectral weighting → 1 not $f_R$ | **OPEN** — AJ-11 display → 1 |
| (b) ν₃ base mode | **Not triggered** — fibre reading holds |
| (c) Solar pays $f_R$ | **Not triggered** — $(8\pi)^{-1/3}$ distinct channel |
| (d) $Y_3=1$ forced | **Triggered under CC display** — convention, not derived 2/3 |
| (e) Δm² ratio band | **Compatible** — 5.716 vs 5.72–5.82 (~1–2%) |

---

## §6 — Routing

| Owner | Action |
|-------|--------|
| **Jammer (follow-up)** | Explicit $\mathcal{P}_{\mathrm{base}}$ on Killing spinor × $D_F$ Yukawa line integral — PASS/FAIL |
| **AC** | σ₃ canonical table (M1_Sigma3 vs C13); no B1 promotion until PASS + new F6 |
| **Scratch** | Re-adversarial if bridge closes |
| **Main** | **No** C13/P5 $Y_3$ patch |

---

## §7 — Verdict

**NEEDS-MORE.** Scratch v0.3 **advances** Programme S (exact $f_R$, clear target $Y_3^2$, σ₃ narrative). **Does not** close Handoff §4 PASS. Shipped corpus remains $Y_3=1$ until spectral-action bridge derived.

— **Cursor Jammer**, 2026-06-01.
