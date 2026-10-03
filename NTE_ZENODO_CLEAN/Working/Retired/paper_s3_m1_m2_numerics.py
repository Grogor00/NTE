#!/usr/bin/env python3
"""Paper S3 M1 (f4 moment) + M2 (Hopf holographic) suppression estimates."""
from __future__ import annotations

import math

M_PL = 2.435e18  # GeV
N_F = 180
BETA_GB = math.sqrt(2 * math.pi) / M_PL
VOL_M = 2 * math.pi**2 * BETA_GB
A0 = N_F * BETA_GB / 2

LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4  # GeV^4
LAMBDA_NAIVE = (45 / math.pi**2) * M_PL**4  # f4=1 naive per Vol(M) scaling
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))

# M1: required f4 suppression if ONLY moment tuning (honest: looks like fine-tuning)
F4_REQUIRED = LAMBDA_OBS / LAMBDA_NAIVE

# M2: Hopf S3->S2 — compare 3D boundary volume to 2D base area scale
# Unit Hopf: S3 radius r, S2 base area ~ pi (Hopf fibre S1)
# Holographic heuristic: Lambda density ~ (spectral a0) / (effective horizon area)
# Effective area ~ Vol(S3)^(2/3) ~ (2 pi^2 r^3)^(2/3) ~ r^2
# Vol(M) ~ r^3 with r ~ beta_GB => area_eff ~ beta_GB^(4/3)
R_EFF = VOL_M ** (2 / 3)
AREA_EFF = math.pi * R_EFF**2  # heuristic 2D scale from internal volume
# Compare to S2 unit sphere area 4pi
HOPF_AREA_RATIO = AREA_EFF / (4 * math.pi)
LAMBDA_M2_HEUR = LAMBDA_A4 * (4 * math.pi / AREA_EFF) ** 2  # double area suppression

print("# Paper S3 M1 + M2 suppression numerics")
print()
print("## Baseline (from paper_s3_lambda_nte_numerics.py)")
print(f"Lambda_obs     = {LAMBDA_OBS:.4e} GeV^4")
print(f"Lambda_naive   = {LAMBDA_NAIVE:.4e} GeV^4  (ratio {LAMBDA_NAIVE/LAMBDA_OBS:.2e})")
print(f"Lambda_a4 resid= {LAMBDA_A4:.4e} GeV^4  (ratio {LAMBDA_A4/LAMBDA_OBS:.2e})")
print()
print("## M1 — f4 moment (if leading term not unimodular-projected)")
print(f"f4 required ~ Lambda_obs/Lambda_naive = {F4_REQUIRED:.4e}")
print(f"log10(f4) ~ {math.log10(F4_REQUIRED):.2f}")
print("Reading: O(1) f4 fails; structural f4 from CC2008 exponential cutoff is candidate")
print("         but MUST be derived — not tuned to match Lambda_obs.")
print()
print("## M2 — Hopf holographic heuristic (S3 volume -> S2 area)")
print(f"Vol(M)       = {VOL_M:.4e} GeV^-1")
print(f"r_eff ~ Vol^(1/3) = {R_EFF:.4e} GeV^-1")
print(f"area_eff     = {AREA_EFF:.4e} GeV^-2")
print(f"Lambda_M2 est= {LAMBDA_M2_HEUR:.4e} GeV^4  (ratio {LAMBDA_M2_HEUR/LAMBDA_OBS:.2e})")
print()
print("## Combined gap (honest)")
print("Unimodular removes naive ~10^121; a4 leaves ~10^83.")
print("M1+M2 must supply ~10^83 further WITHOUT breaking kappa0, a4 structural anchors.")
print("Paper S3: derive f4 + holographic area law from spectral triple — not fit.")
