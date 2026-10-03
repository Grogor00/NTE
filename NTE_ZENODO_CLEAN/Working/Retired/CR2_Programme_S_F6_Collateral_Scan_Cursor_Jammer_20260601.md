# Programme S — F6 collateral scan: √2/3 on m_ν₃ (AJ-13)

**From:** Cursor Jammer  
**To:** Cursor Main (CR2 coordinator), AC, Scratch — Greg  
**Date:** 2026-06-01  
**Re:** AJ-13 — falsifier **F6** from AJ-10 §6 / AJ-11 §7 / PS-13; counterfactual adoption of $Y_3 = \sqrt{2/3}$ on $m_{\nu_3}$  
**Verdict:** **FAIL** — F6 **triggered**; adopting $\sqrt{2/3}$ breaks multiple locked corpus predictions; **no corpus patch**

---

## §0 — One-line summary

Counterfactual scan: if locked corpus adopted $Y_3 = \sqrt{2/3}$ ($m_{\nu_3} = 0.0492$ eV, not $0.0738$ eV) while holding $M_R = 8.2 \times 10^{14}$ GeV and $Y_{\nu_2} = (8\pi)^{-1/3}$ fixed, **atmospheric leg and mass-ratio improve** (~2% both legs) but **collateral breaks** load-bearing locked predictions in **M_R / $Y_3=1$ structural chain**, **mass-ratio register**, and **η leptogenesis Tier A**. **PMNS mixing rows** (angles, $M_2$ split) **do not break**. F6 fires against the $\sqrt{2/3}$ patch pathway.

---

## §1 — F6 condition (from Programme S memos)

| ID | Condition | AJ-11 / PS-13 prior |
|----|-----------|---------------------|
| **F6** | $Y_3 \to \sqrt{2/3}$ breaks another **locked** prediction | **OPEN** — PMNS, $M_R$ heat-kernel, leptogenesis not scanned |

**Scan mandate:** Hold corpus locked inputs ($M_R$, $M_1$, $Y_{\nu_2}$, PMNS angles) fixed; change only σ₃ Yukawa $Y_3$: $1 \to \sqrt{2/3}$; report PASS/FAIL/OPEN per lane and overall.

---

## §2 — Counterfactual register

| Quantity | Corpus locked ($Y_3=1$) | Counterfactual ($Y_3=\sqrt{2/3}$) | Observed (PDG 2024 NO) |
|----------|-------------------------|-----------------------------------|------------------------|
| $Y_3$ | $1$ | $\sqrt{2/3} \approx 0.816$ | — |
| $m_{\nu_3}$ | $0.0738$ eV | $0.0492$ eV | $\sqrt{\Delta m^2_{31}} \approx 0.0495$ eV |
| $m_{\nu_2}$ | $0.00860$ eV | **unchanged** | $\sqrt{\Delta m^2_{21}} \approx 0.00866$ eV |
| $m_{\nu_3}/m_{\nu_2}$ | $(8\pi)^{2/3} \approx 8.57$ | $(2/3)(8\pi)^{2/3} \approx 5.72$ | $\approx 5.72$–$5.82$ |
| $M_R$ | $8.2 \times 10^{14}$ GeV | **unchanged** | — |
| $M_1$ | $\approx 5.4 \times 10^9$ GeV | **unchanged** | — |

---

## §3 — Scan lane A: PMNS rows

**Locked corpus carriers scanned:** C13 §4 mode table; C10 §7 $M_2 = M_1(1+\sin^2\theta_{13})$; master §22.1 $m_{\nu_1} = m_{\nu_2}\sin^2\theta_{13}$; Jammer S5 PMNS-$D_F$ embedding (`Working/Jammer_Paper_S5_PMNS_DF_Charged_Lepton_v0_1_20260524.md`); C7 §3.4 PMNS misalignment framing.

| Locked prediction | Depends on $Y_3$ / $m_{\nu_3}$? | Counterfactual status |
|-------------------|----------------------------------|------------------------|
| $\theta_{12}$, $\theta_{13}$, $\theta_{23}$, $\delta_{\rm CP}$ (J₃(𝕆) / §19.1) | **No** — mixing geometry, not absolute $m_{\nu_3}$ | ✅ **Unchanged** |
| $M_2 = M_1(1+\sin^2\theta_{13}) \approx 6.18 \times 10^9$ GeV | **No** — uses PMNS $\theta_{13}$, not $Y_3$ | ✅ **Unchanged** |
| $m_{\nu_1} = m_{\nu_2}\sin^2\theta_{13} \sim 1.9 \times 10^{-4}$ eV | **No** — routed through $m_{\nu_2}$ only | ✅ **Unchanged** |
| PMNS unitarity / mass-ordering (NO) | **No** — hierarchy preserved ($m_1 < m_2 < m_3$) | ✅ **Unchanged** |

**Lane A verdict:** **PASS** — PMNS rows and σ-mode / $M_i$ routing do **not** collateral-break under $\sqrt{2/3}$ adoption.

---

## §4 — Scan lane B: $M_R$ heat-kernel / S6 structural chain

**Locked corpus carriers scanned:** Paper S6 v1.0 abstract + §1.1–§1.3 + §3.6; C13 §4.4; C7 §7.1; master §22.1; Companion 12 Note 4 cross-coherence; P5 v0.3 §5 falsifier #5 (mass-ratio).

| Locked prediction | Corpus register | Counterfactual break? |
|-------------------|-----------------|----------------------|
| **$Y_3 = 1$** EW inner-fluctuation on σ₃ Cartan (S6 §3.6, Theorem A chain; $c_{\sigma_3}=1$) | Explicit structural closure | ❌ **Breaks** — $\sqrt{2/3}$ replaces unit Yukawa, not a correction within displayed $D_F$ |
| $m_{\nu_3} = v_{\rm EW}^2/M_R = 0.0738$ eV | C13 §4.4; S6 abstract; C10 table | ❌ **Breaks** — becomes $0.0492$ eV |
| $m_{\nu_3}/m_{\nu_2} = (8\pi)^{2/3} \approx 8.57$ | C13 §4.4; P5 §6 falsifier #5; C7 §7.1 | ❌ **Breaks** — drops to $\approx 5.72$ (matches obs but **violates locked ratio**) |
| $M_R = 8.2 \times 10^{14}$ GeV (Hopf 3:1 / heat-kernel) | S6; C12 Note 4 | ✅ **Unchanged** — $M_R$ scale independent of $Y_3$ |
| $m_{\nu_2} = 0.993\times$ solar (Tier A) | C13 §4.1; master §22.1 | ✅ **Unchanged** — σ₁/σ₂ sector untouched |
| Spectral-chord Note 4 ↔ C13 duality coherence | C12 §7 | ⚠️ **Strained** — $M_R$ note survives; **locked $Y_3=1$ → ratio chain** fails |

**Lane B verdict:** **FAIL** — $M_R$ **scale** survives, but the **locked $Y_3=1$ structural closure** and **registered mass-ratio prediction** are load-bearing collateral breaks. S6 honest-scope abstract (“≈1.49× atmospheric; ratio ≈8.57 vs obs ≈5.72”) would require full rewrite, not a σ₃-only patch.

---

## §5 — Scan lane C: leptogenesis (η)

**Locked corpus carriers scanned:** C10 §1.4, §3 table, §1.4 η register; master §22.2; Part3 Gap 1 closure; Register v0.5 η row.

| Locked prediction | Corpus register | Counterfactual |
|-------------------|-----------------|----------------|
| Davidson-Ibarra input **$\Delta m_{\rm eff} \approx m_{\nu_3}$** | C10 §1.4 — framework-derivative, tied to $M_R$ seesaw | $0.0738 \to 0.0492$ eV (**×2/3**) |
| **$\eta = 6.1 \times 10^{-10}$** zero-parameter (Tier A, ratio **0.997×** obs) | C10 §1.4; master §22.2 | $\eta$ scales $\propto \Delta m_{\rm eff}$ at leading DI order → **$\eta \approx 4.1 \times 10^{-10}$** (ratio **$\approx 0.67×$** obs) |
| $M_1 = (8\pi)^{1/3}(M_{\rm Pl}^2 H_{\rm GB})^{1/3}$ Pathway α | Independent of $Y_3$ | ✅ **Unchanged** |
| $v_{\rm EW}$ passthrough | Independent | ✅ **Unchanged** |

**Arithmetic (leading order):** $\eta_{\rm new}/\eta_{\rm corpus} \approx m_{\nu_3,\rm new}/m_{\nu_3,\rm corpus} = 2/3$. Then $\eta_{\rm new} \approx 6.1 \times 10^{-10} \times 2/3 \approx 4.1 \times 10^{-10}$ vs $\eta_B^{\rm obs} = 6.12 \times 10^{-10}$ → **$\approx 33\%$ deficit** (was 0.997×).

**Lane C verdict:** **FAIL** — η **Tier A genuine-test register breaks**; leptogenesis magnitude no longer lands at zero-parameter 0.997×.

---

## §6 — Collateral scorecard

| Scan lane | Verdict | F6 read |
|-----------|---------|---------|
| **A — PMNS rows** | **PASS** | No break |
| **B — $M_R$ / S6 / mass-ratio** | **FAIL** | $Y_3=1$ closure + locked $(8\pi)^{2/3}$ ratio break |
| **C — Leptogenesis η** | **FAIL** | Tier A η breaks (~0.67× obs) |

**Trade-off (explicit):** $\sqrt{2/3}$ **fixes** atmospheric $m_{\nu_3}$ and mass-ratio vs observation (AJ-11 §6.1 fit landing) but **only** by breaking other locked predictions — not a collateral-free patch.

---

## §7 — Overall verdict: **FAIL**

| Criterion | Result |
|-----------|--------|
| F6 scan executed (PMNS, $M_R$ heat-kernel, leptogenesis) | ✅ |
| PMNS collateral break | ❌ **No** (lane PASS) |
| $M_R$ / $Y_3=1$ / mass-ratio collateral break | ✅ **Yes** (lane FAIL) |
| η leptogenesis collateral break | ✅ **Yes** (lane FAIL) |
| **F6 falsifier** | **TRIGGERED** |
| Corpus patch warranted | ❌ **No** |

**Interpretation:** F6 **FAIL** means the $\sqrt{2/3}$ adoption **cannot** be applied as a σ₃-only correction without revising load-bearing locked registers (S6 $Y_3=1$ chain, C13/P5 mass-ratio falsifier, C10/master η Tier A). Combined with F1 (operator yields $Y_3=1$), the 2/3 pathway remains **research-compelling on fit** but **blocked on collateral** at current corpus lock.

**Does not:** reopen B1 honest-scope patch lane; does not ratify 2/3; does not contradict AJ-11 NEEDS-MORE / PS-13 PENDING.

---

## §8 — Routing

| Stream | Action |
|--------|--------|
| **Cursor Scratch** | Optional adversarial re-check of η scaling assumption |
| **Cursor Main** | Hold no-2/3-patch discipline; update programme pointer if desired |
| **AC** | F6 FAIL is additional evidence against corpus 2/3 write without full chord re-derivation |
| **Programme S downstream** | OctExt J₃(𝕆) matrix extraction remains separate from F6 collateral |

---

## §9 — One-line verdict

**F6 collateral scan FAIL: √2/3 on m_ν₃ fixes atmospheric fit but breaks locked $Y_3=1$/mass-ratio chain and η Tier A; PMNS rows pass; no corpus patch.**

— **Cursor Jammer**, 2026-06-01.
