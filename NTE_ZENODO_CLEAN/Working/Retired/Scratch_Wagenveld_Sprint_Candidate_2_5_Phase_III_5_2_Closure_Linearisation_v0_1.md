# Scratch Wagenveld Sprint — Phase III §5.2: Closure-Step Sensitivity ∂κ/∂ε from S_cons Linearisation (v0.1)

**Author:** Scratch (Connes Programme lead, within Jammer-stream)
**Date:** 2026-05-30
**Status:** Phase III v0.1 — Deliverable 2 of 4 for the merged §2.1+§2.5 co-rank-1 arm. **Recognition-gate-level correction to the scoping estimate — see §4/§8.** AC has independently verified the eigenstructure, retracted the ×42 from the §5.1 verdict, and updated the Phase IV framework (2026-05-30).
**Authority:** AC resume pointer (`Handoff_AC_to_Scratch_Resume_Pointer_Phase_III_5_2_Next_20260530.md`); binding Phase II.5 (co-rank-1 §2.7 + merged §2.5).
**Predecessor:** §5.1 seed-amplitude doc (δε ≈ 2ĥ ~ 10⁻³–10⁻²).
**Corpus anchor:** `Papers/Paper_Kappa_AB_v10_17_2.md` (`1p3GeEnQi7ljlL6I-chN-HHZZXR_ZIggy`) §5 closure; §3.3–3.4 κ₀ protection.

---

## §0 — The two tasks

(1) Confirm the (κ/κ₀)²≈42 amplification by explicit linearisation of the §5 closure. (2) Fix the fractional-vs-absolute δε↔δκ normalisation. The honest outcome of (1) is that **the amplification is not confirmed** — explicit linearisation replaces ≈42 with a coefficient ~14× smaller, for a structural reason that also resolves (2).

## §1 — The closure

S_cons (neglecting T^(ν), §5.3) couples the orientations σ=±:  T̃^(σ) = T^(b,σ) + κ₀ T̃^(−σ). At exact CPN: κ = κ₀/(1−κ₀), κ₀ = 3/√(4π) = 0.84628, κ = 5.5057. ρ_DM^(+) = κ₀T̃^(−); ρ_b^(+) = T^(b,+). The §5.1 seed breaks CPN with a dipolar, **antisymmetric source** perturbation T^(b,±) = T^(b)(1+ε_±), δε = ε₊−ε₋. **κ₀ is not perturbed** — it is the monopole matrix element, protected by Gaunt triviality / bundle topology (§3.3–3.4).

## §2 — Exact two-sector solution

M[T̃^(+);T̃^(−)] = [S(1+ε₊); S(1+ε₋)], M = [[1,−κ₀],[−κ₀,1]], S≡T^(b). M⁻¹ = (1/(1−κ₀²))[[1,κ₀],[κ₀,1]]. Then κ^(+) = κ₀T̃^(−)/[S(1+ε₊)] = κ₀[(1+κ₀)+ε₋+κ₀ε₊]/[(1−κ₀²)(1+ε₊)]; at ε=0 → κ. ✓

## §3 — Eigenmode decomposition

M is symmetric: symmetric eigenvector (1,1) → eigenvalue 1−κ₀ → M⁻¹ amplifies ×1/(1−κ₀)=6.505 (this is what makes κ from κ₀; diverges as κ₀→1, the "no 4th neutrino" bound). Antisymmetric eigenvector (1,−1) → eigenvalue 1+κ₀ → M⁻¹ **damps ×1/(1+κ₀)=0.542**. δε is antisymmetric by construction, so it couples to the damped mode. Physically: the bridge mixes the sectors → amplifies common content, equalises (damps) any difference. A CPN-breaking asymmetry is a difference.

## §4 — Result and correction

Linearising (ε₊=+δε/2, ε₋=−δε/2): δκ^(+)/κ = (ε₋−ε₊)/(1+κ₀) = **−δε/(1+κ₀)**.

- **Fractional:** δκ/κ = −δε/(1+κ₀) ≈ −0.542·δε.
- **Absolute:** δκ = −[κ₀/(1−κ₀²)]·δε ≈ −2.982·δε.

Scoping §2.2 wrote δκ ≈ κ₀²/(1−κ₀)²·δε labelled (κ/κ₀)²·δε ≈ 42·δε. (a) Algebra slip: κ₀²/(1−κ₀)² = κ² ≈ 30, not (κ/κ₀)² = 1/(1−κ₀)² ≈ 42. (b) Structural error: both are dκ/dκ₀, the sensitivity to a **coupling** perturbation; δε perturbs the **sources**, κ₀ is protected. Correct absolute coefficient ≈ 2.98 is ~14× below 42.

## §5 — Normalisation (task 2)

δε is a fractional source imbalance → closure returns fractional δκ/κ = δε/(1+κ₀); absolute carries the extra κ. The cosmic-dipole observable D_S is a fractional number-count anisotropy, so **§5.4 uses A_frac = δε/(1+κ₀) ≈ 0.54·δε**. Absolute δκ ≈ 2.98·δε recorded for completeness (e.g. CMB-S4 σ_κ). Supersedes the scoping's implicit absolute A = 42·δε.

## §6 — Handed forward

δε ~ 10⁻³–10⁻² → A_frac ~ 5×10⁻⁴–5×10⁻³ (central ~1.5×10⁻³); A_abs ~ 3×10⁻³–3×10⁻². Intrinsic merged-§2.5 dipole now sub-percent in fractional κ. **§5.3:** the only route to large (~30–42) amplification is the coupling/channel-selection arm (evading Gaunt protection) — resolve there; default = source arm. **§5.4:** ΔD_S = A_frac·P_S. **Phase IV:** smaller A → §2.7-primary at exit, co-rank-1 entry intact, §5.4 decides.

## §7 — Honest scope

**High confidence (exact-algebraic):** δκ/κ = −δε/(1+κ₀); eigenmode reason; ≈42 not the δε response; §5.4 normalisation fractional. **Open:** coupling-anisotropy arm (up to ~6·δε fractional) tied to §5.3; tensorial completeness (scalar channel dominates for dipolar density); c_A (Jammer one-loop, Phase IV). **Does NOT commit to:** that merged §2.5 succeeds.

## §8 — Recognition-gate flag (Greg/AC)

The scoping, §5.1, and register v0.3 carry "(κ/κ₀)²≈42." §5.2 does not reproduce it (~14× smaller absolute; §5.4 input ~0.54·δε). **No corpus claim affected** — κ=5.50 and κ=κ₀/(1−κ₀) untouched; this is the perturbative response of the closure to an antisymmetric seed. AC has integrated the correction (verdict + Phase IV framework, 2026-05-30). Annotate scoping §2.2 and register lines as superseded. Not a Cursor blocker.

This file: `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_2_Closure_Linearisation_v0_1.md`

— Scratch (Connes Programme lead), 2026-05-30. §5.2 v0.1: δκ/κ = −δε/(1+κ₀) (antisymmetric-mode damping, not (κ/κ₀)² amplification); fractional normalisation fixed for §5.4; AC-verified.
