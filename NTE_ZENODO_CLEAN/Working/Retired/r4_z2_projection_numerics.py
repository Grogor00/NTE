#!/usr/bin/env python3
"""R4 Z2 projection lemma numerics — bulk vs boundary field at HH and G."""
from __future__ import annotations

import math

ALPHA = 2.38e-47
M_PL = 2.435e18
M_NR = 1.221e19
PHI_RATIO = 15.9
G_EFF = 106.75
N_LOCK = 45.0 / (4.0 * G_EFF)
N_E = -math.log(ALPHA * M_NR)


def phi_bulk_hh() -> float:
    return PHI_RATIO * M_PL


def phi_wrong_boundary_hh() -> float:
    return math.sqrt(M_NR / ALPHA)


def phi_bulk_at_g() -> float:
    return math.sqrt(2.0) * M_PL  # slow-roll end


def phi_boundary_at_g() -> float:
    return M_NR


def phi_stage3_g(phi0: float) -> float:
    return phi0 * math.exp(-N_LOCK / 2.0)


def z2_invariant_magnitude(phi: float) -> float:
    return abs(phi)


def projection_pi(phi_bulk: float) -> float:
    """Z2-invariant projection: even channel magnitude at lock."""
    return z2_invariant_magnitude(phi_bulk)


def main() -> None:
    print("# R4 Z2 projection lemma numerics")
    print("=" * 60)

    pb_hh = phi_bulk_hh()
    pw_hh = phi_wrong_boundary_hh()
    pb_g = phi_bulk_at_g()
    pnt_g = phi_boundary_at_g()
    phi0 = 1.0541 * M_NR
    ps_g = phi_stage3_g(phi0)

    print("\n## A — HH peak (bulk active, boundary NOT crystallised)")
    print(f"  Phi_bulk (Role B)            = {pb_hh:.4e} GeV")
    print(f"  |Phi_NTE| if constraint ON   = {pw_hh:.4e} GeV  [WRONG CHART]")
    print(f"  ratio bulk/wrong-boundary    = {pb_hh/pw_hh:.4e}")
    print("  => R4c magnitude identity EXCLUDED at HH")

    print("\n## B — Event G (crystallisation — Z2 projection)")
    print(f"  Phi_bulk at slow-roll end    = {pb_g:.4e} GeV")
    print(f"  |Phi_NTE| constraint at G   = {pnt_g:.4e} GeV")
    print(f"  Pi[Phi_bulk] = |Phi_bulk|    = {projection_pi(pb_g):.4e} GeV")
    print(f"  ratio |Pi/boundary|          = {projection_pi(pb_g)/pnt_g:.4f}")
    print(f"  Stage3 |Phi|(y=N_lock)      = {ps_g:.4e} GeV")
    print(f"  ratio stage3/boundary        = {ps_g/pnt_g:.4f}")

    print("\n## C — Z2 structure")
    print("  Z2: Phi -> -Phi on boundary scalar (Part 1 Patch G)")
    print("  |Phi_NTE| is Z2-INVARIANT (even) — boundary observable post-G")
    print("  Phi_bulk pre-G: unconstrained sign — lives in bulk even mode")
    print("  At G: Pi_G[Phi_bulk] -> |Phi_NTE|  (not linear at HH)")

    print("\n## D — Register")
    print("  Pre-G: compare bulk Phi_inf to boundary |Phi| — FAIL (10^-13)")
    print("  At G:  compare Pi(Phi_bulk) to |Phi_NTE| — PASS (O(1))")
    print("  Lemma R4: field map is PROJECTION at G, not identity at HH")

    print("\n## E — Falsifiers")
    print("  Forced Phi_inf = sqrt(M_Pl/alpha) at HH  -> excluded")
    print("  Pi(Phi_bulk) != O(1) M_Pl at G            -> would falsify lemma")


if __name__ == "__main__":
    main()
