# P09 Gate-0 — Lemma S2 VERDICT (Scratch, construction)

## Landing: D2 — B4 probed and active in 2+1d; Term II/IV live; \(\Delta\mathcal{S}\not\approx 0\); W-3-eligible (AC ratifies)

**Explicit \(\Delta\mathcal{S}\) at \(O(\psi^2)\) in 2+1d bigravity + Dirac. \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) is a non-scalar \(2\times 2\) matrix: the Dirac spatial-kinetic dependence on matrix elements \(S^i{}_j\) is not reducible to \(\{e_n(S)\}\) by Cayley–Hamilton for generic bilinears (B4 live and active). DeWitt π-kinetics are nondegenerate (Term IV live). Cross Term II and Dirac-bracket Term IV are nonzero at working order; Term III contributes an ultralocal remainder as in S1. Net \(\Delta\mathcal{S}\not\approx 0\) on the generic constraint surface; HR polynomial preservation identities do not extend to the \(\Delta_{\mathrm{II}}\) piece. Per AC R4 / prereg: D2, eligible for W-3 after AC ratification. 2+1d dof ≠ 3+1d — transfer is AC’s call, not silent.**

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-09
**Authority:** Greg GO; Directive `…Lemma_S2_2plus1d_Bigravity_Dirac_GO…20261009.md`; AC R4
**Pre-registration:** `Working/P09_Gate0_Lemma_S2_PREREGISTRATION_Scratch_…_20261009.md` (filed **before** this computation)
**Blind to:** all `Jammer*Lemma_S2*` files
**Label:** ORIGINAL WORK throughout

---

## 0. AC decision rules applied

| Outcome | Gate 0 action |
|---|---|
| **D2** | **Eligible for W-3** (AC ratifies before close) ← this landing |
| D1 | W-2; suggestive only for 3+1d |
| D4 | W-2; reassess setting |

Even D1 ≠ restore symmetric ν. No f. Not a route to κ. Deposit P04 unchanged.

---

## 1. Setup — 2+1d bigravity + Dirac (ORIGINAL WORK)

Spacetime \((t,x^1,x^2)\). ADM data:

| Object | 2+1d content |
|---|---|
| Spatial metrics | \(\gamma_{ij}^{(g)},\,\gamma_{ij}^{(f)}\) — symmetric \(2\times 2\) |
| Momenta | \(\pi_g^{ij},\,\pi_f^{ij}\) |
| Square-root matrix | \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) — **non-scalar** \(2\times 2\) |
| \(e_n(S)\) | \(e_0=1\), \(e_1=\mathrm{tr}\,S\), \(e_2=\det S\) |
| Relative Lorentz | \(\mathrm{SO}(1,2)_{\mathrm{rel}}\): 2 boosts \(\varphi^\alpha\) + 1 rotation \(\theta\) |
| Dirac field | 2-component spinor \(\psi\); diagonal \(\mathrm{Spin}(1,2)\) only |
| HR potential | \(V=\sqrt{\gamma_g}\,(\beta_0+\beta_1 e_1(S)+\beta_2 e_2(S))\) (equiv. OK) |

Doubly-coupled Dirac action (first order):
\[
S_\psi=\int\mathrm{d}t\,\mathrm{d}^2x\;\Big[
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
H=\int\mathrm{d}^2x\;\big(N_g C_g+N_f C_f+N^i C_i\big).
\]

### 1.1 Why this setting probes what S1 could not (ORIGINAL WORK)

**(P1) Matrix \(S\).** For \(2\times 2\) \(S\), Cayley–Hamilton reads
\[
S^2-(\mathrm{tr}\,S)\,S+(\det S)\,I=0,
\]
so analytic functions of \(S\) are spanned by \(\{I,S\}\). The HR potential depends only on \(\{e_1,e_2\}=\{\mathrm{tr}\,S,\det S\}\). The Dirac spatial kinetic, after symmetric-vielbein presentation \(\varepsilon_\alpha{}^i=e_\alpha{}^j S_j{}^i\), depends on the contraction
\[
S_j{}^i\,B_i{}^j,\qquad
B_i{}^j\sim\bar\psi\,\gamma^\alpha e_\alpha{}^j\,D_i\psi
\]
(schematic; hermitanized form in §3). This equals a function of \(\{e_n(S)\}\) alone **only if** \(B\propto I\). For generic \(\psi\) and generic \((\gamma_g,\gamma_f)\), \(B_i{}^j\) is **not** proportional to \(\delta_i{}^j\). Therefore **B4 does not evaporate** in 2+1d — unlike S1’s scalar \(S=e_1(S)\).

**(P2) Nondegenerate kinetics.** With \(d=2\) spatial dimensions the DeWitt kinetic term
\[
\frac{1}{\sqrt{\gamma}}\Big(\pi^{ij}\pi_{ij}-\pi^2\Big)
\]
is nondegenerate on traceless \(\pi\). (Contrast: 1+1d / \(d=1\), where the DeWitt factor \(1/(d-1)\) is singular and 2D EH is topological — Term IV dead in S1.) **Term IV / π-channel is live.**

**(P3) Dof caveat (honest).** Pure GR in 2+1d has no bulk graviton; massive bigravity restores local dof. Algebraic secondary-constraint structure still governs the BD mode. A 2+1d D2 is W-3-**eligible**, not a silent 3+1d dof identification — AC ratifies transfer.

---

## 2. Sub-lemma S2a — modified SVC \(\Lambda^*\) (ORIGINAL WORK)

Pure-gravity SVC: \(\partial V/\partial\Lambda_{\mathrm{rel}}\big|_{\Lambda_0}=0\), with Hessian \(\partial^2 V/\partial\Lambda_{\mathrm{rel}}^2\big|_{\Lambda_0}\) nondegenerate for generic \((\gamma_g,\gamma_f)\) (relative Lorentz auxiliary — banked B3).

Dirac sources the SVC:
\[
\frac{\partial V}{\partial\Lambda_{\mathrm{rel}}}+\frac{\partial H_{\mathrm{Dirac}}}{\partial\Lambda_{\mathrm{rel}}}=0.
\]
Expand \(\Lambda=\Lambda_0+\delta\Lambda\):
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
**S2a result:** all 3 relative Lorentz parameters remain auxiliary; leading correction is \(O(\psi^2)\), linear in the Dirac bilinears that differentiate through \(A_f(\varphi)\) and the boosted \(f\)-beit.

**Corollary used below:** substituting \(\Lambda^*\) into the constraints corrects \(C_g,C_f\) only at \(O(\psi^4)\), because \(\partial C/\partial\Lambda\big|_{\Lambda_0}=O(\psi^2)\) (the \(V\)-piece vanishes by SVC) and \(\delta\Lambda=O(\psi^2)\). Therefore, at \(O(\psi^2)\), evaluate Dirac contributions at \(\Lambda=\Lambda_0\). Without loss of generality take time-gauge alignment \(\varphi_0^\alpha=0\) and symmetric-vielbein spatial gauge (relative rotation fixed so \(\varepsilon=e\cdot S\)):
\[
\varepsilon_\alpha{}^i=e_\alpha{}^j\,S_j{}^i,\qquad
\Sigma=(\sqrt{\gamma_g}+\sqrt{\gamma_f})\,A_0.
\]

---

## 3. Effective Dirac constraints at \(\Lambda_0\), \(O(\psi^2)\) (ORIGINAL WORK)

After Nelson–Teitelboim absorption of spin-connection momenta into redefinitions, \(C_g^{(\mathrm{D})}\) and \(C_f^{(\mathrm{D})}\) are independent of \((\pi_g,\pi_f)\).

Lapse coefficients from each tetrad’s spatial kinetic + mass (2+1d), in symmetric-vielbein presentation:

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

Substitute \(\varepsilon=e\cdot S\) and \(\sqrt{\gamma_f}=\sqrt{\gamma_g}\,\det S=\sqrt{\gamma_g}\,e_2(S)\):

\[
\boxed{
\begin{aligned}
K_f
&=
\sqrt{\gamma_g}\,e_2(S)\;
\bar\psi\,i\gamma^\alpha e_\alpha{}^j\,S_j{}^i\,D_i\psi
=
\sqrt{\gamma_g}\;
S_j{}^i\,B_i{}^j[e,\psi;\,e_2\text{-weight}],
\\[4pt]
M_f
&=
m\sqrt{\gamma_g}\,e_2(S)\,\bar\psi\psi.
\end{aligned}
}
\]

**Polynomial-class split (load-bearing for B4):**
- \(M_f\) depends on \(S\) only through \(e_2(S)=\det S\) — **inside** the HR class.
- \(K_f\) depends on the **matrix elements** \(S_j{}^i\) contracted with the spinor-geometric tensor \(B_i{}^j\) — **outside** \(\{e_n(S)\}\) for generic \(B\not\propto I\).

At \(\varphi=0\):
\[
\frac{\delta C_g^{(\mathrm{D})}}{\delta\gamma_f}=0
\quad\text{at }O(\psi^2)
\]
(no direct \(\gamma_f\) in \(C_g^{(\mathrm{D})}\) once \(\Lambda\) is fixed at \(\Lambda_0\)), while
\[
\frac{\delta C_f^{(\mathrm{D})}}{\delta\gamma_g}\neq 0
\]
through both \(e_2(S)\) and \(S_j{}^i\) in \(K_f\), and through the \(g\)-triad in the same presentation.

Second-class set: \(\chi=\pi_\psi-\Sigma\psi^\dagger\approx 0\). Dirac bracket:
\[
\{\psi_\alpha(x),\psi^\dagger_\beta(y)\}_D
=(\Sigma^{-1})_{\alpha\beta}\,\delta^{(2)}(x-y),
\qquad
\Sigma^{-1}=A_0^{-1}/(\sqrt{\gamma_g}+\sqrt{\gamma_f}).
\]

Gravitational kinetics (live):
\[
C_I^{(\mathrm{grav})}
=
\frac{1}{\sqrt{\gamma_I}}\Big(\pi_I^{ij}\pi_{I\,ij}-\pi_I^2\Big)
-\sqrt{\gamma_I}\,R_I
+V_I[\beta,S],
\]
so
\[
\frac{\delta C_I^{(\mathrm{grav})}}{\delta\pi_I^{ij}}
=
\frac{2}{\sqrt{\gamma_I}}\Big(\pi_{I\,ij}-\pi_I\,\gamma_{ij}^{(I)}\Big)
\equiv 2K_{ij}^{(I)}
\neq 0
\]
on generic momenta (traceless channel nondegenerate).

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

### 4.1 Term (II) — cross brackets: **nonzero; B4 channel**

\[
\{C_g^{(\mathrm{D})}(x),\,C_f^{(\mathrm{grav})}(y)\}
=
\int\mathrm{d}^2z\;
\frac{\delta C_g^{(\mathrm{D})}(x)}{\delta\gamma_{ij}^{(f)}(z)}
\frac{\delta C_f^{(\mathrm{grav})}(y)}{\delta\pi_f^{ij}(z)}
+\cdots
\]
At \(\Lambda_0\) and \(O(\psi^2)\): \(\delta C_g^{(\mathrm{D})}/\delta\gamma_f=0\), so this half vanishes at working order (S2a corollary: \(\Lambda^*\) corrections enter at \(O(\psi^4)\)).

The partner is the B4 probe:
\[
\{C_g^{(\mathrm{grav})}(x),\,C_f^{(\mathrm{D})}(y)\}
=
\int\mathrm{d}^2z\;
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
m\,\frac{\delta\big(\sqrt{\gamma_g}\,e_2(S)\big)}{\delta\gamma_{ij}^{(g)}}\,\bar\psi\psi
\quad\text{— HR-class (\(e_2\) only).}
\]
\[
\frac{\delta K_f}{\delta\gamma_{ij}^{(g)}}
\propto
\frac{\delta}{\delta\gamma_{ij}^{(g)}}
\Big(
\sqrt{\gamma_g}\,e_2(S)\,S_k{}^\ell\,
\bar\psi\,i\gamma^\alpha e_\alpha{}^k D_\ell\psi
\Big)
\]
contains, among other pieces,
\[
\boxed{
\sqrt{\gamma_g}\,e_2(S)\,
\frac{\partial S_k{}^\ell}{\partial\gamma_{ij}^{(g)}}\,
\bar\psi\,i\gamma^\alpha e_\alpha{}^k D_\ell\psi
}
\]
— **matrix-element channel**, not constrained to \(\mathrm{d}e_n(S)\).

**Cayley–Hamilton does not cancel this** (self-threat §4 of prereg, discharged): writing \(S=a\,I+b\,\hat S_{\mathrm{TF}}\) still leaves the traceless part of \(S\) contracted against the traceless part of \(B\); that scalar \(S_{\mathrm{TF}}{:}B_{\mathrm{TF}}\) is independent of \(\{e_1,e_2\}\) as a functional of the spinor configuration. Explicitly, for \(B=B_0 I+B_{\mathrm{TF}}\),
\[
S_j{}^i B_i{}^j
=e_1 B_0+S_{\mathrm{TF}}{:}B_{\mathrm{TF}},
\]
and \(S_{\mathrm{TF}}{:}B_{\mathrm{TF}}\) is **not** a universal function of \(e_n(S)\) alone.

Therefore
\[
\boxed{
\Delta_{\mathrm{II}}(x,y)
=
2K_g^{ij}(x)\,\mathcal{F}_{ij}^{(\mathrm{D})}(x)\,\delta^{(2)}(x-y)
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
and \(\mathcal{F}^{(S\text{-matrix})}\not\equiv 0\) for generic \((\gamma,\psi)\).

**Weak vanishing?** On \(C_i\approx 0\), derivative-of-δ pieces rearrange into diffeomorphism contributions. The ultralocal remainder \(2K_g^{ij}\mathcal{F}_{ij}^{(\mathrm{D})}\) is **not** a linear combination of \(C_g,\,C_f,\,C_i,\,\mathcal{S}^{(0)}\) for generic data: \(\mathcal{S}^{(0)}\) is built from HR \(e_n\)-derivatives and gravitational momenta in the Hassan–Rosen combination; \(\mathcal{F}^{(S\text{-matrix})}\) injects a linearly independent spinor-weighted tensor structure. Special loci (\(S\propto I\) with \(B_{\mathrm{TF}}=0\), or \(\psi=0\), or \(K_g=0\)) are not the full constraint surface.

\[
\boxed{\Delta_{\mathrm{II}}\not\approx 0\quad\text{at }O(\psi^2)\text{ on the generic constraint surface (B4 active).}}
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
\int\mathrm{d}^2z\;
\frac{\delta C_I^{(\mathrm{grav})}(x)}{\delta\pi_I^{ij}(z)}
\frac{\delta\Sigma(y)}{\delta\gamma_{ij}^{(I)}(z)}
=
2K_I^{ij}(x)\,\frac{\delta\Sigma}{\delta\gamma_{ij}^{(I)}}\,\delta^{(2)}(x-y)
\neq 0
\]
whenever \(K_I\neq 0\) and \(\delta\Sigma/\delta\gamma_I\neq 0\) (both generic: \(\Sigma\propto\sqrt{\gamma_g}+\sqrt{\gamma_f}\)).

Hence
\[
\boxed{\Delta_{\mathrm{IV}}\neq 0\quad\text{in 2+1d (P2; contrast }\Delta_{\mathrm{IV}}=0\text{ in S1).}}
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

**Common-structure pieces.** Kinetic–kinetic \(\{K_g,K_f\}_D\) reproduces spatial-diffeomorphism contributions \(\sim(C_i^{(\mathrm{D})}(x)+C_i^{(\mathrm{D})}(y))\partial_i\delta^{(2)}\), hence **weakly zero** on \(C_i\approx 0\).

**Mass–mass.** \(M_g\propto\sqrt{\gamma_g}\,\bar\psi\psi\) and \(M_f\propto\sqrt{\gamma_f}\,\bar\psi\psi\) share the same Clifford scalar; with \(\Sigma\propto\mathbf{1}\) at \(\varphi=0\), \(\{M_g,M_f\}_D=0\).

**Cross kinetic–mass / connection — survives** (same logic as S1, now with \(2\times 2\) densities):
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
Not weakly zero for generic \((\gamma_g\neq\gamma_f,\,\psi\neq 0)\). **Does not probe B4** (same mechanism as S1 Term III); retained for completeness of \(\Delta\mathcal{S}\).

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

Dominant Gate-0 content is \(\Delta_{\mathrm{II}}\) (B4) with \(\Delta_{\mathrm{IV}}\) (π-channel) as co-live correction; \(\Delta_{\mathrm{III}}\) is additional and already seen in S1.

Because \(\{C_g,C_f\}_D\approx\mathcal{S}^{(0)}+\Delta\mathcal{S}\), consistency for free \(N_f\) forces the **modified secondary**
\[
\mathcal{S}^{(\psi^2)}
\;\equiv\;
\mathcal{S}^{(0)}+\Delta\mathcal{S}_{\mathrm{ultralocal}}
\;\approx\;0
\]
as a candidate phase-space constraint (ultralocal in \((\gamma,\pi,\psi)\)).

### 4.5 Preservation: HR identities do not extend to \(\Delta_{\mathrm{II}}\) (ORIGINAL WORK)

Pure-HR preservation of \(\mathcal{S}^{(0)}\) uses Cayley–Hamilton / elementary-symmetric calculus on \(e_n(S)\) together with the shift-redefinition identities of [arXiv:1111.2070]. Those identities act in the algebra generated by \(\{\mathrm{d}e_n(S)\}\).

The new piece \(\Delta_{\mathrm{II}}\supset 2K_g^{ij}\mathcal{F}_{ij}^{(S\text{-matrix})}\) lies **outside** that algebra (§4.1). Therefore:

1. The pure-HR proof that \(\{\mathcal{S}^{(0)},H\}\) closes on the constraint surface **does not carry** to \(\{\mathcal{S}^{(0)}+\Delta_{\mathrm{II}},H\}\).
2. No Clifford / Fierz identity was found that projects \(\mathcal{F}^{(S\text{-matrix})}\) back into \(\mathrm{span}\{\delta e_n/\delta\gamma\}\) for generic \(B_{\mathrm{TF}}\neq 0\) (self-threat discharged; absence of projection is the content of B4).
3. Term IV further deforms the Dirac bracket used in preservation, so even the gravitational Poisson skeleton of the HR proof is not the operative bracket.

**Structural consequence (D2 mechanism):** the secondary that removes the BD mode is deformed by a term outside the cancellation class. The deformed secondary’s preservation is not protected by the HR polynomial identities. This is the banked obstruction B4, now **explicitly realised** at \(O(\psi^2)\) with live π-channel — not a dimensional artifact.

**What is not claimed:** a full line-by-line 2+1d replay of every identity in 1111.2070 with Dirac insertions. The claim is sharper and sufficient for the pre-registered D2 fork: B4 is probed, active, and produces a weakly nonvanishing \(\Delta_{\mathrm{II}}\) whose preservation cannot inherit the HR proof. That is the ghost-return structure Gate 0 was testing.

---

## 5. Why this is D2, not D1 or D4

| Reading | Why rejected / accepted |
|---|---|
| **D4 (inconclusive / too simple)** | Rejected. The setting did what S1 could not: matrix \(S\) live, Term II B4 channel explicit, Term IV live. Computation closes the pre-registered D2 fork. |
| **D1 (ghost-free / healthy modified secondary)** | Rejected as Gate-0 landing. A “healthy lapse-ratio” reading would ignore that preservation identities fail for the B4 piece — that was the S1 fake-pattern risk AC locked in R1b. 2+1d D1 is also pre-registered as suggestive-only; claiming it here would under-sell an active obstruction. |
| **D2** | **Accepted.** \(\Delta\mathcal{S}\not\approx 0\); B4 active via matrix-element Term II; Term IV live; HR preservation does not extend. Eligible for **W-3** per AC R4; AC ratifies before close. |

**Transfer note (mandatory):** 2+1d dof counting ≠ 3+1d. D2 here is **W-3-eligible**, not automatic 3+1d closure without AC ratification. Residual escape for 3+1d would require a dimension-specific cancellation absent in 2+1d — logically open at low prior, not a reason to land D4 after a successful B4 probe.

**Mini-superspace:** not used. FLRW-only would again risk 1408.0487 (FLRW-safe ≠ Bianchi-safe) and can kill matrix anisotropy in \(S\).

---

## 6. Net \(\Delta\mathcal{S}\) summary (for AC / Jammer)

\[
\boxed{
\begin{aligned}
&\textbf{S2a:}\quad
\Lambda^*=\Lambda_0-\big[V''(\Lambda_0)\big]^{-1}H_{\mathrm{D}}'(\Lambda_0)+O(\psi^4).
\\[6pt]
&\textbf{Lemma S2:}\quad
\Delta\mathcal{S}
=
\Delta_{\mathrm{II}}+\Delta_{\mathrm{III}}+\Delta_{\mathrm{IV}},
\\
&\qquad
\Delta_{\mathrm{II}}
=
2K_g^{ij}\big(\mathcal{F}_{ij}^{(e_n)}+\mathcal{F}_{ij}^{(S\text{-matrix})}\big)\delta^{(2)}+\cdots,
\\
&\qquad\qquad
\mathcal{F}^{(S\text{-matrix})}\not\equiv 0\text{ (B4; CH does not kill)},
\\
&\qquad
\Delta_{\mathrm{IV}}\neq 0\text{ (DeWitt π-channel live)},
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
\text{B4 probed and active. Term II live. Term IV live.}
\quad
\textbf{Landing D2 (W-3-eligible).}
\end{aligned}
}
\]

---

## 7. Constraint / standing reminders

- Relative Lorentz: still auxiliary (S2a). B3 stands; S1a consistent.
- Lapse-linearity: stands. D3 out.
- N_eff ≈ 1.52: stands. **Even D2 does not change deposit** — and even a future D1 would not restore symmetric ν.
- No κ. No f. Deposit P04. Foundation only. No Core.

---

## 8. Comparison to S1 (why the landing changed)

| Feature | S1 (1+1d) | S2 (2+1d) |
|---|---|---|
| \(S\) | scalar \(=e_1(S)\) | \(2\times 2\) matrix |
| B4 | invisible | **probed, active** |
| Term II | \(O(\psi^4)\) | **nonzero, matrix-element channel** |
| Term IV | 0 (topological EH) | **nonzero (DeWitt live)** |
| Term III | nonzero ultralocal | nonzero ultralocal (same family) |
| Landing | D4 (too simple) | **D2 (W-3-eligible)** |

---

## 9. Sources

- Hassan–Rosen secondary constraint: [arXiv:1111.2070](https://arxiv.org/abs/1111.2070)
- Vierbein bigravity / SVC: [arXiv:1203.5783](https://arxiv.org/abs/1203.5783)
- Doubly-coupled scalar ghost; FLRW ≠ Bianchi: [arXiv:1408.0487](https://arxiv.org/abs/1408.0487)
- Nelson–Teitelboim 1978 (Dirac canonical gravity) — background
- Prior Scratch: secondary-constraint D4 lean D2; Lemma S1 D4 (2026-10-09); AC S1 arbitration (2026-10-09)

All constructive claims in §§1–6: **ORIGINAL WORK.**

— Scratch, 2026-10-09. Filed after pre-registration. Blind to Jammer S2 attack files.
