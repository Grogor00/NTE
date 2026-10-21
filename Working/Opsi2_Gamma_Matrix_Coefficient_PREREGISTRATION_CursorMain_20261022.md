# PRE-REGISTRATION — γ-matrix coefficient, current identity, boost sector

**Filed before the run.**  
**Directive:** `Handoffs\Directive_Scratch_to_CursorMain_Gamma_Matrix_Numeric_Exact_Coefficient_Current_Identity_And_Boost_Sector_CN_CN_D_20261022.md`  
**Engines:** NumPy and Wolfram Engine 15. No Core. Posteriors held.

Jammer’s boosted formula and Scratch’s aligned derivation are already filed. This run does not import their numbers. It builds \(C\) from Dirac matrices and inverts it.

## Setup

Dirac representation. \(\alpha^i=\gamma^0\gamma^i\). g-frame in time gauge. Relative boost \(p\), \(\gamma_p=\sqrt{1+|p|^2}\):

\[
C=\Sigma_g\,I+\Sigma_f(\gamma_p I-p\cdot\alpha),\qquad K=C^{-1}.
\]

The derivative leg is \(E\supset\Sigma_g\,\psi^\dagger\alpha^k\partial_k\psi\). Its \(\partial\delta\) matrix is \(\Sigma_g^2\,\alpha^k K\alpha^k\) (no sum on \(k\)). The spin connection is the ultralocal piece \(\Sigma_g\psi^\dagger\alpha^k(\tfrac14\omega_{kab}\gamma^{ab})\psi\), with \(\gamma^{ab}=\tfrac12[\gamma^a,\gamma^b]\) written as matrices.

## Decision

- **Aligned (\(p=0\)).** Pass only if the matrix equals \((\Sigma_g^2/\Sigma)\,I\) to \(10^{-8}\), so the numerical factor in front of \(\Sigma_g^2/\Sigma\) is 1, and the bilinear is \(\psi^\dagger\partial_k\psi\). Fail if a \(\gamma\)-trace multiplies that factor, or if the bilinear is the ultralocal \(\psi^\dagger\alpha^k\psi\).
- **Boost (\(p\neq 0\)).** If that matrix leaves \((\Sigma_g^2/\Sigma)\,I\), the simple weight is aligned-sector-only. Name the \(p\) dependence. Do not call the boosted theory the aligned result.
- **\(\omega\).** It may add a no-derivative bilinear. It must not change the coefficient of \(\psi^\dagger\partial_k\psi\).

\(\Sigma_f=0\) must return \(\Sigma_g\,I\) at any \(p\) that remains after the \(f\)-leg is removed.

Posteriors stay G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Cursor Main, 2026-10-22.
