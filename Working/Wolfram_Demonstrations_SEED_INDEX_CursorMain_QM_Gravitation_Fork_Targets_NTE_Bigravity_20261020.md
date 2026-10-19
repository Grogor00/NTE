# Wolfram Demonstrations — seed index (QM + gravitation)

**Purpose:** Starting notebooks to **fork/modify** for future NTE / bigravity / Opsi2 work — not substitutes for constraint-chain results.  
**Topics:** [quantum-mechanics](https://demonstrations.wolfram.com/topic/quantum-mechanics) · [gravitation-theory](https://demonstrations.wolfram.com/topic/gravitation-theory)  
**Load pattern:** `ResourceData["Demonstration: <Exact Title>"]` (Wolfram Engine 15 on host)  
**Fence:** Working only; no Core. Pedagogical seeds ≠ prior art for action (N).

---

## Matter / spinor seeds → fork toward dual-kinetic Dirac, χ, S1/S2

| Demonstration | URL slug | Fork toward |
|---|---|---|
| Pauli Spin Matrices | `PauliSpinMatrices` | σ/γ algebra checks; ladder ops; SU(2) generators in WL |
| Dirac Matrices in Higher Dimensions | `DiracMatricesInHigherDimensions` | γ-matrix conventions; dim checks before 3+1 ADM spinor work |
| Representation of Spinors by Two-Dimensional Complex Rotations | `RepresentationOfSpinorsByTwoDimensionalComplexRotations` | 2-spinor intuition; normalize/phase; later map to densitized φ |
| Relativistic Quantum Dynamics in 1D and the Klein Paradox | `RelativisticQuantumDynamicsIn1DAndTheKleinParadox` | Dirac vs Schrödinger evolution scaffolding; **not** curved-space |
| Relativistic Ground State of Hydrogen-Like Atoms | `RelativisticGroundStateOfHydrogenLikeAtoms` | Upper/lower Dirac components; Z-scan numerics patterns |
| Schrödinger Equation for a Dirac Bubble Potential | `SchroedingerEquationForADiracBubblePotential` | Radial + δ-shell numerics (name collision only — not GR Dirac) |

---

## Geometry / GR seeds → fork toward HR metrics, X, frames, effective vielbein

| Demonstration | URL slug | Fork toward |
|---|---|---|
| Geodesics in Schwarzschild Space | `GeodesicsInSchwarzschildSpace` | Metric + geodesic integrator patterns → dual-metric geodesics |
| Orbits around Schwarzschild Black Holes | `OrbitsAroundSchwarzschildBlackHoles` | Manipulate/UI + orbital ODEs; retarget to \(g\)/`f` or \(\tilde e\) |
| Schwarzschild Space-Time Embedding Diagram | `SchwarzschildSpaceTimeEmbeddingDiagram` | 3-geometry visualization; later embedding of \(X=\sqrt{h_g^{-1}h_f}\) |
| Geodesic Precession on a Timelike Circular Orbit around a Schwarzschild Black Hole | `GeodesicPrecessionOnATimelikeCircularOrbitAroundASchwarzschi` | Local frames / Fermi–Walker → tetrad transport sketches |
| The Gravitational Two-Body Problem in the Einstein-Infeld-Hoffmann Approximation | `TheGravitationalTwoBodyProblemInTheEinsteinInfeldHoffmannApp` | PN two-metric intuition; **not** ghost-free bigravity |

---

## Weak / ambient (only if needed)

| Demonstration | Note |
|---|---|
| Circle Packing and Hamiltonian Mappings | Kicked Hamiltonian maps — phase-space viz only |
| A Gravitational Optimization Problem | Toy gravity optimization — not ADM |
| Eigenvalue Problem for 2×2 Hermitian Matrices | Tiny Hermitian eigensystem demo; Pauli snapshots |

---

## Suggested fork recipe (when GO’d)

1. `ResourceData["Demonstration: …"]` → save under `Working\WL_Seeds\`.  
2. Strip Manipulate chrome; keep algebraic/ODE core.  
3. Retarget: single metric → \((g,f)\) or \(\tilde e=ae+bf\); flat Dirac → densitized φ / χ sketch.  
4. Never cite a Demonstration as discharging Claim 3 / G-1–G-2.

**Out of scope on these topic pages (build ourselves):** ADM / Dirac–Bergmann, HR \(D(n)\), \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\), χ second-class matrix, Melville–Noller rank-2.

— Cursor Main, 2026-10-20.
