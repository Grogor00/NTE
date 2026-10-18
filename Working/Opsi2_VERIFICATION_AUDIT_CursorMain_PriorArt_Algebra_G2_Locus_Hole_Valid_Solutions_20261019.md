# Verification audit — Opsi2 / Claim-3 chain (Cursor Main)

**Date:** 2026-10-19 · **No Core.**  
**Scope:** prior art; algebra re-check; Round-4 G-2 stress test; known valid solutions (not action N).

---

## 1. Prior art — naive double-kinetic Dirac DB chain

**Question:** Has anyone run Dirac–Bergmann for action (N) — *one* Dirac spinor, *two* independent first-order kinetics on two dynamical vierbeins — to a terminal fork?

| Source | Result for (N) |
|---|---|
| dRHR [1408.1678](https://arxiv.org/abs/1408.1678) | **Same species with two kinetics → BD ghost** (classical + loops). Explicit for scalars / generic matter; **not** a full ADM Dirac-bracket chain for spinors |
| Yamashita–De Felice–Tanaka [1408.0487](https://arxiv.org/abs/1408.0487) | Scalar double kinetic → ghost |
| Melville–Noller [1408.5131](https://arxiv.org/abs/1408.5131), [1511.01485](https://arxiv.org/abs/1511.01485) | **Effective** vielbein / rank-2 couplings; Dirac treated in MSS — **not** (N) |
| Hassan–Kocic–Schmidt-May [1409.1909](https://arxiv.org/abs/1409.1909) | Composite effective metric; fermions via effective vierbein, linear in \(N_{\mathrm{eff}}\) — **not** (N) |
| Hinterbichler–Rosen [1503.06796](https://arxiv.org/abs/1503.06796) | Linear composite vielbein class |
| Hassan–Rosen secondary [1111.2070](https://arxiv.org/abs/1111.2070) | Pure gravity K0 control only |
| Fresh search (Dirac/spinor + bimetric + ADM/ghost) | **No hit** that closes the O(ψ²) DB chain for two independent Dirac kinetics |

**Verdict:** No external working that *replaces* this chain for action (N).  
**But:** the *qualitative* no-go for “same field, two kinetics” is already in the literature (dRHR). Our contribution is the spinor-specific χ / θ / \(R_j\) / D-matrix narrowing — not the first observation that double kinetic is dangerous.

---

## 2. Algebra re-check (this session)

| Claim | Status |
|---|---|
| \(w_g^2 h_g - 2w_g w_f G + w_f^2 h_f = h_g(w_g - w_f X)^2\) on SVC | **Pass** (50 random SPD; max rel err \(\sim 10^{-14}\)) |
| \(D\|_{n=0}=X=\sqrt{\gamma^{-1}f}\) | **Pass** |
| K1: residual vanishes at \(X=I\) (AC and θ forms) | **Pass** |
| θ-corrected \(R_j=h_g(\theta_g I-\theta_f X)^2 P_j\) ≠ AC \(h_g(I-X)^2 p_j\) off \(X=I\) | **Pass** (\(\lambda=1.8\): \(\|R_{\mathrm{AC}}-R_\theta\|\approx 0.115\)) |
| Jammer F16/F17 (θ weights; w not forced by K1) | **Correct** — AC ratified form needs amendment |

---

## 3. Round-4 divergence and G-2 locus hole

| Lane | Landing | Claim |
|---|---|---|
| Cursor | **G-2** | At \(n=0\), \(D\) only in ultralocal \(V\); \(R_j\) uncancelled; \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\not\approx 0\) fixes a lapse |
| Scratch | **G-4** | Channel \(L D^i{}_j n^j \partial_i\mathcal{S}^{(\psi^2)}\) is live and p-structured; fork = one X-polynomial identity; K0′/identity not evaluated |

### Hole in Cursor G-2 (withdraw terminal claim)

Cursor used locus: \(n=0\), \(R_i^{\mathrm{grav}}=0\), phase-gradient \(P\neq 0\).

But \({\cal C}_i^{\mathrm{HR}}(n=0)+P_i = R_i + P_i = 0\). With \(R_i=0\) this forces **\(P_i=0\)**.  
**The locus with \(P\neq 0\) is empty.** F1 failure. G-2 as filed is **not earned**.

On consistent data, \(P\neq 0\) drives \(n=O(\psi^2)\) or uses backgrounds with \(n\neq 0\), where Scratch’s \(LDn\,\partial\mathcal{S}\) channel is live. Cursor’s ultralocal-\(V\)-only argument does not kill that channel.

**Amendment:** Cursor Round-4 terminal G-2 **withdrawn** → **G-4**, aligned with Scratch’s ceiling pending the X-identity + K0′. See companion amendment file.

---

## 4. Valid solutions (healthy alternatives — not action N)

These are externally established or standard; they solve the *physics* problem of coupling fermions in bigravity without claiming (N) is ghost-free:

| Solution | Status | Notes |
|---|---|---|
| **S1.** Dirac on **one** metric only | Healthy | HR matter proof; other metric pure gravity |
| **S2.** Rank-2 **effective vielbein** \(\tilde e = ae + b f\) (Melville–Noller / HR class) | Healthy (MSS + constraint arguments) | Gap-2 “partially addressed”; **not** naive double kinetic |
| **S3.** Composite **effective metric** \(G_{\mu\nu}\) (dRHR / Hassan et al.) | Healthy classically (debated cut-off) | Fermions via effective vierbein of \(G\) |
| **S4.** **Two species** \(\chi_g,\chi_f\) each on one metric | Healthy | Not one shared spinor |
| **S5.** Action (N) naive double kinetic | **No healthy solution found** | dRHR qualitative no-go; our chain consistent with ghost/lapse-fixing but Round-4 fork **not closed** |

**No valid G-1 solution for action (N) is on the table.** Valid solutions are **couplings other than (N)**.

---

## 5. Chain hygiene (what stands / what doesn’t)

| Item | Stands? |
|---|---|
| R1–R3: χ mixes sectors; B1 ≠ \(W\cdot P\) (schematic); perfect-square residual; F14 accept | **Yes** (with θ correction) |
| AC R3 ratification of \(R_j=h_g(I-X)^2 p_j\) | **Needs θ amend** (Jammer) |
| Cursor R4 G-2 | **Withdrawn** (empty locus) |
| Scratch R4 G-4 + X-identity | **Live next object** |
| Claim 3 / (N) established ghost-free | **No** |
| Prior art scoop of full Dirac DB for (N) | **No** |

---

## 6. Recommended next

1. AC: amend residual to θ-form; adjudicate R4 (both lanes → G-4 pending identity).  
2. Evaluate Scratch’s X-polynomial identity with explicit HR \(D(X),n(X)\) + secondary weight \(M(X)\) (K0′).  
3. Do **not** treat (N) as a viable NTE neutrino path; use S1–S3 if a fermion coupling is needed.

— Cursor Main, 2026-10-19.
