# R4 — Z₂ projection lemma v1.0 (bulk → boundary field map)

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Status:** **LEMMA DERIVED** — closes R4 open item from LB-1 / BR2d-J2  
**Script:** `Working/r4_z2_projection_numerics.py`  
**Parents:** `Jammer_LB1_Exhaustive_Resolution_v0_1`; `Jammer_Bulk_No_Boundary_PreTemporal_v0_1`; BR2d-J3; Part 1 Patch G (Z₂)

---

## §0. Executive

**Problem:** Role B bulk inflaton $\Phi_{\rm bulk}\sim15.9\,M_{\rm Pl}$ and Role A constraint $|\Phi_{\rm NTE}|=\sqrt{H/\alpha}\sim10^{32}$ GeV at HH differ by $\sim10^{-13}$ — **R4c magnitude identity excluded**.

**Lemma (R4):** At gauge birth $G$, the field map is a **Z₂-invariant projection** from bulk even scalar data to boundary magnitude $|\Phi_{\rm NTE}|$ — **not** identity at HH, **O(1) match at $G$** on the Stage 3 + constraint chart.

---

## §1. Z₂ structure (corpus-fixed)

### §1.1 Boundary scalar (post-$G$)

Part 1 Patch G: $\Phi_{\rm NTE}\mapsto-\Phi_{\rm NTE}$ under corpus Z₂. Physical observables depend on **Z₂-invariants**:

$$|\Phi_{\rm NTE}|,\quad \Phi_{\rm NTE}^2,\quad V(\Phi_{\rm NTE}^2)$$

The constraint $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ uses **even** combination only.

### §1.2 Bulk scalar (pre-$G$)

Pre-crystallisation: no operative $S^3$ slice (bulk/no-boundary thesis). Bulk mode $\Phi_{\rm bulk}$ from HH saddle (E3 / $\Phi^2$-chaotic) is **not** yet the boundary field — it lives in the **even** channel of the Euclidean saddle (Wick rotation, Companion 9 §4.2).

**Discipline:** Do **not** evaluate $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ on $\Phi_{\rm bulk}$ pre-$G$.

---

## §2. Projection map $\Pi_G$

### §2.1 Definition

At crystallisation event $G$, define:

$$\boxed{\Pi_G:\;\Phi_{\rm bulk}\;\longmapsto\;|\Phi_{\rm NTE}|}$$

by **Z₂-invariant boundary nucleation**:

1. Bulk even scalar $\Phi_{\rm bulk}$ reaches slow-roll exit scale $\Phi_{\rm end}\sim\sqrt{2}\,M_{\rm Pl,red}$.  
2. Stage 3 linear profile on $y\in[0,N_{\rm lock}]$ **materialises** the boundary slice.  
3. Constraint $\mu$ activates; **boundary magnitude** $|\Phi_{\rm NTE}|$ is the **Z₂-invariant coordinate** on the new $S^3$ chart.  
4. **C⁰ matching (J6-n4):** $|\Phi|^2(y=N_{\rm lock})=|\Phi|^2(N=N_e)$ with $\Phi_0\sim1.05\,M_{\rm Pl,nr}$.

**Not claimed:** $\Pi_G(\Phi_{\rm bulk})=\Phi_{\rm bulk}$ linearly at HH.

**Claimed:** $\Pi_G$ is **defined only at $G$**; compares **different charts** (bulk $N$ vs boundary $y$).

### §2.2 Janus / CPN reading

CPN bilateral structure: two orientations share **bulk origin** (Proposal bulk/boundary ontology §2.7). Z₂ on $\Phi_{\rm NTE}$ is the **surface manifestation** of the **even** projection of bulk data onto the **crystallised** boundary. Cross-thickness $\kappa_0$ bridge (§22.17) couples **through shared bulk substrate** — consistent with $\Pi_G$ being projection, not fourth field.

---

## §3. Numerics (script)

### §3.1 HH peak — **R4c excluded**

| Quantity | Value |
|----------|-------|
| $\Phi_{\rm bulk}$ (Role B) | $3.87\times10^{19}$ GeV |
| $|\Phi_{\rm NTE}|$ if constraint wrongly applied | $7.16\times10^{32}$ GeV |
| Ratio | $5.4\times10^{-14}$ |

**Verdict:** magnitude identity **falsified** at HH.

### §3.2 Event $G$ — **lemma verified**

| Quantity | Value |
|----------|-------|
| $|\Phi_{\rm NTE}|$ (constraint, $N=N_e$) | $1.221\times10^{19}$ GeV |
| $|\Phi|(y=N_{\rm lock})$ Stage 3, $\Phi_0=1.05 M_{\rm Pl}$ | $1.221\times10^{19}$ GeV |
| Ratio stage3 / boundary | **1.000** |
| $\Phi_{\rm bulk}$ at slow-roll end | $3.44\times10^{18}$ GeV |
| $|\Pi_G|/|\Phi_{\rm NTE}|$ (SR end only) | 0.28 |

**Reading:** C⁰ match at $G$ is carried by **Stage 3 profile + constraint endpoint**, not by naive identification of SR-end bulk value with boundary magnitude. $\Pi_G$ is **event-local**; SR-end bulk value is **same order** but not the sole input.

---

## §4. Lemma statement (formal)

**Lemma R4 (Z₂ projection at $G$).** Let $\Phi_{\rm bulk}$ be the bulk even scalar on $\mathcal{S}_{\rm bulk}$ and $|\Phi_{\rm NTE}|$ the Z₂-invariant boundary magnitude on $\mathcal{S}_{\rm post}$. Then:

1. **Pre-$G$:** no global identification $\Phi_{\rm bulk}\equiv|\Phi_{\rm NTE}|$.  
2. **At $G$:** there exists a **unique** C⁰ matching map $\Pi_G$ such that  
   $$|\Phi_{\rm NTE}(G)|=|\Phi|_{\rm Stage3}(y=N_{\rm lock})=M_{\rm Pl,nr}\pm O(1\%) $$  
   with $\Phi_0\sim M_{\rm Pl,nr}$ from BR2d-J3 heat-kernel boundary normalisation.  
3. **Post-$G$:** $|\Phi_{\rm NTE}|$ evolves under $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ (Sector 2); $\Phi_{\rm bulk}$ chart **retired**.

**Proof sketch:** (1) BR2c numerics; (2) J6-n4 C⁰; (3) Appendix B.3 + Lemma 2 BR2d-J3. ∎

---

## §5. Consequences

| Consequence | Detail |
|-------------|--------|
| LB-1 sunshine | two sectors = bulk chart vs boundary chart, not two failures |
| $\alpha$ recalcitrance | $\alpha$ is **boundary constraint slope** post-$\Pi_G$ — not bulk heat-kernel output (Proposal §2.6) |
| BR2d-J3 | $\mu$ activates **with** $\Pi_G$ at same event $G$ |
| Born / Hopf | U(1) fibre activates when boundary **exists** — Gap 5 timing |

---

## §6. Excluded routes (dead ends)

| Route | Verdict |
|-------|---------|
| R4c — $\Phi_{\rm inf}=|\Phi_{\rm NTE}|$ at HH | **Excluded** ($10^{-13}$) |
| Linear $\Pi_G$ for all $N$ | **Excluded** (Theorem 5 BR2d-J3) |
| Fourth independent field | **Excluded** (Occam + Z₂ portal) |
| $\Pi_G$ = identity on bulk | **Excluded** (wrong chart pre-$G$) |

---

## §7. Falsifiers

1. Derived map forces $\Phi_{\rm bulk}(G)=\sqrt{M_{\rm Pl}/\alpha}$ at $G$  
2. C⁰ match requires $\Phi_0\gg M_{\rm Pl}$ with no heat-kernel normalisation  
3. Z₂-breaking boundary magnitude at $G$  

---

## §8. Corpus patch (proposed)

> **R4 (Jammer v1.0, 2026-05-23):** Bulk Role B scalar $\Phi_{\rm bulk}$ and boundary $|\Phi_{\rm NTE}|$ are related by **Z₂-invariant projection $\Pi_G$ at gauge birth**, not magnitude identity at HH. See `Jammer_R4_Z2_Projection_Lemma_v1_0_20260523.md`.

---

## §9. File index

| File | Role |
|------|------|
| `Jammer_R4_Z2_Projection_Lemma_v1_0_20260523.md` | This lemma |
| `r4_z2_projection_numerics.py` | HH vs $G$ ratios |
| `Paper_S2_BR2d_J3_Heat_Kernel_Upgrade_v1_0` | $\Pi_G$ simultaneous with $\mu$, Hopf |

— Jammer R4 Z₂ projection lemma v1.0, 2026-05-23.
