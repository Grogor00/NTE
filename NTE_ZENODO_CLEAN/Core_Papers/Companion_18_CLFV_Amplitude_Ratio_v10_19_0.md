---
title: "CLFV amplitude ratio A(μ→eγ)²/A(τ→eγ)² = tan²θ₂₃ from R-matrix freezing"
author: "G. White"
date: "2026-08-03 (v10.19.0 companion)"
---

*Independent Researcher, Auckland, New Zealand*

*Email: gregwhite00@gmail.com*

*Corpus version: NTE v10.19.0 (draft). Companion 18. Rewritten from `New folder/Paper_P4_CLFV_…_v0_2_20260622.md` for Core deposit. Pedagogical twin: `Pedagogical_Notes/Paper_P4_Pedagogical_Note_v10_19_0.md`.*

---

## Scope

Maximal atmospheric mixing $\theta_{23}=\pi/4$ is **inherited** (Lam 2001; Harrison–Perkins–Scott 2002; Mohapatra–Nishiura; Grimus–Lavoura) — credited, not claimed. CLFV *ratios* as flavour-model discriminators are also prior art (Mohapatra et al. hep-ph/0211068; Joshipura–Rindani; SUSY-seesaw/SO(10) literature).

**This companion's increment:** a clean amplitude-level relation

$$\frac{\lvert A(\mu\to e\gamma)\rvert^{2}}{\lvert A(\tau\to e\gamma)\rvert^{2}}=\tan^{2}\theta_{23}$$

that follows when a discrete $Z_2$ on a quasi-degenerate heavy Majorana pair freezes the Casas–Ibarra $R$-matrix from $O(2,\mathbb{C})$ to real $O(2)$, removing the usual seesaw CLFV model-dependence.

---

## 1. Setup

Type-I seesaw $m_\nu=-Y_\nu^\top M_R^{-1}Y_\nu\,v^2$. A heavy pair $(1,2)$ carries a real $Z_2$ exchange $N_1\leftrightarrow N_2$, enforcing degeneracy $M_1=M_2\equiv M$ and reality of the involution. At the light-mixing level this is the 2–3 ($\mu$–$\tau$) exchange whose atmospheric consequence is $\theta_{23}=\pi/4$ (inherited).

**Corpus cross-ref.** Companion 10's $\sigma_1\leftrightarrow\sigma_2$ residual symmetry is the same structural $Z_2$ at the heavy-mode Cartan reading. Generation *labels* of heavy modes vs light generations remain under Item-1 dictionary work (Scratch/Jammer); the CLFV ratio itself is fixed by PMNS $\theta_{23}$ once $R$ is real, so it does not wait on that dictionary.

---

## 2. R-matrix freezing

Casas–Ibarra: $Y_\nu=\frac1v\sqrt{\hat M_R}\,R\,\sqrt{\hat m}\,U^\dagger$ with $R\in O(n,\mathbb{C})$ undetermined by oscillation data. CLFV amplitudes satisfy $A(\ell_i\to\ell_j\gamma)\propto(Y_\nu^\dagger Y_\nu)_{ji}$ (Hisano–Moroi–Tobe–Yamaguchi; Casas–Ibarra), so ratios are generically free.

Degeneracy sets $\hat M_R\big|_{(1,2)}=M\,\mathbb{1}$; the real $Z_2$ forbids the complex (boost-like) part of $R\in O(2,\mathbb{C})$. Hence $R\big|_{(1,2)}\in O(2,\mathbb{R})$, and $(Y_\nu^\dagger Y_\nu)_{e\mu}$, $(Y_\nu^\dagger Y_\nu)_{e\tau}$ are fixed by $\hat m$ and $U$ alone. Common factors cancel between channels:

$$\frac{\lvert A(\mu\to e\gamma)\rvert^{2}}{\lvert A(\tau\to e\gamma)\rvert^{2}}=\tan^{2}\theta_{23}.$$

Unity at $\theta_{23}=\pi/4$.

*(Deposit note: the New-folder draft flagged a pre-send import of channel-by-channel numerics into §4.3. The closed-form collapse under real $R$ is the load-bearing claim; explicit numerical confirmation remains a cross-check, not a substitute.)*

---

## 3. Six qualifiers (travel with the claim)

1. **Single relation** — one ratio, not a full flavour prediction.
2. **Conditional on observation** — fires only if CLFV is seen in both channels.
3. **Amplitude level** — full branching ratios carry lepton-mass powers that distort the simple ratio.
4. **~9:1 vs anarchy** — Monte Carlo over random Casas–Ibarra matrices hits a ratio this close ~once in ten; substantial, not overwhelming.
5. **Unobservable at the preferred scale** — at $M_R\approx8.2\times10^{14}$ GeV, BR$(\mu\to e\gamma)\sim4\times10^{-59}$ vs MEG II $\sim10^{-13}$.
6. **±2–3% width** — subleading degeneracy breaking.

---

## 4. Falsifiers

1. If both CLFV channels are resolved and the measured amplitude-squared ratio departs significantly from $\tan^2\theta_{23}$ (at the measured $\theta_{23}$), the $Z_2$-degeneracy mechanism fails — gated by qualifier 5.
2. Precision $\theta_{23}$ / octant (DUNE/Hyper-K) against subleading $Z_2$ breaking.
3. Narrow $0\nu\beta\beta$ window (few meV) as a related real-$R$ structural consequence (cross-check register).

---

## 5. Relation to other companions

| Companion | Relation |
|---|---|
| **7** | Unresolved-neutrino / Majorana ontology; $\sigma$ eigenmodes |
| **10** | $\sigma_1\leftrightarrow\sigma_2$ residual; $M_1$ scale |
| **13** | Yukawa / solar-leg branch |
| Part 3 falsifiability #6 | Points here |

---

## References

1. C. S. Lam, Phys. Lett. B **507**, 214 (2001).
2. P. F. Harrison, D. H. Perkins, W. G. Scott, Phys. Lett. B **530**, 167 (2002).
3. J. A. Casas and A. Ibarra, Nucl. Phys. B **618**, 171 (2001).
4. J. Hisano et al., Phys. Rev. D **53**, 2442 (1996).
5. R. N. Mohapatra et al., hep-ph/0211068 — CLFV ratios as discriminators (prior art).
6. I. Esteban et al. (NuFIT 6.0), JHEP **12**, 216 (2024).

---

*Companion 18 · NTE v10.19.0 · G. White · 2026-08-03*
