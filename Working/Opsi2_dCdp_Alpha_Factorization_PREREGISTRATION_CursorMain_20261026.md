# PRE-REGISTRATION — the four open blockers

**Filed before the run.** Nothing newer than the 2026-10-22 watermark is in the inbox. These are the four items Jammer left blocking a terminal G-2.

**Engines:** NumPy and Wolfram Engine 15 for the matrix projection. SymPy for the multiplier degree. No Core. Posteriors held.

## Objects

\(C(p)=\Sigma_g I+\Sigma_f(\gamma_p I-p\cdot\alpha)\), \(\gamma_p=\sqrt{1+|p|^2}\).

The \(\partial\psi\) matrix of the bracket, one direction \(k\), is \(M=\Sigma_g^2\alpha^k C^{-1}\alpha^k\).

The mismatch against the g-shift weight is \(\Delta=M-\Sigma_g I\).

\(\partial C/\partial p_i=\Sigma_f(p_i/\gamma_p\,I-\alpha^i)\), computed by differentiating \(C\), not typed in.

## Decision

1. **\(\partial C/\partial p\).** Project \(\Delta\) onto \(\mathrm{span}\{\partial C/\partial p_i\}\) in the Frobenius product. If the relative residual stays above \(10^{-2}\) for \(\Sigma_f>0\), including at \(p=0\), this term does not cancel the mismatch, whether or not \(p\) is the Hassan–Rosen \(n\). If the residual is below \(10^{-8}\), the escape works and the landing is not G-2.
2. **\(\alpha\) channel on the constraint surface.** Project \(M\) onto \(C\). A relative residual above \(10^{-2}\) means \(M\) is not a multiple of the constraint matrix.
3. **Boosted shift factorization.** With \(p\) not among \((N,L,L^i)\), the Dirac matter term under \(N_g=L^i+Ln+N(Dn)\) must stay degree 1. A scalar \((N_g\cdot J)^2/N\) must not.
4. **\(p\) versus \(n\).** Not identified from the papers in this run. Report both readings: \(p\) on its own stationarity condition (the \(\partial C/\partial p\) piece multiplies that equation and drops out), and \(p\) varied freely against \(n\) (the projection above, the most generous cancellation).

\(\Sigma_f=0\) must give \(\|\Delta\|<10^{-8}\).

Posteriors stay G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Cursor Main, 2026-10-26.
