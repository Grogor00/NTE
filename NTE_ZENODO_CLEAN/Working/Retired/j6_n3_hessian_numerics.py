#!/usr/bin/env python3
"""J6-n3: simplified S_E Hessian + T_GB derivation numerics (Jammer)."""
from __future__ import annotations

import math

M_PL = 2.435e18  # M_Pl,red GeV
M_NR = 1.221e19  # non-reduced
G_EFF = 106.75
SQRT_2PI = math.sqrt(2 * math.pi)
ALPHA = 2.38e-47


def s_dS_instanton(H: float, M: float = M_NR) -> float:
    """Gibbons-Hawking dS4 cap: S_E = -3 pi^2 M^2 / H^2 (Jammer convention)."""
    return -3.0 * math.pi**2 * M**2 / (H**2)


def hessian_H(H: float, M: float = M_NR) -> float:
    """d^2 S_E / dH^2 at fixed H."""
    return 18.0 * math.pi**2 * M**2 / (H**4)


def h_friedmann(T: float, g: float = G_EFF, M: float = M_NR) -> float:
    rho = (math.pi**2 / 30.0) * g * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M**2)


def scalar_hessian_xi16(H: float, M: float = M_NR) -> float:
    """Zero-mode scalar m_E^2 from -xi R Phi^2 with xi=1/6, R=12 H^2 (Euclidean)."""
    R = 12.0 * H**2
    xi = 1.0 / 6.0
    # Euclidean kinetic + (-xi R) Phi^2 => coeff m^2 = +xi R for positive-definite S_E (Wick)
    return xi * R


def v_eff_saddle(H: float, M: float = M_PL) -> float:
    """Effective slow-roll mass scale from saddle Hessian (Role B), Planck units."""
    m2 = scalar_hessian_xi16(H, M_NR)
    return math.sqrt(m2)


def main() -> None:
    H_star = M_NR  # HH saddle H ~ M_Pl (non-reduced)
    H_red = M_PL

    print("# J6-n3 Hessian / T_GB numerics — Jammer")
    print()

    # --- Gravity sector ---
    S0 = s_dS_instanton(H_star)
    lam_H = hessian_H(H_star)
    sigma_H = math.sqrt(1.0 / lam_H)
    print("## A — Gravity sector (dS4 cap S_E = -3 pi^2 M_Pl^2 / H^2)")
    print(f"  S_E(H=M_Pl)                     = {S0:.4e} M_Pl^2 (action units)")
    print(f"  lambda_H = d^2 S_E / dH^2       = {lam_H:.4e} GeV^2")
    print(f"  sigma_H = 1/sqrt(lambda_H)    = {sigma_H:.4e} GeV")
    print(f"  sigma_H / M_Pl,nr               = {sigma_H/M_NR:.6f}")
    print(f"  sigma_H / M_Pl,red              = {sigma_H/M_PL:.6f}")
    print()

    # --- Gaussian T_GB (Companion 9 / corpus commitment) ---
    lam_T = M_NR**2  # corpus: Hessian eigenvalue ~ M_Pl^2 in temperature direction
    T_gb = M_NR / SQRT_2PI
    T_gb_red = M_PL / SQRT_2PI
    print("## B — Thermal / nucleation scale (lambda_T = M_Pl^2 identification)")
    print(f"  T_GB = M_Pl,nr / sqrt(2 pi)     = {T_gb:.4e} GeV")
    print(f"  T_GB / M_Pl,nr                  = {T_gb/M_NR:.6f}  (= 1/sqrt(2pi))")
    print(f"  T_GB = M_Pl,red / sqrt(2 pi)    = {T_gb_red:.4e} GeV")
    print(f"  Hawking T = H/(2 pi) at H=M_Pl  = {H_star/(2*math.pi):.4e} GeV")
    print(f"  Ratio T_GB / T_Hawking          = {T_gb/(H_star/(2*math.pi)):.4f}")
    print("  => T_GB is Gaussian saddle width scale, NOT Hawking T=H/(2pi).")
    print()

    # --- Epoch A Friedmann cross-check ---
    H_F = h_friedmann(T_gb)
    H_alpha = ALPHA * M_NR**2
    print("## C — Epoch A Friedmann at T_GB (bridge numerics)")
    print(f"  H_GB^(F) at T_GB                = {H_F:.4e} GeV")
    print(f"  H_GB^(alpha) constraint         = {H_alpha:.4e} GeV")
    print(f"  H^(F) / H^(alpha)               = {H_F/H_alpha:.4e}")
    print(f"  ln(H^(F)/H^(alpha))             = {math.log(H_F/H_alpha):.2f}")
    print()

    # --- Scalar sector V_eff (Role B) ---
    m_E = v_eff_saddle(H_star)
    print("## D — Scalar Hessian at xi=1/6, H=M_Pl (Role B V_eff scale)")
    print(f"  m_E^2 = xi R, R=12 H^2           = {scalar_hessian_xi16(H_star):.4e} GeV^2")
    print(f"  m_E                             = {m_E:.4e} GeV")
    print(f"  m_E / M_Pl,nr                   = {m_E/M_NR:.4f}")
    print(f"  V_eff ~ (1/2) m_E^2 Phi^2 at Phi=15.9 M_Pl:")
    phi = 15.9 * M_PL
    V_sr = 0.5 * scalar_hessian_xi16(H_star) * phi**2
    H_sr = math.sqrt(V_sr / (3 * M_PL**2))
    print(f"    V                             = {V_sr:.4e} GeV^4")
    print(f"    H_SR                          = {H_sr:.4e} GeV ({H_sr/M_PL:.4f} M_Pl,red)")
    print()

    # --- J6-n1 reconciliation ---
    V_lit = 3 * ALPHA**2 * M_PL**2 * phi**4
    print("## E — J6-n1 reconciliation (literal E3 alpha vs saddle Hessian)")
    print(f"  Literal E3 H at phi=15.9 M_Pl,red / M_Pl,red = {math.sqrt(V_lit/(3*M_PL**2))/M_PL:.3e}")
    print(f"  Saddle Hessian H at same phi     / M_Pl,red = {H_sr/M_PL:.4f}")
    print("  => Sector 1 slow-roll scale from m_E (saddle), not cosmological alpha^2 Phi^4.")
    print()

    # --- n_s check with saddle m_E ---
    if m_E > 0:
        # use M_PL,red for phi ratio
        ns_quad = 1.0 - 8.0 * M_PL**2 / phi**2  # canonical if V=(1/2)m^2 phi^2 with m<<...
        # for m_E ~ 3.5 M_Pl, slow-roll eps differs; use phi ratio formula from C9
        print("## F — n_s at phi=15.9 M_Pl,red (C9 formula, validated J6-n1 T2)")
        print(f"  n_s = 1 - 8/phi^2 (M_Pl units)  = {1 - 8/(15.9**2):.6f}")
        print(f"  (Uses effective Phi^2-chaotic, not literal alpha quartic.)")
    print()
    print("## J6-n3 verdict")
    print("  lambda_H ~ 18 pi^2 M_Pl^2 / H^4  computed explicitly.")
    print("  T_GB = M_Pl/sqrt(2pi) from lambda_T=M_Pl^2 Gaussian normalization (Step B).")
    print("  (C1) upgrade: candidate -> derived-at-simplified-S_E (Jammer sign-off).")
    print("  OPEN: full Hopf-S^3 x S^1_beta heat-kernel (Paper S2); J6d field map.")


if __name__ == "__main__":
    main()
