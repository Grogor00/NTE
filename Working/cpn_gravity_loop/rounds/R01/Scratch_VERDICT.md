# Round R01 — Cursor Scratch verdict

**Lands: P3 and G2**

**Register:** research programme. No Core patches. No κ=Ω_DM restore.

---

## Probe run

- Ran `python Working/cpn_gravity_loop/run_all.py` from repo root (2026-10-07).
- Mechanical fork hints: **P2**, **G2**.
- Scratch **rejects** the mechanical P2 endorsement; endorses **P3**. Gravity cross-check endorses mechanical **G2**.

---

## Track P — CPN relation (primary)

### M0 / O2 C-3 confirmed

Deposited formula fails deposit-work:

| Flag | M0 | Deposit cite |
|---|---|---|
| `R_deposited` | True | Companion_05 §5: CPN “is” antipodal `(z₁,z₂)→(−z₁,−z₂)=e^{iπ}` |
| `R_baryon_sort` | False | Part 2 §8.4: matter→+N / antimatter→−N — fibre half-turn does not sort on N-thickness |
| `R_acts_on_N` | False | Part 1 §2.1.2 / §VI: N-thickness is the e-fold extent; Hopf fibre phase is orthogonal |
| `R_not_gauge` | False | Companion_07 §2: resolved fermion fibre phase is unobservable; half-turn is that class |
| `R_su2r` / `R_MA_MB` | False | Part 2 §8.5–8.6 / C5 §6 apparatus need more than S³ fibre rotation |

**C-3 stands.** The deposited z→−z map does not do the CPN work the same §5 paragraph *names* (simultaneous C, P, and e-fold-direction reversal).

Not **P4**: the *work requirements* are mutually consistent; the defect is an identification failure (formula ≠ named work), not a contradiction among requirements.

### Stress-test of candidates — why not P1/P2

**M1 (N-reversal).** Probe: baryon-sort + acts-on-N + M_A=M_B + ¬gauge; fails `R_su2r`; not deposited as operator. Honest: Part 2 §8.4 *prose* commits matter/antimatter to ±N, but no formula `(x,N)→(x,−N)` is deposited. Necessary piece; insufficient alone.

**M2 (C alone).** Deposited locus via Companion_07 (charge conjugation / antipodal exchange on resolved matter). Without N-sorting does not place antimatter on −N. Necessary piece; insufficient.

**M3 ((−1)^ℓ).** Deposited (C5 §5 parity rule). Mode coupling, not baryon sorting.

**M4 (Pin⁻).** Deposited topology (Part 1 §VI: Pin⁻ twist of N-thickness “produces baryogenesis”). Answers “why CPN?” topologically; **not** an explicit field map `ψ₊→…`. Probe correctly withholds `R_su2r` and `R_MA_MB`.

**M5 (research composite C∘P∘N).** Mechanical full-work ID — **flag fiat only.** Probe note: “Would score full work IF defined.” Scratch stress-test:

1. `R_su2r=True` is a package claim. Part 2 §8.5–8.6 asserts that “CPN combined with parity assigns SU(2)_R to the mirror,” but that is prose about an undeposited operator, not a verification that the M5 sketch underwrites the assignment.
2. Geometric content `ψ₊(x,N) ↦ (CP ψ)₋(P·x, −N)` plus Pin⁻ sector choice is a **specification target**, not a scored map. Awarding `full_work=True` before the operator (and sector choice) is written is optimism.
3. Companion_05 §5 already *names* simultaneous C+P+N in prose while depositing only fibre half-turn — M5 restates that naming gap; it does not close it.

Therefore M5 does **not** honestly score full deposit-work. Mechanical **P2** is rejected. Not **P1** (no deposited ∩ full-work).

**M6 (Θ∘CPN).** C5 §5 names `CPT = Θ∘CPN` with Θ unreconciled as a formula. Named gap; does not rescue M0.

**M7 (RP³ quotient).** Fails free-symmetry / sorting; conflicts with §8.4. Rejected.

### P3 landing

**No candidate honestly scores full deposit-work.** O2 C-3 defect stands.

**Partial survivors named (research stack, not Core):**

| ID | Role |
|---|---|
| **M1** | N-orientation sort (the missing act-on-N piece relative to M0) |
| **M2** | Physical C on resolved matter |
| **M4** | Pin⁻ topological reason CPN exists |
| **M3** | Deposited P-piece (mode selection only) |
| **M5** | *Named construction target* for a later round — composite that would need definition before any P2 claim |
| **M6** | Named Θ gap inside C5 |

Constructive next object (still research, still not Core): define M5’s operator and sector choice so `R_su2r` can be re-scored against Part 2 §8.5–8.6 without package fiat. That is advancement *toward* P2, not a P2 landing now.

---

## Track G — Gravity completion (secondary cross-check)

Mechanical hint **G2** — Scratch agrees on numbers only (adversarial depth is Jammer’s).

| Fact from probe | Read |
|---|---|
| Healthy ∩ full ontology | empty |
| Healthy two-metric | H0, H1 (matter on one metric / potential-only second couple) |
| N0 (deposited bilateral action) | `generally_ghost`; `C_kinetic_double_ok=False`; hand `S_cons` |
| 1408 blocks kinetic shared ν | True (H2 class) |
| H3 research path | drops dual-kinetic ν; ontology cost = G2 |

**G2:** A ghost-free HR-class completion compatible with deposited bilateral *ontology shape* appears available only if shared ν loses the second kinetic term (single-kinetic / potential-only subclass), at the cost of departing from the deposited dual-kinetic shared-ν backbone (Part 2 §IX; O1 W-2). Not G1 (no healthy full-ontology hit). Not G3 yet — H3 remains an open research path with that named cost. Blockers restated: 1408 kinetic double-couple; unfinished off-diagonal constraint structure on N0.

Part 1 §VI ontology (one manifold, two orientation-metrics, single bilateral action) retained as settled; completion status remains open under that cost.

---

## Standing constraints (explicit)

- **No Core patches.**
- **No κ=Ω_DM restore** (κ=5.50 withdrawn; κ₀ retained; Planck538 exhausted — outside this programme).

---

— **Cursor Scratch** · Round R01 · 2026-10-07
