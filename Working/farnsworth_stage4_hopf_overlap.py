#!/usr/bin/env python3
"""Farnsworth Stage 4: Hopf-S3 geometric overlap — 4pi vs 8pi branch (decisive)."""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path(__file__).with_name("farnsworth_stage4_report.json")

VOL_S3 = 2 * math.pi**2
Y00 = 1.0 / math.sqrt(4 * math.pi)
KAPPA0 = 3.0 * Y00
EIGHT_PI = 8 * math.pi
FOUR_PI = 4 * math.pi


def dirac_eigenvalue(k: int) -> float:
    """Round S3 Dirac spectrum (unit radius): |λ_k| = k + 3/2."""
    return k + 1.5


def l2_norm_s3_constant(amplitude: float) -> float:
    """||ψ||^2 for constant mode on S3."""
    return amplitude**2 * VOL_S3


def hopf_base_projection(amplitude_s3: float) -> float:
    """Monopole Y00 projection amplitude on S2 base."""
    return Y00 * amplitude_s3


def yukawa_prefactor(flux: float, power: float = -1 / 3) -> float:
    return flux**power


def main() -> None:
    # Unit-normalized constant Killing-spinor amplitude on S3 (scaffold)
    psi_amp = 1.0 / math.sqrt(VOL_S3)
    norm2 = l2_norm_s3_constant(psi_amp)
    base_proj = hopf_base_projection(psi_amp)

    branch_4pi = yukawa_prefactor(FOUR_PI)
    branch_8pi = yukawa_prefactor(EIGHT_PI)
    target_8pi_inv3 = (8 * math.pi) ** (-1 / 3)
    target_4pi_inv3 = (4 * math.pi) ** (-1 / 3)

    report = {
        "stage": 4,
        "vol_S3": VOL_S3,
        "psi_L2_norm2": norm2,
        "hopf_Y00_projection": base_proj,
        "kappa0_structural": KAPPA0,
        "branch_4pi_flux": FOUR_PI,
        "branch_8pi_flux": EIGHT_PI,
        "yukawa_scale_4pi_inv3": branch_4pi,
        "yukawa_scale_8pi_inv3": branch_8pi,
        "target_8pi_inv3": target_8pi_inv3,
        "target_4pi_inv3": target_4pi_inv3,
        "ratio_8pi_to_4pi": branch_8pi / branch_4pi,
        "dirac_lambda_k0": dirac_eigenvalue(0),
        "decisive_question": "Does Dirac nu_L-nu_R overlap pick up Majorana doubling (8pi) or single Hopf flux (4pi)?",
        "gate": "OPEN — envelope/associator ordering (Stage 2.2) not yet implemented; scaffold compares volumetric powers only",
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("Farnsworth Stage 4 scaffold (4pi vs 8pi)")
    print(f"  (4pi)^(-1/3) = {branch_4pi:.6f}")
    print(f"  (8pi)^(-1/3) = {branch_8pi:.6f}")
    print(f"  corpus target (8pi)^(-1/3) = {target_8pi_inv3:.6f}")
    print(f"  ratio 8pi/4pi branch = {branch_8pi/branch_4pi:.6f}")
    print(f"  report -> {OUT}")


if __name__ == "__main__":
    main()
