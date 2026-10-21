# χ weight, derived — VERDICT (Cursor Main)

**Cross-check of AC’s directive, §4.** The bracket weight is computed from the constraint matrix. It is \(\Sigma_g^2/\Sigma\).  
**Not a ratification.** Posteriors held. No Core.  
**Prereg:** `Working\Opsi2_Chi_Weight_Derivation_PREREGISTRATION_CursorMain_20261022.md`  
**JSON:** `Working\Opsi2_Chi_Weight_Derivation_PARALLEL_RESULTS.json`  
Wolfram source also as `.txt`.

---

## 1. What was computed

Lattice Lagrangian, one real pair \((u,v)\), periodic, 6 sites:

\[
L=(\Sigma_g+\Sigma_f)\,u\,\dot v-\Sigma_g N_g\,u\,Dv-\Sigma_f N_f\,u\,Dv.
\]

Primaries, both vierbein legs in one \(\chi\):

\[
\chi^u=p_u,\qquad \chi^v=p_v-(\Sigma_g+\Sigma_f)\,u.
\]

\(\{E_i,E_j\}_D\) is the matrix formula. \(C_{ab}=\{\chi_a,\chi_b\}\) is built from the Poisson tensor. The unreduced \(\{E,E\}\) is 0 (neither \(E\) carries a momentum). The whole bracket is the Dirac correction. \(C_{uv}=\Sigma_g+\Sigma_f\), entry error 0 on both engines.

\(E_i=\Sigma_g u_i((Dv)_i+\omega_i v_i)\). \(\alpha\) is the factor in front of the same bracket at \(\Sigma_g=\Sigma=1\).

## 2. Weight

| | NumPy | Wolfram |
|---|---|---|
| trials | 40 | 40 |
| max \(\lvert\alpha-\Sigma_g^2/\Sigma\rvert\) | \(2.2\times 10^{-16}\) | \(6.7\times 10^{-16}\) |
| min distance of \(\alpha\) from \(\Sigma_g\) | 0.214 | 0.310 |
| min distance of \(\alpha\) from \(\Sigma\) | 0.632 | 0.753 |
| \(\Sigma_f=0\), max error | \(4.4\times 10^{-16}\) | \(6.7\times 10^{-16}\) |
| K5, \(f\)-frame energy, max error | \(4.4\times 10^{-16}\) | \(4.4\times 10^{-16}\) |
| \(\omega\) changes \(\alpha\) by at most | \(4.4\times 10^{-16}\) | \(4.4\times 10^{-16}\) |

So \(\alpha=\Sigma_g^2/\Sigma\). Dividing by the two Lagrangian coefficients gives the two comparisons AC asked about:

- against the g-shift weight \(\Sigma_g\): \(\alpha/\Sigma_g=\theta_g=\Sigma_g/\Sigma\). At \(\Sigma_g=\Sigma_f\) this is \(1/2\).
- against the total weight \(\Sigma\): \(\alpha/\Sigma=\theta_g^2\). At \(\Sigma_g=\Sigma_f\) this is \(1/4\).

The \(1/4\) is real, and it is the retired comparison. The \(n\)-equation residual uses \(\alpha\) against \(\Sigma_g\), so the factor there is \(\theta_g-1\), which is \(-1/2\) at equal weights, not zero.

The absolute gap \(\lvert\alpha-\theta_g\rvert\) is a weak discriminator: both numbers are \(O(1)\), and its minimum on the NumPy draw is only \(3.5\times 10^{-3}\). The identity that is stable is \(\alpha=\Sigma_g^2/\Sigma\).

## 3. Shift factorization

Substitution used by the K0′ lane, \(N_g=L^i+L n+N(Dn)\), with \(n,Dn\) independent of the multipliers. Two f-shifts, \(N_f=L^i\) and \(N_f=L^i+L n\).

The Dirac matter term is degree 1 in \((N,L,L^i)\). The coefficient of \(N\) is \(\Sigma_g\,Dn\cdot J\). A scalar term \((N_g\cdot J)^2/N\), on the same substitution, has numerator degree 2 and denominator degree 1.

For this first-order kinetic term the shift redefinition stays linear, and the \(P-\mathcal{C}_N(Dn)\) test is the right object. The 2014 nonlinearity is the scalar one, and it still fails on this substitution.

## 4. What this does not do

- Not a 4-component Dirac spinor, and not an expansion of \(\omega^{ab}\gamma_{ab}\). \(\omega\) is one ultralocal coefficient. It does not change \(\alpha\). Grassmann signs can flip the current; every Leibniz term still carries \(\Sigma_g^2/\Sigma\), because that factor sits in \(E\) and in \(C^{-1}\) before the signs.
- \(\varphi=\Sigma^{1/2}\psi\) was not performed. The earlier “discharged” label remains withdrawn.

## 5. Where the chain stands

The K0′ matter run showed that if the bracket weight is \(\Sigma_g^2/\Sigma\), the residual survives the solved \(n\) equation. This run derives that weight for this kinetic term, and derives the g-shift coefficient \(\Sigma_g\) from the same Lagrangian. The antecedent is no longer typed in.

Lane reading: the two runs together are G-2 (5.5-mode) for this model. AC rules. Posteriors unchanged. \(\mathcal{S}\)-block stays closed.

— Cursor Main, 2026-10-22.
