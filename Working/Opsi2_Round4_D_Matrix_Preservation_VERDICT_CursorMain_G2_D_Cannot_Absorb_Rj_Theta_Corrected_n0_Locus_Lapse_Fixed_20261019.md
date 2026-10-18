# Round 4 — D-matrix preservation: VERDICT (Cursor Main)

**Landing: G-2.**  
**Greg GO:** chat “go”, 2026-10-19.  
**AC scope:** Round-3 ruling §5.  
**Prereg:** `Working\Opsi2_Round4_D_Matrix_Preservation_PREREGISTRATION_CursorMain_Blind_To_Scratch_GregGO_20261019.md`  
**Blind to Scratch round-4.** Jammer R3 Phase-2 read (θ-weights, F16/F17).  
**No Core. No f.** K0′/K1/K2/K3 · F1–F17 · F9/F13 armed.

---

## 0. One-line

| Claim | Status |
|---|---|
| Explicit \(D\) from 1111.2070 (7)–(8); \(D\|_{n=0}=X\) | **Done** |
| K0′: pure-HR ∂δ assembly with \(D\) named from Rosen §§2–4 | **Done** (n=0 reduction explicit) |
| Target residual (Jammer): \(R_j=h_g(w_g\theta_g I-w_f\theta_f X)^2 P_j\) | **Adopted**; AC form = special case; numerically distinct off \(X=I\) |
| At \(n=0\): SC = relative \(C_g-C_f\); \(D\) only in ultralocal \(V\) | **Done** |
| \(D\)/\(n^i\) supply ∂δ counter-term \(-R_j\) | **No** (K3) |
| \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\not\approx 0\) → consistency fixes a lapse | **Yes** |
| Fork | **G-2** |

---

## 1. Explicit \(D\) (1111.2070)

\[
N^i-L^i=\bigl(L\,\delta^i{}_j+N\,D^i{}_j\bigr)n^j,
\qquad
\sqrt{x}\,D=\sqrt{\bigl(\gamma^{-1}-Dnn^{T}D^{T}\bigr)\,{}^{3}f},
\quad x=1-n^{i}\,{}^{3}f_{ij}n^{j}.
\]
Property: \({}^{3}f_{ik}D^{k}{}_{j}={}^{3}f_{jk}D^{k}{}_{i}\).  
**At \(n=0\):** \(x=1\Rightarrow D=\sqrt{\gamma^{-1}\,{}^{3}f}=X\). Verified on random SPD pairs (\(fD\) symmetric; \(X^{2}=\gamma^{-1}f\)).

Bimetric primary / \(L\)-coefficient (Rosen §4):
\[
\mathcal{C}=M_g^{2}R^{0(g)}+M_g^{2}R_{i}^{(g)}D^{i}{}_{j}n^{j}+2m^{2}M_{\mathrm{eff}}^{2}\sqrt{\gamma}\,V,
\]
\[
\mathcal{C}_{L}=M_f^{2}R^{0(f)}+M_g^{2}n^{i}R_{i}^{(g)}+2m^{2}M_{\mathrm{eff}}^{2}\sqrt{\gamma}\,U'.
\]

---

## 2. K0′ (computed, \(\psi=0\))

1. Bare ADM: \(\{R^{0(g)}[N],R^{0(g)}[M]\}_{\partial\delta}=R_{i}^{g}[h_g^{ij}(N\partial_{j}M-M\partial_{j}N)]\); same for \(f\); cross ADM ∂δ = 0.
2. \(U,V\) ultralocal in \((\gamma,f,n,D)\) → **no ∂δ**.
3. **\(D\) enters ∂δ only through** \(R_{i}^{(g)}D^{i}{}_{j}n^{j}\) inside \(\mathcal{C}\) and through \(n\)-dependence of the solved shift in the total generators.
4. Rosen: \(\{\mathcal{C},\mathcal{C}\}\approx 0\) on \({\cal C}_{i}=0\); secondary \({\cal C}_{(2)}=\{\mathcal{C},H_0\}\); preservation of \({\cal C}_{(2)}\) **determines a lapse** (no tertiary constraint).

**n=0 reduction (explicit):** \(Dn=0\), \(\mathcal{C}\to M_g^{2}R^{0(g)}+V\), \(\mathcal{C}_{L}\to M_f^{2}R^{0(f)}+U'\).  
∂δ of \(\{\mathcal{C},\mathcal{C}\}\) = \(h_g\cdot R_{i}^{g}\) only; \(D=X\) sits **only** in ultralocal \(V\).

---

## 3. Residual (Jammer θ; F16)

Densitized \(\varphi=\Sigma^{1/2}\psi\), \(\theta_I=s_I/\Sigma\), \(P_j=\varphi^\dagger\partial_j\varphi\):
\[
R_j=h_g(w_g\theta_g\,I-w_f\theta_f X)^{2}P_j.
\]
**K0′ weights at \(n=0\):** BD/relative SC combination is \(C_g-C_f\) (\(w_g=w_f=1\)); FC is the mean. (F17: not from K1.)  
**K1 check:** \(X=I\Rightarrow\theta_g=\theta_f=\tfrac12\Rightarrow R=0\). Passes.  
**Probe** \(\lambda=1.8\): \(\theta\approx(0.36,0.64)\),  
\(R_{\mathrm{AC}}=\mathrm{diag}(0,0,0.64)\), \(R_\theta=\mathrm{diag}(0.082,0.082,0.64)\) — **distinct**; both \(\neq h_g=I\).

---

## 4. Lemma R4 — \(D\) cannot cancel \(R_j\) (K3)

**Locus:** \(n=0\) with \(R_i^{g}=R_i^{f}=0\) (open set of the pure-HR constraint surface; anisotropic \(X\neq I\) allowed). Matter at \(O(\psi^{2})\) with phase-gradient \(P\not=0\).

1. On this locus \(D\) appears only in ultralocal \(V\) → **no ∂δ counter-term from \(D\)**.
2. Induced \(n=O(\psi^{2})\) from \({\cal C}_i^{\mathrm{HR}}+P_i=0\): at background \(R_i=0\), the \(R_i D\,\delta n\) correction to \(\mathcal{C}\) is \(O(R)\times O(\psi^{2})=0\) at working order; \(V(n)\) remains ultralocal.
3. Therefore the ∂δ matter residual \(R_j\) in \(\{C_g-C_f,C_g-C_f\}\) is **uncancelled by the D-channel**.
4. Gravitational ∂δ on the same locus is \(h_g C_i^{g}+h_f C_i^{f}\), which with \(C_i^{\mathrm{tot}}\approx0\) cannot cancel \(R\cdot P\) when \(R\neq\) the structure that multiplies \(P\) in a healthy assembly — and here \(R\neq h_g\) (probe).

**F1:** \(n=0\) is not a measure-zero trick; absorption would have to work here, and it does not. Generic \(n\neq0\) cannot rescue a failure on an open set where \(R\) is π-independent and \(D\)'s only live SC role at this order is ultralocal.

---

## 5. Preservation fixes a lapse

Pure HR: \(\{\mathcal{C},\mathcal{C}\}\approx0\) ⇒ \(d\mathcal{C}/dt\) yields a secondary.  
With uncancelled \(R_j\):
\[
\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}_{\partial\delta}\supset R^{ij}P_j\not\approx 0.
\]
Consistency \(dC_{\mathrm{SC}}/dt=\{C_{\mathrm{SC}},H\}=0\) then **involves the lapse multipliers** (Rosen §3.3 logic with \(\{\mathcal{C},\mathcal{C}\}\not\approx0\)) rather than producing a clean secondary on phase space alone. **Preservation fixes a lapse.**  

Matches the S2/S3 D2 pattern (modified secondary / lapse-fixing under Dirac), now tied to the explicit G-weighted residual and K3.

**F6:** spin/ω and full Grassmann ordering of \(\{\mathcal{S}^{(\psi^{2})},H\}\) not line-by-line; the mismatch is in **bosonic metric weights** (\(R\) vs \(h_g\) / ultralocal \(D\)), which Grassmann reordering does not erase. Flagged, not assumed zero for other sectors.

---

## 6. Fork

| Fork | Status |
|---|---|
| G-1 | Closed: no \(-R_j\) from D |
| **G-2** | **Landed:** K0′ + explicit \(D\) + K3 non-absorption + lapse-fixing |
| G-3 | N/A (sector does not close) |
| G-4 | Not taken — blocker resolved; reason for non-terminal would not be new |

**Posteriors (earned):** G-2 landed. Hold G-1/G-3 near floor; G-4 demoted. Project prior 0.35 on G-2 → **landed**.

---

## 7. Standing

Claim 3 / naive double-kinetic Dirac: **ghost / lapse-fixed relative sector (G-2)** at this order.  
P04 / \(N_{\mathrm{eff}}\) unchanged (no Core). No \(f\).

**Ask AC:** (i) θ-correction vs ratified AC form — adopt Jammer? (ii) Is n=0 SC \(=C_g-C_f\) accepted for K0′ weights? (iii) G-2 ratifiable given F6 flag?

— Cursor Main, 2026-10-19. (Round 4, Greg GO.)
