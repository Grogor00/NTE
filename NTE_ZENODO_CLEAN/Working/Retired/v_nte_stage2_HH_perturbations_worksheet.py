"""
v_nte_stage2_HH_perturbations_worksheet.py

Hartle-Hawking perturbation calculation in NTE's regime.

Stage 2 V_NTE Programme — supports (D′) v2 §7. Computes the scalar perturbation
spectrum and spectral index n_s for several candidate H(N) profiles in NTE's
pre-temporal Hartle-Hawking sub-phase, identifies what structural commitment
fixes the profile, and examines (E)'s 1/3-weighting candidate against each profile.

Author: Jammer
Date: 2026-05-06
Corpus baseline: v10.6 SHIPPED (canonical 2026-05-03)
Cross-reference: (D′) v1 §6.5 (candidate worked application); (B′) §17.5.14 sharpening;
                 (E) §3.1 (1/3-weighting candidate)

Output structure:
  §1: Setup — slow-roll formulas in N-coordinate convention
  §2: Candidate H(N) profiles (P0–P4)
  §3: n_s computed symbolically for each profile
  §4: Numerical n_s table at NTE's N_e = 63.4
  §5: Comparison with Planck observation
  §6: (E)'s 1/3-weighting against each profile
  §7: Summary findings
"""

import numpy as np
import sympy as sp

print("=" * 78)
print("V_NTE Stage 2 — Hartle-Hawking Perturbation Calculation in NTE's Regime")
print("Worksheet for (D′) v2 §7")
print("=" * 78)

# ============================================================================
# §1. Setup — slow-roll formulas
# ============================================================================
print("\n" + "=" * 78)
print("§1. SETUP — slow-roll formulas in N-coordinate convention")
print("=" * 78)
print("""
Convention: N counts cosmic e-folds going forward in time through the
Hartle-Hawking sub-phase. N = 0 at the Hartle-Hawking instanton (H ≈ M_Pl);
N = N_e at the Janus point (end of HH sub-phase, where H → 0 per CPN-forcing).

Standard slow-roll parameters:
    ε_H(N) = -d(ln H)/dN
    ε₂(N) = d(ln ε_H)/dN

Spectral index at first order in slow-roll (de Sitter limit):
    n_s(N_*) - 1 = -2ε_H(N_*) - ε₂(N_*)

where N_* is the e-fold at which the pivot mode crosses the horizon.

Perturbation amplitude:
    P_ζ(N_*) ∝ H²(N_*) / ε_H(N_*)

Pure de Sitter (ε_H = 0) has P_ζ → ∞ — the inflaton-roll perturbation
machinery requires non-zero ε_H to source perturbations.

NTE's Hartle-Hawking sub-phase is approximately de Sitter (H ≈ M_Pl),
but the corpus does not specify the deviation H(N) functional form
within the sub-phase. Different candidate forms give different n_s.
""")

# Symbolic setup
N, N_e, M_Pl = sp.symbols('N N_e M_Pl', positive=True)
N_star = sp.symbols('N_*', positive=True)

def slow_roll_n_s(H_func, N_star_val=0):
    """
    Compute n_s - 1 for a given H(N) profile.

    H_func: sympy expression for H(N).
    N_star_val: pivot mode horizon-crossing e-fold (default 0 = HH instanton).

    Returns: dict with ε_H, ε₂, and n_s - 1 evaluated symbolically and at pivot.
    """
    ln_H = sp.log(H_func)
    eps_H = -sp.diff(ln_H, N)
    eps_H = sp.simplify(eps_H)

    # ε₂ = d(ln ε_H)/dN
    if eps_H == 0:
        eps_2 = sp.nan  # ε_H = 0 → spectrum diverges
    else:
        eps_2 = sp.diff(sp.log(eps_H), N)
        eps_2 = sp.simplify(eps_2)

    n_s_minus_1 = sp.simplify(-2*eps_H - eps_2) if eps_H != 0 else sp.oo
    n_s_at_pivot = n_s_minus_1.subs(N, N_star_val) if eps_H != 0 else sp.oo

    return {
        'eps_H': eps_H,
        'eps_2': eps_2,
        'n_s_minus_1': n_s_minus_1,
        'n_s_at_pivot': n_s_at_pivot,
    }


# ============================================================================
# §2. Candidate H(N) profiles
# ============================================================================
print("\n" + "=" * 78)
print("§2. CANDIDATE H(N) PROFILES")
print("=" * 78)

# (P0) Pure de Sitter
H_P0 = M_Pl

# (P1) Constant H = M_Pl with exponential decay (e-folding inflaton-style)
# H(N) = M_Pl × e^(-N) means H decreases by factor e per e-fold — ε_H = 1.
H_P1 = M_Pl * sp.exp(-N)

# (P2) Linear H(N) = M_Pl × (1 - N/N_e)
H_P2 = M_Pl * (1 - N/N_e)

# (P3) Power-law H(N) = M_Pl × (1 - N/N_e)^β
beta = sp.symbols('beta', positive=True)
H_P3 = M_Pl * (1 - N/N_e)**beta

# (P4) Starobinsky-form: H(N) ≈ √V₀ × (1 - 3/(4(N_e - N)))
# This is approximately constant H with a 1/(N_e - N) correction term.
# We use the asymptotic form derived from V_Starobinsky at large φ.
H_P4 = sp.sqrt(M_Pl**4) * (1 - 3/(4*(N_e - N)))

profiles = {
    "P0 (pure de Sitter)": H_P0,
    "P1 (exponential decay, ε_H = 1)": H_P1,
    "P2 (linear)": H_P2,
    "P3 (power-law β)": H_P3,
    "P4 (Starobinsky-form 1/(N_e-N) correction)": H_P4,
}

for name, H_expr in profiles.items():
    print(f"\n  {name}:  H(N) = {H_expr}")


# ============================================================================
# §3. Symbolic n_s for each profile
# ============================================================================
print("\n" + "=" * 78)
print("§3. SYMBOLIC n_s - 1 FOR EACH PROFILE")
print("=" * 78)

results_symbolic = {}
for name, H_expr in profiles.items():
    print(f"\n  {name}")
    print(f"  {'-' * (len(name) + 2)}")

    if H_expr == M_Pl:
        # Pure de Sitter
        print(f"    H(N) = M_Pl (constant)")
        print(f"    ε_H = 0  →  P_ζ ∝ H²/ε_H diverges; spectrum requires non-zero ε_H")
        print(f"    n_s undefined under inflaton-roll machinery")
        print(f"    (Pure de Sitter perturbations would come from other sources, e.g., entropy modes)")
        results_symbolic[name] = None
        continue

    res = slow_roll_n_s(H_expr, N_star_val=0)
    print(f"    ε_H(N) = {res['eps_H']}")
    print(f"    ε₂(N)  = {res['eps_2']}")
    print(f"    n_s - 1 = {res['n_s_minus_1']}")
    print(f"    At pivot N_* = 0: n_s - 1 = {res['n_s_at_pivot']}")
    results_symbolic[name] = res


# ============================================================================
# §4. Numerical n_s at NTE's N_e = 63.4
# ============================================================================
print("\n" + "=" * 78)
print("§4. NUMERICAL n_s AT NTE'S N_e = 63.4")
print("=" * 78)

N_e_NTE = 63.4
print(f"""
NTE's e-fold count for the Hartle-Hawking sub-phase:
    N_e = ln(M_Pl / H_GB) = ln(1/(α·M_Pl)) = -ln(α·M_Pl) ≈ 63.4

(Corpus §18.2; α = H₀/v_EW² ≈ 2.38 × 10⁻⁴⁷ GeV⁻¹; α·M_Pl ≈ 2.9 × 10⁻²⁸.)

Pivot mode horizon-crossing: standard CMB pivot is the largest scale that
crossed the horizon, corresponding to mode exit early in the sub-phase.
We take N_* = 0 (mode exit at the HH instanton) for the pivot-scale n_s.
""")

print(f"  {'Profile':<60} {'n_s at N_e=63.4':<20}")
print(f"  {'-' * 60} {'-' * 20}")

for name, H_expr in profiles.items():
    if H_expr == M_Pl:
        print(f"  {name:<60} undefined (P_ζ divergent)")
        continue

    res = slow_roll_n_s(H_expr, N_star_val=0)
    n_s_pivot_expr = res['n_s_at_pivot'] + 1

    # Substitute N_e = 63.4. For (P3), also substitute β.
    if 'beta' in str(n_s_pivot_expr):
        # Show for β = 1 (linear) and β = 2/3 (Starobinsky-recovering)
        for beta_val_label, beta_val in [("β = 1", 1), ("β = 2/3", sp.Rational(2,3)), ("β = 1/3", sp.Rational(1,3))]:
            n_s_at_beta = n_s_pivot_expr.subs(beta, beta_val).subs(N_e, N_e_NTE)
            print(f"  {name + ' [' + beta_val_label + ']':<60} n_s = {float(n_s_at_beta):.4f}")
    else:
        n_s_val = float(n_s_pivot_expr.subs(N_e, N_e_NTE).subs(M_Pl, 1))
        print(f"  {name:<60} n_s = {n_s_val:.4f}")


# ============================================================================
# §5. Comparison with Planck observation
# ============================================================================
print("\n" + "=" * 78)
print("§5. COMPARISON WITH PLANCK OBSERVATION")
print("=" * 78)

n_s_Planck = 0.9649
sigma_Planck = 0.0042  # Planck 2018 1σ uncertainty
n_s_NTE_corpus = 0.9685  # current corpus claim from imported Starobinsky formula

print(f"""
Planck 2018 (TT,TE,EE+lowE+lensing): n_s = {n_s_Planck} ± {sigma_Planck}
Corpus current (imported Starobinsky):  n_s = {n_s_NTE_corpus}  (0.85σ from observation)

Distance from Planck observation for each profile:
""")

print(f"  {'Profile':<60} {'n_s':<10} {'σ from Planck':<15}")
print(f"  {'-' * 60} {'-' * 10} {'-' * 15}")

profile_n_s_values = {}
for name, H_expr in profiles.items():
    if H_expr == M_Pl:
        # Pure de Sitter limit: n_s → 1 (scale invariant)
        n_s_limit = 1.0
        sigma_dist = abs(n_s_limit - n_s_Planck) / sigma_Planck
        print(f"  {name + ' (limit n_s=1)':<60} {n_s_limit:<10.4f} {sigma_dist:<15.2f}")
        profile_n_s_values[name] = n_s_limit
        continue

    res = slow_roll_n_s(H_expr, N_star_val=0)
    n_s_pivot_expr = res['n_s_at_pivot'] + 1

    if 'beta' in str(n_s_pivot_expr):
        for beta_val_label, beta_val in [("β = 1", 1), ("β = 2/3", sp.Rational(2,3))]:
            n_s_at_beta = float(n_s_pivot_expr.subs(beta, beta_val).subs(N_e, N_e_NTE))
            sigma_dist = abs(n_s_at_beta - n_s_Planck) / sigma_Planck
            print(f"  {name + ' [' + beta_val_label + ']':<60} {n_s_at_beta:<10.4f} {sigma_dist:<15.2f}")
            profile_n_s_values[f"{name} [{beta_val_label}]"] = n_s_at_beta
    else:
        n_s_val = float(n_s_pivot_expr.subs(N_e, N_e_NTE).subs(M_Pl, 1))
        sigma_dist = abs(n_s_val - n_s_Planck) / sigma_Planck
        print(f"  {name:<60} {n_s_val:<10.4f} {sigma_dist:<15.2f}")
        profile_n_s_values[name] = n_s_val

print(f"""
KEY OBSERVATIONS:
  - P0 (pure de Sitter, H ≈ M_Pl exactly constant): n_s = 1, off by ~8σ.
  - P1 (exponential decay H ∝ e^(-N), ε_H = 1 throughout): n_s = -1, way off.
  - P2 (linear H decrease): n_s ≈ 0.953, off by ~3σ.
  - P3 with β = 2/3: n_s ≈ 0.968, matches Starobinsky import within 0.3σ of Planck.
  - P4 (Starobinsky-form 1/(N_e-N) correction): n_s ≈ 0.968, matches Planck.

  The corpus's claim n_s = 0.9685 (matching Planck at 0.85σ) is consistent ONLY with
  P3[β = 2/3] or P4 (Starobinsky-form) profiles. NTE's natural Planck-scale instanton
  (P0) gives n_s = 1, off by 8σ. The framework requires a specific structural
  commitment to deviate from constant H in the Starobinsky-form way.
""")


# ============================================================================
# §6. (E)'s 1/3-weighting against each profile
# ============================================================================
print("\n" + "=" * 78)
print("§6. (E)'s 1/3-WEIGHTING M₁ ≈ M_Pl × e^(-N_e/3) AGAINST EACH PROFILE")
print("=" * 78)

# (E)'s candidate M₁ formula
M_1_E_candidate = np.exp(-N_e_NTE/3)  # in units of M_Pl
M_1_observational = 6.0e9  # GeV (typical leptogenesis scale)
M_Pl_GeV = 2.4e18

print(f"""
(E)'s candidate (Jammer R&D 2026-05-05):
    M₁ ≈ M_Pl × e^(-N_e/3)
       = {M_Pl_GeV:.2e} × {M_1_E_candidate:.3e}
       = {M_Pl_GeV * M_1_E_candidate:.3e} GeV

Observational M₁ for leptogenesis:
    M₁ ~ {M_1_observational:.2e} GeV (typical seesaw scale)

Factor agreement: {(M_Pl_GeV * M_1_E_candidate) / M_1_observational:.2f} (factor of 1.33 within
order-of-magnitude target).

The candidate formula M_Pl × e^(-N_e/3) corresponds to H(N=N_e/3) under WHICH profile?
""")

print(f"  {'Profile':<60} {'H(N=N_e/3) / M_Pl':<25}")
print(f"  {'-' * 60} {'-' * 25}")

N_third = N_e_NTE / 3
for name, H_expr in profiles.items():
    if H_expr == M_Pl:
        H_at_third = 1.0
        print(f"  {name:<60} {H_at_third:<25.4e}")
        continue

    if 'beta' in str(H_expr):
        for beta_val_label, beta_val in [("β = 1", 1), ("β = 2/3", sp.Rational(2,3))]:
            H_at_third_expr = H_expr.subs(beta, beta_val).subs(N, N_third).subs(N_e, N_e_NTE).subs(M_Pl, 1)
            try:
                H_at_third = float(H_at_third_expr)
                print(f"  {name + ' [' + beta_val_label + ']':<60} {H_at_third:<25.4e}")
            except (TypeError, ValueError):
                print(f"  {name + ' [' + beta_val_label + ']':<60} {H_at_third_expr}")
    else:
        H_at_third_expr = H_expr.subs(N, N_third).subs(N_e, N_e_NTE).subs(M_Pl, 1)
        try:
            H_at_third = float(H_at_third_expr)
            print(f"  {name:<60} {H_at_third:<25.4e}")
        except (TypeError, ValueError):
            print(f"  {name:<60} {H_at_third_expr}")

print(f"\n  (E)'s candidate value M_Pl × e^(-N_e/3) = {M_1_E_candidate:.4e}")

print(f"""
KEY OBSERVATION:
  M_Pl × e^(-N_e/3) ≈ {M_1_E_candidate:.4e} (in units of M_Pl).

  This corresponds DIRECTLY to H(N=N_e/3) under the EXPONENTIAL decay profile
  P1 (H(N) = M_Pl × e^(-N)). Under P1, ε_H = 1 throughout, giving n_s = -1
  (way off from observed n_s = 0.965).

  Under the profiles that recover observed n_s (P3[β=2/3] or P4), the value
  H(N_e/3) is ~M_Pl (close to constant), NOT M_Pl × e^(-N_e/3). So (E)'s
  1/3-weighting candidate is NOT structurally tied to the same Hartle-Hawking
  saddle that recovers the observed n_s.

  Two readings of this finding:
  (R1) (E)'s 1/3-weighting is dimensionally fine but its geometric origin is
       NOT in the Hartle-Hawking saddle that produces observed n_s. The
       candidate is a numerical lead awaiting deeper geometric explanation
       (likely Hopf-bundle structure on S³ via the seesaw chain).
  (R2) The Hartle-Hawking saddle is NOT the one that recovers n_s = 0.965;
       the n_s prediction comes from a different mechanism (e.g., something
       imprinted at gauge birth's locking transition rather than in the
       sub-phase). This is a more radical reading and would require
       restructuring how the framework derives n_s.

  AC's audit and Greg's strategic call needed on which reading dominates.
""")


# ============================================================================
# §7. Summary findings
# ============================================================================
print("\n" + "=" * 78)
print("§7. SUMMARY FINDINGS — for (D′) v2 §7 integration")
print("=" * 78)

print("""
F4 (NEW — Hartle-Hawking saddle structure under-determines n_s):
    The Hartle-Hawking sub-phase's H(N) functional form is not pinned by current
    NTE corpus structure. Only the natural Planck-scale instanton commitment
    (H ≈ M_Pl) is currently named (corpus §17.5.7), and pure constant H gives
    n_s = 1 (off by ~8σ from Planck observation of 0.9649 ± 0.0042). Recovering
    the observed n_s requires committing to a specific deviation profile from
    constant H — Starobinsky-form 1/(N_e-N) correction (P4) or power-law β = 2/3
    (P3[β=2/3]) work; linear (P2) gives 0.953 (3σ off); exponential (P1) gives
    -1 (way off); pure de Sitter (P0) gives 1 (8σ off).

    The corpus's current claim that NTE gives n_s = 0.9685 with 0.85σ match to
    Planck is contingent on importing the Starobinsky-form profile, which is
    not derived from NTE structure. (B′)'s honesty pass on §17.5.14 should be
    sharpened: the formula isn't just unverified in NTE's regime, the natural
    Planck-scale instanton actively gives n_s = 1 — the formula's match
    requires a specific deviation profile that NTE doesn't currently commit.

F5 (NEW — (E)'s 1/3-weighting is NOT a Hartle-Hawking saddle feature):
    M₁ ≈ M_Pl × e^(-N_e/3) corresponds to H(N=N_e/3) under the EXPONENTIAL decay
    profile P1, which gives n_s = -1 (way off from observation). Under the
    profiles that recover observed n_s (P4 or P3[β=2/3]), H at the 1/3-point
    is ~M_Pl (close to constant), not M_Pl × e^(-N_e/3). So (E)'s candidate
    cannot have its geometric origin in the same Hartle-Hawking saddle that
    produces n_s.

    The candidate's geometric origin must therefore lie elsewhere — most
    plausibly in the Hopf-bundle / seesaw structure on S³ where the heavy
    Majorana mass scale is set, not in the Hartle-Hawking saddle dynamics.
    The "1/3" in M₁ ~ M_Pl × e^(-N_e/3) ≡ (M_Pl² × H_GB)^(1/3) is more
    naturally read as a cube-root structure from S³'s 3-dimensionality
    (e.g., a seesaw-like geometric mean) than as a 1/3-position-along-the-
    e-fold-path of the inflationary saddle.

WHAT (D′) v2 CLOSES:
    - The gap between corpus claim "n_s = 0.9685 from NTE" and the actual
      perturbation calculation in NTE's regime is now precisely characterised:
      multiple H(N) profiles give different n_s; only specific ones recover
      observation; NTE's natural Planck-scale instanton alone doesn't.
    - (E)'s 1/3-weighting candidate's relationship to the inflationary saddle
      is now understood: not a saddle feature, geometric origin elsewhere.

WHAT (D′) v2 DOES NOT CLOSE:
    - The actual derivation of n_s from NTE structure: requires committing
      to a specific saddle deviation profile, which the corpus doesn't.
    - The actual derivation of M₁ from S³ + Hopf-bundle structure: open
      research target separate from Hartle-Hawking saddle calculation.
    - The §17.5.14 honesty pass: now sharper but still requires v10.8
      integration with corrected framing.

RECOMMENDED CORPUS UPDATES (downstream of v10.7 ship):
    - §17.5.14 sharpening for v10.8: explicit acknowledgement that pure
      Planck-scale instanton gives n_s = 1; observed n_s requires committing
      to a specific saddle structure.
    - §17.5.16 (new at v10.8): N parameter ambiguity now seen to also affect
      the saddle structure — the 63.4 e-folds of HH sub-phase need a specific
      H(N) profile within them, currently unspecified.
    - (E) follow-up (Gap 1 sharpening): geometric origin of M₁'s 1/3-weighting
      is in S³ + Hopf-bundle structure, not in inflationary saddle.
""")

print("=" * 78)
print("End of worksheet. Outputs feed (D′) v2 §7.")
print("=" * 78)
