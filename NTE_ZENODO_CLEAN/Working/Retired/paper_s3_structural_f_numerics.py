#!/usr/bin/env python3
"""Paper S3 structural f — suppression budget (Impact #2)."""
from __future__ import annotations

import math

M_PL = 2.435e18
BETA_GB = math.sqrt(2 * math.pi) / M_PL
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
LAMBDA_NAIVE = (45 / math.pi**2) * M_PL**4
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
F4_TUNING = LAMBDA_OBS / LAMBDA_NAIVE
S_STRUCT_REQ = LAMBDA_OBS / LAMBDA_A4


def log10_ratio(x: float, base: float) -> float:
    return math.log10(x / base) if base > 0 else float("nan")


def main() -> None:
    print("Paper S3 structural f — suppression budget (v0.1)")
    print("=" * 55)
    rows = [
        ("Lambda_obs", LAMBDA_OBS),
        ("Lambda_naive (a0/Vol)", LAMBDA_NAIVE),
        ("Lambda_a4 residual", LAMBDA_A4),
    ]
    for name, val in rows:
        print(f"{name:28s} = {val:.4e} GeV^4  log10/L_obs = {log10_ratio(val, LAMBDA_OBS):.2f}")
    print()
    print(f"Unimodular removes:        log10 ~ {log10_ratio(LAMBDA_NAIVE, LAMBDA_A4):.1f} OOM")
    print(f"Remaining gap (a4):        log10 ~ {log10_ratio(LAMBDA_A4, LAMBDA_OBS):.1f} OOM")
    print(f"S_struct required:         {S_STRUCT_REQ:.4e}  (~10^{-83})")
    print()
    print("M1 tuning route (FORBIDDEN as solution):")
    print(f"  f4_required = {F4_TUNING:.4e}  log10 = {math.log10(F4_TUNING):.2f}")
    print()
    # CC2008: a_{2n}=0 for n>=2 on round S3xS1 — illustrative exponential tail
    print("Candidate R3 (CC2008 a6+ exponential tail):")
    print("  Must supply ~83 log10 suppression from DERIVED spectral gap — not fit.")
    print()
    print("Falsified alone: M2 area heuristic, M3 beta_GB O(1), f4 tuning.")


if __name__ == "__main__":
    main()
