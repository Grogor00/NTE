#!/usr/bin/env python3
"""CR2 CR-H1: sanity check — F1 on S3 x S1 with R=6 (S2 §5.4 notation)."""

from math import pi, sqrt

# Unit 3-sphere: R = 6 (S2 convention, radius 1)
R = 6.0

# Weyl-squared and Euler integrand coefficients on constant-curvature 3-sphere
# S2 §5.4: C^2|_M = 12 - 24 + 12 = 0, E4|_M = 12 - 48 + 36 = 0
C2 = 12 - 24 + 12
E4 = 12 - 48 + 36

# F1 = -18 C^2 + 11 E4  (equivalent to 5R^2 - 8 R_munu^2 - 7 R_munu_rho_sigma^2)
F1_via_CE = -18 * C2 + 11 * E4

# Direct R-only check: coefficient of R^2 in F1 is (5 - 8/3 - 7/3) = 0
F1_R2_coeff = 5 - 8 / 3 - 7 / 3

N_F = 180
beta_GB = sqrt(2 * pi)  # placeholder scale; cancels in F1 test

# S2 §5.5 claimed a4 (proportional)
a4_claimed = 3 * N_F * beta_GB / 2

print("CR2 S2 a4 Gilkey check (CR-H1)")
print(f"  C^2 = {C2}")
print(f"  E4  = {E4}")
print(f"  F1 (via C,E basis) = {F1_via_CE}")
print(f"  F1 R^2 coefficient in standard combination = {F1_R2_coeff}")
print(f"  => integral of F1 over M should be 0 => a4 from §5.1 formula = 0")
print(f"  S2 §5.5 claims a4 coeff ~ 270*beta_GB = {a4_claimed / beta_GB:.0f} * beta_GB")
print("  STATUS: CONTRADICTION unless separate E=R/4 terms restore a4")
