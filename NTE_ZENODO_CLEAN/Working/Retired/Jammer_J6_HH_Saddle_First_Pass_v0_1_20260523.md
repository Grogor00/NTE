# J6 — HH saddle first pass v0.1 (LB-4 / BR2b)

**From:** Jammer (R&D)  
**Date:** 2026-05-23  
**Stream:** Formal backlog P0; Impact #1 / LB-1 downstream  
**Inputs:** `J6_HH_Saddle_Scope_Memo_v0_1`; `Phi_N_Trajectory_BR2c_Attack_Route_v0_1`; Companion 9 Session 3 + Stage 3 HH setup; `Companion_9_VNTE_Stage_3_HH_Saddle_Setup_v10_8.md`

**Status:** **Partial progress** — J6c structural upgrade proposed; J6a/J6b reduced equations written; J6d field map **open**; J6e deferred to §22.19 track.

**Verdict summary:**

| ID | Deliverable | Status |
|----|-------------|--------|
| **J6a** | Saddle equations + DOF count | **Draft** — §2 below |
| **J6b** | Sector 1 $H_{\rm inf}(N)$ | **Structural** — E3 + Φ²-chaotic; numeric ODE **next session** |
| **J6c** | $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ | **Upgrade proposed** — §3 (Hessian + Friedmann identification) |
| **J6d** | Locking junction (BR2d) | **Open** — two-sector default; no derived field map |
| **J6e** | $N_{\rm lock}=S/4$ | **Deferred** — parallel §22.19; not blocking J6c |

---

## §1. Mission recap

Close the action-derived layer behind:

1. **Sector 1 (Role B):** CMB slow-roll — $n_s=0.9685$, $N_e\approx63.4$, $\Phi_{\rm inf}\approx15.9\,M_{\rm Pl}$
2. **$T_{\rm GB}$:** Gaussian saddle width, not numerology
3. **Sector 2 (Role A):** terminal constraint roll (BR2 exponential endpoints) — **separate sector** per BR2c

**Discipline:** Do not merge $H^{(F)}$ and $H^{(\alpha)}$; do not claim single $H(N)$ ansatz closes both $n_s$ and lock endpoints.

---

## §2. J6a — Reduced saddle system ($\xi=1/6$, pre-EWSB)

### §2.1 Lorentzian action (pre-locking, $|H_{\rm SM}|=0$)

$$\mathcal{L} = \frac{R}{16\pi G} - \frac{1}{2}(\partial\Phi)^2 - \frac{1}{12}R\Phi^2 - V_{\rm NTE}(\Phi) + \mu\left(\mathcal{H}-\alpha\Phi^2\right)$$

Closed FRW ($k=+1$ for NTE): $ds^2=-dt^2+a^2(t)(d\chi^2+\sin^2\chi\,d\Omega^2)$.

**Constraint (Role A slaved):** $\mathcal{H}=\alpha\Phi^2$ with $\mathcal{H}\equiv H$ on FRW slices.

### §2.2 Conformally modified Friedmann (Jammer, ξ=1/6)

Define $F(\Phi)=1+\Phi^2/(6M_{\rm Pl}^2)$. The Hamiltonian constraint with non-minimal coupling:

$$3M_{\rm Pl}^2 F(\Phi)\left(H^2+\frac{1}{a^2}\right) = \frac{1}{2}\dot\Phi^2 + V_{\rm NTE}(\Phi) + \frac{1}{6}R\Phi^2$$

For $\Phi\gg M_{\rm Pl}$ (HH peak), $F(\Phi)\approx\Phi^2/(6M_{\rm Pl}^2)$ — conformal factor **amplifies** kinetic/gravity balance; must be kept in numerical integration.

### §2.3 Single-DOF reduction

Under constraint $\Phi^2=H/\alpha$:

$$\dot\Phi = \frac{\dot H}{2\alpha\Phi} = \frac{\dot H}{2\sqrt{\alpha H}}$$

Substituting into Friedmann + scalar EOM yields **one second-order ODE for $H(N)$** (Stage 3 eq. (7), ξ=1/6 correction in $F(\Phi)$):

$$\dot H^2 = 8\alpha H\left[3M_{\rm Pl}^2 F(\sqrt{H/\alpha})\left(H^2+\frac{1}{a^2}\right) - V_{\rm NTE}(\sqrt{H/\alpha}) - \mathcal{C}_{\rm conf}(\Phi,H)\right]$$

where $\mathcal{C}_{\rm conf}$ collects $(1/6)R\Phi^2$ after substituting $\Phi(H)$.

**DOF count:** 1 dynamical ($H$ or $a$); $\Phi$ holonomic; $\mu$ algebraic — **consistent with Companion 9 §4.1**.

### §2.4 Off-trajectory extensions (E1–E3)

| Ext | $V_{\rm NTE}(\Phi)$ | Saddle role |
|-----|---------------------|-------------|
| **E1** | $(3\alpha^2/8\pi G)\Phi^4$ only | Degenerate — $n_s\to1$ (P0); **excluded** for observation |
| **E2** | $+\,-(\alpha^2/8)\Phi^6$ | Starobinsky-class candidate; Session 4 numeric target |
| **E3** | $+\,-(\alpha^2 A^2/8)\Phi^2$ | **Sector 1 candidate** — quadratic → Φ²-chaotic slow-roll |

**J6b target:** solve reduced ODE for **E3** on slow-roll window with HH boundary conditions (Stage 3 §5).

---

## §3. J6c — $T_{\rm GB}=M_{\rm Pl}/\sqrt{2\pi}$ upgrade path

### §3.1 Structural argument (Jammer formalisation)

Euclidean action $S_E[g,\Phi]$ at HH saddle $g=g_*,\Phi=\Phi_*$. Expand:

$$S_E = S_* + \frac{1}{2}\delta X^T \mathcal{H}_{ij}\,\delta X^j + \cdots$$

For temperature / scale-factor direction with Hessian eigenvalue $\lambda_T\sim M_{\rm Pl}^2$:

$$\Psi \propto \exp\left(-\frac{1}{2}\lambda_T \delta T^2\right) \quad\Rightarrow\quad \sigma_T = \lambda_T^{-1/2} \sim M_{\rm Pl}^{-1}$$

Gaussian normalisation $\int e^{-T^2/(2\sigma_T^2)}dT = \sqrt{2\pi}\,\sigma_T$ gives **characteristic scale**

$$T_* = \frac{M_{\rm Pl}}{\sqrt{2\pi}}$$

(identification of $T$ with Hubble-scale exit temperature at saddle peak — Companion 9 §3.1–3.2).

### §3.2 What Jammer still owes for **derived** (C1)

| Step | Task | Status |
|------|------|--------|
| 1 | Write $S_E$ for NTE $\xi=1/6$ + LM constraint on $S^3\times S^1_\beta$ | Open (Paper S2 geometry) |
| 2 | Compute $\mathcal{H}_{TT}$ at saddle explicitly | Open |
| 3 | Verify $\lambda_T\sim M_{\rm Pl}^2$ (not $H_{\rm GB}^{(\alpha)}$ scale) | Open |
| 4 | Match Friedmann $H^{(F)}(T_{\rm GB})$ to Epoch A table | Partial (Companion 9) |

**Proposed register upgrade:** (C1) **candidate → derived-at-Gaussian-saddle** once steps 1–3 close; **not** full Paper S2 heat-kernel yet.

**Corpus patch:** Authorised as **Jammer-proposed** wording for §17.5.4 (C1) footnote — AC to integrate.

---

## §4. J6b — Sector 1 $H_{\rm inf}(N)$ (Role B)

### §4.1 Φ²-chaotic equivalence (confirmed)

Near saddle, E3 with $|A|\ll M_{\rm Pl}$ gives effective $V\approx\frac{1}{2}m_{\rm eff}^2\Phi^2$ with $m_{\rm eff}\sim A$ at $\Phi\sim\Phi_{\rm inf}$. Standard slow-roll:

$$n_s = 1 - \frac{8M_{\rm Pl}^2}{\Phi_{\rm inf}^2}, \qquad N_e \approx \frac{\Phi_{\rm inf}^2}{4M_{\rm Pl}^2}$$

**Corpus targets:** $\Phi_{\rm inf}=15.9\,M_{\rm Pl}$, $n_s=0.9685$, $N_e=63.4$ — **internally consistent** (Companion 9 §2.2).

### §4.2 Profile ansatz (pending numeric derivation)

Companion 9 slow-roll window:

$$H_{\rm inf}(N) \approx H_{\rm HH}\sqrt{1 - N/N_{e,{\rm sr}} + \cdots}$$

**Not** the BR2 exponential (that is Sector 2 terminal roll).

**Next session deliverable:** integrate reduced ODE (§2.3) for E3; extract $\varepsilon(N)$ on last ~60 e-folds; compare to $\sqrt{1-N/N_e}$ ansatz.

### §4.3 Magnitude clash (unchanged)

$|\Phi_{\rm NTE}(0)|=\sqrt{M_{\rm Pl}/\alpha}\sim10^{32}$ GeV vs $\Phi_{\rm inf}\sim10^{20}$ GeV — **do not identify** without J6d map.

---

## §5. J6d — Locking junction (open)

**BR2c default stands:** Sector 1 ends at slow-roll exit; Sector 2 enforces $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ roll $M_{\rm Pl}\to H_{\rm GB}^{(\alpha)}$ over $\Delta N_{\rm term}\approx63.4$.

**Open routes (R4):**

- Z₂ portal / gauge-birth identification of degrees of freedom
- Wick rotation + Stage 3 $y$-coordinate map (BR2d)
- Auxiliary field carrying Role (B) inflaton vs Role (A) constraint scalar

**Falsifier:** Any derived map that forces $\Phi_{\rm inf}=|\Phi_{\rm NTE}(0)|$ **fails** BR2c numerics.

---

## §6. Session plan (Jammer queue)

| Priority | Task | Est. |
|----------|------|------|
| **J6-n1** | Numeric E3 reduced ODE + $n_s$ extraction | 1 session |
| **J6-n2** | E2 comparison / Starobinsky match | 1 session |
| **J6-n3** | Explicit $\mathcal{H}_{TT}$ on simplified $S_E$ | 1–2 sessions |
| **J6-n4** | BR2d $y\leftrightarrow N$ junction memo | 1 session |
| **Parallel** | S3-f3 $d\mu(V)$ once Sector 1 $H(N)$ numeric | after J6-n1 |
| **Parallel** | V-d2 void tracer (Impact #3) | when Greg routes |

---

## §7. Handoff

- **AC:** Integrate J1 sign-off → §22.16 status; optional (C1) footnote from §3.2
- **Cursor:** BR2c unchanged; reference this doc as J6 first pass
- **Greg:** Recognition gate — authorise J6-n1 numeric session (E3 ODE)

**Corpus patch authorised (J6):** **N** — partial progress only; no closure claim

— Jammer J6 first pass v0.1, 2026-05-23.
