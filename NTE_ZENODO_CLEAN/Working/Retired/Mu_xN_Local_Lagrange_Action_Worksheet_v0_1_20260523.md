# μ(x,N) local Lagrange-multiplier action — worksheet v0.1 (§22.16 / Priority IV-1)

**Stream:** Cursor S1 scaffold → Jammer/Programme S closure  
**Date:** 2026-05-23  
**Status:** **Candidate action at S1 structural rigor** (parallel epistemic class to Gap 4b §22.17)  
**Master hooks:** §22.16, §17.5.3, Appendix B.3, §17.5.19

---

## §1. Mission

Derive the **action principle** for local Lagrange multiplier μ(x,N) that:

1. Extends Appendix B.3 cosmological μ(N) to **pointwise** enforcement of H(x,N) = β_NTE|Φ_NTE(x,N)|²  
2. Reproduces **Schwarzschild 1PN** time dilation as constraint consequence (§2.3), not ξR|Φ|² driver  
3. Remains compatible with bare action ξ = 1/6 + Higgs portal (§17.5.15, §22.14) and Janus action §22.17  

**Not claimed:** full covariant uniqueness; ghost-free proof; numerical PPN beyond 1PN.

---

## §2. Cosmological baseline (Appendix B.3 — closed)

$$S_{\rm cosmo} = V_3 \int dN \left\{ \mathcal{L}_{\rm eff}(N) + \mu(N)\,[H(N) - \alpha|\Phi_{\rm NTE}(N)|^2] \right\}$$

- μ(N) ≈ −V(Φ(N)) enforces constraint; V_NTE **consistency-only** (V_NTE Stage 1 S1.1)  
- α not derivable from boundary action (Appendix B.2 Fork B closed)  

**Extension ansatz:** promote μ(N) → μ(x,N), H(N) → H(x,N), |Φ|² → |Φ_NTE(x,N)|² with same constraint density.

---

## §3. Candidate local action (S1 closure target)

**Arena:** single 4D Lorentzian metric g_μν (post-locking; Janus sector decoupled at 1PN solar-system scale per §22.17 EFT note).

$$S_{\rm loc} = S_{\rm EH} + S_{\rm matter} + S_{\rm \Phi} + S_{\rm constr}$$

| Term | Form |
|------|------|
| $S_{\rm EH}$ | $\displaystyle\frac{M_{\rm Pl}^2}{2}\int d^4x\,\sqrt{-g}\,R[g]$ |
| $S_{\rm matter}$ | $\displaystyle\int d^4x\,\sqrt{-g}\,\mathcal{L}_{\rm SM+ν}$ (Path B SM Higgs separate) |
| $S_{\rm \Phi}$ | $\displaystyle\int d^4x\,\sqrt{-g}\left[-\tfrac12 K(\Phi)\,g^{\mu\nu}\partial_\mu\Phi_{\rm NTE}\partial_\nu\Phi_{\rm NTE} - V_{\rm NTE}(\Phi_{\rm NTE})\right]$ with $K=1$ (S2-C-A) |
| $S_{\rm constr}$ | $\displaystyle\int d^4x\,\sqrt{-g}\,\mu(x)\,\mathcal{C}(x)$ |

**Constraint density (primary):**

$$\mathcal{C}(x) \equiv \mathcal{H}(x) - \alpha\,|\Phi_{\rm NTE}(x)|^2 = 0$$

where $\mathcal{H}(x)$ is the **effective Hubble scalar** sourced by g_μν:

- **Homogeneous FRW limit:** $\mathcal{H} = \dot{a}/a = H(t)$ → recovers Appendix B.3  
- **Weak-field static:** $\mathcal{H}(x) = H_0\,[1 + \Phi_N(x)/c^2] + \mathcal{O}(\Phi_N^2)$ with $\Phi_N = -GM/rc^2$ → forces $|\Phi_{\rm NTE}|^2 = v_{\rm EW}^2[1 + \Phi_N/c^2]$ (§2.3 identity)

**Alternative (N-foliation):** if $N(x^\mu)$ is a scalar clock field with unit normal $n^\mu$, use $\mathcal{C} = n^\mu\nabla_\mu N \cdot H(N,x) - \alpha|\Phi|^2$ — ties to e-fold-primary ontology (Part 1 §2.1).

---

## §4. Variation sketch (deliverables checklist)

| Variation | Target equation | Status |
|-----------|-----------------|--------|
| $\delta g_{\mu\nu}$ | Einstein + $\mu\,\delta\mathcal{H}/\delta g_{\mu\nu}$ | **Open** — need explicit $\mathcal{H}[g]$ |
| $\delta \Phi_{\rm NTE}$ | Klein-Gordon + $-2\alpha\mu\Phi_{\rm NTE}$ | **Structural** — constraint slaved |
| $\delta \mu$ | $\mathcal{C}=0$ on-shell | **Closed** by definition |

**PPN 1PN check (required for S1 sign-off):**

1. Static weak field $g_{00} = -(1+2\Phi_N/c^2)$, $|\Phi_{\rm NTE}|^2 = v_{\rm EW}^2(1+\Phi_N/c^2)$  
2. $\tau(x)/\tau(\infty) = 1 + \Phi_N/c^2$ — matches §2.3  
3. $\gamma_{\rm PPN} = 1$, $\beta_{\rm PPN} = 1$ at leading order if $\mathcal{H}$ depends on $g_{00}$ only through standard ADM lapse  

**Script stub:** `Working/mu_xN_ppn_check.py` (Jammer/Cursor v0.2).

---

## §5. Relation to Janus action (§22.17)

- **κ / mirror sector:** §22.17 $S_{\rm bridge}$ + $S_{\rm cons}$ closed Gap 4b at monopole/averaged sector  
- **Local μ(x,N):** operates on **single-orientation** $g_{\mu\nu}$ at solar-system / FRW scales where Y₀₀ averaging applies  
- **Unification target (open):** single master $S = S_{\rm Janus} + S_{\rm constr}^{\rm local}$ with $\mu(x,N)$ enforcing H = β_NTE|Φ|² on each orientation's induced metric  

---

## §6. Relation to Connes / bare action

| Layer | Role |
|-------|------|
| Spectral action + ξ = 1/6 | Bare $\mathcal{L}_\Phi$ with $-\tfrac{1}{12}R\Phi^2$; **not** trajectory driver (§17.5.3) |
| μ(x,N) constraint | **Trajectory + local response** — orthogonal to ξR in vacuum ($R=0$) |
| Paper S2 K(Φ)=1 | Fixes kinetic term in $S_\Phi$ |

Paper S2 does **not** close μ(x,N); provides $S_\Phi$ normalization only.

---

## §7. Honest status

| Claim | Register |
|-------|----------|
| Candidate action form §3 | **S1 scaffold** — mirrors Gap 4b pattern |
| PPN 1PN from variation | **Not yet computed** — v0.2 |
| Uniqueness of $\mathcal{H}[g]$ | **Open** — multiple Hubble scalars exist; corpus picks one tied to §2.3.1 |
| Full S1 closure | **Jammer 2–3 sessions** per §22.16 estimate |

---

## §8. Cross-references

- `Papers/NTE_v10_17_Part3_Accounting.md` Appendix B.3; §22.16–§22.17  
- `Papers/depreciated/Gap_4b_Session_Audit_CrossThickness_Action_Principle.md`  
- `Working/LCDM_VNTE_Rho_Eff_Genuine_Test_Worksheet_v0_1_20260523.md` (V_NTE consistency layer)

— Cursor μ(x,N) v0.1, 2026-05-23.
