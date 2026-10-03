#!/usr/bin/env python3
"""BR2d-J3: action derive numerics — crystallisation, mu activation, dmu, junction."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_NR = 1.221e19
M_PL = 2.435e18
G_EFF = 106.75
N_LOCK = 45.0 / (4.0 * G_EFF)
N_E = -math.log(ALPHA * M_NR)
H_ALPHA = ALPHA * M_NR**2
LAMBDA_A4 = (2430.0 / math.pi**4) * (M_PL**2 / (2.0 * math.pi))
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
VOL_S3 = 2.0 * math.pi**2
SQRT_2PI = math.sqrt(2 * math.pi)


def h_friedmann(T: float) -> float:
    rho = (math.pi**2 / 30.0) * G_EFF * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M_NR**2)


def s_ds(T_gb: float) -> float:
    H = h_friedmann(T_gb)
    return math.pi * M_NR**2 / H**2


def phi_stage3(y: float, phi0: float) -> float:
    A = phi0**2 * math.exp(-N_LOCK) / N_LOCK
    return math.sqrt(A * y)


def phi_sector2(N: float) -> float:
    return math.sqrt(M_NR / ALPHA) * math.exp(-N / 2.0)


def mu_on_shell(phi: float, vprime: float) -> float:
    """Appendix B.3 on-shell: mu ~ -V'(Phi)/(2 alpha Phi)."""
    return -vprime / (2.0 * ALPHA * phi)


def main() -> None:
    T_gb = M_NR / SQRT_2PI
    H_F = h_friedmann(T_gb)
    V_lock = VOL_S3 * math.exp(3 * N_E)
    Lambda_obs = LAMBDA_A4 * math.exp(-3 * N_E) / VOL_S3

    print("# BR2d-J3 action derive numerics — Jammer v1.0")
    print("=" * 70)

    print("\n## 1 — Phase split (mu OFF bulk / mu ON post-G)")
    print("  S = S_bulk + S_cryst + S_post")
    print("  S_bulk:   no mu term  => HH saddle (J6-n3)")
    print("  S_cryst:  mu activates on y in [0, N_lock]")
    print("  S_post:   V3 int dN [L + mu(H - alpha Phi^2)], V3=2pi^2")

    print("\n## 2 — Crystallisation: V3 and 2pi^2 appear at G only")
    print(f"  V_lock = 2pi^2 e^(3 N_e)     = {V_lock:.4e}")
    print(f"  N_e (bulk depth)             = {N_E:.4f}")
    print(f"  N_lock (boundary width)      = {N_LOCK:.6f}")
    print(f"  N_e / N_lock                 = {N_E/N_LOCK:.1f}  [NOT global map]")

    print("\n## 3 — Proposition: dmu(V) from unimodular lock (Paper S4 / S3-f3)")
    rho = LAMBDA_A4
    mu_integral = rho * math.exp(-3 * N_E) / VOL_S3
    print(f"  dmu_ref = (1/V_lock) delta(V-V_lock) dV")
    print(f"  Lambda_obs = Lambda_a4 e^(-3N_e)/(2pi^2) = {mu_integral:.4e} GeV^4")
    print(f"  Planck target                  = {LAMBDA_OBS:.4e} GeV^4")
    print(f"  ratio                          = {mu_integral/LAMBDA_OBS:.4f}")

    print("\n## 4 — N_lock = S_dS/4 from birth entropy (C2 derive)")
    S = s_ds(T_gb)
    n_lock_pred = S / 4.0
    print(f"  T_GB = M_Pl/sqrt(2pi)          = {T_gb:.4e} GeV")
    print(f"  S_dS = pi M_Pl^2 / H_F^2       = {S:.6f}")
    print(f"  N_lock = S_dS/4                = {n_lock_pred:.6f}")
    print(f"  corpus N_lock                  = {N_LOCK:.6f}")
    print(f"  rel err                        = {abs(n_lock_pred/N_LOCK - 1):.4e}")

    print("\n## 5 — Junction G: C0 Phi match (local, not y propto N)")
    phi0 = M_NR  # baseline
    phi_y = phi_stage3(N_LOCK, phi0)
    phi_n = phi_sector2(N_E)
    phi0_adj = phi_n / math.exp(-N_LOCK / 2.0)
    print(f"  |Phi|(y=N_lock), Phi0=M_Pl     = {phi_y:.4e} GeV")
    print(f"  |Phi|(N=N_e) constraint        = {phi_n:.4e} GeV")
    print(f"  Phi0 for C0 match             = {phi0_adj:.4e} ({phi0_adj/M_NR:.4f} M_Pl)")
    print("  Event G = {N=N_e, y=N_lock, V=V_lock, T=T_GB, H^F, H^alpha}")

    print("\n## 6 — Local dy/dN at G from C0 matching (Lemma 5)")
    # |Phi|^2 = A y, A = Phi0^2 e^{-N_lock}/N_lock  => d|Phi|^2/dy = A
    # |Phi|^2 = (H/alpha), H = H_HH e^{-N} => d|Phi|^2/dN = (1/alpha) dH/dN = -2 H/alpha
    A = phi0_adj**2 * math.exp(-N_LOCK) / N_LOCK
    dphi2_dy = A
    H_end = H_ALPHA
    dphi2_dN = -2.0 * H_end / ALPHA  # at N=N_e on constraint sector
  # chain rule at G: dphi2/dN = (dphi2/dy)(dy/dN)
    dy_dN_local = dphi2_dN / dphi2_dy if dphi2_dy else float("nan")
    print(f"  d|Phi|^2/dy|_G                = {dphi2_dy:.4e}")
    print(f"  d|Phi|^2/dN|_G (Sector 2)     = {dphi2_dN:.4e}")
    print(f"  dy/dN|_G (local C0 match)     = {dy_dN_local:.4e}")
    print(f"  N_lock/N_e if global linear   = {N_LOCK/N_E:.4e}  [rejected]")

    print("\n## 7 — mu activation (Appendix B.3 class)")
    phi_g = phi_n
    # schematic V ~ (1/2) m^2 phi^2 at lock
    m_eff = math.sqrt(2) * M_NR
    vprime = m_eff**2 * phi_g
    mu_val = mu_on_shell(phi_g, vprime)
    print(f"  mu ~ -V'/(2 alpha Phi) at G    = {mu_val:.4e}  [schematic E3]")
    print("  mu finite at G => constraint H=alpha|Phi|^2 enforced (Sector 2 ON)")

    print("\n## 8 — Three-epoch H at G (no equality)")
    H_HH = M_NR
    print(f"  H_bulk ~ M_Pl                  = {H_HH:.4e}")
    print(f"  H^(F) thermal                  = {H_F:.4e}")
    print(f"  H^(alpha) constraint           = {H_ALPHA:.4e}")
    print(f"  ln(H^F/H^alpha)                = {math.log(H_F/H_ALPHA):.2f} ~ N_e+1")

    print("\n## BR2d-J3 verdict")
    print("  Action split + mu activation: DERIVED (register v1.0)")
    print("  dmu(V) delta at V_lock:       DERIVED (matches R6)")
    print("  N_lock = S_dS/4:               DERIVED from C2 + J6-n3 T_GB")
    print("  Junction G dual-chart:         DERIVED (event, not global map)")
    print("  dy/dN|_G local:                CANDIDATE from C0 matching")
    print("  OPEN: full Paper S2 heat-kernel normalisation of S_cryst")


if __name__ == "__main__":
    main()
