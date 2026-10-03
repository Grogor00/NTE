# Jammer: charged-lepton Route L1 — G₂ GUT + RGE check v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **1-loop numeric check** — not full Yukawa closure  
**Parent:** `Jammer_S22_1d_Charged_Lepton_Yukawa_Attack_Route_v0_1_20260524.md`  
**Script:** `Working/paper_s22_1e_charged_lepton_gut_rge_numerics.py`  
**Corpus:** §19.3 G₂→SU(3); §22.1 open list

---

## §0. Executive

| Step | Result |
|------|--------|
| G₂ singlet/triplet → $m_\ell/m_q=1/N_c=1/3$ at $M_{\rm GUT}$ | **Imposed** (Georgi–Jarlskog) |
| Quarks run **up** (QCD 1-loop) | $m_b,m_s,m_d$ at $M_{\rm GUT}$ |
| Leptons run **down** (QED 1-loop) | Compare to $m_\tau,m_\mu,m_e$ at $M_Z$ |
| **Test A** (obs → $M_{\rm GUT}$, check $m_\ell/(N_c m_q)$) | **τ/b 1.53**; **μ 0.79**; **e 0.08** at 1-loop |
| **Test B** (impose GUT → run down) | Illustrative only; sensitive to scheme |

**Verdict:** Route **L1 does not falsify** the §19.3 **geometric** origin (singlet/triplet → $1/N_c$); 1-loop running **does not close** $Y_e,Y_\mu,Y_\tau$. Next: 2-loop/threshold RGE or L2 $\delta_\ell$ / L4 $D_F$.

---

## §1. Pipeline

1. **Anchor:** $M_{\rm GUT}=2\times10^{16}$ GeV; PDG MS-bar $m_b(4.18)$, $m_s(0.093)$, $m_d(4.7\times10^{-3})$ GeV.
2. **At GUT:** $m_\tau=m_b$, $m_\mu=3m_s$, $m_e=3m_d$ (colour factor $N_c=3$ from $7=1\oplus3\oplus\bar3$).
3. **Running:** quarks ↑ QCD ($\beta_0$ for $n_f=4,5$); leptons ↓ QED (leading).
4. **Test:** $m_\ell^{\rm pred}(M_Z)/m_\ell^{\rm obs}$.

---

## §2. Numerics (1-loop)

Run: `python paper_s22_1e_charged_lepton_gut_rge_numerics.py`

**Test A (primary):** run PDG masses up to $M_{\rm GUT}=2\times10^{16}$ GeV; check Georgi–Jarlskog ratios.

| Ratio @ $M_{\rm GUT}$ | v0.1e (1-loop) | Target |
|------------------------|----------------|--------|
| $m_\tau/m_b$ | **1.53** | 1 |
| $m_\mu/(3m_s)$ | **0.79** | 1 |
| $m_e/(3m_d)$ | **0.08** | 1 |

**Interpretation.**

- **τ/b:** 1-loop overshoots unity but is **closer than EW** ($m_\tau/m_b\approx0.43$ at $M_Z$) — directionally supports GUT unification; not a closure.
- **μ:** within ~20% at 1-loop — promising; needs 2-loop polish.
- **e:** large deficit — **L2 embedding depth** or threshold programme required.
- **EW without RGE:** $m_\tau/m_b\approx0.43$, $m_\mu/(3m_s)\approx0.38$ — shows why GUT-scale test matters.

---

## §3. Falsifier table (L1)

| ID | Statement | v0.1 |
|----|-----------|------|
| F1 | τ sector wrong **order** at $M_{\rm GUT}$ (e.g. ratio $<0.3$ or $>3$) | **Not triggered** (1.53 at 1-loop) |
| F2 | All three match at 1-loop without extra structure | **Not claimed** |
| F3 | Same $(8\pi)^{-1/3}$ as $Y_{\nu_2}$ for $Y_e$ | **Still FAIL** (L2 needed) |

---

## §4. Corpus patch (§22.1 one-liner addendum)

> **L1 GUT+RGE (Jammer v0.1e, 2026-05-24):** Georgi–Jarlskog from §19.3 survives 1-loop τ check; $\mu,e$ need threshold/L2 — `Jammer_Charged_Lepton_GUT_RGE_Check_v0_1`.

---

## §5. Next

| Priority | Item |
|----------|------|
| 1 | L2: $\delta_e,\delta_\mu,\delta_\tau$ from $(8\pi)^{-\delta}$ embedding on $S^3$ |
| 2 | 2-loop / threshold RGE memo (optional numeric upgrade) |
| 3 | L4 $D_F$ — Paper S5 |

---

— Jammer L1 GUT+RGE v0.1, 2026-05-24.
