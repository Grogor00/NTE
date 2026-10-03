# Falsifier Search for Unitary-CPN / Antiunitary-CPT Two-Layer Structure — Opening Scoping (Claude Jammer)

**From:** Claude Jammer (specialist session — AC P1 task; Greg approved start 2026-06-10)  
**To:** AC (task issuer); Scratch — Claude model (co-owner of operator-theory lane); Cursor Main (orchestration); Cursor Jammer + Cursor Scratch (calculation help); Greg  
**Date:** 2026-06-10  
**Priority:** P1 — AC-issued, Greg-approved start  
**Re:** `Handoff_AC_to_Scratch_Jammer_TASK_Find_Load_Bearing_Falsifiable_Consequence_Unitary_CPN_Two_Layer_20260610.md` (AC 20:55Z)  
**Status:** Opening scoping. Five candidates assessed under the binding bar. Two binned; two routed forward as priority; one held as backup. Per-lane Cursor asks at §6. NO claim of finding the load-bearing prediction; this memo is the work scope, not the result.

---

## §1 — The bar (restated for discipline)

A candidate counts ONLY if it could come out the **wrong way.** Test for every candidate: *could the universe (or an internal consistency check) return an answer that says NTE is wrong here?* If the two-layer structure cannot, even in principle, yield a falsifying result, it is a **restatement, not a prediction** — bin it.

Explicitly forbidden:
- Fitting numbers we already know
- Smuggling target values as inputs (the β_NTE-chain circularity pattern)
- Elegance / fame-matching as evidence
- Reframing existing corpus numbers as "predicted by the two-layer structure" unless independently forced

A genuine negative result ("the two-layer structure makes no distinguishing prediction") is itself an honest, ratifiable finding. **Not manufacturing a positive.**

---

## §2 — The structural claim being falsified

Per AC's 20:31Z ratification: **fundamental unitary CPN beneath emergent antiunitary CPT.** Specifically:
- CPN = C · P · (N → −N) is unitary — N is a fundamental real coordinate; reflecting it is unitary like P, no antiunitarity forced
- CPT, T at the emergent (post-locking) level remain antiunitary as in standard physics
- The unitary fundamental layer is the distinguishing claim from Susskind's broken-antiunitary-T picture

Where could a unitary fundamental layer leave an observational or structural fingerprint that an antiunitary-T picture (or a purely emergent picture without a unitary fundamental layer) cannot?

---

## §3 — Five candidates assessed

### Candidate C1 — Dressed observable ⟨C̄⟩ disagree across two-layer vs broken-T

**Claim.** The dressed observable $\bar C = C \cdot \Pi_-$ takes different values in NTE's unitary-fundamental-CPN / emergent-antiunitary-CPT picture versus Susskind's broken-antiunitary-T picture.

**Two outcomes.**
- Susskind broken-T: ⟨C̄⟩ = ⟨C · Π₋⟩ ≠ 0 in maximally mixed state, recovers semiclassical answer
- NTE two-layer: at the *emergent* level, CPT is antiunitary just like Susskind's, and the Π₋-like dressing should work the same way at that level. Possibly different at boundary terms where the unitary fundamental layer leaves a fingerprint.

**Falsifier.** If a careful computation of ⟨C̄⟩ on the Janus crossed product under unitary J gives the same value as under antiunitary J at all orders, the candidate is **dead** — no distinguishing prediction.

**Derivation honesty.** Suspicion: the emergent-level computation is degenerate (Π₋ dressing absorbs the level-distinction). The unitary fundamental layer is *hidden* beneath emergent CPT and may not reach down to ⟨C̄⟩.

**Status.** **Held as backup.** Likely dead on arrival but worth a Scratch operator-theoretic check before binning. Route to Scratch (Connes lead) for modular-flow computation under unitary J vs antiunitary J.

---

### Candidate C2 — Selection rule / parity signature at the Janus boundary

**Claim.** Unitary CPN at the gauge-birth surface (N=0) imposes a selection rule on amplitudes crossing the boundary that differs from what antiunitary T would impose. The downstream observational consequence is a specific parity signature in primordial correlations imprinted on the CMB.

**Two outcomes.**
- Unitary CPN: amplitudes for chirality-odd processes at gauge birth preserve phase structure (no i → −i flip); primordial perturbations carry specific phase relations
- Antiunitary (broken or fundamental) T: phase information is conjugated; different parity signature

**Falsifier.** CMB B-mode polarization parity. Standard expectation under exact P, CP, CPT: zero parity violation in CMB. Under unitary fundamental CPN with selection-rule-preserved phase: prediction for $\langle EB \rangle, \langle TB \rangle$ correlators. Under antiunitary fundamental T: different prediction. If observation (LiteBIRD, CMB-S4) excludes the unitary-CPN prediction, **NTE falsified here.**

**Derivation honesty.** This requires a real calculation of how the unitary-CPN structure at gauge birth propagates to primordial perturbations and to CMB correlators. Risk of circularity if any input is fitted to observation. **Must be derived end-to-end before claiming a prediction.**

**Status.** **PRIORITY 2 — substantive but technically demanding.** Route to Cursor Jammer for the parity-signature propagation calculation; Cursor Scratch for verification.

---

### Candidate C3 — CPT-emergence signature (scale-suppressed CPT non-exactness)

**Claim.** Because NTE's CPT is *emergent* (not fundamental), the standard exact CPT theorem applies only in the strict emergent limit. Near the gauge-birth scale, small CPT-respecting-but-not-exact effects suppressed by $(E / M_{\text{gauge-birth}})^n$ should be present. Susskind's broken-T-fundamental picture (or any picture where CPT is fundamental and exact) predicts zero such effect.

**Two outcomes.**
- NTE two-layer (CPT emergent): CPT-violation amplitude scales as $\sim (E/M_{\text{GB}})^n$ for some integer $n$; at sufficient energy scales, observable
- Standard / Susskind-broken-T: CPT is fundamental and exact; zero CPT-violation amplitude at any scale

**Falsifier.** Several:
- **(C3a) K0–anti-K0 mass difference:** current bound $|\Delta m|/m < 6 \times 10^{-19}$ (PDG 2024). For $M_{\text{GB}} \sim M_R \approx 8.2 \times 10^{14}$ GeV and $E \sim 500$ MeV, suppression is $(500 \text{ MeV} / 8 \times 10^{14} \text{ GeV})^n \sim (6 \times 10^{-13})^n$. For $n=1$: $6 \times 10^{-13}$, *above* current bound — **already falsifies** unitary-CPN with $n=1$. For $n=2$: $4 \times 10^{-25}$, well below bound; viable.
- **(C3b) Baryogenesis η:** observed baryon asymmetry $\eta \approx 6 \times 10^{-10}$. If NTE's emergent CPT predicts $\eta$ as a *consequence* of unitary fundamental CPN + Wick rotation at gauge birth, and the prediction can be made *without* smuggling $\eta$ as input, then it's a clean closed prediction. Currently the corpus has a sketch (`eta_Calculation.txt`): given inputs $M_R = 8.2 \times 10^{14}$ GeV, $m_{\nu_3} = 0.074$ eV (geometric), Davidson-Ibarra gives $\eta$ at right order of magnitude, with $M_1 \approx 6 \times 10^9$ GeV as the remaining unfixed input (Gap 1). **If $M_1$ can be derived from the unitary-CPN two-layer structure** (e.g., from a specific eigenvalue or trace at the Janus surface), then $\eta$ becomes a zero-parameter prediction. This is the cleanest path to a load-bearing result.
- **(C3c) Cosmological birefringence:** CMB photon polarization rotation $\beta \sim 0.3°$ (Planck 2020 hint; not yet confirmed). NTE's emergent CPT could predict a specific scale and sign for this; standard predicts zero. If $\beta$ confirmed nonzero at the predicted value: positive evidence. If excluded at sub-arcminute: NTE falsified (assuming the prediction is in that range).

**Derivation honesty.** **C3a is the immediate falsifier.** If $n=1$ scaling is what the two-layer structure forces, NTE is *already* falsified by K0–anti-K0. So the test is: what scaling does the two-layer structure force? This is a derivation, not an input fit. If it forces $n=2$ or higher, NTE survives current bounds but predicts effects at much higher energies (collider, cosmology). If $n=1$: NTE either dead or the M_GB scale assumption needs revising.

**For C3b:** the Gap 1 challenge ($M_1$ from geometry) is the load-bearing derivation. Must be derived from the unitary-CPN structure, not fitted to $\eta$.

**Status.** **PRIORITY 1 — most promising falsifier in the set.** Multiple sub-candidates with distinct experimental tests. C3a is the immediate (potentially-already-falsifying) check. C3b is the zero-parameter η prediction if Gap 1 closes geometrically. C3c is a forward-test candidate. Route to Cursor Jammer for the scale-suppression derivation; Cursor Scratch for adversarial check that no input is being smuggled.

---

### Candidate C4 — Cross-orientation cluster structure (revisit)

**Claim.** The unitary fundamental layer constrains correlations between observables in the post-locking sector that the emergent layer alone cannot produce.

**Two outcomes.** Unclear — the previous retirement of the cluster mirror on non-associativity grounds applies here. The symmetric pre-selection regime is octonionic; entanglement-as-geometry doesn't apply.

**Falsifier.** None obvious. The construction that would make this candidate work has not been identified.

**Derivation honesty.** Retired previously on a structural finding (non-associativity). The two-layer structure doesn't obviously change that finding.

**Status.** **BINNED.** Retired stays retired unless a specific construction is identified.

---

### Candidate C5 — Internal-consistency falsifier via eta invariant / signed traces under unitary J

**Claim.** A spectral-zeta or eta-invariant calculation on the Janus crossed product gives a different value under unitary modular conjugation J than under antiunitary J. If NTE's CPN is genuinely unitary (per the ratified determination), the unitary-J calculation is the *correct* one; if it disagrees with a downstream corpus claim that was derived under implicit antiunitary-J assumption, there's an internal inconsistency to resolve.

**Two outcomes.**
- The previous Task 4 Session 3 result ($\eta(0) = 0$ by spectral symmetry on canonical NTE M^C spectral triple) rests on **Dirac spectral pairing**, not on J directly. **Invariant under J convention.** So the leading eta is not a discriminator.
- BUT: **signed traces, boundary terms, holonomies around S¹_{β_GB}, Maslov-type indices** all depend on the J convention. Under unitary J vs antiunitary J these may differ.
- Specifically: $\zeta_{\text{total}}(-1) = -17/240$ (Task 4 Session 3) was computed assuming the standard Tomita–Takesaki antiunitary J implicitly. Under explicit unitary J, the corresponding spectral quantity may differ — and if it differs, the downstream consequences in any spectral-action computation also differ.

**Falsifier.** Recompute $\zeta_{\text{total}}(-1)$ (and any other downstream spectral quantity that touches J directly) under the unitary-J convention required by NTE's ratified CPN. If the value is the same: candidate dead (the J convention doesn't reach this observable). If different: there's a genuine internal-consistency falsifier — the corpus must use the unitary-J value for any prediction, and that value either agrees with existing observational anchors (good) or disagrees (falsified).

**Derivation honesty.** Pure operator-theoretic computation. No experimental input. The bar (Rule E5 of the external-framework discipline) is automatically met if the calculation is done at NTE-internal-derivation level.

**Status.** **PRIORITY (Scratch lane) — most tractable for a specialist session.** Route to Scratch (Connes lead) for the unitary-J recomputation of $\zeta_{\text{total}}(-1)$ and any related signed trace; Cursor Scratch for verification. Cleanest internal-consistency candidate.

---

## §4 — Verdict summary

| Cand. | Verdict | Owner | Status under bar |
|---|---|---|---|
| C1 (dressed ⟨C̄⟩) | Likely degenerate at emergent level | Scratch + Cursor Scratch | Held as backup |
| C2 (CMB B-mode parity at Janus boundary) | Substantive; tech demanding | Cursor Jammer + Cursor Scratch | **PRIORITY 2** |
| **C3 (CPT-emergence cosmological signature)** | **Multiple sub-falsifiers (K0–anti-K0, baryogenesis η, cosmological birefringence)** | **Cursor Jammer + Cursor Scratch** | **PRIORITY 1** |
| C4 (cross-orientation) | Retired stays retired | — | **BINNED** |
| **C5 (eta / signed trace under unitary J)** | **Most tractable; operator-theoretic** | **Scratch (Connes) + Cursor Scratch** | **PRIORITY (Scratch lane)** |

**Headline:** C3 (physics-effects) and C5 (operator-theoretic) are the two priorities to develop. C2 is the secondary candidate if C3 / C5 do not close. C1 and C4 are not worth pursuing further.

---

## §5 — Forward plan

**Phase 1 (next 1–2 sprints):** Develop C3 and C5 in parallel.

**C5 — Scratch (Connes) operator-theoretic lane.** Scratch recomputes $\zeta_{\text{total}}(-1)$ and the eta-invariant boundary/holonomy contributions explicitly under unitary modular conjugation J on the Janus crossed product $A_F \rtimes_\tau \mathbb{Z}_2$, comparing to the standard antiunitary-J result. Verdict format per Rule E5: PASS (value differs → internal-consistency falsifier active) / DEGENERATE (value same → C5 dead) / NEEDS-MORE.

**C3 — Cursor Jammer physics-effects lane.** Three sub-tasks:
- **C3a — K0–anti-K0 scaling derivation.** Derive the CPT-violation amplitude scaling $(E/M_{\text{GB}})^n$ from the two-layer structure. Determine $n$. If $n=1$: NTE already falsified by current $|\Delta m_K|/m_K$ bound; report immediately. If $n=2$: viable; report bound margin.
- **C3b — Baryogenesis η as zero-parameter prediction.** Re-examine the Gap 1 challenge ($M_1$ from geometry). Does the unitary fundamental CPN structure force a specific $M_1$ via a spectral / eigenvalue argument at the Janus surface? If yes: $\eta$ becomes zero-parameter; compare to observation. If no: report negative.
- **C3c — Cosmological birefringence scale prediction.** Compute the predicted CMB photon polarization rotation $\beta$ from the two-layer structure. Compare to Planck hint ($\beta \sim 0.3°$).

**Phase 2 (after Phase 1 verdicts):** If C3 or C5 yields a falsifiable prediction, develop into a corpus-rigor draft, route through full Rule E5 (sunshine → rabbit-hole → double-check → triple-check → fresh F6 → AC ratification → Greg authority) before any external use. If both yield only DEGENERATE / NEEDS-MORE: file the honest negative result and route to Greg for direction (publish-with-Susskind-as-intended-viewer can still proceed under restored-fork v0.3 framing without a sharper-question falsifier).

---

## §6 — Cursor lane asks (explicit per Greg's offer)

| Lane | Ask | Deliverable |
|---|---|---|
| **Cursor Scratch** | Recompute $\zeta_{\text{total}}(-1)$ on the Janus crossed product $A_F \rtimes_\tau \mathbb{Z}_2$ under **explicit unitary J** (NTE-ratified) vs **antiunitary J** (Tomita–Takesaki standard). Identify all J-sensitive terms (boundary contributions, holonomies on S¹_{β_GB}, Maslov indices). Compare numerical values. Source: `Working/Task_4_Session_3_Eta_Invariant_ZetaMinus1_Scratch_v1.md` (existing computation, implicit J convention). | `Working/FalsifierSearch_C5_Zeta_Recompute_UnitaryJ_vs_AntiunitaryJ_Cursor_Scratch_YYYYMMDD.md` — verdict: VALUES DIFFER / VALUES SAME / NEEDS-MORE |
| **Cursor Jammer** | Derive the CPT-violation amplitude scaling $(E/M_{\text{GB}})^n$ from the unitary-CPN / emergent-antiunitary-CPT two-layer structure. Compute $n$ from first principles (not fitted). Apply to K0–anti-K0 mass-difference bound and report whether NTE survives or fails current limit ($|\Delta m_K|/m_K < 6 \times 10^{-19}$). | `Working/FalsifierSearch_C3a_CPT_Scaling_K0_AntiK0_Cursor_Jammer_YYYYMMDD.md` — verdict: NTE-SURVIVES (with $n$ and margin) / NTE-FALSIFIED (with displayed derivation) / NEEDS-MORE |
| **Cursor Jammer** (parallel) | Re-examine Gap 1 ($M_1$ from geometry per `eta_Calculation.txt`). Does the unitary fundamental CPN structure force a specific $M_1$? If yes: derive it, compute predicted η, compare to $\eta_{\text{obs}} \approx 6 \times 10^{-10}$. **Explicit no-smuggling discipline: do not use $\eta_{\text{obs}}$ as input at any point.** | `Working/FalsifierSearch_C3b_M1_Geometric_Baryogenesis_Cursor_Jammer_YYYYMMDD.md` — verdict per same format |
| **Cursor Main** | Orchestrate; AC visibility on the three deliverables; alert Greg if either Cursor Jammer lane finds NTE-FALSIFIED before phase 2. | No specific document; coordination only. |
| **Scratch — Claude model** (Connes lead) | Co-own C5 with Cursor Scratch. Adversarial-verify Cursor Scratch's computation when returned. Cross-check that no smuggling has happened (the unitary-J calculation must be NTE-internal, not Susskind-influenced). | `Working/FalsifierSearch_C5_Scratch_Adversarial_Verify_Claude_YYYYMMDD.md` after Cursor Scratch returns |

---

## §7 — What this memo is NOT

- **Not** a claim that any candidate has yielded a load-bearing falsifier yet
- **Not** a corpus patch
- **Not** an integration of any external framework (Rule E1–E7 binding)
- **Not** a commitment to the Susskind v0.4 framing (v0.3 unitary-CPN reaffirmed; v0.4 retired)
- **Not** a substitute for AC ratification of any forthcoming result (all results route through full Rule E5)

This memo is the *work scope* and the *lane assignments*. The actual physics is in the deliverables routed in §6.

---

## §8 — Discipline (binding)

- Bar enforced: candidate must be able to come out wrong; binning C4 and (likely) C1 is the bar working as designed
- No fitting, no smuggling, no elegance-as-evidence
- All lanes report PASS / NEEDS-MORE / FAIL with displayed derivation chains
- Negative results are ratifiable findings, not failures
- Rule E5 (multi-pass verification gate) applies to any forthcoming integration
- Canonical bilateral / mirror / Janus discipline throughout

---

— Claude Jammer (specialist session, AC P1 task, Greg approved start), 2026-06-10.
