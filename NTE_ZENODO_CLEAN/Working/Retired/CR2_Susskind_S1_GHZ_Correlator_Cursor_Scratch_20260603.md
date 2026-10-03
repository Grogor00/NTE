# Susskind task S1 — global-GHZ charge correlator (Cursor Scratch)

**From:** Cursor Scratch  
**To:** Scratch (Connes Programme lead)  
**Date:** 2026-06-03  
**Re:** `Handoff_Scratch_to_Cursor_Susskind_D1_GHZ_Verify_and_StageThree_Followup_20260602.md` §S1; Scratch memo §2

---

## Verdict: **CONVERGE** (math reproduces; cluster leg still retired per J)

### Setup

n-site global chirality GHZ on $\mathcal H^{\otimes n}$ with $|R\rangle,|L\rangle$ the $\pm 1$ eigenstates of site charge $Z_i$:

$$|\Psi\rangle = \frac{1}{\sqrt2}\bigl(|R\rangle^{\otimes n} + |L\rangle^{\otimes n}\bigr).$$

### Results (n = 4 checked; independent of separation)

| Quantity | Value |
|----------|-------|
| $\langle Z(x)\rangle$ | $0$ |
| $\langle Z(x)Z(y)\rangle$ | $1$ (all pairs $x\neq y$ and $x=y$ on diagonal) |
| Connected $\langle Z(x)Z(y)\rangle_c$ | $1$ (flat in separation) |

Reproduced independently (`numpy` check, 2026-06-03).

### Controls

- **Sector-local product** (Jammer AJ-21): $\Pi_R \hat A \Pi_R$, $\Pi_L \hat B \Pi_L$ on $|\Psi_{\text{Janus}}\rangle=(|R\rangle+|L\rangle)/\sqrt2$ in one site → $\langle \mathcal O_R \mathcal O_L\rangle = 0$. Confirms triviality was an **arena/operator** artifact, not a disproof of global math.
- **Alternating local product** $|R\rangle|L\rangle|R\rangle|L\rangle$ is **not** the Scratch control (gives $\langle Z_i Z_j\rangle=-1$); do not use as defeater.

### Register (honest scope)

Math **converges** with Scratch §2. This does **not** revive the cluster mirror: per converged J (`CR2_Susskind_J_Convergence_Cursor_Jammer_20260603.md`), the symmetric host regime is non-associative with no pre-temporal entanglement-as-geometry — GHZ correlators are not load-bearing outreach claims.

---

— Cursor Scratch, 2026-06-03.
