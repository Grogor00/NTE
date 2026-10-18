# VERDICT — S1/S2 retry (Cursor Main): adopt healthy couplings; (N) stays abandoned

**Landing:** **S1 default; S2 when one spinor must see both frames; (N) not revived.**  
**Prereg:** `Working\Opsi2_S1_S2_RETRY_PREREGISTRATION_CursorMain_…_20261019.md`  
**Compute:** `Working\Opsi2_S1_S2_RETRY_COMPUTE_CursorMain.py` → `…_RESULTS.json`  
**No Core.** Aligns with Gap-2 deep lit (Melville–Noller partial prior art) and Opsi2 solution map.

---

## 1. Constructions

**S1 (single metric):**
\[
S_\psi=\int\sqrt{|g|}\,\bar\psi\,i\gamma_{(e)}\!\cdot\!D^{(e)}\psi
\]
(or \(f\) only). HR potential unchanged. One symplectic density \(\Sigma=\sqrt{\gamma_I}\); χ does not cross sectors.

**S2 (rank-2 effective vielbein):**
\[
\tilde{e}=ae+bf,\quad a,b\ \mathrm{const},\quad
S_\psi=\int\det(\tilde{e})\,\bar\psi\,i\gamma_{(\tilde{e})}\!\cdot\!D^{(\tilde{e})}\psi.
\]
Single kinetic on \(\tilde{e}\) ⇒ single \(\tilde\Sigma\); no action-(N) relative residual.  
Literature: Melville–Noller [1511.01485](https://arxiv.org/abs/1511.01485) — Dirac MSS healthy for rank-2; full ADM ghost only above \(\Lambda_3\).

---

## 2. Compute results (this session)

| Check | S1 | S2 (\(a,b>0\)) | (N) |
|---|---|---|---|
| Relative \(R_j\) | **0** | **0** | \(h_g(\theta_g I-\theta_f X)^2\neq0\) |
| χ crosses two kinetics | **No** | **No** | **Yes** |
| K1 \(e=f\) | OK | \(\tilde{e}=(a+b)e\) OK | OK but residual structure differs |
| MSS lapse linear | trivial | **Yes** (\(Ñ\sim|a|N+|b|L\) at \(n=0\)); SPD \(\tilde\gamma\) for tested \(a,b>0\) | fails (shared π / two lapses) |
| Suite pass | **8/8** | **16/16 interior** | residual diagnostic nonzero; ghost status **undetermined** (AC R5 → G-4) |

Negative-\(b\) trials kept only if \(\tilde\gamma\) SPD; recommendation restricts to \(a,b>0\).

---

## 3. Adoption rule

| Need | Adopt |
|---|---|
| Fermion couples to one geometry | **S1** |
| One spinor must involve both frames | **S2** with \(a,b>0\) (canonical: \(a=b=1\)) |
| Naive double kinetic (N) | **Prefer not** — status **undetermined**; healthy replacements exist |

**NTE / Gap-2:** prefer **S2** (effective vielbein) over Claim-3’s (N) path — Gap-2 deep lit already flagged this as partial prior art; adopt as the working healthy route while (N)’s ghost question remains open (AC R5).

**Caveat (honest):** S2 inherits MN’s EFT cut-off (ghost in full ADM above \(\Lambda_3\)). Acceptable for the same reason bosonic rank-2 couplings are used: the healthy window is the EFT below \(\Lambda_3\). Full nonlinear ADM for Dirac-on-\(\tilde{e}\) remains incremental future work, not a blocker to abandoning (N).

---

## 4. Standing

**(N) undetermined** (AC R5: G-2 not ratified; return to G-4). S1/S2 = healthy replacements, computationally verified against the (N) residual diagnostic — they stand regardless of (N)’s eventual fork. P04 unchanged. No Core.

**Amendment 2026-10-20:** Softened per `RULING_AC_Round5_G2_Not_Ratified_…`.

— Cursor Main, 2026-10-19; amended 2026-10-20.
