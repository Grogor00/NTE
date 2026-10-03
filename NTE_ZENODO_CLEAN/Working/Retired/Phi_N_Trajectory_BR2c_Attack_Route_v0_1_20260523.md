# BR2c — $\Phi(N)$ two-sector attack route v0.1

**Stream:** Cursor attack on **LB-1** → Jammer J6 derivation  
**Date:** 2026-05-23  
**Status:** **RESOLUTION route ratified** — LB-1 closed @ register (`Jammer_LB1_Exhaustive_Resolution_v0_1`); J6 derive open  
**Script:** `Working/phi_n_trajectory_br2c.py`  
**Parents:** `Phi_N_Trajectory_BR2_v0_1`; `Corpus_Gap_Tension_Report_v0_2`; Companion 9 Session 3

---

## §1. Problem (why BR2 v0.1 is insufficient)

BR2 exponential $H(N)=M_{\rm Pl}e^{-N}$ on Role (A) constraint:

| Check | Result |
|-------|--------|
| $N_e=-\ln(\alpha M_{\rm Pl})$ | **PASS** |
| $H(N_e)=H_{\rm GB}^{(\alpha)}$ | **PASS** |
| $|\Phi(N_e)|=M_{\rm Pl}$ | **PASS** |
| Slow-roll $n_s=1-2\varepsilon$ | **FAIL** ($\varepsilon=1\to n_s=-1$) |

Companion 9 Session 3 closes $n_s$ via **Role (B)** inflaton slow-roll:

$$n_s = 1-\frac{8M_{\rm Pl}^2}{\Phi_{\rm inf}^2} = 0.9685, \quad \Phi_{\rm inf}\approx 15.9\,M_{\rm Pl}, \quad N_e\approx\frac{\Phi_{\rm inf}^2}{4M_{\rm Pl}^2}\approx 63.2$$

**Attempting one $H(N)$ ansatz for both roles creates a false contradiction.**

---

## §2. Role (A) vs Role (B) magnitude clash (numerics)

At HH peak ($H\sim M_{\rm Pl}$), constraint Role (A):

$$|\Phi_{\rm NTE}(0)| = \sqrt{\frac{M_{\rm Pl}}{\alpha}} \approx 7.2\times 10^{32}\ {\rm GeV}$$

Companion 9 Role (B) inflaton at slow-roll start:

$$\Phi_{\rm inf} \approx 15.9\,M_{\rm Pl} \approx 1.9\times 10^{20}\ {\rm GeV}$$

**Ratio** $\Phi_{\rm inf}/|\Phi_{\rm NTE}(0)| \sim 3\times 10^{-13}$.

**Corpus default (§17.5.19):** Role (B) is pre-temporal / HH **only**; Role (A) defines post-locking constraint cosmology. **Do not identify magnitudes without a derived map.**

---

## §3. Proposed two-sector $H(N)$ (attack route)

### Sector 1 — Observation / slow-roll (Role B)

- **Domain:** last $\sim 60$ e-folds of HH inflation where CMB modes exit (C9 $\Phi^2$-chaotic equivalence).
- **$H_{\rm inf}(N)$:** C9 profile $H_{\rm HH}\sqrt{1-N/N_{e,{\rm sr}}+\cdots}$ over slow-roll window — **not** the full drop to $H_{\rm GB}^{(\alpha)}$.
- **$n_s$:** from $\Phi_{\rm inf}$ at horizon crossing; $\varepsilon\sim 0.016$.
- **Owner:** Jammer derives from HH saddle + $V_{\rm NTE}$ off-trajectory (J6).

### Sector 2 — Constraint locking (Role A)

- **Domain:** terminal roll where $H = \\beta_{\\mathrm{NTE}}|\Phi_{\rm NTE}|^2$ is enforced; connects HH exit to lock.
- **$H_{\rm lock}(N)$:** BR2 exponential (or Jammer replacement) over $\Delta N_{\rm term}\approx N_e^{\rm (A)}=-\ln(\alpha M_{\rm Pl})\approx 63.4$.
- **Endpoints:** $H(0)\sim M_{\rm Pl}$, $H(N_e)=H_{\rm GB}^{(\alpha)}$, $|\Phi(N_e)|=M_{\rm Pl}$ — **BR2 PASS**.
- **$n_s$:** **not** read from this sector (wrong slow-roll regime).

### Sector 0 — Holographic width (Stage 3 $y$)

- **$N_{\rm lock}=S_{\rm dS}/4\approx 0.105$** on coordinate $y\in[0,N_{\rm lock}]$ — **orthogonal** to Sector 1 $N_e$ and Sector 2 $\Delta N_{\rm term}$ unless Jammer proves a derived map (BR2d).

---

## §4. Attack routes

| Route | Mechanism | Verdict (Cursor) |
|-------|-----------|------------------|
| **R1 — Single ansatz** | One $H(N)$ for $n_s$ + lock endpoints | **Excluded** (constant-$\varepsilon$ needs $N_e\sim4000$; C9 $\sqrt{1-N/N_e}$ does not reach $H^{(\alpha)}$) |
| **R2 — Two-sector (default)** | Role (B) slow-roll + Role (A) constraint terminal roll | **Proposed** — matches §17.5.19 |
| **R3 — Piecewise constant $\varepsilon$** | $\varepsilon\sim0.016$ for $N_1\sim60$ + $\varepsilon\sim1$ for $N_2\sim62$ | **Illustrative only** — unnatural; not derived |
| **R4 — Field map at lock** | $\Pi_G$ Z₂ projection at $G$ | **Derived** (Jammer R4 v1.0) |

---

## §5. Falsifiers

1. Forced equality $H^{(F)}=H^{(\alpha)}$ on same epoch (already excluded).
2. Claim BR2 exponential **derives** $n_s=0.9685$.
3. Identify $\Phi_{\rm inf}=|\Phi_{\rm NTE}|$ at HH **without** derivation while using both numerics.
4. Use $N_{\rm lock}$ in place of $N_e$ in §18.2 counting formula.

---

## §6. Jammer deliverables (unchanged + sharpened)

| Step | Task |
|------|------|
| **BR2b/J6** | Derive Sector 1 $H_{\rm inf}(N)$ from $\xi=1/6$ action + HH saddle |
| **BR2c** | **This doc** — accept two-sector; prove or refute field map at lock |
| **BR2d** | Map $y\leftrightarrow N$; Stage 3 continuity at $y=N_{\rm lock}$ |
| **BR2e** | Thermal $H^{(F)}$ off-constraint (Epoch A) — already numerics |

---

## §7. Cross-references

- `phi_n_trajectory_br2.py` — Sector 2 baseline  
- `phi_n_trajectory_br2c.py` — Role clash + route table  
- `H_GB_Bridge_Attack_Route_v0_1` — three epochs  
- `J6_HH_Saddle_Scope_Memo_v0_1` — formal target  

— Cursor BR2c v0.1, 2026-05-23.
