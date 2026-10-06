# ExitAprime VERDICT — Jammer (adversarial): S-1 and E5, plus whether (a′) and route B exclude each other

**Headline:**
- **E1 does not fire.** Adding R² by hand is compatible with Part 3 item 10. It does not touch a₄(D²) and it does not shift the de Sitter curvature.
- **R² cannot be derived from the spectral construction.** There is no route through a₄ on any geometry with any cutoff. The only radiative route needs a Higgs coupling |ξ_H − 1/6| ~ 10⁴–10⁵, which re-imports exit (a)'s problems and clashes with route B, so **E5 fires against every derivation packaging.** The honest register is **added by hand, with its coefficient (≈ 5.6×10⁸) fitted to A_s**, the same register as β_NTE.
- **Two traps are named in advance.** a₄'s 12□R term, and R² ≡ 6·E₄ on the round S⁴ saddle, would each let an addition pass as a derivation.
- **(a′) and route B are *not* mutually exclusive**, unlike (a). The cost is slower, anomaly-only reheating if route B sets ξ_H = 1/6. That corrects my own earlier "needs ξ_H ≠ 1/6 at O(1)".
- **S-3, cross-lane: NO.** R² is scale-invariant, so it adds a constant on any homothety family and cannot restore a scale extremum.
- **New cross-cutting hazard, affecting every exit:** on the constraint trajectory, C9's (1/12)RΦ² term exceeds the Einstein–Hilbert term for H > 8.5×10⁻¹⁰ GeV (T ≳ 25 TeV). At H_inf it exceeds it by 1.7×10²².
- **A quote in the directive is unlocated.** The C12 wording "a₄ non-dynamical per CC; no standalone R², C² ≡ 0 on RW" is not in C12.

**From:** Jammer · **To:** AC · **Cc:** Greg · **Date:** 2026-09-26
**Directive:** `Handoffs\Directive_AC_Exit_a_prime_Starobinsky_R2_Six_Gates_Spectral_Action_Gate_First_20260926.md`
**Register:** findings, not rulings. Nothing patched. Disqualification permitted.

**Blind-protocol disclosure.** A Drive fullText search I ran to locate the directive's C12 quote returned *snippets* of four other lanes' filed (a′) verdicts in `Working\` (Cursor Scratch ×2, Cursor Main, Cursor Jammer). Among them was Cursor Jammer's one-line summary: "S-1 survives only as imported addition; E1 does not fire; E5 fires against any spectral-derivation packaging."
- My S-1/E5 analysis was worked out before that search, but I cannot prove that.
- **So treat convergence with Cursor Jammer on E1/E5 as not fully independent.**
- I opened no other lane's file body.

---

## 0. Read set (discipline 11)

**Read in full this session, this turn:**
- The directive.
- `Core_Papers\Companion_12_Chord_v10_19_0.md`
- `Core_Papers\Companion_14_RW_Spectral_Action_v10_19_0.md`
- `Core_Papers\Companion_15_EPhi_Farnsworth_Spectral_Data_v10_19_0.md`

**Read in full earlier this session, still in context:** Parts 1–3, C8, C9.

**Not read:** C11, C17, C20.

**Negative-finding scope.** The quote "no standalone R²" / "a₄ non-dynamical per CC; … C² ≡ 0 on RW" and the phrase "Λ⁴·volume + Λ²·EH only" were checked as follows:
- C12 read in full: absent. C12 §2 says instead "a₄|_M = 0 … the fixed combination of Weyl-squared and Euler densities … is pointwise zero on the round S³ × flat S¹ product."
- C14 read in full: absent verbatim. C14 §3.3 says "a₄ does not contribute to the dynamical equation for a(t)", which is the nearest match.
- Drive fullText `'standalone R' or 'no standalone'` hit only today's (a′) lane files and unrelated Working files. Nothing in `Core_Papers\`.
- **The substance is right; the attribution to C12 is not.** It is likely a paraphrase of C14 §3.3.

**External, read this session (abstract level):**
- *Rate of gravitational inflaton decay via gauge trace anomaly*, arXiv:1011.3348: "a concrete calculation of the rate that the inflaton field decays into a pair of gauge fields via the trace anomaly."
- Watanabe & Komatsu, gr-qc/0612120 (abstract gave no ξ dependence).

**From background knowledge, not fetched:**
- The conformal covariance of the massless Dirac operator, and hence the R²-free a₄ integrand. C14's own display, −18C² + 11R*R* + 12□R, confirms the form.
- The one-loop R² counterterm ∝ Σ(ξᵢ − 1/6)².
- The scalaron → scalar decay rate ∝ (1 − 6ξ)².

**Scripts:**
- `scratchpad/staro.py`: the R² coefficient, the radiative-ξ estimate, S⁴ integrals and the constraint threshold.
- `scratchpad/hi.py`: the α = 1 map.

---

## 1. Forks declared before computing

- **S-1:**
  - F-contra: R² contradicts item 10.
  - F-compat-hand: compatible, but enters only by hand.
  - F-compat-derived: compatible, and derivable spectrally.
- **E5:** fires / does not fire / fires only against derivation claims.
- **Route B:**
  - X-excl: mutually exclusive, like (a).
  - X-cost: compatible at a cost.
  - X-free: compatible at no cost.

**Where each landed:** F-compat-hand. E5 fires only against derivation claims. X-cost.

---

## 2. S-1, clause 1: compatibility with item 10. **E1 does not fire.**

**What item 10 is about** (Part 3, read): "a₄ ≠ 0 for the untwisted Dirac operator on S³×S¹ …, or C²/E₄ ≠ 0 pointwise there, falsifies the spectral substrate claims." That is a property of the **operator D**, through its heat-kernel coefficient, and of the **geometry**, through its curvature invariants.

**Why the two objects are distinct, established rather than assumed:**
1. **a₄ is fixed by D and g.** A term c∫R²√g added to the gravitational action changes neither the Dirac operator nor the Seeley–DeWitt densities of D². Item 10's a₄ is untouched.
2. **The pointwise invariants on the substrate are fixed by g.**
   - On S³(radius a) × S¹: C = 0 and E₄ = R² − 4Ric² + Riem² = 36 − 48 + 12 = 0, in units of 1/a⁴. Computed.
   - R² = 36/a⁴ ≠ 0 there, but item 10 does not mention R². The added term's *value* on the substrate is nonzero, and that is not what item 10 is about.
3. **The Λ side (C12 §3, "structural, not numeric") is unaffected.** For f(R) = R + cR² − 2Λ, the trace equation f′R − 2f + 3□f′ = 0 on constant R gives −R + 4Λ = 0, so R = 4Λ **independent of c**. Computed. A quadratic term, being scale-invariant, neither sources nor shifts a de Sitter curvature. The unimodular Λ account and "numeric Λ not claimed" both stand.

**Verdict:** R² sits at the same register as the Einstein–Hilbert and ξ-terms of C9 eq. (1), which is Leg 1 in C15 §5's terms. It is compatible with item 10. **E1 does not fire.**

---

## 3. S-1, clause 2 and E5: can R² be *derived*? No. Here is every route.

1. **A different cutoff f.** f enters a₄ only as the overall moment f₀ = f(0) (C14 §2, read). It rescales a₄ and cannot change its integrand. **Closed negative.**
2. **A non-RW geometry.** The a₄ integrand for the Dirac Laplacian is universal: −18C² + 11E₄ + 12□R (C14 §3.3 display, read). There is **no R² on any geometry**. That is the conformal covariance of the massless Dirac operator, and it is the same fact that gives a₄ = 0 on the substrate. **Closed negative.**
3. **Higher coefficients.** a₆ and above carry dimension-6+ invariants (R³, R□R, …), suppressed by Λ⁻². C9 §7 / C15 §6.3's a₆ budget shows they are ~55× short even for the tilt. They cannot mimic a Λ⁰ R² term. **Closed negative.**
4. **Renormalised moments / one loop.** The one-loop R² counterterm is ∝ Σ(ξᵢ − 1/6)² over scalars (background knowledge).
   - With the deposit's scalars conformal (Φ_NTE at 1/6, and the Higgs at 1/6 if route B runs through an action carrying it; see §4), **no R² is generated.**
   - To generate Starobinsky's coefficient c = M²/(12m²) ≈ 5.6×10⁸ (N* = 55; m ≈ 3.0×10¹³ GeV) radiatively needs N_s(ξ − 1/6)²·L/(32π²) ~ c, i.e. **|ξ_H − 1/6| ~ 3–7×10⁴** (for L = 10–40). Order-of-magnitude estimate.
   - That is Higgs inflation's coupling. The route re-imports every (a) defect: D2 at preheating, the D5 clash, the D1 risk.
   - **E5 fires for this route:** the modification needed breaks the conformal account that route B would deposit.
5. **The conformal anomaly (Starobinsky's own 1980 route).** The trace anomaly's □R coefficient is **scheme-dependent**: it can be shifted by a finite local R² counterterm. So "R² from the anomaly" is a choice of that counterterm, not a derivation. **Closed as a derivation; open as a free coefficient.**

**Two traps named in advance** (addition dressed as derivation, the shape the corpus has retired five times this year):
- **Trap A.** a₄'s own **12□R** term (C14 §3.3). Integrated, it is a surface term; its association with R² in the anomaly effective action is the scheme freedom of route 5. **It is not an R² seed.**
- **Trap B.** On the **round S⁴ no-boundary saddle**, ∫R²√g = 384π² and ∫E₄√g = 64π². Both are radius-independent constants, so **∫R² = 6∫E₄ exactly** there. Computed. Any "the spectral action evaluated on the HH saddle contains R²" is a Gauss–Bonnet constant misread. On the saddle the two cannot be told apart; they separate only off the round geometry.

**Register:** R² enters **added by hand**, with its coefficient fitted to A_s (c ≈ 5.6×10⁸ at N* = 55). **E3's second clause fires literally**, as D3's did for (a), at the same register as β_NTE (Part 1 §2.4). Under Greg's adopted-and-credited framing it is credited to Starobinsky (1980), with "not spectrally derived" stated on the ledger.

---

## 4. Are (a′) and route B mutually exclusive? **No: X-cost.**

- **Route B** (Part 3 open; C15 §6.4 item 1) seeks the spectral origin of ξ = 1/6 through a non-metric E(Φ) entry. C15 §3.2 (read) shows NTE's finite triple puts the Higgs data Φ_IJ into E, alongside ¼R·1, "the standard almost-commutative pieces".
- **Inference, not computed in the deposit:** the same mechanism that gives Chamseddine–Connes a conformally coupled Higgs would then give Φ_IJ ξ_H = 1/6. C15 §6.4 lists E as open, so this stays an inference.
- **(a) versus route B:** (a) needs ξ_H ~ 10⁴, so it is excluded (my previous verdict).
- **(a′) versus route B:** (a′) needs only an added R², which route B neither produces nor forbids. Route B fixes ξ; it does not bar extra gravitational terms. **Compatible.**
- **The cost.** With ξ_H = 1/6, scalaron → Higgs decay ∝ (1 − 6ξ_H)² **vanishes**. Pre-EWSB fermions are massless, so that channel is closed too. **Reheating proceeds through the gauge trace anomaly** (arXiv:1011.3348, abstract read: a nonzero inflaton → gauge-pair rate via the anomaly).
  - Order of magnitude: the rate is suppressed by ~(bα/4π)² ~ 10⁻⁴, and T_rh by ~10².
  - N* drops by ≈ (1/12)·ln(10⁸) ≈ 1.5, and n_s shifts by ≈ −0.001.
  - That moves (a′) **further from P-ACT-LB**, by about −0.3σ more. It is an estimate; S-4 and the Cursor literature pass should fix it.
- **Correction, owned:** my (a)-round verdict §4 said scalaron reheating "needs ξ_H ≠ 1/6 at O(1)". That is too strong; the anomaly channel exists. Corrected: ξ_H ≠ 1/6 makes reheating *efficient*, while ξ_H = 1/6 makes it *anomaly-only*. **E4 does not fire on this ground.**
- **On AC's original ξ = 1/6 "suppresses every candidate" inference:** it now fails a second way. Even a fully conformal matter sector reheats through the anomaly.

---

## 5. S-3, cross-lane: does R² restore the nucleation saddle? **No.**

- ∫R²√g is **scale-invariant**: R² ∝ a⁻⁴ and √g d⁴x ∝ a⁴.
- On any fixed-shape homothety family it adds a radius-independent constant (384π² on the round S⁴).
- The 2b theorem's monotonicity (C9 §7; C15 §6.3, read) is therefore preserved exactly. **R² cannot create a scale extremum.**
- The Starobinsky no-boundary instanton exists as an extremum over the *scalaron field value* (Einstein frame), not over overall scale. It does not reopen P1–P3.
- **"Do not stretch for it": not stretched.**

---

## 6. New cross-cutting hazard (all exits, found while checking S-2's premise)

- C9 eq. (1) (read) has the gravitational coefficient F(Φ) = M² + Φ²/6. C8 eq. (2) (read) puts Φ on the trajectory at Φ² = H/β_NTE.
- **Φ²/6 exceeds M² once H > 6β_NTE M² = 8.5×10⁻¹⁰ GeV** (radiation era T ≳ 2.5×10⁴ GeV). **At H_inf ≈ 1.5×10¹³ GeV, Φ²/(6M²) ≈ 1.7×10²².** Computed.
- If Φ is a physical field at its constraint value, the effective Planck mass above ~25 TeV is set by Φ, not M. That changes every early-universe calculation: (a), (a′), BBN-era H, and my own G4 recollapse arithmetic, which used M.
- If instead Φ is only a relabelling in the FRW sector (Part 1 §2.3), then C9's (1/12)RΦ² term cannot be evaluated at that value, and C17's K(Φ) closure, which is built on exactly this F(Φ), loses its footing.
- **The deposit cannot currently have both.** This is the 10²⁰ constraint mismatch appearing again in the gravitational coefficient rather than in the inflaton.
- **Not a ruling. Priority flag for AC**, and it should be resolved before any exit is adopted.
- On my G4 recollapse: the sign argument (ȧ = 0, ρ + 3p > 0) is qualitative. I have not re-checked it in a scalar-tensor frame with F ≫ M². Flagged, not withdrawn.

---

## 7. Summary

| Item | Finding | Disqualifier |
|---|---|---|
| S-1 clause 1 | Compatible with item 10: a₄(D²) untouched, R = 4Λ independent of c. | **E1 does not fire** |
| S-1 clause 2 | Not derivable: f, geometry, a₆+, the anomaly and one-loop routes all closed. Two traps named. Register: by hand, coefficient fitted to A_s. | **E5 fires against derivation packaging only.** E3 clause 2 fires literally. |
| Route B | Compatible (X-cost): anomaly-only reheating if ξ_H = 1/6. N* ≈ −1.5, n_s ≈ −0.001 (estimate). | E4 does not fire |
| S-3 | No: R² is scale-invariant, so no scale extremum. | — |
| Cross-cutting | F(Φ) = M² + Φ²/6 on the constraint dominates above ~25 TeV (10²² at H_inf). | **Priority flag, all exits** |
| Directive | The C12 quote is not in C12; it is likely a paraphrase of C14 §3.3. | — |

— Jammer, 2026-09-26.
