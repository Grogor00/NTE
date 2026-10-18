# Verification audit — Opsi2 / Claim-3 chain (Cursor Main)

**Greg ask:** verify all work so far; double-check no prior external working; look for valid solutions.  
**Date:** 2026-10-19. **No Core.**

---

## 1. Prior art — what exists vs what does not

### 1.1 No prior: naive double-kinetic Dirac DB chain (action N)

Re-searched this session (arXiv / web). **No paper** runs the full Dirac–Bergmann / ADM constraint algebra for
\[
S_\psi=\int\sqrt{|g|}\,\bar\psi\,i\gamma_e\!\cdot\!D_e\psi+\int\sqrt{|f|}\,\bar\psi\,i\gamma_f\!\cdot\!D_f\psi
\]
(one spinor, two independent first-order kinetics on two dynamical vierbeins) to a terminal fork.

| Source | Couples | Does the Opsi2 chain? |
|---|---|---|
| dRHR [1408.1678](https://arxiv.org/abs/1408.1678) | Same species, two metrics — **ghost at classical level** (scalars / generic; MSS + loops) | **No Dirac ADM** |
| Yamashita–De Felice–Tanaka [1408.0487](https://arxiv.org/abs/1408.0487) | Scalar double kinetic → BD | Scalars only |
| Melville–Noller [1408.5131](https://arxiv.org/abs/1408.5131), [1511.01485](https://arxiv.org/abs/1511.01485) | **One** effective vielbein \(\tilde e\); Dirac in MSS; rank-2 healthy | **Not (N)** |
| Hassan–Kocic–Schmidt-May [1409.1909](https://arxiv.org/abs/1409.1909) | Composite \(G_{\mu\nu}\); fermions via vierbein of \(G\), linear in \(N_{\mathrm{eff}}\) | **Not (N)** |
| Hinterbichler–Rosen [1503.06796](https://arxiv.org/abs/1503.06796) | Linear composite vielbein | **Not (N)** |
| AKMS [1306.0004](https://arxiv.org/abs/1306.0004) | Doubly coupled scalars / particles | No Dirac |
| HR secondary [1111.2070](https://arxiv.org/abs/1111.2070) | Pure gravity | K0 control only |

**Verdict:** prior art **kills double kinetic for scalars/generic matter** and supplies **healthy alternatives**; it does **not** pre-empt the Dirac-specific O(ψ²) bracket chain. Corpus prior-art fetch stands. Original-work register for (N) still holds.

### 1.2 Valid solutions that already exist (not action N)

These are healthy / candidate-healthy couplings — **they are not “solutions to (N)”**; they replace (N):

1. **Single-metric Dirac** — couple ψ to \(g\) only (or a separate species to \(f\)). Ghost-free with HR.
2. **Effective / composite vielbein** (Melville–Noller rank-2; Hassan \(G_{\mu\nu}\); Hinterbichler–Rosen \(\tilde e=e+\alpha\bar e\)) — one kinetic term on \(\tilde e[e,f]\). MSS healthy for Dirac (MN).
3. **Independent species** — \(\chi_g\) on \(g\), \(\chi_f\) on \(f\), no shared ψ.

**No verified healthy solution for naive double-kinetic Dirac (N) appears in the literature or in this chain.**

---

## 2. Algebra re-check (this session)

| Claim | Status |
|---|---|
| \(G=h_g X\), \(h_f=h_g X^2\) on SVC | Holds (eigendecomposition checks) |
| Perfect square \(w_g^2 h_g-2w_g w_f G+w_f^2 h_f=h_g(w_g-w_f X)^2\) | **50 random SPD pairs, max rel err \(\sim10^{-14}\)** |
| \(D\|_{n=0}=X\) from 1111.2070 (7)–(8) | **Verified** |
| K1: residual vanishes at \(X=I\) | **Yes** (AC and θ forms) |
| Jammer θ-correction: \(R=h_g(\theta_g I-\theta_f X)^2 P\) ≠ AC \(h_g(I-X)^2 p\) off \(X=I\) | **Confirmed** (\(\lambda=1.8\): \(\|R_{\mathrm{AC}}-R_\theta\|\approx0.115\)) |
| χ depends on both vierbeins → B1 Dirac ≠ Poisson | **Structurally sound** (F14 accept correct) |
| B1 ∂δ ~ \((ψ†αψ)π_f\) not \(W·P\) | **Plausible / schematic** (Jammer: register “established” too strong; F6) |

---

## 3. Chain audit by round

| Round | Cursor | Scratch | AC / Jammer | Verify note |
|---|---|---|---|---|
| R1 | G-4 | G-4 | G-4 OK | Matter cross carries \(G\) |
| R2 | G-4; freeze omitted χ | G-4; χ mixes sectors | Jammer: Scratch right; F14 | **Cursor error cured** |
| R3 | G-4; \(R_j\); B1≠\(W·p\) | G-4; \(R_j=h_g(I-X)^2 p\) | Ratified \(R_j\); AC typo \(I-X^2\) corrected | **θ-weights missed** (Jammer Phase-2) — both lanes + AC form incomplete |
| R4 | **G-2** (n=0: D ultralocal only) | **G-4** (live channel \(L Dn\,\partial\mathcal{S}\); X-identity) | Await | **LANES DIVERGE** |

---

## 4. Round-4 divergence — stress-test of Cursor G-2

Scratch’s live channel (not used in Cursor R4):
\[
\{\mathcal{S}^{(\psi^2)},(L D^i{}_j n^j)C_i\}=L D^i{}_j n^j\,\partial_i\mathcal{S}^{(\psi^2)},
\]
with \(\partial(\psi^\dagger M\psi)\) **p-structured**. So “ultralocal secondary ⇒ no ∂δ absorption” is **false** (F12 concrete).

**Hole in Cursor G-2:** Lemma R4 treated \(D\) at \(n=0\) as only inside \(V\) (ultralocal) and concluded non-absorption. That **misses the multiplier channel** in \(H\). On \(n=0\) that channel is off; on generic on-shell \(n\neq0\) it is live. Landing G-2 from the \(n=0\) locus alone is **too strong** (F1 / incomplete K3).

**Hole in claiming G-1:** Scratch’s X-identity is **unevaluated**; K0′ incomplete. G-4 is the honest Scratch ceiling.

**Audit verdict on Cursor R4 G-2:** **withdraw as terminal landing**; reclassify as **G-4 with sharpened objection** pending evaluation of
\[
L\,D(X)\,n(X)\,M(X)\;\stackrel{?}{=}\;-h_g(w\theta\text{-corrected }X\text{ residual})
\]
(or AC form). Matches AC’s “terminal or new reason” bar the way Scratch used it.

---

## 5. Valid solution search — summary

| Candidate | Status for Claim-3 / (N) |
|---|---|
| Naive double-kinetic Dirac (N) | **No healthy solution found**; literature generic-matter no-go + this chain’s residual both point ghostward; **Dirac terminal fork not closed** (R4 divergence) |
| Effective vielbein / composite \(G\) | **Valid known route** (not (N)) |
| Single-metric or split species | **Valid known route** |
| Cursor R4 G-2 as published terminal | **Not yet earned** — channel hole |
| Scratch R4 X-identity → G-1 | **Open**; checkable next |

---

## 6. Corrections Cursor should bank

1. **Withdraw terminal G-2** pending X-identity / multiplier-channel check (amendment).
2. **Adopt Jammer θ / F16** before any further absorption test.
3. **Withdraw “w=1 forced by K1”** (F17) — already in Jammer; AC should amend.
4. Prior art: cite dRHR double-kinetic **scalar/generic** no-go as cousin, not as pre-emption of Dirac ADM.

---

## 7. Standing

Claim 3 / (N) **still not established** as a healthy theory.  
P04 unchanged. No Core.  
**Await AC on Round-4 lane split** (Cursor G-2 vs Scratch G-4).

— Cursor Main, 2026-10-19.
