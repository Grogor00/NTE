# Jammer: off-shell ghost scan — $\mathcal{S}_{\rm NTE}^{\rm unified}$ v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **PARTIAL PASS** (holonomic $\mu$ sector); **full off-shell OPEN**  
**Script:** `Working/j1_ghost_scan_numerics.py`  
**Parents:** `Jammer_J1_G4_PaperS2_Unified_Action_Derive_v0_1`; J1 S1 sign-off; §22.16; §17.5.15

---

## §0. Executive

| Scan region | Verdict |
|-------------|---------|
| **$\mu(x)$ holonomic constraint** | **PASS** — no propagating $\mu$ ghost |
| **On-shell static weak field (1PN/2PN)** | **PASS** — J1 S1/G2 |
| **$\Phi_{\rm NTE}+\xi R|\Phi|^2$ off-shell** | **OPEN** |
| **Full bimetric / Janus embedding** | **OPEN** (S2 refinement) |

**Headline.** Ghost scan is **not** a single calculation — it is **sector-labelled**. The unified action does **not** fail at the $\mu$ sector (already signed off in J1). Remaining risk is **off-shell scalar–tensor mixing** from $\xi=\frac16$ non-minimal coupling beyond the holonomic class.

---

## §1. Action under scan

$$\mathcal{S}_{\rm NTE}^{\rm unified}=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R+\mathcal{L}_{\rm SM}+\mathcal{L}_\Phi[\xi]+\mu(x)\big(\mathcal{H}[g]-\alpha|\Phi_{\rm NTE}|^2\big)\right]$$

---

## §2. Sector audit

### §2.1 Holonomic $\mu$ — **PASS**

- $\mu$ enters linearly; variation gives **constraint** $\mathcal{H}=\alpha|\Phi|^2$.  
- On-shell: $\mu$ algebraically determined — **not** an independent propagating DOF.  
- **Theorem (J1 S1):** static weak-field PPN $\gamma=\beta=1$ with no $\mu$-sector ghost.  
- **Theorem 2 (J1-G4):** $\xi R|\Phi|^2$ does **not** duplicate constraint.

**Corpus upgrade:** §22.16 “ghost scan open” → “**$\mu$ sector closed**; full off-shell open.”

### §2.2 SM sector — **orthogonal** (Path B)

SM fields propagate independently; not claimed as NTE ghost-free **proof** — standard SM unitarity assumed.

### §2.3 $\Phi_{\rm NTE}+\xi=\frac16$ — **OPEN**

| Check | Status |
|-------|--------|
| Flat-space kinetic sign | **PASS** at leading order |
| $m_E^2=\xi R$ at HH saddle | **PASS** (J6-n3; G4 §5) |
| FLRW + perturbations Hessian | **OPEN** |
| Conformal mode / $\xi=\frac16$ special role | **Not fully audited** |

**Programme:** constrained propagation analysis or gauge-fixed $(g,\Phi)$ Hessian on homogeneous background + Schwarzschild exterior (extends J1-G2/G3).

### §2.4 Phase split (LB-1)

Ghost content may differ **bulk** ($\mu=0$) vs **post** ($\mu\neq0$). Scan must respect BR2d-J3 sequential activation — not evaluate pre-$G$ constraint as if active.

---

## §3. Relation to Paper S2 / Hassan–Rosen note

Part 3 §22.5: S2 refinement mentions **ghost-free Hassan–Rosen bimetric** embedding — **parallel**, not blocking chord closure.

Janus / $\kappa_0$ sector is **orthogonal** to local $\mu$ ghost question at 1PN.

---

## §4. Acceptance criteria (revised)

| ID | Criterion | v0.1 |
|----|-----------|------|
| G1 | No $\mu$ propagator ghost on-shell | **PASS** |
| G2 | PPN $\gamma,\beta$ healthy | **PASS** (J1) |
| G3 | Off-shell $\Phi$ kinetic operator sign | **OPEN** |
| G4 | Full quantum stability of unified action | **OPEN** |

---

## §5. Corpus patches authorised

**§22.16 / §22.20:**

> **Ghost scan (Jammer v0.1, 2026-05-24).** Holonomic $\mu$ sector: **no propagating ghost** (J1 S1/G4). **Full off-shell** scan for $\Phi_{\rm NTE}+\xi=\frac16$ beyond on-shell constraint class: **open** (`Jammer_Ghost_Scan_Unified_Action_v0_1`).

---

— Jammer ghost scan v0.1, 2026-05-24.
