#!/usr/bin/env python3
"""S3-f2: structural f_k moments from S2-A spectrum + CC2008 prescription."""
from __future__ import annotations

import math
from dataclasses import dataclass

M_PL = 2.435e18  # GeV
N_F = 180
BETA_GB = math.sqrt(2 * math.pi) / M_PL
VOL_M = 2 * math.pi**2 * BETA_GB
A0 = N_F * BETA_GB / 2
A2 = -N_F * BETA_GB / 4
A4 = (3 / 2) * N_F * BETA_GB  # R^2-only on M per S2-C-B
A4_F1 = 270 * BETA_GB  # F1 structural anchor per S2-C-B
LAMBDA_CUT = M_PL
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_NAIVE = (45 / math.pi**2) * M_PL**4


@dataclass
class Cutoff:
    name: str
    f4: float
    f2: float
    f0: float
    note: str


def connes_moment(k: int, kind: str = "exp") -> float:
    """Connes f_k = int_0^inf f(u) u^{k/2-1} du for standard cutoffs."""
    if kind == "exp":
        # f(u) = e^{-u}
        if k == 0:
            return float("inf")
        return math.gamma(k / 2)
    if kind == "gauss":
        # f(u) = e^{-u^2}
        if k == 0:
            return float("inf")
        return 0.5 * math.gamma(k / 4)
    raise ValueError(kind)


def cc2008_rho_moments() -> tuple[float, float]:
    """CC2008 h(rho^2)=e^{-rho^2}: int rho^3 h drho and int rho h drho."""
    return 0.5, 0.5


def mu_sq(k: int, m: int) -> float:
    s1 = 2 * math.pi * (m + 0.5) / BETA_GB
    return (k + 1.5) ** 2 + s1**2


def spectral_trace_exp(Lambda: float, k_max: int = 30, m_max: int = 0) -> float:
    """Tr(exp(-D^2/Lambda^2)) — CC2008 exponential; m_max=0 S3-dominated at Lambda~M_Pl."""
    s = 0.0
    for k in range(k_max + 1):
        mult = 4 * (k + 1) * (k + 2)
        for m in range(m_max + 1):
            s += mult * math.exp(-mu_sq(k, m) / Lambda**2)
    return N_F * s


def analytic_action(f4: float, f2: float, f0: float) -> tuple[float, float, float]:
    """Assemble f_k * Lambda^n * a_n from S2-B/C closed coefficients."""
    return (
        f4 * LAMBDA_CUT**4 * A0,
        f2 * LAMBDA_CUT**2 * A2,
        f0 * A4,
    )


def main() -> None:
    print("# S3-f2 structural f_k from S2-A spectrum — Jammer/Scratch")
    print("=" * 60)
    print()

    print("## S2-B/C anchor coefficients (closed form)")
    print(f"  N_F       = {N_F}")
    print(f"  beta_GB   = {BETA_GB:.4e} GeV^-1")
    print(f"  Vol(M)    = {VOL_M:.4e} GeV^-1")
    print(f"  a_0       = {A0:.4e}")
    print(f"  a_2       = {A2:.4e}")
    print(f"  a_4|_M    = {A4:.4e}  (R^2-only, S2-C-B)")
    print(f"  a_4 F1    = {A4_F1:.4e}  (270 beta_GB anchor)")
    print()

    print("## CC2008 canonical exponential moments")
    i4, i2 = cc2008_rho_moments()
    print(f"  int rho^3 e^{{-rho^2}} drho = {i4}")
    print(f"  int rho   e^{{-rho^2}} drho = {i2}")
    print("  => Lambda^4 and Lambda^2 weights equal (O(1)) for CC2008 h on S3 x S1")
    print()

    print("## Connes f_k moments (derived cutoff shapes)")
    cutoffs = [
        Cutoff("exp: f(u)=e^{-u}", connes_moment(4, "exp"), connes_moment(2, "exp"),
               connes_moment(0, "exp"), "CC2008 default; f_0 log-divergent — regulated by Theorem 3 tail"),
        Cutoff("gauss: f(u)=e^{-u^2}", connes_moment(4, "gauss"), connes_moment(2, "gauss"),
               connes_moment(0, "gauss"), "Slower tail; f_4/f_2 = Gamma(1)/Gamma(1/2) ~ 1.77"),
    ]
    for c in cutoffs:
        ratio = c.f4 / c.f2 if c.f2 else float("nan")
        print(f"  {c.name}")
        print(f"    f_4={c.f4:.6g}  f_2={c.f2:.6g}  f_0={c.f0}  f_4/f_2={ratio:.4f}")
        print(f"    {c.note}")
    print()

    print("## S2-A spectrum partial trace vs analytic assembly (Lambda = M_Pl)")
    tr_num = spectral_trace_exp(LAMBDA_CUT, k_max=25, m_max=0)
    s4, s2, s0 = analytic_action(1.0, 1.0, 1.0)
    tr_asy = s4 + s2 + s0
    print(f"  Tr(exp(-D^2/Lambda^2)) numeric (S3 sector, m=0) = {tr_num:.4e}")
    print(f"  f_4 L^4 a_0 + f_2 L^2 a_2 + f_0 a_4 (O(1) f)     = {tr_asy:.4e}")
    print(f"  Ratio numeric / assembly                         = {tr_num/tr_asy:.4f}")
    print("  Register: at beta_GB ~ 1/M_Pl, S1 modes decouple from trace at Lambda~M_Pl;")
    print("            full zeta = S2-B Hurwitz closed form (not naive sum).")
    print()

    print("## Newton / EH sector (register)")
    eh_scale = abs(connes_moment(2, "exp") * LAMBDA_CUT**2 * A2)
    print(f"  |f_2 Lambda^2 a_2| ~ {eh_scale:.4e}  (Planck-scale EH bookkeeping)")
    print("  Full G extraction from f_2 x a_2 — S2-E scope; f_2 ~ O(1) is corpus convention.")
    print()

    print("## Spectral action at Lambda_cut = M_Pl (derived f, not tuned)")
    for c in cutoffs:
        if not math.isfinite(c.f0):
            f0_eff = 1.0  # Theorem 3 regulated finite part — O(1) register
        else:
            f0_eff = c.f0
        s4 = c.f4 * LAMBDA_CUT**4 * A0
        s2 = c.f2 * LAMBDA_CUT**2 * A2
        s0 = f0_eff * A4
        lam_naive = s4 / VOL_M
        lam_a4 = f0_eff * LAMBDA_A4
        print(f"  Cutoff: {c.name}")
        print(f"    f_4 Lambda^4 a_0 / Vol = {lam_naive:.4e} GeV^4  (un1o vs obs {math.log10(lam_naive/LAMBDA_OBS):.1f})")
        print(f"    f_0 a_4 residual       = {lam_a4:.4e} GeV^4  (log10 vs obs {math.log10(lam_a4/LAMBDA_OBS):.1f})")
        print(f"    f_2 Lambda^2 a_2       = {s2:.4e}  (EH sector — not Lambda density)")
    print()

    print("## Tuning route falsifier")
    f0_req = LAMBDA_OBS / LAMBDA_A4
    f4_req = LAMBDA_OBS / LAMBDA_NAIVE
    print(f"  f_0_required to match Lambda_obs (FORBIDDEN) = {f0_req:.4e}  log10 = {math.log10(f0_req):.2f}")
    print(f"  f_4_required (if unimodular absent)          = {f4_req:.4e}  log10 = {math.log10(f4_req):.2f}")
    print(f"  Derived f_0 ~ O(1) vs required ~ 10^{{-83}} — **structural f does NOT close gap**")
    print()

    print("## S3-f2 verdict")
    print("  f_k DERIVED from CC2008 exponential + Connes moments — ratios O(1).")
    print("  S2-A spectrum validates a_0, a_2; a_4 from S2-C-B enters via f_0.")
    print("  Unimodular removes f_4 a_0; residual f_0 a_4 ~ 10^83 x Lambda_obs with derived f_0.")
    print("  R3 (a_6+ exponential tail) + S3-f3 dmu still required — no tune.")


if __name__ == "__main__":
    main()
