# NODE_g2_cannot_contain_sm

| Field | Content |
|---|---|
| **id** | `g2_cannot_contain_sm` |
| **claim** | G₂ has rank 2; the compact group SU(3)×SU(2)×U(1) has rank 4; a compact Lie subgroup cannot have rank exceeding its parent — therefore **G₂ cannot contain SU(3)×SU(2)×U(1) as a Lie subgroup**. Independently: the centraliser of Stab(e₁) ≅ su(3) inside g₂ is **0**, so no commuting electroweak factors sit inside g₂ beside colour. |
| **source** | Elementary Lie theory (rank). **Computed:** Jammer 2026-10-16; Scratch 2026-10-16 (independent) — SO(4) candidate factors fail to commute with colour (reported residuals). Handoffs: Jammer/Scratch G₂ rank obstruction 2026-10-16. |
| **type** | no-go |
| **assumes** | Standard ranks: rank(G₂)=2; rank(SU(3))=2, rank(SU(2))=1, rank(U(1))=1. Compact connected Lie-group subgroup theorems. |
| **establishes** | Any construction that places the full SM gauge algebra inside g₂ is impossible. Colour-only G₂⊃SU(3) remains allowed (`g2_su3_branching`). |
| **does not establish** | Failure of F₄ or Cl(6)/ℂ⊗ℍ⊗𝕆 programmes (those use larger structure). That the SM group cannot arise in octonion-related models *at all*. Phenomenology. |
| **status** | established |
| **verified** | Cursor Main, 2026-10-16 — rank argument elementary; lane computations cited. `verified: YES`. |

**Edges:** `excludes` “SM ⊂ G₂”. `is-compatible-with` `sm_inside_f4`, `sm_from_cl6_furey` (external sources for electroweak).
