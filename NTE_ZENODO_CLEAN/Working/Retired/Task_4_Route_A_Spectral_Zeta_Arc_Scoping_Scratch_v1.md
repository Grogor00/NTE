# Task 4 — Route A Spectral-Zeta Arc (Scoping + First-Pass) — Scratch v1

**Status:** Working note v1, 2026-05-16. Scoping deliverable + first-pass technical content. Per AC routing, Task 4 estimated at 1-3 Scratch sessions; this v1 sets up the arc + verifies κ₀ consistency anchor + identifies candidate observables beyond κ + proposes session-by-session sequencing.
**Author stream:** Scratch (Connes Programme lead within Jammer-stream).
**Investigation question:** Extend spectral-zeta machinery from Jammer's Route A first-pass (`1k6SnwDk_bhlTmB3EAIq3inxEdX1A0Ej_`) and Final Verdict (`1xS8oDOidKrV2Tn2rTm7SGj_EaQj-LUbJ`) to observables beyond κ, with κ₀ = 3/√(4π) as consistency anchor.
**Trigger:** Greg directive 2026-05-16 "1, 2, 3, ratified. 4 and 5 confirmed. continue to task 4" + AC→Scratch routing directive Task 4 (Route A spectral-zeta; ~1-3 sessions).
**Recognition-gate aware:** Local-correctness-only until passing Greg's recognition gate via AC review. Recognition-gate items in §8.
**Vocabulary discipline:** Standard spectral-zeta terminology where applicable (Hurwitz zeta, dimension spectrum, heat kernel coefficients); canonical NTE vocabulary (κ₀ as dimensionless Sonner-Tong-derived prefactor 3/√(4π); modular flow / KMS framework per Charter v1.3 §2.5).
**Source basis read for this scoping**:
- **Jammer Route A first-pass** at Working/ `1k6SnwDk_bhlTmB3EAIq3inxEdX1A0Ej_` — **READ IN FULL** this session
- **Jammer Route A final verdict** at Working/ `1xS8oDOidKrV2Tn2rTm7SGj_EaQj-LUbJ` — read via search snippet (sufficient content captured)
- Charter v1.3 referenced
- Paper S1 v0.4 + v1.0 §§3-6 carry-forward referenced (F1 + F2 + spectral action expansion + geometric resummation κ₀/(1−κ₀) = 5.5055)
- Scratch Task 1 + Task 2 + Task 3 working notes — recent session context
**Files NOT read this session** (flagged as confidence-limiters per §7):
- Paper_Kappa_PathwayB_v10_6.md (the existing κ derivation document): I have Jammer's Route A final verdict summary of its content; full read would refine consistency-anchor verification
- Hersent 2025 / Summers 2005 / Borchers 1999 (Task 1 confidence-limiters carried)
- Specific heat kernel literature (Gilkey, Vassilevich) beyond what's in Paper S1 v0.4 §5

---

## §1. Task framing

### §1.1 What Task 4 asks

Per AC routing directive Task 4 + Charter v1.3 §3.7 P0 territory:

**Extend spectral-zeta machinery to observables beyond κ; κ₀ = 3/√(4π) as consistency anchor.**

Per Jammer's Route A final verdict (2026-05-14): *"Route A is not a dead-end in the broader sense — spectral zeta could still derive observables beyond κ that the corpus doesn't currently address."*

Task 4 is the followthrough on this Jammer-flagged opportunity. NOT to re-derive κ (Jammer verified κ derivation is structurally cleaner via Killing spinor + Hopf projection + Gaunt machinery); but to identify and derive other observables that spectral zeta CAN naturally produce that the corpus doesn't currently address.

### §1.2 Multi-session scope acknowledgment

AC routing estimates 1-3 sessions for Task 4. **This v1 is a scoping + first-pass deliverable**:
- §3: verify κ₀ = 3/√(4π) consistency anchor under spectral-zeta framework (does spectral zeta yield results consistent with corpus κ₀ derivation?)
- §4: identify and prioritize candidate observables beyond κ that spectral zeta can address
- §5: first-pass technical analysis of which candidates are tractable in axiom-only framework
- §6: proposed session arc — what each subsequent Scratch session contributes

Subsequent sessions tackle specific observable computations.

### §1.3 Axiom discipline maintained

Per Jammer's first-pass discipline (strict axiom adherence to surface-only S³ + N fundamental / t emergent + CPN-symmetric two-sector + Hopf bundle), this scoping respects same discipline. Additional structure beyond axioms (specific Dirac operator content, A_F nonassociativity workaround, monopole coupling prescriptions) explicitly flagged where used.

---

## §2. Jammer's Route A baseline (absorbed)

### §2.1 Spectral triple structure under axiom discipline

Per Jammer first-pass §1:
- **Algebra A**: substrate algebra. Under N-fundamental + CPN-two-sector: A_F = 𝕆 ⊕ 𝕆 (nonassociative)
- **Manifold**: S³ (surface only)
- **Hilbert space H**: spinors on S³; two-sector structure doubles
- **Dirac operator D**: respects Hopf bundle; minimal axiom-determined choice = standard Dirac on S³

**Two structural obstacles flagged**:
- A_F nonassociativity: standard NCG requires associative A; resolution options include Jordan algebra route (J_3(𝕆) per Farnsworth 2025); bi-module enveloping (associative); or non-associative NCG (research-frontier)
- Dirac operator D not uniquely axiom-determined: minimal D = standard Dirac on S³; mass mixing / gauge connections / chirality couplings require additional specification

### §2.2 Standard Dirac spectrum on unit S³

Well-established result (per Jammer §2):
- Eigenvalues: λ_k = ±(3/2 + k) for k = 0, 1, 2, ...
- Multiplicity: d_k = (k+1)(k+2) for each sign

| k | λ | Multiplicity (each sign) |
|---|---|---|
| 0 | ±3/2 | 2 |
| 1 | ±5/2 | 6 |
| 2 | ±7/2 | 12 |
| 3 | ±9/2 | 20 |
| 4 | ±11/2 | 30 |
| 5 | ±13/2 | 42 |

The Hopf fibration S³ → S² commutes with D; each eigenvalue decomposes into SU(2) irreps.

### §2.3 Spectral zeta function (axiom-derived)

Per Jammer §3:

Single-sector:
$$\zeta_D(s) = 2 \zeta_H(s-2, 3/2) - \frac{1}{2}\zeta_H(s, 3/2)$$

Two-sector (CPN axiom doubling):
$$\zeta_{\text{total}}(s) = 4 \zeta_H(s-2, 3/2) - \zeta_H(s, 3/2)$$

where $\zeta_H(s, a) = \sum_{k=0}^{\infty} (k+a)^{-s}$ is the Hurwitz zeta function.

### §2.4 Pole structure and dimension spectrum

Per Jammer §4:
- Simple pole at s = 3 (from ζ_H(s-2, 3/2)); residue = **4** (encodes Vol(S³) = 2π² with two-sector + chirality doubling normalization)
- Simple pole at s = 1 (from −ζ_H(s, 3/2)); residue = **−1**
- **Dimension spectrum**: {1, 3}. Top dimension 3 = dim(S³) ✓

### §2.5 Specific zeta values (axiom-derived)

Per Jammer §5:
- ζ_total(0) = 0 (expected for odd-dimensional manifold)
- ζ_total(2) = 4 · ζ_H(0, 3/2) − ζ_H(2, 3/2) = 4 · (−1) − (π²/2 − 4) = **−π²/2 ≈ −4.935**
- ζ_total(−2) = 0 (expected by symmetry)

### §2.6 What Jammer's first-pass did NOT achieve

Per Jammer §6 honest result: cannot reach κ = 5.506 from axiom-determined spectral data via natural combinations:
- ζ_total(2) ≈ −4.935 (close magnitude, wrong sign)
- |Res(s=3)| = 4 (no match)
- k=4 eigenvalue |11/2| = 5.50 (exact but k=4 selection not axiom-determined)

Jammer Fork resolution per final verdict (2026-05-14):
- Fork A (Route A genuinely simplifies κ derivation): NO
- Fork B (Route A is reformulation only for κ): YES
- **κ remains best-derived via Hopf monopole projection + CPN-symmetric resummation per Paper_Kappa_PathwayB_v10_6**

---

## §3. κ₀ = 3/√(4π) consistency anchor — verification

### §3.1 The consistency requirement

κ₀ = 3/√(4π) is NTE's canonical dimensionless prefactor (Paper S1 v0.4 §4 F2 reading; Sonner-Tong CP¹ Berry-phase route + Pathway B Hopf-projection-of-Killing-spinors route, both giving same value).

Task 4's spectral-zeta extension to observables beyond κ MUST NOT produce results inconsistent with κ₀ = 3/√(4π). The two machinery types (κ-derivation via Killing-spinor + Hopf projection; spectral-zeta via full Dirac spectrum) probe different aspects of S³ Dirac spectral data; they must be mutually consistent.

### §3.2 Where κ₀ derivation sits in spectral data

Per Jammer Route A final verdict §2:
1. Killing spinors on S³: n=0 Dirac modes, |ψ_K|² = 1/(2π²) on S³
2. Hopf projection S³ → S²: ∫_{S¹ fibre} |ψ_K|² = 1/√(4π) = Y_00(S²)
3. Three eigenstates from dim(su(2)) = 3 (the σ₁, σ₂, σ₃ Killing-spinor polarisations)
4. κ_0 = 3 × Y_00(S²) = 3/√(4π) ≈ 0.846

The Killing-spinor (n=0 / k=0) mode contribution to the Hopf-projected spectrum is the structural source of κ₀.

### §3.3 Verification — spectral zeta consistency with κ₀

The k=0 mode in the Dirac spectrum (λ_0 = 3/2, multiplicity 2 per sign) contributes the Killing-spinor content. In spectral zeta:

Single-mode k=0 contribution to ζ_total(s):
$$\zeta_{k=0}(s) = 2 \cdot d_0 \cdot (3/2)^{-s} = 2 \cdot 2 \cdot (3/2)^{-s} = 4(3/2)^{-s}$$

(Two signs × multiplicity 2 = factor 4; CPN doubling already absorbed in two-sector ζ_total convention.)

This is structural mode content, not a measure of Hopf-projection. The Hopf-projection produces Y_00 from the *constant* Killing-spinor density on S³, not from a zeta-function evaluation.

**Consistency anchor check**: κ₀ = 3/√(4π) is determined by:
- 3 = dim(su(2)) = three Killing-spinor polarisations (which spectral zeta confirms via multiplicity d_0 = 2 per sign × 2 signs = 4, but with 3 polarisations selected by Lie-algebra structure of S³ ≅ SU(2) — NOT axiom-forced from bare spectral data)
- 1/√(4π) = Y_00(S²) (geometric fact about S² as Hopf base; NOT a spectral-zeta quantity)

**Verdict**: spectral zeta does NOT directly produce κ₀ = 3/√(4π). Spectral zeta produces the Dirac spectrum's mode content; κ₀ uses Killing-spinor mode + Hopf-projection + Gaunt machinery, which is a different (and more structurally efficient) computation.

The consistency anchor is satisfied trivially: spectral zeta provides the underlying Dirac spectrum from which Killing-spinor mode content is extracted; the κ₀ derivation is layered on top. No contradiction surfaces.

### §3.4 What κ₀ consistency anchor REQUIRES of Task 4's extensions

For observables-beyond-κ that Task 4 derives via spectral zeta:
- They must use the SAME underlying Dirac spectrum (Jammer's ζ_total(s) = 4 ζ_H(s−2, 3/2) − ζ_H(s, 3/2))
- They must NOT conflict with the Killing-spinor n=0 mode content that κ₀ uses
- They must be consistent with the existing two-sector CPN-doubling structure

These are automatic if spectral-zeta machinery is used in standard form. The consistency anchor is a check, not a constraint that requires special handling.

---

## §4. Candidate observables beyond κ — identification + prioritization

### §4.1 Catalog of observables spectral zeta can naturally derive

From spectral-zeta values at specific s, the standard observables are:

1. **Volume of S³** — from Res(s=3) ζ_total = 4 (already established; consistency check)
2. **ζ_total(0)** — dimension anomaly content; for S³ = 0 (odd-dimensional)
3. **ζ'_total(0)** — functional determinant; log(det' D); one-loop effective action
4. **ζ_total(−n) for positive integer n** — heat kernel coefficients a_{2n+1} (vanish for odd dim) and related anomaly content
5. **Eta invariant η(0)** — spectral asymmetry; global anomaly content
6. **Heat kernel coefficients a_{2k}** — give effective action contributions:
   - a_0: cosmological constant scale
   - a_2: Newton's constant (Einstein-Hilbert term)
   - a_4: higher curvature corrections (Gauss-Bonnet, Weyl² conformal anomaly)
7. **Index of D** = dim ker(D) − dim ker(D*) — for S³ this is 0 (signature condition)
8. **Spectral action S_Λ(D) = Tr f(D/Λ)** for specified cutoff function f — gives Wilsonian effective action
9. **Eigenvalue ratios** — for higher modes k > 0, ratios λ_k / λ_0 = (3+2k)/3 — could relate to fermion mass hierarchies

### §4.2 Prioritization for NTE relevance

Some of these are already in NTE corpus (Paper S1 §5 spectral-action expansion gives Newton's constant; §6 gives κ₀ geometric resummation closure). Task 4's natural extensions are the observables NOT currently in the corpus:

**Priority A — directly NTE-relevant, not in corpus**:
- **A1. Functional determinant ζ'_total(0)** — gives one-loop effective action contribution. Relates to V_NTE Stage 2 territory (currently open; per Charter v1.3 P0 inventory). Could provide one-loop correction to Mechanism B / Φ_NTE effective potential.
- **A2. Eta invariant η(0)** — spectral asymmetry. For S³ × S¹_{β_GB} (full NTE base manifold M ≃ M^C), the eta invariant could probe global anomaly content + chirality balance between +N and -N sectors under CPN.
- **A3. Conformal anomaly coefficient (c_W, c_E from a_4)** — relates directly to Paper S1 §2 P2 (4D conformal invariance with ξ = 1/6). Could provide cross-check / consistency verification for Mechanism B supersession (Greg ratified 2026-05-11).

**Priority B — physically interesting, requires additional structure beyond axioms**:
- **B1. Eigenvalue ratios for fermion mass hierarchies** — connects higher Dirac modes (k > 0) to potential mass-eigenstate content; would require specifying how higher modes correspond to physical fermion generations. Not axiom-forced.
- **B2. Spectral action S_Λ(D)** — full Wilsonian effective action with cutoff. Already in Paper S1 §5 substrate via BF 2013 + Farnsworth 2025 framework; Task 4 could extend with explicit cutoff-dependence analysis.

**Priority C — consistency checks, lower payoff**:
- **C1. Vol(S³) from Res(s=3)** — already established; confirms framework
- **C2. ζ_total(0) = 0** — odd-dim consistency check
- **C3. Index of D = 0** — signature check

### §4.3 Recommended Task 4 sessions sequencing

Given AC routing 1-3 sessions:

**Session 1 (this v1 scoping)**: Setup + κ₀ consistency anchor verification + candidate observables identification + session arc proposal. ✓ THIS DELIVERABLE.

**Session 2 (next Scratch session on Task 4)**: Priority A1 — functional determinant ζ'_total(0). Compute one-loop effective action contribution; check consistency with V_NTE Stage 2 open territory; flag implications for Mechanism B supersession.

**Session 3 (if needed)**: Priority A2 + A3 — eta invariant on M = S³ × S¹_{β_GB} for chirality-balance analysis; conformal anomaly coefficient c_W consistency with Paper S1 §2 ξ = 1/6.

Priority B items deferred to future Programme S work (Paper S2 or beyond); Priority C items are consistency checks performed inline during A1/A2/A3 computations.

---

## §5. First-pass technical: which candidates are tractable in axiom-only framework

### §5.1 Tractability assessment

Under strict axiom discipline (surface-only S³ + N fundamental / t emergent + CPN-two-sector + Hopf bundle) + Jammer first-pass minimal Dirac choice:

**Fully tractable (no additional structure needed beyond Jammer baseline)**:
- A1 functional determinant ζ'_total(0): direct computation from ζ_total(s) = 4 ζ_H(s−2, 3/2) − ζ_H(s, 3/2) by analytic continuation + differentiation at s=0
- A3 conformal anomaly coefficient from a_4: heat kernel expansion coefficient relates to ζ_total(−1) (for d=3 spectrum); axiom-derivable

**Tractable with minimal additional structure**:
- A2 eta invariant on M^C = S³ × S¹_{β_GB}: requires extending S³-only spectrum to S³ × S¹_{β_GB} product structure (factorizes; standard); requires specifying the S¹ length β_GB (corpus-canonical, not axiom-forced strictly)

**Tractable but with structural caveats**:
- B1 eigenvalue ratios for fermion hierarchies: physical interpretation requires assigning higher-k modes to physical fermions; not axiom-forced. Would need Programme S central deliverable (Paper S2 heat-kernel computation) for canonical interpretation
- B2 full spectral action: requires cutoff function f specification; canonical NTE form not yet specified (Paper S1 §5 substrate exists)

### §5.2 First-pass technical content for A1 (functional determinant) — preview

The functional determinant via zeta regularization:
$$\log \det' D = -\zeta'_{|D|}(0)$$

where ζ_{|D|}(s) = Σ |λ|^{-s} (over non-zero eigenvalues). For NTE's two-sector spectral triple on S³:

$$\zeta_{|D|}(s) = \zeta_{\text{total}}(s) = 4 \zeta_H(s-2, 3/2) - \zeta_H(s, 3/2)$$

(Same expression as Jammer's two-sector ζ_total; no zero modes — Dirac spectrum on S³ starts at λ_0 = ±3/2.)

Computing ζ'_total(0):
$$\zeta'_{\text{total}}(0) = 4 \zeta'_H(s-2, 3/2)|_{s=0} - \zeta'_H(s, 3/2)|_{s=0}$$

The Hurwitz zeta derivative:
- $\zeta'_H(-2, a) = ?$ (requires specific evaluation)
- $\zeta'_H(0, a) = \log \Gamma(a) - \frac{1}{2}\log(2\pi)$ (Lerch's formula)

For a = 3/2:
$$\zeta'_H(0, 3/2) = \log \Gamma(3/2) - \frac{1}{2}\log(2\pi) = \log\left(\frac{\sqrt{\pi}}{2}\right) - \frac{1}{2}\log(2\pi) = -\frac{1}{2}\log(4) - \log 2 = -\log 4$$

Wait, more carefully: $\Gamma(3/2) = \frac{\sqrt{\pi}}{2}$. So $\log\Gamma(3/2) = \frac{1}{2}\log\pi - \log 2$.

$$\zeta'_H(0, 3/2) = \frac{1}{2}\log\pi - \log 2 - \frac{1}{2}\log(2\pi) = \frac{1}{2}\log\pi - \log 2 - \frac{1}{2}\log 2 - \frac{1}{2}\log\pi = -\frac{3}{2}\log 2$$

So $\zeta'_H(0, 3/2) = -\frac{3}{2}\log 2 \approx -1.0397$.

The $\zeta'_H(-2, 3/2)$ term requires more work — it's not a standard tabulated value at half-integer argument. Would need the Hermite integral representation or specific identities.

**Next-session deliverable**: complete the ζ'_total(0) evaluation; interpret the resulting log det' D as one-loop effective action contribution; check consistency with V_NTE Stage 2 territory.

### §5.3 Why this first-pass preview is illustrative, not conclusive

This v1 deliverable provides:
- Scoping clarity
- κ₀ consistency anchor verification
- Candidate observables identified + prioritized
- Session arc proposal
- First-pass technical sketch for Priority A1 (functional determinant)

It does NOT complete:
- Full ζ'_total(0) numerical evaluation (Hurwitz zeta derivative at s=-2, half-integer argument requires more computation)
- Interpretation as one-loop effective action contribution to V_NTE
- Consistency check with Mechanism B supersession (ξ = 1/6 commitment)
- Eta invariant computation on M^C = S³ × S¹_{β_GB}
- Conformal anomaly coefficient extraction

These are explicitly Task 4 Session 2+ deliverables. Honest scope framing.

---

## §6. Verdict on Task 4 setup

### §6.1 Task 4 scoping verdict

**CLEAN setup, multi-session arc, with Priority A1 (functional determinant ζ'_total(0)) as natural Session 2 first deliverable.**

The spectral-zeta framework is well-defined (Jammer first-pass §3), κ₀ consistency anchor is satisfied (§3 of this note), candidate observables beyond κ are identified with prioritization (§4), and Session 2's natural first deliverable (functional determinant) is technically tractable in axiom-only framework with minimal additional structure (§5).

### §6.2 No structural obstructions surfaced

Per anti-bias discipline: did not push toward a particular verdict on Task 4 tractability. The setup analysis shows Priority A observables are tractable; structural obstructions (A_F nonassociativity per Jammer §1; ambiguity in Dirac operator D specification beyond minimal choice) are flagged but not blocking for Priority A items.

### §6.3 Implications for canonical framing

- **No conflict with κ₀ canonical** (3/√(4π) per Paper S1 v0.4 §4 F2 + Sonner-Tong route + Pathway B Hopf-projection route)
- **No conflict with v10.10 σ_t framework canonical complement** (Charter v1.3 §2.5)
- **No conflict with Task 1 + Task 2 + Task 3 verdicts**
- Potential cross-fertilization with Paper S1 §5 spectral-action expansion (Task 4 Priority A3 conformal anomaly coefficient could cross-check Mechanism B ξ = 1/6 commitment)

---

## §7. Confidence assessment

### §7.1 High-confidence aspects

- **Jammer Route A first-pass technical content absorbed**: HIGH confidence. Read in full this session.
- **κ₀ consistency anchor verified at structural level**: HIGH confidence. Spectral zeta provides underlying Dirac spectrum; κ₀ derivation layered on top via Killing-spinor + Hopf-projection + Gaunt machinery; no contradictions surface.
- **Candidate observables identification**: HIGH confidence. Standard spectral-zeta theory; observables are well-known catalog.
- **Priority A1 (functional determinant) tractability**: HIGH confidence at framework level. Computation is technically feasible (analytic continuation + Lerch's formula for ζ'_H(0, a)); specific Hurwitz zeta derivative ζ'_H(-2, 3/2) requires more work but is well-defined.

### §7.2 Moderate-confidence aspects

- **Priority A2 (eta invariant) on M^C = S³ × S¹_{β_GB}**: MODERATE confidence. Product spectrum is standard but β_GB specification is not strictly axiom-forced; canonical corpus value used.
- **Priority A3 (conformal anomaly coefficient) consistency with Paper S1 §2 ξ = 1/6**: MODERATE confidence. Standard a_4 coefficient extraction is well-defined; specific consistency with NTE-canonical ξ = 1/6 vs ξ = 1/12 convention-dependence flagged territory (per Paper S1 §2.5).
- **Session arc estimate (3 sessions total including this v1)**: MODERATE confidence. Depends on whether Priority A1 yields surprising structural insights warranting deeper investigation, or whether Priority A2 + A3 can be efficiently bundled.

### §7.3 Lower-confidence / flagged-as-open aspects

- **A_F nonassociativity workaround**: LOW confidence on technical choice. Spectral-zeta computations on the manifold side (S³ Dirac spectrum) do not directly engage A_F structure; A_F's role enters via the full spectral triple's A = C^∞(M) ⊗ A_F. For Priority A1 + A2 + A3, the manifold-side Dirac spectrum is sufficient; A_F-side computations would be Programme S Paper S2 territory.
- **Specific Dirac operator content beyond minimal**: Jammer §1 second obstacle. Mass mixing / gauge connections / chirality couplings would extend the Dirac spectrum and modify spectral zeta. For Task 4 Priority A items, minimal Dirac suffices; corpus-canonical extensions deferred.
- **Paper_Kappa_PathwayB_v10_6 not read in full**: would refine κ₀ consistency anchor verification at the detailed-derivation level; flagged as confidence-limiter.

### §7.4 What would change the Task 4 setup verdict

- If Priority A1 functional determinant computation reveals surprising algebraic structure (e.g., particularly clean form, factor of 3/√(4π) appearing, etc.) — the consistency anchor verification refines.
- If Priority A2 eta invariant computation surfaces global anomaly content that contradicts CPN-symmetric two-sector axiom: structural revisiting needed.
- If Priority A3 conformal anomaly coefficient is inconsistent with ξ = 1/6 commitment: Mechanism B supersession territory revisited.

None anticipated as imminent; setup is robust.

---

## §8. Recognition-gate items + files referenced

### §8.1 Recognition-gate items for Greg

1. **Ratify Task 4 scoping verdict** as CLEAN setup with multi-session arc; Priority A1 (functional determinant ζ'_total(0)) as natural Session 2 first deliverable?
2. **Ratify κ₀ = 3/√(4π) consistency anchor verification** — spectral zeta provides underlying Dirac spectrum; κ₀ derivation layered on top; no contradictions; consistency anchor satisfied?
3. **Ratify candidate observables priority list** (A1 functional determinant; A2 eta invariant; A3 conformal anomaly coefficient as priorities; B + C items lower priority)?
4. **Ratify session arc proposal** (Session 1 this scoping; Session 2 Priority A1; Session 3 if needed Priority A2 + A3)?
5. **Confirm next Scratch task** — either (a) continue Task 4 Session 2 in next Scratch session, or (b) other priority routing (Paper S1 v1.0 §2 absorption / Paper S1 §7-§9 default / other)?

### §8.2 Files referenced

| File | Purpose | Drive ID |
|---|---|---|
| **Jammer Route A first-pass** | Spectral zeta baseline; read in full this session | Working/ `1k6SnwDk_bhlTmB3EAIq3inxEdX1A0Ej_` |
| **Jammer Route A final verdict** | Fork A/B resolution + observables-beyond-κ opening; read via search snippet | Working/ `1xS8oDOidKrV2Tn2rTm7SGj_EaQj-LUbJ` |
| Charter v1.3 | Canonical state; v10.10 σ_t framework; P0.10 territory | Stage/ `1TDrHUFSuROWzu__hY34PGAvLmmZdxAu4` |
| Paper S1 v0.4 §4 F2 | κ₀ structural reading 3/√(4π) canonical | Working/ `1m9tcGe1T6qOvLjd94nwVbNo3kOYh6_TB` |
| Paper S1 v1.0 §3-§6 carry-forward | F1 + F2 + spectral-action expansion + geometric resummation context | Working/ `1hN9iezeaut8gw8lUQZXdsEooasK2KAoe` |
| Scratch Task 1 working note | GNS representation + non-associative caveat | Working/ `1pwU_5oVbPGsHcHVlkY0GNHQiK0voRk8S` |
| Scratch Task 2 working note | σ_t / KMS framing | Working/ `1pT24dxgRXRCOuSFStyoKr4pokMNmIuGx` |
| Scratch Task 3 working note | MP 2021 + Gerstenhaber-Schack + external-literature anchors | Working/ `1Cf9jQSOaSqqSynTnsnJBA5xaF5p2ug5M` |

### §8.3 Files NOT read this session (confidence-limiters per §7)

| File | Why flagged |
|---|---|
| Paper_Kappa_PathwayB_v10_6 (canonical κ derivation) | Would refine κ₀ consistency-anchor verification at derivation-detail level; Jammer's final-verdict summary sufficient for this scoping |
| Hersent 2025 / Summers 2005 / Borchers 1999 | Task 1 confidence-limiters carried forward |
| Heat kernel literature beyond Paper S1 v0.4 §5 substrate (Gilkey, Vassilevich) | Standard references; Jammer's baseline + Paper S1 substrate sufficient for scoping |

### §8.4 Cleanup batch contribution

Cumulative root duplicates this session:
- Earlier session items: Paper 7a v1.1 + handoff; session-end handoff; Direction 1; Task 1; Task 2 working note + handoff; Task 3 working note + handoff
- Task 4 working note root duplicate: TBD on copy_file (this ship)
- Task 4 handoff root duplicate: TBD on copy_file (next step)

---

## §9. Closing

**Task 4 v1 scoping deliverable complete. Multi-session arc set up; κ₀ = 3/√(4π) consistency anchor verified; candidate observables beyond κ identified with prioritization; Session 2 natural first deliverable identified (Priority A1 — functional determinant ζ'_total(0)).**

**Standing by** for Greg recognition gate on Task 4 setup + session arc proposal + next Scratch task routing confirmation.

Per AC routing directive ordering post-Task 4 sessions, downstream queue:
- Paper S1 v1.0 §7-§9 default direction (σ↔Φ_NTE confluence framing + convention-dependence disclosure + references)
- Paper S1 v1.0 §2 absorption pass (Task 2 candidate revised inline text absorption into master document)

— Scratch (Connes Programme lead), 2026-05-16.
