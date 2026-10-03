# Top 5 impact items — attack index v0.1

**Date:** 2026-05-23  
**Status:** **Queued for Greg/Cursor/Jammer attack**  
**Preceding lift:** AC Drive sync (#5) — manifest shipped  
**Parent:** Gap/tension report (stream notes 2026-05-23)

---

## Attack order (recommended)

| Priority | Item | Owner lead | First deliverable |
|----------|------|------------|-------------------|
| **#1** | $H_{\rm GB}$ bridge | Jammer + Cursor | ~~BR2~~ **Done** → **BR2c two-sector** (R2 proposed); J6 saddle |
| **#2** | Λ structural $f$ | Jammer / Paper S3 | ~~Attack route v0.1~~ **Done** → S3-f2 $f_k$ |
| **#3** | Void / $\delta w(z)$ | Jammer | ~~Template v0.1~~ **Done** → V-d2 tracer model |
| **#4** | Formal backlog (μ, P0.10, BH, Born) | Jammer / Scratch | **Package v0.1** → J1+J6 first |
| ~~**#5**~~ | ~~AC Drive sync~~ | AC | **Done this lift** — manifest + handoff |

---

## #1 — Bridge $H_{\rm GB}^{(\alpha)} \leftrightarrow H_{\rm GB}^{(F)}$

**Problem:** Two H-scales at gauge birth differ by ~$10^{28}$; $N_{\rm lock}$ chain uses **(F)**; $N_e$, $n_s$, M₁ use **(α)**. Conflation breaks audit (P-dS1 Route B FAIL).

**Existing work:**
- `H_GB_Disambiguation_Note_v0_1_20260523.md` — notation fix, bridge **open**
- §22.18 HH saddle $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ → **(F)**
- §22.19 $N_{\rm lock}=S_{\rm dS}/4$ holographic identity
- `17.5.4_Audit_NLock_Derivation.md`

**Attack routes:**

| Route | Mechanism | Target |
|-------|-----------|--------|
| **R1** | HH instanton exit: thermal **(F)** at $T_{\rm GB}$ → constraint **(α)** at locking via $\Phi(N)$ trajectory | Explicit $\Delta N$ between epochs |
| **R2** | §22.19: $N_{\rm lock}=S/4$ links e-fold depth to horizon entropy — **same** transition, two readings of $H$ | Prove identity, not equality of symbols |
| **R3** | Companion 9 Gaussian saddle: $H_{\rm HH}\sim M_{\rm Pl}$ pre-locking vs $H=\alpha M_{\rm Pl}^2$ at lock | $\lambda$ O(1) in $H_{\rm HH}=\lambda M_{\rm Pl}$ |
| **R4** | **Falsifier:** force $H_{\rm GB}^{(\alpha)}=H_{\rm GB}^{(F)}$ → breaks $N_e$ **or** $N_{\rm lock}$ | Already excluded numerically |

**Delivered:** `H_GB_Bridge_Attack_Route_v0_1`; `Phi_N_Trajectory_BR2_v0_1`; **`Phi_N_Trajectory_BR2c_Attack_Route_v0_1`** + `phi_n_trajectory_br2c.py`  
**Success (partial):** Three-epoch resolution + two-sector $\Phi(N)$ — **field map at lock still open (J6/BR2d)**  
**Do not claim:** Single $H(N)$ ansatz closes $n_s$ and lock endpoints; single $H_{\rm GB}$ without derivation

---

## #2 — Λ numerical closure (Paper S3 / S4)

**Problem:** Unimodular removes ~$10^{121}$; post-$a_4$ residual ~$10^{83}\times\Lambda_{\rm obs}$ (Paper S3 M1/M2/M3 all fail naive closure).

**Existing work:**
- §22.15 unimodular framework; §17.5.18 deferred
- `Paper_S3_Lambda_*` scaffolds + three numerics scripts
- M1 tuning **falsified**; M2 heuristic **fails**; M3 O(1) seam **insufficient**

**Attack routes:**

| Route | Mechanism | Owner |
|-------|-----------|-------|
| **R1** | Structural suppression factor $f(\beta_{\rm GB}, a_4, d\mu(V))$ from spectral action | Jammer Paper S3 |
| **R2** | CC2008 exponential cutoff on $S^3\times S^1$ — higher $a_{2n}$ vanish | Already inherited; residual decomposition |
| **R3** | $\Phi(N)$ trajectory + Friedmann fixes $d\mu(V)$ — compute residual, not import $\Lambda_{\rm obs}$ | Paper S3/S4 |
| **R4** | **Honest deferral:** framework-only until $f$ derived | Corpus default |

**First deliverable:** `Paper_S3_Structural_f_Attack_Route_v0_1` (Jammer)  
**Success:** Residual $<10^{2}$ orders of obs **or** sharp falsifier on route  
**Do not claim:** Λ predicted to $10^{-122}M_{\rm Pl}^4$ today

---

## #3 — Inhomogeneous void / $\delta w(z)$ (P-dS4 empirical layer)

**Problem:** Homogeneous layer ≡ ΛCDM (Gate #2); NTE discrimination requires void-enhancement signatures (§17.5.12 a–d).

**Existing work:**
- `P_dS4_Observational_Anchor_v0_1_20260523.md`
- `LCDM_Void_Bias_BAO_Worksheet_v0_1`, CMB κ scaffold
- DESI hint $w>-1$ low-$z$ — directional only
- `lcdm_growth_numerics.py` — hom done

**Attack routes:**

| Route | Task | Owner |
|-------|------|-------|
| **R1** | CMB κ extraction → compare 5.50 (P-dS4b) | Jammer |
| **R2** | $\delta w(z)$ profile vs DESI DR3+ (P-dS4c) | Jammer |
| **R3** | Diagnostic (a): $w$ vs void fraction LOS | Jammer |
| **R4** | Diagnostic (b): $w(z)\to -1$ high-$z$ | Euclid/DESI era |

**First deliverable:** Jammer execution on Gate #6 CMB worksheet + void BAO numerics  
**Success:** (a)–(d) table with data **or** clean falsifier path  
**Do not claim:** Global χ² beat without inhom layer

---

## #4 — Jammer / Scratch formal backlog

**Aggregated open formal work blocking “theorem” register upgrades:**

| ID | Item | Source | Status |
|----|------|--------|--------|
| **J1** | μ(x,N) covariant δg_μν — formal sign-off | §22.16 R5 | Near-closure; Jammer |
| **J2** | P0.10 Tomita–Takesaki non-associative $A_F$ | Charter §4.1 | GNS partial; P-dS3 |
| **J3** | P-B1b/P-B2b Born formal lemmas | P-Born | Attack routes only |
| **J4** | BH $g(\ell/\ell_\infty)$ from action | P-BH1b | Programme |
| **J5** | M3 β_GB boundary counter-term derivation | Paper S3 M3 | Scaffold |
| **J6** | HH saddle §22.18 — ties to **#1** | Companion 9 | Open |

**First deliverable:** Jammer priority pick (suggest **J1 + J6** — unblocks μ + H_GB)  
**Do not claim:** P0.10 closed without abstract-algebra extension

---

## #5 — AC Drive sync ✓ (this lift)

**Delivered:**
- `Working/Drive_Sync_Manifest_v10_17_1_20260523.md`
- `Handoffs/Handoff_Cursor_to_AC_v10_17_1_Full_Drive_Sync_20260523.md`

**AC action:** Push trilogy + Working bundle per manifest checklist.

---

## Cross-cutting discipline

1. **Gap 5** — mechanism level; §17.5.13 paired  
2. **H_GB** — never conflate (F) and (α) in prose  
3. **Λ** — framework only until Paper S3 closes  
4. **BH** — multiplicative $S=(A/4G)\,g(\ell)$; additive dead  
5. **P-dS** — scaffolds complete; not dS/CFT closure  

---

## Suggested session plan (Greg)

1. **Attack #1** — Cursor drafts `H_GB_Bridge_Attack_Route_v0_1` (R1–R3); Jammer HH saddle  
2. **Parallel #3** — Jammer CMB κ + void (DESI window)  
3. **#2** — Jammer Paper S3 structural $f$ when #1 clarifies $H$ trajectory  
4. **#4** — Jammer μ sign-off + P0.10 as bandwidth allows  

— Cursor Top-5 index v0.1, 2026-05-23.
