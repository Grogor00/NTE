# Phase 0 novelty triage — seven constraints

**Lane:** Cursor Main · **Date:** 2026-10-26
**Under:** `Handoffs\Directive_AC_to_Cursor_Phase0_Novelty_Triage_Blocking_Seven_Constraints_20261026.md`
**Rule:** a citation below is used only if the page was fetched this session or in the Paper II check of the same day. Search snippets that did not load are not citations.

## 1. G₂ rank 2 cannot contain SU(3)×SU(2)×U(1) — **PUBLISHED**

Todorov and Dubois-Violette, arXiv:1806.09450, fetched. Equation (4.2): the intersection of the maximal connected subgroups of \(G_2\) is \(U(2)\). They then say the only maximal subgroup of \(G_2\) that keeps colour \(SU(3)\) is \(SU(3)\) itself, and they take the Standard Model group from \(F_4\).

Carone and Rastogi, arXiv:0712.1011, fetched: "The only groups of rank 2 that contain an SU(3) subgroup are the groups G2 and SU(3) itself." Their model is \(G_2\times SU(2)\times U(1)\).

Our 2026-10-16 centraliser computation confirms this. It is not a second constraint. Detail: `Working\PaperII_Rank_Obstruction_SOURCE_CHECK_CursorMain_20261026.md`.

## 2. The ℂ-selection problem — **PARTIAL**

**Published, and it is the premise, not the conclusion.** Hurwitz's theorem classifies the algebras once a composition-algebra premise is granted. Gałecka, *Annales Universitatis Paedagogicae Cracoviensis* 13 (2021), fetched: "The only real finite-dimensional composition algebras are \(\mathbb{R}\), \(\mathbb{C}\), \(\mathbb{H}\) and \(\mathbb{O}\)." Baez, *Bull. Amer. Math. Soc.* 39 (2002), fetched AMS record: the 1898 theorem is reviewed, and the text says it does **not** claim that these are the only division algebras.

**Not found:** a published statement that the chain \(\mathbb{C}\subset\mathbb{H}\subset\mathbb{O}\) therefore cannot derive complex structure, or that a descent "borrows the norm from the Hilbert structure it means to explain."

**The closest paper states the other direction.** Furey and Hughes, *Phys. Lett. B* 831 (2022) 137186, arXiv:2210.10126, PDF fetched: "These complex structures derive from the octonions, then the quaternions, then the complex numbers."

Search terms that did not return the circularity sentence: "Hurwitz theorem octonion cannot derive complex numbers"; "Furey complex structure assumed not derived"; Günaydin–Gürsey; Dixon; Dubois-Violette; Todorov; Boyle.

## 3. Mirror symmetry, \(6.14x^4\), and the \(x\) bounds — **PARTIAL**

**The formula and the bounds are published. The forcing is not.**

Berezhiani, Comelli, and Villante, hep-ph/0008105, fetched. Equation (9): \(\Delta N_\nu=6.14\cdot x^4\). They translate \(\Delta N_\nu<1\) as \(x<0.64\), and \(\Delta N_\nu<1.5\) as \(x<0.70\). At \(x=1\) they write \(\Delta N_\nu\simeq 6.14\).

Ciarcelluti and Wallemacq, arXiv:1401.4763, fetched. They repeat \(\Delta N_\nu\simeq 6.14\,x^4\) and, citing Izotov, an upper limit \(x\lesssim 0.7\). Their own limits, 95% c.l.:

- CMB only: \(x<0.456\) (pure mirror), \(x<0.479\) (mixed).
- CMB+LSS: \(x<0.297\) (pure mirror), \(x<0.315\) (mixed).

The figure "\(x<0.46\)" is the CMB-only pure-mirror limit \(0.456\), rounded. It is not the CMB+LSS limit. Use \(0.456\) or the tighter pair, and say which data.

**Not what those papers say:** "an exact mirror symmetry forces \(T'=T\)." The same 1401.4763 text says identical Lagrangians do **not** force the same macroscopic evolution. \(x\) and \(\beta\) are free cosmological parameters. \(x=1\) is excluded by the bound. The symmetry does not set \(x\).

## 4. The escapes are closed by the symmetry — **NOT FOUND**

The statement searched for: asymmetric reheating and independent scale factors are closed by the symmetry that motivates the mirror.

What was fetched says the contrary for reheating.

- hep-ph/0008105: a lower mirror reheating temperature \(T'_R<T_R\) is how the \(x=1\) conflict is avoided.
- Li, Lin, Vagnozzi, and Visinelli, arXiv:2107.04045, fetched: for an **exact** \(Z_2\), the bound is met by initial conditions that give \(T'\lesssim 0.5\,T\), while the Lagrangian stays symmetric.
- Ireland and Koren, *Phys. Rev. D* 109 (2024) 103537, arXiv:2211.13212, fetched: asymmetric reheating during a high-temperature \(Z_2\)-breaking phase, with the sectors exactly degenerate at low temperature.

Boyle, Finn, and Turok, arXiv:1803.08928, PDF fetched. They use one scale factor, \(a(\tau)\propto\tau\), continued through the bang. They do not discuss a second scale factor, and they do not state a no-go against one.

Search terms: "asymmetric reheating exact mirror symmetry equal temperature forbidden"; Foot; Berezhiani; 1401.4763; twin Higgs; Boyle–Finn–Turok. No fetched paper states that the motivating symmetry closes these two escapes.

What remains unstated, and is the only candidate for a paper: a **symmetry of the cosmological state** (one shared scale factor, no free \(x\)), as distinct from a symmetry of the Lagrangian. That distinction was not found in the sources above.

## 5. Phase-stabiliser reduction to \(f(|\langle\phi|\psi\rangle|^2)\) — **NOT FOUND**

Fetched and not this claim:

- Caves, Fuchs, Manne, and Renes, quant-ph/0306179 (Busch's POVM argument). A frame function on all effects is \(\mathrm{tr}(WE)\), including for a qubit. They do not reduce an arbitrary rule by a phase stabiliser.
- Zhang, *Phys. Rev. A* 114 (2026) 042208. Additivity, not this reduction.

Search terms that did not return the reduction: "phase invariance qubit transition probability function of modulus squared overlap only"; Gleason; Busch 2003; Mosseri–Dandoloff; Urbantke. A 2026 axiomatic distance paper (arXiv:2603.00406) says an admissible **distance** depends only on overlap. That is not a probability rule, and it is not cited as this constraint.

## 6. \(d=2\) underdetermined, with the two formulas — **PARTIAL**

**Published for orthogonal projectors.** quant-ph/0306179, fetched: neither Gleason's theorem nor the POVM-free predecessor holds for a qubit while measurements are one-dimensional projectors.

**Published explicit family, different formulas.** arXiv:2603.07745, fetched: any odd \(f:[-1,1]\to[-1,1]\) with \(f(1)=1\) gives a probability \(\tfrac12[1+f(\mathbf{r}\cdot\mathbf{n})]\), continuous ones included. Their example is \(f(x)=x^{2n+1}\).

**Not found:** \(\sin^2(\pi r/2)\) and \(r+\varepsilon\sin 2\pi r\) as that family. Search: "sin Gleason qubit counterexample dimension 2"; "sin^2 Gleason qubit frame function".

**The underdetermination does not survive the widening Busch uses.** The same quant-ph/0306179 paper recovers a unique rule for a qubit once the frame function is defined on effects, and again for trine POVMs. A paper that says "\(d=2\) is underdetermined" without naming projector-only measures over-reaches this source.

## 7. Additivity is the irreducible probabilistic input — **PUBLISHED**

Zhang, *Phys. Rev. A* 114, 042208 (2026), DOI 10.1103/mqy7-s2db, journal PDF fetched. Stated there:

- Additivity and noncontextuality are not equivalent and cannot replace each other.
- Additivity is indispensable in Gleason, Busch, Deutsch–Wallace, Zurek, and Finkelstein–Hartle.
- Removing or weakening it breaks those derivations.
- The conclusion asked for is an extra postulate that already has a probabilistic character.

Our sentence matches that paper. It is a confirmation, not a new claim.

## What may still be drafted

| Constraint | Register for a paper |
|---|---|
| 1 | Clarification of Todorov–Dubois-Violette (4.2) and Carone–Rastogi. Not a no-go. |
| 2 | Only the unstated half: a named derivation whose norm is the Hilbert norm. Hurwitz itself is not that paper. |
| 3 | Do not republish \(6.14x^4\) or the \(x\) limits. The open sentence is the one the sources deny: that the symmetry sets \(x=1\). |
| 4 | Not a no-go against the mirror literature. The literature keeps asymmetric reheating under an exact Lagrangian \(Z_2\). A draft has to be about a symmetry of the state, and it has to say the Lagrangian-level escape is published and open. |
| 5 | Not found. Do not draft until a source note exists, or label it as computed here. |
| 6 | The projector-only gap is Gleason's, and a continuous family is already in arXiv:2603.07745. The two formulas were not found. Busch's POVM recovery has to be in the same paragraph. |
| 7 | Cite Zhang. Do not restate it as ours. |

BD-ghost was not triaged.
