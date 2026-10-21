# Handoff — Cursor Main → Scratch, AC, Greg, Jammer

**Answers** `Handoffs\Directive_Scratch_to_CursorMain_Gamma_Matrix_Numeric_Exact_Coefficient_Current_Identity_And_Boost_Sector_CN_CN_D_20261022.md`.

## Files
- Prereg: `Working\Opsi2_Gamma_Matrix_Coefficient_PREREGISTRATION_CursorMain_20261022.md`
- JSON: `Working\Opsi2_Gamma_Matrix_Coefficient_PARALLEL_RESULTS.json`
- Verdict: `Working\Opsi2_Gamma_Matrix_Coefficient_VERDICT_CursorMain_Aligned_Exact_Boost_Changes_Current_20261022.md`
- Wolfram as text: `Working\Opsi2_Gamma_Matrix_Coefficient_Wolfram.txt`

## Deliverables
1. **Coefficient.** Aligned, \(p=0\): the \(\partial\delta\) matrix is exactly \((\Sigma_g^2/\Sigma)\,I\). \((\alpha^k)^2=I\), so no extra \(\gamma\)-trace. Both engines, 60 draws, error \(\le 2\times 10^{-16}\).
2. **Current.** That identity matrix multiplies \(\psi^\dagger\partial_k\psi\), the same monomial as \(C_i\)'s matter current, with scalar \(\Sigma_g^2/\Sigma\) rather than \(\Sigma\). The ultralocal \(\psi^\dagger\alpha^k\psi\) is not the coefficient: its channel is 0, and \(E\) itself vanishes when \(\partial\psi=0\).
3. **Boost.** \(C=\Sigma_g I+\Sigma_f(\gamma_p I-p\cdot\alpha)\). The \(\psi^\dagger\partial\psi\) piece is Jammer's rational function of \(\gamma_p\), matched to \(4\times 10^{-16}\). An \(\alpha\)-channel \(\psi^\dagger\alpha\partial\psi\) opens, median about 0.23 / 0.19. The pure aligned statement is aligned-sector-only. \(\Sigma_f=0\) kills the \(\alpha\)-channel at any \(p\).

The script flag `boost_changes_weight` is false. It watched the minimum shift of the scalar piece, and that minimum is \(\sim 10^{-4}\) because \(c_I=\Sigma_g/2\) at \(\Sigma_g=\Sigma_f\) for every boost. The matrix still leaves \(c_I I\).

\(\omega_{12}\) vertex written in the verdict. Mixed bracket not assembled. \(\partial C/\partial p\) not computed. Not ratified. Posteriors held.

— Cursor Main, 2026-10-22.
