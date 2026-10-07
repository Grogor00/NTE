#!/usr/bin/env python3
"""Score readings of 'drop shared-ν second kinetic' against deposit claims.

Prior: G2 corridor = single-kinetic ν + HR-class potential.
This probe classifies ontology cost — research only, no Core patches.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


# Deposit claims that dual-kinetic / both-EOM language might be carrying
CLAIMS = {
    "D_both_EOM_stress": "Part 2: ν stress-energy appears in both Einstein equations",
    "D_bound_both_curvature": "Part 2 / C7: unresolved ν bound to curvature of both orientations",
    "D_bilateral_support": "C5/C7: bilateral support across CPN orientations (geometry)",
    "D_bridge_kappa0": "κ₀ from Hopf Y₀₀ overlap (C7 §4) — coupling strength",
    "D_shared_backbone": "Part 2: mirror matter couples through neutrino backbone",
    "D_z2_even": "Unresolved ν is Z₂-even (not locked to one orientation)",
    "D_bilateral_action": "Part 2 §IX: shared neutrino sector in single bilateral action",
    "D_amplifier": "Mirror feedback κ₀/(1−κ₀) — already withdrawn as actionless (ratified)",
}


@dataclass(frozen=True)
class ReadingScore:
    id: str
    name: str
    drops_second_kinetic: bool
    claim_fate: dict[str, str]  # claim_id -> survive|die|re_read|withdrawn|n_a
    ghost_outlook: str
    ontology_cost: str  # none|amendment|fatal
    suggested_k: str
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def catalog() -> list[ReadingScore]:
    items: list[ReadingScore] = []

    # R0: status quo dual kinetic (baseline cost of NOT dropping)
    items.append(
        ReadingScore(
            id="R0",
            name="Keep dual-kinetic ν (status quo deposit reading)",
            drops_second_kinetic=False,
            claim_fate={
                "D_both_EOM_stress": "survive",
                "D_bound_both_curvature": "survive",
                "D_bilateral_support": "survive",
                "D_bridge_kappa0": "survive",
                "D_shared_backbone": "survive",
                "D_z2_even": "survive",
                "D_bilateral_action": "survive",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="generally_ghost_1408",
            ontology_cost="none",
            suggested_k="n_a_baseline",
            notes="Preserves literal Part 2 both-EOM stress; blocked by 1408 for HR completion.",
        )
    )

    # R1: K1-shaped — bilateral ≠ dual kinetic
    items.append(
        ReadingScore(
            id="R1",
            name="Single kinetic on g⁺; bilateral = geometric overlap only",
            drops_second_kinetic=True,
            claim_fate={
                "D_both_EOM_stress": "re_read",  # both EOM from bridge variation, not T_ν twice
                "D_bound_both_curvature": "re_read",
                "D_bilateral_support": "survive",
                "D_bridge_kappa0": "survive",
                "D_shared_backbone": "re_read",
                "D_z2_even": "survive",
                "D_bilateral_action": "re_read",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="hr_viable_if_potential_ok",
            ontology_cost="amendment",
            suggested_k="K1",
            notes="Claims 'bound to both' as geometry/κ₀, not second kinetic. Needs deposit re-read of 'appears in both EOMs'.",
        )
    )

    # R2: K2-shaped — admit amendment
    items.append(
        ReadingScore(
            id="R2",
            name="Single kinetic + explicit deposit amendment of both-EOM stress",
            drops_second_kinetic=True,
            claim_fate={
                "D_both_EOM_stress": "die",
                "D_bound_both_curvature": "re_read",
                "D_bilateral_support": "survive",
                "D_bridge_kappa0": "survive",
                "D_shared_backbone": "re_read",
                "D_z2_even": "survive",
                "D_bilateral_action": "re_read",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="hr_viable_if_potential_ok",
            ontology_cost="amendment",
            suggested_k="K2",
            notes="Honest: rewrite Part 2 sentence on both-EOM ν stress. Not a free re-read.",
        )
    )

    # R3: K3 split — κ₀ survives, dual stress dies
    items.append(
        ReadingScore(
            id="R3",
            name="Split: κ₀ + Z₂-even geometry survive; dual T_ν dies",
            drops_second_kinetic=True,
            claim_fate={
                "D_both_EOM_stress": "die",
                "D_bound_both_curvature": "survive",  # as geometric, not kinetic
                "D_bilateral_support": "survive",
                "D_bridge_kappa0": "survive",
                "D_shared_backbone": "re_read",
                "D_z2_even": "survive",
                "D_bilateral_action": "re_read",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="hr_viable_if_potential_ok",
            ontology_cost="amendment",
            suggested_k="K3",
            notes="Sharpest split: C7 κ₀/bilateral geometry ≠ Part 2 dual kinetic stress sentence.",
        )
    )

    # R4: K4 — bridge dies
    items.append(
        ReadingScore(
            id="R4",
            name="Single kinetic kills backbone (no cross-orientation coupling left)",
            drops_second_kinetic=True,
            claim_fate={
                "D_both_EOM_stress": "die",
                "D_bound_both_curvature": "die",
                "D_bilateral_support": "die",
                "D_bridge_kappa0": "die",
                "D_shared_backbone": "die",
                "D_z2_even": "re_read",
                "D_bilateral_action": "die",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="standard_gr_one_sided",
            ontology_cost="fatal",
            suggested_k="K4",
            notes="Only if bilateral work required dual kinetic with no HR/overlap substitute.",
        )
    )

    # R5: potential-only second couple (1408 safe) without second kinetic
    items.append(
        ReadingScore(
            id="R5",
            name="Single kinetic + P̃(ϕ)-style potential couple to g⁻ (1408 §IV)",
            drops_second_kinetic=True,
            claim_fate={
                "D_both_EOM_stress": "re_read",  # potential couple sources both sides differently
                "D_bound_both_curvature": "re_read",
                "D_bilateral_support": "survive",
                "D_bridge_kappa0": "re_read",  # may not equal Y₀₀ unless derived
                "D_shared_backbone": "re_read",
                "D_z2_even": "survive",
                "D_bilateral_action": "re_read",
                "D_amplifier": "withdrawn",
            },
            ghost_outlook="1408_safe_subclass",
            ontology_cost="amendment",
            suggested_k="K3",
            notes="Literature-safe double *potential* couple ≠ dual kinetic. κ₀ identity not automatic.",
        )
    )

    return items


def summary(items: list[ReadingScore] | None = None) -> dict[str, Any]:
    items = items or catalog()
    drop = [r for r in items if r.drops_second_kinetic]
    fatal = [r for r in drop if r.ontology_cost == "fatal"]
    amend = [r for r in drop if r.ontology_cost == "amendment"]
    # Mechanical hint: if any non-fatal drop reading keeps κ₀+bilateral+z2, prefer K3
    keep_core = [
        r
        for r in amend
        if r.claim_fate.get("D_bridge_kappa0") == "survive"
        and r.claim_fate.get("D_bilateral_support") == "survive"
        and r.claim_fate.get("D_z2_even") == "survive"
        and r.claim_fate.get("D_both_EOM_stress") in ("die", "re_read")
    ]
    hint = "K3" if keep_core else ("K4" if fatal and not amend else "K2")
    return {
        "n_readings": len(items),
        "drop_ids": [r.id for r in drop],
        "amendment_ids": [r.id for r in amend],
        "fatal_ids": [r.id for r in fatal],
        "keep_kappa0_bilateral_z2_ids": [r.id for r in keep_core],
        "suggested_fork_hint": hint,
        "claims": CLAIMS,
        "readings": [r.to_dict() for r in items],
        "prior": "G2 corridor from cpn_gravity R01",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(summary(), indent=2))
