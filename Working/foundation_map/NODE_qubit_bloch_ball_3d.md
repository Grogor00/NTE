# NODE_qubit_bloch_ball_3d

| Field | Content |
|---|---|
| **id** | `qubit_bloch_ball_3d` |
| **claim** | In the Masanes–Müller reconstruction, the state space of the elementary system (capacity-2 / qubit) is forced to be the **3-dimensional Bloch ball** (group-theoretic consequence of the physical requirements). |
| **source** | Masanes, L. & Müller, M. P. (2011), *New J. Phys.* **13**, 063001, arXiv:1004.1483. Reused Cursor literature leg 2026-10-15. |
| **type** | reconstruction (group-theoretic corollary) |
| **assumes** | `complex_qm_operational` (Masanes–Müller axiom package). |
| **establishes** | Dimensionality 3 of the qubit state space under those axioms; geometric picture of reversible transformations as rotations of the Bloch ball. |
| **does not establish** | That the physical universe is a 3-sphere. That spin-j systems live on S³ (they live on S^{4j+1}). Identification of Bloch S² / S³ with cosmological geometry. |
| **status** | established within Masanes–Müller |
| **verified** | Cursor Main, 2026-10-15/16 — arXiv abstract/HTML; `verified: YES` at claim strength above. |

**Edges:** `assumes` → `complex_qm_operational`. `gap-between` vs physical-S³ identification programmes (Scratch).
