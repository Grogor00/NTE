# O(ψ²) Dirac–Bergmann chain — VERDICT (Cursor Main, second lane)

**Landing: G-4 (undetermined).**  
**Directive:** `Handoffs\Directive_AC_to_Cursor_Run_Opsi2_Dirac_Bergmann_Independently_Second_Construction_Lane_Blind_20261019.md`  
**Prereg:** `Working\Opsi2_Dirac_Bergmann_PREREGISTRATION_CursorMain_Blind_To_Scratch_Second_Lane_20261019.md`  
**Prior art:** `Working\Opsi2_PRIOR_ART_FETCH_CursorMain_AKMS_HR2015_dRHR_Chain_Not_Done_20261019.md`  
**Blind to Scratch Opsi2 throughout.** Jammer K0/F1–F9 binding. **No Core. No f.**

---

## 0. One-line

| Item | Result |
|---|---|
| Prior art | Chain **not** done externally → computation proceeds |
| K0 | **Pass** (method reduces to HR 1111.2070 / vierbein HR at ψ=0) |
| Sector (a) matter–matter ∂δ | **Closes on total \(C_i^{(\psi)}\)** in controlled probes (lemma below) — F2 alone is **not** G-2 |
| Sector (a) gravity–Dirac cross ∂δ + HR absorption | **Blocked** |
| Sector (b) \(\{\mathcal{S}^{(\psi^2)},H\}\) | **Blocked** (needs (a) closed in the full theory) |
| Fork | **G-4** |

---

## 1. K0 — pure HR control

**Method:** ADM + HR shift-like variables \(n^i\) as in Hassan–Rosen [1111.2070](https://arxiv.org/abs/1111.2070); constraints \(C_g,C_f,C_i\); Dirac–Bergmann preservation.

At \(\psi=0\): \(C_g^{(D)}=C_f^{(D)}=0\), \(\Sigma\)-matter sector absent. Bracket technology and secondary \(\mathcal{S}^{(0)}\) reduce exactly to the pure bimetric proof (1111.2070 §§3–4 and the vierbein form of Hinterbichler–Rosen). Derivative-of-δ parts are handled by the same HR mechanism that already deals with \(\{C_g,C_g\}_{\partial\delta}\) carrying the *g*-momentum density alone.

**K0: pass.** Downstream results are eligible.

---

## 2. Setup at \(O(\psi^2)\) (action N)

\[
C_g=C_g^{(0)}+C_g^{(D)},\quad
C_f=C_f^{(0)}+C_f^{(D)},\quad
C_i=C_i^{(g)}+C_i^{(f)}+C_i^{(\psi)}.
\]

Symplectic factor from the Legendre transform of (N):

\[
\Sigma=\Sigma_g+\Sigma_f,\qquad
\Sigma_g=\sqrt{\gamma_g}\,A_g(\Lambda_{\mathrm{rel}}),\quad
\Sigma_f=\sqrt{\gamma_f}\,A_f(\Lambda_{\mathrm{rel}}).
\]

Dirac brackets: \(\{\psi_\alpha(x),\psi_\beta^\dagger(y)\}_D=-i(\Sigma^{-1})_{\alpha\beta}\delta^3(x-y)\).

Smeared matter Hamiltonians (schematic, masses in \(\mu\)):

\[
H_g[N]=\int N\,\psi^\dagger K_g\psi,\quad
H_f[M]=\int M\,\psi^\dagger K_f\psi,\quad
K_s=-i\alpha_s^j\partial_j+\mu_s.
\]

Grassmann bilinears treated as bosonic \(O(\psi^2)\); fundamental brackets restore \(O(\psi^2)\) in \(\{H_s,H_{s'}\}\) (F6 noted).

**Not used:** S2/S3 D2 labels (F8). Ultralocal \(\Delta\mathcal{S}\not\equiv 0\) is *consistent* with a modified secondary existing but is **not** a premise that the secondary is lost.

---

## 3. Sector (a) — derivative-of-δ

### 3.1 Lemma M1 — matter–matter ∂δ closes on total \(C_i^{(\psi)}\)

**Statement.** For shared \(\Sigma\) and \(H_g,H_f\) built as above, the ∂δ coefficients in \(\{H_g,H_g\}\), \(\{H_f,H_f\}\), and \(\{H_g,H_f\}\) are functionals that **vanish whenever the canonical Dirac momentum density \(C_i^{(\psi)}\) vanishes**, in all controlled probes below. They do **not** require \(C_i^{(D,g)}\) or \(C_i^{(D,f)}\) separately to vanish.

**Why this matters for F2 / K0.**  
S3-style dismissal of \((C_i^{(D)}(x)+C_i^{(D)}(y))\partial\delta\) as weakly zero on \(C_i\approx 0\) is **invalid reasoning** (partial momentum ≠ constraint). But replacing the coefficient by the *actual* matter–matter ∂δ current — which tracks **total** \(C_i^{(\psi)}\) — restores weak vanishing on the true diffeomorphism constraint. A G-2 landing that stops at “partial momentum appears in ∂δ” **fails K0’s spirit** and fails M1.

**Probes (discrete bilinear-operator PB on a periodic lattice; continuum limit not claimed as a proof, used as explicit configurations):**

| Config | \(C_i^{(\psi)}\) | \(\{H_g[N],H_g[M]\}_{\partial\delta\text{-channel}}\) | \(\{H_g,H_f\}\) |
|---|---|---|---|
| Amplitude-only \(\psi=\rho(x)\xi\), aligned | \(=0\) | \(\approx 0\) | \(\approx 0\) in ∂δ channel |
| Amplitude-only + **relative spatial rotation** of \(f\)-dreibein (\(\phi=0.7\)) | \(=0\) | \(\approx 0\) | ∂δ channel \(\approx 0\); **ultralocal** \(\{H_g[N],H_f[N]\}\approx 0.30\neq 0\) |
| Plane-wave control (single-metric) | \(\neq 0\) | nonzero, tracks canonical \(C\) not \(\psi^\dagger\alpha\psi\) | — |

**Explicit generic ultralocal witness (not φ₀=0, not isotropic metrics as the *decisive* ∂δ test):**  
relative rotation \(\phi=0.7\), \(\Sigma_g+\Sigma_f\) shared, amplitude-modulated spinor with \(C_i^{(\psi)}=0\), same smearing \(N=M=\sin(2\pi x/L_x)\):  
\(\{H_g[N],H_f[N]\}\simeq 0.297\neq 0\).  
This is an **ultralocal** \(\delta\)-sector signal (modified secondary / \(\Delta\mathcal{S}\) channel), **not** a ∂δ G-2 witness.

### 3.2 What is still blocked in (a)

To close sector (a) in the **full** theory one still needs:

| ID | Bracket / step | Status |
|---|---|---|
| **B1** | \(\{C_g^{(0)},C_g^{(D)}\}_{\partial\delta}\) and \(g\leftrightarrow f\) | **Uncomputed** |
| **B2** | \(\{C_g^{(0)},C_f^{(D)}\}_{\partial\delta}\) etc. (gravity–matter cross) | **Uncomputed** |
| **B3** | Assemble ∂δ parts of \(\{C_g,C_g\}\), \(\{C_f,C_f\}\), \(\{C_g,C_f\}\) **including HR potential + \(D\)-matrix / shift \(n^i\)** | **Uncomputed** |
| **B4** | Show the O(ψ²) residual (if any after B1–B3) **survives the same absorption mechanism that rescues pure HR** (K0-grade), and is not removable by shift multipliers or the first-class lapse combination | **Uncomputed** |
| **B5** | One explicit **continuum** 3+1d configuration (non-proportional \(\gamma_g,\gamma_f\), \(\Lambda_{\mathrm{rel}}\neq 1\), inhomogeneous \(\psi\)) with the residual written in closed form | **Uncomputed** (lattice probes are not a substitute) |

**Without B1–B4, G-2 is not reached.** M1 removes the cheap F2 route; it does not prove G-1.

---

## 4. Sector (b) — preservation of \(\mathcal{S}^{(\psi^2)}\)

\(\mathcal{S}^{(\psi^2)}\equiv\mathcal{S}^{(0)}+\Delta\mathcal{S}_{\mathrm{ultralocal}}\) is the *candidate* modified secondary **if** sector (a) closes.

| ID | Bracket | Status |
|---|---|---|
| **B6** | \(\{\mathcal{S}^{(\psi^2)},C_g\}\) and \(\{\mathcal{S}^{(\psi^2)},C_f\}\) at \(O(\psi^2)\) | **Blocked on B1–B4** |
| **B7** | Lapse-ratio coefficient nonzero on generic data (G-1) or vanishing (G-3 path) | **Blocked on B6** |

Ultralocal \(\{H_g,H_f\}\neq 0\) at relative rotation (probe) is **consistent** with \(\Delta\mathcal{S}_{\mathrm{ultralocal}}\neq 0\) but does **not** decide preservation.

---

## 5. Fork grading against prereg / Jammer minima

| Fork | Reached? | Why |
|---|---|---|
| G-1 | **No** | B1–B7 open; no dof count earned |
| G-2 | **No** | M1 undermines F2-only G-2; B1–B5 open; no continuum residual surviving HR absorption |
| G-3 | **No** | (a) not closed in full theory |
| **G-4** | **Yes** | Blocked brackets: **B1–B7** above |

**F-trap self-check:** F1 not used as decisive; F2 not committed; F3 not used as landing; F4 K0 done; F5 relative Lorentz kept live in probes; F6 noted; F7 residual dimension not misstated; F8 no D2 premise; F9 partial chain not sold as G-1/G-2.

---

## 6. Priors → posteriors (Cursor Main)

| Fork | Prior | Posterior | Note |
|---|---|---|---|
| G-1 | 0.15 | **0.25** | M1 makes clean matter ∂δ less hostile than feared |
| G-2 | 0.30 | **0.20** | Cheap F2 route closed; gravity–Dirac cross still live |
| G-3 | 0.10 | **0.10** | unchanged |
| G-4 | 0.45 | **0.45** | still the honest state of this lane after one round |

---

## 7. Standing vs Claim 3 / deposit

- **Claim 2** (lapse-linearity): untouched, sound.  
- **Claim 3** (ghost returns): remains **not established**. This lane did **not** establish ghost return; it **refuted** one insufficient argument for it (partial-momentum ∂δ) and named the brackets that still decide.  
- **P04 / N_eff / symmetric ν:** unchanged (directive).  
- **No Core edit.**

---

## 8. What would finish the lane

1. Compute B1–B4 in continuum 3+1d (symbolic ADM, not lattice).  
2. If ∂δ closes fully → compute B6–B7 → G-1 or G-3.  
3. If a residual survives HR absorption → G-2 with the continuum config (B5).

— Cursor Main, 2026-10-19. (Second construction lane, blind to Scratch.)
