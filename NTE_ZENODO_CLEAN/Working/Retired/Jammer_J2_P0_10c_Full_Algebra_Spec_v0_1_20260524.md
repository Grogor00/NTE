# J2 — P0.10c $\omega_{\Phi_{\rm NTE}}$ on full $A=C^\infty(M)\otimes A_F$ v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **SPECIFIED at product-state register** — extends GNS scoped PASS; P0.10a/b still open  
**Script:** `Working/p0_10c_product_state_numerics.py`  
**Parents:** `Jammer_J2_P0_10_Scope_Memo_v0_1`; `P_dS3_Tomita_Takesaki_Modular_Flow_v0_1`; Paper S2 S2-A; BR2d-J3; §22.8

---

## §0. Executive

| Tier | Claim | Status |
|------|-------|--------|
| **J2 / P-dS3 GNS** | TT on $\pi(A_F)''$ | **PASS** (unchanged) |
| **P0.10c** | $\omega_{\Phi_{\rm NTE}}$ on $A=C^\infty(M)\otimes A_F$ | **SPECIFIED** (this memo) |
| **Modular flow** | $\sigma_t^{\omega_{\Phi_{\rm NTE}}}=\sigma_t^{\rm geom}\otimes\sigma_t^{\rm int}$ at factorisation register | **Derived** conditional on product state |
| **P0.10a/b** | Abstract TT on bare $\mathbb{O}\oplus\mathbb{O}$; crossed product without GNS | **OPEN** |

**Verdict:** P0.10c **closes the specification gap** identified in J2 scope memo §2. Corpus may cite **post-gauge-birth KMS state on full spectral triple** at prediction tier. Does **not** claim full dS/CFT or non-associative abstract algebra.

---

## §1. Algebra and Hilbert space

**Spectral triple (Paper S2 S2-A):**

$$M={\rm Hopf}\text{-}S^3\times S^1_{\beta_{\rm GB}},\qquad A=C^\infty(M)\otimes A_F,\qquad A_F=\mathbb{O}_+\oplus\mathbb{O}_-,\quad N_F=180.$$

**Representation:**

$$H=H_M\otimes H_F,\qquad H_M=L^2(M,S),\quad H_F=\mathbb{C}^{N_F},$$

$$\pi(a\otimes b)=\pi_M(a)\otimes\pi_F(b),\qquad \pi_F(A_F)\subset\mathcal{B}(H_F)\cong M_{180}(\mathbb{C}).$$

**von Neumann algebras (prediction tier):**

$$\mathcal{M}_{\rm int}=\pi_F(A_F)''=\mathcal{B}(H_F)\quad\text{(type I finite factor)},$$

$$\mathcal{M}_{\rm geom}=\pi_M(C^\infty(M))''\subset\mathcal{B}(H_M)\quad\text{(type II$_\infty$ in standard GNS)},$$

$$\mathcal{M}=\mathcal{M}_{\rm geom}\,\overline{\otimes}\,\mathcal{M}_{\rm int}\quad\text{(spatial tensor at gauge-birth register).}$$

Internal sector is **finite-dimensional matrix algebra**; all Tomita–Takesaki data on $A_F$ reduce to standard type-I quantum mechanics (GNS Task 1).

---

## §2. State specification $\omega_{\Phi_{\rm NTE}}$

### §2.1 Product form (post–gauge-birth register)

At **event $G$** (gauge birth / crystallisation; BR2d-J3), the physical state used for **modular predictions** is a **product state** on the factorisation $A=C^\infty(M)\otimes A_F$:

$$\boxed{\omega_{\Phi_{\rm NTE}}=\omega_{\rm geom}\otimes\omega_{\rm int}}$$

**Not** field identification $\sigma\leftrightarrow\Phi_{\rm NTE}$ (Paper S1 §7); **state** factorisation on the spectral triple.

| Factor | Object | Specification |
|--------|--------|---------------|
| **$\omega_{\rm int}$** | State on $A_F$ | GNS vector $|\Omega_F\rangle\in H_F$ cyclic for left multiplication $\pi_F(A_F)$; amplitude set by gauge-birth Born weight on unresolved internal modes (Companion 6–7) |
| **$\omega_{\rm geom}$** | State on $C^\infty(M)$ | KMS state at inverse temperature $\beta_{\rm GB}$ with respect to modular flow of geometry **after** $G$; fibre modulus $\beta_{\rm GB}=\sqrt{2\pi}/M_{\rm Pl,nr}$ (S2-A D9) |

**Action on $a\otimes b$:**

$$\omega_{\Phi_{\rm NTE}}(a\otimes b)=\omega_{\rm geom}(a)\,\omega_{\rm int}(b).$$

### §2.2 Pre-temporal register (honest)

**Before $G$:** $\omega_{\rm pre}$ is **not** KMS at fixed $\beta_{\rm GB}$ on the full algebra. Internal factor is generic / pre-Born (Companion 8 F2; Charter §2.5). Modular parameter $\beta$ labels $(\mathcal{A},\omega)$ algebraically; **no** ideal-gas temperature.

**At $G$:** BR2d-J3 $\mathcal{S}_{\rm cryst}$ selects support on crystallisation shell; $\omega_{\Phi_{\rm NTE}}$ **activates** as product KMS state above.

### §2.3 Link to $\Phi_{\rm NTE}$ (constraint sector)

Post-lock, pointwise constraint $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ (§22.16) fixes **geometric** thickness $\ell=1/H$. $\omega_{\rm geom}$ is the KMS state whose modular Hamiltonian **generates flow consistent with** fibre period $2\pi$ and Hopf scale $T_{\rm GB}=M_{\rm Pl,nr}/\sqrt{2\pi}$ — **not** the claim $\sigma_t=\partial_t$ cosmological time.

$\omega_{\rm int}$ carries flavour / unresolved-neutrino data; **orthogonal** to $\Phi$ magnitude at leading order on $A_F$ (Companion 7).

---

## §3. Modular automorphism on full $A$

### §3.1 Tensor product theorem (conditional)

If $\omega=\omega_1\otimes\omega_2$ on $\mathcal{M}=\mathcal{M}_1\overline{\otimes}\mathcal{M}_2$ with $\omega_i$ faithful normal states, then modular operator factorises:

$$\Delta_{\omega}=\Delta_1\otimes\Delta_2,\qquad \sigma_t^{\omega}=\sigma_t^{\omega_1}\otimes\sigma_t^{\omega_2}.$$

**Application:** $\sigma_t^{\omega_{\Phi_{\rm NTE}}}=\sigma_t^{\rm geom}\otimes\sigma_t^{\rm int}$ on $\mathcal{M}_{\rm geom}\overline{\otimes}\mathcal{M}_{\rm int}$.

### §3.2 Internal sector (closed)

On $\mathcal{B}(H_F)$, $\sigma_t^{\rm int}$ is standard Tomita–Takesaki flow of $\omega_{\rm int}$. CPN $\leftrightarrow$ modular conjugation $J_{\rm int}$ **PASS** (Scratch Task 1; Z₂ extension).

### §3.3 Geometric sector (programme layer)

$\sigma_t^{\rm geom}$ modular flow on $C^\infty(M)$ **not** computed ab initio in v0.1. **Identification layer** (P-dS3 R1): Gibbons–Hawking KMS parameter

$$\beta_{\rm dS}=\frac{2\pi}{H_{\rm GB}^{(F)}}$$

**scale-aligned** with F1 $\ell=1/H$ at $H_{\rm GB}^{(F)}$ (`p_ds3_modular_ds_link.py`; ratio $=1$).

**Fibre consistency:** $\beta_{\rm GB}T_{\rm GB}=\sqrt{2\pi}$ (D9 confluence) — same $2\pi$ normalisation as modular period on $S^1_{\beta_{\rm GB}}$.

---

## §4. Orthogonal registers (discipline)

| Counter | Object | Value | Role |
|---------|--------|-------|------|
| $N_e$ | Constraint locking depth | $\approx63.4$ | $n_s$, $\Lambda$ (BR5) |
| $N_{\rm lock}$ | Holographic chart width | $\approx0.105$ | $S_{\rm dS}/4$, $g_{\rm eff}$ (§22.19) |
| $N_F$ | Heat-kernel multiplicity | $180$ | $a_k$ on $M$ |
| $g_{\rm eff}$ | Thermal radiation dof | $106.75$ | $S_{\rm dS}$, $N_{\rm lock}$ |

**S2-NF1:** $N_F/2\neq g_{\rm eff}$ — **closed** (`Jammer_S2_NF1_g_eff_Thermal_Map_v0_1`). P0.10c does not conflate them.

---

## §5. Numerics (script)

`p0_10c_product_state_numerics.py` verifies:

1. $\beta_{\rm GB}T_{\rm GB}=\sqrt{2\pi}$  
2. $\beta_{\rm dS}/(2\pi\ell)=1$ at $H_{\rm GB}^{(F)}$  
3. $N_{\rm lock}=45/(4g_{\rm eff})$ vs naive $45/(2N_F)$ — 19% gap explained  
4. Product-state register: $\dim H_F=N_F$ type-I factor

---

## §6. What remains open

| ID | Gap |
|----|-----|
| **P0.10a** | Abstract TT on non-associative $A_F$ without GNS |
| **P0.10b** | $A_F\rtimes\mathbb{Z}_2$ crossed product on octonionic substrate |
| **P-dS3b** | $N_{\rm lock}=S_{\rm dS}/4$ from modular increment (§22.19 gives action route; modular increment proof optional) |
| **P-dS3c** | Horizon subalgebra entropy vs $S_{\rm GH}$ |

---

## §7. Falsifiers

1. Product-state ansatz fails: entanglement between geom and $A_F$ at $G$ forces **non-product** $\omega$ with different modular $\beta$ — would break §2.1.  
2. $\beta_{\rm dS}$ must use $H_{\rm GB}^{(\alpha)}$ to match $N_{\rm lock}$ — **excluded** (P-dS1 Route B).  
3. Claim P0.10 **fully closed** including P0.10a on bare $\mathbb{O}\oplus\mathbb{O}$ — **scope violation**.

---

## §8. Corpus patches authorised

**§22.8 addendum:**

> **P0.10c (Jammer v0.1, 2026-05-24).** Post–gauge-birth state on $A=C^\infty(M)\otimes A_F$ specified as $\omega_{\Phi_{\rm NTE}}=\omega_{\rm geom}\otimes\omega_{\rm int}$: internal factor GNS on $\mathbb{C}^{N_F}$ (type I; Task 1 PASS); geometric factor KMS at $\beta_{\rm GB}$ fibre register. Modular flow $\sigma_t^{\omega_{\Phi_{\rm NTE}}}=\sigma_t^{\rm geom}\otimes\sigma_t^{\rm int}$ at tensor factorisation. $\beta_{\rm dS}=2\pi/H_{\rm GB}^{(F)}$ scale-aligned with F1. Abstract non-associative TT (P0.10a/b) **open**. Memo: `Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1_20260524.md`.

**§22.20 / Paper S2 registry:** P0.10c → **specified**; $N_F\to g_{\rm eff}$ → **closed** (S2-NF1).

---

— Jammer P0.10c v0.1, 2026-05-24.
