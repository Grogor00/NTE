# S1 λ/R_H — Scratch independent verification: Jammer's resolution reproduced and confirmed applied. CLOSED, no action.

**From:** Scratch · **To:** AC · **Cc:** Greg, Jammer, PC · **Date:** 2026-09-24
**Directed by:** Greg, 2026-09-24 — "resolve the λ/R_H discrepancy."
**Finding:** already resolved by Jammer (`Working\S1_VERDICT_lambda_RH_0p625_vs_3p92_SAME_RELATION_hbar_vs_h_BOTH_on_R3_not_4pi3_Jammer_20260923.md`, 2026-09-23) and already applied to the deposit set and the C21 draft. This note is an **independent arithmetic verification + application check**, not a re-derivation. No further action.

---

## 1. The resolution, independently reproduced

The two figures are **one relation, ħ vs h (a factor 2π), not a contradiction.** With the trigger n_γ·R_H³ = 1 and Planck statistics, x ≡ kT_reset·R_H/(ħc) = (π²/2ζ(3))^(1/3):

| Quantity | Reproduced | Corpus figure |
|---|---|---|
| x = (π²/2ζ(3))^(1/3) | **1.60121** | — |
| ħc/(kT_reset·R_H) = 1/x — **reduced** thermal wavelength / R_H | **0.62453** | 0.625 (v10.5.9 §5.3) |
| hc/(kT_reset·R_H) = 2π/x — **unreduced** wavelength / R_H | **3.92403** | 3.92 (v10.5.9 §6.5) |

Check: 0.62453 × 2π = 3.92402. Same quantity, labelled once as reduced and once as unreduced. Neither is a mistake; a label was missing. Neither is a "typical photon" wavelength either (Wien peak 0.790 R_H, mean-energy photon 1.453 R_H) — the defensible statement is **λ ∼ R_H**, order-of-magnitude. Jammer's arithmetic is correct in full.

## 2. The deeper finding (trigger convention) — also verified, and remedy (a) is the *uniquely consistent* choice

Jammer's second finding: the formula kT_reset = ħH(π²/2ζ(3))^(1/3) follows from **n_γ·R_H³ = 1**, not from the stated V_H = (4π/3)R_H³. Reproduced:
- n_γ·R_H³ = 1 → (kT R_H/ħc)³ = π²/2ζ(3) = 4.1053 → x = 1.60121. ✓
- n_γ·(4π/3)R_H³ = 1 → x = 0.99327, i.e. kT_reset = ħH(3π/8ζ(3))^(1/3), a *different* temperature (×1.612 lower). With the (4π/3) volume and the published formula, the count is **4.19 photons per volume**, so the old "N_γ = 1.00000000" line was false as written. ✓

**Sharpening for the record:** remedy (a) — define V_H ≡ R_H³ (a Hubble cube) — is not merely the minimal edit; it is the **only choice that preserves the already-quoted T_reset = 2.213×10⁻²⁹ K.** The corpus's published T_reset is the cube-convention value; remedy (b) would have forced T_reset → ~1.38×10⁻²⁹ K and shifted N_total by ln 1.612 ≈ 0.48 e-folds. So the Greg-ratified choice (a) is self-consistent with numbers already in the corpus, not just economical.

## 3. Application status — confirmed by direct read of live files

- **Canonical `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` §V** (modified 2026-09-23) now reads: *"n_γ V_H = 1, with V_H ≡ R_H³ = (c/H_dS)³ — one photon per Hubble cube; the O(1) geometric factor is a convention of the order-of-magnitude trigger."* Deposit-set fix **applied** (remedy a, Greg-ratified 2026-09-23). Seed wavelength stated as "∼ R_H." No raw λ/R_H figure in the deposit set (consistent with Cursor's earlier grep).
- **`Working\Paper_C21_ConformalReset_SeedPhoton_v0_3_PC_20260924.md`** §3 states the V_H ≡ R_H³ convention explicitly; §5 carries the "one relation, reduced/unreduced, λ ∼ R_H" wording. C21 draft **applied**.

## 4. Disposition

**S1 / B1 (λ/R_H) is CLOSED.** Nothing to derive, nothing to fix; the resolution is correct and already in both canonical Part 1 §V and C21 v0.3. Independent Scratch verification confirms Jammer's S1 in full and confirms application. κ, δ_J, θ₂₃ and all other register entries untouched.

*Provenance note: an earlier Scratch handoff (`Handoffs\Handoff_Scratch_to_AC_C21_Seed_Boundary_Data_Five_Threads_COMPLETE_no_testable_content_20260924.md`) stated the λ/R_H item was "still routed to Scratch and not addressed." That was read off the superseded C21 outline; it was in fact resolved by Jammer on 2026-09-23 and applied. Corrected here.*

— Scratch, 2026-09-24.
