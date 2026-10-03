#!/usr/bin/env python3
"""Paper S3 M3 — beta_GB boundary / volume scaling OOM."""
from __future__ import annotations

import math

M_PL = 2.435e18
BETA_GB = math.sqrt(2 * math.pi) / M_PL
VOL_M = 2 * math.pi**2 * BETA_GB
A4 = 270 * BETA_GB
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4

# OOM: a4 / Vol^2 type scaling
lambda_vol2 = A4 / VOL_M**2 if VOL_M else float("nan")

# Seam factor: extrinsic ~ 1/beta_GB integrated over S1 circumference ~ beta_GB => O(1)
seam_factor = 1.0  # placeholder
lambda_m3_heur = lambda_vol2 * seam_factor

print("# Paper S3 M3 — beta_GB boundary OOM")
print(f"beta_GB     = {BETA_GB:.4e} GeV^-1")
print(f"Vol(M)      = {VOL_M:.4e} GeV^-1")
print(f"a4 coeff    = {A4:.4e} GeV")
print(f"Lambda_a4   = {LAMBDA_A4:.4e} GeV^4  (ratio to obs {LAMBDA_A4/LAMBDA_OBS:.2e})")
print(f"a4/Vol^2    = {lambda_vol2:.4e} GeV^4  (ratio {lambda_vol2/LAMBDA_OBS:.2e})")
print(f"M3 seam O(1)= {lambda_m3_heur:.4e} GeV^4  (ratio {lambda_m3_heur/LAMBDA_OBS:.2e})")
print()
print("M3 O(1) seam factor cannot close 10^83 gap; needs derived K_beta from boundary action.")
