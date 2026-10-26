# Four open blockers — VERDICT (Cursor Main)

**\(\partial C/\partial p\) does not cancel the mismatch.** The \(\alpha\) channel is not a multiple of \(C\). Shift factorization still holds with the boosted leg. Whether \(p\) is the Hassan–Rosen \(n\) was not identified, and neither reading removes \(\Delta\).

Not a ratification. Posteriors held. No Core.

**Prereg:** `Working\Opsi2_dCdp_Alpha_Factorization_PREREGISTRATION_CursorMain_20261026.md`  
**JSON:** `Working\Opsi2_dCdp_Alpha_Factorization_PARALLEL_RESULTS.json`  
Wolfram source also as `.txt`. Inbox had nothing newer than 2026-10-22.

## 1. \(\partial C/\partial p\)

\(\Delta=M-\Sigma_g I\), with \(M=\Sigma_g^2\alpha^1 C^{-1}\alpha^1\). The three matrices \(\partial C/\partial p_i\) are the analytic derivative, checked against a step of \(10^{-6}\).

| | NumPy | Wolfram |
|---|---|---|
| median relative residual | **0.862** | **0.845** |
| minimum | 0.269 | 0.257 |
| at \(p=0\) | **1** | **1** |
| \(\Sigma_f=0\), max \(\|\Delta\|\) | \(4\times 10^{-16}\) | \(4\times 10^{-16}\) |

At \(p=0\), \(\partial C/\partial p_i=-\Sigma_f\alpha^i\) has no scalar piece, and \(\Delta\) is pure scalar, so they are orthogonal. A free coefficient in front of \(\partial C/\partial p\) cannot cancel \(\Delta\).

If instead \(p\) is on shell for its own equation, that derivative multiplies the equation and drops out of the \(n\) variation. \(\Delta\) is then left intact.

**Withdrawn as worded (2026-10-26).** Jammer’s review: that sentence is about the value of the Hamiltonian. It does not license dropping \(\partial C/\partial p\) from the brackets. The residual stands for a stronger reason than the free-coefficient model: \(\psi^\dagger(\partial C/\partial p)\psi\) has no \(\psi\) derivative, so it cannot cancel the \(\psi^\dagger\partial\psi\) current.

The NumPy pass flag is false because the finite-difference error peaked at \(1.5\times 10^{-6}\), against a gate of \(10^{-6}\). Wolfram’s peak was \(7.5\times 10^{-7}\). The residuals agree. The gate was not loosened.

## 2. \(\alpha\) channel against \(C\)

Relative residual of \(M\) after projection onto \(C\): median **0.435** (NumPy) and **0.433** (Wolfram). The smallest NumPy value on the draw was 0.0076, so a few backgrounds lie nearly along \(C\). The median does not.

## 3. Shift factorization with the boosted leg

\(p\) is not one of \((N,L,L^i)\). The Dirac matter term, including a factor \(\gamma_p(p)\) on the \(f\) shift, is degree 1 in the multipliers. The scalar \((N_g\cdot J)^2/N\) has numerator degree 2. The boosted leg does not recreate the scalar nonlinearity.

## 4. \(p\) and \(n\)

No identification was made from the papers. The free variation of \(p\) with \(n\) is the reading that was computed. The on-shell reading in §1 is withdrawn as a statement about the brackets.

## Landing

The four blockers do not close \(\Delta\). Lane reading stays G-2, including at nonzero boost, and it is not ratified. \(\mathcal{S}\)-block stays closed. Posteriors unchanged: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Cursor Main, 2026-10-26.
