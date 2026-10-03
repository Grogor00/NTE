#!/usr/bin/env python3
"""Open-gap pathway probe — rabbit holes → sunshine checks (Jammer v0.1)."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_NR = 1.221e19
M_PL = 2.435e18
G_EFF = 106.75
N_F = 180
N_E = -math.log(ALPHA * M_NR)
N_LOCK = 45.0 / (4.0 * G_EFF)
N_LOCK_NAIVE = 45.0 / (4.0 * (N_F / 2.0))
NS_T = 0.9685
PHI_INF = 15.9  # M_Pl,red units (C9)


def ns_counting() -> float:
    return 1.0 - 2.0 / N_E


def ns_c9(phi: float) -> float:
    return 1.0 - 8.0 / (phi**2)


def main() -> None:
    print("# Open-gap pathway probe — sunshine checks")
    print("=" * 72)

    # --- G-NS: two n_s formulas ---
    print("\n## G-NS — merge two n_s formulas")
    ns1 = ns_counting()
    ns2 = ns_c9(PHI_INF)
    # Phi from counting identity: 1 - 2/Ne = 1 - 8/Phi^2 => Phi = 2 sqrt(Ne) in M_Pl,red units
    phi_from_ne = 2.0 * math.sqrt(N_E)
    print(f"  n_s = 1 - 2/N_e           = {ns1:.6f}")
    print(f"  n_s = 1 - 8/Phi^2 (C9)    = {ns2:.6f}  (Phi={PHI_INF} M_Pl,red)")
    print(f"  Phi from identity Phi=2 sqrt(N_e) = {phi_from_ne:.4f} M_Pl,red")
    print(f"  C9 Phi / identity Phi     = {PHI_INF/phi_from_ne:.4f}")
    print("  SUNSHINE: same identity when Phi_inf = 2 sqrt(N_e) M_Pl,red (e-fold counting = Gaussian saddle).")
    print("  ACTION: derive Phi_inf = 2 sqrt(N_e) M_Pl from HH saddle integral (J6b), not fit.")

    # --- G-D1: V_NTE projection at G ---
    print("\n## G-D1 — V_NTE bulk-to-boundary (no smooth Phi extension)")
    phi_g = M_NR
    phi0 = 1.0541 * M_NR
    A = phi0**2 * math.exp(-N_LOCK) / N_LOCK
    phi_y = math.sqrt(A * N_LOCK)
    phi_n = math.sqrt(M_NR / ALPHA) * math.exp(-N_E / 2.0)
    H_alpha = ALPHA * M_NR**2
    V_post = 3.0 * ALPHA**2 * M_PL**2 * phi_g**4  # Friedmann inversion schematic
    m_e2 = (1.0 / 6.0) * 12.0 * M_NR**2
    V_bulk = 0.5 * m_e2 * (PHI_INF * M_PL) ** 2
    print(f"  |Phi|(y=N_lock) Stage 3     = {phi_y:.4e} GeV")
    print(f"  |Phi|(N=N_e) constraint     = {phi_n:.4e} GeV  (ratio {phi_y/phi_n:.4f})")
    print(f"  V_post ~ 3 alpha^2 M_Pl^2 Phi^4 @ G = {V_post:.4e} GeV^4")
    print(f"  V_bulk ~ (1/2) m_E^2 Phi^2 @ HH    = {V_bulk:.4e} GeV^4")
    print("  DEAD END: single smooth V(Phi) connecting V_pre to V_post on one chart.")
    print("  SUNSHINE: Pi_G + C0 at G; Role (B) bulk V_eff vs Role (A) boundary inversion (S17.5.19).")

    # --- LB-4 / J6: Sector 1 H from saddle Hessian ---
    print("\n## LB-4 / J6 — Sector 1 H_inf scale")
    phi = PHI_INF * M_PL
    v_sr = 0.5 * m_e2 * phi**2
    h_sr = math.sqrt(v_sr / (3.0 * M_PL**2))
    v_lit = 3.0 * ALPHA**2 * M_PL**2 * phi**4
    h_lit = math.sqrt(v_lit / (3.0 * M_PL**2))
    print(f"  H from saddle m_E (Role B)     = {h_sr:.4e} GeV ({h_sr/M_PL:.4f} M_Pl,red)")
    print(f"  H from literal alpha^2 Phi^4   = {h_lit:.4e} GeV ({h_lit/M_PL:.3e} M_Pl,red)")
    print(f"  H bulk ~ M_Pl                  = {M_NR:.4e} GeV")
    print("  DEAD END: cosmological alpha in bulk slow-roll (J6-n1 Track A).")
    print("  SUNSHINE: Sector 1 uses m_E from xi=1/6 Hessian; alpha constraint ON only Sector 2.")

    # --- N_F → g_eff (N_lock 19% gap) ---
    print("\n## N_lock — N_F vs g_eff thermal map")
    print(f"  N_lock = 45/(4 g_eff)          = {N_LOCK:.6f}")
    print(f"  N_lock naive 45/(4 N_F/2)      = {N_LOCK_NAIVE:.6f}")
    print(f"  rel gap                        = {abs(N_LOCK_NAIVE/N_LOCK - 1):.1%}")
    print("  DEAD END: identify N_F/2 with g_eff (Dirac mult != thermal dof).")
    print("  SUNSHINE: derive g_eff(T_GB) from SM content at gauge birth; N_F enters a_4 only.")

    # --- LB-2 Lambda (R6) ---
    vol = 2.0 * math.pi**2 * math.exp(3 * N_E)
    lam_a4 = (2430.0 / math.pi**4) * (M_PL**2 / (2.0 * math.pi))
    lam_pred = lam_a4 * math.exp(-3 * N_E) / (2.0 * math.pi**2)
    lam_obs = (2.3e-3 * 1e-9) ** 4
    print("\n## LB-2 — Lambda structural f (R6)")
    print(f"  Lambda_pred / Lambda_obs       = {lam_pred/lam_obs:.4f}")
    print("  DEAD END: continuous f_4 tune ~ 10^-84; M1/M2/M3 naive routes.")
    print("  SUNSHINE: delta(V-V_lock) + comoving 2pi^2 e^{3Ne} — REGISTER CLOSED; proof = BR2d-J3+S4.")

    # --- 2pi^2 vs 4pi ---
    print("\n## 2pi^2 vs 4pi (subdominant)")
    print(f"  ratio 2pi^2 / (4pi)            = {2*math.pi**2 / (4*math.pi):.4f}")
    print("  OPEN: spectral vs comoving normalisation — document as register choice (Paper S4 Lemma 2).")

    # --- Master sunshine pattern ---
    print("\n## META — sunshine pattern (post LB-1/LB-6/R6/R4)")
    print("  1. Dissolve false unified chart (single H(N), pre-G S3, Phi identity, N_F=g_eff).")
    print("  2. Event G: sequential activation + dual charts + Pi_G projection.")
    print("  3. Derive queue: J6 Sector-1 ODE -> D1 junction proof -> N_F/g_eff thermal map -> J1/J3 parallel.")

    print("\n## Priority derive queue (executable)")
    for i, item in enumerate(
        [
            "J6-D1: integrate xi=1/6 bulk ODE; last 60 e-folds H_inf(N) + Phi_inf=2sqrt(N_e)M_Pl",
            "D1-PROJ: formalise Pi_G + Stage3 + C0 as V_NTE pre/post (no smooth Phi)",
            "S2-NF: g_eff(T_GB) from SM thermal content; close N_lock 19% without tuning",
            "J6-HESS: full coupled (H,Phi) Hessian at saddle (upgrade J6-n3 partial)",
            "LB-5: apply BR5 prose patch (N_lock != N_e)",
            "J1: mu(x,N) covariant sign-off (LB-3)",
            "J3/J2: Born + Tomita parallel (non-blocking)",
        ],
        1,
    ):
        print(f"  {i}. {item}")


if __name__ == "__main__":
    main()
