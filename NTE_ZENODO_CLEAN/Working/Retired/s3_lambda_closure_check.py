#!/usr/bin/env python3
"""Paper S3 closure formula check — derived fit candidate."""
from __future__ import annotations
import math

M_PL = 2.435e18
M_NR = 1.221e19
ALPHA = 2.38e-47
N_E = -math.log(ALPHA * M_NR)
VOL_S3 = 2 * math.pi**2
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4


def lambda_closure() -> float:
    return LAMBDA_A4 * math.exp(-3 * N_E) / VOL_S3


if __name__ == "__main__":
    lam = lambda_closure()
    print(f"Lambda_NTE closure = Lambda_a4 * exp(-3 N_e) / (2 pi^2)")
    print(f"N_e = {N_E:.6f}")
    print(f"Lambda_pred = {lam:.4e} GeV^4")
    print(f"Lambda_obs  = {LAMBDA_OBS:.4e} GeV^4")
    print(f"ratio pred/obs = {lam/LAMBDA_OBS:.4f}")
    print(f"log10 ratio    = {math.log10(lam/LAMBDA_OBS):.3f}")
