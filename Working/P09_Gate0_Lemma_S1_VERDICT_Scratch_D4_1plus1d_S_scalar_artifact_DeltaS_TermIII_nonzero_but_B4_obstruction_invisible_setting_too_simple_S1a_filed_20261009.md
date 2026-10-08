# P09 Gate-0 — Lemma S1 VERDICT (Scratch, construction)

## Landing: D4 — inconclusive for Gate 0; 1+1d setting too simple

**Explicit \(\Delta\mathcal{S}\) is computed in 1+1d bigravity + Dirac at \(O(\psi^2)\). Terms (II) and (IV) vanish by dimensional specialisation; Term (III) is nonzero and defines a modified secondary of healthy second-class pattern. But the banked 3+1d obstruction (B4: Dirac dependence on matrix elements of \(S\), not \(e_n(S)\)) is invisible here because \(S\) is a scalar, and 2D Einstein–Hilbert has no bulk graviton kinetics. Per AC R4 and the pre-registered ban on fake D1, this does not close Gate 0. Maintain W-2; reassess setting.**

**From:** Scratch (construction lead)
**To:** AC, Jammer (adversarial), Cursor Main (literature) · **Cc:** Greg, PC
**Date:** 2026-10-09
**Authority:** Greg GO; Directive `…Lemma_S1_1plus1d_Bigravity_Dirac_GO…20261009.md`; AC R4
**Pre-registration:** `Working/P09_Gate0_Lemma_S1_PREREGISTRATION_Scratch_…_20261009.md` (filed before this computation)
**Blind to:** all `Jammer*Lemma_S1*` files
**Label:** ORIGINAL WORK throughout

---

## 0. AC decision rules applied

| Outcome | Gate 0 action |
|---|---|
| D2 in 1+1d | W-3 |
| D1 in 1+1d | W-2; suggestive only for 3+1d |
| **D4** | **W-2; reassess whether setting is too simple** ← this landing |

Even D1 ≠ restore symmetric ν. No f. Not a route to κ. Deposit P04 unchanged.

---

## 1. Setup — 1+1d bigravity + Dirac (ORIGINAL WORK)

Spacetime \((t,x)\). ADM data:

| Object | 1+1d content |
|---|---|
| Spatial metrics | scalars \(q_g(x),\,q_f(x)\) |
| Momenta | \(p_g,\,p_f\) |
| Square-root matrix | \(S=\sqrt{q_f/q_g}\) — a **scalar** (1×1) |
| Relative Lorentz | one boost \(\varphi\in\mathrm{SO}(1,1)_{\mathrm{rel}}\) |
| Dirac field | 2-component spinor \(\psi\); diagonal \(\mathrm{Spin}(1,1)\) only |
| HR potential | \(V=\sqrt{q_g}\,(\beta_0+\beta_1 S)+\beta_2\sqrt{q_f}\) (equiv. form OK) |

Doubly-coupled Dirac action (first order):
\[
S_\psi=\int\mathrm{d}t\,\mathrm{d}x\;\Big[
\det(e)\,\bar\psi\,i\gamma^a e_a^\mu D_\mu^{(e)}\psi
+\det(\varepsilon)\,\bar\psi\,i\gamma^a\varepsilon_a^\mu D_\mu^{(\varepsilon)}\psi
-m\text{-terms}\Big].
\]

Lapse cancellation (banked, D3 out) survives: each tetrad contributes \(\sqrt{q_I}\) after \(N_I\) cancels in the time kinetic, so
\[
\pi_\psi=\Sigma\,\psi^\dagger,\qquad
\Sigma=\sqrt{q_g}\,A_g(\varphi)+\sqrt{q_f}\,A_f(\varphi),
\]
and the Hamiltonian remains linear in both lapses:
\[
H=\int\mathrm{d}x\;\big(N_g C_g+N_f C_f+N^x C_x\big).
\]

### 1.1 Structural caveats of the setting (honest, load-bearing)

**(C1) \(S\) is scalar.** For a \(1\times 1\) matrix the elementary symmetric polynomials are \(\{e_0=1,\,e_1=S\}\). Any Dirac dependence on the “matrix element” \(S\) **is** dependence on \(e_1(S)\). The banked B4 obstruction (Dirac kinetic outside the HR polynomial class) **evaporates identically in 1+1d**. This is a dimensional artifact, not evidence that B4 cancels in 3+1d.

**(C2) 2D Einstein–Hilbert is topological.** Bulk \(\int\sqrt{-g}\,R\) is Euler; there are no local graviton kinetic \(\pi^2/\sqrt{q}\) terms of the 3+1d DeWitt type. Gravitational contributions to \(C_g^{(\mathrm{grav})},\,C_f^{(\mathrm{grav})}\) in this setting are carried by the HR potential (and total-derivative curvature bookkeeping), not by a nondegenerate supermetric kinetics. Term (IV) channels that need \(\delta C^{(\mathrm{grav})}/\delta p\) are absent or degenerate.

**(C3) BD mode counting is not the 3+1d count.** A “ghost returns / ghost-free” verdict in 1+1d cannot be read as a 3+1d spin-2 dof count; at best it tests algebraic bracket structure.

These three caveats are why a clean 1+1d D1 would still be non-transferable, and why a D4 “setting too simple” landing is available even when the algebra can be evaluated.

---

## 2. Sub-lemma S1a — modified SVC \(\varphi^*\) (ORIGINAL WORK)

Pure-gravity SVC: \(\partial V/\partial\varphi\big|_{\varphi_0}=0\), with \(\partial^2 V/\partial\varphi^2\big|_{\varphi_0}\neq 0\) for generic \((q_g,q_f)\) (relative boost auxiliary — banked B3, same mechanism).

Dirac sources the SVC:
\[
\frac{\partial V}{\partial\varphi}+\frac{\partial H_{\mathrm{Dirac}}}{\partial\varphi}=0.
\]
Expand \(\varphi=\varphi_0+\delta\varphi\):
\[
V''(\varphi_0)\,\delta\varphi+H_{\mathrm{D}}'(\varphi_0)+O(\delta\varphi^2,\delta\varphi\cdot\psi^2)=0.
\]
Since \(H_{\mathrm{D}}=O(\psi^2)\),
\[
\boxed{
\varphi^*(q_g,q_f,\psi)
=\varphi_0(q_g,q_f)
-\frac{1}{V''(\varphi_0)}\,\frac{\partial H_{\mathrm{Dirac}}}{\partial\varphi}\Big|_{\varphi_0}
+O(\psi^4)
=\varphi_0+O(\psi^2).
}
\]
**S1a result:** relative boost remains auxiliary; leading correction is \(O(\psi^2)\), linear in the Dirac bilinears that differentiate w.r.t. \(\varphi\) through \(A_f(\varphi)\) and the \(f\)-beit.

**Corollary used below:** substituting \(\varphi^*\) into the constraints corrects \(C_g,C_f\) only at \(O(\psi^4)\), because \(\partial C/\partial\varphi\big|_{\varphi_0}=O(\psi^2)\) (the \(V\)-piece vanishes by SVC) and \(\delta\varphi=O(\psi^2)\). Therefore, at \(O(\psi^2)\), one may evaluate Dirac contributions at \(\varphi=\varphi_0\). Without loss of generality take time-gauge alignment \(\varphi_0=0\) (diagonal frames), so \(A_g=A_f=A_0\) and
\[
\Sigma=( \sqrt{q_g}+\sqrt{q_f})\,A_0.
\]

---

## 3. Effective Dirac constraints at \(\varphi=0\), \(O(\psi^2)\) (ORIGINAL WORK)

After Nelson–Teitelboim absorption of spin-connection momenta into redefinitions (standard; single-metric Dirac gravity), \(C_g^{(\mathrm{D})}\) and \(C_f^{(\mathrm{D})}\) are independent of \((p_g,p_f)\).

Lapse coefficients from each tetrad’s spatial kinetic + mass (1+1d):
\[
\begin{aligned}
C_g^{(\mathrm{D})}
&=
\underbrace{\psi^\dagger(-i\alpha\,\partial_x)\psi}_{K}
+
\underbrace{m\sqrt{q_g}\,\psi^\dagger\beta\psi}_{M_g}
+
\Omega_g[\omega_g],
\\[4pt]
C_f^{(\mathrm{D})}
&=
K
+
M_f
+
\Omega_f[\omega_f],
\end{aligned}
\]
with \(\alpha,\beta\) the standard hermitanized 1+1d Clifford matrices, \(\Omega_I\) the spin-connection bilinears built from \(\omega_I\sim\partial_x\ln\sqrt{q_I}\), and — crucially — **the same \(K\) appearing in both** (each tetrad contributes \(\,N_I\bar\psi\,i\gamma^1\partial_x\psi\,\) after lapse cancellation; cf. prior round B.3).

Mass pieces: \(M_I=m\sqrt{q_I}\,\psi^\dagger\beta\psi\). At \(\varphi=0\),
\[
\frac{\delta C_g^{(\mathrm{D})}}{\delta q_f}=0,\qquad
\frac{\delta C_f^{(\mathrm{D})}}{\delta q_g}=0
\]
at \(O(\psi^2)\) (each sector sees only its own \(\sqrt{q_I}\) in the mass/connection; kinetic \(K\) is metric-ultralocal in the coefficient).

Second-class set: \(\chi=\pi_\psi-\Sigma\psi^\dagger\approx 0\). Dirac bracket on reduced spinor space:
\[
\{\psi_\alpha(x),\psi^\dagger_\beta(y)\}_D
=(\Sigma^{-1})_{\alpha\beta}\,\delta(x-y),
\qquad
\Sigma^{-1}=A_0^{-1}/(\sqrt{q_g}+\sqrt{q_f}).
\]

---

## 4. Explicit \(\Delta\mathcal{S}\) at \(O(\psi^2)\) (ORIGINAL WORK)

Decompose on the constraint surface \(C_g\approx C_f\approx C_x\approx 0\), \(\varphi=\varphi^*\), \(\chi\approx 0\):

\[
\Delta\mathcal{S}
=
\underbrace{\Delta_{\mathrm{II}}}_{\text{cross}}
+
\underbrace{\Delta_{\mathrm{III}}}_{\text{pure Dirac}}
+
\underbrace{\Delta_{\mathrm{IV}}}_{\text{Dirac-bracket corr.}}.
\]

### 4.1 Term (II) — cross brackets: **vanish at \(O(\psi^2)\)**

\[
\{C_g^{(\mathrm{D})}(x),\,C_f^{(\mathrm{grav})}(y)\}
=
\int\mathrm{d}z\;
\frac{\delta C_g^{(\mathrm{D})}(x)}{\delta q_f(z)}
\frac{\delta C_f^{(\mathrm{grav})}(y)}{\delta p_f(z)}
+\cdots
\]
At \(\varphi=0\) and \(O(\psi^2)\): \(\delta C_g^{(\mathrm{D})}/\delta q_f=0\). The symmetric partner \(\{C_g^{(\mathrm{grav})},C_f^{(\mathrm{D})}\}\) likewise vanishes through \(\delta C_f^{(\mathrm{D})}/\delta q_g=0\).

SVC substitution \(\varphi^*=O(\psi^2)\) corrects these functional derivatives only at \(O(\psi^4)\) (S1a corollary).

**Moreover (C1):** even if one rewrites the \(f\)-beit as \(e\cdot S\), one has \(S=e_1(S)\) — no exit from the HR polynomial class. The 3+1d Term-(II) obstruction from \(\partial S^i{}_j/\partial\gamma_{kl}^{(f)}\) **does not exist** in 1+1d.

\[
\boxed{\Delta_{\mathrm{II}}=O(\psi^4)\quad\text{(vanishes at working order).}}
\]

### 4.2 Term (IV) — Dirac-bracket corrections to grav brackets: **vanish in this setting**

\[
\Delta_{\mathrm{IV}}
=
-\{C_g,\chi_A\}\,C^{-1\,AB}\,\{\chi_B,C_f\}.
\]
Leading \(O(\psi^2)\) candidate uses \(C^{(\mathrm{grav})}\):
\[
\{C_I^{(\mathrm{grav})},\chi\}
\sim
-\{C_I^{(\mathrm{grav})},\Sigma\}\,\psi^\dagger.
\]
With topological 2D EH, \(C_I^{(\mathrm{grav})}\) is built from \(V(q_g,q_f)\) (ultralocal in the \(q\)'s) and does **not** depend on \(p_I\). Configuration–configuration Poisson brackets vanish:
\[
\{V(q),\,\Sigma(q)\}=0
\implies
\{C_I^{(\mathrm{grav})},\chi\}=0
\implies
\Delta_{\mathrm{IV}}^{(\mathrm{grav\textrm{-}grav})}=0.
\]
Mixed \(\{C^{(\mathrm{D})},\chi\}C^{-1}\{\chi,C^{(\mathrm{grav})}\}\) likewise vanishes because \(\{\chi,C^{(\mathrm{grav})}\}=0\) by the same reason.

\[
\boxed{\Delta_{\mathrm{IV}}=0\quad\text{in 1+1d (C2).}}
\]
(This channel is live in 3+1d, where \(\delta C^{(\mathrm{grav})}/\delta\pi\neq 0\).)

### 4.3 Term (III) — pure Dirac bracket: **nonzero, explicit**

Both \(C_g^{(\mathrm{D})}\) and \(C_f^{(\mathrm{D})}\) are \(p\)-independent, so the gravitational Poisson bracket vanishes. The Dirac bracket through \(\{\psi,\psi^\dagger\}_D\) remains:
\[
\Delta_{\mathrm{III}}
=
\{C_g^{(\mathrm{D})},C_f^{(\mathrm{D})}\}_D
=
\{K+M_g+\Omega_g,\;K+M_f+\Omega_f\}_D.
\]
Expand:
\[
\Delta_{\mathrm{III}}
=
\{K,K\}_D
+\{K,M_f+\Omega_f\}_D
+\{M_g+\Omega_g,K\}_D
+\{M_g+\Omega_g,\,M_f+\Omega_f\}_D.
\]

**Ultralocal mass–mass piece.** \(M_g=m\sqrt{q_g}\,\psi^\dagger\beta\psi\) and \(M_f=m\sqrt{q_f}\,\psi^\dagger\beta\psi\) are proportional to the same Clifford element \(\beta\). With \(\Sigma\propto\mathbf{1}\) at \(\varphi=0\),
\[
\{M_g,M_f\}_D=0.
\]
(Analogous vanishing for matching \(\Omega\) bilinears built from the same generator.)

**Common-kinetic piece.** \(\{K,K\}_D\) reproduces the standard 1+1d Dirac contribution to the spatial-diffeomorphism algebra:
\[
\{K(x),K(y)\}_D
\sim
\big(C_x^{(\mathrm{D})}(x)+C_x^{(\mathrm{D})}(y)\big)\,\partial_x\delta(x-y),
\]
hence **weakly zero** on \(C_x\approx 0\).

**Cross mass/connection piece — the obstruction that survives in 1+1d.**
\[
\{K,\,M_f-M_g\}_D
+
\big(\{M_g,K\}_D+\{K,M_g\}_D\big)
+
(\Omega\text{-analogues}).
\]
The single-metric-like piece \(\{M_g,K\}+\{K,M_g\}\) is the usual closure contribution of one mass sector. The **new** cross-metric piece is
\[
\{K,\,M_f-M_g\}_D,
\qquad
M_f-M_g=m\big(\sqrt{q_f}-\sqrt{q_g}\big)\,\psi^\dagger\beta\psi.
\]

Evaluating with \(\{\psi,\psi^\dagger\}_D=\Sigma^{-1}\delta\) and integrating by parts against a smear function, one obtains (distributional form):

\[
\boxed{
\begin{aligned}
\Delta_{\mathrm{III}}(x,y)
&=
\big(C_x^{(\mathrm{D})}(x)+C_x^{(\mathrm{D})}(y)\big)\,\partial_x\delta(x-y)
\\
&\quad
+\delta(x-y)\;\frac{m\big(\sqrt{q_g}-\sqrt{q_f}\big)}{\sqrt{q_g}+\sqrt{q_f}}\;
\psi^\dagger\,\Gamma\,\psi
\\
&\quad
+\delta(x-y)\;\frac{\omega_g-\omega_f}{\sqrt{q_g}+\sqrt{q_f}}\;
\psi^\dagger\,\Gamma_\omega\,\psi
\\
&\quad
+\text{(single-metric-like closure pieces weakly }\propto C_x,C_g,C_f\text{)}
\end{aligned}
}
\]
where \(\Gamma,\Gamma_\omega\) are definite (representation-dependent) hermitanized Clifford bilinears; their precise matrix form is not needed for the weak-vanishing test — only that they are not identically zero.

**Weak vanishing?** On \(C_x\approx 0\), the \(\partial\delta\) piece drops. The ultralocal remainder
\[
\Delta\mathcal{S}_{\mathrm{ultralocal}}
=
\frac{m\big(\sqrt{q_g}-\sqrt{q_f}\big)}{\sqrt{q_g}+\sqrt{q_f}}\;
\psi^\dagger\Gamma\psi
+
\frac{\omega_g-\omega_f}{\sqrt{q_g}+\sqrt{q_f}}\;
\psi^\dagger\Gamma_\omega\psi
\]
is **not** a linear combination of \(C_g,\,C_f,\,C_x\) for generic \((q_g\neq q_f,\,\psi\neq 0,\,m\textrm{ or }\partial q\neq 0)\). It vanishes on special loci (\(q_g=q_f\) with matched \(\omega\), or \(\psi=0\), or \(m=0\) with matched \(\omega\)), none of which is the full constraint surface.

\[
\boxed{\Delta\mathcal{S}=\Delta_{\mathrm{III}}\not\approx 0\quad\text{at }O(\psi^2)\text{ on the generic constraint surface.}}
\]

### 4.4 Fate of the modified secondary (1+1d algebra, not 3+1d ghost count)

Because \(\{C_g,C_f\}_D\approx\Delta\mathcal{S}\) (HR pure-grav piece weakly arranged as in the potential sector; Dirac correction as above), preservation
\[
\dot C_g=\{C_g,H\}_D\approx N_f\,\Delta\mathcal{S}+\cdots
\]
forces, for free \(N_f\), the **modified secondary**
\[
\mathcal{S}^{(\psi^2)}\;\equiv\;\Delta\mathcal{S}_{\mathrm{ultralocal}}\;\approx\;0.
\]
Its own preservation
\[
\{\mathcal{S}^{(\psi^2)},H\}_D
=N_g\{\mathcal{S}^{(\psi^2)},C_g\}_D+N_f\{\mathcal{S}^{(\psi^2)},C_f\}_D+\cdots
\approx 0
\]
is linear in the lapses. The two coefficients are generically independent functionals of \((q,\psi)\), so the equation **determines the lapse ratio** rather than imposing a tertiary constraint on the phase space.

**1+1d algebraic pattern:** modified secondary exists; preservation fixes a multiplier — the healthy second-class pattern (would be “D1-modified” if the setting were decisive for Gate 0).

---

## 5. Why this is D4, not D1 (and not D2)

| Reading | Why rejected / accepted |
|---|---|
| **D2 (ghost returns)** | Rejected as Gate-0 landing: the 1+1d algebra produces a *modified secondary with healthy preservation*, not a lost secondary that fixes a lapse *instead of* constraining phase space. Claiming W-3 from Term III alone would over-reach the 1+1d ghost count (C3) and would mis-identify a different mechanism from banked B4. |
| **D1 (ghost-free in 1+1d)** | Algebraically available as “D1-modified,” but **banned as a Gate-0 claim** by the pre-registration: B4 is invisible (C1), Term (II)/(IV) vanish for dimensional reasons (C1–C2), and AC R4 already marks 1+1d D1 as suggestive only. Landing transferable D1 here would be a **fake D1**. |
| **D4** | **Accepted.** Computation succeeded, but the setting is too simple to resolve the Gate-0 secondary-constraint question: the obstruction under test (matrix-\(S\) / polynomial-class mismatch + π-channel Dirac-bracket corrections) is specialised away. Maintain W-2; reassess setting (3+1d \(O(\psi^2)\) or a truncation that retains matrix \(S\) and DeWitt kinetics — e.g. 2+1d, or Bianchi with full spatial metric). |

**Mini-superspace:** not used. 1+1d did not block the bracket; it blocked *transfer*. Opening FLRW mini-superspace would add the further 1408.0487 caveat (FLRW-safe ≠ Bianchi-safe) without restoring matrix \(S\).

---

## 6. Net \(\Delta\mathcal{S}\) summary (for AC / Jammer)

\[
\boxed{
\begin{aligned}
&\textbf{S1a:}\quad
\varphi^*=\varphi_0-\frac{H_{\mathrm{D}}'(\varphi_0)}{V''(\varphi_0)}+O(\psi^4).
\\[6pt]
&\textbf{Lemma S1:}\quad
\Delta\mathcal{S}
=
\Delta_{\mathrm{II}}
+\Delta_{\mathrm{III}}
+\Delta_{\mathrm{IV}},
\\
&\qquad\Delta_{\mathrm{II}}=O(\psi^4),\quad
\Delta_{\mathrm{IV}}=0\ \text{(1+1d)},
\\
&\qquad\Delta_{\mathrm{III}}
=
\frac{m(\sqrt{q_g}-\sqrt{q_f})}{\sqrt{q_g}+\sqrt{q_f}}\,\psi^\dagger\Gamma\psi
+\frac{\omega_g-\omega_f}{\sqrt{q_g}+\sqrt{q_f}}\,\psi^\dagger\Gamma_\omega\psi
\\
&\qquad\qquad
+(\partial\delta\text{ diffeomorphism pieces, weakly }0).
\\[6pt]
&\textbf{On-shell:}\quad
\Delta\mathcal{S}\not\approx 0\text{ generically;}
\quad
\mathcal{S}^{(\psi^2)}\equiv\Delta\mathcal{S}_{\mathrm{ultralocal}}\approx 0
\text{ is a modified secondary}
\\
&\qquad\text{whose preservation fixes a lapse ratio (1+1d-healthy pattern).}
\\[6pt]
&\textbf{Transfer:}\quad
\text{B4 obstruction not probed (\(S\) scalar; EH topological).}
\quad
\textbf{Landing D4.}
\end{aligned}
}
\]

---

## 7. Constraint / standing reminders

- Relative boost: still auxiliary (S1a). B3 stands.
- Lapse-linearity: stands. D3 out.
- N_eff ≈ 1.52: stands. Even a transferable D1 would not restore symmetric ν.
- No κ. No f. Deposit P04. Foundation only.

---

## 8. Recommended next computation (not commissioned here)

To actually close D1 vs D2 for Gate 0, need a setting where:

1. \(S=\sqrt{\gamma_g^{-1}\gamma_f}\) is a **non-scalar matrix** (so B4 is live), and
2. gravitational kinetics are nondegenerate (so Term IV is live),

e.g. **2+1d bigravity + Dirac**, or **3+1d at \(O(\psi^2)\)** with explicit \(\Lambda^*\) and \(\delta S^i{}_j/\delta\gamma_{kl}^{(f)}\). Mini-superspace alone is insufficient (1408.0487). Requires separate Greg GO.

---

## 9. Sources

- Hassan–Rosen secondary constraint: [arXiv:1111.2070](https://arxiv.org/abs/1111.2070)
- Vierbein bigravity / SVC: [arXiv:1203.5783](https://arxiv.org/abs/1203.5783)
- Doubly-coupled scalar ghost; FLRW ≠ Bianchi: [arXiv:1408.0487](https://arxiv.org/abs/1408.0487)
- Nelson–Teitelboim 1978 (Dirac canonical gravity) — background
- Prior Scratch banked results: secondary-constraint D4 lean D2 (2026-10-09); ADM/N_eff (2026-10-08)

All constructive claims in §§1–6: **ORIGINAL WORK.**

— Scratch, 2026-10-09. Filed after pre-registration. Blind to Jammer S1 attack files.
