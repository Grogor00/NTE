# Boost full-matrix n-equation — verdict

**Lane result. Not a ratification.** Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. No Core.

**Run:** `Working\Opsi2_Boost_FullMatrix_nEOM_PARALLEL_CursorMain.py`  
**JSON:** `Working\Opsi2_Boost_FullMatrix_nEOM_PARALLEL_RESULTS.json`  
**Wolfram:** `Working\Opsi2_Boost_FullMatrix_nEOM_WOLFRAM.json` (flat \(\gamma\); the 3-metric \(n\)-equation is the NumPy run)

The bracket matrix is \(M_k=\Sigma_g^2\,\alpha^k C^{-1}\alpha^k\), built from the Dirac matrices. \(C=\Sigma_g I+\Sigma_f(\gamma_p I-p\cdot\alpha)\). The \(n\)-equation uses the g-weight \(\Sigma_g\) on the \(I\)-channel current. \(P\) carries \(c_I\) and the \(\alpha\) channel. \(\psi^\dagger(\partial C/\partial p)\psi\) is computed from a normalised spinor and from the analytic derivative.

## NumPy, 80 boost draws, median

| | |
|---|---|
| \(\|P-\mathcal{C}_N(Dn)\|\) | 0.778 |
| \(\alpha\)-channel piece | 0.291 |
| \(I\)-channel piece, \(c_I-\Sigma_g\) | 0.587 |
| fraction of that vector orthogonal to the ultralocal source | 0.806 |
| draws with residual \(>10^{-3}\) | 1.00 |
| \(\max\|c_I-\text{closed form}\|\) over all three directions | \(6.7\times 10^{-16}\) |
| remainder outside \(\mathrm{span}\{I,\alpha^i\}\) | \(4.4\times 10^{-16}\) |
| finite-difference of \(\partial C/\partial p\), step \(10^{-6}\) | \(1.8\times 10^{-6}\) |

Pure HR in the same run: max residual 0, off-shell \(\|P\|\) at least 0.060. Pass.

\(\Sigma_f=0\) is an exact draw, 40 backgrounds, \(p\neq 0\): median residual \(2.2\times 10^{-16}\), \(\alpha\) coefficient 0.

K5 rebuilds \(C\) after \(\Sigma_g\leftrightarrow\Sigma_f\). Median residual 0.678. Fraction above \(10^{-3}\) is 1.

\(\Sigma_g=\Sigma_f\): \(c_I=\Sigma_g/2\) to a median absolute error of 0, at every \(p\) in the draw. Median residual 0.590. Median \(\alpha\) coefficient 0.248.

\(p=0\): \(\alpha\) coefficient 0. Median residual 0.679, the aligned mismatch \(c_I=\Sigma_g^2/\Sigma\) against \(\Sigma_g\).

## What \(\partial C/\partial p\) does in this equation

Routing the ultralocal vector \(u_i=\psi^\dagger(\partial C/\partial p_i)\psi\) through the solved \(n\)-equation leaves \(\gamma^{-1}u\) in \(P-\mathcal{C}_N(Dn)\). The largest such shift on the draw is 4.00. The current residual is a different vector: after removing its projection onto \(u\), the median fraction left is 0.806.

## Wolfram, flat \(\gamma\), 40 draws

Median residual 0.831. Median \(\alpha\) piece 0.431. Median \(I\) piece 0.658. Median orthogonal fraction 0.911. Closed form, all three directions, max error \(3.9\times 10^{-16}\). \(\Sigma_f=0\): max residual \(6.4\times 10^{-16}\), \(\alpha\) coefficient 0.

The two medians are different draws. Both are order 1, and both \(\Sigma_f=0\) limits are roundoff.

## Not in this run

The mixed bracket \(\{E_\partial, E_\omega\}\) was not assembled.

— Cursor Main, 2026-10-27.
