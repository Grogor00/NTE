# P-Born P-B1 — complex structure from CPN / gauge birth v0.1 (§17.5.13)

**Stream:** Cursor scaffold → Jammer / Paper 2 extension  
**Date:** 2026-05-23  
**Status:** **Attack route mapped** — Kähler on $\mathbb{CP}^1$ forced **given** U(1) fibre; full theorem from gauge birth **open**  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-B1

---

## §1. Mission

Reduce Paper 2's **input** "complex Hilbert space + global U(1) phase" to NTE **gauge-birth geometry**:

> U(1) fibre activation at $N_{\rm lock}$ (Companion 6) $\Rightarrow$ projective state space $\mathbb{CP}^{n-1}$ with **canonical Kähler (Fubini–Study) metric** $\Rightarrow$ Born weights as geometric overlap.

**Target register (§17.5.13):** complex structure as **theorem from gauge birth**, not free input. **Honest v0.1:** fibre activation + Hopf quotient **forces FS structure on $\mathbb{CP}^1$**; promotion to full $\mathbb{C}^n$ from S³ alone remains **partial** (Cayley-Dickson route).

---

## §2. Corpus chain (closed layers)

| Step | Content | Register |
|------|---------|----------|
| **S0** | Pre-$N_{\rm lock}$: Dirac modes on $S^3$, **no U(1) gauge** | Companion 6 §2 |
| **S1** | At gauge birth: U(1)$_Y$ activates → global phase **unobservable** | Companion 6 §3.2 |
| **S2** | Hopf fibration $S^3 \to S^2$ as $S^3/U(1)$ quotient | Paper 2 Facts 2–3 |
| **S3** | Physical states = $\mathbb{CP}^1 \cong S^2$ (spin-1/2 sector) | **Closed given S1–S2** |
| **S4** | Fubini–Study metric on $\mathbb{CP}^1$ is **unique** Kähler metric invariant under U(1) | Standard; see §3 |
| **S5** | FS distance $\Rightarrow$ $|\langle\phi|\psi\rangle|^2$ overlap | Paper 2 Step 1 **given** complex coords |

**Gap (P-B1 open):** S0→S1 does not yet **derive** $\mathbb{C}$ from $\mathbb{R}$ spinors without importing complex amplitudes.

---

## §3. Kähler / Fubini–Study (spin-1/2 sector)

**State:** $[\psi] \in \mathbb{CP}^1$, representative $(z_1,z_2) \in \mathbb{C}^2$, $|z|^2=1$.

**U(1) gauge:** $(z_1,z_2) \sim (e^{i\xi}z_1, e^{i\xi}z_2)$.

**Fubini–Study metric (unique Kähler on $\mathbb{CP}^1$):**

$$ds^2_{\rm FS} = \frac{4\,(dz_1 d\bar z_1 + dz_2 d\bar z_2) - (z_1 d\bar z_1 + z_2 d\bar z_2)(\bar z_1 dz_1 + \bar z_2 dz_2)}{|z|^4}$$

**Overlap probability (geometric):**

$$P(\phi \to \psi) = |\langle\phi|\psi\rangle|^2 = \cos^2(\theta/2)$$

for spin-1/2 angle $\theta$ on Bloch sphere — Paper 2 + Companion 6 §4.

**P-B1 partial closure:** Once S1–S2 hold, **Kähler structure is not an extra input** — it is the unique U(1)-invariant Kähler metric on the projective space.

---

## §4. Attack route to full complex structure (open)

| Route | Mechanism | Owner | Status |
|-------|-----------|-------|--------|
| **R1** | Cayley-Dickson $\mathbb{O}\to\mathbb{H}\to\mathbb{C}$ at gauge birth (§VIII.7) selects **complex** line inside quaternionic spinor data | Jammer | **Partial** — narrative in Companion 6 footnote |
| **R2** | CPN / Janus orientation picks **complex structure** on $T S^3$ compatible with Hopf map | Jammer | Open |
| **R3** | Spectral triple $A_F=\mathbb{O}\oplus\mathbb{O}$ → forced $\mathbb{C}$ representation on observable sector | Scratch | Open (P0.10 kin) |
| **R4** | Two-layer gauge argument (Companion 6 §3.3) closes **when** rule applies; does not close **$\mathbb{C}$ from $\mathbb{R}$** alone | **Closed at mechanism** | ✓ |

**Discipline:** keep §17.5.13 label — **reformulation not derivation from less** until R1–R3 closes.

---

## §5. Relation to P-B2 / P-B3

| Item | Dependency |
|------|------------|
| **P-B2** (bilinearity without $|ψ|^2$ input) | Hopf quadratic coords + $f(r)=r$ — see `P_Born_P2_Hopf_Bilinearity_v0_1`; full overlap needs P-B1 Route C |
| **P-B3** (Zurek scope) | Independent — complementary mechanism (decoherence vs gauge-birth activation) |

---

## §6. Falsifiers

1. Gauge birth without U(1) fibre → Born rule should not activate (pre-$N_{\rm lock}$) — **consistent with corpus**  
2. Alternative Kähler metric on $\mathbb{CP}^1$ breaking U(1) — **excluded** by uniqueness  
3. Claim "complex structure derived" while still importing $\mathbb{C}^2$ coordinates — **scope violation**

---

## §7. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| P-B1a | This attack-route note | **Done v0.1** |
| P-B1b | Formal lemma: U(1) quotient $\Rightarrow$ FS Kähler | Jammer |
| P-B1c | Cayley-Dickson $\Rightarrow$ $\mathbb{C}$ on spinor sector | Jammer / §VIII.7 |

---

## §8. Cross-references

- Companion 2 v2, Companion 6 v2; §17.5.13, §20.5  
- Part 2 §VIII.7 (Cayley-Dickson); Part 1 §2.1.3 (pre-temporal)

— Cursor P-Born P-B1 v0.1, 2026-05-23.
