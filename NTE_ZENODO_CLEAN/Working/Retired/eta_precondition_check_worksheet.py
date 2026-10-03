"""
Eta Precondition Check Worksheet — companion to Eta_Asymmetry_Magnitude_Reframing_Audit.md

Verifies the structural claim of §1.4: that Δm_eff in the Davidson-Ibarra leptogenesis
formula is geometric in NTE (not an independent free parameter), via the chain:

    M_R = M_Pl^(3/4) × v_EW^(1/4)        [Hopf bundle structure, corpus line 1274]
       → m_ν₃ = v_EW² / M_R               [seesaw]
       → Δm_eff ≈ m_ν₃                    [Davidson-Ibarra effective neutrino mass]

Reverse-checks via the Davidson-Ibarra + sphaleron formula that this geometric Δm_eff
gives the right order of magnitude for M₁ (corpus quotes 6.06 × 10⁹ GeV).
"""

import numpy as np

# ============================================================
# Constants
# ============================================================
v_EW = 246.0       # GeV (SM Higgs VEV; SM-inherited under Path B)
M_Pl = 1.22e19     # GeV (Planck mass)
H0 = 1.5e-42       # GeV (Hubble today)
g_star = 106.75    # SM degrees of freedom at high T (gauge birth-ish)
eta_obs = 6.1e-10  # observed baryon-to-photon ratio

print("=" * 70)
print("Precondition check: is Δm_eff geometric in NTE?")
print("=" * 70)
print()

# ============================================================
# Step 1: M_R from Hopf bundle structure (corpus §19.7 line 1274)
# ============================================================
M_R = M_Pl**(3/4) * v_EW**(1/4)
print(f"Step 1: M_R from Hopf bundle structure")
print(f"  M_R = M_Pl^{{3/4}} × v_EW^{{1/4}}")
print(f"      = {M_R:.3e} GeV")
print(f"  Corpus quoted: 8.2 × 10¹⁴ GeV")
print(f"  Match: {'✓' if abs(M_R/8.2e14 - 1) < 0.05 else '✗'} (within 5%)")
print()

# ============================================================
# Step 2: m_ν₃ from seesaw (corpus line 1276)
# ============================================================
m_nu3 = v_EW**2 / M_R
m_nu3_eV = m_nu3 * 1e9  # GeV → eV
print(f"Step 2: m_ν₃ from seesaw")
print(f"  m_ν₃ = v_EW² / M_R = {m_nu3_eV:.4f} eV")
print(f"  Corpus quoted: 0.074 eV")
print(f"  Observed √(Δm²_atm) ≈ 0.05 eV")
print(f"  Predicted/observed: {m_nu3_eV/0.05:.2f} (corpus says 'factor 1.5')")
print()

# ============================================================
# Step 3: Δm_eff identification — DI uses MASS not mass-squared
# ============================================================
# Standard Davidson-Ibarra:
#   ε₁^max = (3/16π) × M₁ × m_ν_max / v_EW²
# where m_ν_max is the heaviest light neutrino mass (units of mass, not mass²).
# The "Δm_eff" notation in some references is misleading — the Δ is conventional,
# not a difference; Δm_eff = m_ν₃ for the saturating bound.

Delta_m_eff_geometric = m_nu3   # GeV — NTE-geometric
print(f"Step 3: Δm_eff identification")
print(f"  Davidson-Ibarra: Δm_eff has units of MASS (not mass²)")
print(f"  Δm_eff_geometric = m_ν₃ = {Delta_m_eff_geometric*1e9:.4f} eV")
print()

# ============================================================
# Step 4: Reverse-check via DI + sphaleron
# ============================================================
# ε₁ = (3/16π) × (M₁/v_EW²) × Δm_eff
# η = (28/79) × (3/4) × ε₁/g*
#
# Solve: η = (28/79)(3/4)(3/16π)(M₁ × Δm_eff)/(v_EW² × g*)
# M₁ = η × v_EW² × g* × (16π/3) × (79/28) × (4/3) / Δm_eff

M_1_from_geometric = (eta_obs * v_EW**2 * g_star
                     * (16*np.pi/3) * (79/28) * (4/3)
                     / Delta_m_eff_geometric)

M_1_from_observed = (eta_obs * v_EW**2 * g_star
                    * (16*np.pi/3) * (79/28) * (4/3)
                    / (np.sqrt(2.5e-3) * 1e-9))   # observed √Δm²_atm in GeV

print(f"Step 4: Reverse-check via Davidson-Ibarra + sphaleron")
print(f"  Solving η = (28/79)(3/4)(3/16π)(M₁/v_EW²)(Δm_eff)/g* for M₁:")
print(f"  Using NTE-geometric Δm_eff = m_ν₃ = 0.074 eV:")
print(f"    M₁ = {M_1_from_geometric:.3e} GeV")
print(f"  Using observed √(Δm²_atm) = 0.05 eV:")
print(f"    M₁ = {M_1_from_observed:.3e} GeV")
print(f"  Corpus quoted M₁: 6.06 × 10⁹ GeV")
print()
print(f"  Both calculations land at the right ORDER OF MAGNITUDE (~10⁹-10¹⁰ GeV).")
print(f"  Factor-of-2 spread reflects (i) factor-1.5 between geometric m_ν₃ and observed,")
print(f"  (ii) Davidson-Ibarra convention details (which variant of the formula,")
print(f"       sphaleron asphericity factor, exact g*(T) at leptogenesis epoch).")
print()

# ============================================================
# Conclusion
# ============================================================
print("=" * 70)
print("Conclusion")
print("=" * 70)
print("""
The chain M_R → m_ν₃ → Δm_eff is geometric in NTE, with the same factor-1.5
precision the corpus already acknowledges for m_ν₃.

This means the Davidson-Ibarra closure has THREE inputs of which TWO are
geometric in NTE:
  (i) v_EW = 246 GeV — SM-inherited under Path B; geometric in the weak sense.
  (ii) Δm_eff ≈ m_ν₃ ≈ 0.074 eV — derived in NTE from Hopf bundle on S³.
  (iii) M₁ ≈ 6.06 × 10⁹ GeV — constrained by observation; first-principles open (Gap 1).

The asymmetry-vs-magnitude framing's claim that "one input is missing" is correct:
M₁ is the remaining first-principles target. Two of three inputs are geometric.

Closing Gap 1 (M₁ from S³ curvature radius and T_GB) would make the η magnitude
a complete zero-parameter prediction.
""")

# ============================================================
# Suggestive numerics for the M₁ target
# ============================================================
print("=" * 70)
print("Suggestive numerics for M₁ from geometry (Gap 1 target)")
print("=" * 70)

T_GB_estimate = 0.4 * M_Pl  # corpus reference: T_GB ~ 0.4 M_Pl
print(f"Gauge birth temperature (corpus reference): T_GB ~ 0.4 M_Pl = {T_GB_estimate:.2e} GeV")
print()

M_1_target = 6.06e9
print(f"Hierarchies to consider:")
print(f"  M₁ / M_Pl = {M_1_target/M_Pl:.2e}")
print(f"  M₁ / T_GB = {M_1_target/T_GB_estimate:.2e}")
print(f"  M₁ / M_R  = {M_1_target/M_R:.2e}")
print(f"  v_EW / M_Pl = {v_EW/M_Pl:.2e}")
print(f"  v_EW / M_1 = {v_EW/M_1_target:.2e}")
print()
print(f"Geometric scale candidates (combinations of M_Pl, v_EW, T_GB):")
print(f"  M_Pl^{{1/2}} × v_EW^{{1/2}} = {(M_Pl*v_EW)**0.5:.2e} GeV  (natural geometric mean)")
print(f"  M_Pl^{{1/3}} × v_EW^{{2/3}} = {M_Pl**(1/3) * v_EW**(2/3):.2e} GeV")
print(f"  M_Pl^{{2/3}} × v_EW^{{1/3}} = {M_Pl**(2/3) * v_EW**(1/3):.2e} GeV")
print(f"  M_Pl^{{3/4}} × v_EW^{{1/4}} = {M_R:.2e} GeV  (this is M_R)")
print(f"  M_Pl^{{1/4}} × v_EW^{{3/4}} = {M_Pl**(1/4) * v_EW**(3/4):.2e} GeV")
print()
print(f"Target M₁ = 6.06 × 10⁹ GeV")
print()
print("Observation: M₁ does NOT obviously land at any simple Hopf-bundle-style")
print("power-law combination of M_Pl and v_EW. The closest low-power combinations")
print("are M_Pl^{1/2} × v_EW^{1/2} ≈ 5.5 × 10¹⁰ GeV (factor 9 too large) and")
print("M_Pl^{1/3} × v_EW^{2/3} ≈ 9.3 × 10⁸ GeV (factor 6.5 too small).")
print()
print("This suggests M₁'s geometric origin is NOT a simple power-law of geometric")
print("scales. It may involve T_GB or a different geometric handle (perhaps the")
print("see-saw scale times a suppression factor; perhaps related to neutrino")
print("Yukawa structure on S³). This is what Gap 1 / item (E) would investigate.")
