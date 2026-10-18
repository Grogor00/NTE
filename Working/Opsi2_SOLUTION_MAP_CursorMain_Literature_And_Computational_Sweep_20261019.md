# Solution map — bigravity + Dirac / double coupling

**Date:** 2026-10-19 · Cursor Main · **No Core.**  
**Engines:** NumPy + SymPy (Wolfram unavailable).  
**Scripts:** `Opsi2_SOLUTION_SWEEP_CursorMain.py`, `Opsi2_Round5_X_Identity_COMPUTE_CursorMain.py`  
**JSON:** `Opsi2_SOLUTION_SWEEP_RESULTS.json`

---

## 1. Literature routes (external, established)

| ID | Coupling | Ghost status | Key refs |
|---|---|---|---|
| **S1** | Dirac (or any matter) on **one** metric only | **Healthy** | HR matter; dRHR 1408.1678 |
| **S2** | Rank-2 **effective vielbein** \(\tilde e=ae+bf\) | **Healthy** in MSS for Dirac+YM+scalar; ghost only above \(\Lambda_3\) in full ADM | Melville–Noller 1408.5131, **1511.01485** |
| **S3** | Composite **effective metric** \(G=\alpha^2 g+2\alpha\beta gX+\beta^2 f\) | **Healthy classically** (Hassan–Kocic–Schmidt-May); **unique** non-minimal below \(\Lambda_3\) | 1408.1678, **1409.1909**, **1505.02616** |
| **S4** | Two **independent** species \(\chi_g,\chi_f\) | **Healthy** | dRHR eq. (7) |
| **S5** | Kinetic on one metric, potential on other (special rewrite) | Healthy in cited scalar examples | 1408.0487 §III |
| **(N)** | **Same** Dirac, **two** independent kinetics | **Scalars:** ghost/no-go. **Spinor ADM:** **undetermined** (AC R5 → G-4; Round 6 pending) | 1408.0487, 1408.1678; our R1–R5 + AC R5 |

**No literature** finds a healthy partially-massless or exotic spinor rescue of (N).

---

## 2. Computational sweep (this session)

### Mode A — dimensions \(d=1,2,3\)
- For \(X\neq I\), residual \(R\neq 0\) in all \(d\).
- **\(d=1\) special:** \(X\propto R\) always (1×1). Matrix obstruction dies; **does not** imply healthy (N) — scalar double-kinetic still ghosts via lapse nonlinearity (1408.0487). Matches S1 “1+1d artifact” discipline.
- \(d=2,3\): \(X\not\propto R\); ranks mismatch (AC rank-1 vs \(X\) full).

### Mode B — rank-2 effective vielbein
- Single \(\tilde e\) ⇒ single \(\Sigma\) ⇒ relative double-kinetic \(R\) **absent by construction**.
- Aligns with Melville–Noller MSS Dirac ✓.

### Mode C — weighted kinetics \(\alpha L_g+\beta L_f\)
- Interior \((\alpha,\beta)\in(0,1)^2\): **cannot** drive \(R\to 0\) for anisotropic \(X\).
- Only endpoints \(\alpha=0\) or \(\beta=0\) (→ S1) vanish.

### Mode D — field-dependent SC weights \(w(X)\)
- SymPy: \(w_g\theta_g I=w_f\theta_f X\) on anisotropic diag \(X\) ⇒ \(\lambda=1\) or \(\theta_f=0\).
- Numeric opt: best \(|R|\) stays \(>10^{-4}\)–\(10^{-2}\), never vanishes.

### Mode E — composite \(G\)
- \(G_{\mathrm{sp}}=h_g(\alpha I+\beta X)^2\) SPD on probes; single effective metric ⇒ S3.

### Mode F — densitized θ
- θ vs no-θ differ off \(X=I\); θ required (Jammer F16 / K4).

### Mode G — isotropic scalar analog all \(d\)
- Relative weight vanishes iff scale ratio \(=1\).

### Mode H — \(S_{\mathrm{grav}}=R\) match
- 50/50 random metrics: no match to \(h_g,h_f,(h_g+h_f)/2,h_g X\).

### Round-5 identity (prior; superseded as terminal)
- Cursor refuted Scratch’s mis-posed \(LDnM=-R\) (X-only framing). **AC R5:** that does **not** establish non-absorption; G-2 **not ratified**; return to G-4. Strike 90/90 from any packet.

---

## 3. Robust conclusion

| Question | Answer |
|---|---|
| Robust healthy solution for **action (N)**? | **None found** among tested rescues (literature + multi-mode compute); ghost status of (N) itself **undetermined** |
| Robust healthy solutions for **fermions in bigravity**? | **S1, S2, S3, S4** (S5 special cases) |
| Recommended for NTE / Gap-2? | **S2** (Melville–Noller rank-2 / effective vielbein) or **S3** (composite \(G\)); prefer these over pursuing (N) |
| Claim 3 / (N) ghost-free? | **Not established; (N) undetermined** (AC R5 holds posteriors at G-4) |

---

## 4. What was *not* a rescue

- Tuning \(\alpha,\beta\) or \(w(X)\) interior  
- Going to \(d=1\) (false hope: matrix id holds, ghost mechanism differs)  
- Partially massless graviton literature (no spinor-(N) fix)  
- Dropping θ weights (fails single-metric control)  
- D-matrix X-polynomial identity as *terminal* kill of (N) — **withdrawn as G-2** (AC R5); still shows no X-only rescue

---

## 5. Iteration log

1. Lit sweep → S1–S5 catalogued; (N) no-go confirmed externally for scalars.  
2. Sweep A–H run → no interior rescue of (N).  
3. Rechecked \(d=1\) proportionality → documented as non-rescue.  
4. Cross-checked against R5 → consistent with “no X-only rescue,” **not** with settled G-2.  
5. Stop: further modes would repeat S1–S4 or rebrand (N).  
6. **2026-10-20 amend:** AC R5 — soften (N) to **undetermined**; S1–S4 unchanged.

— Cursor Main, 2026-10-19; amended 2026-10-20.
