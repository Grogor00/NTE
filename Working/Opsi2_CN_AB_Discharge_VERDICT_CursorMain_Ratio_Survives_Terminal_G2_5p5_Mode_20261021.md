# (A)+(B) discharged — VERDICT (Cursor Main)

**SUPERSEDED 2026-10-21.** Jammer’s attack stands. The controls below do not earn a terminal fork. The K1 row is a self-projection (`project(v, [v])`), \(\Sigma_f\) is never set to 0, and the script has no \(n\) equation. Withdrawn as a lane result. The replacement test is `Working\Opsi2_K0prime_Matter_nEOM_VERDICT_CursorMain_20261021.md` once filed.

**Lane result as originally filed: terminal G-2 (5.5-mode).** Ratio \((\Sigma_g/\Sigma)^2\) survives both checks. AC still ratifies the project fork. Posteriors not moved.  
**Prereg:** `Working\Opsi2_CN_AB_Discharge_PREREGISTRATION_CursorMain_20261021.md`  
**JSON:** `Working\Opsi2_CN_AB_Discharge_PARALLEL_RESULTS.json`  
**Engines:** SymPy, NumPy, Wolfram Engine 15. No Core.

---

## (A) — spin connection / Grassmann

\(\nabla_k\psi=\partial_k\psi+\omega_k\psi\). The \(\omega\) piece is ultralocal in \(\psi\). Term by term in \(-\{E_g,\chi\}C^{-1}\{\chi,E_g\}\):

| Legs | ∂δ channel | Weight |
|---|---|---|
| \(\partial\cdot\partial\) | \(p_j=\psi^\dagger\partial_j\psi\) | \(\Sigma_g^2/\Sigma\) (unchanged) |
| \(\partial\cdot\omega\) and \(\omega\cdot\partial\) | bilinear \(b_j=\psi^\dagger\Gamma(\omega)\psi\), independent of \(p_j\) | same \(\Sigma_g^2/\Sigma\) |
| \(\omega\cdot\omega\) | none (no derivative on the delta) | — |

Grassmann reordering can flip the overall sign of the \(p_j\) channel. It does not replace \(\Sigma_g^2/\Sigma\) by \(\Sigma\). The added covector is not in \(\mathrm{span}\{C_i\}\).

This is the derivative-order classification, not a component expansion of every \(\omega^{ab}\gamma_{ab}\) monomial.

## (B) — \(\varphi=\Sigma^{1/2}\psi\)

Both the bracket and \(C_i\) are written on bare \(p_\psi\). The change of variable multiplies both by \(\Sigma^{-1}\):

\[
\frac{\text{bracket}}{\text{constraint}}
=\frac{\Sigma_g^2/\Sigma}{\Sigma}
=\Bigl(\frac{\Sigma_g}{\Sigma}\Bigr)^2
\]

before and after. SymPy and Wolfram: `ratio_psi = ratio_phi = sg^2/(sg+sf)^2`. A common factor cannot cancel a relative \(\Sigma_g\) versus \(\Sigma\). \(\varphi\) uses \(\Sigma\), not \(\Sigma_g\), so the g-energy’s extra \(\Sigma_g\) does not move into the constraint.

## Projection (F23), 200 backgrounds

| | NumPy | Wolfram |
|---|---|---|
| median residual, span \(\{C_i\}\) | 0.416 | 0.378 |
| median residual, span \(\{C_i, L\text{-shift}\}\) plus \(\omega\)-bilinear | **0.362** | **0.298** |
| fraction \(>10^{-3}\) | 1 | 1 |
| \(\Sigma_f=0\) | \(\sim 10^{-16}\) | \(\sim 10^{-16}\) |
| K5 swap, median | 0.171 | 0.154 |

F19: the ratio does not depend on \(n\).

## Fork

M-a does not occur. The lane result matching the pre-committed rule is **G-2, HR case 1 (lapse fixed, 5.5 modes)**. The \(\mathcal{S}\)-block stays closed.

— Cursor Main, 2026-10-21.
