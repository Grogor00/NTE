# Pre-registration — one O(ψ⁴) run, ³f Hessian

**Filed before the script and before the run.** No numbers from this test exist.
**Under:** the 2026-10-31 ruling §5, Scratch's eq (10) note, and Jammer's 2026-11-01 reduction. The two readouts are one run.
**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.
**This run does not move posteriors and does not declare the ghost.**

## The Hessian

\(A = L\,{}^3f + N\,{}^3f D\), with \(D\) frozen at the background. \({}^3f\) is the f-sector spatial metric of that background. \(D^{-T}\) is \({}^3f D^{-1} {}^3f^{-1}\). It is not a numerical transpose of \(D\).

The quartic piece is \(-\tfrac12 G\cdot A^{-1}G\). \(G\) is the \(n\)-derivative of the g-leg, the f-leg, and the kinetic piece, as in the 2026-10-31 substitution, with the boost vector equal to \(n\).

## What is reported

Forty backgrounds. Medians.

- Frozen-\(D\), \(\Sigma_f=0\), g-leg only. This is the control.
- Frozen-\(D\) full median, g-leg plus f-leg plus kinetic.
- Identity residual \(\|u_f + k_f - D^{-T} k_g\|/\max(\|u_f+k_f\|,\|D^{-T}k_g\|,10^{-15})\). \(u_f\) is the f-leg \(n\)-gradient at \(L=1\). \(k_f\) is the kinetic gradient of the \(L\)-weighted \(M\) piece. \(k_g\) is the kinetic gradient of the \(N\)-weighted \(\alpha\) piece.
- Live g-only median, with the same \(A\) built from \(D(n_0)\). Diagnostic only.
- Median relative asymmetry of \({}^3f D\). Diagnostic only.

## Outcomes

- **No decision.** The frozen control median is \(\ge 10^{-8}\), or more than half the backgrounds have a singular \(A\).
- **Void.** The control passes, and the full median and the identity residual sit on opposite sides of the bars below.
- **Removed.** The control passes, the full median is \(<10^{-8}\), and the identity residual is \(<10^{-8}\).
- **Survives.** The control passes, the full median is \(>10^{-3}\), and the identity residual is \(>10^{-3}\).
- **No decision** also if both medians fall between the two bars.

The live median is not a bar. A failed control decides nothing.
