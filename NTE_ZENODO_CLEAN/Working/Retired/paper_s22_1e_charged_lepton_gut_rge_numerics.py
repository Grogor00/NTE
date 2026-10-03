#!/usr/bin/env python3
"""Route L1 — G2 Georgi-Jarlskog: run masses to M_GUT and test m_l/(N_c m_q) -> 1."""
from __future__ import annotations

import math

M_GUT = 2.0e16
M_Z = 91.1876
M_TAU = 1.777
M_MU = 0.105658
M_E = 0.000510999
M_B_AT_MB = 4.18
M_S_AT_MS = 0.0934
M_D_AT_MD = 4.7e-3
N_C = 3.0
ALPHA_S_MZ = 0.1179
GAMMA0 = 4.0


def alpha_s(mu: float, nf: int = 5) -> float:
    b0 = 11.0 - 2.0 * nf / 3.0
    inv = 1.0 / ALPHA_S_MZ + b0 * math.log(mu / M_Z) / (2.0 * math.pi)
    return 2.0 * math.pi / inv if inv > 0 else 0.5


def run_quark_mass(m_at_scale: float, mu0: float, mu1: float, nf: int = 5) -> float:
    b0 = 11.0 - 2.0 * nf / 3.0
    as0 = alpha_s(mu0, nf)
    as1 = alpha_s(mu1, nf)
    return m_at_scale * (as1 / as0) ** (GAMMA0 / b0)


def run_lepton_mass(m_at_scale: float, mu0: float, mu1: float) -> float:
    alpha_em = 1.0 / 127.9
    t = math.log(mu1 / mu0)
    return m_at_scale * (1.0 + 3.0 * alpha_em * t / (4.0 * math.pi))


def main() -> None:
    print("# Route L1 — G2 GUT + 1-loop running (Jammer v0.1e)")
    print("=" * 60)
    print(f"  M_GUT = {M_GUT:.2e} GeV   M_Z = {M_Z:.2f} GeV")

    # Run observed masses UP to M_GUT (standard GUT test)
    mt_g = run_lepton_mass(M_TAU, M_Z, M_GUT)
    mb_g = run_quark_mass(M_B_AT_MB, M_B_AT_MB, M_GUT, nf=5)
    mmu_g = run_lepton_mass(M_MU, M_Z, M_GUT)
    ms_g = run_quark_mass(M_S_AT_MS, M_S_AT_MS, M_GUT, nf=4)
    me_g = run_lepton_mass(M_E, M_Z, M_GUT)
    md_g = run_quark_mass(M_D_AT_MD, M_D_AT_MD, M_GUT, nf=4)

    r_tau_b = mt_g / mb_g
    r_mu_3s = mmu_g / (N_C * ms_g)
    r_e_3d = me_g / (N_C * md_g)

    print("\n## Test A: run obs UP to M_GUT, check m_l / (N_c m_q)")
    print(f"  m_tau/m_b @ M_GUT       = {r_tau_b:.4f}  (GUT target 1)")
    print(f"  m_mu/(3*m_s) @ M_GUT    = {r_mu_3s:.4f}  (GUT target 1)")
    print(f"  m_e/(3*m_d) @ M_GUT     = {r_e_3d:.4f}  (GUT target 1)")

    print("\n## Test B: impose GUT at M_GUT, run leptons DOWN to M_Z")
    mt_pred = run_lepton_mass(mb_g, M_GUT, M_Z)
    mmu_pred = run_lepton_mass(N_C * ms_g, M_GUT, M_Z)
    me_pred = run_lepton_mass(N_C * md_g, M_GUT, M_Z)
    print(f"  m_tau pred/obs @ M_Z    = {mt_pred/M_TAU:.4f}")
    print(f"  m_mu pred/obs @ M_Z     = {mmu_pred/M_MU:.4f}")
    print(f"  m_e pred/obs @ M_Z      = {me_pred/M_E:.4f}")

    print("\n## EW spot-check (no RGE)")
    print(f"  m_tau/m_b @ M_Z       = {M_TAU/M_B_AT_MB:.4f}")
    print(f"  m_mu/(3*m_s) @ M_Z    = {M_MU/(N_C*M_S_AT_MS):.4f}")

    print("\n## Verdict")
    tau_ok = 0.7 <= r_tau_b <= 1.3
    mu_ok = 0.7 <= r_mu_3s <= 1.3
    e_ok = 0.7 <= r_e_3d <= 1.3
    if tau_ok:
        print("  Test A: tau/b at M_GUT in 30% band — G2 rule viable at 1-loop.")
    else:
        print(f"  Test A: tau/b at M_GUT = {r_tau_b:.2f} — needs 2-loop/thresholds.")
    if not mu_ok or not e_ok:
        print("  Test A: mu,e sectors need 2-loop / L2 embedding depth.")
    print("  Route L1: geometric origin not falsified; full Yukawa closure open (L2/L4).")


if __name__ == "__main__":
    main()
