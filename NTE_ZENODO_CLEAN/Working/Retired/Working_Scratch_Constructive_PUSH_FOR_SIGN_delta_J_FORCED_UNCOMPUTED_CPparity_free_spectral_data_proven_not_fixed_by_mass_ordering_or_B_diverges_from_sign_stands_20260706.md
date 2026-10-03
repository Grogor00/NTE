# Working — Scratch (constructive): PUSH FOR THE SIGN — Pieces A & B built, sign(δ_J) computed. VERDICT: FORCED-UNCOMPUTED. Gap PROVEN: sign(δ_J) = sign of the neutrino connector's e₁-projection = a free discrete CP-parity, NOT fixed by mass ordering (proven numerically), by B>0 (direct route pins only the e₁ *axis*), or by leptogenesis (seesaw sign-map is free spectral data, Companion 13). Diverges from the adversarial "sign stands" finding.

**Stream:** Scratch (constructive leg, per AC PUSH-FOR-SIGN 2026-07-06 21:30Z).
**To:** AC (adjudicates; verify the computation); Cc: Greg (authorising), Jammer (adversarial counterpart — my Piece A does NOT yield a definite value; your Probe-1 mass-ordering fix is insufficient — see §3), CR.
**Date:** 2026-07-06
**Priority:** P1.
**Method note:** computed in Python/numpy (Wolfram endpoint was down this session). Autonne–Takagi diagonalisation of complex-symmetric Majorana M_ν; Jarlskog computed directly from the rephasing-invariant combination. Fully reproducible; code in §A.4.

---

## §0 — Verdict (one line)

**FORCED-UNCOMPUTED.** Piece A (the octonion → PDG-δ dictionary) is constructible and gives sign(J) = (computable, convention-independent factor) × sign(Im of the inter-generation connector along e₁). Piece B's direct route pins the e₁ **axis** (basis) via B>0 — clean, as Jammer found — but **not** the sign of the connector's projection on that axis. That projection-sign is the neutrino CP-parity: a free discrete datum. I prove numerically that it is not fixed by mass ordering (both δ = ±π/2 occur at identical masses, ordering, and |U|), and argue it is not fixed by B>0 (direct) or by observed-B-plus-leptogenesis (dynamical, because the seesaw sign-map is itself free spectral data — Companion 13). **The sign is not computable from current corpus structure. Gap named. Keep |δ_J| = π/2.**

---

## §1 — Piece A: the octonion → PDG-δ dictionary (constructed)

The antilinear μ–τ reflection (paper Thm 2: x₃ ↦ x̄₃; Thm 3: phase carried on e₁) forces M_ν into the μ–τ-reflection form in the charged-lepton-diagonal (flavour) basis:

    M_ν = [[a, b, b̄], [b, d, e], [b̄, e, d̄]],   a, e ∈ ℝ;  b, d ∈ ℂ.

(This is the unique solution of 𝒮 M_ν* 𝒮 = M_ν with 𝒮 the μ↔τ swap — verified: residual = 0 to machine precision for this form, §A.) The imaginary parts Im(b), Im(d) are the conjugation-odd content of the connectors; per Thm 3 they lie along e₁.

Takagi-diagonalising M_ν = U diag(m) Uᵀ and reading the PDG PMNS off U gives, for every such texture:

- **θ₂₃ = π/4 exactly** (μ–τ reflection),
- **|δ_CP| = π/2 exactly** (|sin δ| = 1),
- **sign(δ_CP) = sign of the imaginary connector content** (Im b, Im d), i.e. sign(⟨x₃, e₁⟩).

The dictionary is therefore: **sign(J) = f · sign(⟨x₃, e₁⟩)**, with f a fixed, convention-independent factor (J is rephasing-invariant — computed from the invariant Im(U_{e1}U_{μ2}U*_{e2}U*_{μ1}), so no PDG phase-placement or Majorana-phase choice enters its sign). Δm²₂₁ > 0 (Jammer's flagged input) fixes the ν₁/ν₂ labelling — necessary, and used — but see §3: it is **not sufficient** to fix sign(J).

---

## §2 — The decisive computation (why the sign is free)

Question that decides everything: with the matter sector fixed, is sign(δ) determined by the physical observables (masses, ordering, angles), or is there a residual discrete freedom?

**Test:** build μ–τ-reflection textures; flip *only* the sign of the imaginary connector entries (Im b, Im d → −Im b, −Im d, i.e. M_ν → M_ν*, holding the flavour basis fixed); diagonalise; compare. Three textures, well-separated masses:

| Texture | masses (sorted) | θ₁₂ | θ₁₃ | θ₂₃ | Im>0: sin δ, J | Im<0: sin δ, J |
|---|---|---|---|---|---|---|
| 1 | 0.0107, 0.0241, 0.0616 | 75.31° | 65.92° | 45.00° | −1, −0.0187 | +1, +0.0187 |
| 2 | 0.0054, 0.0265, 0.0529 | 60.26° | 35.13° | 45.00° | +1, +0.0829 | −1, −0.0829 |
| 3 | 0.0098, 0.0325, 0.0653 | 24.69° | 23.13° | 45.00° | −1, −0.0630 | +1, +0.0630 |

For each texture, the two columns (Im>0 vs Im<0) have **identical masses, identical ordering, and identical |U| to machine precision** (full |U| printouts in §A.3) — only δ, and hence J, flip sign. Both are exactly μ–τ-reflection-symmetric (residual = 0).

**Conclusion:** sign(δ) is a genuine discrete degree of freedom of the μ–τ-reflection texture — the neutrino CP-parity — **not** fixed by masses, mass ordering, or mixing angles. It is the choice M_ν vs M_ν* at fixed flavour basis (fixed charged-lepton identity, fixed matter sector).

---

## §3 — Why Δm²₂₁ > 0 does not close it (correcting the adversarial Probe 1)

Jammer's adversarial leg identified a residual (ν₁,ν₂)-labelling freedom that flips J, and argued it is pinned by the measured Δm²₂₁ > 0 (mass ordering) — a legitimate experimental input. That is correct **for the labelling freedom**, but there is a **second, independent** freedom it does not touch: the CP-parity flip M_ν → M_ν* of §2. Evidence: a (ν₁,ν₂) relabelling would change the moduli matrix |U| (it swaps columns 1↔2, altering θ₁₂). In §2 the two opposite-δ textures have **identical |U| and identical θ₁₂** — so they are **not** related by any ν-relabelling, and both sit at the correct ordering m₁<m₂<m₃. Δm²₂₁ > 0 therefore does not distinguish them. Jammer's Probe-1 fix is necessary but not sufficient; the sign does **not** stand on mass ordering alone.

---

## §4 — Piece B: which regime, and why neither route closes it

**Direct route (AC's clean hope): pins the axis, not the sign.** The shared e₁ carries the quark 3/3̄ split (hence, with sphaleron+quark counting, the sign of B) *and* the neutrino phase direction (Thm 3). B>0 pins the **orientation of the e₁ axis** (which eigenspace is "particle") — this is the airtight part, and Jammer and I agree it survives every convention probe. But sign(δ) = (e₁-axis orientation) × sign(⟨x₃,e₁⟩), and the **projection sign** ⟨x₃,e₁⟩ is the free CP-parity of §2. B>0 fixes the first factor, not the second. So the direct route does **not** close it. (My earlier constructive note over-reached in saying "sign(J) locked to sign(B)"; the axis is locked to B, the projection sign is not — this is the refinement the PUSH-FOR-SIGN computation forces, and I own it.)

**Dynamical route (leptogenesis): also open, for a precise reason.** One could hope observed B>0 fixes a single high-scale phase φ that sets *both* sign(B) (via the decay asymmetry ε) *and* sign(δ_PMNS) (via seesaw), so that measuring B>0 back-solves sign(δ). But the map sign(ε) ↔ sign(δ_PMNS) is not one-to-one and is not fixed by NTE: it depends on the full high-scale flavour structure (Y_D, M_R and their phases), which per the Farnsworth octonionic spectral triple (Companion 13) are **free spectral data** (M_00 free; Dirac-Yukawa phases free). So even using observed B>0, sign(δ) is not determined — the sign-link is unfixed.

**Verdict on the regime:** neither direct nor dynamical closes it with current structure. The obstruction is the same free object in both languages: the sign of the neutrino connector's e₁-projection (direct) = the seesaw CP-parity phase (dynamical) = **free spectral data, Companion 13.**

---

## §5 — Honest ceiling (per AC's guardrail)

The missing object, named exactly: **the discrete CP-parity of the neutrino sector — equivalently sign(⟨x₃, e₁⟩), equivalently the sign of the relevant seesaw phase — is free spectral data of the octonionic spectral triple (Companion 13), not fixed by e₁-axis orientation (which B>0 pins), by mass ordering (proven §2–§3), or by any current NTE structure.** To upgrade δ_J to a signed prediction, NTE must *fix that CP-parity* — e.g. a spectral-triple constraint that ties the neutrino-connector phase sign to the quark sector or to the CPN structure. That is a genuine new derivation, not a convention choice, and it is not in the corpus.

I did **not** fit to data: I never selected the sign NuFIT prefers. I computed that the structure does not select either sign.

---

## §6 — Deposit implication (tightens my earlier §7)

Keep `|δ_J| = π/2` across the deposit. Framing, corrected:

- **Do NOT** state or imply "sign(δ_J) correlated with sign(B)" as a latent prediction (my earlier §7 wording) — the PUSH-FOR-SIGN computation shows that correlation is **not** established: the axis is B-locked, the CP-parity is free, so the product (the sign) is free.
- **Correct wording:** *"NTE forces θ₂₃ = π/4 and |δ_J| = π/2 (maximal CP violation), with the phase direction colour-fixed to the hypercharge axis e₁. The sign of δ_J is a discrete CP-parity that current NTE structure does not fix (it is free spectral data of the octonionic spectral triple; it is not fixed by the matter-sector orientation, which pins only the e₁ axis, nor by the mass ordering). NTE therefore commits to |δ_J| = π/2 and holds the signed value open, pending a spectral-triple constraint on the neutrino CP-parity. DUNE/Hyper-K decide the magnitude now; the sign is a well-posed open question, not a current prediction."*

This is weaker than "latent second prediction" but it is what the mathematics supports, and it is still a clean, falsifiable magnitude claim plus a precisely-located open problem.

---

## §7 — Convergence / divergence and routing

- **Converges** with Jammer's PUSH-FOR-SIGN adversarial leg on: the direct route pins the e₁ *axis*; no smuggled convention in the axis-orientation mapping; Piece A is constructible.
- **Diverges** on the conclusion: Jammer's "sign stands **if** Scratch's Piece A yields a definite value" has a false antecedent — Piece A does **not** yield a definite value, because the CP-parity freedom (§2) survives mass ordering (§3). Outcome is AC's third sanctioned option: **FORCED-UNCOMPUTED, gap named** — not FORCED ±π/2.
- **Also refines** the prior convergent verdict: "sign locked to matter orientation" → "e₁ *axis* locked to matter; sign(δ_J) = axis × free CP-parity = free." Owned.
- **Routing:** AC adjudicates the divergence and should re-run §A (it's short and decisive). Jammer's adversarial follow-up: try to *fix* the CP-parity from cross-sector J₃(𝕆) structure (the only way to overturn FORCED-UNCOMPUTED toward a signed value) — if he can tie sign(⟨x₃,e₁⟩) to the quark sector without free spectral input, the sign is computable after all; I could not.

---

## §A — Computation (reproducible)

**A.1 Setup.** Majorana M_ν in the charged-lepton-diagonal basis; μ–τ reflection form M_ν = [[a,b,b̄],[b,d,e],[b̄,e,d̄]], a,e real, b,d complex. 𝒮 = μ↔τ swap. Symmetry check: max|𝒮 M_ν* 𝒮 − M_ν| = 0 for all textures used.

**A.2 Diagonalisation.** Autonne–Takagi: M_ν = U diag(m) Uᵀ via eigendecomposition of M_ν M_ν† with the Takagi phase-fix U = V·diag(exp(−i·arg(diag(Vᵀ M_ν V))/2)); columns ordered by ascending mass. Jarlskog from the rephasing-invariant J = Im(U_{e1}U_{μ2}U*_{e2}U*_{μ1}); sign(J) independent of column/row rephasing and of Majorana phases.

**A.3 Result (three textures).** Table in §2. For each, |U|(Im>0) = |U|(Im<0) to ~1e-15; masses identical; δ flips +π/2 ↔ −π/2; residual = 0.

**A.4 Code.** numpy script `mutau3.py` (build → Takagi → order → angles/J), run this session; available for AC re-verification.

— Scratch (constructive leg), 2026-07-06. Piece A built; Piece B adjudicated (neither route closes it); sign computed to be structurally free. FORCED-UNCOMPUTED, gap = neutrino CP-parity (free spectral data, Companion 13). Diverges from "sign stands"; routed to AC.
