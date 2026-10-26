# NODE_g2_cannot_contain_sm

| Field | Content |
|---|---|
| **id** | `g2_cannot_contain_sm` |
| **claim** | G₂ cannot contain SU(3)×SU(2)×U(1) as a Lie subgroup. Todorov and Dubois-Violette: the only maximal subgroup of G₂ that keeps colour SU(3) is SU(3) itself, and the intersection of the maximal connected subgroups is U(2). Carone and Rastogi: the only rank-2 groups containing an SU(3) subgroup are G₂ and SU(3). |
| **source** | Todorov and Dubois-Violette, arXiv:1806.09450, equation (4.2), HTML fetched 2026-10-27. Carone and Rastogi, arXiv:0712.1011, HTML fetched 2026-10-27. |
| **type** | no-go |
| **assumes** | Standard ranks: rank(G₂)=2; rank(SU(3))=2, rank(SU(2))=1, rank(U(1))=1. Compact connected Lie-group subgroup theorems. |
| **establishes** | Any construction that places the full SM gauge algebra inside g₂ is impossible. Colour-only G₂⊃SU(3) remains allowed (`g2_su3_branching`). |
| **does not establish** | Failure of F₄ or Cl(6)/ℂ⊗ℍ⊗𝕆 programmes (those use larger structure). That the SM group cannot arise in octonion-related models *at all*. Phenomenology. |
| **status** | established |
| **established by** | Todorov–Dubois-Violette, arXiv:1806.09450, and Carone–Rastogi, arXiv:0712.1011. |
| **verified** | Cursor Main, 2026-10-27 — both HTML primaries fetched. `verified: YES`. |

**Edges:** `excludes` “SM ⊂ G₂”. `is-compatible-with` `sm_inside_f4`, `sm_from_cl6_furey` (external sources for electroweak).
