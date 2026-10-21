# PRE-REGISTRATION — derive the χ weight, do not insert it

**Filed before the run.**  
**Directive:** `Handoffs\Directive_AC_to_Jammer_Scratch_K0prime_Matter_Lane_G2_Controls_Real_But_Weight_Still_Posited_20261022.md` §4, run here as a cross-check.  
**Engines:** NumPy (Dirac matrix), SymPy (shift polynomials), Wolfram Engine 15 (same matrix). No Core. Posteriors held.

The K0′ matter run is conditional on \(w_{\mathrm{br}}=\Sigma_g^2/\Sigma\). This run computes that coefficient. It does not project onto a constraint and it does not insert the factor.

## Lagrangian being bracketed

One real pair \((u,v)\) on a periodic lattice, the orbital piece of a first-order kinetic term:

\[
L=(\Sigma_g+\Sigma_f)\,u\,\dot v-\Sigma_g N_g\,u\,Dv-\Sigma_f N_f\,u\,Dv.
\]

Primary constraints from the velocities, both vierbein legs in one \(\chi\):

\[
\chi^u=p_u,\qquad \chi^v=p_v-(\Sigma_g+\Sigma_f)\,u.
\]

\(E_i=\Sigma_g\,u_i\bigl((Dv)_i+\omega_i v_i\bigr)\). \(\omega\) is an ultralocal background (the spin-connection slot). The bracket is the matrix formula

\[
\{E_i,E_j\}_D=\{E_i,E_j\}-\{E_i,\chi_a\}(C^{-1})^{ab}\{\chi_b,E_j\},
\]

with \(C_{ab}=\{\chi_a,\chi_b\}\) built from the Poisson tensor, not typed in as \(1/\Sigma\).

## Decision

Let \(\alpha\) be the least-squares factor \(\{E,E\}_D=\alpha\,\{E,E\}_D\big|_{\Sigma_g=\Sigma=1}\) on the same \((u,v,\omega)\).

- **Weight derived as \(\Sigma_g^2/\Sigma\)** if, for \(\Sigma_f>0\), \(|\alpha\,\Sigma/\Sigma_g^2-1|<10^{-8}\), and the same \(\alpha\) is separated from \(\Sigma_g\), from \(\Sigma\), and from \(\Sigma_g/\Sigma\) by more than \(10^{-3}\). \(\Sigma_f=0\) must give \(\alpha=\Sigma_g\). K5 (the \(f\)-frame energy, weight \(\Sigma_f\)) must give \(\Sigma_f^2/\Sigma\).
- **Wrong object** if \(\alpha\) matches a different closed form. Then the K0′ matter run tested the wrong weight.
- **G-4 on this check** if \(C\) is singular or the engines disagree.

Shift factorization, same substitution the K0′ lane used, \(N_g^i=L^i+L n^i+N(Dn)^i\), \(n\) and \(Dn\) independent of the multipliers:

- Dirac matter linear in \((N,L,L^i)\) and a quadratic scalar kinetic term nonlinear, on that same substitution → factorization holds for this kinetic term, and the \(P-\mathcal{C}_N(Dn)\) test is the right object.
- Dirac matter nonlinear → dRHR mechanism, and that test is the wrong object.

\(\omega\) may add a bilinear. It must not change \(\alpha\).

Posteriors stay G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

— Cursor Main, 2026-10-22.
