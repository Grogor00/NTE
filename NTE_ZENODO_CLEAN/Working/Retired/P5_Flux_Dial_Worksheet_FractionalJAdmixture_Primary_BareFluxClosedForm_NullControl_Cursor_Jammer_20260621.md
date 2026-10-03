# P5 Flux-Dial Worksheet — Fractional J-Admixture (Primary) + Bare-Flux Null Control

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** P5-FLUX-DIAL-WORKSHEET  
**Script:** `Working/p5_flux_dial_worksheet.py`

---

## Target (honest dial — not a derivation)

| Quantity | Value |
|----------|-------|
| $r_\mathrm{obs}$ (central) | 5.82 |
| $\Phi_* = r^{3/2}$ | **14.0406** |
| $4\pi$ | 12.5664 |
| $8\pi$ | 25.1327 |
| $f = (\Phi_* - 4\pi)/(4\pi)$ | **0.1173** |

## §2 — f-band (PDG/NuFIT spread)

| $r_\mathrm{obs}$ | $\Phi_*$ | $f$ |
|---|---|---|
| 5.74 | 13.7521 | 0.0944 |
| 5.82 | 14.0406 | 0.1173 |
| 5.9 | 14.3311 | 0.1404 |

**Band spread:** 0.04607 absolute (39.27% relative) — **UNSTABLE (KC2)**.

## Primary lens — σ₃/PMNS (no new parameter?)

**Question:** does a fixed PMNS combination reproduce $f \approx 0.117$?

| Candidate | Value | vs $f=0.117$ |
|-----------|-------|-------------|
| sin²θ₁₃ (PMNS) | 0.0220 | 81.2% err |
| sin²θ₁₂ | 0.3070 | 162.4% err |
| sin²θ₂₃ | 0.5460 | 366.7% err |
| 2 sin²θ₁₃ | 0.0440 | 62.4% err |
| sin²θ₁₂ sin²θ₁₃ | 0.0068 | 94.2% err |
| sin²θ₁₃ sin²θ₂₃ | 0.0120 | 89.7% err |
| sin²θ₁₃ / sin²θ₂₃ | 0.0403 | 65.6% err |
| sin²θ₁₃ (M₂/M₁−1 route per P5 σ₂ split) | 0.0220 | 81.2% err |
| √(sin²θ₁₂ sin²θ₁₃) | 0.0822 | 29.8% err |
| (sin²θ₁₂ + sin²θ₁₃)/2 | 0.1645 | 40.6% err |
| 1/8 (fixed rational — unmotivated pre-fit) | 0.1250 | 6.8% err |

**σ₃ route (P5):** $M_2/M_1 - 1 = \sin^2\theta_{13} = 0.0220$ → **81.2%** from $f$ (factor $\approx 5.3$ short).

**Best fixed combo:** 1/8 (fixed rational — unmotivated pre-fit) = 0.1250 — still **not** within 10% without a new coefficient.

## Null control — bare-flux closed forms (run to FAIL)

| Form | Value | vs $\Phi_*$ | Within 1%? | Numerology gate |
|------|-------|-------------|------------|-----------------|
| 9π/2 | 14.1372 | 0.69% | yes | NON-evidence |
| √2·π² | 13.9577 | 0.59% | yes | NON-evidence |
| 4π·2^(1/3) | 15.8326 | 12.76% | no | ruled out |
| 14 (integer) | 14.0000 | 0.29% | yes | NON-evidence |
| π²/√2 | 6.9789 | 50.29% | no | ruled out |
| (4π+8π)/2 | 18.8496 | 34.25% | no | ruled out |
| 4π + π/2 | 14.1372 | 0.69% | yes | NON-evidence |

Near-miss forms ($9\pi/2$, $\sqrt{2}\pi^2$) land within $\sim 1%$ but are **not motivated pre-fit** → recorded as **NON-evidence** per §3 discipline gate.

## Kill-conditions

| KC | Result |
|----|--------|
| KC1 (new parameter required) | **FIRE** |
| KC2 (f unstable across band) | **FIRE** |
| KC3 (multi-free numerology only) | **FIRE** |
| KC4 (σ₃ lead) | **no** |

**Verdict:** **NULL**

**One-line finding:** The between-branches value is the M_R-mechanism residual, not a flux quantum.

---

Magnitude stays **FREE**. No corpus edits. Not a derivation.

— Cursor Jammer, 2026-06-21.
