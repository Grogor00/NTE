# Wagenveld Sprint — Joint-Fit DOF Accounting (Cursor v0.1)

**Date:** 2026-05-29  
**Authority:** AC Phase II top-3 handoff §6 (Cursor deliverable); supports §2.7 rank-1 read  
**Worksheet:** `lcdm_bao_void_bias.py` — delta-sigma objective, no χ²

---

## §1 — Question

Can Branch I's Wagenveld overshoot be absorbed by **shared** parameters `(b, α, g(z))` only, or does it require **survey-specific** effective `(z_eff, p)` — and how many extra degrees of freedom?

---

## §2 — Parameter tiers

| Tier | Free parameters | Extra DOF vs defaults |
|------|-----------------|------------------------|
| **0** | Fixed: `b=0.055`, `α=0.24`, `g=pow2`, table `z_eff`, `p` | 0 |
| **1** | Shared: `b`, `α`, `g(z)` model | +2 (b, α; model discrete) |
| **2** | Tier 1 + Wagenveld-only `(z_w, p_w)` | +2 |
| **3** | Per-survey `(z, p)` all four surveys | +6 (not fully scanned here) |

**Observations:** 4 surveys × 1 amplitude each = 4 constraints (informal; not a formal χ² fit).

---

## §3 — Results (bounded grid, 2026-05-29)

### Tier 0 — defaults

| Survey | δσ |
|--------|-----|
| CatWISE | −0.13 |
| Wagenveld | **+3.28** |
| Singal | +0.63 |
| Quaia | +0.52 |

`max|δσ| = 3.28`

### Tier 1 — shared `(α, b, g(z))` only

Best grid corner: `α=0.12`, `b=0.055`, `g=exp`  
`max|δσ| = **1.21**`

| Survey | δσ |
|--------|-----|
| CatWISE | −1.21 |
| Wagenveld | +1.12 |
| Singal | −0.58 |
| Quaia | −0.10 |

**Read:** Shared fit **cannot** bring Wagenveld inside 1σ without pushing CatWISE to ~−1.2σ. Trade-off, not closure.

### Tier 2 — shared + Wagenveld-only `(z_w, p_w)`

Best grid corner: `α=0.24`, `b=0.04`, `g=exp`, `z_w=0.35`, `p_w=0.8`  
`max|δσ| = **0.42**

| Survey | δσ |
|--------|-----|
| CatWISE | −0.34 |
| Wagenveld | +0.16 |
| Singal | +0.37 |
| Quaia | +0.42 |

**Read:** **+2 DOF** on Wagenveld alone collapses amplitude tension across all four surveys to sub-0.5σ (worksheet placeholders). This is **not** a physical closure — it is **survey-specific nuisance absorption**.

### Tier 2b — Wagenveld-only grid (script v0.4 block; others fixed at table)

Best: `α=0.16`, `p_w=1.0`, `z_w=0.40`, `g=exp` → `max|δσ| = **0.57**`

Consistent with Phase I §5.

---

## §4 — Sprint implications

1. **§2.7 (survey-geometry / selection-specific)** — Phase I + this memo support AC rank-1: Wagenveld isolation + need for survey-specific parameters to absorb amplitude without breaking others.

2. **§2.1+§2.5 merged** — Not ruled out; angular axis (Phase I.5) shows Wagenveld **direction-normal** (~7° from CMB) while **amplitude-anomalous** — consistent with mechanism that affects amplitude via κ closure more than sky direction at leading order.

3. **Honest-scope for Phase IV:** Report Tier 0, Tier 1, Tier 2 side-by-side; penalize Tier 2+ fits by extra DOF explicitly. Do not claim Branch I "closed" on Tier 2 without survey-geometry justification.

---

## §5 — Cursor next

- Add `print_joint_fit_dof()` to worksheet (reproducible).  
- Re-run after catalogue-sourced `D_obs`, `z_eff`, `p`.  
- Phase IV: compare candidate predictions on same tiered fit ladder.

*End v0.1.*
