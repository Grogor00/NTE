"""Candidate bridge laws and FLRW / CPN algebraic reductions (Phase 0).

No Core patches. No fitting to Planck 5.38. Stress-tensor-in-action
candidates are marked non-fundamental.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Any

KAPPA0 = 3.0 / math.sqrt(4.0 * math.pi)
PLANCK_OMEGA_DM_OB = 5.38  # reference only — not a fit target


@dataclass(frozen=True)
class CandidateResult:
    id: str
    name: str
    fundamental: bool
    track: str
    eom_sketch: str
    r_bg: float | None
    r_bg_formula: str
    total_over_baryon: float | None
    amp_like: bool
    ghost_risk: str
    perturbation_character: str
    notes: str
    phase0_status: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _cpn_linear(alpha: float) -> tuple[float, float]:
    """G = 8π M (1+α); extra/baryon = α; total/baryon = 1+α."""
    return alpha, 1.0 + alpha


def _cpn_total_feedback(k0: float) -> tuple[float, float]:
    """G - k0 G = 8π M  =>  G/(8πM) = 1/(1-k0); extra/baryon = k0/(1-k0)."""
    if k0 >= 1.0:
        return float("inf"), float("inf")
    r = k0 / (1.0 - k0)
    return r, 1.0 / (1.0 - k0)


def catalog(kappa0: float = KAPPA0) -> list[CandidateResult]:
    r_lin, tot_lin = _cpn_linear(kappa0)
    r_fb, tot_fb = _cpn_total_feedback(kappa0)

    return [
        CandidateResult(
            id="C0",
            name="No bridge",
            fundamental=True,
            track="null",
            eom_sketch="G± = 8π T_m±",
            r_bg=0.0,
            r_bg_formula="0",
            total_over_baryon=1.0,
            amp_like=False,
            ghost_risk="none",
            perturbation_character="n/a",
            notes="Baseline: no cross-sector gravity.",
            phase0_status="algebra_done",
        ),
        CandidateResult(
            id="C1",
            name="Linear cross-sourcing at α=κ₀",
            fundamental=False,  # EOM-level until S_ν derives it
            track="N-effective",
            eom_sketch="G± = 8π (T_m± + κ₀ T_m∓)",
            r_bg=r_lin,
            r_bg_formula="α = κ₀",
            total_over_baryon=tot_lin,
            amp_like=False,
            ghost_risk="low_if_from_matter",
            perturbation_character="inherits twin: baryon-like / hot under CPN",
            notes=(
                "Natural variation target for shared channel copying bare twin stress. "
                "Mutual solve is simultaneous, not a geometric series in total G."
            ),
            phase0_status="algebra_done",
        ),
        CandidateResult(
            id="C2",
            name="Total-feedback / Einstein-tensor mixing",
            fundamental=False,
            track="amplifier",
            eom_sketch="G± − κ₀ G∓ = 8π T_m±",
            r_bg=r_fb,
            r_bg_formula="κ₀/(1−κ₀)",
            total_over_baryon=tot_fb,
            amp_like=True,
            ghost_risk="high_if_kinetic_mixing",
            perturbation_character="still not Planck CDM under P2 (location-blind / hot twin)",
            notes=(
                "Produces ~5.50. Requires mixing solved gravity or hand S_cons. "
                "Not entailed by 'two sectors interact' alone."
            ),
            phase0_status="algebra_done",
        ),
        CandidateResult(
            id="C3",
            name="Historical bilinear T·T + S_cons (quarantine)",
            fundamental=False,
            track="historical",
            eom_sketch="S_bridge∝T_b+ T_b− ; S_cons: T̃=T_b+κ₀ T̃",
            r_bg=r_fb,
            r_bg_formula="κ₀/(1−κ₀) via S_cons inversion",
            total_over_baryon=tot_fb,
            amp_like=True,
            ghost_risk="ill_posed_as_fundamental",
            perturbation_character="same as C2 for background; P2 blocks CDM ID",
            notes=(
                "Pathway A A3: bilinear not first-principles forced; T in action "
                "is not a fundamental field. Control case only."
            ),
            phase0_status="quarantine_control",
        ),
        CandidateResult(
            id="C4",
            name="Bilkinetic Majorana S_ν (Track N target)",
            fundamental=True,
            track="N",
            eom_sketch="G± = 8π (T_m± + T_ν[g±,ν]); joint Dirac/Majorana EOM",
            r_bg=None,
            r_bg_formula="ρ_ν / ρ_b  (from ν solution; not κ₀/(1−κ₀) a priori)",
            total_over_baryon=None,
            amp_like=False,
            ghost_risk="low_standard_spinor",
            perturbation_character="light ν → hot / free-streaming; ΔN_eff risk under CPN",
            notes=(
                "BL-1 deliverable: write S_ν, vary, reduce. Phase 0 does not invent ρ_ν."
            ),
            phase0_status="bl1_open",
        ),
        CandidateResult(
            id="C5",
            name="Hassan–Rosen ghost-free bigravity (+ optional ν)",
            fundamental=True,
            track="B",
            eom_sketch="G(g)=8π T_m(g)+τ(g,f); G(f)=8π T_m(f)+τ(f,g)",
            r_bg=None,
            r_bg_formula="interaction / branch dependent (not fixed by κ₀ alone)",
            total_over_baryon=None,
            amp_like=False,
            ghost_risk="healthy_on_HR_branch",
            perturbation_character="branch-dependent; often DE-like / modified gravity, not CDM",
            notes="Track B. Adopt-and-credit HR; identify NTE metrics with (g,f).",
            phase0_status="bl1_open",
        ),
        CandidateResult(
            id="C6",
            name="Wrong-sign metric kinetic mixing",
            fundamental=False,
            track="killed_unless_proven",
            eom_sketch="□h + κ₀ □l = −T_h (schematic)",
            r_bg=r_fb if kappa0 < 1 else None,
            r_bg_formula="can mimic C2 algebraically",
            total_over_baryon=tot_fb if kappa0 < 1 else None,
            amp_like=True,
            ghost_risk="typically_ghost",
            perturbation_character="n/a if ghostly",
            notes="BL-4 default FAIL. Only revive with a proof of health.",
            phase0_status="default_fail_bl4",
        ),
    ]


def summary_table(rows: list[CandidateResult]) -> str:
    lines = [
        "| ID | Name | Fund. | r_bg | Amp? | Status |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        rbg = "—" if r.r_bg is None else f"{r.r_bg:.4f}"
        lines.append(
            f"| {r.id} | {r.name} | {r.fundamental} | {rbg} | {r.amp_like} | {r.phase0_status} |"
        )
    return "\n".join(lines)


def phase0_verdict(rows: list[CandidateResult]) -> str:
    c1 = next(r for r in rows if r.id == "C1")
    c2 = next(r for r in rows if r.id == "C2")
    return (
        "## Phase-0 algebraic verdict\n\n"
        f"- κ₀ = {KAPPA0:.6f}\n"
        f"- **C1 (linear, α=κ₀):** r_bg = {c1.r_bg:.4f}, "
        f"total/baryon = {c1.total_over_baryon:.4f} — simultaneous mutual solve, "
        f"**no** amplifier.\n"
        f"- **C2/C3 (total-feedback / historical):** r_bg = {c2.r_bg:.4f} "
        f"(≈5.50). Decimal proximity to Planck {PLANCK_OMEGA_DM_OB} is "
        f"**not** Phase-0 success; law is not fundamental until derived.\n"
        "- **C4/C5:** open — require BL-1 variational work; r_bg not assumed.\n"
        "- **C6:** default BL-4 fail (ghost risk).\n"
        "- **Landing so far:** E1–E3 confirmed algebraically; "
        "terminal fork still **F-OPEN** pending BL-1.\n"
    )
