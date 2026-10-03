#!/usr/bin/env python3
"""Paper S3 Lambda_NTE residual — order-of-magnitude scaffold (Priority IV-3)."""
from __future__ import annotations

import math

M_PL_GEV = 2.435e18
N_F = 180
BETA_GB = math.sqrt(2 * math.pi) / M_PL_GEV
VOL_M = 2 * math.pi**2 * BETA_GB  # Hopf-S3 x S1_GB volume scale
A0 = N_F * BETA_GB / 2
A4_R2 = 270 * BETA_GB  # Phase S2-C-B leading piece

LAMBDA_OBS_GEV4 = (2.3e-3 * 1e-9) ** 4  # ~2.3 meV → GeV (ℏ=c=1: 1 eV = 10^-9 GeV)

# a4-level residual S2-D §2.3: Lambda ~ (2430/pi^4) * beta_GB^-2 ~ M_Pl^2/(2pi) GeV^4
LAMBDA_A4_GEV4 = (2430 / math.pi**4) * (M_PL_GEV**2 / (2 * math.pi))
LAMBDA_NAIVE_GEV4 = (45 / math.pi**2) * M_PL_GEV**4  # per-unit-volume naive ~5 M_Pl^4

print("# Paper S3 Lambda_NTE — order-of-magnitude table (GeV^4 primary; S2-D §2.3)")
print()
print("| Channel | Lambda [GeV^4] | vs obs | log10 ratio to obs |")
print("|---------|----------------|--------|---------------------|")
for name, val in [
    ("Observed (~meV)^4", LAMBDA_OBS_GEV4),
    ("Naive spectral a0 / Vol(M)", LAMBDA_NAIVE_GEV4),
    ("a4 residual (S2-D §2.3)", LAMBDA_A4_GEV4),
]:
    ratio = val / LAMBDA_OBS_GEV4 if LAMBDA_OBS_GEV4 else float("nan")
    logr = math.log10(ratio) if ratio > 0 else float("nan")
    print(f"| {name} | {val:.4e} | {ratio:.2e}x | {logr:.2f} |")

print()
print(f"N_F={N_F}, Vol(M)~{VOL_M:.4e} GeV^-1, a0={A0:.4e} GeV")
print("Unimodular projects naive ~M_Pl^4; residual still ~10^83 off at a4 level (S2-D honest scope).")
print("Paper S3 must identify suppression mechanism stack (f4, holographic, boundary).")
