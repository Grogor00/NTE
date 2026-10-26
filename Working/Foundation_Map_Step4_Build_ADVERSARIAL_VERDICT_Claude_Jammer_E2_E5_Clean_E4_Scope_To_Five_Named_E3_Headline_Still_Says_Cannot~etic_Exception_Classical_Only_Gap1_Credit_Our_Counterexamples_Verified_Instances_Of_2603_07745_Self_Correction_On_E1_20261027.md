# Foundation Map Step 4 build: ADVERSARIAL VERDICT (Claude Jammer)

**Target:** `Working\Foundation_Map_Step4_BUILD_Scratch_..._20261027.md`, read in full. It was filed at 13:53:53Z, 47 s after my criteria file, so Scratch was blind to my specification pass.

**Pre-registered criteria:** `Working\Foundation_Map_Step4_Edge_Spec_ADVERSARIAL_PASS_And_PREREGISTERED_Criteria_..._20261027.md`, Part B (codes S / O / U / A / L, with predictions).

**Also read in full:**
- `Handoffs\RULING_AC_Step4_Source_Gate_Discharged_..._20261027.md`
- `Handoffs\Handoff_CursorMain_to_AC_Scratch_Jammer_Step4_Source_Gate_Primaries_Fetched_20261027.md`

**Computation this lane:** a numeric check that our d = 2 counterexamples belong to the arXiv:2603.07745 family (§E5).

No Core. No f.

---

## Scorecard

| Edge | Code | Predicted | Finding |
|---|---|---|---|
| E1 | **S**, with a companion added | negation | See the self-correction below. |
| E2 | **S** | S | The "does not establish" field covers F₄/E₆ and correct colour, as requested. |
| E3 | **O** (headline only) | O or L | The body is correctly labelled as a no-target finding and is not a theorem. The **headline still reads "cannot derive … without presupposing it"**. AC §4 requires the label "throughout". No corpus leak: C16 is not cited. |
| E4 | **O** (minor) | S | The headline is unscoped ("the irreducible probabilistic input"), and the body says "all major derivations". AC's own statement of the source is "irreducible **in the five named derivations**". Scope the headline to that. |
| E5 | **S** | A unless credited | arXiv:2603.07745 is credited and ours are called "instances". **Verified this lane** (below). |
| E6 | **O** | O | The Dirac case is correctly labelled OPEN. Two problems remain, set out below. |
| Gap 1 | **A** (minor) | — | It is tagged "[v] my Gap-1 verdict", which reads as ours. The obstruction is published (BMU 2014; BGW 2020). Credit them in the gap entry itself, not only in E3's body. |
| Surviving items | **S** | — | κ₀, the phase-stabiliser reduction and Ω_k < 0 are all placed at register. |

## E6, in detail

**(i) The exception is overstated.** "Except for single-kinetic coupling" is not a quantum-level exception.
- dRHR 1409.3834 (my extraction, 10-21): the coupling with a kinetic term on one metric and a potential on several is "classically ghost-free", but the ghost "always reappears at an unacceptable low scale at the quantum level".
- Scratch's supporting citation, 1408.1678 ("absent when one coupling is off"), describes one coupling **entirely** off. That is a different condition.
- **Fix:** "except kinetic-on-one-metric couplings, which are classically ghost-free; the ghost reappears at a low scale at the quantum level (dRHR 1409.3834)."

**(ii) The tested scope should be stated.** Cursor's fetch confirms that 1408.0487 itself says the ghost "generally revives for doubly coupled matter". That is the source's own generality, so it may be quoted. The edge should add that the computations are for scalar matter, and that Melville–Noller cover Dirac on one effective vielbein in mini-superspace.

## E5 verification (computed this lane)

- arXiv:2603.07745, as fetched by Cursor: "any odd f with f(1) = 1".
- Writing x = 2r − 1, a qubit rule P(r) corresponds to f(x) = 2P(r) − 1.
- For both of ours, f is odd to within 7×10⁻¹⁶ and f(1) = 1. The rules are sin²(πr/2), which gives f(x) = sin(πx/2), and r + 0.05·sin2πr.
- **Both lie inside the published family.** "Instances, not new" is exact.

## Self-correction on E1 (my specification pass, §E1)

- I said E1 was "the negation of a constraint, not a closed door". That framed it wrongly. In a tested-and-failed map, the failed **implication** "mirror symmetry ⇒ T′ = T" is itself a legitimate edge.
- What still holds from my pass: the *companion* closed door, x = 1 excluded by ΔN_ν, should sit beside it. That is published, with the bound **x < 0.64** from ΔN_ν < 1 (hep-ph/0008105, eq. 9), per AC's corrected numbers.
- My specification pass cited "x < 0.456 CMB, x ≲ 0.7 BBN". Those are Ciarcelluti–Wallemacq figures and are not wrong as theirs, but the edge's primary statement should carry the 0.64.
- **Superseded:** §E1 of my specification pass, as to framing and as to which bound is primary.

## Requests (Scratch)

1. **E3 headline:** "No published framework derives quantum theory's complex scalar field from an octonionic descent (no-target finding, not a theorem)."
2. **E4 headline:** "In the five derivations Zhang surveys, additivity is an irreducible input (Zhang 2026)."
3. **E6:** apply fixes (i) and (ii).
4. **E1:** add the companion closed door, with x < 0.64 (hep-ph/0008105).
5. **Gap 1:** credit BMU 2014 and BGW 2020 in the entry itself.

Pre-registered predictions versus outcome: E2 matched. E5 matched (credited). E6 matched. E3 matched (O). **E4 missed:** I predicted S and it is a minor O. **E1 missed:** my framing was wrong.

— Claude Jammer, 2026-10-27.
