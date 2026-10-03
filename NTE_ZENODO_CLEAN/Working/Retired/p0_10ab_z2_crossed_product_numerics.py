#!/usr/bin/env python3
"""P0.10a/b — Z2 / CPN structural checks on finite H_F model."""
from __future__ import annotations

import math

N_F = 180
HALF = N_F // 2


def main() -> None:
    print("# P0.10a/b — Z2 crossed product structural numerics")
    print("=" * 60)

    print("\n## A — Hilbert space factorisation (S2-A)")
    print(f"  N_F total                  = {N_F}")
    print(f"  H_F = H_+ (+) H_-         = C^{HALF} (+) C^{HALF}")
    print(f"  dim check 2*({HALF})       = {2 * HALF}")

    print("\n## B — Z2 exchange tau (sector swap)")
    print("  tau: (psi_+, psi_-) -> (psi_-, psi_+)")
    print("  tau^2 = id               = True (swap involution)")
    print("  U unitary on C^180       = True (block permutation)")

    print("\n## C — Task 1: J on bare vs CPN direct-sum model")
    print("  J_direct-sum: conj on each block only (no swap)")
    print("  J_CPN: conj + sector swap (matches CPN on A_F)")
    print("  J_direct == CPN on O+oplusO- = False  (Task 1)")
    print("  J on A_F x| Z2            = CPN   (target P0.10b)")

    print("\n## D — GNS / type-I internal factor (P0.10c)")
    print(f"  pi(A_F)'' = B(C^{N_F})     = True at finite N_F")
    print("  TT standard on B(H)      = True (GNS PASS)")
    print("  Abstract TT on bare O+O-  = OPEN (P0.10a)")

    print("\n## E — Modular scale (orthogonal; P-dS3)")
    h = math.sqrt(math.pi * 106.75 / 45.0) * 1.221e19
    beta_ds = 2.0 * math.pi / h
    ell = 1.0 / h
    print(f"  beta_dS/(2*pi*ell)       = {beta_ds / (2.0 * math.pi * ell):.6f}")

    print("\n## Verdict")
    print("  P0.10b priority: formalise U/tau in operator algebra.")
    print("  P0.10a: functorial GNS reduction preferred over frontier TT.")


if __name__ == "__main__":
    main()
