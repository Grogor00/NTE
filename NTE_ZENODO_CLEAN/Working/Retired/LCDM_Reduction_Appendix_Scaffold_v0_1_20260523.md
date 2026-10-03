# ΛCDM reduction in tested regimes — working scaffold (Tier 2)

**Stream:** Cursor draft → AC master integration; Jammer cosmology bench  
**Date:** 2026-05-23  
**Master target:** §17.5.9 (`NTE_v10_12_Part3_Accounting.md`)  
**Status:** Scaffold for explicit reduction argument — **not** a completed χ² fit programme

---

## §1. Claim structure (honest)

| Claim level | Statement |
|-------------|-----------|
| **Structural** | Post-locking, NTE uses H(N) = α\|Φ_NTE\|² and recovers standard FRW when ρ_Φ is identified with critical density (§2.3.1). |
| **Reduction (target)** | In homogeneous, post-EWSB, Λ-dominated limits, observables **reduce to ΛCDM** within stated approximations. |
| **Distinguishing** | Spatial \|Φ_NTE(x)\| variation predicts Hubble tension bias, DESI w₀wₐ pattern, κ — **deviations from homogeneous ΛCDM**, not failures of FRW reduction. |
| **Open** | Full global-fit χ² to Planck + DESI + BAO chains not performed in corpus. |

---

## §2. Reduction chain (logical steps)

1. **Core equation:** H = α\|Φ_NTE\|² (scalar constraint; Part 1 §2.3).
2. **Trajectory:** \|Φ_NTE\|²(N) = v_EW² · H(N)/H₀ (§2.3.1 self-consistency).
3. **Friedmann identification:** Require α²\|Φ\|⁴ = 8πG ρ_Φ/3 — open epoch-by-epoch verification (§2.3.1).
4. **Matter content:** SM radiation + matter + geometric unloading → standard ρ(a) composition in post-temporal regime (Part 2 §XII–XIII).
5. **Λ limit:** w → −1, H → H₀ Ω_Λ^{1/2} asymptote; true equation of state w = −1 (Part 2 §13.3).
6. **Observational layer:** Homogeneous FRW + ΛCDM parameter set {Ω_b, Ω_c, Ω_Λ, H₀, n_s, …} is the **baseline**; NTE-specific signals are **inhomogeneity / selection** effects on top.

---

## §3. Benchmark map

| Observable | ΛCDM role | NTE status in corpus | Deviation type |
|------------|-----------|----------------------|----------------|
| CMB T_CMB, peak positions | Standard thermal history | Implicit via SM + BBN (Companion papers) | None claimed at homogeneous level |
| CMB κ (amplitude) | Ω_m, Ω_b, n_s | **Prediction** κ ≈ 5.50 (§9.3) | Testable; void bias should **not** affect z~1100 CMB κ (Part 2 §13.3(d)) |
| n_s | Inflation | **Derived** 0.9685 (Companion 9; §17.5.14) | Independent of H₀ construction |
| r | Tensor/scalar | Three-readings; hilltop ≈ 4×10⁻³ favoured (§18.4) | Explicit tension management |
| BAO scale | H(z), Ω_m | **Implicit** FRW recovery | Void enhancement → shorter distances → mimics w > −1 |
| σ_8, LSS P(k) | Growth | **Implicit**; not fitted | Open: structure growth under H(x,N) |
| H₀ (local vs CMB) | Single parameter | **Split** H_local > H_CMB (§13.2) | NTE distinguishing prediction |
| DESI w₀, w_a | Dark energy EOS | **Explained** as void bias (Part 2 §13.3) | Not phantom DE; parameterisation artifact |
| BBN (D/H, Y_p) | H(N) during BBN | Constraints on \|Φ_NTE\| trajectory | Falsification surface (Part 1 Path B) |

---

## §4. Homogeneous limit theorem (prose target for §17.5.9)

When spatial gradients of \|Φ_NTE\|² are negligible (δρ/ρ ≪ 1 on Hubble scales), H(x,N) → H(N) and the system reduces to a single-fluid FRW cosmology with effective density ρ_eff = 3H²/(8πG). If, in addition, the matter sector splits into standard radiation + non-relativistic matter + cosmological constant in the usual way, the background expansion history is **ΛCDM-class** with parameters fixed by NTE's α, trajectory, and SM content. NTE does not replace ΛCDM in this limit; it supplies a geometric origin for H(N) and for selected parameters (κ, n_s, M₁ at S1, etc.) while reducing to the same FRW bookkeeping.

---

## §5. Where NTE is *not* ΛCDM (reviewer clarity)

Explicit deviations (predictions, not bugs):

- Spatial H(x,N) from \|Φ_NTE(x)\|² → Hubble tension, DESI EOS, local κ surveys.
- CPN / mirror sector → dark matter as geometric coupling (κ), not ΛCDM particle DM — **different microphysics**, same FRW background possible.
- Pre-temporal / gauge-birth regime → outside ΛCDM entirely (by definition).

---

## §6. Research programme (post–§17.5.9 expansion)

| Priority | Task | Owner |
|----------|------|-------|
| P1 | Epoch-by-epoch ρ_Φ ↔ α²\|Φ\|⁴ check through radiation/matter/Λ | Jammer |
| P2 | Explicit BAO distance comparison: NTE H(z) homogeneous vs ΛCDM | Jammer |
| P3 | Growth equation with H(x,N) — σ_8 at z=0 | Jammer / AC |
| P4 | Document χ² fit scope (Planck + DESI) or defer with falsifier list | AC |

---

## §7. Cross-references

- Part 1 §2.3.1, §2.4.3 (H₀ vs n_s independence)
- Part 2 §13.2–§13.3 (void / DESI)
- §17.5.14–§17.5.15, §18.4 (inflation sector)
- `depreciated/17.5.4_Audit_NLock_Derivation.md` (N_lock candidate — separate Tier 2 item)

— Cursor, 2026-05-23
