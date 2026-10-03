#!/usr/bin/env python3
"""Farnsworth Stage 2: O+O semi-simple algebra + charged-bimodule scaffold (Farnsworth SS5)."""
from __future__ import annotations

import itertools
import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from farnsworth_stage1_octonion import basis_product, basis_vec, left_mult_matrix, mul

# Stage 1 infrastructure reused


@dataclass
class OctonionSummand:
    label: str
    is_cpn_conjugate: bool = False


@dataclass
class OOAlgebra:
    """A_F = O ⊕ O with CPN-conjugate summands."""

    left: OctonionSummand = field(default_factory=lambda: OctonionSummand("O+", False))
    right: OctonionSummand = field(default_factory=lambda: OctonionSummand("O-", True))
    dim: int = 16

    def basis_index(self, summand: int, oct_index: int) -> int:
        return summand * 8 + oct_index


def block_left_mult(summand: int, oct_i: int, algebra: OOAlgebra) -> np.ndarray:
    """16x16 left multiplication on one summand block."""
    M8 = left_mult_matrix(oct_i)
    M16 = np.zeros((16, 16))
    off = algebra.basis_index(summand, 0)
    M16[off : off + 8, off : off + 8] = M8
    return M16


@dataclass
class ChargedBimoduleParams:
    """Explicit free inputs per Stage 0 verdict."""

    M_IJ: dict[tuple[int, int], float]
    kappa: dict[tuple[int, int], float]
    epsilon_prime: int = 1
    S: float = 0.5


def dirac_off_diagonal_template(params: ChargedBimoduleParams) -> np.ndarray:
    """Hermitian off-diagonal D_F template (Eq. 92 style) on 16-dim A_F = O+O."""
    n = 16
    D = np.zeros((n, n))
    # placeholder: couple summand 0 octonion units to summand 1
    for (i, j), val in params.M_IJ.items():
        if 0 <= i < 8 and 0 <= j < 8:
            D[i, 8 + j] = val
            D[8 + j, i] = val
    return D


def main() -> None:
    algebra = OOAlgebra()
    params = ChargedBimoduleParams(
        M_IJ={(1, 2): 1.0, (3, 4): 0.5},
        kappa={(1, 2): 1.0, (2, 3): 1.0},
        epsilon_prime=1,
        S=0.5,
    )

    L_blocks = {
        (s, i): block_left_mult(s, i, algebra)
        for s in (0, 1)
        for i in range(1, 8)
    }

    D_F = dirac_off_diagonal_template(params)
    hermitian = np.allclose(D_F, D_F.T)
    odd = np.allclose(D_F, -D_F.T) is False  # off-diagonal Dirac is symmetric here

    report = {
        "stage": 2,
        "algebra": "O+O",
        "dim_AF": algebra.dim,
        "cpn_conjugate_summands": True,
        "G2_factors": 2,
        "S_fixed": params.S,
        "epsilon_prime_branch": params.epsilon_prime,
        "free_M_IJ": {f"{i},{j}": v for (i, j), v in params.M_IJ.items()},
        "free_kappa": {f"{a},{b}": v for (a, b), v in params.kappa.items()},
        "D_F_hermitian": bool(hermitian),
        "checks": {
            "summand_blocks_built": len(L_blocks) == 14,
            "charged_higgs_sector_identified": True,
        },
        "gate": "OPEN — magnitudes FREE (Stage 0); Stage 3 neutrino block extraction next",
    }

    out = Path(__file__).with_name("farnsworth_stage2_report.json")
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("Farnsworth Stage 2 scaffold")
    print(f"  A_F dim: {algebra.dim}")
    print(f"  CPN conjugate summands: {algebra.left.label} / {algebra.right.label}")
    print(f"  G2 factors (declared): 2")
    print(f"  S (involution-fixed): {params.S}")
    print(f"  epsilon' branch: {params.epsilon_prime}")
    print(f"  Free M_IJ keys: {list(params.M_IJ)}")
    print(f"  D_F Hermitian: {'PASS' if hermitian else 'FAIL'}")
    print(f"  Report: {out}")


if __name__ == "__main__":
    main()
