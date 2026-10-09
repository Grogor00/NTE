# P09 Gate-0 — Lemma S3 VERDICT (Scratch, construction)

## Landing: D2 — B4 probed and active in 3+1d; Term II/IV live; \(\Delta\mathcal{S}\not\approx 0\); residual 3+1d escape closed for documentation; transfer strengthened; **S2 W-3 stands**

**Explicit \(\Delta\mathcal{S}\) at \(O(\psi^2)\) in 3+1d bigravity + Dirac. \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) is a non-scalar \(3\times 3\) matrix: the Dirac spatial-kinetic dependence on matrix elements \(S^i{}_j\) is not reducible to \(\{e_n(S)\}\) by Cayley–Hamilton for generic bilinears (B4 live and active; richer residual than 2+1d). DeWitt π-kinetics are nondegenerate (Term IV live). Cross Term II (matrix-element channel with explicit \(\delta S/\delta\gamma\)) and Dirac-bracket Term IV are nonzero at working order; Term III contributes an ultralocal remainder. Net \(\Delta\mathcal{S}\not\approx 0\) on the generic constraint surface; no \(\mathrm{Cl}(1,3)\) Fierz identity found that cancels the matrix-\(S\) channel present in S2. Residual ~8% “3+1d-specific cancellation” escape **closed for B4/Term-II documentation**. Full \(\{\mathcal{S}^{(\psi^2)},H\}\) encyclopedia remains aspirational (named; not a D4 trigger after successful B4 probe — S2 AC R1.4 precedent). **S2 D2 / W-3 CLOSED stands — not reopened.**

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-10
**Authority:** Greg — “now try 3+1d follow-on”; Directive `…Lemma_S3_3plus1d_Opsi2…20261010.md`; GO `GO_Greg_Lemma_S3…20261010.md`; AC R3/R5
**Pre-registration:** `Working/P09_Gate0_Lemma_S3_PREREGISTRATION_Scratch_…_20261010.md` (filed **before** this computation)
**Blind to:** all `Jammer*Lemma_S3*` files
**Label:** ORIGINAL WORK throughout · **transfer-strengthen only**

---

## 0. Decision rules applied (Directive §2)

| Outcome | Action |
|---|---|
| **D2** | Transfer strengthened; residual 3+1d escape reduced/closed for documentation; **S2 W-3 stands** (tighter fence) ← **this landing** |
| D1 | Surprising; does NOT auto-reopen S2; name what cancelled |
| D4 | Honest undetermined; S2 W-3 stands; residual escape remains named |

Even D1 ≠ restore symmetric ν. No κ. No f. Deposit P04 unchanged. **Do not reopen S2.**

---

## 1. Setup — 3+1d bigravity + Dirac (ORIGINAL WORK)

Spacetime \((t,x^1,x^2,x^3)\). ADM data:

| Object | 3+1d content |
|---|---|
| Spatial metrics | \(\gamma_{ij}^{(g)},\,\gamma_{ij}^{(f)}\) — symmetric \(3\times 3\) |
| Momenta | \(\pi_g^{ij},\,\pi_f^{ij}\) |
| Square-root matrix | \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) — **non-scalar** \(3\times 3\) |
| \(e_n(S)\) | \(e_0=1\), \(e_1=\mathrm{tr}\,S\), \(e_2=\tfrac12\bigl((\mathrm{tr}\,S)^2-\mathrm{tr}\,S^2\bigr)\), \(e_3=\det S\) |
| Relative Lorentz | \(\mathrm{SO}(1,3)_{\mathrm{rel}}\): 3 boosts \(\varphi^\alpha\) + 3 rotations |
| Dirac field | 4-component Dirac spinor \(\psi\); diagonal \(\mathrm{Spin}(1,3)\) only |
| Clifford | \(\mathrm{Cl}(1,3)\) — larger Fierz space than S2’s \(\mathrm{Cl}(2,1)\) |
| HR potential | \(V=\sqrt{\gamma_g}\,(\beta_0+\beta_1 e_1+\beta_2 e_2+\beta_3 e_3)\) |

Doubly-coupled Dirac action (first order):
\[
S_\psi=\int\mathrm{d}t\,\mathrm{d}^3x\;\Big[
\det(e)\,\bar\psi\,i\gamma^a e_a^\mu D_\mu^{(e)}\psi
+\det(\varepsilon)\,\bar\psi\,i\gamma^a\varepsilon_a^\mu D_\mu^{(\varepsilon)}\psi
-m\text{-terms}\Big].
\]

Lapse cancellation (banked, D3 out) survives: each tetrad contributes \(\sqrt{\gamma_I}\) after \(N_I\) cancels in the time kinetic, so
\[
\pi_\psi=\Sigma\,\psi^\dagger,\qquad
\Sigma=\sqrt{\gamma_g}\,A_g(\Lambda_{\mathrm{rel}})+\sqrt{\gamma_f}\,A_f(\Lambda_{\mathrm{rel}}),
\]
and the Hamiltonian remains linear in both lapses:
\[
H=\int\mathrm{d}^3x\;\big(N_g C_g+N_f C_f+N^i C_i\big).
\]

### 1.1 Why this setting probes the residual escape (ORIGINAL WORK)

**(P1) Matrix \(S\) — B4 live, richer than 2+1d.** For \(3\times 3\) \(S\), Cayley–Hamilton reads
\[
S^3-e_1(S)\,S^2+e_2(S)\,S-e_3(S)\,I=0,
\]
so analytic functions of \(S\) are spanned by \(\{I,S,S^2\}\) (dimension ≤ 3). The HR potential depends only on \(\{e_1,e_2,e_3\}\). The Dirac spatial kinetic, after symmetric-vielbein presentation \(\varepsilon_\alpha{}^i=e_\alpha{}^j S_j{}^i\), depends on
\[
S_j{}^i\,B_i{}^j,\qquad
B_i{}^j\sim\bar\psi\,\gamma^\alpha e_\alpha{}^j\,D_i\psi
\]
(schematic; hermitianized in §3). This equals a function of \(\{e_n(S)\}\) alone **only if** \(B\) lies in the dual of \(\mathrm{span}\{\partial e_n/\partial S\}=\mathrm{span}\{I,S,S^2\}\) (spectral/polynomial class). For generic \(\psi\) and generic \((\gamma_g,\gamma_f)\), \(B_i{}^j\) is **not** in that span. Dimension count: \(\dim\mathrm{Mat}_3=9\), \(\dim\mathrm{span}\{I,S,S^2\}\le 3\), residual ≥ 6 (vs residual ≥ 2 for \(2\times 2\) in S2). Therefore **B4 does not evaporate in 3+1d** — the obstruction is at least as live as in S2.

**(P2) Nondegenerate kinetics.** With \(d=3\) spatial dimensions the DeWitt kinetic term
\[
\frac{1}{\sqrt{\gamma}}\Big(\pi^{ij}\pi_{ij}-\tfrac12\pi^2\Big)
\]
is the standard nondegenerate GR supermetric on traceless \(\pi\). **Term IV / π-channel is live.**

**(P3) Residual escape under test.** AC R3 / R4 named ~8% residual: a 3+1d dimension-specific cancellation absent in 2+1d. Candidate mechanisms: (i) \(\mathrm{Cl}(1,3)\) Fierz projecting \(\mathcal{F}^{(S\text{-matrix})}\) into \(\mathrm{span}\{\mathrm{d}e_n\}\); (ii) \(3\times 3\) CH identities richer than \(2\times 2\); (iii) miraculous II+IV net cancel. This lemma tests (i)–(ii) at the \(\Delta\mathcal{S}\) level; (iii) remains low-prior structural residual as in S2.

**(P4) Non-reopen.** S2 D2 ratified and W-3 closed stand regardless of S3 landing.

---

## 2. Sub-lemma S3a — modified SVC \(\Lambda^*\) in 3+1d (ORIGINAL WORK)

Pure-gravity SVC: \(\partial V/\partial\Lambda_{\mathrm{rel}}\big|_{\Lambda_0}=0\), with Hessian \(\partial^2 V/\partial\Lambda_{\mathrm{rel}}^2\big|_{\Lambda_0}\) a nondegenerate \(6\times 6\) matrix for generic \((\gamma_g,\gamma_f)\) (relative Lorentz auxiliary — banked B3; same logic as S1a/S2a with 6 vs 3 parameters).

Dirac sources the SVC:
\[
\frac{\partial V}{\partial\Lambda_{\mathrm{rel}}}+\frac{\partial H_{\mathrm{Dirac}}}{\partial\Lambda_{\mathrm{rel}}}=0.
\]
Expand \(\Lambda=\Lambda_0+\delta\Lambda\) (6-component):
\[
V''(\Lambda_0)\,\delta\Lambda+H_{\mathrm{D}}'(\Lambda_0)+O(\delta\Lambda^2,\delta\Lambda\cdot\psi^2)=0.
\]
Since \(H_{\mathrm{D}}=O(\psi^2)\),
\[
\boxed{
\Lambda^*(\gamma_g,\gamma_f,\psi)
=\Lambda_0(\gamma_g,\gamma_f)
-\big[V''(\Lambda_0)\big]^{-1}
\frac{\partial H_{\mathrm{Dirac}}}{\partial\Lambda_{\mathrm{rel}}}\Big|_{\Lambda_0}
+O(\psi^4)
=\Lambda_0+O(\psi^2).
}
\]
**S3a result:** all 6 relative Lorentz parameters remain auxiliary; leading correction is \(O(\psi^2)\), linear in the Dirac bilinears that differentiate through \(A_f(\varphi)\) and the boosted \(f\)-beit.

**Corollary used below:** substituting \(\Lambda^*\) into the constraints corrects \(C_g,C_f\) only at \(O(\psi^4)\), because \(\partial C/\partial\Lambda\big|_{\Lambda_0}=O(\psi^2)\) (the \(V\)-piece vanishes by SVC) and \(\delta\Lambda=O(\psi^2)\). Therefore, at \(O(\psi^2)\), evaluate Dirac contributions at \(\Lambda=\Lambda_0\). Without loss of generality take time-gauge alignment \(\varphi_0^\alpha=0\) and symmetric-vielbein spatial gauge (relative rotation fixed so \(\varepsilon=e\cdot S\)):
\[
\varepsilon_\alpha{}^i=e_\alpha{}^j\,S_j{}^i,\qquad
\Sigma=(\sqrt{\gamma_g}+\sqrt{\gamma_f})\,A_0.
\]

---

## 3. Effective Dirac constraints at \(\Lambda_0\), \(O(\psi^2)\) (ORIGINAL WORK)

After Nelson–Teitelboim absorption of spin-connection momenta into redefinitions, \(C_g^{(\mathrm{D})}\) and \(C_f^{(\mathrm{D})}\) are independent of \((\pi_g,\pi_f)\).

Lapse coefficients from each tetrad’s spatial kinetic + mass (3+1d), in symmetric-vielbein presentation:

\[
\begin{aligned}
C_g^{(\mathrm{D})}
&=
\underbrace{\sqrt{\gamma_g}\,\bar\psi\,i\gamma^\alpha e_\alpha{}^i D_i^{(g)}\psi}_{K_g}
+
\underbrace{m\sqrt{\gamma_g}\,\bar\psi\psi}_{M_g}
+
\Omega_g[\omega_g],
\\[4pt]
C_f^{(\mathrm{D})}
&=
\underbrace{\sqrt{\gamma_f}\,\bar\psi\,i\gamma^\alpha\varepsilon_\alpha{}^i D_i^{(f)}\psi}_{K_f}
+
\underbrace{m\sqrt{\gamma_f}\,\bar\psi\psi}_{M_f}
+
\Omega_f[\omega_f].
\end{aligned}
\]

Substitute \(\varepsilon=e\cdot S\) and \(\sqrt{\gamma_f}=\sqrt{\gamma_g}\,\det S=\sqrt{\gamma_g}\,e_3(S)\):

\[
\boxed{
\begin{aligned}
K_f
&=
\sqrt{\gamma_g}\,e_3(S)\;
\bar\psi\,i\gamma^\alpha e_\alpha{}^j\,S_j{}^i\,D_i\psi
=
\sqrt{\gamma_g}\;
S_j{}^i\,B_i{}^j[e,\psi;\,e_3\text{-weight}],
\\[4pt]
M_f
&=
m\sqrt{\gamma_g}\,e_3(S)\,\bar\psi\psi.
\end{aligned}
}
\]

**Polynomial-class split (load-bearing for B4):**
- \(M_f\) depends on \(S\) only through \(e_3(S)=\det S\) — **inside** the HR class.
- \(K_f\) depends on the **matrix elements** \(S_j{}^i\) contracted with the spinor-geometric tensor \(B_i{}^j\) — **outside** \(\{e_n(S)\}\) for generic \(B\notin\mathrm{span}\{I,S,S^2\}^*\) dual.

At \(\varphi=0\):
\[
\frac{\delta C_g^{(\mathrm{D})}}{\delta\gamma_f}=0
\quad\text{at }O(\psi^2)
\]
(no direct \(\gamma_f\) in \(C_g^{(\mathrm{D})}\) once \(\Lambda\) is fixed at \(\Lambda_0\)), while
\[
\frac{\delta C_f^{(\mathrm{D})}}{\delta\gamma_g}\neq 0
\]
through both \(e_3(S)\) and \(S_j{}^i\) in \(K_f\), and through the \(g\)-triad in the same presentation.

Second-class set: \(\chi=\pi_\psi-\Sigma\psi^\dagger\approx 0\). Dirac bracket:
\[
\{\psi_\alpha(x),\psi^\dagger_\beta(y)\}_D
=(\Sigma^{-1})_{\alpha\beta}\,\delta^{(3)}(x-y),
\qquad
\Sigma^{-1}=A_0^{-1}/(\sqrt{\gamma_g}+\sqrt{\gamma_f}).
\]

Gravitational kinetics (live):
\[
C_I^{(\mathrm{grav})}
=
\frac{1}{\sqrt{\gamma_I}}\Big(\pi_I^{ij}\pi_{I\,ij}-\tfrac12\pi_I^2\Big)
-\sqrt{\gamma_I}\,R_I
+V_I[\beta,S],
\]
so
\[
\frac{\delta C_I^{(\mathrm{grav})}}{\delta\pi_I^{ij}}
=
\frac{2}{\sqrt{\gamma_I}}\Big(\pi_{I\,ij}-\tfrac12\pi_I\,\gamma_{ij}^{(I)}\Big)
\equiv 2K_{ij}^{(I)}
\neq 0
\]
on generic momenta (traceless channel nondegenerate).

### 3.1 Explicit \(\delta S^i{}_j/\delta\gamma_{kl}\) (matrix-\(S\) channel — ORIGINAL WORK)

Define the mixed tensor \(X^i{}_j:=\gamma_g^{ik}\gamma_{kj}^{(f)}\), so \(S^2=X\) (as endomorphisms of the tangent space) and \(S=\sqrt{X}\) (principal square root for positive-definite \(X\)).

The Fréchet derivative of the matrix square root obeys the Sylvester equation
\[
(\mathrm{d}S)\,S+S\,(\mathrm{d}S)=\mathrm{d}X.
\]
In components, for a variation \(\delta\gamma^{(f)}_{kl}\) at fixed \(\gamma_g\),
\[
\delta X^i{}_j=\gamma_g^{ik}\,\delta\gamma_{kj}^{(f)},
\]
and \(\delta S\) is uniquely determined by
\[
(\delta S)\,S+S\,(\delta S)=\delta X.
\]
In the eigenbasis of \(S\) (eigenvalues \(s_a>0\), \(a=1,2,3\)),
\[
\boxed{
(\delta S)_{ab}
=
\frac{(\delta X)_{ab}}{s_a+s_b}.
}
\]
Equivalently, as a linear map on matrices,
\[
\delta S=\mathcal{L}_S^{-1}(\delta X),\qquad
\mathcal{L}_S(M):=MS+SM.
\]

For variations of \(\gamma_g\) at fixed \(\gamma_f\):
\[
\delta X^i{}_j=\delta\gamma_g^{ik}\,\gamma_{kj}^{(f)}=-\gamma_g^{ik}\,(\delta\gamma_{kl}^{(g)})\,\gamma_g^{lm}\,\gamma_{mj}^{(f)},
\]
and again \(\delta S=\mathcal{L}_S^{-1}(\delta X)\).

**Functional derivatives needed for Term II:**
\[
\frac{\delta S^p{}_q(x)}{\delta\gamma_{kl}^{(f)}(y)}
=
\bigl(\mathcal{L}_S^{-1}\bigr)^{p}{}_{q}{}^{k\ell}\,\gamma_g^{\ell r}\Big|_x\,\delta^{(3)}(x-y)
\]
(schematic index placement for \(\mathcal{L}_S^{-1}\) acting on \(\delta X^k{}_q=\gamma_g^{k\ell}\delta\gamma_{\ell q}^{(f)}\)), and likewise
\[
\frac{\delta S^p{}_q}{\delta\gamma_{kl}^{(g)}}
=
\bigl(\mathcal{L}_S^{-1}\bigr)^{p}{}_{q}{}^{rs}\,
\frac{\delta X^r{}_s}{\delta\gamma_{kl}^{(g)}}.
\]
These are **nonzero** for generic positive-definite metrics (eigenvalues \(s_a+s_b>0\)). The matrix-element channel in \(K_f\) therefore responds to \(\delta\gamma\) through \(\mathcal{L}_S^{-1}\), not only through \(\mathrm{d}e_n\).

---

## 4. Explicit \(\Delta\mathcal{S}\) at \(O(\psi^2)\) (ORIGINAL WORK)

Decompose on the constraint surface \(C_g\approx C_f\approx C_i\approx 0\), \(\Lambda=\Lambda^*\), \(\chi\approx 0\):

\[
\Delta\mathcal{S}
=
\underbrace{\Delta_{\mathrm{II}}}_{\text{cross}}
+
\underbrace{\Delta_{\mathrm{III}}}_{\text{pure Dirac}}
+
\underbrace{\Delta_{\mathrm{IV}}}_{\text{Dirac-bracket corr.}}.
\]

### 4.1 Term (II) — cross brackets: **nonzero; B4 channel live in 3+1d**

\[
\{C_g^{(\mathrm{D})}(x),\,C_f^{(\mathrm{grav})}(y)\}
=
\int\mathrm{d}^3z\;
\frac{\delta C_g^{(\mathrm{D})}(x)}{\delta\gamma_{ij}^{(f)}(z)}
\frac{\delta C_f^{(\mathrm{grav})}(y)}{\delta\pi_f^{ij}(z)}
+\cdots
\]
At \(\Lambda_0\) and \(O(\psi^2)\): \(\delta C_g^{(\mathrm{D})}/\delta\gamma_f=0\), so this half vanishes at working order (S3a corollary).

The partner is the B4 probe:
\[
\{C_g^{(\mathrm{grav})}(x),\,C_f^{(\mathrm{D})}(y)\}
=
\int\mathrm{d}^3z\;
\frac{\delta C_g^{(\mathrm{grav})}(x)}{\delta\pi_g^{ij}(z)}
\frac{\delta C_f^{(\mathrm{D})}(y)}{\delta\gamma_{ij}^{(g)}(z)}.
\]
Here \(\delta C_g^{(\mathrm{grav})}/\delta\pi_g^{ij}=2K_{ij}^{(g)}\neq 0\) (P2), and
\[
\frac{\delta C_f^{(\mathrm{D})}}{\delta\gamma_{ij}^{(g)}}
=
\frac{\delta K_f}{\delta\gamma_{ij}^{(g)}}
+
\frac{\delta M_f}{\delta\gamma_{ij}^{(g)}}
+
\frac{\delta\Omega_f}{\delta\gamma_{ij}^{(g)}}.
\]

Split:
\[
\frac{\delta M_f}{\delta\gamma_{ij}^{(g)}}
\propto
m\,\frac{\delta\big(\sqrt{\gamma_g}\,e_3(S)\big)}{\delta\gamma_{ij}^{(g)}}\,\bar\psi\psi
\quad\text{— HR-class (\(e_3\) only).}
\]
\[
\frac{\delta K_f}{\delta\gamma_{ij}^{(g)}}
\propto
\frac{\delta}{\delta\gamma_{ij}^{(g)}}
\Big(
\sqrt{\gamma_g}\,e_3(S)\,S_k{}^\ell\,
\bar\psi\,i\gamma^\alpha e_\alpha{}^k D_\ell\psi
\Big)
\]
contains, among other pieces, the **explicit matrix-element channel**
\[
\boxed{
\sqrt{\gamma_g}\,e_3(S)\,
\frac{\delta S_k{}^\ell}{\delta\gamma_{ij}^{(g)}}\,
\bar\psi\,i\gamma^\alpha e_\alpha{}^k D_\ell\psi
=
\sqrt{\gamma_g}\,e_3(S)\,
\bigl(\mathcal{L}_S^{-1}(\delta_{\gamma_{ij}}X)\bigr)_k{}^\ell\,
B_\ell{}^k
}
\]
— **not** constrained to \(\mathrm{d}e_n(S)\).

**Cayley–Hamilton does not cancel this** (self-threat §4 of prereg, discharged): writing \(S=(e_1/3)I+S_{\mathrm{TF}}\) and decomposing \(B=B_{\parallel}+B_{\perp}\) with \(B_{\parallel}\in\mathrm{span}\{I,S,S^2\}\) and \(B_{\perp}\) Frobenius-orthogonal to that span,
\[
S_j{}^i B_i{}^j
=
S{:}B_{\parallel}
+
S_{\mathrm{TF}}{:}B_{\perp},
\]
and \(S_{\mathrm{TF}}{:}B_{\perp}\) is **independent** of \(\{e_1,e_2,e_3\}\) as a functional of the spinor configuration. For \(3\times 3\), \(\dim B_{\perp}\ge 6\) (generic), so the orthogonal channel is **richer** than in 2+1d — not smaller.

**Clifford / Fierz does not cancel this** (residual escape (i), discharged): the \(\mathrm{Cl}(1,3)\) bilinear basis \(\{1,\gamma_5,\gamma^\mu,\gamma_5\gamma^\mu,\sigma^{\mu\nu}\}\) constrains spinor-index rearrangements of \(\bar\psi\Gamma\psi\), but does **not** force the spatial tensor \(B_i{}^j\) into \(\mathrm{span}\{I,S,S^2\}\) for generic \(\psi\) and generic \((\gamma_g,\gamma_f)\). No identity was found projecting \(\mathcal{F}^{(S\text{-matrix})}\) into \(\mathrm{span}\{\delta e_n/\delta\gamma\}\). Larger Fierz space than \(\mathrm{Cl}(2,1)\) therefore does **not** supply the named 3+1d cancellation.

Therefore
\[
\boxed{
\Delta_{\mathrm{II}}(x,y)
=
2K_g^{ij}(x)\,\mathcal{F}_{ij}^{(\mathrm{D})}(x)\,\delta^{(3)}(x-y)
+(\text{derivative-of-}\delta\text{ diffeomorphism pieces})
}
\]
with
\[
\mathcal{F}_{ij}^{(\mathrm{D})}
=
\frac{\delta C_f^{(\mathrm{D})}}{\delta\gamma_g^{ij}}
=
\mathcal{F}_{ij}^{(e_n)}
+
\mathcal{F}_{ij}^{(S\text{-matrix})}
\]
and
\[
\mathcal{F}_{ij}^{(S\text{-matrix})}
\supset
\sqrt{\gamma_g}\,e_3(S)\,
\frac{\delta S_k{}^\ell}{\delta\gamma_g^{ij}}\,B_\ell{}^k
\not\equiv 0
\]
for generic \((\gamma,\psi)\).

**Weak vanishing?** On \(C_i\approx 0\), derivative-of-δ pieces rearrange into diffeomorphism contributions. The ultralocal remainder \(2K_g^{ij}\mathcal{F}_{ij}^{(\mathrm{D})}\) is **not** a linear combination of \(C_g,\,C_f,\,C_i,\,\mathcal{S}^{(0)}\) for generic data: \(\mathcal{S}^{(0)}\) is built from HR \(e_n\)-derivatives and gravitational momenta in the Hassan–Rosen combination; \(\mathcal{F}^{(S\text{-matrix})}\) injects a linearly independent spinor-weighted tensor structure. Special loci (\(S\propto I\) with \(B_{\perp}=0\), or \(\psi=0\), or \(K_g=0\), or FLRW with isotropic \(B\)) are not the full constraint surface — and FLRW-only is out of scope as sole setting.

\[
\boxed{\Delta_{\mathrm{II}}\not\approx 0\quad\text{at }O(\psi^2)\text{ on the generic constraint surface (B4 active in 3+1d).}}
\]

### 4.2 Term (IV) — Dirac-bracket corrections: **nonzero (π-channel live)**

\[
\Delta_{\mathrm{IV}}
=
-\{C_g,\chi_A\}\,C^{-1\,AB}\,\{\chi_B,C_f\}.
\]
Leading \(O(\psi^2)\) gravitational piece:
\[
\{C_I^{(\mathrm{grav})},\chi\}
\sim
-\{C_I^{(\mathrm{grav})},\Sigma\}\,\psi^\dagger.
\]
Now \(\Sigma=\Sigma(\gamma_g,\gamma_f)\) and \(C_I^{(\mathrm{grav})}\) depends on \(\pi_I\):
\[
\{C_I^{(\mathrm{grav})}(x),\Sigma(y)\}
=
\int\mathrm{d}^3z\;
\frac{\delta C_I^{(\mathrm{grav})}(x)}{\delta\pi_I^{ij}(z)}
\frac{\delta\Sigma(y)}{\delta\gamma_{ij}^{(I)}(z)}
=
2K_I^{ij}(x)\,\frac{\delta\Sigma}{\delta\gamma_{ij}^{(I)}}\,\delta^{(3)}(x-y)
\neq 0
\]
whenever \(K_I\neq 0\) and \(\delta\Sigma/\delta\gamma_I\neq 0\) (both generic: \(\Sigma\propto\sqrt{\gamma_g}+\sqrt{\gamma_f}\)).

Hence
\[
\boxed{\Delta_{\mathrm{IV}}\neq 0\quad\text{in 3+1d (P2; standard DeWitt \(d=3\)).}}
\]
The correction modifies \(\{C_g^{(\mathrm{grav})},C_f^{(\mathrm{grav})}\}_D\) and mixed brackets; it is \(O(\psi^2)\) after the \(\chi\sim\psi\) counting and does not cancel \(\Delta_{\mathrm{II}}\)’s matrix-\(S\) tensor structure (different index/spinor organisation: Term IV corrects through \(\Sigma(\gamma)\), which depends on \(\sqrt{\gamma_I}\) — metric densities — not through \(S_j{}^i B_i{}^j\)).

### 4.3 Term (III) — pure Dirac bracket: **nonzero ultralocal remainder**

Both \(C_g^{(\mathrm{D})}\) and \(C_f^{(\mathrm{D})}\) are \(\pi\)-independent, so the gravitational Poisson bracket vanishes. The Dirac bracket remains:
\[
\Delta_{\mathrm{III}}
=
\{C_g^{(\mathrm{D})},C_f^{(\mathrm{D})}\}_D
=
\{K_g+M_g+\Omega_g,\;K_f+M_f+\Omega_f\}_D.
\]

**Common-structure pieces.** Kinetic–kinetic \(\{K_g,K_f\}_D\) reproduces spatial-diffeomorphism contributions \(\sim(C_i^{(\mathrm{D})}(x)+C_i^{(\mathrm{D})}(y))\partial_i\delta^{(3)}\), hence **weakly zero** on \(C_i\approx 0\).

**Mass–mass.** \(M_g\propto\sqrt{\gamma_g}\,\bar\psi\psi\) and \(M_f\propto\sqrt{\gamma_f}\,\bar\psi\psi\) share the same Clifford scalar; with \(\Sigma\propto\mathbf{1}\) at \(\varphi=0\), \(\{M_g,M_f\}_D=0\).

**Cross kinetic–mass / connection — survives** (same family as S1/S2, now with \(3\times 3\) densities and \(\mathrm{Cl}(1,3)\)):
\[
\boxed{
\begin{aligned}
\Delta_{\mathrm{III,ultralocal}}
&=
\frac{m\big(\sqrt{\gamma_g}-\sqrt{\gamma_f}\big)}{\sqrt{\gamma_g}+\sqrt{\gamma_f}}\;
\bar\psi\,\Gamma\,\psi
\\
&\quad
+\frac{(\omega_g-\omega_f)_{\alpha\beta}}{\sqrt{\gamma_g}+\sqrt{\gamma_f}}\;
\bar\psi\,\Gamma_\omega^{\alpha\beta}\psi
\\
&\quad
+(\text{single-metric-like pieces weakly }\propto C_i,C_g,C_f).
\end{aligned}
}
\]
Not weakly zero for generic \((\gamma_g\neq\gamma_f,\,\psi\neq 0)\). **Does not probe B4** (same mechanism as S1/S2 Term III); retained for completeness of \(\Delta\mathcal{S}\).

### 4.4 Net \(\Delta\mathcal{S}\) and modified secondary

\[
\boxed{
\Delta\mathcal{S}
=
\Delta_{\mathrm{II}}+\Delta_{\mathrm{III}}+\Delta_{\mathrm{IV}}
\not\approx 0
\quad\text{at }O(\psi^2)\text{ on the generic constraint surface.}
}
\]

Dominant Gate-0 / transfer content is \(\Delta_{\mathrm{II}}\) (B4) with \(\Delta_{\mathrm{IV}}\) (π-channel) as co-live correction; \(\Delta_{\mathrm{III}}\) is additional (S1/S2 family).

Because \(\{C_g,C_f\}_D\approx\mathcal{S}^{(0)}+\Delta\mathcal{S}\), consistency for free \(N_f\) forces the **modified secondary**
\[
\mathcal{S}^{(\psi^2)}
\;\equiv\;
\mathcal{S}^{(0)}+\Delta\mathcal{S}_{\mathrm{ultralocal}}
\;\approx\;0
\]
as a candidate phase-space constraint (ultralocal in \((\gamma,\pi,\psi)\)).

### 4.5 Preservation: HR identities do not extend to \(\Delta_{\mathrm{II}}\) (ORIGINAL WORK; encyclopedia aspirational)

Pure-HR preservation of \(\mathcal{S}^{(0)}\) uses Cayley–Hamilton / elementary-symmetric calculus on \(e_n(S)\) together with the shift-redefinition identities of [arXiv:1111.2070]. Those identities act in the algebra generated by \(\{\mathrm{d}e_n(S)\}\).

The new piece \(\Delta_{\mathrm{II}}\supset 2K_g^{ij}\mathcal{F}_{ij}^{(S\text{-matrix})}\) lies **outside** that algebra (§4.1). Therefore:

1. The pure-HR proof that \(\{\mathcal{S}^{(0)},H\}\) closes on the constraint surface **does not carry** to \(\{\mathcal{S}^{(0)}+\Delta_{\mathrm{II}},H\}\).
2. No \(\mathrm{Cl}(1,3)\) Fierz / Clifford identity was found that projects \(\mathcal{F}^{(S\text{-matrix})}\) back into \(\mathrm{span}\{\delta e_n/\delta\gamma\}\) for generic \(B_{\perp}\neq 0\) (self-threat discharged; absence of projection is B4 in 3+1d).
3. Term IV further deforms the Dirac bracket used in preservation, so even the gravitational Poisson skeleton of the HR proof is not the operative bracket.

**Structural consequence (D2 mechanism in 3+1d):** same as S2 — the secondary that removes the BD mode is deformed by a term outside the cancellation class; preservation is not protected by HR polynomial identities. Now realised in the **physical** spatial dimension with live DeWitt kinetics and explicit \(\delta S/\delta\gamma=\mathcal{L}_S^{-1}\).

**What is not claimed (honest blocker, not D4 trigger):** a full line-by-line 3+1d replay of every identity in 1111.2070 with Dirac insertions — the \(\{\mathcal{S}^{(\psi^2)},H\}\) encyclopedia. **Named aspirational blocker:** completing that encyclopedia would further tighten transfer documentation but is not required for the pre-registered D2 fork after a successful B4 + live-π probe (S2 AC R1.4 precedent applied in 3+1d). Prefer this named residual over fake D1.

---

## 5. Residual “3+1d-specific cancellation” escape — status

| Candidate escape (AC ~8%) | Status after S3 |
|---|---|
| \(\mathrm{Cl}(1,3)\) Fierz kills matrix-\(S\) channel | **Closed** — no such projection found; \(B_{\perp}\) survives |
| \(3\times 3\) CH richer than \(2\times 2\) kills B4 | **Closed** — CH spans \(\{I,S,S^2\}\); residual \(\dim B_{\perp}\ge 6\) **larger** than 2+1d |
| Miraculous ultralocal II+IV net cancel | **Still open at low prior** (~S2 P3 / AC ~4%); different tensor organisation; not inflated to D4 |
| Full \(\{\mathcal{S},H\}\) encyclopedia surprise | **Aspirational / named blocker**; structural non-inheritance of HR proof stands for D2 fork |

**Verdict on escape:** the named residual ~8% “3+1d dimension-specific cancellation” for the **B4 / Term II documentation** is **closed**. Low-prior II+IV miracle and unfinished encyclopedia remain as hygiene residuals only — same class AC already accepted under S2 R1, now with an actual 3+1d probe.

**Transfer fence update (for AC):** 2+1d D2 + 3+1d D2 ⇒ B4/live-π ghost-return structure is **not** a lower-dimensional artifact. W-3 from S2 stands with a **tighter** transfer fence. Still not a silent deposit change; still not a full dof-count encyclopedia.

---

## 6. Why this is D2, not D1 or D4

| Reading | Why rejected / accepted |
|---|---|
| **D4 (inconclusive / blocked)** | Rejected as primary landing. Setting did what was commissioned: non-scalar \(3\times 3\) \(S\), Term II B4 channel with explicit \(\delta S/\delta\gamma\), Term IV live. Pre-registered D2 fork met. Encyclopedia incompleteness is named aspirational — not a D4 trigger after successful B4 probe. |
| **D1 (ghost-free / healthy modified secondary)** | Rejected. No 3+1d identity cancelled \(\Delta_{\mathrm{II}}^{(S\text{-matrix})}\). Landing D1 would require naming a cancellation that was not found — that would be a fake D1. |
| **D2** | **Accepted.** \(\Delta\mathcal{S}\not\approx 0\); B4 active via matrix-element Term II; Term IV live; HR preservation does not extend; residual 3+1d B4-escape closed for documentation. **S2 W-3 stands** with tighter fence. |

**Mini-superspace:** not used as sole setting. FLRW-only would again risk 1408.0487 and can kill matrix anisotropy in \(S\) / \(B_{\perp}\).

**S2 not reopened.** This landing does not revisit S2’s D2 ratification or W-3 close.

---

## 7. Net \(\Delta\mathcal{S}\) summary (for AC / Jammer)

\[
\boxed{
\begin{aligned}
&\textbf{S3a:}\quad
\Lambda^*=\Lambda_0-\big[V''(\Lambda_0)\big]^{-1}H_{\mathrm{D}}'(\Lambda_0)+O(\psi^4)
\quad(6\text{ relative Lorentz params}).
\\[6pt]
&\textbf{Lemma S3:}\quad
\Delta\mathcal{S}
=
\Delta_{\mathrm{II}}+\Delta_{\mathrm{III}}+\Delta_{\mathrm{IV}},
\\
&\qquad
\Delta_{\mathrm{II}}
=
2K_g^{ij}\big(\mathcal{F}_{ij}^{(e_n)}+\mathcal{F}_{ij}^{(S\text{-matrix})}\big)\delta^{(3)}+\cdots,
\\
&\qquad\qquad
\mathcal{F}^{(S\text{-matrix})}
\supset
\sqrt{\gamma_g}\,e_3\,\bigl(\mathcal{L}_S^{-1}\delta X\bigr){:}B
\not\equiv 0
\text{ (B4; CH/Fierz do not kill)},
\\
&\qquad
\Delta_{\mathrm{IV}}\neq 0\text{ (DeWitt \(d=3\) π-channel live)},
\\
&\qquad
\Delta_{\mathrm{III,ultralocal}}
=
\frac{m(\sqrt{\gamma_g}-\sqrt{\gamma_f})}{\sqrt{\gamma_g}+\sqrt{\gamma_f}}\,\bar\psi\Gamma\psi
+\text{(ω mismatch)}+\cdots.
\\[6pt]
&\textbf{On-shell:}\quad
\Delta\mathcal{S}\not\approx 0\text{ generically;}
\quad
\mathcal{S}^{(\psi^2)}\equiv\mathcal{S}^{(0)}+\Delta\mathcal{S}_{\mathrm{ultralocal}}\approx 0
\\
&\qquad\text{is a modified secondary whose HR preservation proof does not extend to }\Delta_{\mathrm{II}}.
\\[6pt]
&\textbf{Probe status:}\quad
\text{B4 probed and active in 3+1d. Term II live. Term IV live.}
\\
&\textbf{Residual 3+1d B4-escape: CLOSED for documentation.}
\\
&\textbf{Landing D2 (transfer strengthened; S2 W-3 stands).}
\end{aligned}
}
\]

---

## 8. Constraint / standing reminders

- Relative Lorentz: still auxiliary (S3a). B3 / S1a / S2a consistent.
- Lapse-linearity: stands. D3 out.
- N_eff ≈ 1.52: stands. **Even D2 does not change deposit.**
- No κ. No f. Deposit P04. Foundation / transfer documentation only. No Core.
- **S2 D2 ratified / W-3 CLOSED: stands — not reopened.**

---

## 9. Comparison to S1 / S2 (why transfer strengthens)

| Feature | S1 (1+1d) | S2 (2+1d) | S3 (3+1d) |
|---|---|---|---|
| \(S\) | scalar \(=e_1\) | \(2\times 2\) matrix | \(3\times 3\) matrix |
| B4 | invisible | probed, active | **probed, active (richer \(B_{\perp}\))** |
| Term II | \(O(\psi^4)\) | nonzero, matrix-el. | **nonzero, matrix-el. + explicit \(\mathcal{L}_S^{-1}\)** |
| Term IV | 0 | nonzero (DeWitt \(d=2\)) | **nonzero (DeWitt \(d=3\))** |
| Term III | ultralocal | ultralocal | ultralocal (same family) |
| Residual 3+1d escape | n/a | named ~8% open | **B4-escape closed for docs** |
| Landing | D4 | D2 (W-3 closed) | **D2 (transfer strengthen; W-3 stands)** |

---

## 10. Sources

- Hassan–Rosen secondary constraint: [arXiv:1111.2070](https://arxiv.org/abs/1111.2070)
- Vierbein bigravity / SVC: [arXiv:1203.5783](https://arxiv.org/abs/1203.5783)
- Doubly-coupled scalar ghost; FLRW ≠ Bianchi: [arXiv:1408.0487](https://arxiv.org/abs/1408.0487)
- Nelson–Teitelboim 1978 (Dirac canonical gravity) — background
- Prior Scratch: Secondary-Constraint D4 lean D2 (B4 banked); Lemma S1 D4; Lemma S2 D2; AC S2 arbitration R1–R5 (2026-10-09)

All constructive claims in §§1–7: **ORIGINAL WORK.**

— Scratch, 2026-10-10. Filed after pre-registration. Blind to Jammer S3. Do not reopen S2.
