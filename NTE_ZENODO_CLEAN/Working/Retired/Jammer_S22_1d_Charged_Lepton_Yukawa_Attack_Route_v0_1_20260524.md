# Jammer: §22.1d charged-lepton Yukawa attack route v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **RATIO EXIT** — sunshine v0.1k signed off (`Handoff_Jammer_S22_1_Sunshine_Exit_Signoff_20260524`)  
**Script:** `Working/paper_s22_1d_charged_lepton_yukawa_numerics.py`  
**Parents:** §19.3 G₂→SU(3); Companion 13 D5 inverse; §22.1; Paper S2 $D_F$

---

## §0. Executive

| Target | Corpus anchor | v0.1 |
|--------|---------------|------|
| $Y_e$, $Y_\mu$, $Y_\tau$ | §22.1 open; §19.3 GUT relations | **Routes mapped** |
| $m_e$, $m_\mu$, $m_\tau$ | Observation inputs today | **GUT-ratio check** |

**Headline.** Charged leptons are the **G₂ singlet** in $7=1\oplus3\oplus\bar3$; quarks are the **triplet**. Leading colour factor $N_c=3$ gives Georgi–Jarlskog **$m_\ell/m_q=1/3$** at unification — new geometric origin in corpus (§19.3). Full $Y_e,Y_\mu,Y_\tau$ from $D_F$ / embedding depth remains **Programme S** (Paper S5 / spectral action).

---

## §1. Structural starting point (§19.3)

$$7_{\rm G_2}=1\oplus3\oplus\bar3 \quad\Rightarrow\quad \text{singlet}=\text{lepton},\;\text{triplet}=\text{quark}$$

At GUT-scale unification:

$$\frac{m_{\rm lepton}}{m_{\rm quark}}=\frac{1}{N_c}=\frac13.$$

**Georgi–Jarlskog relations (corpus):**

| Relation | GUT | RGE to EW (order) |
|----------|-----|-------------------|
| $m_\tau/m_b$ | 1 | ~0.8–1.2 |
| $m_\mu/(3m_s)$ | 1 | needs RGE |
| $m_e/(3m_d)$ | 1 | needs RGE |

Script §A: numeric spot-check at EW scale (illustrative, not closure).

---

## §2. Attack routes

### Route L1 — G₂ + RGE pipeline (fastest phenomenology)

| Step | Action |
|------|--------|
| L1-1 | Fix $m_t$ or $m_b$ anchor from corpus / obs |
| L1-2 | Apply $m_\ell/m_q=1/3$ at $M_{\rm GUT}\sim2\times10^{16}$ GeV |
| L1-3 | Run 1-loop SM RGE for $Y_e,Y_\mu,Y_\tau$ |
| L1-4 | Compare to $m_e,m_\mu,m_\tau$ — falsifier if order wrong |

**Deliverable:** `Jammer_Charged_Lepton_GUT_RGE_Check_v0_1` — **DONE** (2026-05-24).

### Route L2 — D5 / $(8\pi)^{-\delta_\ell}$ embedding depth — **BRACKET v0.1e**

Neutrinos: Majorana $(8\pi)^{1/3}$, Dirac $(8\pi)^{-1/3}$ → $\delta_\nu=\tfrac13$.

**Structural:** G₂ **singlet** line → $\delta_{\rm singlet}=\tfrac23$ (one extra inverse volumetric power vs $\sigma_1/\sigma_2$).

$$Y_\ell \sim (8\pi)^{-\delta_\ell},\qquad
\delta_\ell^{(g)}=\tfrac23+\text{(§19.4 overlap bracket)}.$$

**Deliverable:** `Jammer_S22_1e_Charged_Lepton_Embedding_Depth_L2_v0_1` — **DONE** (2026-05-24). Generation depths **not** closed; L4 $D_F$ or radiative tower next.

### Route L3 — Associator radiative (§19.4)

$$\delta y_{13}\sim y_3\times\langle\psi_0|\psi_2\rangle^2/(16\pi^2)$$

Extend to charged-lepton **texture zeros** (ψ₀ ⊥ σ₃) → Cabibbo + solar angle corrections.

**Status:** programme, not derivation.

### Route L4 — Spectral action $D_F$ heat-kernel — **DERIVED bracket v0.1f**

$D_F$ on $A_F=\mathbb{O}\oplus\mathbb{O}$ (S2-C-C) + $S^3$ spectrum → $\delta_n$ from $\mathcal{S}_n=(d_0/d_n)\mathcal{O}_{n,0}^{2r}$; $\delta_{\rm singlet}=2/3$ anchor.

**Deliverable:** `Jammer_S22_1f_DF_Heat_Kernel_Delta_L4_v0_1` — **DONE** (2026-05-24).

### Route L4b — Paper S5 PMNS + off-diagonal $D_F$ — **v0.1 DONE**

**Deliverable:** `Jammer_Paper_S5_PMNS_DF_Charged_Lepton_v0_1`. PMNS rotation alone does not split eigenvalues; off-diagonal $D_F$ required; $r=3$ → $m_{\tau}/m_{\mu}$ bracket. **Open:** $m_{\mu}/m_{e}$, $\mathrm{Tr}_F(D_F^4)$ tower.

---

## §3. Recommended sequence

```
L1 GUT+RGE check (numeric)  →  1 memo
L2 embedding depth conjecture + (8pi) powers  →  parallel Paper S5
L4 D_F full matrix  →  long arc
```

**Does not block:** chord, Λ, neutrino closures, ghost scan.

---

## §4. Falsifiers

| # | Test |
|---|------|
| F1 | $m_\tau/m_b$ incompatible with $1/3$ at $M_{\rm GUT}$ after consistent RGE |
| F2 | D5 inverse forces same $(8\pi)^{-1/3}$ for $Y_e$ as $Y_{\nu_2}$ without depth split |
| F3 | Claim full $Y_e,Y_\mu,Y_\tau$ closed without $D_F$ or RGE anchor |

---

## §5. Corpus patch (§22.1 one-liner)

> **Charged-lepton programme (Jammer v0.1d, 2026-05-24):** leading route = G₂ singlet/triplet $\Rightarrow m_\ell/m_q=1/3$ at GUT (§19.3) + RGE; structural parallel to D5 inverse via embedding depth $\delta_\ell$ — open. Attack route: `Jammer_S22_1d_Charged_Lepton_Yukawa_Attack_Route_v0_1`.

---

— Jammer §22.1d v0.1, 2026-05-24.
