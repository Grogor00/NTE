# NODE_doubly_coupled_bd_ghost

| Field | Content |
|---|---|
| **id** | `doubly_coupled_bd_ghost` |
| **claim** | arXiv:1408.0487: the Boulware–Deser ghost generally revives when matter is doubly coupled, and ghost-freeness strongly restricts kinetically doubly coupled matter. That paper does not discuss a Dirac field. arXiv:1511.01485 treats a Dirac field on one effective vielbein in mini-superspace and finds that only rank-2 couplings are ghost-free for scalar, Yang–Mills, and Dirac fields simultaneously in that analysis. |
| **source** | Yamashita, De Felice, and Tanaka, arXiv:1408.0487, HTML fetched 2026-10-27. Melville and Noller, arXiv:1511.01485, HTML fetched 2026-10-27, equations (4.16)–(4.21). |
| **type** | theorem (no-go with stated exceptions) |
| **assumes** | Ghost-free vacuum bimetric setup; matter stress-energy sourcing more than one metric in the generic way analysed in that paper. |
| **establishes** | Double kinetic coupling revives the ghost in the setting of arXiv:1408.0487. In the mini-superspace of arXiv:1511.01485, only rank-2 couplings are ghost-free for a Dirac field together with the other species they treat. |
| **does not establish** | That every coupling to two metrics revives the ghost. That a Dirac field with two independent kinetic terms, one on each vielbein, has been analysed. That coupling was not found in either fetched paper. It stays open. Lapse-linearity of the double-lapse theory is an aligned-sector result. It does not establish lapse-linearity in the boost sector. The reading of that sector is settled: the f-leg spatial operator is the boosted tetrad \(M^k\) (Reading F). Three statements stay separate. Through O(\(\psi^2\)) the Hamiltonian is lapse-linear, by the envelope theorem in the 2026-10-31 ruling. At O(\(\psi^2\)) the bracket statement is \(c_I(p)\neq w_g\) given a posited \(w_g=\Sigma_g\). The \(\Sigma_f=0\) comparison is genuine and trivial, because then \(C=\Sigma_g I\) and \(c_I=\Sigma_g\). The first O(\(\psi^4\)) substitution used a plain-symmetric stand-in and landed no decision: frozen-\(D\) median defect 0.00013061802459940486, above \(10^{-8}\). The 2026-11-01 run was pre-registered with \(A = L\,{}^3f + N\,{}^3f D\) and \(D^{-T} = {}^3f D^{-1} {}^3f^{-1}\). Frozen g-only median defect \(2.3592239273284576\times 10^{-16}\). Full median defect 0.17213192083195888. Identity median relative residual 1.057043420910219. Both sit above \(10^{-3}\), so the pre-registered landing is that the quartic piece survives. The same run's median relative asymmetry of \({}^3f D\) is 0.23477974400100576, so this \(D\) is not symmetric with respect to \({}^3f\). The ghost is not declared. |
| **status** | established for arXiv:1408.0487 and for the mini-superspace rank-2 result; the two-kinetic Dirac coupling is open |
| **established by** | Yamashita–De Felice–Tanaka, arXiv:1408.0487. Melville–Noller, arXiv:1511.01485, for the effective-vielbein mini-superspace. |
| **verified** | Cursor Main, 2026-10-27 — both HTML primaries fetched. `verified: YES`. |

**Edges:** `excludes` naive doubly-coupled matter in HR bimetric. Constrains `hassan_rosen_bimetric` matter sector.
