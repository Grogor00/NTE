# Round 5 — X-polynomial absorption identity: VERDICT (Cursor Main)

> **AC R5 AMENDMENT (2026-10-20): G-2 NOT RATIFIED. Project returns to G-4.**  
> Kill 2 misframed; Scratch identity mis-staged (Ṡ vs Ċ); covector channel \(R_i D n\) in primary uncomputed.  
> 90/90 **struck**. This filing stands as a **refutation of a mis-posed X-only identity**, not as a terminal ghost fork.  
> See `Handoffs\RULING_AC_Round5_G2_Not_Ratified_Return_To_G4_…_20261020.md`.

**Landing (lane, superseded):** G-2 (computational) — **not project-ratified**.  
**Engine:** NumPy (+ SymPy claimed; SymPy not run in filed script).  
**Script:** `Working\Opsi2_Round5_X_Identity_COMPUTE_CursorMain.py`  
**Results JSON:** `Working\Opsi2_Round5_X_Identity_COMPUTE_RESULTS.json`  
**Greg auth:** compute-narrow directive 2026-10-19.  
**No Core. No f.** Distinct from withdrawn R4 empty-locus G-2.

---

## 0. Object

Scratch R4 identity (schematic):
\[
L\,D^i{}_j(X)\,n^j\,M(X) \;=\; -\,h_g(I-X)^2
\]
(and Jammer θ-target \(h_g(\theta_g I-\theta_f X)^2\)).  
HR inputs: \(D=\sqrt{\gamma^{-1}fQ}\,Q^{-1}\), \(Q=xI+nn^{T}f\) ([1109.3515](https://arxiv.org/abs/1109.3515) (20)–(21)); minimal \(n\) from (24).

---

## 1. What was computed (repeated probes)

| Probe | Result |
|---|---|
| \(n=0\Rightarrow D=X\); \(Dn=0\); \(\|R_{\mathrm{AC}}\|>0\) for \(\lambda\neq1\) | Pass / identity fails as matrix eq |
| SymPy: \(X=\mathrm{diag}(1,1,\lambda)\) ∝ \((I-X)^2\)? | **Impossible** (\(R_{11}=0\), \(X_{11}=1\)) |
| SymPy: \(X\) ∝ \(R_\theta\)? | **No** — \(a_{11}\neq a_{33}\) by \((l^2+l+1)/(l-1)^2\) |
| Linear response: need \(X\propto R\) for \(Dn\sim XP\) to track \(RP\) | min rel err \(>0.34\) (θ), \(>0.42\) (AC) |
| Mean angle \(XP\) vs \(RP\) | up to \(60^\circ\) (AC), \(29^\circ\) (θ) |
| Explicit random \((h_g,h_f,R_g,P)\): \(\lvert\cos\rvert\) median | \(\sim 0.35\)–\(0.38\) (not aligned) |
| Fit scalar on \(P_1\), transfer to \(P_2\) | **90/90 fail** (AC and θ) |
| \(n\) function of \(X\) only? | **No** — same \(X\), different \(R_g\Rightarrow\) different \(n\) |
| Rank \(R_{\mathrm{AC}}\) anisotropic | **1** (only one axis); \(X\) rank 3 |

Re-runs: suite + symbolic + cross-\(P\) adversarial all agree. No seed / \(\lambda\) rescue off the proportional locus.

---

## 2. Structural kills (independent of numerics)

1. **Premise false:** \(n^j=n^j(\gamma,\pi)\) from (24), not \(n(X)\). LHS is π-dependent; RHS is not. An “X-only identity” cannot hold on an open set of phase space.
2. **Type mismatch:** \(\{\mathcal{S},(LDn)C_i\}=L(Dn)^i\partial_i\mathcal{S}\) is a **scalar** density (lapse equation). \(R_j\) is a **3-covector** ∂δ coefficient in \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\). A scalar cannot cancel three independent residual components.
3. **Rank / anisotropy:** even treating the schematic as “\(Dn\parallel Rp\) for all \(P\)”, need the linear response ∝ \(R\). With \(n\sim P\) and \(D\approx X\), need \(X\propto R\) — false for anisotropic \(X\) (symbolic).

Proportional \(X=cI\) can match scalars (special locus). **F1:** not decisive for health; anisotropic continuum is the generic case and fails.

---

## 3. Fork *(lane claim — superseded by AC R5 → project G-4)*

| Fork | Status |
|---|---|
| G-1 | Lane-closed on mis-posed identity only — **not project-closed** |
| G-2 | Lane-landed — **not ratified** |
| **G-4** | **Project position** (AC R5 / Jammer V3) |

**K0′:** minimal-model \(D(n)\), \(n(R)\) and \(n=0\) reduction used explicitly (1111.2070 / 1109.3515). Full non-minimal \(\beta_2,\beta_3\neq0\) \(n\) is not closed-form in HR; obstruction (π-dependence + type/rank) does not use minimality of \(n\), only that \(n\) solves \(C_i(\pi,n)=0\).

**F6:** Grassmann/spin in \(M(X)\) — if \(M\) is any ultralocal matrix, \(\partial_i(\psi^\dagger M\psi)\) still yields a scalar when contracted with \((Dn)^i\). Does not restore three ∂δ components.

**θ (F16):** tested; fails the same way.

---

## 4. Relation to R4 withdrawal

R4 G-2 used an **empty locus** (\(n=0\) with \(P\neq0\)) — correctly withdrawn.  
R5 originally claimed independence via on-shell \(n(\pi)\) / type / rank — **AC/Jammer: not independent** (θ-test linearises at \(n=0\); kill 2 misframed; object mis-staged).

---

## 5. Standing

**Superseded by AC R5:** Action (N) ghost status **undetermined** (return to G-4). This file refutes a mis-posed X-only identity; it does **not** close absorption via the correctly staged \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\) channel.  
Healthy couplings **S1–S4** remain available regardless. P04 unchanged. No Core. Round 6 needs Greg’s GO.

— Cursor Main, 2026-10-19. (Round 5, computational; AC-amended 2026-10-20.)
