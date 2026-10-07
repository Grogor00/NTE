#!/usr/bin/env python3
"""Classify gravity-completion candidates vs HR / 1408.0487 / ontology.

Advances O1 (W-2): HR exists; deposited shared-ν kinetic double couple
is in the generally-ghostly class. Research classification only — no Core patches.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


CRITERIA = {
    "C_ghost_free_known": "Known ghost-free in literature (or proven subclass)",
    "C_two_orientation_metrics": "Carries two dynamical orientation-metrics",
    "C_one_manifold": "Compatible with one-manifold ontology (Part 1 §VI)",
    "C_shared_nu_both_EOM": "Allows Z₂-even ν stress in BOTH Einstein equations",
    "C_kinetic_double_ok": "Kinetic double-coupling of matter allowed without BD revival",
    "C_constraint_complete": "Off g⁺≠g⁻ constraint/conservation structure known",
    "C_deposited_nte": "Matches NTE deposited bilateral action as written",
    "C_no_hand_constraint": "Needs no hand-imposed self-consistency constraint",
}


@dataclass(frozen=True)
class CompletionScore:
    id: str
    name: str
    literature: str
    scores: dict[str, bool]
    ontology_fit: str  # full | partial | conflict | other
    ghost_status: str  # free | generally_ghost | unknown | n_a
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _s(**flags: bool) -> dict[str, bool]:
    out = {k: False for k in CRITERIA}
    out.update(flags)
    return out


def catalog() -> list[CompletionScore]:
    items: list[CompletionScore] = []

    s = _s(
        C_ghost_free_known=True,
        C_two_orientation_metrics=True,
        C_one_manifold=False,  # standard HR is two metrics; ontology map open
        C_shared_nu_both_EOM=False,  # matter on one metric in healthy case
        C_kinetic_double_ok=False,
        C_constraint_complete=True,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="H0",
            name="Hassan–Rosen + matter on one metric",
            literature="HR 2011/2012; 1408.0487 § intro",
            scores=s,
            ontology_fit="partial",
            ghost_status="free",
            notes="Healthy. Does not host shared ν in both EOMs. W-2 content gap.",
        )
    )

    s = _s(
        C_ghost_free_known=True,
        C_two_orientation_metrics=True,
        C_one_manifold=False,
        C_shared_nu_both_EOM=False,  # potential-only on second metric
        C_kinetic_double_ok=False,
        C_constraint_complete=True,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="H1",
            name="HR + P̃=P̃(ϕ) potential-only second-metric couple",
            literature="1408.0487 §IV safe subclass",
            scores=s,
            ontology_fit="partial",
            ghost_status="free",
            notes="Safe double *potential* couple; not kinetic shared ν backbone.",
        )
    )

    s = _s(
        C_ghost_free_known=False,
        C_two_orientation_metrics=True,
        C_one_manifold=False,
        C_shared_nu_both_EOM=True,
        C_kinetic_double_ok=False,
        C_constraint_complete=False,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="H2",
            name="HR + kinetic doubly coupled matter (two kinetic terms)",
            literature="1408.0487 §§III–IV — BD generally revives",
            scores=s,
            ontology_fit="conflict",
            ghost_status="generally_ghost",
            notes="Closest naive home for shared ν kinetics; literature says ghost.",
        )
    )

    s = _s(
        C_ghost_free_known=False,
        C_two_orientation_metrics=True,
        C_one_manifold=True,
        C_shared_nu_both_EOM=True,
        C_kinetic_double_ok=False,
        C_constraint_complete=False,
        C_deposited_nte=True,
        C_no_hand_constraint=False,  # Part 2 §IX hand constraint
    )
    items.append(
        CompletionScore(
            id="N0",
            name="NTE deposited bilateral action (as written)",
            literature="Part 2 §IX; Part 3 OPEN; O1 W-2",
            scores=s,
            ontology_fit="full",
            ghost_status="generally_ghost",
            notes="Ontology fit by construction; ghost/constraint unfinished; hand S_cons.",
        )
    )

    s = _s(
        C_ghost_free_known=True,
        C_two_orientation_metrics=False,
        C_one_manifold=True,
        C_shared_nu_both_EOM=False,
        C_kinetic_double_ok=False,
        C_constraint_complete=True,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="E0",
            name="Elliptic de Sitter dS/ℤ₂ (antipodal quotient)",
            literature="hep-th/0209120; 1509.05890",
            scores=s,
            ontology_fit="other",
            ghost_status="n_a",
            notes="Single metric. Not two orientation-metrics. Conflicts with free-symmetry sorting.",
        )
    )

    s = _s(
        C_ghost_free_known=True,
        C_two_orientation_metrics=False,
        C_one_manifold=True,
        C_shared_nu_both_EOM=False,
        C_kinetic_double_ok=False,
        C_constraint_complete=True,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="B0",
            name="BFT CPT two-sheeted universe (a→−a isometry)",
            literature="1803.08928; 2109.06204",
            scores=s,
            ontology_fit="other",
            ghost_status="n_a",
            notes="One metric + CPT image; DM = sterile RH ν particle, not κ₀ bridge.",
        )
    )

    s = _s(
        C_ghost_free_known=True,
        C_two_orientation_metrics=False,
        C_one_manifold=True,
        C_shared_nu_both_EOM=False,
        C_kinetic_double_ok=False,
        C_constraint_complete=True,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="S0",
            name="Strict one-metric (all matter sources one g)",
            literature="standard GR",
            scores=s,
            ontology_fit="conflict",
            ghost_status="free",
            notes="Deletes dark sector / κ₀ bridge. Forbidden by settled ontology.",
        )
    )

    s = _s(
        C_ghost_free_known=False,
        C_two_orientation_metrics=True,
        C_one_manifold=True,
        C_shared_nu_both_EOM=False,  # ν kinetic on one; bridge by HR potential
        C_kinetic_double_ok=False,
        C_constraint_complete=False,
        C_deposited_nte=False,
        C_no_hand_constraint=True,
    )
    items.append(
        CompletionScore(
            id="H3",
            name="Research: HR on two orientation-metrics + ν single-kinetic + κ₀ from overlap",
            literature="not constructed; O1 W-2 missing content",
            scores=s,
            ontology_fit="partial",
            ghost_status="unknown",
            notes="Would need: derive HR potential from NTE; drop dual-kinetic ν; keep κ₀ as overlap. Ontology cost = G2.",
        )
    )

    return items


def summary(items: list[CompletionScore] | None = None) -> dict[str, Any]:
    items = items or catalog()
    healthy_full_ontology = [
        c
        for c in items
        if c.ghost_status == "free"
        and c.scores["C_one_manifold"]
        and c.scores["C_two_orientation_metrics"]
        and c.scores["C_shared_nu_both_EOM"]
        and c.scores["C_constraint_complete"]
    ]
    healthy_partial = [
        c
        for c in items
        if c.ghost_status == "free" and c.scores["C_two_orientation_metrics"]
    ]
    nte = next(c for c in items if c.id == "N0")
    return {
        "n_candidates": len(items),
        "healthy_full_ontology_ids": [c.id for c in healthy_full_ontology],
        "healthy_two_metric_ids": [c.id for c in healthy_partial],
        "nte_ghost_status": nte.ghost_status,
        "nte_ontology_fit": nte.ontology_fit,
        "shared_nu_kinetic_blocked_by_1408": True,
        "suggested_fork_hint": (
            "G1"
            if healthy_full_ontology
            else (
                "G2"
                if any(c.id == "H3" for c in items)
                else "G3"
            )
        ),
        "criteria": CRITERIA,
        "completions": [c.to_dict() for c in items],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(summary(), indent=2))
