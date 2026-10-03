# κ-closure P²=P idempotency check — Cursor Main

**Date:** 2026-06-20
**Task:** KAPPA-CLOSURE-P2eqP-CHECK

## Decisive result: **G = 1.000000000000**

### Computation (monopole / Y₀₀ sector — sector used for κ=5.50 comparison)

| Check | Value |
|-------|-------|
| κ₀ = 3/√(4π) | 0.846284 |
| Y₀₀ = 1/√(4π) | 0.282095 |
| ∫ Y₀₀² dΩ (L² norm²) | 1.000000 |
| Projector P²=P overlap ratio G | **1.000000** |
| S_cons algebraic 2nd-order coeff / κ₀² | 1.000000 |
| κ = κ₀/(1−κ₀) if G=1 | 5.5055 |

**Interpretation:** G = 1 → second-order cross-thickness insertion equals κ₀² exactly
(idempotent projector on normalized Y₀₀ monopole zero-mode). Neumann resolvent
κ₀/(1−κ₀) is algebraically forced in this sector.

### Cross-checks (handoff §3)

| Check | Result |
|-------|--------|
| Stability κ₀ < 1 (loop convergence) | **PASS** (κ₀=0.8463 < 1) |
| ↔ no-4th-species (4/√(4π)=1.1284 > 1) | **CONSISTENT** |
| Clausius–Mossotti N=1 → κ | 5.5055 (≈5.50) |
| N=1/3 → κ | 1.1788 (≠ 5.50; falsifies spherical bulk) |
| Positive-feedback sign (S_cons +κ₀ T̃^{(−σ)}) | **PASS** (not −κ₀) |

### Caveat for AC adjudication

Full 𝒦 = Y₀₀·Θ bridge with non-averaged Θ not recomputed here; κ comparison
is made in monopole/averaged sector (Part3 §22.17, Paper Kappa §5.1).
G=1 holds in that sector per Hopf §5 Gaunt triviality.

**Route to AC:** G=1 → candidate for OPEN→DERIVED; KAPPA0-SIMPLIFY disposition
may flip from simplify/pull to strengthen (per AC handoff §4).

— Cursor Main, 2026-06-20.