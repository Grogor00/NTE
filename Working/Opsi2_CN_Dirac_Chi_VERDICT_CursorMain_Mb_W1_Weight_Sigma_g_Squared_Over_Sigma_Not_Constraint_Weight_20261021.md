# χ-corrected {C_N, C_N}_D — VERDICT (Cursor Main)

**Lane result: M-b, W-1 (5.5-mode G-2).** AC rules whether that is the project fork.  
**Not blind:** the Scratch directive was read before this run. Tests were fixed in the pre-registration.  
**Prereg:** `Working\Opsi2_CN_Dirac_Chi_PREREGISTRATION_CursorMain_NotBlind_Directive_Read_20261021.md`  
**JSON:** `Working\Opsi2_CN_Dirac_Chi_PARALLEL_RESULTS.json` (NumPy ∥ Wolfram, 200 backgrounds each).  
**No Core. No f.** Posteriors not moved.

---

## 1. Field content of the diagonal correction

R3’s cross term \(B_1\) is \((\Sigma_g/\Sigma)(\psi^\dagger\alpha^k\psi)\,(\pi_f)\), because one leg is \(C_f^{(\mathrm{grav})}\).

The diagonal has **two** \(E_g\) legs. \(E_g\) does not contain \(\pi_f\), so \(\{\chi,E_g\}\) has no \(\pi_f\). With \(E_g\supset\Sigma_g\psi^\dagger\alpha^k\nabla_k\psi\) and \(C^{-1}\sim\Sigma^{-1}\),

\[
\bigl[-\{E_g,\chi\}C^{-1}\{\chi,E_g\}\bigr]_{\partial\delta}
\;\propto\;
\frac{\Sigma_g^{2}}{\Sigma}\,p_j,
\qquad \Sigma=\Sigma_g+\Sigma_f.
\]

**Same monomial as \(p_j\).** The R3 “bilinear × π, not \(W\cdot p\)” distinctness **does not** hold for this diagonal. M-b is not that shortcut.

## 2. Why it still fails weak vanishing (F23)

The matter piece of \(C_i^{\mathrm{tot}}\) is the canonical momentum \(\pi_\psi\partial_i\psi\propto\Sigma\,p_j\). The bracket weight is \(\Sigma_g^{2}/\Sigma\), not \(\Sigma\). Their ratio is \((\Sigma_g/\Sigma)^{2}\neq 1\) once \(\Sigma_f\neq 0\).

∂δ covector \(v=R+(\Sigma_g^{2}/\Sigma)\,p\), constraint direction \(u=R+\Sigma\,p\). Projection, not a scalar fit:

| | NumPy | Wolfram |
|---|---|---|
| n | 200 | 200 |
| median \(\|v-\mathrm{proj}_u v\|/\|v\|\) | **0.425** | **0.399** |
| fraction \(>10^{-3}\) | **1.0** | (same test, pass_Mb true) |
| \(\Sigma_f=0\) max residual | **0** | **0** |
| K5 swap \(\Sigma_g\leftrightarrow\Sigma_f\), median residual | **0.373** | in JSON `median_rel_swap` |

The residual is not removed by varying \(n\) (F19): the ratio is built from \(\Sigma_g,\Sigma_f\), which the matter-modified multiplier does not set equal. L-sector (F21) holds \(E_f\); it is not inside this gate. Gate is \(C_N\) (F20). Bracket used is Dirac (F22).

## 3. Fork

| | |
|---|---|
| M-a / W-0 | no — weight is not the constraint weight |
| **M-b / W-1** | **yes — f-dependence in the gate’s own self-bracket, projection residual survives** |
| W-2 | not taken |

**W-1 here means HR case 1: the lapse is fixed and the phase space is odd (5.5 modes), not a fully restored Boulware–Deser mode.**

**Caveat, load-bearing:** spin connection and a term-by-term Grassmann expansion are not in the script. The claim is the two-leg contraction: \(p_j\) with weight \(\Sigma_g^{2}/\Sigma\) against \(C_i\) weight \(\Sigma\). If the canonical momentum is normalised differently, the ratio changes and this landing moves with it.

\(\mathcal{S}\)-block not opened: the self-bracket did not vanish weakly.

— Cursor Main, 2026-10-21.
