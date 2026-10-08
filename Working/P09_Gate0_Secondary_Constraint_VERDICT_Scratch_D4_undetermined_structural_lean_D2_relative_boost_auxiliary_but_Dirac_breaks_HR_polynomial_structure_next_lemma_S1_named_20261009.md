# P09 Gate-0 — Secondary Constraint VERDICT (Scratch, construction)

## Landing: D4 — undetermined, with structural lean D2

**The relative boost is auxiliary (non-propagating) — a genuine positive result. But the Dirac field's dependence on the square-root matrix $S$ breaks the algebraic structure the HR secondary-constraint cancellation relies on, and the bracket $\{C_g, C_f\}$ receives corrections whose sign and magnitude I cannot determine without the explicit computation named as Lemma S1. The honest landing is D4 with a structural lean toward D2.**

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-09
**Authority:** Greg GO 2026-10-09
**Pre-registration:** `Working/P09_Gate0_Secondary_Constraint_PREREGISTRATION_Scratch_…_20261009.md` (filed before this computation)
**Label:** ORIGINAL WORK — the two-tetrad Dirac constraint algebra below has no prior art

---

## Read set this session

- `Working/P09_Gate0_O1_ADM_ROUND_…UNDETERMINED_20261008.md` (my prior round: lapse-linearity banked, D4 at secondary)
- `Handoffs/Directive_Cursor_Main_to_Scratch_Jammer_Gate0_…_20261009.md` (Greg GO, object specified)
- `Handoffs/Arbitration_AC_Spinor_Lapse_Linearity_Gate0_…_20261008.md` (AC's commission, openings 1–3)
- Background (cited, flagged for Cursor Main source-verification): Hassan–Rosen [arXiv:1111.2070](https://arxiv.org/abs/1111.2070) (secondary constraint proof); Hinterbichler–Rosen [arXiv:1203.5783](https://arxiv.org/abs/1203.5783) (vierbein bigravity, SVC, relative Lorentz); [arXiv:1408.0487](https://arxiv.org/abs/1408.0487) (scalar ghost mechanism); Nelson–Teitelboim 1978 (Dirac canonical gravity)

---

## Step 1: The relative Lorentz parameters remain AUXILIARY — Opening 2 does not directly propagate new dof

### 1.1 Setup

Two independent tetrads $e^a_\mu$ (for $g_{\mu\nu}$) and $\varepsilon^a_\mu$ (for $f_{\mu\nu}$), each with its own local Lorentz group: $\text{SO}(1,3)_g \times \text{SO}(1,3)_f$ — twelve independent parameters per spacetime point.

The bimetric mass term (HR potential) preserves only the **diagonal** Lorentz: $\Lambda_g = \Lambda_f = \Lambda$. This reduces to 6 gauge parameters. The remaining 6 (the relative Lorentz $\Lambda_{\text{rel}} = \Lambda_f^{-1}\Lambda_g$) are NOT gauge.

A Dirac spinor $\psi$ coupled to both tetrads transforms under a single $\text{Spin}(1,3)$:
$$\psi \to S(\Lambda)\,\psi$$
For invariance of both kinetic terms, the SAME $\Lambda$ must act on both tetrads → only diagonal Lorentz survives. **The spinor does not break any symmetry that the potential hasn't already broken.**

### 1.2 ADM gauge-fixing

Use the 3 diagonal boosts to set the $g$-tetrad in time-gauge: $e^\alpha_0 = 0$. This exhausts the boost gauge. The $f$-tetrad generically has $\varepsilon^\alpha_0 = \varphi^\alpha \neq 0$ — the **relative boost** between the two frames. Under the remaining diagonal spatial rotations (3 parameters), we can gauge-fix 3 of the 6 relative Lorentz parameters. The remaining 3 (relative spatial rotation) plus 3 (relative boost $\varphi^\alpha$) = 6 relative parameters must be dealt with.

### 1.3 The Dirac Lagrangian does NOT give kinetic terms for the relative Lorentz parameters

The Dirac action is first-order in $\psi$:
$$S_\psi = \int d^4x\;\Big[\det(e)\;\bar\psi\,\gamma^a\,e_a^\mu\,D_\mu^{(g)}\psi \;+\; \det(\varepsilon)\;\bar\psi\,\gamma^a\,\varepsilon_a^\mu\,D_\mu^{(\varepsilon)}\psi \;-\; \text{mass}\Big]$$

The relative Lorentz parameters $\Lambda_{\text{rel}}$ enter through the relationship between $e$ and $\varepsilon$. Crucially:

**(a) No $\dot\Lambda_{\text{rel}}$ from the tetrad factors.** The tetrads $e^a_\mu$ and $\varepsilon^a_\mu$ appear algebraically (not differentiated) in the products $\bar\psi\,\gamma^a\,e_a^\mu$ and $\bar\psi\,\gamma^a\,\varepsilon_a^\mu$. So the Dirac action has NO time derivatives of $\Lambda_{\text{rel}}$ from these factors.

**(b) No $\dot\Lambda_{\text{rel}}$ from the spin connections.** The spin connection $\omega^{ab}_\mu$ for the $g$-tetrad depends on $\partial_\mu e^a_\nu$, which involves $\partial_0 e^\alpha_i$ (extrinsic curvature of $g$) but NOT $\partial_0\Lambda_{\text{rel}}$, because the $g$-tetrad is in time-gauge ($e^\alpha_0 = 0$, no $\Lambda_{\text{rel}}$-dependence). The $f$-spin connection $\tilde\omega^{ab}_\mu$ depends on $\partial_\mu \varepsilon^a_\nu$, and $\varepsilon^a_0$ depends on $\Lambda_{\text{rel}}$ — but $\tilde\omega^{ab}_i$ involves $\partial_i \varepsilon^a_0$ (spatial derivatives of $\Lambda_{\text{rel}}$, NOT time derivatives), and $\tilde\omega^{ab}_0$ involves $\partial_0 \varepsilon^\alpha_i$ (time derivative of the spatial $f$-triad) and $\partial_i \varepsilon^a_0$ (spatial derivatives). **No $\partial_0\Lambda_{\text{rel}}$ appears.**

**(c) The Einstein–Hilbert terms have full individual Lorentz invariance.** The $g$-EH action is invariant under $\text{SO}(1,3)_g$; the $f$-EH action under $\text{SO}(1,3)_f$. Their contributions to the momentum conjugate to $\Lambda_{\text{rel}}$ vanish identically.

**Result:** The conjugate momentum to $\Lambda_{\text{rel}}$ receives ZERO contribution from every sector:
$$p_{\Lambda_{\text{rel}}} \approx 0 \qquad \text{(primary constraint)}$$

This is a primary constraint. Its preservation under time evolution:
$$\dot p_{\Lambda_{\text{rel}}} = \{p_{\Lambda_{\text{rel}}},\,H\} = -\frac{\partial H}{\partial \Lambda_{\text{rel}}} \approx 0$$

gives the **modified symmetric vierbein condition (SVC)**:
$$\frac{\partial V_{\text{HR}}}{\partial \Lambda_{\text{rel}}} + \frac{\partial H_{\text{Dirac}}}{\partial \Lambda_{\text{rel}}} = 0 \qquad \text{(secondary constraint = modified SVC)}$$

This is an **algebraic** equation for $\Lambda_{\text{rel}}$ (no time derivatives). It determines $\Lambda_{\text{rel}}$ as a function of $(\gamma_g, \gamma_f, \psi)$.

### 1.4 Non-degeneracy of the second-class pair

The pair $(p_{\Lambda_{\text{rel}}},\;\text{modified SVC})$ is second-class if:
$$\{p_{\Lambda_{\text{rel}}},\;\text{modified SVC}\} = -\frac{\partial^2 H}{\partial \Lambda_{\text{rel}}^2}\bigg|_{\Lambda_{\text{rel}}=\Lambda^*} \neq 0$$

In the pure gravity case: $\partial^2 V_{\text{HR}}/\partial\Lambda_{\text{rel}}^2 \neq 0$ at the SVC solution (guaranteed by the HR potential structure for generic metrics).

With the spinor: $\partial^2 H_{\text{Dirac}}/\partial\Lambda_{\text{rel}}^2$ is proportional to the fermionic bilinear $\bar\psi[\ldots]\psi$, a PERTURBATIVE correction to a non-degenerate matrix. Non-degeneracy is preserved for generic $(\gamma_g, \gamma_f, \psi)$.

**Result:** The $(p_\Lambda, \text{SVC})$ pair forms 6 second-class constraints → **removes all 6 relative Lorentz parameters from the phase space.** The relative boost does NOT propagate — it is auxiliary.

### 1.5 Summary on Opening 2

**Opening 2 does not directly introduce new propagating degrees of freedom.** The relative boost becomes physical (it depends on the Dirac field and both metrics), but it is determined algebraically, not dynamically. This is a genuine positive finding.

**However:** after eliminating $\Lambda_{\text{rel}}$ via the modified SVC, the effective constraints $C_g$ and $C_f$ acquire a modified dependence on both metrics — and this modified dependence is where the threat to the secondary constraint lives. Opening 2 feeds into Opening 1, not independently.

---

## Step 2: Dirac second-class constraints

### 2.1 The canonical momentum

In the ADM decomposition, the Dirac time-derivative terms from both tetrads combine:
$$L \supset (\sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f)\;\psi^\dagger\,\dot\psi$$

where $A_g, A_f$ are the $\gamma^0$-related normal projectors from each tetrad (both equal $\gamma^0$ in the time-gauge for $g$; $A_f$ acquires a relative-boost-dependent correction from $\varepsilon^\alpha_0 = \varphi^\alpha$). The conjugate momentum:
$$\pi_\psi = (\sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f)\;\psi^\dagger \equiv \Sigma\;\psi^\dagger$$

where $\Sigma = \sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f$ is the **total symplectic density**, a matrix in spinor space depending on $(\gamma_g, \gamma_f, \Lambda_{\text{rel}})$.

### 2.2 The second-class constraint structure

The constraint $\chi \equiv \pi_\psi - \Sigma\,\psi^\dagger \approx 0$ and its conjugate form a second-class set. The constraint matrix:
$$C_{AB} = \{\chi_A,\,\chi^\dagger_B\}$$

depends on $\Sigma$ and hence on $(\gamma_g, \gamma_f, \Lambda_{\text{rel}})$.

After passing to the Dirac bracket:
$$\{F,\,G\}_D = \{F,\,G\} - \{F,\,\chi_A\}\,C^{AB}_{-1}\,\{\chi_B,\,G\}$$

**all** subsequent brackets (including gravitational ones) are modified by the Dirac-bracket correction. Because $C_{AB}$ depends on both metrics AND on the relative boost, the correction to $\{C_g, C_f\}_D$ is structurally different from the single-metric case. This is Opening 4 from the directive.

### 2.3 After elimination

After the Dirac-bracket reduction, the effective fermionic degrees of freedom are half the original (the momentum $\pi_\psi$ is identified with $\Sigma\,\psi^\dagger$). The Dirac contribution to the Hamiltonian depends on $(\gamma_g, \gamma_f, \psi)$ but NOT on the gravitational momenta $(\pi_g, \pi_f)$, after the standard Nelson–Teitelboim momentum redefinition that absorbs the spin-connection contributions.

---

## Step 3: The effective Hamiltonian after all eliminations

After eliminating the relative Lorentz parameters (Step 1, via modified SVC: $\Lambda_{\text{rel}} = \Lambda^*(\gamma_g, \gamma_f, \psi)$) and the Dirac second-class constraints (Step 2), the total Hamiltonian takes the form:

$$H = N_g\,C_g + N_f\,C_f + n^i\,C_i$$

where:

$$C_g = \underbrace{H_\perp^{(g,\text{grav})}(\gamma_g, \pi_g, \gamma_f)}_{\text{gravity + HR potential}} + \underbrace{\sqrt{\gamma_g}\;\bar\psi\,\mathcal{O}_g(\gamma_g, \gamma_f, \Lambda^*)\,\psi}_{\text{Dirac, } g\text{-sector}}$$

$$C_f = \underbrace{H_\perp^{(f,\text{grav})}(\gamma_f, \pi_f, \gamma_g)}_{\text{gravity + HR potential}} + \underbrace{\sqrt{\gamma_f}\;\bar\psi\,\mathcal{O}_f(\gamma_g, \gamma_f, \Lambda^*)\,\psi}_{\text{Dirac, } f\text{-sector}}$$

The operators $\mathcal{O}_g$ and $\mathcal{O}_f$ involve the spatial triads, spatial spin connections, spatial covariant derivatives $D_i$, and the mass $m$. After SVC elimination ($\Lambda^*$ substituted), they depend on BOTH spatial metrics.

**Crucially:** The $\gamma_f$-dependence of $C_g^{(\text{D})}$ and the $\gamma_g$-dependence of $C_f^{(\text{D})}$ come from:
1. The SVC solution: $\varepsilon_\alpha^i = e_\alpha^j\,S_j^i + O(\psi^2)$ where $S = \sqrt{\gamma_g^{-1}\gamma_f}$
2. The relative boost: $\varphi^\alpha = \varphi^\alpha(\gamma_g, \gamma_f, \psi)$

The dependence is through the **matrix elements** $S^i_j$, not through the elementary symmetric polynomials $e_n(S)$ that parameterize the HR potential.

---

## Step 4: The bracket — structure and the structural obstruction

### 4.1 Decomposition

$$\{C_g(x),\,C_f(y)\} = \underbrace{\{C_g^{(\text{grav})},\,C_f^{(\text{grav})}\}}_{\text{(I): pure HR}} + \underbrace{\{C_g^{(\text{D})},\,C_f^{(\text{grav})}\} + \{C_g^{(\text{grav})},\,C_f^{(\text{D})}\}}_{\text{(II): cross terms}} + \underbrace{\{C_g^{(\text{D})},\,C_f^{(\text{D})}\}}_{\text{(III): pure Dirac}} + \underbrace{\text{Dirac-bracket corrections}}_{\text{(IV): from Step 2}}$$

**Term (I):** The pure HR bracket. This is the known result from [arXiv:1111.2070](https://arxiv.org/abs/1111.2070): it generates the secondary constraint $\mathcal{S}^{(0)} \approx 0$ that removes the BD ghost. **Banked.**

**Terms (II)–(IV):** The Dirac corrections. These are the unknowns.

### 4.2 Why the cross terms (II) are generically non-zero

Consider $\{C_g^{(\text{D})}(x),\,C_f^{(\text{grav})}(y)\}$.

$C_g^{(\text{D})}$ depends on $(\gamma_g, \gamma_f, \psi)$. After the momentum redefinition (Nelson–Teitelboim), it does NOT depend on $(\pi_g, \pi_f)$.

$C_f^{(\text{grav})}$ depends on $(\gamma_f, \pi_f, \gamma_g)$ (the $\gamma_g$-dependence is through the HR potential $V(\gamma_g, \gamma_f)$, and the $\pi_f$-dependence is from the kinetic/curvature term $R̃^0$).

The non-trivial bracket comes from the canonical pair $(\gamma_f, \pi_f)$:
$$\{C_g^{(\text{D})}(x),\,C_f^{(\text{grav})}(y)\} = \int d^3z\;\frac{\delta C_g^{(\text{D})}(x)}{\delta\gamma_{ij}^{(f)}(z)}\;\frac{\delta C_f^{(\text{grav})}(y)}{\delta\pi^{ij}_{(f)}(z)}$$

(The reverse term vanishes because $C_g^{(\text{D})}$ doesn't depend on $\pi_f$.)

This is **non-zero** because:
- $\delta C_g^{(\text{D})}/\delta\gamma_{ij}^{(f)} \neq 0$ — the Dirac $g$-Hamiltonian depends on $\gamma_f$ through the SVC-eliminated triad $\varepsilon_\alpha^i(\gamma_g, \gamma_f)$
- $\delta C_f^{(\text{grav})}/\delta\pi^{ij}_{(f)} \neq 0$ — this is $\propto K^{ij}_{(f)}$ (the $f$-extrinsic curvature), the standard velocity term

**Contrast with single-metric matter:** If the spinor coupled to $g$ only, $C_g^{(\text{D})}$ would NOT depend on $\gamma_f$, so $\delta C_g^{(\text{D})}/\delta\gamma_{ij}^{(f)} = 0$, and the cross term would vanish. **The doubly-coupled spinor's dependence on the other metric, through the SVC-eliminated relative Lorentz parameters, is what activates the cross term.**

### 4.3 The structural obstruction — algebraic mismatch

The HR secondary constraint relies on a specific cancellation in the bracket of the interaction potential $V$ with the gravitational kinetic terms. This cancellation works because:

1. $V$ depends on the square-root matrix $S = \sqrt{\gamma_g^{-1}\gamma_f}$ through the **elementary symmetric polynomials** $e_n(S)$: $V = \sum_{n=0}^{D} \beta_n\,e_n(S)$
2. The $e_n(S)$ satisfy Cayley–Hamilton identities: $S$ obeys its own characteristic equation, constraining the functional dependence
3. The HR shift redefinition is designed to exploit these polynomial identities, separating the lapse-dependent and shift-dependent sectors

The Dirac contribution $C_g^{(\text{D})}$ depends on $S$ through the SVC-eliminated $f$-triad:
$$\varepsilon_\alpha^i = e_\alpha^j\,S_j^i \qquad (\text{leading order in }\psi)$$

The Dirac bilinear:
$$\bar\psi\,\gamma^\alpha\,\varepsilon_\alpha^i\,D_i\,\psi = \bar\psi\,\gamma^\alpha\,e_\alpha^j\,S_j^i\,D_i\,\psi$$

depends on the **matrix elements** $S_j^i$ — i.e., the full matrix $S$, not just its symmetric polynomials $e_n(S)$. The mass term similarly:
$$\sqrt{\gamma_f}\,m\bar\psi\psi = \sqrt{\gamma_g}\,\det(S)\,m\bar\psi\psi$$

where $\det(S) = e_D(S)$ IS a symmetric polynomial — but the spatial-derivative term is not.

**The spatial-derivative (kinetic) Dirac term breaks the polynomial structure.** The bracket $\{C_g^{(\text{D})}, C_f^{(\text{grav})}\}$ involves $\partial(\bar\psi\,\gamma^\alpha e_\alpha^j S_j^i D_i\psi)/\partial\gamma^{(f)}_{kl}$, which is a derivative of the full matrix $S$ with respect to $\gamma_f$ — not constrained to the elementary-symmetric-polynomial sector.

**This is the core structural reason why the HR cancellation is expected to fail:** the Dirac contribution introduces a dependence on $S$ that falls outside the algebraic class where the HR cancellation operates.

### 4.4 The bracket correction — what can and cannot be determined

**Can determine:**
- The cross terms (II) are non-zero: YES (§4.2)
- The cross terms involve a structurally different dependence on $S$ from the HR potential: YES (§4.3)
- The Dirac-bracket corrections (IV) are non-zero: YES (because $C_{AB}$ depends on both metrics, giving non-trivial corrections to gravitational brackets)

**Cannot determine without explicit computation:**
- Whether the cross terms, when evaluated on the full constraint surface ($C_g = C_f = C_i = 0$, modified SVC, fermionic constraints), **vanish** or **are proportional to existing constraints**. If they are weakly zero, the secondary constraint survives (D1). If they are not weakly zero, they modify or spoil it (D2 or modified-D1).
- Whether gamma-matrix identities (Fierz, Clifford algebra) or properties of the Dirac bracket (its specific spinor-index structure) provide **unexpected cancellations** among terms (II), (III), and (IV).
- Whether the mass term's polynomial dependence on $\det(S)$ dominates over the spatial-derivative term's non-polynomial dependence, in any controlled expansion.

### 4.5 Why this is NOT resolved by the semiclassical expansion alone

At $O(\psi^0)$: the pure HR bracket holds → secondary constraint exists. No information about the Dirac correction.

At $O(\psi^2)$: the leading Dirac correction appears. But:
- The correction depends on the specific spinor configuration $\psi(x)$, the spatial metrics, and the momenta.
- Even if the correction is non-zero for generic $\psi$, it might be proportional to the (already existing) secondary constraint — modifying it but not destroying it.
- To determine whether the correction spoils the constraint or preserves it, one must check whether the MODIFIED secondary constraint $\mathcal{S}^{(0)} + \mathcal{S}^{(\psi^2)} \approx 0$ is consistent with its own preservation. This requires the NEXT bracket: $\{\mathcal{S}^{(0)} + \mathcal{S}^{(\psi^2)},\,H\}$, which is a further computation.

The semiclassical expansion can identify the MECHANISM, but closing the question requires either:
- A non-perturbative structural argument, OR
- An explicit computation in a tractable truncation (1+1d or mini-superspace)

---

## Step 5: Controlled truncation — the lean

Although I cannot close the full bracket, I can identify the structural lean.

### 5.1 The mechanism by which D2 occurs (if it does)

The chain is:
1. Doubly-coupled spinor → only diagonal Lorentz survives (shared with the HR potential)
2. Relative boost eliminated by modified SVC → $\Lambda^*(\gamma_g, \gamma_f, \psi)$ substituted
3. After substitution, $C_g^{(\text{D})}$ depends on $\gamma_f$ through the MATRIX ELEMENTS of $S = \sqrt{\gamma_g^{-1}\gamma_f}$
4. The bracket $\{C_g^{(\text{D})}, C_f^{(\text{grav})}\}$ involves $\delta/\delta\gamma_f$ acting on these matrix elements, producing terms outside the HR polynomial class
5. These terms contribute to $\{C_g, C_f\}$ and modify the secondary constraint
6. If the modification is INCOMPATIBLE with the constraint structure (the modified secondary is no longer preserved under time evolution, or its preservation determines a lapse instead of generating a new constraint), the BD ghost returns

### 5.2 The mechanism by which D1 could hold (despite the structural argument)

1. The Dirac bilinear $\bar\psi[\ldots]\psi$ might satisfy algebraic identities (from the spinor index structure) that FORCE the correction to be proportional to existing constraints — a "spinor miracle." This is not ruled out.
2. The Dirac-bracket corrections (IV) might CANCEL the cross terms (II), leaving the net correction zero. This would be a remarkable cancellation between the fermionic sector's second-class structure and its Hamiltonian contributions.
3. In the massive case, the mass term's dependence on $\det(S)$ (a symmetric polynomial) might dominate, and the spatial-derivative terms might be subleading in some controlled limit. But K4 requires non-perturbative closure.

### 5.3 Lean: D2

The structural argument favours D2 because:
- The non-polynomial dependence on $S$ from the Dirac spatial-derivative term is a **generic** obstruction, not a special or fine-tuned one
- There is no known algebraic identity in the Clifford algebra that would force the Dirac bilinear's sensitivity $\delta(\bar\psi\gamma^\alpha e_\alpha^j S_j^i D_i\psi)/\delta\gamma_f$ to lie in the span of the elementary symmetric polynomials of $S$
- Every known doubly-coupled matter field that enters the kinetic sector of both metrics reintroduces the ghost (1408.0487); the spinor evades the PRIMARY mechanism (lapse-linearity) but faces the SAME structural issue at the secondary level
- The "spinor miracle" (D1 mechanism 1 above) would be an entirely new algebraic result with no precedent in the constraint-algebra literature

**I lean D2 at ~60–65% credence**, but I land D4 because I cannot PROVE the correction doesn't cancel.

---

## Named next lemma: S1

**Lemma S1 (the computation that closes D1 vs D2):**

Compute, in a tractable setting, the leading Dirac correction to the secondary constraint:

$$\Delta\mathcal{S} \;\equiv\; \{C_g^{(\text{D})}(x),\,C_f^{(\text{grav})}(y)\} + \{C_g^{(\text{grav})}(x),\,C_f^{(\text{D})}(y)\} + \{C_g^{(\text{D})}(x),\,C_f^{(\text{D})}(y)\} + (\text{Dirac-bracket corrections})$$

evaluated on the constraint surface at $O(\psi^2)$.

**If $\Delta\mathcal{S} \approx 0$ (weakly zero):** the secondary constraint survives → D1.
**If $\Delta\mathcal{S} \not\approx 0$:** the secondary constraint is modified → check whether the modified constraint is preserved (D1-modified) or determines a lapse (D2).

**Tractable settings (in order of decisiveness):**
1. **1+1 dimensional bigravity + Dirac:** 2×2 tetrads, 2-component spinor, single relative-boost parameter. The constraint algebra is drastically simpler. If D2 appears here, it appears generically. If D1 holds here, it is suggestive but not sufficient for 3+1d.
2. **Mini-superspace (FLRW × FLRW):** homogeneous/isotropic metrics, homogeneous spinor. The constraint algebra reduces to finite-dimensional mechanics. Caveat: 1408.0487 showed FLRW-safe ≠ Bianchi-safe for scalars (§III.1.2), so a D1 in mini-superspace does NOT prove D1 globally — but a D2 in mini-superspace DOES prove D2 globally.
3. **Full 3+1d, perturbative to $O(\psi^2)$:** the most decisive but most laborious. Requires the explicit modified SVC solution and the full bracket with Dirac-bracket corrections.

**Pre-requisite for S1:** the explicit modified SVC solution $\Lambda_{\text{rel}}^* = \Lambda^*(\gamma_g, \gamma_f, \psi)$ to leading order. This is straightforward (first-order perturbation of the standard SVC, with the Dirac source), and I outline it as sub-lemma S1a.

---

## Assessment against the openings

| Opening | Status | Finding |
|---|---|---|
| **1 (shift sector)** | OPEN | The Dirac contribution enters the shift-redefined Hamiltonian through the cross-metric dependence (§4.2–4.3). The identity $\partial C/\partial n^k \propto C_i$ has not been verified for the spinor case. This is the primary blocker for closing D1 vs D2. |
| **2 (relative Lorentz)** | PARTIALLY RESOLVED | The relative boost is **auxiliary** (non-propagating) — a positive result (§1). It does not directly introduce new dof. But it **modifies the effective constraints** through the SVC elimination, feeding into Opening 1. |
| **3 (cross-metric lapse coefficients)** | RESOLVED (non-fatal) | Confirmed non-fatal, as in the prior round. Lapse-linearity holds; cross-metric dependence enters the secondary, not the primary. |
| **4 (Dirac bracket)** | OPEN | The Dirac-bracket correction (§2.2, term IV in §4.1) is non-zero and structurally novel. Not computed explicitly. Part of the Lemma S1 computation. |

---

## Constraint counting (consistency check)

Phase space after all second-class reductions:
- Gravitational: $2 \times 12 = 24$ (two spatial metrics + momenta)
- Dirac (after second-class): 8 real (4 complex spinor components; momenta identified with fields)
- Relative Lorentz (after SVC): 0 (eliminated by 6 second-class constraints)
- **Total: 32**

Constraints:
- Spatial diffeomorphisms $C_i \approx 0$: 3 first-class → remove 6
- Hamiltonian constraints $C_g \approx 0,\,C_f \approx 0$: second-class pair → remove at least 2

**If secondary constraint survives (D1):** $C_g, C_f, \mathcal{S}, \mathcal{S}' $ = 4 second-class → remove 4. Total removed: 6 + 4 = 10. Remaining: 22 → **11 dof** = 7 (HR bigravity, ghost-free) + 4 (Dirac on-shell). ✓

**If secondary constraint lost (D2):** $C_g, C_f$ = 2 second-class → remove 2. Total removed: 6 + 2 = 8. Remaining: 24 → **12 dof** = 8 (bigravity with BD ghost) + 4 (Dirac). One extra bosonic dof = the ghost. ✓

Both counts are consistent. The secondary constraint is the difference between 11 and 12 dof — i.e., between ghost-free (D1) and ghost (D2).

---

## Net assessment

| Item | Finding |
|---|---|
| Relative boost propagation | **No** — auxiliary, eliminated by modified SVC. Positive result. |
| Primary constraints (lapse-linearity) | **Banked** — D3 excluded (prior round). |
| Secondary constraint | **UNDETERMINED** — the Dirac correction to $\{C_g, C_f\}$ is structurally non-zero and outside the algebraic class of the HR cancellation. Structural lean: **D2** (~60–65%). |
| Next step | **Lemma S1** — compute the correction in a tractable setting (1+1d or mini-superspace). |
| Deposit impact | **None** — even D1 does not restore symmetric ν (N_eff ≈ 1.52, ~10σ excluded). |

**Landing: D4 — undetermined, structural lean D2.**

---

## Honest statement of what this round establishes and what it does not

**Establishes (original work):**
1. The relative Lorentz parameters (6 components) remain auxiliary under the doubly-coupled Dirac field: they are determined algebraically by the modified SVC, not dynamically. No new propagating dof from the relative-Lorentz sector.
2. The Dirac contribution to the Hamiltonian constraint, after SVC elimination, depends on the square-root matrix $S$ through its matrix elements (from the spatial-derivative/kinetic term), not through the elementary symmetric polynomials that the HR cancellation relies on.
3. The bracket $\{C_g, C_f\}$ receives non-zero corrections from the doubly-coupled Dirac field, specifically from the cross-metric dependence activated by the SVC elimination.
4. These corrections fall outside the algebraic class where the HR secondary-constraint cancellation operates.

**Does not establish:**
1. Whether the corrections actually spoil the secondary constraint (they might cancel due to Clifford-algebra identities, Dirac-bracket effects, or other mechanisms).
2. The explicit form of the modified secondary constraint (or its absence).
3. A non-perturbative proof in either direction.

**Does not restore:**
- No number. No f. No κ. The symmetric ν remains excluded by N_eff regardless.

---

**Sources (this session):** [arXiv:1111.2070](https://arxiv.org/abs/1111.2070) (HR secondary constraint); [arXiv:1203.5783](https://arxiv.org/abs/1203.5783) (vierbein bigravity, SVC); [arXiv:1408.0487](https://arxiv.org/abs/1408.0487) (scalar ghost mechanism). Standard/background: Nelson–Teitelboim 1978 (Dirac canonical gravity). All cited for Cursor Main source-verification.

— Scratch, 2026-10-09. Original work. Filed after pre-registration.
