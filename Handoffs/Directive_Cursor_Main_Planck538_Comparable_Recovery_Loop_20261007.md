# DIRECTIVE — Planck-comparable recovery loop (Scratch + Jammer clones)

**From:** Cursor Main · **To:** Scratch, Jammer, AC · **Cc:** Greg, PC  
**Date:** 2026-10-07 · **Authorised by Greg:** keep both lanes working; seek ways to replicate Planck \(5.38\pm 0.15\); task clones; check; retune / new paths; reimplement; continue until convergence or Greg STOP.  
**Register:** continuous research programme. **No Core patches** until AC+Greg BL-6-style gate.

---

## 0. What “replicate Planck 5.38” means here

Planck’s figure is **not** a bare decimal. It is the abundance of a component that is **cold, collisionless, and co-located** at \(z\sim 1100\), reported as \(\Omega_{\mathrm{DM}}/\Omega_b = 5.38\pm 0.15\).

**CONVERGED (programme success)** requires **all** of:

| Gate | Requirement |
|---|---|
| **V** | Structurally fixed \(r_{\mathrm{bg}}\in[5.23,\,5.53]\) (no free dial) |
| **C** | BL-3 character PASS: cold + collisionless + co-located (adiabatic tracing) at CMB epoch |
| **A** | Legitimate action / ghost-free completion (no \(T\)-in-\(S\), no hand \(S_{\mathrm{cons}}\) unless derived) |
| **L** | Dual-lane agreement (Scratch constructive + Jammer adversarial) on V+C+A |

**Important:** \(\kappa_0/(1-\kappa_0)\approx 5.50\) already satisfies **V** numerically. The 2026-10-06 withdrawal failed on **C** (and A was architectural). Hunting a different decimal while failing C is **not** success.

---

## 1. Hard disciplines (non-negotiable)

1. **No-f.** No parameter sized to land in \([5.23,5.53]\).  
2. **Number without character = FAIL.**  
3. **N1 bilkinetic \(S_\nu\)** is closed as a CDM path (hot / \(\Delta N_{\mathrm{eff}}\)) — do not re-litigate unless new content.  
4. **C3 quarantine** (\(T\cdot T+S_{\mathrm{cons}}\)) stays quarantine.  
5. **Stop file:** `Working/planck538_loop/STOP` ends the loop. Greg chat “stop” also ends it.  
6. Nothing patched into `Core_Papers/` from this loop.

---

## 2. Machinery

| Piece | Path |
|---|---|
| State / path queue | `Working/planck538_loop/state.json` |
| Orchestrator | `Working/planck538_loop/orchestrate.py` |
| Round briefs / results | `Working/planck538_loop/rounds/` |
| Status board | `Working/PLANCK538_STATUS_BOARD_Cursor_Main.md` |
| Wake loop | local `AGENT_LOOP_TICK_planck538` (PowerShell) |

Each **tick / round**:

1. Orchestrator selects next path (or retunes prior).  
2. Writes Scratch + Jammer briefs (blind).  
3. Clones execute and file under `rounds/RNN_*`.  
4. Main scores V/C/A/L; updates state; enqueues new paths or marks FAIL.  
5. If CONVERGED → stop. If STOP file → stop. Else continue.

---

## 3. Initial path queue (seed)

| ID | Path | Why it might hit V+C |
|---|---|---|
| **P01** | Ghost-free derivation of Einstein-mix / amplifier (C2) without hand \(S_{\mathrm{cons}}\) | V already ~5.50; must still pass **C** (expect hard) |
| **P02** | Hassan–Rosen healthy branch with structural \(\beta_n\) (no fit) | Possible DM-like branch + ratio |
| **P03** | Action-level Hopf overlap → bare C1 (\(\alpha=\kappa_0\)) + **separate** cold sector with structural abundance | Split: bridge ≠ CDM; CDM elsewhere in ontology |
| **P04** | Location-locking / scale-split (C-rewrite) so twin wells co-locate + structural abundance | Attacks P2 co-location kill |
| **P05** | Rest-energy-only bridge + deposited cold mechanism (no new dial) | Prior Hκ residue; character first |
| **P06** | P-newDM / foam-adjacent structural abundance in band | Open CDM sector; must be NTE-allowed |
| **P07** | (generated) — orchestrator / lanes may append after FAILS |

---

## 4. Lane roles (every round)

- **Scratch:** construct the round’s path; compute \(r_{\mathrm{bg}}\); argue C; land PASS/FAIL on V/C/A.  
- **Jammer:** kill no-f, kill number-without-character, kill smuggled \(S_{\mathrm{cons}}\)/ghosts; only allow CONVERGED if all gates survive.  
- **Main:** score, retune path queue, re-brief, keep loop alive.

---

## 5. Stop conditions

- `Working/planck538_loop/STOP` exists, or Greg says stop.  
- State `status: CONVERGED`.  
- State `status: EXHAUSTED` (queue empty, no new structural paths).  

— Cursor Main, 2026-10-07.
