# NODE_d2_underdetermined

| Field | Content |
|---|---|
| **id** | `d2_underdetermined` |
| **claim** | Gleason, 1957: in dimension two a frame function may be defined arbitrarily on a closed quadrant of the unit circle, and the standard theorem does not apply. Once the frame function is defined on effects, uniqueness is recovered for a qubit. A published continuous family of non-Born rules on the Bloch sphere is any odd \(f:[-1,1]\to[-1,1]\) with \(f(1)=1\); the paper's example is \(f(x)=x^{2n+1}\). |
| **source** | Gleason, *J. Math. Mech.* 6 (1957) 885–893, PDF fetched 2026-10-27: dimension at least three for the trace formula; dimension two stated separately. Caves, Fuchs, Manne, and Renes, quant-ph/0306179, HTML fetched 2026-10-27: the effect argument works for qubits, where the standard theorem fails. arXiv:2603.07745, HTML fetched 2026-10-27. |
| **type** | counterexample family (verified) + theorem (Busch POVM route) |
| **assumes** | Measurements restricted to one-dimensional projectors, for the underdetermination. Effects, for the recovery. |
| **establishes** | Projector-only uniqueness fails for a qubit. Effect-valued frame functions restore it. |
| **does not establish** | That a qubit is underdetermined once effects are allowed. That every non-Born formula is the family in arXiv:2603.07745. |
| **status** | established |
| **established by** | Gleason 1957 for the dimension-two gap; quant-ph/0306179 for the effect recovery; arXiv:2603.07745 for an explicit family. |
| **verified** | Cursor Main, 2026-10-27 — all three primaries fetched. `verified: YES`. |

**Edges:** `assumes`-context → `gleason_born_d_ge_3` (shows its d≥3 hypothesis is essential).
