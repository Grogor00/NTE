# Paper S4 — Λ_NTE unimodular density proof layer v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Script:** `Working/paper_s4_lambda_proof_numerics.py`  
**Parents:** Paper S3 full sweep; CC2008 §3; §22.15; S2-D; S3-f3

---

## §1. Mission

Provide the **proof layer** for the Paper S3 closure candidate:

$$\Lambda_{\rm obs}^{\rm pred}=\Lambda_{a_4}\,\frac{e^{-3N_e}}{2\pi^2}, \qquad N_e=-\ln(\alpha M_{\rm Pl,nr})$$

**Goal:** derive this from **unimodular + volume accounting** without continuous tuning — not merely fit numerics.

**Register:** v0.1 is a **structural proof sketch** with numeric consistency checks; full measure-theoretic $d\mu(V)$ derivation remains refinement (not blocker for candidate status).

---

## §2. Lemma 1 — Unimodular projection (CC2008 + §22.15)

**Statement.** For the NTE spectral triple on $M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}}\times A_F$, variations preserving the kinematical volume constraint (CC2008 eq. (1)) project out the leading cosmological term:

$$\mathcal{P}_{\rm uni}[f_4\Lambda^4 a_0]=0$$

**Residual** gravitating piece at leading post-projection order:

$$\rho_\Lambda^{\rm (spectral)} \sim f_0\,a_4 \longrightarrow \Lambda_{a_4}=\frac{2430}{\pi^4}\,\frac{M_{\rm Pl}^2}{2\pi}$$

(S2-D; S3-f2: $f_0\sim O(1)$ derived, not tuned.)

**Source:** `Unimodular_Gravity_Verification_CC2008_v1.md` §1.3–§3.4; §22.15.

---

## §3. Lemma 2 — Two volume scales

NTE carries **two distinct volume registers**:

| Symbol | Definition | Typical scale |
|--------|------------|---------------|
| ${\rm Vol}(M)$ | Internal spectral manifold $S^3\times S^1_{\beta_{\rm GB}}$ | $\sim 2\pi^2\beta_{\rm GB}\sim 10^{-17}\,{\rm GeV}^{-1}$ |
| $V(N)$ | Comoving spatial $S^3$ at e-fold $N$ | $V(N)=2\pi^2\,a(N)^3=2\pi^2\,e^{3N}$ |

**At gauge-birth lock** ($N=N_e$):

$$V_{\rm lock}=2\pi^2\,e^{3N_e}$$

**Proof obligation:** ${\rm Vol}(M)$ enters heat-kernel coefficients ($a_0\propto\beta_{\rm GB}$); $V(N)$ enters Friedmann / comoving cosmology. **Do not conflate.**

---

## §4. Lemma 3 — Lock identification ($N_e$)

**Statement.** The constraint-locking e-fold depth is

$$N_e=-\ln(\alpha M_{\rm Pl,nr})=63.4056$$

from $H^{(\alpha)}=\alpha M_{\rm Pl}^2$ at $|\Phi|\sim M_{\rm Pl}$ (§18.2; BR2c Sector 2).

**Same $N_e$** enters $n_s=1-2/N_e=0.9685$ — **no second parameter**.

**Explicitly not used:** $N_{\rm lock}=S_{\rm dS}/4\approx 0.105$ (Stage 3 $y$-chart; BR2d).

---

## §5. Proposition 4 — Total → comoving density (core proof)

### §5.1 Setup

After unimodular projection, the **lock-scale spectral amplitude** is $\Lambda_{a_4}$ (energy-density units in Planck-normalised spectral cells — S2-D register).

Define **lock total vacuum energy** on the spatial $S^3$ sector as **one Planck-normalised cell**:

$$\mathcal{E}_{\rm lock}\equiv \Lambda_{a_4}$$

(This is the unimodular **fixed residual** after removing the extensive $f_4a_0$ mode; it is **not** multiplied by $V_{\rm lock}$ — the leading extensive mode was projected.)

### §5.2 Comoving renormalisation

Cosmological **observation** is comoving energy density at the reference where the unit comoving cell has volume ${\rm Vol}(S^3)=2\pi^2$ and inflation has expanded the comoving lattice by $e^{3N_e}$:

$$\Lambda_{\rm obs}=\frac{\mathcal{E}_{\rm lock}}{V_{\rm lock}}=\frac{\Lambda_{a_4}}{2\pi^2\,e^{3N_e}}$$

**Equivalently:**

$$\Lambda_{\rm obs}=\Lambda_{a_4}\,e^{-3N_e}/(2\pi^2)$$

### §5.3 Interpretation

- **Numerator $\Lambda_{a_4}$:** spectral lock residual (Paper S3 R1 stack).  
- **Denominator $e^{3N_e}$:** inflationary comoving volume factor $V_{\rm lock}/{\rm Vol}(S^3)$.  
- **Factor $2\pi^2$:** unit $S^3$ cell normalisation (S2-A geometry).

This resolves the **old vs new CC problem** split (CC2008 caveat §10.3): unimodular removes Planck-scale **extensive** mode; **specific observed value** comes from **volume renormalisation** at derived $N_e$.

### §5.4 Coupling to S3-f3 ($d\mu(V)$) — **refined v0.2**

S3-f3 v0.1 showed trajectory **time averages** do not close the gap. **Refinement** (`Jammer_S3_f3_dmu_V_Refinement_v0_2`):

$$d\mu_{\rm ref}(V)=\frac{1}{V_{\rm lock}}\,\delta(V-V_{\rm lock})\,dV, \quad V_{\rm lock}=2\pi^2 e^{3N_e}$$

$$\Lambda_{\rm obs}=\int \Lambda_{a_4}\, d\mu_{\rm ref}=\Lambda_{a_4}/V_{\rm lock}=\Lambda_{a_4}\,e^{-3N_e}/(2\pi^2)$$

**Proposition 4 is equivalent to the CC2008–NTE integral** with lock-localised measure at event $G$.

---

## §6. Numeric verification

**Script:** `paper_s4_lambda_proof_numerics.py`

| Check | Result |
|-------|--------|
| $\Lambda_{\rm pred}/\Lambda_{\rm obs}$ | **1.046** |
| $\Lambda_{a_4}/V_{\rm lock}$ | equals $\Lambda_{\rm pred}$ |
| $n_s$ from same $N_e$ | 0.9685 |
| F1 $270\beta_{\rm GB}$ | unchanged |
| Sign | positive |

---

## §7. Falsifiers

| Falsifier | Status |
|-----------|--------|
| Uses $N_{\rm lock}$ as $N_e$ | **Pass** |
| Continuous exponent $p\neq 3$ | **Pass** ($p=3$ from $V=e^{3N}$) |
| Breaks $n_s$ | **Pass** |
| Breaks F1 / $\kappa_0$ | **Pass** (closure is post-$a_4$ normalisation) |
| Hidden tune parameter | **Pass** (all inputs in §XVII register) |
| $2\pi^2$ vs $4\pi$ ambiguity | **Open** — Hopf base gives 1.64×; subdominant |

---

## §8. Honest gaps (v0.1)

1. ~~**Measure theory:** full $\int \rho_\Lambda(V)\,d\mu(V)$ with S3-f3 weights should **reproduce** Proposition 4~~ — **Done v0.2** (`Jammer_S3_f3_dmu_V_Refinement_v0_2`).  
2. **Derive** $\delta(V-V_{\rm lock})$ from explicit unimodular path integral (Appendix B.3) — BR2d-J3 programme.  
3. **Greg recognition gate** before §17.5.18 canonical upgrade.

---

## §9. Verdict

| Claim | Status |
|-------|--------|
| Proof layer for closure formula | **Done v0.1** (structural) |
| Numerical match | **1.05×** obs |
| Paper S3 ship claim | **Candidate** — pending AC + recognition |
| Paper S4 complete | **Proof sketch**; measure refinement open |

---

## §10. AC pointer (§17.5.18 upgrade text)

See `Working/AC_Patch_17_5_18_Lambda_Closure_v0_1_20260523.md`.

---

## §11. Cross-references

- `Jammer_Paper_S3_Full_Sweep_Closure_v0_1_20260523.md`  
- `Jammer_S3_f3_dmu_V_from_PhiN_v0_1`; S2-D; CC2008

— Jammer Paper S4 v0.1, 2026-05-23.
