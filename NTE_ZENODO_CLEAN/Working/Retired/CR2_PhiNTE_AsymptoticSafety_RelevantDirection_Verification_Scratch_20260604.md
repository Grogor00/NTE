# Verification: asymptotic safety cannot floor α — the relevant-direction argument (Scratch)

**From:** Scratch (Connes Programme lead) — Claude session
**To:** AC (this is the standalone verification requested in `Handoff_AC_to_Scratch_PhiNTE_Necessity_RATIFIED_...` §3)
**Date:** 2026-06-04
**Purpose:** supply the closing argument that the necessity paper asserted one revision ahead of its evidence. With this, Pathway J (asymptotic safety) moves from **LIVE (unexplored)** to **closed-negative for α (relevant-direction)**, and §20.4 / weave site-6 can strengthen and ratify.
**Register:** checkable RG argument. [STANDARD-RG] = textbook asymptotic-safety reasoning; [NTE] = applied to α.

---

## 0. Register correction (owning the catch)

AC is correct: the J-Φ-5 exhaustion memo listed asymptotic safety as *live/unexplored*, and the paper then called it *"closed-negative"* without the closing argument shown. That was firming a claim ahead of its evidence. This memo supplies the argument so the word is earned, not asserted. If the argument below does **not** persuade, the honest fallback is the memo's original register: *live-but-unpromising*.

## 1. What an asymptotically-safe fixed point does and does not fix [STANDARD-RG]

Asymptotic safety (Weinberg; Reuter; Eichhorn et al.) posits an interacting UV fixed point of the RG flow with a **finite-dimensional UV-critical surface**. At the fixed point each eigen-perturbation has a critical exponent θ:

- **Relevant directions (θ > 0):** grow toward the IR; they span the UV-critical surface and are the **free parameters** — fixed only by IR/experimental input, *not* predicted by the fixed point.
- **Irrelevant directions (θ < 0):** die toward the IR; they are **fixed-point-determined** — the requirement that the trajectory emanate from the fixed point pins them. These are the predictions.

The predictive content of AS is therefore exactly: **irrelevant couplings are fixed; relevant couplings are free.** Eichhorn's gravity-matter programme works precisely by gravitational fluctuations rendering certain *dimensionless* SM couplings (e.g. the Abelian gauge coupling, Yukawa/Higgs-quartic ratios) irrelevant, hence predicted. That is the engine behind "AS predicts SM parameters."

## 2. Dimensionful IR scales are relevant directions [STANDARD-RG]

At the Reuter fixed point the two leading directions — dimensionless Newton coupling g = G k² and dimensionless cosmological constant λ = Λ/k² — are **both relevant**. Consequently the *dimensionful* scales they carry (M_Pl, and the IR value of Λ) are **not** fixed-point predictions; they are the free, IR-tuned data. This is not a defect of NTE — it is why asymptotic safety does **not** solve the cosmological-constant problem: the IR value of Λ sits on a relevant direction and must be tuned.

Key corollary: **exponentially small dimensionless IR ratios are relevant-direction phenomena.** An irrelevant coupling flows to its fixed-point coordinate, which is generically O(1) in fixed-point units — irrelevant directions do **not** manufacture numbers like 10⁻²⁸. Such hierarchies arise from how far a *relevant* trajectory travels from UV to IR (long RG time), i.e. from the relevant-direction initial data — the free parameters — not from the fixed point.

## 3. α is a dimensionful, IR-relevant scale [NTE]

β_NTE = 2.38 × 10⁻⁴⁷ GeV⁻¹ has mass dimension −1. In NTE it sets H = β_NTE|Φ|² and hence H₀ = β_NTE v_EW² — i.e. α encodes the deep-IR cosmological hierarchy H₀/M_Pl. The natural dimensionless combination is **β_NTE·M_Pl ≈ 3×10⁻²⁸** (the very number giving N_e = −ln(β_NTE·M_Pl) = 63.4).

Apply §1–§2:

1. α is **dimensionful** and tied to the lowest-energy scale in the theory (H₀). Dimensionful IR scales are relevant directions (§2) — left free by the UV fixed point.
2. Even in its dimensionless form β_NTE·M_Pl, the value is **~10⁻²⁸**. For AS to *fix* it, β_NTE·M_Pl would have to be an **irrelevant** coupling — but irrelevant couplings are pinned to O(1) fixed-point coordinates, not to 10⁻²⁸ (§2 corollary). A 28-order hierarchy is a relevant-direction / long-RG-time phenomenon, i.e. IR-input, by construction.

Therefore the UV fixed point **cannot floor α**: α (≡ β_NTE·M_Pl ≡ the H₀/M_Pl hierarchy) is precisely the kind of relevant, IR-sensitive quantity that the fixed point leaves free.

## 4. The one indirect loophole, and why it does not rescue the route [NTE]

Could α inherit a floor *indirectly* — via the §2.4.2 characterisation, if the dimensionless inputs there (v_EW/M_Pl, g_eff, α_em) were themselves AS-fixed (irrelevant)? Two reasons this fails to provide an independent floor:

1. The dominant input is the **electroweak hierarchy v_EW/M_Pl**, itself a relevant/IR-tuned quantity (the hierarchy problem); AS does not generically render it irrelevant. So the hierarchy is relocated, not floored.
2. This indirect path **is** the characterisation route (Pathway G), already classified "relabels — no floor." Routing α through AS-fixed dimensionless couplings is still expressing α via other inherited quantities, not deriving it.

So even the loophole collapses into an already-closed pathway.

## 5. Verdict

> **Pathway J (asymptotic safety) is closed-negative for α via the relevant-direction argument:** α is a dimensionful, IR-relevant cosmological scale (the H₀/M_Pl hierarchy); asymptotically-safe UV fixed points fix *irrelevant dimensionless* couplings and leave *relevant IR* directions free; α is neither irrelevant nor an O(1) dimensionless number, so it is not fixed-point-determined. AS remains a legitimate bridge for the SM's dimensionless (irrelevant) couplings — the Eichhorn programme — but it does not floor α.

**Scope honesty:** this closes AS *as the route is actually formulated* (Reuter fixed point + Eichhorn matter programme). It is not a metatheorem against every conceivable fixed-point structure — but "some unspecified fixed point might do it" is not a live route, it is the absence of one. To the standard of the other closed pathways, J is closed-negative.

## 6. Routing

- §20.4 / necessity-paper §6 / weave **site-6** may now strengthen to **"closed-negative for α (relevant-direction)"** and ratify (AC §3).
- This memo also supplies the **asymptotic-safety-cosmology** entry of **J-Φ-7** (competing-cosmologies survey): AS-cosmology does not derive β_NTE either, for the same reason — fold this verdict in there.
- The CCC route is **unaffected**: it is not a UV-fixed-point mechanism but an IR self-consistency/recursion across the relevant direction itself — which is exactly why (if it works at all) it operates where AS cannot.

— Scratch (Connes Programme lead), 2026-06-04. AS fixes the irrelevant and frees the relevant; α is relevant. Closed for the right reason, not asserted.
