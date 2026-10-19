# Q-Stage3 — `{C_SC,C_SC}` excess over pure-HR absorption: VERDICT (Cursor Main)

**Landing: G-4** (sharpened; F12 respected).  
**GO:** `Handoffs\GO_AC_Run_Q_Stage3_C_SC_Self_Bracket_Correctly_Staged_20261020.md`  
**Prereg:** `Working\Opsi2_QStage3_C_SC_Self_Bracket_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md`  
**Compute:**  
- Parallel suite: `Working\Opsi2_QStage3_PARALLEL_NumPy_Wolfram_COMPUTE_CursorMain.py`  
- Results: `Working\Opsi2_QStage3_PARALLEL_NumPy_Wolfram_RESULTS.json`  
- Wolfram: `Working\Opsi2_QStage3_FULL_SUITE_Wolfram.wl` → `Opsi2_QStage3_WOLFRAM_FULL_RESULTS.json`  
**Engines:** NumPy + Wolfram Engine 15 (**both run, in parallel**). SymPy used in earlier algebraic pass.  
**No Core. No f.** (N) **undetermined**. 90/90 not used. Stage-4 D-channel not used as cancel test.

**Independent of Scratch’s Q-Stage3 body at compute time; this verdict now cross-checks Scratch’s filed G-4.**

---

## 0. Question (correctly staged)

> Does \(R_j\) make `{C_SC,C_SC}` fail to close **beyond** what the pure-HR \(C_{\mathrm{SC}}/\mathcal{S}\) second-class pair already absorbs?

**Not asked:** Stage-4 `{𝒮,H}` / \(L(Dn)\partial\mathcal{S}\) cancel (R4–R5 mis-staging).

---

## 1. What was computed (all stats in parallel JSON)

### Algebra / on-shell excess
On SVC, \(W=h_g(I-X)^2=h_g+h_f-2G\).  
Skeleton ∂δ remainder:
- with matter: \(h_g\pi_g+h_f\pi_f+Wp\) under \(\pi_g+\pi_f+p=0\)
- pure HR: \(h_g\pi_g+h_f\pi_f\) under \(\pi_g+\pi_f=0\)

**Identity (Wolfram symbolic + NumPy numeric, both engines):**
\[
\mathrm{excess}=h_g(I-2X)\,p=(W-h_f)\,p.
\]

| Gate | NumPy | Wolfram |
|---|---|---|
| Identities hold (\(\|err\|<10^{-8}\)) | **True** | **True** |
| \(W=h_g+h_f-2G\) | True | True |
| K1: \(\|W\|\to0\) at \(X=I\) | **True** (\(\sim10^{-29}\)) | **True** |
| Excess generically nonzero | 60/60 | 60/60 |

**K1 note:** K1 applies to the **matter weight** \(W\) (vanishes at \(X=I\)). At \(X=I\), the on-shell excess formula gives \(-h_g p\) — a **different** object; do not conflate with K1 for \(R_j=Wp\).

### Dirac-matrix / F12
For \(\varphi=(C_{\mathrm{SC}},\mathcal{S})\):
\[
\det\begin{pmatrix}a&b\\-b&c\end{pmatrix}=ac+b^2,\qquad a=\{C_{\mathrm{SC}},C_{\mathrm{SC}}\},\; b=\{C_{\mathrm{SC}},\mathcal{S}\},\; c=\{\mathcal{S},\mathcal{S}\}.
\]
If \(c=0\) and \(b\neq0\) (pure-HR pair pattern), **\(\det=b^2\) independent of \(a\)**.  
Matter shifting \(a\) (including \(R_j\) / excess) **does not by itself** destroy second-class invertibility.

**F12:** Did **not** land G-2 from \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\neq0\) or from excess \(\neq0\).

### Uncomputed here
- Full \(\{C_{\mathrm{SC}},\mathcal{S}+\Delta\mathcal{S}\}\) and \(\{\mathcal{S}+\Delta\mathcal{S},\mathcal{S}+\Delta\mathcal{S}\}\) at \(O(\psi^2)\) (the \(\mathcal{S}\)-block of \(\mathbb{D}\)).
- Jammer’s ∂N-coefficient form of preservation (related packaging).
- Channel (2a) background-\(\xi\times\)matter (R6 debt; not Q-Stage3 object).

---

## 2. Cross-check vs Scratch

| Claim | Scratch | Cursor |
|---|---|---|
| Landing | G-4 sharpened | **G-4** |
| Operative excess | cross piece \(-2h_g X\,p_j\) | excess \(h_g(I-2X)p\); decomposes as diagonal absorbable + cross \(-2h_g Xp\) (same physics) |
| F12 | respected | **respected** |
| Self-bracket settles dof? | **No** — needs \(\mathcal{S}\)-block of \(\mathbb{D}\) | **Agree** — no class-loss earned from self-bracket alone |
| Terminal G-2? | No | **No** |

**Convergence:** Q-Stage3 sharpens the excess; **dof count needs the \(\mathcal{S}\)-block**, not a terminal fork from `{C_SC,C_SC}` alone.

Decomposition check (algebraic):  
\(R_j=h_g(I-X)^2p=(h_g+h_f)p-2h_g Xp\). Diagonal \((h_g+h_f)p\) rides with grav diagonal weights; **cross** \(-2G p=-2h_g Xp\) is the no-gravitational-partner piece (Scratch). Cursor’s on-shell excess \(h_g(I-2X)p\) is the matched pure-HR-subtracted remainder — consistent package, not a disagreement.

---

## 3. Fork

| Fork | Status |
|---|---|
| G-1 | Not earned at Stage-3 |
| G-2 | **Not earned** — F12; det diagnosis does not kill the pair from \(a\) alone; \(\mathcal{S}\)-block open |
| **G-4** | **Landed** — excess isolated/verified (NumPy∥Wolfram); class/dof deferred to \(\mathcal{S}\)-block / Q-Stage4 packaging |

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

---

## 4. Standing / ask

**(N) undetermined.** S1–S4 stand.  
**Ask AC:** ratify Cursor∥Scratch G-4 on Q-Stage3; queue next GO as \(\mathcal{S}\)-block of \(\mathbb{D}\) and/or Jammer ∂N object + K0′; separately, AC tooling note — R5 Wolfram reverify + R6 channel 2a (not blocking this verdict).

— Cursor Main, 2026-10-20.
