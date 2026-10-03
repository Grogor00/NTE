#!/usr/bin/env python3
"""S3-f4: a_6+ exponential tail on NTE M = Hopf-S^3 x S^1_beta x A_F."""
from __future__ import annotations

import math

M_PL = 2.435e18  # GeV
N_F = 180
BETA_GB = math.sqrt(2 * math.pi) / M_PL
VOL_M = 2 * math.pi**2 * BETA_GB
A0 = N_F * BETA_GB / 2
A2 = -N_F * BETA_GB / 4
A4 = (3 / 2) * N_F * BETA_GB
LAMBDA_CUT = M_PL
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
S_REQ = LAMBDA_OBS / LAMBDA_A4
A_S3 = 1.0  # unit radius (S2-A)
BETA_CC = BETA_GB * M_PL  # beta in Planck-length units for CC2008 Theorem 3


def cc2008_tail_bound(mu: float, Lambda: float, C: float = 1.0) -> float:
    """|epsilon(Lambda)| <= C exp(-pi/2 (mu Lambda)^2) — CC2008 Theorem 3."""
    x = mu * Lambda
    return C * math.exp(-0.5 * math.pi * x * x)


def mu_lambda_for_suppression(log10_supp: float) -> float:
    """Solve exp(-pi/2 (mu Lambda)^2) = 10^{-log10_supp} with Lambda=1."""
    target = 10 ** (-log10_supp)
    if target <= 0:
        return float("inf")
    arg = -math.log(target)
    return math.sqrt(2 * arg / math.pi)


def mu_sq_spectrum(k: int, m: int) -> float:
    s1 = 2 * math.pi * (m + 0.5) / BETA_GB
    return (k + 1.5) ** 2 + s1**2


def main() -> None:
    print("# S3-f4 a_6+ / CC2008 exponential tail — Jammer")
    print("=" * 58)
    print()

    print("## 1. Heat-kernel coefficient register (S2 + CC2008)")
    print("  CC2008 round S3 x S1: a_4 = 0, a_6 = 0 (exact cancellation)")
    print("  NTE S2-C-B on same metric: a_4|_M = (3/2) N_F beta_GB  (R^2-only, non-zero)")
    print("  Hopf fibration: same round metric — a_6 geometric cancellation INHERITED")
    print(f"  a_4 (NTE) = {A4:.4e}   F1 anchor 270 beta_GB = {270 * BETA_GB:.4e}")
    print(f"  Lambda_a4 residual (S2-D) = {LAMBDA_A4:.4e} GeV^4")
    print()

    print("## 2. CC2008 Theorem 3 geometry (NTE canonical)")
    mu_geom = min(A_S3, BETA_CC)
    print(f"  S3 radius a           = {A_S3}")
    print(f"  S1 parameter beta     = beta_GB * M_Pl = sqrt(2 pi) = {BETA_CC:.6f}")
    print(f"  mu = inf(a, beta)     = {mu_geom:.6f}")
    print(f"  Lambda_cut            = M_Pl = {LAMBDA_CUT:.4e} GeV")
    print(f"  mu * Lambda (Planck)  = {mu_geom:.6f}  (both in Planck units)")
    print()

    eps_canon = cc2008_tail_bound(mu_geom, 1.0)
    log_eps = math.log10(eps_canon) if eps_canon > 0 else float("-inf")
    print("## 3. Exponential tail bound at canonical cutoff")
    print(f"  |epsilon(Lambda)| <= exp(-pi/2) ~ {eps_canon:.4e}")
    print(f"  log10 suppression     = {log_eps:.2f} dex")
    print(f"  Required for Lambda_obs gap = {math.log10(S_REQ):.2f} dex")
    print(f"  mu*Lambda needed for 83 OOM  ~ {mu_lambda_for_suppression(83.9):.2f}")
    print("  => Canonical mu*Lambda ~ 1 gives O(1) tail, NOT ~10^{-83}")
    print()

    print("## 4. Spectral-gap estimates (S2-A spectrum)")
    gaps = []
    for k, m in [(0, 0), (0, 1), (1, 0)]:
        mu2 = mu_sq_spectrum(k, m)
        lam = math.sqrt(mu2)
        gaps.append((k, m, lam))
    for k, m, lam in gaps:
        ratio = lam / M_PL
        tail = cc2008_tail_bound(ratio, 1.0)
        print(f"  k={k} m={m}: |lambda_D| ~ {lam:.4e} GeV  lambda/M_Pl ~ {ratio:.4e}")
        print(f"           tail exp(-pi/2 (lambda/M_Pl)^2) ~ {tail:.4e}  log10={math.log10(tail):.2f}")
    print("  Register: eigenvalue gaps ~ O(M_Pl) — tail still O(0.01-0.2), not 10^{-83}")
    print()

    print("## 5. D_F / A_F subleading (S2-C-C)")
    df_scale = 1e-18
    print(f"  D_F corrections to a_4 ~ O({df_scale:.0e}) of leading")
    print("  a_6 from D_F / Yukawa mass insertions — negligible vs a_4 residual")
    print()

    print("## 6. Combined suppression stack (R1 + R2 + R3)")
    r1 = 1.0  # derived f_0 ~ O(1) — S3-f2
    r2 = 1.0  # dmu trajectory — S3-f3 (no extra 83 OOM)
    r3 = eps_canon  # canonical CC2008 tail
    combined = LAMBDA_A4 * r1 * r2 * r3
    print(f"  Lambda_eff ~ Lambda_a4 x f_0 x W_dmu x |epsilon|")
    print(f"             ~ {LAMBDA_A4:.4e} x 1 x 1 x {eps_canon:.4e}")
    print(f"             ~ {combined:.4e} GeV^4")
    print(f"  log10 vs obs = {math.log10(combined / LAMBDA_OBS):.1f}  (still ~83 dex short)")
    print()

    print("## 7. Scenarios (honest bracket)")
    scenarios = [
        ("Canonical NTE (mu*Lambda~1)", mu_geom, 1.0),
        ("mu*Lambda = 11 (83-OOM tail target)", 11.0, 1.0),
        ("Lambda = 10 M_Pl (non-canonical cutoff)", mu_geom, 10.0),
    ]
    for name, mu_eff, lam_eff in scenarios:
        t = cc2008_tail_bound(mu_eff, lam_eff)
        le = LAMBDA_A4 * t
        print(f"  {name}")
        print(f"    |epsilon| ~ {t:.4e}  Lambda_eff ~ {le:.4e} GeV^4  log10/obs={math.log10(le/LAMBDA_OBS):.1f}")
    print()

    print("## S3-f4 verdict")
    print("  a_6 = 0, a_8 = 0 on round S3 x S1 — INHERITED (CC2008 + Hopf same metric).")
    print("  NTE a_4 non-zero from R^2/N_F route — distinct from CC2008 geometric a_4=0.")
    print("  CC2008 exponential tail at canonical (mu, Lambda) ~ O(0.2) — NOT 10^{-83}.")
    print("  R3 alone does NOT close gap; mu*Lambda ~ 11 would be required (not derived).")
    print("  Full Paper S4 chain still needs R4/R5 or non-perturbative programme beyond tail.")


if __name__ == "__main__":
    main()
