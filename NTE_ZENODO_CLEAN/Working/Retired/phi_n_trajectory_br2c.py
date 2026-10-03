#!/usr/bin/env python3
"""BR2c: two-sector Phi(N) attack — Role (A) vs (B) + route verdicts."""
from __future__ import annotations

import math

ALPHA = 2.38e-47  # GeV^-1
M_PL = 1.221e19  # GeV
NS_TARGET = 0.9685
PHI_INF_RATIO = 15.9  # Companion 9 M_Pl units


def h_epoch_b_exp(N: float, h_hh: float = M_PL) -> float:
    return h_hh * math.exp(-N)


def phi_from_h(H: float) -> float:
    return math.sqrt(max(H / ALPHA, 0.0))


def h_phi2_chaotic(N: float, ne: float = 63.4, h0: float = M_PL) -> float:
    x = max(1.0 - N / ne, 1e-12)
    return h0 * math.sqrt(x)


def eps_h(H_fn, N: float, dN: float = 1e-4) -> float:
    H0 = H_fn(N)
    H1 = H_fn(N + dN)
    return -(math.log(H1) - math.log(H0)) / dN


def main() -> None:
    h_alpha = ALPHA * M_PL**2
    n_e_a = -math.log(ALPHA * M_PL)
    phi_nete_hh = phi_from_h(M_PL)
    phi_inf = PHI_INF_RATIO * M_PL

    print("BR2c two-sector Phi(N) attack — numerics (v0.1)")
    print("=" * 64)

    print("\n## Role magnitude clash at HH (H ~ M_Pl)")
    print(f"  |Phi_NTE| (Role A, sqrt(M_Pl/alpha)) = {phi_nete_hh:.4e} GeV")
    print(f"  Phi_inf   (Role B, 15.9 M_Pl)        = {phi_inf:.4e} GeV")
    print(f"  ratio Phi_inf / |Phi_NTE|            = {phi_inf / phi_nete_hh:.4e}")
    print("  => single-field identification FAILS unless map derived (BR2c R4)")

    print("\n## Sector 2 — Role (A) exponential (BR2 v0.1)")
    h_end = h_epoch_b_exp(n_e_a)
    print(f"  N_e^A = -ln(alpha M_Pl)              = {n_e_a:.4f}")
    print(f"  H(N_e)/H^(alpha) - 1               = {h_end / h_alpha - 1.0:.4e}")
    print(f"  |Phi(N_e)|/M_Pl - 1                 = {phi_from_h(h_end) / M_PL - 1.0:.4e}")
    eps_exp = 1.0
    print(f"  n_s (SR import, eps=1)               = {1 - 2 * eps_exp:.4f}  [FAIL vs {NS_TARGET}]")

    print("\n## Sector 1 — Role (B) Companion 9 Phi^2 chaotic")
    ns_c9 = 1.0 - 8.0 / PHI_INF_RATIO**2
    ne_c9 = PHI_INF_RATIO**2 / 4.0
    print(f"  n_s = 1 - 8/Phi^2                    = {ns_c9:.6f}  (target {NS_TARGET})")
    print(f"  N_e ~ Phi^2/(4 M_Pl^2)               = {ne_c9:.4f}")
    print(f"  eps ~ (1 - n_s)/2                    = {(1 - NS_TARGET) / 2:.5f}")

    print("\n## Route R1 — single constant-epsilon exponential")
    eps_sr = (1.0 - NS_TARGET) / 2.0
    n_e_needed = math.log(M_PL / h_alpha) / eps_sr
    print(f"  eps for n_s                          = {eps_sr:.5f}")
    print(f"  N_e required (same H drop)           = {n_e_needed:.1f}  [FAIL vs corpus 63.4]")

    print("\n## Route R3 — piecewise constant eps (illustrative)")
    n1 = 60.0
    drop_total = math.log(M_PL / h_alpha)
    drop1 = eps_sr * n1
    drop2 = drop_total - drop1
    n2 = drop2 / 1.0
    print(f"  N1={n1} at eps={eps_sr:.4f}  -> drop {drop1:.2f}")
    print(f"  N2 at eps=1.0             -> {n2:.1f} e-folds  [ad hoc, not derived]")

    print("\n## C9 H(N)=H_HH sqrt(1-N/Ne) — endpoint check")
    for n in (0, 30, 60, 63.4):
        h = h_phi2_chaotic(n)
        e = eps_h(lambda x: h_phi2_chaotic(x), n)
        print(f"  N={n:5.1f}  H={h:.3e} GeV  eps={e:.4f}  n_s~{1-2*e:.4f}")
    print(f"  H(Ne) = {h_phi2_chaotic(63.4):.3e} GeV  vs H^(alpha) = {h_alpha:.3e} GeV")
    print("  => C9 sqrt profile does NOT reach H^(alpha) — sector split required")

    print("\n## Verdict table")
    routes = [
        ("R1 single ansatz", "EXCLUDED"),
        ("R2 two-sector (Role A/B)", "PROPOSED"),
        ("R3 piecewise eps", "ILLUSTRATIVE ONLY"),
        ("R4 field map at lock", "OPEN (Jammer J6)"),
    ]
    for name, v in routes:
        print(f"  {name:32s}  {v}")

    print("\n## Register")
    print("  Sector 2 (A): BR2 endpoints PASS; n_s not from this sector")
    print("  Sector 1 (B): C9 n_s PASS; H(N) does not span full lock drop")
    print("  Jammer: derive Sector 1 from action; BR2d map at lock")


if __name__ == "__main__":
    main()
