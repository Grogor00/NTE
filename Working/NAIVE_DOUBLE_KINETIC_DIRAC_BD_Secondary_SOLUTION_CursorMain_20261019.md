# SOLUTION — Naive double-kinetic Dirac on two vierbeins: BD secondary **does not survive**; ghost-free completion named

**From:** Cursor Main · **To:** AC, Greg, Scratch, Jammer, PC · **Date:** 2026-10-19  
**Register:** Working / original analysis + sourced priors. **No Core.** Does not reopen S2/S3 landings.  
**Arises from:** Gap-2 deep lit (`DEEP_LIT_Dirac_Two_Vierbeins_…_20261018.md`) — Melville–Noller never wrote the *naive* case; Greg: work it and find a solution.

---

## 0. One-line answer

| Question | Answer |
|---|---|
| Does the BD **secondary** constraint survive for a Dirac field with **two independent kinetic terms**, one per vierbein? | **No.** |
| Does that mean the BD ghost returns? | **Yes** (one extra bosonic dof). |
| What is the ghost-free **solution** for Dirac matter that still “sees” both spin-2 fields? | Couple to **one** rank-2 **effective** matter vielbein \(\tilde{E}(E_g,E_f)\) — Melville–Noller [1511.01485](https://arxiv.org/abs/1511.01485) — **not** two independent kinetic terms. |

Primary lapse-linearity **holds** (Yamashita’s scalar mechanism is evaded). That is **not** enough: the secondary / relative-Lorentz sector fails.

---

## 1. The naive action (what Melville–Noller did not write)

Two dynamical vierbeins \(E_\mu{}^A\), \(F_\mu{}^A\) (Hassan–Rosen / Hinterbichler–Rosen), **one** Dirac spinor \(\psi\), **two** first-order kinetic terms:

\[
\boxed{
\begin{aligned}
S_\psi
&=
\int\mathrm{d}^4x\;\Big[
\det E\;\bar\psi\,i\,\gamma^A E_A{}^\mu D_\mu^{(E)}\psi
+
\det F\;\bar\psi\,i\,\gamma^A F_A{}^\mu D_\mu^{(F)}\psi
\Big]
\\[4pt]
&\quad
-\int\mathrm{d}^4x\;\Big[
m_E\,\det E\;\bar\psi\psi
+
m_F\,\det F\;\bar\psi\psi
\Big].
\end{aligned}
}
\tag{N}
\]

This is **not** Melville–Noller’s effective coupling
\[
S_{\mathrm{MN}}=\int\mathrm{d}^4x\;\det\tilde{E}\;\Big[\tfrac{i}{2}\tilde{E}^\mu{}_A\bar\psi\gamma^A\overset{\leftrightarrow}{\nabla}_\mu\psi-m\bar\psi\psi\Big],
\qquad
\tilde{E}=\tilde{E}(E,F).
\tag{MN}
\]

(N) = two kinetic metrics. (MN) = one kinetic metric built from both.

---

## 2. Primary sector — lapse-linearity **holds** (Cursor Main, elementary)

### 2.1 Single-tetrad reminder (Nelson–Teitelboim)

Time-gauge: \(E\cdot E_A{}^0 \propto \sqrt{\gamma}\). The product \(\det E\cdot E_A{}^0\) cancels the lapse in the time kinetic, so

\[
\pi_\psi \propto \sqrt{\gamma}\,\psi^\dagger,
\qquad
H_\psi = N\,\mathcal{H}_\perp[\gamma,\psi] + N^i\mathcal{H}_i,
\]

linear in \(N\). Standard; not claimed as novel.

### 2.2 Naive double kinetic — both lapses cancel independently

Each term in (N) cancels **its own** lapse:

\[
\pi_\psi
=
\sqrt{\gamma_g}\,A_g(\Lambda_{\mathrm{rel}})\,\psi^\dagger
+
\sqrt{\gamma_f}\,A_f(\Lambda_{\mathrm{rel}})\,\psi^\dagger,
\tag{1}
\]

\[
H_\psi
=
N_g\,C_g^{(\mathrm{D})}[\gamma_g,\gamma_f,\psi,\Lambda_{\mathrm{rel}}]
+
N_f\,C_f^{(\mathrm{D})}[\gamma_g,\gamma_f,\psi,\Lambda_{\mathrm{rel}}]
+
\text{(shifts)}.
\tag{2}
\]

**Contrast with scalar double kinetic** ([1408.0487](https://arxiv.org/abs/1408.0487); Soloviev [1505.00840](https://arxiv.org/abs/1505.00840) §5.3):

\[
\pi_\phi
=
\Big(\frac{\sqrt{\gamma_g}}{N_g}+\frac{\sqrt{\gamma_f}}{N_f}\Big)\dot\phi
\quad\Rightarrow\quad
H_\phi
\supset
\frac{\pi_\phi^2}{2\big(\sqrt{\gamma_g}/N_g+\sqrt{\gamma_f}/N_f\big)}
\quad\text{**nonlinear in both lapses**}.
\]

**Verdict (primary):** Yamashita’s \(1/N\) mechanism **does not fire** for (N). Both primary Hamiltonian constraints survive as coefficients of \(N_g,N_f\). **D3 excluded.** (Banked since Scratch ADM round 2026-10-08; re-derived here.)

### 2.3 Mini-superspace check (Cursor Main)

FLRW: \(N_g=N\), \(N_f=M\), scales \(a,b\), homogeneous \(\psi(t)\).

\[
L_\psi
=
\tfrac{i}{2}a^3\big(\bar\psi\gamma_0\dot\psi-\cdots\big)
+
\tfrac{i}{2}b^3\big(\bar\psi\gamma_0\dot\psi-\cdots\big)
-
N a^3 m_E\bar\psi\psi
-
M b^3 m_F\bar\psi\psi
+
\text{(spatial → 0 if homogeneous)}.
\]

After the primary \(\pi=\tfrac{i}{2}(a^3+b^3)\bar\psi\gamma_0\),

\[
H_\psi = N\,(a^3 m_E\bar\psi\psi) + M\,(b^3 m_F\bar\psi\psi)
\quad\text{(plus spin-connection / curvature pieces linear in }N,M\text{)}.
\]

Still linear in \((N,M)\). Mini-superspace **cannot** kill the ghost by itself when the failure is in the secondary / relative-Lorentz algebra — same lesson as pure HR needing the full ADM secondary, not just MSS lapse count.

---

## 3. Secondary sector — BD constraint **lost** (solution of the open question)

Hassan–Rosen remove the BD ghost by a **secondary** constraint \(\mathcal{S}\approx 0\) generated from \(\{C_g,C_f\}\) after the shift / square-root redefinition ([1111.2070](https://arxiv.org/abs/1111.2070)).

### 3.1 Why (N) enters that sector

- One spinor, two tetrads ⇒ only the **diagonal** local Lorentz acts on \(\psi\); the **relative** Lorentz \(\Lambda_{\mathrm{rel}}\) is no longer pure gauge in the matter sector (Hinterbichler–Rosen [1203.5783](https://arxiv.org/abs/1203.5783) logic + Dirac coupling).
- The symplectic factor \(\Sigma\) in (1) depends on \(\Lambda_{\mathrm{rel}}\).
- Spatial kinetics of the \(f\)-term, written with \(S=\sqrt{\gamma_g^{-1}\gamma_f}\), depend on **matrix elements** \(S^i{}_j\) contracted with spinor bilinears \(B_i{}^j\sim\bar\psi\gamma\,D\psi\) — **not** only on the elementary symmetric polynomials \(e_n(S)\) that the HR potential uses.

### 3.2 What was already computed (ratified — not reopened)

| Lemma | Setting | Landing |
|---|---|---|
| S2 | 2+1d, \(O(\psi^2)\) | **D2** — \(\Delta\mathcal{S}\not\approx 0\); W-3 closed |
| S3 | 3+1d, matrix \(S\), live DeWitt π | **D2** — B4/Term II+IV live; residual escape closed for documentation; chair ~92% |

Sources: `Working/P09_Gate0_Lemma_S3_VERDICT_Scratch_…_20261010.md`; `Handoffs/Arbitration_AC_Lemma_S3_D2_Ratified_…_20261010.md`.

**Cursor Main does not recompute \(\{\mathcal{S}^{(\psi^2)},H\}\).** The open external-literature question is answered by that ratified original work: for action (N),

\[
\boxed{
\Delta\mathcal{S}\;\not\approx\;0
\quad\text{on the generic constraint surface}
\quad\Rightarrow\quad
\text{BD secondary lost}
\quad\Rightarrow\quad
\text{ghost returns (12 phase-space dof vs 11)}.
}
\tag{★}
\]

Dof sketch (from Gate-0 secondary verdict): ghost-free HR + healthy Dirac = 11; lost secondary = 12 = BD ghost + Dirac.

### 3.3 Structural one-paragraph proof sketch (why ★ is not a fluke)

HR secondary identities use that variations of \(V(e_n(S))\) stay in \(\mathrm{span}\{\mathrm{d}e_n\}\). The Dirac correction \(\mathcal{F}^{(S\text{-matrix})}\propto S_j{}^i B_i{}^j\) lies **outside** that span for generic \(B\) (\(\dim\mathrm{Mat}_3=9\), \(\dim\mathrm{span}\{I,S,S^2\}\le 3\)). No \(\mathrm{Cl}(1,3)\) Fierz was found that projects \(B\) back into the HR class (S3). Therefore the pure-HR cancellation that produces \(\mathcal{S}\) does **not** inherit to (N).

---

## 4. The solution (constructive)

Naive double kinetic (N) is **not** a ghost-free matter coupling. Use one of:

### Solution A — **Effective rank-2 vielbein** (preferred if both metrics must source matter)

\[
\tilde{E}_\mu{}^A
=
\alpha\,E_\mu{}^A+\beta\,F_\mu{}^A
\quad\text{(or other rank-2 string; MN Table 1)},
\]
then couple Dirac **only** through \(\tilde{E}\) as in (MN).

- Mini-superspace: Dirac conditions (MN eqs. 4.16–4.21) satisfied for rank-2.
- Full ADM: ghost above \(\Lambda_3\) for non-minimal rank-2 (MN); healthy **low-energy EFT** up to that scale — same status as the standard effective-metric matter coupling ([1409.1909](https://arxiv.org/abs/1409.1909), [1408.1678](https://arxiv.org/abs/1408.1678)).
- **This is the spinor analogue of “matter on \(g_{\mathrm{eff}}\)”** — not a rediscovery of (N).

### Solution B — **Single-metric coupling**

Couple \(\psi\) to \(E\) only (or \(F\) only). Ghost-free by the standard HR+matter theorem (matter absorbed into one constraint). Loses bilateral / twin phenomenology.

### Solution C — **Two independent spinors**

\(\psi_g\) on \(E\) only, \(\psi_f\) on \(F\) only. Each copy is singly coupled ⇒ no Yamashita double-kinetic ghost from a shared field. Different model (two baths / two species) — **not** the shared-\(\psi\) reading.

### Non-solutions

| Proposal | Why it fails |
|---|---|
| “Lapse-linearity ⇒ ghost-free” | Only kills Yamashita’s **primary** mechanism; secondary still dies under (N). |
| Conformal rescaling of double kinetic | Does not restore HR \(e_n\)-class cancellation for matrix-\(S\) bilinears (prior conformal-matter check). |
| Mini-superspace-only health | Insufficient; secondary lives in the full algebra / relative Lorentz. |

---

## 5. Publishable claim map (external, non-NTE)

**Claim 1 (elementary, not novel alone):** First-order Dirac on one tetrad is lapse-linear (Nelson–Teitelboim).

**Claim 2 (elementary extension):** Naive double kinetic (N) remains **linear in both lapses**; Yamashita 1408.0487 does not apply verbatim.

**Claim 3 (original / gap fill):** Despite Claim 2, the Hassan–Rosen **secondary** constraint fails for (N) at \(O(\psi^2)\) because Dirac spatial kinetics source matrix-\(S\) channels outside \(\{e_n(S)\}\) and the relative Lorentz is matter-entangled — **BD ghost returns.**

**Claim 4 (solution):** Ghost-free Dirac “bimetric” matter = Melville–Noller **effective** vielbein (MN), or single-metric coupling — **not** (N).

External literature status after this note: Claim 3 is the gap Scratch flagged; the computation lives in the S2/S3 deposit of original work (2026-10-09/10). A clean arXiv note could package §§1–4 with the S3 algebra as the technical appendix.

---

## 6. Standing / fences

- Does **not** restore symmetric shared-\(\nu\) deposit (N_eff exclusion stands, independent).
- Does **not** reopen S2 W-3 or S3 D2.
- No κ, no Core, no foundation-map Step-4 entry of “ours.”
- Edge `EDGE_doubly_coupled_bd_ghost__fermionic_spinor_matter_two_metrics.md`: naive double-kinetic gap is **answered** (ghost); effective-vielbein branch remains MN-partial as filed 2026-10-18.

### Attribution hold (2026-10-19) — **Claim 3 / arXiv blocked**

AC reports **no record** of writing `Arbitration_AC_Lemma_S2_…` or `…_S3_…`. Provenance check (`Handoffs/Handoff_Cursor_Main_to_AC_Attribution_Lemma_S2_S3_…_20261019.md`): both are **likely Cursor_AC** under a wrong `Arbitration_AC_` filename; discipline-14 sweep renamed only Gate-0 and left S1–S3 unverified.

**Until Claude AC reads the S3 Scratch + Jammer bodies and adopts / revises / renames those arbitrations, Claim 3 must not be packaged for arXiv as “AC-ratified.”** Primary Claims 1–2 and Solution A (effective vielbein) stand independently of that ratification.

— Cursor Main, 2026-10-19.
