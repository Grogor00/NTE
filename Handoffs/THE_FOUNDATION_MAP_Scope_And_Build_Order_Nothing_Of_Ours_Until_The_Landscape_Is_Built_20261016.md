# THE FOUNDATION MAP — scope and build order. **The true beginning of the rebuild.** Nothing of ours enters until the external landscape is mapped.

**From:** AC (Claude) · **To:** Greg (ratification), Cursor Main (build), Jammer, Scratch (verification), PC (cc)
**Date:** 2026-10-16 · **Greg's direction 08:27 NZDT:** *"We are starting on the shoulders of giants. We're not making shit up from the get-go."*
**Status: scope + build order. Greg ratifies, then Cursor begins.**

---

## 0. **AC's failure, stated first, because it is why this document exists**

**AC proposed the dependency graph on 2026-09-30, specified it in detail, and never built it.** AC raised it again on 2026-10-11 as methodology weakness (d), wrote that *"every propagation failure is what it was designed to catch"*, and still did not build it. **Cursor Main offered the prep twice.**

**The reason it lapsed is diagnosable: it was never anyone's next action.** It was always infrastructure to be built after the current urgent item, and there was always a current urgent item.

**The fix: the map IS the task.** Nothing else is scheduled until it exists. **Greg has asked for this repeatedly across the project's life and has been right every time.**

## 1. **What this map is — and it is not the graph AC proposed before**

**Greg's original purpose, from the project's beginning:** a meta-analysis of what the world's best minds have established about quantum physics, mathematics and cosmology — **to find which links between established results have been missed.**

**That needs a different object than a dependency graph over our own papers.** It is a map of the **external** landscape:

> **claim → who established it → what it rests on → what it is compatible with → where the gaps between established results actually are.**

**The gaps are where a contribution can live, and they are only visible once the landscape is mapped.** A map built around our own claims would show our gaps, not the field's.

## 2. **The rule that makes it worth having**

> **Nothing of ours enters the map until the external landscape is built. Not one claim.**

**Then our surviving results are placed inside it and we see what they touch.** **This ordering is the method** — the same discipline as *anomaly-first, never prediction-first*, applied to the literature instead of to data.

## 3. **Node schema — fixed now so it is uniform**

| Field | Content |
|---|---|
| **id** | stable short key |
| **claim** | one sentence, at the strength its source supports |
| **source** | author, year, arXiv/DOI — **fetched, never recollection** |
| **type** | theorem / experimental result / no-go / reconstruction / framework / open problem |
| **assumes** | premises, each a node id where possible |
| **establishes** | what follows |
| **does not establish** | **the field whose absence caused three axiom failures in our own work** |
| **status** | established / contested / superseded — dispute named |
| **verified** | who read the source, when |

**Edges:** `assumes`, `excludes`, `supersedes`, `is-compatible-with`, `gap-between`.

**`gap-between` is the field Greg's purpose actually requires** — two established results with no established bridge.

## 4. **Seed set — this month's work supplies it, verified**

**These are not our claims. They are external results already sourced, several computed by our own lanes.**

| Node | Source | Established |
|---|---|---|
| **Born rule from non-contextual additivity, d ≥ 3** | Gleason 1957 | theorem |
| **d = 2 is underdetermined** | **computed 2026-10-15**; Busch 2003 for the POVM route | **counterexample family verified** |
| **Complex QM from operational axioms** | Hardy 2001; CDP 2011; Masanes–Müller 2011 | reconstruction |
| **Qubit Bloch ball is 3-dimensional** | Masanes–Müller 2011 | group-theoretic |
| **G₂ ⊃ SU(3), 7 → 1 ⊕ 3 ⊕ 3̄** | Günaydin–Gürsey; **computed 2026-10-16** | theorem |
| **G₂ cannot contain SU(3)×SU(2)×U(1)** | **rank 2 vs 4; computed 2026-10-16** | **no-go** |
| **SM group inside F₄ = Aut(J₃(𝕆))** | Dubois-Violette–Todorov | framework |
| **SM from Cl(6) ideals** | Furey | framework |
| **Doubly-coupled matter revives the BD ghost** | arXiv:1408.0487 | theorem, with exception |
| **Ghost-free bimetric gravity** | Hassan–Rosen | framework; **β coefficients free** |
| **Unimodular / trace-free Λ** | Buchmüller–Dragon; Henneaux–Teitelboim; **Jiroušek 2023 condition** | framework, contested |
| **N_eff = 2.86 ± 0.13** | ACT DR6 + Planck | experimental |
| **Mirror baryons need x ≲ 0.3** | mirror-matter literature | constraint |
| **Spectral action's cosmological term; volume quantisation** | Chamseddine–Connes; CCM 2014 | theorem — **needs M₂(ℍ) ⊕ M₄(ℂ)** |
| **CPT-symmetric universe; RH neutrino dark matter** | Boyle–Finn–Turok | framework |

**Every one carries a source; several carry our own verification.**

## 5. Build order

1. **Cursor Main builds the seed set** as structured files in `Working\foundation_map\`, one per node, schema §3. **Fetch every source; mark anything unfetched as unverified.**
2. **Jammer verifies** — **is any node stated at a strength its source does not support?** **That is the single most important check**, and it is the failure mode that produced our register drift.
3. **Scratch extends** — **which established results are adjacent but unconnected?** Those become `gap-between` edges. **This is where Greg's original purpose is served.**
4. **Only then: place our surviving results** — the f(|⟨φ|ψ⟩|²) reduction, κ₀ as geometry, the S³ topology — **and see what they touch.**

## 6. Standing

**No f. No Core. This does not reopen the closure**, which proceeds in parallel under Stage 1.

**Sourced or marked unverified — no exceptions.**

**"We thought this was established and it is contested" is a valuable node, not a failure.**

---

— AC, 2026-10-16.
