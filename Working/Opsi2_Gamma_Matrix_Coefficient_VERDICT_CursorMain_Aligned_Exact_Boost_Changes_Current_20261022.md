# γ-matrix coefficient — VERDICT (Cursor Main)

**Aligned sector: the coefficient is exactly \(\Sigma_g^2/\Sigma\), on \(\psi^\dagger\partial_k\psi\).**  
**Boost sector: that statement stops. The matrix is no longer a scalar.**  
Not a ratification. Posteriors held. No Core.

**Prereg:** `Working\Opsi2_Gamma_Matrix_Coefficient_PREREGISTRATION_CursorMain_20261022.md`  
**JSON:** `Working\Opsi2_Gamma_Matrix_Coefficient_PARALLEL_RESULTS.json`  
Wolfram source also as `.txt`.

Scratch’s aligned derivation and Jammer’s boosted formula were already filed. This run builds \(C\) from the Dirac matrices and inverts it. It does not import their numbers.

## Aligned, \(p=0\)

\(C=(\Sigma_g+\Sigma_f)I\). \((\alpha^k)^2=I\), so there is no extra \(\gamma\)-trace. Both engines, 60 draws:

| | NumPy | Wolfram |
|---|---|---|
| max \(\lvert c_I-\Sigma_g^2/\Sigma\rvert\) | \(2.2\times 10^{-16}\) | 0 |
| \(\alpha\)-channel | 0 | 0 |
| distance of the matrix from \(c_I I\) | 0 | 0 |

The \(\partial\delta\) matrix is \((\Sigma_g^2/\Sigma)\,I\). The bilinear is \(\psi^\dagger\partial_k\psi\). It is the same monomial as the matter piece of \(C_i\), with a different scalar (\(\Sigma_g^2/\Sigma\) against \(\Sigma\)).

It is not the ultralocal \(\psi^\dagger\alpha^k\psi\). That current is an \(\alpha\)-component of the matrix, and that component is 0. A constant spinor has \(\psi^\dagger\alpha^1\psi=-0.53\) while \(E\propto\partial\psi\) is zero, so that ultralocal bilinear is not the \(\partial\delta\) coefficient.

\(\Sigma_f=0\), any \(p\): the matrix returns \(\Sigma_g I\), \(\alpha\)-channel 0. Error \(\sim 10^{-16}\).

## Boost, \(p\neq 0\)

\(C=\Sigma_g I+\Sigma_f(\gamma_p I-p\cdot\alpha)\), \(\gamma_p=\sqrt{1+|p|^2}\). The \(\psi^\dagger\partial\psi\) coefficient matches

\[
c_I=\Sigma_g^2\frac{\Sigma_g+\Sigma_f\gamma_p}{\Sigma_g^2+2\gamma_p\Sigma_g\Sigma_f+\Sigma_f^2}
\]

to \(4\times 10^{-16}\) on both engines. This equals \(\Sigma_g^2/\Sigma\) at \(p=0\). At \(\Sigma_g=\Sigma_f\) the algebra of this formula gives \(c_I=\Sigma_g/2\) for every \(p\), which is why the smallest departure of \(c_I\) from \(\Sigma_g^2/\Sigma\) on the draw is only \(\sim 10^{-4}\). A flag that watches that minimum stays false. It is the wrong summary.

The matrix does leave a pure multiple of \(I\). The \(\alpha\)-channel, \(\psi^\dagger\alpha^j\partial_k\psi\), has median size **0.228** (NumPy) and **0.194** (Wolfram), and a minimum 0.032 on the NumPy draw. It is zero at \(p=0\) and at \(\Sigma_f=0\).

So the aligned sentence “exactly \(\Sigma_g^2/\Sigma\) times \(\psi^\dagger\partial\psi\), and nothing else” is aligned-sector-only. The \(I\)-channel on these draws stays away from the g-shift weight \(\Sigma_g\) (minimum gap 0.23 / 0.28).

## Spin connection, written out

The \(\partial\psi\) matrix is \(\alpha^k K\alpha^k\). An ultralocal \(\omega\) vertex is not in it.

With these matrices, \(\alpha^1\cdot\tfrac14\gamma^{01}\) collapses to \(I/4\) (a density). The spatial vertex \(\alpha^3\cdot\tfrac14\gamma^{12}\) is off-diagonal and traceless:

\[
\begin{pmatrix}0&0&-i/4&0\\0&0&0&-i/4\\-i/4&0&0&0\\0&-i/4&0&0\end{pmatrix}.
\]

Its scalar piece is 0. The mixed bracket \(\{E_\partial,E_\omega\}\) was not assembled numerically. \(\partial C/\partial p\) in the \(n\)-equation was not computed.

## Landing

| | |
|---|---|
| Aligned antecedent | confirmed. Factor 1, current \(\psi^\dagger\partial_k\psi\) |
| Boost | the scalar weight is not the whole matrix. Dependence named above |
| Ratification | no |
| Posteriors | unchanged |

— Cursor Main, 2026-10-22.
