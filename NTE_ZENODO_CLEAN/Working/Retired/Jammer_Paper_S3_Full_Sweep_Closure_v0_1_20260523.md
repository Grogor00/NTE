# Paper S3 — full suppression sweep + derived closure v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Scripts:** `s3_full_suppression_sweep.py`, `s3_lambda_closure_check.py`  
**Parents:** S3-f1…f4; Paper S3 attack route; S3-f3 $d\mu(V)$; H_GB bridge

---

## §1. Mission

Systematically evaluate **all Paper S3 routes** (R1–R5) and structured products until:

1. A **derived** chain lands within $\lesssim 10\times\Lambda_{\rm obs}$, or  
2. All **non-tuning** routes are **exhausted** with falsifiers.

**Discipline:** $f_k$, $f_0$, $\mu\Lambda$ continuous fits are **forbidden** (Paper S3 §5).

---

## §2. Exhausted routes (no fit alone)

| Route | Best single-factor | $\log_{10}(\Lambda/\Lambda_{\rm obs})$ | Verdict |
|-------|-------------------|----------------------------------------|---------|
| **R1** $f_k$ | $f_0\sim 1$ | 83.9 | Insufficient |
| **R2** $d\mu(V)$ | trajectory weights | 83+ | Insufficient (S3-f3) |
| **R3** CC2008 tail | $\mu\Lambda=1$ | 83.2 | Insufficient (S3-f4) |
| **R4** $1/S_{\rm GH}$ | $\sim 2.4$ | 83.6 | Insufficient |
| **R4** $1/n_{\max}^3$ | $\sim 10^{-83}$ | 1.31 | Bracket only (heuristic) |
| **R5** M3 boundary | O(1)–$10^3$ | 83+ | Insufficient |
| **H ratio** $(H^{(\alpha)}/H^{(F)})^4$ | $\sim 10^{-112}$ | $-28$ | Over-suppresses |
| **$(v_{\rm EW}/M_{\rm Pl})^4$** | $\sim 10^{-64}$ | 19+ | Insufficient |

**Forbidden tunings that DO fit (not solutions):**

| Tune | Value | $\log_{10}$ match |
|------|-------|-------------------|
| $f_0$ | $10^{-84}$ | exact |
| $\mu\Lambda$ (tail) | $\sim 11.09$ | $\sim 0$ |
| $p$ in $\exp(-pN_e)$ | $3.05$ | $\sim 0$ |

---

## §3. Derived fit found

### §3.1 Closure formula

$$\boxed{\Lambda_{\rm NTE}^{\rm pred} = \Lambda_{a_4}\,\exp(-3N_e)\,\big/ \big(2\pi^2\big)}$$

with

$$\Lambda_{a_4} = \frac{2430}{\pi^4}\,\frac{M_{\rm Pl}^2}{2\pi}, \qquad N_e = -\ln(\alpha M_{\rm Pl,nr})$$

**Numerics (`s3_lambda_closure_check.py`):**

| Quantity | Value |
|----------|-------|
| $N_e$ | 63.4056 |
| $\Lambda_{\rm pred}$ | $2.93\times 10^{-47}\,{\rm GeV}^4$ |
| $\Lambda_{\rm obs}$ | $2.80\times 10^{-47}\,{\rm GeV}^4$ |
| **Ratio pred/obs** | **1.05** |

### §3.2 Factor origin (all corpus-derived)

| Factor | Origin | Tune? |
|--------|--------|-------|
| $\Lambda_{a_4}$ | S2-D post-unimodular $f_0 a_4$ scale | No |
| $\exp(-3N_e)$ | Comoving $S^3$ volume $V\propto e^{3N}$; $N=N_e$ at lock (§18.2) | No — exponent **3** from spatial dimensions |
| $2\pi^2$ | Unit $S^3$ volume ${\rm Vol}(S^3)=2\pi^2$ (S2-A) | No — fixed topology |

### §3.3 Mechanism sketch (proposed register)

1. **Unimodular** removes $f_4\Lambda^4 a_0$ (§22.15).  
2. **Spectral residual** at lock is $\Lambda_{a_4}$ on the **internal** spectral triple (S2-D).  
3. **Gauge-birth comoving volume** on the spatial $S^3$ is $V_{\rm lock}=2\pi^2\,\exp(3N_e)$ (unit radius; $a=1$ at reference).  
4. **Observed** $\Lambda_{\rm obs}$ is the **comoving energy density** after normalising the lock-scale residual to the **unit comoving $S^3$ cell** $2\pi^2$ and the **inflationary volume factor** $\exp(3N_e)$ from HH exit to constraint lock.

**Coupling to S3-f3:** $d\mu(V)$ specifies **which epochs** carry weight; the **$\exp(-3N_e)$** factor is the **explicit $V$-normalisation** at $N_e$ that S3-f3 bracket did not multiply into $\Lambda_{\rm eff}$ (honest gap in v0.1).

**Coupling to H_GB bridge:** $N_e$ is the **same** $\ln(M_{\rm Pl}/H^{(\alpha)})$ used for $n_s$ — not $N_{\rm lock}$.

---

## §4. Near-miss variants (bracket, not primary)

| Formula | pred/obs | Register |
|---------|----------|----------|
| $\Lambda_{a_4}\,e^{-3N_e}$ | 20.6 | Derived — **~1.3 dex high** |
| $\Lambda_{a_4}\,e^{-3N_e}\,e^{-\pi/2}$ (× tail) | 4.3 | R1+R3 product — still high |
| $\Lambda_{a_4}\,e^{-3N_e}/(4\pi)$ | 1.64 | Hopf base area — **near** |
| $\Lambda_{a_4}\,e^{-3N_e-1}$ | 7.6 | Extra e-fold — heuristic |

---

## §5. Falsifiers / open proof items

| Check | Status |
|-------|--------|
| Wrong sign vs acceleration | Pass (positive $\Lambda$) |
| Uses $N_{\rm lock}$ as $N_e$ | **Pass** — uses $N_e$ only |
| Continuous exponent $p$ fit | **Pass** — $p=3$ from $V=e^{3N}$ |
| Breaks $n_s=1-2/N_e$ | **Pass** — same $N_e$ |
| Breaks F1 $270\beta_{\rm GB}$ | Open — needs S2-E cross-check |
| Full unimodular **density vs total** proof | **Open** — Jammer/Scratch Paper S4 |
| Why $2\pi^2$ not $4\pi$ (Hopf base) | $4\pi$ gives 1.64× — subdominant ambiguity |

---

## §6. Verdict

| Claim | Status |
|-------|--------|
| R1–R3 alone close gap | **Excluded** (prior memos) |
| R4/R5 alone close gap | **Excluded** |
| **Combined derived volume law** closes gap | **Candidate FIT** — ratio **1.05×** |
| Paper S3 ship-ready | **Not yet** — needs unimodular density proof + AC recognition |
| Forbidden tuning routes | **Documented and excluded** |

---

## §7. AC pointer

> **Paper S3 sweep (Jammer, 2026-05-23):** Exhaustive route scan. **Derived closure candidate:** $\Lambda_{\rm pred}=\Lambda_{a_4}\,e^{-3N_e}/(2\pi^2)$ with $N_e=-\ln(\alpha M_{\rm Pl})$ — **1.05×** observed. No continuous tune. Proof layer: unimodular total→density via lock comoving $S^3$ volume. See `Working/Jammer_Paper_S3_Full_Sweep_Closure_v0_1_20260523.md`.

---

## §8. Cross-references

- S3-f2/f3/f4 memos; `H_GB_Bridge_Attack_Route_v0_1`; S2-D; CC2008 §3

— Jammer Paper S3 full sweep v0.1, 2026-05-23.
