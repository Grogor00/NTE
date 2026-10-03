# BR2 — $\Phi(N)$ trajectory scaffold v0.1 (H_GB bridge)

**Stream:** Cursor scaffold → **Jammer** (J6 HH saddle + action derivation)  
**Date:** 2026-05-23  
**Status:** **Sector 2 (Role A) baseline** — endpoints match §18.2; **superseded for $n_s$ by BR2c** (two-sector)  
**Script:** `Working/phi_n_trajectory_br2.py`  
**Parent:** `H_GB_Bridge_Attack_Route_v0_1`; **Upgrade:** `Phi_N_Trajectory_BR2c_Attack_Route_v0_1`

---

## §1. Mission

Supply an explicit **$|\Phi_{\rm NTE}(N)|$** history connecting:

| Anchor | Constraint | Symbol |
|--------|------------|--------|
| HH peak | $H\sim M_{\rm Pl}$ | §18.2 start |
| Locking | $H=\alpha M_{\rm Pl}^2$ | $H_{\rm GB}^{(\alpha)}$ |
| Locking | $\|\Phi\|=M_{\rm Pl}$ | §18.5 / audit |
| Inflation depth | $N_e=-\ln(\alpha M_{\rm Pl})$ | §18.2 |
| Thermal (off-trajectory) | Friedmann at $T_{\rm GB}$ | $H_{\rm GB}^{(F)}$ |

**Register:** thermal $H^{(F)}$ is **not** equal to $H(N)$ from $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ at the same instant — Epoch A vs Epoch B/C (bridge v0.1).

---

## §2. Coordinate systems (do not conflate)

| Coordinate | Range | Role |
|------------|-------|------|
| **$N$** (cosmological e-fold) | $0\to N_e$ at pre-temporal inflation | §18.2 $n_s$ sector; $H(N)$ roll |
| **$y$** (Stage 3 surface ontology) | $0\to N_{\rm lock}\approx0.1$ | Pre-temporal **profile**; Wick kink at $y=N_{\rm lock}$ |
| **$t$** | post-locking | Emergent; $dt=dN/(\alpha|\Phi|^2)$ |

$N_{\rm lock}\neq N_e$ — holographic width vs inflation depth (BR5 prose fix).

---

## §3. Candidate Epoch B — exponential (scaffold)

**Ansatz** (Jammer to derive or replace):

$$H(N) = H_{\rm HH}\,e^{-N}, \qquad H_{\rm HH}=M_{\rm Pl}, \quad N=0\ \text{at HH peak}$$

Constraint $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ gives:

$$|\Phi(N)| = \sqrt{\frac{H_{\rm HH}}{\alpha}}\,e^{-N/2} = \frac{M_{\rm Pl}}{\sqrt{\alpha M_{\rm Pl}}}\,e^{-N/2}$$

**Endpoint checks (script):**

| Quantity | Target | Scaffold |
|----------|--------|----------|
| $N_e$ | $-\ln(\alpha M_{\rm Pl})\approx63.4$ | **exact** from $H(N_e)/H(0)=\alpha M_{\rm Pl}$ |
| $H(N_e)$ | $\alpha M_{\rm Pl}^2$ | **match** |
| $|\Phi(N_e)|$ | $M_{\rm Pl}$ | **match** |
| $H^{(F)}$ at $T_{\rm GB}$ | Friedmann | **off** constraint curve ($\sim e\,M_{\rm Pl}$) |

---

## §4. Three-epoch placement

```
Janus (|Phi|->0, H->0)
    |
    |  Stage 3 y in [0, N_lock] — linear profile (audit §2)
    v
HH peak N=0:  H ~ M_Pl,  |Phi| ~ M_Pl/sqrt(alpha M_Pl)
    |
    |  Epoch B: N = 0 .. N_e (~63 e-folds)  [candidate H = M_Pl e^{-N}]
    v
Locking:  H = H_GB^(alpha),  |Phi| = M_Pl
    ||
    ||  Epoch A (simultaneous): thermal bath T_GB,  H^(F) = Friedmann(T_GB)
    v
Gauge birth + Wick rotation (y = N_lock)
```

---

## §5. Stage 3 pre-locking profile (unchanged)

Audit §2 / Stage 3:

$$|\Phi_{\rm pre}|^2(y) = \frac{\Phi_0^2 e^{-N_{\rm lock}}}{N_{\rm lock}}\,y, \quad y\in(0,N_{\rm lock})$$

**Bridge open:** map $y\to N$ near locking so exponential Epoch B **matches** Stage 3 endpoint at $y=N_{\rm lock}$.

---

## §6. Honest tensions (Jammer)

| Issue | Detail |
|-------|--------|
| **n_s** | $H=M_{\rm Pl}e^{-N}$ gives $\varepsilon=1$ → $n_s=-1$ (slow-roll import) — **wrong**; need $\varepsilon\sim0.016$ (Companion 9 hilltop). Scaffold matches **$N_e$ only**. |
| **Derivation** | Ansatz is **not** from $V_{\rm NTE}$ or HH saddle — J6 required |
| **$H^{(F)}$** | Thermal Friedmann **not** on $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ curve — intentional |
| **Janus → HH** | Segment from $|Phi|=0$ to $H=M_{\rm Pl}$ not specified here |

---

## §7. Jammer deliverables (upgrade path)

| Step | Task |
|------|------|
| **BR2b** | Derive $H(N)$ from HH saddle + $\xi=1/6$ action (J6) |
| **BR2c** | Replace exponential with slow-roll $H(N)$ matching **both** $N_e$ and $n_s$ |
| **BR2d** | Map $y\leftrightarrow N$ at locking; Stage 3 continuity |
| **BR2e** | Thermal $H^{(F)}$ from plasma $\rho(T_{\rm GB})$ — prove off-constraint |

---

## §8. Falsifiers

1. No $|\Phi|(N)$ satisfying $H = \\beta_{\\mathrm{NTE}}|\Phi|^2$ **and** $H(N_e)=\alpha M_{\rm Pl}^2$ **and** $|\Phi(N_e)|=M_{\rm Pl}$  
2. Forced $H^{(F)}=H^{(\alpha)}$ on same $N$  
3. Claim BR2 closes bridge **without** J6/J6 derivation

---

## §9. Cross-references

- `H_GB_Bridge_Attack_Route_v0_1`, `h_gb_bridge_numerics.py`  
- `17.5.4_Audit_NLock_Derivation.md` §2; §18.2, §18.5  
- `Jammer_Formal_Backlog_Package_v0_1` (J6, BR2)

— Cursor BR2 v0.1, 2026-05-23.
