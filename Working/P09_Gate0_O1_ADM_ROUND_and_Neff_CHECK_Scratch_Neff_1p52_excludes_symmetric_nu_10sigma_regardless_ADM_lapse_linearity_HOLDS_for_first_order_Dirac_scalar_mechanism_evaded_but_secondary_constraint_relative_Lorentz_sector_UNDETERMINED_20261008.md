# P09 Gate-0 (O1) — ADM round + N_eff check — Scratch

**Two results, in the sequence Greg set.**
- **Task A (N_eff), first and decisive:** the symmetric doubly-coupled Z₂-even neutrino predicts **N_eff ≈ 1.52** in our Friedmann equation, a **~10σ deficit** against the measured 2.86 ± 0.13 — **excluded, parameter-free, and independent of the ghost question.** Jammer's count is confirmed. So for deposit the symmetric-ν route is dead on the thermal count **whatever the ADM analysis finds.**
- **Task B (ADM), landing D4 — undetermined, sharpened:** the first-order Dirac structure **does** keep the two-tetrad Hamiltonian **linear in both lapses**, so **the specific Boulware–Deser mechanism of 1408.0487 is evaded** (Jammer's lapse-linearity sketch holds — the first solid good news for the symmetric ν on the *ghost* question). **But** the ghost's life-or-death in Hassan–Rosen bimetric sits in the *secondary* constraint, and a single spinor coupling to two tetrads breaks the relative local Lorentz to the diagonal, promoting the relative boost to a physical variable that the Dirac symplectic current depends on. **Whether the secondary constraint survives is not settled by lapse-linearity and remains open** — AC's even-odds "ghost returns" (D2) is fully live.

Because Task A ran first, **Task B cannot be a rescue:** the symmetric ν is already excluded, so the ADM analysis is a clean *foundation* question (is two-orientation gravity with a doubly-coupled spinor consistent in principle?), not a route to restoring the neutrino-as-DM. No f; not a route to κ.

**From:** Scratch (construction lead) · **To:** AC, Jammer (attack), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-08 · **Commissioned:** `Arbitration_AC_Spinor_Lapse_Linearity_Gate0_Reopens_Undetermined_ADM_Analysis_Commissioned_20261008.md` (Greg's direction 01:28 NZDT)
**Independence:** blind to Jammer's forthcoming attack on this ADM analysis. Jammer's lapse-linearity *sketch* (relayed in AC's arbitration) is the object I was told to make rigorous and to attack at its three named openings.

---

## PART A — the N_eff check (AC's Task 2)

**Claim under test (Jammer, AC R5):** a symmetric doubly-coupled Z₂-even ν splits its stress between orientations → our orientation sees ~half → N_eff ≈ 1.52 against ACT's 2.86 ± 0.13.

**Independent verification:**
- Standard relativistic count: N_eff = 3.044 (three SM neutrinos, instantaneous-decoupling corrected). ρ_rad = ρ_γ[1 + (7/8)(4/11)^{4/3} N_eff].
- The deposited symmetric reading is **one** Z₂-even ν field, bilaterally supported, whose stress-energy "sources curvature on both sides" (Companion 5 §6; Part 2 §IX). **Energy conservation across the Janus pair** (total energy zero, C5 §5; M_A = M_B) requires its energy to be *shared*, not duplicated: our Friedmann equation sees a fraction of its total. **CPN symmetry (the exact mirror, M_A = M_B) forces that fraction to be exactly 1/2** — no tunable split (**no f**).
- Therefore N_eff(our) = 3.044 × ½ = **1.522**.
- **Against the bands** (computed): vs 2.86 ± 0.13 → **10.3σ** below; vs Planck 2.99 ± 0.17 → 8.6σ; vs a deliberately generous 2.80 ± 0.30 → 4.3σ. **Excluded across every reasonable band.**

**The one honest caveat (and why it does not save it):** if instead *each* orientation independently thermalised a *full, separate* neutrino bath, N_eff = 3.044 and there is no deficit — but that is **not** the symmetric-single-Z₂-even-ν reading under test (it is two independent baths, which also forfeits the bilateral coupling's observable footprint and is a different model). Under the reading AC/Jammer specified, 1.52 holds.

**Task A verdict: CONFIRMED. The symmetric doubly-coupled Z₂-even neutrino is excluded at ~10σ on N_eff, parameter-free, independent of the ghost question. This is decisive against the symmetric-ν route for deposit regardless of Part B.**

---

## PART B — the ADM constraint analysis (AC's Task 1)

### B.0 Pre-registered forks (declared before the analysis)

- **D1** — Hamiltonian linear in both lapses **and** the secondary (BD-ghost-removing) constraint survives → ghost-free for the doubly-coupled spinor → **W-1** on the gravity-sector ghost question.
- **D2** — lapse-linear, but the secondary constraint is **lost** (the relative-boost / relative-Lorentz sector reintroduces the mode) → **ghost returns → W-3.** *(AC's even-odds expectation.)*
- **D3** — lapse-linearity itself **fails** (some first-order subtlety) → scalar-like → **W-3.**
- **D4** — lapse-linear, secondary constraint **undetermined** without the explicit constraint-algebra computation → **W-4, sharpened.** *(My pre-registered expected landing: I can establish lapse-linearity but not close the secondary constraint in one round.)*
- **Failure licensed:** "the constraint is lost and the ghost returns" (D2/D3) is fully available and I do not avoid it.

### B.1 Read set / sourcing (discipline 11)

- **Fetched this session:** arXiv:1408.0487 (the scalar BD-ghost mechanism; the safe exception). 
- **Standard results, cited as background, flagged for Cursor Main source-verification where load-bearing:** canonical (ADM) structure of a Dirac field in gravity, incl. the lapse cancellation — Nelson–Teitelboim 1978 (*Hamiltonian formulation of interacting gravitational and electron fields*); the ghost-free bimetric primary+secondary constraint structure — Hassan–Rosen arXiv:1111.2070; the bimetric vierbein / symmetric-vierbein condition and the relative local Lorentz — Hinterbichler–Rosen arXiv:1203.5783. Cursor Main confirmed **no paper** does the two-tetrad single first-order-fermion Hamiltonian analysis (1511.01485 is composite/mini-superspace only) → **the two-tetrad combination below is original work.**
- My load-bearing *positive* claim (B.3, lapse cancels for a first-order field) is elementary and derived inline; I do **not** claim to have resolved the secondary constraint (B.4).

### B.2 Why the scalar gets a ghost (1408.0487), stated so the spinor contrast is exact

A scalar's time-kinetic term is e·g^{00}(∂₀φ)². In ADM, g^{00} = −1/N², and e = N√γ, so the coefficient is **−√γ/N** — the lapse enters as 1/N. With two metrics the conjugate momentum is π_φ = (√γ_g/N_g + √γ_f/N_f)φ̇, and inverting for the Hamiltonian, H ⊃ π_φ²/[2(√γ_g/N_g + √γ_f/N_f)], is **nonlinear in both lapses.** That nonlinearity destroys the primary constraint ∂H/∂N = 0 that removes the BD mode. **The mechanism is specific to the second-order (two-time-derivative) kinetic structure that produces 1/N.**

### B.3 The spinor evades it — lapse-linearity holds (the positive result)

A Dirac field is **first order** in time derivatives. Its time-kinetic term is e·ψ̄γ^a e_a^0 ∂₀ψ. In the time-gauge tetrad the timelike leg is the normal, e_a^0 ∝ n^μ with n^0 = 1/N, so the product **e·e_a^0 = N√γ·(1/N)(leg) = √γ — the lapse cancels.** Hence:
- the conjugate momentum is π_ψ ∝ √γ ψ† (a lapse-independent primary second-class constraint, handled by Dirac brackets);
- the Dirac Hamiltonian is H = N H_⊥ + N^i H_i, **linear in N**; the mass term e·mψ̄ψ = N√γ·mψ̄ψ is **also linear in N**.

**Two tetrads (NTE's symmetric doubly-coupled ν):** each kinetic term carries its own √γ (both lapses cancel, independently):
$$\pi_\psi \;\propto\; \sqrt{\gamma_g}\,A_g + \sqrt{\gamma_f}\,A_f \,,\qquad H \;=\; N_g\,H_\perp^{(g)} + N_f\,H_\perp^{(f)} + N_g^i H_i^{(g)} + N_f^i H_i^{(f)},$$
with A_g, A_f the two time-leg (normal) projectors. **The Hamiltonian is linear in both lapses.** The two primary Hamiltonian constraints H_⊥^{(g)} ≈ 0, H_⊥^{(f)} ≈ 0 therefore **survive** the addition of the doubly-coupled Dirac field.

**Result B.3: D3 is excluded. The first-order structure holds; the two-tetrad Dirac Hamiltonian is lapse-linear; the scalar mechanism of 1408.0487 does NOT arise for a spinor — massive or massless, conformal metrics or not.** Jammer's sketch is correct at the level of the *primary* constraints. This is genuine good news for the symmetric Z₂-even ν on the ghost question.

### B.4 Where it is NOT settled — the three openings (attacking my own construction)

Lapse-linearity gives the **primary** constraints. In Hassan–Rosen bimetric, the BD ghost is removed not by the primaries alone but by a **secondary** constraint, generated by the Poisson bracket of the two primary constraints after a redefinition of the shift (the √(g⁻¹f) sector). The openings AC relayed bear exactly here:

- **Opening 2 (decisive, not addressed by B.3):** a **single** spinor couples to **both** tetrads but transforms under only **one** Lorentz group — so only the **diagonal** local Lorentz survives; the **relative** boost between the two tetrads, normally pure gauge (6 parameters, fixed by the symmetric-vierbein condition), **becomes physical** in the spinor sector. Extra physical variables are exactly where a ghost can hide, and lapse-linearity says nothing about them.
- **Opening 1:** the Dirac symplectic current (√γ_g A_g + √γ_f A_f) **depends on that relative boost**, which lives in the **shift-redefinition sector** the HR secondary-constraint derivation relies on. So the doubly-coupled Dirac matter enters precisely the sector whose structure removes the ghost — and can modify {H_⊥^{(g)}, H_⊥^{(f)}}.
- **Opening 3 (not fatal):** the coefficient of each lapse depends on both spatial metrics γ_g, γ_f. This does **not** by itself reintroduce the ghost — the BD-removing primary constraint comes from lapse-*linearity* (∂H/∂N = constraint), which survives even when the constraint involves both spatial metrics. I rule opening 3 non-fatal.

**The open calculation, named precisely:** compute the constraint algebra {H_⊥^{(g)}, H_⊥^{(f)}} **including the relative-boost-dependent Dirac symplectic current**, after the HR shift redefinition, and determine whether a **secondary constraint** is still generated (→ D1, ghost-free) or whether the relative-boost dof spoils it (→ D2, ghost returns). This is the object no paper in the fetched set computes; it is original and it is where the answer lives.

### B.5 Landing

**D4 — undetermined, sharpened.** The ghost question is **relocated, not resolved:** the *lapse* sector is resolved **favourably** (B.3 — scalar mechanism evaded, D3 excluded), and the live question is now the **secondary-constraint / relative-Lorentz sector** (B.4), where D1 (survives → ghost-free) and D2 (lost → ghost returns, AC's even-odds) are both open pending the one named computation. Gate 0 stays **UNDETERMINED**, but with the locus pinned and the first positive piece banked.

---

## Net for Gate 0 and the sequence

1. **Deposit-decisive (Part A):** the symmetric doubly-coupled Z₂-even neutrino — NTE's *actual* deposited neutrino — is **excluded at ~10σ on N_eff**, parameter-free, **independent of the ghost**. For deposit, this route is closed **regardless of Part B.** (Consistent with AC R5.)
2. **Foundation (Part B):** two-orientation gravity with a doubly-coupled **spinor** evades the scalar BD mechanism (lapse-linearity holds) but its ghost-freedom is **undetermined** pending the secondary-constraint/relative-Lorentz computation. This matters for whether the gravity framework is consistent *in principle*; it does **not** rescue the symmetric ν (Part A already excluded it), which is what keeps Part B clean of the rescue trap.
3. **Recommendation:** Gate 0 remains **W-2/undetermined**; **do not** treat lapse-linearity as a W-1 (it is only the primary-constraint half). Next step is the secondary-constraint calculation (Scratch constructs, Jammer attacks). But note that **even a D1 (ghost-free) outcome does not make the symmetric ν deposit-viable** — N_eff has already excluded it — so the honest framing of any further ADM work is "is the gravity sector consistent in principle," and a *different* (non-thermally-symmetric, non-DM) realization would be needed before N_eff could be revisited, which is Gate-2/P03 territory and not authorized here.
4. **No f; not a route to κ.** Nothing here restores a number. Deposit position unchanged: **P04, adopted ΛCDM, cosmological sector open.**

Sources: [arXiv:1408.0487](https://arxiv.org/abs/1408.0487) (fetched). Standard/background, for Cursor Main source-verification: Nelson–Teitelboim 1978 (Dirac canonical gravity); Hassan–Rosen [arXiv:1111.2070](https://arxiv.org/abs/1111.2070) (bimetric secondary constraint); Hinterbichler–Rosen [arXiv:1203.5783](https://arxiv.org/abs/1203.5783) (bimetric vierbein / relative Lorentz).

— Scratch, 2026-10-08.
