# CPN Universe-Pair T1 Jammer-Side Parity Computation — VERDICT: PASS-DERIVED (Claude Jammer)

**From:** Claude Jammer (specialist session — Session 1 deliverable for the CPN universe-pair adversarial stress-test; Jammer-independent counterpart to Cursor Task CPN-T1)  
**To:** AC (verdict destination), Cursor Main (convergence-check counterpart), Scratch (cc; the corpus foundation reader)  
**Cc:** Greg  
**Date:** 2026-06-17  
**Priority:** P1 — load-bearing target; root of the same-t reading  
**Re:** `Working/Working_CPN_Universe_Pair_SameT_Mirror_Adversarial_StressTest_Opening_Scoping_Claude_Jammer_20260617.md` §3.1 (T1 scoping); `Handoff_AC_to_Jammer_CPN_Universe_Pair_SameT_Mirror_20260617.md` (AC brief)

---

## §0 — Executive verdict

**T1: PASS-DERIVED.**

The same-t reading is structurally forced by canonical NTE corpus content. Specifically:

> *Under CPN (real-orthogonal involution at fundamental level, with C trivial on a real scalar and P trivial on the field representation), Φ_NTE(N) → Φ_NTE(−N). The corpus's Janus / bilateral Z₂ discipline + symmetric Hartle–Hawking boundary conditions force the inflaton profile Φ_NTE(N) to be even in N, so |Φ_NTE|² is CPN-invariant. β_NTE is a calibration constant, trivially invariant. The outward-|ΔN| orientation for emergent t is derived from the canonical Hartle–Hawking gauge-birth structure (Companion 9 §3 + corpus §22.14) — both Lorentzian sectors emerge from the saddle with positive proper time outward. Combining: dt is even under CPN; both halves run t forward; P2 is proven.*

**Stronger than my opening prior** (PASS-CONDITIONAL) — the three conditions ARE derived from canonical corpus content, not postulated. The convergence-check awaits Cursor Task CPN-T1 return.

---

## §1 — The question

The emergence law for NTE's emergent time is:

$$dt = \frac{dN}{\beta_{\text{NTE}} \, |\Phi_{\text{NTE}}|^2}$$

Under CPN (the candidate fundamental mirror), N → −N. The brief's load-bearing question:

> *Does the CPN action on the emergence law leave dt EVEN (both halves run t forward, same-t reading; T1 PASS) or ODD (t flips between halves, same-t reading dies, claim collapses back to ordinary CPT; T1 FALSIFIED)?*

The verdict requires:
1. **Crux #1:** Show |Φ_NTE|² is CPN-invariant
2. **Crux #2:** Show β_NTE is CPN-invariant
3. **Crux #3:** Derive the outward-|ΔN| orientation for emergent t from canonical structure (not postulate)

If all three derive: dt EVEN under CPN; T1 PASS.

---

## §2 — Canonical CPN action on Φ_NTE

Per the doubly-ratified two-Scratch C-route closure (AC 2026-06-10 23:28Z):

> *Fundamental CPN is a real-orthogonal involution on 𝕆₊⊕𝕆₋ (pre-EWSB; no unitary/antiunitary dichotomy yet defined). Once the emergent ℂ switches on at EWSB, CPN lifts to unitary. The modular conjugation J = K∘U is the antiunitary emergent CPT.*

The inflaton dynamics relevant for T1 are at the **gauge-birth scale** (T ~ M_R = 8.2×10¹⁴ GeV; pre-EWSB by many orders of magnitude). At this regime CPN is the real-orthogonal involution at fundamental level.

Φ_NTE per Necessity v0.3 is a **real, constraint-bound scalar** with V depending only on |Φ_NTE|² (Lagrange-multiplier μ enforcing |Φ_NTE|² ≥ Φ_min² at lock surfaces).

For a real scalar field, the three CPN components act as:

| Component | Action on neutral real scalar Φ(x, N) |
|---|---|
| **C** charge conjugation | Trivial (no charge to flip; field unchanged) |
| **P** spatial parity | Trivial on field representation; reflects spatial argument: Φ(x, N) → Φ(−x, N) |
| **N** the new NTE operation | Reflects N argument: Φ(x, N) → Φ(x, −N) |

Combined:

$$\Phi_{\text{NTE}}(\mathbf{x}, N) \xrightarrow{\text{CPN}} \Phi_{\text{NTE}}(-\mathbf{x}, -N)$$

For the canonical inflaton setup (homogeneous background), Φ_NTE depends on N only:

$$\Phi_{\text{NTE}}(N) \xrightarrow{\text{CPN}} \Phi_{\text{NTE}}(-N)$$

---

## §3 — Crux #1: |Φ_NTE|² is CPN-invariant (DERIVED)

**Claim:** |Φ_NTE(N)|² = |Φ_NTE(−N)|² for the canonical inflaton trajectory.

**Derivation:**

The canonical inflaton Lagrangian on the bilateral NTE substrate is:

$$\mathcal{L} = \frac{1}{2} K(\Phi_{\text{NTE}}) (\partial \Phi_{\text{NTE}})^2 - V(|\Phi_{\text{NTE}}|^2)$$

with K(Φ_NTE) = 1 as the default (per the K(Φ) physics call ratified 2026-06-16 — minimally-coupled-constraint-bound-real-scalar default) and V depending only on |Φ_NTE|² (Necessity v0.3 constraint structure).

The equation of motion derived from this Lagrangian is symmetric under N → −N because:
- K(Φ_NTE) = 1 (constant) → invariant
- V(|Φ_NTE|²) → V(|Φ_NTE(−N)|²) — the form depends only on the modulus, and we're checking the value at the reflected point
- (∂Φ_NTE/∂N)² → (∂Φ_NTE/∂(−N))² = (∂Φ_NTE/∂N)² — squared, invariant

So the EOM is Z₂-symmetric under N → −N.

**Boundary conditions** at the lock surface N = N_lock (conventionally N = 0) are the canonical Hartle-Hawking saddle conditions:
- Φ_NTE = Φ_max (the Euclidean turning point, where the slow-roll potential's leading behavior begins)
- ∂Φ_NTE/∂N = 0 (smooth Euclidean ↔ Lorentzian matching — Hartle-Hawking ground-state condition)

Both boundary conditions are **invariant under N → −N** by construction (they specify the field value and its derivative at the symmetric point N = 0).

**Standard result for symmetric ODE + symmetric boundary conditions:** the solution is either even or odd under the symmetry. For the slow-roll inflaton with the boundary conditions above:
- Φ_NTE(N) is **even** in N (the field rolls down the same potential in both directions from the turning point)

Therefore:

$$\Phi_{\text{NTE}}(N) = \Phi_{\text{NTE}}(-N) \implies |\Phi_{\text{NTE}}(N)|^2 = |\Phi_{\text{NTE}}(-N)|^2$$

**Crux #1 PASS — derived from canonical Janus / bilateral Z₂ discipline + symmetric Hartle-Hawking boundary conditions.**

**Honest note on what this rests on:** the derivation assumes (a) K(Φ_NTE) = 1 default (yesterday's K(Φ) physics call), (b) V depends only on |Φ_NTE|² (Necessity v0.3 constraint structure), (c) bilateral Z₂ as a symmetry of the action (canonical NTE Janus discipline), (d) symmetric Hartle-Hawking ground-state boundary conditions (Companion 9 §3). If any one of these were broken (e.g., a CP-violating coupling at the fundamental level), the parity could fail. The corpus has CPN as exact at the fundamental level (per the unitary CPN determination + Octonion Extension §2.3); CP-violation enters only in the emergent post-EWSB layer. **No fundamental-level CPN-breaking enters.**

---

## §4 — Crux #2: β_NTE is CPN-invariant (TRIVIAL)

β_NTE is the **fundamental NTE coefficient**, set by global calibration to N_total (the e-fold count including the late-time Ω_Λ regime).

It is a **constant** — no spacetime dependence, no field dependence, no coordinate dependence.

Under any spacetime or symmetry transformation (including CPN), constants are invariant by definition.

$$\beta_{\text{NTE}} \xrightarrow{\text{CPN}} \beta_{\text{NTE}}$$

**Crux #2 PASS — trivially.**

---

## §5 — Crux #3: Outward-|ΔN| orientation (DERIVED from Hartle-Hawking)

The brief specifies that "emergent t is oriented by accumulated |ΔN| outward from N_lock, not signed N." The load-bearing question is whether this orientation is **derived** from canonical corpus content or **postulated** as an extra axiom.

**Claim:** The outward-|ΔN| orientation is forced by the canonical Hartle-Hawking gauge-birth structure (Companion 9 §3; corpus §22.14).

**Derivation:**

The canonical NTE gauge-birth architecture (Hartle-Hawking saddle):
- **Pre-temporal Euclidean section** is a smooth saddle solution centered at the lock surface N = N_lock (= 0 by convention)
- **Gauge-birth seam** is the K_ij = 0 maximal-volume slice where Euclidean → Lorentzian transition occurs
- **Lorentzian emergence:** both +N and −N sectors emerge from the saddle as Lorentzian de Sitter-like sections with **positive proper time outward** from the gauge-birth seam

This last point is the load-bearing one. In the Hartle-Hawking framework, the Lorentzian section that emerges from a saddle is a **half-Lorentzian** with proper time increasing outward from the matching surface. The Lorentzian section CANNOT extend to negative proper time toward the Euclidean section (the metric signature would be wrong). So the Lorentzian sector's proper time accumulates only OUTWARD from N_lock.

In the +N sector: t accumulates as N increases from 0 outward. dN > 0; dt > 0.

In the −N sector: t accumulates as N decreases from 0 outward (toward more negative N). The Lorentzian coordinate distance from N_lock is |N| (because N is negative there); dt > 0 corresponds to d|N| > 0, which corresponds to dN < 0.

Formally:

$$t_{+}(N) = \frac{1}{\beta_{\text{NTE}}} \int_0^{N} \frac{dN'}{|\Phi_{\text{NTE}}(N')|^2} \quad (N > 0)$$

$$t_{-}(N) = \frac{1}{\beta_{\text{NTE}}} \int_0^{|N|} \frac{d|N'|}{|\Phi_{\text{NTE}}(-|N'|)|^2} \quad (N < 0)$$

Both expressions are **positive and increasing functions** of the Lorentzian coordinate distance |N| from N_lock. Both halves run t forward.

**This is the outward-|ΔN| orientation.** It is **derived** from the Hartle-Hawking architecture, not postulated. The signature constraint (Lorentzian section requires positive proper time outward from the matching surface) is the load-bearing fact.

**Crux #3 PASS — derived from canonical Hartle-Hawking gauge-birth structure.**

---

## §6 — Net dt parity verdict

Under CPN, the +N sector maps to the −N sector (bilateral exchange via N → −N).

Take a trajectory in the +N sector at Lorentzian coordinate N = +N₀ (corresponding to emergent t = t₀ > 0 via the t_+ formula).

Under CPN, this trajectory maps to a trajectory in the −N sector at Lorentzian coordinate N = −N₀ (corresponding to emergent t = t₀ > 0 via the t_− formula).

**The two emergent-t readings are the same (both t₀ > 0).** Both trajectories share the t axis. CPN does not flip t.

In differential form:

$$dt(N) \xrightarrow{\text{CPN}} dt(-N) = +dt(N)$$

**dt is EVEN under CPN.** T1 PASS-DERIVED.

The same-t reading is structurally forced by:
1. Crux #1 — |Φ_NTE|² invariance (Janus Z₂ + Hartle-Hawking symmetric BCs)
2. Crux #2 — β_NTE invariance (constant)
3. Crux #3 — Outward-|ΔN| orientation (Hartle-Hawking Lorentzian signature)

**All three derive from canonical corpus content.** No extra postulate required.

---

## §7 — Comparison to ordinary CPT in the literature cluster

In the Boyle-Turok / Sakharov / et al. cluster, the partner universe has **reversed t** because the CPT operator includes an antiunitary T. The two halves of the literature pair run in **opposite t directions**, joined at the t = 0 surface.

NTE's CPN-pair reading (per T1 verdict) has **same t** in both halves because:
- **The mirror is CPN, not CPT.** CPN includes N → −N (fundamental coordinate reflection), not T → −T (emergent-time reversal).
- **Emergent t is even under CPN** (per T1 verdict).
- **The Θ-CPN factorisation** (C5 corpus identity, CPT = Θ∘CPN) makes the literature pair the Wick-image (under Θ = Euclidean rotation) of the NTE pair, not a structurally distinct partner.

**The same-t reading is genuinely distinct from the reversed-t literature reading.** They are Θ-related descriptions of one seam.

---

## §8 — What this verifies, what it doesn't

**Verified:**
- **P2** (emergent t even under N → −N; both halves run t forward) — DERIVED from canonical corpus
- **P1** (mirror is CPN; emergent t not an argument) — implicit and consistent
- **P3** (CPT = Θ∘CPN; structural framing) — consistent (this was C5 corpus identity used as input, not derived here)
- **P4** (Euclidean instanton joining) — consistent (the Hartle-Hawking architecture is exactly the Euclidean-instanton joining)

**Not yet verified (later targets):**
- **P5** (cross-seam DM channel) — T2 target; my prior is FALSIFIED-AS-LIVE-CHANNEL with salvage to primordial-spectral-imprint reading
- **P6** (uniqueness vs Barbour / B-T / Page-Wootters) — S3 target
- **S1** (Gibbons-Hartle conserved global charge) — separate target
- **S2** (Θ = G-H 𝒮 operator-exactness) — separate target
- **S4** (r-discriminator integrity) — discipline check

**T1 PASS-DERIVED unlocks the cross-seam co-evolution as a structural feature** (the same-t reading is real and rigorously derived). **P5 viability still depends on T2** — whether a live DM channel can exist consistent with P4's Euclidean-instanton-only joining.

---

## §9 — Cross-check architecture

This is the Jammer-side independent T1 deliverable. Cursor Task CPN-T1 (re-routed in `Handoff_Claude_Jammer_to_Cursor_Main_CPN_Three_Cursor_Tasks_RE_ROUTED_Ledger_Targeted_..._20260617.md`) is the convergence-check counterpart.

**Expected outcomes:**
- **Cursor T1 returns PASS-DERIVED:** doubly-confirmed T1 PASS — the adversarial-convergence pattern (10th catch). Route to AC for ratification.
- **Cursor T1 returns PASS-CONDITIONAL** (the weaker form):** essentially-converged with finer-grained framing of what's "derived" vs "default"; route to AC; either accept the weaker reading or sharpen.
- **Cursor T1 returns FALSIFIED:** **divergence with the Jammer-side verdict.** Routes to AC immediately for adjudication; identify which derivation step is in error. The most likely sources of divergence would be: (a) different reading of the canonical CPN action on Φ_NTE (especially at the C component); (b) different reading of the Hartle-Hawking BC structure; (c) discovery of a CPN-breaking term I missed.
- **Cursor T1 returns NEEDS-MORE:** the parity is not determined at the level of detail Cursor could reach; route to additional adversarial pass.

**Honest disclosure of what could be wrong on the Jammer side:**
- I assumed the slow-roll inflaton is the canonical structure; if Φ_NTE has additional coupling (e.g., to a CP-odd auxiliary field) at the fundamental level, this could break the Z₂ symmetry of the action
- I assumed Hartle-Hawking ground-state BCs; if the relevant saddle is a different one (e.g., Vilenkin tunneling), the BCs could differ
- I assumed K(Φ_NTE) = 1 default per yesterday's K(Φ) physics call; if the default fails on closer inspection, Crux #1's EOM-symmetry argument could shift

These are the failure modes the convergence-check is designed to catch.

---

## §10 — Discipline (binding)

- T1 verdict is **PASS-DERIVED** (Jammer-side, independent computation); awaits Cursor convergence check
- No corpus patch from this deliverable (per the CPN-pair brief's standing rule: nothing touches corpus until full verdict + Greg authorization)
- This deliverable advances Session 1 of the multi-session schedule per `Working/Working_CPN_Universe_Pair_..._Opening_Scoping_..._20260617.md`
- Session 2 (T2 verdict via Cursor toy junction) is downstream — awaits Cursor execution + my own T2 work
- E1–E7 not applicable here (no external framework invoked; the computation is purely NTE-internal)
- Canonical bilateral / mirror / Janus discipline throughout (positive form)
- Pre-ship grep applies to any forthcoming publication-bound material

---

— Claude Jammer (specialist session, T1 Jammer-side parity computation; verdict PASS-DERIVED; awaits Cursor T1 convergence check), 2026-06-17.
