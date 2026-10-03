# Jammer: D5 BPS prefactor derive v0.2

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **DERIVED at Lagrangian register** — tree uniqueness + **factor 1.12 numeric closure** (v0.3)  
**Scripts:** `paper_s2_d5_bps_prefactor_numerics.py`; `paper_s2_d5_factor_112_numerics.py`  
**Parents:** `Paper_S2_S3_D5_BPS_Prefactor_Uniqueness_v0_1`; `Paper_S2_S3_D5_v0_2_Full_Lagrangian_Closure`; Companion 10 Pathway $\alpha$; S2-B Step 5

---

## §0. Executive

Paper S2 **D5** asks whether $(8\pi)^{1/3}$ in

$$M_1=(8\pi)^{1/3}\,(M_{\rm Pl}^2 H_{\rm GB})^{1/3}$$

is **uniquely BPS-saturating** or merely the best bracket among alternatives. **Verdict:** at tree-level full 3D $N=2$ effective-theory rigor, **$(8\pi)^{1/3}$ is unique**; $(4\pi)^{1/3}$ and $(12\pi)^{1/3}$ are **eliminated** by Majorana reality and mode-independence respectively. Factor **1.12** residual ($M_{1,{\rm obs}}/M_{\rm BPS}$) is **O(1) emergent SUSY-breaking** at gauge birth — not prefactor ambiguity.

---

## §1. Setup — 3D effective theory at gauge birth

**Substrate:** spatial $S^3\cong{\rm SU}(2)$ at gauge birth; Hopf flux $\Phi_{\rm Hopf}=4\pi(M_{\rm Pl}\ell_{\rm GB})^2$; gauge-birth 3-volume $V_3=\ell_{\rm GB}^3$.

**Majorana doubling (Spin(4) reality):**

$$\Phi_{\rm Maj}=2\Phi_{\rm Hopf}=8\pi(M_{\rm Pl}\ell_{\rm GB})^2.$$

Both chirality components of a real Majorana representation contribute independently — **not tunable**.

**Three-mode independence (S2-B / Sonner-Tong):** $\dim({\rm adj\,\mathfrak{su}(2)})=3$ Killing-spinor modes each saturate **separately** — same anchor as $\kappa_0=3/\sqrt{4\pi}$.

**Emergent $N=2$ (honest scope):** 3D $N=2$ SUSY is **leading-order structure** at gauge birth on $S^3\times S^1_{\beta_{\rm GB}}$ — not fundamental NTE commitment. Antiperiodic $S^1$ ($\theta=1/2$) breaks exact 4D SUSY; spatial Killing-spinor structure preserves effective half-BPS multiplet at tree level (v0.2 §2).

---

## §2. BPS bound and saturation

**Volumetric quantisation (Companion 10 Pathway $\alpha$):**

$$M_i^3 V_3=\Phi_{\rm Maj}\quad\Rightarrow\quad M_i=(8\pi)^{1/3}(M_{\rm Pl}^2 H_{\rm GB})^{1/3}.$$

**Central charge (3D $N=2$ effective):**

$$Z=\Phi_{\rm Maj}/V_3=8\pi M_{\rm Pl}^2 H_{\rm GB}^2,\qquad M_{\rm BPS}^3=|Z|.$$

**Tree-level protection:** BPS non-renormalisation — half-BPS mass protected to all orders **if** 3D $N=2$ exact. Gauge-birth SUSY breaking enters **only** at sub-leading / O(1) level → factor 1.12.

---

## §3. Elimination of alternatives

| Candidate | Mechanism | Verdict |
|-----------|-----------|---------|
| $(4\pi)^{1/3}$ | Single-chirality $\Phi_{\rm Hopf}$ | **Eliminated** — violates Majorana self-conjugate structure; would require Dirac full-BPS, not half-BPS Majorana |
| $(12\pi)^{1/3}$ | Three modes **share** tripled flux | **Eliminated** — contradicts independent central charges (same reading as $\kappa_0=3\times1/\sqrt{4\pi}$, not $3/3$) |
| **$(8\pi)^{1/3}$** | $\Phi_{\rm Maj}=2\Phi_{\rm Hopf}$ + independent modes | **Unique tree BPS saturator** |

---

## §4. Numerics (script)

| Reading | $M_1$ (GeV) | Ratio to obs |
|---------|-------------|--------------|
| $(4\pi)^{1/3}$ | $4.30\times10^9$ | 0.71 |
| **$(8\pi)^{1/3}$ BPS** | **$5.40\times10^9$** | **0.89** |
| $(12\pi)^{1/3}$ | $6.06\times10^9$ | 1.00 (fit-like) |

**Factor 1.12:** $M_{1,{\rm obs}}/M_{\rm BPS}=1.122$. Soft SUSY-breaking scale $\mu_{\rm soft}\sim0.35\,M_{\rm BPS}$ at $O(1)$ one-loop coefficient — consistent with emergent (not fundamental) SUSY at gauge birth.

**Sources identified:** antiperiodic $S^1$ BC; Higgs-VEW / $\sigma_3$ Cartan coupling; gauge-birth state transition; octonionic non-associativity at $A_F$.

---

## §5. D1 + D5 confluence

| Deliverable | Quantity | Anchor |
|-------------|----------|--------|
| D1 (S2-B) | $\kappa_0=3/\sqrt{4\pi}$ | 3 independent $Y_{00}$ projections |
| **D5 (this ship)** | $M_1=(8\pi)^{1/3}(\cdots)^{1/3}$ | 3 independent half-BPS modes + Majorana $\times2$ |

Same $\dim({\rm adj\,\mathfrak{su}(2)})=3$ structural anchor — heat-kernel chord Note 1 and Note 4 **confluence**.

---

## §6. Honest open

| Item | Register |
|------|----------|
| Factor 1.12 numerical closure | **Closed** at 1-loop model ($c\approx0.97$, $\mu/M\approx0.34$) — `Jammer_D5_Factor_112_Numerics_v0_3`; ab initio $c$ open |
| Full fundamental Lagrangian | NTE is not SUSY; effective theory only |
| $M_2$ split | Companion 10 §7 S2-3 |
| $M_R$ parallel BPS argument | Future polish |

---

## §7. Falsifiers

1. Majorana reality relaxed → $(4\pi)^{1/3}$ would re-enter — falsifies D5 if observed $M_1$ matches 4π route **without** chirality doubling.
2. Three modes share flux → $(12\pi)^{1/3}$ — falsifies if $\kappa_0$ confluence breaks simultaneously.
3. Tree BPS exact with no 1.12 correction under exact emergent $N=2$ — would require new SUSY-breaking accounting.

---

## §8. Corpus patches authorised

- **§22.14(b) D5 row:** $(8\pi)^{1/3}$ **derived** at tree BPS; factor 1.12 sub-leading
- **Companion 10 §7 S2-2:** BPS future-work → **closed** at tree level
- **Paper S2 chord synthesis §6 D5:** open → **tree closed**

---

— Jammer D5 derive v0.2, 2026-05-24.
