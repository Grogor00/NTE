# Handoff — AC (Route A, by-hand): the N–t tilt-map propagator bridge — result, confirmed identity, and two honest corrections

**Stream:** AC (Route A, worked by hand with Greg, 2026-07-09), independent counterpart to Cursor's Route B (propagator route, still out — poll 91, no verdict filed).
**To:** Greg (adjudicate / authorise). **Cc:** Cursor (Route B — convergence check on landing), Scratch (constructive leg — converges), Jammer (adversarial — press §5 below), CR (O-series).
**Date:** 2026-07-09
**Priority:** P2 — exploratory, NOT deposit-blocking. Nothing proposed for the corpus.
**Sources:** Scratch constructive Working note (N–t tilt map, 2026-07-08); canonical Part 1 v10.18.0 (§II.0 t = iΔN as Wick; §2.1 dt/dN = 1/(β|Φ|²) = 1/H); Companion 8 v10.18.0 (F1 ℓ = 1/H; F3 §5 open kinetic structure; F4 §6 n_s ← H(N) profile); Companion 9 v10.18.0 (eq. 1 master Lagrangian; §2 constraint reduction); Companion 12 v10.18.0 (a₄ = 0 blocks the a₄-based inflaton kinetic term); Part 3 ledger (n_s, r conditional on open kinetic normalisation K(Φ)).

---

## §0 — Verdict (one line)

**DISTINCTIVE-EXPLANATION, firm on the Gap-2 independence question.** The N–t tilt map closes to

  **tan θ = m / (K(Φ)·H)**,

with the rest mass entering *kinematically* (rest-energy propagator weight balanced against the boundary-tilt kinetic cost), so §VII's δ ∝ m is **reproduced, not assumed** — the map is not "§VII in polar coordinates." The one free input is **confirmed to be the corpus's already-open Φ_NTE kinetic structure** — the same open node n_s and r hang on — not §VII and not a new parameter. Honest cost: the tilt *scale* and the *net power of H* are exactly as open as n_s itself, and close with it. Explanatory tier only; M = K(Φ)·H is pre-lock, no post-lock observable, O1 stands.

---

## §1 — What Route A had to close

Two gaps stood between the tilt map and "firm":

1. **Form I vs Form II** — is θ = arctan(m/M) (rate-ratio, pole at m→∞, no tachyon) or arcsin (bounded amplitude, finite-m pole, tachyon/SICK)?
2. **Independence from §VII** — is tan θ ∝ m a second derivation converging with §VII, or the same δ ∝ y postulate in disguise?

Scratch's constructive leg had already landed DISTINCTIVE-EXPLANATION (soft): Form I forced by the Euclidean-section metric (tan θ = δ/N, opposite/adjacent), 2T→Wick resolved (one Lorentzian time, no ghost), poles clean (m=0 → photon; pure-t → m→∞ unreachable). Soft because the *quantitative* core m ∝ δ was read as pre-existing §VII. Route A's job was to test whether the propagator route hardens the independence.

## §2 — Gap 1: Form I forced (rate, not amplitude)

The propagator delivers m as the **logarithmic rate** of the Euclidean exponential: e^{−imt} with t = iΔN gives e^{+mΔN}, so d(ln G)/dΔN = m — a rate, unbounded above, no ceiling in the free propagator. arcsin requires a **bounded** argument (a normalised amplitude ∈ [−1,1]); to feed a rate into arcsin one must divide by a saturation scale m_max the propagator route does not contain. So Form II is not merely un-tidy — it is **not constructible** from the propagator data without importing an exogenous scale. **arctan forced; tachyon-absence derived from QM + the Wick axiom.** Robust to §VII's saturating-y branch: saturation caps tan θ below 90° (capped arctan), not a finite-m divergence. Converges with Scratch's metric derivation by an independent road.

## §3 — The bridge: variational balance → tan θ = m/(K·H)

The imaginary-time leg carries three coincident roles (from Scratch's reading of Part 1 §2.1.2): **N_I = δ (embedding depth, §VII) = the Wick-rotated time axis (t = i·N_I)**. Time and embedding depth are the same direction; the rest mass sits on the leg that becomes time.

The propagator lands its rate there: e^{−imt} → e^{+m·N_I}. Balance the rest-energy Euclidean weight (pull into the thickness, linear rate m) against the kinetic cost of leaving the boundary (canonical −½(∂Φ)², Companion 9 eq. 1, hence quadratic):

  E(N_I) = m·N_I − ½K·N_I²/τ,  ∂E/∂N_I = 0  ⟹  N_I = mτ/K.

Use the corpus emergent-time relation as the lever — dt/dN = 1/(β|Φ|²) = 1/H (Part 1 §2.1), so proper time over an e-fold span is τ = N/H. Then N_I = mN/(K·H) and

  **tan θ = N_I/N = m/(K·H).**

∝ m forced; photon at m=0 (numerator rate zero, denominator finite); pole at m→∞ unreachable. §VII reproduced: δ = N_I = mN/(K·H), with its proportionality constant now *expressed* via K and H rather than posited.

## §4 — Gap 2: the identity, confirmed against primaries

The denominator normalisation K is **confirmed** to be the corpus's open Φ_NTE kinetic structure, not §VII:

- Companion 9 eq. 1 has a **canonical** Φ_NTE kinetic term — no K(Φ) in the master action. K(Φ) is not fundamental; it is the effective/reduced normalisation after the constraint H = β|Φ|² slaves Φ to H (Companion 9 §2).
- Companion 8 F3 (§5) and F4 (§6) name the open object precisely: the **choice of kinetic structure for |Φ_NTE|** — "(∂Φ)² vs (∂ℓ)²" — "different kinetic terms yield different on-trajectory V_NTE." Companion 9's canonical term is a *working* choice, not committed.
- F1 fixes ℓ = 1/H = 1/(β|Φ|²) as the thickness. The tilt-cost in §3 is charged in exactly that thickness variable (N_I ≈ ℓ). So the cost of tilting into the thickness **is** the (∂ℓ)² kinetic structure Companion 8 floats as the open candidate.

Therefore K in tan θ = m/(K·H) **is** the corpus's open Φ_NTE kinetic structure — the same node n_s and r are conditional on (Part 3 ledger). One closure feeds all three: tilt scale, n_s, r. Grounding on that node: cleanest closure route is the S³ boundary spectral action's Euclidean saddle (Companion 8 §6, target of Companion 9); the heat-kernel route is *blocked* (a₄ = 0 ⟹ no a₄-based inflaton kinetic term, Companion 12); and Companion 9's saddle delivers T_GB cleanly but does **not** pin n_s. The tilt map plugs into that single open node; it introduces no new unknown.

## §5 — Two honest corrections (for Jammer to hold me to)

1. **The net power of H is open — withdraw the "KH² excluded" claim.** K(Φ) runs with the field (Φ ∝ √H, Companion 8 eq. 2), so it stays formally dimensionless while carrying real H-dependence; the (∂ℓ)²-vs-(∂Φ)² choice alone injects up to ~H^{−3} (ℓ = 1/H ⟹ dℓ/dΦ ∝ H^{−3/2}). So M = K(Φ)·H has **one explicit power of H** (from τ = N/H) **plus whatever the open kinetic structure adds**. Dimensional analysis does not settle it.
2. **n_s does not hang on K alone.** F4 makes n_s a function of the H(N) profile (P0–P4 table); the kinetic structure is one of three equivalent routes to pin H(N) (the others: boundary spectral action; HH instanton). Precise tie: tilt map and n_s/r are downstream of the same open **kinetic-structure sector**, not literally the same scalar in two formulas.

## §6 — Where it leaves firm/soft, and the convergence target

Gap 1: closed (arctan forced, tachyon-absence derived). Gap 2: **firm** — mass enters kinematically, §VII reproduced, and the one free input is the independently-open inflationary kinetic sector, so the map is genuinely not §VII relabelled. The residual (scale + net H-power) is real but **shared with n_s/r** and closes with them. Net: the soft→firm upgrade Scratch's leg lacked, bought honestly, with the residual named exactly.

**For Cursor's Route B (convergence check):** does the independent propagator line also land the denominator on the Φ_NTE kinetic structure with a coeff-1 kinematic numerator? Hit = two derivations converge → eligible for CR + Greg as an emergent-time exposition upgrade. Miss (e.g. denominator fixed only by the §VII embedding scale) = divergence flag → stays soft.

**What CR should press (O-series):** the tilt map is conditional on the same open kinetic structure as n_s and r, and stands or falls with it. It does not overturn O1 — M = K(Φ)·H is pre-lock, no post-lock observable — but it gives the t = iΔN axiom a derived explanatory role (mass-dependent proper-time embedding + tachyon-absence) that O1 correctly said the bare sub-claim lacked.

## §7 — Routing

- **Verdict:** DISTINCTIVE-EXPLANATION, firm on Gap-2 independence; tan θ = m/(K(Φ)·H); K = confirmed open Φ_NTE kinetic structure (= n_s/r node); Gap 1 arctan forced; two corrections logged (H-power open; n_s via H(N)).
- **Not deposit-blocking (P2).** Nothing proposed for the corpus.
- **Jammer:** press §5 — argue the rate→extent balance smuggles the linear result; test whether the kinetic-structure identification is load-bearing or decorative.
- **Route:** AC → Greg; hold beside Cursor Route B on its return; adjudicate the two side by side.

— AC (Route A, by-hand), 2026-07-09. tan θ = m/(K(Φ)·H); mass kinematic, §VII reproduced; K = the open inflationary kinetic node (n_s/r), scale and H-power open and shared; firm on independence, explanatory tier, O1 stands.
