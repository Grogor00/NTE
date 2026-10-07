# Round R04 — Cursor Scratch VERDICT

**Programme:** Planck-comparable recovery (V+C+A+L) · **No-f** · **No Core patches**  
**Date:** 2026-10-07 · **Lane:** Cursor Scratch (constructive, blind to Jammer R04)  
**Paths:** P07, P08  
**κ₀ = 3/√(4π) ≈ 0.846284** (deposited; not fitted)

**Hard reminder:** κ₀/(1−κ₀) ≈ **5.5055 ∈ [5.23, 5.53]** already satisfies **V** numerically. Success still requires **C** (cold + collisionless + co-located at CMB epoch). Number without character = FAIL. R01–R03 killed P01–P06 on that kill (and A).

**Honest priors (used, not re-litigated):** N1 light bilkinetic closed as CDM (hot / ΔN_eff). CDM inventory **D3** on heavy RH (leptogenesis instability) and **D4** overall. BFT deep-read **B0∧B3**: sterile-particle DM rejected; odd-μ production not deposited; M₁∼5.4×10⁹ GeV is leptogenesis parent, not DM. P02: HR healthy dS branches DE-like; A-PASS for HR class does not buy V+C.

---

## P07 — Heavy shared Majorana \(M\gg T_{\mathrm{CMB}}\) structural abundance

### Mechanism proposed (concrete)

**Target:** keep the N1 bilkinetic *action class* (shared CPN-even Majorana on both metrics) but take the **heavy** seesaw branch so the relic is non-relativistic by \(z\sim 1100\):

\[
\begin{aligned}
S_\nu
&= \tfrac{i}{2}\!\int\!\sqrt{-g^+}\,\bar\nu\,i\not D_+\nu
+ \tfrac{i}{2}\!\int\!\sqrt{-g^-}\,\bar\nu\,i\not D_-\nu
- \tfrac{M}{2}\!\int\!\big(\sqrt{-g^+}+\sqrt{-g^-}\big)\,\bar\nu\nu,
\end{aligned}
\]

with \(M\gg T_{\mathrm{CMB}}\) structural from Companion-10/13 seesaw scales (not sized to Ω). Under CPN \(g^+=g^-\),

\[
G_{\mu\nu}=8\pi\big(T_b+T_\nu\big)_{\mu\nu},\qquad
r_{\mathrm{bg}}\equiv\rho_\nu/\rho_b.
\]

**Hope:** cold + collisionless from \(M\gg T\); co-location from shared bilateral field / adiabatic tracing; abundance from deposited production (Bogoliubov / thickness / heat-kernel), **no-f**.

**Constructive attempts this round:**

| Attempt | Structure | Result |
|---|---|---|
| P07-M1 | Identify cold sector with deposited heavy RH modes \(M_1,M_2,M_R\) (C10) | **Seesaw/leptogenesis conflict (honest).** \(M_1\approx 5.4\times10^9\,\mathrm{GeV}\) is the **leptogenesis parent** — must decay / washout to generate η (C10 §5; inventory **D3**). Unstable ⇒ **not** a stable CDM relic. |
| P07-M2 | Stabilise one RH column with BFT-style Z₂ while leaving others for leptogenesis | **Role mismatch + new content.** Deposit Z₂: unresolved ν is **even** (κ bridge); resolved fermions odd. BFT flips one RH to make a *stable particle DM* — deposit §IX **rejects** sterile-of-definite-mass DM (B0). Freezing M₁ **removes** a leptogenesis channel. Fourth heavy sterile threatens three-mode κ₀ logic if it participates in Hopf; if not, pure new particle ontology. **A FAIL** as deposited completion. |
| P07-M3 | Heavy *shared* light-sector Majorana (same field as N1 bridge) with \(M\gg T_{\mathrm{CMB}}\) | **Scale conflict.** Deposit seesaw: light active masses ≪ eV; heavy RH separate. Raising the *shared bridge* mass to \(M\gg T_{\mathrm{CMB}}\) either (i) destroys light-ν phenomenology / N1 F-NU role, or (ii) silently means “RH sterile” → collapses to P07-M1/M2. |
| P07-M4 | Structural abundance from Janus Bogoliubov / CPT vacuum → \(n_{\mathrm{dm}}/s\) | **Not deposited** (BFT E3). Deposit Bogoliubov is geometric CP \(\lvert\delta_J\rvert=\pi/2\) → **leptogenesis existence**, not Ω_c. Equating BFT \(m_{\mathrm{dm}}\sim 4.8\times10^8\,\mathrm{GeV}\) with NTE \(M_1\) is ~11× near-miss, **wrong job**, Ω_DM-first fit (**NF**). |
| P07-M5 | Size \(M\) or yield \(Y\) so \(\rho_M/\rho_b\in[5.23,5.53]\) | Instant **no-f** kill. |

**Honest landing:** Heavy-\(M\) buys *kinematic* coldness only if a **stable** relic exists. Deposit heavy modes are **leptogenesis parents (D3)**; stabilising them breaks leptogenesis and/or CPN/Z₂ ontology (B0∧B3). No deposited structural \(\rho_M/\rho_b\). Prior medium C-risk materialises as **stability + abundance**, not as “maybe warm.”

### \(r_{\mathrm{bg}}\) estimate

| Bookkeeping | \(r_{\mathrm{bg}}\) | In band? |
|---|---|---|
| Light N1 (closed) | hot / ΔN_eff ratio | Wrong character |
| Decaying \(M_1\) after leptogenesis | **0** as CDM (unstable) | No |
| BFT-style stable sterile (not deposited) | would require fit / new axiom | Forbidden |
| Shared bridge with structural \(M\gg T\) + deposited yield | **undefined on deposit** | No |
| **P07 owned estimate** | **none legitimate in band** | — |

### Gates

| Gate | Verdict | Evidence |
|---|---|---|
| **V** | **FAIL** | No deposit-derived \(\rho_M/\rho_b\in[5.23,5.53]\). Seesaw scales fix leptogenesis / light masses, not Ω_c/Ω_b. Pinning yield or \(M\) into band = **f**. |
| **C** | **FAIL** | Cold+collisionless requires **stability**. Deposited heavy RH **fail stability** (leptogenesis). Shared bilateral field helps co-location *if* stable — irrelevant when the candidate decays. Light-fourth-mode escape = C7 falsifier. |
| **A** | **FAIL** | Bare bilkinetic spinor is ghost-free (N1 class), but the **CDM package** needs a stability completion (Z₂ / extra mode / non-decay) that is **not deposited** and conflicts with C10 leptogenesis + §IX sterile rejection. Fail-closed for programme A on this path’s claim. |

**P07 V:** FAIL  
**P07 C:** FAIL  
**P07 A:** FAIL  
**P07 path:** **FAIL**

---

## P08 — Single-metric matter + HR massive graviton as dark component

### Mechanism proposed (concrete)

**Target:** break CPN-equal twin-baryon bookkeeping so “extra” is **not** mirror baryons; put Standard Model matter only on \(g^+\), leave \(f=g^-\) matter-empty, and identify Planck CDM with the **healthy massive spin-2** sector of Hassan–Rosen:

\[
\begin{aligned}
S
&= \frac{M_g^2}{2}\!\int\!\sqrt{-g}\,R(g)
+ \frac{M_f^2}{2}\!\int\!\sqrt{-f}\,R(f)
+ m^2 M_{\mathrm{eff}}^2\!\int\!\sqrt{-g}\,V(g^{-1}f;\beta_n) \\
&\quad + S_m[g,\psi^+]
\quad\big(\text{no }S_m[f]\big).
\end{aligned}
\]

**Structural β_n / m:** same no-f discipline as P02 — healthy branch relations, equal Planck masses; **m** not fitted to 5.38.  
**V hope:** graviton / DM branch ratio \(\Omega_{\mathrm{MG}}/\Omega_b\in[5.23,5.53]\).  
**C hope:** massive graviton cold + collisionless; co-location via gravitational clustering with baryons.  
**A hope:** HR ghost-free on healthy branch; \(S_m[f]=0\) justified by orientation-local SM ontology.

**Constructive attempts this round:**

| Attempt | Structure | Result |
|---|---|---|
| P08-A1 | Justify \(S_m[f]=0\) via “orientation-local SM” (Part 1 null-time locality slogan) | **CPN bookkeeping break (honest).** Deposit locality: photons/gluons (null-time) are orientation-local and off the κ bridge. It does **not** deposit “no twin baryons / empty \(f\)-matter.” Maximal CPN readings used throughout P2/Hκ/inventory assume **equal twin matter**. Setting \(S_m[f]=0\) is a **preferred-orientation matter asymmetry** — either new axiom or silent CPN break. Brief’s high C-risk is real and is also an **A** risk. |
| P08-A2 | Keep HR healthy *infinite / dS* branch; read \(\rho_V\) as CDM | Same P02 kill: \(\rho_V\) is **DE-like / modified-gravity**, not cold clustering dust at \(z\sim 1100\). |
| P08-A3 | Finite / “matter” branch: propagating massive graviton as CDM | Character *can* be cold+collisionless in spin-2 DM literature — **but** NTE deposit supplies **no** production lemma, no structural \(m\) from κ₀/Hopf/fibre, no \(\Omega_{\mathrm{MG}}/\Omega_b\). Sizing \(m\) or β_n into band = **f**. |
| P08-A4 | Identify \(\Omega_{\mathrm{MG}}/\Omega_b\) with κ₀/(1−κ₀) | **Number-without-character + smuggling.** κ₀ does not appear in \(V(g^{-1}f;\beta_n)\) (P02). Amplifier decimal ≠ graviton abundance. |
| P08-A5 | Twin empty ⇒ no hot-twin C kill, so C PASS by absence | Evades *mirror-baryon* HT only by **breaking** the CPN premise that generated HT. Programme still needs a positive cold co-located component with structural abundance — graviton packet absent → **C FAIL** fail-closed, not PASS-by-deletion. |

**Honest landing:** P08 correctly diagnoses that CPN-equal twin matter forces baryon-like character — then “solves” it by **deleting twin matter**, which is not deposited. HR can host a healthy massive spin-2, but without structural \(m\)→Ω and without a CMB-character proof on an NTE-identified branch, V and C stay fail-closed. Prior high CPN-break risk materialises.

### \(r_{\mathrm{bg}}\) estimate

| Bookkeeping | \(r_{\mathrm{bg}}\) | In band? |
|---|---|---|
| Twin matter (CPN, P02) | ∼1 | No (and path deletes this) |
| \(\rho_V/\rho_b\) on healthy dS branch | DE-like; epoch-dependent | Not structural CDM band |
| Massive-graviton DM yield | **undefined on deposit** | Would need **f** on \(m\)/β_n |
| κ₀/(1−κ₀) assigned to MG | 5.5055 | In band **only as smuggled amplifier** — not owned |
| **P08 owned estimate** | **none legitimate in band** | — |

### Gates

| Gate | Verdict | Evidence |
|---|---|---|
| **V** | **FAIL** | No structural \(\Omega_{\mathrm{MG}}/\Omega_b\in[5.23,5.53]\). Healthy HR parameters do not force the Planck band without fitting \(m\) or β_n. |
| **C** | **FAIL** | dS-branch extra is DE-like (not CDM). Matter-branch graviton DM lacks deposited production + CMB character packet. \(S_m[f]=0\) removes twin HT only by CPN break — does not prove BL-3 PASS for the graviton sector. |
| **A** | **FAIL** | HR class remains ghost-free on healthy branches (P02 residue), but **NTE identification with \(S_m[f]=0\)** is an undeposited CPN matter asymmetry. Programme A requires legitimate completion *in the NTE ontology*; asymmetry-as-dial / asymmetry-without-lemma → **A FAIL**. |

**P08 V:** FAIL  
**P08 C:** FAIL  
**P08 A:** FAIL  
**P08 path:** **FAIL**

---

## Round gates (Scratch lane)

```
P07 V: FAIL
P07 C: FAIL
P07 A: FAIL

P08 V: FAIL
P08 C: FAIL
P08 A: FAIL
```

**Overall V:** FAIL  
**Overall C:** FAIL (hard gate; heavy-M unstable / undeposited; graviton packet empty; CPN break not a character PASS)  
**Overall A:** FAIL  
**Overall L:** PENDING (dual-lane; Scratch does not self-PASS L)

**Round landing:** **both active paths FAIL.**  
- **P07** dies on the deposited **seesaw/leptogenesis conflict**: heavy RH cannot be stable CDM without destroying η-generation or importing BFT sterile ontology the deposit already refused. No structural abundance.  
- **P08** dies on the deposited **CPN twin-matter bookkeeping**: single-metric matter is not an earned rewrite; HR still supplies no no-f in-band CDM ratio.  

Do not promote κ≈5.50. Do not re-open light N1 as CDM.

Queue already holds **P09–P12**. Scratch does **not** re-propose those four.

---

## New structural paths proposed (≤2; no dials)

### P13 — Derive twin temperature ratio \(x=T'/T\) from deposited Janus / N-thickness (no dial); character-first cold-conjugate test

- **Why new vs P04/P07/P08:** P04 attacked co-location with adopted \(\ell_c\). P07/P08 delete or reassign the twin. Mirror-matter literature needs \(x\lesssim 0.3\) for conjugate-as-CDM; NTE under maximal CPN has been read as **\(x=1\)** (thermal contact via shared ν). **P13** asks whether a **structural** \(x\neq 1\) is forced by deposited Janus thickness / Bogoliubov / bilateral cooling — **or FAIL** (no dialing \(x\) into the band that makes conjugate CDM).
- **V demand:** after forced \(x\), structural \(\rho_{\mathrm{cold}}/\rho_b\in[5.23,5.53]\) **or FAIL** (no κ-amplifier smuggling).
- **C hope:** cold+collisionless+co-located only if derived \(x\) actually kills twin acoustics/Silk at CMB; equal-\(T\) HT remains the default kill.
- **A hope:** temperature ratio from deposited bilateral thermodynamics / shared-ν decoupling — no hand \(S_{\mathrm{cons}}\), no preferred-orientation matter deletion (contrast P08). Fail-closed if \(x=1\) is forced.

### P14 — HR finite / matter-branch massive graviton CDM with structural \(m\) from deposited fibre or \(M_R\) (bilateral matter kept)

- **Why new vs P02/P08:** P02 used healthy dS/β_n and got DE-like extras under **CPN-equal matter**. P08 deleted \(S_m[f]\). **P14** keeps \(S_m[g]+S_m[f]\) (no CPN matter break) and demands a **matter-branch** spin-2 CDM packet whose mass scale is **identified** with a deposited scale (Hopf fibre radius, \(M_R\sim 10^{14}\,\mathrm{GeV}\), or heat-kernel mass gap) — then compute \(\Omega_{\mathrm{MG}}/\Omega_b\) **or FAIL**. Twin baryons remain *not* the CDM (bridge/twin stress separate); dark component is the graviton.
- **V demand:** explicit structural ratio in [5.23, 5.53] from that identification **or FAIL** (no fitting \(m\)).
- **C hope:** prove \(w\simeq 0\), collisionless, co-located at \(z\sim 1100\) on that branch — not DE unloading.
- **A hope:** standard HR healthy finite-branch action + deposited scale ID only; no \(S_m[f]=0\). Fail-closed if scale ID is slogan or branch is DE-only.

---

## Sign-off

P07 and P08 do **not** survive V+C+A. Affirm inventory **D3** (heavy RH unstable) and BFT **B0∧B3** (sterile DM refused; no odd-μ yield). Affirm that **CPN twin bookkeeping** cannot be escaped by undeposited single-metric matter without failing A. Recommend Main keep **P09–P12**, add **P13, P14** (P13 first if C-triage on \(x\); else P14 if graviton lane still wanted without CPN break).

— **Cursor Scratch**, 2026-10-07
