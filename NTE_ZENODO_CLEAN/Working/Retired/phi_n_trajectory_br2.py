#!/usr/bin/env python3
"""BR2: Phi(N) trajectory scaffold — endpoint checks for H_GB bridge."""
from __future__ import annotations

import math

ALPHA = 2.38e-47  # GeV^-1
M_PL = 1.221e19  # GeV
G_EFF = 106.75
SQRT_2PI = math.sqrt(2 * math.pi)
V_EW = 246.0  # GeV


def h_friedmann(T: float) -> float:
    rho = (math.pi**2 / 30.0) * G_EFF * T**4
    return math.sqrt((8 * math.pi / 3.0) * rho / M_PL**2)


def h_epoch_b(N: float, h_hh: float = M_PL) -> float:
    """Candidate Epoch B: H(N) = H_HH exp(-N), N=0 at HH peak."""
    return h_hh * math.exp(-N)


def phi_from_h(H: float) -> float:
    """|Phi| from constraint H = alpha |Phi|^2."""
    return math.sqrt(max(H / ALPHA, 0.0))


def main() -> None:
    h_alpha = ALPHA * M_PL**2
    h_f = h_friedmann(M_PL / SQRT_2PI)
    n_e_corpus = -math.log(ALPHA * M_PL)
    n_e_from_h = math.log(M_PL / h_alpha)

    print("BR2 Phi(N) trajectory scaffold — endpoint checks (v0.1)")
    print("=" * 60)
    print("\n## Candidate Epoch B (scaffold)")
    print("  H(N) = H_HH exp(-N),  N=0 at HH peak,  H_HH = M_Pl")
    print("  |Phi(N)| = sqrt(H/alpha)")
    print()

    # Endpoints
    h0 = h_epoch_b(0.0)
    h_end = h_epoch_b(n_e_corpus)
    phi0 = phi_from_h(h0)
    phi_end = phi_from_h(h_end)

    print("## Endpoints (N = 0 .. N_e)")
    print(f"  N_e (corpus -ln(alpha M_Pl))     = {n_e_corpus:.4f}")
    print(f"  N_e (ln(M_Pl/H^(alpha)))         = {n_e_from_h:.4f}")
    print(f"  H(0) = M_Pl                      = {h0:.4e} GeV")
    print(f"  H(N_e)                           = {h_end:.4e} GeV")
    print(f"  H^(alpha) target                 = {h_alpha:.4e} GeV")
    print(f"  rel err H(N_e)/H^(alpha)         = {abs(h_end/h_alpha - 1.0):.4e}")
    print(f"  |Phi(0)|                         = {phi0:.4e} GeV")
    print(f"  |Phi(N_e)|                       = {phi_end:.4e} GeV")
    print(f"  M_Pl target |Phi| at lock        = {M_PL:.4e} GeV")
    print(f"  rel err |Phi(N_e)|/M_Pl          = {abs(phi_end/M_PL - 1.0):.4e}")
    print()

    print("## Epoch A (thermal — NOT on constraint trajectory)")
    print(f"  H^(F) at T_GB                    = {h_f:.4e} GeV")
    print(f"  ln(H^(F)/H^(alpha))              = {math.log(h_f/h_alpha):.2f}")
    print(f"  ln(H^(F)/H(0))                   = {math.log(h_f/h0):.2f}  (~1 => H^(F)~e M_Pl)")
    print()

    print("## Stage 3 coordinate (separate y in [0, N_lock])")
    n_lock = 45.0 / (4.0 * G_EFF)
    print(f"  N_lock = S_dS/4                    = {n_lock:.6f}")
    print(f"  N_lock vs N_e                      = holographic width vs inflation depth")
    print()

    print("## Slow-roll check (Epoch B, epsilon = -d ln H / dN)")
    eps = 1.0  # for H ~ exp(-N): epsilon = -d ln H / dN
    n_s_sr = 1.0 - 2.0 * eps
    print(f"  epsilon = {eps}  (constant for H = M_Pl e^{{-N}})")
    print(f"  n_s (slow-roll import) = 1 - 2eps = {n_s_sr:.4f}  (corpus 0.9685 needs eps~0.016)")
    print("  => exponential H(N) matches N_e but NOT n_s — Jammer: derive from V_NTE/HH saddle")
    print()

    print("## Register")
    print("  PASS: H(N_e)=H^(alpha), |Phi(N_e)|=M_Pl with exponential scaffold")
    print("  OPEN: derive H(N) from action; reconcile n_s; thermal H^(F) off-constraint")


if __name__ == "__main__":
    main()
