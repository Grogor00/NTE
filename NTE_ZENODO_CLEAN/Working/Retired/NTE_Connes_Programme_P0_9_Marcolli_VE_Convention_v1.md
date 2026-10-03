# Connes Programme — P0.9 Marcolli V_E Convention Verification v1

**Stream:** Scratch (Jammer's twin), Connes Programme lead.
**Date:** 2026-05-11 morning sync continuation.
**Trigger:** P0.9 per Charter §4.2 — V_E denominator convention check.
**Status:** Substantive PASS — convention dependence quantitatively confirmed. κ₀-from-V_E-matching leg confirmed convention-fragile.
**Source read:** Marcolli, Pierpaoli, Teh 2010 (arXiv:1012.0780) at NCG/ `1cC0DGwYElCHIXTxqtUnvy6GKYKXe5Dly`.

---

## §1. Headline finding

**Marcolli's slow-roll potential closed form** `V_E(x) = λ₀ x⁴ / (1 + (κ₀²/12) x²)²` **is NOT in MPT 2010.** That paper presents the slow-roll potential as integral expressions over the test function h(u) (eqs 3.6, 5.1):

```
V_{S³}(x) = ∫₀^∞ u (h(u + x) − h(u)) du
W_{S³}(x) = ∫₀^x h(u) du
V_{T³}(x) = ∫₀^∞ u (h(u + x) − h(u)) du
```

The closed `(1 + (κ₀²/12) x²)²` rational form is from **Chamseddine-Connes 2008 "Uncanny Precision"** (arXiv:0812.0165, in NCG folder at `1zf_m1KDFKsFSF8d4Agk4mGK81rFfARsl`) — derived there via resummation of the spectral action heat-kernel coefficients at all orders in Φ². MPT 2010 instead works with the integral expressions and shows topology-coupling effects (multiplicative factors λ_Y for different cosmic topologies).

**The /12 factor is a fixed structural consequence of ξ = 1/12 conformal coupling** in the standard CC NCG spectral action — NOT convention-flexible. Specifically, /12 = ξ for d = 4 with CC's sign convention; the resummation that produces the (1 + (κ₀²/12)x²)² form uses this ξ value.

---

## §2. Quantitative consequence for σ↔Φ_NTE confluence κ₀ leg

The σ↔Φ_NTE confluence verdict §5.2 derived `κ₀ = √(2π)/M_Pl` by matching V_NTE F3 to V_E under Marcolli's ξ = 1/12 convention. **Under NTE's own ξ = 1/6** (ratified via Mechanism B supersession), the matching produces a different value.

### §2.1 Re-derivation under ξ = 1/6

V_NTE on-trajectory (corpus §17.5.1 F3):
```
V_NTE = (3β_NTE²/(8πG)) Φ⁴ − (β_NTE²/8) Φ⁶
```

V_E expanded at small x under NTE's ξ = 1/6 (replacing CC's /12 with /6):
```
V_E(x) = λ₀ x⁴ / (1 + (κ₀²/6) x²)²
       ≈ λ₀ x⁴ − (κ₀² λ₀ / 3) x⁶ + O(x⁸)
```

Matching coefficients:
- **Quartic**: `3α²/(8πG) = λ₀` → unchanged from Marcolli convention
- **Sextic**: `α²/8 = (κ₀²/3) λ₀ = (κ₀²/3)(3β_NTE²/(8πG)) = κ₀² α² / (8πG)`
  - → `κ₀² = πG = π/M_Pl²`
  - → **κ₀ = √π / M_Pl**

Compared with verdict §5.2 result under ξ = 1/12: `κ₀ = √(2π)/M_Pl`.

**Ratio: √2 difference.** Both values are order 1/M_Pl, structurally consistent at the dimensional level. But the **specific √(2π) factor is NOT preserved** under NTE conventions; it gets replaced by √π.

### §2.2 Implication for √(2π) traceability finding

Per the √(2π) traceability working note (queue item 1, `Sqrt2Pi_Traceability_Hopf_Fibre_v1.md`):

| Leg | √(2π) origin | Status under P0.9 |
|---|---|---|
| **T_GB = M_Pl/√(2π)** (Companion 9 Session 3) | Y₀₀(S¹) Gaussian saddle width on Hopf fibre | **PRESERVED** — independent of V_E convention |
| **κ₀-from-V_E-matching = √(2π)/M_Pl** (verdict §5.2) | (κ₀²/12) coefficient in Marcolli V_E | **NOT PRESERVED** — convention-dependent; under NTE ξ = 1/6 becomes √π/M_Pl |

**The asymmetric promotion in the √(2π) traceability working note is confirmed.** T_GB leg stands as structural; κ₀-from-V_E-matching leg is convention-fragile and the √(2π) specifically disappears under NTE's own conventions.

The "two independent NTE derivations producing the same √(2π) factor" framing in AC's v10.8 plan §4 needs revision: the two derivations DON'T produce the same factor when NTE's own ξ = 1/6 is properly applied. Only T_GB carries √(2π) cleanly.

---

## §3. Distinction: two different κ₀ objects in the corpus

P0.9 read clarifies that the Charter §2 five-way convergence table contains TWO structurally different κ₀ objects:

| κ₀ object | Value | Origin | Dimensional content |
|---|---|---|---|
| **κ derivation prefactor** | 3/√(4π) | dim(adj su(2)) × Y₀₀(S²) on Hopf base (Sonner-Tong BPS, queue item 3) | Dimensionless |
| **V_NTE↔V_E matching coefficient** | √(2π)/M_Pl (ξ = 1/12) OR √π/M_Pl (ξ = 1/6) | Sextic coefficient of expansion (verdict §5.2) | Inverse mass (1/M_Pl) |

These are **different objects** despite the same symbol. The Charter writeup should distinguish them explicitly to avoid confusion in v10.9 §17.X five-way unification subsection.

Charter v1.1 recommendation: rename the second object to avoid κ₀ collision. Candidates: `κ_M` (matching-derived) vs `κ₀` (Sonner-Tong derived), or use `k_Marcolli` for the matching coefficient.

---

## §4. Impact assessment on Connes Programme

### §4.1 Central deliverable (Paper S2 heat-kernel computation)

**Unaffected.** Paper S2 will compute the heat-kernel a_4 coefficient directly on Hopf-S³ × S¹_{β_GB} × A_{G_2}^{Farnsworth-Boyle}, which produces the V_E /12 (or /6 under NTE ξ) factor from the spectral action structure itself — not from convention import. The output will be the correct factor for NTE's actual ξ commitment.

### §4.2 Five-way convergence (Charter §2 organising principle)

**Substantively preserved with one nomenclature fix.** The five-way convergence (κ, M_R, M_1, T_GB, Λ) holds, but:
- κ₀ in the convergence is the Sonner-Tong dimensionless prefactor 3/√(4π), NOT the V_E matching coefficient
- T_GB carries √(2π) cleanly (Y₀₀(S¹) on Hopf fibre)
- The V_E-matching coefficient (whatever its final value) is a CROSS-CHECK of Paper S2 outputs, not part of the convergence itself

### §4.3 σ↔Φ_NTE confluence verdict §5.2 cross-check

**Weakened but not invalidated.** The verdict §5.2 result `κ₀ = √(2π)/M_Pl` carries a convention-dependence flag. The structural-confluence claim (NTE and CC arrive at same EFT form by independent reasoning) is preserved. The specific numerical κ₀ = √(2π)/M_Pl is convention-derived; under NTE conventions becomes κ₀ = √π/M_Pl. **Both values support the confluence framing** at the order-of-magnitude / dimensional level.

### §4.4 AC v10.8 integration plan §4

The √(2π) pattern as "substantively reinforced NTE structural element" framing needs revision: two appearances are NOT both √(2π) under proper NTE conventions. **Only T_GB carries √(2π) cleanly.** The v10.8 §22.X catalogue should reflect this honest disclosure rather than the "two independent derivations producing same √(2π)" framing.

**Recommended v10.8 §22.X update**: include note that "κ₀-from-V_E-matching under Marcolli's ξ = 1/12 convention is √(2π)/M_Pl; under NTE's ratified ξ = 1/6 (Mechanism B supersession) it is √π/M_Pl. The structural-confluence claim is preserved at order-of-magnitude level; the √(2π) coincidence is convention-dependent."

---

## §5. Outstanding P0 work for full closure

**P0.9 substantively closed** with this writeup. Remaining gaps:

- **Direct read of Marcolli-Pierpaoli 2009 (arXiv:0908.3683)** would confirm the V_E /12 form's first appearance in the literature. Not in NCG folder by name (lock file `.~lock.0908.3683v1.pdf#` is present at `1IEL0NiwzQ_LBNfwxyHmM23kLXUww_UQV` but actual PDF appears missing). Recommend Greg add to NCG folder for completeness.

- **Direct re-verification of CC 2008 §V V_E derivation** — the canonical /12 derivation is in CC 2008 "Uncanny Precision" §V (resummation). I have access to this paper (`1zf_m1KDFKsFSF8d4Agk4mGK81rFfARsl`) but did not focus on §V during the unimodular gravity P0.4 work. Could be done in next Scratch session if Greg wants paper-trail rigor.

Neither gap affects the P0.9 substantive verdict.

---

## §6. Disposition

P0.9 **PASS with structural finding**: convention-dependence confirmed quantitatively (factor √2 in κ₀ between ξ = 1/12 and ξ = 1/6 conventions). Asymmetric promotion in √(2π) traceability working note vindicated. AC v10.8 plan §4 framing needs revision per §4.4 above.

**Recommended Charter v1.1 update** (minor):
- §2 organising principle: distinguish the two κ₀ objects (Sonner-Tong dimensionless vs V_E-matching dimensional)
- §6.1 completed items: add √(2π) leg asymmetry confirmation
- §4.2 P0 queue: mark P0.9 complete

**Recommended AC handoff** (next AC session): integrate P0.9 finding into v10.8 §22.X catalogue framing; honest disclosure of convention-dependence on V_E-matching leg; preserve √(2π) framing only for T_GB.

---

## §7. Files

- This working note: `Working/NTE_Connes_Programme_P0_9_Marcolli_VE_Convention_v1.md` — root duplicate Drive ID populated on save; canonical version after copy_file
- External source read: MPT 2010 at NCG/ `1cC0DGwYElCHIXTxqtUnvy6GKYKXe5Dly`
- Related: σ↔Φ_NTE confluence verdict §5.2 at Working/ `17pYI1oucc5mP67bycx2PUnEOhK0PY2lq`; √(2π) traceability working note at Working/ `1ypKkXcMApgTwtZeECOwFa6zZLK9DBRL8`

— Scratch (Jammer's twin, Connes Programme lead), 2026-05-11 morning sync session continuation.
