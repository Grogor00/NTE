# K0′ with matter — VERDICT (Cursor Main)

**Lane result: G-2 (5.5-mode). Not a ratification.**  
On the surface \(\mathcal{C}_N=0\), with the \(n\) equation solved, \(P\) is not \(\mathcal{C}_N(Dn)\).  
**Prereg:** `Working\Opsi2_K0prime_Matter_nEOM_PREREGISTRATION_CursorMain_20261021.md`  
**JSON:** `Working\Opsi2_K0prime_Matter_nEOM_PARALLEL_RESULTS.json`  
**Engines:** NumPy and Wolfram Engine 15. Wolfram source also as `.txt` (Drive does not open `.wl`).  
**No Core.** Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. \(\mathcal{S}\)-block stays closed.

The (A)+(B) terminal filing is withdrawn. Jammer’s reading of that script is right.

---

## 1. What was wrong in the withdrawn filing

Confirmed in `Opsi2_CN_AB_Discharge_PARALLEL_CursorMain.py`:

- The labelled K1 control is `project(R+sg*p, [R+sg*p])`. A vector projected onto itself is zero, and `pass_G2` required that zero.
- \(\Sigma_f\) is drawn from \((0.3, 2)\). The “\(\Sigma_f=0\)” row was that same self-projection.
- (B) divides numerator and denominator by \(\Sigma\) in the expression. It is not a change of variables.
- The \(\omega\) term is added to the vector being projected. The second column is a bare random vector. There is no \(n\) equation.

**K1, as AC asked it:** accepted as Jammer’s K-ii. At \(e=f\), \(\Sigma_g=\Sigma_f\), and the retired ratio of the bracket weight against \(\Sigma\) is \(1/4\). That arithmetic is right, and it is not a failing control for \(\mathcal{C}_N\). K1 belongs to \(\mathcal{C}_{\mathrm{SC}}\). The limit that must close for \(\mathcal{C}_N\) is \(\Sigma_f=0\).

## 2. This run

The vacuum identity of the K0′ engine is

\[
P_{\mathrm{grav}}=\mathcal{C}_{\mathrm{grav}}(Dn)+\gamma^{-1}(R-U).
\]

The \(n\) equation with the g-shift weight is \(R+\Sigma_g\,\mathrm{cur}=U\), \(\mathrm{cur}=J+b\). \(\mathcal{C}_N\) contains \(E_g+(Dn)\cdot(\Sigma_g\,\mathrm{cur})\). The total momentum \(\Sigma\,\mathrm{cur}\) is solved by an f-momentum \(R_f\), which does not enter \(P\) or \(\mathcal{C}_N\).

Ordinary matter is required to obey the same identity whenever the bracket weight equals the g-shift weight. The \(\chi\) change replaces only that weight, \(\Sigma_g\to\Sigma_g^2/\Sigma\). The prereg states this completion. It is not a \(\gamma\)-matrix derivation of \(\{E_g,E_g\}_D\).

Checked identity, both engines, max error \(\sim 10^{-15}\):

\[
P-\mathcal{C}_N(Dn)=\Sigma_g(\theta_g-1)\,\gamma^{-1}(J+b),\qquad\theta_g=\Sigma_g/\Sigma.
\]

The right-hand side does not depend on \(\mathcal{C}_N\) or on \(R_f\). Shifting \(\mathcal{C}_N\) off zero leaves it unchanged. Solving \(R_f\) makes the total momentum zero to \(\sim 10^{-15}\) and does not remove it.

## 3. Numbers

| | NumPy | Wolfram |
|---|---|---|
| Pure HR, max \(\|P-\mathcal{C}(Dn)\|\) | 0 | 0 |
| Pure HR, min \(\|P\|\) at \(\mathcal{C}\neq 0\) | 0.060 | 0.068 |
| Matter, median \(\|P\|\) on \(\mathcal{C}_N=0\) | **0.922** | **0.891** |
| Fraction \(>10^{-3}\) | 200/200 | 200/200 |
| Same, \(b=0\) (current \(J\) only) | 0.651 | 0.723 |
| \(\Sigma_f=0\), max residual | \(2.0\times 10^{-15}\) | \(2.5\times 10^{-15}\) |
| K5 swap, median | 0.726 | 0.775 |
| \(\Sigma_g=\Sigma_f\), median (report only) | 0.786 | 1.104 |
| \(\theta_g\) at \(\Sigma_g=\Sigma_f\) | 1/2 | 1/2 |

At \(\Sigma_g=\Sigma_f\) the residual is not zero. \(w_{\mathrm{br}}/w_g=\theta_g=1/2\). The figure \(1/4\) is \(w_{\mathrm{br}}/\Sigma\), the retired comparison. Minimum \(\|P\|\) on the matter surface is 0.080 (NumPy), so the median is not one large outlier.

## 4. Scope

- Minimal model \(\beta_2=\beta_3=0\), \(\beta_1=1\), generic \(n\neq 0\). Same scope as the passing K0′.
- \(b\) is an independent covector with the same weights as \(J\). The \(J\)-only column is already nonzero, so this \(b\) is not the source of the residual. The monomials \(\omega^{ab}\gamma_{ab}\) are not written out.
- \(\Sigma_g\) and \(\Sigma_f\) are drawn as kinetic weights, independent of the random metric.
- Shift factorization (de Rham–Heisenberg–Ribeiro 1409.3834) is assumed, not re-tested. If the shift redefinition fails, the mechanism is the 2014 one and this \(P-\mathcal{C}_N(Dn)\) test is the wrong object.
- (B), \(\varphi=\Sigma^{1/2}\psi\), was not rerun. Jammer’s point stands: weak vanishing is canonical-invariant, and the earlier script did not perform the transformation.

## 5. Fork

| | |
|---|---|
| Pure HR in this engine | passes |
| \(\Sigma_f=0\) | passes |
| Matter on the solved \(n\) equation | **not** \(P=\mathcal{C}_N(Dn)\) |
| **Lane** | **G-2 (5.5-mode)** |
| Ratification | no. AC rules. |
| \(\mathcal{S}\)-block | closed |

— Cursor Main, 2026-10-21.
