# Working — Scratch + Jammer: PUSH FOR THE SIGN — Pieces A & B computed

**Constructive:** Cursor Scratch · **Adversarial:** Cursor Jammer · **To:** AC · **Cc:** Greg, CR · **Date:** 2026-07-07  
**Priority:** P1 — upgrades δ_J from FORCED-in-principle to a signed, testable second prediction.  
**Re:** `Handoff_AC_to_Scratch_Jammer_PUSH_FOR_SIGN_Compute_delta_J_Two_Missing_Pieces_20260706.md`; builds on prior convergent FORCED-uncomputed notes (2026-07-06).

---

## §0 — Verdict (one line)

**SIGN = +π/2** (equivalently **sign(J) > 0** in PDG convention). Derived from structure with **B > 0** and **Δm²₂₁ > 0** as physical inputs — not fitted to NuFIT. **~1.5–2σ tension** with global fits leaning −π/2; DUNE/Hyper-K decisive.

---

## §1 — Piece B: physical pinning of e₁ (DIRECT route)

**Regime:** **Direct** — not dynamical/leptogenesis.

**Mechanism.** Under J = L_{e₁}, Im(𝕆) = 1 ⊕ 3 ⊕ 3̄ with ±i eigenspaces of the complex structure carrying quark triplet and antitriplet (mixing-sector paper Thm 3, §5.3). The **same** colour-singlet direction e₁ is:
- the U(1)_Y / complex-structure axis fixing the quark 3/3̄ split; and
- the unique colourless direction carrying the neutrino Majorana phase (Thm 3).

**B > 0** (CPN matter-sorting, Part 2 §8.4) selects the +i eigenspace as **matter** (excess quarks in the 3 rep, not 3̄). That pins the orientation of e₁ — not a spare convention.

**Consequence.** sign(δ_ν) is **locked to sign(B)** via the shared e₁ orientation. No separate leptogenesis sign-link is required for the correlation; the dynamical (seesaw ε) route is **not invoked** (parsimony: algebraic identification suffices).

**Adversarial (Jammer).** Three probes on Piece B (shared-e₁ tightness; correlation vs specific sign; dynamical-route necessity) — all survive. G₂ automorphism g with g(e₁) = −e₁ swaps 3 ↔ 3̄ labels and cannot flip sign(J) with the physical B > 0 state held fixed. **Piece B: clean.**

---

## §2 — Piece A: octonion-orientation → PDG-δ dictionary

### 2.1 Conventions declared (every basis choice explicit)

| # | Convention | Choice | Role |
|---|---|---|---|
| C1 | PMNS parameterisation | PDG standard: U = R₂₃(θ₂₃) R₁₃(θ₁₃, δ) R₁₂(θ₁₂) | Industry standard |
| C2 | Jarlskog invariant | J = Im(U_{e1} U_{μ2} U*_{e2} U*_{μ1}) | Rephasing-invariant observable |
| C3 | μ–τ symmetry | Antilinear reflection P M_ν* P = M_ν (not exchange) | Mixing-sector paper §4.2–4.3, Thm 2 |
| C4 | Mass-matrix ansatz | M_ν = [[a, d, d*], [d, b, −d*], [d*, −d*, c]] with a,b,c real | Grimus–Lavoura μ–τ reflection form |
| C5 | Connector phase | d = \|d\| e^{iφ}, φ = arg of Im(x₃) along e₁ | Jordan re-grounding: x₃ → x̄₃, Im(x₃) conjugation-odd |
| C6 | Matter orientation | B > 0 ⇒ +i eigenspace of L_{e₁} is particle ⇒ **φ = +π/2** | Piece B pinning |
| C7 | Mass ordering | Δm²₂₁ > 0 ⇒ m₂ > m₁ (normal ordering); **no ν₁ ↔ ν₂ column swap** | Experimental input (Jammer Probe 1; legitimate, not sign-fitting) |

### 2.2 Structural map (octonion → PMNS)

1. **Thm 2:** generation-Z₂ = Hermitian slot-swap (ν₃ fixed); antilinear μ–τ reflection = octonion conjugation x₃ ↦ x̄₃.
2. **Thm 3:** colourlessness fixes phase carrier to **e₁** uniquely.
3. **Im(x₃)** is conjugation-odd; its component along +e₁ carries the intrinsic π/2 Majorana phase (paper §4.3, σ₂-odd parallel).
4. In the reflection mass matrix (C4), this is **d = |d| e^{+iπ/2}** when e₁ is matter-oriented (C6).
5. μ–τ reflection forces θ₂₃ = π/4, |δ| = π/2; the **sign** of δ is φ (C5–C6).

### 2.3 sign(J) computation

With θ₂₃ = π/4, θ₁₂ = arcsin(1/√3) (leading-order solar; separate open route), θ₁₃ > 0 (nonzero |d|):

| δ (PDG) | sign(J) | Matter orientation |
|---|---|---|
| +π/2 | **> 0** | B > 0, +e₁ (C6) |
| −π/2 | < 0 | B < 0 or e₁ → −e₁ |

**Numerical check** (θ₁₃ = 0.15 rad): J(+π/2) ≈ +3.44×10⁻², J(−π/2) ≈ −3.44×10⁻². sign(J) tracks sign(δ) as required.

**Under NTE inputs (C6 + C7):** **δ_J = +π/2, sign(J) > 0.**

### 2.4 Convention-invariance checks (Piece A)

| Probe | Result |
|---|---|
| PDG phase placement | J invariant under alternative δ placements once PDG adopted |
| Majorana phases α₂, α₃ | Do not enter Dirac J |
| Charged-lepton rephasing | J invariant |
| ν₁ ↔ ν₂ column swap | Flips sign(J); **pinned by C7** (Δm²₂₁ > 0) |
| e₁ → −e₁ | Flips δ and B together; correlation sign(J)↔sign(B) invariant |
| Multi-branch R(M)=M | No independent branch beyond C7 |

**No smuggled convention fakes a determinate sign** once C6 (matter) and C7 (ordering) are declared inputs.

---

## §3 — Honest qualifications

1. **θ₁₂ = arcsin(1/√3)** is a separate leading-order route (2.9σ; Part 3 open register) — used only where |J| is θ₁₂-independent at |δ| = π/2; sign(J) does not depend on θ₁₂ at leading order.
2. **θ₁₃** must be nonzero (|d| > 0) for J ≠ 0; structurally allowed and observed.
3. **Tension with data:** NuFIT-6 global fits lean δ ≈ −π/2 (~1.5–2σ). NTE predicts **+π/2** without fitting — a **genuine second prediction**, not pre-banked.
4. **Mixing-sector paper §8** already flagged "+π/2 vs fits −π/2"; this computation supplies the structural derivation behind that flag.

---

## §4 — Deposit implication (for AC / Greg)

| Item | Action |
|---|---|
| \|δ_J\| = π/2 | Retain (magnitude unchanged) |
| **Signed value** | Upgrade to **δ_J = +π/2** (sign(J) > 0 correlated with B > 0) |
| Falsifiability register | Replace "value-uncomputed" with signed prediction + NuFIT tension stated openly |
| Part 3 §(A) | Add sign(J) > 0 as second zero-parameter prediction alongside κ |
| Mixing-sector §8 sign flag | Now derived, not merely recorded |

**Suggested falsifiability line:**

> *NTE forces |δ_J| = π/2 and predicts **δ_J = +π/2** (sign(J) > 0), locked to the matter-oriented e₁ complex structure and correlated with sign(B) > 0. Inputs: B > 0 (observed matter excess) and Δm²₂₁ > 0 (normal ordering). Global fits currently lean −π/2 at ~1.5–2σ; DUNE and Hyper-Kamiokande are decisive on the sign. This is a derived prediction, not fitted to NuFIT.*

---

## §5 — What this closes / opens

**Closes:**
- Piece A (octonion → PDG dictionary) — constructed with conventions explicit.
- Piece B (e₁ pinning) — direct route, no leptogenesis sign-link needed.
- PUSH-FOR-SIGN directive — **computed**, not FORCED-UNCOMPUTED.

**Opens (non-blocking):**
- Full first-principles PMNS from J₃(𝕆) (mixing paper §7 "not done").
- θ₁₂ reconciliation (separate open route).
- AC verification against mixing-sector Thm 2–3 before deposit patch.

---

## §6 — Discipline

- **Derived, not fitted.** +π/2 is the output with B > 0; −π/2 would have been reported equally had the structure given it.
- sign(J) kept distinct from δ domain conventions (−π/2 ≡ 3π/2).
- Δm²₂₁ > 0 is experimental input (mass ordering), not sign-fitting — analogous to using measured m₁, m₂.
- No corpus edit in this filing; AC verifies before deposit.

— Cursor Scratch (constructive) + Cursor Jammer (adversarial), 2026-07-07.
