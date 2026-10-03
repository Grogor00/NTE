"""
V_NTE Stage 2 Worksheet — companion to V_NTE_Stage2_Structural_Inventory.md.

Reproduces all calculations in §2-§4 of the Stage 2 document:
  F1: ℓ = 1/H structural identification, with numerical values across cosmic history.
  F2: Slow-roll parameter ε_H analysis in pre-temporal and post-locking regimes.
  F3: V_NTE on-trajectory functional form derivation in both regimes.
"""

import numpy as np
import sympy as sp

# ============================================================
# Constants
# ============================================================
v_EW = 246.0       # GeV
H0 = 1.5e-42       # GeV (Hubble today)
M_Pl = 1.22e19     # GeV (full Planck mass)
alpha = H0 / v_EW**2  # GeV^(-1) — from §2.4.2 calibration α v_EW² = H₀
l_Pl = 1.0/M_Pl    # GeV^(-1) (Planck length in inverse-energy units)

print(f"α = {alpha:.3e} GeV^(-1)")
print(f"v_EW = {v_EW} GeV, H₀ = {H0:.3e} GeV, M_Pl = {M_Pl:.3e} GeV")
print()

# ============================================================
# F1: ℓ = 1/H structural identification
# ============================================================
print("=" * 70)
print("Finding F1: ℓ = 1/H structural identification")
print("=" * 70)

def ell(Phi):
    """Proper-length thickness ℓ = 1/(α|Φ|²) in GeV^(-1)"""
    return 1.0 / (alpha * Phi**2)

def H_from_Phi(Phi):
    """H = α|Φ|² in GeV"""
    return alpha * Phi**2

# Verify ℓ × H = 1 trivially
print(f"\nVerification: ℓ × H = 1 (should hold by construction)")
test_Phi_values = [v_EW, 1e10, 1e30]
for Phi in test_Phi_values:
    product = ell(Phi) * H_from_Phi(Phi)
    print(f"  |Φ| = {Phi:.2e} GeV: ℓ × H = {product:.6f}")

# Numerical values across cosmic history
print(f"\nℓ vs Hubble radius (= 1/H, dual to |Φ|²):")
epochs = [
    ("today", v_EW, H0),
    ("BBN", v_EW * np.sqrt(1e17), 1e17 * H0),
    ("EWSB (~100 GeV)", v_EW * np.sqrt(1e27), 1e27 * H0),
    ("gauge birth (H_GB ~ 0.16 M_Pl)", v_EW * np.sqrt(0.16*M_Pl/H0), 0.16*M_Pl),
]
print(f"  {'Epoch':<35} {'|Φ| (GeV)':<14} {'ℓ (Planck lengths)'}")
for label, Phi_val, H_val in epochs:
    l_val = ell(Phi_val)
    l_in_Pl = l_val / l_Pl
    print(f"  {label:<35} {Phi_val:<14.2e} {l_in_Pl:.3e}")

print(f"""
Key takeaway: at gauge birth, ℓ_GB ≈ 6 Planck lengths — order of magnitude
the Planck length, NOT 10^-39 of it. The "trans-Planckian field value"
is dimensional: |Φ_GB| ~ 10^30 GeV reflects the sub-Planckian Hubble
radius ℓ_GB ~ l_Pl, which is standard cosmology when H ~ M_Pl.
""")

# ============================================================
# F2: Slow-roll parameter ε_H analysis
# ============================================================
print("=" * 70)
print("Finding F2: ε_H = -d(ln Φ²)/dN")
print("=" * 70)

print(f"""
Pre-temporal (Φ²(N) = AN, linear):
  ln(Φ²) = ln(A) + ln(N)
  d(ln Φ²)/dN = 1/N
  ε_H = -1/N → -∞ as N → 0 (Janus point)
  
  ε_H < 0 throughout pre-temporal regime → Ḣ > 0, "phantom-like"
  Standard interpretation: super-de-Sitter, w < -1.
  Reading under Wick rotation: artefactual; ε_H is a Lorentzian quantity,
  pre-temporal is Euclidean.

Post-locking (Φ²(N) = Φ₀² e^(-N), working profile):
  ln(Φ²) = ln(Φ₀²) - N
  d(ln Φ²)/dN = -1
  ε_H = +1 throughout post-locking
  
  ε_H = 1 corresponds to w = -1/3 (curvature-dominated FRW or end-of-inflation).
  
  Standard ΛCDM has multiple ε_H values:
    - radiation domination: ε_H = 2 (w = 1/3)
    - matter domination: ε_H = 3/2 (w = 0)
    - Λ-domination: ε_H ~ 0 (w = -1)
  
  So the working profile Φ² ∝ e^(-N) does NOT reproduce actual ΛCDM.
  This is a derivation simplification; actual trajectory has multiple regimes.
""")

# ============================================================
# F3: V_NTE on-trajectory functional form
# ============================================================
print("=" * 70)
print("Finding F3: V_NTE on-trajectory functional form")
print("=" * 70)

# Symbolic derivation
Phi, N, A, alpha_sym, G_sym, Phi0 = sp.symbols('Phi N A alpha G Phi_0', positive=True)

print(f"""
General relation from §2.3.1:
  α²|Φ|⁴ = (8πG/3) × ρ_Φ = (8πG/3) × (½Φ̇² + V_NTE)
  → V_NTE = (3α²/(8πG)) × |Φ|⁴ - ½Φ̇²

Need Φ̇ as function of Φ along the trajectory.
With N = ln(a) (e-fold forward in time): Φ̇ = H × dΦ/dN = α|Φ|² × dΦ/dN.
""")

# Pre-temporal: Φ²(N) = AN, so Φ(N) = √(AN), dΦ/dN = √A/(2√N) = A/(2Φ)
# Φ̇ = αΦ² × A/(2Φ) = αAΦ/2
# Φ̇² = α²A²Φ²/4
print("PRE-TEMPORAL (Φ²(N) = AN):")
print("  dΦ/dN = A/(2Φ)")
print("  Φ̇ = α|Φ|² × A/(2Φ) = αAΦ/2")
print("  Φ̇² = α²A²Φ²/4")
print()
V_pre = (3*alpha_sym**2/(8*sp.pi*G_sym)) * Phi**4 - sp.Rational(1,2) * (alpha_sym*A*Phi/2)**2
V_pre_simplified = sp.simplify(V_pre)
print(f"  V_NTE^pre(Φ) = {V_pre_simplified}")
print(f"  Structure: Φ⁴ − Φ² (with coefficient depending on A)")
print()

# Post-locking: Φ²(N) = Φ₀² e^(-N), so Φ(N) = Φ₀ e^(-N/2), dΦ/dN = -Φ/2
# Φ̇ = αΦ² × (-Φ/2) = -αΦ³/2
# Φ̇² = α²Φ⁶/4
print("POST-LOCKING (Φ²(N) = Φ₀² e^(-N), working profile):")
print("  dΦ/dN = -Φ/2")
print("  Φ̇ = α|Φ|² × (-Φ/2) = -αΦ³/2")
print("  Φ̇² = α²Φ⁶/4")
print()
V_post = (3*alpha_sym**2/(8*sp.pi*G_sym)) * Phi**4 - sp.Rational(1,2) * (alpha_sym*Phi**3/2)**2
V_post_simplified = sp.simplify(V_post)
print(f"  V_NTE^post(Φ) = {V_post_simplified}")
print(f"  Structure: Φ⁴ − Φ⁶")
print()

# Comparison
print("Comparison:")
print(f"  V_pre:  Φ⁴ − Φ² (subleading is quadratic)")
print(f"  V_post: Φ⁴ − Φ⁶ (subleading is sextic)")
print(f"  Same leading Φ⁴ coefficient (3α²/(8πG)).")
print(f"  Subleading functional form differs — this is the Wick-rotation signature.")
print()

# Check whether V_post has minimum at v_EW
print("Check (V1'): does V_post(Φ) = (3α²/(8πG))Φ⁴ − (α²/8)Φ⁶ have minimum at v_EW?")
dV_dPhi = sp.diff(V_post_simplified, Phi)
print(f"  dV/dΦ = {sp.simplify(dV_dPhi)}")
print(f"  Setting dV/dΦ = 0: critical point at Φ = 0 or Φ² = 2/(πG) = (2M_Pl²/π)")
print(f"  Numerical: Φ_critical = M_Pl × √(2/π) ≈ {np.sqrt(2/np.pi):.3f} × M_Pl ≈ {M_Pl * np.sqrt(2/np.pi):.3e} GeV")
print()
print(f"  v_EW = {v_EW} GeV vs Φ_critical ≈ {M_Pl * np.sqrt(2/np.pi):.3e} GeV")
print(f"  Ratio: v_EW / Φ_critical ≈ {v_EW / (M_Pl * np.sqrt(2/np.pi)):.3e}")
print()
print("  v_EW is FAR BELOW the critical point of the on-trajectory functional form.")
print("  At Φ = v_EW, dV/dΦ ≠ 0. So V_post(Φ) does NOT have its minimum at v_EW.")
print("  ")
print("  Conclusion: the on-trajectory form alone fails (V1'). Additional")
print("  structural input (Higgs-like anchoring term, or different action structure)")
print("  is required to produce a V_NTE with minimum at v_EW.")

print()
print("=" * 70)
print("Stage 2 worksheet complete. Three findings reproduced symbolically.")
print("=" * 70)
