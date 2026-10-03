---
title: "How Φ_NTE enters the spectral data"
subtitle: "The Seeley–DeWitt endomorphism E(Φ), the Farnsworth finite triple, and the spectral-entry interface"
author: "Gregory Lyndon White"
date: "2026-08 (Companion 15; Farnsworth Stage 0–5 park + E(Φ) interface)"
---

*Part of NTE Corpus v10.19.0. Companion 15.*

> **Door B status (2026-09-27).** This companion was written against the constrained action of Companion 9 (2026-08), in which μ(N) enforced H = β_NTE|Φ_NTE|² at action level and Φ_NTE carried a conformal coupling and a Higgs portal. **That action is withdrawn.** Under Door B, H = β_NTE|Φ_NTE|² is a Part 1 / Companion 8 **identity**, not an action-level constraint; Companion 9 no longer carries μ(N), F(Φ)R or the portal; and general relativity is restored for the metric sector. **References below to "Leg 1", the constrained variational problem, and Companion 9 eq. (1) are historical and are not current corpus physics.** What this companion contributes that is **unaffected**: the Farnsworth Stage 0–5 park (§4), the **metric-only-entry theorem (§6.1)** — which Part 3 carries as *proven empty* and which Door B independently corroborates — and the **raw-trace monotonicity / a₆ budget results (§6.3)**.

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*This companion parks the Farnsworth Stage 0–5 build (archive pull 2026-08-02) and specifies the interface by which scalar data enter the heat-kernel endomorphism $E$ — the spectral-entry interface, written alongside the constrained $\mu(N)$ action of Companion 9 that Door B has since withdrawn. It does **not** claim a closed derivation of $E(\Phi_{\mathrm{NTE}})$ or of Yukawa magnitudes. Structure vs magnitude, and $\Phi_{\mathrm{NTE}}\neq\sigma$, are kept sharp.*

---

## Abstract

This companion specifies the rule by which $\Phi_{\mathrm{NTE}}$ (and the finite-triple scalars) enter the spectral / Seeley–DeWitt data, as an **interface specification** grounded in the Farnsworth–Boyle non-associative spectral programme and in the Stage 0–5 build executed 2026-06-19…21. **It was written as the second leg of a constrained variational problem whose first leg — an action-level Lagrange multiplier enforcing $H=\beta_{\mathrm{NTE}}\lvert\Phi_{\mathrm{NTE}}\rvert^{2}$ — was withdrawn under Door B (2026-09-27); see the status note above.** Its surviving content is the Farnsworth park (§4), the metric-only-entry theorem (§6.1), and the raw-trace / $a_6$ results (§6.3).

The finite algebra is $A_F=\mathbb{O}\oplus\mathbb{O}$. Fluctuations of the finite Dirac operator produce charged Higgs data $\Phi_{IJ}$ whose **representation structure** is fixed by Farnsworth's alternative-law / involution conditions, while the **magnitudes** $M_{IJ}$, $\kappa(ab)$ remain free spectral parameters (Stage 0 outcome (ii); Farnsworth's own $M_{00}$ "single free parameter"). The heat-kernel expansion remains valid once $D+F$ is an ordinary self-adjoint operator on $H$ (Boyle–Farnsworth 2013). For the Dirac $\nu_2$ Yukawa geometric branch, Stage-4-full associator numerics select the **$4\pi$** (single $\varepsilon'$ sector) normalisation, not the Majorana $8\pi$ doubling — magnitude still free.

$\Phi_{\mathrm{NTE}}$ itself is **not** identified with the Chamseddine–Connes $\sigma$ nor with Farnsworth's $\Phi_{IJ}$. It entered the bosonic sector through the almost-commutative product geometry and the then-current constrained action of Companion 9 (withdrawn, Door B); the explicit closed-form endomorphism $E(\Phi_{\mathrm{NTE}})$ on the NTE substrate remains the open heat-kernel computation. This companion records what is fixed, what is free, and how the two legs join.

---

## 1. Why this companion exists

Companions 8–9 constructed $V_{\mathrm{NTE}}$ and the Euclidean saddle under the constraint

$$H=\beta_{\mathrm{NTE}}\lvert\Phi_{\mathrm{NTE}}\rvert^{2},$$

then enforced at action level by a Lagrange multiplier $\mu(N)$ — **an action withdrawn under Door B (2026-09-27); the constraint is now an identity (Part 1 §2.3, Companion 8), not an action-level condition.** Companions 11–12 and 14 treat the gravitational heat-kernel spine ($a_0,a_2,a_4,\ldots$) on $S^3\times S^1$ and on RW metrics. None of those papers specifies how $\Phi_{\mathrm{NTE}}$ enters the spectral endomorphism $E$ that appears when

$$D_A^2 = -(\nabla^2+E)$$

is expanded for the fluctuated Dirac operator — nor do they park the Farnsworth finite-triple findings that control the internal scalar data.

Without that interface, the constrained variational problem was incomplete: one had $\mu(N)[H-\beta\lvert\Phi\rvert^{2}]$ but not the spectral dependence of the bosonic action on $\Phi$. This companion closed that documentation gap. It does not close the computation of $E(\Phi_{\mathrm{NTE}})$, **which remains open independently of Door B.**

**Archive source.** Stages 0–5 and supporting reads were pulled from the historical archive into
`Working/Farnsworth_Archive_Pull_20260802/`
(build-spec, Stage memos, Stage-5 Scratch interpretation, scripts/JSON scaffolds).

---

## 2. Three scalar channels (do not collapse them)

| Symbol | Origin | Role in NTE |
|--------|--------|-------------|
| $\Phi_{IJ}$ | Farnsworth 2025 fluctuations of $D_F$ on $A_F=\mathbb{O}\oplus\mathbb{O}$ | Charged / uncharged Higgs of the *finite* triple; Yukawa structure |
| $\sigma$ | Chamseddine–Connes SM almost-commutative geometry (RH-neutrino Majorana block) | Spectral-action scalar of the *associative* SM triple; **not** present as such in NTE (no RH/LH neutrino of that kind — Companion 7) |
| $\Phi_{\mathrm{NTE}}$ | Boundary-expansion scalar on $S^3$; $H=\beta_{\mathrm{NTE}}\lvert\Phi_{\mathrm{NTE}}\rvert^{2}$ | Geometric field of Companions 8–9; distinct from the SM Higgs |

Companions 5 and 8 already forbid field identification $\sigma\equiv\Phi_{\mathrm{NTE}}$. Farnsworth 2025 strengthens the *shared algebraic machinery* story (octonionic spectral geometry can generate charged scalars without RH-Majorana $\sigma$) without collapsing the two fields (Octonionic Spectral Triple Read §4): same EFT *form* by structural confluence; different generation loci (boundary trajectory vs finite-triple fluctuation).

---

## 3. How scalars enter $E$ (the interface)

### 3.1 Laplace-type form

For a fluctuated Dirac operator $D_A=D+F$ on the product geometry

$$C^{\infty}(M)\otimes A_F,\qquad M=S^{3}\times S^{1}\quad\text{(NTE canonical base)},$$

one writes

$$D_A^{2} = -(g^{\mu\nu}\nabla_{\mu}\nabla_{\nu} + E),$$

with $E$ a matrix-valued endomorphism on the spinor$\otimes$finite Hilbert space. The Seeley–DeWitt coefficients $a_{2n}$ are local integrals of curvature invariants built from the metric, the connection, and $E$ (Gilkey; Vassilevich; Companion 14 for the pure-RW gravitational case).

### 3.2 Finite-triple contribution (Farnsworth / BF)

Per Boyle–Farnsworth 2013 and Farnsworth 2025 (Stage 0 extract):

1. Non-associativity enters **upstream**: left-multiplication representation $L_a$, derivations, reconstituted bimodules, fluctuation $F$ with Higgs blocks $\Phi_{IJ}$.
2. Once $D_A$ is an ordinary self-adjoint operator on $H$, the heat-kernel / spectral-action step proceeds as in the associative case (BF 2013 §4.3: Theorems 3.3 and 3.7 apply). Stage 0: foundational block **not** triggered.
3. The finite Dirac template is the Hermitian off-diagonal form

$$D_F = M_{IJ}\begin{pmatrix}0 & e_I\otimes e_J^{*}\\ e_J\otimes e_I^{*} & 0\end{pmatrix}$$

(Farnsworth eq.\ (92)), with real $M_{IJ}$ as free spectral data.
4. Gauge / Higgs fluctuations produce $F$ constrained by $FJ=\varepsilon'JF$; the endomorphism $E$ then acquires the standard almost-commutative pieces

$$E \supset \tfrac{1}{4} R\,\mathbf{1} + E_{\mathrm{gauge}}(F_{\mu\nu}) + E_{\mathrm{Higgs}}(\Phi_{IJ},D_F) + E_{\mathrm{Yukawa}}.$$

Explicit local formulae are those of the spectral-action literature once $D_A$ is assembled; NTE does not re-derive Gilkey here.

### 3.3 Boundary field $\Phi_{\mathrm{NTE}}$ (NTE-specific)

$\Phi_{\mathrm{NTE}}$ is **not** one of the Farnsworth $\Phi_{IJ}$. It enters the bosonic sector by two routes that this companion keeps separate:

**(A) Constrained Einstein–scalar action (Companions 8–9) — WITHDRAWN 2026-09-27 (Door B); recorded here as the historical setting of §6.1's theorem.**

$$L = \frac{R}{16\pi G} - \tfrac{1}{2}(\partial\Phi_{\mathrm{NTE}})^{2} + \tfrac{1}{12}R\,\Phi_{\mathrm{NTE}}^{2} - V_{\mathrm{NTE}}(\Phi_{\mathrm{NTE}}) - 2e\,\lvert H\rvert^{2}\Phi_{\mathrm{NTE}}^{2} + \mu(N)\bigl[H - \beta_{\mathrm{NTE}}\lvert\Phi_{\mathrm{NTE}}\rvert^{2}\bigr].$$

In that action $\Phi_{\mathrm{NTE}}$ coupled conformally ($\xi=1/6$) and through a Higgs portal, with the multiplier $\mu(N)$ enforcing the constraint at action level. **All three are withdrawn under Door B (2026-09-27): Companion 9 no longer carries $\mu(N)$, $F(\Phi)R$ or the portal, and the constraint is an identity rather than an action-level condition.** The Lagrangian above is retained only because §6.1's theorem is stated against it.

**(B) Spectral endomorphism $E(\Phi_{\mathrm{NTE}})$ — interface open.**
A full spectral-action derivation would promote $\Phi_{\mathrm{NTE}}$ (or a geometric proxy on the $S^3$ factor) into $D_A$ so that $E=E(R,\Phi_{\mathrm{NTE}},\Phi_{IJ},\ldots)$ and the heat-kernel coefficients reproduce (A)'s kinetic / potential structure, including $K(\Phi)$. That computation is the archived Paper-S2 central deliverable (Octonionic Read §5–§6): evaluate the spectral action on Hopf-$S^3\times A_{G_2}$ and extract $K(\Phi)$, $V_E$ coefficients, and related scales **together**. **It is not closed in Stages 0–5**, which targeted the finite Yukawa / flux branch.

Until (B) is carried out, the honest reading is:

- use (A) for the constrained variational / saddle problem;
- treat (B) as the spectral completion that would *derive* $V_{\mathrm{NTE}}$ / $K(\Phi)$ off-trajectory rather than commit them;
- do **not** substitute Farnsworth $\Phi_{IJ}$ or CC $\sigma$ for $\Phi_{\mathrm{NTE}}$ inside $E$.

---

## 4. Farnsworth Stage 0–5 — parked findings

| Stage | Result | Status for corpus |
|-------|--------|-------------------|
| **0** Fixed vs free | Representation / charged-sector structure **FIXED**; magnitudes $M_{IJ}$, $\kappa(ab)$, $\Phi_{IJ}$ scale **FREE** (Hermiticity + $FJ=\varepsilon'JF$ only). Uncharged sector: $M_{00}$ "single free parameter" (Farnsworth §4.2). | **Ratified finding:** outcome (ii) — relations, not numbers |
| **0** Heat kernel | BF 2013: non-associativity upstream; Gilkey applies to $D_A^2$. | **PASS** — route sound |
| **1** Octonion + $L_a$ | Fano table, left-mult matrices, 1+7 split, 196 nonzero associators. | Infrastructure **PASS** |
| **2** $\mathbb{O}\oplus\mathbb{O}$ bimodule | Reconstituted actions; $S=\tfrac12$ by involution; $\varepsilon'$ branch; $M_{IJ},\kappa$ free inputs. | Scaffold **PASS** |
| **3** $D_F$ neutrino block | Hermitian template; raw $\nu_L^{(2)}$–$\nu_R^{(2)}$ entry Ansatz-scaled. | Magnitude **FREE** |
| **4 / 4-full** Hopf overlap + associator | Dirac Yukawa: **one** active $\varepsilon'$ sector → flux prefactor **$4\pi$**, not $8\pi$. Associator cross-summand mixing null in scaffold. | Geometric branch: **$4\pi$** (Dirac); Majorana $M_1$ **$8\pi$** untouched |
| **5** Assemble | Magnitude not derived; $(8\pi)^{-1/3}$ undercut on *both* legs (free $M_{IJ}$ + $4\pi$ expectation). | Outcome **(ii)**; Companion 13's open normalisation sits here |

**Operator-theory criterion (Scratch Stage-5 interpretation).** Majorana masses live in the $J$-block and carry the real-representation doubling $\Phi_{\mathrm{Maj}}=8\pi$; the Dirac Yukawa is a within-sector $\nu_L$–$\nu_R$ coupling and does **not** inherit that doubling → default **$4\pi$**. Stage-4-full numerics agree (single active $\varepsilon'$ sector). Absolute $Y_{\nu_2}$ remains free pending fixation of $M_{IJ}$.

**What Stages 0–5 do *not* deliver:** a closed $E(\Phi_{\mathrm{NTE}})$; a derived $K(\Phi)$; a derived Yukawa magnitude; identification $\Phi_{\mathrm{NTE}}\equiv\Phi_{IJ}$ or $\sigma$.

---

## 5. The constrained variational problem (both legs)

**Leg 1 — constraint (Companion 9) — WITHDRAWN (Door B, 2026-09-27); retained for the historical record.** Vary

$$S=\int\!d^{4}x\sqrt{\lvert g\rvert}\;L$$

with $L$ as in §3.3(A). The multiplier $\mu(N)$ enforces $H-\beta_{\mathrm{NTE}}\lvert\Phi_{\mathrm{NTE}}\rvert^{2}=0$, reducing dynamics to a single geometric degree of freedom (Companion 9 §2).

**Leg 2 — spectral data (this companion).** The bosonic spectral action

$$\operatorname{Tr} f(D_A/\Lambda)=\sum_n f_n\Lambda^{4-2n}a_n(D_A^2)$$

depends on $E$ through the $a_n$. Finite-triple scalars enter via §3.2. $\Phi_{\mathrm{NTE}}$ enters today through the Einstein–scalar action (A); spectrally through the open map (B).

**Joint use (historical).** For saddle / trajectory analysis the constrained action was Leg 1; under Door B no such constrained saddle exists, and the origin sector is open (Part 3). For claiming that $V_{\mathrm{NTE}}$ or $K(\Phi)$ is *derived* from the triple: require Leg 2(B) closed — and that closure must use a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ (§6.1). **That requirement stands on §6.1's theorem and is unaffected by Door B; the targets themselves, however, are not live — off-trajectory $V_{\mathrm{NTE}}$ is not required under the identity reading (Companion 8 F3), and frame-level $K(\Phi)$ is withdrawn (§6.4).** Confluence with $V_E(x)=\lambda_0 x^4/(1+(\kappa_{\mathrm{cfm}}^2/12)x^2)^2$ (Companion 8 §8) is structural form-match only, and **historical/audit under Door B**. **Note the symbol: $\kappa_{\mathrm{cfm}}=\sqrt{2}/M_{\mathrm{Pl}}$ is the confluence coefficient, not the dark-matter Hopf coupling $\kappa_0 = 3/\sqrt{4\pi}$ (Companion 7); the two must not be conflated.**

---

## 6. Closed result and open work

### 6.1 Theorem — metric-only entry is empty (minisuperspace redefinition)

**Statement.** Every gravitational Seeley–DeWitt density $a_{2n}$ is a functional of the metric alone. Therefore any entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ *purely through the metric* — the radius-modulus / $\ell=1/H$ route, at any order, with any cutoff moments — is a field redefinition of Leg 1's gravitational dynamics and **cannot** yield an independent kinetic factor $K(\Phi)$ or an off-trajectory potential $V(\Phi)$.

**Computation (Step 1, 2026-08-02).** Substitute the constraint radius $a=1/(\beta\Phi^{2})$ into the verified Chamseddine–Connes RW coefficients (Companion 14) and integrate by parts. The local densities become

$$a_0 = \frac{1}{2\beta^{3}\Phi^{6}},\qquad a_2 = -\frac{(\Phi')^{2}}{\beta^{3}\Phi^{8}}-\frac{1}{4\beta\Phi^{2}}$$

(up to total derivatives). The metric route therefore induces $K(\Phi)\propto 1/(\beta^{3}\Phi^{8})$, whose canonical field is $\chi\propto\Phi^{-3}$. The check $\chi\propto a^{3/2}$ holds at constant ratio $-\sqrt{2}/3$ — exactly the standard FRW minisuperspace variable. In canonical variables the spectral-action truncation collapses to kinetic $(\chi')^{2}$ plus $c_4\Lambda^{4}\chi^{2}+c_2\Lambda^{2}\chi^{2/3}$: volume term plus curvature term. Pure gravity, re-lettered.

**Corpus status.** Part 3's open-work note had asserted this circularity ("the natural geometric route via $\ell=1/H$ is circular… does not fix $K(\Phi)$ independently"). It is now **computed rather than asserted**, with the explicit map $\chi\propto a^{3/2}$ as the proof. The caution upgrades to a closed negative theorem: an entire class of would-be derivations is eliminated before further sessions.

**Consequence for Paper S2.** Branch-deciding content, if any, lives entirely in a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ — the Hopf-fibre connection / $E$-coupling channel named by the deliverable "Hopf-$S^3\times A_{G_2}$" — feeding Gilkey's $\mathrm{tr}\,E$, $\mathrm{tr}\,E^2$, and the fluctuation kinetic trace. That entry's *form* is fixed by the archived Octonionic Read §5–§6 and BUILD SPEC, not by ansatz (blind protocol).

### 6.2 Frame-level $K(\Phi)$ vs spectral $K(\Phi)$

Companion 17 obtained $K(\Phi)$ as the Einstein-frame kinetic factor of the conformal coupling then carried in Companion 9 — a frame transform of that action, not a Seeley–DeWitt extraction. **Under Door B that coupling is withdrawn and Companion 17 is retained as audit trail only; the frame-level $K(\Phi)$ is not current corpus physics.** The present companion's §6.1 theorem still stands for spectral routes: metric-only entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ cannot yield an independent spectral $K(\Phi)$. Spectral origin of $\xi$ itself (route B) remains open.

### 6.3 Addendum (2026-08) — raw-trace monotonicity and $a_6$ budget

Parked from the Session 2026-08-02/03 saddle work (full statement also in Companion 9 §7):

- **Raw-trace theorem:** $\mathrm{Tr}\,f(D^2/\Lambda^2)$ is strictly monotone in overall scale on fixed-shape families for positive decreasing $f$ — no scale extremum. Truncation artifacts produced a spurious "Planck-scale instanton." Nucleation, if any, belongs to the constrained system.
- **$a_6$ budget:** $R_6=(31/1260)(H/\Lambda)^{4}$ is far too small to produce $\lvert n_s-1\rvert\approx0.035$ at $H\sim0.4\,M_{\mathrm{Pl}}$. Pure gravity cannot supply the tilt. Companion 14 $a_8$, $a_{10}$ sphere values confirmed numerically against the exact spectrum.

### 6.4 Open work (named)

1. **Non-metric $E(\Phi_{\mathrm{NTE}})$** on Hopf-$S^3\times S^1\times(\mathbb{O}\oplus\mathbb{O})$ — assemble $E$ from the archived Hopf / $E$-coupling entry; run $\mathrm{tr}\,E$, $\mathrm{tr}\,E^2$ through $a_2/a_4$; extract the fluctuation kinetic trace; settle the *spectral* origin of $\xi$ / any residual kinetic structure beyond Companion 17's frame result (Paper-S2 central item; Octonionic Read §5–§6 + BUILD SPEC). Metric channel **closed empty** (§6.1). Frame-level $K(\Phi)$ **withdrawn (Door B); Companion 17 audit trail only.**
2. **Fix or leave free $M_{IJ}$** under NTE CPN / $\sigma_1$–$\sigma_2$ constraints (Stages 0/5: presently free).
3. **Associator-envelope hardening** beyond scaffold (Stage-4-full convergent with Stream 2; keep as cross-check, not a magnitude derivation).
4. **Do not** re-import $(8\pi)^{-1/3}$ as a derived Dirac Yukawa magnitude; Companion 13's honest branch language stands.

---

## 7. Relation to other companions

| Companion | Relation |
|-----------|----------|
| **8** | $V_{\mathrm{NTE}}$, $\ell=1/H$, $V_E$ confluence; motivates $\mu(N)$ structure |
| **9** | Historical: the constrained $L$ with $\mu(N)[\cdots]$, **withdrawn under Door B (2026-09-27)**; Companion 9 now carries restored GR with $\Phi_{\mathrm{NTE}}$ as an identity |
| **11–12** | Gravitational $a_k$ / $a_4=0$ spine — independent of Farnsworth magnitudes |
| **13** | $\nu_2$ Yukawa / open normalisation — Stage 0–5 is its finite-triple ground |
| **14** | RW $a_0$–$a_{10}$ prior art — pure gravitational $E=R/4$ limit |

---

## References

1. S. Farnsworth, "The geometry of the Standard Model from alternative algebras," arXiv:2506.21496 (2025) — $A_F=\mathbb{O}\oplus\mathbb{O}$, charged bimodules, free $M_{IJ}$.
2. L. Boyle and S. Farnsworth, "Non-associative geometry and the spectral action principle," JHEP **07** (2015) 023 [arXiv:1303.1782] — heat kernel after $D_A$ assembled.
3. S. Farnsworth and L. Boyle, "Rethinking Connes' approach…" arXiv:1408.5367 — chirality from non-associative derivations.
4. A. H. Chamseddine and A. Connes — spectral action / $\sigma$ (associative SM triple); contrast §2 of this companion.
5. Archive park: `Working/Farnsworth_Archive_Pull_20260802/` — Stage 0–5 memos, BUILD SPEC, Stage-5 Scratch interpretation, scripts.
6. NTE Companions 8–9 (constraint action), 11–13 (Λ / chord / $\nu_2$), 14 (RW coefficients).

— End of Companion 15.
