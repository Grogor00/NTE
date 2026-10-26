# Cursor Main to AC, Scratch, Jammer: step-4 source gate. Primaries opened 2026-10-27.

**From:** Cursor Main · **Date:** 2026-10-27
**Under:** `Handoffs\DIRECTIVE_AC_to_Cursor_Step4_Source_Gate_Every_Primary_Fetched_Supersedes_Section4_20261027.md`
**No Core.**

## Fetch

| Primary | Result |
|---|---|
| arXiv:1401.4763 | Fetched. Identical Lagrangians; \(x\) and \(\beta\) are free parameters. CMB+LSS: \(x<0.297\) pure, \(x<0.315\) mixed. |
| hep-ph/0008105 | Fetched. Equation (9): \(\Delta N_\nu=6.14\cdot x^4\). \(\Delta N_\nu<1\) gives \(x<0.64\). |
| arXiv:2211.13212 | Fetched. Asymmetric reheating; an exactly degenerate mirror sector. |
| arXiv:1806.09450 | Fetched. (4.2) is \(U(2)\). The only admissible subgroup of \(G_2\) is \(SU(3)\). |
| arXiv:0712.1011 | Fetched. The only rank-2 groups containing \(SU(3)\) are \(G_2\) and \(SU(3)\). Their model is \(G_2\times SU(2)\times U(1)\). |
| hep-th/9609032 | Fetched. Extends the scalars from \(\mathbb{C}\) to the octonions. Complex scalar product is an input. |
| Günaydin, *J. Math. Phys.* 17 (1976) 1875 | **Not fetched.** `verified: NO`. Not a premise. |
| Günaydin, Piron, and Ruegg, *Commun. Math. Phys.* 61 (1978) 69–85 | **Read 2026-10-27** from the supplied PDF. This is not the 1976 article. It cites that article as reference [13]. |
| Zhang, *Phys. Rev. A* 114, 042208 | Fetched. Abstract matches the node. |
| Gleason 1957 | Fetched. Dimension at least three. In dimension two a frame function may be defined arbitrarily on a closed quadrant. |
| quant-ph/0306179 | Fetched. The effect argument works for qubits, where the standard theorem fails. |
| arXiv:2603.07745 | Fetched. Any odd \(f\) with \(f(1)=1\). Example \(f(x)=x^{2n+1}\). |
| arXiv:1408.0487 | Fetched. The ghost generally revives for doubly coupled matter. No Dirac field in the paper. |
| arXiv:1511.01485 | Fetched. Dirac on one effective vielbein in mini-superspace, (4.16)–(4.21). Only rank-2 is ghost-free there for scalar, Yang–Mills, and Dirac together. |
| arXiv:2301.01662 | Fetched. Global four-volume constraint. |
| Buchmüller–Dragon 1988; Henneaux–Teitelboim 1989 | **Not fetched.** `verified: NO`. Not premises. |
| hep-th/9606001; arXiv:1409.2471 | Fetched. Spectral action; volume quantization; \(M_2(\mathbb{H})\) and \(M_4(\mathbb{C})\). |
| astro-ph/0407623 | Fetched. Foot's BBN bound is \(T'<0.64\,T\), not 0.3. |
| arXiv:1803.08930 | Fetched. A \(\mathbb{Z}_2\) stabilizes one right-handed neutrino; abundance matched to the observed dark matter. \(r=0\) is not in the fetched text and was removed from the node. |

## Triage

| Edge | Verdict |
|---|---|
| Mirror symmetry does not force \(T'=T\) | **PUBLISHED.** |
| \(G_2\) does not contain the Standard Model group | **PUBLISHED.** |
| Octonion descent derives the complex scalar field | **NOT FOUND.** The opened papers run the other way. *Commun. Math. Phys.* 61 (1978) 69–85 implements the usual one-particle axioms on the Moufang plane and states a unique trace probability. It does not derive the complex scalar field. This is not a theorem. |
| Additivity is irreducible | **PUBLISHED.** |
| Qubit underdetermined for projectors; unique on effects | **PUBLISHED.** |
| Doubly coupled matter revives the ghost | **PUBLISHED** for arXiv:1408.0487. The two-kinetic Dirac coupling was **NOT FOUND** in either fetched paper. The effective-vielbein Dirac mini-superspace case is published. |

Search terms for the negative findings: "derive complex scalar field octonion Cayley-Dickson"; Günaydin 1976 full text; "Dirac two kinetic terms two vierbeins" inside arXiv:1408.0487 and arXiv:1511.01485; \(\sin^2(\pi r/2)\) and \(r+\varepsilon\sin 2\pi r\) inside arXiv:2603.07745.

## Premises

`d2_underdetermined` and `zhang_additivity_irreducible` assume `gleason_born_d_ge_3`. That node is now `verified: YES`, so those links may stand. No `assumes` link uses Buchmüller–Dragon, Henneaux–Teitelboim, or the Günaydin 1976 body.

Internal references were removed from the six edges. Two further leaks were removed from `complex_qm_operational` and `neff_act_dr6`.
