# Round 3 — Dirac-bracket coefficient + D-matrix absorption: VERDICT (Cursor Main)

**Landing: G-4 (sharpened).**  
**GO:** `Handoffs\GO_AC_Round3_One_Dirac_Bracket_Coefficient_And_D_Matrix_Absorption_20261019.md`  
**Prereg:** `Working\Opsi2_Round3_Dirac_Bracket_Coefficient_PREREGISTRATION_CursorMain_Blind_To_Scratch_20261019.md`  
**Blind to Scratch round-3 bodies at compute time** (Jammer R2/R3 controls and GO used).  
**Accept F14 on self:** Round-2 §3.3 freeze was Poisson-only; χ omitted.  
**No Core. No f.** K0′/K1/K2/K3 · F1–F15 · F9/F13 armed.

---

## 0. One-line

| Claim | Status |
|---|---|
| χ-corrected B1/B2 \(\{C_g^{(\psi)},C_f^{(\mathrm{grav})}\}_D\) is generically nonzero | **Yes** (mechanism) |
| That ∂δ coefficient is \(\propto(\psi^\dagger\alpha\psi)\,\pi_f\) (× \(\Sigma_g/\Sigma\)), **not** \(\propto W^{ij}p_j\) | **Established** (field content) |
| B1/B2 therefore **do not** cancel \(h_g(w_g-w_f X)^2 p_j\) | **Established** |
| Net matter ∂δ weight in the lapse-weighted second-class direction | \(h_g(w_g-w_f X)^2\) (perfect square; K1 at \(X=1\)) |
| D-matrix absorbs that residual | **Uncomputed** ← remaining blocker |
| Fork | **G-4** (not G-1/G-2: F13 / K0′ incomplete / K3 unmet) |

---

## 1. Setup

\[
\chi=\pi_\psi-\tfrac{i}{2}\bigl[\det e\cdot\bar\psi\gamma e^0+\det f\cdot\bar\psi\gamma f^0\bigr]\approx\pi_\psi-i\Sigma\psi,
\quad\Sigma=\Sigma_g+\Sigma_f.
\]
Dirac bracket:
\[
\{A,B\}_D=\{A,B\}-\{A,\chi\}C^{-1}\{\chi,B\}
\]
(with \(\bar\chi\) partners understood). On SVC: \(G=h_g X\), \(X=\sqrt{h_g^{-1}h_f}\), \(h_f=h_g X^2\).  
Matter–matter ∂δ weights (R1/R2 object, carried): \(\{C_g^{(\psi)},C_g^{(\psi)}\}\to h_g\cdot p\), \(\{C_f^{(\psi)},C_f^{(\psi)}\}\to h_f\cdot p\), cross \(\to G\cdot p\), with \(p_j\) the frame-neutral Dirac momentum density.

Probes: anisotropic \(e\neq f\) on SVC (\(\gamma_g=\delta\), \(\gamma_f=\mathrm{diag}(1,1,\lambda^2)\), \(\lambda=1.8\)); phase-gradient \(p\not\parallel\) residual; \(X=1\) for K1.

---

## 2. Lemma R3-A — B1 field content (χ-corrected gravity–matter cross)

Poisson disjointness: \(\{C_g^{(\psi)},C_f^{(\mathrm{grav})}\}_{\mathrm{PB}}=0\). Entire B1 is the χ correction
\[
B_1=-\{C_g^{(\psi)},\chi\}C^{-1}\{\chi,C_f^{(\mathrm{grav})}\}.
\]

**Factor 1.** \(\{\chi,C_f^{(\mathrm{grav})}\}\) is ultralocal. \(C_f^{(\mathrm{grav})}=G_{ijkl}\pi_f\pi_f/\sqrt{h_f}-\sqrt{h_f}R_f\); \(\chi\) depends on \(f\) through \(\Sigma_f[h_f]\) (config), not on \(\pi_f\). Config–config PB of \(\Sigma_f\) with \(-\sqrt{h_f}R_f\) vanishes. Only the kinetic \(\pi\pi\) piece contributes:
\[
\{\Sigma_f,C_f^{(\mathrm{grav})}\}\propto\pi_f\quad\text{(ultralocal \(\delta\))}.
\]
Hence \(\{\chi,C_f^{(\mathrm{grav})}\}\propto\psi\,\pi_f\) (ultralocal).

**Factor 2.** \(\{C_g^{(\psi)},\chi\}\) carries ∂δ. With \(C_g^{(\psi)}\supset -i\Sigma_g\psi^\dagger\alpha^k\nabla_k\psi+\mathrm{h.c.}\),
\[
\{C_g^{(\psi)}(x),\pi_\psi(y)\}\supset\Sigma_g\,(\psi^\dagger\alpha^k)\,\partial_k\delta(x-y)+\text{(ultralocal \(\nabla\psi\) pieces)}.
\]

**Product.** \(C^{-1}\sim\Sigma^{-1}\). The ∂δ coefficient of \(B_1\) is therefore
\[
\boxed{
\bigl[B_1\bigr]_{\partial\delta}^{\;k}
\;\sim\;
\frac{\Sigma_g}{\Sigma}\,(\psi^\dagger\alpha^k\psi)\,(\pi_f\text{-structure})
}
\]
(+ \(g\leftrightarrow f\) for B2: \(\propto(\psi^\dagger\alpha\psi)\,\pi_g\)).

**Not** of the form \(W^{ij}p_j\) with \(p_j=\psi^\dagger\nabla_j\psi\) and \(W\) built from \((h_g,h_f,G)\). Different field content: B1 is *(spinor bilinear)×(extrinsic-curvature/π)*; the perfect-square residual is *(metric weight)×(momentum density)*. Off-shell they cannot cancel. Weak equality via \(C_f\approx0\) replaces \(\pi\pi/\sqrt{h}\) by curvature+matter, and still does not manufacture a pure \(W\cdot p\) counter-term matching the matter–matter residual.

**Densitized cross-check (K4, schematic).** \(\varphi=\Sigma^{1/2}\psi\). Then \(C_g^{(\psi)}\) depends on \(h_f\) through \(\Sigma_g/\Sigma\), and \(\{C_g^{(\psi)},C_f^{\mathrm{EH}}[\tilde\pi_f]\}\) proceeds by \(\{h_f,\tilde\pi_f\}\) against the kinetic \(\pi\pi\) piece only → again ultralocal×π_f from the gravity–matter channel; the ∂δ \(W\cdot p\) sector stays in the matter–matter brackets. No double-count that would turn B1 into a \(W\cdot p\) counter-term.

**Conclusion.** Holding B1/B2 as Jammer asked: they are nonzero, but **they are not the counter-term to \(h_g(w_g-w_f X)^2 p_j\).** G-1 via “χ-cross cancels G” is closed as a route. F14 cured relative to Round 2.

---

## 3. Lemma R3-B — net residual is the perfect square

In the lapse-weighted second-class combination \(C_w=w_g C_g-w_f C_f\), matter–matter ∂δ assembles as
\[
w_g^2 h_g-2w_g w_f G+w_f^2 h_f=h_g(w_g-w_f X)^2
\]
(Jammer A4; re-verified numerically on 20 random SPD pairs, relative error \(\sim10^{-15}\); PSD).  
Equal-weight HR combination \(w_g=w_f=1\):
\[
\boxed{R^{ij}=h_g(I-X)^2,\qquad R_j=R^{ij}p_j.}
\]
**K1:** \(X=I\Rightarrow R=0\). Shown.  
**Continuum probe** (\(\lambda=1.8\), \(p=(0.3,-0.5,0.7)\)): \(R=\mathrm{diag}(0,0,0.64)\), \(Rp=(0,0,0.448)\not\parallel p\). So \(R\cdot p\) is **not** a scalar multiple of the frame-neutral matter part of total \(C_j\). Diagonal-shift absorption into \(C_j^{\mathrm{tot}}\propto p\) fails.

B1/B2 do not remove \(R_j\) (Lemma R3-A). Residual stands.

---

## 4. K0′ (partial) — where the D-matrix enters at \(\psi=0\)

At \(\psi=0\): no χ, no \(p\). Pure HR.

1. Bare ADM: \(\{C_g^{\mathrm{EH}}[N],C_g^{\mathrm{EH}}[M]\}_{\partial\delta}=C_i^g[h_g^{ij}(N\partial_jM-M\partial_jN)]\); same for \(f\). Cross \(\{C_g^{\mathrm{EH}},C_f^{\mathrm{EH}}\}_{\partial\delta}=0\) (disjoint \(\pi\)).
2. HR potential \(V[\gamma_g,\gamma_f,n]\) is ultralocal → no ∂δ.
3. **D-matrix entry:** shift redefinition \(N^i=L^i+L\,D^i{}_j(X)\,n^j+N\,n^i\) mixes the smeared momentum constraints into the lapse-weighted generators. The first-class / second-class split of \((C_g,C_f)\) and the structure functions in their ∂δ algebra are built from this redefinition; \(D=D(X)\) is the same square-root data as in \(V\) and in \(G=h_g X\).

**Gap (honest):** line-by-line reproduction of Hassan–Rosen eqs. for the assembled structure functions of the second-class combination (full symbolic K0′) is **not** completed this round. Terminal fork blocked by K0′ incompleteness alone.

---

## 5. D-matrix absorption (K3) — status

Live candidate (F12 honored): \(R_j=h_g(I-X)^2 p_j\) is built from HR’s own \(X\); \(D(X)\) could in principle produce a cancelling structure in the preservation / assembled algebra.

**Not shown this round:**
- that \(\{C_w,C_w\}_{\partial\delta}=S^{ij}(X)\,(C_j^{g}+C_j^{f}+p_j)\) with \(S=h_g(I-X)^2\), or
- that preservation \(\{\mathcal{S}^{(\psi^2)},H\}\) with \(D\) inserted yields \(-R_j\).

Structural tension (motive, not a landing): \(D\) mixes two gravitational momentum densities; matter contributes one \(p_j\) with frame-dependent weight \(R\neq \propto I\). That is the K3 question, not an answer. **Asserting G-2 without the D-matrix bracket is F12/K3 failure. Declined.**

---

## 6. Fork

| Fork | Why not / why |
|---|---|
| G-1 | No counter-term exhibited; B1/B2 ruled out as the \(W\cdot p\) counter-term; \(\{\mathcal{S}^{(\psi^2)},H\}\) not reached |
| G-2 | K3 unmet; K0′ incomplete; F13 |
| G-3 | Sector (a) not closed |
| **G-4** | **Yes** — residual \(R_j=h_g(I-X)^2 p_j\) named; B1/B2 χ-channel computed and shown *not* to cancel it; blocker = D-matrix preservation / assembly bracket + completed K0′ |

**Priors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. No posterior movement (B1 negative result removes one G-1 route but does not earn G-2).

---

## 7. Standing

Claim 3 not established. P04 / \(N_{\mathrm{eff}}\) unchanged. No Core.

**Blocker for Round 4:** compute \(\{C_w,C_w\}_{\partial\delta}\) / \(\{\mathcal{S}^{(\psi^2)},H\}\) with explicit \(D^i{}_j(X)\), with K0′ finished; test whether \(-R_j\) appears.

— Cursor Main, 2026-10-19. (Round 3.)
