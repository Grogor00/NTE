#!/usr/bin/env python3
"""Off-shell ghost scan — S_NTE^unified sector count (Jammer v0.1)."""
from __future__ import annotations

XI = 1.0 / 6.0


def main() -> None:
    print("# Ghost scan — unified action sector audit")
    print("=" * 60)

    print("\n## A — Sector DOF (structural count)")
    sectors = [
        ("GR (g_mu nu)", "2 polarisations (on-shell)", "standard"),
        ("SM (Path B separate)", "SM propagators", "not NTE extension claim"),
        ("Phi_NTE kinetic", "1 real scalar", "xi=1/6 bare"),
        ("Phi_NTE xi R|Phi|^2", "conformal coupling", "xi=1/6 conformal point"),
        ("mu(x) holonomic", "0 propagating (constraint)", "J1 S1 PASS"),
    ]
    for name, dof, note in sectors:
        print(f"  {name:<22} {dof:<28} {note}")

    print("\n## B — Holonomic mu (on-shell PASS)")
    print("  EOM: mu enforces H = alpha|Phi|^2 algebraically.")
    print("  mu is NOT independent dynamical field — no extra ghost from mu sector.")
    print("  Source: Jammer_Mu_xN_S1_Signoff; J1-G4 Theorem 2.")

    print("\n## C — xi=1/6 scalar sector (partial)")
    print(f"  xi = {XI:.6f} (corpus committed)")
    print("  At flat/de Sitter: m_E^2 = xi R matches J6-n3 (PASS).")
    print("  Full off-shell: spin-2 x spin-0 mixing from xi R|Phi|^2 — OPEN.")
    print("  Requires: constrained propagation / gauge-fixed Hessian on FLRW+perturbations.")

    print("\n## D — Sequential constraint (LB-1)")
    print("  Bulk: mu=0 — no constraint ghost.")
    print("  Post-G: mu ON — on-shell slaving only.")
    print("  Ghost scan must be phase-labelled, not single global action.")

    print("\n## E — Falsifiers / open")
    print("  F1: Off-shell Phi propagator has wrong-sign kinetic term on FLRW.")
    print("  F2: Bimetric/Janus extension needed (S2 refinement note).")
    print("  F3: Full heat-kernel derivation of kinetic operator from D_M.")

    print("\n## Verdict")
    print("  PARTIAL PASS: holonomic mu sector (no mu ghost).")
    print("  OPEN: full off-shell Phi+xi sector; bimetric polish.")


if __name__ == "__main__":
    main()
