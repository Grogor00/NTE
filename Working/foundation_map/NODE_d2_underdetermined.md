# NODE_d2_underdetermined

| Field | Content |
|---|---|
| **id** | `d2_underdetermined` |
| **claim** | At Hilbert-space dimension d = 2, Gleason-type uniqueness fails: there exist probability assignments on rays (or related structures) other than the standard Born rule that still satisfy the remaining frame-function / symmetry conditions used in that setting; the Born rule is therefore **underdetermined** at d = 2 without extra assumptions (e.g. POVM / effect-valued measures). |
| **source** | (i) **Computed counterexample family**, Scratch, 2026-10-15: functions including sin²(πr/2) and r + ε·sin(2πr) pass the stated d=2 conditions (see Scratch C2-counterexample handoff 2026-10-15). (ii) Busch, P. (2003), “Quantum states and generalized observables: a simple proof of Gleason’s theorem,” *Phys. Rev. Lett.* **91**, 120403 — POVM route restoring uniqueness by enlarging the domain. |
| **type** | counterexample family (verified) + theorem (Busch POVM route) |
| **assumes** | The d=2 conditions Scratch used (state as r ∈ [0,1] / related); Busch assumes effects/POVMs rather than sharp projectors only. |
| **establishes** | Projector-level Born uniqueness does **not** hold at d = 2 without further assumptions; POVM/effect Gleason restores uniqueness under those larger assumptions. |
| **does not establish** | That C2’s specific Hopf uniqueness claim is false for reasons other than d=2 underdetermination (that is a deposit reading). That complex QM is false. Any positive derivation of the Born exponent from geometry alone. |
| **status** | established (underdetermination at d=2); Busch POVM uniqueness established under its assumptions |
| **verified** | Cursor Main, 2026-10-16 — Scratch computation cited as lane verification (2026-10-15); Busch claim from standard citation / secondary summary this session (`verified: YES` for Scratch leg; `PARTIAL` for Busch primary text). |

**Edges:** `assumes`-context → `gleason_born_d_ge_3` (shows its d≥3 hypothesis is essential). `gap-between` candidate vs Hopf-geometric uniqueness programmes (Scratch to name).
