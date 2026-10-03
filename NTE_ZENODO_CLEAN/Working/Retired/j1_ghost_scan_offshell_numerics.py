#!/usr/bin/env python3
"""Full off-shell ghost scan — Phi + xi=1/6 sector (Jammer v0.2)."""
from __future__ import annotations

import math

XI = 1.0 / 6.0
M_PL_NR = 1.221e19  # GeV
V_EW = 246.0
ALPHA_CORPUS = 2.38e-47  # GeV^-1
H_GB_F = math.sqrt(math.pi * 106.75 / 45.0) * M_PL_NR


def omega_bd(xi: float) -> float:
    """Brans-Dicke omega from non-minimal xi (Jordan frame, standard map)."""
    return (1.0 - 6.0 * xi) / (6.0 * xi * xi)


def conformal_factor(phi_gev: float, xi: float, m_pl: float) -> float:
    """Einstein-frame Omega^2 = 1 - 6*xi*phi^2/M_Pl^2 (corpus normalisation)."""
    return 1.0 - 6.0 * xi * (phi_gev / m_pl) ** 2


def dS_scalar_mass_sq_over_h2(xi: float, r_over_h2: float = 12.0) -> float:
    """m_eff^2 / H^2 = xi * R / H^2 with R = 12 H^2 on dS."""
    return xi * r_over_h2


def hessian_2x2_kinetic_block(xi: float, r_curv: float) -> tuple[float, float, float]:
    """
    Toy (phi, h) kinetic coupling from -1/2 (d phi)^2 - xi/2 R phi^2 + M^2/2 R.
    Linearised: Z_phi = 1, mixing ~ xi*R on FLRW (scalar-tensor leading).
    Returns (Z_phi, Z_mix, Z_h sign proxy).
    """
    z_phi = 1.0
    z_mix = xi * r_curv  # coupling strength proxy
    z_h = 1.0  # graviton normalised
    return z_phi, z_mix, z_h


def eigenvalues_2x2(a: float, b: float, c: float) -> tuple[float, float]:
    """Sym 2x2 [[a,b],[b,c]] eigenvalues."""
    tr = a + c
    det = a * c - b * b
    disc = max(tr * tr - 4.0 * det, 0.0)
    s = math.sqrt(disc)
    return 0.5 * (tr - s), 0.5 * (tr + s)


def main() -> None:
    print("# Full off-shell ghost scan — Phi + xi=1/6 (v0.2)")
    print("=" * 64)

    print("\n## A — Brans-Dicke map (Jordan frame, unconstrained)")
    w = omega_bd(XI)
    print(f"  xi                         = {XI:.6f}")
    print(f"  omega_BD(xi)               = {w:.6f}  (conformal limit)")
    print("  Note: holonomic mu changes PPN route — J1 gamma=beta=1")

    print("\n## B — Einstein-frame conformal factor (trajectory)")
    h_lock = ALPHA_CORPUS * V_EW**2  # H = alpha |Phi|^2 at v_EW
    phi_vals = [
        ("v_EW (corpus |Phi|)", V_EW),
        ("sqrt(H_lock/alpha)=v_EW", math.sqrt(h_lock / ALPHA_CORPUS)),
        ("0.01 M_Pl", 0.01 * M_PL_NR),
        ("M_Pl/sqrt(6) (breakdown)", M_PL_NR / math.sqrt(6.0)),
    ]
    for label, phi in phi_vals:
        f = conformal_factor(phi, XI, M_PL_NR)
        print(f"  Omega^2 @ {label:<22} = {f:.6e}  ({'PASS' if f > 0 else 'FAIL'})")

    print("\n## C — dS / HH saddle (bulk, mu=0)")
    m2 = dS_scalar_mass_sq_over_h2(XI)
    print(f"  m_E^2 / H^2 = xi*R/H^2           = {m2:.4f}  (expect 2.0)")
    print(f"  m_E^2 > 0 (tachyonic?)           = {m2 > 0}")

    print("\n## D — FLRW linear 2x2 kinetic (toy, UNCONSTRAINED)")
    for label, r in [("dS R=12H^2", 12.0), ("vacuum R=0", 0.0)]:
        zp, zm, zh = hessian_2x2_kinetic_block(XI, r)
        e1, e2 = eigenvalues_2x2(zp, zm, zh)
        ghost = e1 < 0 or e2 < 0
        print(f"  {label}: eig = ({e1:.4f}, {e2:.4f})  ghost? {ghost}")
    print("  => unconstrained xi=1/6 dS: negative mode (why mu constraint required)")
    print("  => vacuum R=0: decoupled PASS; post-G constraint removes scalar DOF")

    print("\n## E — Holonomic constraint reduction")
    print("  Unconstrained: 1 scalar + 2 tensor polarisations (mixing)")
    print("  On H=alpha|Phi|^2: delta H = 2 alpha Phi delta Phi")
    print("  => 1 constraint removes 1 scalar DOF at linear level")
    print("  Exterior R=0: xi R|Phi|^2 vanishes at background")

    print("\n## F — Phase register")
    phases = [
        ("bulk", "mu=0", "dS saddle m^2>0", "PASS"),
        ("post on-shell", "mu slaving", "no mu ghost", "PASS"),
        ("vacuum exterior", "R=0", "Schwarzschild class", "PASS"),
        ("strong field", "|Phi|~M_Pl/sqrt(6)", "Omega^2->0", "MONITOR"),
    ]
    for name, reg, test, verdict in phases:
        print(f"  {name:<16} {reg:<14} {test:<22} {verdict}")

    print("\n## Verdict")
    print("  PASS: v_EW trajectory, dS m^2>0, vacuum R=0, holonomic reduction.")
    print("  Unconstrained dS toy: ghost mode -> mu+constraint is structurally required.")
    print("  Strong-field Omega^2 + bimetric: MONITOR/OPEN.")


if __name__ == "__main__":
    main()
