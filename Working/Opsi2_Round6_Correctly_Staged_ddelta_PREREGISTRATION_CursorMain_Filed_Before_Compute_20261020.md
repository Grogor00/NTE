# PRE-REGISTRATION — Cursor Main, Round 6: correctly staged ∂δ of {C_SC, C_SC} on generic background

**Filed before any Round-6 compute result.**  
**Directive:** `Handoffs\Directive_AC_to_Cursor_Pursue_Correctly_Staged_ddelta_Bracket_Generic_Background_20261020.md`  
**Greg direction:** 2026-10-20 01:04 NZDT.  
**Parallel:** Scratch writes constraint-chain reference — **do not merge**.  
**No Core. No f. P04 unchanged.**  
**Blind:** not reading Scratch’s Round-6 chain document before filing this prereg / first compute (contamination on R5 already noted project-wide).

---

## 0. Corrections carried (binding)

- R5 G-2 **not ratified**; (N) **undetermined** (project G-4).
- Kill 2 (scalar vs covector) **does not hold** as a terminal kill.
- Scratch X-only identity **mis-staged** (Ṡ vs Ċ) — withdrawn by Scratch.
- Rank-1 argument on **unweighted** R only; θ-form is rank 3.
- **90/90 struck.** SymPy only if actually run; else say unavailable/not run.
- **F1:** no linearisation about n = 0 as the decisive locus. Background must be **n ≠ 0**, R_i^(g) ≠ 0.

---

## 1. Object (correctly staged)

Compute the **∂δ coefficient** in `{C_SC, C_SC}` at O(ψ²) on a **generic** background:

- n ≠ 0, R_i^(g) ≠ 0, on-SVC, anisotropic X ≠ I, phase-gradient P ≠ 0.

**Three contributions (all required in the ledger):**

| # | Contribution | Stage |
|---|---|---|
| (1) | Matter–matter θ-weighted residual \(R^{jk}P_k\), \(R=h_g(\theta_g I-\theta_f X)^2\) | Ċ_SC via `{C_SC,C_SC}` |
| (2) | Vector channel from \(R_i^{(g)} D^i{}_j n^j\) inside \(\mathcal{C}\), with matter-induced \(\delta n=O(\psi^2)\) linear in P | same |
| (3) | χ-corrected cross terms (F14) | same (Dirac, not Poisson) |

**Decision rule (pre-committed):**
- If (2)+(3) cancel (1) modulo constraints → sector closes; **G-4 with sector note** or move toward Ṡ (G-1 route) — do **not** claim G-1 without Ṡ.
- If (2)+(3) leave a nonzero remainder and nothing absorbs it → **G-2 with K3 on this channel**.
- If (3) cannot be computed with filed methods → **ceiling G-4**; report (1) vs (2) as partial; do **not** terminal-fork on (1)+(2) alone unless remainder is clearly unabsorbable even granting (3) a free schematic form (state that argument explicitly if used).

---

## 2. K0′ gate (must pass before matter claims)

**Reproduce pure-HR ∂δ closure logic at GENERIC n ≠ 0** (not via n = 0 reduction).

**Pass criteria (pre-committed):**
1. Construct explicit \(D(n)\) from 1109.3515 (20)–(21) with \(n\neq 0\), \(x>0\); verify \(D\neq X\) generically.
2. On-shell minimal \(n(R_g)\) from (24) with \(R_g\neq 0\); verify \(n\neq 0\).
3. Show the vector \(\xi^i=(Dn)^i\) is the ∂δ-capable channel named in R4 §1–§2 (index type matches).
4. **Method check:** at ψ = 0, on-shell \(C_i=0\), the pure-HR expectation is `{C,C}_∂δ ≈ 0`. Implement the structural identity that the ∂δ coefficient is proportional to the spatial constraint combination that vanishes on-shell — **or** file failure of method and stop (nothing downstream counts).

**Fail K0′ → stop; land G-4 with blocker = method.**

---

## 3. Computational plan (engines)

- **NumPy + SymPy** (both available on host). Wolfram: not installed — will not claim Wolfram results.
- Script path (to be written after this file is saved): `Working\Opsi2_Round6_Correctly_Staged_ddelta_COMPUTE_CursorMain.py`
- Every verdict statistic must appear in the JSON emitted by that script.

### (1) Residual
Densitized θ-weights; \(R_\theta=h_g(\theta_g I-\theta_f X)^2\); vector \(r_{(1)}=R_\theta P\).

### (2) Vector channel + δn(P)
- Background: random SPD \((h_g,h_f)\), random \(R_g\neq 0\) → \(n=n_{\min}(R_g)\), \(D=D(n)\).
- Matter: finite-difference / Jacobian \(\delta n = (\partial n/\partial R)\,P\) from (24) with \(R\mapsto R+P\) (P as covector in same slot as \(R_g\)).
- Channel vector candidates (pre-registered; report all):
  - \(v_A = D\,(\delta n)\)
  - \(v_B = \delta(Dn)\) full (including \(D(n)\) dependence)
  - \(v_C = R_g\cdot(\partial(Dn)/\partial n)\,\delta n\) schematic weight if needed for density matching
- **Cancel test:** exists scalar α (or constrained α from HR normalizations) with \(\|α v + r_{(1)}\| / \|r_{(1)}\| < ε\) for ε = 10⁻⁶ on ≥ 90% of generic trials? Also report median angle / residual without fitting α if α is fixed by theory (prefer fixed).

### (3) χ-cross
- **Scope honesty:** full Dirac \(\{C_g^{(\psi)},C_f^{(\mathrm{grav})}\}_D\) at O(ψ²) is **not** closed-form in hand.
- Pre-commit: extract only structure already earned (shared-π_ψ χ ⇒ B1/B2 generically nonzero — R2). **Do not invent coefficients.**
- If no numeric (3): verdict marks (3) **uncomputed**; apply decision rule §1 ceiling.

---

## 4. Controls

| Control | Requirement |
|---|---|
| K1 | X = I ⇒ r_{(1)}=0; channel (2) consistent with 0 remainder |
| K2 | on-SVC metrics / on-shell n |
| K3 | G-2 only if remainder on **this** channel after (2)+(3) |
| F1 | decisive probes have n≠0, R_g≠0 |
| F14 | Poisson-only claims flagged; χ in ledger |
| Reproducibility | no statistic absent from script/JSON |

---

## 5. Fork pre-commit (no posterior movement claimed until compute)

Priors held until verdict: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

**Allowed landings:** G-2 (K3 met on correct channel); G-4 (blocker correctly staged); partial close toward G-1 only with explicit Ṡ deferral — **not** a silent G-1.

---

## 6. §4 edit status

Solution-map / S1–S2 “(N) undetermined” soften: **already filed** 2026-10-20 (accept handoff).

---

— Cursor Main, 2026-10-20. **Pre-registration filed. Compute begins only after this file exists on disk.**
