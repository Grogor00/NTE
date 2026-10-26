# NODE_gleason_born_d_ge_3

| Field | Content |
|---|---|
| **id** | `gleason_born_d_ge_3` |
| **claim** | In a Hilbert space of dimension d ≥ 3, any non-contextual frame function (probability assignment additive on orthogonal resolutions of the identity) is given by the Born rule Tr(ρP) for a unique density operator ρ. |
| **source** | Gleason, A. M., “Measures on the closed subspaces of a Hilbert space,” *J. Math. Mech.* 6 (1957) 885–893. PDF fetched 2026-10-27. Theorem 4.1: dimension at least three, real or complex. The same paper: in dimension two a frame function can be defined arbitrarily on a closed quadrant. |
| **type** | theorem |
| **assumes** | Complex Hilbert space; d ≥ 3; non-contextual additivity on orthogonal projectors (frame-function axioms). |
| **establishes** | Uniqueness of the Born rule among non-contextual additive probability assignments in d ≥ 3. |
| **does not establish** | The dimension-two case, which the paper states separately. Measures on projections in factors of type II or III. |
| **status** | established |
| **verified** | Cursor Main, 2026-10-27 — PDF fetched. `verified: YES`. |

**Edges (seed):** `excludes` → underdetermination of pure projector Born rule in d=2 (see `d2_underdetermined`). `is-compatible-with` → `complex_qm_operational` (reconstructions recover Born as part of QT).
