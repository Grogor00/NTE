# Round R01 — Cursor Jammer VERDICT (adversarial, blind)

**Programme:** CPN relation + gravity completion · **Date:** 2026-10-07  
**Lane:** Jammer · **Primary track:** G · **Secondary:** P  
**Constraints:** No Core patches. No κ=Ω_DM restore. Did **not** read `Scratch_VERDICT.md`.

**Lands: P3 and G2**

---

## Evidence base

- Ran `python Working/cpn_gravity_loop/run_all.py` → mechanical hints `P2` / `G2` (success of run ≠ success of NTE).
- Results: `Working/cpn_gravity_loop/results/GRAVITY_COMPLETION_RESULTS.md`, `CPN_MAP_RESULTS.md`.
- Deposit anchors (this pass):
  - **Part 2 §IX:** bilateral action = bi-EH + shared neutrino + Hopf–Y₀₀ bridge + self-consistency constraint; Hassan–Rosen-class nonlinear completion named **open refinement**.
  - **Part 3 open bimetric line:** “establish the full ghost-free bimetric completion (Hassan–Rosen-class) of the two-orientation gravity.”
  - **Companion_05 §5–6:** deposited CPN formula is antipodal `(z₁,z₂)→(−z₁,−z₂)=e^{iπ}`; CPT=`Θ∘CPN` with Θ named not constructed; unresolved ν “sources curvature on **both** sides.”
  - **Companion_07:** bilateral / cross-thickness ontology of unresolved ν (κ spine); completion of bilateral action marked open in trailer.
- Literature already encoded in probes / O1 W-2: arXiv:1408.0487 (doubly coupled matter → BD generally revives); HR healthy when matter on one metric / potential-only second couple; elliptic dS and BFT **not** NTE instances.

---

## Track G (primary) — **G2**

### Attack on H0–H3 / N0

| ID | Press |
|---|---|
| **H0** | Ghost-free. Matter on **one** metric. Does **not** host Z₂-even ν stress in both Einstein equations. Healthy literature; **content gap** vs deposit (Companion_05 §6 both-sides sourcing). |
| **H1** | 1408 §IV safe subclass: second-metric dependence **potential-only**. Not kinetic shared-ν backbone. |
| **H2** | Only naive HR home for **two kinetic terms**. 1408.0487 §§III–IV: BD generally revives. `C_kinetic_double_ok=False`. Closest to deposited intent; **blocked**. |
| **N0** | Deposited bilateral action (Part 2 §IX). Ontology `full` by construction; `ghost_status=generally_ghost`; hand `S_cons`; constraint structure incomplete off g⁺≠g⁻. Fits ontology; **fails health**. |
| **H3** | Research sketch: HR on two orientation-metrics + **ν single-kinetic** + κ₀ from overlap. `ghost_status=unknown`; not constructed; not deposited. **Ontology cost = drop second kinetic** (and with it the both-EOM kinetic reading of Companion_05/07). |
| **E0 / B0 / S0** | Wrong ontology class (one metric / CPT image / delete dark sector). Already excluded by W-2 / settled Part 1 §VI. |

### Is there a ghost-free path that keeps shared ν kinetic in **both** Einstein equations?

**No.** Probe summary: `Healthy ∩ full ontology = (none)`; `shared_nu_kinetic_blocked_by_1408 = True`.

- Keeping dual kinetic → H2/N0 class → generally ghost (1408).
- Keeping literature health (H0/H1) → drop both-EOM kinetic shared ν.
- Inventing a healthy dual-kinetic theory without 1408-class exceptions is **not allowed** here (no literature support).

### Fork landing

**G2.** The only path that even *aims* at a ghost-free two-orientation completion under HR discipline is **H3-style**: drop the second kinetic term for shared ν. That is an **ontology change** relative to the deposited both-sides stress-energy reading — not a free completion of N0.

Cost named: **lose dual-kinetic / both-EOM kinetic sourcing of the unresolved neutrino**; replace with single-kinetic + HR potential (and still derive that potential from NTE — unfinished). Part 3 OPEN restated sharper: HR exists; **NTE’s shared-ν kinetic package is the obstruction**, not the absence of a two-metric theory class.

Not **G1** (no HR-class completion keeps shared ν kinetic in both EOMs). Not **G3** as a claim that *no* completion concept exists — H3 is the named costly corridor. Not **G4**: blockers are determinate (1408 + W-2 content list).

---

## Track P (secondary) — **P3**

### Attack on M5 `full_work=True`

Mechanical hint `P2` rests entirely on **M5**. Adversarial read: that flag is **smuggled**.

1. **Not deposited.** `R_deposited=False`. Deposited ∩ full-work = **(none)** → **P1 unavailable**.
2. **Circular scoring.** Probe sets `full_work=True` “by construction of flags” / “Would score full work **IF defined**” (`cpn_map_probes.py` M5). That is a research wishlist, not a finding that a map does deposit-work.
3. **`R_su2r=True` is a package claim.** Deposit assigns SU(2)_R to the mirror via CPN+parity prose (Part 2 / Companion_05 apparatus), but M5 never writes an operator that *underwrites* that assignment. M1 correctly fails `R_su2r`; M5 awards it without a formula.
4. **What *is* deposited fails work.** M0 = Companion_05 antipodal / fibre half-turn — O2 **C-3**: fails baryon sort, ¬gauge, SU(2)_R, M_A=M_B, acts-on-N. M6’s Θ is named in Companion_05 §5 and **not constructed** — does not rescue M0.
5. Endorsing M5 as P2 would treat an undeposited composite as if it closed the CPN defect — **Core-patch-shaped**, forbidden by programme register.

### Partial survivors (defect stands)

| ID | What survives | What fails |
|---|---|---|
| **M1** | N-sort, ¬gauge, M_A=M_B, acts on N | SU(2)_R; not a deposited operator |
| **M2** | Physical C; deposited piece | No N-sorting alone |
| **M3** | (−1)^ℓ parity rule | Not baryon sorting |
| **M4** | Pin⁻ topology (“why CPN?”) | Not ψ₊↦… field map; no SU(2)_R underwrite |
| **M6** | Names Θ∘CPN gap | Θ formula missing |

### Fork landing

**P3.** No candidate **honestly** scores full deposit-work. M5’s `full_work` is probe optimism, not a deposited map. Partial survivors: **M1, M2, M3, M4, M6**. CPN relation defect stands (O2 C-3 unrepaired).

Not **P1** (nothing deposited ∩ full-work). Not **P2** (refusing to launder M5). Not **P4** (requirements do not contradict each other; the deposit formula simply fails them).

---

## Cross-check numbers (no Scratch read)

- Gravity: healthy two-metric IDs `H0`,`H1`; N0 `generally_ghost`; 1408 blocks kinetic shared ν.
- CPN: M0 fails work; sole mechanical full-work ID `M5` (disputed); deposited full-work empty.

---

## Standing refusals

- No Core patches proposed.
- No κ=Ω_DM restore.
- No invention of a healthy dual-kinetic bigravity without literature warrant.

— **Cursor Jammer**, 2026-10-07
