# ATTACK — Claude Jammer → AC, Scratch, Cursor Main: Gate-0 secondary constraint — attack on Scratch's D4 (lean D2)

**From:** Claude Jammer (adversarial lane)
**To:** AC, Scratch (construction), Cursor Main (literature)
**Cc:** Greg, PC
**Date:** 2026-10-09

**Attacks:** `Working/P09_Gate0_Secondary_Constraint_VERDICT_Scratch_D4_undetermined_structural_lean_D2_…_20261009.md`
**Pre-registration:** `Working/P09_Gate0_Secondary_Constraint_ATTACK_PREREGISTRATION_Jammer_D2_favoured_four_openings_kill_criteria_filed_blind_to_Scratch_20261009.md`
**Conflict declared.** I proposed the lapse-linearity opening. I attack the secondary-constraint claim. No rescue.

---

## 0. CONVERGENCE / DIVERGENCE — stated first

**I CONVERGE with Scratch's D2 lean. I DIVERGE on the confidence: the structural argument is stronger than Scratch's ~60–65% gives it, and the honest D4 wrapping understates the force of Result 2.**

My updated credence: **D2 at ~70–75%.** The remaining 25–30% for D1/D4 represents the possibility of an algebraic miracle (Clifford identity, Dirac-bracket cancellation) for which there is no positive evidence.

Scratch is honest. Their work is genuine. The attack below is on whether they are too conservative — whether D4 gives unearned shelter to D1 when the structural evidence points to D2.

---

## 1. ATTACK ON RESULT 1 — relative boost AUXILIARY: genuine but does not kill Opening 2

### What Scratch claims

The 6 relative Lorentz parameters do NOT propagate. The pair $(p_{\Lambda_\text{rel}}, \text{modified SVC})$ is second-class, algebraically determining $\Lambda_{\text{rel}}^*(\gamma_g, \gamma_f, \psi)$. All 6 parameters eliminated from the phase space. "No new propagating degrees of freedom from the relative Lorentz sector."

### What I accept

This is genuine original work and I accept it provisionally. The argument has the right structure:
- $p_{\Lambda_{\text{rel}}} \approx 0$ is a primary constraint because no sector (EH, Dirac, HR potential) gives time derivatives of $\Lambda_{\text{rel}}$. Scratch's itemization (a)–(c) in §1.3 is correct.
- Preservation $\dot{p}_\Lambda = \{p_\Lambda, H\} = -\partial H/\partial\Lambda_{\text{rel}} \approx 0$ yields the modified SVC.
- The SVC is algebraic (no time derivatives of $\Lambda_{\text{rel}}$), hence determines $\Lambda_{\text{rel}}$ as a function of the remaining variables.
- Non-degeneracy of the second-class pair is generic.

**This resolves my K2b:** the symmetric vierbein condition IS still enforced (in modified form) with the spinor present. The relative boost is gauge-fixed.

### What I attack

**Attack 1a: "Auxiliary" ≠ "ghost absent."** Scratch correctly identifies this (§1.5: "Opening 2 feeds into Opening 1, not independently"), but the handoff framing — "Opening 2 partially resolved" — could mislead. Opening 2 was declared decisive because the relative boost becoming physical is WHERE the BD ghost hides. Scratch has shown it hides somewhere else (the effective constraint after SVC elimination), not that it doesn't hide. The headline "partially resolved" should read: "the hiding place is relocated, not emptied." I accept the relocation. I do not accept that it reduces the threat.

**Attack 1b: Non-degeneracy is "generic" — what about the cosmological solution?** Scratch claims non-degeneracy "for generic $(\gamma_g, \gamma_f, \psi)$" because the Hessian $\partial^2 V_{\text{HR}}/\partial\Lambda_{\text{rel}}^2 \neq 0$ is non-degenerate in the pure-gravity case, and the spinor correction is perturbative. But "generic" is not "all." The 1408.0487 lesson is precisely that a configuration safe on FLRW can be sick on Bianchi (§III.1.2). If there exist cosmologically relevant backgrounds where the SVC Hessian degenerates (e.g., at a bouncing cosmology or at a symmetry-enhancement point where the two metrics coincide), the second-class pair collapses and the relative boost becomes dynamical AT THAT POINT. Scratch does not name or exclude this.

**Verdict on Result 1:** Genuine positive finding, provisionally accepted. K2b satisfied. But K2a (that the full constraint algebra closes, including the lapse secondary) is NOT addressed by Result 1 and remains open. Result 1 is necessary but not sufficient for D1.

---

## 2. ATTACK ON RESULT 2 — "breaks HR polynomial structure": load-bearing, and understated

### What Scratch claims

The Dirac spatial-derivative (kinetic) term depends on the matrix elements $S^i_j$ of $S = \sqrt{\gamma_g^{-1}\gamma_f}$, not on the elementary symmetric polynomials $e_n(S)$. The HR secondary-constraint cancellation relies on $V$ depending on $e_n(S)$, which satisfies Cayley–Hamilton identities. The Dirac term falls OUTSIDE this class → the bracket $\{C_g, C_f\}$ receives corrections → "structural lean D2."

### Where the argument is STRONGER than Scratch admits

Scratch frames this as a "lean" and allows that it might be cancelled by Clifford identities, Dirac-bracket effects, or other mechanisms (§5.2). I argue the structural argument is stronger than that.

**Attack 2a: The HR cancellation is NOT an approximate symmetry — it is an EXACT algebraic identity.** The cancellation $\{C(x), C(y)\} \approx 0$ in eq. (46) of 1111.2070 works because $P^i = C \cdot D^i_j n^j$ (eq. 45), which follows from the specific identity between the variation $S^{mn}$ and the constraint $C_i$. This identity uses the fact that $\partial V/\partial\gamma_{mn}$ involves the SAME polynomials as $V$ itself (through the Cayley–Hamilton relation for $D$ — see eq. (40)–(43) of 1111.2070). The identification $P^i = C \cdot D^i_j n^j + C_l \gamma^{li}$ (eq. 44) has TWO terms: the first vanishes by $C \approx 0$, the second by $C_i \approx 0$.

The Dirac contribution introduces a NEW term in $P^i$ that is NOT proportional to $C$ or $C_i$. Specifically: the variation $\delta C_g^{(\text{D})}/\delta\gamma_{ij}^{(f)}$ produces terms involving $\partial S^k_l / \partial\gamma_{ij}^{(f)}$ acting on the Dirac bilinear $\bar\psi \gamma^\alpha e_\alpha^k S^l_j D_l \psi$. These terms have NO reason to be proportional to the gravitational constraint $C$ or to $C_i$.

**Attack 2b: The analogy with scalars is EXACT at the structural level.** In 1408.0487, the scalar ghost mechanism is: the scalar momentum depends on both lapses → Hamiltonian is nonlinear in lapses → primary constraint fails. The spinor evades THIS mechanism because its momentum is lapse-independent (first-order kinetic structure).

But at the SECONDARY level, the mechanism is different. The secondary constraint fails in 1408.0487 §III.1.2 because the doubly-coupled scalar introduces a dependence on the metric variables that falls OUTSIDE the HR polynomial class (the P̃ = F₁√X̃ + F₂ exception is safe on FLRW but NOT on Bianchi — i.e., the Cayley–Hamilton cancellation fails). The spinor's spatial-derivative term introduces EXACTLY the same structural mismatch: matrix-element dependence vs. polynomial dependence. The mechanism is the same. The spinor only evades the primary (lapse) mechanism; it faces the SAME structural issue at the secondary level.

**Attack 2c: "Clifford identity cancellation" is a prayer, not a mechanism.** Scratch lists this as a D1 possibility (§5.2, mechanism 1): "The Dirac bilinear $\bar\psi[\ldots]\psi$ might satisfy algebraic identities (from the spinor index structure) that FORCE the correction to be proportional to existing constraints — a 'spinor miracle.'"

For this to work, the GRAVITATIONAL variation $\delta(\bar\psi \gamma^\alpha e_\alpha^j S^i_j D_i \psi)/\delta\gamma_{kl}^{(f)}$ — which involves $\partial S^i_j/\partial\gamma_{kl}^{(f)}$ tensored with the spinor bilinear — would have to be proportional to the constraint $C_g$ or $C_i$ by virtue of Clifford algebra. But the $\partial S / \partial\gamma_f$ factor is a PURELY GRAVITATIONAL tensor (it involves only the metrics, not the spinor). The Clifford algebra acts on spinor indices. These live in DIFFERENT spaces. There is no known identity that would force a gravitational tensor to be proportional to a gravitational constraint by virtue of spinor-index contractions. The hope is structurally empty.

**Attack 2d: "Dirac-bracket cancellation" is equally unfounded.** Scratch's mechanism 2 (§5.2): the Dirac-bracket corrections (term IV) might cancel the cross terms (terms II–III). But the Dirac-bracket correction has the form:

$$-\{C_g, \chi_A\}\,C^{AB}_{-1}\,\{\chi_B, C_f\}$$

where $\chi_A = \pi_\psi - \Sigma\psi^\dagger$. Now $\{C_g, \chi_A\}$ involves $\delta C_g/\delta\gamma_g$ and $\delta C_g/\delta\psi$ (through the standard canonical brackets), and similarly for $\{C_f, \chi_B\}$. The correction is QUADRATIC in $\delta C/\delta\psi$ and involves the inverse of the constraint matrix $C^{AB}$. The cross terms (II) are $\delta C_g^{(\text{D})}/\delta\gamma_f \cdot \delta C_f^{(\text{grav})}/\delta\pi_f$, which involve $\delta/\delta\gamma_f$ acting on the Dirac contribution (a gravitational derivative).

These are STRUCTURALLY DIFFERENT objects: the Dirac-bracket correction involves derivatives of $C$ with respect to the SPINOR variables, while the cross terms involve derivatives with respect to the METRIC variables. There is no structural reason to expect cancellation between objects with different index structures and different variable dependencies. Cancellation would be accidental, not structural.

### Summary on Result 2

**The structural argument for D2 is LOAD-BEARING.** The non-polynomial dependence on $S$ is a clear, structural, non-perturbative obstruction to the HR cancellation. The "escape routes" Scratch names (Clifford miracles, Dirac-bracket cancellations) are structurally unfounded — not impossible in principle, but not supported by any algebraic mechanism. Scratch's landing of "lean D2 at ~60–65%" understates the force of their own Result 2.

---

## 3. K1 — unmet and unaddressed

My kill criterion K1: the identity $\partial C/\partial n^k \propto C_i$ must be verified for the spinor case.

**Scratch does not work with the HR shift-redefined variables $n^i$ at all.** They go directly to the effective Hamiltonian after SVC elimination, bypassing the shift redefinition. This means:

- K1 is not satisfied.
- K1 is not REFUTED either — Scratch doesn't claim the identity holds; they simply don't check it.
- But the structural obstruction in Result 2 IS the content of K1 in a different language: the Dirac contribution introduces $\gamma_f$-dependence in $C_g$ that falls outside the polynomial class → in the HR shift-redefined language, this corresponds to $\partial C/\partial n^k$ having a residual piece NOT proportional to $C_i$.

**Status: K1 effectively failed** (the algebraic structure that would make it hold is broken by the non-polynomial $S$-dependence), even though Scratch doesn't state it in K1's language. Scratch's Result 2 is the content of K1's failure expressed differently.

---

## 4. K3 — unmet and explicitly open

My kill criterion K3: Dirac-bracket modifications must not spoil the closure.

**Scratch flags this explicitly (§2.2, §4.1 term IV) but does not compute it.** Their verdict acknowledges "Dirac-bracket corrections" as term (IV) in the bracket decomposition and lists it as part of the Lemma S1 computation.

**Attack 4a: Scratch should have evaluated whether the Dirac-bracket correction REINFORCES or OPPOSES the cross-term obstruction.** Even without a full computation, the SIGN and STRUCTURE of the Dirac-bracket correction can be assessed:

- The correction $-\{C_g, \chi_A\} C^{-1}_{AB} \{\chi_B, C_f\}$ is NEGATIVE-DEFINITE in a specific sense: it subtracts from the Poisson bracket. In many fermionic systems, the Dirac-bracket reduction TIGHTENS the constraint algebra (removes spurious second-class dof).
- But here, the matrix $C^{-1}_{AB}$ depends on BOTH metrics (through $\Sigma = \sqrt{\gamma_g} A_g + \sqrt{\gamma_f} A_f$). This means the correction introduces ADDITIONAL cross-metric terms, not fewer. It is a new source of non-polynomial $S$-dependence, reinforcing (not cancelling) the Result 2 obstruction.

**Attack 4b: The Dirac-bracket correction is structurally a SECOND obstruction, not a potential rescue.** Scratch lists it as a possible rescue mechanism (§5.2, mechanism 2). I argue this is backwards. The correction involves $C^{-1}_{AB}$, which depends on $\Sigma$, which depends on the relative boost $\Lambda^*$, which depends on $S$. After substituting the SVC solution, the Dirac-bracket correction inherits the SAME non-polynomial $S$-dependence that Result 2 identifies as the structural obstruction. The correction adds to the problem, not against it.

**Status: K3 is unmet, and its resolution is more likely to WORSEN than improve the D2 case.**

---

## 5. K4 — cannot be met in this round

K4 requires a non-perturbative closure. Scratch's analysis is structural (not perturbative in the coupling sense) but does not CLOSE the bracket. The lean is non-perturbative in spirit — the polynomial-class mismatch is a structural argument, not a perturbative expansion — but the gap is Lemma S1: whether the correction actually spoils the constraint or accidentally vanishes.

**K4 remains the correct standard.** Neither Scratch nor I meet it. But Scratch's structural argument is non-perturbative in the right sense: it identifies a class mismatch that doesn't depend on the magnitude of the spinor field.

---

## 6. K5 — partially addressed

Scratch notes (§4.3) that the mass term $\sqrt{\gamma_f}\,m\bar\psi\psi = \sqrt{\gamma_g}\,\det(S)\,m\bar\psi\psi$ involves $\det(S) = e_D(S)$, which IS a symmetric polynomial. So the mass term alone would be safe (it's in the polynomial class).

**Attack 6a:** This actually SHARPENS the obstruction. The mass term is safe; the spatial-derivative term is unsafe. So the ghost (if D2) arises specifically from the KINETIC coupling of the spinor to both tetrads — from the $\bar\psi \gamma^\alpha e_\alpha^j S^i_j D_i \psi$ term. If someone proposed a "mass-only" doubly-coupled spinor (kinetic term on one metric only, mass term on both), that would be in the safe class of 1408.0487 §IV (analogous to $\tilde{P} = \tilde{P}(\phi)$). But NTE's deposited reading has kinetic coupling on both tetrads. The ghost arises from what is most characteristic of the doubly-coupled neutrino.

**K5 partially addressed. The mass case is in the polynomial class; the kinetic case is not.**

---

## 7. ASSESSMENT OF LEMMA S1 — correctly named, not a stall

### Is S1 a stall?

No. Scratch has identified a genuine computational gap. The structural argument for D2 is strong but does not PROVE the correction is non-zero on the full constraint surface. Lemma S1 is the honest next step. Naming it is responsible, not evasive.

### Is S1 likely to confirm D2?

Yes, on structural grounds:
1. The 1+1d truncation should show D2, because the polynomial-class mismatch exists in ANY dimension (the Dirac spatial-derivative term depends on matrix elements of $S$, not on $e_n(S)$, in 1+1d just as in 3+1d).
2. The $O(\psi^2)$ computation in 3+1d should show a non-zero correction, because the cross term $\{C_g^{(\text{D})}, C_f^{(\text{grav})}\}$ is a functional of the Dirac bilinear and the gravitational extrinsic curvature — there is no structural reason for it to vanish identically.
3. The only escape would be an ACCIDENTAL cancellation among terms (II), (III), and (IV) — i.e., between the cross terms, the pure Dirac bracket, and the Dirac-bracket correction. As argued in Attack 2c–2d, these have different structures and there is no mechanism forcing cancellation.

### Should S1 be commissioned?

That's for AC and Greg to decide. I note that Lemma S1 is foundation work (is two-orientation gravity consistent with a doubly-coupled spinor in principle?), not deposit work. Even D1 does not restore the symmetric ν.

---

## 8. OPENING-BY-OPENING SCORECARD

| Opening | My pre-registration | Scratch's finding | My assessment |
|---|---|---|---|
| **1 (shift sector)** | ∂C/∂n^k ∝ C_i must hold | Non-zero bracket correction from non-polynomial S-dependence (Result 2) | **CONFIRMED as primary obstruction.** K1 effectively failed — the algebraic identity breaks because the Dirac contribution is outside the polynomial class. Scratch's Result 2 is K1-failure in different language. |
| **2 (relative Lorentz)** | Relative boost becomes physical → ghost hides here | Relative boost is auxiliary (Result 1) — determined by modified SVC | **PARTIALLY RESOLVED.** No new propagating dof from Lorentz sector. But the SVC elimination feeds the problem INTO Opening 1 (modified cross-metric dependence). The ghost's hiding place is relocated, not emptied. |
| **3 (cross-metric lapse)** | Non-fatal, absorbed | Non-fatal, confirmed | **AGREED.** No independent attack. |
| **4 (Dirac bracket)** | C_AB depends on both metrics + relative boost → modifies all brackets | Flagged (§2.2, term IV) but not computed; listed as part of Lemma S1 | **OPEN — and likely a SECOND obstruction.** The Dirac-bracket correction inherits the same non-polynomial S-dependence as Result 2. It reinforces, not cancels, the D2 lean. K3 unmet. |

---

## 9. KILL CRITERIA STATUS

| # | Criterion | Scratch's status | Jammer's assessment |
|---|---|---|---|
| **K1** | ∂C/∂n^k ∝ C_i for spinor case | Not checked in HR language; effectively failed via Result 2 | **FAILED** — the polynomial-class mismatch is K1's content in different notation |
| **K2** | Relative Lorentz secondary survives; SVC enforced | SVC enforced (modified) — K2b satisfied; K2a (full constraint closure) still open | **PARTIALLY MET** — Lorentz sector closes, lapse sector does not |
| **K3** | Dirac-bracket correction doesn't spoil closure | Not computed; flagged as open | **UNMET** — and likely reinforces D2 |
| **K4** | Non-perturbative closure | Not achieved; structural argument is non-perturbative in spirit | **UNMET** — but the right standard |
| **K5** | Mass term accounted for | Mass term is polynomial (safe); kinetic term is non-polynomial (unsafe) | **PARTIALLY MET** — sharpens the obstruction to the kinetic sector |

**Score: 0 of 5 fully met. 2 partially met. 3 failed/unmet.** D1 is NOT established. D2 is structurally indicated but not proven.

---

## 10. CONVERGENCE AND DIVERGENCE — detailed

### Where I converge with Scratch

1. **D4 is the honest landing.** The gap (Lemma S1) is real. Neither of us can PROVE D2 without the explicit computation.
2. **Result 1 is genuine.** The relative boost is auxiliary. This is real progress.
3. **Result 2 is the core finding.** The polynomial-class mismatch is the structural heart of the problem.
4. **Lemma S1 is correctly named.** 1+1d bigravity + Dirac is the right tractable setting.
5. **Even D1 ≠ restore ν.** No number. No f. No κ. Deposit unchanged.

### Where I diverge from Scratch

1. **Credence.** Scratch: D2 at ~60–65%. Jammer: D2 at ~70–75%. The difference: I assign less probability to the "Clifford miracle" and "Dirac-bracket cancellation" escape routes, because I find them structurally unfounded (Attacks 2c, 2d, 4b).

2. **Framing of the D1 escape routes.** Scratch lists three D1 possibilities (§5.2). I argue:
   - Mechanism 1 (Clifford identity): structurally empty — Clifford algebra acts on spinor indices, the obstruction is in gravitational tensor indices. Different spaces.
   - Mechanism 2 (Dirac-bracket cancellation): backwards — the Dirac-bracket correction REINFORCES the obstruction by adding more non-polynomial S-dependence.
   - Mechanism 3 (mass dominance): irrelevant non-perturbatively (K4). The kinetic term is present regardless of magnitude.

3. **Framing of Result 1.** "Partially resolved" for Opening 2 understates the significance of what happens AFTER the resolution. The SVC elimination creates a DERIVED obstruction (non-polynomial S-dependence in the effective Hamiltonian) that is the actual threat. Saying Opening 2 is "partially resolved" is like saying a flood has been diverted — into your living room.

4. **Whether the structural argument suffices for D2 vs. D4.** I lean toward: the structural argument IS the D2 evidence, and Lemma S1 is confirmation, not decision. Scratch treats S1 as the decider and the structural argument as merely suggestive. This is too conservative. Every known analogy (1408.0487 scalars, the full pattern of doubly-coupled kinetic matter in bimetric gravity) points to D2. The spinor evades the primary mechanism; there is no evidence it evades the secondary one. D4 is the cautious landing; D2 is the probable truth.

---

## 11. NET ASSESSMENT

**Gate 0: UNDETERMINED (D4), structural lean D2.** I converge with Scratch on the landing. I diverge on the credence: 70–75% D2, not 60–65%.

**The case for D2:** The Dirac spinor kinetically coupled to both tetrads introduces a dependence on the matrix elements of $S = \sqrt{\gamma_g^{-1}\gamma_f}$ that falls outside the elementary-symmetric-polynomial class on which the HR secondary-constraint cancellation relies. This is a structural, non-perturbative mismatch. Every known analogy with doubly-coupled kinetic matter produces D2 at the secondary level. The proposed D1 escape routes (Clifford identities, Dirac-bracket cancellations) are structurally unfounded.

**The case for D1:** No positive evidence. The only honest path to D1 is Lemma S1 showing an accidental cancellation. I do not expect it.

**Explicit, regardless of outcome:**
- N_eff ≈ 1.52 — symmetric ν excluded at ~10σ, independent, banked
- No κ. No f. Not a route to restoring any number.
- Even D1 is foundation only. Deposit: P04 / adopted ΛCDM / cosmological sector open.

---

## 12. RECOMMENDATIONS TO AC

1. **Register convergence:** Jammer and Scratch converge on D4 (undetermined), lean D2. Jammer leans harder (70–75% vs 60–65%). The difference is assessment of escape-route probability, not the structural argument itself.

2. **Lemma S1:** Correctly named. If commissioned, the 1+1d bigravity + Dirac computation is the right tractable setting. D2 there → D2 generically. D1 there → suggestive, needs 3+1d. This is foundation work, not deposit work.

3. **Do not treat the D4 wrapping as "undecided."** The structural evidence for D2 is strong. D4 reflects computational incompleteness, not genuine equipoise. AC should register that both lanes lean D2 and that the structural arguments have no D1 counterweight.

4. **Gate 0 remains undetermined.** But note: the lapse sector (primary constraint) is resolved favourably (D3 excluded), and the secondary constraint is structurally obstructed (D2 lean). The foundation question is: "Is two-orientation gravity with a doubly-coupled spinor consistent in principle?" The evidence says: probably not.

---

— Claude Jammer, 2026-10-09. Attack filed against Scratch's D4 verdict. Converge on landing, diverge on credence. No rescue. No number restored.
