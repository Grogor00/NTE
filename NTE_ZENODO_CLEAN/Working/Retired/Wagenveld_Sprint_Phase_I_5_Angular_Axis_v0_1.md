# Wagenveld Sprint — Phase I.5 Angular Axis (Cursor v0.1)

**Date:** 2026-05-29  
**Coordinator:** Cursor  
**Inputs:** `wagenveld_sprint_surveys.json` v0.2; `lcdm_bao_void_bias.py` angular block  
**Parent:** `Wagenveld_Sprint_Phase_I_Pattern_Characterisation_v0_1.md`

---

## §1 — Purpose

Close Phase I **axis 3 (angular structure)** at worksheet/literature-anchor level so Phase II can discriminate §2.1 ↔ §2.5 ↔ §2.6 (Scratch flag #3; three-way self-consistency per Scratch scoping review).

**Honest scope:** Directions are **central values + conservative σ_dir**, not catalogue re-fits. Magnitude overshoot analysis unchanged from Phase I.

---

## §2 — Direction table (galactic l, b)

| Survey | l (°) | b (°) | σ_dir (°) | sep from CMB (°) | sep from Branch I n_void (°) |
|--------|-------|-------|-----------|------------------|------------------------------|
| CMB kinematic | 264.0 | 48.3 | 0.2 | — | ~0 |
| CatWISE | 240.0 | 30.0 | 15 | **25.9** | 25.7 |
| Wagenveld | 268.0 | 42.0 | 20 | **6.9** | 6.6 |
| Singal | 262.0 | 46.0 | 18 | **2.6** | 2.4 |
| Quaia | 195.0 | 35.0 | 25 | **51.4** | 51.5 |

Branch I void axis anchor: (264°, 48°) — aligned with CMB per Jammer §1.3 design target.

---

## §3 — Inter-survey separations (°)

|  | CatWISE | Wagenveld | Singal | Quaia |
|--|---------|-----------|--------|-------|
| **CatWISE** | — | 25.5 | 23.4 | 38.0 |
| **Wagenveld** | 25.5 | — | 5.9 | 55.8 |
| **Singal** | 23.4 | 5.9 | — | 50.6 |
| **Quaia** | 38.0 | 55.8 | 50.6 | — |

---

## §4 — Pattern read (Phase II input)

1. **Wagenveld vs Singal (radio):** Amplitude δσ vastly different (+3.28 vs +0.63) but directions **within ~6°** (sep 5.9°). Supports **survey-specific amplitude / selection / z_eff** over “radio points another way on the sky.”

2. **Quaia vs others:** Direction **~38–56°** off CatWISE / radio cluster in these anchors — consistent with Jammer note that high-z QSO dipole direction is poorly constrained and may differ. **Cannot** yet test §2.1↔§2.5↔§2.6 three-way same-direction prediction until Quaia direction is catalogue-sourced.

3. **All radio + CatWISE vs CMB:** CatWISE offset ~26°; Wagenveld/Singal **≲ 7°** from CMB — Wagenveld amplitude anomaly is **not** accompanied by large directional offset from kinematic dipole; CatWISE is the directional outlier among anchors, not Wagenveld.

4. **§2.5 (anisotropic κ) vs §2.1 (gauge-birth seed):** Angular table **does not separate** them at v0.1 — both predict manifold-preferred direction; need Hopf-fibre sky map (Scratch Phase III) + tighter survey directions.

5. **§2.2 (leakage, scale-driven):** Not ruled in/out on angle alone.

---

## §5 — Phase II implication (for AC / Scratch)

- **Do not** rank §2.1 as “highest prior” on z-scaling alone (Phase I + Scratch flag #1).  
- **Do** treat Wagenveld as **amplitude + selection** outlier with **direction near Singal/CMB**.  
- **Treat §2.5 as potentially downstream of §2.1** (Scratch flag #2) — top-3 should not double-count without explicit disentanglement plan.  
- **Quaia direction** = highest leverage ingest for next Cursor increment.

---

## §6 — Next Cursor increment

- Replace JSON directions from primary papers (Wagenveld 2024/2025, CatWISE, Singal, Quaia).  
- Joint-fit DOF memo (shared vs per-survey nuisance).  
- Optional: dipole **amplitude** vs misalignment angle 2D diagnostic per survey.

*End Phase I.5 v0.1.*
