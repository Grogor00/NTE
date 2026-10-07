# Round R01 — Cursor Scratch VERDICT

**Programme:** Planck-comparable recovery (V+C+A+L) · **No-f** · **No Core patches**  
**Date:** 2026-10-07 · **Lane:** Cursor Scratch (constructive, blind to Jammer R01)  
**Paths:** P01, P02  
**κ₀ = 3/√(4π) ≈ 0.846284** (deposited; not fitted)

**Hard reminder used throughout:** κ₀/(1−κ₀) ≈ **5.5055 ∈ [5.23, 5.53]** already satisfies **V** numerically. Success still requires **C** (cold + collisionless + co-located at CMB epoch). Number without character = FAIL.

---

## P01 — Ghost-free C2 amplifier without hand S_cons

### Mechanism proposed (concrete)

**Target EOM (Phase-0 C2):**
\[
G^\pm - \kappa_0 G^\mp = 8\pi T_m^\pm
\quad\Rightarrow\quad
r_{\mathrm{bg}}=\frac{\kappa_0}{1-\kappa_0}\approx 5.5055.
\]

**Candidate completions tested constructively (none succeed as healthy derived C2):**

| Attempt | Action / structure | Result |
|---|---|---|
| P01-a | Hand constraint \(S_{\mathrm{cons}}\): \(\tilde T=T_b+\kappa_0\tilde T\) | Recovers 5.50 by construction; **forbidden** (hand \(S_{\mathrm{cons}}\); C3 quarantine class) |
| P01-b | Wrong-sign metric kinetic mixing (Phase-0 C6) | Algebraically mimics C2; **ghost** → A FAIL |
| P01-c | Integrate out light bilkinetic \(S_\nu\) (N1) | Yields additive \(T_\nu\), **not** \(G^\pm-\kappa_0 G^\mp\); κ₀ absent (already closed as CDM path) |
| P01-d | “Mutual recursion / self-consistency” slogan without new \(S\) | Entails at most simultaneous linear solve (C1, \(r_{\mathrm{bg}}=\kappa_0\)), **not** geometric amplifier |
| P01-e | Hassan–Rosen \(V(g^{-1}f)\) as C2 surrogate | Healthy on standard branches, but EOM is \(G(g)=8\pi T+\tau(g,f)\), **not** Einstein-tensor mixing; does not derive C2 |

**Honest landing:** No ghost-free local action on file produces C2 without hand \(S_{\mathrm{cons}}\) or ghostly kinetic mixing. P01’s *V hope* assumes a derivation that is not exhibited.

### \(r_{\mathrm{bg}}\) estimate

- **If** C2 were derived: \(r_{\mathrm{bg}}=\kappa_0/(1-\kappa_0)\approx 5.5055\) (in band).  
- **As actually available:** either (i) no legitimate C2 → \(r_{\mathrm{bg}}\) undefined for this path, or (ii) C3/C6 mimic → 5.5055 with A violated.

### Gates

| Gate | Verdict | Evidence |
|---|---|---|
| **V** | **PASS\*** | \*Conditional on C2 algebra: 5.5055 ∈ [5.23, 5.53], structural in κ₀, no-f. Without a derived C2, V is *vacuous* (number not owned by a legitimate law). Scratch scores **PASS** only for the *conditional* decimal; see Overall. |
| **C** | **FAIL** | Under CPN equal-T twin matter, total-feedback “extra” is **twin baryon / radiation stress**, not cold collisionless CDM. P2 perturbation verdict (2026-10-06): acoustic + Silk damping; location-blind (“magnitude not location”). Co-location FAIL; cold FAIL; collisionless FAIL. |
| **A** | **FAIL** | No ghost-free derivation of C2 without hand \(S_{\mathrm{cons}}\). C6 mimic is ghostly. N1 does not smuggle C2. |

**P01 V:** PASS (conditional decimal only; law not derived)  
**P01 C:** FAIL  
**P01 A:** FAIL  
**P01 path:** **FAIL** (C hard-kill; A hard-kill)

---

## P02 — Hassan–Rosen healthy branch, structural β_n (no fit)

### Mechanism proposed (concrete)

**Adopt-and-credit action** (Hassan & Rosen 2012; NTE ID \((g,f)\leftrightarrow(g^+,g^-)\)):
\[
\begin{aligned}
S
&= \frac{M_g^2}{2}\int\sqrt{-g}\,R(g)
+ \frac{M_f^2}{2}\int\sqrt{-f}\,R(f)
+ m^2 M_{\mathrm{eff}}^2\int\sqrt{-g}\,V\big(g^{-1}f;\beta_n\big) \\
&\quad + S_m[g,\psi^+] + S_m[f,\psi^-].
\end{aligned}
\]

**Structural β_n ansatz (no fit to 5.38)** — standard finite-branch / healthy cosmological choice used in the bimetric literature (not tuned here):

- Take \(M_g=M_f=M_{\mathrm{Pl}}\) (CPN-even equal Planck masses; relative mass ratio ≠1 would be a new dial).  
- Restrict to the **common healthy subset** with only \(\beta_0,\beta_1,\beta_2\) active and the **infinite-branch / dS-compatible** relations that eliminate the Boulware–Deser ghost at the action level (HR potential), e.g. schematic:
  \[
  \beta_0,\beta_1,\beta_2\ \text{fixed by requiring a flat/dS reference with } V'(I)=0 \text{ at } g=f,
  \]
  with **m** the graviton mass scale left as the theory’s mass parameter — **not** sized to land \(r_{\mathrm{bg}}\) in [5.23, 5.53].

**What “extra” is under CPN \(g=f\), equal matter:**

1. **Interaction effective density** \(\rho_V(g,f)\big|_{g=f}\): on healthy dS-compatible branches this is typically a **constant / DE-like** term (effective Λ), not a clustering CDM fluid.  
2. **Twin matter on \(f\)**: under CPN equal \(T_m\), \(\rho_f/\rho_g=1\), not ≈5.5.  
3. **Massive graviton / tensor sector**: can be collisionless, but abundance is set by \(m\) and branch data — **not** by κ₀; pinning it into [5.23, 5.53] without a deposited structural formula for \(m/\rho_b\) would be **f**.

κ₀ does **not** appear in \(V(g^{-1}f;\beta_n)\) unless Hopf-overlap inserts it (none deposited for this round).

### \(r_{\mathrm{bg}}\) estimate

| Bookkeeping choice | \(r_{\mathrm{bg}}\) | In band? |
|---|---|---|
| Twin matter ratio under CPN | \(\rho_f/\rho_b\sim 1\) | No |
| \(\rho_V/\rho_b\) on healthy dS branch | \(\sim\Lambda_{\mathrm{eff}}/\rho_b\) (DE-like; epoch-dependent) | Not structurally fixed to [5.23, 5.53]; would require dialing \(m\) or β_n → **no-f forbid** |
| Amplifier identity κ₀/(1−κ₀) | **Not derived** from HR | Must not be assumed |

**Estimate:** \(r_{\mathrm{bg}}\) **not in band by structure**. Branch-dependent; **V FAIL** for Planck-comparable DM ratio.

### Gates

| Gate | Verdict | Evidence |
|---|---|---|
| **V** | **FAIL** | No structural extraction yields \(r_{\mathrm{bg}}\in[5.23,5.53]\) without fitting \(m\) or β_n. Twin ratio → ~1; ρ_V → DE-like, not κ₀-amplifier. |
| **C** | **FAIL** | Healthy cosmological HR branches used for late-time acceleration are **DE / modified-gravity**, not cold co-located CDM at \(z\sim 1100\). Twin matter under CPN is baryon-like (same P2 kill). Massive-graviton DM would need a separate cold + co-location + abundance packet — not supplied by “healthy β_n” alone. |
| **A** | **PASS** | HR action is ghost-free on the stated healthy branch class (adopt-and-credit); no hand \(S_{\mathrm{cons}}\); no T-in-S. (Health is conditional on staying on that branch — standard caveat.) |

**P02 V:** FAIL  
**P02 C:** FAIL  
**P02 A:** PASS  
**P02 path:** **FAIL** (V+C)

---

## Overall (R01 Scratch)

| Path | V | C | A | Survive? |
|---|---|---|---|---|
| P01 | PASS* (conditional) | **FAIL** | **FAIL** | **NO** |
| P02 | **FAIL** | **FAIL** | PASS | **NO** |

**Overall V:** FAIL (no surviving path owns an in-band ratio with a legitimate law *and* character)  
**Overall C:** FAIL  
**Overall A:** FAIL (P01 kills A; P02 alone does not deliver V+C)  
**Overall L:** PENDING (dual-lane; Scratch does not self-PASS L)

**Round landing:** **both active paths FAIL.** C remains the hard gate. P01’s beautiful 5.50 is exactly the trap named in the directive: V without C (and here without A).

---

## New structural paths proposed (≤2; no dials)

Queue already holds P03–P06. Scratch appends **two new** structural candidates (not dials; not Core patches):

### P07 — Heavy shared Majorana (structural \(M\gg T_{\mathrm{CMB}}\)) as cold collisionless sector

- **Why new:** N1 closed only the *light* bilkinetic as hot/ΔN_eff. A **Companion-deposited seesaw / heavy-\(M\)** branch can be cold + collisionless without re-litigating light N1 as CDM.  
- **V demand:** abundance \(\rho_M/\rho_b\) must come from a **structural** formula (heat-kernel / Hopf / thickness), **not** by sizing \(M\) to 5.38.  
- **C hope:** cold + collisionless plausible; **co-location** still must be shown (shared field on both metrics helps adiabatic tracing — must be argued, not assumed).  
- **A hope:** same bilkinetic action class as N1; ghost-free spinor.

### P08 — Single-metric matter + HR massive graviton as the dark component (matter only on \(g^+\))

- **Why new:** Breaks CPN-equal twin-baryon bookkeeping that forces baryon-like character; “extra” is the **healthy massive spin-2** sector, not mirror baryons.  
- **V demand:** structural \(m\) / branch data → \(\Omega_{\mathrm{MG}}/\Omega_b\) in band without fit (hard; fail-closed if only DE branch exists).  
- **C hope:** massive graviton can be cold/collisionless; co-location = gravitational clustering with baryons (standard).  
- **A hope:** HR healthy branch retained; asymmetry \(S_m[f]=0\) must be **ontology-justified** (e.g. orientation-local Standard Model), not a ratio dial.

---

## Sign-off

P01 and P02 do **not** survive V+C+A. Recommend Main enqueue **P07, P08** after P03–P06 (or interleave if C-first triage prefers heavy-\(M\) / massive graviton over amplifier revival).  
Do not promote κ≈5.50 to Planck-comparable without C PASS.

— **Cursor Scratch**, 2026-10-07
