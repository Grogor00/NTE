# Round 6 — correctly staged ∂δ `{C_SC,C_SC}`: VERDICT (Cursor Main)

**Landing: G-4** (blocker correctly staged).  
**Directive:** `Handoffs\Directive_AC_to_Cursor_Pursue_Correctly_Staged_ddelta_Bracket_Generic_Background_20261020.md`  
**Prereg (filed first):** `Working\Opsi2_Round6_Correctly_Staged_ddelta_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md`  
**Script / JSON:** `Working\Opsi2_Round6_Correctly_Staged_ddelta_COMPUTE_CursorMain.py` / `_RESULTS.json`  
**Engines:** NumPy + SymPy (both **run**). Wolfram: **not installed** — no Wolfram claims.  
**No Core. No f.** (N) undetermined. 90/90 **not used**.

---

## 0. Object (this time)

∂δ coefficient in `{C_SC,C_SC}` at O(ψ²) on **generic** backgrounds: n ≠ 0, R_g ≠ 0, anisotropic, on-SVC, phase-gradient P.

| # | Contribution | Result |
|---|---|---|
| (1) | θ-residual \(R_\theta P\), \(R_\theta=h_g(\theta_g I-\theta_f X)^2\) | nonzero generically; rank 3 (median); **K1:** vanishes at X=I (20/20) |
| (2) | Vector channel via \(\delta(Dn)\) from matter-induced \(\delta n(P)\) (minimal n from (24)) | **does not cancel (1)** |
| (3) | χ-corrected cross (F14) | **uncomputed** (no closed-form coefficient in script) |

---

## 1. K0′ at generic n

**Numeric gate (JSON `k0_numeric_generic_n`):**
- fraction n ≠ 0: **1.0**; ξ = Dn ≠ 0: **1.0**
- fraction D = X: **0.0** (median ‖D−X‖/… ≈ 0.19) — **not** the n=0 locus
- **pass_generic_n: true**

**SymPy:** (i) rank diagnostic — unweighted \((I-X)^2\) rank 1 vs θ-toy rank 3 on diag(1,1,λ); (ii) ADM/HR **skeleton** — ∂δ coeff from \(R_i\xi^i\) is R-weighted and vanishes on-shell R=0 at generic ξ≠0.  
**Honesty:** SymPy item (ii) is an index/on-shell skeleton, **not** a line-by-line reproduction of Hassan–Rosen `{C,C}`. Full pure-HR bracket ledger is Scratch’s parallel chain document. Method gate for this lane = numeric generic-n construction + skeleton.

**K0′: PASS** for proceeding to (1) vs (2). n=0 reduction **not** used as decisive locus.

---

## 2. Cancel test: does (2) cancel (1)?

Map \(P\mapsto\delta(Dn)\) by central differences on \(n_{\min}(R)\) and \(D(n)\) at **background n≠0**. Compare to \(-R_\theta P\).

| Statistic (from JSON) | Value |
|---|---|
| trials kept (n≠0) | 52 |
| fraction n > 10⁻² | 0.981 |
| median rank \(R_\theta\) | **3** |
| fraction cancel (α=1) | **0.0** |
| fraction cancel (free α lstsq) | **0.0** |
| median rel err (α=1) | **0.990** |
| median rel err (free α) | **0.949** |
| median mean angle (δ(Dn)P vs −R_θP) | **62°** |
| K1: X=I ⇒ ‖R_θ‖=0 | **1.0** (20/20) |

**Same for** \(D(\delta n)\) without varying D: median rel err α=1 ≈ **0.992**.

**Conclusion on (2):** the R4-named vector channel, evaluated through matter-induced δn on generic n≠0, **is not a scalar multiple of −R_θ** and does **not** cancel the θ-residual.

---

## 3. Contribution (3) and fork

χ-cross Dirac terms: **uncomputed** here. R2 structure only (shared-π_ψ ⇒ B1/B2 generically nonzero) — **no coefficients**.

Per prereg decision rule: a free schematic linear map from (3) could still cancel the remainder → **K3 for terminal G-2 not met**.  
(2) failing does **not** by itself close G-1.

| Fork | Status |
|---|---|
| G-1 | **Not earned** — sector not shown closed; Ṡ not opened |
| G-2 | **Not earned** — K3 needs (3) or a proof χ cannot supply the missing ∂δ covector |
| **G-4** | **Landed** — (2)≠−(1) on correct channel/locus; blocker = (3) χ-cross (or chain-doc tractability) |

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

---

## 4. What this changes relative to R4/R5

- **R4 hole filled in part:** vector channel at **generic n≠0** is now probed; it does not cancel θ-residual under δ(Dn).
- **R5 mis-posed identity:** not reused; no Ṡ/X-only object; 90/90 absent.
- **Not a terminal ghost claim.** (N) remains **undetermined**.

S1–S4 healthy alternates **unchanged**.

---

## 5. Standing / ask

**Ask AC / Jammer:** attack (i) identification of (2) with \(\delta(Dn)\) as the full R_iDn ∂δ matter piece; (ii) whether χ-cross can be scoped to block free absorption of the remainder (would reopen G-2 path); (iii) K0′ skeleton vs Scratch chain-doc reference.

**Round 6 compute complete for this directive.** No Core. P04 unchanged.

— Cursor Main, 2026-10-20.
