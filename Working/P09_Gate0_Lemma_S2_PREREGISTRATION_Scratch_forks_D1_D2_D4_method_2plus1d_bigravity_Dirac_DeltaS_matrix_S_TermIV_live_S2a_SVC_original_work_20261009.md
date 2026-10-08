# P09 Gate-0 — Lemma S2 PREREGISTRATION (Scratch, construction)

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-09
**Authority:** Greg GO — “GO on recommended next”; Directive `Directive_Cursor_Main_to_Scratch_Jammer_Lemma_S2_2plus1d_Bigravity_Dirac_GO_Original_Work_20261009.md`; GO `GO_Greg_Lemma_S2_2plus1d_Bigravity_Dirac_Matrix_S_Authorized_20261009.md`; AC R4 in `Arbitration_AC_Lemma_S1_D4_Ratified_…_20261009.md`
**Status:** PRE-REGISTERED BEFORE COMPUTING — forks and method declared; results follow in separate VERDICT file
**Blind to:** all `Jammer*Lemma_S2*` attack / prereg files (not read)
**Label:** ORIGINAL WORK — 2+1d bigravity + Dirac secondary-constraint algebra with matrix \(S\); no silent prior-art borrow

---

## 0. Banked (do not re-derive)

- Gate 0 = **W-2 / undetermined**; chair lean D2 ~67% (unchanged by S1).
- **Lemma S1 (1+1d):** D4 ratified. \(S\) scalar ⇒ B4 invisible; Term II/IV specialised away. **Do not re-run 1+1d.**
- Primary lapse-linearity banked (D3 out). Relative boost auxiliary (B3). Dirac vs \(e_n(S)\) mismatch banked (B4) — **now to be probed**.
- Symmetric ν excluded on N_eff ≈ 1.52 (~10σ). **Even D1 does not restore it.**
- No κ. No f. No Core. Deposit P04.

---

## 1. Exact object

In **2+1 dimensional bigravity + Dirac** (two spatial dimensions):

\[
\Delta\mathcal{S}
\;\equiv\;
\{C_g^{(\mathrm{D})}, C_f^{(\mathrm{grav})}\}
+ \{C_g^{(\mathrm{grav})}, C_f^{(\mathrm{D})}\}
+ \{C_g^{(\mathrm{D})}, C_f^{(\mathrm{D})}\}
+ (\text{Dirac-bracket corrections})
\]

at \(O(\psi^2)\) on the constraint surface (after modified SVC / relative-boost elimination as needed).

**Must retain:**
1. \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) as a **non-scalar** \(2\times 2\) matrix (B4 live), and
2. **Nondegenerate gravitational kinetics** (Term IV / π-channel live).

**Sub-lemma S2a (prerequisite):** modified SVC \(\Lambda^*(\gamma_g,\gamma_f,\psi)\) to leading order in 2+1d — file with or before the bracket.

**Out of scope:** FLRW-only mini-superspace; re-running 1+1d; full 3+1d \(O(\psi^2)\) (separate GO if needed after S2).

---

## 2. Pre-registered forks (AC R4 provisional — fixed before computing)

| S2 outcome (2+1d) | Meaning | Gate 0 action |
|---|---|---|
| **D2** | \(\Delta\mathcal{S}\not\approx 0\) spoils secondary / B4 active with live π; ghost-return structure in 2+1d | Eligible for **W-3** (AC ratifies before close) |
| **D1** | Secondary survives (possibly modified) in 2+1d | Maintain **W-2**; 2+1d D1 is **suggestive only** — transfer to 3+1d needs AC scrutiny / likely separate GO |
| **D4** | Inconclusive, or setting still fails to resolve the Gate-0 question honestly | Maintain **W-2**; reassess setting |

**Failure licensed.** Prefer honest D2 or D4 over a fake D1. Even D1 ≠ restore symmetric ν. No f. Not a route to κ.

---

## 3. Method — declared before any bracket evaluation

**Step 0 — Setup (2+1d).**
- Spacetime \((t,x^1,x^2)\); spatial metrics \(\gamma_{ij}^{(g)},\,\gamma_{ij}^{(f)}\) (symmetric \(2\times 2\)); momenta \(\pi_g^{ij},\,\pi_f^{ij}\).
- Square-root matrix \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) — genuine **non-scalar** \(2\times 2\). Elementary symmetric polynomials: \(e_0=1\), \(e_1=\mathrm{tr}\,S\), \(e_2=\det S\).
- Relative Lorentz: \(\mathrm{SO}(1,2)_{\mathrm{rel}}\) — 3 parameters (2 boosts + 1 rotation). Dirac: 2-component spinor; diagonal \(\mathrm{Spin}(1,2)\) only.
- HR potential: \(V=\sqrt{\gamma_g}\,(\beta_0+\beta_1 e_1(S)+\beta_2 e_2(S))\) (equiv. form OK).
- Gravitational kinetics: DeWitt supermetric in \(d=2\) spatial dimensions,
  \[
  \mathcal{H}_\perp^{(I)}\supset\frac{1}{\sqrt{\gamma_I}}\Big(\pi_I^{ij}\pi_{I\,ij}-\pi_I^2\Big),
  \]
  nondegenerate on traceless \(\pi\) — **Term IV channel live** (contrast 1+1d topological EH).
- **Mandatory caveats to record in verdict:** (i) 2+1d bulk graviton count ≠ 3+1d; (ii) Cayley–Hamilton for \(2\times 2\) \(S\) does **not** automatically collapse matrix-element dependence of Dirac bilinears to \(\{e_n(S)\}\) — record whether B4 survives that identity.

**Step 1 — S2a (modified SVC).**
Solve \(\partial V_{\mathrm{HR}}/\partial\Lambda_{\mathrm{rel}}+\partial H_{\mathrm{Dirac}}/\partial\Lambda_{\mathrm{rel}}=0\) perturbatively about the pure-gravity SVC root \(\Lambda_0\). Record \(\Lambda^*=\Lambda_0+O(\psi^2)\). Corollary: at \(O(\psi^2)\), evaluate Dirac contributions at \(\Lambda_0\) (take time-gauge alignment \(\varphi_0=0\)).

**Step 2 — Effective constraints at \(O(\psi^2)\).**
Substitute \(\Lambda^*\). Expand \(C_g=C_g^{(\mathrm{grav})}+C_g^{(\mathrm{D})}\), \(C_f=C_f^{(\mathrm{grav})}+C_f^{(\mathrm{D})}\). In symmetric-vielbein presentation \(\varepsilon_\alpha{}^i=e_\alpha{}^j S_j{}^i\), identify which Dirac pieces depend on matrix elements of \(S\) vs only on \(e_n(S)\).

**Step 3 — Dirac second-class reduction.**
\(\chi=\pi_\psi-\Sigma\psi^\dagger\), \(\Sigma=\sqrt{\gamma_g}\,A_g+\sqrt{\gamma_f}\,A_f\). Pass to Dirac bracket. Track Term (IV) through \(\{C^{(\mathrm{grav})},\Sigma\}\neq 0\).

**Step 4 — Compute \(\Delta\mathcal{S}\) term by term at \(O(\psi^2)\) on the constraint surface.**
- (II) cross: especially \(\{C_g^{(\mathrm{grav})},C_f^{(\mathrm{D})}\}\) via \(\delta C_f^{(\mathrm{D})}/\delta\gamma_g\) acting on \(S^i{}_j\)
- (III) pure Dirac: \(\{C_g^{(\mathrm{D})},C_f^{(\mathrm{D})}\}_D\)
- (IV) Dirac-bracket corrections involving π-channel

Decide weakly-zero vs not. If modified secondary \(\mathcal{S}^{(0)}+\Delta\mathcal{S}\approx 0\) appears, check whether HR polynomial identities extend to the \(\Delta_{\mathrm{II}}\) piece under preservation, or fail (B4 active).

**Step 5 — Landing discipline.**
- If B4 invisible or Term IV dead despite 2+1d setup → D4 (setting failed its design purpose).
- If \(\Delta\mathcal{S}\approx 0\) weakly by a genuine identity → D1 (suggestive only).
- If \(\Delta\mathcal{S}\not\approx 0\) with B4-active matrix-element channel and HR preservation not inherited → D2 (W-3-eligible).
- If algebra blocks short of that decision → honest D4.

---

## 4. Self-threats (construction attacks itself)

1. **Cayley–Hamilton fake cancellation:** \(S^2-(\mathrm{tr}\,S)S+(\det S)I=0\) spans \(\{I,S\}\), but Dirac contraction \(S_j{}^i B_i{}^j\) collapses to \(e_n\) only if \(B\propto I\); do not claim B4 dead from CH alone.
2. **2+1d dof ≠ 3+1d:** even a clean D2 here needs AC ratification for W-3; do not silently equate spin-2 counts.
3. **φ*-induced O(ψ⁴):** do not smuggle relative-boost corrections into \(O(\psi^2)\) Term II; use S2a corollary.
4. **Fake D1:** do not land transferable D1 from a partial cancellation or from Term III alone (S1 lesson).
5. **Blindness:** do not read Jammer S2 prereg if it appears mid-flight.

---

## 5. Expected landing (stated before computing)

**D2 or honest D4.** I expect B4 to be live (matrix \(S\); Term II through \(\partial S^i{}_j/\partial\gamma\)), Term IV live (DeWitt π-channel), and net \(\Delta\mathcal{S}\not\approx 0\) on the generic constraint surface — favouring D2 / W-3-eligible. If preservation of the modified secondary cannot be closed honestly, land D4 with B4-probed status recorded rather than a fake D1.

---

— Scratch, 2026-10-09. Pre-registered before computing. Original work. Blind to Jammer S2.
