# Round 2 — G-weighted ∂δ: VERDICT (Cursor Main, second lane)

**Landing: G-4 (sharpened).**  
**GO:** `Handoffs\GO_AC_Round2_G_Weighted_ddelta_Sector_…_20261019.md`  
**Prereg:** `Working\Opsi2_Round2_G_Weighted_ddelta_PREREGISTRATION_CursorMain_…_20261019.md`  
**Blind to Scratch round-2.** M1 not revived. **No Core. No f.** K0/F1–F9 binding; **F9 armed.**

---

## 0. One-line

| Claim | Status |
|---|---|
| \(G^{ij}p_j\) appears in matter cross-bracket ∂δ (round-1 object) | Carried forward (not re-derived from Scratch) |
| \(G\notin\mathrm{span}\{h_g,h_f\}\) as operators on \(p\) when \(e\neq f\) | **Established** (explicit continuum config) |
| Same-metric ED crosses \(\{C_g^{\mathrm{EH}},C_g^{(D)}\}\) cancel **G** | **No** — they never see mixed-frame \(G\) |
| Ultralocal HR potential \(V[\gamma_g,\gamma_f]\) PBs with \(C_f^{(D)}\) | **Vanishes** (both configuration-side; no \(\pi\)) |
| Gravity–matter **cross-metric** ∂δ via live \(n^i\) and \(\Lambda_{\mathrm{rel}}\) cancels \(G\cdot p\) | **Uncomputed** ← sharpened blocker |
| Shift absorbs \(G\cdot p\) | **Not shown;** shifts multiply total \(C_i\), not a free \(G\)-channel |
| Fork | **G-4** (not G-2: F9 — assembly through auxiliaries still open) |

---

## 1. Setup (action N, \(O(\psi^2)\))

\[
C_g=C_g^{(0)}+C_g^{(D)},\quad
C_f=C_f^{(0)}+C_f^{(D)},\quad
C_g^{(0)}=C_g^{\mathrm{EH}}+C_g^{\mathrm{pot}},
\]
and likewise for \(f\). Matter Hamiltonians \(C_g^{(D)}=\psi^\dagger K_g\psi\), \(C_f^{(D)}=\psi^\dagger K_f\psi\) with shared symplectic factor \(\Sigma=\Sigma_g+\Sigma_f\).

Round-1 / Jammer synthesis (adopted as the object of this round, not re-proven here): the ∂δ sector of the **matter cross-bracket** \(\{C_g^{(D)},C_f^{(D)}\}\) carries
\[
\rho^i = G^{ij}p_j,\qquad G^{ij}=e_a{}^i f^{aj},
\]
with \(p_j\) the canonical Dirac momentum density. Pure HR produces only \(h_g\)- and \(h_f\)-weighted gravitational momenta.

---

## 2. Lemma R2-A — \(G\notin\mathrm{span}\{h_g,h_f\}\) when \(e\neq f\)

**Config (continuum, not MSS-decisive):**  
\(\gamma_g=\delta_{ij}\), \(\gamma_f=\mathrm{diag}(1,1,\lambda^2)\) with \(\lambda\neq 1\), aligned boost \(\Lambda_{\mathrm{rel}}=1\), dreibeine \(e_a{}^i=\delta_a{}^i\), \(f_a{}^i=\mathrm{diag}(1,1,\lambda)\).

Then \(h_g^{ij}=\delta^{ij}\), \(h_f^{ij}=\mathrm{diag}(1,1,\lambda^{-2})\), and
\[
G^{ij}=\sum_a e_a{}^i f_a{}^j=\mathrm{diag}(1,1,\lambda).
\]

Suppose \(G\cdot p=\alpha\,h_g\cdot p+\beta\,h_f\cdot p\) for all \(p\). Then
\[
\alpha+\beta=1\quad(i=1,2),\qquad
\alpha+\beta\lambda^{-2}=\lambda\quad(i=3).
\]
These are incompatible for \(\lambda\neq 1\). **Hence \(G\notin\mathrm{span}\{h_g,h_f\}\).**

**Consequence for B3:** any HR assembly that cancels only \(h_g\)- and \(h_f\)-weighted ∂δ currents **cannot** cancel a residual proportional to \(G\cdot p\) by re-using the pure-HR identities. A counter-term must come from somewhere new — the gravity–matter crosses (B1/B2) or a shift channel that sees \(G\) explicitly.

---

## 3. Lemma R2-B — where B1/B2 can and cannot act

### 3.1 Same-metric crosses (do not touch \(G\))

\(\{C_g^{\mathrm{EH}},C_g^{(D)}\}\) and \(\{C_f^{\mathrm{EH}},C_f^{(D)}\}\) are the Einstein–Dirac cross terms that, in **single-metric** theory, help assemble \(\{C,C\}_{\partial\delta}\) onto the **total** \(C_i\) for that metric. They involve one dreibein only. They **cannot** produce a mixed-frame \(G^{ij}p_j\) counter-term in \(\{C_g,C_f\}\).

### 3.2 Ultralocal potential

\(C_g^{\mathrm{pot}}\) (HR \(V[\gamma_g,\gamma_f,n]\), configuration dependence aside from \(n^i[\pi]\)) has vanishing Poisson bracket with \(C_f^{(D)}[\psi,\gamma_f]\) when both sides are evaluated as functionals of configuration variables alone:
\[
\{V[\gamma],\,C_f^{(D)}[\gamma,\psi]\}=0
\]
because neither side involves the conjugate momenta that generate \(\{\gamma,\pi\}\) brackets into the other. **The potential does not, by itself, cancel \(G\cdot p\).**

### 3.3 Cross-metric gravity–matter — the open half

The candidates for a \(G\)-counter-term are
\[
\{C_g^{\mathrm{EH}},C_f^{(D)}\},\quad
\{C_g^{(D)},C_f^{\mathrm{EH}}\},
\]
and the same with \(\mathrm{pot}\) after including **live** dependence of \(n^i\) and \(\Lambda_{\mathrm{rel}}\) on the phase space.

**Leading freeze:** if \(C_f^{(D)}\) is treated as independent of \((\gamma_g,\pi_g)\) and \(C_g^{(D)}\) as independent of \((\gamma_f,\pi_f)\), then
\[
\{C_g^{\mathrm{EH}},C_f^{(D)}\}=0,\qquad
\{C_f^{\mathrm{EH}},C_g^{(D)}\}=0
\]
at that freeze — so **no** counter-term.

**Thaw:** \(C_{g,f}^{(D)}\) depend on \(\Lambda_{\mathrm{rel}}\), and after HR reduction \(n^i=n^i(\gamma,\pi)\) (and, with matter, \(n^i\) eom pick up \(O(\psi^2)\) corrections). Then
\[
\{C_g^{\mathrm{EH}}[\pi_g],\,C_f^{(D)}[\Lambda_{\mathrm{rel}}(n[\pi]),\psi]\}
\]
can be nonzero. **This continuum evaluation is B1/B2 and is not completed in this filing.**

---

## 4. Shifts

Diagonal shift multipliers enforce total \(C_i=C_i^{(g)}+C_i^{(f)}+C_i^{(\psi)}\approx 0\). That constrains one linear combination of momentum densities. It does **not** automatically set \(G^{ij}p_j=0\) when \(G\notin\mathrm{span}\{h_g,h_f\}\) relative to the combinations already used by the lapse-weighted preservation equation. **Absorption by shifts is not established;** ruling it out completely wants the same B1–B3 assembly written with smeared multipliers (still open).

---

## 5. What was computed vs blocked

| ID | Item | Status |
|---|---|---|
| R2-A | \(G\notin\mathrm{span}\{h_g,h_f\}\) (\(e\neq f\)) | **Done** |
| R2-B1 | Same-metric crosses cannot cancel \(G\) | **Done** |
| R2-B2 | Ultralocal \(V\) PB with \(C^{(D)}\) vanishes | **Done** |
| **B1/B2*** | Cross-metric \(\{C_g^{\mathrm{EH}},C_f^{(D)}\}\) etc. with **live** \(n^i,\Lambda_{\mathrm{rel}}\) | **Open** |
| **B3*** | Full HR lapse-weighted assembly of ∂δ including \(G\cdot p\) | **Open** (depends on B1/B2*) |
| B6/B7 | \(\{\mathcal{S}^{(\psi^2)},H\}\) | **Blocked** (sector (a) not closed) |

\* = sharpened round-2 blocker.

---

## 6. Fork and F-traps

**G-2 not claimed:** R2-A + R2-B1 + R2-B2 make G-2 *plausible* and remove the cheap “HR will eat anything \(h\)-like” hope, but the live-auxiliary cross (B1/B2*) is exactly the counter-term channel that could still save G-1. Claiming G-2 now is **F9**.

**G-1 not claimed:** no counter-term exhibited; \(\{\mathcal{S}^{(\psi^2)},H\}\) not reached.

**G-4:** yes — blocker named: **continuum evaluation of cross-metric gravity–matter ∂δ through \(n^i\) and \(\Lambda_{\mathrm{rel}}\), then HR assembly against \(G\cdot p\).**

F1: anisotropic continuum config used for R2-A, not as MSS decision. F4 K0 inherited. F8 no D2 premise. M1 not revived.

## 7. Priors

Hold project line: G-1 0.20, G-2 0.35, G-3 0.10, G-4 0.35.  
**No posterior movement** — R2-A strengthens the *motive* for G-2 but does not earn the fork.

---

## 8. Standing

Claim 3 still not established. P04 unchanged. No Core.

— Cursor Main, 2026-10-19. (Round 2, blind to Scratch.)
