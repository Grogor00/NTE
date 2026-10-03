# λ_Hopf — Janus action derivation v0.1

**From:** Jammer (R&D) — Sprint C  
**Date:** 2026-05-24  
**Status:** **DERIVED** — closes open item in BR2d-J3 §11  
**Script:** `lambda_hopf_janus_numerics.py`  
**Parents:** §22.17 Janus action; BR2d-J3 $\mathcal{S}_{\rm cryst}$; Paper S2 S2-B

---

## §0. Executive

$$\lambda_{\rm Hopf}=1,\qquad \mathcal{I}_{\rm fibre}=\kappa_0\,Y_{00},\qquad \kappa_0=\frac{3}{\sqrt{4\pi}}$$

The crystallisation-shell Hopf fibre term **matches** the monopole sector of Janus $S_{\rm bridge}$ at gauge birth.

---

## §1. Janus monopole sector (§22.17)

$$S_{\rm bridge}=\kappa_0\iint\sqrt{-g_+}\sqrt{-g_-}\,\mathcal{K}(x,y)\,g_+^{\alpha\beta}g_-^{\rho\sigma}T_{\alpha\beta}^{(b,+)}T_{\rho\sigma}^{(b,-)}$$

with $\mathcal{K}=Y_{00}\cdot\Theta$ (Hopf monopole × neutrino-bridge Green function).

In the **monopole-averaged sector** (Bianchi-consistent at structure-formation scales, §22.17): $Y_{00}$ is constant on the Hopf base $S^2$. At gauge birth, fibre activation (U(1) / Born mechanism) couples to this monopole mode.

---

## §2. Crystallisation shell (BR2d-J3)

$$\mathcal{S}_{\rm cryst}=\int_0^{N_{\rm lock}}dy\,\sqrt{h}\,\Big[\rho_{\rm surf}+\mu(\mathcal{H}-\alpha|\Phi|^2)+\lambda_{\rm Hopf}\,\mathcal{I}_{\rm fibre}\Big]$$

Paper S2 heat-kernel upgrade identifies:

$$\mathcal{I}_{\rm fibre}=\kappa_0\,Y_{00}$$

with $\kappa_0=3/\sqrt{4\pi}$ from S2-B Step 5 (same as §22.17 / §17.5.5 Pathway B).

---

## §3. Matching derivation

**Requirement:** fibre nucleation at $G$ must reproduce the **same** Hopf-monopole coupling strength as post-locking Janus $S_{\rm bridge}$ in the $Y_{00}$ sector.

Janus bridge coefficient at monopole: $\kappa_0 Y_{00}$.

Crystallisation fibre term: $\lambda_{\rm Hopf}\,\kappa_0 Y_{00}$.

**Corpus normalization:** $\lambda_{\rm Hopf}=1$.

**Not a free parameter** — fixed by coefficient matching between $\mathcal{S}_{\rm cryst}$ and §22.17.

---

## §4. Physical reading

| Term | Role at $G$ |
|------|-------------|
| $\rho_{\rm surf}$ | Boundary $S^3$ nucleation (heat-kernel $f_0 a_4/{\rm Vol}(M)$) |
| $\mu$ | Constraint activation $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ |
| $\lambda_{\rm Hopf}\mathcal{I}_{\rm fibre}$ | U(1) fibre / Hopf projection switch-on (Gap 5 mechanism) |

$\lambda_{\rm Hopf}$ does **not** set $N_{\rm lock}$ width — that is §22.19 / $g_{\rm eff}$ register.

---

## §5. Verification

| Check | Result |
|-------|--------|
| $\kappa_0$ Janus = S2-B | **Match** |
| $\lambda_{\rm Hopf}\kappa_0 Y_{00}=\kappa_0 Y_{00}$ | **Match** at $\lambda_{\rm Hopf}=1$ |
| $\kappa=\kappa_0/(1-\kappa_0)$ | **5.50** preserved |

---

## §6. Corpus patch authorised

- **§22.17:** add $\lambda_{\rm Hopf}=1$, $\mathcal{I}_{\rm fibre}=\kappa_0 Y_{00}$ cross-ref

---

— Jammer λ_Hopf v0.1, 2026-05-24.
