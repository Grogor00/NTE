"""
(E) Gap 1 / M₁ from S³ Geometry — numerical search.

Target: M₁ = 6.06 × 10⁹ GeV (corpus value, set to reproduce η_obs via Davidson-Ibarra).

Eta v2 §17.5.15 already excluded simple M_Pl^a · v_EW^b combinations:
  - M_Pl^{1/2}·v_EW^{1/2} = 5.5e10 GeV (factor 9 high)
  - M_Pl^{1/3}·v_EW^{2/3} = 9.04e7 GeV (factor 67 low)
    [NB: eta v2 cites 9.3e8 (factor 6.5 low). Recomputation gives 9.04e7
     (factor 67 low). See worksheet §8 for the bug catch.]

Per Gap 1 (corpus §22.5): the geometric handle (if any) involves T_GB (≈ 0.4 M_Pl)
or another scale beyond M_Pl and v_EW.

This script enumerates candidate combinations involving M_Pl, v_EW, T_GB, H_GB,
and the dimensionless α·M_Pl, with mass dimension 1, and reports those landing
within factor 3 of M₁.

Headline finding (worksheet §0):
  M₁ candidate = (M_Pl² · H_GB)^(1/3) = α^(1/3) · M_Pl^(4/3) = 8.08 × 10⁹ GeV
  Factor 1.33 high vs corpus M₁ = 6.06 × 10⁹ GeV
  Within Davidson-Ibarra's intrinsic factor-2 precision.
"""

import math
import itertools

# Scales (all in GeV unless noted)
M_Pl    = 1.22e19
v_EW    = 246.0
alpha   = 2.38e-47    # GeV^{-1}
H_GB    = alpha * M_Pl**2          # = 3.54e-9 GeV
T_GB    = 0.4 * M_Pl                # = 4.88e18 GeV (corpus line 683)
H_HH    = M_Pl                       # Hartle-Hawking upper bound
ell_GB  = 1.0 / H_GB                 # = 2.83e8 GeV^{-1}, S³ Hubble radius at gauge birth
N_e     = -math.log(alpha * M_Pl)   # = 63.4
N_lock  = 0.1

M1_target = 6.06e9   # corpus value

print("=" * 70)
print("Scale inventory:")
print(f"  M_Pl     = {M_Pl:.3e} GeV  (Planck mass)")
print(f"  v_EW     = {v_EW:.3e} GeV  (electroweak VEV)")
print(f"  T_GB     = {T_GB:.3e} GeV  (≈ 0.4 M_Pl, corpus line 683)")
print(f"  H_GB     = {H_GB:.3e} GeV  (= α·M_Pl²)")
print(f"  α·M_Pl   = {alpha*M_Pl:.3e}    (dimensionless)")
print(f"  N_e      = {N_e:.2f}            (= -ln(α·M_Pl))")
print(f"  M₁ target = {M1_target:.3e} GeV (Davidson-Ibarra → η_obs)")
print("=" * 70)
print()

# Candidates: M_Pl^a · v_EW^b · T_GB^c · H_GB^d
# Constraint: a + b + c + d = 1 (mass dimension 1)
# Note: T_GB and M_Pl are nearly degenerate (T_GB = 0.4 M_Pl); split them anyway
#       since the structural origin would differ.

# Try simple rationals for each exponent: -1, -2/3, -1/2, -1/3, 0, 1/3, 1/2, 2/3, 1, 4/3, 3/2
exps = [-1, -2/3, -1/2, -1/3, 0, 1/3, 1/2, 2/3, 1, 4/3, 3/2]

candidates = []
for a, b, c, d in itertools.product(exps, repeat=4):
    s = a + b + c + d
    if abs(s - 1) > 1e-6:
        continue
    # Skip trivial (M_Pl alone, v_EW alone, etc.)
    nonzero = [x for x in [a,b,c,d] if abs(x) > 1e-6]
    if len(nonzero) < 2:
        continue
    
    val = (M_Pl**a) * (v_EW**b) * (T_GB**c) * (H_GB**d)
    ratio = val / M1_target
    if 0.33 < ratio < 3.0:
        candidates.append((a, b, c, d, val, ratio, sum(abs(x)>1e-6 for x in [a,b,c,d])))

# Sort by closest to 1.0
candidates.sort(key=lambda x: abs(math.log(x[5])))

print(f"Candidates within factor 3 of M₁ ({M1_target:.2e} GeV):")
print(f"{'a (M_Pl)':>10} {'b (v_EW)':>10} {'c (T_GB)':>10} {'d (H_GB)':>10}  {'value (GeV)':>15} {'ratio':>10} {'#nonzero':>9}")
print("-" * 90)
for a, b, c, d, val, ratio, n in candidates[:25]:
    print(f"{a:>10.3f} {b:>10.3f} {c:>10.3f} {d:>10.3f}  {val:>15.3e} {ratio:>10.3f} {n:>9}")
print()

# Filter: prefer minimal-exponent solutions (fewer non-zero exponents)
print(f"Filtered: 2 nonzero exponents only:")
print(f"{'a (M_Pl)':>10} {'b (v_EW)':>10} {'c (T_GB)':>10} {'d (H_GB)':>10}  {'value (GeV)':>15} {'ratio':>10}")
print("-" * 80)
for a, b, c, d, val, ratio, n in candidates:
    if n != 2:
        continue
    print(f"{a:>10.3f} {b:>10.3f} {c:>10.3f} {d:>10.3f}  {val:>15.3e} {ratio:>10.3f}")
print()

# Specific structural candidate: (M_Pl² · H_GB)^{1/3} = α^{1/3} · M_Pl^{4/3}
print("=" * 70)
print("Structural candidate spotlight: (M_Pl² · H_GB)^(1/3)")
print("=" * 70)
m1_cand = (M_Pl**2 * H_GB)**(1/3)
print(f"  Formula: (M_Pl² · H_GB)^(1/3) = α^(1/3) · M_Pl^(4/3)")
print(f"  Value: {m1_cand:.3e} GeV")
print(f"  Ratio to M₁ target: {m1_cand/M1_target:.3f}")
print(f"  Equivalent forms:")
print(f"    M_Pl · (α·M_Pl)^(1/3)  = {M_Pl * (alpha*M_Pl)**(1/3):.3e}  ✓")
print(f"    M_Pl · e^(-N_e/3)      = {M_Pl * math.exp(-N_e/3):.3e}  ✓")
print(f"    (H_HH² · H_GB)^(1/3)   = {(M_Pl**2 * H_GB)**(1/3):.3e}  ✓ (same as above)")
print()

# Same with T_GB instead of M_Pl as the high scale
print("Alternative: (T_GB² · H_GB)^(1/3) — using T_GB as the upper scale")
m1_cand_T = (T_GB**2 * H_GB)**(1/3)
print(f"  Value: {m1_cand_T:.3e} GeV")
print(f"  Ratio to M₁ target: {m1_cand_T/M1_target:.3f}")
print()

# Test: 1/3-rule with a different upper scale combination
print("Probe: how special is the 1/3-rule? Try other geometric means:")
print(f"  (M_Pl · H_GB)^(1/2)        = {(M_Pl * H_GB)**(0.5):.3e}  ratio {((M_Pl * H_GB)**(0.5))/M1_target:.3f}")
print(f"  (M_Pl² · H_GB)^(1/3)       = {(M_Pl**2 * H_GB)**(1/3):.3e}  ratio {((M_Pl**2 * H_GB)**(1/3))/M1_target:.3f}  ★")
print(f"  (M_Pl³ · H_GB)^(1/4)       = {(M_Pl**3 * H_GB)**(1/4):.3e}  ratio {((M_Pl**3 * H_GB)**(1/4))/M1_target:.3f}")
print(f"  (M_Pl · H_GB²)^(1/3)       = {(M_Pl * H_GB**2)**(1/3):.3e}  ratio {((M_Pl * H_GB**2)**(1/3))/M1_target:.3f}")
print()

# Compare with eta v2 §17.5.15 excluded candidates (M_Pl^a · v_EW^b only)
print("For comparison, eta v2 §17.5.15 excluded candidates (M_Pl^a · v_EW^b only):")
print(f"  M_Pl^(1/2) · v_EW^(1/2)    = {(M_Pl**0.5) * (v_EW**0.5):.3e}  ratio {((M_Pl**0.5) * (v_EW**0.5))/M1_target:.3f}")
print(f"  M_Pl^(1/3) · v_EW^(2/3)    = {(M_Pl**(1/3)) * (v_EW**(2/3)):.3e}  ratio {((M_Pl**(1/3)) * (v_EW**(2/3)))/M1_target:.3f}")
print(f"  M_Pl^(2/3) · v_EW^(1/3)    = {(M_Pl**(2/3)) * (v_EW**(1/3)):.3e}  ratio {((M_Pl**(2/3)) * (v_EW**(1/3)))/M1_target:.3f}")
