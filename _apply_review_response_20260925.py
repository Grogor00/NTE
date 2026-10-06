# -*- coding: utf-8 -*-
"""Byte-exact apply: X/Y/Z≻U2/U/AA. Match-or-report. Never force."""
from pathlib import Path

BOOK = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
report = []


def apply(src: Path, dst: Path, patches, label: str) -> None:
    text = src.read_text(encoding="utf-8")
    for pid, old, new in patches:
        if old not in text:
            report.append(f"FAIL {label}/{pid}: OLD not found")
            continue
        n = text.count(old)
        if n != 1:
            report.append(f"FAIL {label}/{pid}: expected 1 occurrence, found {n}")
            continue
        text = text.replace(old, new, 1)
        report.append(f"OK   {label}/{pid}")
    dst.write_text(text, encoding="utf-8", newline="\n")
    report.append(f"WROTE {dst.name} ({dst.stat().st_size} B)")


# --- Ch4 X ---
apply(
    BOOK / "Chapter_04_Time_and_Expansion_v9.md",
    BOOK / "Chapter_04_Time_and_Expansion_v10.md",
    [
        (
            "X1",
            "Both Chapter 1 and Chapter 3 returned to the photon at their close, because the photon is the framework's first and clearest test case. Here, with the time-emergence picture in place, we can give the cleanest version yet.",
            "Both Chapter 1 and Chapter 3 returned to the photon at their close, because the photon is the framework's first and clearest test case. Here, with the binding of time to expansion in place, we can give the cleanest version yet.",
        ),
        (
            "X2",
            "The *post-temporal* regime is everything we usually mean when we talk about the universe. It's the era from very shortly after the Big Bang to the present. In this regime, *t* has emerged, the relationship dt/dN = 1/(β_NTE|Φ_NTE|²) is well-defined and stable, and ordinary time-based physics works. General relativity, quantum mechanics, thermodynamics, nuclear physics — all of them apply normally. Using *t* in this regime is correct, not an approximation. The deeper structure (*N*) is always there, but the emergent description (*t*) is complete and self-consistent within its domain of validity.",
            "The *post-temporal* regime is everything we usually mean when we talk about the universe. It's the era from very shortly after the Big Bang to the present. In this regime *t* is well-defined, the relationship dt/dN = 1/(β_NTE|Φ_NTE|²) is stable, and ordinary time-based physics works. General relativity, quantum mechanics, thermodynamics, nuclear physics — all of them apply normally. Using *t* in this regime is correct, not an approximation. The deeper structure (*N*) is always there, but the derived description (*t*) is complete and self-consistent within its domain of validity.",
        ),
        (
            "X3",
            'The *pre-temporal* regime is everything before time emerged. In the framework\'s picture, this is not "the early universe before the Big Bang" in any conventional sense.',
            'The *pre-temporal* regime is everything below the range of *N* in which *t* is definable at all. In the framework\'s picture, this is not "the early universe before the Big Bang" in any conventional sense.',
        ),
        (
            "X4",
            "You can use it pre-temporally, when the framework explicitly says no temporal structure has yet emerged, and the equations still make sense.",
            "You can use it pre-temporally, where the framework explicitly says no temporal structure is yet in place, and the equations still make sense.",
        ),
        (
            "X5",
            "For now, the picture to hold is this: the boundary expansion field does not just regulate the rate of proper time accumulation.",
            "For now, the picture to hold is this: the boundary expansion field does not just regulate the rate at which cosmic time accumulates.",
        ),
        (
            "X6",
            "The framework's central scalar is |Φ_NTE|, the geometric scalar whose strength regulates the rate at which proper time accumulates per unit expansion.",
            "The framework's central scalar is |Φ_NTE|, the geometric scalar whose strength regulates the rate at which cosmic time accumulates per unit expansion.",
        ),
        (
            "X7",
            "This is not a metaphor. It's the framework's specific claim. Time, for any physical system, is the integrated outcome of that system's embedding in the universe's expansion. A different coupling pattern would give a different time.",
            "This is not a metaphor. It's the framework's specific claim. Time, for any physical system, is the integrated outcome of that system's embedding in the universe's expansion. A different distribution of rest energy would give a different time.",
        ),
    ],
    "Ch4",
)

# --- Ch5 Y ---
apply(
    BOOK / "Chapter_05_The_Eighth_Colour_v8.md",
    BOOK / "Chapter_05_The_Eighth_Colour_v9.md",
    [
        (
            "Y1",
            "Before the gauge birth, in the pre-temporal regime, |Φ_NTE| existed as a geometric scalar without the dynamics that V_NTE imposes post-locking.",
            "Before the gauge birth, in the pre-temporal regime, |Φ_NTE| existed as a geometric scalar without the post-locking dynamics it later acquires.",
        ),
        (
            "Y2",
            "What it has not done is develop the geometric *origin* of |Φ_NTE|. Where does the field come from? Why does its potential V_NTE have the form it has, with the specific dynamics the technical corpus develops? What is the relationship between |Φ_NTE|'s pre-temporal identity as a geometric scalar and its post-temporal identity as the field that sources H?",
            "What it has not done is develop the geometric *origin* of |Φ_NTE|. Where does the field come from? What governs its post-locking dynamics, and why those rather than others? What is the relationship between |Φ_NTE|'s pre-temporal identity as a geometric scalar and its post-temporal identity as the field that sources H?",
        ),
    ],
    "Ch5",
)

# --- Ch15 AA ---
apply(
    BOOK / "Chapter_15_The_Score_v4.md",
    BOOK / "Chapter_15_The_Score_v5.md",
    [
        (
            "AA1",
            "Chapter 10's companion claim: the transition to tight convergence near ~40 Mpc.",
            "Chapter 10's companion claim: the transition to tight convergence above a coherence mass of around 4 × 10¹⁴ solar masses, the neutrino free-streaming scale — which the framework adopts rather than derives, its own contribution being the combination of that scale with the scaling law and the mean.",
        ),
    ],
    "Ch15",
)

# --- Ch10: U1, U3, U4, U5, Z1 (≻U2), Z2, Z3 ---
apply(
    BOOK / "Chapter_10_The_Silvered_Boundary_v7.md",
    BOOK / "Chapter_10_The_Silvered_Boundary_v8.md",
    [
        (
            "U1",
            "Recall from Chapter 9 the cross-thickness coupling: the geometry of the manifold itself knits the two orientations together, and gravitational curvature on either orientation registers across the manifold's N-thickness in the other orientation's metric. This registration is mediated through the unresolved neutrino's bilateral wavefunction, the only species in the framework whose quantum state has support across both orientations.",
            "Recall from Chapter 9 the cross-thickness coupling: the geometry of the manifold itself knits the two orientations together, and gravitational curvature on either orientation registers across the manifold's N-thickness in the other orientation's metric. The registration needs something bilaterally supported to register against, and the unresolved neutrino is the only species in the framework whose quantum state has support across both orientations. It is worth keeping the roles apart, because the natural misreading is the one Chapter 9 works hardest to prevent: the neutrino does not carry the coupling and nothing passes through it. The coupling is a fact about the manifold's geometry, present whether or not anything bilateral exists; the neutrino is the structure that gives it somewhere to act, and so the thing that makes it show up in the equations we measure.",
        ),
        (
            "U3",
            "The mirror relation flips the orientation of the manifold's e-fold thickness — the N direction — and emergent proper time is not that direction; time, in the framework, runs orthogonal to the thickness, and flipping N leaves the arrow of time untouched.",
            "The mirror relation flips the orientation of the manifold's e-fold thickness — the N direction — and the emergent cosmic time is not that direction; time, in the framework, runs orthogonal to the thickness, and flipping N leaves the arrow of time untouched.",
        ),
        (
            "U4",
            "A system's gravitational accounting samples the fluctuating coupling across however many independent coherence patches the system spans, and averaging over independent samples is one of the oldest results in mathematics: the scatter of the average falls as the square root of the number of samples.",
            "A system's gravitational accounting samples the fluctuating coupling across however many independent coherence patches the system spans, and averaging over independent samples is one of the oldest results in mathematics: the scatter of the average falls as one over the square root of the number of samples.",
        ),
        (
            "U5",
            "Chapter 15 assembles the framework's claims into the scorecard, each at its graded register. κ stands there among the three genuine zero-parameter predictions, alongside the maximal CP phase and the maximal atmospheric mixing angle; the spectral index and the tensor-to-scalar ratio sit in the conditional tier, awaiting an open normalisation; the neutrino mass scales sit as cross-checks, the striking solar match carried with its branch caveat; the cosmic-mean Hubble parameter is filed honestly as a consequence of construction rather than a test, with the genuine prediction being the void-correlated scatter in local measurements; the quietness of empty space stands as structural mechanism without a claimed number; and the framework's live tensions are catalogued at full volume in Appendix C.",
            "Chapter 15 assembles the framework's claims into the scorecard, each at its graded register. κ stands there among the three genuine zero-parameter predictions, alongside the maximal CP phase and the maximal atmospheric mixing angle; the spectral index and the tensor-to-scalar ratio sit in the conditional tier, resting on a conformal coupling the framework selects rather than derives; the neutrino mass scales sit as cross-checks, the striking solar match carried with its branch caveat; the cosmic-mean Hubble parameter is filed honestly as a consequence of construction rather than a test, with the genuine prediction being the void-correlated scatter in local measurements; the quietness of empty space stands as structural mechanism without a claimed number. And the scorecard does not stop at the favourable entries. The framework is currently losing on the dark-energy equation of state, where DESI's second release prefers an evolving value over the fixed w = −1 the geometry requires, at about three standard deviations and with nothing internal to absorb it; it is losing on the atmospheric mass ratio and on primordial lithium; and it has withdrawn its leading-order solar mixing angle outright rather than replace it with a fitted one. All of that is catalogued at full volume in Appendix C, which is where a reader who wants to know whether this framework polices itself should go first.",
        ),
        (
            "Z1",
            "The framework's reading of dark matter has specific testable predictions beyond κ = 5.50. The cross-thickness coupling, mediated through the unresolved neutrino's bilateral wavefunction, has a *coherence length* set by the neutrino's free-streaming distance — the typical scale over which an unresolved neutrino's wavefunction maintains its bilateral structure before decoherence and gravitational scattering disrupt the coherent superposition.",
            "The framework's reading of dark matter has specific testable predictions beyond κ = 5.50. The coupling acts wherever the neutrino's bilateral wavefunction gives it a structure to act on, and that wavefunction does not hold its bilateral character over unlimited distances. So the coupling inherits a scale from it — the neutrino's free-streaming scale, the reach over which an unresolved neutrino's wavefunction maintains its bilateral structure before decoherence and gravitational scattering disrupt the coherent superposition. The framework states that scale as a *coherence mass* rather than a length, because a mass is what the gravitational accounting of a system actually turns on: above roughly 4 × 10¹⁴ solar masses, a system is large enough to average over many independent patches of the coupling; below it, it is not.",
        ),
        (
            "Z2",
            "This scale is roughly forty megaparsecs — about a hundred and thirty million light-years.\n\nTo put that in context: a typical dwarf galaxy is a few thousand light-years across. A typical large galaxy like our own Milky Way is about a hundred thousand light-years across. A typical galaxy cluster is a few million light-years across. A typical large-scale structure (a filament or supervoid in the cosmic web) is tens to hundreds of millions of light-years across. The framework's coherence length sits roughly at the boundary between galaxy-cluster scale and large-scale-structure scale.",
            "Four hundred trillion solar masses is a rich galaxy cluster. To put it in context: a typical dwarf galaxy holds perhaps a hundred million solar masses in total; our own Milky Way, a trillion or so; a large galaxy cluster, a few hundred trillion. The coherence mass therefore sits at the boundary between the cluster scale and the scale of the cosmic web's filaments and voids — which is the boundary the next section's prediction turns on.\n\nOne caveat travels with this, and the framework states it rather than leaving it implicit: the free-streaming scale is standard neutrino physics, not an NTE derivation. What is the framework's own is the *combination* — this scaling law, around this particular mean of 5.50, with the transition at this scale. And the *size* of the scatter within a single coherence patch is not predicted at all; the corpus carries that amplitude as open. The framework predicts that the scatter is there and how it falls away with mass, not how large it is at the bottom.",
        ),
        (
            "Z3",
            "The framework predicts that dwarf-galaxy dark-matter fractions will continue to show wide scatter, while galaxy-cluster fractions will converge toward the cosmic mean — with the scatter falling as σ(M) ∝ M^(−1/2) and the transition near the coherence length, ~40 megaparsecs. As galaxy surveys map increasingly large samples, the distribution should settle into that three-part pattern: shape, mean, and scale. A failure of any part would break the framework's specific claim.",
            "The framework predicts that dwarf-galaxy dark-matter fractions will continue to show wide scatter, while galaxy-cluster fractions will converge toward the cosmic mean — with the scatter falling as σ(M) ∝ M^(−1/2) above the coherence mass, around 4 × 10¹⁴ solar masses. As galaxy surveys map increasingly large samples, the distribution should settle into that three-part pattern: shape, mean, and scale. The sharpest of the three is the shape: the corpus's own falsifier is the absence of the M^(−1/2) scaling above the coherence mass, and that is the leg that would break the two-sector mechanism outright.",
        ),
    ],
    "Ch10",
)

print("\n".join(report))
fails = [r for r in report if r.startswith("FAIL")]
raise SystemExit(1 if fails else 0)
