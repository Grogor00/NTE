# F_Phi F-1 VERDICT — Jammer: **neither horn as posed.** Φ is slaved (no independent degree of freedom) but still consequential. Once the multiplier is eliminated, C9's RΦ² term is a real, frame-independent modification of the Friedmann constraint, with the **opposite sign to AC's H³ ≈ 2βρ**. Consequence: **no de Sitter phase above vacuum energy ~(37–62 TeV)⁴ exists in NTE's own gravity.** The withdrawal is **not** reopened; it is reinforced.

**From:** Jammer · **To:** AC · **Cc:** Greg, Scratch (F-2 owner) · **Date:** 2026-09-26
**Directive:** `Handoffs\Directive_AC_ALL_LANES_F_Phi_Effective_Planck_Mass_May_Reopen_Withdrawal_Highest_Priority_20260926.md`
**Register:** findings, not rulings. Nothing patched. Blind: no other lane's F-Φ file opened. Search results this turn showed titles only.

---

## 0. Read set (discipline 11)

**Read in full this session:**
- The directive (this turn).
- Part 1 (§2.3, §VI).
- C8 (eq. (2), F1 §3, F3 eq. (5)–(6)).
- C9 (eq. (1), §2, §3).
- C15 (§3.3, §6.1).

All of these except the directive were read earlier this session and are still in context. C12 and C14 were read last turn.

**Not read:** C17 (**[not re-read]** where cited).

**Computation:** `scratchpad/mini.py` and `scratchpad/mini_dN.py` (sympy minisuperspace: flat FRW, lapse n, the full C9 eq. (1) Lagrangian with V = λΦ⁴, Euler–Lagrange in n, Φ and μ), plus `scratchpad/cross.py` and `scratchpad/cross2.py` (numerical integration).

**Caveats, stated up front:**
- k = 0. Closed-S³ curvature adds −3F/a² terms, which do not change the high-H structure.
- Minisuperspace only; perturbations are not treated.

---

## 1. Outcomes

- **Directive outcomes:** H1–H4 adopted as written, before computing.
- **H5 (not pre-registered; found in the computation, so flagged as such):** "slaved but consequential". Φ carries no independent degree of freedom, yet the F(Φ)R term evaluated on the constraint changes the metric dynamics. It cannot be removed by a frame choice.

**Landing:** H5. Under H5 the withdrawal stands, as under H2 and H3, for a different reason from either.

---

## 2. The deposit asserts both horns (quoted, read this session)

**Relabelling / artefact horn:**
- Part 1 §2.3: "in the cosmological (FRW) sector … Φ_NTE is a relabelling of the expansion history."
- C8 eq. (2): Φ is read off after "H set by FRW dynamics and the actual matter content".
- C8 F1 §3: the large |Φ| "is a dimensional artefact of the variable's normalisation, not a field excursion."
- C9 §2: "Φ_NTE slaved to" a(t); "dynamical content reduces from two fields … to one".
- C15 §6.1 **(AC's prior, now confirmed from the deposited text):** metric-only entry is "a field redefinition of Leg 1's gravitational dynamics", with canonical χ ∝ Φ⁻³ ∝ a^{3/2}, "Pure gravity, re-lettered."

**Physical-field horn:**
- C9 eq. (1): canonical −½(∂Φ)², +(1/12)RΦ², V, portal, μ(N)[H − β|Φ|²].
- C9 §5: Φ ≈ 15.9 M_Pl as a slow-roll inflaton (since withdrawn).
- C17: Einstein-frame K(Φ) built on F(Φ) = M² + Φ²/6 **[not re-read]**.

**Internal contradiction 1: C8 F1 against C9's ξ = 1/6.** ξ = 1/6 is the conformal value *only for a canonically normalised field* (C9 §1: invariance under g → Ω²g, Φ → Ω⁻¹Φ). Rescaling Φ changes ξ. So once C9 fixes ξ = 1/6 with a canonical kinetic term, Φ's numerical value is fixed, and Φ²/(6M²) is a dimensionless physical ratio. **"A dimensional artefact of the variable's normalisation" (C8 F1) is false in C9's normalisation.** The two cannot both stand.

**Internal contradiction 2: C9 §2's "slightly".** C9 §2 says the ξ = 1/6 term "modifies the 3M_Pl² coefficient slightly without changing the structure". On C9's own constraint in its own Hartle–Hawking regime (H ≈ M_Pl), Φ²/6 = M_Pl/(6β) ≈ 1.7×10⁶⁴ GeV², against M² ≈ 5.9×10³⁶ GeV², a factor of **~10²⁷**. The claim is wrong by 27 orders, and it is where this whole issue was missed.

---

## 3. The computation: what F(Φ)R does once Φ is slaved

**Setup.** Vary C9 eq. (1) in minisuperspace (lapse n; Φ; μ). The multiplier is fixed by the Φ equation and substituted into the Hamiltonian constraint (the n equation). Then impose Φ² = H/β. The result, symbolic and exact within the stated caveats, is:

**3M²H² + (λ/β²)H² − H³/(2β) + [3HḢ/4 + Ḧ/4 − Ḣ²/(4H)]/β = ρ_matter**

**Four features:**
1. **The multiplier cannot be dropped.** μ enters the Friedmann constraint at the same order as the F terms. In de Sitter, μ = (H² − 2λΦ²)/β. Dropping μ (as the directive's "3FH² ≈ ρ" does) gives +Φ²H²/2. Keeping it gives **−Φ²H²/2**: **the sign flips.** AC's **H³ ≈ 2βρ has the wrong sign** and should not be used by F-2 lanes.
2. **The potential's sign also flips.** In de Sitter, V − ΦV′/2 = −λΦ⁴, so V_NTE enters against ρ. This is a second, structural reason Φ_NTE cannot drive acceleration under its own constraint.
3. **The result is measure-robust.** Writing the multiplier term with the √g measure or with the dN = (ȧ/a)dt measure gives the identical constraint (both scripts). C9's "∫{L + μ(N)[…]}" leaves the measure ambiguous; the result does not depend on it.
4. **This is a real metric-sector modification, not a frame choice.** The constraint uses H, a foliation-dependent, non-covariant quantity. Matter couples to g (Jordan frame, C9 eq. (1)). The substituted action is third order in a (Ḧ terms). No field redefinition of an independent scalar removes it, because there is no independent scalar. **AC's H3 premise, "relabelling ⇒ M_eff is a frame choice, physics unchanged", is false for this action.**

**The crossover.** In the static limit the H² coefficient vanishes at H = 6βM² = 8.5×10⁻¹⁰ GeV (λ = 0), which confirms the F-4 figure. With C8 eq. (6)'s on-trajectory λ = 3β²M² it is 12βM² ≈ 1.7×10⁻⁹ GeV.

**3.1 No high-scale de Sitter.** For Ḣ = 0 the constraint is (3M² + λ/β²)H² − H³/(2β) = ρ_vac.
- The left side is bounded above:
  - λ = 0: maximum at H = 4βM², giving **ρ_vac,max = 16β²M⁶ ≈ (3.7×10⁴ GeV)⁴**.
  - λ = 3β²M²: **≈ (6.2×10⁴ GeV)⁴**.
- **No de Sitter solution exists with vacuum energy above ~(37–62 TeV)⁴, and none at all with H above ~10⁻⁹ GeV.**
- Higgs inflation (V^¼ ≈ 7.9×10¹⁵ GeV) and Starobinsky are therefore not solutions of NTE's gravity as written. Nor is AC's "H ≈ 7×10⁵ GeV" recomputation.

**3.2 The radiation era through the crossover** (numerical; one branch of the third-order ODE, matched to GR at low H; λ = 0).
- No singularity at the crossover: the higher-derivative terms carry the solution through.
- Above it, H departs sharply from GR. H/H_GR = 1.06 at h = 0.06, 1.66 at h ≈ 0.9, 6.9 at h ≈ 35, 27 at h ≈ 820 (h ≡ H/(6βM²)).
- It steepens roughly as H ∝ a^{−3.5}.

**3.3 Observational floor (F-4 cross-check).**
- The fractional deviation ~ H/(6βM²) is ≈ 5×10⁻¹⁶ at BBN (T ~ 1 MeV) and ≈ 2×10⁻⁵ at the electroweak crossover (T ~ 100 GeV).
- **Nothing observable is disturbed** from BBN to today at this order. Perturbations are not checked.

---

## 4. F-1 answer

**Φ is slaved.** That settles the degree-of-freedom question: C9 §2 and C15 §6.1 both say so, and the computation confirms that the Φ equation serves only to fix μ.

But **H3's "physics unchanged" does not follow.** With C9 eq. (1) as written, the slaved RΦ² term plus the multiplier makes NTE's gravity **non-GR above ~25–45 TeV in a specific, computable way**: sign-flipped, third-order, and with no high-scale de Sitter.

**The deposit must choose between two readings; either one keeps the withdrawal:**
- **Keep C9 eq. (1) as written (H5).** No inflation of any kind above ~(40–60 TeV)⁴ is possible. Exits (a) and (a′) cannot run. The early universe above ~25 TeV must be redone in the modified gravity (see §5). **The withdrawal stands, reinforced.** Exit (c) becomes the only one not blocked by the gravity itself; (b) is untested here.
- **Drop the RΦ² coupling (or the constraint's action-level enforcement) (H3 proper).** GR returns. C9 eq. (1)'s ξ = 1/6 term and C17's K(Φ) closure withdraw, and C8 F1's "artefact" reading survives. The withdrawal stands on its GR calculation. Exits reopen for gating.

**H1 (reverse the withdrawal) is contradicted by the leading-order analysis.** The recomputation that suggested the mismatch "shrinks" omitted the multiplier and had the wrong sign.

**What would settle it** is a single commitment: **whether the μ(N) constraint is enforced at action level (C9 eq. (1)) or read off post hoc (C8 eq. (2), Part 1 §2.3).** The deposit currently does both.

---

## 5. What else assumed GR (for F-3, Cursor Scratch; flagged, not swept)

- **NTE's own leptogenesis** (Part 2 §X: M₁ ≈ 5.4×10⁹ GeV, Davidson–Ibarra). It runs at T ≫ 25 TeV, deep in the modified regime (§3.2), so H at T ~ M₁ is far from GR. The out-of-equilibrium and washout inputs to η_B change. **This is a deposited result, not an exit, and it is affected under H5.**
- T_GB and the Hartle–Hawking saddle (C9 §3–4). C9 §3's cancellation "the Φ⁴ term cancels the H² term exactly" was done without the multiplier's back-reaction; it needs redoing.
- My G4 recollapse argument. The ȧ = 0 junction is kinematic and should survive, but the "ρ + 3p > 0 ⇒ recollapse" step used the GR acceleration equation. Under H5 the acceleration equation differs, so it is **flagged for re-check, not withdrawn**.
- Horizon matching N*, Scratch's T_GB dilution numbers, every (n_s, r) computation, and the Higgs, Starobinsky and item (a) exit numbers: all GR, and all moot under H5 above ~40 TeV.

---

## 6. For F-2 (Scratch) and Cursor Jammer

Use the constraint in §3, not "3FH² ≈ ρ". Check the multiplier elimination independently. Extend it to k = +1 and to the full V_NTE of C8 eq. (6), including its −β²Φ⁶/8 term. The claim to confirm or break is: "no de Sitter above ~(40–60 TeV)⁴".

— Jammer, 2026-09-26.
