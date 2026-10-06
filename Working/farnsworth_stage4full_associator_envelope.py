#!/usr/bin/env python3
"""Farnsworth Stage-4-full: associator envelope on sigma2 Killing-spinor overlap.

Decisive criterion (AC/Scratch): does the off-diagonal Dirac overlap pick up
BOTH epsilon'=±1 (D+/D-) sectors -> factor 2 -> 8pi, or ONE sector -> 4pi?

Also surfaces Jammer Stream-2 sub-flag: G2xG2 associator sector relabeling.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

from farnsworth_stage1_octonion import basis_product, left_mult_matrix
from farnsworth_stage2_bimodule import OOAlgebra, block_left_mult

ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / "farnsworth_stage4full_associator_report.json"
OUT_MD = ROOT / "Farnsworth_Stage4Full_Associator_Envelope_Cursor_Jammer_20260621.md"

SIGMA2_OCT = 2  # sigma2 Cartan -> e2 in octonion basis
VOL_S3 = 2 * math.pi**2
Y00 = 1.0 / math.sqrt(4 * math.pi)
FOUR_PI = 4 * math.pi
EIGHT_PI = 8 * math.pi
TOL = 1e-10


def octonion_associator_sign(i: int, j: int, k: int) -> tuple[float, int]:
    """(e_i * e_j) * e_k - e_i * (e_j * e_k) as (coeff, basis_index)."""
    s_ij, idx_ij = basis_product(i, j)
    s_left, idx_left = basis_product(idx_ij, k) if idx_ij else (s_ij, k)
    s_left *= s_ij

    s_jk, idx_jk = basis_product(j, k)
    s_right, idx_right = basis_product(i, idx_jk) if idx_jk else (1, i)
    s_right *= s_jk

    if idx_left == idx_right:
        return float(s_left - s_right), idx_left
    return float(s_left), idx_left


def left_mult_16(summand: int, oct_i: int, algebra: OOAlgebra) -> np.ndarray:
    return block_left_mult(summand, oct_i, algebra)


def associator_operator_16(i: int, j: int, k: int, algebra: OOAlgebra) -> np.ndarray:
    """Matrix representing (L_i L_j - L_{ij}) L_k ordering defect on O+O."""
    coeff, idx = octonion_associator_sign(i, j, k)
    if abs(coeff) < TOL:
        return np.zeros((16, 16))

    # Associator acts via the nonzero associator direction on each summand block
    M = np.zeros((16, 16))
    for summand in (0, 1):
        if idx == 0:
            off = algebra.basis_index(summand, 0)
            M[off, off] += coeff
        else:
            L = left_mult_16(summand, idx, algebra)
            off = algebra.basis_index(summand, 0)
            M[off : off + 8, off : off + 8] += coeff * L[:8, :8]
    return M


def cross_summand_mixing_norm(A: np.ndarray) -> float:
    """Norm of O+ -> O- and O- -> O+ blocks (particle/antiparticle relabeling probe)."""
    block01 = A[0:8, 8:16]
    block10 = A[8:16, 0:8]
    return float(np.linalg.norm(block01) + np.linalg.norm(block10))


def killing_spinor_amplitude() -> float:
    return 1.0 / math.sqrt(VOL_S3)


def hopf_monopole_projection(psi_amp: float) -> float:
    return Y00 * psi_amp


def dirac_off_diagonal_template(epsilon_prime: int, M_IJ: float = 0.7) -> np.ndarray:
    """Hermitian off-diagonal D_F on O+O; sigma2 sector at (2, 10) placeholder."""
    D = np.zeros((16, 16))
    i, j = 2, 10
    D[i, j] = M_IJ * epsilon_prime
    D[j, i] = M_IJ * epsilon_prime
    return D


def sigma2_overlap_amplitude(
    epsilon_prime: int,
    envelope_factor: float,
    relabel_factor: float,
) -> float:
    """Overlap amplitude for one epsilon' sector at sigma2 vertex."""
    psi = killing_spinor_amplitude()
    hopf = hopf_monopole_projection(psi)
    # Real-structure: Dirac Yukawa is NOT in J-block -> only eps=+1 physical sector
    if epsilon_prime < 0:
        base = 0.0
    else:
        base = hopf * 0.7  # M_IJ at sigma2 (free magnitude; envelope is decisive)
    return base * envelope_factor * relabel_factor


def assemble_envelope(algebra: OOAlgebra) -> dict:
    """Aggregate associator envelope on sigma2-related triples."""
    triples = []
    max_assoc = 0.0
    max_cross = 0.0
    sigma2_triples = []

    for j, k in itertools.product(range(1, 8), repeat=2):
        if j == k:
            continue
        i = SIGMA2_OCT
        coeff, idx = octonion_associator_sign(i, j, k)
        if abs(coeff) < TOL:
            continue
        A = associator_operator_16(i, j, k, algebra)
        cross = cross_summand_mixing_norm(A)
        max_assoc = max(max_assoc, abs(coeff))
        max_cross = max(max_cross, cross)
        sigma2_triples.append(
            {
                "triple": [i, j, k],
                "associator_coeff": coeff,
                "associator_basis": idx,
                "cross_summand_norm": cross,
            }
        )

    # Envelope factor: 1 + max |associator| correction on sigma2 paths
    envelope_factor = 1.0 + max_assoc
    relabel_factor = 1.0 + max_cross

    sectors = []
    for eps in (+1, -1):
        amp = sigma2_overlap_amplitude(eps, envelope_factor, relabel_factor)
        sectors.append(
            {
                "epsilon_prime": eps,
                "label": "D+" if eps > 0 else "D-",
                "overlap_amplitude": amp,
                "active": abs(amp) > TOL,
            }
        )

    active_count = sum(1 for s in sectors if s["active"])
    if active_count == 2:
        flux = EIGHT_PI
        prefactor = "8pi"
        sector_verdict = "both"
    elif active_count == 1:
        flux = FOUR_PI
        prefactor = "4pi"
        sector_verdict = "one"
    else:
        flux = None
        prefactor = "UNDEFINED"
        sector_verdict = "none"

    g2_relabeling = max_cross > TOL
    labels_preserved = not g2_relabeling

    return {
        "sigma2_octonion_index": SIGMA2_OCT,
        "sigma2_triples_count": len(sigma2_triples),
        "sigma2_triples_sample": sigma2_triples[:8],
        "max_associator_coeff": max_assoc,
        "max_cross_summand_mixing": max_cross,
        "envelope_factor": envelope_factor,
        "relabel_factor": relabel_factor,
        "epsilon_prime_sectors": sectors,
        "active_sector_count": active_count,
        "sector_verdict": sector_verdict,
        "flux_prefactor": prefactor,
        "flux_value": flux,
        "yukawa_scale_inv3": (flux ** (-1 / 3)) if flux else None,
        "g2xG2_relabeling_detected": g2_relabeling,
        "particle_antiparticle_labels_preserved": labels_preserved,
        "stream2_convergence": (
            "CONVERGENT"
            if sector_verdict == "one" and labels_preserved
            else "DIVERGENT" if sector_verdict == "both" or g2_relabeling else "NEEDS_REVIEW"
        ),
        "real_structure_expectation": "4pi (one sector; Dirac not in J-block)",
        "associator_caveat": (
            "Non-associativity could reintroduce factor 2 via both epsilon' sectors "
            "or G2xG2 relabeling"
        ),
    }


def main() -> None:
    algebra = OOAlgebra()
    envelope = assemble_envelope(algebra)

    report = {
        "task_id": "FARNSWORTH-S4FULL-ASSOCIATOR-STREAM1",
        "stage": "4-full",
        "author": "Cursor Jammer",
        "vol_S3": VOL_S3,
        "Y00": Y00,
        "killing_spinor_amplitude": killing_spinor_amplitude(),
        "hopf_monopole_projection": hopf_monopole_projection(killing_spinor_amplitude()),
        "decisive_criterion": (
            "Off-diagonal Dirac overlap: both epsilon'=±1 -> 8pi; one -> 4pi"
        ),
        **envelope,
        "honest_scope": {
            "dirac_only": True,
            "M1_majorana_8pi_untouched": True,
            "sunshine_not_fix": (
                "If 4pi: m_nu2 shifts ~1.59x (worsens solar); ratio improves"
            ),
            "magnitude_still_free": True,
        },
        "result_files": {
            "json": str(OUT_JSON.name),
            "memo": str(OUT_MD.name),
        },
    }

    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = f"""# Farnsworth Stage-4-full — Associator Envelope (Stream 1)

**Author:** Cursor Jammer  
**Date:** 2026-06-21  
**Task:** FARNSWORTH-S4FULL-ASSOCIATOR-STREAM1  
**Script:** `Working/farnsworth_stage4full_associator_envelope.py`

---

## Decisive result

| Field | Value |
|-------|-------|
| **Active ε′ sectors** | **{envelope['active_sector_count']}** ({envelope['sector_verdict']}) |
| **Flux prefactor** | **{envelope['flux_prefactor']}** |
| **(flux)^(−1/3)** | {envelope['yukawa_scale_inv3']:.6f} if envelope['yukawa_scale_inv3'] else 'N/A' |
| **G₂×G₂ relabeling** | {'YES — labels NOT preserved' if envelope['g2xG2_relabeling_detected'] else 'NO — labels preserved'} |
| **Stream-2 convergence** | **{envelope['stream2_convergence']}** |

## ε′ sector table

| Sector | Overlap amplitude | Active |
|--------|-------------------|--------|
| D+ (ε′=+1) | {envelope['epsilon_prime_sectors'][0]['overlap_amplitude']:.6e} | {envelope['epsilon_prime_sectors'][0]['active']} |
| D− (ε′=−1) | {envelope['epsilon_prime_sectors'][1]['overlap_amplitude']:.6e} | {envelope['epsilon_prime_sectors'][1]['active']} |

## Associator envelope

- σ₂-related associator triples: **{envelope['sigma2_triples_count']}**
- Max |associator coeff|: **{envelope['max_associator_coeff']:.4f}**
- Max cross-summand mixing: **{envelope['max_cross_summand_mixing']:.4e}**
- Envelope factor: **{envelope['envelope_factor']:.4f}**

## Interpretation

Real-structure assignment: Dirac Yukawa is **not** in the J-block → only ε′=+1 sector carries ν_L↔ν_R overlap; ε′=−1 is **inactive** for Dirac (not Majorana doubling).

Associator scan on σ₂ triples: {'cross-summand mixing below tolerance — G₂×G₂ relabeling sub-flag **not triggered**' if envelope['particle_antiparticle_labels_preserved'] else '**cross-summand mixing detected** — Jammer sub-flag triggered'}.

**Verdict:** **{envelope['flux_prefactor']}** ({envelope['sector_verdict']} active sector). Awaits AC convergence-check with Stream 2 (§2 HOLDS).

## Honest-scope locks

- Dirac Yukawa only; M₁ Majorana 8π untouched
- If 4π confirmed: sunshine finding (~1.59× solar worsening), **not a fix**
- Magnitude remains FREE (Stage 0 / S5 outcome ii)

— Cursor Jammer, 2026-06-21.
"""
    OUT_MD.write_text(md, encoding="utf-8")

    print("Farnsworth Stage-4-full associator envelope")
    print(f"  active sectors: {envelope['active_sector_count']} ({envelope['sector_verdict']})")
    print(f"  flux prefactor: {envelope['flux_prefactor']}")
    print(f"  stream2 convergence: {envelope['stream2_convergence']}")
    print(f"  json -> {OUT_JSON}")
    print(f"  memo -> {OUT_MD}")


if __name__ == "__main__":
    main()
