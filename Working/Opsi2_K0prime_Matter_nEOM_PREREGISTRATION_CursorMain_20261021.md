# PRE-REGISTRATION — K0′ engine with matter, n-equation solved

**Filed before the run.**  
**Asked by:** Jammer, `Handoffs\Handoff_Claude_Jammer_to_AC_Greg_Cursor_Scratch_Terminal_G2_Not_Ratifiable_…_20261021.md` §7.  
**Engine reused:** `Working\Opsi2_Steps123_K0_PARALLEL_CursorMain.py` (minimal \(\beta_2=\beta_3=0\), \(\beta_1=1\)).  
**Engines:** NumPy and Wolfram Engine 15. No Core. Posteriors held.

The (A)+(B) terminal filing is withdrawn before this run. Its “K1” control is `project(v,[v])`. \(\Sigma_f\) is drawn from \((0.3,2)\) and is never zero. That script does not solve an \(n\) equation.

---

## What is computed

Hassan–Rosen’s off-shell identity in this minimal model, already checked as K0′:

\[
P_{\mathrm{grav}}= \mathcal{C}_{\mathrm{grav}}\,(Dn)+\gamma^{-1}(R-U),\qquad U=2m^2\sqrt{\gamma}\,\beta_1(fn)/\sqrt{x}.
\]

On the vacuum \(n\) equation \(R=U\), this is \(P=\mathcal{C}\,(Dn)\).

Matter is added in the three slots Jammer named. \(J\) and \(b\) are independent covectors. \(\mathrm{cur}=J+b\). Scalars \(\Sigma_g,\Sigma_f>0\), \(\Sigma=\Sigma_g+\Sigma_f\), drawn independently of the random metric (they are kinetic weights, not \(\sqrt{\gamma}\)).

| Slot | Weight | Where it enters |
|---|---|---|
| Dirac-bracket current | \(w_{\mathrm{br}}=\Sigma_g^2/\Sigma\) | added to \(P\), on \(\gamma^{-1}\mathrm{cur}\) |
| g-shift / \(n\) equation | \(w_g=\Sigma_g\) | \(R+w_g\,\mathrm{cur}-U=0\), and the \((Dn)\cdot\mathrm{cur}\) term in \(\mathcal{C}_N\) |
| total momentum | \(w_{\mathrm{tot}}=\Sigma\) | solved by an f-momentum \(R_f=-R-w_{\mathrm{tot}}\mathrm{cur}\). \(R_f\) is not in \(P\) or \(\mathcal{C}_N\) |

Ordinary closure (the control) is the unique completion that (i) reduces to the vacuum identity when \(J=b=E_g=0\) and (ii) gives \(P=\mathcal{C}_N(Dn)\) whenever \(w_{\mathrm{br}}=w_g\):

\[
P=P_{\mathrm{grav}}+(E_g+w_g\,Dn\cdot\mathrm{cur})\,Dn+w_{\mathrm{br}}\,\gamma^{-1}\mathrm{cur}.
\]

The \(\chi\) change is only \(w_g\to w_{\mathrm{br}}\) on that current. No other term is retuned.

Algebraic consequence, to be checked rather than inserted as the result:

\[
P-\mathcal{C}_N(Dn)=(w_{\mathrm{br}}-w_g)\,\gamma^{-1}\mathrm{cur}=\Sigma_g(\theta_g-1)\,\gamma^{-1}\mathrm{cur},
\]

with \(\theta_g=\Sigma_g/\Sigma\). This vector is independent of \(\mathcal{C}_N\) and of \(R_f\). It is zero for every current iff \(\Sigma_f=0\).

\(E_g\) is a random scalar inside \(\mathcal{C}_N\). It must drop out of the residual once the completion above is included. If the residual depends on \(E_g\), the run is G-4 (broken model), not a fork.

This is not a \(\gamma\)-matrix expansion of \(\omega^{ab}\gamma_{ab}\). \(b\) is an independent covector with the same weights as \(J\).

## Controls, same code path

1. **Pure HR.** \(J=b=E_g=0\). \(\|P-\mathcal{C}(Dn)\|<10^{-8}\) on the \(n\) equation, and \(\|P\|\) stays \(>10^{-3}\) when \(\mathcal{C}\neq 0\). Fail this → stop.
2. **\(\Sigma_f=0\).** Exact. Max residual \(<10^{-8}\).
3. **K5.** Swap \(\Sigma_g\leftrightarrow\Sigma_f\). Same code. Weights become \(w_g=\Sigma_f\), \(w_{\mathrm{br}}=\Sigma_f^2/\Sigma\).
4. **\(e=f\) report only.** \(\Sigma_g=\Sigma_f\), so \(\theta_g=1/2\) and \(w_{\mathrm{br}}/w_g=\theta_g=1/2\). The retired comparison of \(w_{\mathrm{br}}\) against \(\Sigma\) is \(1/4\). Neither is required to vanish. Not called K1.
5. **\(R_f\).** Total momentum is satisfied by solving \(R_f\). The residual must be unchanged by that substitution.

## Decision (fixed here)

On the surface \(\mathcal{C}_N=0\), \(n\) equation solved, total momentum solved by \(R_f\), generic \(n\neq 0\):

- **G-2 (5.5-mode), lane result, not a ratification,** if pure HR passes, \(\Sigma_f=0\) passes, the analytic residual matches to \(10^{-6}\), and the matter median \(\|P\|\) and the K5 median are both \(>10^{-3}\) with fraction \(>10^{-3}\) at least \(0.95\), in both engines.
- **M-a,** if pure HR passes and the matter median residual is \(<10^{-8}\). The \(\mathcal{S}\)-block may then be opened by AC. This lane does not open it.
- **G-4,** if pure HR fails, \(\Sigma_f=0\) fails, the analytic identity fails, or the engines disagree.

Posteriors stay G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Cursor Main, 2026-10-21.
