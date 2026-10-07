#!/usr/bin/env python3
"""Score candidate CPN maps against deposited work requirements.

Advances O2 (C-3): the deposited z→−z formula fails deposit-work.
This probe enumerates alternatives and scores them — research objects,
not Core patches. No κ=Ω_DM restore.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


# Deposit-work requirements (from O2 read set / Part 2 / C5 / C7 / Part 1)
REQUIREMENTS = {
    "R_baryon_sort": "Can implement §8.4 matter→+N / antimatter→−N sorting",
    "R_not_gauge": "Not merely unobservable fibre phase on resolved matter (C7)",
    "R_su2r": "Can underwrite SU(2)_R → mirror (§8.5–8.6)",
    "R_MA_MB": "Can underwrite M_A = M_B (C5 §6 apparatus)",
    "R_acts_on_N": "Acts on N-thickness / e-fold orientation (Part 1 §2.1.2)",
    "R_deposited": "Explicitly deposited as a formula or operator locus",
    "R_free_symmetry": "Compatible with antipodal as free symmetry (not RP³ quotient)",
}


@dataclass(frozen=True)
class MapScore:
    id: str
    name: str
    geometric_content: str
    scores: dict[str, bool]
    full_work: bool
    deposited: bool
    notes: str
    o2_relation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _score(**flags: bool) -> dict[str, bool]:
    out = {k: False for k in REQUIREMENTS}
    out.update(flags)
    return out


def catalog() -> list[MapScore]:
    """Candidate maps. Booleans are structural judgments encoded for scoring;
    clones may dispute individual flags in verdicts with deposit cites."""

    items: list[MapScore] = []

    s = _score(
        R_baryon_sort=False,
        R_not_gauge=False,  # C7: fibre phase unobservable
        R_su2r=False,
        R_MA_MB=False,
        R_acts_on_N=False,  # acts on S³ coords, not N
        R_deposited=True,  # C5 §5
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M0",
            name="Deposited fibre half-turn z→−z = e^{iπ}",
            geometric_content="Hopf U(1) fibre rotation by π; identity on S² base",
            scores=s,
            full_work=all(s[k] for k in s if k != "R_deposited"),
            deposited=True,
            notes="O2 C-3 object. Deposit formula; fails deposit-work.",
            o2_relation="C-3 confirmed if scores hold",
        )
    )

    s = _score(
        R_baryon_sort=True,  # sorting is exactly N-commitment
        R_not_gauge=True,
        R_su2r=False,  # gauge assignment needs more than N-flip
        R_MA_MB=True,  # CPN-symmetric equal |N| sheets
        R_acts_on_N=True,
        R_deposited=False,  # stated in prose, no operator formula
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M1",
            name="N-reversal only: (x,N) → (x,−N) on thickness",
            geometric_content="Orientation flip of N-thickness; orthogonal to S³ fibre",
            scores=s,
            full_work=all(
                s[k]
                for k in (
                    "R_baryon_sort",
                    "R_not_gauge",
                    "R_su2r",
                    "R_MA_MB",
                    "R_acts_on_N",
                    "R_free_symmetry",
                )
            ),
            deposited=False,
            notes="Does sorting + equal sheets; does NOT by itself assign SU(2)_R. Not a deposited formula.",
            o2_relation="Partial survivor; not full CPN",
        )
    )

    s = _score(
        R_baryon_sort=False,
        R_not_gauge=True,
        R_su2r=False,
        R_MA_MB=False,
        R_acts_on_N=False,
        R_deposited=True,  # C7 identifies C with antipodal exchange
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M2",
            name="Field charge conjugation C alone",
            geometric_content="ψ → ψ^c on spinors; deposit links to antipodal points",
            scores=s,
            full_work=False,
            deposited=True,
            notes="Physical on resolved matter, but without N-sorting does not place antimatter on −N.",
            o2_relation="Necessary piece; insufficient alone",
        )
    )

    s = _score(
        R_baryon_sort=False,
        R_not_gauge=True,
        R_su2r=False,
        R_MA_MB=False,
        R_acts_on_N=False,
        R_deposited=True,  # parity rule (−1)^ℓ in C5
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M3",
            name="Spatial parity / harmonic rule (−1)^ℓ",
            geometric_content="Mode coupling selection under antipodal map",
            scores=s,
            full_work=False,
            deposited=True,
            notes="Governs cross-boundary mode coupling; not baryon sorting.",
            o2_relation="P-piece only",
        )
    )

    s = _score(
        R_baryon_sort=True,  # Part 1: Pin⁻ produces baryogenesis
        R_not_gauge=True,
        R_su2r=False,
        R_MA_MB=False,
        R_acts_on_N=True,  # twist of N-thickness
        R_deposited=True,  # Part 1 §VI
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M4",
            name="Pin⁻ spin structure on Z₂ orbifold",
            geometric_content="Topological twist of N-thickness; two spin structures",
            scores=s,
            full_work=False,
            deposited=True,
            notes="Answers 'why CPN?' topologically; not an explicit field map ψ₊→….",
            o2_relation="Topology, not operator",
        )
    )

    s = _score(
        R_baryon_sort=True,
        R_not_gauge=True,
        R_su2r=True,  # package claim
        R_MA_MB=True,
        R_acts_on_N=True,
        R_deposited=False,  # composite never written as one operator
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M5",
            name="Research composite: C ∘ P ∘ N on fields + thickness",
            geometric_content="ψ₊(x,N) ↦ (CP ψ)₋(P·x, −N) with Pin⁻ sector choice",
            scores=s,
            full_work=True,  # by construction of flags — clone must stress-test
            deposited=False,
            notes="Would score full work IF defined. Not deposited. Research object only (P2 candidate).",
            o2_relation="P2 if clone endorses; else P3",
        )
    )

    s = _score(
        R_baryon_sort=True,
        R_not_gauge=True,
        R_su2r=False,
        R_MA_MB=True,
        R_acts_on_N=True,
        R_deposited=False,  # Θ named not constructed
        R_free_symmetry=True,
    )
    items.append(
        MapScore(
            id="M6",
            name="CPT = Θ∘CPN with constructed Θ",
            geometric_content="C5 names Θ reconciling N-flip with common proper time",
            scores=s,
            full_work=False,
            deposited=False,
            notes="Θ is a label without a formula. Does not rescue M0.",
            o2_relation="Named gap inside C5",
        )
    )

    s = _score(
        R_baryon_sort=False,  # quotient: antimatter has nowhere distinct to go
        R_not_gauge=True,
        R_su2r=False,
        R_MA_MB=False,
        R_acts_on_N=False,
        R_deposited=False,  # Scratch: deposit is free symmetry NOT quotient
        R_free_symmetry=False,
    )
    items.append(
        MapScore(
            id="M7",
            name="Elliptic / RP³ quotient (antipodes identified)",
            geometric_content="S³/ℤ₂ or dS/ℤ₂ single-metric identification",
            scores=s,
            full_work=False,
            deposited=False,
            notes="Kills second budget; conflicts with §8.4 sorting. Not NTE's reading.",
            o2_relation="Rejected by deposit + Scratch G1",
        )
    )

    return items


def summary(maps: list[MapScore] | None = None) -> dict[str, Any]:
    maps = maps or catalog()
    full = [m for m in maps if m.full_work]
    deposited_full = [m for m in full if m.deposited]
    partial = [
        m
        for m in maps
        if not m.full_work
        and sum(m.scores.values()) >= 3
        and m.id != "M0"
    ]
    return {
        "n_candidates": len(maps),
        "full_work_ids": [m.id for m in full],
        "deposited_full_work_ids": [m.id for m in deposited_full],
        "partial_survivor_ids": [m.id for m in partial],
        "m0_fails_work": not maps[0].full_work,
        "suggested_fork_hint": (
            "P1"
            if deposited_full
            else ("P2" if full else "P3")
        ),
        "requirements": REQUIREMENTS,
        "maps": [m.to_dict() for m in maps],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(summary(), indent=2))
