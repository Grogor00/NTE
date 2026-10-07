#!/usr/bin/env python3
"""Cosmology-modification paths that aim to keep particle locks.

Greg 2026-10-07: axioms may need modifying for cosmology; chase paths that
maintain particle-sector successes. Research catalogue only — no Core patches
until Greg/AC select. No κ=Ω_DM restore by fitting.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

# Hard locks from PARTICLE_LOCK.md
HARD_LOCKS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10"]


@dataclass(frozen=True)
class ModPath:
    id: str
    name: str
    axiom_changes: list[str]
    keeps_hard_locks: bool
    soft_lock_cost: str
    cosmology_targets: list[str]  # what it tries to unlock
    prior_blockers_addressed: list[str]  # G2, P3, CDM, origin, Neff, …
    ghost_outlook: str
    particle_risk: str
    status_hint: str  # live | costly | kill_likely | presentation
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def catalog() -> list[ModPath]:
    return [
        ModPath(
            id="P01",
            name="G2 corridor: single-kinetic ν + HR potential + amend both-EOM stress",
            axiom_changes=[
                "Rewrite Part 2/C5: ν stress not kinetically in both EOMs",
                "Adopt HR-class potential (to be derived or imported+credited)",
                "Keep κ₀ as overlap; no amplifier action",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S3 regraded (geometry not dual-kinetic); K2∩K3",
            cosmology_targets=["well-posed two-orientation gravity", "bridge without BD"],
            prior_blockers_addressed=["G2", "1408", "K2∩K3"],
            ghost_outlook="viable_if_HR_constructed",
            particle_risk="low",
            status_hint="live",
            notes="Direct continuation of R01 G2 + single-kinetic programme. Does not by itself give CDM or origin.",
        ),
        ModPath(
            id="P02",
            name="P01 + deposit working CPN map (C∘P∘N / N-reversal operator)",
            axiom_changes=[
                "All of P01",
                "Replace C5 z→−z work-claim with explicit field+thickness map (research→axiom if selected)",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S2 repaired if map works; P3 addressed",
            cosmology_targets=["baryon sorting well-defined", "orientation relation defined"],
            prior_blockers_addressed=["P3", "O2 C-3", "G2"],
            ghost_outlook="same_as_P01",
            particle_risk="low_if_map_preserves_Majorana_and_deltaJ",
            status_hint="live",
            notes="Closes CPN defect as axiom choice. Must not disturb L2/L4.",
        ),
        ModPath(
            id="P03",
            name="Particle CDM (sterile/Z₂ or other) + thin bilateral geometry",
            axiom_changes=[
                "Withdraw conjugate-footprint-as-CDM permanently",
                "Add P-newDM particle sector (BFT-like or other) with abundance law",
                "Bilateral geometry optional / κ₀ structural only",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S3 optional; S4 referent becomes particle not geometric echo",
            cosmology_targets=["observed CDM", "possibly N_eff if twin radiation dropped"],
            prior_blockers_addressed=["CDM open", "maybe Neff"],
            ghost_outlook="standard_if_single_metric_or_P01",
            particle_risk="low; must not spoil L2 Majorana story",
            status_hint="live",
            notes="Separates DM from bilateral echo. Compatible with honest-path body A.",
        ),
        ModPath(
            id="P04",
            name="Body A full strength + ΛCDM cosmology grafted (minimal B)",
            axiom_changes=[
                "Cosmology sector = standard ΛCDM (+ optional NTE w=-1 emphasis)",
                "Bilateral dark sector demoted to open geometry essay",
                "No claim of geometric CDM or NTE inflation unless separately rebuilt",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S2/S3/S4 not load-bearing for observations",
            cosmology_targets=["empirically adequate cosmology now", "clear registers"],
            prior_blockers_addressed=["CDM", "origin", "ghost", "CPN-for-cosmo"],
            ghost_outlook="n_a_standard_GR",
            particle_risk="none",
            status_hint="live",
            notes="AC honest-path extreme: particle wins; cosmology not native. Not a failure — a scope choice.",
        ),
        ModPath(
            id="P05",
            name="BFT-style CPT two sheets replace two orientation-metrics",
            axiom_changes=[
                "Replace CPN/N-thickness twin by CPT/analytic a→−a sheets",
                "Adopt BFT sterile DM or equivalent",
                "Rewrite Part 1 §VI bilateral action accordingly",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S1/S3 heavily rewritten; NTE distinctness vs BFT shrinks",
            cosmology_targets=["CDM", "baryon asymmetry via CPT", "no primordial GW option"],
            prior_blockers_addressed=["CDM", "ghost dual-metric", "CPN map"],
            ghost_outlook="single_metric_ok",
            particle_risk="medium — must re-derive L2/L4 in CPT language or keep as imports",
            status_hint="costly",
            notes="Converges toward published cousin. Preserve L1–L10 by keeping Hopf/Majorana/δ_J modules.",
        ),
        ModPath(
            id="P06",
            name="Drop second Einstein equation; single metric + κ₀ effective coupling",
            axiom_changes=[
                "One dynamical metric",
                "κ₀ as effective cross-term only if derived without second metric",
                "Delete load-bearing two-equation dark sector",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S1 kept; S3 dies as two-metric; Scratch warned this deletes dark sector",
            cosmology_targets=["ghost-free trivially", "need new CDM"],
            prior_blockers_addressed=["G2", "1408", "BD"],
            ghost_outlook="free",
            particle_risk="low",
            status_hint="costly",
            notes="Forces P03 or P04 for CDM. Ontology simplification with cosmology outsourcing.",
        ),
        ModPath(
            id="P07",
            name="Cosmological origin exit only (Starobinsky / singlet / move handover)",
            axiom_changes=[
                "Select origin-sector exit (Part 3 option D live options)",
                "Do not touch bilateral/ν kinetic until separate path",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="none on soft locks",
            cosmology_targets=["inflation/handover", "n_s/r eventually"],
            prior_blockers_addressed=["origin OPEN"],
            ghost_outlook="unchanged_bilateral_still_open",
            particle_risk="low if not Higgs-doublet inflation (dead)",
            status_hint="live",
            notes="Necessary but not sufficient — does not fix G2/P3/CDM.",
        ),
        ModPath(
            id="P08",
            name="Two-register deposit (A strong / B open) — presentation path",
            axiom_changes=[
                "No physics change required",
                "Restructure claim registers per AC honest path",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="none",
            cosmology_targets=["reader trust", "parallel open B research"],
            prior_blockers_addressed=["register mismatch"],
            ghost_outlook="unchanged",
            particle_risk="none",
            status_hint="presentation",
            notes="Compatible with any physics path. Should ship alongside live physics paths.",
        ),
        ModPath(
            id="P09",
            name="Hybrid: P01 gravity fix + P03 particle CDM + P07 origin",
            axiom_changes=[
                "Union of P01+P03+P07 axiom lists",
                "Geometric bilateral retained without CDM claim",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S3 geometry-only; S4 not Ω_DM",
            cosmology_targets=["well-posed gravity", "CDM", "origin"],
            prior_blockers_addressed=["G2", "CDM", "origin", "partial P3 if +P02"],
            ghost_outlook="viable_if_HR",
            particle_risk="low",
            status_hint="live",
            notes="Maximal cosmology rebuild without abandoning bilateral geometry essay.",
        ),
        ModPath(
            id="P10",
            name="Keep dual-kinetic ν; seek 1408 exception / new ghost-free double couple",
            axiom_changes=[
                "Assert NTE ν is special healthy doubly-coupled matter",
                "Requires new proof beyond 1408",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="none if succeeds",
            cosmology_targets=["preserve literal Part 2 both-EOM stress"],
            prior_blockers_addressed=["G2_if_proven"],
            ghost_outlook="blocked_by_1408_until_exception",
            particle_risk="low",
            status_hint="kill_likely",
            notes="Literature presumption against. Live only if a proof appears — clones should not assume one.",
        ),
        ModPath(
            id="P11",
            name="Restore κ=Ω_DM by new cold co-located mechanism (forbidden-shaped)",
            axiom_changes=["Whatever makes geometric echo look like Planck CDM"],
            keeps_hard_locks=True,
            soft_lock_cost="high temptation to f",
            cosmology_targets=["headline DM number"],
            prior_blockers_addressed=["CDM_if_honest"],
            ghost_outlook="unknown",
            particle_risk="discipline L10 at risk",
            status_hint="kill_likely",
            notes="Pre-registered kill unless mechanism is cold+co-located+collisionless without fitting. Planck538 exhausted.",
        ),
        ModPath(
            id="P12",
            name="Elliptic dS / antipodal quotient cosmology",
            axiom_changes=[
                "Quotient identification (conflicts with free-symmetry baryon sorting)",
                "Single metric",
            ],
            keeps_hard_locks=True,
            soft_lock_cost="S2 sorting broken unless rebuilt",
            cosmology_targets=["simpler global geometry"],
            prior_blockers_addressed=["two-metric ghost"],
            ghost_outlook="single_metric",
            particle_risk="medium — baryogenesis story",
            status_hint="costly",
            notes="Rejected as NTE reading before; only live if S2 rebuilt differently.",
        ),
    ]


def summary() -> dict[str, Any]:
    paths = catalog()
    live = [p for p in paths if p.status_hint == "live"]
    costly = [p for p in paths if p.status_hint == "costly"]
    kill = [p for p in paths if p.status_hint == "kill_likely"]
    pres = [p for p in paths if p.status_hint == "presentation"]
    unbroken = [p for p in paths if p.keeps_hard_locks and p.status_hint in ("live", "costly", "presentation")]
    return {
        "n_paths": len(paths),
        "live_ids": [p.id for p in live],
        "costly_ids": [p.id for p in costly],
        "kill_likely_ids": [p.id for p in kill],
        "presentation_ids": [p.id for p in pres],
        "hard_lock_ok_ids": [p.id for p in unbroken],
        "recommended_chase_set": ["P01", "P02", "P03", "P04", "P07", "P08", "P09"],
        "hard_locks": HARD_LOCKS,
        "paths": [p.to_dict() for p in paths],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(summary(), indent=2))
