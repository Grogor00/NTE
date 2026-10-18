# Solution map — alternate routes + computational sweep (Cursor Main)

**Date:** 2026-10-19 · **No Core.**  
**Engines:** NumPy + SymPy (Wolfram unavailable).  
**Scripts:** `Opsi2_SOLUTION_SWEEP_CursorMain.py`, `Opsi2_Round5_X_Identity_COMPUTE_CursorMain.py`  
**JSON:** `Opsi2_SOLUTION_SWEEP_RESULTS.json`

---

## 1. Literature: what is already known

| Route | Refs | Ghost status |
|---|---|---|
| **S1.** Matter on **one** metric only | HR; dRHR 1408.1678 | **Healthy** |
| **S2.** Rank-2 **effective vielbein** \(\tilde e=ae+bf\) | Melville–Noller 1408.5131, **1511.01485** (Dirac MSS ✓) | **Healthy to \(\Lambda_3\)**; full ADM ghost above cut-off |
| **S3.** Composite **effective metric** \(G=\alpha^2g+2\alpha\beta gX+\beta^2f\) | dRHR 1408.1678; Hassan–Kocic–Schmidt-May **1409.1909**; uniqueness **1505.02616** | **Healthy classically**; unique non-minimal below strong-coupling scale |
| **S4.** Two **independent species** \(\chi_g,\chi_f\) | dRHR eq. (7) | **Healthy** |
| **(N).** Same Dirac, **two independent kinetics** | Yamashita 1408.0487 (scalars); dRHR; this corpus R1–R5 | **Ghost / lapse-fixed** — no healthy rescue found |
| Kinetic↔potential split tricks | dRHR §alt | Special; not two full Dirac kinetics |
| Partially massless + spinor | search | **No usable hit** for rescuing (N) |

**Uniqueness (1505.02616):** among local composite metrics, the dRHR \(G\) is the unique non-minimal coupling passing decoupling + loop diagnostics below the strong-coupling scale.

---

## 2. Computational modes (check → adjust → recheck)

| Mode | Question | Result |
|---|---|---|
| **A.** Residual in spatial \(d=1,2,3\) | Does (N) heal in lower D? | **No.** \(R\neq0\) for \(X\neq I\) in all \(d\). (\(d=1\): \(X\propto R\) algebraically but \(R\neq h_g\) still — S1-style dimensional artifact, not 3+1d rescue) |
| **B.** Rank-2 \(\tilde e\) | Single kinetic on \(\tilde e\) | **Relative \(R=0\) by construction**; literature MSS Dirac healthy |
| **C.** Weights \(\alpha,\beta\) on two kinetics | Interior \(\alpha\beta\neq0\) with \(R=0\)? | **No** — min interior \(\|R\|\) stays \(O(0.1)\)–\(O(1)\) |
| **D.** Field-dependent \(w_g,w_f\) | Optimize to kill \(R\) on anisotropic \(X\)? | **No** — best \(\|R\|\sim10^{-3}\)–\(10^{-2}\), never vanishes; SymPy: needs \(X\propto I\) |
| **E.** Composite \(G\) | SPD effective spatial metric | **Yes** on tested \((\alpha,\beta,\lambda)\); single-metric ED structure |
| **F.** Densitized \(\theta\) | Required? | **Yes** — \(\theta\) vs no-\(\theta\) differ off \(X=I\); single-metric control needs \(\theta\) |
| **G.** Isotropic scalar analog | Lower-\(d\) volumes | Residual \(\propto(s_g-s_f)^2\) vanishes iff equal scales |
| **H.** \(S_{\mathrm{grav}}=R\) match | 50 random metrics vs \(\{h_g,h_f,(h_g+h_f)/2,G\}\) | **0/50** matched |
| **R5.** \(LDnM=-R\) identity | Explicit HR \(D(n),n(R)\) | Mis-posed object fails as X-only id; **≠ terminal G-2** (AC R5) |

---

## 3. Robust conclusion

### No robust solution for action (N)
Every rescue attempted inside naive double-kinetic Dirac fails:
- dimensional reduction,
- kinetic reweighting,
- field-dependent SC weights,
- D-matrix / \(n^i\) X-identity,
- structure-function matching.

Consistent with dRHR/Yamashita for scalars and with Opsi2 R1–R5 for spinors.

### Robust solutions (use these)
1. **S1 — single-metric Dirac** (other metric pure HR)  
2. **S2 — rank-2 effective vielbein** \(\tilde{e}=ae+bf\) (Melville–Noller; Dirac MSS OK)  
3. **S3 — composite \(G_{\mu\nu}\)** (Hassan et al.; unique per 1505.02616)  
4. **S4 — two species**, one per metric  

For NTE / Claim-3 purposes: **do not use (N)**. Prefer **S2** if a single spinor must “see” both frames; prefer **S1** if minimal.

---

## 4. Recommended path

| Goal | Choice |
|---|---|
| Ghost-free fermion in HR bigravity | **S1 or S2** |
| Symmetric treatment of \(g,f\) | **S3** (composite \(G\)) or **S2** with \(a=b\) |
| Keep action (N) | **Not recommended** — ghost status **undetermined** (AC R5: return to G-4; Round 6 pending) |
| Next corpus compute | Round 6 on Greg GO only; if S2 adopted, MSS→ADM checklist from 1511.01485 Table 1 |

---

## 5. Standing

Claim 3 / naive double-kinetic: **not established as ghost-free; (N) undetermined** (AC R5: G-2 not ratified; mis-posed identity refuted ≠ absorption settled).  
Healthy routes **S1–S4 stand regardless**. P04 / \(N_{\mathrm{eff}}\) unchanged (no Core). Prior art for (N) spinor DB chain: none; for alternate routes: substantial.

**Amendment 2026-10-20:** Softened per `RULING_AC_Round5_G2_Not_Ratified_…`. Do not treat (N) as settled G-2.

— Cursor Main, 2026-10-19; amended 2026-10-20.
